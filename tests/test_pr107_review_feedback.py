"""Regression tests for actionable review feedback on PR #107."""

import copy
import unittest
from fractions import Fraction

from ucns import (
    BridgeValidationError,
    S2,
    UCNSObject,
    UNIT,
    evidence_from_factorization_result,
    export_bridge_record,
    factorization_result,
    import_bridge_record,
)


class TestBridgeExactnessFeedback(unittest.TestCase):
    def test_export_rejects_coerced_mutated_angles(self) -> None:
        for angle in ("0", 0.0, True):
            obj = UCNSObject(
                2,
                2,
                [(Fraction(0), UNIT), (Fraction(1), UNIT)],
                [0, 0],
            )
            obj.A_plus[0] = (angle, UNIT)
            with self.subTest(angle=angle):
                with self.assertRaisesRegex(
                    BridgeValidationError,
                    "exact rational angles",
                ):
                    export_bridge_record(obj)

    def test_import_rejects_boolean_face_bits(self) -> None:
        record = export_bridge_record(S2)
        record["object"]["cells"][0]["face"] = True
        with self.assertRaisesRegex(
            BridgeValidationError,
            "integer bit 0 or 1",
        ):
            import_bridge_record(record)

    def test_import_rejects_non_normalized_angle_sequence(self) -> None:
        record = copy.deepcopy(export_bridge_record(S2))
        record["object"]["cells"][0]["angle"] = {"num": 1, "den": 1}
        record["object"]["cells"][1]["angle"] = {"num": 2, "den": 1}
        with self.assertRaisesRegex(
            BridgeValidationError,
            "non-normalized angles",
        ):
            import_bridge_record(record)


class TestEvidenceBoundaryFeedback(unittest.TestCase):
    def test_unit_short_circuit_attaches_no_proof_status(self) -> None:
        evidence = evidence_from_factorization_result(factorization_result(UNIT))
        self.assertTrue(evidence.construction_succeeded)
        self.assertFalse(evidence.search_boundary_exhausted)
        self.assertFalse(evidence.catalogue_coverage_validated)
        self.assertFalse(evidence.negative_result_certified)
        self.assertFalse(evidence.proof_status_attached)
        self.assertEqual(evidence.theorem_layer_statuses, ())
        self.assertFalse(evidence.has_any_proof_evidence)

    def test_incomplete_catalogue_is_not_validated_coverage(self) -> None:
        result = factorization_result(S2, catalogue=[])
        self.assertTrue(result.coverage_record_validated)
        self.assertTrue(result.coverage_bound_to_search_report)
        self.assertEqual(result.catalogue_coverage_status, "uncertified")

        evidence = evidence_from_factorization_result(result)
        self.assertTrue(evidence.search_boundary_exhausted)
        self.assertFalse(evidence.catalogue_coverage_validated)
        self.assertFalse(evidence.negative_result_certified)


if __name__ == "__main__":
    unittest.main()
