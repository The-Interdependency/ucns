"""
test_failure_boundary_e109
===========================
Regression tests capturing the E10.9 failure boundary.

The E10.9 analysis identified the root cause of depth-2 failures:

    Primary failure stage: PAYLOAD QUOTIENT RECOVERY (recursive).
    Secondary failure:     Missing global witness consistency check.
    Root cause:            The old recursion treated S0_A as atomic even
                           when it is itself a depth-1 object (S2).

These tests verify that factor_search_v08 DOES NOT exhibit those failures.

Specifically:
1.  When S0_A = S2 and the target payload is multiply(S2, S2), the solver
    must recurse into the payload equation rather than doing an atomic
    equality check.
2.  The witness matrix must enforce global consistency (one assignment of
    all payload factors that explains every cell of P).
"""

import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject, multiply, is_unit
from ucns_recursive.factor_search_v08 import factor_search_v08
from ucns_recursive.witness_matrix import build_witness_matrix

UNIT = None


def make_S2() -> UCNSObject:
    return UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])


def make_S3() -> UCNSObject:
    # Angles [0, 2/3, 4/3]: evenly-spaced n_min=3 sequence (matches catalogue)
    return UCNSObject(
        3, 3,
        [(Fraction(0), UNIT), (Fraction(2, 3), UNIT), (Fraction(4, 3), UNIT)],
        [0, 0, 0],
    )


class TestFailureBoundaryE109(unittest.TestCase):
    """Regression: the E10.9 root cause must no longer reproduce."""

    def setUp(self) -> None:
        self.S2 = make_S2()

    def test_s2_squared_payload_recoverable(self) -> None:
        """The solver must recover a factor of (S2*S2) given S2 as one factor.

        Root cause regression: old code did equality check target == S0_A
        and failed for target = multiply(S2, S2).
        """
        S2 = self.S2
        target = multiply(S2, S2)
        # factor_search_v08 on target itself (it IS a product: S2 * S2)
        result = factor_search_v08(target)
        self.assertIsInstance(result, tuple, "multiply(S2, S2) must be seq-composite")
        rec_A, rec_B = result
        self.assertEqual(multiply(rec_A, rec_B), target)

    def test_witness_matrix_global_consistency(self) -> None:
        """The witness matrix must flag inconsistent payload assignments."""
        S2 = self.S2
        S2S2 = multiply(S2, S2)

        # Consistent assignment: S_A = [S2], S_B = [S2]
        S_A = [S2]
        S_B = [S2]
        P_payloads = [[S2S2]]
        wm_good = build_witness_matrix(S_A, S_B, P_payloads)
        self.assertTrue(wm_good.globally_consistent())

        # Inconsistent assignment: S_A = [S2], but wrong target
        wrong_target = S2  # multiply(S2, S2) != S2
        P_payloads_bad = [[wrong_target]]
        wm_bad = build_witness_matrix(S_A, S_B, P_payloads_bad)
        self.assertFalse(wm_bad.globally_consistent())

    def test_no_false_atomicity_on_depth1_payload(self) -> None:
        """Depth-1 payload objects must be descended into, not treated as atoms."""
        S2 = self.S2
        # Build a product whose payload grid requires multiply(S2, S2) = P_00
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        P = multiply(A, B)

        # P_payloads[0][0] = multiply(S2, S2) — the old code failed here
        # because it treated S2 as atomic instead of solving the sub-equation.
        result = factor_search_v08(P)
        self.assertIsInstance(
            result, tuple,
            "Solver must not treat S2 as atomic; depth-1 payloads must be descended into",
        )
        rec_A, rec_B = result
        self.assertEqual(multiply(rec_A, rec_B), P)

    def test_global_witness_required_for_all_cells(self) -> None:
        """Every cell of P must be explained by a single globally consistent
        payload assignment, not just the first row and column."""
        S2 = self.S2
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        P = multiply(A, B)

        result = factor_search_v08(P)
        self.assertIsInstance(result, tuple)
        rec_A, rec_B = result

        # Verify ALL four payload cells, not just (0,0)
        for k in range(2):
            for j in range(2):
                cell_payload = P.A_plus[k * 2 + j][1]
                expected = multiply(rec_A.A_plus[k][1], rec_B.A_plus[j][1])
                self.assertEqual(
                    expected, cell_payload,
                    f"Payload at cell ({k},{j}) must be globally consistent",
                )


if __name__ == "__main__":
    unittest.main()
