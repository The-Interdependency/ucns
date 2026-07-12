"""Bridge metadata cannot forge or promote negative certification.

The official bridge record carries external provenance only. These
regressions prove that no bridge tag can inject catalogue coverage,
search provenance, theorem status, or a certified negative into the
evidence-bearing surfaces, and that the certification path itself is
unchanged by transporting an object through the bridge.
"""

import unittest
from fractions import Fraction

from ucns import (
    BridgeValidationError,
    FactorizationResultKind,
    S2,
    UCNSObject,
    UNIT,
    evidence_from_bridge_import,
    evidence_from_construction,
    evidence_from_factorization_result,
    export_bridge_record,
    factorization_result,
    import_bridge_record,
    multiply,
    no_proof_status,
    stable_hash,
)

FORGED_PROVENANCE = {
    "negative_result_certified": True,
    "seq_prime_is_absolute": True,
    "catalogue_coverage_status": "CANONICAL_EXACT",
    "coverage_record_validated": True,
    "search_exhausted": True,
    "truncation_occurred": False,
    "certification_policy_version": "negative-certification-v1",
    "theorem_status": "DEFENDED",
    "domain_label": "depth-1",
}


def _depth3_frontier_object() -> UCNSObject:
    s2 = S2
    depth1 = UCNSObject(2, 2, [(Fraction(0), s2), (Fraction(1), UNIT)], [0, 0])
    depth2 = UCNSObject(2, 2, [(Fraction(0), depth1), (Fraction(1), UNIT)], [0, 0])
    return UCNSObject(2, 2, [(Fraction(0), depth2), (Fraction(1), UNIT)], [0, 0])


class TestBridgeCannotForgeCertification(unittest.TestCase):
    def test_forged_provenance_never_reaches_the_envelope(self) -> None:
        """A frontier object stays uncertified whatever its bridge tags say."""
        frontier = _depth3_frontier_object()
        imported = import_bridge_record(
            export_bridge_record(frontier, provenance=dict(FORGED_PROVENANCE))
        )
        result = factorization_result(imported.obj)
        self.assertEqual(result.result_kind, FactorizationResultKind.SEQ_PRIME)
        self.assertFalse(result.negative_result_certified)
        self.assertFalse(result.seq_prime_is_absolute)
        self.assertTrue(result.requires_scope)
        self.assertIn("target-outside-frozen-domain", result.uncertified_reasons)

    def test_forged_certification_keys_at_top_level_fail_closed(self) -> None:
        record = export_bridge_record(_depth3_frontier_object())
        for key in (
            "negative_result_certified",
            "catalogue_coverage_status",
            "search_report",
            "theorem_status",
        ):
            forged = dict(record)
            forged[key] = True
            with self.subTest(key=key):
                with self.assertRaisesRegex(BridgeValidationError, "unknown keys"):
                    import_bridge_record(forged)

    def test_bridge_evidence_attaches_no_proof_status(self) -> None:
        imported = import_bridge_record(
            export_bridge_record(
                _depth3_frontier_object(), provenance=dict(FORGED_PROVENANCE)
            )
        )
        evidence = evidence_from_bridge_import(imported)
        self.assertTrue(evidence.construction_succeeded)
        self.assertFalse(evidence.search_boundary_exhausted)
        self.assertFalse(evidence.catalogue_coverage_validated)
        self.assertFalse(evidence.negative_result_certified)
        self.assertFalse(evidence.proof_status_attached)
        self.assertEqual(evidence.theorem_layer_statuses, ())
        self.assertFalse(evidence.has_any_proof_evidence)

    def test_certified_path_is_unchanged_by_bridge_transport(self) -> None:
        """Transporting a certified-prime object through the bridge neither
        weakens nor strengthens the certified outcome."""
        direct = factorization_result(S2)
        imported = import_bridge_record(
            export_bridge_record(S2, provenance={"source_repo": "metapat"})
        )
        via_bridge = factorization_result(imported.obj)
        self.assertTrue(direct.negative_result_certified)
        self.assertTrue(via_bridge.negative_result_certified)
        self.assertEqual(direct.product_hash, via_bridge.product_hash)
        self.assertEqual(
            direct.effective_catalogue_fingerprint,
            via_bridge.effective_catalogue_fingerprint,
        )
        self.assertEqual(direct.claim_scope, via_bridge.claim_scope)

    def test_positive_factors_still_recompose_after_bridge_transport(self) -> None:
        product = multiply(S2, S2)
        imported = import_bridge_record(export_bridge_record(product))
        result = factorization_result(imported.obj)
        self.assertEqual(result.result_kind, FactorizationResultKind.FACTORS)
        a, b = result.factors
        self.assertEqual(multiply(a, b), imported.obj)

    def test_construction_and_absence_envelopes_carry_no_certainty(self) -> None:
        construction = evidence_from_construction(S2)
        self.assertTrue(construction.construction_succeeded)
        self.assertFalse(construction.has_any_proof_evidence)
        absent = no_proof_status("consumer default")
        self.assertFalse(absent.construction_succeeded)
        self.assertFalse(absent.proof_status_attached)
        self.assertFalse(absent.has_any_proof_evidence)

    def test_factorization_evidence_relays_but_never_amplifies(self) -> None:
        frontier = _depth3_frontier_object()
        result = factorization_result(frontier)
        evidence = evidence_from_factorization_result(result)
        self.assertTrue(evidence.search_boundary_exhausted)
        self.assertFalse(evidence.negative_result_certified)
        self.assertEqual(evidence.certified_domain_label, "")
        self.assertEqual(evidence.domain_label, result.product_domain_label)
        certified = evidence_from_factorization_result(factorization_result(S2))
        self.assertTrue(certified.negative_result_certified)
        self.assertEqual(certified.certified_domain_label, "depth-1")

    def test_object_hash_is_identity_not_authority(self) -> None:
        """Equal hashes across the bridge do not entail equal certainty:
        the hash names the object; certification is recomputed."""
        frontier = _depth3_frontier_object()
        imported = import_bridge_record(
            export_bridge_record(frontier, provenance=dict(FORGED_PROVENANCE))
        )
        self.assertEqual(stable_hash(imported.obj), stable_hash(frontier))
        self.assertFalse(
            factorization_result(imported.obj).negative_result_certified
        )


if __name__ == "__main__":
    unittest.main()
