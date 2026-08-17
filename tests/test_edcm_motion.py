# === CHECKS ===
# id: check_edcm_word_motion_binding
#   proves: edcm_motion_retains_trajectory_identity
#   call: self::test_word_motion_binding_preserves_exact_evidence
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_edcm_recursive_trace
#   proves: edcm_motion_retains_trajectory_identity
#   call: self::test_trace_preserves_order_parentage_and_completion
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_edcm_completion_scope
#   proves: edcm_completion_is_scoped_not_epistemic_exhaustion
#   call: self::test_completion_cannot_exhaust_the_underlying_unknowable
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_edcm_lossy_projection
#   proves: edcm_scalar_projection_is_declared_lossy
#   call: self::test_scalar_projection_requires_loss_and_source_link
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_edcm_parentage_fail_closed
#   proves: edcm_motion_retains_trajectory_identity
#   call: self::test_trace_rejects_forward_parentage
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_edcm_unknown_laws_visible
#   proves: edcm_unknown_motion_laws_remain_explicit
#   call: self::test_unknown_assignment_and_motion_laws_remain_visible
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.edcm import EdcmWordGonolProfile
from ucns.edcm_motion import (
    EDCM_ASSIGNMENT_LAW_STATUS,
    EDCM_HIGHER_MOTION_LAW_STATUS,
    CompletionRegistration,
    CompletionState,
    EdcmCompletionTrace,
    EdcmMetricFamily,
    EdcmMotionError,
    EpicyclicParentage,
    EvidenceStatus,
    GeometricAssignment,
    GeometryKind,
    HmmmBoundary,
    LawStanding,
    MotionStep,
    ScalarProjection,
    record_word_motion,
)


def _boundary() -> HmmmBoundary:
    return HmmmBoundary(
        boundary_id="construction:fixture",
        declaration="Complete the declared two-word fixture construction.",
        scope="fixture-only",
        unresolved_constraints=(
            "element-assignment law",
            "Mobius coordinate",
            "circle-to-disk transition",
        ),
    )


def _assignment(relation_id: str, geometry: GeometryKind) -> GeometricAssignment:
    return GeometricAssignment(
        relation_id=relation_id,
        geometry=geometry,
        assignment_law_id="fixture.explicit-assignment",
        assignment_law_version="0.1.0",
        law_standing=LawStanding.CANDIDATE,
        orientation="widdershins",
        sidedness="left",
        parameters=(("lane", "fixture-lane"),),
        evidence=("supplied fixture relation",),
    )


def _motion(
    step_id: str,
    to_relation_id: str,
    from_relation_id: str | None = None,
) -> MotionStep:
    return MotionStep(
        step_id=step_id,
        from_relation_id=from_relation_id,
        to_relation_id=to_relation_id,
        motion_law_id="fixture.explicit-motion",
        motion_law_version="0.1.0",
        law_standing=LawStanding.CANDIDATE,
        description="supplied ordered fixture motion",
        path_evidence=("before/after relation receipt",),
    )


def _completion(
    state: CompletionState,
    effect: str,
) -> CompletionRegistration:
    return CompletionRegistration(
        construction_id="fixture-construction",
        boundary_id="construction:fixture",
        condition_id="fixture-condition",
        state=state,
        effect=effect,
        evidence=("fixture completion receipt",),
        remaining_unresolved_capacity=(
            "underlying unknowable remains outside the declared boundary",
        ),
    )


def _turn():
    return EdcmWordGonolProfile().observe_turn(
        speaker_id="speaker-a",
        turn_index=3,
        text="Alpha beta",
        source_id="fixture-source",
    )


def _observation(
    *,
    observation_id: str,
    sequence_index: int,
    word_index: int,
    relation_id: str,
    geometry: GeometryKind,
    parentage: EpicyclicParentage,
    state: CompletionState,
    projections: tuple[ScalarProjection, ...] = (),
):
    prior = None if sequence_index == 0 else "relation:alpha"
    return record_word_motion(
        turn=_turn(),
        word_index=word_index,
        observation_id=observation_id,
        sequence_index=sequence_index,
        source_reference="fixture://dialogue/3",
        boundary=_boundary(),
        assignment=_assignment(relation_id, geometry),
        motion=_motion(f"step:{sequence_index}", relation_id, prior),
        parentage=parentage,
        completion=_completion(state, "candidate completion effect"),
        measurement_status=(
            EvidenceStatus.CANDIDATE_MEASURED
            if projections
            else EvidenceStatus.REPRESENTED
        ),
        scalar_projections=projections,
    )


def test_word_motion_binding_preserves_exact_evidence() -> None:
    observed = _observation(
        observation_id="observation:alpha",
        sequence_index=0,
        word_index=0,
        relation_id="relation:alpha",
        geometry=GeometryKind.CIRCLE,
        parentage=EpicyclicParentage("root", ()),
        state=CompletionState.IN_MOTION,
    )
    assert observed.element.raw_value == "Alpha"
    assert (observed.element.source_start, observed.element.source_end) == (0, 5)
    assert observed.element.grain == "word"
    assert observed.element.provenance.source_id == "fixture-source"
    assert observed.element.provenance.speaker_id == "speaker-a"
    assert observed.assignment.orientation == "widdershins"
    assert observed.assignment.sidedness == "left"


def test_trace_preserves_order_parentage_and_completion() -> None:
    alpha = _observation(
        observation_id="observation:alpha",
        sequence_index=0,
        word_index=0,
        relation_id="relation:alpha",
        geometry=GeometryKind.CIRCLE,
        parentage=EpicyclicParentage("root", ()),
        state=CompletionState.IN_MOTION,
    )
    beta = _observation(
        observation_id="observation:beta",
        sequence_index=1,
        word_index=1,
        relation_id="relation:beta",
        geometry=GeometryKind.EPICYCLE,
        parentage=EpicyclicParentage("epicycle-of", ("observation:alpha",)),
        state=CompletionState.REGISTERED,
    )
    trace = EdcmCompletionTrace(
        trace_id="trace:fixture",
        construction_id="fixture-construction",
        boundary=_boundary(),
    ).append(alpha).append(beta)
    assert [item.element.raw_value for item in trace.observations] == ["Alpha", "beta"]
    assert trace.observations[1].parentage.parent_observation_ids == (
        "observation:alpha",
    )
    assert trace.registered_complete
    assert trace.observations[-1].completion.underlying_unknowable_exhausted is False


def test_completion_cannot_exhaust_the_underlying_unknowable() -> None:
    with pytest.raises(EdcmMotionError, match="underlying unknowable"):
        replace(
            _completion(CompletionState.REGISTERED, "complete"),
            underlying_unknowable_exhausted=True,
        )


def test_scalar_projection_requires_loss_and_source_link() -> None:
    with pytest.raises(EdcmMotionError, match="information_loss"):
        ScalarProjection(
            metric_family=EdcmMetricFamily.DRIFT,
            value=0.25,
            unit="candidate-ratio",
            policy_id="fixture.drift",
            policy_version="0.1.0",
            source_observation_id="observation:alpha",
            information_loss=(),
        )

    projection = ScalarProjection(
        metric_family=EdcmMetricFamily.DRIFT,
        value=0.25,
        unit="candidate-ratio",
        policy_id="fixture.drift",
        policy_version="0.1.0",
        source_observation_id="wrong-observation",
        information_loss=("epicyclic path is not represented by one scalar",),
    )
    with pytest.raises(EdcmMotionError, match="complete source observation"):
        _observation(
            observation_id="observation:alpha",
            sequence_index=0,
            word_index=0,
            relation_id="relation:alpha",
            geometry=GeometryKind.CIRCLE,
            parentage=EpicyclicParentage("root", ()),
            state=CompletionState.IN_MOTION,
            projections=(projection,),
        )

    linked = replace(
        projection,
        source_observation_id="observation:alpha",
    )
    observed = _observation(
        observation_id="observation:alpha",
        sequence_index=0,
        word_index=0,
        relation_id="relation:alpha",
        geometry=GeometryKind.CIRCLE,
        parentage=EpicyclicParentage("root", ()),
        state=CompletionState.IN_MOTION,
        projections=(linked,),
    )
    trace = EdcmCompletionTrace(
        trace_id="trace:projection",
        construction_id="fixture-construction",
        boundary=_boundary(),
        observations=(observed,),
    )
    assert trace.observations[0] is observed
    assert trace.scalar_projections == (linked,)
    assert linked.metric_family.code == "DRIFT"
    assert "epicyclic path" in linked.information_loss[0]


def test_trace_rejects_forward_parentage() -> None:
    forward = _observation(
        observation_id="observation:alpha",
        sequence_index=0,
        word_index=0,
        relation_id="relation:alpha",
        geometry=GeometryKind.CIRCLE,
        parentage=EpicyclicParentage("epicycle-of", ("observation:future",)),
        state=CompletionState.IN_MOTION,
    )
    with pytest.raises(EdcmMotionError, match="earlier observation"):
        EdcmCompletionTrace(
            trace_id="trace:fixture",
            construction_id="fixture-construction",
            boundary=_boundary(),
            observations=(forward,),
        )


def test_unknown_assignment_and_motion_laws_remain_visible() -> None:
    assert EDCM_ASSIGNMENT_LAW_STATUS == "hmmm-unresolved"
    assert EDCM_HIGHER_MOTION_LAW_STATUS == "hmmm-unresolved"
    assert {standing.value for standing in LawStanding} == {
        "unresolved",
        "experiment-candidate",
    }
    assert "canonical" not in {standing.value for standing in LawStanding}
