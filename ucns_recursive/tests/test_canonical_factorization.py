"""
Tests for canonical factor selection (T1.2).

Layers:

1. Validity: every enumerated/selected pair exactly recomposes P.
2. Determinism: the canonical choice is invariant under catalogue
   permutation, duplication, and pruning on/off.
3. Completeness parity: the store-free enumerator agrees with
   UCNSStore.factor_decompose (under include_trivial=True) on the same
   catalogue.
4. Semantics: nontriviality filtering matches factor_search_v08's
   convention; unit-only products report SEQ_PRIME by default.
5. Key totality: canonical_key separates non-equal pairs and agrees on
   equal ones.
"""

import random
import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject, multiply
from ucns_recursive.canonical_factorization import (
    canonical_factorization,
    canonical_key,
    enumerate_factorizations,
)
from ucns_recursive.domains import generate_payload_catalogue
from ucns_recursive.factor_search_v08 import SEQ_PRIME, is_multiplicative_unit
from ucns_recursive.store import UCNSStore


def _atoms():
    return [c for c in generate_payload_catalogue() if c is not None]


class TestValidity(unittest.TestCase):
    def test_every_enumerated_pair_recomposes(self):
        cat = generate_payload_catalogue()
        atoms = _atoms()
        rng = random.Random(17)
        for i in range(60):
            P = multiply(rng.choice(atoms), rng.choice(atoms))
            for A, B in enumerate_factorizations(P, cat):
                with self.subTest(trial=i):
                    self.assertEqual(multiply(A, B), P)
                    self.assertFalse(is_multiplicative_unit(A))
                    self.assertFalse(is_multiplicative_unit(B))

    def test_selected_pair_recomposes(self):
        cat = generate_payload_catalogue()
        atoms = _atoms()
        rng = random.Random(19)
        found = 0
        for _ in range(60):
            P = multiply(rng.choice(atoms), rng.choice(atoms))
            r = canonical_factorization(P, cat)
            if r is not SEQ_PRIME:
                found += 1
                self.assertEqual(multiply(*r), P)
        self.assertGreater(found, 0)


class TestDeterminism(unittest.TestCase):
    def test_invariant_under_catalogue_permutation_and_duplication(self):
        cat = generate_payload_catalogue()
        atoms = _atoms()
        rng = random.Random(23)
        for i in range(30):
            P = multiply(rng.choice(atoms), rng.choice(atoms))
            base = canonical_factorization(P, cat)
            shuffled = list(cat)
            rng.shuffle(shuffled)
            doubled = shuffled + list(reversed(cat))
            with self.subTest(trial=i):
                for variant in (shuffled, doubled):
                    r = canonical_factorization(P, variant)
                    if base is SEQ_PRIME:
                        self.assertIs(r, SEQ_PRIME)
                    else:
                        self.assertEqual(canonical_key(r), canonical_key(base))

    def test_invariant_under_pruning(self):
        cat = generate_payload_catalogue()
        atoms = _atoms()
        rng = random.Random(29)
        for i in range(30):
            P = multiply(rng.choice(atoms), rng.choice(atoms))
            with_prune = list(enumerate_factorizations(P, cat, prune=True))
            without = list(enumerate_factorizations(P, cat, prune=False))
            with self.subTest(trial=i):
                self.assertEqual(
                    sorted(map(canonical_key, with_prune)),
                    sorted(map(canonical_key, without)),
                )


class TestFactorDecomposeParity(unittest.TestCase):
    def test_matches_store_enumeration_with_trivial_included(self):
        cat = generate_payload_catalogue()
        atoms = _atoms()
        rng = random.Random(31)
        store = UCNSStore()
        for i in range(25):
            P = multiply(rng.choice(atoms), rng.choice(atoms))
            # insert() encodes raw data; inject the object directly since
            # this test exercises factor_decompose's enumeration, not encoding.
            store._objects[("P", i)] = P
            store_pairs = store.factor_decompose(("P", i), atoms)
            free_pairs = list(
                enumerate_factorizations(
                    P, cat, include_trivial=True, prune=False
                )
            )
            with self.subTest(trial=i):
                self.assertEqual(
                    sorted(map(canonical_key, store_pairs)),
                    sorted(map(canonical_key, free_pairs)),
                )


class TestSemantics(unittest.TestCase):
    def test_unit_only_product_is_seq_prime_by_default(self):
        cat = generate_payload_catalogue()
        unit_like = UCNSObject(2, 1, [(Fraction(0), None)], [0])
        self.assertTrue(is_multiplicative_unit(unit_like))
        nontrivial = UCNSObject(
            4, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 1]
        )
        P = multiply(nontrivial, unit_like)
        self.assertIs(canonical_factorization(P, cat), SEQ_PRIME)
        r = canonical_factorization(P, cat, include_trivial=True)
        self.assertIsInstance(r, tuple)
        self.assertEqual(multiply(*r), P)

    def test_canonical_key_total_and_equality_respecting(self):
        a = UCNSObject(4, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
        b = UCNSObject(4, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
        c = UCNSObject(4, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 1])
        self.assertEqual(a, b)
        self.assertEqual(canonical_key((a, a)), canonical_key((b, b)))
        self.assertNotEqual(a, c)
        self.assertNotEqual(canonical_key((a, a)), canonical_key((c, c)))


if __name__ == "__main__":
    unittest.main()
