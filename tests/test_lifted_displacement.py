# === CHECKS ===
# id: check_lifted_displacement_sums_before_reduction
#   proves: lifted_displacement_sums_before_reduction
#   call: self::test_sums_before_reduction
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_lifted_displacement_preserves_visible_positions
#   proves: lifted_displacement_preserves_visible_positions
#   call: self::test_preserves_visible_positions
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_lifted_displacement_is_modular_orbit_equivariant
#   proves: lifted_displacement_is_modular_orbit_equivariant
#   call: self::test_is_modular_orbit_equivariant
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_lifted_displacement_fails_closed
#   proves: lifted_displacement_fails_closed
#   call: self::test_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_lifted_displacement_candidate
#   proves: geometry_public_surface_includes_lifted_displacement_candidate
#   call: self::test_facade_exports_lifted
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

from fractions import Fraction

import pytest

from ucns import (
    LiftedDisplacementError,
    build_lifted_displacement,
    native_mobius_state,
    replay_lifted_displacement,
)


def test_sums_before_reduction() -> None:
    record = build_lifted_displacement(100, 57, 0)
    assert record.total_turn == Fraction(157, 157)
    assert "reversed" in record.frame


def test_preserves_visible_positions() -> None:
    record = build_lifted_displacement(100, 57, 0)
    payload = record.as_dict()
    assert payload["visible_residues"] == {
        "ordinal": 100,
        "semantic": 57,
        "context": 0,
    }


def test_is_modular_orbit_equivariant() -> None:
    for a in (2, 3):
        for triple in ((7, 11, 13), (100, 57, 0)):
            acted = build_lifted_displacement(*(a * r for r in triple))
            expected = native_mobius_state().advance(Fraction(a * sum(triple), 157))
            assert acted.phase_turns == expected.phase_turns
            assert acted.frame == expected.frame.value


def test_fails_closed() -> None:
    with pytest.raises(LiftedDisplacementError):
        build_lifted_displacement(True, 0, 0)  # type: ignore[arg-type]
    with pytest.raises(LiftedDisplacementError):
        build_lifted_displacement(1, 0, 0, covering_degree=157)

    record = build_lifted_displacement(10, 20, 30)
    replayed = replay_lifted_displacement(record.receipt_bytes())
    assert replayed == record

    tampered = bytearray(record.receipt_bytes())
    tampered[30] ^= 0x01
    with pytest.raises(LiftedDisplacementError):
        replay_lifted_displacement(bytes(tampered))


def test_facade_exports_lifted() -> None:
    import ucns

    assert hasattr(ucns, "build_lifted_displacement")
    assert hasattr(ucns, "replay_lifted_displacement")
    assert ucns.LIFTED_DISPLACEMENT_SCHEMA == "ucns.lifted-displacement-candidate"
