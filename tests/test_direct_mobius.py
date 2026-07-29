# === CHECKS ===
# id: check_direct_mobius_structural_null_identity
#   proves: direct_mobius_structural_null_is_typed_and_source_preserving
#   call: self::test_structural_null_is_singular_typed_and_source_preserving
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_direct_mobius_initiation_cardinality
#   proves: direct_mobius_initiation_is_causal_and_cardinality_exact
#   call: self::test_every_word_has_one_exact_causal_initiation
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_direct_mobius_repeated_space
#   proves: direct_mobius_repeated_space_preserves_singular_origin_and_occurrences
#   call: self::test_repeated_space_retains_two_manifestations_and_immediate_cause
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_direct_mobius_native_motion
#   proves: direct_mobius_native_motion_has_360_change_720_return_and_inverse
#   call: self::test_native_quotient_motion_is_exact_for_360_720_and_inverse
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_direct_mobius_candidate_independence
#   proves: direct_mobius_candidate_is_independent_and_nonselecting
#   call: self::test_native_trace_supports_motion_and_independence_without_selection
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_direct_mobius_frontier_retention
#   proves: direct_mobius_report_retains_unresolved_frontier
#   call: self::test_v06_report_retains_complete_matrix_and_unresolved_frontier
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from fractions import Fraction

import pytest

from ucns.direct_mobius import (
    STRUCTURAL_NULL_ORIGIN,
    V06_DIRECT_MOBIUS_SCHEMA_ID,
    V06_DIRECT_MOBIUS_SCHEMA_VERSION,
    DirectMobiusError,
    NativeMobiusFrame,
    StructuralNullKind,
    build_native_mobius_initiation_packet,
    native_direct_mobius_trace,
    run_v06_direct_mobius_experiment,
)
from ucns.mobius_experiment import (
    CarrierRelationship,
    FalsifierVerdict,
    evaluate_candidate_trace,
)


def test_structural_null_is_singular_typed_and_source_preserving() -> None:
    packet = build_native_mobius_initiation_packet()
    turn_boundaries = tuple(
        item
        for item in packet.manifestations
        if item.kind is StructuralNullKind.TURN_BOUNDARY
    )
    exact_spaces = tuple(
        item
        for item in packet.manifestations
        if item.kind is StructuralNullKind.SPACE_MANIFESTATION
    )

    assert len(packet.witnesses) == 9
    assert len(turn_boundaries) == 9
    assert len(exact_spaces) == 7
    assert len(packet.manifestations) == 16
    assert all(item.origin is STRUCTURAL_NULL_ORIGIN for item in packet.manifestations)
    assert STRUCTURAL_NULL_ORIGIN != 0
    assert STRUCTURAL_NULL_ORIGIN != "0"
    assert STRUCTURAL_NULL_ORIGIN != ""
    assert STRUCTURAL_NULL_ORIGIN is not None

    nbsp = tuple(
        item
        for item in packet.witness_manifestations("W-nbsp")
        if item.kind is StructuralNullKind.SPACE_MANIFESTATION
    )
    assert len(nbsp) == 1
    assert nbsp[0].source_value == "\u00a0"
    assert nbsp[0].source_offset == 1
    assert nbsp[0].source_reference.endswith("offset:1:U+00A0")


def test_every_word_has_one_exact_causal_initiation() -> None:
    packet = build_native_mobius_initiation_packet()
    expected_word_count = sum(
        len(witness.turn.word_gonols) for witness in packet.witnesses
    )

    assert expected_word_count == 14
    assert len(packet.initiations) == expected_word_count
    for witness in packet.witnesses:
        events = packet.witness_initiations(witness.witness_id)
        assert len(events) == len(witness.turn.word_gonols)
        for event, word in zip(events, witness.turn.word_gonols, strict=True):
            assert event.word_index == word.word_index
            assert event.source_start == word.source_start
            assert event.post_state.initiation_event_id == event.event_id
            assert event.post_state.phase_turns == 0
            assert event.post_state.frame is NativeMobiusFrame.POSITIVE

    first = packet.witness_initiations("W-first")
    assert len(first) == 1
    assert first[0].boundary.kind is StructuralNullKind.TURN_BOUNDARY
    assert first[0].boundary.source_value is None

    spaced = packet.witness_initiations("W-space")
    assert len(spaced) == 2
    assert spaced[0].boundary.kind is StructuralNullKind.TURN_BOUNDARY
    assert spaced[1].boundary.kind is StructuralNullKind.SPACE_MANIFESTATION
    assert spaced[1].boundary.source_offset == 1
    assert spaced[1].boundary.source_value == " "


def test_repeated_space_retains_two_manifestations_and_immediate_cause() -> None:
    packet = build_native_mobius_initiation_packet()
    witness = next(item for item in packet.witnesses if item.witness_id == "W-repeat-space")
    spaces = tuple(
        item
        for item in packet.witness_manifestations("W-repeat-space")
        if item.kind is StructuralNullKind.SPACE_MANIFESTATION
    )
    events = packet.witness_initiations("W-repeat-space")

    assert witness.turn.raw_text == "A  B"
    assert "".join(segment.raw_text for segment in witness.turn.segments) == "A  B"
    assert tuple(item.source_offset for item in spaces) == (1, 2)
    assert tuple(item.source_value for item in spaces) == (" ", " ")
    assert spaces[0].manifestation_id != spaces[1].manifestation_id
    assert spaces[0].origin is spaces[1].origin is STRUCTURAL_NULL_ORIGIN
    assert len(events) == 2
    assert events[1].source_start == 3
    assert events[1].boundary is spaces[1]


def test_native_quotient_motion_is_exact_for_360_720_and_inverse() -> None:
    packet = build_native_mobius_initiation_packet()
    initial = packet.witness_initiations("W-first")[0].post_state
    half = initial.advance(Fraction(1, 2))
    after_360 = initial.advance(1)
    after_720 = initial.advance(2)
    inverse = after_360.advance(-1)

    assert half.phase_turns == Fraction(1, 2)
    assert half.frame is NativeMobiusFrame.POSITIVE
    assert half.advance(Fraction(1, 2)) == after_360
    assert after_360.phase_turns == initial.phase_turns == 0
    assert after_360.frame is NativeMobiusFrame.REVERSED
    assert after_360.visible_key == initial.visible_key
    assert after_360.complete_key != initial.complete_key
    assert after_720 == initial
    assert inverse == initial
    assert initial.advance(-1).advance(1) == initial

    with pytest.raises(DirectMobiusError, match="exact Fraction"):
        initial.advance(0.5)


def test_native_trace_supports_motion_and_independence_without_selection() -> None:
    trace = native_direct_mobius_trace()
    results = {
        item.falsifier_id: item for item in evaluate_candidate_trace(trace)
    }

    assert trace.candidate is CarrierRelationship.DIRECT_MOBIUS
    assert trace.declared_dependencies == ()
    assert trace.native_independence_evidence
    assert trace.initial.sheet == "not-applicable-native-mobius"
    assert trace.after_360.sheet == "not-applicable-native-mobius"
    for falsifier_id in ("F06", "F07", "F08", "F14"):
        assert results[falsifier_id].verdict is FalsifierVerdict.SUPPORTED
    assert results["F09"].verdict is FalsifierVerdict.UNRESOLVED
    assert trace.after_720.completion_receipt is None


def test_v06_report_retains_complete_matrix_and_unresolved_frontier() -> None:
    report = run_v06_direct_mobius_experiment()

    assert report.schema_id == V06_DIRECT_MOBIUS_SCHEMA_ID
    assert report.schema_version == V06_DIRECT_MOBIUS_SCHEMA_VERSION
    assert report.selection_effect == "none"
    assert report.experiment.selection_effect == "none"
    assert report.experiment.relationships == tuple(CarrierRelationship)
    assert len(report.experiment.results) == 48
    assert len(report.experiment.metric_displays) == 27
    assert len(report.packet.initiations) == 14

    for falsifier_id in ("F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08", "F14", "F15"):
        assert (
            report.experiment.result(
                CarrierRelationship.DIRECT_MOBIUS,
                falsifier_id,
            ).verdict
            is FalsifierVerdict.SUPPORTED
        )
    assert (
        report.experiment.result(
            CarrierRelationship.DIRECT_MOBIUS,
            "F09",
        ).verdict
        is FalsifierVerdict.UNRESOLVED
    )
    assert (
        report.experiment.result(
            CarrierRelationship.COVER_CHART,
            "F12",
        ).verdict
        is FalsifierVerdict.UNRESOLVED
    )
    assert (
        report.experiment.result(
            CarrierRelationship.INCOMPATIBLE,
            "F13",
        ).verdict
        is FalsifierVerdict.UNRESOLVED
    )
    assert any("arbitrary element assignment" in item for item in report.hmmm)
    assert any("not promoted to scoped completion" in item for item in report.hmmm)
