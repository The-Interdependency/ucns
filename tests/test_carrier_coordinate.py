# === CHECKS ===
# id: check_carrier_coordinate_family_identity
#   proves: carrier_coordinate_family_is_explicit_and_nonselecting
#   call: self::test_candidate_family_is_explicit_ordered_and_nonselecting
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_carrier_coordinate_actual_cover_fields
#   proves: carrier_coordinate_uses_actual_cover_fields
#   call: self::test_candidate_image_materializes_declared_breadth_and_root_angle
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_carrier_coordinate_witness_identities
#   proves: carrier_coordinate_report_validates_complete_witness_identities
#   call: self::test_report_rejects_count_preserving_identity_substitution
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_carrier_coordinate_root_restriction
#   proves: carrier_coordinate_zero_fiber_restricts_to_v07
#   call: self::test_every_candidate_zero_fiber_is_the_v07_actual_root
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_carrier_coordinate_failure_retention
#   proves: carrier_coordinate_admissibility_retains_failures
#   call: self::test_rejected_candidates_retain_exact_collision_and_motion_witnesses
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_carrier_coordinate_constructive_boundary
#   proves: carrier_coordinate_constructive_result_does_not_select
#   call: self::test_signed_local_candidate_is_bounded_admissible_without_selection
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction

import pytest

from ucns.carrier import LiftedCarrierPoint, VISIBLE_PERIOD
from ucns.carrier_coordinate import (
    CARRIER_COORDINATE_COMPARISON_POLICY_NAME,
    CARRIER_COORDINATE_COMPARISON_POLICY_VERSION,
    CARRIER_COORDINATE_SCOPE,
    V010_CARRIER_COORDINATE_SCHEMA_ID,
    V010_CARRIER_COORDINATE_SCHEMA_VERSION,
    CarrierCoordinateAdmissibility,
    CarrierCoordinateBasis,
    CarrierCoordinateError,
    carrier_coordinate_candidates,
    carrier_coordinate_exact_comparison_policy,
    map_transverse_to_actual_cover,
    run_v010_carrier_coordinate_experiment,
)
from ucns.direct_mobius import build_native_mobius_initiation_packet
from ucns.transverse_envelope import (
    FramedMobiusStripState,
    TransverseCoordinateConvention,
    mobius_to_transverse_envelope,
)


@pytest.fixture(scope="module")
def report():
    return run_v010_carrier_coordinate_experiment()


def _result(report, candidate_id: str):
    return next(
        item
        for item in report.results
        if item.candidate.candidate_id == candidate_id
    )


def test_candidate_family_is_explicit_ordered_and_nonselecting(report) -> None:
    candidates = carrier_coordinate_candidates()
    assert tuple(item.candidate_id for item in candidates) == (
        "constant-root-breadth",
        "unsigned-local-radial",
        "signed-local-affine-radial",
        "signed-global-affine-radial",
    )
    assert tuple(item.basis for item in candidates) == tuple(
        CarrierCoordinateBasis
    )
    assert all(item.scope == CARRIER_COORDINATE_SCOPE for item in candidates)
    assert all(item.selection_effect == "none" for item in candidates)
    assert all(item.formula and item.code_reference for item in candidates)
    assert report.candidates == candidates
    assert report.selection_effect == "none"


def test_candidate_image_materializes_declared_breadth_and_root_angle() -> None:
    packet = build_native_mobius_initiation_packet()
    root = packet.witness_initiations("W-first")[0].post_state.advance(
        Fraction(7, 11)
    )
    native = FramedMobiusStripState(root, Fraction(97, 101))
    candidate = carrier_coordinate_candidates()[2]
    policy = carrier_coordinate_exact_comparison_policy()

    for convention in TransverseCoordinateConvention:
        envelope = mobius_to_transverse_envelope(native, convention)
        image = map_transverse_to_actual_cover(envelope, candidate, policy)
        assert isinstance(image.actual_point, LiftedCarrierPoint)
        assert image.declared_breadth == Fraction(299, 202)
        assert image.declared_lifted_turns == envelope.root_chart.lifted_turns
        assert image.actual_point.breadth == float(Fraction(299, 202))
        assert image.actual_point.angle == float(Fraction(7, 11)) * VISIBLE_PERIOD
        assert image.mapping_status == "candidate-mapped-into-actual-cover"
        assert image.source_state.carrier_mapping_status == "unmapped-sidecar"


def test_report_rejects_count_preserving_identity_substitution(report) -> None:
    first = report.results[0]
    with pytest.raises(
        CarrierCoordinateError,
        match="candidate images must cover",
    ):
        replace(
            report,
            results=(
                replace(
                    first,
                    images=(first.images[0],) * len(first.images),
                ),
                *report.results[1:],
            ),
        )

    with pytest.raises(
        CarrierCoordinateError,
        match="results must retain candidate order",
    ):
        replace(report, results=tuple(reversed(report.results)))


def test_every_candidate_zero_fiber_is_the_v07_actual_root(report) -> None:
    for result in report.results:
        assert len(result.root_restrictions) == 14 * 2
        assert result.root_restriction_passes
        for witness in result.root_restrictions:
            assert witness.image.declared_breadth == 1
            assert witness.passes


def test_rejected_candidates_retain_exact_collision_and_motion_witnesses(
    report,
) -> None:
    constant = _result(report, "constant-root-breadth")
    unsigned = _result(report, "unsigned-local-radial")
    global_signed = _result(report, "signed-global-affine-radial")

    assert constant.admissibility is CarrierCoordinateAdmissibility.REJECTED
    assert len(constant.collision_witnesses) == 14 * 2 * 44
    assert constant.motion_commutation_passes

    assert unsigned.admissibility is CarrierCoordinateAdmissibility.REJECTED
    assert len(unsigned.collision_witnesses) == 14 * 2 * 22
    assert unsigned.motion_commutation_passes
    assert all(
        first.first.local_transverse
        == -first.second.local_transverse
        for first in unsigned.collision_witnesses
    )

    assert global_signed.admissibility is CarrierCoordinateAdmissibility.REJECTED
    assert global_signed.fiber_injectivity_passes
    assert not global_signed.motion_commutation_passes
    failures = tuple(
        item for item in global_signed.motion_witnesses if not item.passes
    )
    assert len(failures) == 14 * 44 * 2 * 2
    assert {item.label for item in failures} == {"advance-360", "inverse"}


def test_signed_local_candidate_is_bounded_admissible_without_selection(
    report,
) -> None:
    signed_local = _result(report, "signed-local-affine-radial")
    assert report.schema_id == V010_CARRIER_COORDINATE_SCHEMA_ID
    assert report.schema_version == V010_CARRIER_COORDINATE_SCHEMA_VERSION
    assert report.comparison_policy.name == (
        CARRIER_COORDINATE_COMPARISON_POLICY_NAME
    )
    assert report.comparison_policy.version == (
        CARRIER_COORDINATE_COMPARISON_POLICY_VERSION
    )
    assert len(report.fibers) == 45
    assert len(signed_local.images) == 14 * 45 * 2
    assert len(signed_local.motion_witnesses) == 14 * 45 * 2 * 4
    assert signed_local.collision_witnesses == ()
    assert all(value for _criterion, value in signed_local.criterion_receipts)
    assert signed_local.admissibility is CarrierCoordinateAdmissibility.ADMISSIBLE
    assert report.admissible_candidate_ids == (
        "signed-local-affine-radial",
    )
    assert report.selection_effect == "none"
    assert any("not a selected carrier" in item for item in report.hmmm)
