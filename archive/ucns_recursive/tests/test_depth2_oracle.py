"""
test_depth2_oracle
==================
Formal restricted completeness test for the smallest depth-2 oracle.

THEOREM (v0.8.1 — Depth-2 Oracle Completeness)
Let O be the smallest depth-2 oracle:
    A = UCNSObject with payload S2 at position 0  (depth-1)
    B = UCNSObject with payload S2 at position 0  (depth-1)
    P = A ⊠ B

Then factor_search_v08(P) returns (A', B') with multiply(A', B') == P,
and A', B' are both non-unit.

This oracle must remain GREEN.
"""

import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject, multiply, is_unit
from ucns_recursive.factor_search_v08 import factor_search_v08

UNIT = None


def make_S2() -> UCNSObject:
    return UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])


class TestDepth2Oracle(unittest.TestCase):
    def setUp(self) -> None:
        self.S2 = make_S2()

    def test_oracle_A_eq_B_S2_payload(self) -> None:
        """Standard oracle: A = B = (S2, unit) host at depth-1."""
        S2 = self.S2
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        P = multiply(A, B)
        self.assertIsNotNone(P)

        result = factor_search_v08(P)

        self.assertIsInstance(result, tuple, "Oracle must return a factor pair")
        rec_A, rec_B = result
        self.assertFalse(is_unit(rec_A), "A factor must not be unit")
        self.assertFalse(is_unit(rec_B), "B factor must not be unit")
        self.assertEqual(multiply(rec_A, rec_B), P, "Recomposition must equal P")

    def test_oracle_product_is_composite(self) -> None:
        """factor_search_v08 must not report the oracle product as SEQ-PRIME."""
        S2 = self.S2
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        P = multiply(A, B)

        result = factor_search_v08(P)
        self.assertNotEqual(result, "SEQ-PRIME", "Oracle product is not SEQ-PRIME")

    def test_recomposition_roundtrip(self) -> None:
        """The recovered factors must recompose to exactly P."""
        S2 = self.S2
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        P = multiply(A, B)

        result = factor_search_v08(P)
        self.assertIsInstance(result, tuple)
        rec_A, rec_B = result
        self.assertEqual(multiply(rec_A, rec_B), P)

    def test_oracle_asymmetric_payloads(self) -> None:
        """Oracle variant: A has S2 payload, B has unit payload only."""
        S2 = self.S2
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        P = multiply(A, B)

        result = factor_search_v08(P)
        self.assertIsInstance(result, tuple)
        rec_A, rec_B = result
        self.assertEqual(multiply(rec_A, rec_B), P)


if __name__ == "__main__":
    unittest.main()
