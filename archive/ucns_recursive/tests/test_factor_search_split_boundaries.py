"""Regression tests for factor_search_v08 split enumeration boundaries."""

import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject, is_multiplicative_unit, multiply
from ucns_recursive.factor_search_v08 import factor_search_v08

UNIT = None


def make_s2() -> UCNSObject:
    return UCNSObject(
        2,
        2,
        [(Fraction(0), UNIT), (Fraction(1), UNIT)],
        [0, 0],
    )


def make_s3() -> UCNSObject:
    return UCNSObject(
        3,
        3,
        [
            (Fraction(0), UNIT),
            (Fraction(2, 3), UNIT),
            (Fraction(4, 3), UNIT),
        ],
        [0, 0, 0],
    )


class TestFactorSearchSplitBoundaries(unittest.TestCase):
    def test_right_singleton_non_unit_factor_is_found(self) -> None:
        """The search must try p=n, q=1, not only p=1, q=n."""
        s2 = make_s2()
        s3 = make_s3()

        left = UCNSObject(
            2,
            2,
            [(Fraction(0), UNIT), (Fraction(1), s3)],
            [0, 0],
        )
        right = UCNSObject(
            1,
            1,
            [(Fraction(0), s2)],
            [0],
        )
        self.assertFalse(is_multiplicative_unit(right))

        product = multiply(left, right)
        result = factor_search_v08(product, catalogue=[UNIT, s2, s3], prune=False)

        self.assertIsInstance(
            result,
            tuple,
            "right-singleton non-unit factorization must be recovered",
        )
        recovered_left, recovered_right = result
        self.assertEqual(len(recovered_right.A_plus), 1)
        self.assertFalse(is_multiplicative_unit(recovered_left))
        self.assertFalse(is_multiplicative_unit(recovered_right))
        self.assertEqual(multiply(recovered_left, recovered_right), product)


if __name__ == "__main__":
    unittest.main()
