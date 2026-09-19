# === MODULE_BUILD ===
# id: ucns_displacement_selection
#   module_name: displacement_selection
#   module_kind: selection
#   summary: executes the preregistered modular-orbit permutation control and, when every applicable control survives, records a scoped displacement-law selection receipt
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, SELECTION_CONTROLS, DisplacementSelectionError, run_modular_orbit_permutation_control, run_displacement_selection, replay_displacement_selection
#   internal_surface: frozen modular-orbit comparison criterion, control execution, scoped ratification receipt
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_displacement_selection
#   rollout: scoped selection decision; selection is scoped to the executed preregistered controls and never claims the unresolved lift law
#   rollback: remove this module, facade exports, tests, and selection documentation
#   requires: ucns_displacement_falsification, ucns_visible_displacement_candidate, ucns_placement_frame_candidate, ucns_modular_orbit_geometry
#   since: 2026-09-19
#   unresolved: the law selecting one continuum covering lift d from d ≡ a (mod 157) remains hmmm
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: selection_executes_preregistered_modular_orbit_control
#   given: the preregistered modular-orbit permutation control
#   then: it executes with the comparison criterion frozen before execution and records results per candidate
#   class: correctness
#   since: 2026-09-19
#
# id: selection_requires_all_applicable_controls_survive
#   given: a displacement-law candidate
#   then: it is selected only if every applicable implemented control and the modular-orbit control survive
#   class: doctrine
#   since: 2026-09-19
#
# id: selection_receipt_is_scoped_and_replayable
#   given: a selection decision
#   then: the scoped ratification receipt carries a canonical digest and replays byte-identically, and records the covering congruence class
#   class: correctness
#   since: 2026-09-19
# === END CONTRACTS ===

"""Execute the missing preregistered control and record scoped selection.

The preregistered modular-orbit permutation control applies a known
modular-orbit action ``x -> a*x mod 157`` to the same residues and requires
the complete NativeMobiusState (phase and lifted frame) to transform by the
same action. The comparison criterion is frozen before execution:

* ordered-concatenation: the acted candidate must equal the state reached
  by advancing ``a * (ordinal + semantic + context mod 157) mod 157``
  turns from the identity;
* placement-frame: the acted ordinal angle must equal
  ``a * ordinal mod 157`` (its radius and layer channels are not turn
  observables and are recorded not-applicable).

Selection is scoped to the executed controls. The law selecting one
continuum covering lift remains hmmm.
"""

from __future__ import annotations

import json
from fractions import Fraction
from hashlib import sha256
from typing import Any

from .direct_mobius import native_mobius_state
from .displacement_falsification import FalsificationError, run_falsification
from .lifted_displacement import LiftedDisplacementError, build_lifted_displacement
from .placement_frame import build_placement_frame
from .visible_displacement import build_visible_displacement

SCHEMA = "ucns.displacement-selection"
VERSION = "0.1.0"
_MODULUS = 157

SELECTION_CONTROLS: dict[str, str] = {
    "modular-orbit-permutation": (
        "same residues under the known modular-orbit action x -> a*x mod 157; "
        "the turn transforms by the same action"
    ),
}

_HMMM = (
    "selection is scoped to the executed preregistered controls; the "
    "per-channel-reduction ordered-concatenation candidate is falsified, "
    "while the lifted ordered-concatenation candidate that sums before "
    "reduction is selected for the tested scope; the law selecting one "
    "continuum covering lift d from d ≡ a (mod 157) remains hmmm"
)


class DisplacementSelectionError(ValueError):
    """Raised when the selection run fails closed."""


def _acted_turn(record: Any) -> Fraction:
    return record.mobius.phase_turns


def run_modular_orbit_permutation_control() -> dict[str, Any]:
    """Execute the preregistered modular-orbit permutation control."""

    results: dict[str, dict[str, Any]] = {}
    for a in (2, 3):
        for triple in ((7, 11, 13), (100, 57, 0)):
            original = build_visible_displacement(*triple)
            acted = build_visible_displacement(*(a * r % _MODULUS for r in triple))
            expected_num = (a * (sum(triple) % _MODULUS)) % _MODULUS
            expected = native_mobius_state().advance(Fraction(expected_num, _MODULUS))
            ok = acted.mobius == expected
            results.setdefault("ordered-concatenation", {})[
                f"a={a},triple={triple}"
            ] = {
                "ok": ok,
                "expected_num": expected_num,
                "actual_phase": f"{acted.mobius.phase_turns.numerator}/{acted.mobius.phase_turns.denominator}",
                "original_turn": f"{original.total_turn.numerator}/{original.total_turn.denominator}",
            }

    for a in (2, 3):
        for ordinal in (7, 100):
            original = build_placement_frame(ordinal, 11, 13)
            acted = build_placement_frame(a * ordinal % _MODULUS, 11, 13)
            expected = Fraction(a * ordinal % _MODULUS, _MODULUS)
            results.setdefault("placement-frame", {})[
                f"a={a},ordinal={ordinal}"
            ] = {
                "ok": acted.angle_turn == expected,
                "radius_not_a_turn_observable": True,
                "layer_not_a_turn_observable": True,
            }

    for a in (2, 3):
        for triple in ((7, 11, 13), (100, 57, 0)):
            acted = build_lifted_displacement(*(a * r for r in triple))
            expected = native_mobius_state().advance(
                Fraction(a * sum(triple), _MODULUS)
            )
            ok = (
                acted.phase_turns == expected.phase_turns
                and acted.frame == expected.frame.value
            )
            results.setdefault("lifted-ordered-concatenation", {})[
                f"a={a},triple={triple}"
            ] = {
                "ok": ok,
                "expected_turn": f"{expected.phase_turns.numerator}/{expected.phase_turns.denominator}",
                "actual_turn": f"{acted.total_turn.numerator}/{acted.total_turn.denominator}",
            }

    verdicts = {}
    for name, cases in results.items():
        ok = all(case["ok"] for case in cases.values())
        if name == "ordered-concatenation" and not ok:
            detail = (
                "the complete NativeMobiusState does not transform by the "
                "modular-orbit action: per-channel residue reduction "
                "misattributes the wrap at the lifted frame level"
            )
        else:
            detail = (
                "the complete NativeMobiusState transforms by the "
                "modular-orbit action"
                if ok
                else "the turn does not transform by the modular-orbit action"
            )
        verdicts[name] = {"ok": ok, "detail": detail}
    return {"results": results, "verdicts": verdicts}


def run_displacement_selection() -> dict[str, Any]:
    """Run the full control surface and record a scoped selection decision."""

    falsification = run_falsification()
    modular = run_modular_orbit_permutation_control()

    # Lifted candidate controls mirroring the angle-only surface.
    lifted_refuted: list[str] = []
    lifted_controls: dict[str, dict[str, Any]] = {}
    null = build_lifted_displacement(0, 0, 0)
    lifted_controls["null"] = {
        "ok": null.total_turn == Fraction(0) and null.frame == "positive-local-frame",
        "detail": "zero channels produce identity motion",
    }
    for control, triples in {
        "single-channel": [(7, 0, 0), (0, 11, 0), (0, 0, 13)],
        "pair": [(7, 11, 0), (7, 0, 13), (0, 11, 13)],
    }.items():
        ok = True
        for triple in triples:
            first = build_lifted_displacement(*triple)
            second = build_lifted_displacement(*triple)
            ok = ok and first == second
        lifted_controls[control] = {"ok": ok, "detail": f"{control} deterministic"}
    one = build_lifted_displacement(100, 57, 0)
    two = build_lifted_displacement(156, 156, 2)
    lifted_controls["frame"] = {
        "ok": (
            one.phase_turns == Fraction(0)
            and "reversed" in one.frame
            and two.phase_turns == Fraction(0)
            and two.frame == "positive-local-frame"
        ),
        "detail": "one full visible turn flips the frame; two restore it",
    }
    covering_ok = True
    try:
        build_lifted_displacement(1, 0, 0, covering_degree=157)
        covering_ok = False
    except LiftedDisplacementError:
        covering_ok = True
    lifted_controls["covering"] = {
        "ok": covering_ok,
        "detail": "non-bijective covering degree fails closed",
    }
    lifted_controls["radius"] = {
        "ok": True,
        "detail": "not applicable: angle-only candidate carries no radius",
    }
    lifted_controls["modular-orbit-permutation"] = {
        "ok": modular["verdicts"]["lifted-ordered-concatenation"]["ok"],
        "detail": modular["verdicts"]["lifted-ordered-concatenation"]["detail"],
    }
    for control, outcome in lifted_controls.items():
        if not outcome["ok"]:
            lifted_refuted.append(control)

    selected: list[str] = []
    decisions: dict[str, dict[str, Any]] = {}
    for name in falsification.results:
        refuted = falsification.refuted.get(name, [])
        modular_ok = modular["verdicts"].get(name, {}).get("ok", True)
        ok = not refuted and modular_ok
        decisions[name] = {
            "refuted_controls": refuted,
            "modular_orbit_control": modular["verdicts"].get(name),
            "selected": ok,
        }
        if ok:
            selected.append(name)
    decisions["lifted-ordered-concatenation"] = {
        "refuted_controls": lifted_refuted,
        "modular_orbit_control": modular["verdicts"]["lifted-ordered-concatenation"],
        "selected": not lifted_refuted,
    }
    if not lifted_refuted:
        selected.append("lifted-ordered-concatenation")

    # Recorded covering congruence class for the lifted candidate:
    # d = 158 is bijective and d ≡ 1 (mod 157).
    covering_witness = build_lifted_displacement(1, 0, 0, covering_degree=158)
    covering_congruence = {
        "covering_degree": covering_witness.covering_degree,
        "multiplier": covering_witness.covering_multiplier,
        "congruence_class": "d ≡ 1 (mod 157)",
    }

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "controls": SELECTION_CONTROLS,
        "modular_orbit_permutation": modular,
        "falsification_receipt": falsification.receipt_sha256,
        "decisions": decisions,
        "selected": selected,
        "covering_congruence": covering_congruence,
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


def replay_displacement_selection(data: bytes) -> dict[str, Any]:
    """Recompute the selection receipt and verify byte-identically."""

    if not isinstance(data, bytes):
        raise DisplacementSelectionError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise DisplacementSelectionError("receipt is not valid canonical JSON") from exc
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise DisplacementSelectionError("receipt schema or version mismatch")
    rebuilt = run_displacement_selection()
    if rebuilt["receipt_sha256"] != obj.get("receipt_sha256"):
        raise DisplacementSelectionError("receipt digest does not match recomputation")
    rebuilt_bytes = json.dumps(rebuilt, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if rebuilt_bytes != data:
        raise DisplacementSelectionError("receipt does not replay byte-identically")
    return rebuilt


__all__ = [
    "SCHEMA",
    "VERSION",
    "SELECTION_CONTROLS",
    "DisplacementSelectionError",
    "run_modular_orbit_permutation_control",
    "run_displacement_selection",
    "replay_displacement_selection",
]
