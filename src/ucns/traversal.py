# === MODULE_BUILD ===
# id: cycle_safe_traversal_policy
#   module_name: traversal
#   module_kind: instrument
#   summary: traverses recursive evidence under explicit cycle, shared-reference, identity, depth, node, and fixed-point policies
#   owner: Erin Spencer
#   public_surface: CycleMode, TraversalBudget, TraversalPolicy, Visit, ReferenceReceipt, TruncationReceipt, FixedPointReceipt, TraversalResult, CycleDetectedError, traverse
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_traversal.py
#   rollout: recursive-evidence research infrastructure only
#   rollback: remove traversal exports; recursive candidates fail closed
#   requires: retained_structure_envelope
#   since: 2026-07-21
#   unresolved: canonical recursive identity, sharing, and fixed-point semantics
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: recursive_cycles_require_explicit_policy
#   given: retained recursive evidence repeats an identity on the active path
#   then: traversal rejects, references, depth-unfolds, or invokes a fixed-point resolver only as explicitly selected
#   class: safety
#   since: 2026-07-21
#
# id: shared_identity_references_are_retained
#   given: reference traversal encounters an identity previously visited on another path
#   then: traversal emits a ReferenceReceipt to the first path rather than double-counting or silently discarding shared structure
#   class: evidence
#   since: 2026-07-21
#
# id: traversal_budgets_emit_receipts
#   given: recursive traversal reaches a depth or node budget
#   then: traversal stops that path and retains a TruncationReceipt rather than silently dropping evidence
#   class: evidence
#   since: 2026-07-21
#
# id: fixed_point_traversal_requires_resolver
#   given: fixed-point cycle handling is selected
#   then: construction fails unless an explicit resolver is supplied
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from enum import Enum
from typing import Any, Hashable


class CycleMode(str, Enum):
    REJECT = "reject"
    REFERENCE = "reference"
    UNFOLD_TO_DEPTH = "unfold-to-depth"
    FIXED_POINT = "fixed-point"


@dataclass(frozen=True, slots=True)
class TraversalBudget:
    max_depth: int = 64
    max_nodes: int = 10000

    def __post_init__(self) -> None:
        if self.max_depth < 0 or self.max_nodes <= 0:
            raise ValueError(
                "traversal budget requires max_depth >= 0 and max_nodes > 0"
            )


@dataclass(frozen=True, slots=True)
class TruncationReceipt:
    reason: str
    identity: Hashable
    depth: int
    path: tuple[Hashable, ...]


@dataclass(frozen=True, slots=True)
class ReferenceReceipt:
    identity: Hashable
    first_path: tuple[Hashable, ...]
    repeated_path: tuple[Hashable, ...]


@dataclass(frozen=True, slots=True)
class FixedPointReceipt:
    identity: Hashable
    path: tuple[Hashable, ...]
    value: Any


@dataclass(frozen=True, slots=True)
class Visit:
    identity: Hashable
    node: Any
    depth: int
    path: tuple[Hashable, ...]


FixedPointResolver = Callable[[Any, tuple[Hashable, ...]], Any]


@dataclass(frozen=True, slots=True)
class TraversalPolicy:
    name: str
    cycle_mode: CycleMode
    budget: TraversalBudget = TraversalBudget()
    fixed_point_resolver: FixedPointResolver | None = None
    version: str = "1"

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.version.strip():
            raise ValueError("traversal policy name and version must be nonempty")
        object.__setattr__(self, "cycle_mode", CycleMode(self.cycle_mode))
        if self.cycle_mode is CycleMode.FIXED_POINT and not callable(
            self.fixed_point_resolver
        ):
            raise ValueError("fixed-point traversal requires a resolver")
        if (
            self.cycle_mode is not CycleMode.FIXED_POINT
            and self.fixed_point_resolver is not None
        ):
            raise ValueError(
                "fixed-point resolver is valid only for fixed-point traversal"
            )


@dataclass(frozen=True, slots=True)
class TraversalResult:
    policy_name: str
    visits: tuple[Visit, ...]
    references: tuple[ReferenceReceipt, ...]
    truncations: tuple[TruncationReceipt, ...]
    fixed_points: tuple[FixedPointReceipt, ...]

    @property
    def complete(self) -> bool:
        return not self.truncations


class CycleDetectedError(ValueError):
    pass


Children = Callable[[Any], Iterable[Any]]
Identity = Callable[[Any], Hashable]


def traverse(
    root: Any,
    *,
    children: Children,
    identity: Identity,
    policy: TraversalPolicy,
) -> TraversalResult:
    if not callable(children) or not callable(identity):
        raise TypeError("children and identity must be callable")

    visits: list[Visit] = []
    references: list[ReferenceReceipt] = []
    truncations: list[TruncationReceipt] = []
    fixed_points: list[FixedPointReceipt] = []
    first_paths: dict[Hashable, tuple[Hashable, ...]] = {}

    def walk(node: Any, depth: int, ancestry: tuple[Hashable, ...]) -> None:
        node_id = identity(node)
        try:
            hash(node_id)
        except TypeError as exc:
            raise TypeError("traversal identity must be hashable") from exc

        path = ancestry + (node_id,)
        if len(visits) >= policy.budget.max_nodes:
            truncations.append(
                TruncationReceipt("max-nodes", node_id, depth, path)
            )
            return
        if depth > policy.budget.max_depth:
            truncations.append(
                TruncationReceipt("max-depth", node_id, depth, path)
            )
            return

        is_cycle = node_id in ancestry
        if is_cycle:
            first_path = first_paths.get(node_id, (node_id,))
            if policy.cycle_mode is CycleMode.REJECT:
                raise CycleDetectedError(f"cycle detected at {node_id!r}")
            if policy.cycle_mode is CycleMode.REFERENCE:
                references.append(ReferenceReceipt(node_id, first_path, path))
                return
            if policy.cycle_mode is CycleMode.UNFOLD_TO_DEPTH:
                if depth >= policy.budget.max_depth:
                    truncations.append(
                        TruncationReceipt("cycle-depth", node_id, depth, path)
                    )
                    return
            elif policy.cycle_mode is CycleMode.FIXED_POINT:
                assert policy.fixed_point_resolver is not None
                fixed_points.append(
                    FixedPointReceipt(
                        node_id,
                        path,
                        policy.fixed_point_resolver(node, path),
                    )
                )
                return
        elif (
            node_id in first_paths
            and policy.cycle_mode is CycleMode.REFERENCE
        ):
            references.append(
                ReferenceReceipt(node_id, first_paths[node_id], path)
            )
            return

        first_paths.setdefault(node_id, path)
        visits.append(Visit(node_id, node, depth, path))
        for child in tuple(children(node)):
            walk(child, depth + 1, path)

    walk(root, 0, ())
    return TraversalResult(
        policy.name,
        tuple(visits),
        tuple(references),
        tuple(truncations),
        tuple(fixed_points),
    )
