# === MODULE_BUILD ===
# id: ucns_relational_carrier
#   module_name: relational_carrier
#   module_kind: schema
#   summary: constructs deterministic metadata-free ordered relational carriers from dense occurrence addresses and caller-declared relation codes
#   owner: Erin Spencer
#   public_surface: RelationalNode, RelationalEdge, RelationalCarrier, build_relational_carrier, relational_carrier_bytes, parse_relational_carrier
#   internal_surface: _canonical_bytes
#   auth_boundary: none
#   storage_boundary: serialized intrinsic representation bytes only
#   network_boundary: none
#   user_data_boundary: accepts integers only; domain evidence and provenance remain external
#   admin_only: false
#   tests: tests.test_relational_carrier
#   rollout: explicit non-geometric representation bridge; no consumer activation or canonical UCNS object
#   rollback: remove module and exports without changing carrier, geometry, measurement, or option decisions
#   requires: none
#   since: 2026-08-16
#   unresolved: geometric assignment, higher-gonol composition, canonical structural equivalence, M, B, and domain interpretation of relation codes
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: relational_carrier_is_intrinsic_and_metadata_free
#   given: a relational carrier is constructed or parsed
#   then: its complete intrinsic payload contains only schema identity, dense integer node addresses, ordered typed integer relations, and permanently false transfer fields
#   class: safety
#   since: 2026-08-16
#
# id: relational_carrier_preserves_order_multiplicity_and_sidedness
#   given: node order, edge order, multiplicity, relation code, endpoint, or sidedness differs
#   then: the canonical bytes and stable identity differ without sorting or deduplication
#   class: correctness
#   since: 2026-08-16
#
# id: relational_carrier_roundtrip_is_canonical
#   given: canonical carrier bytes are parsed and serialized again
#   then: the resulting bytes are exactly identical and malformed or noncanonical input fails closed
#   class: evidence
#   since: 2026-08-16
# === END CONTRACTS ===

"""A metadata-free UCNS-owned relational representation boundary.

This is an intrinsic *representation*, not a complete ``UCNSObject`` and not a
placement, geometry, composition, equivalence, measurement, or theorem law.
Domain owners keep labels, language evidence, provenance, and the meaning of
relation codes in separately frozen identity bindings.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Iterable

SCHEMA_ID = "ucns.relational-carrier"
SCHEMA_VERSION = "1.0.0"


class RelationalCarrierError(ValueError):
    """Raised when intrinsic relational representation is not exact."""


@dataclass(frozen=True, slots=True)
class RelationalNode:
    """One dense intrinsic occurrence address."""

    address: int

    def __post_init__(self) -> None:
        if isinstance(self.address, bool) or not isinstance(self.address, int):
            raise RelationalCarrierError("node address must be an integer")
        if self.address < 0:
            raise RelationalCarrierError("node address must be nonnegative")


@dataclass(frozen=True, slots=True)
class RelationalEdge:
    """One ordered, directed, typed relation occurrence."""

    source: int
    relation: int
    target: int

    def __post_init__(self) -> None:
        for name, value in (
            ("source", self.source),
            ("relation", self.relation),
            ("target", self.target),
        ):
            if isinstance(value, bool) or not isinstance(value, int):
                raise RelationalCarrierError(f"edge {name} must be an integer")
            if value < 0:
                raise RelationalCarrierError(f"edge {name} must be nonnegative")


@dataclass(frozen=True, slots=True)
class RelationalCarrier:
    """Exact ordered relational carrier with no domain metadata."""

    nodes: tuple[RelationalNode, ...]
    edges: tuple[RelationalEdge, ...]
    schema_id: str = SCHEMA_ID
    schema_version: str = SCHEMA_VERSION
    geometry_attached: bool = False
    measurement_attached: bool = False
    theorem_status_transfer: bool = False

    def __post_init__(self) -> None:
        if self.schema_id != SCHEMA_ID or self.schema_version != SCHEMA_VERSION:
            raise RelationalCarrierError("relational carrier schema mismatch")
        if self.geometry_attached or self.measurement_attached or self.theorem_status_transfer:
            raise RelationalCarrierError("geometry, measurement, and theorem transfer are forbidden")
        addresses = tuple(node.address for node in self.nodes)
        if addresses != tuple(range(len(self.nodes))):
            raise RelationalCarrierError("node addresses must be dense and ordered from zero")
        limit = len(self.nodes)
        if any(edge.source >= limit or edge.target >= limit for edge in self.edges):
            raise RelationalCarrierError("edge endpoint is outside the node carrier")

    def as_payload(self) -> dict[str, object]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "nodes": [node.address for node in self.nodes],
            "edges": [
                [edge.source, edge.relation, edge.target] for edge in self.edges
            ],
            "geometry_attached": self.geometry_attached,
            "measurement_attached": self.measurement_attached,
            "theorem_status_transfer": self.theorem_status_transfer,
        }

    @property
    def stable_identity(self) -> str:
        return f"{SCHEMA_ID}:sha256:{sha256(relational_carrier_bytes(self)).hexdigest()}"


def _canonical_bytes(payload: object) -> bytes:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"


def build_relational_carrier(
    node_count: int,
    edges: Iterable[tuple[int, int, int] | RelationalEdge],
) -> RelationalCarrier:
    """Build one intrinsic carrier while preserving supplied edge order."""

    if isinstance(node_count, bool) or not isinstance(node_count, int) or node_count < 0:
        raise RelationalCarrierError("node_count must be a nonnegative integer")
    edge_values = tuple(
        edge if isinstance(edge, RelationalEdge) else RelationalEdge(*edge)
        for edge in edges
    )
    return RelationalCarrier(
        nodes=tuple(RelationalNode(address) for address in range(node_count)),
        edges=edge_values,
    )


def relational_carrier_bytes(carrier: RelationalCarrier) -> bytes:
    """Return the sole canonical byte encoding of an intrinsic carrier."""

    if not isinstance(carrier, RelationalCarrier):
        raise TypeError("carrier must be a RelationalCarrier")
    return _canonical_bytes(carrier.as_payload())


def parse_relational_carrier(payload: bytes) -> RelationalCarrier:
    """Parse exact canonical bytes and reject aliases or unknown fields."""

    if not isinstance(payload, bytes):
        raise TypeError("payload must be bytes")
    try:
        value = json.loads(payload.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RelationalCarrierError("carrier must be strict UTF-8 JSON") from exc
    if not isinstance(value, dict) or set(value) != {
        "schema_id", "schema_version", "nodes", "edges", "geometry_attached",
        "measurement_attached", "theorem_status_transfer",
    }:
        raise RelationalCarrierError("carrier fields must match the exact schema")
    if not isinstance(value["nodes"], list) or not isinstance(value["edges"], list):
        raise RelationalCarrierError("nodes and edges must be arrays")
    try:
        carrier = RelationalCarrier(
            nodes=tuple(RelationalNode(item) for item in value["nodes"]),
            edges=tuple(RelationalEdge(*item) for item in value["edges"]),
            schema_id=value["schema_id"],
            schema_version=value["schema_version"],
            geometry_attached=value["geometry_attached"],
            measurement_attached=value["measurement_attached"],
            theorem_status_transfer=value["theorem_status_transfer"],
        )
    except (TypeError, RelationalCarrierError) as exc:
        raise RelationalCarrierError("invalid relational carrier payload") from exc
    if relational_carrier_bytes(carrier) != payload:
        raise RelationalCarrierError("carrier bytes are not canonical")
    return carrier


__all__ = [
    "RelationalCarrier", "RelationalCarrierError", "RelationalEdge",
    "RelationalNode", "build_relational_carrier", "parse_relational_carrier",
    "relational_carrier_bytes",
]
