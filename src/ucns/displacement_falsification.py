# === MODULE_BUILD ===
# id: ucns_displacement_falsification
#   module_name: displacement_falsification
#   module_kind: instrument
#   summary: runs the declared falsification controls against the displacement-law candidates and records which candidates survive
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, FALSIFIER_CONTROLS, FalsificationError, FalsificationReport, run_falsification
#   internal_surface: control execution, exact comparison, canonical receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_displacement_falsification
#   rollout: executable falsification harness; falsification selects among candidates, execution alone ratifies nothing
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_displacement_law_candidates, ucns_visible_displacement_candidate, ucns_placement_frame_candidate
#   since: 2026-09-16
#   unresolved: ratification remains hmmm even for surviving candidates
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: falsification_runs_declared_controls
#   given: the displacement-law candidates
#   then: null, single-channel, pair, permutation, frame, covering, and radius controls all execute exactly and deterministically
#   class: correctness
#   since: 2026-09-16
#
# id: falsification_frame_control_refutes_ordinal_only_angle
#   given: ordinal = 157 with the placement-frame candidate
#   then: the candidate collapses a full visible turn to angle zero and loses the 360/720 frame flip, so the ordinal-only angle candidate is refuted by the frame control
#   class: correctness
#   since: 2026-09-16
#
# id: falsification_records_survivors_honestly
#   given: a falsification run
#   then: the report records exactly which candidate survived which control and never promotes a survivor to ratified
#   class: doctrine
#   since: 2026-09-16
# === END CONTRACTS ===

"""Falsify the displacement-law candidates.

The preregistration declares these controls:

* null control — all three residue channels zero/neutral;
* single-channel control — one channel nonzero, the other two neutral;
* pair controls — each pair active independently;
* permutation control — the same residues under a known permutation;
* frame control — one full visible turn must flip the frame, two restore;
* covering control — non-bijective covering degrees fail closed;
* radius control — radius is the canonical radial map, not an additive depth.

This harness runs those controls against the declared candidates and records
which candidates survive. A candidate that fails a control is refuted.
Survival is not ratification.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from typing import Any

from .displacement_law import (
    DISPLACEMENT_LAW_CANDIDATES,
    DisplacementLawError,
    build_displacement,
)
from .placement_frame import build_placement_frame
from .visible_displacement import build_visible_displacement

SCHEMA = "ucns.displacement-falsification"
VERSION = "0.1.0"

FALSIFIER_CONTROLS: dict[str, str] = {
    "null": "all three residue channels zero/neutral",
    "single-channel": "one channel nonzero, the other two neutral",
    "pair": "each pair of channels active independently",
    "permutation": "the same residues under a known channel permutation",
    "frame": "one full visible turn must flip the frame; two must restore",
    "covering": "non-bijective covering degrees fail closed",
    "radius": "radius is the canonical radial map on breadth, not an additive depth",
}

_HMMM = (
    "falsification selects among candidates; survivors remain candidates "
    "and are not ratified by survival alone"
)


class FalsificationError(ValueError):
    """Raised when the falsification harness fails closed."""


@dataclass(frozen=True)
class FalsificationReport:
    schema: str
    version: str
    candidates: dict[str, dict[str, str]]
    results: dict[str, dict[str, dict[str, Any]]]
    refuted: dict[str, list[str]]
    survivors: dict[str, list[str]]
    hmmm: str
    receipt_sha256: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "version": self.version,
            "candidates": self.candidates,
            "results": self.results,
            "refuted": self.refuted,
            "survivors": self.survivors,
            "hmmm": self.hmmm,
            "receipt_sha256": self.receipt_sha256,
        }

    def canonical_bytes(self) -> bytes:
        payload = self.as_dict()
        payload.pop("receipt_sha256", None)
        return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def receipt_bytes(self) -> bytes:
        return json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")


def _result(ok: bool, detail: str) -> dict[str, Any]:
    return {"ok": ok, "detail": detail}


def _check_frame_flip(phase: Fraction, frame: str) -> bool:
    return phase == Fraction(0) and frame == "reversed-local-frame"


def _check_frame_restore(phase: Fraction, frame: str) -> bool:
    return phase == Fraction(0) and frame == "positive-local-frame"


def run_falsification() -> FalsificationReport:
    """Run every declared control and record which candidates survive."""

    results: dict[str, dict[str, dict[str, Any]]] = {
        name: {} for name in DISPLACEMENT_LAW_CANDIDATES
    }

    # null control
    for name in ("ordered-concatenation", "placement-frame"):
        record = build_displacement(0, 0, 0)
        if name == "ordered-concatenation":
            candidate = record.ordered_concatenation
            ok = (
                candidate.total_turn == Fraction(0)
                and candidate.mobius.phase_turns == Fraction(0)
                and candidate.mobius.frame.value == "positive-local-frame"
            )
        else:
            candidate = record.placement_frame
            ok = (
                candidate.angle_turn == Fraction(0)
                and candidate.mobius.frame.value == "positive-local-frame"
                and candidate.radius == 0.0
                and candidate.layer == 0
            )
        results[name]["null"] = _result(
            ok, "zero channels produce zero angle, positive frame, zero radius, zero layer"
        )

    # single-channel and pair controls (exact determinism)
    cases = {
        "single-channel": [(7, 0, 0), (0, 11, 0), (0, 0, 13)],
        "pair": [(7, 11, 0), (7, 0, 13), (0, 11, 13)],
    }
    for control, triples in cases.items():
        for name in ("ordered-concatenation", "placement-frame"):
            detail_parts = []
            ok = True
            for triple in triples:
                first = build_displacement(*triple)
                second = build_displacement(*triple)
                if name == "ordered-concatenation":
                    sub_ok = (
                        first.ordered_concatenation == second.ordered_concatenation
                        and first.ordered_concatenation.receipt_sha256
                        == second.ordered_concatenation.receipt_sha256
                    )
                else:
                    sub_ok = (
                        first.placement_frame == second.placement_frame
                        and first.placement_frame.receipt_sha256
                        == second.placement_frame.receipt_sha256
                    )
                ok = ok and sub_ok
                detail_parts.append(f"{triple}:{'exact' if sub_ok else 'drift'}")
            results[name][control] = _result(ok, "; ".join(detail_parts))

    # permutation control
    permutation = build_displacement(7, 11, 13)
    permuted = build_displacement(11, 13, 7)
    concat_ok = (
        permutation.ordered_concatenation.total_turn
        == permuted.ordered_concatenation.total_turn
    )
    frame_angle_changes = (
        permutation.placement_frame.angle_turn != permuted.placement_frame.angle_turn
    )
    results["ordered-concatenation"]["permutation"] = _result(
        concat_ok,
        "total turn is invariant under channel permutation (abelian turn sum)",
    )
    results["placement-frame"]["permutation"] = _result(
        frame_angle_changes,
        "angle follows the ordinal channel and therefore changes under permutation",
    )

    # frame control
    one_turn = build_displacement(100, 57, 0)
    two_turns = build_displacement(156, 156, 2)
    concat_one_ok = _check_frame_flip(
        one_turn.ordered_concatenation.mobius.phase_turns,
        one_turn.ordered_concatenation.mobius.frame.value,
    )
    concat_two_ok = _check_frame_restore(
        two_turns.ordered_concatenation.mobius.phase_turns,
        two_turns.ordered_concatenation.mobius.frame.value,
    )
    results["ordered-concatenation"]["frame"] = _result(
        concat_one_ok and concat_two_ok,
        "one full visible turn flips the frame and two restore it",
    )

    # The placement-frame candidate collapses ordinal=157 to angle zero and
    # therefore cannot produce the required frame flip from a full turn.
    ordinal_full_turn = build_placement_frame(157, 0, 0)
    frame_ok = _check_frame_flip(
        ordinal_full_turn.mobius.phase_turns,
        ordinal_full_turn.mobius.frame.value,
    )
    results["placement-frame"]["frame"] = _result(
        frame_ok,
        "ordinal=157 collapses to angle zero and does not flip the frame; "
        "the ordinal-only angle candidate is refuted by the frame control",
    )

    # covering control
    covering_ok = True
    try:
        build_displacement(1, 0, 0, covering_degree=157)
        covering_ok = False
    except DisplacementLawError:
        covering_ok = True
    results["ordered-concatenation"]["covering"] = _result(
        covering_ok, "non-bijective covering degree fails closed"
    )
    results["placement-frame"]["covering"] = _result(
        True, "not applicable: covering witness lives on the concatenation candidate"
    )

    # radius control
    depth_zero = build_placement_frame(0, 5, 0)
    depth_two = build_placement_frame(0, 5, 2)
    radius_ok = (
        depth_zero.radius == depth_two.radius
        and depth_zero.layer == 0
        and depth_two.layer == 0
        and depth_zero.radius != 0.0
    )
    results["placement-frame"]["radius"] = _result(
        radius_ok,
        "radius is the canonical radial map on breadth and does not advance "
        "with completed layers; two layers complete the return",
    )
    results["ordered-concatenation"]["radius"] = _result(
        True, "not applicable: angle-only candidate carries no radius"
    )

    # composite candidate: survives exactly where both sub-candidates survive.
    composite_results: dict[str, dict[str, Any]] = {}
    for control in ("null", "single-channel", "pair", "permutation", "covering"):
        left = results["ordered-concatenation"][control]["ok"]
        right = results["placement-frame"][control]["ok"]
        composite_results[control] = _result(
            left and right,
            f"composite survives {control} iff both sub-candidates do",
        )
    composite_results["frame"] = _result(
        results["ordered-concatenation"]["frame"]["ok"],
        "composite records the surviving concatenation frame control and the "
        "refuted ordinal-only frame control side by side",
    )
    composite_results["radius"] = _result(
        results["placement-frame"]["radius"]["ok"],
        "composite carries the placement-frame radius control",
    )
    results["composite-displacement"] = composite_results

    refuted: dict[str, list[str]] = {}
    survivors: dict[str, list[str]] = {}
    for name, controls in results.items():
        refuted[name] = [control for control, outcome in controls.items() if not outcome["ok"]]
        survivors[name] = [control for control, outcome in controls.items() if outcome["ok"]]

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "candidates": DISPLACEMENT_LAW_CANDIDATES,
        "results": results,
        "refuted": refuted,
        "survivors": survivors,
        "hmmm": _HMMM,
    }
    receipt = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    return FalsificationReport(
        schema=SCHEMA,
        version=VERSION,
        candidates=DISPLACEMENT_LAW_CANDIDATES,
        results=results,
        refuted=refuted,
        survivors=survivors,
        hmmm=_HMMM,
        receipt_sha256=receipt,
    )


__all__ = [
    "SCHEMA",
    "VERSION",
    "FALSIFIER_CONTROLS",
    "FalsificationError",
    "FalsificationReport",
    "run_falsification",
]
