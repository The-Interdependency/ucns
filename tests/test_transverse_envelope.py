# === CHECKS ===
# id: check_transverse_envelope_exact_round_trip
#   proves: transverse_envelope_maps_preserve_exact_rational_state
#   call: self::test_parametric_exact_rational_maps_and_motion
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_transverse_envelope_convention_round_trip
#   proves: transverse_envelope_maps_preserve_exact_rational_state
#   call: self::test_local_and_global_descriptions_remain_reversible
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_transverse_envelope_explicit_policy
#   proves: transverse_envelope_comparison_policy_is_explicit
#   call: self::test_every_witness_retains_the_pinned_exact_policy
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_transverse_envelope_witness_identities
#   proves: transverse_envelope_report_validates_complete_witness_identities
#   call: self::test_report_rejects_count_preserving_identity_substitution
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_transverse_envelope_root_restriction
#   proves: transverse_envelope_restricts_exactly_to_v07_root_loop
#   call: self::test_zero_sidecar_restricts_exactly_to_v07
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_transverse_envelope_cover_collision
#   proves: transverse_envelope_exposes_cover_nonembedding
#   call: self::test_distinct_transverse_values_collide_in_the_actual_cover
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_transverse_envelope_verdict_boundary
#   proves: transverse_envelope_does_not_extend_cover_verdicts
#   call: self::test_v09_report_keeps_transverse_cover_extension_inconclusive
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction

import pytest

from ucns.direct_mobius import build_native_mobius_initiation_packet
from ucns.mobius_experiment import CarrierRelationship, FalsifierVerdict
from ucns.root_loop_chart import (
    ROOT_LOOP_CHART_MAP_ID,
    ROOT_LOOP_CHART_MAP_VERSION,
    mobius_to_root_loop_cover,
)
from ucns.transverse_envelope import (
    TRANSVERSE_COMPARISON_POLICY_NAME,
    TRANSVERSE_COMPARISON_POLICY_VERSION,
    TRANSVERSE_ENVELOPE_ADAPTER_ID,
    TRANSVERSE_ENVELOPE_ADAPTER_VERSION,
    TRANSVERSE_STRESS_MAX_DENOMINATOR,
    V09_TRANSVERSE_ENVELOPE_SCHEMA_ID,
    V09_TRANSVERSE_ENVELOPE_SCHEMA_VERSION,
    FramedMobiusStripState,
    TransverseCoordinateConvention,
    TransverseEnvelopeError,
    convert_transverse_convention,
    exact_rational_stress_fibers,
    mobius_to_transverse_envelope,
    run_v09_transverse_envelope_experiment,
    transverse_envelope_to_mobius,
    transverse_exact_comparison_policy,
)


@pytest.fixture(scope="module")
def report():
    return run_v09_transverse_envelope_experiment()


def test_parametric_exact_rational_maps_and_motion() -> None:
    packet = build_native_mobius_initiation_packet()
    root = packet.witness_initiations("W-first")[0].post_state
    policy = transverse_exact_comparison_policy()
    transverse_values = (
        Fraction(-1),
        Fraction(-97, 101),
        Fraction(-2, 3),
        Fraction(0),
        Fraction(3, 5),
        Fraction(997, 1000),
        Fraction(1),
    )
    turns = (
        Fraction(-19, 7),
        Fraction(-1),
        Fraction(-1, 3),
        Fraction(0),
        Fraction(2, 5),
        Fraction(1),
        Fraction(2),
        Fraction(17, 6),
    )

    for transverse in transverse_values:
        native = FramedMobiusStripState(
            root.advance(Fraction(7, 11)),
            transverse,
        )
        for convention in TransverseCoordinateConvention:
            envelope = mobius_to_transverse_envelope(native, convention)
            recovered = transverse_envelope_to_mobius(envelope)
            assert policy.matches(
                recovered.complete_identity,
                native.complete_identity,
            )
            for displacement in turns:
                expected = mobius_to_transverse_envelope(
                    native.advance(displacement),
                    convention,
                )
                observed = envelope.advance(displacement)
                assert policy.matches(
                    expected.complete_identity,
                    observed.complete_identity,
                )


def test_every_witness_retains_the_pinned_exact_policy(report) -> None:
    assert report.comparison_policy.name == TRANSVERSE_COMPARISON_POLICY_NAME
    assert report.comparison_policy.version == TRANSVERSE_COMPARISON_POLICY_VERSION
    witness_groups = (
        report.round_trips,
        report.root_restrictions,
        report.motion_witnesses,
        report.convention_round_trips,
        report.convention_motion_witnesses,
        report.carrier_collisions,
    )
    for group in witness_groups:
        assert group
        assert all(
            item.comparison_policy.name == TRANSVERSE_COMPARISON_POLICY_NAME
            and item.comparison_policy.version
            == TRANSVERSE_COMPARISON_POLICY_VERSION
            for item in group
        )


def test_report_rejects_count_preserving_identity_substitution(report) -> None:
    with pytest.raises(TransverseEnvelopeError, match="round trips must cover"):
        replace(
            report,
            round_trips=(report.round_trips[0],) * len(report.round_trips),
        )
    with pytest.raises(TransverseEnvelopeError, match="motion witnesses must cover"):
        replace(
            report,
            motion_witnesses=(report.motion_witnesses[0],)
            * len(report.motion_witnesses),
        )
    with pytest.raises(
        TransverseEnvelopeError,
        match="cannot alter the v0.7 carrier verdict matrix",
    ):
        replace(
            report,
            experiment=replace(report.experiment, report_id="substituted"),
        )


def test_zero_sidecar_restricts_exactly_to_v07(report) -> None:
    packet = report.root_report.direct_report.packet
    assert len(report.root_restrictions) == len(packet.initiations) * 2
    for item in report.root_restrictions:
        event = next(
            event for event in packet.initiations if event.event_id == item.event_id
        )
        assert item.native_envelope.root_state == event.post_state
        assert item.cover_envelope.root_chart == mobius_to_root_loop_cover(
            event.post_state
        )
        assert item.cover_envelope.local_transverse == 0
        assert item.cover_envelope.global_transverse == 0


def test_distinct_transverse_values_collide_in_the_actual_cover(report) -> None:
    policy = report.comparison_policy
    assert len(report.carrier_collisions) == 14 * 2
    for collision in report.carrier_collisions:
        assert not policy.matches(
            collision.first.complete_identity,
            collision.second.complete_identity,
        )
        assert policy.matches(
            collision.first.actual_cover_identity,
            collision.second.actual_cover_identity,
        )
        assert collision.first.carrier_mapping_status == "unmapped-sidecar"
        assert collision.second.carrier_mapping_status == "unmapped-sidecar"


def test_local_and_global_descriptions_remain_reversible(report) -> None:
    witness = report.convention_round_trips[-1]
    local = witness.local_state
    global_side = convert_transverse_convention(
        local,
        TransverseCoordinateConvention.GLOBAL_SIDE,
    )
    assert report.comparison_policy.matches(
        global_side.complete_identity,
        witness.global_state.complete_identity,
    )
    assert report.comparison_policy.matches(
        convert_transverse_convention(
            global_side,
            TransverseCoordinateConvention.LOCAL_FRAME,
        ).complete_identity,
        local.complete_identity,
    )


def test_v09_report_keeps_transverse_cover_extension_inconclusive(report) -> None:
    fibers = exact_rational_stress_fibers(TRANSVERSE_STRESS_MAX_DENOMINATOR)
    assert len(fibers) == 45
    assert report.fibers == fibers
    assert report.schema_id == V09_TRANSVERSE_ENVELOPE_SCHEMA_ID
    assert report.schema_version == V09_TRANSVERSE_ENVELOPE_SCHEMA_VERSION
    assert report.candidate_id == TRANSVERSE_ENVELOPE_ADAPTER_ID
    assert report.candidate_version == TRANSVERSE_ENVELOPE_ADAPTER_VERSION
    assert report.selection_effect == "none"
    assert report.transverse_cover_verdict is FalsifierVerdict.INCONCLUSIVE

    assert len(report.round_trips) == 14 * 45 * 2
    assert len(report.motion_witnesses) == 14 * 45 * 2 * 4
    assert len(report.convention_round_trips) == 14 * 45
    assert len(report.convention_motion_witnesses) == 14 * 45 * 4

    f12 = report.experiment.result(CarrierRelationship.COVER_CHART, "F12")
    f13 = report.experiment.result(CarrierRelationship.INCOMPATIBLE, "F13")
    root_map = f"map:{ROOT_LOOP_CHART_MAP_ID}@{ROOT_LOOP_CHART_MAP_VERSION}"
    assert f12.verdict is FalsifierVerdict.SUPPORTED
    assert f13.verdict is FalsifierVerdict.FALSIFIED
    assert root_map in f12.evidence
    assert root_map in f13.evidence
    assert all(
        TRANSVERSE_ENVELOPE_ADAPTER_ID not in item
        for item in (*f12.evidence, *f13.evidence)
    )
    assert any("not a transverse directed-cover embedding" in item for item in report.hmmm)
