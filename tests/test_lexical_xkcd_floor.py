# === CHECKS ===
# id: xkcd_floor_bind_check
#   proves: xkcd_floor_binds_exact_source_and_atomic_corpus
#   call: self::test_xkcd_floor_binds_exact_source_and_atomic_corpus
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_membership_check
#   proves: xkcd_floor_membership_is_exact_surface_identity
#   call: self::test_xkcd_floor_membership_is_exact_surface_identity
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_nonclaim_check
#   proves: xkcd_floor_does_not_invent_family_mapping, xkcd_floor_does_not_close_definitions
#   call: self::test_xkcd_floor_refuses_family_map_and_closed_definitions
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_replay_check
#   proves: xkcd_floor_receipt_replays
#   call: self::test_xkcd_floor_receipt_replays
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.lexical_sources import XKCD_SURFACE_COUNT, load_xkcd_simplewriter
from ucns.lexical_xkcd_floor import (
    XKCD_LEXICAL_FLOOR_ID,
    XKCD_LEXICAL_FLOOR_STANDING,
    XkcdLexicalFloorError,
    load_xkcd_lexical_floor,
    replay_xkcd_lexical_floor,
)


def test_xkcd_floor_binds_exact_source_and_atomic_corpus() -> None:
    source = load_xkcd_simplewriter()
    floor = load_xkcd_lexical_floor()
    assert floor.floor_id == XKCD_LEXICAL_FLOOR_ID
    assert floor.standing == XKCD_LEXICAL_FLOOR_STANDING
    assert floor.source == source
    assert floor.corpus.source_receipt_id == source.receipt_id
    assert len(floor.corpus.word_gonols) == XKCD_SURFACE_COUNT
    assert tuple(item.surface for item in floor.corpus.word_gonols) == source.surface_forms
    assert floor.all_pairs_graph_materialized is False
    assert floor.corpus.all_pairs_graph_materialized is False
    assert all(item.atomic_at_next_scale for item in floor.corpus.word_gonols)


def test_xkcd_floor_membership_is_exact_surface_identity() -> None:
    floor = load_xkcd_lexical_floor()
    assert floor.contains("branch") is True
    assert floor.word_gonol("branch").surface == "branch"
    assert floor.contains("BRANCH") is False
    assert floor.contains(" branch") is False
    with pytest.raises(XkcdLexicalFloorError, match="exact xkcd floor admission"):
        floor.word_gonol("BRANCH")
    with pytest.raises(XkcdLexicalFloorError, match="nonempty exact surface"):
        floor.contains("")


def test_xkcd_floor_refuses_family_map_and_closed_definitions() -> None:
    floor = load_xkcd_lexical_floor()
    assert floor.source.family_count == 1000
    assert floor.family_mapping_available is False
    assert floor.closed_definition_support is False
    assert not hasattr(floor, "family_of")
    assert not hasattr(floor, "build_closed_definition")
    with pytest.raises(XkcdLexicalFloorError, match="family mapping"):
        replace(floor, family_mapping_available=True)
    with pytest.raises(XkcdLexicalFloorError, match="close definition"):
        replace(floor, closed_definition_support=True)
    with pytest.raises(XkcdLexicalFloorError, match="standing"):
        replace(floor, standing="canonical-lexical-floor")


def test_xkcd_floor_receipt_replays() -> None:
    floor = load_xkcd_lexical_floor()
    replayed = replay_xkcd_lexical_floor(floor)
    assert replayed == floor
    assert replayed.receipt_id == floor.receipt_id
    assert replayed.receipt_id.startswith("ucns.xkcd-lexical-floor-receipt:sha256:")
    assert replayed.source.receipt_id == floor.source.receipt_id
    assert replayed.corpus.corpus_id == floor.corpus.corpus_id
