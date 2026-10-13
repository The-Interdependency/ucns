# === CHECKS ===
# id: check_epicyclic_edge_expands_through_space
#   proves: epicyclic_edge_expands_through_space
#   call: self::test_edge_expands_through_space
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_epicyclic_nodes_stay_on_the_deck_lattice
#   proves: epicyclic_nodes_stay_on_the_deck_lattice
#   call: self::test_nodes_stay_on_the_deck_lattice
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_epicyclic_identity_is_a_loop
#   proves: epicyclic_identity_is_a_loop
#   call: self::test_identity_is_a_loop
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_epicyclic_graph_is_replayable
#   proves: epicyclic_graph_is_replayable
#   call: self::test_graph_is_replayable
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===
import json

import pytest

from ucns import (
    EpicyclicGraphError,
    build_epicyclic_edge,
    build_epicyclic_graph,
    replay_epicyclic_graph,
    run_epicyclic_graph_controls,
)


def test_edge_expands_through_space() -> None:
    edge = build_epicyclic_edge(7, 11, 13)
    expansion = edge["expansion"]
    assert "phase_turns" in expansion
    assert "frame" in expansion
    assert isinstance(expansion["radius"], float)
    assert isinstance(expansion["layer"], int)
    assert len(expansion["circle_cover"]) == 3
    assert expansion["circle_cover"][2] in (-1, 1)


def test_nodes_stay_on_the_deck_lattice() -> None:
    edge = build_epicyclic_edge(7, 11, 13)
    for node in (edge["from_node"], edge["to_node"]):
        assert len(node) == 2
        assert all(isinstance(value, int) for value in node)
        assert 0 <= node[0] < 157


def test_identity_is_a_loop() -> None:
    identity = build_epicyclic_edge(0, 0, 0)
    assert identity["from_node"] == identity["to_node"] == [0, 0]
    assert identity["expansion"]["phase_turns"] == "0/1"
    assert identity["expansion"]["radius"] == 0.0
    assert identity["expansion"]["layer"] == 0


def test_graph_is_replayable() -> None:
    edges = [
        build_epicyclic_edge(7, 11, 13),
        build_epicyclic_edge(0, 0, 0),
        build_epicyclic_edge(3, 5, 8, covering_degree=158),
    ]
    graph = build_epicyclic_graph(edges)
    data = json.dumps(graph, sort_keys=True, separators=(",", ":")).encode("utf-8")
    replayed = replay_epicyclic_graph(data)
    assert replayed["receipt_sha256"] == graph["receipt_sha256"]

    tampered = bytearray(data)
    tampered[40] ^= 0x01
    with pytest.raises(EpicyclicGraphError):
        replay_epicyclic_graph(bytes(tampered))

    report = run_epicyclic_graph_controls()
    assert report["ok"] is True
