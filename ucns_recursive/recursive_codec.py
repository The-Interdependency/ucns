"""
ucns_recursive.recursive_codec
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
    - ``dict[Hashable, T]`` (insertion order preserved)

**Leaf coercion.**  All non-bytes leaves round-trip as ``bytes``:

    - ``str``     → utf-8 encoded; round-trip recovers ``bytes``
    - ``int``     → ``str(int).encode('utf-8')``; round-trip recovers ``bytes``
    - ``float``   → ``repr(float).encode('utf-8')``; round-trip recovers ``bytes``
    - ``bool``    → ``b"1"`` / ``b"0"``

Callers who need typed round-trip should wrap with their own tag layer.
This is honest about the v0.1 surface: the encoding stores bytes; type
recovery is the caller's job.

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
        a_plus.append((angle_k, recursive_encode(key)))
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
            k = recursive_decode(content[i][1])
            v = recursive_decode(content[i + 1][1])
            result[k] = v
        return result

    raise EncodingError(
        f"Unexpected leading sentinel count: {sentinel_count} "
        f"(expected 1, 2, or 3)"
    )
