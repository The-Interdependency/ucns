# === CHECKS ===
# id: check_radius_recursion_radius_is_canonical_radial_map
#   proves: radius_recursion_radius_is_canonical_radial_map
#   call: self::test_radius_is_canonical_radial_map_not_depth
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_radius_recursion_layers_are_deck_translations
#   proves: radius_recursion_layers_are_deck_translations
#   call: self::test_layers_are_deck_translations
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_radius_recursion_two_laps_complete_return
#   proves: radius_recursion_two_laps_complete_return
#   call: self::test_two_laps_complete_return
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_radius_recursion_english_depth_is_not_a_radius
#   proves: radius_recursion_english_depth_is_not_a_radius
#   call: self::test_english_depth_is_not_a_radius
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_radius_recursion_fails_closed
#   proves: radius_recursion_fails_closed
#   call: self::test_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_radius_recursion_candidate
#   proves: geometry_public_surface_includes_radius_recursion_candidate
#   call: self::test_facade_exports_radius_recursion
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

import json
from math import isclose, pi

import pytest

from ucns import (
    RADIUS_RECURSION_SCHEMA,
    RadiusRecursionError,
    build_radius_recursion,
    replay_radius_recursion,
)
from ucns.carrier import radius_from_breadth


def test_radius_is_canonical_radial_map_not_depth() -> None:
    base = 0.5
    for depth in (0, 1, 2, 3):
        record = build_radius_recursion(depth, base)
        assert record.radius == radius_from_breadth(base)
        assert record.schema == RADIUS_RECURSION_SCHEMA


def test_layers_are_deck_translations() -> None:
    for depth in (0, 1, 2):
        record = build_radius_recursion(depth, 1.0)
        expected_lifted = (depth * 2.0 * pi) % (4.0 * pi)
        assert isclose(record.lifted_angle, expected_lifted, abs_tol=1e-12)
        assert isclose(record.visible_angle, 0.0, abs_tol=1e-12)
        assert record.lifted_null is False


def test_two_laps_complete_return() -> None:
    zero = build_radius_recursion(0, 1.0)
    two = build_radius_recursion(2, 1.0)
    assert isclose(zero.lifted_angle, two.lifted_angle, abs_tol=1e-12)
    assert two.radius == zero.radius


def test_english_depth_is_not_a_radius() -> None:
    record = build_radius_recursion(3, 0.5)
    assert "superseded" in record.conclusion
    assert "deck-translation" in record.conclusion


def test_fails_closed() -> None:
    with pytest.raises(RadiusRecursionError):
        build_radius_recursion(-1, 1.0)
    with pytest.raises(RadiusRecursionError):
        build_radius_recursion(0, float("inf"))
    with pytest.raises(RadiusRecursionError):
        replay_radius_recursion(b"not json")

    record = build_radius_recursion(2, 1.0)
    replayed = replay_radius_recursion(record.receipt_bytes())
    assert replayed == record

    tampered = bytearray(record.receipt_bytes())
    tampered[20] ^= 0x01
    with pytest.raises(RadiusRecursionError):
        replay_radius_recursion(bytes(tampered))


def test_facade_exports_radius_recursion() -> None:
    import ucns

    assert hasattr(ucns, "build_radius_recursion")
    assert hasattr(ucns, "replay_radius_recursion")
    assert ucns.RADIUS_RECURSION_SCHEMA == RADIUS_RECURSION_SCHEMA
