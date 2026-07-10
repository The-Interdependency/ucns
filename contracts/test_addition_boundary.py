# ratios: loc_comments=58:42 imports_exports=3:7 calls_definitions=59:7
"""O7 — addition_boundary: is there a primitive addition?

Witness for the CONTRACTS entry ``addition_boundary`` in
``ucns/canonical.py``.  Ruling: ``docs/base-geometry.md`` §7.

RULING: ⊠ is the sole primitive.  Radial growth is emergent — the
degree valuation r = log(len) is additive under ⊠ itself, so "addition
of degrees" is already realized multiplicatively and no second
primitive is required.  The only natural derived candidate, top-level
sequence concatenation ⊕, is associative and RIGHT-distributive over ⊠
but fails LEFT distributivity (row interleaving vs block order), so it
earns at most a right-near-semiring role and is NOT adopted into the
v1.0 operation set.  The base geometry's operation set closes as:
⊠, its partial multivalued left/right division, the identity, and the
order-2 unit group.
"""

# === MODULE_BUILD ===
# id: addition_boundary
#   module_name: addition_boundary
#   module_kind: experiment
#   summary: rule whether a primitive addition exists or radial growth stays derived
#   owner: Erin Spencer
#   public_surface: none
#   internal_surface: contract_addition_boundary, test_r_additive_under_multiply, test_concat_is_associative, test_concat_right_distributive, test_concat_left_distributivity_fails, test_concat_noncommutative, test_mutation_caught
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_addition_boundary
#   rollout: sets the full operation set for the base geometry
#   rollback: n/a
#   since: 2026-07-10
#   unresolved: none - ruled: no second primitive; concatenation stays derived
# === END MODULE_BUILD ===

from ucns.canonical import multiply
from ucns.geometry_bridge import ucns_a_to_g

from contracts._harness import (
    E,
    U1,
    concat,
    flat,
    make_rng,
    mutant_concat_gauge_drift,
    rand_obj,
)


def test_r_additive_under_multiply():
    """Radial growth needs no second operation: r adds under ⊠ alone."""
    rng = make_rng(60)
    for _ in range(200):
        a = rand_obj(rng, rng.randint(1, 3))
        b = rand_obj(rng, rng.randint(1, 3))
        assert (
            abs(
                ucns_a_to_g(multiply(a, b)).r
                - (ucns_a_to_g(a).r + ucns_a_to_g(b).r)
            )
            < 1e-9
        )


def test_concat_is_associative():
    rng = make_rng(61)
    for _ in range(200):
        a = rand_obj(rng, rng.randint(1, 2), 2)
        b = rand_obj(rng, rng.randint(1, 2), 2)
        c = rand_obj(rng, rng.randint(1, 2), 2)
        assert concat(concat(a, b), c) == concat(a, concat(b, c))


def test_concat_right_distributive():
    """(b ⊕ c) ⊠ a == (b ⊠ a) ⊕ (c ⊠ a): block order is preserved."""
    rng = make_rng(62)
    for i in range(200):
        a = rand_obj(rng, rng.randint(1, 2), 2)
        b = rand_obj(rng, rng.randint(1, 2), 2)
        c = rand_obj(rng, rng.randint(1, 2), 2)
        assert multiply(concat(b, c), a) == concat(
            multiply(b, a), multiply(c, a)
        ), f"sample {i}: right distributivity failed"


def test_concat_left_distributivity_fails():
    """a ⊠ (b ⊕ c) interleaves rows while (a⊠b) ⊕ (a⊠c) blocks them, so
    ⊕ is not a two-sided distributive addition."""
    a = flat([(0, 0), (1, 0)])
    assert multiply(a, concat(E, U1)) != concat(
        multiply(a, E), multiply(a, U1)
    )


def test_concat_noncommutative():
    assert concat(E, U1) != concat(U1, E)


def test_mutation_caught():
    """[mutation-verified]: a gauge-drifting concatenation breaks right
    distributivity on a concrete witness — detected."""
    a = flat([(0, 0), (3, 1)])
    b = flat([(0, 0), (1, 0)])
    c = flat([(0, 0), (2, 0)])
    assert multiply(mutant_concat_gauge_drift(b, c), a) != mutant_concat_gauge_drift(
        multiply(b, a), multiply(c, a)
    ), "gauge-drift mutant was not caught"


def contract_addition_boundary():
    """test-build aggregate entry point for obligation O7."""
    test_r_additive_under_multiply()
    test_concat_is_associative()
    test_concat_right_distributive()
    test_concat_left_distributivity_fails()
    test_concat_noncommutative()
    test_mutation_caught()
# ratios: loc_comments=58:42 imports_exports=3:7 calls_definitions=59:7
