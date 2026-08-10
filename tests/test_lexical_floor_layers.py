# === CHECKS ===
# id: lexical_floor_layer_check
#   proves: lexical_hyperspace_is_occurrence_preserving_projection_not_embedding, affixiation_and_compounding_are_candidate_layers, definitions_are_context_plural_and_immutable
#   call: self::test_projection_candidate_and_definition_boundaries
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.lexical_floor import (
    CHARACTER_RELATIONSHIP_STANDING,
    DEFINITION_STANDING,
    GLYPH_TYPE_SET_IDENTITY_POLICY,
    GLYPH_TYPE_SET_INFORMATION_LOSS,
    ORTHOGRAPHIC_CANDIDATE_STANDING,
    DefinitionSense,
    LexicalFloorError,
    SharedGlyphOccurrence,
    create_definition_layer,
    create_hyperspace_potential,
    create_word_gonols,
    derive_affixiation_candidates,
    derive_compound_candidates,
    load_ngsl_words,
)


def test_projection_candidate_and_definition_boundaries():
    potential = create_hyperspace_potential(create_word_gonols(load_ngsl_words()))
    relation = potential.project("all", "ball")
    assert relation.shared_occurrences == (
        SharedGlyphOccurrence("a", 0, 1),
        SharedGlyphOccurrence("l", 1, 2), SharedGlyphOccurrence("l", 1, 3),
        SharedGlyphOccurrence("l", 2, 2), SharedGlyphOccurrence("l", 2, 3),
    )
    assert relation.shared_glyph_type_set.glyphs == ("a", "l")
    assert relation.shared_glyph_type_set.identity_policy == GLYPH_TYPE_SET_IDENTITY_POLICY
    assert relation.shared_glyph_type_set.information_loss == GLYPH_TYPE_SET_INFORMATION_LOSS
    assert relation.standing == CHARACTER_RELATIONSHIP_STANDING
    with pytest.raises(TypeError):
        potential._by_word["forged"] = potential.gonol("all")
    with pytest.raises(LexicalFloorError, match="standing"):
        replace(relation, standing="canonical")
    with pytest.raises(LexicalFloorError, match="occurrence"):
        replace(relation, shared_occurrences=relation.shared_occurrences[:-1])

    action = next(item for item in derive_affixiation_candidates(potential)
                  if item.base_word == "act" and item.derived_word == "action" and item.affix == "ion")
    background = next(item for item in derive_compound_candidates(potential)
                      if item.compound_word == "background" and item.left_word == "back" and item.right_word == "ground")
    assert action.standing == background.standing == ORTHOGRAPHIC_CANDIDATE_STANDING
    with pytest.raises(LexicalFloorError, match="base identity"):
        replace(action, base_gonol_id="word-gonol:sha256:" + "0" * 64)
    with pytest.raises(LexicalFloorError, match="standing"):
        replace(background, standing="attested")

    word = potential.gonol("bank")
    river = DefinitionSense(word.gonol_id, "context:river", "Land beside a river.", "source:test")
    finance = DefinitionSense(word.gonol_id, "context:finance", "An institution holding money.", "source:test")
    layer = create_definition_layer(potential, (river, finance))
    assert layer[word.gonol_id] == (river, finance)
    assert all(item.standing == DEFINITION_STANDING for item in layer[word.gonol_id])
    with pytest.raises(TypeError):
        layer[word.gonol_id] = ()
    with pytest.raises(LexicalFloorError, match="duplicate contextual"):
        create_definition_layer(potential, (river, replace(river)))
    with pytest.raises(LexicalFloorError, match="standing"):
        replace(river, standing="canonical")
