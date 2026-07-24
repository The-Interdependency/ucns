import json

import pytest

import ucns
from ucns.bridge import (
    BRIDGE_SCHEMA_ID,
    BridgeValidationError,
    EdcmMetapatBridgeRecord,
)
from ucns.carrier import STRUCTURAL_NULL
from ucns.profiles import (
    PROFILE_OPTIONS,
    EdcmMetapatOrderedOccurrenceProfile,
    ProfileBoundStructure,
)
from ucns.structure import Cell, make_carrier, pair, support_weight

SOURCE_COMMIT = "1" * 40


def _profile():
    return EdcmMetapatOrderedOccurrenceProfile()


def _bridge(cells, *, operator_history=("source-append",)):
    profile = _profile()
    bound = profile.bind(make_carrier(cells))
    return profile.to_bridge(
        bound,
        source_commit=SOURCE_COMMIT,
        operator_history=operator_history,
    )


def test_equal_valued_duplicate_occurrences_remain_distinct() -> None:
    bound = _profile().bind(
        make_carrier([Cell(payload=42), Cell(payload=42)])
    )
    assert len(bound.cells) == 2
    assert bound.cells[0].payload == bound.cells[1].payload
    assert bound.occurrence_ids[0] != bound.occurrence_ids[1]


def test_reordering_changes_stable_identity() -> None:
    first = _bridge([Cell(payload="a"), Cell(payload="b")])
    second = _bridge([Cell(payload="b"), Cell(payload="a")])
    assert first.stable_identity != second.stable_identity


def test_cartesian_pairing_produces_p_times_q_occurrences() -> None:
    left = make_carrier([Cell(payload="l1"), Cell(payload="l2")])
    right = make_carrier(
        [Cell(payload="r1"), Cell(payload="r2"), Cell(payload="r3")]
    )
    result = pair(left, right)
    assert result is not STRUCTURAL_NULL
    assert len(result.cells) == 6


def test_cartesian_pairing_is_left_major() -> None:
    left = make_carrier([Cell(payload="l1"), Cell(payload="l2")])
    right = make_carrier([Cell(payload="r1"), Cell(payload="r2")])
    result = pair(left, right)
    assert result is not STRUCTURAL_NULL
    assert [cell.payload for cell in result.cells] == [
        ("l1", "r1"),
        ("l1", "r2"),
        ("l2", "r1"),
        ("l2", "r2"),
    ]


def test_pairing_preserves_left_right_sidedness() -> None:
    result = pair(
        make_carrier([Cell(provenance="left")]),
        make_carrier([Cell(provenance="right")]),
    )
    assert result is not STRUCTURAL_NULL
    assert result.cells[0].provenance == ("left", "right")


def test_algebraic_zero_remains_positive_retained_structure() -> None:
    carrier = make_carrier([Cell(payload=0)])
    assert carrier is not STRUCTURAL_NULL
    assert carrier.cells[0].payload == 0
    assert support_weight(carrier) == 1.0


def test_structural_null_is_distinct_from_algebraic_zero() -> None:
    null = make_carrier([])
    zero = make_carrier([Cell(payload=0)])
    assert null is STRUCTURAL_NULL
    assert zero is not STRUCTURAL_NULL
    assert support_weight(null) == 0.0
    assert support_weight(zero) == 1.0


def test_retained_relation_layer_does_not_change_scalar_support() -> None:
    plain = make_carrier([Cell(payload="event", mu=2.0)])
    related = make_carrier(
        [Cell(payload="event", relation={"edge": "refers-to"}, mu=2.0)]
    )
    assert support_weight(plain) == support_weight(related) == 2.0
    bridge = _bridge(
        [Cell(payload="event", relation={"edge": "refers-to"}, mu=2.0)]
    )
    assert [layer.name for layer in bridge.retained_layers] == ["relation"]


def test_serialization_is_byte_deterministic() -> None:
    bridge = _bridge(
        [Cell(payload={"b": 2, "a": 1}, provenance={"z": 0, "x": 1})]
    )
    assert bridge.to_json_bytes() == bridge.to_json_bytes()
    assert EdcmMetapatBridgeRecord.from_json_bytes(
        bridge.to_json_bytes()
    ).to_json_bytes() == bridge.to_json_bytes()


def test_bridge_round_trip_preserves_complete_record() -> None:
    bridge = _bridge(
        [Cell(coordinate=0, payload="event", state="active", provenance="src")]
    )
    restored = EdcmMetapatBridgeRecord.from_json_bytes(bridge.to_json_bytes())
    assert restored == bridge
    assert restored.stable_identity == bridge.stable_identity


def test_archived_schema_ids_fail_closed() -> None:
    bridge = _bridge([Cell(payload="event")])
    payload = json.loads(bridge.to_json_bytes())
    payload["schema_id"] = "ucns.bridge.v1"
    with pytest.raises(BridgeValidationError, match="archived bridge schema"):
        EdcmMetapatBridgeRecord.from_json_bytes(json.dumps(payload))


def test_option_mismatch_fails_closed() -> None:
    options = dict(PROFILE_OPTIONS)
    options["multiplicity_preserved"] = False
    with pytest.raises(ValueError, match="profile options"):
        EdcmMetapatOrderedOccurrenceProfile(
            options=tuple(sorted(options.items()))
        )

    bound = _profile().bind(make_carrier([Cell(payload="event")]))
    with pytest.raises(ValueError, match="option declaration"):
        ProfileBoundStructure(
            structure=bound.structure,
            occurrence_ids=bound.occurrence_ids,
            options=tuple(sorted(options.items())),
        )


def test_profile_identity_participates_in_stable_identity() -> None:
    bridge = _bridge([Cell(payload="event")])
    payload = json.loads(bridge.to_json_bytes())
    payload["profile_id"] = "ucns.profile.some-other-profile"
    with pytest.raises(BridgeValidationError, match="profile identity"):
        EdcmMetapatBridgeRecord.from_json_bytes(json.dumps(payload))


def test_validity_transfer_fields_are_permanently_false() -> None:
    bridge = _bridge([Cell(payload="event")])
    assert bridge.theorem_status_transfer is False
    assert bridge.edcm_measurement_validity_transfer is False
    assert bridge.metapat_validity_transfer is False

    payload = json.loads(bridge.to_json_bytes())
    payload["theorem_status_transfer"] = True
    with pytest.raises(BridgeValidationError, match="permanently false"):
        EdcmMetapatBridgeRecord.from_json_bytes(json.dumps(payload))


def test_profile_does_not_restore_factorization_or_universal_multiplication() -> None:
    assert "EdcmMetapatOrderedOccurrenceProfile" in ucns.__all__
    assert "multiply" not in ucns.__all__
    assert "factor" not in ucns.__all__
    assert "UCNSObject" not in ucns.__all__
    assert not hasattr(ucns, "multiply")
    assert not hasattr(ucns, "UCNSObject")


def test_existing_public_exports_remain_present() -> None:
    for expected in (
        "LiftedCarrierPoint",
        "Cell",
        "Carrier",
        "support_weight",
        "StructurePolicy",
        "RetainedStructure",
        "ComparisonPolicy",
        "TraversalPolicy",
        "EvaluatorCandidate",
        "LayerPairPolicy",
        "ExperimentManifest",
        "geometric_mean_product_candidate",
    ):
        assert expected in ucns.__all__
        assert hasattr(ucns, expected)
    assert BRIDGE_SCHEMA_ID in {
        "ucns.bridge.edcm-metapat-ordered-occurrence"
    }
