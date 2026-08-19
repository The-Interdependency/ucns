# === CHECKS ===
# id: xkcd_floor_payload_check
#   proves: xkcd_floor_reconstructs_official_source_payload
#   call: self::test_xkcd_floor_reconstructs_official_source_payload
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_function_participant_check
#   proves: xkcd_floor_functions_are_public_gonol_participants, xkcd_floor_preserves_order_occurrence_and_multiplicity
#   call: self::test_xkcd_floor_functions_preserve_order_occurrence_and_multiplicity
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_closure_check
#   proves: xkcd_floor_closes_relations_without_invented_grammar
#   call: self::test_xkcd_floor_closes_relations_without_invented_grammar
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
    FUNCTION_KIND,
    LETTER_RUN_KIND,
    VERTICAL_LINE_INDEX,
    XKCD_LEXICAL_FLOOR_STANDING,
    XKCD_LEXICAL_FLOOR_VERSION,
    XkcdLexicalFloorError,
    load_xkcd_lexical_floor,
    official_xkcd_source_payload,
    reconstruct_xkcd_lexical_floor,
    replay_xkcd_lexical_floor,
)
from ucns.oewn_core import OEWNCoreSnapshot, OEWNLexicalEntry, OEWNSense, OEWNSynset
from ucns.oewn_definition_recursion import build_oewn_definition_layer
from ucns.public_gonol_functions import (
    FUNCTIONAL_INDEX_NAMES,
    AtomicFunctionState,
    apply_public_gonol_function,
    build_public_gonol_function_table,
)


def _function_table():
    receipt = "ucns.oewn-core-receipt:sha256:" + "2" * 64
    entries = []
    synsets = []
    for ordinal, (_, _, name) in enumerate(FUNCTIONAL_INDEX_NAMES):
        lemma = name.lower()
        sense_id = f"function-{ordinal}%1"
        synset_id = f"function-{ordinal}"
        entries.append(OEWNLexicalEntry(
            lemma, "n", (), (OEWNSense(sense_id, synset_id, (), (), None),),
        ))
        synsets.append(OEWNSynset(
            synset_id, "n", (lemma,), (f"source function for {lemma}",), (),
        ))
    snapshot = OEWNCoreSnapshot(receipt, tuple(entries), tuple(synsets))
    return build_public_gonol_function_table(snapshot, build_oewn_definition_layer(snapshot))


def test_xkcd_floor_reconstructs_official_source_payload() -> None:
    source = load_xkcd_simplewriter()
    floor = load_xkcd_lexical_floor()
    payload = official_xkcd_source_payload(source)
    assert floor.payload == payload
    assert payload.count("|") == XKCD_SURFACE_COUNT - 1
    assert "".join(item.exact_text for item in floor.stream) == payload
    assert tuple(item.surface for item in floor.surfaces) == source.surface_forms


def test_xkcd_floor_functions_preserve_order_occurrence_and_multiplicity() -> None:
    floor = load_xkcd_lexical_floor()
    apostrophe = next(index for index, glyph, _ in FUNCTIONAL_INDEX_NAMES if glyph == "'")
    curly = next(index for index, glyph, _ in FUNCTIONAL_INDEX_NAMES if glyph == "’")
    functions = floor.function_occurrences()
    assert all(item.kind == FUNCTION_KIND for item in functions)
    assert all(item.public_gonol_index is not None for item in functions)
    assert sum(item.public_gonol_index == VERTICAL_LINE_INDEX for item in functions) == XKCD_SURFACE_COUNT - 1
    assert sum(item.public_gonol_index == apostrophe for item in functions) == 18
    assert sum(item.public_gonol_index == curly for item in functions) == 18
    surface = floor.closed_surface("don't")
    assert tuple((item.kind, item.exact_text) for item in surface.occurrences) == (
        (LETTER_RUN_KIND, "don"),
        (FUNCTION_KIND, "'"),
        (LETTER_RUN_KIND, "t"),
    )
    assert all(
        not any(ch in {"'", "’", "|"} for ch in item.exact_text)
        for item in floor.stream if item.kind == LETTER_RUN_KIND
    )


def test_xkcd_floor_closes_relations_without_invented_grammar() -> None:
    table = _function_table()
    source = load_xkcd_simplewriter()
    floor = reconstruct_xkcd_lexical_floor(source, table)
    assert floor.punctuation_functions_intrinsic is True
    assert floor.independent_punctuation_grammar_attached is False
    assert len(floor.carrier.nodes) == 1 + len(floor.stream)
    surface = floor.closed_surface("don't")
    assert surface.independent_punctuation_grammar_attached is False
    assert len(surface.carrier.nodes) == 4
    assert floor.function_applications
    first_pipe = next(
        item for item in floor.stream
        if item.public_gonol_index == VERTICAL_LINE_INDEX
    )
    prior = floor.stream[first_pipe.ordinal - 1]
    following = (floor.stream[first_pipe.ordinal + 1].participant_id,)
    expected = apply_public_gonol_function(
        table,
        VERTICAL_LINE_INDEX,
        AtomicFunctionState(prior.participant_id),
        following,
    )
    assert floor.function_applications[0] == expected


def test_xkcd_floor_refuses_family_map_and_closed_definitions() -> None:
    floor = load_xkcd_lexical_floor()
    assert floor.version == XKCD_LEXICAL_FLOOR_VERSION
    assert floor.standing == XKCD_LEXICAL_FLOOR_STANDING
    assert floor.source.family_count == 1000
    assert floor.family_mapping_available is False
    assert floor.closed_definition_support is False
    assert not hasattr(floor, "family_of")
    assert not hasattr(floor, "build_closed_definition")
    with pytest.raises(XkcdLexicalFloorError, match="family mapping"):
        replace(floor, family_mapping_available=True)
    with pytest.raises(XkcdLexicalFloorError, match="nonclaims"):
        replace(floor, closed_definition_support=True)
    with pytest.raises(XkcdLexicalFloorError, match="standing"):
        replace(floor, standing="current-lexical-floor-candidate")


def test_xkcd_floor_receipt_replays() -> None:
    floor = load_xkcd_lexical_floor()
    replayed = replay_xkcd_lexical_floor(floor)
    assert replayed == floor
    assert replayed.receipt_id == floor.receipt_id
    assert replayed.receipt_id.startswith("ucns.xkcd-lexical-floor-receipt:sha256:")
    assert replayed.carrier.stable_identity == floor.carrier.stable_identity
