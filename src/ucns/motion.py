# === MODULE_BUILD ===
# id: ucns_motion_candidate
#   module_name: motion
#   module_kind: candidate
#   summary: candidate gonol motion over a definition walk; each step advances a NativeMobiusState by the ordered-concatenation displacement candidate while radius and layer are recorded from the canonical radial map and deck translations
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, MotionError, MotionStepRecord, MotionRecord, build_motion, replay_motion
#   internal_surface: cumulative native-mobius advancement, per-step radius/layer, canonical receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_motion
#   rollout: executable candidate motion; inherits the unselected status of the ordered-concatenation displacement candidate
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_visible_displacement_candidate, directed_carrier_floor
#   since: 2026-09-19
#   unresolved: the consumed displacement candidate remains unselected; motion selection/ratification follows from displacement selection
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: motion_step_advances_native_mobius_state
#   given: one definition-walk step with three exact residues
#   then: the step advances a NativeMobiusState by the ordered-concatenation turn exactly
#   class: correctness
#   since: 2026-09-19
#
# id: motion_records_radius_and_layer_per_step
#   given: one definition-walk step
#   then: radius is the canonical radial map on the semantic breadth and layer is the context deck-translation count
#   class: correctness
#   since: 2026-09-19
#
# id: motion_inherits_unselected_displacement_status
#   given: the consumed displacement candidate
#   then: the motion record carries the candidate's unselected status and never claims selection
#   class: doctrine
#   since: 2026-09-19
#
# id: motion_fails_closed
#   given: malformed walk residues or a malformed receipt
#   then: construction or replay raises MotionError rather than inventing motion
#   class: safety
#   since: 2026-09-19
# === END CONTRACTS ===

"""Candidate gonol motion over a definition walk.

One walk step ``(ordinal, semantic, context)`` advances a cumulative
``NativeMobiusState`` by the ordered-concatenation displacement candidate.
Radius is the canonical radial map on the semantic breadth; layer is the
context deck-translation count. The consumed displacement candidate is
UNSELECTED, and this motion candidate inherits that status.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from math import isfinite
from typing import Any

from .carrier import radius_from_breadth
from .direct_mobius import NativeMobiusState, native_mobius_state
from .visible_displacement import VisibleDisplacementError, build_visible_displacement

SCHEMA = "ucns.motion-candidate"
VERSION = "0.1.0"
_MODULUS = 157
_DISPLACEMENT_CANDIDATE = "ordered-concatenation"
_DISPLACEMENT_CANDIDATE_STATUS = "unselected"


class MotionError(ValueError):
    """Raised when the motion candidate fails closed."""


@dataclass(frozen=True)
class MotionStepRecord:
    index: int
    ordinal: int
    semantic: int
    context: int
    turn: Fraction
    phase_after: Fraction
    frame_after: str
    radius: float
    layer: int

    def as_dict(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "ordinal": self.ordinal,
            "semantic": self.semantic,
            "context": self.context,
            "turn": f"{self.turn.numerator}/{self.turn.denominator}",
            "phase_after": f"{self.phase_after.numerator}/{self.phase_after.denominator}",
            "frame_after": self.frame_after,
            "radius": repr(self.radius),
            "layer": self.layer,
        }


@dataclass(frozen=True)
class MotionRecord:
    schema: str
    version: str
    displacement_candidate: str
    displacement_candidate_status: str
    steps: tuple[MotionStepRecord, ...]
    end_phase: Fraction
    end_frame: str
    end_radius: float
    end_layer: int
    total_turn: Fraction
    receipt_sha256: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "version": self.version,
            "displacement_candidate": self.displacement_candidate,
            "displacement_candidate_status": self.displacement_candidate_status,
            "steps": [step.as_dict() for step in self.steps],
            "end_phase": f"{self.end_phase.numerator}/{self.end_phase.denominator}",
            "end_frame": self.end_frame,
            "end_radius": repr(self.end_radius),
            "end_layer": self.end_layer,
            "total_turn": f"{self.total_turn.numerator}/{self.total_turn.denominator}",
            "receipt_sha256": self.receipt_sha256,
        }

    def canonical_bytes(self) -> bytes:
        payload = self.as_dict()
        payload.pop("receipt_sha256", None)
        return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def receipt_bytes(self) -> bytes:
        return json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")


def _coerce_residue(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise MotionError(f"{name} must be an exact integer")
    return value % _MODULUS


def build_motion(
    walk: tuple[tuple[int, int, int], ...],
) -> MotionRecord:
    """Build one candidate motion over a definition walk."""

    if not isinstance(walk, (tuple, list)) or len(walk) == 0:
        raise MotionError("walk must be a non-empty tuple of (ordinal, semantic, context)")
    state: NativeMobiusState = native_mobius_state()
    steps: list[MotionStepRecord] = []
    total_turn = Fraction(0)
    end_radius = 0.0
    end_layer = 0
    for index, triple in enumerate(walk):
        if not isinstance(triple, (tuple, list)) or len(triple) != 3:
            raise MotionError("each walk step must be an (ordinal, semantic, context) triple")
        ordinal = _coerce_residue("ordinal", triple[0])
        semantic = _coerce_residue("semantic", triple[1])
        context = _coerce_residue("context", triple[2])
        try:
            displacement = build_visible_displacement(ordinal, semantic, context)
        except VisibleDisplacementError as exc:
            raise MotionError(str(exc)) from exc
        turn = displacement.total_turn
        state = state.advance(turn)
        total_turn += turn
        breadth = float(semantic)
        if not isfinite(breadth) or breadth < 0.0:
            raise MotionError("semantic breadth must be finite and nonnegative")
        radius = radius_from_breadth(breadth)
        layer = context % 2
        steps.append(
            MotionStepRecord(
                index=index,
                ordinal=ordinal,
                semantic=semantic,
                context=context,
                turn=turn,
                phase_after=state.phase_turns,
                frame_after=state.frame.value,
                radius=radius,
                layer=layer,
            )
        )
        end_radius = radius
        end_layer = layer

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "displacement_candidate": _DISPLACEMENT_CANDIDATE,
        "displacement_candidate_status": _DISPLACEMENT_CANDIDATE_STATUS,
        "steps": [step.as_dict() for step in steps],
        "end_phase": f"{state.phase_turns.numerator}/{state.phase_turns.denominator}",
        "end_frame": state.frame.value,
        "end_radius": repr(end_radius),
        "end_layer": end_layer,
        "total_turn": f"{total_turn.numerator}/{total_turn.denominator}",
    }
    receipt = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    return MotionRecord(
        schema=SCHEMA,
        version=VERSION,
        displacement_candidate=_DISPLACEMENT_CANDIDATE,
        displacement_candidate_status=_DISPLACEMENT_CANDIDATE_STATUS,
        steps=tuple(steps),
        end_phase=state.phase_turns,
        end_frame=state.frame.value,
        end_radius=end_radius,
        end_layer=end_layer,
        total_turn=total_turn,
        receipt_sha256=receipt,
    )


def replay_motion(data: bytes) -> MotionRecord:
    """Rebuild the motion record and verify it byte-for-byte."""

    if not isinstance(data, bytes):
        raise MotionError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise MotionError("receipt is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise MotionError("receipt root must be an object")
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise MotionError("receipt schema or version mismatch")
    walk = tuple(
        (step["ordinal"], step["semantic"], step["context"])
        for step in obj["steps"]
    )
    record = build_motion(walk)
    if record.receipt_sha256 != obj.get("receipt_sha256"):
        raise MotionError("receipt digest does not match replayed motion")
    if record.receipt_bytes() != data:
        raise MotionError("receipt does not replay byte-identically")
    return record


__all__ = [
    "SCHEMA",
    "VERSION",
    "MotionError",
    "MotionStepRecord",
    "MotionRecord",
    "build_motion",
    "replay_motion",
]
