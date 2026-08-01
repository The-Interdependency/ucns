# === CHECKS ===
# id: check_explicit_geometry_independent_exact_input
#   proves: explicit_geometry_requires_initiated_word_and_independent_exact_input
#   call: self::test_proposal_requires_initiated_word_and_independent_exact_input
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_explicit_geometry_exact_candidate_application
#   proves: explicit_geometry_applies_exact_signed_local_candidate_reversibly
#   call: self::test_assignment_applies_exact_signed_local_candidate_reversibly
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_explicit_geometry_frame_side_and_rendering
#   proves: explicit_geometry_preserves_mobius_frame_and_local_side
#   call: self::test_assignment_preserves_frame_side_and_rendering_boundary
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_explicit_geometry_total_outcomes
#   proves: explicit_geometry_outcomes_are_total_exclusive_and_ordered
#   call: self::test_trace_is_total_exclusive_ordered_and_occurrence_preserving
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_explicit_geometry_rejected_mechanisms
#   proves: explicit_geometry_rejects_identity_projection_and_upstream_substitution
#   call: self::test_rejected_mechanisms_never_create_an_applied_assignment
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_explicit_geometry_nonactivation_boundary
#   proves: explicit_geometry_does_not_claim_total_law_complete_select_or_activate
#   call: self::test_v018_report_retains_unresolved_law_and_nonactivation
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction

import pytest

from ucns.assignment_boundary import admit_observed_element
from ucns.direct_mobius import (
    NativeMobiusFrame,
    StructuralNullKind,
    StructuralNullManifestation,
)
from ucns.edcm_motion import GeometryKind, LawStanding
from ucns.exact_coordinate import (
    BINARY64_RENDERING_STATUS,
    EXACT_COORDINATE_CANDIDATE_ID,
    recover_signed_local_transverse,
    render_exact_coordinate_binary64,
    signed_local_exact_coordinate,
)
from ucns.experiments import text_content_adapter
from ucns.explicit_geometric_assignment import (
    ARBITRARY_ELEMENT_ASSIGNMENT_STATUS,
    EXPLICIT_ASSIGNMENT_CODE_REFERENCE,
    EXPLICIT_ASSIGNMENT_LAW_ID,
    EXPLICIT_ASSIGNMENT_LAW_VERSION,
    EXPLICIT_ASSIGNMENT_STATUS,
    EXPLICIT_COORDINATE_INPUT_ROLE,
    GEOMETRIC_ASSIGNMENT_FALSIFIER_IDS,
    SOURCE_TO_COORDINATE_LAW_STATUS,
    V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_ID,
    V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_VERSION,
    AppliedGeometricAssignment,
    ExplicitGeometricAssignmentError,
    GeometricAssignmentDisposition,
    GeometricAssignmentEvidenceStanding,
    GeometricAssignmentFalsifierResult,
    GeometricAssignmentTrace,
    RejectedGeometricAssignmentMechanism,
    apply_explicit_geometric_assignment,
    propose_explicit_coordinate,
    record_geometric_assignment_outcome,
    run_v018_explicit_geometric_assignment_experiment,
)
from ucns.gonol_initiation import (
    GonolInitiationTrace,
    initiate_word_gonol,
    record_gonol_initiation_outcome,
)


def _initiated_outcome(index: int, *, subject: str = "same"):
    admission = admit_observed_element(
        admission_id=f"v018-fixture:occurrence:{index}",
        occurrence_index=index,
        subject_name=f"v018-subject-{index}",
        subject=subject,
        adapter=text_content_adapter(name="v018-fixture", version="1"),
        source_id="v018-fixture-source",
        source_reference="fixture://explicit-geometric-assignment",
        grain="word",
        provenance=("hand-authored v0.18 fixture",),
    )
    initiation = initiate_word_gonol(
        admission,
        gonol_id=f"v018-fixture:word-gonol:{index}",
        boundary_manifestation=StructuralNullManifestation(
            manifestation_id=f"v018-fixture:turn-boundary:{index}",
            witness_id="v018-fixture-source",
            kind=StructuralNullKind.TURN_BOUNDARY,
            source_offset=None,
            source_value=None,
        ),
    )
    return record_gonol_initiation_outcome(
        admission,
        initiation=initiation,
        evidence=("explicit fixture word-gonol declaration",),
    )


def _proposal(
    index: int = 0,
    *,
    local_transverse: Fraction = Fraction(1, 3),
    lifted_turns: Fraction = Fraction(0),
):
    outcome = _initiated_outcome(index)
    assert outcome.initiation is not None
    return propose_explicit_coordinate(
        outcome.initiation,
        local_transverse=local_transverse,
        lifted_turns=lifted_turns,
        evidence=("independent exact rational test proposal",),
    )


def test_proposal_requires_initiated_word_and_independent_exact_input() -> None:
    proposal = _proposal(lifted_turns=Fraction(5, 2))

    assert proposal.local_transverse == Fraction(1, 3)
    assert proposal.lifted_turns == Fraction(1, 2)
    assert proposal.input_role == EXPLICIT_COORDINATE_INPUT_ROLE
    assert proposal.derived_from_evidence_identity is False
    assert proposal.initiation.evidence_identity in proposal.evidence_identity

    with pytest.raises(TypeError, match="GonolInitiationReceipt"):
        propose_explicit_coordinate(  # type: ignore[arg-type]
            None,
            local_transverse=Fraction(0),
            lifted_turns=Fraction(0),
            evidence=("invalid missing initiation",),
        )
    for invalid_flag in (True, None, 0):
        with pytest.raises(
            ExplicitGeometricAssignmentError,
            match="exact false boolean",
        ):
            replace(
                proposal,
                derived_from_evidence_identity=invalid_flag,  # type: ignore[arg-type]
            )
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match=r"normalized to \[0, 2\)",
    ):
        replace(proposal, lifted_turns=Fraction(5, 2))
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="native frame",
    ):
        replace(proposal, frame=NativeMobiusFrame.REVERSED)


def test_assignment_applies_exact_signed_local_candidate_reversibly() -> None:
    proposal = _proposal(
        local_transverse=Fraction(-7, 11),
        lifted_turns=Fraction(8, 7),
    )
    receipt = apply_explicit_geometric_assignment(proposal)

    assert receipt.exact_coordinate.breadth == Fraction(15, 22)
    assert recover_signed_local_transverse(receipt.exact_coordinate) == Fraction(
        -7,
        11,
    )
    assert receipt.assignment.geometry is GeometryKind.CIRCLE
    assert receipt.assignment.assignment_law_id == EXPLICIT_ASSIGNMENT_LAW_ID
    assert (
        receipt.assignment.assignment_law_version
        == EXPLICIT_ASSIGNMENT_LAW_VERSION
    )
    assert receipt.assignment.law_standing is LawStanding.CANDIDATE
    assert receipt.assignment.parameters[0] == (
        "candidate-id",
        EXACT_COORDINATE_CANDIDATE_ID,
    )
    assert receipt.completion_registered is False
    assert receipt.parent_gonol_ids == ()

    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="exact signed-local coordinate",
    ):
        replace(
            receipt,
            exact_coordinate=signed_local_exact_coordinate(
                Fraction(0),
                proposal.lifted_turns,
            ),
        )
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="identity and fields",
    ):
        replace(
            receipt,
            assignment=replace(
                receipt.assignment,
                assignment_law_id="digest-derived-law",
            ),
        )
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="identity and fields",
    ):
        replace(
            receipt,
            assignment=replace(
                receipt.assignment,
                evidence=("fabricated",),
            ),
        )
    assert receipt.assignment.evidence in receipt.evidence_identity
    assert EXPLICIT_ASSIGNMENT_CODE_REFERENCE in receipt.evidence_identity
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="cannot register construction completion",
    ):
        replace(receipt, completion_registered=True)
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="higher-gonol composition",
    ):
        replace(receipt, parent_gonol_ids=("invented-parent",))


def test_assignment_preserves_frame_side_and_rendering_boundary() -> None:
    cases = (
        (Fraction(-1), Fraction(0), NativeMobiusFrame.POSITIVE, "local-negative"),
        (Fraction(0), Fraction(1), NativeMobiusFrame.REVERSED, "local-root"),
        (Fraction(1), Fraction(2), NativeMobiusFrame.POSITIVE, "local-positive"),
    )
    for index, (local, turns, frame, side) in enumerate(cases):
        proposal = _proposal(
            index,
            local_transverse=local,
            lifted_turns=turns,
        )
        receipt = apply_explicit_geometric_assignment(proposal)

        assert proposal.frame is frame
        assert proposal.local_side == side
        assert receipt.assignment.orientation == frame.value
        assert receipt.assignment.sidedness == side
        assert receipt.rendering_role == BINARY64_RENDERING_STATUS
        assert receipt.rendering.exact_coordinate == receipt.exact_coordinate

    receipt = apply_explicit_geometric_assignment(_proposal())
    wrong_rendering = render_exact_coordinate_binary64(
        signed_local_exact_coordinate(Fraction(0), Fraction(0))
    )
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="linked to exact coordinate",
    ):
        replace(receipt, rendering=wrong_rendering)
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="declared-loss rendering",
    ):
        replace(receipt, rendering_role="authoritative-exact-identity")


def test_trace_is_total_exclusive_ordered_and_occurrence_preserving() -> None:
    upstream = (_initiated_outcome(0), _initiated_outcome(1))
    upstream_trace = GonolInitiationTrace(
        "v018-fixture:upstream-trace",
        upstream,
    )
    proposals = tuple(
        propose_explicit_coordinate(
            outcome.initiation,
            local_transverse=local,
            lifted_turns=Fraction(index),
            evidence=("independent per-occurrence exact input",),
        )
        for index, (outcome, local) in enumerate(
            zip(upstream, (Fraction(-1, 4), Fraction(3, 5)), strict=True)
        )
        if outcome.initiation is not None
    )
    outcomes = tuple(
        record_geometric_assignment_outcome(
            upstream[index],
            applied_assignment=apply_explicit_geometric_assignment(proposal),
            evidence=("explicit candidate application",),
        )
        for index, proposal in enumerate(proposals)
    )
    trace = GeometricAssignmentTrace(
        "v018-fixture:trace",
        upstream_trace,
        outcomes,
    )

    assert trace.has_total_outcome_evidence
    assert len(set(trace.subject_digests)) == 1
    assert len(trace.subject_digests) == 2
    assert len(trace.assigned_receipts) == 2
    assert (
        trace.assigned_receipts[0].exact_coordinate.exact_identity
        != trace.assigned_receipts[1].exact_coordinate.exact_identity
    )
    assert tuple(
        outcome.upstream.admission.occurrence_index for outcome in trace.outcomes
    ) == (0, 1)

    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="complete exact upstream trace",
    ):
        GeometricAssignmentTrace(
            "v018-fixture:reordered",
            upstream_trace,
            outcomes[::-1],
        )

    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="complete exact upstream trace",
    ):
        GeometricAssignmentTrace(
            "v018-fixture:prefix",
            upstream_trace,
            outcomes[:1],
        )

    upstream_with_equal_receipt = _initiated_outcome(0)
    assert upstream_with_equal_receipt.initiation is not None
    equal_but_distinct_initiation = replace(
        upstream_with_equal_receipt.initiation
    )
    assert equal_but_distinct_initiation == upstream_with_equal_receipt.initiation
    assert equal_but_distinct_initiation is not upstream_with_equal_receipt.initiation
    spliced_proposal = propose_explicit_coordinate(
        equal_but_distinct_initiation,
        local_transverse=Fraction(0),
        lifted_turns=Fraction(0),
        evidence=("equal-value but distinct initiation graph",),
    )
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="exact upstream initiation receipt",
    ):
        record_geometric_assignment_outcome(
            upstream_with_equal_receipt,
            applied_assignment=apply_explicit_geometric_assignment(
                spliced_proposal
            ),
            evidence=("reject equal-value evidence-graph splice",),
        )


def test_rejected_mechanisms_never_create_an_applied_assignment() -> None:
    upstream = _initiated_outcome(0)
    applied = apply_explicit_geometric_assignment(_proposal())

    for mechanism in RejectedGeometricAssignmentMechanism:
        outcome = record_geometric_assignment_outcome(
            upstream,
            rejected_mechanism=mechanism,
            evidence=(f"negative evidence:{mechanism.value}",),
        )
        assert outcome.disposition is GeometricAssignmentDisposition.REJECTED
        assert outcome.applied_assignment is None
        assert outcome.rejected_mechanism is mechanism

    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="cannot be assigned and rejected",
    ):
        record_geometric_assignment_outcome(
            upstream,
            applied_assignment=applied,
            rejected_mechanism=RejectedGeometricAssignmentMechanism.CONTENT_DIGEST,
            evidence=("invalid mixed outcome",),
        )


def test_v018_report_retains_unresolved_law_and_nonactivation() -> None:
    report = run_v018_explicit_geometric_assignment_experiment()

    class AlwaysEqualTuple(tuple):
        def __eq__(self, other: object) -> bool:
            return True

        def __ne__(self, other: object) -> bool:
            return False

    class AlwaysEqualFalsifierResult(GeometricAssignmentFalsifierResult):
        __slots__ = ()

        def __eq__(self, other: object) -> bool:
            return True

        def __ne__(self, other: object) -> bool:
            return False

    assert report.schema_id == V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_ID
    assert report.schema_version == V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_VERSION
    assert report.explicit_candidate_application_status == EXPLICIT_ASSIGNMENT_STATUS
    assert report.source_to_coordinate_law_status == SOURCE_TO_COORDINATE_LAW_STATUS
    assert report.arbitrary_element_assignment_status == (
        ARBITRARY_ELEMENT_ASSIGNMENT_STATUS
    )
    assert tuple(result.falsifier_id for result in report.results) == (
        GEOMETRIC_ASSIGNMENT_FALSIFIER_IDS
    )
    assert report.result("GA01").standing is (
        GeometricAssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED
    )
    assert report.result("GA08").standing is (
        GeometricAssignmentEvidenceStanding.UNRESOLVED
    )
    assert report.result("GA09").standing is (
        GeometricAssignmentEvidenceStanding.UNRESOLVED
    )
    assert report.selection_effect == "none"
    assert report.edcm_activation == "inactive"
    assert report.metapat_activation == "inactive"
    assert any("deriving exact" in item for item in report.hmmm)
    assert any("higher-gonol composition" in item for item in report.hmmm)

    promoted_results = AlwaysEqualTuple(
        report.results[:7]
        + (
            replace(
                report.results[7],
                standing=(
                    GeometricAssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED
                ),
            ),
            replace(
                report.results[8],
                standing=(
                    GeometricAssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED
                ),
            ),
        )
    )
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="exact tuple",
    ):
        replace(report, results=promoted_results)

    overloaded_result = AlwaysEqualFalsifierResult(
        report.results[0].falsifier_id,
        report.results[0].standing,
        report.results[0].evidence,
        report.results[0].limitation,
    )
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="exact tuple",
    ):
        replace(
            report,
            results=(overloaded_result,) + report.results[1:],
        )

    with pytest.raises(ExplicitGeometricAssignmentError, match="activate EDCM"):
        replace(report, edcm_activation="active")
    with pytest.raises(ExplicitGeometricAssignmentError, match="cannot select"):
        replace(report, selection_effect="candidate-selected")
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="standings are fixed",
    ):
        replace(report, source_to_coordinate_law_status="universal-derived-law")

    unresolved_outcomes = tuple(
        record_geometric_assignment_outcome(
            upstream,
            evidence=("no independent coordinate proposal",),
        )
        for upstream in report.upstream.demonstration_trace.outcomes
    )
    zero_assignment_trace = GeometricAssignmentTrace(
        "v018-fixture:zero-assignment-trace",
        report.upstream.demonstration_trace,
        unresolved_outcomes,
    )
    with pytest.raises(
        ExplicitGeometricAssignmentError,
        match="at least one applied assignment",
    ):
        replace(
            report,
            demonstration_trace=zero_assignment_trace,
        )
