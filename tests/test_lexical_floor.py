# === CHECKS ===
# id: lexical_floor_source_and_word_check
#   proves: lexical_floor_source_receipt_binds_packaged_bytes, lexical_floor_words_are_unique_exact_glyph_sets, lexical_floor_order_is_serialization_only, lexical_floor_reuses_canonical_glyph_assignment
#   call: self::test_source_word_and_glyph_boundaries
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from importlib.resources import files
import json

import pytest

from ucns.lexical_floor import (
    LEXICAL_SOURCE_STANDING,
    NGSL_ATTRIBUTION_RESOURCE,
    NGSL_SOURCE_RESOURCE,
    NGSL_WORD_COUNT,
    NGSL_WORD_RESOURCE,
    LexicalFloorError,
    LexicalWordGonol,
    _parse_source_bundle,
    create_hyperspace_potential,
    create_word_gonols,
    define_glyphs,
    load_ngsl_source_receipt,
    load_ngsl_words,
    word_gonol_id,
)


def test_source_word_and_glyph_boundaries():
    receipt = load_ngsl_source_receipt()
    words = load_ngsl_words()
    gonols = create_word_gonols(words)
    potential = create_hyperspace_potential(gonols)
    glyphs = define_glyphs(words)
    assert potential.gonol("bank").word == "bank"
    assert receipt.word_count == len(words) == NGSL_WORD_COUNT == 2809
    assert receipt.standing == LEXICAL_SOURCE_STANDING
    assert receipt.receipt_id.startswith("ucns.lexical-source-receipt:sha256:")
    assert all(len(value) == 64 for value in (
        receipt.metadata_sha256, receipt.word_file_sha256,
        receipt.word_sequence_sha256, receipt.attribution_sha256,
    ))
    assert len(set(words)) == len(words) and words[0] == "a" and words[-1] == "zone" and "I" in words
    assert len(glyphs) == 27 and all(glyph.carrier_position > 0 for glyph in glyphs)
    assert len(gonols) == len({gonol.gonol_id for gonol in gonols}) == len(words)

    package = files("ucns")
    metadata = package.joinpath(NGSL_SOURCE_RESOURCE).read_bytes()
    word_bytes = package.joinpath(NGSL_WORD_RESOURCE).read_bytes()
    attribution = package.joinpath(NGSL_ATTRIBUTION_RESOURCE).read_bytes()
    changed = json.loads(metadata.decode())
    changed["acquisition"]["target_git_blob"] = "0" * 40
    with pytest.raises(LexicalFloorError, match="declared Git blob"):
        _parse_source_bundle((json.dumps(changed) + "\n").encode(), word_bytes, attribution)
    with pytest.raises(LexicalFloorError, match="declared digest"):
        _parse_source_bundle(metadata, word_bytes, attribution + b"tamper\n")
    with pytest.raises(LexicalFloorError, match="standing"):
        replace(receipt, standing="canonical")

    for invalid in ("", "a b", "a\tb", "a\u00a0b", "a🙂"):
        with pytest.raises(LexicalFloorError):
            word_gonol_id(invalid)
    with pytest.raises(LexicalFloorError, match="SPACE"):
        LexicalWordGonol("a b", ("a", " ", "b"), "word-gonol:sha256:" + "0" * 64)
    with pytest.raises(LexicalFloorError, match="serialization"):
        create_word_gonols(("b", "a"))
    with pytest.raises(LexicalFloorError, match="duplicate"):
        create_word_gonols(("a", "a"))
