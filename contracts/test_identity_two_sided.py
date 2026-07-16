# ratios: loc_comments=37:30 imports_exports=2:6 calls_definitions=32:6
"""O2 — multiply_identity: the normalized factorization identity is two-sided.

Witness for the CONTRACTS entry ``multiply_identity`` in
``ucns/canonical.py``.  Proof: ``docs/base-geometry.md`` §2.  Because ⊠
is non-commutative (O4), the two sides are checked separately.
"""

# === MODULE_BUILD ===
# id: multiply_identity
#   module_name: multiply_identity
#   module_kind: engine
#   summary: prove the normalized factorization identity is two-sided; do not conflate it with the public-gonol SPACE/ZERO twist origin
#   owner: Erin Spencer
#   public_surface: none
#   internal_surface: contract_multiply_identity, test_left_identity, test_right_identity, test_none_sentinel, test_unit_group_not_identity, test_mutation_caught
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_identity_two_sided
#   rollout: required for any monoid/group claim in O6
#   rollback: n/a
#   since: 2026-07-10
#   unresolved: bridge between the fixed-origin public gonol and ordinary normalized factorization objects remains hmmm
# === END MODULE_BUILD ===

from ucns.canonical import multiply

from contracts._harness import E, U1, make_rng, mutant_multiply_face_flip, rand_obj


def test_left_identity():
    rng = make_rng(10)
    for i in range(300):
        a = rand_obj(rng, rng.randint(1, 3))
        assert multiply(E, a) == a, f"sample {i}: e is not a LEFT identity"


def test_right_identity():
    rng = make_rng(11)
    for i in range(300):
        a = rand_obj(rng, rng.randint(1, 3))
        assert multiply(a, E) == a, f"sample {i}: e is not a RIGHT identity"


def test_none_sentinel():
    rng = make_rng(12)
    for i in range(100):
        a = rand_obj(rng, rng.randint(1, 3))
        assert multiply(None, a) == a, f"sample {i}: None sentinel left"
        assert multiply(a, None) == a, f"sample {i}: None sentinel right"


def test_unit_group_not_identity():
    """u1 (face-flipped unit) re-signs faces on both sides, so it is in
    the unit group but is NOT an identity; it is self-inverse."""
    rng = make_rng(13)
    for i in range(100):
        a = rand_obj(rng, rng.randint(1, 3))
        assert multiply(U1, a) != a, f"sample {i}: u1 acted as left identity"
        assert multiply(a, U1) != a, f"sample {i}: u1 acted as right identity"
    assert multiply(U1, U1) == E, "u1 must be self-inverse"


def test_mutation_caught():
    """[mutation-verified]: a face-law mutant (extra XOR 1) makes the
    normalized factorization identity fail, and the identity witness detects it."""
    rng = make_rng(14)
    a = rand_obj(rng, 2)
    assert (
        mutant_multiply_face_flip(E, a) != a
        or mutant_multiply_face_flip(a, E) != a
    ), "face-flip mutant was not caught"


def contract_multiply_identity():
    """test-build aggregate entry point for obligation O2."""
    test_left_identity()
    test_right_identity()
    test_none_sentinel()
    test_unit_group_not_identity()
    test_mutation_caught()
# ratios: loc_comments=37:30 imports_exports=2:6 calls_definitions=32:6
