# === MODULE_BUILD ===
# id: ucns_visible_displacement_candidate
#   module_name: visible_displacement
#   module_kind: candidate
#   summary: exact visible-circle displacement candidate composing Public Gonol positions, modular orbit geometry, circle-wave covering witnesses, and the native framed Mobius root loop
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, VisibleDisplacementError, VisibleDisplacementRecord, build_visible_displacement, replay_visible_displacement
#   internal_surface: canonical residue validation, ordered turn concatenation, receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable exact records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_visible_displacement
#   rollout: executable candidate displacement law inside the preregistered admissible law class; candidate standing, not UCNS canon
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_public_gonol_geometry, ucns_modular_orbit_geometry, ucns_gonal_boundary_trace, ucns_native_mobius_geometry
#   since: 2026-09-15
#   unresolved: the exact UCNS composition law for the three evidence residue channels; the law selecting one continuum lift from d ≡ a (mod 157)
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: visible_displacement_channel_turns_are_exact
#   given: three integer evidence residues and the 157-position carrier
#   then: each channel contributes exactly residue/157 visible turns as a Fraction
#   class: correctness
#   since: 2026-09-15
#
# id: visible_displacement_zero_channels_are_structural_null
#   given: all three residue channels are zero
#   then: the total displacement is exactly zero turns with the positive native Mobius frame and a deterministic receipt
#   class: correctness
#   since: 2026-09-15
#
# id: visible_displacement_preserves_native_mobius_law
#   given: any valid residue triple
#   then: the total displacement advances a NativeMobiusState by exact turns, so one full visible turn reverses the frame and two restore it
#   class: correctness
#   requires: native_mobius_one_turn_reverses_frame
#   since: 2026-09-15
#
# id: visible_displacement_covering_degree_is_explicit
#   given: a caller-declared continuum covering degree
#   then: the degree is recorded and verified congruent to the modular multiplier modulo 157 through a circle-wave covering witness
#   class: correctness
#   since: 2026-09-15
#
# id: visible_displacement_fails_closed_on_non_bijective_covering
#   given: a covering degree congruent to 0 modulo 157
#   then: construction raises VisibleDisplacementError rather than building a non-bijective covering witness
#   class: safety
#   since: 2026-09-15
#
# id: visible_displacement_fails_closed_on_invalid_input
#   given: non-integer residue channels or a malformed receipt
#   then: construction or replay raises VisibleDisplacementError rather than inventing a correspondence
#   class: safety
#   since: 2026-09-15
#
# id: visible_displacement_replay_is_byte_identical
#   given: a canonical receipt produced by the builder
#   then: replaying the receipt bytes rebuilds the identical record byte-for-byte
#   class: correctness
#   since: 2026-09-15
#
# id: visible_displacement_replay_detects_tamper
#   given: a canonical receipt with any byte altered
#   then: replay raises VisibleDisplacementError
#   class: safety
#   since: 2026-09-15
#
# id: visible_displacement_residues_wrap_on_the_carrier
#   given: negative or large integer residue channels
#   then: each residue is canonicalized modulo 157 without floating-point arithmetic
#   class: correctness
#   since: 2026-09-15
#
# id: visible_displacement_remains_candidate
#   given: an exact executable displacement exists
#   then: the ordered concatenation composition and the lift selection remain candidates; execution alone is not ratification
#   class: doctrine
#   since: 2026-09-15
# === END CONTRACTS ===

"""Exact visible-circle displacement candidate.

The candidate consumes three declared integer evidence residue channels::

    ordinal, semantic, context

Each channel contributes its own exact visible turn ``residue / 157`` on the
Public Gonol carrier. The three turns are combined by the circle group law
(ordered concatenation on the native framed Möbius root loop), so the total
displacement is exact rational arithmetic only:

    total = (ordinal + semantic + context) / 157 turns

One full visible turn reverses the local Möbius frame and two full visible
turns restore the complete state. A caller may additionally declare a
continuum covering degree ``d``; the candidate records ``d`` and witnesses
``d % 157 == a`` through the established circle-wave covering pullback.

The ordered concatenation composition and the continuum lift selection are
candidates, not ratified UCNS law.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
from hashlib import sha256
from typing import Any

from .direct_mobius import (
    DirectMobiusError,
    NativeMobiusFrame,
    NativeMobiusState,
    native_mobius_state,
)
from .gonal_boundary_trace import (
    build_circle_wave_mode_trace,
    pullback_circle_wave_trace,
)
from .modular_orbit import build_modular_orbit_geometry
from .public_gonol import PUBLIC_GONOL_157

SCHEMA = "ucns.visible-displacement-candidate"
VERSION = "0.1.0"

_MODULUS = len(PUBLIC_GONOL_157)
_ALL_POSITIONS = tuple(range(_MODULUS))


class VisibleDisplacementError(ValueError):
    """Raised when the candidate fails closed on malformed input."""


def _coerce_residue(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VisibleDisplacementError(f"{name} must be an exact integer")
    return value % _MODULUS


def _coerce_covering_degree(covering_degree: int | None) -> int | None:
    if covering_degree is None:
        return None
    if isinstance(covering_degree, bool) or not isinstance(covering_degree, int):
        raise VisibleDisplacementError("covering_degree must be a positive integer or None")
    if covering_degree <= 0:
        raise VisibleDisplacementError("covering_degree must be a positive integer")
    return covering_degree


@dataclass(frozen=True)
class VisibleDisplacementRecord:
    """One exact candidate displacement with receipt and replay fields."""

    schema: str
    version: str
    ordinal: int
    semantic: int
    context: int
    ordinal_turn: Fraction
    semantic_turn: Fraction
    context_turn: Fraction
    total_turn: Fraction
    mobius: NativeMobiusState
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
            "turns": {
                "ordinal": f"{self.ordinal_turn.numerator}/{self.ordinal_turn.denominator}",
                "semantic": f"{self.semantic_turn.numerator}/{self.semantic_turn.denominator}",
                "context": f"{self.context_turn.numerator}/{self.context_turn.denominator}",
                "total": f"{self.total_turn.numerator}/{self.total_turn.denominator}",
            },
            "mobius": {
                "phase_turns": f"{self.mobius.phase_turns.numerator}/{self.mobius.phase_turns.denominator}",
                "frame": self.mobius.frame.value,
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


def _build_covering_witness(covering_degree: int) -> tuple[int, None]:
    """Witness ``covering_degree % 157 == multiplier`` via the circle-wave pullback.

    Returns ``(covering_degree, multiplier)``. Fails closed when the finite
    action is not bijective on the full 157-position carrier.
    """

    multiplier = covering_degree % _MODULUS
    if multiplier == 0:
        raise VisibleDisplacementError(
            "covering degree congruent to 0 mod 157 is not bijective on the carrier"
        )
    geometry = build_modular_orbit_geometry(
        modulus=_MODULUS,
        multiplier=multiplier,
        positions=_ALL_POSITIONS,
    )
    trace = build_circle_wave_mode_trace(
        modulus=_MODULUS,
        harmonic=1,
        positions=_ALL_POSITIONS,
    )
    pullback_circle_wave_trace(trace, geometry, covering_degree)
    return covering_degree, multiplier


def build_visible_displacement(
    ordinal: int,
    semantic: int,
    context: int,
    *,
    covering_degree: int | None = None,
) -> VisibleDisplacementRecord:
    """Build one exact candidate displacement on the visible Public Gonol circle."""

    ordinal_residue = _coerce_residue("ordinal", ordinal)
    semantic_residue = _coerce_residue("semantic", semantic)
    context_residue = _coerce_residue("context", context)
    resolved_covering = _coerce_covering_degree(covering_degree)

    ordinal_turn = Fraction(ordinal_residue, _MODULUS)
    semantic_turn = Fraction(semantic_residue, _MODULUS)
    context_turn = Fraction(context_residue, _MODULUS)

    try:
        mobius = (
            native_mobius_state()
            .advance(ordinal_turn)
            .advance(semantic_turn)
            .advance(context_turn)
        )
    except DirectMobiusError as exc:
        raise VisibleDisplacementError(str(exc)) from exc

    total_turn = ordinal_turn + semantic_turn + context_turn

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
                "ordinal": ordinal_residue,
                "semantic": semantic_residue,
                "context": context_residue,
                "turns": {
                    "ordinal": f"{ordinal_turn.numerator}/{ordinal_turn.denominator}",
                    "semantic": f"{semantic_turn.numerator}/{semantic_turn.denominator}",
                    "context": f"{context_turn.numerator}/{context_turn.denominator}",
                    "total": f"{total_turn.numerator}/{total_turn.denominator}",
                },
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

    return VisibleDisplacementRecord(
        schema=SCHEMA,
        version=VERSION,
        ordinal=ordinal_residue,
        semantic=semantic_residue,
        context=context_residue,
        ordinal_turn=ordinal_turn,
        semantic_turn=semantic_turn,
        context_turn=context_turn,
        total_turn=total_turn,
        mobius=mobius,
        covering_degree=resolved_covering,
        covering_multiplier=covering_multiplier,
        receipt_sha256=receipt.hexdigest(),
    )


def replay_visible_displacement(data: bytes) -> VisibleDisplacementRecord:
    """Rebuild a displacement from its canonical receipt bytes and verify it byte-for-byte."""

    if not isinstance(data, bytes):
        raise VisibleDisplacementError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise VisibleDisplacementError("receipt is not valid canonical JSON") from exc

    if not isinstance(obj, dict):
        raise VisibleDisplacementError("receipt root must be an object")
    if obj.get("schema") != SCHEMA:
        raise VisibleDisplacementError(f"receipt schema must be {SCHEMA}")
    if obj.get("version") != VERSION:
        raise VisibleDisplacementError(f"receipt version must be {VERSION}")

    record = build_visible_displacement(
        obj["ordinal"],
        obj["semantic"],
        obj["context"],
        covering_degree=obj.get("covering_degree"),
    )
    if record.receipt_sha256 != obj.get("receipt_sha256"):
        raise VisibleDisplacementError("receipt digest does not match replayed construction")
    if record.receipt_bytes() != data:
        raise VisibleDisplacementError("receipt does not replay byte-identically")
    return record


__all__ = [
    "SCHEMA",
    "VERSION",
    "VisibleDisplacementError",
    "VisibleDisplacementRecord",
    "build_visible_displacement",
    "replay_visible_displacement",
]
