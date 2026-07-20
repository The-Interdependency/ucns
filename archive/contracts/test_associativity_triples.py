# ratios: loc_comments=42:46 imports_exports=3:5 calls_definitions=40:5
"""O3 — multiply_associativity: (a⊠b)⊠c == a⊠(b⊠c), over TRIPLES.

Witness for the CONTRACTS entry ``multiply_associativity`` in
``ucns/canonical.py``.  Proof: ``docs/base-geometry.md`` §3.

Resolution of the handoff's open question ("does the theta payload
carry the resultant vector, not just the angle"): the UCNS object
carries its FULL angle sequence — all p·q product angles — so nothing
is collapsed to a circular mean inside the algebra.  The collapse
happens only in the geometry_bridge projection.  Associativity of ⊠
therefore reduces to entrywise associativity of exact angle addition
mod 4, XOR, and the payload merge — all proved.  The mean-collapse
failure mode is real, and the mutant below exhibits it: an operation
that combines angles by circular mean IS non-associative and the
triples witness catches it.
"""

# === MODULE_BUILD ===
# id: multiply_associativity
#   module_name: multiply_associativity
#   module_kind: experiment
#   summary: prove or bound (a x b) x c = a x (b x c)
#   owner: Erin Spencer
#   public_surface: none
#   internal_surface: contract_multiply_associativity, test_random_triples, test_adversarial_triples, test_full_sequence_carried, test_mutation_caught
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_associativity_triples
#   rollout: gates every structure name in O6 (monoid requires it)
#   rollback: keep as open
#   since: 2026-07-10
#   unresolved: none - resolved: the payload carries the full angle sequence; mean-collapse exists only in the projection
# === END MODULE_BUILD ===

from fractions import Fraction

from ucns.canonical import UCNSObject, multiply

from contracts._harness import (
    E,
    U1,
    flat,
    make_rng,
    mutant_multiply_mean_angle,
    rand_obj,
    tower,
)


def test_random_triples():
    """400 mixed-depth random TRIPLES (the prior 500+ evidence base was
    binary pairs only; this is the missing test set)."""
    rng = make_rng(20)
    for i in range(400):
        a = rand_obj(rng, rng.randint(1, 3))
        b = rand_obj(rng, rng.randint(1, 3))
        c = rand_obj(rng, rng.randint(1, 3))
        assert multiply(multiply(a, b), c) == multiply(a, multiply(b, c)), (
            f"triple {i}: associativity violated"
        )


def test_adversarial_triples():
    """Exhaustive triples over the adversarial family: identities,
    unit-group elements, towers (absorption-prone payloads), and a
    degenerate-theta object whose circular mean is undefined."""
    degenerate = flat([(0, 0), (1, 0), (2, 0), (3, 0)])
    family = [E, U1, tower(2), tower(3), tower(3, [1, 0, 1]), degenerate]
    for a in family:
        for b in family:
            for c in family:
                assert multiply(multiply(a, b), c) == multiply(
                    a, multiply(b, c)
                ), "adversarial associativity violated"


def test_full_sequence_carried():
    """The algebra never collapses to the mean: a product of length-4
    degenerate-theta objects keeps all 16 cells."""
    degenerate = flat([(0, 0), (1, 0), (2, 0), (3, 0)])
    assert len(multiply(degenerate, degenerate).A_plus) == 16


def test_mutation_caught():
    """[mutation-verified]: combining angles by circular mean (the
    collapsed-theta failure mode) breaks associativity on a concrete
    triple, and the triples witness catches it."""
    a = UCNSObject(24, 1, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
    b = UCNSObject(24, 1, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
    c = UCNSObject(24, 1, [(Fraction(0), None), (Fraction(2), None)], [0, 0])
    lhs = mutant_multiply_mean_angle(mutant_multiply_mean_angle(a, b), c)
    rhs = mutant_multiply_mean_angle(a, mutant_multiply_mean_angle(b, c))
    assert lhs != rhs, "mean-angle mutant was not caught"


def contract_multiply_associativity():
    """test-build aggregate entry point for obligation O3."""
    test_random_triples()
    test_adversarial_triples()
    test_full_sequence_carried()
    test_mutation_caught()
# ratios: loc_comments=42:46 imports_exports=3:5 calls_definitions=40:5
