# === MODULE_BUILD ===
# id: ucns_singleton_axis_geometry
#   module_name: singleton_geometry
#   module_kind: geometry
#   summary: generic singleton-axis construction geometry with occurrence paths, finite cyclic closure, unit-circle relations, exact tangency, attention frames, and framed Mobius views
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, SingletonGeometryError, SingletonRecord, SingletonAxis, OccurrenceRecord, OccurrenceLedger, ClosureEdge, ClosureGraph, UnitCircleRelation, TangencyRecord, relation_tangency, AttentionFrame, MobiusFrameRecord, build_mobius_frame, advance_mobius_frame, SingletonConstruct, SingletonConstructBuilder
#   internal_surface: canonical serialization, deterministic strong-component cycle detection
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_singleton_geometry
#   rollout: generic geometry candidate; downstream domains supply identities, provenance, and declared circle centers/radii
#   rollback: remove this module, facade exports, tests, and documentation
#   requires: ucns_native_mobius_geometry
#   since: 2026-09-13
#   unresolved: the exact law selecting center/radius turns for bare unit-circle relations; tangency between undeclared circles remains hmmm
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: singleton_axis_admits_exactly_one_record_per_identity
#   given: a SingletonAxis
#   then: admitting an identity returns the same ordinal record on reuse and appends exactly one new record for a new identity
#   class: correctness
#   since: 2026-09-13
#
# id: occurrence_records_are_ordinal_and_provenance_bearing
#   given: an OccurrenceLedger records occurrences against an axis
#   then: each record carries a 1-based occurrence ordinal and an exact provenance path tuple, and reusing a singleton increments only the occurrence ordinal
#   class: correctness
#   since: 2026-09-13
#
# id: closure_graph_is_finite_and_deterministic
#   given: a finite set of ClosureEdges
#   then: ClosureGraph.build returns sorted unique nodes and edges and a deterministic cyclic decomposition with no node or edge invented
#   class: correctness
#   since: 2026-09-13
#
# id: unit_circle_relation_positions_are_exact_turns
#   given: a unit-circle relation with modulus m and canonical residues
#   then: positions are recorded as exact r/m Fractions and density is the exact Fraction len(positions)/m
#   class: correctness
#   since: 2026-09-13
#
# id: tangency_never_invents_undeclared_geometry
#   given: two unit-circle relations
#   then: exact external/internal tangency is recorded only from declared exact center and radius turns; undeclared geometry returns an explicit hmmm record
#   class: safety
#   since: 2026-09-13
#
# id: mobius_frame_preserves_native_return_law
#   given: a MobiusFrameRecord wrapping an attention frame
#   then: one visible turn reverses the local frame and two visible turns restore the complete frame state
#   class: correctness
#   since: 2026-09-13
#
# id: singleton_construct_serializes_canonically_and_replays_byte_identically
#   given: two independently built SingletonConstructs with identical recorded content
#   then: canonical_bytes and receipt_sha256 are byte-identical
#   class: correctness
#   since: 2026-09-13
# === END CONTRACTS ===

"""Generic singleton-axis construction geometry.

This module owns geometry machinery only:

* one singleton per admitted identity on a named axis;
* ordinal, provenance-bearing occurrence records;
* deterministic finite closure into cyclic structure with cycle detection;
* exact unit-circle relation positions and density;
* exact circle tangency only where center and radius turns are declared;
* attention frames (declared projections, non-mutating);
* framed Mobius views that preserve the native 360/720-degree return law.

Identities, axis names, provenance strings, and relation ids are opaque
caller-supplied scalars. UCNS does not divide them into lexical, semantic, or
corpus classes, and never invents center/radius geometry for relations that
have not declared it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from hashlib import sha256
import json
from typing import Any, Iterable, Mapping, Sequence

from .direct_mobius import NativeMobiusFrame, NativeMobiusState

SCHEMA = "ucns.singleton-construct"
VERSION = "1.0.0"

_UNIT_TURN = Fraction(1)


class SingletonGeometryError(ValueError):
    """Raised when a requested construction is outside the declared geometry."""


@dataclass(frozen=True, slots=True)
class SingletonRecord:
    """One admitted singleton on one axis."""

    axis_id: str
    ordinal: int
    identity: str

    def __post_init__(self) -> None:
        if isinstance(self.ordinal, bool) or not isinstance(self.ordinal, int) or self.ordinal < 0:
            raise SingletonGeometryError("singleton ordinal must be a non-negative integer")
        if not isinstance(self.axis_id, str) or not self.axis_id:
            raise SingletonGeometryError("axis_id must be a non-empty string")
        if not isinstance(self.identity, str) or not self.identity:
            raise SingletonGeometryError("identity must be a non-empty string")


class SingletonAxis:
    """One named axis admitting exactly one singleton per identity."""

    def __init__(self, axis_id: str) -> None:
        if not isinstance(axis_id, str) or not axis_id:
            raise SingletonGeometryError("axis_id must be a non-empty string")
        self.axis_id = axis_id
        self._by_identity: dict[str, SingletonRecord] = {}
        self._records: list[SingletonRecord] = []

    def admit(self, identity: str) -> SingletonRecord:
        if not isinstance(identity, str) or not identity:
            raise SingletonGeometryError("identity must be a non-empty string")
        existing = self._by_identity.get(identity)
        if existing is not None:
            return existing
        record = SingletonRecord(self.axis_id, len(self._records), identity)
        self._by_identity[identity] = record
        self._records.append(record)
        return record

    def singleton(self, identity: str) -> SingletonRecord | None:
        if not isinstance(identity, str) or not identity:
            raise SingletonGeometryError("identity must be a non-empty string")
        return self._by_identity.get(identity)

    @property
    def records(self) -> tuple[SingletonRecord, ...]:
        return tuple(self._records)

    def __len__(self) -> int:
        return len(self._records)

    def __repr__(self) -> str:
        return f"SingletonAxis({self.axis_id!r}, {len(self._records)} singletons)"


@dataclass(frozen=True, slots=True)
class OccurrenceRecord:
    """One ordinal, provenance-bearing occurrence of a singleton."""

    axis_id: str
    ordinal: int
    identity: str
    provenance: tuple[str, ...]

    def __post_init__(self) -> None:
        if isinstance(self.ordinal, bool) or not isinstance(self.ordinal, int) or self.ordinal < 1:
            raise SingletonGeometryError("occurrence ordinal must be a positive integer")
        if not isinstance(self.axis_id, str) or not self.axis_id:
            raise SingletonGeometryError("axis_id must be a non-empty string")
        if not isinstance(self.identity, str) or not self.identity:
            raise SingletonGeometryError("identity must be a non-empty string")
        if not all(isinstance(step, str) and step for step in self.provenance):
            raise SingletonGeometryError("provenance steps must be non-empty strings")


class OccurrenceLedger:
    """Records occurrences per axis with 1-based ordinals."""

    def __init__(self) -> None:
        self._counts: dict[str, int] = {}
        self._records: list[OccurrenceRecord] = []

    def record(
        self,
        axis_id: str,
        identity: str,
        provenance: Sequence[str],
    ) -> OccurrenceRecord:
        if not isinstance(axis_id, str) or not axis_id:
            raise SingletonGeometryError("axis_id must be a non-empty string")
        ordinal = self._counts.get(axis_id, 0) + 1
        self._counts[axis_id] = ordinal
        record = OccurrenceRecord(axis_id, ordinal, identity, tuple(provenance))
        self._records.append(record)
        return record

    @property
    def records(self) -> tuple[OccurrenceRecord, ...]:
        return tuple(self._records)

    def occurrence_count(self, axis_id: str) -> int:
        return self._counts.get(axis_id, 0)


@dataclass(frozen=True, slots=True)
class ClosureEdge:
    """One directed reuse edge between two admitted singletons."""

    source_axis: str
    source_identity: str
    relation: str
    target_axis: str
    target_identity: str

    def __post_init__(self) -> None:
        for value in (
            self.source_axis,
            self.source_identity,
            self.relation,
            self.target_axis,
            self.target_identity,
        ):
            if not isinstance(value, str) or not value:
                raise SingletonGeometryError("closure edge fields must be non-empty strings")


def _node(axis: str, identity: str) -> tuple[str, str]:
    return (axis, identity)


def _deterministic_successors(
    edges: Sequence[ClosureEdge],
) -> dict[tuple[str, str], tuple[tuple[str, str], ...]]:
    adjacency: dict[tuple[str, str], set[tuple[str, str]]] = {}
    for edge in edges:
        source = _node(edge.source_axis, edge.source_identity)
        target = _node(edge.target_axis, edge.target_identity)
        adjacency.setdefault(source, set()).add(target)
        adjacency.setdefault(target, set())
    return {
        node: tuple(sorted(targets))
        for node, targets in sorted(adjacency.items())
    }


def _strong_components(
    adjacency: Mapping[tuple[str, str], Sequence[tuple[str, str]]],
) -> tuple[tuple[tuple[str, str], ...], ...]:
    """Deterministic iterative Tarjan strong-component decomposition."""

    nodes = tuple(adjacency.keys())
    index = 0
    indices: dict[tuple[str, str], int] = {}
    lowlinks: dict[tuple[str, str], int] = {}
    on_stack: set[tuple[str, str]] = set()
    stack: list[tuple[str, str]] = []
    components: list[tuple[tuple[str, str], ...]] = []

    for root in nodes:
        if root in indices:
            continue
        call_stack: list[tuple[tuple[str, str], int]] = [(root, 0)]
        while call_stack:
            node, next_index = call_stack[-1]
            if next_index == 0:
                indices[node] = index
                lowlinks[node] = index
                index += 1
                stack.append(node)
                on_stack.add(node)
            successors = adjacency.get(node, ())
            if next_index < len(successors):
                successor = successors[next_index]
                call_stack[-1] = (node, next_index + 1)
                if successor not in indices:
                    call_stack.append((successor, 0))
                elif successor in on_stack:
                    lowlinks[node] = min(lowlinks[node], indices[successor])
            else:
                call_stack.pop()
                if call_stack:
                    parent = call_stack[-1][0]
                    lowlinks[parent] = min(lowlinks[parent], lowlinks[node])
                if lowlinks[node] == indices[node]:
                    component: list[tuple[str, str]] = []
                    while True:
                        member = stack.pop()
                        on_stack.discard(member)
                        component.append(member)
                        if member == node:
                            break
                    components.append(tuple(sorted(component)))

    return tuple(sorted(components))


def _representative_cycle(
    component: tuple[tuple[str, str], ...],
    adjacency: Mapping[tuple[str, str], Sequence[tuple[str, str]]],
) -> tuple[tuple[str, str], ...]:
    """Return one canonical cycle for a cyclic strong component."""

    if len(component) == 1 and component[0] in adjacency.get(component[0], ()):
        return (component[0], component[0])

    allowed = set(component)
    start = component[0]
    walk: list[tuple[str, str]] = [start]
    seen: dict[tuple[str, str], int] = {start: 0}
    current = start
    while True:
        successors = adjacency.get(current, ())
        chosen: tuple[str, str] | None = None
        for successor in successors:
            if successor in allowed:
                chosen = successor
                break
        if chosen is None:
            raise SingletonGeometryError("cyclic component has no internal successor")
        if chosen in seen:
            start_index = seen[chosen]
            return tuple(walk[start_index:] + [chosen])
        seen[chosen] = len(walk)
        walk.append(chosen)
        current = chosen


@dataclass(frozen=True, slots=True)
class ClosureGraph:
    """Finite closure graph with deterministic cyclic structure."""

    nodes: tuple[tuple[str, str], ...]
    edges: tuple[ClosureEdge, ...]
    cyclic_nodes: tuple[tuple[str, str], ...]
    cycles: tuple[tuple[tuple[str, str], ...], ...]
    closed: bool = True

    @classmethod
    def build(cls, edges: Iterable[ClosureEdge]) -> "ClosureGraph":
        unique_edges = tuple(
            sorted(
                set(edges),
                key=lambda edge: (
                    edge.source_axis,
                    edge.source_identity,
                    edge.relation,
                    edge.target_axis,
                    edge.target_identity,
                ),
            )
        )
        adjacency = _deterministic_successors(unique_edges)
        nodes = tuple(adjacency.keys())
        components = _strong_components(adjacency)

        cycles: list[tuple[tuple[str, str], ...]] = []
        cyclic_nodes: set[tuple[str, str]] = set()
        for component in components:
            is_cyclic = len(component) > 1 or (
                len(component) == 1 and component[0] in adjacency.get(component[0], ())
            )
            if is_cyclic:
                cycles.append(_representative_cycle(component, adjacency))
                cyclic_nodes.update(component)

        return cls(
            nodes=nodes,
            edges=unique_edges,
            cyclic_nodes=tuple(sorted(cyclic_nodes)),
            cycles=tuple(cycles),
            closed=True,
        )


@dataclass(frozen=True, slots=True)
class UnitCircleRelation:
    """One exact unit-circle relation with canonical residue positions."""

    relation_id: str
    modulus: int
    positions: tuple[int, ...]
    center_turns: Fraction | None = None
    radius_turns: Fraction | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.relation_id, str) or not self.relation_id:
            raise SingletonGeometryError("relation_id must be a non-empty string")
        if isinstance(self.modulus, bool) or not isinstance(self.modulus, int) or self.modulus < 1:
            raise SingletonGeometryError("modulus must be a positive integer")
        canonical = tuple(sorted(set(self.positions)))
        for residue in canonical:
            if isinstance(residue, bool) or not isinstance(residue, int) or not 0 <= residue < self.modulus:
                raise SingletonGeometryError("positions must be canonical residues in [0, modulus)")
        object.__setattr__(self, "positions", canonical)
        for name, value in (("center_turns", self.center_turns), ("radius_turns", self.radius_turns)):
            if value is not None and (
                not isinstance(value, Fraction)
                or isinstance(value, bool)
                or value < 0
                or value >= 1
            ):
                raise SingletonGeometryError(f"{name} must be a Fraction in [0, 1) when declared")

    @property
    def density(self) -> Fraction:
        return Fraction(len(self.positions), self.modulus)

    @property
    def exact_positions(self) -> tuple[Fraction, ...]:
        return tuple(Fraction(residue, self.modulus) for residue in self.positions)


def _circle_distance(a: Fraction, b: Fraction) -> Fraction:
    delta = abs(a - b)
    return min(delta, _UNIT_TURN - delta)


@dataclass(frozen=True, slots=True)
class TangencyRecord:
    """One tangency verdict between two unit-circle relations."""

    relation_a: str
    relation_b: str
    status: str  # "external" | "internal" | "hmmm"
    reason: str
    center_distance_turns: Fraction | None = None

    def __post_init__(self) -> None:
        if self.status not in {"external", "internal", "hmmm"}:
            raise SingletonGeometryError("tangency status must be external, internal, or hmmm")
        if not self.reason:
            raise SingletonGeometryError("tangency reason must be non-empty")


def relation_tangency(a: UnitCircleRelation, b: UnitCircleRelation) -> TangencyRecord | None:
    """Return the exact tangency verdict between two relations.

    Exact external/internal tangency is computed only when both relations
    declare exact center and radius turns. Otherwise the verdict is an
    explicit ``hmmm`` record; no center, radius, or weight is invented.
    """

    if a.relation_id == b.relation_id:
        raise SingletonGeometryError("tangency requires two distinct relations")
    if a.center_turns is None or a.radius_turns is None or b.center_turns is None or b.radius_turns is None:
        return TangencyRecord(
            relation_a=a.relation_id,
            relation_b=b.relation_id,
            status="hmmm",
            reason="center/radius turns are undeclared; tangency remains unresolved without invented geometry",
        )
    distance = _circle_distance(a.center_turns, b.center_turns)
    if distance == a.radius_turns + b.radius_turns:
        return TangencyRecord(
            relation_a=a.relation_id,
            relation_b=b.relation_id,
            status="external",
            reason="exact center distance equals the sum of radii",
            center_distance_turns=distance,
        )
    if distance != 0 and distance == abs(a.radius_turns - b.radius_turns):
        return TangencyRecord(
            relation_a=a.relation_id,
            relation_b=b.relation_id,
            status="internal",
            reason="exact center distance equals the absolute difference of radii",
            center_distance_turns=distance,
        )
    return None


@dataclass(frozen=True, slots=True)
class AttentionFrame:
    """One declared, non-mutating projection view over a construct."""

    frame_id: str
    axis_ids: tuple[str, ...]
    relation_ids: tuple[str, ...]
    projected_fields: tuple[tuple[str, str], ...]
    nonclaims: tuple[str, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.frame_id, str) or not self.frame_id:
            raise SingletonGeometryError("frame_id must be a non-empty string")
        object.__setattr__(self, "axis_ids", tuple(sorted(set(self.axis_ids))))
        object.__setattr__(self, "relation_ids", tuple(sorted(set(self.relation_ids))))
        object.__setattr__(
            self,
            "projected_fields",
            tuple(sorted((str(field), str(value)) for field, value in self.projected_fields)),
        )
        object.__setattr__(self, "nonclaims", tuple(sorted(set(self.nonclaims))))


@dataclass(frozen=True, slots=True)
class MobiusFrameRecord:
    """One attention frame carried on the native framed Mobius quotient."""

    frame_id: str
    attention_frame_id: str
    phase_turns: Fraction
    frame: NativeMobiusFrame

    def __post_init__(self) -> None:
        if not isinstance(self.frame_id, str) or not self.frame_id:
            raise SingletonGeometryError("frame_id must be a non-empty string")
        if not isinstance(self.attention_frame_id, str) or not self.attention_frame_id:
            raise SingletonGeometryError("attention_frame_id must be a non-empty string")
        if not isinstance(self.phase_turns, Fraction) or not 0 <= self.phase_turns < 1:
            raise SingletonGeometryError("phase_turns must be a Fraction in [0, 1)")
        if not isinstance(self.frame, NativeMobiusFrame):
            raise SingletonGeometryError("frame must be a NativeMobiusFrame")


def build_mobius_frame(
    frame_id: str,
    attention_frame_id: str,
    turns: Fraction | int = 0,
) -> MobiusFrameRecord:
    """Wrap an attention frame in a native Mobius frame at an exact phase."""

    state = NativeMobiusState(phase_turns=Fraction(0), frame=NativeMobiusFrame.POSITIVE)
    advanced = state.advance(Fraction(turns))
    return MobiusFrameRecord(
        frame_id=frame_id,
        attention_frame_id=attention_frame_id,
        phase_turns=advanced.phase_turns,
        frame=advanced.frame,
    )


def advance_mobius_frame(
    record: MobiusFrameRecord,
    turns: Fraction | int,
) -> MobiusFrameRecord:
    """Advance a Mobius frame; one visible turn flips, two restore."""

    state = NativeMobiusState(phase_turns=record.phase_turns, frame=record.frame)
    advanced = state.advance(Fraction(turns))
    return MobiusFrameRecord(
        frame_id=record.frame_id,
        attention_frame_id=record.attention_frame_id,
        phase_turns=advanced.phase_turns,
        frame=advanced.frame,
    )


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _fraction_to_str(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True, slots=True)
class SingletonConstruct:
    """Immutable canonical snapshot of a singleton-axis construction."""

    axes: tuple[tuple[str, tuple[str, ...]], ...]
    occurrences: tuple[OccurrenceRecord, ...]
    closure: ClosureGraph
    relation_circles: tuple[UnitCircleRelation, ...]
    tangencies: tuple[TangencyRecord, ...]
    attention_frames: tuple[AttentionFrame, ...]
    mobius_frames: tuple[MobiusFrameRecord, ...]
    hmmm: tuple[str, ...]

    def _payload(self) -> dict[str, Any]:
        return {
            "schema": SCHEMA,
            "version": VERSION,
            "axes": {
                axis_id: list(identities)
                for axis_id, identities in self.axes
            },
            "occurrences": [
                {
                    "axis": record.axis_id,
                    "ordinal": record.ordinal,
                    "identity": record.identity,
                    "provenance": list(record.provenance),
                }
                for record in self.occurrences
            ],
            "closure": {
                "closed": self.closure.closed,
                "nodes": [list(node) for node in self.closure.nodes],
                "edges": [
                    [
                        edge.source_axis,
                        edge.source_identity,
                        edge.relation,
                        edge.target_axis,
                        edge.target_identity,
                    ]
                    for edge in self.closure.edges
                ],
                "cyclic_nodes": [list(node) for node in self.closure.cyclic_nodes],
                "cycles": [
                    [list(node) for node in cycle]
                    for cycle in self.closure.cycles
                ],
            },
            "relation_circles": [
                {
                    "relation_id": circle.relation_id,
                    "modulus": circle.modulus,
                    "positions": list(circle.positions),
                    "center_turns": _fraction_to_str(circle.center_turns) if circle.center_turns is not None else None,
                    "radius_turns": _fraction_to_str(circle.radius_turns) if circle.radius_turns is not None else None,
                    "density": _fraction_to_str(circle.density),
                }
                for circle in self.relation_circles
            ],
            "tangencies": [
                {
                    "relation_a": record.relation_a,
                    "relation_b": record.relation_b,
                    "status": record.status,
                    "reason": record.reason,
                    "center_distance_turns": (
                        _fraction_to_str(record.center_distance_turns)
                        if record.center_distance_turns is not None
                        else None
                    ),
                }
                for record in self.tangencies
            ],
            "attention_frames": [
                {
                    "frame_id": frame.frame_id,
                    "axis_ids": list(frame.axis_ids),
                    "relation_ids": list(frame.relation_ids),
                    "projected_fields": [list(pair) for pair in frame.projected_fields],
                    "nonclaims": list(frame.nonclaims),
                }
                for frame in self.attention_frames
            ],
            "mobius_frames": [
                {
                    "frame_id": frame.frame_id,
                    "attention_frame_id": frame.attention_frame_id,
                    "phase_turns": _fraction_to_str(frame.phase_turns),
                    "frame": frame.frame.value,
                }
                for frame in self.mobius_frames
            ],
            "hmmm": list(self.hmmm),
        }

    def canonical_bytes(self) -> bytes:
        return _canonical_json_bytes(self._payload())

    def receipt_sha256(self) -> str:
        return sha256(self.canonical_bytes()).hexdigest()

    def replay_equals(self, other: "SingletonConstruct") -> bool:
        return self.canonical_bytes() == other.canonical_bytes()


class SingletonConstructBuilder:
    """Deterministic builder for a :class:`SingletonConstruct`."""

    def __init__(self, *, hmmm: Sequence[str] = ()) -> None:
        self._axes: dict[str, SingletonAxis] = {}
        self._ledger = OccurrenceLedger()
        self._edges: list[ClosureEdge] = []
        self._relation_circles: list[UnitCircleRelation] = []
        self._tangencies: list[TangencyRecord] = []
        self._attention_frames: list[AttentionFrame] = []
        self._mobius_frames: list[MobiusFrameRecord] = []
        self._hmmm: list[str] = [str(item) for item in hmmm]

    def axis(self, axis_id: str) -> SingletonAxis:
        if axis_id not in self._axes:
            self._axes[axis_id] = SingletonAxis(axis_id)
        return self._axes[axis_id]

    def admit(self, axis_id: str, identity: str) -> SingletonRecord:
        return self.axis(axis_id).admit(identity)

    def record_occurrence(
        self,
        axis_id: str,
        identity: str,
        provenance: Sequence[str],
    ) -> OccurrenceRecord:
        self.admit(axis_id, identity)
        return self._ledger.record(axis_id, identity, provenance)

    def add_edge(
        self,
        source_axis: str,
        source_identity: str,
        relation: str,
        target_axis: str,
        target_identity: str,
    ) -> ClosureEdge:
        self.admit(source_axis, source_identity)
        self.admit(target_axis, target_identity)
        edge = ClosureEdge(source_axis, source_identity, relation, target_axis, target_identity)
        self._edges.append(edge)
        return edge

    def add_relation_circle(
        self,
        relation_id: str,
        modulus: int,
        positions: Sequence[int],
        *,
        center_turns: Fraction | None = None,
        radius_turns: Fraction | None = None,
    ) -> UnitCircleRelation:
        circle = UnitCircleRelation(
            relation_id=relation_id,
            modulus=modulus,
            positions=tuple(positions),
            center_turns=center_turns,
            radius_turns=radius_turns,
        )
        self._relation_circles.append(circle)
        return circle

    def add_tangency(self, record: TangencyRecord) -> TangencyRecord:
        self._tangencies.append(record)
        return record

    def add_attention_frame(self, frame: AttentionFrame) -> AttentionFrame:
        self._attention_frames.append(frame)
        return frame

    def add_mobius_frame(self, frame: MobiusFrameRecord) -> MobiusFrameRecord:
        self._mobius_frames.append(frame)
        return frame

    def add_hmmm(self, item: str) -> None:
        if not item:
            raise SingletonGeometryError("hmmm item must be non-empty")
        self._hmmm.append(item)

    def build(self) -> SingletonConstruct:
        axes = tuple(
            sorted(
                ((axis_id, axis.records and tuple(record.identity for record in axis.records) or ())
                 for axis_id, axis in self._axes.items()),
                key=lambda pair: pair[0],
            )
        )
        return SingletonConstruct(
            axes=axes,
            occurrences=self._ledger.records,
            closure=ClosureGraph.build(self._edges),
            relation_circles=tuple(self._relation_circles),
            tangencies=tuple(self._tangencies),
            attention_frames=tuple(self._attention_frames),
            mobius_frames=tuple(self._mobius_frames),
            hmmm=tuple(self._hmmm),
        )
