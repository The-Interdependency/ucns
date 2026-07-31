# === CHECKS ===
# id: check_full_carrier_affine_certificate
#   proves: full_carrier_affine_certificate_is_universal_and_exact
#   call: self::test_affine_certificate_retains_exact_universal_proof_data
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_full_carrier_quotient_certificate
#   proves: full_carrier_quotient_certificate_commutes_without_moving_the_marked_seam
#   call: self::test_quotient_certificate_commutes_and_excludes_structural_null
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_full_carrier_mixed_scope_report
#   proves: full_carrier_attachment_retains_mixed_evidence_scopes
#   call: self::test_report_retains_analytic_and_bounded_executable_scopes
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_full_carrier_nonactivation_boundary
#   proves: full_carrier_attachment_does_not_complete_select_or_activate
#   call: self::test_report_rejects_scope_completion_selection_and_activation
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_edcm_multiwoz_v0141_handoff
#   proves: external_multiwoz_v0141_handoff_is_exact_and_nonpromoting
#   call: self::test_external_edcm_receipt_handoff_is_exact_and_nonpromoting
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction
import json
from pathlib import Path

import pytest

from ucns.full_carrier_attachment import (
    AFFINE_REAL_SCOPE,
    ANALYTIC_PROOF_STATUS,
    COORDINATE_CUT_STATUS,
    NON_NULL_QUOTIENT_SCOPE,
    STRUCTURAL_NULL_ATTACHMENT_STATUS,
    STRUCTURAL_NULL_DOMAIN_STATUS,
    V015_COMPLETE_RELATIONSHIP_STATUS,
    AffineContinuityCertificate,
    ContinuityEvidenceStanding,
    FullCarrierAttachmentError,
    QuotientSeamCommutationCertificate,
    run_v015_full_carrier_attachment_experiment,
)
from ucns.initiation_boundary import PARTIAL_INITIATION_SCOPE
from ucns.mobius_experiment import FalsifierVerdict


def test_affine_certificate_retains_exact_universal_proof_data() -> None:
    certificate = AffineContinuityCertificate()

    assert certificate.source_interval == (Fraction(-1), Fraction(1))
    assert certificate.target_interval == (
        Fraction(1, 2),
        Fraction(3, 2),
    )
    assert certificate.forward_after_inverse_coefficients == (
        Fraction(0),
        Fraction(1),
    )
    assert certificate.inverse_after_forward_coefficients == (
        Fraction(0),
        Fraction(1),
    )
    assert certificate.forward_delta(Fraction(3, 7)) == Fraction(6, 7)
    assert certificate.inverse_delta(Fraction(3, 7)) == Fraction(3, 14)
    assert certificate.scope == AFFINE_REAL_SCOPE
    assert certificate.proof_status == ANALYTIC_PROOF_STATUS

    with pytest.raises(
        FullCarrierAttachmentError,
        match="coefficients are fixed",
    ):
        replace(certificate, forward_slope=Fraction(2, 3))
    with pytest.raises(
        FullCarrierAttachmentError,
        match="epsilon-delta multiplier",
    ):
        replace(certificate, forward_delta_multiplier=Fraction(1))
    with pytest.raises(FullCarrierAttachmentError, match="positive"):
        certificate.forward_delta(Fraction(0))
    with pytest.raises(FullCarrierAttachmentError, match="exact Fraction"):
        certificate.inverse_delta(0.5)  # type: ignore[arg-type]


def test_quotient_certificate_commutes_and_excludes_structural_null() -> None:
    certificate = QuotientSeamCommutationCertificate()

    left, right = certificate.sheet_commutation_coefficients
    assert left == right == (Fraction(1), Fraction(-1, 2))
    assert certificate.source_deck_period == certificate.target_deck_period == 2
    assert certificate.coordinate_cut_status == COORDINATE_CUT_STATUS
    assert (
        certificate.structural_null_domain_status
        == STRUCTURAL_NULL_DOMAIN_STATUS
    )
    assert certificate.scope == NON_NULL_QUOTIENT_SCOPE

    with pytest.raises(
        FullCarrierAttachmentError,
        match="deck periods and turn map are fixed",
    ):
        replace(certificate, source_deck_period=Fraction(1))
    with pytest.raises(
        FullCarrierAttachmentError,
        match="sheet involution coefficients are fixed",
    ):
        replace(certificate, sheet_reflection_intercept=Fraction(1))
    with pytest.raises(
        FullCarrierAttachmentError,
        match="identity, scope, and standing are fixed",
    ):
        replace(
            certificate,
            structural_null_domain_status="included-as-coordinate-limit",
        )


def test_report_retains_analytic_and_bounded_executable_scopes() -> None:
    report = run_v015_full_carrier_attachment_experiment()

    assert report.result("RC01").standing is (
        ContinuityEvidenceStanding.ANALYTIC_SUPPORTED
    )
    assert report.result("RC01").scope == AFFINE_REAL_SCOPE
    assert report.result("RC03").standing is (
        ContinuityEvidenceStanding.ANALYTIC_SUPPORTED
    )
    assert report.result("RC03").scope == NON_NULL_QUOTIENT_SCOPE
    for falsifier_id in (
        "RC02",
        "RC04",
        "RC05",
        "RC06",
        "RC07",
        "RC08",
        "RC09",
        "RC10",
    ):
        result = report.result(falsifier_id)
        assert result.standing is (
            ContinuityEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED
        )
        assert result.scope == PARTIAL_INITIATION_SCOPE

    assert report.partial_initiation_report.result("RC01").verdict is (
        FalsifierVerdict.INCONCLUSIVE
    )
    assert report.partial_initiation_report.result("RC03").verdict is (
        FalsifierVerdict.INCONCLUSIVE
    )
    assert len(report.partial_initiation_report.attachments) == 14
    assert (
        report.structural_null_attachment_status
        == STRUCTURAL_NULL_ATTACHMENT_STATUS
    )
    assert (
        report.complete_relationship_status
        == V015_COMPLETE_RELATIONSHIP_STATUS
    )
    assert report.arbitrary_element_assignment_status == "unresolved"
    assert any("machine-checked" in item for item in report.hmmm)


def test_report_rejects_scope_completion_selection_and_activation() -> None:
    report = run_v015_full_carrier_attachment_experiment()

    promoted_rc03 = replace(
        report.result("RC03"),
        scope="structural-null-and-arbitrary-real-global-carrier",
    )
    with pytest.raises(
        FullCarrierAttachmentError,
        match="mixed scopes are fixed",
    ):
        replace(
            report,
            results=(
                report.results[0],
                report.results[1],
                promoted_rc03,
                *report.results[3:],
            ),
        )
    with pytest.raises(
        FullCarrierAttachmentError,
        match="relationship standings are fixed",
    ):
        replace(
            report,
            complete_relationship_status="complete-global-carrier",
        )
    with pytest.raises(FullCarrierAttachmentError, match="select"):
        replace(report, selection_effect="signed-local-selected")
    with pytest.raises(FullCarrierAttachmentError, match="activate EDCM"):
        replace(report, edcm_activation="active")
    with pytest.raises(FullCarrierAttachmentError, match="activate METAPAT"):
        replace(report, metapat_activation="active")


def test_external_edcm_receipt_handoff_is_exact_and_nonpromoting() -> None:
    handoff_path = (
        Path(__file__).parents[1]
        / "docs"
        / "evidence"
        / "EDCM_MULTIWOZ_V0141_HANDOFF.json"
    )
    handoff = json.loads(handoff_path.read_text(encoding="utf-8"))

    assert handoff["schema_id"] == "ucns.edcm.external-evidence-handoff"
    assert handoff["status"] == "downstream-complete-receipt-recorded"
    assert handoff["ucns"]["producer_commit"] == (
        "868d80878c9ecd93ff30e91ca289122ded805a49"
    )
    assert handoff["ucns"]["completion_receipt_id"] == (
        "921ceacad026de1d884eec3e049b090246014706c937c062bd32f40bbff01f0c"
    )
    assert handoff["edcm"]["pull_request"] == 44
    assert handoff["receipt"]["status"] == "complete"
    assert handoff["reconciliation"]["source_native_complete"] is True
    assert handoff["corpus"] == {
        "archive_sha256": (
            "d377a176f5ec82dc9f6a97e4653d4eddc6cad917704c1aaaa5a8ee3e79f63a8e"
        ),
        "dialogues": 10438,
        "id": "multiwoz-2.1",
        "source_turns": 143048,
    }
    assert handoff["boundary"]["canon_selection"] is None
    assert handoff["boundary"]["proof_status_transfers_to_measurement_validity"] is False
    assert handoff["boundary"]["edcm_activation"] == "inactive"
    assert handoff["boundary"]["metapat_activation"] == "inactive"
