# === CHECKS ===
# id: check_source_coordinate_complete_ordered_address
#   proves: source_coordinate_law_uses_complete_ordered_source_address
#   call: self::test_ordered_source_coordinate_uses_exact_complete_address
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_source_coordinate_scope_injectivity
#   proves: source_coordinate_law_is_exact_and_scope_injective
#   call: self::test_ordered_source_coordinate_is_exact_and_scope_injective
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_source_coordinate_upstream_identity
#   proves: source_coordinate_derivation_retains_exact_initiation_identity
#   call: self::test_derivation_retains_exact_upstream_identity
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_source_coordinate_exact_assignment
#   proves: source_coordinate_assignment_applies_exact_candidate_reversibly
#   call: self::test_source_coordinate_assignment_is_exact_and_reversible
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_source_coordinate_total_outcomes
#   proves: source_coordinate_outcomes_are_total_exclusive_and_ordered
#   call: self::test_trace_retains_total_ordered_outcomes_and_blockers
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_source_coordinate_negative_and_nonselection
#   proves: source_coordinate_law_rejects_identity_shortcuts_and_nonselection
#   call: self::test_equal_content_is_separate_and_report_remains_nonselecting
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction

import pytest

from ucns.direct_mobius import (
    NativeMobiusFrame,
    StructuralNullKind,
    StructuralNullManifestation,
)
from ucns.edcm_motion import GeometryKind, LawStanding
from ucns.exact_coordinate import (
    BINARY64_RENDERING_STATUS,
    recover_signed_local_transverse,
    render_exact_coordinate_binary64,
)
from ucns.gonol_initiation import (
    GonolInitiationDisposition,
    GonolInitiationTrace,
    initiate_word_gonol,
    record_gonol_initiation_outcome,
)
from ucns.source_coordinate import (
    ARBITRARY_SOURCE_ASSIGNMENT_STATUS,
    SOURCE_COORDINATE_ASSIGNMENT_STATUS,
    SOURCE_COORDINATE_FALSIFIER_IDS,
    SOURCE_COORDINATE_LAW_FORMULA,
    SOURCE_COORDINATE_LAW_ID,
    SOURCE_COORDINATE_LAW_STATUS,
    SOURCE_COORDINATE_LAW_VERSION,
    SOURCE_COORDINATE_OUTCOME_RELATION_STATUS,
    V019_HMMM,
    V019_SOURCE_COORDINATE_SCHEMA_ID,
    V019_SOURCE_COORDINATE_SCHEMA_VERSION,
    SourceCoordinateDisposition,
    SourceCoordinateError,
    SourceCoordinateEvidenceStanding,
    SourceCoordinateTrace,
    apply_source_coordinate_assignment,
    derive_ordered_source_coordinate,
    derive_source_coordinate,
    derive_source_coordinate_trace,
    run_v019_source_coordinate_derivation_experiment,
)


def test_ordered_source_coordinate_uses_exact_complete_address() -> None:
    address = derive_ordered_source_coordinate(2, 5)
    assert address.source_position == Fraction(1, 2)
    assert address.local_transverse == Fraction(0)
    assert address.lifted_turns == Fraction(1)
    assert address.frame is NativeMobiusFrame.REVERSED
    assert address.local_side == "local-root"
    assert address.law_id == SOURCE_COORDINATE_LAW_ID
    assert address.law_version == SOURCE_COORDINATE_LAW_VERSION
    assert address.formula == SOURCE_COORDINATE_LAW_FORMULA

    for args in ((-1, 5), (5, 5), (0, 0)):
        with pytest.raises(SourceCoordinateError):
            derive_ordered_source_coordinate(*args)
    with pytest.raises(TypeError):
        derive_ordered_source_coordinate(True, 5)
    with pytest.raises(SourceCoordinateError):
        replace(address, scope_cardinality=4)
    with pytest.raises(SourceCoordinateError):
        replace(address, source_position=Fraction(2, 5))


def test_ordered_source_coordinate_is_exact_and_scope_injective() -> None:
    for cardinality in range(1, 33):
        addresses = tuple(
            derive_ordered_source_coordinate(index, cardinality)
            for index in range(cardinality)
        )
        assert len({item.exact_identity for item in addresses}) == cardinality
        assert len({item.source_position for item in addresses}) == cardinality
        assert len({item.local_transverse for item in addresses}) == cardinality
        assert len({item.lifted_turns for item in addresses}) == cardinality
        assert addresses == tuple(sorted(addresses, key=lambda item: item.source_position))
        for index, address in enumerate(addresses):
            expected = Fraction(2 * index + 1, 2 * cardinality)
            assert address.source_position == expected
            assert address.local_transverse == 2 * expected - 1
            assert address.lifted_turns == 2 * expected


def test_derivation_retains_exact_upstream_identity() -> None:
    report = run_v019_source_coordinate_derivation_experiment()
    trace = report.demonstration_trace
    upstream = trace.upstream_trace
    first = upstream.outcomes[0]
    derivation = derive_source_coordinate(upstream, first)

    assert derivation.upstream_trace is upstream
    assert derivation.upstream_outcome is first
    assert derivation.initiation is first.initiation
    assert derivation.address.occurrence_index == first.admission.occurrence_index
    assert derivation.address.scope_cardinality == len(upstream.outcomes)
    assert derivation.derived_from_source_occurrence_address is True
    assert derivation.derived_from_content_or_digest is False
    assert "content-and-digest-not-used" in derivation.evidence

    with pytest.raises(SourceCoordinateError):
        replace(derivation, derived_from_content_or_digest=True)
    with pytest.raises(SourceCoordinateError):
        derive_source_coordinate(upstream, upstream.outcomes[1])
    with pytest.raises(SourceCoordinateError):
        replace(derivation, upstream_outcome=upstream.outcomes[1])


def test_source_coordinate_assignment_is_exact_and_reversible() -> None:
    report = run_v019_source_coordinate_derivation_experiment()
    applied = report.demonstration_trace.assignments[0]
    address = applied.derivation.address

    assert applied.exact_coordinate.local_transverse == address.local_transverse
    assert applied.exact_coordinate.lifted_turns == address.lifted_turns
    assert recover_signed_local_transverse(applied.exact_coordinate) == address.local_transverse
    expected_rendering = render_exact_coordinate_binary64(applied.exact_coordinate)
    assert applied.rendering.exact_coordinate == expected_rendering.exact_coordinate
    assert applied.rendering.rendering_identity == expected_rendering.rendering_identity
    assert applied.rendering.information_loss == expected_rendering.information_loss
    assert applied.rendering_role == BINARY64_RENDERING_STATUS
    assert applied.assignment.geometry is GeometryKind.CIRCLE
    assert applied.assignment.assignment_law_id == SOURCE_COORDINATE_LAW_ID
    assert applied.assignment.assignment_law_version == SOURCE_COORDINATE_LAW_VERSION
    assert applied.assignment.law_standing is LawStanding.CANDIDATE
    assert applied.assignment.orientation == address.frame.value
    assert applied.assignment.sidedness == address.local_side
    assert applied.completion_registered is False
    assert applied.selection_effect == "none"

    with pytest.raises(SourceCoordinateError):
        replace(
            applied,
            exact_coordinate=replace(
                applied.exact_coordinate,
                lifted_turns=Fraction(1),
            ),
        )
    with pytest.raises(SourceCoordinateError):
        replace(
            applied,
            assignment=replace(
                applied.assignment,
                assignment_law_version="wrong",
            ),
        )


def test_trace_retains_total_ordered_outcomes_and_blockers() -> None:
    report = run_v019_source_coordinate_derivation_experiment()
    trace = report.demonstration_trace
    upstream = trace.upstream_trace
    assert trace.has_total_outcome_evidence
    assert trace.outcome_relation_status == SOURCE_COORDINATE_OUTCOME_RELATION_STATUS
    assert tuple(item.upstream for item in trace.outcomes) == upstream.outcomes
    assert tuple(item.disposition for item in trace.outcomes) == (
        SourceCoordinateDisposition.DERIVED_ASSIGNED,
        SourceCoordinateDisposition.BLOCKED_UNRESOLVED,
        SourceCoordinateDisposition.BLOCKED_REJECTED,
    )
    assert trace.outcomes[1].applied_assignment is None
    assert trace.outcomes[2].applied_assignment is None

    with pytest.raises(SourceCoordinateError):
        replace(trace, outcomes=trace.outcomes[:1])
    with pytest.raises(SourceCoordinateError):
        replace(trace, outcomes=tuple(reversed(trace.outcomes)))
    with pytest.raises(SourceCoordinateError):
        replace(trace.outcomes[0], evidence=("invented evidence",))
    with pytest.raises(SourceCoordinateError):
        SourceCoordinateTrace(
            trace.trace_id,
            replace(upstream),
            trace.outcomes,
        )


def test_equal_content_is_separate_and_report_remains_nonselecting() -> None:
    report = run_v019_source_coordinate_derivation_experiment()
    base = report.upstream.upstream.demonstration_trace
    first, second = base.outcomes[:2]
    assert first.admission.subject_record.digest == second.admission.subject_record.digest

    boundary = StructuralNullManifestation(
        manifestation_id="v019-test:second-boundary",
        witness_id=second.admission.source_id,
        kind=StructuralNullKind.TURN_BOUNDARY,
        source_offset=None,
        source_value=None,
    )
    second_initiation = initiate_word_gonol(
        second.admission,
        gonol_id="v019-test:word-gonol:1",
        boundary_manifestation=boundary,
    )
    initiated_second = record_gonol_initiation_outcome(
        second.admission,
        initiation=second_initiation,
        evidence=("second equal-content occurrence explicitly initiated",),
    )
    assert initiated_second.disposition is GonolInitiationDisposition.INITIATED
    equal_content_trace = GonolInitiationTrace(
        "v019-test:equal-content-trace",
        (first, initiated_second),
    )
    derived = derive_source_coordinate_trace(equal_content_trace)
    assert len(derived.assignments) == 2
    assert derived.assignments[0].derivation.address.local_transverse == Fraction(-1, 2)
    assert derived.assignments[1].derivation.address.local_transverse == Fraction(1, 2)
    assert (
        derived.assignments[0].exact_coordinate.exact_identity
        != derived.assignments[1].exact_coordinate.exact_identity
    )

    assert report.schema_id == V019_SOURCE_COORDINATE_SCHEMA_ID
    assert report.schema_version == V019_SOURCE_COORDINATE_SCHEMA_VERSION
    assert report.law_status == SOURCE_COORDINATE_LAW_STATUS
    assert report.assignment_status == SOURCE_COORDINATE_ASSIGNMENT_STATUS
    assert report.arbitrary_source_assignment_status == ARBITRARY_SOURCE_ASSIGNMENT_STATUS
    assert report.selection_effect == "none"
    assert report.edcm_activation == report.metapat_activation == "inactive"
    assert report.hmmm == V019_HMMM
    assert tuple(item.falsifier_id for item in report.results) == SOURCE_COORDINATE_FALSIFIER_IDS
    assert report.result("SC06").standing is SourceCoordinateEvidenceStanding.NEGATIVE_SUPPORTED
    assert report.result("SC09").standing is SourceCoordinateEvidenceStanding.UNRESOLVED
    assert report.result("SC10").standing is SourceCoordinateEvidenceStanding.UNRESOLVED
