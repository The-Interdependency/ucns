#!/usr/bin/env python3
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
