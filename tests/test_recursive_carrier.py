# === CHECKS ===
# id: check_recursive_carrier_source_fails_closed
#   proves: recursive_carrier_source_fails_closed
#   call: self::test_source_fails_closed
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_recursive_carrier_preserves_structural_null_attachment
#   proves: recursive_carrier_preserves_structural_null_attachment
#   call: self::test_origin_attachment_is_preserved
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
# === END CHECKS ===

import json

import pytest

from ucns import (
    RecursiveCarrierError,
    STRUCTURAL_NULL_ORIGIN,
    build_epicyclic_edge,
    build_recursive_carrier,
    replay_recursive_carrier,
)


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def test_source_fails_closed() -> None:
    edge = build_epicyclic_edge(7, 11, 13)
    tampered = json.loads(json.dumps(edge))
    tampered["expansion"]["layer"] += 1
    with pytest.raises(RecursiveCarrierError):
        build_recursive_carrier(tampered)

    with pytest.raises(RecursiveCarrierError):
        build_recursive_carrier(build_epicyclic_edge(0, 0, 0))

    with pytest.raises(RecursiveCarrierError):
        build_recursive_carrier(edge, steps=0)


def test_origin_attachment_is_preserved() -> None:
    record = build_recursive_carrier(build_epicyclic_edge(7, 11, 13))
    assert record["origin_attachment"] == {
        "origin_id": STRUCTURAL_NULL_ORIGIN.origin_id,
        "carrier_position": STRUCTURAL_NULL_ORIGIN.carrier_position,
    }


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
