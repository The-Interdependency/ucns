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
# === END CHECKS ===

import pytest

from ucns import (
    OPTION_REGISTRY_SCHEMA_ID,
    PROFILE_ID,
    PROFILE_OPTIONS,
    UCNS_IDENTIFIER,
    OptionRegistryError,
    load_option_registry,
    option_dimension,
)


def test_ucns_identifier_has_no_canonical_expansion() -> None:
    registry = load_option_registry()
    assert OPTION_REGISTRY_SCHEMA_ID == "ucns.option-registry"
    assert UCNS_IDENTIFIER == registry["identifier"]["value"] == "UCNS"
    assert registry["identifier"]["canonical_expansion"] is None


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
    assert constraints["support_policy"] == "unit-turn"
    assert constraints["equivalence_baseline"] == "exact-evidence"
    assert constraints["equivalence_progression"] == "evidence-scaled-projection"
    assert constraints["payload_operator"] == "carrier-pairing-only"
    assert constraints["profile_scope"] == "edcm-specific"

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
