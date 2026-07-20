"""
Tests for UCNS object inspection records.
"""

import unittest
from fractions import Fraction

from ucns_recursive import (
    UCNSObject,
    UNIT,
    object_record,
    stable_hash,
)
from ucns_recursive.domains import S2


class TestObjectRecord(unittest.TestCase):
    def test_unit_record(self):
        record = object_record(UNIT)

        self.assertEqual(record.object_hash, stable_hash(UNIT))
        self.assertEqual(record.domain_label, "depth-0")
        self.assertEqual(record.depth, 0)
        self.assertEqual(record.n_min, 1)
        self.assertEqual(record.length, 0)
        self.assertTrue(record.is_unit)
        self.assertTrue(record.is_verified_domain)
        self.assertFalse(record.is_frontier)

    def test_depth_1_record(self):
        record = object_record(S2)

        self.assertEqual(record.object_hash, stable_hash(S2))
        self.assertEqual(record.domain_label, "depth-1")
        self.assertEqual(record.depth, 1)
        self.assertEqual(record.n_min, S2.n_min)
        self.assertEqual(record.length, len(S2.A_plus))
        self.assertFalse(record.is_unit)
        self.assertTrue(record.is_verified_domain)
        self.assertFalse(record.is_frontier)
        self.assertIn('"kind":"object"', record.canonical_json)

    def test_frontier_depth_3_record(self):
        depth2_payload = UCNSObject(
            2,
            2,
            [(Fraction(0), S2), (Fraction(1), UNIT)],
            [0, 0],
        )
        obj = UCNSObject(
            2,
            2,
            [(Fraction(0), depth2_payload), (Fraction(1), UNIT)],
            [0, 0],
        )

        record = object_record(obj)

        self.assertEqual(record.domain_label, "depth-3+")
        self.assertEqual(record.depth, 3)
        self.assertFalse(record.is_verified_domain)
        self.assertTrue(record.is_frontier)


if __name__ == "__main__":
    unittest.main()
