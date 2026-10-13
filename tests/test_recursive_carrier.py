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
# id: check_recursive_carrier_serialization_fails_closed
#   proves: recursive_carrier_source_fails_closed
#   call: self::test_source_serialization_fails_closed
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_recursive_carrier_parser_limits_fail_closed
#   proves: recursive_carrier_source_fails_closed
#   call: self::test_replay_parser_limits_fail_closed
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_recursive_carrier_reconstruction_limits_fail_closed
#   proves: recursive_carrier_source_fails_closed
#   call: self::test_reconstruction_limits_fail_closed
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import json
import sys
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


def test_source_serialization_fails_closed() -> None:
    edge = build_epicyclic_edge(7, 11, 13)
    for value in (object(), float("nan"), float("inf"), float("-inf"), "\ud800"):
        malformed = edge.copy()
        malformed["unexpected"] = value
        with pytest.raises(RecursiveCarrierError, match="not canonical JSON"):
            build_recursive_carrier(malformed)

    circular = edge.copy()
    circular["unexpected"] = circular
    with pytest.raises(RecursiveCarrierError, match="not canonical JSON"):
        build_recursive_carrier(circular)

    # Python's JSON decoder accepts non-finite literals. A tampered source
    # must still fail through the same advertised domain exception on replay.
    for value in (float("nan"), float("inf"), float("-inf")):
        record = build_recursive_carrier(edge)
        record["source_edge"]["unexpected"] = value
        with pytest.raises(RecursiveCarrierError, match="not canonical JSON"):
            replay_recursive_carrier(_canonical(record))


def test_replay_parser_limits_fail_closed() -> None:
    prior = sys.get_int_max_str_digits()
    try:
        sys.set_int_max_str_digits(640)
        oversized_integer = b'{"steps":' + b"9" * 641 + b"}"
        with pytest.raises(RecursiveCarrierError, match="not valid canonical JSON"):
            replay_recursive_carrier(oversized_integer)
    finally:
        sys.set_int_max_str_digits(prior)

    depth = 10_000
    deeply_nested = b"[" * depth + b"0" + b"]" * depth
    # Parser recursion limits differ across supported Python versions. The
    # nested array must fail at either parsing or the public object boundary.
    with pytest.raises(RecursiveCarrierError):
        replay_recursive_carrier(deeply_nested)
    for malformed in (b"{", b"\xff"):
        with pytest.raises(RecursiveCarrierError, match="not valid canonical JSON"):
            replay_recursive_carrier(malformed)

    # Exercise normalization independently of a particular interpreter limit.
    from unittest.mock import patch

    with patch("ucns.recursive_carrier.json.loads", side_effect=RecursionError("parser limit")):
        with pytest.raises(RecursiveCarrierError, match="not valid canonical JSON"):
            replay_recursive_carrier(b"{}")


def test_reconstruction_limits_fail_closed() -> None:
    edge = build_epicyclic_edge(7, 11, 13)
    prior = sys.get_int_max_str_digits()
    try:
        sys.set_int_max_str_digits(640)
        for index in range(3):
            oversized = edge.copy()
            oversized["connection"] = edge["connection"].copy()
            oversized["connection"][index] = 10 ** 700
            with pytest.raises(RecursiveCarrierError, match="cannot be reconstructed canonically"):
                build_recursive_carrier(oversized)
        oversized_covering = edge.copy()
        oversized_covering["covering_degree"] = 10 ** 700
        with pytest.raises(RecursiveCarrierError, match="cannot be reconstructed canonically"):
            build_recursive_carrier(oversized_covering)
        with pytest.raises(RecursiveCarrierError, match="not canonical JSON"):
            build_recursive_carrier(edge, steps=10 ** 700)
        assert replay_recursive_carrier(_canonical(build_recursive_carrier(edge)))
    finally:
        sys.set_int_max_str_digits(prior)

    # Unexpected implementation faults remain visible, rather than being
    # mislabeled as malformed user data.
    from unittest.mock import patch

    with patch("ucns.recursive_carrier.build_epicyclic_edge", side_effect=RuntimeError("fault")):
        with pytest.raises(RuntimeError, match="fault"):
            build_recursive_carrier(edge)
