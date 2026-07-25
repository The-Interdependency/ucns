# === MODULE_BUILD ===
# id: ucns_option_decision_registry
#   module_name: options
#   module_kind: schema
#   summary: loads and validates the authoritative UCNS decision and unresolved-option registry
#   owner: Erin Spencer
#   public_surface: OPTION_REGISTRY_SCHEMA_ID, OPTION_REGISTRY_SCHEMA_VERSION, UCNS_IDENTIFIER, OptionRegistryError, load_option_registry, option_dimension
#   internal_surface: _validate_registry
#   auth_boundary: none
#   storage_boundary: packaged option_registry.json
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_option_decisions.py
#   rollout: authoritative decisions and explicit unresolved choices; no mathematical option selection
#   rollback: remove the registry surface without changing existing carrier or profile behavior
#   since: 2026-07-25
#   unresolved: ideal EDCM-scoped configuration and the option dimensions marked required-evaluation or unresolved
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: ucns_identifier_is_stable_without_canonical_expansion
#   given: the UCNS decision registry is loaded
#   then: the identifier is exactly UCNS and canonical expansion is absent
#   class: doctrine
#   since: 2026-07-25
#
# id: ucns_options_have_explicit_non_default_standing
#   given: an option dimension is declared
#   then: every choice has a recognized standing and no dimension appoints a hidden default or selected winner
#   class: safety
#   since: 2026-07-25
#
# id: edcm_configuration_selection_is_empirical_and_scoped
#   given: the current option-configuration project is inspected
#   then: EDCM tests real systems for an EDCM-only selection with every authority-transfer field false
#   class: doctrine
#   since: 2026-07-25
#
# id: current_downstream_profile_is_one_configuration
#   given: the current post-reset profile is inspected
#   then: its exact option values are registered as an implemented candidate with no selection effect
#   class: correctness
#   since: 2026-07-25
# === END CONTRACTS ===

"""UCNS decision and unresolved-option registry.

The registry records authority boundaries and candidate standing. It does not
select mathematics merely by loading data.
"""

from __future__ import annotations

from importlib.resources import files
import json
from typing import Any

OPTION_REGISTRY_SCHEMA_ID = "ucns.option-registry"
OPTION_REGISTRY_SCHEMA_VERSION = "1.0.0"
UCNS_IDENTIFIER = "UCNS"

STANDING_VALUES = frozenset(
    {
        "decided-constraint",
        "implemented-candidate",
        "experiment-candidate",
        "required-evaluation",
        "rejected-pre-reset",
        "unresolved",
    }
)

REQUIRED_DECISION_IDS = frozenset(
    {
        "stable-identifier",
        "optionalized-construction",
        "old-new-decomposition",
        "edcm-empirical-selection",
        "selection-non-transfer",
        "exact-configuration-identity",
        "initial-occurrence-boundary",
        "negative-results-are-evidence",
        "typed-absence",
    }
)


class OptionRegistryError(ValueError):
    """Raised when the packaged option registry violates its authority contract."""


def _validate_registry(data: dict[str, Any]) -> None:
    if data.get("schema_id") != OPTION_REGISTRY_SCHEMA_ID:
        raise OptionRegistryError("option registry schema identity mismatch")
    if data.get("schema_version") != OPTION_REGISTRY_SCHEMA_VERSION:
        raise OptionRegistryError("option registry schema version mismatch")

    identifier = data.get("identifier")
    if not isinstance(identifier, dict):
        raise OptionRegistryError("identifier record is required")
    if identifier.get("value") != UCNS_IDENTIFIER:
        raise OptionRegistryError("UCNS identifier mismatch")
    if identifier.get("canonical_expansion") is not None:
        raise OptionRegistryError("UCNS cannot acquire a canonical expansion")

    project = data.get("project")
    if not isinstance(project, dict):
        raise OptionRegistryError("project record is required")
    if project.get("selection_scope") != "edcm-only":
        raise OptionRegistryError("selection scope must remain EDCM-only")
    for field in (
        "universal_ucns_canon_transfer",
        "theorem_status_transfer",
        "measurement_validity_transfer",
        "metapat_validity_transfer",
    ):
        if project.get(field) is not False:
            raise OptionRegistryError(f"{field} must remain false")

    decisions = data.get("decisions")
    if not isinstance(decisions, list):
        raise OptionRegistryError("decision list is required")
    decision_ids = [item.get("id") for item in decisions if isinstance(item, dict)]
    if len(decision_ids) != len(set(decision_ids)):
        raise OptionRegistryError("decision ids must be unique")
    if not REQUIRED_DECISION_IDS.issubset(decision_ids):
        raise OptionRegistryError("required decisions are missing")

    dimensions = data.get("dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        raise OptionRegistryError("at least one option dimension is required")
    dimension_ids = [item.get("id") for item in dimensions if isinstance(item, dict)]
    if len(dimension_ids) != len(set(dimension_ids)):
        raise OptionRegistryError("option dimension ids must be unique")
    for dimension in dimensions:
        if not isinstance(dimension, dict):
            raise OptionRegistryError("option dimensions must be mappings")
        if "default" in dimension or "default_choice" in dimension or "selected_choice" in dimension:
            raise OptionRegistryError("option dimensions cannot appoint hidden defaults")
        choices = dimension.get("choices")
        if not isinstance(choices, list) or not choices:
            raise OptionRegistryError("every option dimension requires choices")
        choice_ids = [choice.get("id") for choice in choices if isinstance(choice, dict)]
        if len(choice_ids) != len(set(choice_ids)):
            raise OptionRegistryError("choice ids must be unique within a dimension")
        for choice in choices:
            if not isinstance(choice, dict) or choice.get("standing") not in STANDING_VALUES:
                raise OptionRegistryError("every choice requires recognized standing")

    current_profile = data.get("current_profile")
    if not isinstance(current_profile, dict):
        raise OptionRegistryError("current profile record is required")
    if current_profile.get("standing") != "implemented-candidate":
        raise OptionRegistryError("current profile must remain an implemented candidate")
    if current_profile.get("selection_effect") != "none":
        raise OptionRegistryError("current profile cannot select global or EDCM canon")

    hmmm = data.get("hmmm")
    if not isinstance(hmmm, list) or not hmmm:
        raise OptionRegistryError("unresolved hmmm choices must remain visible")


def load_option_registry() -> dict[str, Any]:
    """Load a fresh validated copy of the packaged decision registry."""

    resource = files(__package__).joinpath("option_registry.json")
    data = json.loads(resource.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise OptionRegistryError("option registry root must be a mapping")
    _validate_registry(data)
    return data


def option_dimension(dimension_id: str) -> dict[str, Any]:
    """Return one named option dimension or fail closed."""

    if not dimension_id:
        raise OptionRegistryError("dimension_id must be nonempty")
    for dimension in load_option_registry()["dimensions"]:
        if dimension["id"] == dimension_id:
            return dimension
    raise OptionRegistryError(f"unknown UCNS option dimension: {dimension_id}")


__all__ = [
    "OPTION_REGISTRY_SCHEMA_ID",
    "OPTION_REGISTRY_SCHEMA_VERSION",
    "UCNS_IDENTIFIER",
    "OptionRegistryError",
    "load_option_registry",
    "option_dimension",
]
