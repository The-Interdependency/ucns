# === CHECKS ===
# id: lexical_floor_snapshot_check
#   proves: every_added_layer_has_a_source_bound_snapshot
#   call: self::test_snapshot_chain_is_source_bound_and_fail_closed
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.lexical_floor import (
    LexicalFloorError,
    load_ngsl_source_receipt,
    load_ngsl_words,
    snapshot_layers,
    validate_snapshot_chain,
)


def test_snapshot_chain_is_source_bound_and_fail_closed():
    words = load_ngsl_words()
    receipt = load_ngsl_source_receipt()
    snapshots = snapshot_layers(words)
    assert tuple(snapshot.layer_id for snapshot in snapshots) == (
        "00-words", "01-glyphs", "02-word-gonols",
        "03-character-hyperspace-potential", "04-affixiation",
        "05-compounding", "06-definitions",
    )
    assert snapshots[0].parent_snapshot_id is None
    assert all(current.parent_snapshot_id == previous.snapshot_id
               for previous, current in zip(snapshots, snapshots[1:]))
    assert all(snapshot.source_receipt_id == receipt.receipt_id for snapshot in snapshots)
    assert (snapshots[0].item_count, snapshots[1].item_count,
            snapshots[2].item_count, snapshots[3].item_count,
            snapshots[-1].item_count) == (2809, 27, 2809, 2809, 0)
    assert validate_snapshot_chain(snapshots, receipt) == snapshots

    changed = list(words)
    changed[1] = "ab"
    with pytest.raises(LexicalFloorError, match="exact packaged source"):
        snapshot_layers(changed)
    forged = replace(snapshots[1], parent_snapshot_id="00-words:sha256:" + "0" * 64)
    with pytest.raises(LexicalFloorError, match="parent mismatch"):
        validate_snapshot_chain((snapshots[0], forged, *snapshots[2:]), receipt)
    with pytest.raises(LexicalFloorError, match="standing"):
        replace(snapshots[4], standing="attested")
    with pytest.raises(LexicalFloorError, match="unresolved boundary"):
        replace(snapshots[0], hmmm="resolved")
