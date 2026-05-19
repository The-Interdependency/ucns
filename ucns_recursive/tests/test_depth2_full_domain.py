"""
test_depth2_full_domain
========================
Compact closure sweep over the frozen depth-2 domain D':

    depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4

Status (v1.0 canon): the full frozen depth-2 domain is IMPLEMENTED +
TEST-BACKED in ``factor_search_v08``. It is **not** yet DEFENDED at the
formal-spec level, and this suite is **not** a literal exhaustive
enumeration of every payload assignment in D' (which is combinatorially
expensive). The suite combines hand-constructed edge cases with a
generated closure sweep over a compact basis family. It is the standing
TEST-BACKED witness for the depth-2 IMPLEMENTED claim, not a proof
substitute. See ``docs/ucns-spec-status-addendum-2026-05-16.md`` and
``ucns-spec.md`` §F2.

Target shape (for the closure-sweep cases):

    factor_search_v08(P) returns a factor pair
    iff
    P is sequence-composite in the swept slice of D'.

The current test suite checks:
1.  Every explicitly constructed composite P is recovered.
2.  Products of depth-1 × depth-1 objects are always composite.
3.  Recovered factors recompose exactly to P.
4.  No SEQ-PRIME is reported for a known composite.
5.  No spurious factor is reported for a known prime. A length-≥2
    flat object (e.g. (0, UNIT)(1, UNIT) F=[0, 0]) is seq-prime: the
    only candidate factorization uses a 1-cell face-flip element from
    the multiplicative unit group, which the engine filters via
    ``is_multiplicative_unit``. Identifying the full unit group (not
    just the identity) is what makes SEQ-PRIME a meaningful predicate.
"""

import unittest
from fractions import Fraction
from typing import Optional

from ucns_recursive.canonical import (
    UCNSObject,
    is_multiplicative_unit,
    is_unit,
    multiply,
)
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
    # Primality: only length-1 objects are seq-prime
    # ------------------------------------------------------------------

    def test_length1_object_is_prime(self) -> None:
        """A length-1 object cannot be factored into two non-unit objects."""
        obj = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
        result = factor_search_v08(obj, self.catalogue)
        self.assertEqual(result, "SEQ-PRIME", "Length-1 object must be SEQ-PRIME")

    def test_length2_flat_is_seq_prime(self) -> None:
        """A flat length-2 object with no payload is seq-prime.

        The only candidate factorization at p=1 uses a 1-cell face-flip
        element of the multiplicative unit group as one factor, with the
        XOR cancellation absorbed into the other factor. The engine's
        ``is_multiplicative_unit`` filter rejects this trivial split,
        leaving no non-degenerate (A, B) with A ⊠ B = obj. The object is
        therefore seq-prime.

        This is the primality boundary in the depth-1 verified domain:
        face-flip elements u = (0, UNIT) F=[1] satisfy u ⊠ u = identity
        and form the unit group together with the identity. Admitting
        them as factors would make every length-≥2 object composite,
        which would collapse SEQ-PRIME to a useless predicate.
        """
        obj = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        result = factor_search_v08(obj, self.catalogue)
        self.assertEqual(
            result, "SEQ-PRIME",
            "flat length-2 object must be seq-prime once the unit group is filtered",
        )

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
                if is_multiplicative_unit(A) or is_multiplicative_unit(B):
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
