# === MODULE_BUILD ===
# id: ucns_axis_circle_position_candidate
#   module_name: axis_circle
#   module_kind: candidate
#   summary: binds one axis of an explicitly identified finite origin to its exact normalized-circle position so object identity survives label changes
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, AxisCircleError, AxisCirclePosition, build_axis_circle_position, replay_axis_circle_position
#   internal_surface: exact ordinal-to-turn mapping, origin receipt validation, deterministic identity and replay receipt
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_axis_circle
#   rollout: candidate geometric identity attachment; labels and language semantics remain external
#   rollback: remove this module, facade exports, tests, documentation, and candidate canon entry
#   requires: ucns_modular_orbit_geometry
#   since: 2026-10-05
#   unresolved: whether every UCNS object class ultimately uses this finite-origin circle identity
# === END MODULE_BUILD ===
#
# === CONTRACTS ===
# id: axis_circle_position_is_exact
#   given: a finite origin with N axes and one zero-based axis ordinal r
#   then: the axis occupies exactly r/N normalized turns using Fraction
#   class: correctness
#   since: 2026-10-05
#
# id: axis_circle_identity_is_label_independent
#   given: the same origin identity, axis count, and axis ordinal under any external labels
#   then: the geometric identity digest is unchanged because labels are not admitted inputs
#   class: doctrine
#   since: 2026-10-05
#
# id: axis_circle_origin_change_changes_identity
#   given: the same ordinal on a different origin receipt or a different finite axis carrier
#   then: the geometric identity digest changes
#   class: correctness
#   since: 2026-10-05
#
# id: axis_circle_fails_closed
#   given: malformed origin identity, nonpositive axis count, out-of-range ordinal, or tampered replay
#   then: construction raises AxisCircleError rather than coercing or inventing a position
#   class: safety
#   since: 2026-10-05
#
# id: axis_circle_work_graph_binds_enforced_skill_authority
#   given: the polyglot axis-circle work graph coordinates UCNS with external consumers
#   then: its skill-lib participant matches the exact vendored skill authority enforced by this checkout and the graph digest recomputes
#   class: provenance_contract
#   since: 2026-10-05
# === END CONTRACTS ===

"""Exact candidate identity for an axis as a position on its finite origin circle.

For a declared finite origin with N ordered axes, zero-based axis ordinal r
occupies exactly r/N normalized turns. The origin is bound by an external
SHA-256 receipt produced by the owning construction. That receipt identifies
which ordered origin is being used; UCNS supplies only the geometry.

Labels, words, language tags, dictionary senses, and other semantic names are
intentionally absent. A consumer may attach any number of external labels to
the resulting identity_sha256 without changing the UCNS object.

Canonical JSON integer rendering and replay are implemented without Python's
process-wide integer-to-decimal digit limit, so finite exact inputs do not gain
an accidental geometry bound from host interpreter configuration.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
import re

SCHEMA = "ucns.axis-circle-position-candidate"
VERSION = "0.1.0"
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class AxisCircleError(ValueError):
    """Raised when an axis-circle identity fails closed."""


def _int_decimal(value: int) -> str:
    """Render an integer without Python's process-wide int->str digit limit."""

    if isinstance(value, bool) or not isinstance(value, int):
        raise AxisCircleError("canonical integer must be an int")
    if value == 0:
        return "0"
    sign = "-" if value < 0 else ""
    value = abs(value)
    chunks: list[int] = []
    base = 1_000_000_000
    while value:
        value, chunk = divmod(value, base)
        chunks.append(chunk)
    head = str(chunks.pop())
    tail = "".join(f"{chunk:09d}" for chunk in reversed(chunks))
    return sign + head + tail


def _parse_decimal_integer(text: str) -> int:
    """Parse a JSON integer without Python's process-wide str->int digit limit."""

    if not isinstance(text, str) or not text:
        raise AxisCircleError("canonical JSON integer is malformed")
    sign = -1 if text.startswith("-") else 1
    digits = text[1:] if sign < 0 else text
    if not digits or not digits.isascii() or not digits.isdigit():
        raise AxisCircleError("canonical JSON integer is malformed")
    value = 0
    first = len(digits) % 9 or 9
    value = int(digits[:first])
    for offset in range(first, len(digits), 9):
        value = value * 1_000_000_000 + int(digits[offset:offset + 9])
    return sign * value


def _canonical_json(value: object) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return _int_decimal(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise AxisCircleError("canonical JSON object keys must be strings")
        return "{" + ",".join(
            json.dumps(key, ensure_ascii=False) + ":" + _canonical_json(value[key])
            for key in sorted(value)
        ) + "}"
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(_canonical_json(item) for item in value) + "]"
    raise AxisCircleError("axis-circle payload contains unsupported canonical JSON value")


def _canonical(payload: dict[str, object]) -> bytes:
    try:
        return _canonical_json(payload).encode("utf-8")
    except (ValueError, OverflowError, RecursionError) as exc:
        raise AxisCircleError("axis-circle payload cannot be rendered canonically") from exc


def _identity_payload(
    origin_sha256: str,
    axis_count: int,
    axis_ordinal: int,
) -> dict[str, object]:
    turn = Fraction(axis_ordinal, axis_count)
    return {
        "schema": SCHEMA,
        "version": VERSION,
        "origin_sha256": origin_sha256,
        "axis_count": axis_count,
        "axis_ordinal": axis_ordinal,
        "turn": {
            "numerator": turn.numerator,
            "denominator": turn.denominator,
        },
    }


@dataclass(frozen=True, slots=True)
class AxisCirclePosition:
    """One exact axis identity on one exact finite origin circle."""

    origin_sha256: str
    axis_count: int
    axis_ordinal: int
    turn: Fraction
    identity_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.origin_sha256, str) or not _SHA256_RE.fullmatch(self.origin_sha256):
            raise AxisCircleError("origin_sha256 must be a lowercase hexadecimal SHA-256")
        if isinstance(self.axis_count, bool) or not isinstance(self.axis_count, int) or self.axis_count <= 0:
            raise AxisCircleError("axis_count must be a positive integer")
        if isinstance(self.axis_ordinal, bool) or not isinstance(self.axis_ordinal, int):
            raise AxisCircleError("axis_ordinal must be an integer")
        if not 0 <= self.axis_ordinal < self.axis_count:
            raise AxisCircleError("axis_ordinal must be in [0, axis_count)")
        expected_turn = Fraction(self.axis_ordinal, self.axis_count)
        if not isinstance(self.turn, Fraction) or self.turn != expected_turn:
            raise AxisCircleError("turn must equal the exact canonical axis_ordinal/axis_count fraction")
        expected_identity = sha256(
            _canonical(_identity_payload(self.origin_sha256, self.axis_count, self.axis_ordinal))
        ).hexdigest()
        if self.identity_sha256 != expected_identity:
            raise AxisCircleError("identity_sha256 does not match the exact geometric identity")

    def as_dict(self) -> dict[str, object]:
        payload = _identity_payload(self.origin_sha256, self.axis_count, self.axis_ordinal)
        payload["identity_sha256"] = self.identity_sha256
        return payload

    def receipt_bytes(self) -> bytes:
        return _canonical(self.as_dict())


def build_axis_circle_position(
    *,
    origin_sha256: str,
    axis_count: int,
    axis_ordinal: int,
) -> AxisCirclePosition:
    """Bind one ordered axis to its exact normalized-circle position."""

    if not isinstance(origin_sha256, str) or not _SHA256_RE.fullmatch(origin_sha256):
        raise AxisCircleError("origin_sha256 must be a lowercase hexadecimal SHA-256")
    if isinstance(axis_count, bool) or not isinstance(axis_count, int) or axis_count <= 0:
        raise AxisCircleError("axis_count must be a positive integer")
    if isinstance(axis_ordinal, bool) or not isinstance(axis_ordinal, int):
        raise AxisCircleError("axis_ordinal must be an integer")
    if not 0 <= axis_ordinal < axis_count:
        raise AxisCircleError("axis_ordinal must be in [0, axis_count)")

    turn = Fraction(axis_ordinal, axis_count)
    identity = sha256(
        _canonical(_identity_payload(origin_sha256, axis_count, axis_ordinal))
    ).hexdigest()
    return AxisCirclePosition(
        origin_sha256=origin_sha256,
        axis_count=axis_count,
        axis_ordinal=axis_ordinal,
        turn=turn,
        identity_sha256=identity,
    )


def replay_axis_circle_position(data: bytes) -> AxisCirclePosition:
    """Reconstruct one identity and require byte-identical canonical replay."""

    if not isinstance(data, bytes):
        raise AxisCircleError("axis-circle receipt must be bytes")
    try:
        obj = json.loads(
            data.decode("utf-8"),
            parse_int=_parse_decimal_integer,
            parse_float=lambda _: (_ for _ in ()).throw(AxisCircleError("floating-point JSON is not canonical")),
            parse_constant=lambda _: (_ for _ in ()).throw(AxisCircleError("non-finite JSON is not canonical")),
        )
    except (UnicodeDecodeError, ValueError, RecursionError) as exc:
        # json.loads may raise ValueError for interpreter-enforced integer
        # digit limits or RecursionError for excessive nesting. Normalize
        # every parser failure to the documented fail-closed boundary.
        raise AxisCircleError("axis-circle receipt is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise AxisCircleError("axis-circle receipt root must be an object")
    expected_keys = {
        "schema",
        "version",
        "origin_sha256",
        "axis_count",
        "axis_ordinal",
        "turn",
        "identity_sha256",
    }
    if set(obj) != expected_keys:
        raise AxisCircleError("axis-circle receipt fields do not match the schema")
    if obj["schema"] != SCHEMA or obj["version"] != VERSION:
        raise AxisCircleError("axis-circle receipt schema or version mismatch")

    turn_obj = obj["turn"]
    if not isinstance(turn_obj, dict) or set(turn_obj) != {"numerator", "denominator"}:
        raise AxisCircleError("turn must be an exact numerator/denominator object")
    rebuilt = build_axis_circle_position(
        origin_sha256=obj["origin_sha256"],
        axis_count=obj["axis_count"],
        axis_ordinal=obj["axis_ordinal"],
    )
    if {
        "numerator": rebuilt.turn.numerator,
        "denominator": rebuilt.turn.denominator,
    } != turn_obj:
        raise AxisCircleError("turn does not match the reconstructed exact position")
    if rebuilt.identity_sha256 != obj["identity_sha256"]:
        raise AxisCircleError("identity digest does not match reconstruction")
    if rebuilt.receipt_bytes() != data:
        raise AxisCircleError("axis-circle receipt does not replay byte-identically")
    return rebuilt


__all__ = [
    "SCHEMA",
    "VERSION",
    "AxisCircleError",
    "AxisCirclePosition",
    "build_axis_circle_position",
    "replay_axis_circle_position",
]
