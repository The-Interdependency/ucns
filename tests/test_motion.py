# === CHECKS ===
# id: check_motion_step_advances_native_mobius_state
#   proves: motion_step_advances_native_mobius_state
#   call: self::test_step_advances_native_mobius_state
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_motion_records_radius_and_layer_per_step
#   proves: motion_records_radius_and_layer_per_step
#   call: self::test_records_radius_and_layer_per_step
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_motion_inherits_unselected_displacement_status
#   proves: motion_inherits_unselected_displacement_status
#   call: self::test_inherits_unselected_displacement_status
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_motion_fails_closed
#   proves: motion_fails_closed
#   call: self::test_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_motion_candidate
#   proves: geometry_public_surface_includes_motion_candidate
#   call: self::test_facade_exports_motion
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

from fractions import Fraction

import pytest

from ucns import MotionError, build_motion, replay_motion
from ucns.carrier import radius_from_breadth


def test_step_advances_native_mobius_state() -> None:
    record = build_motion(((100, 57, 0),))
    assert record.steps[0].turn == Fraction(157, 157)  # one full visible turn
    assert record.steps[0].phase_after == Fraction(0)
    assert "reversed" in record.steps[0].frame_after


def test_records_radius_and_layer_per_step() -> None:
    record = build_motion(((0, 5, 1),))
    step = record.steps[0]
    assert step.radius == radius_from_breadth(5.0)
    assert step.layer == 1


def test_inherits_unselected_displacement_status() -> None:
    record = build_motion(((1, 2, 3),))
    assert record.displacement_candidate == "ordered-concatenation"
    assert record.displacement_candidate_status == "unselected"


def test_fails_closed() -> None:
    with pytest.raises(MotionError):
        build_motion(())
    with pytest.raises(MotionError):
        build_motion(((True, 0, 0),))  # type: ignore[arg-type]
    with pytest.raises(MotionError):
        replay_motion(b"not json")

    record = build_motion(((10, 20, 30), (40, 50, 60)))
    replayed = replay_motion(record.receipt_bytes())
    assert replayed == record

    tampered = bytearray(record.receipt_bytes())
    tampered[30] ^= 0x01
    with pytest.raises(MotionError):
        replay_motion(bytes(tampered))


def test_facade_exports_motion() -> None:
    import ucns

    assert hasattr(ucns, "build_motion")
    assert hasattr(ucns, "replay_motion")
    assert hasattr(ucns, "run_motion_falsification")
    assert ucns.MOTION_SCHEMA == "ucns.motion-candidate"
