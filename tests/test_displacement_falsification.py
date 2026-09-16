# === CHECKS ===
# id: check_falsification_runs_declared_controls
#   proves: falsification_runs_declared_controls
#   call: self::test_runs_declared_controls
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
# id: check_falsification_records_survivors_honestly
#   proves: falsification_records_survivors_honestly
#   call: self::test_records_survivors_honestly
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
    FALSIFIER_CONTROLS,
    run_falsification,
)


def test_runs_declared_controls() -> None:
    report = run_falsification()
    assert report.schema == DISPLACEMENT_FALSIFICATION_SCHEMA
    assert set(report.results) == {
        "ordered-concatenation",
        "placement-frame",
        "composite-displacement",
    }
    for candidate, controls in report.results.items():
        for control in ("null", "single-channel", "pair", "permutation", "frame", "covering", "radius"):
            assert control in controls, f"{candidate} missing {control}"

    again = run_falsification()
    assert again.receipt_sha256 == report.receipt_sha256
    assert again.receipt_bytes() == report.receipt_bytes()


def test_frame_control_refutes_ordinal_only_angle() -> None:
    report = run_falsification()

    # ordered concatenation survives the frame control.
    assert report.results["ordered-concatenation"]["frame"]["ok"] is True
    # placement-frame is refuted: ordinal=157 collapses to angle zero.
    assert report.results["placement-frame"]["frame"]["ok"] is False
    assert "frame" in report.refuted["placement-frame"]
    assert "frame" in report.survivors["ordered-concatenation"]


def test_records_survivors_honestly() -> None:
    report = run_falsification()
    for name in report.results:
        assert set(report.refuted[name]) | set(report.survivors[name]) == set(
            report.results[name]
        )
    # surviving candidates are not promoted to ratified.
    assert "not ratified" in report.hmmm
    for name, controls in report.results.items():
        if report.survivors[name]:
            for outcome in controls.values():
                assert "ok" in outcome


def test_facade_exports_falsification() -> None:
    import ucns

    assert hasattr(ucns, "run_falsification")
    assert hasattr(ucns, "FalsificationReport")
    assert hasattr(ucns, "FALSIFIER_CONTROLS")
    assert ucns.DISPLACEMENT_FALSIFICATION_SCHEMA == DISPLACEMENT_FALSIFICATION_SCHEMA
