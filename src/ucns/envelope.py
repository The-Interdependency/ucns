# === MODULE_BUILD ===
# id: retained_structure_envelope
#   module_name: envelope
#   module_kind: schema
#   summary: retains optional structural layers without forcing them into cells or silently extending aggregate support
#   owner: Erin Spencer
#   public_surface: ContributionStatus, RetainedLayer, RetainedStructure, RetainedEnvelope, make_retained_structure, cell_support_weight, project_layer
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_envelope.py
#   rollout: importable evidence envelope; not a complete UCNS object
#   rollback: remove public exports and this module
#   requires: structural_cell_support_floor, structural_choice_policy_layer
#   since: 2026-07-21
#   unresolved: layer measurement laws, canonical layer equivalence, complete UCNS object
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: retained_layers_append_without_overwrite
#   given: repeated or differently named structural layers are added
#   then: every occurrence remains ordered and addressable and no earlier evidence is overwritten
#   class: doctrine
#   since: 2026-07-21
#
# id: retained_layer_presence_is_explicit
#   given: retained evidence may be falsey or equal to None
#   then: presence is determined only by the retained flag rather than truthiness
#   class: safety
#   since: 2026-07-21
#
# id: retained_envelope_has_unique_complete_null
#   given: a cell carrier and optional retained layers are assembled
#   then: Structural Null is returned exactly when no cell carrier and no retained layer occurrence remains
#   class: doctrine
#   since: 2026-07-21
#
# id: retained_layers_do_not_silently_enter_cell_support
#   given: receipts, metadata, relations, recursion, provenance, or state are retained
#   then: cell_support_weight reports only the current cell carrier W and every other layer keeps explicit contribution status
#   class: safety
#   since: 2026-07-21
#
# id: retained_layer_projection_is_non_destructive
#   given: a selected retained layer is viewed through a structural policy
#   then: the policy projection retains the untouched layer evidence and does not mutate the envelope
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

"""Evidence-preserving retained structural layers above the cell-only floor."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum
from typing import Any, TypeAlias, Union

from .carrier import STRUCTURAL_NULL, _StructuralNull
from .policy import PolicyRegistry, Projection, StructurePolicy, apply_policy
from .structure import Carrier, Structure, support_weight


class ContributionStatus(str, Enum):
    """Whether a retained layer currently contributes to a named measurement."""

    MEASURED = "measured"
    UNMEASURED = "unmeasured"
    EXCLUDED = "excluded"


@dataclass(frozen=True, slots=True)
class RetainedLayer:
    """One occurrence of named evidence with explicit policy and measurement status."""

    name: str
    evidence: Any = None
    retained: bool = True
    policy_name: str | None = None
    contribution_status: ContributionStatus = ContributionStatus.UNMEASURED
    contribution_note: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("retained layer name must be nonempty")
        try:
            status = ContributionStatus(self.contribution_status)
        except ValueError as exc:
            raise ValueError("unknown retained-layer contribution status") from exc
        object.__setattr__(self, "contribution_status", status)

        if self.policy_name is not None and not self.policy_name.strip():
            raise ValueError("policy name must be nonempty when supplied")

        if not self.retained:
            if self.evidence is not None:
                raise ValueError("an absent layer placeholder cannot carry evidence")
            if self.policy_name is not None:
                raise ValueError("an absent layer placeholder cannot bind a policy")
            if status is not ContributionStatus.UNMEASURED or self.contribution_note:
                raise ValueError("an absent layer placeholder cannot claim contribution status")
        elif status in (ContributionStatus.MEASURED, ContributionStatus.EXCLUDED):
            if not self.contribution_note.strip():
                raise ValueError("measured or excluded layers require a scoped contribution note")


@dataclass(frozen=True, slots=True)
class RetainedStructure:
    """A non-null envelope retaining a cell carrier, optional layers, or both."""

    carrier: Structure = STRUCTURAL_NULL
    layers: tuple[RetainedLayer, ...] = ()

    def __post_init__(self) -> None:
        if self.carrier is not STRUCTURAL_NULL and not isinstance(self.carrier, Carrier):
            raise TypeError("carrier must be STRUCTURAL_NULL or Carrier")
        layers = tuple(self.layers)
        if any(not isinstance(layer, RetainedLayer) for layer in layers):
            raise TypeError("layers must contain RetainedLayer values")
        if self.carrier is STRUCTURAL_NULL and not any(layer.retained for layer in layers):
            raise ValueError("complete absence is STRUCTURAL_NULL, not RetainedStructure")
        object.__setattr__(self, "layers", layers)

    @property
    def cells(self) -> tuple[Any, ...]:
        return () if self.carrier is STRUCTURAL_NULL else self.carrier.cells

    @property
    def retained_layers(self) -> tuple[RetainedLayer, ...]:
        return tuple(layer for layer in self.layers if layer.retained)

    def layers_named(self, name: str) -> tuple[RetainedLayer, ...]:
        return tuple(layer for layer in self.layers if layer.name == name)

    def layer(self, name: str, *, occurrence: int = 0) -> RetainedLayer:
        matches = self.layers_named(name)
        try:
            return matches[occurrence]
        except IndexError as exc:
            raise IndexError(f"no retained layer occurrence {occurrence} for {name!r}") from exc

    def with_layer(self, layer: RetainedLayer) -> "RetainedStructure":
        if not isinstance(layer, RetainedLayer):
            raise TypeError("layer must be RetainedLayer")
        return RetainedStructure(self.carrier, self.layers + (layer,))


RetainedEnvelope: TypeAlias = Union[_StructuralNull, RetainedStructure]


def make_retained_structure(
    carrier: Structure = STRUCTURAL_NULL,
    layers: Iterable[RetainedLayer] = (),
) -> RetainedEnvelope:
    """Return Structural Null only when no carrier and no retained layer remains."""

    if carrier is not STRUCTURAL_NULL and not isinstance(carrier, Carrier):
        raise TypeError("carrier must be STRUCTURAL_NULL or Carrier")
    retained_layers = tuple(layers)
    if any(not isinstance(layer, RetainedLayer) for layer in retained_layers):
        raise TypeError("layers must contain RetainedLayer values")
    if carrier is STRUCTURAL_NULL and not any(layer.retained for layer in retained_layers):
        return STRUCTURAL_NULL
    return RetainedStructure(carrier, retained_layers)


def cell_support_weight(envelope: RetainedEnvelope) -> float:
    """Return only the cell carrier's established aggregate support W."""

    if envelope is STRUCTURAL_NULL:
        return 0.0
    if not isinstance(envelope, RetainedStructure):
        raise TypeError("envelope must be STRUCTURAL_NULL or RetainedStructure")
    return support_weight(envelope.carrier)


def project_layer(
    envelope: RetainedStructure,
    layer: str | int,
    policy: StructurePolicy | str | None = None,
    *,
    occurrence: int = 0,
    registry: PolicyRegistry | None = None,
) -> Projection:
    """Project one retained layer without altering its raw evidence."""

    if not isinstance(envelope, RetainedStructure):
        raise TypeError("envelope must be RetainedStructure")
    if isinstance(layer, int):
        try:
            selected = envelope.layers[layer]
        except IndexError as exc:
            raise IndexError(f"no retained layer at index {layer}") from exc
    elif isinstance(layer, str):
        selected = envelope.layer(layer, occurrence=occurrence)
    else:
        raise TypeError("layer selector must be a name or integer index")
    if not selected.retained:
        raise ValueError("cannot project an absent layer placeholder")

    chosen: StructurePolicy | str
    if policy is None:
        if selected.policy_name is None:
            raise ValueError("no policy supplied or bound to the selected layer")
        chosen = selected.policy_name
    else:
        chosen = policy
    return apply_policy(selected.evidence, chosen, registry=registry)
