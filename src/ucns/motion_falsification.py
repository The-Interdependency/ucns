# === MODULE_BUILD ===
# id: ucns_motion_falsification
#   module_name: motion_falsification
#   module_kind: instrument
#   summary: runs the displacement controls plus the walk-permutation control against the motion candidate
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, MOTION_FALSIFIER_CONTROLS, MotionFalsificationError, MotionFalsificationReport, run_motion_falsification
#   internal_surface: control execution, exact comparison, canonical receipt
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_motion_falsification
#   rollout: executable motion falsification harness; survival is not selection
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_motion_candidate, ucns_displacement_falsification
#   since: 2026-09-19
#   unresolved: motion selection follows displacement selection, which is unresolved
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: motion_falsification_runs_declared_controls
#   given: the motion candidate
#   then: null, single-channel, pair, frame, covering, radius, and walk-permutation controls all execute deterministically
#   class: correctness
#   since: 2026-09-19
#
# id: motion_falsification_walk_permutation_changes_path_not_terminal
#   given: two walk steps in either order
#   then: the recorded path differs while the terminal angle is invariant (abelian terminal displacement)
#   class: correctness
#   since: 2026-09-19
#
# id: motion_falsification_survival_is_not_selection
#   given: a surviving motion candidate
#   then: the report never promotes survival to selection
#   class: doctrine
#   since: 2026-09-19
# === END CONTRACTS ===

"""Falsify the motion candidate.

Controls: the displacement controls (null, single-channel, pair, frame,
covering, radius) plus the walk-permutation control. Survival is not
selection; motion selection follows displacement selection, which remains
unresolved.
"""

from __future__ import annotations

import json
from fractions import Fraction
from hashlib import sha256
from typing import Any

from .lifted_displacement import LiftedDisplacementError, build_lifted_displacement
from .motion import MotionError, build_motion

SCHEMA = "ucns.motion-falsification"
VERSION = "0.1.0"

MOTION_FALSIFIER_CONTROLS: dict[str, str] = {
    "null": "a walk of all-zero residues produces identity motion",
    "single-channel": "one channel nonzero per step, deterministic",
    "pair": "each pair of channels active, deterministic",
    "frame": "one full visible turn flips the frame; two restore it",
    "covering": "non-bijective covering degrees fail closed",
    "radius": "radius is the canonical radial map per step",
    "walk-permutation": (
        "reordering the walk changes the recorded path but not the "
        "terminal angle (abelian terminal displacement)"
    ),
}

_HMMM = (
    "surviving controls do not select the motion candidate; motion "
    "selection follows displacement selection, which remains unresolved"
)


class MotionFalsificationError(ValueError):
    """Raised when the motion falsification harness fails closed."""


def run_motion_falsification() -> dict[str, Any]:
    results: dict[str, dict[str, Any]] = {}

    # null control
    null_record = build_motion(((0, 0, 0), (0, 0, 0)))
    results["null"] = {
        "ok": all(
            step.turn == Fraction(0) and step.phase_after == Fraction(0)
            for step in null_record.steps
        )
        and null_record.end_frame == "positive-local-frame",
        "detail": "all-zero walk produces identity steps and positive frame",
    }

    # single-channel and pair controls (deterministic)
    for control, walk in {
        "single-channel": ((7, 0, 0), (0, 11, 0), (0, 0, 13)),
        "pair": ((7, 11, 0), (7, 0, 13), (0, 11, 13)),
    }.items():
        first = build_motion(walk)
        second = build_motion(walk)
        results[control] = {
            "ok": first.receipt_sha256 == second.receipt_sha256,
            "detail": f"{walk} deterministic",
        }

    # frame control
    one_turn = build_motion(((100, 57, 0),))
    two_turns = build_motion(((156, 156, 2),))
    results["frame"] = {
        "ok": (
            one_turn.end_phase == Fraction(0)
            and "reversed" in one_turn.end_frame
            and two_turns.end_phase == Fraction(0)
            and two_turns.end_frame == "positive-local-frame"
        ),
        "detail": "one full visible turn flips the frame; two restore it",
    }

    # covering control
    covering_ok = True
    try:
        build_lifted_displacement(1, 0, 0, covering_degree=157)
        covering_ok = False
    except LiftedDisplacementError:
        covering_ok = True
    results["covering"] = {
        "ok": covering_ok,
        "detail": "non-bijective covering degree fails closed",
    }

    # radius control
    radius_record = build_motion(((0, 5, 0), (0, 5, 2)))
    results["radius"] = {
        "ok": (
            radius_record.steps[0].radius == radius_record.steps[1].radius
            and radius_record.steps[0].layer == 0
            and radius_record.steps[1].layer == 0
        ),
        "detail": "radius is the canonical radial map per step; two layers return",
    }

    # walk-permutation control
    forward = build_motion(((10, 20, 30), (40, 50, 60)))
    reversed_walk = build_motion(((40, 50, 60), (10, 20, 30)))
    path_differs = (
        forward.steps[0].turn != reversed_walk.steps[0].turn
        or forward.steps[0].phase_after != reversed_walk.steps[0].phase_after
    )
    terminal_invariant = (
        forward.end_phase == reversed_walk.end_phase
        and forward.end_frame == reversed_walk.end_frame
    )
    results["walk-permutation"] = {
        "ok": path_differs and terminal_invariant,
        "path_differs": path_differs,
        "terminal_invariant": terminal_invariant,
        "detail": (
            "reordering the walk changes the recorded path while the "
            "terminal angle stays invariant (abelian terminal displacement)"
        ),
    }

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "controls": MOTION_FALSIFIER_CONTROLS,
        "results": results,
        "survivors": [name for name, result in results.items() if result["ok"]],
        "refuted": [name for name, result in results.items() if not result["ok"]],
        "hmmm": _HMMM,
    }
    payload["receipt_sha256"] = sha256(
        json.dumps(
            {key: value for key, value in payload.items() if key != "receipt_sha256"},
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    return payload


__all__ = [
    "SCHEMA",
    "VERSION",
    "MOTION_FALSIFIER_CONTROLS",
    "MotionFalsificationError",
    "run_motion_falsification",
]
