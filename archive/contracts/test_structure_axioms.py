# ratios: loc_comments=85:48 imports_exports=4:8 calls_definitions=80:8
"""O6 — structure_naming: the capstone axiom bundle.

Witness for the CONTRACTS entry ``structure_naming`` in
``ucns/canonical.py``.  Theorem: ``docs/base-geometry.md`` §6.

The earned name: (nonempty normalized UCNS objects, ⊠, e) is a
NON-COMMUTATIVE, NON-CANCELLATIVE MONOID, GRADED BY LENGTH over
(ℕ≥1, ×) — equivalently, the degree valuation r = log(len) is additive
— with unit group of order 2 and center exactly the unit towers.  It is
not a group, not a groupoid, not embeddable in a group, and carries no
primitive addition (O7), so "number system" remains aspirational.
"""

# === MODULE_BUILD ===
# id: structure_naming
#   module_name: structure_theorem
#   module_kind: engine
#   summary: name the algebraic object (UCNS, multiply) given O1-O5 and the r-grading
#   owner: Erin Spencer
#   public_surface: none
#   internal_surface: contract_structure_naming, test_monoid_axioms, test_grading, test_unit_group_is_z2, test_not_cancellative, test_center_sample, test_idempotents_exist, test_mutation_caught
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_structure_axioms
#   rollout: base geometry complete == this theorem lands
#   rollback: n/a
#   requires: multiply_well_defined, multiply_identity, multiply_associativity, multiply_commutativity_ruling, division_theory
#   since: 2026-07-10
#   unresolved: none
# === END MODULE_BUILD ===

import math

from ucns.canonical import (
    is_multiplicative_unit,
    multiply,
)
from ucns.geometry_bridge import ucns_a_to_g

from contracts._harness import (
    E,
    U1,
    flat,
    make_rng,
    mutant_multiply_dedup,
    rand_obj,
    tower,
)


def test_monoid_axioms():
    """Closure + associativity + two-sided identity on one sample."""
    rng = make_rng(50)
    for _ in range(100):
        a = rand_obj(rng, rng.randint(1, 3))
        b = rand_obj(rng, rng.randint(1, 3))
        c = rand_obj(rng, rng.randint(1, 3))
        assert multiply(multiply(a, b), c) == multiply(a, multiply(b, c))
        assert multiply(E, a) == a and multiply(a, E) == a


def test_grading():
    """len is a monoid homomorphism to (N>=1, x); r = log len additive."""
    rng = make_rng(51)
    for _ in range(200):
        a = rand_obj(rng, rng.randint(1, 3))
        b = rand_obj(rng, rng.randint(1, 3))
        p = multiply(a, b)
        assert len(p.A_plus) == len(a.A_plus) * len(b.A_plus)
        assert (
            abs(ucns_a_to_g(p).r - (ucns_a_to_g(a).r + ucns_a_to_g(b).r))
            < 1e-9
        )


def test_unit_group_is_z2():
    """Within a probe family covering units, towers, and length-2
    objects, exactly e and u1 are invertible; both satisfy the
    is_multiplicative_unit predicate and u1^2 = e."""
    probes = [
        E, U1, tower(2), tower(2, [1, 1]),
        flat([(0, 0), (1, 0)]), flat([(0, 0), (2, 0)]),
        flat([(0, 0), (1, 0), (2, 0), (3, 0)]),
    ]
    invertible = []
    for u in probes:
        for v in probes:
            if multiply(u, v) == E and multiply(v, u) == E:
                invertible.append(u)
                break
    assert len(invertible) == 2, f"unit probe found {len(invertible)} units"
    assert all(
        is_multiplicative_unit(u) and len(u.A_plus) == 1 for u in invertible
    )
    assert multiply(U1, U1) == E


def test_not_cancellative():
    """The tower witness kills cancellativity on BOTH sides, so the
    monoid does not embed in a group and quotients are multivalued."""
    t3, t2 = tower(3), tower(2)
    assert multiply(t3, t2) == multiply(t3, t3) and t2 != t3
    assert multiply(t2, t3) == multiply(t3, t3) and t2 != t3


def test_center_sample():
    """Center = unit towers (proof in docs/base-geometry.md §4.3):
    towers commute with everything; the witnesses B1/B2 separate
    longer objects."""
    rng = make_rng(52)
    b1 = flat([(0, 0), (1, 0)])
    b2 = flat([(0, 0), (2, 0)])
    for _ in range(100):
        a = rand_obj(rng, rng.randint(1, 3))
        t = tower(rng.randint(1, 3))
        assert multiply(t, a) == multiply(a, t)
        if len(a.A_plus) >= 2:
            assert (
                multiply(a, b1) != multiply(b1, a)
                or multiply(a, b2) != multiply(b2, a)
            )


def test_idempotents_exist():
    """All-zero-face towers are non-identity idempotents — impossible in
    a group, characteristic of the absorption-driven monoid."""
    t3 = tower(3)
    assert multiply(t3, t3) == t3 and t3 != E


def test_mutation_caught():
    """[mutation-verified]: a cell-deduplicating product breaks the
    grading (len 4 -> 3 on the witness), and the grading witness
    catches it."""
    w = flat([(0, 0), (2, 0)])
    assert len(mutant_multiply_dedup(w, w).A_plus) != 4, (
        "dedup mutant was not caught"
    )
    assert math.isclose(
        ucns_a_to_g(multiply(w, w)).r, 2 * ucns_a_to_g(w).r
    )


def contract_structure_naming():
    """test-build aggregate entry point for obligation O6."""
    test_monoid_axioms()
    test_grading()
    test_unit_group_is_z2()
    test_not_cancellative()
    test_center_sample()
    test_idempotents_exist()
    test_mutation_caught()
# ratios: loc_comments=85:48 imports_exports=4:8 calls_definitions=80:8
