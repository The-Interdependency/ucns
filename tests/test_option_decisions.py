# === CHECKS ===
# id: check_stable_identifier_boundary
#   proves: ucns_identifier_is_stable_without_canonical_expansion
#   call: self::test_ucns_identifier_has_no_canonical_expansion
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_explicit_non_default_standing
#   proves: ucns_options_have_explicit_non_default_standing
#   call: self::test_option_dimensions_have_no_hidden_default
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_edcm_scoped_selection
#   proves: edcm_configuration_selection_is_empirical_and_scoped
#   call: self::test_edcm_selection_project_is_scoped_and_non_transferring
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_current_profile_registration
#   proves: current_downstream_profile_is_one_configuration
#   call: self::test_current_profile_is_one_exact_candidate_configuration
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_unknown_dimension_fails_closed
#   proves: ucns_options_have_explicit_non_default_standing
#   call: self::test_unknown_option_dimension_fails_closed
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_edcm_explicit_constraints_and_corpora
#   proves: edcm_constraints_are_explicit_without_early_collapse
#   call: self::test_edcm_constraints_plural_displays_and_corpora_remain_explicit
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_ucns_completion_motion_root
#   proves: ucns_completion_motion_root_is_authoritative
#   call: self::test_completion_motion_root_scope_and_projection_firewall
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from copy import deepcopy

import pytest

from ucns import (
    EDCM_PROFILE_ID,
    EDCM_PROFILE_VERSION,
    EDCM_SOURCE_DOMAIN,
    EDCM_SPACE_ASSIGNMENT_POLICY,
    EDCM_SPACE_CODE_POINTS,
    PUBLIC_GONOL_SHA256,
    OPTION_REGISTRY_SCHEMA_ID,
    OPTION_REGISTRY_SCHEMA_VERSION,
    PROFILE_ID,
    PROFILE_OPTIONS,
    UCNS_IDENTIFIER,
    OptionRegistryError,
    load_option_registry,
    option_dimension,
)
from ucns.options import _validate_registry


def test_ucns_identifier_has_no_canonical_expansion() -> None:
    registry = load_option_registry()
    assert OPTION_REGISTRY_SCHEMA_ID == "ucns.option-registry"
    assert UCNS_IDENTIFIER == registry["identifier"]["value"] == "UCNS"
    assert registry["identifier"]["canonical_expansion"] is None
    assert OPTION_REGISTRY_SCHEMA_VERSION == registry["schema_version"] == "1.13.0"


def test_completion_motion_root_scope_and_projection_firewall() -> None:
    project = load_option_registry()["project"]
    assert project["system_root"] == (
        "UCNS assigns elements of an unknowable to completion through "
        "geometric motion."
    )
    assert "does not exhaust" in project["completion_scope"]
    assert (
        project["motion_evidence_schema"]
        == "ucns.edcm.completion-motion-evidence/0.1.0"
    )
    assert (
        project["full_corpus_execution_schema"]
        == "ucns.edcm.full-corpus-execution/0.14.1"
    )
    assert (
        project["full_carrier_attachment_schema"]
        == "ucns.edcm.full-carrier-attachment-evidence/0.15.0"
    )
    assert (
        project["assignment_admission_schema"]
        == "ucns.edcm.assignment-admission-boundary/0.16.0"
    )
    assert (
        project["gonol_initiation_schema"]
        == "ucns.edcm.gonol-initiation-structural-null-boundary/0.17.0"
    )
    assert project["trajectory_identity"] == "complete-assignment-and-motion-trajectory"
    assert (
        project["scalar_projection_policy"]
        == "optional-declared-loss-with-source-link"
    )


def test_option_dimensions_have_no_hidden_default() -> None:
    registry = load_option_registry()
    standings = set(registry["standing_vocabulary"])
    for dimension in registry["dimensions"]:
        assert "default" not in dimension
        assert "default_choice" not in dimension
        assert "selected_choice" not in dimension
        assert dimension["choices"]
        assert all(choice["standing"] in standings for choice in dimension["choices"])

    carrier = option_dimension("carrier-model")
    standing_by_choice = {choice["id"]: choice["standing"] for choice in carrier["choices"]}
    assert standing_by_choice["directed-twofold-branched-angular-cover"] == "implemented-candidate"
    assert standing_by_choice["mobius-origin-hidden-zero"] == "decided-constraint"
    cover_evidence = {
        choice["id"]: choice["evidence"] for choice in carrier["choices"]
    }["directed-twofold-branched-angular-cover"]
    assert "v0.9 corrects the attempted v0.8 transverse extension" in cover_evidence
    assert "collide at the same actual directed-cover coordinate" in cover_evidence
    decisions = {
        item["id"]: item["statement"] for item in registry["decisions"]
    }
    assert "bounded-root-loop-cover-chart" in decisions
    assert "bounded, nonselecting" in decisions["bounded-root-loop-cover-chart"]
    assert "exact-rational-transverse-envelope-correction" in decisions
    assert "not a transverse directed-cover embedding" in decisions[
        "exact-rational-transverse-envelope-correction"
    ]
    assert "bounded-carrier-coordinate-admissibility" in decisions
    assert "signed local affine radial" in decisions[
        "bounded-carrier-coordinate-admissibility"
    ]
    assert "selection effect" in decisions[
        "bounded-carrier-coordinate-admissibility"
    ]
    assert "exact-coordinate-representation-boundary" in decisions
    assert "lossy binary64 renderings" in decisions[
        "exact-coordinate-representation-boundary"
    ]
    assert "partial-initiation-boundary" in decisions
    assert "fourteen minimum-packet word initiations" in decisions[
        "partial-initiation-boundary"
    ]
    assert "full-corpus-execution-gate" in decisions
    assert "iterator is exhausted" in decisions["full-corpus-execution-gate"]
    assert "cannot select a carrier" in decisions["full-corpus-execution-gate"]
    assert "multiwoz-v0141-downstream-receipt" in decisions
    assert "143,048 turns reconcile" in decisions[
        "multiwoz-v0141-downstream-receipt"
    ]
    assert "full-carrier-attachment-evidence" in decisions
    assert "epsilon-delta" in decisions["full-carrier-attachment-evidence"]
    assert "assignment-admission-boundary" in decisions
    assert "exactly one ordered outcome" in decisions[
        "assignment-admission-boundary"
    ]
    assert "gonol-initiation-structural-null-boundary" in decisions
    assert "only the singular superpositioned Structural Null" in decisions[
        "gonol-initiation-structural-null-boundary"
    ]
    coordinate_dimension = option_dimension("carrier-coordinate-admissibility")
    assert coordinate_dimension["display_rule"] == "display-all-four"
    assert coordinate_dimension["selection_effect"] == "none"
    assert coordinate_dimension["display_order"] == [
        "constant-root-breadth",
        "unsigned-local-radial",
        "signed-local-affine-radial",
        "signed-global-affine-radial",
    ]
    assert {
        choice["standing"] for choice in coordinate_dimension["choices"]
    } == {"experiment-candidate"}
    representation_dimension = option_dimension(
        "exact-coordinate-representation"
    )
    assert representation_dimension["display_rule"] == (
        "display-exact-source-and-rendering-together"
    )
    assert representation_dimension["display_order"] == [
        "signed-local-exact-rational-coordinate",
        "linked-binary64-carrier-rendering",
    ]
    assert representation_dimension["selection_effect"] == "none"
    assert {
        choice["standing"] for choice in representation_dimension["choices"]
    } == {"experiment-candidate"}
    attachment_dimension = option_dimension("initiation-attachment")
    assert attachment_dimension["display_rule"] == (
        "preserve-all-seam-alternatives"
    )
    assert attachment_dimension["display_order"] == [
        "marked-source-bound-partial-attachment",
        "intrinsic-derived-initiation-seam",
        "invariant-initiation-equivalence-class",
    ]
    assert attachment_dimension["selection_effect"] == "none"
    assert {
        choice["id"]: choice["standing"]
        for choice in attachment_dimension["choices"]
    } == {
        "marked-source-bound-partial-attachment": "implemented-candidate",
        "intrinsic-derived-initiation-seam": "unresolved",
        "invariant-initiation-equivalence-class": "unresolved",
    }
    continuity_dimension = option_dimension(
        "full-carrier-continuity-evidence"
    )
    assert continuity_dimension["display_order"] == [
        "analytic-affine-and-non-null-quotient-certificates",
        "runtime-arbitrary-real-representation",
        "total-structural-null-carrier-relationship",
    ]
    assert continuity_dimension["selection_effect"] == "none"
    assert {
        choice["id"]: choice["standing"]
        for choice in continuity_dimension["choices"]
    } == {
        "analytic-affine-and-non-null-quotient-certificates": (
            "implemented-candidate"
        ),
        "runtime-arbitrary-real-representation": "unresolved",
        "total-structural-null-carrier-relationship": "unresolved",
    }
    assignment_dimension = option_dimension("assignment-admission-evidence")
    assert assignment_dimension["display_rule"] == (
        "separate-admission-outcomes-from-geometric-success"
    )
    assert assignment_dimension["display_order"] == [
        "explicit-adapter-admission-and-tagged-outcome",
        "identity-derived-geometric-assignment",
        "arbitrary-element-geometric-assignment-law",
    ]
    assert assignment_dimension["selection_effect"] == "none"
    assert {
        choice["id"]: choice["standing"]
        for choice in assignment_dimension["choices"]
    } == {
        "explicit-adapter-admission-and-tagged-outcome": (
            "implemented-candidate"
        ),
        "identity-derived-geometric-assignment": "rejected-pre-reset",
        "arbitrary-element-geometric-assignment-law": "unresolved",
    }
    initiation_dimension = option_dimension("gonol-initiation-evidence")
    assert initiation_dimension["display_rule"] == (
        "separate-causal-initiation-from-geometry-and-completion"
    )
    assert initiation_dimension["display_order"] == [
        "explicit-structural-null-twist-and-tagged-outcome",
        "bounded-native-root-360-change-720-return",
        "zero-or-absence-as-structural-null-prestate",
        "total-structural-null-carrier-topology",
    ]
    assert initiation_dimension["selection_effect"] == "none"
    assert {
        choice["id"]: choice["standing"]
        for choice in initiation_dimension["choices"]
    } == {
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
    }

    promoted_registry = deepcopy(registry)
    promoted_attachment = next(
        dimension
        for dimension in promoted_registry["dimensions"]
        if dimension["id"] == "initiation-attachment"
    )
    promoted_attachment["choices"][0]["standing"] = "decided-constraint"
    with pytest.raises(
        OptionRegistryError,
        match="choice standings are fixed",
    ):
        _validate_registry(promoted_registry)

    promoted_assignment_registry = deepcopy(registry)
    promoted_assignment = next(
        dimension
        for dimension in promoted_assignment_registry["dimensions"]
        if dimension["id"] == "assignment-admission-evidence"
    )
    promoted_assignment["choices"][2]["standing"] = "implemented-candidate"
    with pytest.raises(
        OptionRegistryError,
        match="assignment admission choice standings are fixed",
    ):
        _validate_registry(promoted_assignment_registry)

    promoted_initiation_registry = deepcopy(registry)
    promoted_initiation = next(
        dimension
        for dimension in promoted_initiation_registry["dimensions"]
        if dimension["id"] == "gonol-initiation-evidence"
    )
    promoted_initiation["choices"][3]["standing"] = "implemented-candidate"
    with pytest.raises(
        OptionRegistryError,
        match="gonol initiation choice standings are fixed",
    ):
        _validate_registry(promoted_initiation_registry)


def test_edcm_selection_project_is_scoped_and_non_transferring() -> None:
    project = load_option_registry()["project"]
    assert project["selection_scope"] == "edcm-only"
    assert "real systems" in project["objective"]
    assert project["universal_ucns_canon_transfer"] is False
    assert project["theorem_status_transfer"] is False
    assert project["measurement_validity_transfer"] is False
    assert project["metapat_validity_transfer"] is False


def test_current_profile_is_one_exact_candidate_configuration() -> None:
    profile = load_option_registry()["current_profile"]
    assert profile["profile_id"] == PROFILE_ID
    assert profile["standing"] == "implemented-candidate"
    assert profile["selection_effect"] == "none"
    assert profile["option_values"] == dict(PROFILE_OPTIONS)


def test_edcm_constraints_plural_displays_and_corpora_remain_explicit() -> None:
    registry = load_option_registry()
    project = registry["project"]
    constraints = project["decided_configuration_constraints"]

    assert project["configuration_state"] == "decided-constraints-with-incomplete-evidence"
    assert "Refuse early collapse" in project["selection_principle"]
    assert constraints["carrier_requirement"] == "mobius-origin-hidden-zero"
    assert constraints["structural_null_semantics"] == "superpositioned-space"
    assert constraints["twist_event"] == "new-gonol-initiation"
    assert constraints["occurrence_operation"] == "ordered-concatenation"
    assert constraints["support_policy"] == "unit-speaker-turn"
    assert constraints["smallest_gonol"] == "word"
    assert constraints["nesting_boundary"] == "superpositioned-space"
    assert constraints["token_alphabet"] == "public-gonol-157"
    assert constraints["token_identity"] == "unicode-code-point"
    assert constraints["normalization_policy"] == "none-preserve-source"
    assert constraints["source_domain"] == EDCM_SOURCE_DOMAIN
    assert constraints["space_assignment_policy"] == EDCM_SPACE_ASSIGNMENT_POLICY
    assert constraints["corpus_execution"] == "full-corpus"
    assert constraints["out_of_alphabet_policy"] == "retain-and-report"
    assert constraints["equivalence_baseline"] == "exact-evidence"
    assert constraints["equivalence_progression"] == "evidence-scaled-projection"
    assert constraints["payload_operator"] == "carrier-pairing-only"
    assert constraints["profile_scope"] == "edcm-specific"
    assert constraints["measurement_identity"] == "completion-motion-trajectory"
    assert constraints["scalar_projection"] == "optional-declared-loss"
    assert constraints["completion_scope"] == "declared-construction-boundary"

    assert option_dimension("product-character-M")["display_order"] == [
        "geometric-mean-support",
        "maximum-support",
        "minimum-support",
    ]
    assert option_dimension("product-character-M")["selection_effect"] == "none"
    assert option_dimension("faithful-breadth-B")["display_order"] == [
        "cell-log-support",
        "cell-detail",
        "retained-presence",
    ]
    assert option_dimension("faithful-breadth-B")["selection_effect"] == "none"

    target = registry["target_profile"]
    assert target["profile_id"] == EDCM_PROFILE_ID
    assert target["profile_version"] == EDCM_PROFILE_VERSION
    assert target["selection_effect"] == "none"
    assert target["source_domain"] == EDCM_SOURCE_DOMAIN
    assert target["smallest_gonol"] == "word"
    assert target["support_policy"] == "unit-speaker-turn"
    assert target["corpus_execution"] == "full-corpus"
    assert target["token_alphabet"]["arity"] == 157
    assert target["token_alphabet"]["origin_token"] == " "
    assert target["token_alphabet"]["digit_zero_position"] == 139
    assert target["token_alphabet"]["sha256"] == PUBLIC_GONOL_SHA256
    assert target["space_assignment"] == {
        "policy_id": EDCM_SPACE_ASSIGNMENT_POLICY,
        "carrier_position": 0,
        "carrier_token": " ",
        "source_code_points": [
            f"U+{ord(value):04X}" for value in EDCM_SPACE_CODE_POINTS
        ],
    }

    assert option_dimension("gonol-scale")["choices"][0]["id"] == "word-gonol"
    token_alphabet_choices = {
        choice["id"]: choice["standing"]
        for choice in option_dimension("token-alphabet")["choices"]
    }
    assert (
        token_alphabet_choices["space-manifestations-map-to-origin"]
        == "decided-constraint"
    )
    assert (
        token_alphabet_choices["unicode-scalar-source-domain"]
        == "decided-constraint"
    )
    assert option_dimension("unicode-normalization")["choices"][0]["id"] == "none-preserve-source"
    assert option_dimension("corpus-execution")["choices"][0]["id"] == "full-corpus"

    corpus_ids = {corpus["id"] for corpus in registry["real_system_corpus_candidates"]}
    assert {
        "wildchat-1m",
        "prism-alignment",
        "lmsys-chat-1m",
        "icsi-meeting-corpus",
        "ami-meeting-corpus",
        "multiwoz-2.1",
        "molweni",
    } <= corpus_ids


def test_unknown_option_dimension_fails_closed() -> None:
    with pytest.raises(OptionRegistryError, match="unknown UCNS option dimension"):
        option_dimension("not-registered")
