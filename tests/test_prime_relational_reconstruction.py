# === CHECKS ===
# id: check_prime_relational_identity_nonleakage
#   proves: prime_relational_fixture_identity_excludes_values
#   call: self::test_public_identity_does_not_leak_value
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_h1_reconstruction
#   proves: prime_relational_h1_requires_complementary_unique_reconstruction
#   call: self::test_h1_all_erased_relations_reconstruct_exactly_in_both_implementations
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_h2_irreducibility
#   proves: prime_relational_h2_tests_every_whole_view
#   call: self::test_h2_every_whole_view_is_irreducible
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_h3_matched_baseline
#   proves: prime_relational_h3_fails_on_simpler_matched_equivalence
#   call: self::test_h3_simpler_matched_baseline_falsifies_prime_advantage
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_failure_propagation
#   proves: prime_relational_failure_propagates_before_repair
#   call: self::test_h3_failure_propagates_without_erasing_local_survivors
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from pathlib import Path

import pytest

from ucns.prime_relational_reconstruction import (
    PREREGISTRATION_PATH,
    public_relation_identity,
    run_architecture_gates,
)


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def report():
    return run_architecture_gates(ROOT / PREREGISTRATION_PATH)


def test_public_identity_does_not_leak_value():
    fields = dict(group="G2", ordinal=0, source="n0", target="n1")
    assert public_relation_identity(**fields, value=19) == public_relation_identity(
        **fields, value=20
    )


def test_h1_all_erased_relations_reconstruct_exactly_in_both_implementations(report):
    assert report["h1"]["status"] == "SURVIVED"
    assert report["h1"]["exact_recoveries"] == 17
    assert all(len(row["replay_candidates"]) == 1 for row in report["h1"]["erasures"])
    assert all(row["primary_recovery"] == row["replay_candidates"][0] for row in report["h1"]["erasures"])
    assert {row["checksum_view"] for row in report["h1"]["erasures"]} == {"P2", "P3", "P5", "P7"}


def test_h2_every_whole_view_is_irreducible(report):
    assert report["h2"]["status"] == "SURVIVED"
    assert report["h2"]["irreducible_leave_outs"] == 4
    assert [row["view"] for row in report["h2"]["leave_outs"]] == ["P2", "P3", "P5", "P7"]
    assert all(row["independent_replay_degrees_of_freedom"] > 0 for row in report["h2"]["leave_outs"])


def test_h3_simpler_matched_baseline_falsifies_prime_advantage(report):
    h3 = report["h3"]
    assert h3["status"] == "FALSIFIED"
    assert h3["baseline_matches_or_exceeds"] is True
    assert h3["baseline_strictly_simpler"] is True
    assert h3["baseline"]["encoded_field_cells"] == h3["prime_family"]["encoded_field_cells"] == 21
    assert h3["baseline"]["h1_exact_recoveries"] == h3["prime_family"]["h1_exact_recoveries"] == 17
    assert h3["baseline"]["h2_irreducible_leave_outs"] == h3["prime_family"]["h2_irreducible_leave_outs"] == 4


def test_h3_failure_propagates_without_erasing_local_survivors(report):
    assert report["architecture_status"] == "FALSIFIED"
    assert report["load_bearing_failure"] == "H3"
    assert set(report["dependent_escalations"].values()) == {"DEPRECATED"}
    assert report["prior_bounded_results"] == {
        "edcm_absolute_recovered_dissonance": "FALSIFIED",
        "edcm_normalized_recovered_dissonance": "SURVIVED",
        "ucns_p5_p7_exact_distinction": "SURVIVED",
    }
    assert report["external_or_sealed_labels_inspected"] is False
    assert report["canon_selection"] is None
