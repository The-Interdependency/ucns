# === CHECKS ===
# id: lexical_floor_exact_collection_check
#   resolves: lexical_floor_words_are_unique_exact_glyph_sets, lexical_floor_order_is_serialization_only
#   test: test_ngsl_word_only_collection_is_exact_unique_and_reproducible
#   class: correctness
#   since: 2026-08-04
#
# id: lexical_floor_glyph_and_gonol_check
#   resolves: lexical_floor_reuses_canonical_glyph_assignment
#   test: test_existing_glyph_canon_builds_one_gonol_per_word
#   class: evidence
#   since: 2026-08-04
#
# id: lexical_floor_projection_check
#   resolves: lexical_hyperspace_is_projection_not_embedding
#   test: test_hyperspace_projects_character_relations_without_embedding_claim
#   class: safety
#   since: 2026-08-04
#
# id: lexical_floor_candidate_layer_check
#   resolves: affixiation_and_compounding_are_candidate_layers
#   test: test_affixiation_and_compounding_begin_as_orthographic_candidates
#   class: doctrine
#   since: 2026-08-04
#
# id: lexical_floor_definition_plurality_check
#   resolves: definitions_are_context_plural
#   test: test_one_word_gonol_accepts_many_context_sourced_definitions
#   class: evidence
#   since: 2026-08-04
#
# id: lexical_floor_snapshot_check
#   resolves: every_added_layer_has_a_snapshot
#   test: test_each_added_layer_has_a_parented_snapshot
#   class: correctness
#   since: 2026-08-04
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.lexical_floor import (
    DEFINITION_STANDING,
    NGSL_WORD_COUNT,
    ORTHOGRAPHIC_CANDIDATE_STANDING,
    DefinitionSense,
    LexicalFloorError,
    create_definition_layer,
    create_hyperspace_potential,
    create_word_gonols,
    define_glyphs,
    derive_affixiation_candidates,
    derive_compound_candidates,
    load_ngsl_words,
    snapshot_layers,
)


def _floor():
    words = load_ngsl_words()
    gonols = create_word_gonols(words)
    return words, gonols, create_hyperspace_potential(gonols)


def test_ngsl_word_only_collection_is_exact_unique_and_reproducible():
    words = load_ngsl_words()

    assert len(words) == NGSL_WORD_COUNT == 2809
    assert len(set(words)) == len(words)
    assert all(word and not any(glyph.isspace() for glyph in word) for word in words)
    assert words[0] == "a"
    assert words[-1] == "zone"
    assert "I" in words
    assert not any("," in word for word in words)


def test_existing_glyph_canon_builds_one_gonol_per_word():
    words, gonols, _ = _floor()
    glyphs = define_glyphs(words)

    assert len(glyphs) == 27
    assert {glyph.value for glyph in glyphs} == set("abcdefghijklmnopqrstuvwxyzI")
    assert all(glyph.carrier_position is not None for glyph in glyphs)
    assert len(gonols) == len(words)
    assert len({gonol.gonol_id for gonol in gonols}) == len(words)
    assert all(gonol.glyphs == tuple(gonol.word) for gonol in gonols)


def test_hyperspace_projects_character_relations_without_embedding_claim():
    _, _, potential = _floor()

    relation = potential.project("act", "action")

    assert relation.common_prefix_length == 3
    assert relation.right_contains_left is True
    assert relation.left_contains_right is False
    assert relation.edit_distance == 3
    assert relation.standing == "character-derived-projection"


def test_affixiation_and_compounding_begin_as_orthographic_candidates():
    _, _, potential = _floor()

    affixiation = derive_affixiation_candidates(potential)
    compounds = derive_compound_candidates(potential)

    assert any(
        item.base_word == "act"
        and item.derived_word == "action"
        and item.affix == "ion"
        and item.side == "suffix"
        and item.standing == ORTHOGRAPHIC_CANDIDATE_STANDING
        for item in affixiation
    )
    assert any(
        item.compound_word == "background"
        and item.left_word == "back"
        and item.right_word == "ground"
        and item.standing == ORTHOGRAPHIC_CANDIDATE_STANDING
        for item in compounds
    )


def test_one_word_gonol_accepts_many_context_sourced_definitions():
    _, _, potential = _floor()
    word = potential.gonol("bank")
    river = DefinitionSense(
        word_gonol_id=word.gonol_id,
        context_identity="context:river-bank",
        definition="The land beside a river.",
        source_identity="source:test-contexts-v1",
    )
    finance = DefinitionSense(
        word_gonol_id=word.gonol_id,
        context_identity="context:financial-bank",
        definition="An institution that holds and lends money.",
        source_identity="source:test-contexts-v1",
    )

    layer = create_definition_layer(potential, (river, finance))

    assert tuple(layer) == (word.gonol_id,)
    assert layer[word.gonol_id] == (river, finance)
    assert all(item.standing == DEFINITION_STANDING for item in layer[word.gonol_id])
    with pytest.raises(LexicalFloorError, match="duplicate contextual"):
        create_definition_layer(potential, (river, replace(river)))


def test_each_added_layer_has_a_parented_snapshot():
    words = load_ngsl_words()
    snapshots = snapshot_layers(words)
    expected_layers = (
        "00-words",
        "01-glyphs",
        "02-word-gonols",
        "03-character-hyperspace-potential",
        "04-affixiation",
        "05-compounding",
        "06-definitions",
    )

    assert tuple(snapshot.layer_id for snapshot in snapshots) == expected_layers
    assert snapshots[0].parent_snapshot_id is None
    assert all(
        current.parent_snapshot_id == previous.snapshot_id
        for previous, current in zip(snapshots, snapshots[1:])
    )
    assert snapshots[0].item_count == 2809
    assert snapshots[1].item_count == 27
    assert snapshots[2].item_count == 2809
    assert snapshots[3].item_count == 2809
    assert snapshots[-1].item_count == 0
    assert all(len(snapshot.content_digest) == 64 for snapshot in snapshots)
    assert all(snapshot.hmmm for snapshot in snapshots)
