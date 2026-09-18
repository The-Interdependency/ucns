# === CHECKS ===
# id: check_falsification_runs_implemented_controls
#   proves: falsification_runs_implemented_controls
#   call: self::test_runs_implemented_controls
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_falsification_frame_control_refutes_ordinal_only_angle
#   proves: falsification_frame_control_refutes_ordinal_only_angle
#   call: self::test_frame_control_refutes_ordinal_only_angle
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_falsification_composite_propagates_failed_hard_gate
#   proves: falsification_composite_propagates_failed_hard_gate
#   call: self::test_composite_propagates_failed_frame_gate
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_falsification_blocks_selection_until_preregistered_controls_complete
#   proves: falsification_blocks_selection_until_preregistered_controls_complete
#   call: self::test_missing_modular_orbit_control_blocks_selection
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_displacement_falsification
#   proves: geometry_public_surface_includes_displacement_falsification
#   call: self::test_facade_exports_falsification
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

from ucns import (
    DISPLACEMENT_FALSIFICATION_SCHEMA,
    DISPLACEMENT_LAW_CANDIDATES,
    FALSIFIER_CONTROLS,
    run_falsification,
)


IMPLEMENTED_CONTROLS = (
    "null",
    "single-channel",
    "pair",
    "channel-permutation",
    "frame",
    "covering",
    "radius",
)


def test_runs_implemented_controls() -> None:
    report = run_falsification()
    assert report.schema == DISPLACEMENT_FALSIFICATION_SCHEMA
    assert set(report.results) == {
        "ordered-concatenation",
        "placement-frame",
        "composite-displacement",
    }
    for candidate, controls in report.results.items():
        for control in IMPLEMENTED_CONTROLS:
            assert control in controls, f"{candidate} missing {control}"
        assert "modular-orbit-permutation" not in controls

    assert "modular-orbit-permutation" in FALSIFIER_CONTROLS
    assert FALSIFIER_CONTROLS["modular-orbit-permutation"].startswith("UNRESOLVED")

    again = run_falsification()
    assert again.receipt_sha256 == report.receipt_sha256
    assert again.receipt_bytes() == report.receipt_bytes()


def test_frame_control_refutes_ordinal_only_angle() -> None:
    report = run_falsification()

    assert report.results["ordered-concatenation"]["frame"]["ok"] is True
    assert report.results["placement-frame"]["frame"]["ok"] is False
    assert "frame" in report.refuted["placement-frame"]
    assert "frame" in report.survivors["ordered-concatenation"]


def test_composite_propagates_failed_frame_gate() -> None:
    report = run_falsification()
    assert report.results["composite-displacement"]["frame"]["ok"] is False
    assert "frame" in report.refuted["composite-displacement"]


def test_missing_modular_orbit_control_blocks_selection() -> None:
    report = run_falsification()
    assert "modular-orbit permutation control has not been executed" in report.hmmm
    assert "no displacement-law candidate is selected" in report.hmmm
    assert all(
        record["standing"] == "candidate"
        for record in DISPLACEMENT_LAW_CANDIDATES.values()
    )


def test_facade_exports_falsification() -> None:
    import ucns

    assert hasattr(ucns, "run_falsification")
    assert hasattr(ucns, "FalsificationReport")
    assert hasattr(ucns, "FALSIFIER_CONTROLS")
    assert ucns.DISPLACEMENT_FALSIFICATION_SCHEMA == DISPLACEMENT_FALSIFICATION_SCHEMA
