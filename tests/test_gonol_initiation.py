# === CHECKS ===
# id: check_gonol_initiation_origin_role_separation
#   proves: gonol_initiation_origin_roles_are_domain_separated
#   call: self::test_origin_registry_separates_structural_null_from_neighboring_roles
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_gonol_initiation_explicit_transition
#   proves: gonol_initiation_requires_explicit_structural_null_transition
#   call: self::test_word_gonol_requires_one_source_bound_structural_null_twist
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_gonol_initiation_total_outcome_relation
#   proves: gonol_initiation_outcome_is_total_and_exclusive
#   call: self::test_initiation_trace_is_total_exclusive_ordered_and_occurrence_preserving
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_gonol_initiation_root_return_boundary
#   proves: gonol_initiation_root_return_is_bounded_and_noncompleting
#   call: self::test_root_return_preserves_360_change_720_return_and_noncompletion
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_gonol_initiation_rejected_substitutions
#   proves: gonol_initiation_rejects_zero_and_absence_substitutions
#   call: self::test_neighboring_zero_and_absence_roles_cannot_become_prestate
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_gonol_initiation_nonactivation_boundary
#   proves: gonol_initiation_does_not_assign_complete_select_or_activate
#   call: self::test_v017_report_retains_unresolved_geometry_and_nonactivation
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.assignment_boundary import (
    ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS,
    admit_observed_element,
)
from ucns.direct_mobius import (
    STRUCTURAL_NULL_ORIGIN,
    NativeMobiusFrame,
    StructuralNullIdentity,
    StructuralNullKind,
    StructuralNullManifestation,
)
from ucns.experiments import text_content_adapter
from ucns.gonol_initiation import (
    GONOL_INITIATION_FALSIFIER_IDS,
    GONOL_INITIATION_OUTCOME_RELATION_STATUS,
    INITIATED_WORD_STATE_STATUS,
    ROOT_LOOP_COMPLETION_STATUS,
    TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS,
    V017_GONOL_INITIATION_SCHEMA_ID,
    V017_GONOL_INITIATION_SCHEMA_VERSION,
    GonolInitiationDisposition,
    GonolInitiationError,
    GonolInitiationEvidenceStanding,
    GonolInitiationTrace,
    OriginRole,
    OriginTermStanding,
    RejectedOriginSubstitution,
    build_root_loop_return_witness,
    initiate_word_gonol,
    origin_term_registry,
    record_gonol_initiation_outcome,
    run_v017_gonol_initiation_boundary_experiment,
)
from ucns.initiation_boundary import (
    run_v013_partial_initiation_boundary_experiment,
)


def _admission(index: int, *, grain: str = "word", subject: str = "same"):
    return admit_observed_element(
        admission_id=f"fixture:occurrence:{index}",
        occurrence_index=index,
        subject_name=f"fixture-subject-{index}",
        subject=subject,
        adapter=text_content_adapter(name="v017-fixture", version="1"),
        source_id="fixture-source",
        source_reference="fixture://gonol-initiation",
        grain=grain,
        provenance=("hand-authored v0.17 fixture",),
    )


def _boundary(*, witness_id: str = "fixture-source"):
    return StructuralNullManifestation(
        manifestation_id=f"{witness_id}:turn-boundary",
        witness_id=witness_id,
        kind=StructuralNullKind.TURN_BOUNDARY,
        source_offset=None,
        source_value=None,
    )


def test_origin_registry_separates_structural_null_from_neighboring_roles() -> None:
    terms = origin_term_registry()

    assert tuple(term.role for term in terms) == tuple(OriginRole)
    assert len({term.term_id for term in terms}) == len(terms) == 8
    assert all(term.term_id.startswith("ucns.") for term in terms)
    assert [
        term.role for term in terms if term.may_be_initiation_prestate
    ] == [OriginRole.STRUCTURAL_NULL]
    assert terms[0].standing is OriginTermStanding.DECIDED_CONSTRAINT

    with pytest.raises(
        GonolInitiationError,
        match="only Structural Null",
    ):
        replace(terms[1], may_be_initiation_prestate=True)
    with pytest.raises(
        GonolInitiationError,
        match="decided-constraint",
    ):
        replace(terms[0], standing=OriginTermStanding.TYPED_DISTINCTION)


def test_word_gonol_requires_one_source_bound_structural_null_twist() -> None:
    admission = _admission(0)
    receipt = initiate_word_gonol(
        admission,
        gonol_id="fixture:word-gonol:0",
        boundary_manifestation=_boundary(),
    )

    assert receipt.pre_state is STRUCTURAL_NULL_ORIGIN
    assert receipt.twist_receipt_count == 1
    assert receipt.post_state_status == INITIATED_WORD_STATE_STATUS
    assert receipt.geometric_assignment is None
    assert receipt.parent_gonol_ids == ()
    assert receipt.completion_registered is False
    assert admission.evidence_identity in receipt.evidence_identity

    with pytest.raises(GonolInitiationError, match="smallest word gonol"):
        initiate_word_gonol(
            _admission(0, grain="phrase"),
            gonol_id="fixture:phrase-gonol",
            boundary_manifestation=_boundary(),
        )
    with pytest.raises(GonolInitiationError, match="source identity"):
        initiate_word_gonol(
            admission,
            gonol_id="fixture:word-gonol:wrong-source",
            boundary_manifestation=_boundary(witness_id="other-source"),
        )
    with pytest.raises(GonolInitiationError, match="exactly one"):
        replace(receipt, twist_receipt_count=2)
    with pytest.raises(GonolInitiationError, match="manufacture"):
        replace(receipt, geometric_assignment="digest-angle")
    with pytest.raises(GonolInitiationError, match="higher-gonol"):
        replace(receipt, parent_gonol_ids=("parent",))
    with pytest.raises(GonolInitiationError, match="not registered"):
        replace(receipt, completion_registered=True)


def test_initiation_trace_is_total_exclusive_ordered_and_occurrence_preserving() -> None:
    admissions = tuple(_admission(index) for index in range(3))
    initiation = initiate_word_gonol(
        admissions[0],
        gonol_id="fixture:word-gonol:0",
        boundary_manifestation=_boundary(),
    )
    outcomes = (
        record_gonol_initiation_outcome(
            admissions[0],
            initiation=initiation,
            evidence=("explicit word-gonol declaration",),
        ),
        record_gonol_initiation_outcome(
            admissions[1],
            evidence=("no gonol declaration",),
        ),
        record_gonol_initiation_outcome(
            admissions[2],
            rejected_substitution=(
                RejectedOriginSubstitution.ALGEBRAIC_ZERO_AS_PRESTATE
            ),
            evidence=("algebraic zero is not Structural Null",),
        ),
    )
    trace = GonolInitiationTrace("fixture:v017-trace", outcomes)

    assert trace.has_total_outcome_evidence
    assert trace.outcome_relation_status == (
        GONOL_INITIATION_OUTCOME_RELATION_STATUS
    )
    assert tuple(outcome.disposition for outcome in trace.outcomes) == (
        GonolInitiationDisposition.INITIATED,
        GonolInitiationDisposition.UNRESOLVED,
        GonolInitiationDisposition.REJECTED_SUBSTITUTION,
    )
    assert len(set(trace.subject_digests)) == 1
    assert len(trace.subject_digests) == 3

    with pytest.raises(GonolInitiationError, match="both initiated and rejected"):
        record_gonol_initiation_outcome(
            admissions[0],
            initiation=initiation,
            rejected_substitution=(
                RejectedOriginSubstitution.ALGEBRAIC_ZERO_AS_PRESTATE
            ),
            evidence=("invalid mixed outcome",),
        )
    with pytest.raises(GonolInitiationError, match="contiguous input order"):
        GonolInitiationTrace("fixture:reordered", outcomes[::-1])


def test_root_return_preserves_360_change_720_return_and_noncompletion() -> None:
    upstream = run_v013_partial_initiation_boundary_experiment()
    witness = build_root_loop_return_witness(upstream)

    assert witness.initial.visible_identity == witness.after_360.visible_identity
    assert (
        witness.initial.complete_local_identity
        != witness.after_360.complete_local_identity
    )
    assert (
        witness.initial.complete_local_identity
        == witness.after_720.complete_local_identity
    )
    assert witness.initial.native_state.frame is NativeMobiusFrame.POSITIVE
    assert witness.after_360.native_state.frame is NativeMobiusFrame.REVERSED
    assert witness.after_720.native_state.frame is NativeMobiusFrame.POSITIVE
    assert len(witness.after_720.motion_history) == 2
    assert witness.completion_status == ROOT_LOOP_COMPLETION_STATUS
    assert witness.completion_registered is False

    with pytest.raises(GonolInitiationError, match="cannot register"):
        replace(witness, completion_registered=True)
    with pytest.raises(GonolInitiationError, match="degrees, scope"):
        replace(witness, complete_local_return_degrees=360)


def test_neighboring_zero_and_absence_roles_cannot_become_prestate() -> None:
    admission = _admission(0)
    initiation = initiate_word_gonol(
        admission,
        gonol_id="fixture:word-gonol:0",
        boundary_manifestation=_boundary(),
    )

    with pytest.raises(GonolInitiationError, match="singular Structural Null"):
        replace(initiation, pre_state=StructuralNullIdentity())

    for substitution in RejectedOriginSubstitution:
        outcome = record_gonol_initiation_outcome(
            admission,
            rejected_substitution=substitution,
            evidence=(f"rejected {substitution.value}",),
        )
        assert (
            outcome.disposition
            is GonolInitiationDisposition.REJECTED_SUBSTITUTION
        )
        assert outcome.initiation is None
        assert outcome.rejected_substitution is substitution


def test_v017_report_retains_unresolved_geometry_and_nonactivation() -> None:
    report = run_v017_gonol_initiation_boundary_experiment()

    assert report.schema_id == V017_GONOL_INITIATION_SCHEMA_ID
    assert report.schema_version == V017_GONOL_INITIATION_SCHEMA_VERSION
    assert tuple(result.falsifier_id for result in report.results) == (
        GONOL_INITIATION_FALSIFIER_IDS
    )
    assert all(
        report.result(f"GI{index:02d}").standing
        is GonolInitiationEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED
        for index in range(1, 5)
    )
    assert all(
        report.result(f"GI{index:02d}").standing
        is GonolInitiationEvidenceStanding.BOUNDED_UPSTREAM_SUPPORTED
        for index in (5, 6)
    )
    assert (
        report.result("GI07").standing
        is GonolInitiationEvidenceStanding.NEGATIVE_SUPPORTED
    )
    assert (
        report.result("GI08").standing
        is GonolInitiationEvidenceStanding.UNRESOLVED
    )
    assert report.arbitrary_element_assignment_status == (
        ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS
    )
    assert report.total_structural_null_topology_status == (
        TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS
    )
    assert report.selection_effect == "none"
    assert report.edcm_activation == "inactive"
    assert report.metapat_activation == "inactive"
    assert report.hmmm

    with pytest.raises(GonolInitiationError, match="standings are fixed"):
        replace(
            report,
            total_structural_null_topology_status="implemented-total-topology",
        )
    with pytest.raises(GonolInitiationError, match="cannot activate EDCM"):
        replace(report, edcm_activation="active")
    with pytest.raises(GonolInitiationError, match="cannot activate METAPAT"):
        replace(report, metapat_activation="active")
    with pytest.raises(GonolInitiationError, match="cannot select geometry"):
        replace(report, selection_effect="selected")
