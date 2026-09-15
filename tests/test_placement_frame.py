# === CHECKS ===
# id: check_placement_frame_ordinal_carries_angle
#   proves: placement_frame_ordinal_carries_angle
#   call: self::test_ordinal_carries_angle
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_placement_frame_semantic_carries_radius_via_breadth
#   proves: placement_frame_semantic_carries_radius_via_breadth
#   call: self::test_semantic_carries_radius_via_breadth
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_placement_frame_context_carries_layer
#   proves: placement_frame_context_carries_layer
#   call: self::test_context_carries_layer
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_placement_frame_preserves_native_mobius_law
#   proves: placement_frame_preserves_native_mobius_law
#   call: self::test_preserves_native_mobius_law
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_placement_frame_remains_candidate
#   proves: placement_frame_remains_candidate
#   call: self::test_remains_candidate
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_placement_frame_fails_closed
#   proves: placement_frame_fails_closed
#   call: self::test_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_placement_frame_candidate
#   proves: geometry_public_surface_includes_placement_frame_candidate
#   call: self::test_facade_exports_placement_frame
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

from fractions import Fraction
from math import isclose, pi

import pytest

from ucns import (
    PLACEMENT_FRAME_SCHEMA,
    PlacementFrameError,
    build_placement_frame,
    replay_placement_frame,
)
from ucns.carrier import radius_from_breadth
from ucns.direct_mobius import NativeMobiusFrame


def test_ordinal_carries_angle() -> None:
    record = build_placement_frame(1, 0, 0)
    assert record.angle_turn == Fraction(1, 157)
    assert record.mobius.phase_turns == Fraction(1, 157)
    assert record.mobius.frame is NativeMobiusFrame.POSITIVE


def test_semantic_carries_radius_via_breadth() -> None:
    record = build_placement_frame(0, 5, 0)
    assert record.radius == radius_from_breadth(5.0)


def test_context_carries_layer() -> None:
    zero = build_placement_frame(0, 0, 0)
    one = build_placement_frame(0, 0, 1)
    two = build_placement_frame(0, 0, 2)
    assert zero.layer == 0
    assert one.layer == 1
    assert two.layer == 0  # two laps complete return
    assert isclose(one.lifted_angle, 2.0 * pi, abs_tol=1e-12)


def test_preserves_native_mobius_law() -> None:
    from ucns.direct_mobius import native_mobius_state

    record = build_placement_frame(100, 0, 0)
    expected = native_mobius_state().advance(Fraction(100, 157))
    assert record.mobius == expected
    assert record.mobius.phase_turns == Fraction(100, 157)
    assert record.mobius.frame is NativeMobiusFrame.POSITIVE


def test_remains_candidate() -> None:
    record = build_placement_frame(1, 2, 3)
    assert "candidate" in PLACEMENT_FRAME_SCHEMA
    assert "candidates" in record.hmmm


def test_fails_closed() -> None:
    with pytest.raises(PlacementFrameError):
        build_placement_frame(True, 0, 0)  # type: ignore[arg-type]
    with pytest.raises(PlacementFrameError):
        replay_placement_frame(b"not json")

    record = build_placement_frame(10, 20, 30)
    replayed = replay_placement_frame(record.receipt_bytes())
    assert replayed == record

    tampered = bytearray(record.receipt_bytes())
    tampered[30] ^= 0x01
    with pytest.raises(PlacementFrameError):
        replay_placement_frame(bytes(tampered))


def test_facade_exports_placement_frame() -> None:
    import ucns

    assert hasattr(ucns, "build_placement_frame")
    assert hasattr(ucns, "replay_placement_frame")
    assert ucns.PLACEMENT_FRAME_SCHEMA == PLACEMENT_FRAME_SCHEMA
