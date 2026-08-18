# === CHECKS ===
# id: current_glyph_axis_check
#   proves: glyph_axis_is_mobius_and_public_carrier_bound
#   call: self::test_current_glyph_axes_are_mobius_and_public_carrier_bound
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: current_lexical_traversal_check
#   proves: lexical_traversal_history_constrains_future, completed_word_gonols_are_atomic_and_reused
#   call: self::test_complete_xkcd_word_gonols_preserve_history_potential_and_atomicity
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: current_lexical_replay_check
#   proves: lexical_word_gonols_replay_exactly, lexical_traversal_history_constrains_future
#   call: self::test_word_gonol_replay_and_tamper_rejection
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.lexical_sources import load_xkcd_simplewriter
from ucns.lexical_word_gonols import (
    LexicalWordGonolError,
    construct_xkcd_word_gonols,
    replay_word_gonol,
)


def test_current_glyph_axes_are_mobius_and_public_carrier_bound() -> None:
    corpus = construct_xkcd_word_gonols(load_xkcd_simplewriter())
    assert len(corpus.axes) == 28
    assert {axis.glyph for axis in corpus.axes} == set("abcdefghijklmnopqrstuvwxyz'’")
    assert all(axis.topology == "mobius-one-sided-axis" for axis in corpus.axes)
    assert all(axis.glyph_role == "tic-on-axis" for axis in corpus.axes)
    assert all(axis.carrier_position > 0 for axis in corpus.axes)
    assert all(axis.continuous_coordinates_exposed is False for axis in corpus.axes)


def test_complete_xkcd_word_gonols_preserve_history_potential_and_atomicity() -> None:
    source = load_xkcd_simplewriter()
    corpus = construct_xkcd_word_gonols(source)
    assert len(corpus.word_gonols) == len(source.surface_forms) == 3_634
    assert tuple(item.surface for item in corpus.word_gonols) == source.surface_forms
    assert len(corpus.by_surface) == 3_634
    assert corpus.all_pairs_graph_materialized is False
    assert all(item.atomic_at_next_scale for item in corpus.word_gonols)
    branch = corpus.by_surface["branch"]
    assert [state.realized_prefix for state in branch.traversal] == [
        "b", "br", "bra", "bran", "branc", "branch",
    ]
    assert branch.traversal[-1].space_boundary_available is True
    assert "e" in branch.traversal[-1].admissible_next_glyphs
    r_after_b = branch.traversal[1]
    r_after_t = corpus.by_surface["tree"].traversal[1]
    assert r_after_b.selected_glyph == r_after_t.selected_glyph == "r"
    assert r_after_b.state_id != r_after_t.state_id
    assert r_after_b.admissible_next_glyphs != r_after_t.admissible_next_glyphs


def test_word_gonol_replay_and_tamper_rejection() -> None:
    source = load_xkcd_simplewriter()
    word = construct_xkcd_word_gonols(source).by_surface["branch"]
    assert replay_word_gonol(word, source) == word
    with pytest.raises(LexicalWordGonolError):
        replace(word.traversal[2], realized_prefix="xxx")
    with pytest.raises(LexicalWordGonolError, match="replay mismatch"):
        replay_word_gonol(replace(word, standing="atomic-xkcd-floor-word-gonol-candidate"), replace(source, surface_forms=source.surface_forms[::-1]))
