"""
test_catalogue_d3
=================
Tests for ucns_recursive.catalogue_d3:

- is_in_oracle_class_d3 predicate
- build_catalogue_d3_oracle builder (ValueError, empty basis, narrow basis,
  max_objects truncation, basis filtering)
- D3CatalogueResult.coverage_attestation() format
- _recursive_obj_key deduplication key
"""

import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject
from ucns_recursive.catalogue_d3 import (
    is_in_oracle_class_d3,
    D3CatalogueResult,
    build_catalogue_d3_oracle,
    _recursive_obj_key,
)
from ucns_recursive.domains import depth_of, is_in_oracle_class

UNIT = None


def _make_S2() -> UCNSObject:
    return UCNSObject(2, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 0])


def _make_d2() -> UCNSObject:
    """Minimal depth-2 oracle object: 1-cell with an oracle-atom payload."""
    return UCNSObject(1, 1, [(Fraction(0), _make_S2())], [0])


class TestIsInOracleClassD3(unittest.TestCase):
    """Predicate coverage: None, depth-1, depth-2, depth-3, depth-4."""

    def setUp(self) -> None:
        self.S2 = _make_S2()
        self.d2 = _make_d2()
        self.d3 = UCNSObject(1, 1, [(Fraction(0), self.d2)], [0])

    def test_none_is_in_d3_class(self) -> None:
        self.assertTrue(is_in_oracle_class_d3(None))

    def test_depth1_oracle_atom_is_in_d3_class(self) -> None:
        self.assertEqual(depth_of(self.S2), 1)
        self.assertTrue(is_in_oracle_class_d3(self.S2))

    def test_depth2_oracle_object_is_in_d3_class(self) -> None:
        self.assertEqual(depth_of(self.d2), 2)
        self.assertTrue(is_in_oracle_class_d3(self.d2))

    def test_depth3_object_with_oracle_payloads_is_in_d3_class(self) -> None:
        self.assertEqual(depth_of(self.d3), 3)
        self.assertTrue(is_in_oracle_class_d3(self.d3))

    def test_depth4_object_is_not_in_d3_class(self) -> None:
        try:
            d4 = UCNSObject(1, 1, [(Fraction(0), self.d3)], [0])
        except ValueError:
            self.skipTest("depth-4 UCNSObject rejected by constructor")
        self.assertEqual(depth_of(d4), 4)
        self.assertFalse(is_in_oracle_class_d3(d4))


class TestBuildCatalogueD3Oracle(unittest.TestCase):
    """Builder: ValueError, empty basis, depth-3 invariants, truncation."""

    def setUp(self) -> None:
        self.d2 = _make_d2()

    def test_none_payload_basis_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            build_catalogue_d3_oracle(None)

    def test_empty_basis_gives_zero_objects_exhausted(self) -> None:
        result = build_catalogue_d3_oracle([])
        self.assertIsInstance(result, D3CatalogueResult)
        self.assertEqual(len(result.objects), 0)
        self.assertTrue(result.exhausted)
        self.assertIsNone(result.truncated_at)
        self.assertEqual(result.payload_basis_size, 0)

    def test_none_only_basis_gives_zero_objects_exhausted(self) -> None:
        """Basis with only None (depth-0) never produces depth-3 objects."""
        result = build_catalogue_d3_oracle([None])
        self.assertEqual(len(result.objects), 0)
        self.assertTrue(result.exhausted)
        self.assertIsNone(result.truncated_at)
        self.assertEqual(result.payload_basis_size, 1)  # None passes filter

    def test_non_oracle_elements_filtered_from_basis(self) -> None:
        """A depth-3 object fails is_in_oracle_class → filtered out of basis."""
        d3 = UCNSObject(1, 1, [(Fraction(0), self.d2)], [0])
        self.assertFalse(is_in_oracle_class(d3))  # depth>=3 → False
        result = build_catalogue_d3_oracle([d3])
        self.assertEqual(result.payload_basis_size, 0)  # filtered to empty
        self.assertEqual(len(result.objects), 0)

    def test_narrow_basis_all_objects_depth3_and_in_d3_class(self) -> None:
        result = build_catalogue_d3_oracle([None, self.d2])
        self.assertGreater(len(result.objects), 0)
        for obj in result.objects:
            self.assertEqual(depth_of(obj), 3)
            self.assertTrue(is_in_oracle_class_d3(obj))

    def test_max_objects_truncates(self) -> None:
        result = build_catalogue_d3_oracle([None, self.d2], max_objects=5)
        self.assertEqual(len(result.objects), 5)
        self.assertFalse(result.exhausted)
        self.assertIsNotNone(result.truncated_at)
        self.assertIsInstance(result.truncated_at, tuple)
        self.assertEqual(len(result.truncated_at), 3)


class TestD3CatalogueResultAttestation(unittest.TestCase):
    """coverage_attestation() string content for exhausted and partial cases."""

    def setUp(self) -> None:
        self.d2 = _make_d2()

    def test_coverage_attestation_exhausted_empty_basis(self) -> None:
        result = build_catalogue_d3_oracle([])
        self.assertTrue(result.exhausted)
        attest = result.coverage_attestation()
        self.assertIn("COVERS D''", attest)
        self.assertIn("enumeration exhausted", attest)
        self.assertIn("0 objects", attest)
        self.assertIn("basis_size=0", attest)

    def test_coverage_attestation_partial(self) -> None:
        result = build_catalogue_d3_oracle([None, self.d2], max_objects=5)
        self.assertFalse(result.exhausted)
        attest = result.coverage_attestation()
        self.assertIn("PARTIAL:", attest)
        self.assertIn("5 objects", attest)
        self.assertIn("coverage NOT attested", attest)
        self.assertIn(f"basis_size={result.payload_basis_size}", attest)

    def test_attestation_exhausted_records_basis_size(self) -> None:
        result = build_catalogue_d3_oracle([None])
        attest = result.coverage_attestation()
        self.assertIn("basis_size=1", attest)


class TestRecursiveObjKey(unittest.TestCase):
    """_recursive_obj_key: None handling, structural equality, deduplication."""

    def setUp(self) -> None:
        self.d2 = _make_d2()

    def test_none_key_is_none(self) -> None:
        self.assertIsNone(_recursive_obj_key(None))

    def test_identical_depth3_objects_same_key(self) -> None:
        d3a = UCNSObject(1, 1, [(Fraction(0), self.d2)], [0])
        d3b = UCNSObject(1, 1, [(Fraction(0), self.d2)], [0])
        self.assertEqual(_recursive_obj_key(d3a), _recursive_obj_key(d3b))

    def test_different_face_gives_different_key(self) -> None:
        d3_f0 = UCNSObject(1, 1, [(Fraction(0), self.d2)], [0])
        try:
            d3_f1 = UCNSObject(1, 1, [(Fraction(0), self.d2)], [1])
        except ValueError:
            self.skipTest("F_plus=[1] construction rejected by constructor")
        self.assertNotEqual(_recursive_obj_key(d3_f0), _recursive_obj_key(d3_f1))

    def test_builder_produces_no_duplicate_keys(self) -> None:
        result = build_catalogue_d3_oracle([None, self.d2])
        keys = [_recursive_obj_key(obj) for obj in result.objects]
        self.assertEqual(
            len(keys), len(set(keys)),
            "Duplicate objects in catalogue — deduplication failed",
        )


if __name__ == "__main__":
    unittest.main()
