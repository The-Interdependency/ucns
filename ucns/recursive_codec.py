"""
ucns.recursive_codec
==============================
Recursive encoder/decoder between Python values and UCNSObject.

Bridges the embedding side (where data enters and leaves) and the
algebraic side (where ``multiply``, ``left_quotient``, and the
witness-matrix machinery operate).

Design choices (frozen for v0.1)
--------------------------------

**Encoding shape (option (c) — type from shape).**  Container kind is
recovered at decode time from the number of leading sentinel cells:

    1 leading sentinel   →  bytes leaf
    2 leading sentinels  →  list/tuple
    3 leading sentinels  →  dict

A sentinel cell has angle 0, ``payload = None``, and ``face = 0``.
Content cells have ``face = 1``.

The leading sentinel is *required* even for non-empty leaves because
``UCNSObject.normalize()`` shifts the first angle to 0; without an
anchor cell, a leaf's first byte value would be lost.

**Face bit semantics — presence flag.**  ``F_plus[k] = 1`` means "this
cell carries user-supplied content"; ``F_plus[k] = 0`` means "padding,
sentinel, or default".  The decoder strips face-0 cells when
reconstructing.  Domain-specific encoders may reinterpret the bit
*only when the base presence/default meaning is vacuous in their
context* (e.g. transcript encoders may use it for modified-vs-original
since transcripts have no concept of "default").

**Order — preserved as presented.**  Dicts encode in insertion order;
lists in index order.  No canonical sort.  Dicts that differ only in
key order encode to *different* UCNSObjects — by design.

**Round-trip.**  ``recursive_decode(recursive_encode(v)) == v`` for:

    - ``bytes`` (round-trips exactly)
    - ``list[T]`` and ``tuple[T]`` (round-trip as ``list``)
    - dictionaries whose keys are drawn from the supported key set
      below (insertion order preserved; keys round-trip with exact
      type identity)

**Dictionary keys (versioned tag layer, codex-handoff/06).**  Newly
encoded dictionaries wrap every key in a versioned, type-tagged capsule
so keys round-trip with type identity and never collapse silently.
The supported key types are exactly:

    bytes, str, int, bool, finite float,
    tuple of supported key types (recursively)

Exact-type dispatch is used (``bool`` is never encoded as ``int``), so
``{1: b"int", "1": b"str", b"1": b"bytes"}`` round-trips as three
distinct, correctly typed entries.  ``bytearray``, lists, dicts, sets,
custom objects, non-finite floats, and tuples containing unsupported
elements raise :class:`EncodingError` at encode time.  (Python itself
identifies ``True`` and ``1`` as the same dictionary key; the codec
cannot and does not claim to preserve two entries that cannot coexist
in the input.)

The decoder validates the capsule version and tag strictly, rebuilds
tuple keys as tuples, verifies decoded keys are hashable, and raises
:class:`EncodingError` on duplicate decoded keys instead of silently
overwriting.  Legacy dictionaries (encoded before the tag layer)
still decode with the historical bytes-coercion behavior; the legacy
path also rejects unhashable keys and duplicate collapse.

**Leaf coercion (values).**  All non-bytes leaf VALUES round-trip as
``bytes``:

    - ``str``     → utf-8 encoded; round-trip recovers ``bytes``
    - ``int``     → ``str(int).encode('utf-8')``; round-trip recovers ``bytes``
    - ``float``   → ``repr(float).encode('utf-8')``; round-trip recovers ``bytes``
    - ``bool``    → ``b"1"`` / ``b"0"``

Callers who need typed VALUE round-trip should wrap with their own tag
layer; the typed capsule applies to dictionary keys only.

**Distinguishability.**  Empty leaf, empty list, empty dict encode to
1, 2, 3 cells respectively — all distinct.  No collisions.

**Depth cap.**  No cap is enforced at the encoder.  The natural depth
of the input determines the depth of the output.  Out-of-domain
rejection (depth ≥ 3, or outside the depth-2 oracle class) happens at
the *retrieval store* layer, not here.

References
----------
- Items 2 + 4 of the depth-2-walk roadmap (May 2026 conversation).
- ``canonical.py`` for ``UCNSObject`` and the ``n_dec % n_min == 0``
  constraint.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_codec
#   module_name: recursive_codec
#   module_kind: engine
#   summary: Recursive encoder/decoder between Python values (bytes/list/tuple/dict and coercible leaves) and UCNSObject, with type recovered from leading-sentinel count.
#   owner: Erin Spencer
#   public_surface: recursive_encode, recursive_decode, EncodingError
#   internal_surface: _byte_to_angle, _angle_to_byte, _safe_n_dec, _make_sentinel_cells, _encode_bytes, _encode_list, _encode_dict, _count_leading_sentinels, _key_capsule, _decode_key_capsule
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_recursive_codec
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

import math
import re
from fractions import Fraction
from typing import Any, List, Optional, Tuple

from .canonical import UCNSObject

__all__ = ["recursive_encode", "recursive_decode", "EncodingError"]


# ---------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------


class EncodingError(TypeError):
    """Raised when a value cannot be encoded into a UCNSObject."""


# ---------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------


# Byte values map to angles via ``Fraction(byte, 64)``.  After Fraction
# reduction, the denominator divides 128, so ``n_dec = 128`` always
# satisfies the constructor's ``n_dec % n_min == 0`` constraint.
_BYTE_N_DEC = 128

_LEAF_SENTINELS = 1
_LIST_SENTINELS = 2
_DICT_SENTINELS = 3

# Versioned dictionary-key capsule (codex-handoff/06).  A key is
# encoded as the 3-list [marker, tag, payload]; the marker names the
# capsule version, the tag names the exact Python type, the payload is
# the tag-specific representation.
_KEY_MARKER_PREFIX = b"__ucns_key_v"
_KEY_MARKER = b"__ucns_key_v1__"
_KEY_TAG_BYTES = b"bytes"
_KEY_TAG_STR = b"str"
_KEY_TAG_INT = b"int"
_KEY_TAG_BOOL = b"bool"
_KEY_TAG_FLOAT = b"float"
_KEY_TAG_TUPLE = b"tuple"

_INT_TEXT = re.compile(rb"^-?[0-9]+$")


def _key_capsule(key: Any) -> list:
    """Wrap a supported dictionary key in its versioned typed capsule.

    Exact-type dispatch: ``bool`` is checked before ``int`` so it is
    never encoded as an integer.  Unsupported or non-finite keys raise
    :class:`EncodingError` at encode time.
    """
    if type(key) is bool:
        return [_KEY_MARKER, _KEY_TAG_BOOL, b"true" if key else b"false"]
    if type(key) is int:
        return [_KEY_MARKER, _KEY_TAG_INT, str(key).encode("ascii")]
    if type(key) is float:
        if not math.isfinite(key):
            raise EncodingError(
                f"Cannot encode non-finite float dictionary key: {key!r}"
            )
        return [_KEY_MARKER, _KEY_TAG_FLOAT, repr(key).encode("ascii")]
    if type(key) is str:
        return [_KEY_MARKER, _KEY_TAG_STR, key.encode("utf-8")]
    if type(key) is bytes:
        return [_KEY_MARKER, _KEY_TAG_BYTES, key]
    if type(key) is tuple:
        return [_KEY_MARKER, _KEY_TAG_TUPLE, [_key_capsule(el) for el in key]]
    raise EncodingError(
        f"Unsupported dictionary key type {type(key).__name__!r}; "
        "supported: bytes, str, int, bool, finite float, and tuples thereof"
    )


def _decode_key_capsule(raw: Any) -> Any:
    """Strictly parse a decoded key capsule back to the original key.

    ``raw`` is the plain-value decode of an encoded key.  New-format
    capsules are validated field by field; a list that looks like a
    capsule of an unknown version is rejected; anything else falls back
    to the legacy bytes-coercion path (which must still produce a
    hashable key).
    """
    if isinstance(raw, list):
        if len(raw) == 3 and raw[0] == _KEY_MARKER:
            tag, payload = raw[1], raw[2]
            if tag == _KEY_TAG_BYTES:
                if not isinstance(payload, bytes):
                    raise EncodingError("Malformed bytes key capsule")
                return payload
            if tag == _KEY_TAG_STR:
                if not isinstance(payload, bytes):
                    raise EncodingError("Malformed str key capsule")
                try:
                    return payload.decode("utf-8")
                except UnicodeDecodeError:
                    raise EncodingError("Invalid utf-8 in str key capsule")
            if tag == _KEY_TAG_INT:
                if not isinstance(payload, bytes) or not _INT_TEXT.match(payload):
                    raise EncodingError(
                        f"Invalid integer text in key capsule: {payload!r}"
                    )
                return int(payload)
            if tag == _KEY_TAG_BOOL:
                if payload == b"true":
                    return True
                if payload == b"false":
                    return False
                raise EncodingError(
                    f"Invalid boolean text in key capsule: {payload!r}"
                )
            if tag == _KEY_TAG_FLOAT:
                if not isinstance(payload, bytes):
                    raise EncodingError("Malformed float key capsule")
                try:
                    value = float(payload.decode("ascii"))
                except (UnicodeDecodeError, ValueError):
                    raise EncodingError(
                        f"Invalid float text in key capsule: {payload!r}"
                    )
                if not math.isfinite(value):
                    raise EncodingError(
                        f"Non-finite float in key capsule: {payload!r}"
                    )
                return value
            if tag == _KEY_TAG_TUPLE:
                if not isinstance(payload, list):
                    raise EncodingError("Malformed tuple key capsule")
                return tuple(_decode_key_capsule(el) for el in payload)
            raise EncodingError(f"Unknown key capsule tag: {tag!r}")
        if (
            raw
            and isinstance(raw[0], bytes)
            and raw[0].startswith(_KEY_MARKER_PREFIX)
        ):
            raise EncodingError(
                f"Unknown key capsule version or shape: {raw[0]!r}"
            )
    # Legacy path: the key is the plain decoded value (historically a
    # bytes coercion).  It must still be usable as a dictionary key.
    try:
        hash(raw)
    except TypeError:
        raise EncodingError(
            f"Legacy dictionary key decodes to unhashable {type(raw).__name__}"
        )
    return raw


# ---------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------


def _byte_to_angle(b: int) -> Fraction:
    if not 0 <= b <= 255:
        raise EncodingError(f"byte value out of range: {b}")
    return Fraction(b, 64)


def _angle_to_byte(a: Fraction) -> int:
    val = a * 64
    if val.denominator != 1:
        raise EncodingError(
            f"angle {a} does not encode an integer byte (denom={val.denominator})"
        )
    b = int(val.numerator)
    if not 0 <= b <= 255:
        raise EncodingError(f"recovered byte out of range: {b}")
    return b


def _safe_n_dec(n_min_upper_bound: int) -> int:
    return max(n_min_upper_bound, 1)


def _make_sentinel_cells(count: int) -> Tuple[
    List[Tuple[Fraction, Optional[UCNSObject]]], List[int]
]:
    """All sentinel cells share angle 0, payload None, face 0.
    Distinguished from content cells by face bit; distinguished from
    each other only by position in A_plus."""
    return ([(Fraction(0), None)] * count, [0] * count)


# ---------------------------------------------------------------------
# Encode
# ---------------------------------------------------------------------


def _encode_bytes(b: bytes) -> UCNSObject:
    sentinels_a, sentinels_f = _make_sentinel_cells(_LEAF_SENTINELS)
    a_plus = list(sentinels_a) + [(_byte_to_angle(byte), None) for byte in b]
    f_plus = list(sentinels_f) + [1] * len(b)
    return UCNSObject(_BYTE_N_DEC, _BYTE_N_DEC, a_plus, f_plus)


def _encode_list(xs: list) -> UCNSObject:
    n = len(xs)
    total = _LIST_SENTINELS + n
    n_dec = _safe_n_dec(total)
    sentinels_a, sentinels_f = _make_sentinel_cells(_LIST_SENTINELS)
    a_plus = list(sentinels_a)
    f_plus = list(sentinels_f)
    for k, item in enumerate(xs):
        angle = Fraction(4 * (_LIST_SENTINELS + k), total)
        a_plus.append((angle, recursive_encode(item)))
        f_plus.append(1)
    return UCNSObject(n_dec, n_dec, a_plus, f_plus)


def _encode_dict(d: dict) -> UCNSObject:
    n = len(d)
    total = _DICT_SENTINELS + 2 * n
    n_dec = _safe_n_dec(total)
    sentinels_a, sentinels_f = _make_sentinel_cells(_DICT_SENTINELS)
    a_plus = list(sentinels_a)
    f_plus = list(sentinels_f)
    for i, (key, value) in enumerate(d.items()):
        angle_k = Fraction(4 * (_DICT_SENTINELS + 2 * i), total)
        angle_v = Fraction(4 * (_DICT_SENTINELS + 2 * i + 1), total)
        a_plus.append((angle_k, recursive_encode(_key_capsule(key))))
        a_plus.append((angle_v, recursive_encode(value)))
        f_plus.extend([1, 1])
    return UCNSObject(n_dec, n_dec, a_plus, f_plus)


def recursive_encode(value: Any) -> UCNSObject:
    """Encode a Python value as a ``UCNSObject``.

    Supported types: ``bytes``, ``bytearray``, ``str``, ``int``,
    ``float``, ``bool``, ``list``, ``tuple``, ``dict``.  Anything else
    raises :class:`EncodingError`.

    Round-trip behavior is documented in the module docstring.
    """
    if isinstance(value, (bytes, bytearray)):
        return _encode_bytes(bytes(value))
    if isinstance(value, str):
        return _encode_bytes(value.encode("utf-8"))
    if isinstance(value, bool):
        return _encode_bytes(b"1" if value else b"0")
    if isinstance(value, int):
        return _encode_bytes(str(value).encode("utf-8"))
    if isinstance(value, float):
        return _encode_bytes(repr(value).encode("utf-8"))
    if isinstance(value, (list, tuple)):
        return _encode_list(list(value))
    if isinstance(value, dict):
        return _encode_dict(value)
    raise EncodingError(f"Cannot encode type {type(value).__name__}")


# ---------------------------------------------------------------------
# Decode
# ---------------------------------------------------------------------


def _count_leading_sentinels(obj: UCNSObject) -> int:
    count = 0
    for f in obj.F_plus:
        if f == 0:
            count += 1
        else:
            break
    return count


def recursive_decode(obj: Optional[UCNSObject]) -> Any:
    """Inverse of :func:`recursive_encode`.

    Reconstructs a Python value from a ``UCNSObject``.  Type is
    inferred from the leading-sentinel count (option (c) of the design).
    """
    if obj is None:
        return b""
    L = len(obj.A_plus)
    if L == 0:
        return b""

    sentinel_count = _count_leading_sentinels(obj)
    content = obj.A_plus[sentinel_count:]

    if sentinel_count == _LEAF_SENTINELS:
        out = bytearray()
        for angle, _payload in content:
            out.append(_angle_to_byte(angle))
        return bytes(out)

    if sentinel_count == _LIST_SENTINELS:
        return [recursive_decode(payload) for _angle, payload in content]

    if sentinel_count == _DICT_SENTINELS:
        if len(content) % 2 != 0:
            raise EncodingError(
                f"Dict-shaped object has odd content length {len(content)}"
            )
        result: dict = {}
        for i in range(0, len(content), 2):
            k = _decode_key_capsule(recursive_decode(content[i][1]))
            v = recursive_decode(content[i + 1][1])
            if k in result:
                raise EncodingError(
                    f"Duplicate decoded dictionary key {k!r}; refusing to "
                    "overwrite an earlier entry"
                )
            result[k] = v
        return result

    raise EncodingError(
        f"Unexpected leading sentinel count: {sentinel_count} "
        f"(expected 1, 2, or 3)"
    )
