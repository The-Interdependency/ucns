# === CHECKS ===
# id: check_root_loop_chart_two_way_inverse
#   proves: root_loop_chart_maps_are_exact_two_way_inverses
#   call: self::test_chart_maps_are_exact_inverses_for_rational_root_loop_states
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_root_loop_chart_all_initiations
#   proves: root_loop_chart_preserves_every_source_linked_initiation
#   call: self::test_all_fourteen_initiations_round_trip_without_evidence_loss
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_root_loop_chart_commutation
#   proves: root_loop_chart_commutes_with_bounded_motion
#   call: self::test_chart_commutes_with_initiation_360_720_and_inverse
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_root_loop_chart_sheet_hypothesis
#   proves: root_loop_chart_uses_cover_sheet_as_hypothesis_not_native_orientation
#   call: self::test_sheet_correspondence_materializes_on_existing_cover_without_mutation
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_root_loop_chart_bounded_verdict
#   proves: root_loop_chart_support_is_bounded_and_nonselecting
#   call: self::test_v07_report_supports_f12_only_on_bounded_domain_without_selection
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from fractions import Fraction

from ucns.carrier import LiftedCarrierPoint, project, same_visible_position
from ucns.direct_mobius import (
    NativeMobiusFrame,
    build_native_mobius_initiation_packet,
)
from ucns.mobius_experiment import (
    REQUIRED_COMMUTATION_LABELS,
    REQUIRED_MAP_DISTINCTIONS,
    CarrierRelationship,
    FalsifierVerdict,
)
from ucns.root_loop_chart import (
    ROOT_LOOP_CHART_SCOPE,
    V07_ROOT_LOOP_CHART_SCHEMA_ID,
    V07_ROOT_LOOP_CHART_SCHEMA_VERSION,
    build_root_loop_chart_evidence,
    build_root_loop_chart_round_trips,
    mobius_to_root_loop_cover,
    root_loop_cover_to_mobius,
    run_v07_root_loop_chart_experiment,
)


def test_chart_maps_are_exact_inverses_for_rational_root_loop_states() -> None:
    packet = build_native_mobius_initiation_packet()
    initial = packet.witness_initiations("W-first")[0].post_state
    states = (
        initial,
        initial.advance(Fraction(1, 3)),
        initial.advance(Fraction(7, 6)),
        initial.advance(Fraction(-5, 4)),
        initial.advance(1),
        initial.advance(2),
    )

    for state in states:
        cover = mobius_to_root_loop_cover(state)
        assert root_loop_cover_to_mobius(cover) == state
        assert mobius_to_root_loop_cover(root_loop_cover_to_mobius(cover)) == cover
        assert cover.chart_scope == ROOT_LOOP_CHART_SCOPE


def test_all_fourteen_initiations_round_trip_without_evidence_loss() -> None:
    packet = build_native_mobius_initiation_packet()
    round_trips = build_root_loop_chart_round_trips(packet)

    assert len(round_trips) == len(packet.initiations) == 14
    assert tuple(item.event.event_id for item in round_trips) == tuple(
        item.event_id for item in packet.initiations
    )
    for item in round_trips:
        assert item.mobius_round_trip == item.mobius_original
        assert item.cover_round_trip == item.cover_image
        assert item.cover_image.source_links == item.mobius_original.source_links
        assert (
            item.cover_image.parent_observation_ids
            == item.mobius_original.parent_observation_ids
        )
        assert (
            item.cover_image.initiation_event_id
            == item.event.event_id
            == item.mobius_original.initiation_event_id
        )
        assert (
            item.cover_image.completion_scope
            == item.mobius_original.completion_scope
        )
        assert (
            f"boundary:{item.event.boundary.manifestation_id}"
            in item.cover_image.source_links
        )


def test_chart_commutes_with_initiation_360_720_and_inverse() -> None:
    evidence = build_root_loop_chart_evidence(
        build_native_mobius_initiation_packet()
    )

    assert tuple(item.label for item in evidence.commutation_witnesses) == (
        "initiation",
        "advance-360",
        "advance-720",
        "inverse",
    )
    assert tuple(item.label for item in evidence.commutation_witnesses) == (
        REQUIRED_COMMUTATION_LABELS
    )
    for witness in evidence.commutation_witnesses:
        assert (
            witness.expected.complete_identity
            == witness.observed.complete_identity
        )
    assert evidence.preserved_distinctions == REQUIRED_MAP_DISTINCTIONS
    assert evidence.information_loss == ()


def test_sheet_correspondence_materializes_on_existing_cover_without_mutation() -> None:
    packet = build_native_mobius_initiation_packet()
    initial = packet.witness_initiations("W-first")[0].post_state
    first = mobius_to_root_loop_cover(initial.advance(Fraction(1, 4)))
    second = mobius_to_root_loop_cover(initial.advance(Fraction(5, 4)))

    assert first.mapped_frame is NativeMobiusFrame.POSITIVE
    assert second.mapped_frame is NativeMobiusFrame.REVERSED
    assert first.sheet == "first-lifted-representative"
    assert second.sheet == "second-lifted-representative"
    assert isinstance(first.materialized_point, LiftedCarrierPoint)
    assert isinstance(second.materialized_point, LiftedCarrierPoint)
    assert same_visible_position(
        project(first.materialized_point),
        project(second.materialized_point),
    )
    for field in ("orientation", "frame", "mapped_frame"):
        assert not hasattr(first.materialized_point, field)


def test_v07_report_supports_f12_only_on_bounded_domain_without_selection() -> None:
    report = run_v07_root_loop_chart_experiment()

    assert report.schema_id == V07_ROOT_LOOP_CHART_SCHEMA_ID
    assert report.schema_version == V07_ROOT_LOOP_CHART_SCHEMA_VERSION
    assert report.selection_effect == "none"
    assert report.experiment.selection_effect == "none"
    assert len(report.round_trips) == 14
    assert len(report.experiment.results) == 48
    assert len(report.experiment.metric_displays) == 27
    assert report.chart_evidence.witness_domain == tuple(
        item.witness_id for item in report.direct_report.packet.witnesses
    )
    assert (
        report.experiment.result(
            CarrierRelationship.COVER_CHART,
            "F12",
        ).verdict
        is FalsifierVerdict.SUPPORTED
    )
    assert "initiation-round-trips:14" in report.experiment.result(
        CarrierRelationship.COVER_CHART,
        "F12",
    ).evidence
    assert "commutation-witnesses:4" in report.experiment.result(
        CarrierRelationship.COVER_CHART,
        "F12",
    ).evidence
    assert (
        report.experiment.result(
            CarrierRelationship.INCOMPATIBLE,
            "F13",
        ).verdict
        is FalsifierVerdict.FALSIFIED
    )
    assert not hasattr(report, "selected_candidate")
    assert any("only" in item and "root-loop" in item for item in report.hmmm)
    assert any("not canonical B" in item for item in report.hmmm)
    assert any("not promoted to scoped completion" in item for item in report.hmmm)
