#!/usr/bin/env python3
# === MODULE_BUILD ===
# id: ucns_affixiate_oewn_construction_run
#   module_name: run_affixiate_oewn_construction
#   module_kind: instrument
#   summary: constructs and independently replays OEWN character-word, xkcd subset, definition, and recursive gonols through affixiate
#   owner: Erin Spencer
#   public_surface: command-line interface
#   internal_surface: OEWN load, character-word corpus, xkcd subset, definition layer, recursive layer, receipt write
#   auth_boundary: requires UCNS_OEWN_2025_CORE_ROOT
#   storage_boundary: write new generated receipts; does not rewrite historical receipts
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_oewn_character_words
#   rollout: candidate construction runner; selection remains unresolved
#   rollback: remove the runner without rewriting historical receipts
#   requires: ucns_generic_gonol_affixiation, ucns_oewn_character_word_gonols
#   since: 2026-08-19
#   unresolved: selection of affixiate as canon
# === END MODULE_BUILD ===
#
# === CONTRACTS ===
# id: affixiate_run_does_not_rewrite_historical_receipts
#   given: the affixiate OEWN construction runner writes receipts
#   then: historical punctuation-aware definition and source-native recursive receipts remain the previously sealed bytes
#   class: safety
#   since: 2026-08-19
# === END CONTRACTS ===
"""Build and independently replay the affixiate OEWN/xkcd candidate scope."""

from __future__ import annotations

import os
import time
from pathlib import Path

from ucns.gonol_affixiation import AffixiationSource
from ucns.lexical_sources import load_xkcd_simplewriter, verify_oewn_2025_core
from ucns.lexical_xkcd_floor import reconstruct_xkcd_lexical_floor, replay_xkcd_lexical_floor
from ucns.oewn_character_words import (
    build_oewn_character_word_corpus,
    character_word_corpus_bytes,
    replay_oewn_character_word_corpus,
)
from ucns.oewn_core import load_oewn_core
from ucns.oewn_definition_recursion import (
    build_oewn_definition_layer,
    definition_layer_bytes,
    replay_oewn_definition_layer,
)
from ucns.recursive_gonol_relations import (
    build_source_native_recursive_gonols,
    recursive_gonol_layer_bytes,
    replay_source_native_recursive_gonols,
)


def main() -> int:
    root = os.environ.get("UCNS_OEWN_2025_CORE_ROOT")
    if not root:
        raise SystemExit("UCNS_OEWN_2025_CORE_ROOT is required")
    generated = Path("generated")
    generated.mkdir(exist_ok=True)
    started = time.time()

    def mark(label: str) -> None:
        print(f"{label} t={time.time() - started:.1f}s", flush=True)

    receipt = verify_oewn_2025_core(root)
    mark("verified")
    snapshot = load_oewn_core(root, receipt)
    mark(
        "loaded entries={0} synsets={1} defs={2} rels={3}".format(
            len(snapshot.lexical_entries),
            len(snapshot.synsets),
            snapshot.definition_count,
            snapshot.relation_occurrence_count,
        )
    )
    corpus = build_oewn_character_word_corpus(snapshot)
    mark(f"words={len(corpus.words)} tokens={len(corpus.tokens)}")
    replay_oewn_character_word_corpus(corpus, snapshot)
    word_bytes = character_word_corpus_bytes(corpus)
    (generated / "oewn-2025-core-character-word-gonol-receipt.json").write_bytes(word_bytes)
    mark(f"word_receipt={corpus.corpus_id}")

    xkcd = load_xkcd_simplewriter()
    floor = reconstruct_xkcd_lexical_floor(xkcd, corpus)
    replay_xkcd_lexical_floor(floor, corpus)
    mark(
        "xkcd surfaces={0} absent_from_oewn={1} receipt={2}".format(
            len(floor.surfaces),
            len(floor.xkcd_surfaces_absent_from_oewn),
            floor.receipt_id,
        )
    )

    layer = build_oewn_definition_layer(snapshot, corpus)
    replay_oewn_definition_layer(layer, snapshot)
    layer_bytes = definition_layer_bytes(layer)
    (generated / "oewn-2025-core-affixiate-definition-layer-receipt.json").write_bytes(layer_bytes)
    mark(f"definition_receipt={layer.layer_id} defs={len(layer.definition_gonols)}")

    recursive = build_source_native_recursive_gonols(snapshot, layer)
    replay_source_native_recursive_gonols(recursive, snapshot, layer)
    rec_bytes = recursive_gonol_layer_bytes(recursive)
    (generated / "oewn-2025-core-affixiate-recursive-gonol-receipt.json").write_bytes(rec_bytes)
    mark(
        f"recursive_receipt={recursive.layer_id} gonols={len(recursive.gonols)} selected={recursive.selected}"
    )
    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
