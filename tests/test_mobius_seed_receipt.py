# === CHECKS ===
# id: check_mobius_seed_receipt_counts
#   proves: mobius_seed_receipt_validates_complete_invariant_counts
#   call: self::test_receipt_counts_and_digest
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_mobius_seed_receipt_authority
#   proves: mobius_seed_receipt_separates_source_assumptions_and_zeta_authority
#   call: self::test_receipt_preserves_source_and_authority_boundaries
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from ucns.mobius_seed_build import build_mobius_seed_of_life_candidate


def test_receipt_counts_and_digest() -> None:
    seed = build_mobius_seed_of_life_candidate()
    assert seed.center_bundle.multiplicity == 15
    assert len(seed.construction_digest) == 64
    assert seed.construction_digest in seed.manifest_json()


def test_receipt_preserves_source_and_authority_boundaries() -> None:
    manifest = build_mobius_seed_of_life_candidate().manifest()
    assert manifest["source_basis"]["title"] == "Intersecting Möbius Strips and Quantum Geometry"
    assert "the exact one-sixth-turn outer phase increment" in manifest["source_basis"]["not_fixed_by_source"]
    assert manifest["center_interpretation_boundary"]["resolution"] == "hmmm-unresolved-without-authority-transfer"
    assert manifest["authority_boundary"]["authority_transfer"] == "none"
    assert "separately defined spectral operator" in manifest["authority_boundary"]["metapat_may_consume_later"]
    assert "no-spectral-operator" in manifest["zeta_bridge_status"]
