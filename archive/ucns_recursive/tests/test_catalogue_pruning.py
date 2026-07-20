"""
Tests for the Carrier-LCM Law and carrier-support catalogue pruning.

Three layers:

1. The Law itself, as a property test on this substrate (``ucns_recursive``):
   n_min(multiply(A, B)) == lcm(n_min(A), n_min(B)) for normalized operands.
   This is the bridging witness tying the per-sublattice finiteness work
   (witnessed previously on the edcmbone ``ucns_v04`` substrate) to the
   canonical recursive engine in this repository.

2. Pruning soundness: pruning never removes an actual factor of P.

3. Search equivalence: factor_search_v08 over the pruned catalogue returns
   results equivalent to the unpruned search (factorization found both
   ways and exactly recomposing, or SEQ_PRIME both ways).
"""

import random
import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject, lcm, multiply
from ucns_recursive.catalogue_pruning import (
    carrier_lcm,
    prime_support,
    prune_catalogue,
)
from ucns_recursive.domains import generate_payload_catalogue
from ucns_recursive.factor_search_v08 import SEQ_PRIME, factor_search_v08

DENOMS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15]


def _rand_obj(rng: random.Random, depth: int) -> UCNSObject:
    length = rng.randint(1, 3)
    cells = []
    for _ in range(length):
        d = rng.choice(DENOMS)
        ang = Fraction(rng.randint(0, 4 * d - 1), d)
        payload = (
            _rand_obj(rng, depth - 1)
            if (depth > 0 and rng.random() < 0.6)
            else None
        )
        cells.append((ang, payload))
    n_min = 1
    for a, _ in cells:
        frac = (a % 2) / 2
        if frac != 0:
            n_min = lcm(n_min, frac.denominator)
    n_dec = n_min * rng.randint(1, 3)
    faces = [rng.randint(0, 1) for _ in range(length)]
    return UCNSObject(n_dec, n_min, cells, faces)


class TestPrimeSupport(unittest.TestCase):
    def test_basic_supports(self):
        self.assertEqual(prime_support(1), set())
        self.assertEqual(prime_support(2), {2})
        self.assertEqual(prime_support(12), {2, 3})
        self.assertEqual(prime_support(40), {2, 5})
        self.assertEqual(prime_support(53), {53})

    def test_rejects_nonpositive(self):
        with self.assertRaises(ValueError):
            prime_support(0)


class TestCarrierLcmLaw(unittest.TestCase):
    """Property test: the Carrier-LCM Law holds on this substrate."""

    TRIALS = 2000

    def test_law_exact_equality(self):
        rng = random.Random(53)
        for i in range(self.TRIALS):
            A = _rand_obj(rng, rng.randint(0, 2))
            B = _rand_obj(rng, rng.randint(0, 2))
            P = multiply(A, B)
            with self.subTest(trial=i):
                self.assertEqual(
                    P.n_min,
                    lcm(A.n_min, B.n_min),
                    msg=f"Law violated: {A.n_min}, {B.n_min} -> {P.n_min}",
                )
                self.assertEqual(P.n_min, carrier_lcm(A, B))

    def test_law_with_unit(self):
        rng = random.Random(7)
        for _ in range(100):
            A = _rand_obj(rng, 1)
            self.assertEqual(carrier_lcm(A, None), A.n_min)
            self.assertEqual(carrier_lcm(None, A), A.n_min)
        self.assertEqual(carrier_lcm(None, None), 1)


class TestPruningSoundness(unittest.TestCase):
    """Pruning never removes a candidate that is an actual factor."""

    def test_factor_carriers_survive(self):
        rng = random.Random(11)
        for i in range(500):
            A = _rand_obj(rng, rng.randint(0, 1))
            B = _rand_obj(rng, rng.randint(0, 1))
            P = multiply(A, B)
            kept = prune_catalogue(P, [None, A, B])
            with self.subTest(trial=i):
                self.assertIn(None, kept)
                self.assertTrue(any(c is A for c in kept))
                self.assertTrue(any(c is B for c in kept))

    def test_escaping_candidate_removed(self):
        # P with carrier 3; a candidate with carrier 5 cannot be a factor.
        P = UCNSObject(
            6, 3,
            [(Fraction(0), None), (Fraction(2, 3), None)],
            [0, 0],
        )
        c5 = UCNSObject(
            10, 5,
            [(Fraction(0), None), (Fraction(2, 5), None)],
            [0, 0],
        )
        kept = prune_catalogue(P, [None, c5])
        self.assertEqual(len(kept), 1)
        self.assertIsNone(kept[0])


class TestSearchEquivalence(unittest.TestCase):
    """factor_search_v08 over the pruned oracle catalogue is equivalent
    to the unpruned search on the frozen depth-2 domain."""

    def _equivalent(self, P, full, pruned):
        r_full = factor_search_v08(P, catalogue=full)
        r_pruned = factor_search_v08(P, catalogue=pruned)
        if r_full is SEQ_PRIME or r_pruned is SEQ_PRIME:
            self.assertIs(r_full, SEQ_PRIME)
            self.assertIs(r_pruned, SEQ_PRIME)
            return
        A_f, B_f = r_full
        A_p, B_p = r_pruned
        self.assertEqual(multiply(A_f, B_f), P)
        self.assertEqual(multiply(A_p, B_p), P)

    def test_equivalence_on_constructed_products(self):
        full = generate_payload_catalogue()
        atoms = [c for c in full if c is not None]
        rng = random.Random(29)
        for i in range(40):
            A = rng.choice(atoms)
            B = rng.choice(atoms)
            P = multiply(A, B)
            pruned = prune_catalogue(P, full)
            with self.subTest(trial=i, kept=len(pruned), total=len(full)):
                self.assertLessEqual(len(pruned), len(full))
                self._equivalent(P, full, pruned)

    def test_equivalence_on_prime_objects(self):
        full = generate_payload_catalogue()
        # An object engineered to be sequence-prime in the frozen domain:
        P = UCNSObject(
            8, 4,
            [(Fraction(0), None), (Fraction(1, 2), None),
             (Fraction(3, 2), None)],
            [1, 0, 0],
        )
        pruned = prune_catalogue(P, full)
        self._equivalent(P, full, pruned)


if __name__ == "__main__":
    unittest.main()


class TestPayloadPruning(unittest.TestCase):
    """Corollary 2: payload-catalogue pruning soundness + default-on
    equivalence in factor_search_v08."""

    def test_factor_payloads_survive(self):
        from ucns_recursive.catalogue_pruning import prune_payload_catalogue
        rng = random.Random(37)
        for i in range(300):
            A = _rand_obj(rng, 1)
            B = _rand_obj(rng, 1)
            P = multiply(A, B)
            payloads = [pl for _, pl in A.A_plus if pl is not None]
            payloads += [pl for _, pl in B.A_plus if pl is not None]
            kept = prune_payload_catalogue(P, [None] + payloads)
            with self.subTest(trial=i):
                self.assertIn(None, kept)
                for pl in payloads:
                    self.assertTrue(any(c is pl for c in kept))

    def test_host_rule_would_be_unsound_here(self):
        # Witness for the §4 warning: host n_min misses payload primes.
        from ucns_recursive.catalogue_pruning import (
            payload_support,
            prime_support,
        )
        inner = UCNSObject(
            10, 5, [(Fraction(0), None), (Fraction(2, 5), None)], [0, 0]
        )
        host = UCNSObject(
            6, 3,
            [(Fraction(0), inner), (Fraction(2, 3), None)],
            [0, 0],
        )
        self.assertNotIn(5, prime_support(host.n_min))
        self.assertIn(5, payload_support(host))

    def test_search_equivalence_prune_on_off(self):
        full = generate_payload_catalogue()
        atoms = [c for c in full if c is not None]
        rng = random.Random(41)
        for i in range(40):
            P = multiply(rng.choice(atoms), rng.choice(atoms))
            r_on = factor_search_v08(P, catalogue=full, prune=True)
            r_off = factor_search_v08(P, catalogue=full, prune=False)
            with self.subTest(trial=i):
                if r_on is SEQ_PRIME or r_off is SEQ_PRIME:
                    self.assertIs(r_on, SEQ_PRIME)
                    self.assertIs(r_off, SEQ_PRIME)
                else:
                    self.assertEqual(multiply(*r_on), P)
                    self.assertEqual(multiply(*r_off), P)

    def test_all_unit_payload_edge(self):
        from ucns_recursive.catalogue_pruning import prune_payload_catalogue
        P = UCNSObject(
            4, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 1]
        )
        full = generate_payload_catalogue()
        kept = prune_payload_catalogue(P, full)
        self.assertIn(None, kept)
        for c in kept:
            if c is not None:
                self.assertEqual(c.n_min, 1)
        r = factor_search_v08(P, catalogue=full)
        if r is not SEQ_PRIME:
            self.assertEqual(multiply(*r), P)
