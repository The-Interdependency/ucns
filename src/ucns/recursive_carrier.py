# === MODULE_BUILD ===
# id: ucns_recursive_carrier_successor_candidate
#   module_name: recursive_carrier
#   module_kind: candidate
#   summary: binds a validated non-identity epicyclic connection to successor carrier layers while preserving Structural Null attachment, canonical radius, and the native Mobius deck law
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, RecursiveCarrierError, build_recursive_carrier, replay_recursive_carrier
#   internal_surface: exact epicyclic-edge replay, Structural Null attachment, native Mobius successor derivation, deterministic receipts
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_recursive_carrier
#   rollout: candidate successor-carrier binding; does not ratify the full circle-to-sphere recursive construction
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_epicyclic_graph_candidate, ucns_native_mobius_geometry, ucns_radius_recursion_candidate
#   since: 2026-10-04
#   unresolved: disk/sphere closure, distant-scale coupling, and full recursive carrier ratification
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: recursive_carrier_source_fails_closed
#   given: an epicyclic connection proposed as a recursion source
#   then: it must replay exactly from its declared construction inputs; tampering or the zero identity connection is rejected
#   class: safety
#
# id: recursive_carrier_preserves_structural_null_attachment
#   given: any admitted successor transition
#   then: every resulting carrier layer remains attached to the singular Structural Null origin
#   class: correctness
#
# id: recursive_carrier_uses_deck_translation_as_successor
#   given: k positive successor layers
#   then: layer advances by k and native Mobius state advances by exactly k visible laps
#   class: correctness
#
# id: recursive_carrier_radius_is_not_depth
#   given: any admitted successor transition
#   then: radius is inherited unchanged from the source epicyclic placement; recursion does not add depth to radius
#   class: correctness
#
# id: recursive_carrier_two_layers_restore_complete_mobius_state
#   given: two successor layers
#   then: visible phase and local frame return exactly to the source complete Mobius state
#   class: correctness
# === END CONTRACTS ===

"""Candidate recursive carrier successor law.

An epicyclic connection can generate a successor carrier only after the source
edge has replayed exactly from its declared construction inputs.

The successor operation is deliberately minimal and already implied by UCNS
primitives:

* Structural Null remains the singular origin attachment.
* Radius remains the canonical placement radius; recursion does not add depth
  to radius.
* Each successor layer is one visible-lap deck translation.
* Therefore one successor preserves visible phase and reverses the local
  Mobius frame; two successors restore the complete Mobius state.

This is a carrier-successor binding, not a disk/sphere identification and not
ratification of the complete recursive UCNS construction.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from typing import Any

from .direct_mobius import (
    NativeMobiusFrame,
    STRUCTURAL_NULL_ORIGIN,
    native_mobius_state,
)
from .epicyclic_graph import (
    SCHEMA as EPICYCLIC_GRAPH_SCHEMA,
    VERSION as EPICYCLIC_GRAPH_VERSION,
    EpicyclicGraphError,
    build_epicyclic_edge,
)

SCHEMA = "ucns.recursive-carrier-successor-candidate"
VERSION = "0.1.0"


class RecursiveCarrierError(ValueError):
    """Raised when recursive carrier construction fails closed."""


def _canonical(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _receipt(payload: dict[str, Any]) -> str:
    return sha256(_canonical(payload)).hexdigest()


def _parse_phase(value: object) -> Fraction:
    if not isinstance(value, str) or "/" not in value:
        raise RecursiveCarrierError("source phase_turns must be an exact fraction string")
    try:
        numerator_text, denominator_text = value.split("/", 1)
        phase = Fraction(int(numerator_text), int(denominator_text))
    except (ValueError, ZeroDivisionError) as exc:
        raise RecursiveCarrierError("source phase_turns is malformed") from exc
    if not Fraction(0) <= phase < Fraction(1):
        raise RecursiveCarrierError("source phase_turns must be canonical in [0, 1)")
    return phase


def _source_state(edge: dict[str, Any]):
    expansion = edge.get("expansion")
    if not isinstance(expansion, dict):
        raise RecursiveCarrierError("source edge expansion is missing")
    phase = _parse_phase(expansion.get("phase_turns"))
    try:
        frame = NativeMobiusFrame(expansion.get("frame"))
    except ValueError as exc:
        raise RecursiveCarrierError("source edge frame is not a native Mobius frame") from exc
    return native_mobius_state(phase, frame)


def _validate_source_edge(edge: object) -> dict[str, Any]:
    if not isinstance(edge, dict):
        raise RecursiveCarrierError("source edge must be an object")
    if edge.get("schema") != EPICYCLIC_GRAPH_SCHEMA or edge.get("version") != EPICYCLIC_GRAPH_VERSION:
        raise RecursiveCarrierError("source edge schema or version mismatch")

    connection = edge.get("connection")
    if (
        not isinstance(connection, list)
        or len(connection) != 3
        or any(isinstance(v, bool) or not isinstance(v, int) for v in connection)
    ):
        raise RecursiveCarrierError("source connection must contain three exact integers")
    if connection == [0, 0, 0]:
        raise RecursiveCarrierError("identity connection has no spatial expansion to promote")

    try:
        rebuilt = build_epicyclic_edge(
            connection[0],
            connection[1],
            connection[2],
            covering_degree=edge.get("covering_degree"),
        )
    except EpicyclicGraphError as exc:
        raise RecursiveCarrierError(str(exc)) from exc

    if _canonical(rebuilt) != _canonical(edge):
        raise RecursiveCarrierError("source edge does not replay exactly")
    return rebuilt


def _state_payload(state) -> dict[str, str]:
    return {
        "phase_turns": f"{state.phase_turns.numerator}/{state.phase_turns.denominator}",
        "frame": state.frame.value,
    }


def build_recursive_carrier(edge: object, *, steps: int = 1) -> dict[str, Any]:
    """Promote one validated epicyclic connection through successor layers."""

    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 1:
        raise RecursiveCarrierError("steps must be a positive integer")

    source = _validate_source_edge(edge)
    expansion = source["expansion"]
    source_layer = expansion["layer"]
    if isinstance(source_layer, bool) or not isinstance(source_layer, int):
        raise RecursiveCarrierError("source layer must be an integer")

    radius = expansion["radius"]
    if isinstance(radius, bool) or not isinstance(radius, (int, float)):
        raise RecursiveCarrierError("source radius must be numeric")

    source_state = _source_state(source)
    target_state = source_state.advance(steps)

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "source_edge": source,
        "source_edge_receipt_sha256": source["receipt_sha256"],
        "origin_attachment": {
            "origin_id": STRUCTURAL_NULL_ORIGIN.origin_id,
            "carrier_position": STRUCTURAL_NULL_ORIGIN.carrier_position,
        },
        "source_layer": source_layer,
        "target_layer": source_layer + steps,
        "steps": steps,
        "radius": radius,
        "source_mobius": _state_payload(source_state),
        "target_mobius": _state_payload(target_state),
        "successor_law": "one successor layer = one visible-lap deck translation",
        "standing": "candidate",
        "hmmm": (
            "disk/sphere identification, direct distant-scale coupling, and full "
            "circle-to-epicycle-to-disk-to-sphere recursive closure remain unresolved"
        ),
    }
    payload["receipt_sha256"] = _receipt(payload)
    return payload


def replay_recursive_carrier(data: bytes) -> dict[str, Any]:
    """Rebuild and verify a recursive-carrier receipt byte-identically."""

    if not isinstance(data, bytes):
        raise RecursiveCarrierError("recursive carrier record must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RecursiveCarrierError("recursive carrier record is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise RecursiveCarrierError("recursive carrier record root must be an object")
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise RecursiveCarrierError("recursive carrier schema or version mismatch")

    rebuilt = build_recursive_carrier(obj.get("source_edge"), steps=obj.get("steps"))
    if rebuilt["receipt_sha256"] != obj.get("receipt_sha256"):
        raise RecursiveCarrierError("recursive carrier receipt does not match recomputation")
    if _canonical(rebuilt) != data:
        raise RecursiveCarrierError("recursive carrier record does not replay byte-identically")
    return rebuilt


__all__ = [
    "SCHEMA",
    "VERSION",
    "RecursiveCarrierError",
    "build_recursive_carrier",
    "replay_recursive_carrier",
]
