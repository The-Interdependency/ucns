"""
Tests for canonical UCNS serialization and stable hashing.
"""

import json
import unittest
from fractions import Fraction

from ucns_recursive import (
    UCNSObject,
    UNIT,
    canonical_bytes,
    canonical_data,
    canonical_json,
    stable_hash,
)
from ucns_recursive.domains import S2


class TestCanonicalSerialization(unittest.TestCase):
    def test_unit_serializes_deterministically(self):
        data = canonical_data(UNIT)
        self.assertEqual(data["kind"], "unit")
        self.assertEqual(canonical_json(UNIT), canonical_json(UNIT))
        self.assertEqual(canonical_bytes(UNIT), canonical_json(UNIT).encode("utf-8"))

    def test_json_is_valid_and_sorted(self):
        obj = S2
        text = canonical_json(obj)
        parsed = json.loads(text)
        self.assertEqual(parsed["kind"], "object")
        self.assertEqual(parsed["n_min"], obj.n_min)

    def test_equal_objects_have_same_bytes_and_hash(self):
        a = UCNSObject(
            4,
            2,
            [(Fraction(0), UNIT), (Fraction(1), UNIT)],
            [0, 1],
        )
        b = UCNSObject(
            8,
            2,
            [(Fraction(2), UNIT), (Fraction(3), UNIT)],
            [0, 1],
        )
        self.assertEqual(a, b)
        self.assertEqual(canonical_bytes(a), canonical_bytes(b))
        self.assertEqual(stable_hash(a), stable_hash(b))

    def test_different_face_state_changes_hash(self):
        a = UCNSObject(
            4,
            2,
            [(Fraction(0), UNIT), (Fraction(1), UNIT)],
            [0, 0],
        )
        b = UCNSObject(
            4,
            2,
            [(Fraction(0), UNIT), (Fraction(1), UNIT)],
            [0, 1],
        )
        self.assertNotEqual(a, b)
        self.assertNotEqual(stable_hash(a), stable_hash(b))

    def test_recursive_payload_affects_hash(self):
        a = UCNSObject(
            2,
            2,
            [(Fraction(0), S2), (Fraction(1), UNIT)],
            [0, 0],
        )
        b = UCNSObject(
            2,
            2,
            [(Fraction(0), UNIT), (Fraction(1), UNIT)],
            [0, 0],
        )
        self.assertNotEqual(a, b)
        self.assertNotEqual(stable_hash(a), stable_hash(b))

    def test_unsupported_hash_algorithm_raises(self):
        with self.assertRaises(ValueError):
            stable_hash(S2, algorithm="not-a-real-hash")

    def test_mismatched_angle_and_face_lengths_raise(self):
        obj = UCNSObject(
            4,
            2,
            [(Fraction(0), UNIT), (Fraction(1), UNIT)],
            [0],
        )
        with self.assertRaises(ValueError):
            canonical_data(obj)

    def test_mismatched_lengths_error_mentions_observed_sizes(self):
        obj = UCNSObject(
            4,
            2,
            [(Fraction(0), UNIT), (Fraction(1), UNIT), (Fraction(2), UNIT)],
            [0],
        )
        with self.assertRaisesRegex(ValueError, r"got 3 and 1"):
            canonical_data(obj)

    def test_mismatched_lengths_raise_across_serialization_entrypoints(self):
        obj = UCNSObject(
            4,
            2,
            [(Fraction(0), UNIT), (Fraction(1), UNIT)],
            [0],
        )
        with self.assertRaises(ValueError):
            canonical_json(obj)
        with self.assertRaises(ValueError):
            canonical_bytes(obj)
        with self.assertRaises(ValueError):
            stable_hash(obj)


if __name__ == "__main__":
    unittest.main()
