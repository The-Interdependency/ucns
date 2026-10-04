# === CHECKS ===
# id: check_convergence_path_distinction
#   proves: convergence_preserves_path_distinction
#   call: self::test_witness_preserves_distinct_paths_and_independence
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_convergence_shared_ancestry
#   proves: convergence_preserves_path_distinction
#   call: self::test_shared_ancestry_is_recorded_without_destroying_witness
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_convergence_typed_replay
#   proves: convergence_replay_is_typed
#   call: self::test_unknown_replay_remains_typed_unknown
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_convergence_digest_tamper
#   proves: convergence_digest_tamper_rejected
#   call: self::test_receipt_is_deterministic_and_tamper_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_convergence_no_semantic_judgment
#   proves: convergence_records_not_judges
#   call: self::test_no_semantic_outcome_is_encoded
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
import pytest

from ucns.structural_convergence import (
    InvariantObservation,
    OriginPath,
    StructuralConvergenceWitness,
    StructuralMapping,
)


def witness(**overrides):
    data = dict(
        source=OriginPath("asimov", "population-statistics", "system-set:a", ("book:foundation",)),
        target=OriginPath("erin", "distributed-attractor", "system-set:b", ("note:ps-fauna",)),
        mappings=(
            StructuralMapping("many-agents", "many-hosts"),
            StructuralMapping("system-regularity", "distributed-regularity"),
        ),
        invariants=(
            InvariantObservation("many-to-system", "many->system", "many->system", True),
            InvariantObservation("higher-order-regularity", "present", "present", True),
        ),
        mapping_complete=True,
        replay_passed=True,
    )
    data.update(overrides)
    return StructuralConvergenceWitness(**data)


def test_witness_preserves_distinct_paths_and_independence():
    record = witness()
    assert record.paths_distinct
    assert record.independent
    assert record.preserved_invariant_ids == ("many-to-system", "higher-order-regularity")


def test_shared_ancestry_is_recorded_without_destroying_witness():
    record = witness(shared_ancestry=("source:shared-corpus",))
    assert not record.independent
    assert record.shared_ancestry == ("source:shared-corpus",)


def test_unknown_replay_remains_typed_unknown():
    record = witness(replay_passed=None, unresolved=("replay unavailable",))
    assert record.replay_passed is None
    assert record.unresolved


def test_receipt_is_deterministic_and_tamper_fails_closed():
    record = witness()
    clone = StructuralConvergenceWitness.from_dict(record.to_dict())
    assert clone.receipt_sha256 == record.receipt_sha256
    payload = record.to_dict()
    payload["mapping_complete"] = False
    with pytest.raises(ValueError, match="receipt_sha256 mismatch"):
        StructuralConvergenceWitness.from_dict(payload)


def test_no_semantic_outcome_is_encoded():
    keys = witness().to_dict()
    assert "outcome" not in keys
    assert "analogy" not in keys
    assert "semantic_equivalence" not in keys
