# === MODULE_BUILD ===
# id: structural_choice_policy_layer
#   module_name: policy
#   module_kind: instrument
#   summary: registers explicit structural interpretations and returns reversible projections with declared information loss
#   owner: Erin Spencer
#   public_surface: InformationLoss, Projection, StructurePolicy, PolicyRegistry, OccurrenceGroup, SetEntry, apply_policy, ordered_sequence_policy, unordered_multiset_policy, set_policy
#   internal_surface: _no_losses, _require_hashable
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_policy.py
#   rollout: importable candidate-policy infrastructure; no canonical structural policy
#   rollback: remove public exports and this module
#   requires: structural_cell_support_floor
#   since: 2026-07-21
#   unresolved: graph policy, tree policy, canonical structural equivalence
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: policy_registry_preserves_multiple_choices
#   given: multiple named structural policies are registered
#   then: every policy remains independently addressable and no default winner is appointed
#   class: doctrine
#   since: 2026-07-21
#
# id: projection_retains_source_and_declares_loss
#   given: a policy projects retained evidence into a view
#   then: the untouched source remains attached and every ignored or discarded distinction is explicitly reported
#   class: safety
#   since: 2026-07-21
#
# id: lossy_builtin_policies_require_explicit_keys
#   given: multiset or set semantics are requested for arbitrary evidence
#   then: the caller supplies the identity key and UCNS does not invent equality or hashing semantics
#   class: safety
#   since: 2026-07-21
#
# id: unknown_policy_names_fail_closed
#   given: a caller requests a policy name absent from the selected registry
#   then: policy application raises rather than choosing a fallback
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

"""Explicit structural-choice policies without implicit canonization."""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class InformationLoss:
    """One distinction ignored or discarded by a projected view."""

    dimension: str
    description: str
    recoverable_from_source: bool = True

    def __post_init__(self) -> None:
        if not self.dimension.strip():
            raise ValueError("information-loss dimension must be nonempty")
        if not self.description.strip():
            raise ValueError("information-loss description must be nonempty")


@dataclass(frozen=True, slots=True)
class Projection:
    """A policy view that keeps the untouched source available for later choices."""

    policy_name: str
    source: Any
    view: Any
    losses: tuple[InformationLoss, ...] = ()

    def __post_init__(self) -> None:
        if not self.policy_name.strip():
            raise ValueError("projection policy name must be nonempty")
        object.__setattr__(self, "losses", tuple(self.losses))

    @property
    def is_lossy(self) -> bool:
        return bool(self.losses)

    @property
    def recoverable(self) -> bool:
        return all(loss.recoverable_from_source for loss in self.losses)


Projector = Callable[[Any], Any]
LossReporter = Callable[[Any, Any], Iterable[InformationLoss]]


def _no_losses(source: Any, view: Any) -> tuple[InformationLoss, ...]:
    del source, view
    return ()


@dataclass(frozen=True, slots=True)
class StructurePolicy:
    """A named interpretation that projects evidence without rewriting it."""

    name: str
    description: str
    projector: Projector
    loss_reporter: LossReporter = _no_losses

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("policy name must be nonempty")
        if not self.description.strip():
            raise ValueError("policy description must be nonempty")
        if not callable(self.projector) or not callable(self.loss_reporter):
            raise TypeError("policy projector and loss reporter must be callable")

    def apply(self, source: Any) -> Projection:
        view = self.projector(source)
        losses = tuple(self.loss_reporter(source, view))
        return Projection(self.name, source, view, losses)


@dataclass(slots=True)
class PolicyRegistry:
    """A collection of independently addressable policies with no default."""

    _policies: dict[str, StructurePolicy] = field(default_factory=dict, repr=False)

    def register(self, policy: StructurePolicy, *, replace: bool = False) -> None:
        if policy.name in self._policies and not replace:
            raise ValueError(f"policy already registered: {policy.name}")
        self._policies[policy.name] = policy

    def resolve(self, name: str) -> StructurePolicy:
        try:
            return self._policies[name]
        except KeyError as exc:
            raise KeyError(f"unknown structural policy: {name}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(self._policies)

    def policies(self) -> tuple[StructurePolicy, ...]:
        return tuple(self._policies.values())


@dataclass(frozen=True, slots=True)
class OccurrenceGroup:
    """Occurrences sharing a caller-supplied identity key."""

    key: Hashable
    occurrences: tuple[Any, ...]

    @property
    def count(self) -> int:
        return len(self.occurrences)


@dataclass(frozen=True, slots=True)
class SetEntry:
    """One representative retained by a caller-keyed set view."""

    key: Hashable
    representative: Any


def _require_hashable(value: Any) -> Hashable:
    try:
        hash(value)
    except TypeError as exc:
        raise TypeError("policy identity key must return a hashable value") from exc
    return value


def apply_policy(
    source: Any,
    policy: StructurePolicy | str,
    *,
    registry: PolicyRegistry | None = None,
) -> Projection:
    """Apply a policy object or an explicitly resolved registry name."""

    if isinstance(policy, str):
        if registry is None:
            raise ValueError("a registry is required when applying a policy by name")
        selected = registry.resolve(policy)
    elif isinstance(policy, StructurePolicy):
        selected = policy
    else:
        raise TypeError("policy must be a StructurePolicy or registered policy name")
    return selected.apply(source)


def ordered_sequence_policy(*, name: str = "ordered-sequence") -> StructurePolicy:
    """Retain encounter order and multiplicity in the projected view."""

    return StructurePolicy(
        name=name,
        description="retain encounter order, multiplicity, and sidedness",
        projector=lambda source: tuple(source),
    )


def unordered_multiset_policy(
    key: Callable[[Any], Hashable], *, name: str = "unordered-multiset"
) -> StructurePolicy:
    """Retain keyed multiplicity while declaring encounter order ignored."""

    if not callable(key):
        raise TypeError("multiset policy key must be callable")

    def projector(source: Any) -> tuple[OccurrenceGroup, ...]:
        groups: dict[Hashable, list[Any]] = {}
        for occurrence in tuple(source):
            identity = _require_hashable(key(occurrence))
            groups.setdefault(identity, []).append(occurrence)
        return tuple(
            OccurrenceGroup(identity, tuple(occurrences))
            for identity, occurrences in groups.items()
        )

    def losses(source: Any, view: Any) -> tuple[InformationLoss, ...]:
        del source, view
        return (
            InformationLoss(
                "order",
                "encounter order is ignored by multiset semantics; source order remains attached",
            ),
        )

    return StructurePolicy(
        name=name,
        description="group caller-keyed occurrences while retaining multiplicity",
        projector=projector,
        loss_reporter=losses,
    )


def set_policy(
    key: Callable[[Any], Hashable], *, name: str = "set"
) -> StructurePolicy:
    """Retain one caller-keyed representative and declare order/multiplicity ignored."""

    if not callable(key):
        raise TypeError("set policy key must be callable")

    def projector(source: Any) -> tuple[SetEntry, ...]:
        representatives: dict[Hashable, Any] = {}
        for occurrence in tuple(source):
            identity = _require_hashable(key(occurrence))
            representatives.setdefault(identity, occurrence)
        return tuple(
            SetEntry(identity, representative)
            for identity, representative in representatives.items()
        )

    def losses(source: Any, view: Any) -> tuple[InformationLoss, ...]:
        del source, view
        return (
            InformationLoss(
                "order",
                "encounter order is ignored by set semantics; source order remains attached",
            ),
            InformationLoss(
                "multiplicity",
                "duplicate multiplicity is ignored by set semantics; occurrences remain attached to the source",
            ),
        )

    return StructurePolicy(
        name=name,
        description="retain one representative per caller-supplied identity key",
        projector=projector,
        loss_reporter=losses,
    )
