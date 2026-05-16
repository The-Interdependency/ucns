"""
Tests for the public UCNS facade helpers.
"""

import unittest
from fractions import Fraction

from ucns import a0_safe
from ucns_recursive import (
    FactorizationResultKind,
    UCNSObject,
    UNIT,
    multiply,
    stable_hash,
)
from ucns_recursive.domains import S2


class TestA0SafeFacade(unittest.TestCase):
    def test_identity_matches_stable_hash(self):
        self.assertEqual(a0_safe.identity(S2), stable_hash(S2))

    def test_describe_returns_object_record(self):
        record = a0_safe.describe(S2)
        self.assertEqual(record.domain_label, "depth-1")
        self.assertEqual(record.object_hash, stable_hash(S2))

    def test_canonical_returns_text_or_bytes(self):
        text = a0_safe.canonical(S2)
        data = a0_safe.canonical(S2, as_bytes=True)

        self.assertIsInstance(text, str)
        self.assertIsInstance(data, bytes)
        self.assertEqual(data, text.encode("utf-8"))

    def test_factor_returns_envelope_not_raw_sentinel(self):
        A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
        P = multiply(A, B)

        result = a0_safe.factor(P)

        self.assertEqual(result.result_kind, FactorizationResultKind.FACTORS)
        self.assertTrue(result.has_factors)


if __name__ == "__main__":
    unittest.main()
