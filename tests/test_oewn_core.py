# === CHECKS ===
# id: oewn_core_complete_ingestion_check
#   proves: oewn_core_ingestion_is_complete_and_deterministic
#   call: self::test_exact_oewn_core_complete_counts_and_replay
#   timeout: 180
#   mutates: none
#   cleanup: none
#
# id: oewn_morphology_inventory_check
#   proves: oewn_morphology_inventory_precedes_law
#   call: self::test_morphology_inventory_preserves_evidence_without_selecting_law
#   timeout: 180
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import os

import pytest

from ucns.lexical_sources import verify_oewn_2025_core
from ucns.oewn_core import inventory_oewn_morphology, load_oewn_core


@pytest.fixture(scope="module")
def exact_snapshot():
    root = os.environ.get("UCNS_OEWN_2025_CORE_ROOT")
    if not root:
        pytest.skip("UCNS_OEWN_2025_CORE_ROOT is not configured")
    receipt = verify_oewn_2025_core(root)
    return load_oewn_core(root, receipt)


def test_exact_oewn_core_complete_counts_and_replay(exact_snapshot) -> None:
    snapshot = exact_snapshot
    assert len(snapshot.lexical_entries) == 135_969
    assert len(snapshot.synsets) == 107_519
    assert snapshot.sense_count == 185_129
    assert snapshot.definition_count == 107_524
    assert snapshot.relation_occurrence_count == 244_727
    assert snapshot.source_receipt_id == "ucns.oewn-core-receipt:sha256:3ea1f9f0d60bb0c440d7bcb6375050673c0cd03b774f87fed9e4be223bc3c973"


def test_morphology_inventory_preserves_evidence_without_selecting_law(exact_snapshot) -> None:
    inventory = inventory_oewn_morphology(exact_snapshot)
    assert inventory.lexical_entry_count == 135_969
    assert inventory.explicit_form_count == 4_473
    assert inventory.entries_with_forms == 3_084
    assert inventory.unique_lemma_count == 128_009
    assert inventory.single_inscription_entry_count == 82_909
    assert inventory.multi_inscription_entry_count == 53_060
    assert inventory.public_carrier_unassigned_characters == ("ç", "ê", "ñ", "ò")
    assert inventory.explicit_decomposition_records == 0
    assert inventory.final_morphology_law_selected is False
    assert inventory.inventory_id.startswith("ucns.oewn-morphology-inventory:sha256:")
