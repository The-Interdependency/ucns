# ratios: loc_comments=60:41 imports_exports=4:7 calls_definitions=50:7
"""O4 — multiply_commutativity_ruling.

Witness for the CONTRACTS entry ``multiply_commutativity_ruling`` in
``ucns/canonical.py``.  Proof: ``docs/base-geometry.md`` §4.

Ruling (corrects the handoff's guess): ⊠ is non-commutative in general,
but the commutator does NOT live in the chirality bits — the (z, w)
composition rule z(A⊠B) = z_A·w_B + w_A·z_B (mod 2) is symmetric, and
the whole (r, θ, z, w) projection always commutes.  The commutator
lives in the SEQUENCE ORDERING (row-major vs column-major interleaving,
and payload order at depth).  The commuting subclass (the center) is
exactly the unit towers: nested length-1 objects with arbitrary face
bits.
"""

# === MODULE_BUILD ===
# id: multiply_commutativity_ruling
#   module_name: commutativity_ruling
#   module_kind: experiment
#   summary: prove non-commutative in general; characterize the commuting subclass
#   owner: Erin Spencer
#   public_surface: none
#   internal_surface: contract_multiply_commutativity_ruling, test_noncommutative_witness, test_projection_always_commutes, test_towers_are_central, test_long_objects_not_central, test_nontower_payload_not_central, test_mutation_caught
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_commutator
#   rollout: fixes whether O5 needs left AND right division (it does)
#   rollback: n/a
#   since: 2026-07-10
#   unresolved: none - ruling landed: commutator lives in sequence ordering, not chirality
# === END MODULE_BUILD ===

from fractions import Fraction

from ucns.canonical import UCNSObject, multiply
from ucns.geometry_bridge import ucns_a_to_g

from contracts._harness import (
    flat,
    geo_eq,
    make_rng,
    mutant_multiply_sorted,
    rand_obj,
    tower,
)

B1 = flat([(0, 0), (1, 0)])
B2 = flat([(0, 0), (2, 0)])


def test_noncommutative_witness():
    assert multiply(B1, B2) != multiply(B2, B1), (
        "witness pair unexpectedly commutes"
    )


def test_projection_always_commutes():
    """(r, θ, z, w) of A⊠B equals that of B⊠A for every pair: the
    geometry is blind to the commutator."""
    rng = make_rng(30)
    for i in range(400):
        a = rand_obj(rng, rng.randint(1, 3))
        b = rand_obj(rng, rng.randint(1, 3))
        assert geo_eq(
            ucns_a_to_g(multiply(a, b)), ucns_a_to_g(multiply(b, a))
        ), f"pair {i}: projection failed to commute"


def test_towers_are_central():
    rng = make_rng(31)
    for i in range(200):
        a = rand_obj(rng, rng.randint(1, 3))
        depth = rng.randint(1, 3)
        t = tower(depth, [rng.randint(0, 1) for _ in range(depth)])
        assert multiply(t, a) == multiply(a, t), (
            f"sample {i}: tower failed to commute"
        )


def test_long_objects_not_central():
    """Any object of length >= 2 is separated from the center by B1 or
    B2 (two-witness separation, docs/base-geometry.md §4.3)."""
    rng = make_rng(32)
    for i in range(300):
        a = rand_obj(rng, rng.randint(1, 3))
        if len(a.A_plus) < 2:
            continue
        separated = (
            multiply(a, B1) != multiply(B1, a)
            or multiply(a, B2) != multiply(B2, a)
        )
        assert separated, f"sample {i}: length>=2 object not separated"


def test_nontower_payload_not_central():
    """Length-1 objects whose payload is not central are not central."""
    non_tower = UCNSObject(24, 1, [(Fraction(0), B1)], [0])
    probes = [B1, B2, UCNSObject(24, 1, [(Fraction(0), B2)], [0])]
    assert any(
        multiply(non_tower, p) != multiply(p, non_tower) for p in probes
    ), "non-tower-payload object behaved centrally"


def test_mutation_caught():
    """[mutation-verified]: a product that re-sorts its cells erases the
    commutator, making the witness pair commute — detected."""
    assert mutant_multiply_sorted(B1, B2) == mutant_multiply_sorted(B2, B1), (
        "sorted mutant was not caught"
    )


def contract_multiply_commutativity_ruling():
    """test-build aggregate entry point for obligation O4."""
    test_noncommutative_witness()
    test_projection_always_commutes()
    test_towers_are_central()
    test_long_objects_not_central()
    test_nontower_payload_not_central()
    test_mutation_caught()
# ratios: loc_comments=60:41 imports_exports=4:7 calls_definitions=50:7
