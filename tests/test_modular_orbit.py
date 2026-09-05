# === CHECKS ===
# id: check_modular_orbit_mod9_times_two
#   proves: modular_orbit_action_decomposes_exact_permutation, modular_orbit_circle_embedding_is_exact
#   call: self::test_mod9_times_two_decomposes_expected_orbits
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_modular_orbit_mod9_times_seven
#   proves: modular_orbit_action_decomposes_exact_permutation
#   call: self::test_mod9_times_seven_decomposes_expected_orbits
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_modular_orbit_fails_closed
#   proves: modular_orbit_fails_closed_outside_permutation_boundary
#   call: self::test_invalid_carriers_fail_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_modular_orbit_semantic_boundary
#   proves: modular_orbit_carries_geometry_not_domain_semantics
#   call: self::test_serialized_surface_contains_geometry_only
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from fractions import Fraction

import pytest

from ucns.modular_orbit import ModularOrbitError, build_modular_orbit_geometry


def test_mod9_times_two_decomposes_expected_orbits() -> None:
    geometry = build_modular_orbit_geometry(9, 2, range(1, 9))

    assert geometry.positions == (1, 2, 3, 4, 5, 6, 7, 8)
    assert geometry.orbits == ((1, 2, 4, 8, 7, 5), (3, 6))
    assert geometry.periods == (6, 2)
    assert geometry.target(7) == 5
    assert geometry.turn_of(1) == Fraction(1, 9)
    assert geometry.turn_of(8) == Fraction(8, 9)

    full = build_modular_orbit_geometry(9, 2)
    assert full.orbits == ((0,), (1, 2, 4, 8, 7, 5), (3, 6))


def test_mod9_times_seven_decomposes_expected_orbits() -> None:
    geometry = build_modular_orbit_geometry(9, 7, range(1, 9))

    assert geometry.orbits == ((1, 7, 4), (2, 5, 8), (3,), (6,))
    assert geometry.periods == (3, 3, 1, 1)


def test_invalid_carriers_fail_closed() -> None:
    with pytest.raises(ModularOrbitError):
        build_modular_orbit_geometry(1, 2)
    with pytest.raises(ModularOrbitError):
        build_modular_orbit_geometry(9, 2, ())
    with pytest.raises(ModularOrbitError):
        build_modular_orbit_geometry(9, 2, (1, 1))
    with pytest.raises(ModularOrbitError):
        build_modular_orbit_geometry(9, 2, (1, 2, 4))
    with pytest.raises(ModularOrbitError):
        build_modular_orbit_geometry(9, 3)

    valid = build_modular_orbit_geometry(9, 2, range(1, 9))
    with pytest.raises(ModularOrbitError):
        type(valid)(
            modulus=valid.modulus,
            multiplier=valid.multiplier,
            positions=valid.positions,
            action=valid.action,
            orbits=valid.orbits,
            periods=(99, 99),
            embedding=valid.embedding,
        )


def test_serialized_surface_contains_geometry_only() -> None:
    payload = build_modular_orbit_geometry(9, 2, range(1, 9)).as_dict()

    assert set(payload) == {
        "modulus",
        "multiplier",
        "positions",
        "action",
        "orbits",
        "periods",
        "embedding",
    }
    assert payload["embedding"][0] == {
        "residue": 1,
        "turn": {"numerator": 1, "denominator": 9},
    }
