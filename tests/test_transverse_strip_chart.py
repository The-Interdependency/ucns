# === CHECKS ===
# id: check_transverse_strip_two_way_inverse
#   proves: transverse_strip_maps_are_exact_two_way_inverses
#   call: self::test_transverse_maps_are_exact_inverses_for_both_conventions
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_transverse_strip_all_witnesses
#   proves: transverse_strip_preserves_every_source_linked_witness
#   call: self::test_all_initiations_fibers_and_conventions_round_trip
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_transverse_strip_root_restriction
#   proves: transverse_strip_restricts_exactly_to_v07_root_loop
#   call: self::test_zero_fiber_restricts_exactly_to_v07_root_loop
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_transverse_strip_motion
#   proves: transverse_strip_commutes_with_bounded_motion
#   call: self::test_both_conventions_commute_with_all_declared_motion
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_transverse_convention_change
#   proves: transverse_coordinate_conventions_remain_reversible_and_nonselecting
#   call: self::test_local_and_global_coordinates_are_exact_reversible_conventions
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_transverse_strip_bounded_verdict
#   proves: transverse_strip_support_is_bounded_and_nonselecting
#   call: self::test_v08_report_is_complete_bounded_and_nonselecting
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from fractions import Fraction

from ucns.direct_mobius import build_native_mobius_initiation_packet
from ucns.mobius_experiment import (
    CarrierRelationship,
    FalsifierVerdict,
)
from ucns.root_loop_chart import mobius_to_root_loop_cover
from ucns.transverse_strip_chart import (
    TRANSVERSE_TRANSITION_LABELS,
    TRANSVERSE_WITNESS_VALUES,
    V08_TRANSVERSE_STRIP_SCHEMA_ID,
    V08_TRANSVERSE_STRIP_SCHEMA_VERSION,
    FramedMobiusStripState,
    TransverseCoordinateConvention,
    build_convention_motion_witnesses,
    build_convention_round_trips,
    build_root_loop_restrictions,
    build_transverse_motion_witnesses,
    build_transverse_round_trips,
    convert_transverse_convention,
    mobius_to_transverse_cover,
    run_v08_transverse_strip_experiment,
    transverse_cover_to_mobius,
)


def test_transverse_maps_are_exact_inverses_for_both_conventions() -> None:
    packet = build_native_mobius_initiation_packet()
    initial = packet.witness_initiations("W-first")[0].post_state
    states = (
        FramedMobiusStripState(initial, Fraction(-1)),
        FramedMobiusStripState(initial.advance(Fraction(1, 3)), Fraction(-2, 3)),
        FramedMobiusStripState(initial.advance(Fraction(7, 6)), Fraction(0)),
        FramedMobiusStripState(initial.advance(Fraction(-5, 4)), Fraction(3, 5)),
        FramedMobiusStripState(initial.advance(2), Fraction(1)),
    )

    for native in states:
        for convention in TransverseCoordinateConvention:
            cover = mobius_to_transverse_cover(native, convention)
            assert transverse_cover_to_mobius(cover) == native
            assert (
                mobius_to_transverse_cover(
                    transverse_cover_to_mobius(cover),
                    convention,
                )
                == cover
            )


def test_all_initiations_fibers_and_conventions_round_trip() -> None:
    packet = build_native_mobius_initiation_packet()
    rows = build_transverse_round_trips(packet)

    assert len(rows) == 14 * 3 * 2 == 84
    assert {item.native_original.local_transverse for item in rows} == set(
        TRANSVERSE_WITNESS_VALUES
    )
    assert {item.convention for item in rows} == set(
        TransverseCoordinateConvention
    )
    for item in rows:
        assert item.native_round_trip == item.native_original
        assert item.cover_round_trip == item.cover_image
        assert (
            item.cover_image.root_chart.source_links
            == item.native_original.root_state.source_links
        )
        assert (
            item.cover_image.root_chart.parent_observation_ids
            == item.native_original.root_state.parent_observation_ids
        )
        assert (
            item.cover_image.root_chart.initiation_event_id
            == item.event.event_id
        )
        assert (
            item.cover_image.root_chart.completion_scope
            == item.native_original.root_state.completion_scope
        )


def test_zero_fiber_restricts_exactly_to_v07_root_loop() -> None:
    packet = build_native_mobius_initiation_packet()
    restrictions = build_root_loop_restrictions(packet)

    assert len(restrictions) == 14 * 2 == 28
    for item in restrictions:
        event = next(
            event
            for event in packet.initiations
            if event.event_id == item.event_id
        )
        assert item.native_strip.root_state == event.post_state
        assert item.cover_strip.root_chart == mobius_to_root_loop_cover(
            event.post_state
        )
        assert item.cover_strip.local_transverse == 0
        assert item.cover_strip.global_transverse == 0


def test_both_conventions_commute_with_all_declared_motion() -> None:
    packet = build_native_mobius_initiation_packet()
    witnesses = build_transverse_motion_witnesses(packet)

    assert len(witnesses) == 14 * 3 * 2 * 4 == 336
    assert {item.label for item in witnesses} == set(
        TRANSVERSE_TRANSITION_LABELS
    )
    assert all(item.expected == item.observed for item in witnesses)

    event = packet.witness_initiations("W-first")[0]
    native = FramedMobiusStripState(event.post_state, Fraction(1))
    local = mobius_to_transverse_cover(
        native,
        TransverseCoordinateConvention.LOCAL_FRAME,
    )
    global_side = mobius_to_transverse_cover(
        native,
        TransverseCoordinateConvention.GLOBAL_SIDE,
    )
    assert local.advance(1).transverse_coordinate == 1
    assert global_side.advance(1).transverse_coordinate == -1
    assert local.advance(2).transverse_coordinate == 1
    assert global_side.advance(2).transverse_coordinate == 1


def test_local_and_global_coordinates_are_exact_reversible_conventions() -> None:
    packet = build_native_mobius_initiation_packet()
    round_trips = build_convention_round_trips(packet)
    commutations = build_convention_motion_witnesses(packet)

    assert len(round_trips) == 14 * 3 == 42
    assert len(commutations) == 14 * 3 * 4 == 168
    assert all(item.local_round_trip == item.local_state for item in round_trips)
    assert all(item.global_round_trip == item.global_state for item in round_trips)
    assert all(
        item.expected_global == item.observed_global for item in commutations
    )

    reversed_native = FramedMobiusStripState(
        packet.witness_initiations("W-first")[0].post_state.advance(1),
        Fraction(1),
    )
    local = mobius_to_transverse_cover(
        reversed_native,
        TransverseCoordinateConvention.LOCAL_FRAME,
    )
    global_side = convert_transverse_convention(
        local,
        TransverseCoordinateConvention.GLOBAL_SIDE,
    )
    assert local.transverse_coordinate == 1
    assert global_side.transverse_coordinate == -1
    assert convert_transverse_convention(
        global_side,
        TransverseCoordinateConvention.LOCAL_FRAME,
    ) == local


def test_v08_report_is_complete_bounded_and_nonselecting() -> None:
    report = run_v08_transverse_strip_experiment()

    assert report.schema_id == V08_TRANSVERSE_STRIP_SCHEMA_ID
    assert report.schema_version == V08_TRANSVERSE_STRIP_SCHEMA_VERSION
    assert report.selection_effect == "none"
    assert report.experiment.selection_effect == "none"
    assert len(report.round_trips) == 84
    assert len(report.root_restrictions) == 28
    assert len(report.motion_witnesses) == 336
    assert len(report.convention_round_trips) == 42
    assert len(report.convention_motion_witnesses) == 168
    assert len(report.experiment.results) == 48
    assert len(report.experiment.metric_displays) == 27
    assert (
        report.experiment.result(
            CarrierRelationship.COVER_CHART,
            "F12",
        ).verdict
        is FalsifierVerdict.SUPPORTED
    )
    assert (
        report.experiment.result(
            CarrierRelationship.INCOMPATIBLE,
            "F13",
        ).verdict
        is FalsifierVerdict.FALSIFIED
    )
    assert "transverse-round-trips:84" in report.experiment.result(
        CarrierRelationship.COVER_CHART,
        "F12",
    ).evidence
    assert "coordinate-change-commutations:168" in report.experiment.result(
        CarrierRelationship.COVER_CHART,
        "F12",
    ).evidence
    assert not hasattr(report, "selected_candidate")
    assert not hasattr(report, "selected_convention")
    assert any("finite witness packet" in item for item in report.hmmm)
    assert any("not canonical B" in item for item in report.hmmm)
    assert any("not promoted to scoped completion" in item for item in report.hmmm)
