# === CHECKS ===
# id: check_v05_minimum_witness_packet
#   proves: mobius_experiment_preserves_minimum_source_witnesses
#   call: self::test_minimum_witness_packet_preserves_exact_source_and_support
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_v05_directed_cover_motion
#   proves: directed_cover_experiment_reports_360_change_and_720_return
#   call: self::test_directed_cover_trace_reports_360_change_720_return_and_inverse
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_v05_complete_relationship_matrix
#   proves: carrier_experiment_preserves_three_relationships_without_selection
#   call: self::test_report_retains_all_relationships_and_falsifiers_without_selection
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_v05_direct_candidate_stays_candidate
#   proves: carrier_experiment_preserves_three_relationships_without_selection
#   call: self::test_direct_trace_is_evaluated_without_promotion
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_v05_chart_separation
#   proves: chart_and_incompatibility_evidence_remain_separating
#   call: self::test_chart_map_success_and_round_trip_failure_separate_c2_from_c3
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_v05_incompatibility_witness
#   proves: chart_and_incompatibility_evidence_remain_separating
#   call: self::test_complete_failed_map_witness_supports_incompatibility_only
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_v05_metric_grid
#   proves: carrier_experiment_displays_all_metric_candidates_without_zero_fill
#   call: self::test_metric_grid_displays_all_nine_combinations_without_values
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_v05_comparison_error_receipt
#   proves: carrier_experiment_retains_evaluation_errors
#   call: self::test_comparison_policy_exception_is_retained_as_error
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

from ucns.comparison import custom_comparison_policy, exact_comparison_policy
from ucns.mobius_experiment import (
    BREADTH_CANDIDATE_IDS,
    FALSIFIER_IDS,
    MINIMUM_WITNESS_TEXTS,
    PRODUCT_CANDIDATE_IDS,
    REQUIRED_COMMUTATION_LABELS,
    REQUIRED_MAP_DISTINCTIONS,
    CandidateTrace,
    CarrierExperimentState,
    CarrierMapEvidence,
    CarrierRelationship,
    FalsifierVerdict,
    MapCommutationWitness,
    SeparatingWitness,
    build_v05_witness_packet,
    directed_cover_trace,
    evaluate_candidate_trace,
    run_v05_carrier_experiment,
)


def _direct_state(
    state_id: str,
    complete_phase: str,
    *,
    orientation: str,
    sheet: str,
    completion_receipt: str | None = None,
) -> CarrierExperimentState:
    return CarrierExperimentState(
        candidate=CarrierRelationship.DIRECT_MOBIUS,
        state_id=state_id,
        complete_key=(("native-phase", complete_phase),),
        visible_key=(("visible-phase", "0-degrees"),),
        orientation=orientation,
        sidedness="declared-native-side",
        sheet=sheet,
        source_links=("synthetic-direct-mobius-state:s",),
        parent_observation_ids=(),
        completion_scope="direct-mobius-candidate-only",
        initiation_event_id="initiation:synthetic-s",
        completion_receipt=completion_receipt,
    )


def _direct_trace() -> CandidateTrace:
    return CandidateTrace(
        candidate=CarrierRelationship.DIRECT_MOBIUS,
        version="fixture/1",
        code_reference="tests.test_mobius_experiment:_direct_trace",
        comparison_policy=exact_comparison_policy(
            name="direct-mobius-fixture-exact",
            version="1",
        ),
        initial=_direct_state(
            "mobius:s",
            "0",
            orientation="front",
            sheet="first",
        ),
        after_360=_direct_state(
            "mobius:s+360",
            "360",
            orientation="back",
            sheet="second",
        ),
        after_720=_direct_state(
            "mobius:s+720",
            "0",
            orientation="front",
            sheet="first",
        ),
        inverse_after_360=_direct_state(
            "mobius:inverse(s+360)",
            "0",
            orientation="front",
            sheet="first",
        ),
        native_independence_evidence=(
            "fixture native state supplies phase and orientation without C2",
        ),
    )


def _chart_evidence(
    *,
    bad_cover_round_trip: bool = False,
) -> CarrierMapEvidence:
    cover = directed_cover_trace()
    mobius = _direct_trace()
    return CarrierMapEvidence(
        map_id="fixture.cover-mobius-map",
        version="1",
        code_reference="tests.test_mobius_experiment:_chart_evidence",
        comparison_policy=exact_comparison_policy(
            name="chart-map-fixture-exact",
            version="1",
        ),
        cover_original=cover.initial,
        cover_round_trip=(
            cover.after_360 if bad_cover_round_trip else cover.initial
        ),
        mobius_original=mobius.initial,
        mobius_round_trip=mobius.initial,
        commutation_witnesses=(
            MapCommutationWitness("initiation", mobius.initial, mobius.initial),
            MapCommutationWitness(
                "advance-360",
                mobius.after_360,
                mobius.after_360,
            ),
            MapCommutationWitness(
                "advance-720",
                mobius.after_720,
                mobius.after_720,
            ),
            MapCommutationWitness(
                "inverse",
                mobius.inverse_after_360,
                mobius.inverse_after_360,
            ),
        ),
        preserved_distinctions=REQUIRED_MAP_DISTINCTIONS,
        information_loss=(),
        witness_domain=("W-first", "synthetic-state:s"),
    )


def test_minimum_witness_packet_preserves_exact_source_and_support() -> None:
    packet = build_v05_witness_packet()
    assert tuple(item.witness_id for item in packet) == tuple(
        item[0] for item in MINIMUM_WITNESS_TEXTS
    )
    assert tuple(item.turn.raw_text for item in packet) == tuple(
        item[1] for item in MINIMUM_WITNESS_TEXTS
    )
    assert all(item.turn.unit_support == 1.0 for item in packet)
    assert all(
        "".join(segment.raw_text for segment in item.turn.segments)
        == item.turn.raw_text
        for item in packet
    )

    by_id = {item.witness_id: item.turn for item in packet}
    assert by_id["W-space"].nesting_boundaries[0].raw_text == " "
    assert by_id["W-nbsp"].nesting_boundaries[0].raw_text == "\u00a0"
    assert (
        by_id["W-space"].nesting_boundaries[0].token.alphabet_position
        == by_id["W-nbsp"].nesting_boundaries[0].token.alphabet_position
        == 0
    )
    assert len(by_id["W-repeat-space"].nesting_boundaries) == 2
    assert [word.raw_text for word in by_id["W-repeat-word"].word_gonols] == [
        "AB",
        "AB",
    ]
    assert [token.value for token in by_id["W-unassigned"].carrier_unassigned] == [
        "🙂"
    ]


def test_directed_cover_trace_reports_360_change_720_return_and_inverse() -> None:
    trace = directed_cover_trace()
    results = {item.falsifier_id: item for item in evaluate_candidate_trace(trace)}
    assert trace.candidate is CarrierRelationship.COVER_CHART
    assert (
        trace.initial.visible_identity
        == trace.after_360.visible_identity
        == trace.after_720.visible_identity
    )
    assert trace.initial.complete_identity != trace.after_360.complete_identity
    assert trace.initial.complete_identity == trace.after_720.complete_identity
    assert trace.initial.complete_identity == trace.inverse_after_360.complete_identity
    assert results["F06"].verdict is FalsifierVerdict.SUPPORTED
    assert results["F07"].verdict is FalsifierVerdict.SUPPORTED
    assert results["F08"].verdict is FalsifierVerdict.SUPPORTED
    assert results["F09"].verdict is FalsifierVerdict.UNRESOLVED
    assert "completion" in results["F09"].detail


def test_report_retains_all_relationships_and_falsifiers_without_selection() -> None:
    report = run_v05_carrier_experiment()
    assert report.relationships == tuple(CarrierRelationship)
    assert len(report.results) == len(CarrierRelationship) * len(FALSIFIER_IDS)
    assert report.selection_effect == "none"
    assert not hasattr(report, "selected_candidate")
    assert report.hmmm

    assert (
        report.result(CarrierRelationship.DIRECT_MOBIUS, "F06").verdict
        is FalsifierVerdict.UNRESOLVED
    )
    assert (
        report.result(CarrierRelationship.COVER_CHART, "F06").verdict
        is FalsifierVerdict.SUPPORTED
    )
    assert (
        report.result(CarrierRelationship.COVER_CHART, "F12").verdict
        is FalsifierVerdict.UNRESOLVED
    )
    assert (
        report.result(CarrierRelationship.INCOMPATIBLE, "F13").verdict
        is FalsifierVerdict.UNRESOLVED
    )


def test_direct_trace_is_evaluated_without_promotion() -> None:
    report = run_v05_carrier_experiment(direct_trace=_direct_trace())
    for falsifier_id in ("F06", "F07", "F08", "F14"):
        assert (
            report.result(
                CarrierRelationship.DIRECT_MOBIUS,
                falsifier_id,
            ).verdict
            is FalsifierVerdict.SUPPORTED
        )
    assert (
        report.result(CarrierRelationship.DIRECT_MOBIUS, "F09").verdict
        is FalsifierVerdict.UNRESOLVED
    )
    assert report.selection_effect == "none"


def test_chart_map_success_and_round_trip_failure_separate_c2_from_c3() -> None:
    supported = run_v05_carrier_experiment(
        direct_trace=_direct_trace(),
        chart_map=_chart_evidence(),
    )
    assert (
        supported.result(CarrierRelationship.COVER_CHART, "F12").verdict
        is FalsifierVerdict.SUPPORTED
    )
    assert (
        supported.result(CarrierRelationship.INCOMPATIBLE, "F13").verdict
        is FalsifierVerdict.FALSIFIED
    )

    failed = run_v05_carrier_experiment(
        direct_trace=_direct_trace(),
        chart_map=_chart_evidence(bad_cover_round_trip=True),
    )
    assert (
        failed.result(CarrierRelationship.COVER_CHART, "F12").verdict
        is FalsifierVerdict.FALSIFIED
    )
    assert (
        failed.result(CarrierRelationship.INCOMPATIBLE, "F13").verdict
        is FalsifierVerdict.UNRESOLVED
    )
    assert set(REQUIRED_COMMUTATION_LABELS) == {
        item.label for item in _chart_evidence().commutation_witnesses
    }


def test_complete_failed_map_witness_supports_incompatibility_only() -> None:
    cover = directed_cover_trace()
    witness = SeparatingWitness(
        witness_id="synthetic-state:s-vs-s+360",
        comparison_policy=cover.comparison_policy,
        left_state=cover.initial,
        right_state=cover.after_360,
        admissible_map_ids=("map:a", "map:b"),
        failed_map_ids=("map:a", "map:b"),
        violated_invariant="complete lifted representative",
        maps_identify_states=True,
        detail="both attempted maps retain only the visible 360-degree key",
        rollback_behavior="retain both representations and failed-map receipts",
    )
    report = run_v05_carrier_experiment(separating_witness=witness)
    assert (
        report.result(CarrierRelationship.INCOMPATIBLE, "F13").verdict
        is FalsifierVerdict.SUPPORTED
    )
    assert report.selection_effect == "none"

    incomplete = replace(witness, failed_map_ids=("map:a",))
    inconclusive = run_v05_carrier_experiment(
        separating_witness=incomplete
    ).result(CarrierRelationship.INCOMPATIBLE, "F13")
    assert inconclusive.verdict is FalsifierVerdict.INCONCLUSIVE


def test_metric_grid_displays_all_nine_combinations_without_values() -> None:
    report = run_v05_carrier_experiment()
    assert len(report.metric_displays) == len(CarrierRelationship) * 9
    for relationship in CarrierRelationship:
        displays = tuple(
            item
            for item in report.metric_displays
            if item.relationship is relationship
        )
        assert {
            (item.product_candidate_id, item.breadth_candidate_id)
            for item in displays
        } == {
            (product_id, breadth_id)
            for product_id in PRODUCT_CANDIDATE_IDS
            for breadth_id in BREADTH_CANDIDATE_IDS
        }
        assert all(item.value is None for item in displays)
        assert all(
            item.verdict is FalsifierVerdict.UNRESOLVED for item in displays
        )
        assert (
            report.result(relationship, "F15").verdict
            is FalsifierVerdict.SUPPORTED
        )


def test_comparison_policy_exception_is_retained_as_error() -> None:
    def raising_comparator(left, right):
        raise RuntimeError("fixture comparison failure")

    broken = replace(
        _direct_trace(),
        comparison_policy=custom_comparison_policy(
            "raising-fixture",
            raising_comparator,
            version="1",
            code_reference=(
                "tests.test_mobius_experiment:"
                "test_comparison_policy_exception_is_retained_as_error"
            ),
        ),
    )
    report = run_v05_carrier_experiment(direct_trace=broken)
    result = report.result(CarrierRelationship.DIRECT_MOBIUS, "F06")
    assert result.verdict is FalsifierVerdict.ERROR
    assert result.error == "RuntimeError: fixture comparison failure"
    assert len(report.results) == len(CarrierRelationship) * len(FALSIFIER_IDS)
