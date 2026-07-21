# === CHECKS ===
# id: check_layer_append_behavior
#   proves: retained_layers_append_without_overwrite
#   call: self::test_layer_append_behavior
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_falsey_retained_evidence
#   proves: retained_layer_presence_is_explicit
#   call: self::test_falsey_retained_evidence
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_retained_null_boundary
#   proves: retained_envelope_has_unique_complete_null
#   call: self::test_retained_null_boundary
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_layer_measurement_firewall
#   proves: retained_layers_do_not_silently_enter_cell_support
#   call: self::test_layer_measurement_firewall
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_layer_projection
#   proves: retained_layer_projection_is_non_destructive
#   call: self::test_layer_projection
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import pytest

from ucns import STRUCTURAL_NULL, Carrier, Cell
from ucns.envelope import (
    ContributionStatus,
    RetainedLayer,
    RetainedStructure,
    cell_support_weight,
    make_retained_structure,
    project_layer,
)
from ucns.policy import PolicyRegistry, set_policy


def test_layer_append_behavior() -> None:
    first = RetainedLayer("receipt", "r1")
    second = RetainedLayer("receipt", "r2")
    envelope = RetainedStructure(layers=(first,)).with_layer(second)
    assert envelope.layers == (first, second)
    assert envelope.layers_named("receipt") == (first, second)
    assert envelope.layer("receipt", occurrence=1) is second


def test_falsey_retained_evidence() -> None:
    layers = (
        RetainedLayer("zero", 0),
        RetainedLayer("false", False),
        RetainedLayer("none", None),
        RetainedLayer("empty", ()),
    )
    envelope = make_retained_structure(layers=layers)
    assert isinstance(envelope, RetainedStructure)
    assert envelope.retained_layers == layers

    with pytest.raises(ValueError):
        RetainedLayer("absent", 0, retained=False)


def test_retained_null_boundary() -> None:
    absent = RetainedLayer("receipt", retained=False)
    assert make_retained_structure(layers=(absent,)) is STRUCTURAL_NULL
    with pytest.raises(ValueError):
        RetainedStructure()

    receipt_only = make_retained_structure(layers=(RetainedLayer("receipt", "r"),))
    assert isinstance(receipt_only, RetainedStructure)
    assert receipt_only.carrier is STRUCTURAL_NULL


def test_layer_measurement_firewall() -> None:
    carrier = Carrier((Cell(coordinate="cell", mu=2.0),))
    layers = (
        RetainedLayer("receipt", "r", contribution_status=ContributionStatus.UNMEASURED),
        RetainedLayer(
            "metadata",
            {"source": "x"},
            contribution_status=ContributionStatus.EXCLUDED,
            contribution_note="excluded from cell-only W",
        ),
    )
    envelope = make_retained_structure(carrier, layers)
    assert isinstance(envelope, RetainedStructure)
    assert cell_support_weight(envelope) == 2.0

    receipt_only = make_retained_structure(layers=(RetainedLayer("receipt", "r"),))
    assert cell_support_weight(receipt_only) == 0.0
    with pytest.raises(ValueError):
        RetainedLayer("metadata", {}, contribution_status=ContributionStatus.EXCLUDED)


def test_layer_projection() -> None:
    evidence = ("a", "a", "b")
    layer = RetainedLayer("receipt", evidence, policy_name="set")
    envelope = RetainedStructure(layers=(layer,))
    registry = PolicyRegistry()
    registry.register(set_policy(lambda value: value))

    projection = project_layer(envelope, "receipt", registry=registry)
    assert projection.source is evidence
    assert len(projection.view) == 2
    assert envelope.layers == (layer,)
