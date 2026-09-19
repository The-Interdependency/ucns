# === CHECKS ===
# id: check_selection_executes_preregistered_modular_orbit_control
#   proves: selection_executes_preregistered_modular_orbit_control
#   call: self::test_executes_preregistered_modular_orbit_control
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_selection_requires_all_applicable_controls_survive
#   proves: selection_requires_all_applicable_controls_survive
#   call: self::test_requires_all_applicable_controls_survive
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_selection_receipt_is_scoped_and_replayable
#   proves: selection_receipt_is_scoped_and_replayable
#   call: self::test_receipt_is_scoped_and_replayable
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_displacement_selection
#   proves: geometry_public_surface_includes_displacement_selection
#   call: self::test_facade_exports_selection
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

import json

import pytest

from ucns import (
    DisplacementSelectionError,
    replay_displacement_selection,
    run_displacement_selection,
    run_modular_orbit_permutation_control,
)


def test_executes_preregistered_modular_orbit_control() -> None:
    control = run_modular_orbit_permutation_control()
    # the full NativeMobiusState criterion refutes ordered-concatenation:
    # per-channel residue reduction misattributes the wrap at the frame level
    assert control["verdicts"]["ordered-concatenation"]["ok"] is False
    assert "frame" in control["verdicts"]["ordered-concatenation"]["detail"]
    assert control["verdicts"]["placement-frame"]["ok"] is True


def test_requires_all_applicable_controls_survive() -> None:
    report = run_displacement_selection()
    decisions = report["decisions"]
    # ordered-concatenation fails the preregistered modular-orbit control
    assert decisions["ordered-concatenation"]["selected"] is False
    # placement-frame fails the frame hard gate, so it is not selected
    assert decisions["placement-frame"]["selected"] is False
    assert "frame" in decisions["placement-frame"]["refuted_controls"]
    assert decisions["composite-displacement"]["selected"] is False
    assert report["selected"] == []


def test_receipt_is_scoped_and_replayable() -> None:
    report = run_displacement_selection()
    assert report["covering_congruence"]["congruence_class"] == "d ≡ 1 (mod 157)"
    data = json.dumps(report, sort_keys=True, separators=(",", ":")).encode("utf-8")
    replayed = replay_displacement_selection(data)
    assert replayed["receipt_sha256"] == report["receipt_sha256"]

    tampered = bytearray(data)
    tampered[40] ^= 0x01
    with pytest.raises(DisplacementSelectionError):
        replay_displacement_selection(bytes(tampered))


def test_facade_exports_selection() -> None:
    import ucns

    assert hasattr(ucns, "run_displacement_selection")
    assert hasattr(ucns, "replay_displacement_selection")
    assert hasattr(ucns, "run_modular_orbit_permutation_control")
    assert ucns.DISPLACEMENT_SELECTION_SCHEMA == "ucns.displacement-selection"
