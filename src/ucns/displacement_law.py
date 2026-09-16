# === MODULE_BUILD ===
# id: ucns_displacement_law_candidates
#   module_name: displacement_law
#   module_kind: candidate
#   summary: enumerates the declared displacement-law candidates and records a composite candidate displacement that carries every candidate sub-result for comparison and falsification
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, DISPLACEMENT_LAW_CANDIDATES, DisplacementLawError, DisplacementRecord, build_displacement, replay_displacement
#   internal_surface: candidate registry, composite construction from established candidates, canonical receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_displacement_law
#   rollout: executable candidate displacement law with declared falsifiers; candidate standing, not UCNS canon
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_visible_displacement_candidate, ucns_placement_frame_candidate
#   since: 2026-09-15
#   unresolved: none of the enumerated candidates is ratified; falsification selects among them, not execution
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: displacement_law_enumerates_declared_candidates
#   given: the displacement-law candidate registry
#   then: every declared candidate carries its schema, summary, and candidate standing with no canon selection
#   class: doctrine
#   since: 2026-09-15
#
# id: displacement_law_records_every_candidate_subresult
#   given: one composite displacement construction
#   then: the ordered-concatenation angle candidate and the placement-frame angle candidate are both recorded exactly so falsification can compare them
#   class: correctness
#   since: 2026-09-15
#
# id: displacement_law_preserves_frame_components
#   given: the same three channels
#   then: radius is the canonical radial map on semantic breadth and layer is context deck translations
#   class: correctness
#   since: 2026-09-15
#
# id: displacement_law_covering_degree_is_explicit
#   given: a caller-declared continuum covering degree
#   then: it is recorded through the ordered-concatenation candidate with d ≡ a (mod 157) and fails closed when non-bijective
#   class: correctness
#   since: 2026-09-15
#
# id: displacement_law_remains_candidate
#   given: an exact executable composite displacement
#   then: no candidate is ratified by execution alone
#   class: doctrine
#   since: 2026-09-15
#
# id: displacement_law_fails_closed
#   given: non-integer channels or a malformed receipt
#   then: construction or replay raises DisplacementLawError rather than inventing a law
#   class: safety
#   since: 2026-09-15
# === END CONTRACTS ===

"""Enumerate the declared displacement-law candidates.

Current candidates:

* ``ordered-concatenation`` (``ucns.visible-displacement-candidate``) — the
  three channel turns concatenate on the native Möbius root loop; angle only.
* ``placement-frame`` (``ucns.placement-frame-candidate``) — ordinal carries
  angle, semantic carries radius via the canonical radial map, context
  carries layer as deck translations.
* ``composite-displacement`` (this module) — records both angle candidates
  plus radius and layer in one receipt so falsification can compare them.

None is ratified; execution alone never selects one.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from typing import Any

from .placement_frame import (
    PlacementFrameRecord,
    build_placement_frame,
)
from .visible_displacement import (
    VisibleDisplacementError,
    VisibleDisplacementRecord,
    build_visible_displacement,
)

SCHEMA = "ucns.displacement-law-candidate"
VERSION = "0.1.0"

DISPLACEMENT_LAW_CANDIDATES: dict[str, dict[str, str]] = {
    "ordered-concatenation": {
        "schema": "ucns.visible-displacement-candidate",
        "summary": (
            "three channel turns concatenate on the native Mobius root loop; "
            "angle only, 360/720 frame law preserved"
        ),
        "standing": "candidate",
    },
    "placement-frame": {
        "schema": "ucns.placement-frame-candidate",
        "summary": (
            "ordinal carries angle, semantic carries radius via the canonical "
            "radial map, context carries layer as deck translations"
        ),
        "standing": "candidate",
    },
    "composite-displacement": {
        "schema": SCHEMA,
        "summary": (
            "records both angle candidates plus radius and layer in one "
            "receipt so falsification can compare them"
        ),
        "standing": "candidate",
    },
}

_HMMM = (
    "none of the enumerated displacement-law candidates is ratified; "
    "falsification selects among them, not execution"
)


class DisplacementLawError(ValueError):
    """Raised when the composite displacement fails closed."""


@dataclass(frozen=True)
class DisplacementRecord:
    schema: str
    version: str
    ordinal: int
    semantic: int
    context: int
    ordered_concatenation: VisibleDisplacementRecord
    placement_frame: PlacementFrameRecord
    candidates: dict[str, dict[str, str]]
    hmmm: str
    receipt_sha256: str

    def as_dict(self) -> dict[str, Any]:
        concatenation = self.ordered_concatenation.as_dict()
        frame = self.placement_frame.as_dict()
        return {
            "schema": self.schema,
            "version": self.version,
            "ordinal": self.ordinal,
            "semantic": self.semantic,
            "context": self.context,
            "ordered_concatenation": {
                "schema": concatenation["schema"],
                "version": concatenation["version"],
                "ordinal": concatenation["ordinal"],
                "semantic": concatenation["semantic"],
                "context": concatenation["context"],
                "total_turn": concatenation["turns"]["total"],
                "mobius": concatenation["mobius"],
                "covering_degree": concatenation["covering_degree"],
                "covering_multiplier": concatenation["covering_multiplier"],
                "receipt_sha256": concatenation["receipt_sha256"],
            },
            "placement_frame": {
                "schema": frame["schema"],
                "version": frame["version"],
                "angle_turn": frame["angle_turn"],
                "mobius": frame["mobius"],
                "radius": frame["radius"],
                "layer": frame["layer"],
                "lifted_angle": frame["lifted_angle"],
                "receipt_sha256": frame["receipt_sha256"],
            },
            "candidates": self.candidates,
            "hmmm": self.hmmm,
            "receipt_sha256": self.receipt_sha256,
        }

    def canonical_bytes(self) -> bytes:
        payload = self.as_dict()
        payload.pop("receipt_sha256", None)
        return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def receipt_bytes(self) -> bytes:
        return json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")


def _coerce_channel(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise DisplacementLawError(f"{name} must be an exact integer")
    return value % 157


def build_displacement(
    ordinal: int,
    semantic: int,
    context: int,
    *,
    covering_degree: int | None = None,
) -> DisplacementRecord:
    """Record the composite candidate displacement with every candidate sub-result."""

    ordinal_residue = _coerce_channel("ordinal", ordinal)
    semantic_residue = _coerce_channel("semantic", semantic)
    context_residue = _coerce_channel("context", context)

    try:
        concatenation = build_visible_displacement(
            ordinal_residue,
            semantic_residue,
            context_residue,
            covering_degree=covering_degree,
        )
    except VisibleDisplacementError as exc:
        raise DisplacementLawError(str(exc)) from exc
    frame = build_placement_frame(ordinal_residue, semantic_residue, context_residue)

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "ordinal": ordinal_residue,
        "semantic": semantic_residue,
        "context": context_residue,
        "ordered_concatenation": {
            "schema": concatenation.schema,
            "version": concatenation.version,
            "ordinal": concatenation.ordinal,
            "semantic": concatenation.semantic,
            "context": concatenation.context,
            "total_turn": (
                f"{concatenation.total_turn.numerator}/{concatenation.total_turn.denominator}"
            ),
            "mobius": {
                "phase_turns": (
                    f"{concatenation.mobius.phase_turns.numerator}/"
                    f"{concatenation.mobius.phase_turns.denominator}"
                ),
                "frame": concatenation.mobius.frame.value,
            },
            "covering_degree": concatenation.covering_degree,
            "covering_multiplier": concatenation.covering_multiplier,
            "receipt_sha256": concatenation.receipt_sha256,
        },
        "placement_frame": {
            "schema": frame.schema,
            "version": frame.version,
            "angle_turn": f"{frame.angle_turn.numerator}/{frame.angle_turn.denominator}",
            "mobius": {
                "phase_turns": (
                    f"{frame.mobius.phase_turns.numerator}/"
                    f"{frame.mobius.phase_turns.denominator}"
                ),
                "frame": frame.mobius.frame.value,
            },
            "radius": repr(frame.radius),
            "layer": frame.layer,
            "lifted_angle": repr(frame.lifted_angle),
            "receipt_sha256": frame.receipt_sha256,
        },
        "candidates": DISPLACEMENT_LAW_CANDIDATES,
        "hmmm": _HMMM,
    }
    receipt = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    return DisplacementRecord(
        schema=SCHEMA,
        version=VERSION,
        ordinal=ordinal_residue,
        semantic=semantic_residue,
        context=context_residue,
        ordered_concatenation=concatenation,
        placement_frame=frame,
        candidates=DISPLACEMENT_LAW_CANDIDATES,
        hmmm=_HMMM,
        receipt_sha256=receipt,
    )


def replay_displacement(data: bytes) -> DisplacementRecord:
    """Rebuild the composite displacement and verify it byte-for-byte."""

    if not isinstance(data, bytes):
        raise DisplacementLawError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise DisplacementLawError("receipt is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise DisplacementLawError("receipt root must be an object")
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise DisplacementLawError("receipt schema or version mismatch")

    record = build_displacement(
        ordinal=obj["ordinal"],
        semantic=obj["semantic"],
        context=obj["context"],
        covering_degree=obj.get("ordered_concatenation", {}).get("covering_degree"),
    )
    if record.receipt_sha256 != obj.get("receipt_sha256"):
        raise DisplacementLawError("receipt digest does not match replayed displacement")
    if record.receipt_bytes() != data:
        raise DisplacementLawError("receipt does not replay byte-identically")
    return record


__all__ = [
    "SCHEMA",
    "VERSION",
    "DISPLACEMENT_LAW_CANDIDATES",
    "DisplacementLawError",
    "DisplacementRecord",
    "build_displacement",
    "replay_displacement",
]
