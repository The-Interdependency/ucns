# === CHECKS ===
# id: check_recursive_carrier_source_fails_closed
#   proves: recursive_carrier_source_fails_closed
#   call: self::test_source_fails_closed
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_recursive_carrier_leaves_unwitnessed_origin_unresolved
#   proves: recursive_carrier_leaves_unwitnessed_origin_unresolved
#   call: self::test_unwitnessed_origin_attachment_remains_unresolved
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_recursive_carrier_uses_deck_translation_as_successor
#   proves: recursive_carrier_uses_deck_translation_as_successor
#   call: self::test_successor_is_deck_translation
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_recursive_carrier_radius_is_not_depth
#   proves: recursive_carrier_radius_is_not_depth
#   call: self::test_radius_is_inherited
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_recursive_carrier_two_layers_restore_complete_mobius_state
#   proves: recursive_carrier_two_layers_restore_complete_mobius_state
#   call: self::test_two_layers_restore_complete_state
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_recursive_carrier_public_surface
#   proves: geometry_public_surface_includes_recursive_carrier_candidate
#   call: self::test_recursive_carrier_public_surface
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import json
from hashlib import sha256

import pytest

from ucns import (
    RecursiveCarrierError,
    build_epicyclic_edge,
    build_recursive_carrier,
    replay_recursive_carrier,
)


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def test_recursive_carrier_public_surface() -> None:
    import ucns
    from ucns import recursive_carrier

    expected = {
        "RECURSIVE_CARRIER_SCHEMA": recursive_carrier.SCHEMA,
        "RECURSIVE_CARRIER_VERSION": recursive_carrier.VERSION,
        "RecursiveCarrierError": recursive_carrier.RecursiveCarrierError,
        "build_recursive_carrier": recursive_carrier.build_recursive_carrier,
        "replay_recursive_carrier": recursive_carrier.replay_recursive_carrier,
    }
    assert expected.keys() <= set(ucns.__all__)
    for name, implementation in expected.items():
        assert getattr(ucns, name) is implementation
    assert ucns.RECURSIVE_CARRIER_SCHEMA == "ucns.recursive-carrier-successor-candidate"


def test_source_fails_closed() -> None:
    edge = build_epicyclic_edge(7, 11, 13)
    tampered = json.loads(json.dumps(edge))
    tampered["expansion"]["layer"] += 1
    with pytest.raises(RecursiveCarrierError):
        build_recursive_carrier(tampered)

    for ordinal in (0, 314, -314, 628, -628):
        with pytest.raises(RecursiveCarrierError, match="identity connection"):
            build_recursive_carrier(build_epicyclic_edge(ordinal, 0, 0))

    # A visible return with a reversed frame is not a complete identity.
    for ordinal in (157, -157):
        record = build_recursive_carrier(build_epicyclic_edge(ordinal, 0, 0))
        assert record["source_mobius"]["frame"] == "reversed-local-frame"
        assert record["target_mobius"]["frame"] == "positive-local-frame"

    # A nonzero deck displacement is not an identity even if phase/frame return.
    shifted = build_recursive_carrier(build_epicyclic_edge(0, 314, 0))
    assert shifted["source_edge"]["from_node"] != shifted["source_edge"]["to_node"]

    with pytest.raises(RecursiveCarrierError):
        build_recursive_carrier(edge, steps=0)


def test_unwitnessed_origin_attachment_remains_unresolved() -> None:
    for ordinal in (7, 321, -307):
        record = build_recursive_carrier(build_epicyclic_edge(ordinal, 11, 13))
        assert record["origin_attachment"] is None
        assert "Structural Null attachment witness" in record["hmmm"]
        assert replay_recursive_carrier(_canonical(record)) == record

        # Neither a forged source witness nor a rehashed output can turn an
        # absent construction relation into inherited geometric evidence.
        source = record["source_edge"].copy()
        source["origin_attachment"] = {"origin_id": "structural-null"}
        with pytest.raises(RecursiveCarrierError):
            build_recursive_carrier(source)
        tampered = record.copy()
        tampered["origin_attachment"] = {"origin_id": "structural-null"}
        tampered.pop("receipt_sha256")
        tampered["receipt_sha256"] = sha256(_canonical(tampered)).hexdigest()
        with pytest.raises(RecursiveCarrierError):
            replay_recursive_carrier(_canonical(tampered))

        old_version = record.copy()
        old_version["version"] = "0.1.0"
        with pytest.raises(RecursiveCarrierError, match="schema or version"):
            replay_recursive_carrier(_canonical(old_version))


def test_successor_is_deck_translation() -> None:
    record = build_recursive_carrier(build_epicyclic_edge(7, 11, 13))
    assert record["target_layer"] == record["source_layer"] + 1
    assert record["target_mobius"]["phase_turns"] == record["source_mobius"]["phase_turns"]
    assert record["target_mobius"]["frame"] != record["source_mobius"]["frame"]


def test_radius_is_inherited() -> None:
    edge = build_epicyclic_edge(7, 11, 13)
    one = build_recursive_carrier(edge, steps=1)
    seven = build_recursive_carrier(edge, steps=7)
    assert one["radius"] == edge["expansion"]["radius"]
    assert seven["radius"] == edge["expansion"]["radius"]


def test_two_layers_restore_complete_state() -> None:
    edge = build_epicyclic_edge(7, 11, 13)
    record = build_recursive_carrier(edge, steps=2)
    assert record["target_layer"] == record["source_layer"] + 2
    assert record["target_mobius"] == record["source_mobius"]

    data = _canonical(record)
    assert replay_recursive_carrier(data) == record

    tampered = json.loads(data)
    tampered["target_layer"] += 1
    with pytest.raises(RecursiveCarrierError):
        replay_recursive_carrier(_canonical(tampered))
