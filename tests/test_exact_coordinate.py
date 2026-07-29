# === CHECKS ===
# id: check_exact_coordinate_signed_local_round_trip
#   proves: exact_coordinate_signed_local_law_round_trips
#   call: self::test_signed_local_exact_law_round_trips_rational_domain
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_exact_coordinate_fixed_provenance
#   proves: exact_coordinate_provenance_is_fixed_and_retained
#   call: self::test_exact_coordinate_retains_fixed_provenance_and_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_exact_coordinate_binary64_rendering_boundary
#   proves: exact_coordinate_binary64_is_declared_rendering
#   call: self::test_binary64_point_is_linked_lossy_rendering_only
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_exact_coordinate_binary64_breadth_collision
#   proves: exact_coordinate_binary64_breadth_collision_is_retained
#   call: self::test_binary64_breadth_collision_retains_exact_distinction
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_exact_coordinate_binary64_turn_collision
#   proves: exact_coordinate_binary64_turn_collision_is_retained
#   call: self::test_binary64_turn_collision_retains_exact_distinction
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_exact_coordinate_nonselection_boundary
#   proves: exact_coordinate_boundary_does_not_select_or_activate
#   call: self::test_v011_report_keeps_selection_and_activation_absent
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction

import pytest

from ucns.carrier import LiftedCarrierPoint
from ucns.exact_coordinate import (
    BINARY64_RENDERING_STATUS,
    EXACT_COORDINATE_CANDIDATE_ID,
    EXACT_COORDINATE_LAW_ID,
    EXACT_COORDINATE_SCOPE,
    V011_EXACT_COORDINATE_SCHEMA_ID,
    V011_EXACT_COORDINATE_SCHEMA_VERSION,
    Binary64CollisionKind,
    ExactCoordinateError,
    binary64_collision_witnesses,
    recover_signed_local_transverse,
    render_exact_coordinate_binary64,
    run_v011_exact_coordinate_boundary_experiment,
    signed_local_exact_coordinate,
)


def test_signed_local_exact_law_round_trips_rational_domain() -> None:
    for denominator in range(1, 65):
        for numerator in range(-denominator, denominator + 1):
            transverse = Fraction(numerator, denominator)
            turns = Fraction(numerator + 3 * denominator, denominator)
            coordinate = signed_local_exact_coordinate(transverse, turns)

            assert coordinate.breadth == 1 + transverse / 2
            assert Fraction(1, 2) <= coordinate.breadth <= Fraction(3, 2)
            assert recover_signed_local_transverse(coordinate) == transverse
            assert Fraction(0) <= coordinate.lifted_turns < Fraction(2)
            assert coordinate.selection_effect == "none"

    with pytest.raises(ExactCoordinateError, match="exact Fraction"):
        signed_local_exact_coordinate(0.0, Fraction(0))  # type: ignore[arg-type]
    with pytest.raises(ExactCoordinateError, match=r"\[-1, 1\]"):
        signed_local_exact_coordinate(Fraction(2), Fraction(0))


def test_exact_coordinate_retains_fixed_provenance_and_fails_closed() -> None:
    coordinate = signed_local_exact_coordinate(Fraction(7, 11), Fraction(5, 7))
    provenance = coordinate.provenance

    assert provenance.source_candidate_id == EXACT_COORDINATE_CANDIDATE_ID
    assert provenance.law_id == EXACT_COORDINATE_LAW_ID
    assert provenance.scope == EXACT_COORDINATE_SCOPE
    assert provenance.code_reference
    assert provenance.selection_effect == "none"

    with pytest.raises(
        ExactCoordinateError,
        match="provenance identity is fixed",
    ):
        replace(provenance, source_candidate_id="substituted-candidate")
    with pytest.raises(
        ExactCoordinateError,
        match="signed-local affine law",
    ):
        replace(coordinate, breadth=coordinate.breadth + 1)


def test_binary64_point_is_linked_lossy_rendering_only() -> None:
    coordinate = signed_local_exact_coordinate(
        Fraction(97, 101),
        Fraction(7, 11),
    )
    rendering = render_exact_coordinate_binary64(coordinate)

    assert isinstance(rendering.actual_point, LiftedCarrierPoint)
    assert rendering.exact_coordinate is coordinate
    assert rendering.actual_point.breadth == float(coordinate.breadth)
    assert rendering.rendering_identity[0][0] == "breadth-binary64"
    assert rendering.rendering_identity[1][0] == "angle-binary64"
    assert rendering.status == BINARY64_RENDERING_STATUS
    assert rendering.information_loss
    assert rendering.selection_effect == "none"

    with pytest.raises(
        ExactCoordinateError,
        match="classified as a rendering",
    ):
        replace(rendering, status="authoritative-exact-coordinate")


def test_binary64_breadth_collision_retains_exact_distinction() -> None:
    breadth_witness = binary64_collision_witnesses()[0]
    first = breadth_witness.first
    second = breadth_witness.second

    assert breadth_witness.kind is Binary64CollisionKind.BREADTH
    assert first.exact_coordinate.local_transverse == 0
    assert second.exact_coordinate.local_transverse == Fraction(1, 2**53)
    assert (
        second.exact_coordinate.breadth - first.exact_coordinate.breadth
        == Fraction(1, 2**54)
    )
    assert first.exact_coordinate.exact_identity != (
        second.exact_coordinate.exact_identity
    )
    assert first.actual_point.breadth == second.actual_point.breadth == 1.0
    assert first.rendering_identity == second.rendering_identity


def test_binary64_turn_collision_retains_exact_distinction() -> None:
    turn_witness = binary64_collision_witnesses()[1]
    first = turn_witness.first
    second = turn_witness.second

    assert turn_witness.kind is Binary64CollisionKind.LIFTED_TURN
    assert first.exact_coordinate.breadth == second.exact_coordinate.breadth
    assert (
        second.exact_coordinate.lifted_turns
        - first.exact_coordinate.lifted_turns
        == Fraction(1, 2**54)
    )
    assert first.exact_coordinate.exact_identity != (
        second.exact_coordinate.exact_identity
    )
    assert first.rendering_identity == second.rendering_identity


def test_v011_report_keeps_selection_and_activation_absent() -> None:
    report = run_v011_exact_coordinate_boundary_experiment()

    assert report.schema_id == V011_EXACT_COORDINATE_SCHEMA_ID
    assert report.schema_version == V011_EXACT_COORDINATE_SCHEMA_VERSION
    assert report.exact_law_status == (
        "exact-rational-bijection-on-declared-transverse-interval"
    )
    assert report.binary64_status == (
        "not-injective-on-arbitrary-exact-rational-domain"
    )
    assert report.rendering_role == BINARY64_RENDERING_STATUS
    assert tuple(item.kind for item in report.collision_witnesses) == tuple(
        Binary64CollisionKind
    )
    assert report.selection_effect == "none"
    assert report.edcm_activation == "inactive"
    assert report.metapat_activation == "inactive"
    assert any("real continuity" in item for item in report.hmmm)
    assert any("arbitrary observed-element assignment" in item for item in report.hmmm)

    with pytest.raises(ExactCoordinateError, match="exact-law status is fixed"):
        replace(report, exact_law_status="selected-global-law")
    with pytest.raises(
        ExactCoordinateError,
        match="collision witness identities are fixed",
    ):
        replace(
            report,
            collision_witnesses=(
                replace(
                    report.collision_witnesses[0],
                    exact_difference="substituted difference",
                ),
                report.collision_witnesses[1],
            ),
        )
