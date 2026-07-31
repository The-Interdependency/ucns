# === MODULE_BUILD ===
# id: ucns_option_decision_registry
#   module_name: options
#   module_kind: schema
#   summary: loads and validates the authoritative UCNS completion-motion root, EDCM decisions, external receipt standing, analytic carrier evidence, assignment-admission boundary, gonol-initiation and Structural Null boundary, and unresolved-option registry
#   owner: Erin Spencer
#   public_surface: OPTION_REGISTRY_SCHEMA_ID, OPTION_REGISTRY_SCHEMA_VERSION, UCNS_IDENTIFIER, OptionRegistryError, load_option_registry, option_dimension
#   internal_surface: _validate_registry
#   auth_boundary: none
#   storage_boundary: packaged option_registry.json
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_option_decisions.py
#   rollout: authoritative completion-motion root, scoped completion, trajectory identity, exact MultiWOZ receipt standing, v0.15 mixed carrier-evidence scopes, v0.16 assignment admission, v0.17 gonol-initiation and Structural Null standing, decisions, and explicit unresolved choices; no mathematical option selection
#   rollback: remove the registry surface without changing existing carrier or profile behavior
#   since: 2026-07-25
#   unresolved: arbitrary-element geometric assignment beyond admitted and initiated evidence outcomes, total Structural Null topology, later corpus runs, ideal EDCM-scoped configuration, non-SPACE alphabet expansion or escape, and the option dimensions marked required-evaluation or unresolved
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
#
# id: edcm_constraints_are_explicit_without_early_collapse
#   given: Erin's EDCM configuration directions and the real-system research boundary are inspected
#   then: every decided constraint, plural M and B display, failure-seeking principle, and corpus candidate is explicit while unresolved dimensions remain open
#   class: doctrine
#   since: 2026-07-25
#
# id: ucns_completion_motion_root_is_authoritative
#   given: the UCNS option registry is loaded
#   then: completion-motion is the system root, completion remains scoped, trajectory is the observation identity, and scalar projections remain optional declared-loss views
#   class: doctrine
#   since: 2026-07-26
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
OPTION_REGISTRY_SCHEMA_VERSION = "1.13.0"
UCNS_IDENTIFIER = "UCNS"

STANDING_VALUES = frozenset(
    {
        "decided-constraint",
        "implemented-candidate",
        "experiment-candidate",
        "required-evaluation",
        "rejected-pre-reset",
        "superseded-for-edcm",
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
        "edcm-mobius-causal-carrier",
        "structural-null-superposition",
        "edcm-ordered-concatenation",
        "edcm-unit-support",
        "exact-to-projection-evidence-scale",
        "plural-M-display",
        "plural-B-display",
        "edcm-carrier-pairing-only",
        "edcm-specific-profile",
        "real-system-corpora-required",
        "failure-seeking-research",
        "word-gonol-smallest-scale",
        "exact-public-gonol-157",
        "edcm-source-domain-scalar-values",
        "edcm-space-origin-assignment",
        "edcm-source-normalization-none",
        "full-corpus-runs",
        "full-corpus-execution-gate",
        "multiwoz-v0141-downstream-receipt",
        "ucns-completion-motion-root",
        "completion-scoped-to-declared-boundary",
        "trajectory-before-scalar",
        "bounded-root-loop-cover-chart",
        "exact-rational-transverse-envelope-correction",
        "bounded-carrier-coordinate-admissibility",
        "exact-coordinate-representation-boundary",
        "partial-initiation-boundary",
        "full-carrier-attachment-evidence",
        "assignment-admission-boundary",
        "gonol-initiation-structural-null-boundary",
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
    expected_root = {
        "system_root": (
            "UCNS assigns elements of an unknowable to completion through "
            "geometric motion."
        ),
        "completion_scope": (
            "Completion closes a declared construction relative to its declared "
            "boundary and does not exhaust the underlying unknowable."
        ),
        "motion_evidence_schema": "ucns.edcm.completion-motion-evidence/0.1.0",
        "full_corpus_execution_schema": (
            "ucns.edcm.full-corpus-execution/0.14.1"
        ),
        "full_carrier_attachment_schema": (
            "ucns.edcm.full-carrier-attachment-evidence/0.15.0"
        ),
        "assignment_admission_schema": (
            "ucns.edcm.assignment-admission-boundary/0.16.0"
        ),
        "gonol_initiation_schema": (
            "ucns.edcm.gonol-initiation-structural-null-boundary/0.17.0"
        ),
        "trajectory_identity": "complete-assignment-and-motion-trajectory",
        "scalar_projection_policy": "optional-declared-loss-with-source-link",
    }
    for field, expected in expected_root.items():
        if project.get(field) != expected:
            raise OptionRegistryError(f"UCNS completion-motion root mismatch: {field}")
    for field in (
        "universal_ucns_canon_transfer",
        "theorem_status_transfer",
        "measurement_validity_transfer",
        "metapat_validity_transfer",
    ):
        if project.get(field) is not False:
            raise OptionRegistryError(f"{field} must remain false")

    if project.get("configuration_state") != "decided-constraints-with-incomplete-evidence":
        raise OptionRegistryError("EDCM configuration state must preserve honest incompletion")
    selection_principle = project.get("selection_principle")
    if not isinstance(selection_principle, str) or "Refuse early collapse" not in selection_principle:
        raise OptionRegistryError("failure-seeking anti-collapse principle is required")

    constraints = project.get("decided_configuration_constraints")
    expected_constraints = {
        "carrier_requirement": "mobius-origin-hidden-zero",
        "structural_null_semantics": "superpositioned-space",
        "twist_event": "new-gonol-initiation",
        "occurrence_operation": "ordered-concatenation",
        "support_policy": "unit-speaker-turn",
        "smallest_gonol": "word",
        "nesting_boundary": "superpositioned-space",
        "token_alphabet": "public-gonol-157",
        "token_identity": "unicode-code-point",
        "source_domain": "unicode-scalar-values",
        "normalization_policy": "none-preserve-source",
        "space_assignment_policy": "unicode-white-space-origin-v1",
        "corpus_execution": "full-corpus",
        "out_of_alphabet_policy": "retain-and-report",
        "equivalence_baseline": "exact-evidence",
        "equivalence_progression": "evidence-scaled-projection",
        "payload_operator": "carrier-pairing-only",
        "profile_scope": "edcm-specific",
        "measurement_identity": "completion-motion-trajectory",
        "scalar_projection": "optional-declared-loss",
        "completion_scope": "declared-construction-boundary",
    }
    if not isinstance(constraints, dict):
        raise OptionRegistryError("decided EDCM constraints are required")
    for key, value in expected_constraints.items():
        if constraints.get(key) != value:
            raise OptionRegistryError(f"EDCM constraint mismatch: {key}")

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

    dimension_by_id = {dimension["id"]: dimension for dimension in dimensions}
    required_dimension_ids = {
        "carrier-model",
        "carrier-coordinate-admissibility",
        "exact-coordinate-representation",
        "initiation-attachment",
        "full-carrier-continuity-evidence",
        "assignment-admission-evidence",
        "gonol-initiation-evidence",
        "origin-semantics",
        "occurrence-structure",
        "support-assignment",
        "graph-contribution",
        "structural-equivalence",
        "product-character-M",
        "faithful-breadth-B",
        "typed-payload-operators",
        "profile-scope",
        "selection-evidence",
        "gonol-scale",
        "token-alphabet",
        "unicode-normalization",
        "corpus-execution",
    }
    if not required_dimension_ids.issubset(dimension_by_id):
        raise OptionRegistryError("required EDCM option dimensions are missing")

    def choice_standing(dimension_id: str, choice_id: str) -> str | None:
        for choice in dimension_by_id[dimension_id]["choices"]:
            if choice["id"] == choice_id:
                return choice["standing"]
        return None

    decided_choices = {
        ("carrier-model", "mobius-origin-hidden-zero"),
        ("origin-semantics", "superpositioned-structural-null"),
        ("origin-semantics", "gonol-initiation-mobius-twist"),
        ("occurrence-structure", "ordered-concatenation"),
        ("support-assignment", "unit-speaker-turn"),
        ("gonol-scale", "word-gonol"),
        ("token-alphabet", "exact-public-gonol-157"),
        ("token-alphabet", "unicode-scalar-source-domain"),
        ("token-alphabet", "space-manifestations-map-to-origin"),
        ("token-alphabet", "retain-out-of-alphabet-evidence"),
        ("unicode-normalization", "none-preserve-source"),
        ("corpus-execution", "full-corpus"),
        ("structural-equivalence", "exact-evidence"),
        ("typed-payload-operators", "carrier-pairing-only"),
        ("profile-scope", "edcm-specific-profile"),
        ("selection-evidence", "real-system-corpora"),
        ("selection-evidence", "failure-seeking-full-corpus-analysis"),
    }
    for dimension_id, choice_id in decided_choices:
        if choice_standing(dimension_id, choice_id) != "decided-constraint":
            raise OptionRegistryError(
                f"EDCM decided constraint missing: {dimension_id}/{choice_id}"
            )

    if choice_standing(
        "profile-scope", "combined-edcm-metapat-ordered-occurrence"
    ) != "superseded-for-edcm":
        raise OptionRegistryError("combined profile must be superseded for EDCM selection")

    expected_m = [
        "geometric-mean-support",
        "maximum-support",
        "minimum-support",
    ]
    expected_b = [
        "cell-log-support",
        "cell-detail",
        "retained-presence",
    ]
    for dimension_id, expected_display in (
        ("product-character-M", expected_m),
        ("faithful-breadth-B", expected_b),
    ):
        dimension = dimension_by_id[dimension_id]
        if dimension.get("display_rule") != "display-all-three":
            raise OptionRegistryError(f"{dimension_id} must display all three candidates")
        if dimension.get("display_order") != expected_display:
            raise OptionRegistryError(f"{dimension_id} display order mismatch")
        if dimension.get("selection_effect") != "none":
            raise OptionRegistryError(f"{dimension_id} cannot select a candidate")

    representation = dimension_by_id["exact-coordinate-representation"]
    if representation.get("display_rule") != (
        "display-exact-source-and-rendering-together"
    ):
        raise OptionRegistryError(
            "exact-coordinate representation must retain source and rendering"
        )
    if representation.get("display_order") != [
        "signed-local-exact-rational-coordinate",
        "linked-binary64-carrier-rendering",
    ]:
        raise OptionRegistryError(
            "exact-coordinate representation display order mismatch"
        )
    if representation.get("selection_effect") != "none":
        raise OptionRegistryError(
            "exact-coordinate representation cannot select a candidate"
        )

    attachment = dimension_by_id["initiation-attachment"]
    if attachment.get("display_rule") != "preserve-all-seam-alternatives":
        raise OptionRegistryError(
            "initiation attachment must preserve all seam alternatives"
        )
    if attachment.get("display_order") != [
        "marked-source-bound-partial-attachment",
        "intrinsic-derived-initiation-seam",
        "invariant-initiation-equivalence-class",
    ]:
        raise OptionRegistryError(
            "initiation attachment display order mismatch"
        )
    if attachment.get("selection_effect") != "none":
        raise OptionRegistryError(
            "initiation attachment cannot select a candidate"
        )
    attachment_standings = {
        choice.get("id"): choice.get("standing")
        for choice in attachment.get("choices", ())
        if isinstance(choice, dict)
    }
    if attachment_standings != {
        "marked-source-bound-partial-attachment": "implemented-candidate",
        "intrinsic-derived-initiation-seam": "unresolved",
        "invariant-initiation-equivalence-class": "unresolved",
    }:
        raise OptionRegistryError(
            "initiation attachment choice standings are fixed"
        )

    continuity = dimension_by_id["full-carrier-continuity-evidence"]
    if continuity.get("display_rule") != (
        "display-analytic-and-unresolved-attachment-standings-together"
    ):
        raise OptionRegistryError(
            "full-carrier continuity must retain mixed standings"
        )
    if continuity.get("display_order") != [
        "analytic-affine-and-non-null-quotient-certificates",
        "runtime-arbitrary-real-representation",
        "total-structural-null-carrier-relationship",
    ]:
        raise OptionRegistryError(
            "full-carrier continuity display order mismatch"
        )
    if continuity.get("selection_effect") != "none":
        raise OptionRegistryError(
            "full-carrier continuity evidence cannot select a candidate"
        )
    continuity_standings = {
        choice.get("id"): choice.get("standing")
        for choice in continuity.get("choices", ())
        if isinstance(choice, dict)
    }
    if continuity_standings != {
        "analytic-affine-and-non-null-quotient-certificates": (
            "implemented-candidate"
        ),
        "runtime-arbitrary-real-representation": "unresolved",
        "total-structural-null-carrier-relationship": "unresolved",
    }:
        raise OptionRegistryError(
            "full-carrier continuity choice standings are fixed"
        )

    assignment = dimension_by_id["assignment-admission-evidence"]
    if assignment.get("display_rule") != (
        "separate-admission-outcomes-from-geometric-success"
    ):
        raise OptionRegistryError(
            "assignment admission must remain separate from geometric success"
        )
    if assignment.get("display_order") != [
        "explicit-adapter-admission-and-tagged-outcome",
        "identity-derived-geometric-assignment",
        "arbitrary-element-geometric-assignment-law",
    ]:
        raise OptionRegistryError(
            "assignment admission display order mismatch"
        )
    if assignment.get("selection_effect") != "none":
        raise OptionRegistryError(
            "assignment admission evidence cannot select geometry"
        )
    assignment_standings = {
        choice.get("id"): choice.get("standing")
        for choice in assignment.get("choices", ())
        if isinstance(choice, dict)
    }
    if assignment_standings != {
        "explicit-adapter-admission-and-tagged-outcome": (
            "implemented-candidate"
        ),
        "identity-derived-geometric-assignment": "rejected-pre-reset",
        "arbitrary-element-geometric-assignment-law": "unresolved",
    }:
        raise OptionRegistryError(
            "assignment admission choice standings are fixed"
        )

    initiation = dimension_by_id["gonol-initiation-evidence"]
    if initiation.get("display_rule") != (
        "separate-causal-initiation-from-geometry-and-completion"
    ):
        raise OptionRegistryError(
            "gonol initiation must remain separate from geometry and completion"
        )
    if initiation.get("display_order") != [
        "explicit-structural-null-twist-and-tagged-outcome",
        "bounded-native-root-360-change-720-return",
        "zero-or-absence-as-structural-null-prestate",
        "total-structural-null-carrier-topology",
    ]:
        raise OptionRegistryError(
            "gonol initiation display order mismatch"
        )
    if initiation.get("selection_effect") != "none":
        raise OptionRegistryError(
            "gonol initiation evidence cannot select geometry"
        )
    initiation_standings = {
        choice.get("id"): choice.get("standing")
        for choice in initiation.get("choices", ())
        if isinstance(choice, dict)
    }
    if initiation_standings != {
        "explicit-structural-null-twist-and-tagged-outcome": (
            "implemented-candidate"
        ),
        "bounded-native-root-360-change-720-return": (
            "implemented-candidate"
        ),
        "zero-or-absence-as-structural-null-prestate": (
            "rejected-pre-reset"
        ),
        "total-structural-null-carrier-topology": "unresolved",
    }:
        raise OptionRegistryError(
            "gonol initiation choice standings are fixed"
        )

    corpora = data.get("real_system_corpus_candidates")
    if not isinstance(corpora, list) or not corpora:
        raise OptionRegistryError("real-system corpus candidates are required")
    corpus_ids = [corpus.get("id") for corpus in corpora if isinstance(corpus, dict)]
    if len(corpus_ids) != len(corpora) or len(corpus_ids) != len(set(corpus_ids)):
        raise OptionRegistryError("real-system corpus candidates require unique ids")
    for corpus in corpora:
        if corpus.get("standing") not in STANDING_VALUES:
            raise OptionRegistryError("corpus candidate requires recognized standing")
        for field in ("provenance", "source", "access", "edcm_fit", "limitation"):
            if not corpus.get(field):
                raise OptionRegistryError(f"corpus candidate missing {field}")

    target_profile = data.get("target_profile")
    if not isinstance(target_profile, dict):
        raise OptionRegistryError("EDCM target profile record is required")
    if target_profile.get("profile_id") != "ucns.profile.edcm-word-gonol":
        raise OptionRegistryError("EDCM target profile identity mismatch")
    if target_profile.get("profile_version") != "0.2.0":
        raise OptionRegistryError("EDCM target profile version mismatch")
    if target_profile.get("scope") != "edcm-only":
        raise OptionRegistryError("EDCM target profile scope mismatch")
    if target_profile.get("standing") != "implemented-candidate":
        raise OptionRegistryError("EDCM target profile standing mismatch")
    if target_profile.get("selection_effect") != "none":
        raise OptionRegistryError("EDCM target profile cannot select itself")
    token_alphabet = target_profile.get("token_alphabet")
    if not isinstance(token_alphabet, dict):
        raise OptionRegistryError("EDCM target token alphabet is required")
    expected_alphabet = {
        "id": "public-gonol-157",
        "arity": 157,
        "source_repository": "The-Interdependency/a0-betatest",
        "source_commit": "7af8debf6ef3905f01baff02b43d8c3bee16ccbc",
        "source_path": "backend/interdependent_lib/gonal/gonal.py",
        "sha256": "55d10c84529a4d7bc7714786357e977b68d9df2ac3f73d20e229580b552c2ef5",
        "origin_position": 0,
        "origin_token": " ",
        "digit_zero_position": 139,
    }
    if token_alphabet != expected_alphabet:
        raise OptionRegistryError("EDCM target token alphabet mismatch")
    expected_space_assignment = {
        "policy_id": "unicode-white-space-origin-v1",
        "carrier_position": 0,
        "carrier_token": " ",
        "source_code_points": [
            "U+0009",
            "U+000A",
            "U+000B",
            "U+000C",
            "U+000D",
            "U+0020",
            "U+0085",
            "U+00A0",
            "U+1680",
            "U+2000",
            "U+2001",
            "U+2002",
            "U+2003",
            "U+2004",
            "U+2005",
            "U+2006",
            "U+2007",
            "U+2008",
            "U+2009",
            "U+200A",
            "U+2028",
            "U+2029",
            "U+202F",
            "U+205F",
            "U+3000",
        ],
    }
    if target_profile.get("space_assignment") != expected_space_assignment:
        raise OptionRegistryError("EDCM SPACE-origin assignment mismatch")
    expected_target_values = {
        "smallest_gonol": "word",
        "nesting_boundary": "superpositioned-space",
        "gonol_initiation": "mobius-twist",
        "occurrence_operation": "ordered-concatenation",
        "support_policy": "unit-speaker-turn",
        "source_domain": "unicode-scalar-values",
        "normalization_policy": "none-preserve-source",
        "out_of_alphabet_policy": "retain-and-report",
        "corpus_execution": "full-corpus",
    }
    for key, value in expected_target_values.items():
        if target_profile.get(key) != value:
            raise OptionRegistryError(f"EDCM target profile mismatch: {key}")

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
