# === CHECKS ===
# id: check_partial_initiation_structural_null_topology
#   proves: partial_initiation_structural_null_topology_is_explicit
#   call: self::test_structural_null_is_disjoint_typed_prestate_with_partial_edges
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_partial_initiation_marked_seam_provenance
#   proves: partial_initiation_seam_is_provenance_bearing
#   call: self::test_marked_seam_survives_numeric_coordinate_cut_movement
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_partial_initiation_twist_receipts
#   proves: partial_initiation_twist_receipt_is_source_bound
#   call: self::test_every_word_attachment_has_one_source_bound_twist_receipt
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_partial_initiation_motion_history
#   proves: partial_initiation_motion_preserves_360_720_and_history
#   call: self::test_360_changes_720_returns_and_two_motion_receipts_survive
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_partial_initiation_sheet_involution
#   proves: partial_initiation_exact_quotient_compatibility
#   call: self::test_exact_sheet_involution_matches_signed_local_quotient
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_partial_initiation_rc_packet
#   proves: partial_initiation_report_executes_rc_packet_without_selection
#   call: self::test_v013_report_is_complete_bounded_and_nonselecting
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction

import pytest

from ucns.direct_mobius import (
    STRUCTURAL_NULL_ORIGIN,
    StructuralNullKind,
    build_native_mobius_initiation_packet,
)
from ucns.initiation_boundary import (
    PARTIAL_INITIATION_RELATION_ID,
    RC_FALSIFIER_IDS,
    SEAM_COORDINATE_VIEW_STATUS,
    V013_INITIATION_BOUNDARY_SCHEMA_ID,
    V013_INITIATION_BOUNDARY_SCHEMA_VERSION,
    InitiationBoundaryError,
    StructuralNullTopologyKind,
    advance_attached_state,
    build_partial_initiation_attachments,
    exact_sheet_involution,
    initiate_carrier_state,
    run_v013_partial_initiation_boundary_experiment,
    view_marked_seam_at_cut,
)
from ucns.exact_coordinate import signed_local_exact_coordinate
from ucns.mobius_experiment import FalsifierVerdict


def test_structural_null_is_disjoint_typed_prestate_with_partial_edges() -> None:
    attachments = build_partial_initiation_attachments()

    assert len(attachments) == 14
    assert all(
        item.seam.topology
        is StructuralNullTopologyKind.DISJOINT_MARKED_PRESTATE
        for item in attachments
    )
    assert all(
        item.twist_receipt.pre_state is STRUCTURAL_NULL_ORIGIN
        for item in attachments
    )
    assert all(
        item.twist_receipt.relation_id == PARTIAL_INITIATION_RELATION_ID
        for item in attachments
    )
    assert all(
        item.twist_receipt.post_coordinate.local_transverse == 0
        and item.twist_receipt.post_coordinate.breadth == 1
        and item.twist_receipt.post_coordinate.lifted_turns == 0
        for item in attachments
    )
    assert STRUCTURAL_NULL_ORIGIN not in {
        item.twist_receipt.post_coordinate for item in attachments
    }


def test_marked_seam_survives_numeric_coordinate_cut_movement() -> None:
    seam = build_partial_initiation_attachments()[0].seam
    initial_view = view_marked_seam_at_cut(seam, Fraction(0))
    shifted_view = view_marked_seam_at_cut(seam, Fraction(7, 3))

    assert initial_view.coordinate_cut_turns == 0
    assert shifted_view.coordinate_cut_turns == Fraction(1, 3)
    assert initial_view.status == SEAM_COORDINATE_VIEW_STATUS
    assert initial_view.structural_seam_identity == (
        shifted_view.structural_seam_identity
    )
    assert initial_view.seam is shifted_view.seam is seam

    with pytest.raises(InitiationBoundaryError, match="exact Fraction"):
        view_marked_seam_at_cut(seam, 0.5)  # type: ignore[arg-type]
    with pytest.raises(
        InitiationBoundaryError,
        match="nonauthoritative",
    ):
        replace(initial_view, status="authoritative-hidden-zero-coordinate")


def test_every_word_attachment_has_one_source_bound_twist_receipt() -> None:
    packet = build_native_mobius_initiation_packet()
    attachments = build_partial_initiation_attachments(packet)

    assert tuple(item.event.event_id for item in attachments) == tuple(
        item.event_id for item in packet.initiations
    )
    for attachment, event in zip(
        attachments,
        packet.initiations,
        strict=True,
    ):
        receipt = attachment.twist_receipt
        assert receipt.event is event
        assert receipt.seam is attachment.seam
        assert receipt.seam.manifestation is event.boundary
        assert receipt.post_native_state is event.post_state
        assert f"witness:{event.witness_id}" in receipt.source_links
        assert f"seam:{attachment.seam.seam_id}" in receipt.source_links
        assert receipt.selection_effect == "none"

    repeated = tuple(
        item
        for item in attachments
        if item.event.witness_id == "W-repeat-space"
    )
    assert len(repeated) == 2
    assert repeated[1].seam.manifestation.kind is (
        StructuralNullKind.SPACE_MANIFESTATION
    )
    assert repeated[1].seam.manifestation.source_offset == 2


def test_360_changes_720_returns_and_two_motion_receipts_survive() -> None:
    attachment = build_partial_initiation_attachments()[0]
    initial = initiate_carrier_state(attachment)
    after_360 = advance_attached_state(initial, 1)
    after_720 = advance_attached_state(after_360, 1)
    inverse = advance_attached_state(after_360, -1)

    assert initial.visible_identity == after_360.visible_identity
    assert initial.complete_local_identity != after_360.complete_local_identity
    assert initial.complete_local_identity == after_720.complete_local_identity
    assert len(initial.motion_history) == 0
    assert len(after_360.motion_history) == 1
    assert len(after_720.motion_history) == 2
    assert tuple(
        item.motion_turns for item in after_720.motion_history
    ) == (Fraction(1), Fraction(1))
    assert tuple(
        item.step_index for item in after_720.motion_history
    ) == (0, 1)
    assert inverse.complete_local_identity == initial.complete_local_identity
    assert len(inverse.motion_history) == 2

    with pytest.raises(InitiationBoundaryError, match="nonzero"):
        advance_attached_state(initial, 0)
    with pytest.raises(InitiationBoundaryError, match="exact Fraction"):
        advance_attached_state(initial, 0.5)  # type: ignore[arg-type]


def test_exact_sheet_involution_matches_signed_local_quotient() -> None:
    coordinate = signed_local_exact_coordinate(
        Fraction(7, 11),
        Fraction(5, 13),
    )
    image = exact_sheet_involution(coordinate)
    restored = exact_sheet_involution(image)

    assert image.local_transverse == -coordinate.local_transverse
    assert image.breadth == 2 - coordinate.breadth
    assert image.lifted_turns == (
        coordinate.lifted_turns + 1
    ) % 2
    assert restored == coordinate


def test_v013_report_is_complete_bounded_and_nonselecting() -> None:
    report = run_v013_partial_initiation_boundary_experiment()

    assert report.schema_id == V013_INITIATION_BOUNDARY_SCHEMA_ID
    assert report.schema_version == V013_INITIATION_BOUNDARY_SCHEMA_VERSION
    assert len(report.attachments) == 14
    assert len(report.binary64_witnesses) == 2
    assert tuple(item.falsifier_id for item in report.results) == (
        RC_FALSIFIER_IDS
    )
    assert report.result("RC01").verdict is FalsifierVerdict.INCONCLUSIVE
    assert report.result("RC03").verdict is FalsifierVerdict.INCONCLUSIVE
    for falsifier_id in (
        "RC02",
        "RC04",
        "RC05",
        "RC06",
        "RC07",
        "RC08",
        "RC09",
        "RC10",
    ):
        assert (
            report.result(falsifier_id).verdict
            is FalsifierVerdict.SUPPORTED
        )
    assert report.complete_relationship_status.startswith("inconclusive")
    assert report.selection_effect == "none"
    assert report.edcm_activation == "inactive"
    assert report.metapat_activation == "inactive"
    assert any("arbitrary-real" in item for item in report.hmmm)
    assert any("arbitrary observed-element" in item for item in report.hmmm)

    with pytest.raises(
        InitiationBoundaryError,
        match="cannot select",
    ):
        replace(report, selection_effect="marked-seam-selected")
