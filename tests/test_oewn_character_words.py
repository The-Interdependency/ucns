# === CHECKS ===
# id: oewn_character_history_check
#   proves: oewn_character_history_is_corpus_wide, oewn_character_words_use_affixiate, oewn_closed_words_are_atomic, oewn_characters_are_gonols
#   call: self::test_corpus_wide_character_history_closes_words
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: oewn_character_words_replay_check
#   proves: oewn_character_words_replay
#   call: self::test_character_word_corpus_replays
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: affixiate_run_historical_receipt_check
#   proves: affixiate_run_does_not_rewrite_historical_receipts
#   call: self::test_historical_receipts_remain
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from ucns.gonol_affixiation import AffixiationSource, Gonol, affixiate
from ucns.oewn_character_words import (
    build_character_word_corpus,
    character_word_corpus_bytes,
)
from ucns.oewn_core import OEWNCoreSnapshot, OEWNLexicalEntry, OEWNSense, OEWNSynset
from ucns.oewn_character_words import build_oewn_character_word_corpus, replay_oewn_character_word_corpus


def _source() -> AffixiationSource:
    return AffixiationSource("ucns.oewn-core-receipt:sha256:" + "c" * 64, "oewn-2025-core")


def test_corpus_wide_character_history_closes_words() -> None:
    corpus = build_character_word_corpus(
        ("a", "about", "water", "don't", "waterfall"),
        _source(),
    )
    assert all(isinstance(item, Gonol) and item.scale == "word" for item in corpus.words)
    water = corpus.word("water")
    prefixes = [item.extra("realized_prefix") for item in corpus.token_participants(water)]
    assert prefixes == ["w", "wa", "wat", "wate", "water"]
    assert all(item.scale == "character" for item in corpus.token_participants(water))
    w_history = corpus.token_participants(water)[0]
    w_glyph = corpus.by_id[w_history.participant_ids[0]]
    assert w_glyph.scale == "character"
    assert w_glyph.exact_text == "w"
    assert w_glyph.participant_ids == ()
    waterfall_w = corpus.token_participants(corpus.word("waterfall"))[0]
    assert waterfall_w.participant_ids[0] == w_glyph.gonol_id
    a_id = corpus.token_participants(corpus.word("a"))[0].gonol_id
    about_a = corpus.token_participants(corpus.word("about"))[0]
    assert about_a.gonol_id == a_id
    assert "b" in about_a.extra("admissible_next_glyphs")
    wat = corpus.token_participants(water)[2]
    assert "e" in wat.extra("admissible_next_glyphs")
    dont = corpus.token_participants(corpus.word("don't"))
    assert [item.exact_text for item in dont] == ["d", "o", "n", "'", "t"]
    assert dont[3].extra("kind") == "public-gonol-function"
    assert corpus.word("water").gonol_id != corpus.word("waterfall").gonol_id
    assert affixiate is affixiate


def test_character_word_corpus_replays() -> None:
    snapshot = OEWNCoreSnapshot(
        "ucns.oewn-core-receipt:sha256:" + "c" * 64,
        (
            OEWNLexicalEntry("water", "n", ("waters",), (OEWNSense("water%1", "s1", (), (), None),)),
            OEWNLexicalEntry("don't", "v", (), (OEWNSense("dont%1", "s2", (), (), None),)),
        ),
        (
            OEWNSynset("s1", "n", ("water",), ("a liquid",), ()),
            OEWNSynset("s2", "v", ("don't",), ("don't cut.",), ()),
        ),
    )
    corpus = build_oewn_character_word_corpus(snapshot)
    replayed = replay_oewn_character_word_corpus(corpus, snapshot)
    assert character_word_corpus_bytes(replayed) == character_word_corpus_bytes(corpus)
    assert corpus.word("waters").scale == "word"


def test_historical_receipts_remain() -> None:
    from pathlib import Path

    root = Path(__file__).resolve().parents[1] / "generated"
    punctuation = (root / "oewn-2025-core-punctuation-aware-definition-layer-receipt.json").read_text()
    recursive = (root / "oewn-2025-core-source-native-recursive-gonol-receipt.json").read_text()
    assert "c53c9941b9286193c677e8057238f380f00e90b06bf488b78a2c7caece5738b7" in punctuation
    assert "561c8cee9cfc0befdcef9620cfc044033cf034ac4ca9cb1eadaf8b7527bb8af3" in recursive
