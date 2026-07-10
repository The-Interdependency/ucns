# ratios: loc_comments=200:67 imports_exports=8:10 calls_definitions=141:12
"""O5 — division_theory: left/right quotient existence + multiplicity.

Witness for the CONTRACTS entry ``division_theory`` in
``ucns/division_theory.py``.  Proof: ``docs/base-geometry.md`` §5.

This obligation also carries the 2026-07-10 scope correction to the
v0.6 Left-Quotient Completeness theorem: the greedy ``left_quotient``
misses solvable payload-absorption-ambiguous instances (the theorem
depended on E10.4 cancellativity, which is false in general).  The
counterexample is a permanent regression here, together with the proof
that the ``division_theory`` enumerators close the gap.
"""

# === MODULE_BUILD ===
# id: division_theory
#   module_name: division_theory
#   module_kind: engine
#   summary: left/right quotient solvability and multiplicity for multiply
#   owner: Erin Spencer
#   public_surface: none
#   internal_surface: contract_division_theory, test_enumerator_exhaustive_universe, test_soundness_random, test_length_gate, test_multiplicity_towers, test_flat_divisor_cancellativity, test_cancellativity_dichotomy, test_v06_scope_correction, test_greedy_left_quotient_still_sound, test_mutation_caught
#   auth_boundary: none
#   storage_boundary: read
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_quotient_solvability
#   rollout: this IS "division and the like"
#   rollback: keep left_factors as standing hmmm
#   since: 2026-07-10
#   unresolved: AlignedComplete-domain cancellativity proof remains a formal/ obligation; canonical-choice procedure among multiple quotients remains open (structural, per O6)
# === END MODULE_BUILD ===

import os
from fractions import Fraction

from ucns.canonical import UCNSObject, multiply
from ucns.division_theory import left_quotients, right_quotients
from ucns.left_quotient import left_quotient

from contracts._harness import E, make_rng, rand_obj, tower

# The full 78x78 sweep costs minutes; CI runs a deterministic 25% stride.
# Set UCNS_EXHAUSTIVE=1 for the full 6,084-pair audit sweep.
_EXHAUSTIVE = os.environ.get("UCNS_EXHAUSTIVE") == "1"


def _closed_universe():
    """78 objects closed enough to exercise every payload-merge branch:
    lengths 1-2, angles {0, 2}, faces {0, 1}, payloads {None, e, T2}."""
    payloads = [None, E, tower(2)]
    universe = []
    for payload in payloads:
        for face in (0, 1):
            universe.append(
                UCNSObject(4, 1, [(Fraction(0), payload)], [face])
            )
    for angle in (Fraction(0), Fraction(2)):
        for p0 in payloads:
            for p1 in payloads:
                for f0 in (0, 1):
                    for f1 in (0, 1):
                        universe.append(
                            UCNSObject(
                                4, 1,
                                [(Fraction(0), p0), (angle, p1)],
                                [f0, f1],
                            )
                        )
    return universe


def test_enumerator_exhaustive_universe():
    """Completeness + soundness over the closed universe: x is among
    left_quotients(a⊠x, a) and every returned solution verifies; dually
    for right_quotients.  Full 6,084-pair sweep (verified 2026-07-10)
    with UCNS_EXHAUSTIVE=1; the CI default is a deterministic stride
    sample of the same universe."""
    universe = _closed_universe()
    for i, a in enumerate(universe):
        for j, x in enumerate(universe):
            if not _EXHAUSTIVE and (i + j) % 4 != 0:
                continue
            b = multiply(a, x)
            left = left_quotients(b, a)
            assert any(g is not None and g == x for g in left), (
                "left enumerator missed a known solution"
            )
            for g in left:
                assert multiply(a, g) == b, "left enumerator unsound"
            right = right_quotients(b, x)
            assert any(g is not None and g == a for g in right), (
                "right enumerator missed a known solution"
            )
            for g in right:
                assert multiply(g, x) == b, "right enumerator unsound"


def test_soundness_random():
    rng = make_rng(40)
    for i in range(200):
        a = rand_obj(rng, rng.randint(1, 2), 2)
        x = rand_obj(rng, rng.randint(1, 2), 2)
        b = multiply(a, x)
        left = left_quotients(b, a)
        assert any(g is not None and g == x for g in left), f"pair {i}: miss"
        for g in left:
            assert multiply(a, g) == b, f"pair {i}: unsound"


def test_length_gate():
    """Existence is gated by the degree valuation: len(a) must divide
    len(b) (r(x) = r(b) - r(a) is forced), so division is PARTIAL."""
    rng = make_rng(41)
    checked = 0
    for _ in range(300):
        a = rand_obj(rng, 1, 3)
        b = rand_obj(rng, 1, 3)
        if len(b.A_plus) % len(a.A_plus) == 0:
            continue
        assert left_quotients(b, a) == [], "length gate violated (left)"
        assert right_quotients(b, a) == [], "length gate violated (right)"
        checked += 1
    assert checked > 0, "gate never exercised"


def test_multiplicity_towers():
    """Quotients are structurally non-unique: T_d ⊠ x = T_d has exactly
    d solutions {e, T_2, ..., T_d}.  ALT-FACTOR multiplicity is a
    property of the problem, not a solver defect."""
    towers = {1: E}
    for d in (2, 3, 4):
        towers[d] = tower(d)
    for d in (1, 2, 3, 4):
        solutions = left_quotients(towers[d], towers[d])
        assert len(solutions) == d, (
            f"T_{d}: expected {d} solutions, got {len(solutions)}"
        )
    # the same witness kills left AND right cancellativity
    t3, t2 = towers[3], towers[2]
    assert multiply(t3, t2) == multiply(t3, t3) and t2 != t3
    assert multiply(t2, t3) == multiply(t3, t3) and t2 != t3


def test_flat_divisor_cancellativity():
    """Uniqueness is restored on flat divisors: left/right
    multiplication by a depth-1 object is injective
    (docs/base-geometry.md §5.3) — which is why the v0.5.1 empirical
    regression at depths 0-1 saw zero violations."""
    rng = make_rng(42)
    for i in range(400):
        a = rand_obj(rng, 1, 3)
        x = rand_obj(rng, rng.randint(1, 2), 2)
        y = rand_obj(rng, rng.randint(1, 2), 2)
        if x == y:
            continue
        assert multiply(a, x) != multiply(a, y), (
            f"sample {i}: flat left cancellativity violated"
        )
        assert multiply(x, a) != multiply(y, a), (
            f"sample {i}: flat right cancellativity violated"
        )


def test_cancellativity_dichotomy():
    """Theorem 5.5: a divisor cancels iff some top-level payload is the
    unit.  (⇐) unit-payload divisors have singleton fibers; (⇒) an
    all-payloads-present divisor collides on X = [(0, e, 0)] vs Y = e."""
    rng = make_rng(44)
    e_payload = UCNSObject(1, 1, [(Fraction(0), E)], [0])
    checked_none = checked_full = 0
    for _ in range(200):
        a = rand_obj(rng, 2, 3)
        b = rand_obj(rng, rng.randint(1, 2), 2)
        if any(p is None for _, p in a.A_plus):
            left_fiber = left_quotients(multiply(a, b), a)
            assert len(left_fiber) == 1 and left_fiber[0] == b, (
                "unit-payload divisor left fiber is not the singleton {b}"
            )
            right_fiber = right_quotients(multiply(b, a), a)
            assert len(right_fiber) == 1 and right_fiber[0] == b, (
                "unit-payload divisor right fiber is not the singleton {b}"
            )
            checked_none += 1
        else:
            assert multiply(a, e_payload) == multiply(a, E), (
                "all-payloads-present divisor failed the e/None left witness"
            )
            assert multiply(e_payload, a) == multiply(E, a), (
                "all-payloads-present divisor failed the e/None right witness"
            )
            checked_full += 1
    assert checked_none > 0 and checked_full > 0, "dichotomy sides not both hit"


def test_v06_scope_correction():
    """Permanent regression for the v0.6 greedy-era counterexample.

    The pre-v1.0 greedy ``left_quotient`` returned None on this
    solvable instance (its E10.4 cancellativity premise is false).
    Since codex-handoff/04 the singular function is a selector over the
    complete solution set, so it must now RECOVER the missed solution —
    and the plural API must contain it."""
    a = UCNSObject(4, 1, [(Fraction(0), E), (Fraction(2), None)], [0, 0])
    b = UCNSObject(1, 1, [(Fraction(0), E)], [0])
    p = multiply(a, b)
    assert p != a, "counterexample degenerated"
    recovered = left_quotient(p, a)
    assert recovered is not None and multiply(a, recovered) == p, (
        "compatibility selector regressed to the greedy miss"
    )
    solutions = left_quotients(p, a)
    assert any(g is not None and g == b for g in solutions), (
        "enumerator failed to recover the missed solution"
    )


def test_greedy_left_quotient_still_sound():
    """The greedy primitive remains sound: whatever it returns verifies."""
    rng = make_rng(43)
    for i in range(200):
        a = rand_obj(rng, rng.randint(1, 2), 2)
        x = rand_obj(rng, rng.randint(1, 2), 2)
        b = multiply(a, x)
        got = left_quotient(b, a)
        if got is not None:
            assert multiply(a, got) == b, f"pair {i}: greedy unsound"


def test_mutation_caught():
    """[mutation-verified], against the witnessed module itself: an
    enumerator mutant that recovers payloads from row 0 only — skipping
    the cross-row intersection of Theorem 5.2 — emits an unsound
    candidate on the absorption witness, and the soundness law catches
    it.  (The final in-module verification is a guard expected never to
    fire; the intersection is the load-bearing step, so that is what
    the mutant removes.)  The greedy primitive's phase-3 dependence is
    pinned separately on a host-inconsistent input."""
    from itertools import product as iproduct

    from ucns.division_theory import _left_payload_solutions

    def mutant_left_quotients_row0(target_p, divisor):
        rows, total = len(divisor.A_plus), len(target_p.A_plus)
        assert rows and total % rows == 0
        q = total // rows
        x_angles = [angle for angle, _ in target_p.A_plus[:q]]
        x_faces = [f ^ divisor.F_plus[0] for f in target_p.F_plus[:q]]
        columns = [
            _left_payload_solutions(
                divisor.A_plus[0][1], target_p.A_plus[j][1], 1000
            )
            for j in range(q)
        ]
        return [
            UCNSObject(target_p.n_dec, 1,
                       list(zip(x_angles, list(choice))), x_faces)
            for choice in iproduct(*columns)
        ]

    a = UCNSObject(4, 1, [(Fraction(0), E), (Fraction(2), None)], [0, 0])
    b = UCNSObject(1, 1, [(Fraction(0), E)], [0])
    p = multiply(a, b)
    mutant_solutions = mutant_left_quotients_row0(p, a)
    assert any(multiply(a, g) != p for g in mutant_solutions), (
        "row-0-only enumerator mutant was not caught by the soundness law"
    )
    real = left_quotients(p, a)
    assert real and all(multiply(a, g) == p for g in real), (
        "real enumerator must return exactly the sound set on this input"
    )

    # greedy primitive: phase-3 verification is load-bearing there
    p_bad = UCNSObject(
        24, 1,
        [(Fraction(0), None), (Fraction(1), None),
         (Fraction(1), None), (Fraction(3), None)],
        [0, 0, 0, 0],
    )
    a_bad = UCNSObject(24, 1, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
    assert left_quotient(p_bad, a_bad) is None, "real solver must reject"
    assert left_quotients(p_bad, a_bad) == [], "enumerator must reject"
    q = 2
    mutant_candidate = UCNSObject(
        p_bad.n_dec, 1,
        [(x, payload) for x, payload in p_bad.A_plus[:q]],
        [f ^ a_bad.F_plus[0] for f in p_bad.F_plus[:q]],
    )
    assert multiply(a_bad, mutant_candidate) != p_bad, (
        "verification-skipping greedy mutant was not caught"
    )


def contract_division_theory():
    """test-build aggregate entry point for obligation O5."""
    test_enumerator_exhaustive_universe()
    test_soundness_random()
    test_length_gate()
    test_multiplicity_towers()
    test_flat_divisor_cancellativity()
    test_cancellativity_dichotomy()
    test_v06_scope_correction()
    test_greedy_left_quotient_still_sound()
    test_mutation_caught()
# ratios: loc_comments=200:67 imports_exports=8:10 calls_definitions=141:12
