# === MODULE_BUILD ===
# id: ucns_displacement_falsification
#   module_name: displacement_falsification
#   module_kind: instrument
#   summary: runs the implemented displacement controls, propagates hard-gate failures, and exposes the preregistered modular-orbit control as unresolved
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, FALSIFIER_CONTROLS, FalsificationError, FalsificationReport, run_falsification
#   internal_surface: control execution, exact comparison, canonical receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_displacement_falsification
#   rollout: executable partial falsification harness; incomplete preregistered evidence blocks selection
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_displacement_law_candidates, ucns_visible_displacement_candidate, ucns_placement_frame_candidate
#   since: 2026-09-16
#   unresolved: the preregistered modular-orbit permutation control is not yet implemented
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: falsification_runs_implemented_controls
#   given: the displacement-law candidates
#   then: null, single-channel, pair, diagnostic channel-permutation, frame, covering, and radius controls execute exactly and deterministically while the missing preregistered modular-orbit control stays explicit
#   class: correctness
#   since: 2026-09-17
#
# id: falsification_frame_control_refutes_ordinal_only_angle
#   given: ordinal = 157 with the placement-frame candidate
#   then: the candidate collapses a full visible turn to angle zero and loses the 360/720 frame flip, so the placement-frame candidate fails the frame hard gate
#   class: correctness
#   since: 2026-09-16
#
# id: falsification_composite_propagates_failed_hard_gate
#   given: one composite sub-candidate fails an applicable hard control
#   then: the composite fails that control rather than borrowing survival from the other sub-candidate
#   class: safety
#   since: 2026-09-17
#
# id: falsification_blocks_selection_until_preregistered_controls_complete
#   given: the preregistered modular-orbit permutation control has not been executed
#   then: the report preserves that missing evidence as hmmm and authorizes no candidate selection
#   class: doctrine
#   since: 2026-09-17
# === END CONTRACTS ===

"""Run the implemented displacement-law falsification controls.

The preregistration requires a permutation control using the same residues under
a known modular-orbit action. The original harness instead rotated the three
channel positions. That channel rotation remains useful as a diagnostic, but it
is not the preregistered modular-orbit control and cannot close the selection
gate.

Implemented controls:

* null control — all three residue channels zero/neutral;
* single-channel control — one channel nonzero, the other two neutral;
* pair controls — each pair active independently;
* channel-permutation diagnostic — the same residues under a channel reorder;
* frame control — one full visible turn must flip the frame, two restore;
* covering control — non-bijective covering degrees fail closed;
* radius control — radius is the canonical radial map, not an additive depth.

Unresolved required control:

* modular-orbit permutation — the same residues under a known modular-orbit
  action, with its expected comparison criterion frozen before execution.

A candidate that fails an implemented hard control is refuted. A candidate that
survives the implemented controls is not selected while required preregistered
evidence remains unresolved.
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

SCHEMA = "ucns.displacement-falsification"
VERSION = "0.2.0"

FALSIFIER_CONTROLS: dict[str, str] = {
    "null": "all three residue channels zero/neutral",
    "single-channel": "one channel nonzero, the other two neutral",
    "pair": "each pair of channels active independently",
    "channel-permutation": (
        "diagnostic channel reorder only; not the preregistered modular-orbit action"
    ),
    "modular-orbit-permutation": (
        "UNRESOLVED: same residues under a known modular-orbit action"
    ),
    "frame": "one full visible turn must flip the frame; two must restore",
    "covering": "non-bijective covering degrees fail closed",
    "radius": "radius is the canonical radial map on breadth, not an additive depth",
}

_HMMM = (
    "the preregistered modular-orbit permutation control has not been executed; "
    "the implemented channel-permutation diagnostic is not a substitute, so no "
    "displacement-law candidate is selected by this report"
)


class FalsificationError(ValueError):
    """Raised when the falsification harness fails closed."""


@dataclass(frozen=True)
class FalsificationReport:
    schema: str
    version: str
    candidates: dict[str, dict[str, str]]
    controls: dict[str, str]
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
            "controls": self.controls,
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
    """Run implemented controls without claiming the missing preregistered control."""

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

    # Diagnostic channel-permutation control. This is deliberately not named or
    # represented as the preregistered modular-orbit permutation falsifier.
    permutation = build_displacement(7, 11, 13)
    permuted = build_displacement(11, 13, 7)
    concat_ok = (
        permutation.ordered_concatenation.total_turn
        == permuted.ordered_concatenation.total_turn
    )
    frame_angle_changes = (
        permutation.placement_frame.angle_turn != permuted.placement_frame.angle_turn
    )
    results["ordered-concatenation"]["channel-permutation"] = _result(
        concat_ok,
        "total turn is invariant under channel reorder (abelian turn sum)",
    )
    results["placement-frame"]["channel-permutation"] = _result(
        frame_angle_changes,
        "angle follows the ordinal channel and therefore changes under channel reorder",
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
        "the placement-frame candidate fails the frame hard gate",
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

    # Composite candidate: a failed hard gate in either carried sub-candidate
    # remains a failed hard gate for the composite. It cannot be compensated by
    # the other sub-candidate's survival.
    composite_results: dict[str, dict[str, Any]] = {}
    for control in (
        "null",
        "single-channel",
        "pair",
        "channel-permutation",
        "frame",
        "covering",
        "radius",
    ):
        left = results["ordered-concatenation"][control]["ok"]
        right = results["placement-frame"][control]["ok"]
        composite_results[control] = _result(
            left and right,
            f"composite survives {control} iff both carried sub-candidates do",
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
        "controls": FALSIFIER_CONTROLS,
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
        controls=FALSIFIER_CONTROLS,
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
