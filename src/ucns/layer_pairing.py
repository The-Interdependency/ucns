# === MODULE_BUILD ===
# id: retained_layer_pairing_laboratory
#   module_name: layer_pairing
#   module_kind: instrument
#   summary: composes retained layers through explicit occurrence-level pairing plans while preserving sources and losses
#   owner: Erin Spencer
#   public_surface: LayerPairMode, UnmatchedLayerMode, LayerRef, LayerPairProjection, LayerPairPolicy, LayerPairRegistry, LayerPairRule, EnvelopePairPlan, LayerPairDecision, EnvelopePairResult, pair_retained, concatenate_layer_policy, cartesian_layer_policy, positional_zip_layer_policy, keep_sides_layer_policy, select_left_layer_policy, select_right_layer_policy, exclude_layer_policy, custom_layer_pair_policy
#   internal_surface: _no_losses, _as_structure, _select
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_layer_pairing.py
#   rollout: candidate envelope-pairing infrastructure; no canonical retained-layer product
#   rollback: remove layer-pairing exports; retained envelopes remain unpaired
#   requires: retained_structure_envelope, structural_cell_support_floor
#   since: 2026-07-21
#   unresolved: canonical retained-layer pairing laws and measurement contributions
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: retained_layer_pairing_requires_explicit_plan
#   given: two retained envelopes contain layer occurrences
#   then: every consumed occurrence is selected by an explicit LayerPairRule and policy name
#   class: doctrine
#   since: 2026-07-21
#
# id: layer_pairing_preserves_sources_and_declares_loss
#   given: a retained-layer pairing policy projects two layer occurrences
#   then: both untouched sources, the projected view, and every declared information loss remain in the result evidence
#   class: safety
#   since: 2026-07-21
#
# id: unmatched_layers_follow_explicit_mode
#   given: retained layer occurrences remain outside the plan
#   then: pairing fails closed, preserves sided occurrences, or excludes them only according to the plan's explicit unmatched mode
#   class: safety
#   since: 2026-07-21
#
# id: retained_pairing_does_not_extend_measurements
#   given: retained layers are paired into a result envelope
#   then: their result layers remain unmeasured and do not silently enter W, M, or B
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from .carrier import STRUCTURAL_NULL
from .envelope import (
    ContributionStatus,
    RetainedEnvelope,
    RetainedLayer,
    RetainedStructure,
    make_retained_structure,
)
from .policy import InformationLoss
from .structure import pair as pair_carriers


class LayerPairMode(str, Enum):
    CONCATENATE = "concatenate"
    CARTESIAN = "cartesian"
    POSITIONAL_ZIP = "positional-zip"
    KEEP_SIDES = "keep-sides"
    SELECT_LEFT = "select-left"
    SELECT_RIGHT = "select-right"
    EXCLUDE = "exclude"
    CUSTOM = "custom"


class UnmatchedLayerMode(str, Enum):
    ERROR = "error"
    PRESERVE_SIDES = "preserve-sides"
    EXCLUDE = "exclude"


@dataclass(frozen=True, slots=True)
class LayerRef:
    name: str
    occurrence: int = 0

    def __post_init__(self) -> None:
        if not self.name.strip() or self.occurrence < 0:
            raise ValueError(
                "layer reference requires a name and nonnegative occurrence"
            )


@dataclass(frozen=True, slots=True)
class LayerPairProjection:
    policy_name: str
    left_source: Any
    right_source: Any
    view: Any
    retained: bool
    losses: tuple[InformationLoss, ...] = ()

    def __post_init__(self) -> None:
        if not self.policy_name.strip():
            raise ValueError("layer-pair policy name must be nonempty")
        object.__setattr__(self, "losses", tuple(self.losses))


LayerProjector = Callable[[Any, Any], Any]
LayerLossReporter = Callable[[Any, Any, Any], Iterable[InformationLoss]]


def _no_losses(
    left: Any, right: Any, view: Any
) -> tuple[InformationLoss, ...]:
    del left, right, view
    return ()


@dataclass(frozen=True, slots=True)
class LayerPairPolicy:
    name: str
    mode: LayerPairMode
    projector: LayerProjector
    loss_reporter: LayerLossReporter = _no_losses
    retained: bool = True
    version: str = "1"
    description: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.version.strip():
            raise ValueError(
                "layer-pair policy name and version must be nonempty"
            )
        object.__setattr__(self, "mode", LayerPairMode(self.mode))
        if not callable(self.projector) or not callable(self.loss_reporter):
            raise TypeError(
                "layer-pair projector and loss reporter must be callable"
            )

    def apply(self, left: Any, right: Any) -> LayerPairProjection:
        view = self.projector(left, right)
        losses = tuple(self.loss_reporter(left, right, view))
        return LayerPairProjection(
            self.name, left, right, view, self.retained, losses
        )


@dataclass(slots=True)
class LayerPairRegistry:
    _policies: dict[str, LayerPairPolicy] = field(
        default_factory=dict, repr=False
    )

    def register(
        self, policy: LayerPairPolicy, *, replace: bool = False
    ) -> None:
        if policy.name in self._policies and not replace:
            raise ValueError(
                f"layer-pair policy already registered: {policy.name}"
            )
        self._policies[policy.name] = policy

    def resolve(self, name: str) -> LayerPairPolicy:
        try:
            return self._policies[name]
        except KeyError as exc:
            raise KeyError(f"unknown layer-pair policy: {name}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(self._policies)


@dataclass(frozen=True, slots=True)
class LayerPairRule:
    left: LayerRef
    right: LayerRef
    policy_name: str
    result_name: str

    def __post_init__(self) -> None:
        if not self.policy_name.strip() or not self.result_name.strip():
            raise ValueError(
                "layer-pair rule requires policy and result names"
            )


@dataclass(frozen=True, slots=True)
class EnvelopePairPlan:
    name: str
    rules: tuple[LayerPairRule, ...]
    unmatched_mode: UnmatchedLayerMode = UnmatchedLayerMode.ERROR
    version: str = "1"

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.version.strip():
            raise ValueError(
                "envelope-pair plan name and version must be nonempty"
            )
        object.__setattr__(self, "rules", tuple(self.rules))
        object.__setattr__(
            self, "unmatched_mode", UnmatchedLayerMode(self.unmatched_mode)
        )
        left_refs = [rule.left for rule in self.rules]
        right_refs = [rule.right for rule in self.rules]
        if len(set(left_refs)) != len(left_refs) or len(set(right_refs)) != len(
            right_refs
        ):
            raise ValueError(
                "a layer occurrence may appear in at most one pairing rule"
            )


@dataclass(frozen=True, slots=True)
class LayerPairDecision:
    rule: LayerPairRule
    projection: LayerPairProjection


@dataclass(frozen=True, slots=True)
class EnvelopePairResult:
    plan_name: str
    left: RetainedEnvelope
    right: RetainedEnvelope
    envelope: RetainedEnvelope
    decisions: tuple[LayerPairDecision, ...]
    unmatched_left: tuple[RetainedLayer, ...]
    unmatched_right: tuple[RetainedLayer, ...]
    losses: tuple[InformationLoss, ...]


def _as_structure(
    value: RetainedEnvelope,
) -> tuple[Any, tuple[RetainedLayer, ...]]:
    if value is STRUCTURAL_NULL:
        return STRUCTURAL_NULL, ()
    if not isinstance(value, RetainedStructure):
        raise TypeError("pair operands must be retained envelopes")
    return value.carrier, value.layers


def _select(
    layers: tuple[RetainedLayer, ...], ref: LayerRef
) -> tuple[int, RetainedLayer]:
    count = -1
    for index, layer in enumerate(layers):
        if layer.name == ref.name:
            count += 1
            if count == ref.occurrence:
                if not layer.retained:
                    raise ValueError(
                        f"selected layer is an absent placeholder: {ref}"
                    )
                return index, layer
    raise IndexError(
        f"no retained layer occurrence {ref.occurrence} for {ref.name!r}"
    )


def pair_retained(
    left: RetainedEnvelope,
    right: RetainedEnvelope,
    plan: EnvelopePairPlan,
    *,
    registry: LayerPairRegistry,
) -> EnvelopePairResult:
    left_carrier, left_layers = _as_structure(left)
    right_carrier, right_layers = _as_structure(right)
    paired_carrier = pair_carriers(left_carrier, right_carrier)

    used_left: set[int] = set()
    used_right: set[int] = set()
    output_layers: list[RetainedLayer] = []
    decisions: list[LayerPairDecision] = []
    losses: list[InformationLoss] = []

    for rule in plan.rules:
        left_index, left_layer = _select(left_layers, rule.left)
        right_index, right_layer = _select(right_layers, rule.right)
        used_left.add(left_index)
        used_right.add(right_index)
        projection = registry.resolve(rule.policy_name).apply(
            left_layer.evidence, right_layer.evidence
        )
        decisions.append(LayerPairDecision(rule, projection))
        losses.extend(projection.losses)
        if projection.retained:
            output_layers.append(
                RetainedLayer(
                    rule.result_name,
                    projection.view,
                    retained=True,
                    contribution_status=ContributionStatus.UNMEASURED,
                )
            )

    unmatched_left = tuple(
        layer
        for index, layer in enumerate(left_layers)
        if layer.retained and index not in used_left
    )
    unmatched_right = tuple(
        layer
        for index, layer in enumerate(right_layers)
        if layer.retained and index not in used_right
    )

    if (
        unmatched_left or unmatched_right
    ) and plan.unmatched_mode is UnmatchedLayerMode.ERROR:
        raise ValueError(
            "retained layer occurrences remain without an explicit pairing rule"
        )

    if plan.unmatched_mode is UnmatchedLayerMode.PRESERVE_SIDES:
        output_layers.extend(
            RetainedLayer(
                f"left:{layer.name}",
                layer.evidence,
                policy_name=layer.policy_name,
            )
            for layer in unmatched_left
        )
        output_layers.extend(
            RetainedLayer(
                f"right:{layer.name}",
                layer.evidence,
                policy_name=layer.policy_name,
            )
            for layer in unmatched_right
        )
    elif plan.unmatched_mode is UnmatchedLayerMode.EXCLUDE:
        losses.extend(
            InformationLoss(
                "unmatched-left",
                f"excluded unmatched left layer {layer.name!r}",
            )
            for layer in unmatched_left
        )
        losses.extend(
            InformationLoss(
                "unmatched-right",
                f"excluded unmatched right layer {layer.name!r}",
            )
            for layer in unmatched_right
        )

    envelope = make_retained_structure(paired_carrier, output_layers)
    return EnvelopePairResult(
        plan.name,
        left,
        right,
        envelope,
        tuple(decisions),
        unmatched_left,
        unmatched_right,
        tuple(losses),
    )


def concatenate_layer_policy(
    *, name: str = "concatenate", version: str = "1"
) -> LayerPairPolicy:
    return LayerPairPolicy(
        name,
        LayerPairMode.CONCATENATE,
        lambda left, right: tuple(left) + tuple(right),
        version=version,
    )


def cartesian_layer_policy(
    *, name: str = "cartesian", version: str = "1"
) -> LayerPairPolicy:
    return LayerPairPolicy(
        name,
        LayerPairMode.CARTESIAN,
        lambda left, right: tuple(
            (first, second)
            for first in tuple(left)
            for second in tuple(right)
        ),
        version=version,
    )


def positional_zip_layer_policy(
    *, name: str = "positional-zip", version: str = "1"
) -> LayerPairPolicy:
    def projector(left: Any, right: Any) -> tuple[tuple[Any, Any], ...]:
        return tuple(zip(tuple(left), tuple(right)))

    def report_losses(
        left: Any, right: Any, view: Any
    ) -> tuple[InformationLoss, ...]:
        del view
        left_count = len(tuple(left))
        right_count = len(tuple(right))
        if left_count == right_count:
            return ()
        return (
            InformationLoss(
                "unpaired-occurrences",
                "positional zip ignored "
                f"{abs(left_count - right_count)} unmatched occurrence(s)",
            ),
        )

    return LayerPairPolicy(
        name,
        LayerPairMode.POSITIONAL_ZIP,
        projector,
        report_losses,
        version=version,
    )


def keep_sides_layer_policy(
    *, name: str = "keep-sides", version: str = "1"
) -> LayerPairPolicy:
    return LayerPairPolicy(
        name,
        LayerPairMode.KEEP_SIDES,
        lambda left, right: (left, right),
        version=version,
    )


def select_left_layer_policy(
    *, name: str = "select-left", version: str = "1"
) -> LayerPairPolicy:
    def report_losses(
        left: Any, right: Any, view: Any
    ) -> tuple[InformationLoss, ...]:
        del left, right, view
        return (
            InformationLoss(
                "right-evidence",
                "right evidence is omitted from the projected view",
            ),
        )

    return LayerPairPolicy(
        name,
        LayerPairMode.SELECT_LEFT,
        lambda left, right: left,
        report_losses,
        version=version,
    )


def select_right_layer_policy(
    *, name: str = "select-right", version: str = "1"
) -> LayerPairPolicy:
    def report_losses(
        left: Any, right: Any, view: Any
    ) -> tuple[InformationLoss, ...]:
        del left, right, view
        return (
            InformationLoss(
                "left-evidence",
                "left evidence is omitted from the projected view",
            ),
        )

    return LayerPairPolicy(
        name,
        LayerPairMode.SELECT_RIGHT,
        lambda left, right: right,
        report_losses,
        version=version,
    )


def exclude_layer_policy(
    *, name: str = "exclude", version: str = "1"
) -> LayerPairPolicy:
    def report_losses(
        left: Any, right: Any, view: Any
    ) -> tuple[InformationLoss, ...]:
        del left, right, view
        return (
            InformationLoss(
                "paired-layer",
                "both selected layer occurrences are excluded from the result",
            ),
        )

    return LayerPairPolicy(
        name,
        LayerPairMode.EXCLUDE,
        lambda left, right: None,
        report_losses,
        retained=False,
        version=version,
    )


def custom_layer_pair_policy(
    name: str,
    projector: LayerProjector,
    *,
    version: str,
    loss_reporter: LayerLossReporter = _no_losses,
    retained: bool = True,
    description: str = "",
) -> LayerPairPolicy:
    return LayerPairPolicy(
        name,
        LayerPairMode.CUSTOM,
        projector,
        loss_reporter,
        retained,
        version,
        description,
    )
