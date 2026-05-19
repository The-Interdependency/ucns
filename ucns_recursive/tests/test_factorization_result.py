"""
Tests for A0-facing factorization result envelopes.
"""

import unittest
from fractions import Fraction

from ucns_recursive import (
    FactorizationResultKind,
    UCNSObject,
    UNIT,
    factorization_result,
    multiply,
    stable_hash,
)
from ucns_recursive.domains import S2


class TestFactorizationResultEnvelope(unittest.TestCase):
    def test_composite_product_returns_factors_with_product_hash(self):
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        P = multiply(A, B)

        result = factorization_result(P)

        self.assertEqual(result.result_kind, FactorizationResultKind.FACTORS)
        self.assertTrue(result.has_factors)
        self.assertEqual(result.product_hash, stable_hash(P))
        self.assertEqual(result.claim_scope, "composite-found")
        rec_A, rec_B = result.factors
        self.assertEqual(multiply(rec_A, rec_B), P)

    def test_seq_prime_length1_in_verified_domain_is_absolute_with_scope(self):
        """Length-1 is the defended seq-prime example.

        Length-2 flat objects are now composite via the one-cell face-flip
        factorization path; see test_depth2_full_domain for the standing
        regression. This envelope test therefore uses the length-1 object
        when it needs an absolute SEQ-PRIME result.
        """
        P = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])

        result = factorization_result(P)

        self.assertEqual(result.result_kind, FactorizationResultKind.SEQ_PRIME)
        self.assertFalse(result.has_factors)
        self.assertEqual(result.product_domain_label, "depth-1")
        self.assertTrue(result.seq_prime_is_absolute)
        self.assertFalse(result.requires_scope)
        self.assertEqual(result.claim_scope, "defended-domain-relative")

    def test_length2_flat_is_composite_not_seq_prime(self):
        """A flat length-2 object should not be treated as seq-prime."""
        P = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])

        result = factorization_result(P)

        self.assertEqual(result.result_kind, FactorizationResultKind.FACTORS)
        self.assertTrue(result.has_factors)
        rec_A, rec_B = result.factors
        self.assertEqual(multiply(rec_A, rec_B), P)
        self.assertFalse(result.seq_prime_is_absolute)
        self.assertEqual(result.claim_scope, "composite-found")

    def test_seq_prime_in_frontier_domain_is_non_absolute(self):
        depth2_payload = UCNSObject(
            2,
            2,
            [(Fraction(0), S2), (Fraction(1), UNIT)],
            [0, 0],
        )
        P = UCNSObject(
            2,
            2,
            [(Fraction(0), depth2_payload), (Fraction(1), UNIT)],
            [0, 0],
        )

        result = factorization_result(P, catalogue=[UNIT])

        self.assertEqual(result.result_kind, FactorizationResultKind.SEQ_PRIME)
        self.assertFalse(result.has_factors)
        self.assertEqual(result.product_domain_label, "depth-3+")
        self.assertFalse(result.seq_prime_is_absolute)
        self.assertTrue(result.requires_scope)
        self.assertEqual(result.claim_scope, "experimental-non-absolute")


if __name__ == "__main__":
    unittest.main()
