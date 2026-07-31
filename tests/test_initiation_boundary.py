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
    RC_COMPARISON_POLICY_NAME,
    RC_COMPARISON_POLICY_VERSION,
    RC_FALSIFIER_IDS,
    ROOT_VISIBLE_PROJECTION_ID,
    ROOT_VISIBLE_PROJECTION_INFORMATION_LOSS,
    ROOT_VISIBLE_PROJECTION_VERSION,
    SEAM_COORDINATE_VIEW_STATUS,
    V013_COMPLETE_RELATIONSHIP_STATUS,
    V013_INITIATION_BOUNDARY_SCHEMA_ID,
    V013_INITIATION_BOUNDARY_SCHEMA_VERSION,
    InitiationBoundaryError,
    StructuralNullTopologyKind,
    advance_attached_state,
    build_partial_initiation_attachments,
    exact_sheet_involution,
    initiate_carrier_state,
    project_root_visible_state,
    run_v013_partial_initiation_boundary_experiment,
    view_marked_seam_at_cut,
)
from ucns.comparison import ComparisonMode, exact_comparison_policy
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

    first_event = packet.initiations[0]
    source_variant = replace(
        first_event,
        post_state=replace(
            first_event.post_state,
            source_links=first_event.post_state.source_links
            + ("review-distinct-source-link",),
        ),
    )
    parent_variant = replace(
        first_event,
        post_state=replace(
            first_event.post_state,
            parent_observation_ids=(
                first_event.post_state.parent_observation_ids
                + ("review-distinct-parent",)
            ),
        ),
    )
    source_packet = replace(
        packet,
        initiations=(source_variant,) + packet.initiations[1:],
    )
    parent_packet = replace(
        packet,
        initiations=(parent_variant,) + packet.initiations[1:],
    )
    original_identity = attachments[0].attachment_identity
    assert (
        build_partial_initiation_attachments(source_packet)[
            0
        ].attachment_identity
        != original_identity
    )
    assert (
        build_partial_initiation_attachments(parent_packet)[
            0
        ].attachment_identity
        != original_identity
    )


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
    projection = project_root_visible_state(initial)
    assert projection == initial.visible_identity
    assert projection.projection_id == ROOT_VISIBLE_PROJECTION_ID
    assert projection.projection_version == ROOT_VISIBLE_PROJECTION_VERSION
    assert projection.attachment_identity == attachment.attachment_identity
    assert projection.source_links == (
        attachment.twist_receipt.post_native_state.source_links
    )
    assert projection.parent_observation_ids == (
        attachment.twist_receipt.post_native_state.parent_observation_ids
    )
    assert projection.information_loss == (
        ROOT_VISIBLE_PROJECTION_INFORMATION_LOSS
    )

    first_receipt = after_360.motion_history[0]
    with pytest.raises(
        InitiationBoundaryError,
        match="before endpoint",
    ):
        replace(
            after_360,
            motion_history=(
                replace(
                    first_receipt,
                    before_native_key=(("forged", "native-state"),),
                ),
            ),
        )
    with pytest.raises(
        InitiationBoundaryError,
        match="after endpoint",
    ):
        replace(
            after_360,
            motion_history=(
                replace(
                    first_receipt,
                    after_coordinate_identity=(
                        ("forged", "coordinate-state"),
                    ),
                ),
            ),
        )

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
    assert report.comparison_policy.name == RC_COMPARISON_POLICY_NAME
    assert report.comparison_policy.version == RC_COMPARISON_POLICY_VERSION
    assert report.comparison_policy.mode is ComparisonMode.EXACT
    assert report.comparison_policy.matches(("same",), ("same",))
    assert not report.comparison_policy.matches(("left",), ("right",))
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
    assert (
        report.complete_relationship_status
        == V013_COMPLETE_RELATIONSHIP_STATUS
    )
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
    with pytest.raises((TypeError, ValueError), match="init=False"):
        replace(
            report,
            comparison_policy=exact_comparison_policy(
                name=RC_COMPARISON_POLICY_NAME,
                version=RC_COMPARISON_POLICY_VERSION,
            ),
        )

    promoted_rc01 = replace(
        report.results[0],
        verdict=FalsifierVerdict.SUPPORTED,
    )
    with pytest.raises(
        InitiationBoundaryError,
        match="verdict map is fixed",
    ):
        replace(
            report,
            results=(promoted_rc01,) + report.results[1:],
        )
    with pytest.raises(
        InitiationBoundaryError,
        match="boundary statuses are fixed",
    ):
        replace(
            report,
            complete_relationship_status="completed-global-relationship",
        )
    widened_rc02 = replace(
        report.results[1],
        scope="arbitrary-real-complete-global-carrier",
    )
    with pytest.raises(
        InitiationBoundaryError,
        match="partial initiation scope",
    ):
        replace(
            report,
            results=(
                report.results[0],
                widened_rc02,
                *report.results[2:],
            ),
        )

    forged_evidence = replace(
        report.results[3],
        evidence=("completed-global-carrier:true",),
    )
    with pytest.raises(
        InitiationBoundaryError,
        match="RC result payload is fixed",
    ):
        replace(
            report,
            results=(
                *report.results[:3],
                forged_evidence,
                *report.results[4:],
            ),
        )
    forged_limitation = replace(
        report.results[3],
        limitation="arbitrary-real completion established",
    )
    with pytest.raises(
        InitiationBoundaryError,
        match="RC result payload is fixed",
    ):
        replace(
            report,
            results=(
                *report.results[:3],
                forged_limitation,
                *report.results[4:],
            ),
        )

    other_initial = initiate_carrier_state(report.attachments[1])
    other_360 = advance_attached_state(other_initial, 1)
    other_720 = advance_attached_state(other_360, 1)
    with pytest.raises(
        InitiationBoundaryError,
        match="one initiation attachment",
    ):
        replace(
            report,
            trajectory=(report.trajectory[0], other_360, other_720),
        )

    packet = build_native_mobius_initiation_packet()
    external_event = replace(
        packet.initiations[0],
        post_state=replace(
            packet.initiations[0].post_state,
            source_links=packet.initiations[0].post_state.source_links
            + ("valid-but-unreported-source-link",),
        ),
    )
    external_packet = replace(
        packet,
        initiations=(external_event,) + packet.initiations[1:],
    )
    external_attachment = build_partial_initiation_attachments(
        external_packet
    )[0]
    external_initial = initiate_carrier_state(external_attachment)
    external_360 = advance_attached_state(external_initial, 1)
    external_720 = advance_attached_state(external_360, 1)
    with pytest.raises(
        InitiationBoundaryError,
        match="retained report attachment",
    ):
        replace(
            report,
            trajectory=(external_initial, external_360, external_720),
        )

    initial, _, _ = report.trajectory
    after_1080 = advance_attached_state(initial, 3)
    after_1440 = advance_attached_state(after_1080, 1)
    with pytest.raises(
        InitiationBoundaryError,
        match="one exact turn",
    ):
        replace(
            report,
            trajectory=(initial, after_1080, after_1440),
        )
