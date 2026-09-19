# === MODULE_BUILD ===
# id: ucns_lifted_displacement_candidate
#   module_name: lifted_displacement
#   module_kind: candidate
#   summary: lifted ordered-concatenation displacement; the exact integer channels are summed before any residue reduction so the NativeMobiusState transforms exactly under the modular-orbit action
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, LiftedDisplacementError, LiftedDisplacementRecord, build_lifted_displacement, replay_lifted_displacement
#   internal_surface: exact-integer channel coercion, single native-mobius advancement, visible residue recording, covering witness
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_lifted_displacement
#   rollout: corrected candidate after the per-channel-reduction candidate failed the modular-orbit permutation control at the lifted frame level
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_visible_displacement_candidate, directed_carrier_floor
#   since: 2026-09-19
#   unresolved: selection follows the full control surface; the continuum lift-selection law remains hmmm
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: lifted_displacement_sums_before_reduction
#   given: three exact integer channels
#   then: the total turn is the exact sum over 157 and the mobius state advances once, preserving the wrap on the lift
#   class: correctness
#   since: 2026-09-19
#
# id: lifted_displacement_preserves_visible_positions
#   given: three exact integer channels
#   then: each recorded visible residue equals the channel value modulo 157
#   class: correctness
#   since: 2026-09-19
#
# id: lifted_displacement_is_modular_orbit_equivariant
#   given: a modular-orbit action x -> a*x mod 157 applied to the channels
#   then: the acted NativeMobiusState equals the state reached by advancing a times the original exact sum over 157
#   class: correctness
#   since: 2026-09-19
#
# id: lifted_displacement_fails_closed
#   given: malformed channels, non-bijective covering, or a malformed receipt
#   then: construction or replay raises LiftedDisplacementError
#   class: safety
#   since: 2026-09-19
# === END CONTRACTS ===

"""Lifted ordered-concatenation displacement.

The per-channel-reduction candidate failed the preregistered modular-orbit
permutation control because reducing each channel before summing
misattributes the wrap at the lifted frame level. This corrected candidate
sums the exact integer channels first and advances the NativeMobiusState
once by that exact sum over 157. Visible positions remain the channel
values modulo 157.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from typing import Any

from .direct_mobius import DirectMobiusError, native_mobius_state
from .modular_orbit import build_modular_orbit_geometry
from .gonal_boundary_trace import build_circle_wave_mode_trace
from .visible_displacement import VisibleDisplacementError

SCHEMA = "ucns.lifted-displacement-candidate"
VERSION = "0.1.0"
_MODULUS = 157
_ALL_POSITIONS = tuple(range(_MODULUS))


class LiftedDisplacementError(ValueError):
    """Raised when the lifted displacement candidate fails closed."""


def _coerce_channel(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise LiftedDisplacementError(f"{name} must be an exact integer")
    return value


def _coerce_covering_degree(covering_degree: int | None) -> int | None:
    if covering_degree is None:
        return None
    if isinstance(covering_degree, bool) or not isinstance(covering_degree, int):
        raise LiftedDisplacementError("covering_degree must be a positive integer or None")
    if covering_degree <= 0:
        raise LiftedDisplacementError("covering_degree must be a positive integer")
    return covering_degree


def _build_covering_witness(covering_degree: int) -> tuple[int, int]:
    multiplier = covering_degree % _MODULUS
    if multiplier == 0:
        raise LiftedDisplacementError(
            "covering degree congruent to 0 mod 157 is not bijective on the carrier"
        )
    build_modular_orbit_geometry(
        modulus=_MODULUS,
        multiplier=multiplier,
        positions=_ALL_POSITIONS,
    )
    build_circle_wave_mode_trace(
        modulus=_MODULUS,
        harmonic=1,
        positions=_ALL_POSITIONS,
    )
    return covering_degree, multiplier


@dataclass(frozen=True)
class LiftedDisplacementRecord:
    schema: str
    version: str
    ordinal: int
    semantic: int
    context: int
    total_turn: Fraction
    phase_turns: Fraction
    frame: str
    covering_degree: int | None
    covering_multiplier: int | None
    receipt_sha256: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "version": self.version,
            "ordinal": self.ordinal,
            "semantic": self.semantic,
            "context": self.context,
            "visible_residues": {
                "ordinal": self.ordinal % _MODULUS,
                "semantic": self.semantic % _MODULUS,
                "context": self.context % _MODULUS,
            },
            "total_turn": f"{self.total_turn.numerator}/{self.total_turn.denominator}",
            "mobius": {
                "phase_turns": f"{self.phase_turns.numerator}/{self.phase_turns.denominator}",
                "frame": self.frame,
            },
            "covering_degree": self.covering_degree,
            "covering_multiplier": self.covering_multiplier,
            "receipt_sha256": self.receipt_sha256,
        }

    def canonical_bytes(self) -> bytes:
        payload = self.as_dict()
        payload.pop("receipt_sha256", None)
        return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def receipt_bytes(self) -> bytes:
        return json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")


def build_lifted_displacement(
    ordinal: int,
    semantic: int,
    context: int,
    *,
    covering_degree: int | None = None,
) -> LiftedDisplacementRecord:
    """Build one lifted ordered-concatenation displacement."""

    o = _coerce_channel("ordinal", ordinal)
    s = _coerce_channel("semantic", semantic)
    c = _coerce_channel("context", context)
    resolved_covering = _coerce_covering_degree(covering_degree)

    total_turn = Fraction(o + s + c, _MODULUS)
    try:
        mobius = native_mobius_state().advance(total_turn)
    except DirectMobiusError as exc:
        raise LiftedDisplacementError(str(exc)) from exc

    if resolved_covering is None:
        covering_multiplier: int | None = None
    else:
        _, covering_multiplier = _build_covering_witness(resolved_covering)

    receipt = sha256()
    receipt.update(
        json.dumps(
            {
                "schema": SCHEMA,
                "version": VERSION,
                "ordinal": o,
                "semantic": s,
                "context": c,
                "total_turn": f"{total_turn.numerator}/{total_turn.denominator}",
                "mobius": {
                    "phase_turns": f"{mobius.phase_turns.numerator}/{mobius.phase_turns.denominator}",
                    "frame": mobius.frame.value,
                },
                "covering_degree": resolved_covering,
                "covering_multiplier": covering_multiplier,
            },
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    )

    return LiftedDisplacementRecord(
        schema=SCHEMA,
        version=VERSION,
        ordinal=o,
        semantic=s,
        context=c,
        total_turn=total_turn,
        phase_turns=mobius.phase_turns,
        frame=mobius.frame.value,
        covering_degree=resolved_covering,
        covering_multiplier=covering_multiplier,
        receipt_sha256=receipt.hexdigest(),
    )


def replay_lifted_displacement(data: bytes) -> LiftedDisplacementRecord:
    """Rebuild a lifted displacement from receipt bytes and verify byte-for-byte."""

    if not isinstance(data, bytes):
        raise LiftedDisplacementError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise LiftedDisplacementError("receipt is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise LiftedDisplacementError("receipt root must be an object")
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise LiftedDisplacementError("receipt schema or version mismatch")
    record = build_lifted_displacement(
        obj["ordinal"],
        obj["semantic"],
        obj["context"],
        covering_degree=obj.get("covering_degree"),
    )
    if record.receipt_sha256 != obj.get("receipt_sha256"):
        raise LiftedDisplacementError("receipt digest does not match replayed displacement")
    if record.receipt_bytes() != data:
        raise LiftedDisplacementError("receipt does not replay byte-identically")
    return record


__all__ = [
    "SCHEMA",
    "VERSION",
    "LiftedDisplacementError",
    "LiftedDisplacementRecord",
    "build_lifted_displacement",
    "replay_lifted_displacement",
]
