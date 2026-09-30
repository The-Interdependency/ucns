# === MODULE_BUILD ===
# id: ucns_epicyclic_graph_candidate
#   module_name: epicyclic_graph
#   module_kind: candidate
#   summary: epicyclic graph - each connection expands through space as a circle-plus-cover turn with radius and layer on the deck lattice
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, EpicyclicGraphError, build_epicyclic_edge, build_epicyclic_graph, replay_epicyclic_graph, run_epicyclic_graph_controls
#   internal_surface: lifted displacement, placement frame, exact deck lattice arithmetic, deterministic receipts
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_epicyclic_graph
#   rollout: candidate epicyclic graph replacing the admission cube as the spatial structure; connections expand, they are not scalar weights
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_lifted_displacement_candidate, ucns_placement_frame_candidate
#   since: 2026-09-29
#   unresolved: selection follows preregistered controls; no harmonic substrate claim
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: epicyclic_edge_expands_through_space
#   given: three exact channels
#   then: the edge carries phase, frame, radius, and layer from the selected lifted displacement and placement frame
#   class: correctness
# id: epicyclic_nodes_stay_on_the_deck_lattice
#   given: any edge
#   then: from_node and to_node are exact integers on the 157 deck lattice
#   class: correctness
# id: epicyclic_identity_is_a_loop
#   given: the zero connection
#   then: the edge is a loop with zero phase, zero radius, and zero layer
#   class: correctness
# id: epicyclic_graph_is_replayable
#   given: a graph record
#   then: the canonical receipt replays byte-identically and tampering fails closed
#   class: safety
# === END CONTRACTS ===
"""Epicyclic graph candidate.

Nodes sit on the 157 deck lattice. Each connection is an epicycle: it
expands through space as a circle-plus-cover turn (cos, sin, epsilon)
with a placement radius and layer. Connections are spatial expansions,
never scalar weights.
"""

from __future__ import annotations

import json
import math
from hashlib import sha256
from typing import Any

from .lifted_displacement import LiftedDisplacementError, build_lifted_displacement
from .placement_frame import PlacementFrameError, build_placement_frame

SCHEMA = "ucns.epicyclic-graph-candidate"
VERSION = "0.1.0"
_MODULUS = 157


class EpicyclicGraphError(ValueError):
    """Raised when the epicyclic graph fails closed."""


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def _receipt(payload: dict[str, Any]) -> str:
    return sha256(_canonical(payload)).hexdigest()


def _epsilon(frame: str) -> int:
    return 1 if frame == "positive-local-frame" else -1


def _circle_cover(p: int, epsilon: int) -> list[float]:
    return [
        round(math.cos(2 * math.pi * p / _MODULUS), 15),
        round(math.sin(2 * math.pi * p / _MODULUS), 15),
        epsilon,
    ]


def build_epicyclic_edge(
    ordinal: int,
    semantic: int,
    context: int,
    *,
    covering_degree: int | None = None,
) -> dict[str, Any]:
    """One connection as a spatial expansion between two lattice nodes."""

    try:
        lifted = build_lifted_displacement(ordinal, semantic, context,
                                           covering_degree=covering_degree)
        placement = build_placement_frame(ordinal, semantic, context)
    except (LiftedDisplacementError, PlacementFrameError) as exc:
        raise EpicyclicGraphError(str(exc)) from exc

    total = ordinal + semantic + context
    from_node = [ordinal % _MODULUS, ordinal // _MODULUS]
    to_node = [total % _MODULUS, total // _MODULUS + placement.layer]
    phase_p = int(lifted.phase_turns.numerator) % _MODULUS
    epsilon = _epsilon(lifted.frame)
    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "connection": [ordinal, semantic, context],
        "from_node": from_node,
        "to_node": to_node,
        "expansion": {
            "phase_turns": f"{lifted.phase_turns.numerator}/{lifted.phase_turns.denominator}",
            "frame": lifted.frame,
            "circle_cover": _circle_cover(phase_p, epsilon),
            "radius": placement.radius,
            "layer": placement.layer,
        },
        "covering_degree": covering_degree,
    }
    payload["receipt_sha256"] = _receipt(payload)
    return payload


def build_epicyclic_graph(edges: list[dict[str, Any]]) -> dict[str, Any]:
    """Assemble edges into a graph; nodes derive only from the edges."""

    nodes: list[Any] = []
    seen: set[str] = set()
    for edge in edges:
        for node in (edge["from_node"], edge["to_node"]):
            key = _canonical(node)
            if key not in seen:
                seen.add(key)
                nodes.append(node)
    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "node_count": len(nodes),
        "nodes": nodes,
        "edges": edges,
        "edge_count": len(edges),
        "expansion_through_space": True,
    }
    payload["receipt_sha256"] = _receipt(payload)
    return payload


def replay_epicyclic_graph(data: bytes) -> dict[str, Any]:
    """Rebuild a graph record and verify byte-identically."""

    if not isinstance(data, bytes):
        raise EpicyclicGraphError("graph record must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise EpicyclicGraphError("graph record is not valid canonical JSON") from exc
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise EpicyclicGraphError("graph record schema or version mismatch")
    rebuilt = build_epicyclic_graph(
        [
            build_epicyclic_edge(
                edge["connection"][0],
                edge["connection"][1],
                edge["connection"][2],
                covering_degree=edge.get("covering_degree"),
            )
            for edge in obj["edges"]
        ]
    )
    if rebuilt["receipt_sha256"] != obj.get("receipt_sha256"):
        raise EpicyclicGraphError("graph receipt does not match recomputation")
    if _canonical(rebuilt) != data:
        raise EpicyclicGraphError("graph does not replay byte-identically")
    return rebuilt


def run_epicyclic_graph_controls() -> dict[str, Any]:
    """The preregistered controls for the epicyclic graph."""

    identity = build_epicyclic_edge(0, 0, 0)
    first = build_epicyclic_edge(7, 11, 13, covering_degree=None)
    second = build_epicyclic_edge(7, 11, 13, covering_degree=None)
    results = {
        "identity-loop": {
            "ok": (
                identity["from_node"] == identity["to_node"]
                and identity["expansion"]["radius"] == 0.0
                and identity["expansion"]["layer"] == 0
                and identity["expansion"]["phase_turns"] == "0/1"
            ),
            "detail": "zero connection is a loop with no expansion",
        },
        "determinism": {
            "ok": first["receipt_sha256"] == second["receipt_sha256"],
            "detail": "same connection, same receipt",
        },
        "lattice-closure": {
            "ok": all(
                isinstance(value, int)
                for edge in (first, identity)
                for node in (edge["from_node"], edge["to_node"])
                for value in node
            ),
            "detail": "all nodes are exact deck-lattice integers",
        },
        "spatial-expansion": {
            "ok": (
                len(first["expansion"]["circle_cover"]) == 3
                and first["expansion"]["circle_cover"][2] in (-1, 1)
                and isinstance(first["expansion"]["radius"], float)
            ),
            "detail": "the connection expands through space as circle plus cover",
        },
    }
    ok = all(case["ok"] for case in results.values())
    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "results": results,
        "ok": ok,
        "hmmm": "connections expand through space; no scalar weight and no harmonic substrate is claimed",
    }
    payload["receipt_sha256"] = _receipt(payload)
    return payload


__all__ = [
    "SCHEMA",
    "VERSION",
    "EpicyclicGraphError",
    "build_epicyclic_edge",
    "build_epicyclic_graph",
    "replay_epicyclic_graph",
    "run_epicyclic_graph_controls",
]
