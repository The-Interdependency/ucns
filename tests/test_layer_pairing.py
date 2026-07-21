# === CHECKS ===
# id: check_explicit_layer_pair_plan
#   proves: retained_layer_pairing_requires_explicit_plan
#   call: self::test_explicit_layer_pair_plan
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_layer_pair_source_and_loss_evidence
#   proves: layer_pairing_preserves_sources_and_declares_loss
#   call: self::test_layer_pair_source_and_loss_evidence
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_unmatched_layer_modes
#   proves: unmatched_layers_follow_explicit_mode
#   call: self::test_unmatched_layer_modes
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_retained_pair_measurement_firewall
#   proves: retained_pairing_does_not_extend_measurements
#   call: self::test_retained_pair_measurement_firewall
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import pytest

from ucns import (
    Carrier,
    Cell,
    ContributionStatus,
    EnvelopePairPlan,
    LayerPairRegistry,
    LayerPairRule,
    LayerRef,
    RetainedLayer,
    RetainedStructure,
    UnmatchedLayerMode,
    cartesian_layer_policy,
    cell_support_weight,
    concatenate_layer_policy,
    pair_retained,
    positional_zip_layer_policy,
)


def envelope(label: str) -> RetainedStructure:
    return RetainedStructure(
        Carrier((Cell(coordinate=label, mu=2.0),)),
        (
            RetainedLayer(
                "receipts", (f"{label}-1", f"{label}-2")
            ),
            RetainedLayer("metadata", {"side": label}),
        ),
    )


def registry() -> LayerPairRegistry:
    result = LayerPairRegistry()
    for policy in (
        concatenate_layer_policy(),
        cartesian_layer_policy(),
        positional_zip_layer_policy(),
    ):
        result.register(policy)
    return result


def test_explicit_layer_pair_plan() -> None:
    left, right = envelope("L"), envelope("R")
    plan = EnvelopePairPlan(
        "receipts",
        (
            LayerPairRule(
                LayerRef("receipts"),
                LayerRef("receipts"),
                "concatenate",
                "receipts",
            ),
        ),
        UnmatchedLayerMode.PRESERVE_SIDES,
    )
    result = pair_retained(left, right, plan, registry=registry())
    assert result.envelope.layer("receipts").evidence == (
        "L-1",
        "L-2",
        "R-1",
        "R-2",
    )
    assert result.envelope.layer("left:metadata").evidence == {
        "side": "L"
    }


def test_layer_pair_source_and_loss_evidence() -> None:
    left, right = envelope("L"), envelope("R")
    plan = EnvelopePairPlan(
        "zip",
        (
            LayerPairRule(
                LayerRef("receipts"),
                LayerRef("metadata"),
                "positional-zip",
                "mixed",
            ),
        ),
        UnmatchedLayerMode.EXCLUDE,
    )
    result = pair_retained(left, right, plan, registry=registry())
    decision = result.decisions[0]
    assert decision.projection.left_source == ("L-1", "L-2")
    assert decision.projection.right_source == {"side": "R"}
    assert result.losses


def test_unmatched_layer_modes() -> None:
    with pytest.raises(ValueError):
        pair_retained(
            envelope("L"),
            envelope("R"),
            EnvelopePairPlan("fail", ()),
            registry=registry(),
        )


def test_retained_pair_measurement_firewall() -> None:
    result = pair_retained(
        envelope("L"),
        envelope("R"),
        EnvelopePairPlan(
            "receipts",
            (
                LayerPairRule(
                    LayerRef("receipts"),
                    LayerRef("receipts"),
                    "cartesian",
                    "receipts",
                ),
            ),
            UnmatchedLayerMode.EXCLUDE,
        ),
        registry=registry(),
    )
    assert (
        result.envelope.layer("receipts").contribution_status
        is ContributionStatus.UNMEASURED
    )
    assert cell_support_weight(result.envelope) == 4.0
