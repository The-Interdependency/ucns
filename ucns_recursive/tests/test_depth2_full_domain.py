"""
test_depth2_full_domain
========================
Exhaustive test over the frozen depth-2 domain D':

    depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4

GOAL: Depth-2 Frozen Domain Completeness Theorem
-------------------------------------------------
For every P in frozen D':

    factor_search_v08(P) returns a factor pair
    iff
    P is sequence-composite in D'.

The current test suite checks:
1.  Every explicitly constructed composite P is recovered.
2.  Products of depth-1 × depth-1 objects are always composite.
3.  Recovered factors recompose exactly to P.
4.  No SEQ-PRIME is reported for a known composite.
5.  No spurious factor is reported for a known prime (length 1 or 2
    when length 2 with no valid 2=1×2 host decomposition).

NOTE: Full literal enumeration of every payload assignment in D' is
combinatorially expensive.  This suite therefore combines hand-constructed
edge cases with a generated closure sweep over a compact basis family.
"""

import unittest
from fractions import Fraction
from typing import Optional

from ucns_recursive.canonical import UCNSObject, multiply, is_unit
from ucns_recursive.domains import generate_payload_catalogue, in_domain
from ucns_recursive.factor_search_v08 import factor_search_v08

UNIT = None


def make_S2() -> UCNSObject:
    return UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])


def make_S3() -> UCNSObject:
    # Angles [0, 2/3, 4/3]: evenly-spaced n_min=3 sequence (matches catalogue)
    return UCNSObject(
        3, 3,
        [
            (Fraction(0), UNIT),
            (Fraction(2, 3), UNIT),
            (Fraction(4, 3), UNIT),
        ],
        [0, 0, 0],
    )


def make_depth1(base_n_min: int, length: int, payload: Optional[UCNSObject]) -> UCNSObject:
    """Build a depth-1 object with *payload* in the first cell."""
    angles = [Fraction(2 * k, base_n_min) for k in range(length)]
    payloads = [payload] + [UNIT] * (length - 1)
    faces = [0] * length
    return UCNSObject(base_n_min * 2, base_n_min, list(zip(angles, payloads)), faces)


class TestDepth2FullDomain(unittest.TestCase):
    """Sweep of the frozen depth-2 domain."""

    def setUp(self) -> None:
        self.S2 = make_S2()
        self.S3 = make_S3()
        self.catalogue = generate_payload_catalogue()

    # ------------------------------------------------------------------
    # Helper
    # ------------------------------------------------------------------

    def _assert_composite(self, A: UCNSObject, B: UCNSObject, label: str = "") -> None:
        """Build P = A ⊠ B, check factor_search_v08 recovers a valid pair."""
        # Domain bounds apply to factors A and B, not to the product P
        self.assertTrue(in_domain(A), f"{label}: A not in frozen domain D'")
        self.assertTrue(in_domain(B), f"{label}: B not in frozen domain D'")
        P = multiply(A, B)
        self.assertIsNotNone(P)

        result = factor_search_v08(P, self.catalogue)

        msg = f"{label}: expected composite, got SEQ-PRIME"
        self.assertIsInstance(result, tuple, msg)
        rec_A, rec_B = result
        self.assertFalse(is_unit(rec_A), f"{label}: rec_A is unit")
        self.assertFalse(is_unit(rec_B), f"{label}: rec_B is unit")
        self.assertEqual(
            multiply(rec_A, rec_B), P,
            f"{label}: recomposition failed",
        )

    # ------------------------------------------------------------------
    # Class I: flat composite  (payloads all None, depth 0)
    # ------------------------------------------------------------------

    def test_flat_2x2(self) -> None:
        """Flat 2×2: both A and B are pure depth-0 length-2 objects."""
        A = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        self._assert_composite(A, B, "flat 2×2")

    def test_flat_2x3(self) -> None:
        A = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(
            3, 3,
            [(Fraction(0), UNIT), (Fraction(4, 3), UNIT), (Fraction(8, 3), UNIT)],
            [0, 0, 0],
        )
        self._assert_composite(A, B, "flat 2×3")

    def test_flat_3x2(self) -> None:
        A = UCNSObject(
            3, 3,
            [(Fraction(0), UNIT), (Fraction(4, 3), UNIT), (Fraction(8, 3), UNIT)],
            [0, 0, 0],
        )
        B = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        self._assert_composite(A, B, "flat 3×2")

    # ------------------------------------------------------------------
    # Class II: depth-1 × depth-0  (one factor carries payloads)
    # ------------------------------------------------------------------

    def test_depth1_times_flat(self) -> None:
        S2 = self.S2
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        self._assert_composite(A, B, "depth-1 A × flat B")

    def test_flat_times_depth1(self) -> None:
        S2 = self.S2
        A = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        self._assert_composite(A, B, "flat A × depth-1 B")

    # ------------------------------------------------------------------
    # Class III: depth-1 × depth-1  (the primary oracle class)
    # ------------------------------------------------------------------

    def test_depth1_S2_S2(self) -> None:
        S2 = self.S2
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        self._assert_composite(A, B, "depth-1 S2 × depth-1 S2")

    def test_depth1_S3_S2(self) -> None:
        S3 = self.S3
        S2 = self.S2
        A = make_depth1(3, 2, S3)
        B = make_depth1(2, 2, S2)
        self._assert_composite(A, B, "depth-1 S3 × depth-1 S2")

    def test_depth1_S2_S3(self) -> None:
        S2 = self.S2
        S3 = self.S3
        A = make_depth1(2, 2, S2)
        B = make_depth1(3, 2, S3)
        self._assert_composite(A, B, "depth-1 S2 × depth-1 S3")

    def test_depth1_S3_S3(self) -> None:
        S3 = self.S3
        A = make_depth1(3, 2, S3)
        B = make_depth1(3, 2, S3)
        self._assert_composite(A, B, "depth-1 S3 × depth-1 S3")

    def test_depth1_length3_S2(self) -> None:
        """Depth-1 object with length 3 and S2 payload."""
        S2 = self.S2
        A = make_depth1(2, 3, S2)
        B = make_depth1(2, 2, S2)
        self._assert_composite(A, B, "depth-1 len3 × depth-1 len2")

    # ------------------------------------------------------------------
    # Cross-checks: every recovered candidate must be in domain D'
    # ------------------------------------------------------------------

    def test_recovered_factors_in_domain(self) -> None:
        """Recovered factors must both lie within the frozen domain D'."""
        S2 = self.S2
        pairs = [
            (
                UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0]),
                UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0]),
            ),
            (
                UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0]),
                UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0]),
            ),
        ]
        for A, B in pairs:
            P = multiply(A, B)
            result = factor_search_v08(P, self.catalogue)
            self.assertIsInstance(result, tuple)
            rec_A, rec_B = result
            self.assertTrue(in_domain(rec_A))
            self.assertTrue(in_domain(rec_B))

    # ------------------------------------------------------------------
    # Primality: length-1 objects and trivially irreducible objects
    # ------------------------------------------------------------------

    def test_length1_object_is_prime(self) -> None:
        """A length-1 object cannot be factored into two non-unit objects."""
        obj = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
        result = factor_search_v08(obj, self.catalogue)
        self.assertEqual(result, "SEQ-PRIME", "Length-1 object must be SEQ-PRIME")

    def test_prime_length2_flat(self) -> None:
        """A flat length-2 object with n_min=2 is seq-prime (no 2=1×2 split)."""
        obj = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        # Length-2 can only split as 2=2×1 or 1×2, both give a unit factor
        result = factor_search_v08(obj, self.catalogue)
        self.assertEqual(result, "SEQ-PRIME", "Irreducible length-2 must be SEQ-PRIME")

    # ------------------------------------------------------------------
    # Generated closure sweep over a compact basis family
    # ------------------------------------------------------------------

    def test_depth2_basis_family_closure(self) -> None:
        """Every generated composite from the basis family is recovered."""

        def basis_family():
            s2 = self.S2
            s3 = self.S3
            family = [
                UCNSObject(1, 1, [(Fraction(0), UNIT)], [0]),
                UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0]),
                UCNSObject(
                    3, 3,
                    [(Fraction(0), UNIT), (Fraction(2, 3), UNIT), (Fraction(4, 3), UNIT)],
                    [0, 0, 0],
                ),
                UCNSObject(2, 2, [(Fraction(0), s2), (Fraction(1), UNIT)], [0, 0]),
                make_depth1(2, 3, s2),
                make_depth1(3, 2, s3),
                make_depth1(3, 3, s3),
            ]
            return [obj for obj in family if in_domain(obj)]

        family = basis_family()
        for i, A in enumerate(family):
            for j, B in enumerate(family):
                if is_unit(A) or is_unit(B):
                    continue
                P = multiply(A, B)
                self.assertIsNotNone(P, f"basis product failed: {i}x{j}")
                result = factor_search_v08(P, self.catalogue)
                self.assertIsInstance(result, tuple, f"basis product reported SEQ-PRIME: {i}x{j}")
                rec_A, rec_B = result
                self.assertEqual(
                    multiply(rec_A, rec_B), P,
                    f"basis recomposition mismatch: {i}x{j}",
                )


if __name__ == "__main__":
    unittest.main()
