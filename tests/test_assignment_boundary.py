# === CHECKS ===
# id: check_assignment_admission_explicit_adapter
#   proves: assignment_admission_requires_explicit_domain_adapter
#   call: self::test_admission_requires_adapter_and_keeps_digest_out_of_geometry
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_assignment_admission_occurrence_preservation
#   proves: assignment_admission_preserves_occurrence_order_and_multiplicity
#   call: self::test_trace_preserves_equal_content_as_distinct_ordered_occurrences
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_assignment_outcome_partition
#   proves: assignment_outcome_is_total_and_exclusive_over_admitted_evidence
#   call: self::test_outcome_partition_is_total_exclusive_and_fail_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_assignment_identity_mechanism_rejection
#   proves: assignment_identity_mechanisms_cannot_derive_geometry
#   call: self::test_identity_derived_mechanisms_are_rejected_without_geometry
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_assignment_supplied_candidate_evidence
#   proves: supplied_assignment_remains_candidate_evidence
#   call: self::test_supplied_candidate_is_retained_without_derivation_or_selection
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_assignment_boundary_nonactivation
#   proves: assignment_boundary_does_not_complete_initiation_or_activate
#   call: self::test_v016_report_retains_upstream_and_unresolved_geometry
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.assignment_boundary import (
    ADAPTER_EVIDENCE_IDENTITY_ROLE,
    ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS,
    ASSIGNMENT_FALSIFIER_IDS,
    ASSIGNMENT_OUTCOME_RELATION_STATUS,
    AssignmentAdmissionError,
    AssignmentAdmissionTrace,
    AssignmentDisposition,
    AssignmentEvidenceStanding,
    RejectedAssignmentMechanism,
    admit_observed_element,
    record_assignment_outcome,
    run_v016_assignment_admission_boundary_experiment,
)
from ucns.edcm_motion import (
    GeometricAssignment,
    GeometryKind,
    LawStanding,
)
from ucns.experiments import json_content_adapter, text_content_adapter
from ucns.full_carrier_attachment import V015_COMPLETE_RELATIONSHIP_STATUS


def _admission(index: int, subject: object = "same"):
    adapter = (
        text_content_adapter(name="fixture-text", version="1")
        if isinstance(subject, str)
        else json_content_adapter(name="fixture-json", version="1")
    )
    return admit_observed_element(
        admission_id=f"fixture:occurrence:{index}",
        occurrence_index=index,
        subject_name=f"subject-{index}",
        subject=subject,
        adapter=adapter,
        source_id="fixture-source",
        source_reference="fixture://assignment-boundary",
        grain="word",
        provenance=("hand-authored fixture",),
    )


def _candidate(relation_id: str = "fixture:relation") -> GeometricAssignment:
    return GeometricAssignment(
        relation_id=relation_id,
        geometry=GeometryKind.EPICYCLE,
        assignment_law_id="fixture.explicit-supplied-assignment",
        assignment_law_version="0.1.0",
        law_standing=LawStanding.CANDIDATE,
        orientation="widdershins",
        sidedness="left",
        parameters=(("transverse-witness", "caller-supplied"),),
        evidence=("hand-authored candidate relation",),
    )


def test_admission_requires_adapter_and_keeps_digest_out_of_geometry() -> None:
    source = {"node": [1]}
    admission = _admission(0, source)
    source["node"].append(2)

    assert admission.subject_record.subject == {"node": [1]}
    assert admission.subject_record.adapter_name == "fixture-json"
    assert admission.evidence_identity_role == ADAPTER_EVIDENCE_IDENTITY_ROLE
    assert admission.subject_record.digest in admission.evidence_identity
    assert not any(
        isinstance(value, GeometricAssignment)
        for value in admission.evidence_identity
    )

    with pytest.raises(TypeError, match="adapter must be ContentAdapter"):
        admit_observed_element(
            admission_id="bad",
            occurrence_index=0,
            subject_name="bad",
            subject=object(),
            adapter=object(),  # type: ignore[arg-type]
            source_id="fixture",
            source_reference="fixture://bad",
            grain="object",
            provenance=("fixture",),
        )
    with pytest.raises(TypeError, match="text adapter requires str"):
        admit_observed_element(
            admission_id="bad-domain",
            occurrence_index=0,
            subject_name="bad-domain",
            subject={"not": "text"},
            adapter=text_content_adapter(),
            source_id="fixture",
            source_reference="fixture://bad-domain",
            grain="object",
            provenance=("fixture",),
        )


def test_trace_preserves_equal_content_as_distinct_ordered_occurrences() -> None:
    first = _admission(0)
    second = _admission(1)
    trace = AssignmentAdmissionTrace(
        trace_id="trace:duplicates",
        outcomes=(
            record_assignment_outcome(first, evidence=("unresolved",)),
            record_assignment_outcome(second, evidence=("unresolved",)),
        ),
    )

    assert trace.subject_digests == (
        first.subject_record.digest,
        first.subject_record.digest,
    )
    assert trace.outcomes[0].admission.admission_id != (
        trace.outcomes[1].admission.admission_id
    )
    assert trace.has_total_outcome_evidence
    assert not trace.all_have_supplied_candidate_relations

    with pytest.raises(AssignmentAdmissionError, match="contiguous input order"):
        AssignmentAdmissionTrace(
            trace_id="trace:reordered",
            outcomes=(
                record_assignment_outcome(second, evidence=("unresolved",)),
                record_assignment_outcome(first, evidence=("unresolved",)),
            ),
        )


def test_outcome_partition_is_total_exclusive_and_fail_closed() -> None:
    admission = _admission(0)
    unresolved = record_assignment_outcome(
        admission,
        evidence=("no ratified law",),
    )
    supplied = record_assignment_outcome(
        admission,
        assignment=_candidate(),
        evidence=("explicit caller-supplied candidate",),
    )
    rejected = record_assignment_outcome(
        admission,
        rejected_mechanism=(
            RejectedAssignmentMechanism.CONTENT_DIGEST_TO_GEOMETRY
        ),
        evidence=("identity is not geometry",),
    )

    assert unresolved.disposition is AssignmentDisposition.UNRESOLVED
    assert supplied.disposition is AssignmentDisposition.SUPPLIED_CANDIDATE
    assert rejected.disposition is AssignmentDisposition.REJECTED_MECHANISM

    with pytest.raises(AssignmentAdmissionError, match="both supplied and rejected"):
        record_assignment_outcome(
            admission,
            assignment=_candidate(),
            rejected_mechanism=(
                RejectedAssignmentMechanism.CONTENT_DIGEST_TO_GEOMETRY
            ),
            evidence=("invalid",),
        )
    with pytest.raises(AssignmentAdmissionError, match="cannot contain"):
        replace(unresolved, assignment=_candidate())
    with pytest.raises(AssignmentAdmissionError, match="cannot supply"):
        replace(rejected, assignment=_candidate())


def test_identity_derived_mechanisms_are_rejected_without_geometry() -> None:
    for mechanism in RejectedAssignmentMechanism:
        outcome = record_assignment_outcome(
            _admission(0),
            rejected_mechanism=mechanism,
            evidence=(f"reject {mechanism.value}",),
        )
        assert outcome.disposition is AssignmentDisposition.REJECTED_MECHANISM
        assert outcome.rejected_mechanism is mechanism
        assert outcome.assignment is None
        assert not outcome.geometric_relation_derived_from_subject_digest

    unresolved = record_assignment_outcome(
        _admission(0),
        evidence=("no law",),
    )
    with pytest.raises(AssignmentAdmissionError, match="cannot derive geometry"):
        replace(
            unresolved,
            geometric_relation_derived_from_subject_digest=True,
        )


def test_supplied_candidate_is_retained_without_derivation_or_selection() -> None:
    admission = _admission(0)
    candidate = _candidate()
    outcome = record_assignment_outcome(
        admission,
        assignment=candidate,
        evidence=("caller supplied relation without derivation",),
    )

    assert outcome.assignment is candidate
    assert outcome.assignment.assignment_law_id == (
        "fixture.explicit-supplied-assignment"
    )
    assert outcome.assignment.law_standing is LawStanding.CANDIDATE
    assert outcome.assignment.orientation == "widdershins"
    assert outcome.selection_effect == "none"

    with pytest.raises(AssignmentAdmissionError, match="cannot select"):
        replace(outcome, selection_effect="selected")


def test_v016_report_retains_upstream_and_unresolved_geometry() -> None:
    report = run_v016_assignment_admission_boundary_experiment()

    assert report.schema_version == "0.16.0"
    assert report.outcome_relation_status == ASSIGNMENT_OUTCOME_RELATION_STATUS
    assert (
        report.arbitrary_element_assignment_status
        == ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS
    )
    assert report.complete_relationship_status == V015_COMPLETE_RELATIONSHIP_STATUS
    assert report.upstream.schema_version == "0.15.0"
    assert report.upstream.arbitrary_element_assignment_status == "unresolved"
    assert tuple(item.falsifier_id for item in report.results) == (
        ASSIGNMENT_FALSIFIER_IDS
    )
    assert report.result("AA05").standing is (
        AssignmentEvidenceStanding.NEGATIVE_SUPPORTED
    )
    assert report.result("AA07").standing is AssignmentEvidenceStanding.UNRESOLVED
    assert report.demonstration_trace.subject_digests[0] == (
        report.demonstration_trace.subject_digests[1]
    )
    assert report.selection_effect == "none"
    assert report.edcm_activation == report.metapat_activation == "inactive"
    assert any("Structural Null" in item for item in report.hmmm)

    with pytest.raises(AssignmentAdmissionError, match="standings are fixed"):
        replace(report, arbitrary_element_assignment_status="implemented")
    with pytest.raises(AssignmentAdmissionError, match="standings are fixed"):
        replace(report, complete_relationship_status="complete")
    promoted_aa07 = replace(
        report.result("AA07"),
        standing=AssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
    )
    with pytest.raises(AssignmentAdmissionError, match="packet is fixed"):
        replace(
            report,
            results=(*report.results[:-1], promoted_aa07),
        )
    with pytest.raises(AssignmentAdmissionError, match="activate EDCM"):
        replace(report, edcm_activation="active")
    with pytest.raises(AssignmentAdmissionError, match="activate METAPAT"):
        replace(report, metapat_activation="active")
