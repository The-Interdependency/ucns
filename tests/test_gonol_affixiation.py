# === CHECKS ===
# id: affixiate_generic_constructor_check
#   proves: affixiate_is_one_generic_constructor, affixiate_scale_is_context_not_type, affixiate_relation_enters_the_gonol, affixiate_reuses_completed_identity
#   call: self::test_affixiate_is_one_generic_constructor
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: affixiate_refuses_selection_check
#   proves: affixiate_refuses_invented_scale_or_selection
#   call: self::test_affixiate_refuses_invented_scale_or_selection
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: affixiate_characters_are_gonols_check
#   proves: affixiate_characters_are_gonols
#   call: self::test_affixiate_characters_are_gonols
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.gonol_affixiation import (
    AFFIXIATE_STANDING,
    SCALE_CONTEXTS,
    AffixiationClosure,
    AffixiationError,
    AffixiationRelation,
    AffixiationSource,
    Gonol,
    affixiate,
)


def _source() -> AffixiationSource:
    return AffixiationSource("ucns.oewn-core-receipt:sha256:" + "a" * 64, "fixture")


def test_affixiate_is_one_generic_constructor() -> None:
    source = _source()
    glyph = affixiate(
        (),
        AffixiationRelation(9, "character-glyph"),
        source,
        "character",
        AffixiationClosure(exact_text="w", extras=(("kind", "character"),)),
    )
    letter = affixiate(
        (glyph,),
        AffixiationRelation(8, "history-bearing-character-step"),
        source,
        "character",
        AffixiationClosure(exact_text="w", extras=(("realized_prefix", "w"),)),
    )
    word = affixiate(
        (letter,),
        AffixiationRelation(6, "ordered-character-word-closure"),
        source,
        "word",
        AffixiationClosure(exact_text="w"),
    )
    again = affixiate(
        (letter,),
        AffixiationRelation(6, "ordered-character-word-closure"),
        source,
        "word",
        AffixiationClosure(exact_text="w"),
    )
    assert isinstance(letter, Gonol) and isinstance(word, Gonol)
    assert letter.scale == "character" and word.scale == "word"
    assert word.gonol_id == again.gonol_id
    assert word.selected is False
    assert word.standing == AFFIXIATE_STANDING
    assert word.atomic_at_next_scale is True
    assert len(word.carrier.nodes) == 2
    assert {item.scale for item in (glyph, letter, word)}.issubset(SCALE_CONTEXTS)
    assert glyph.participant_ids == ()
    assert letter.participant_ids == (glyph.gonol_id,)


def test_affixiate_characters_are_gonols() -> None:
    source = _source()
    glyph = affixiate(
        (),
        AffixiationRelation(9, "character-glyph"),
        source,
        "character",
        AffixiationClosure(exact_text="w", extras=(("kind", "character"),)),
    )
    assert isinstance(glyph, Gonol)
    assert glyph.scale == "character"
    assert glyph.exact_text == "w"
    assert glyph.atomic_at_next_scale is True


def test_affixiate_refuses_invented_scale_or_selection() -> None:
    source = _source()
    with pytest.raises(AffixiationError, match="scale context"):
        affixiate((), AffixiationRelation(8, "step"), source, "phoneme", AffixiationClosure())
    gonol = affixiate(
        (),
        AffixiationRelation(8, "step"),
        source,
        "character",
        AffixiationClosure(exact_text="a"),
    )
    with pytest.raises(AffixiationError, match="selected"):
        replace(gonol, selected=True)
    with pytest.raises(AffixiationError, match="participant"):
        affixiate((), AffixiationRelation(6, "word"), source, "word", AffixiationClosure())
