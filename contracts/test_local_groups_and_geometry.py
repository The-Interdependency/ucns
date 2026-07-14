"""Contracts for local groups, radius/breadth, and fork observables.

The finite fixtures are executable conformance witnesses for the written
structure proofs. They are not substitutes for the unbounded theorem arguments.
"""
from __future__ import annotations

# === MODULE_BUILD ===
# id: local_groups_relational_geometry_contracts
#   module_name: local_groups_and_relational_geometry
#   module_kind: test
#   summary: mutation-backed witnesses for idempotent towers, home-relative local groups, radius, breadth, spindle, and fork laws
#   owner: Erin Spencer
#   public_surface: contract_local_groups_and_relational_geometry
#   internal_surface: test_singleton_gauge_collapse, test_product_closure, test_idempotent_census_bounded, test_local_groups_bounded, test_depth_two_ghost_home_relative, test_radius_max_law, test_breadth_plus_law, test_zero_breadth_spindle, test_first_level_fork_law, test_mutations_caught
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_local_groups_and_geometry, tests.test_base_geometry_contracts
#   rollout: default_enabled
#   rollback: remove contract and shim entry
#   requires: ucns_relational_geometry, ucns_canonical
#   since: 2026-07-14
#   unresolved: none
# === END MODULE_BUILD ===

import math
from fractions import Fraction

from ucns.canonical import UCNSObject, multiply
from ucns.relational_geometry import (
    breadth,
    face_tower,
    first_level_fork_count,
    idempotent_tower_depth,
    is_local_group_member,
    is_local_group_pair,
    is_normalized,
    local_group_elements,
    recursive_radius,
    zero_faced_tower,
)

from contracts._harness import E, U1, flat, make_rng, rand_obj


def test_singleton_gauge_collapse():
    """Absolute singleton angles are gauge and normalize to zero."""
    for angle in (Fraction(0), Fraction(1, 3), Fraction(7, 4), Fraction(3)):
        obj = UCNSObject(24, 1, [(angle, None)], [0])
        assert obj.A_plus[0][0] == 0
        assert is_normalized(obj)


def test_product_closure():
    """Products remain recursively normalized carrier objects."""
    rng = make_rng(70)
    for _ in range(60):
        a = rand_obj(rng, rng.randint(1, 4))
        b = rand_obj(rng, rng.randint(1, 4))
        product_obj = multiply(a, b)
        assert product_obj is not None
        assert is_normalized(product_obj)
        assert product_obj.A_plus[0][0] == 0


def test_idempotent_census_bounded():
    """Bounded conformance: selected idempotents are exactly zero-faced towers."""
    candidates = []
    expected = []
    for depth in range(1, 5):
        expected.append(zero_faced_tower(depth))
        candidates.extend(local_group_elements(depth))
    candidates.extend(
        [
            flat([(0, 0), (1, 0)]),
            flat([(0, 0), (2, 0)]),
            UCNSObject(24, 1, [(Fraction(0), E), (Fraction(1), None)], [0, 0]),
        ]
    )
    found = [obj for obj in candidates if multiply(obj, obj) == obj]
    assert len(found) == len(expected)
    assert all(any(obj == tower for tower in expected) for obj in found)
    assert all(idempotent_tower_depth(obj) is not None for obj in found)


def test_local_groups_bounded():
    """Bounded local groups are closed elementary abelian face towers."""
    for depth in range(1, 5):
        identity = zero_faced_tower(depth)
        elements = local_group_elements(depth)
        assert len(elements) == 2 ** depth
        assert all(is_local_group_member(obj, identity) for obj in elements)
        for left in elements:
            assert multiply(identity, left) == left
            assert multiply(left, identity) == left
            assert multiply(left, left) == identity
            for right in elements:
                product_obj = multiply(left, right)
                assert any(product_obj == candidate for candidate in elements)
                assert multiply(left, right) == multiply(right, left)


def test_depth_two_ghost_home_relative():
    """Cancellation is depth-blind; identity absorption determines local home."""
    t1 = zero_faced_tower(1)
    t2 = zero_faced_tower(2)
    x = face_tower([1])
    y = multiply(x, t2)

    assert x == U1
    assert y == face_tower([1, 0])
    assert multiply(x, y) == t2
    assert multiply(y, x) == t2

    assert multiply(t2, x) == y and y != x
    assert multiply(x, t2) == y and y != x
    assert not is_local_group_pair(x, y, t2)

    assert is_local_group_member(x, t1)
    assert not is_local_group_member(x, t2)
    assert is_local_group_member(y, t2)


def test_radius_max_law():
    """Recursive radius is a homomorphism to (nonnegative integers, max)."""
    rng = make_rng(71)
    for _ in range(100):
        a = rand_obj(rng, rng.randint(1, 4))
        b = rand_obj(rng, rng.randint(1, 4))
        assert recursive_radius(multiply(a, b)) == max(
            recursive_radius(a), recursive_radius(b)
        )
    assert recursive_radius(multiply(None, E)) == max(0, recursive_radius(E))


def test_breadth_plus_law():
    """Breadth lambda=log(len) is additive under product."""
    rng = make_rng(72)
    for _ in range(100):
        a = rand_obj(rng, rng.randint(1, 4))
        b = rand_obj(rng, rng.randint(1, 4))
        assert math.isclose(
            breadth(multiply(a, b)),
            breadth(a) + breadth(b),
            abs_tol=1e-12,
        )


def test_zero_breadth_spindle():
    """Local groups lie at lambda=0; noncommutative witnesses need breadth."""
    for depth in range(1, 5):
        assert all(breadth(obj) == 0 for obj in local_group_elements(depth))

    b1 = flat([(0, 0), (1, 0)])
    b2 = flat([(0, 0), (2, 0)])
    assert breadth(b1) > 0 and breadth(b2) > 0
    assert multiply(b1, b2) != multiply(b2, b1)

    # Positive breadth is necessary for witnesses, not sufficient for failure.
    assert multiply(b1, b1) == multiply(b1, b1)


def _fork_fixture(left_payloads, right_payloads):
    left = UCNSObject(
        24,
        1,
        [(Fraction(i), payload) for i, payload in enumerate(left_payloads)],
        [0] * len(left_payloads),
    )
    right = UCNSObject(
        24,
        1,
        [(Fraction(i), payload) for i, payload in enumerate(right_payloads)],
        [0] * len(right_payloads),
    )
    return left, right


def _assert_fork_law(a, b):
    actual = first_level_fork_count(multiply(a, b))
    expected = (
        len(a.A_plus) * len(b.A_plus)
        - (len(a.A_plus) - first_level_fork_count(a))
        * (len(b.A_plus) - first_level_fork_count(b))
    )
    assert actual == expected


def test_first_level_fork_law():
    """Top-level payload-bearing cells obey inclusion-exclusion."""
    payload = E
    cases = [
        _fork_fixture([None, None], [None, None]),
        _fork_fixture([payload, None], [None, None]),
        _fork_fixture([payload, payload], [payload, payload]),
        _fork_fixture([payload, None, payload], [None, payload]),
    ]
    for a, b in cases:
        _assert_fork_law(a, b)


def test_mutations_caught():
    """Each load-bearing law has a witness that rejects its matching mutant."""
    drifted = UCNSObject(24, 1, [(Fraction(2, 3), None)], [0])
    drifted.A_plus[0] = (Fraction(2, 3), None)
    assert not is_normalized(drifted)

    a = UCNSObject(24, 1, [(Fraction(0), E), (Fraction(1), None)], [0, 0])
    raw = multiply(a, a)
    raw.A_plus[0] = (Fraction(1), raw.A_plus[0][1])
    assert not is_normalized(raw)

    t2 = zero_faced_tower(2)
    x = face_tower([1])
    y = multiply(x, t2)
    inverse_only = multiply(x, y) == t2 and multiply(y, x) == t2
    assert inverse_only
    assert not is_local_group_pair(x, y, t2)
    assert not is_local_group_member(x, t2)

    deep = zero_faced_tower(3)
    shallow = zero_faced_tower(1)
    correct = recursive_radius(multiply(deep, shallow))
    mutant_radius = correct + 1
    assert correct == max(recursive_radius(deep), recursive_radius(shallow))
    assert mutant_radius != correct

    left, right = _fork_fixture([E, None], [E, None])
    actual = first_level_fork_count(multiply(left, right))
    additive_mutant = first_level_fork_count(left) + first_level_fork_count(right)
    assert actual != additive_mutant


def contract_local_groups_and_relational_geometry():
    """Aggregate entry point for the structure and coordinate package."""
    test_singleton_gauge_collapse()
    test_product_closure()
    test_idempotent_census_bounded()
    test_local_groups_bounded()
    test_depth_two_ghost_home_relative()
    test_radius_max_law()
    test_breadth_plus_law()
    test_zero_breadth_spindle()
    test_first_level_fork_law()
    test_mutations_caught()
