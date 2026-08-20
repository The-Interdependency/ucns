# === CHECKS ===
# id: xkcd_floor_payload_check
#   proves: xkcd_floor_reconstructs_official_source_payload
#   call: self::test_xkcd_floor_reconstructs_official_source_payload
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_character_composition_check
#   proves: xkcd_floor_characters_compose_words, xkcd_floor_traversal_history_changes_identity, xkcd_floor_repeated_words_reuse_identity
#   call: self::test_xkcd_floor_characters_compose_words
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_function_participant_check
#   proves: xkcd_floor_functions_are_public_gonol_participants, xkcd_floor_preserves_order_occurrence_and_multiplicity
#   call: self::test_xkcd_floor_functions_preserve_order_occurrence_and_multiplicity
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_closure_check
#   proves: xkcd_floor_closes_relations_without_invented_grammar
#   call: self::test_xkcd_floor_closes_relations_without_invented_grammar
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_nonclaim_check
#   proves: xkcd_floor_does_not_invent_family_mapping, xkcd_floor_does_not_close_definitions
#   call: self::test_xkcd_floor_refuses_family_map_and_closed_definitions
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_replay_check
#   proves: xkcd_floor_receipt_replays
#   call: self::test_xkcd_floor_receipt_replays
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_source_validation_check
#   proves: xkcd_floor_source_is_validated_before_receipt
#   call: self::test_xkcd_floor_source_is_validated_before_receipt
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: xkcd_floor_explicit_context_check
#   proves: xkcd_floor_applications_require_explicit_context, xkcd_floor_receipt_binds_application_identities
#   call: self::test_xkcd_floor_applications_require_explicit_context
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from functools import lru_cache

import pytest

from ucns.gonol_affixiation import AffixiationSource
from ucns.lexical_sources import XKCD_SURFACE_COUNT, load_xkcd_simplewriter
from ucns.lexical_xkcd_floor import (
    CHARACTER_KIND,
    CLOSED_WORD_KIND,
    FUNCTION_KIND,
    VERTICAL_LINE_INDEX,
    XKCD_LEXICAL_FLOOR_STANDING,
    XKCD_LEXICAL_FLOOR_VERSION,
    FunctionApplicationPlan,
    XkcdLexicalFloorError,
    _close,
    official_xkcd_source_payload,
    reconstruct_xkcd_lexical_floor,
    replay_xkcd_lexical_floor,
)
from ucns.oewn_character_words import build_character_word_corpus
from ucns.oewn_definition_recursion import CLOSED_WORD_KIND, build_oewn_definition_layer
from ucns.oewn_core import OEWNCoreSnapshot, OEWNLexicalEntry, OEWNSense, OEWNSynset

from ucns.public_gonol_functions import (
    FUNCTIONAL_INDEX_NAMES,
    AtomicFunctionState,
    apply_public_gonol_function,
    build_public_gonol_function_table,
)


@lru_cache(maxsize=1)
def _word_corpus():
    source = load_xkcd_simplewriter()
    extras = ("waterfall", "anatomy", "branched")
    surfaces = tuple(dict.fromkeys((*source.surface_forms, *extras)))
    return build_character_word_corpus(
        surfaces,
        AffixiationSource("ucns.oewn-core-receipt:sha256:" + "c" * 64, "oewn-2025-core"),
    )


def _floor():
    return reconstruct_xkcd_lexical_floor(load_xkcd_simplewriter(), _word_corpus())


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
    floor = _floor()
    payload = official_xkcd_source_payload(source)
    assert floor.payload == payload
    assert payload.count("|") == XKCD_SURFACE_COUNT - 1
    assert "".join(item.exact_text for item in floor.stream) == payload
    assert tuple(item.surface for item in floor.surfaces) == source.surface_forms
    assert len(floor.surfaces) == XKCD_SURFACE_COUNT == 3_634
    assert all("".join(item.exact_text for item in surface.occurrences) == surface.surface for surface in floor.surfaces)
    assert all(item.kind != "letter-run" for item in floor.stream)
    assert sum(item.kind == CLOSED_WORD_KIND for item in floor.stream) == XKCD_SURFACE_COUNT
    assert floor.family_mapping_available is False


def test_xkcd_floor_characters_compose_words() -> None:
    floor = _floor()
    water = floor.closed_surface("water")
    assert tuple((item.kind, item.exact_text) for item in water.occurrences) == tuple(
        (CHARACTER_KIND, glyph) for glyph in "water"
    )
    acc = ""
    prefixes = []
    for item in water.occurrences:
        acc += item.exact_text
        prefixes.append(acc)
    assert prefixes == ["w", "wa", "wat", "wate", "water"]
    assert len({item.participant_id for item in water.occurrences}) == 5
    assert all(item.participant_id.startswith("ucns.gonol:sha256:") for item in water.occurrences)
    branch_r = floor.closed_surface("branch").occurrences[1]
    tree_r = floor.closed_surface("tree").occurrences[1]
    assert branch_r.exact_text == tree_r.exact_text == "r"
    assert branch_r.participant_id != tree_r.participant_id
    a_surface = floor.closed_surface("a").occurrences[0]
    about_a = floor.closed_surface("about").occurrences[0]
    assert a_surface.participant_id == about_a.participant_id
    assert a_surface.start == about_a.start == 0
    assert floor.closed_surface("a").gonol_id != floor.closed_surface("about").gonol_id
    assert floor.closed_surface("water").word_gonol_id.startswith("ucns.gonol:sha256:")
    snapshot = OEWNCoreSnapshot(
        "ucns.oewn-core-receipt:sha256:" + "9" * 64,
        (OEWNLexicalEntry("don't", "v", (), (OEWNSense("dont%1", "s1", (), (), None),)),),
        (OEWNSynset("s1", "v", ("don't",), ("don't cut.",), ()),),
    )
    layer = build_oewn_definition_layer(snapshot)
    punctuated = next(item for item in layer.definition_gonols if item.exact_gloss == "don't cut.")
    lemma_id = dict(layer.closed_word_pairs)["don't"]
    assert punctuated.occurrences[0].kind == CLOSED_WORD_KIND
    assert punctuated.occurrences[0].participant_id == lemma_id


def test_xkcd_floor_functions_preserve_order_occurrence_and_multiplicity() -> None:
    floor = _floor()
    apostrophe = next(index for index, glyph, _ in FUNCTIONAL_INDEX_NAMES if glyph == "'")
    curly = next(index for index, glyph, _ in FUNCTIONAL_INDEX_NAMES if glyph == "’")
    internal = [
        item for surface in floor.surfaces for item in surface.occurrences
        if item.kind == FUNCTION_KIND
    ]
    functions = floor.function_occurrences()
    assert all(item.kind == FUNCTION_KIND for item in functions)
    assert all(item.public_gonol_index is not None for item in functions)
    assert sum(item.public_gonol_index == VERTICAL_LINE_INDEX for item in functions) == XKCD_SURFACE_COUNT - 1
    assert sum(item.public_gonol_index == apostrophe for item in internal) == 18
    assert sum(item.public_gonol_index == curly for item in internal) == 18
    surface = floor.closed_surface("don't")
    assert tuple((item.kind, item.exact_text) for item in surface.occurrences) == (
        (CHARACTER_KIND, "d"),
        (CHARACTER_KIND, "o"),
        (CHARACTER_KIND, "n"),
        (FUNCTION_KIND, "'"),
        (CHARACTER_KIND, "t"),
    )
    t_after_apostrophe = surface.occurrences[-1]
    t_in_tree = floor.closed_surface("tree").occurrences[0]
    assert t_after_apostrophe.exact_text == t_in_tree.exact_text == "t"
    assert t_after_apostrophe.participant_id != t_in_tree.participant_id
    assert all(item.kind != CHARACTER_KIND for item in floor.stream)


def test_xkcd_floor_closes_relations_without_invented_grammar() -> None:
    table = _function_table()
    source = load_xkcd_simplewriter()
    corpus = _word_corpus()
    floor = reconstruct_xkcd_lexical_floor(source, corpus, table)
    assert floor.punctuation_functions_intrinsic is True
    assert floor.independent_punctuation_grammar_attached is False
    assert floor.function_applications == ()
    assert floor.table_id == table.table_id
    assert len(floor.carrier.nodes) == 1 + len(floor.stream)
    surface = floor.closed_surface("don't")
    assert floor.word_gonol("don't") is surface
    assert surface.independent_punctuation_grammar_attached is False
    assert len(surface.carrier.nodes) == 6
    replay_xkcd_lexical_floor(floor, corpus, table)


def test_xkcd_floor_refuses_family_map_and_closed_definitions() -> None:
    floor = _floor()
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
    with pytest.raises(XkcdLexicalFloorError, match="official packaged receipt"):
        replace(floor, source=replace(floor.source, source_url="https://example.invalid/words.js"))
    water = floor.closed_surface("water")
    with pytest.raises(XkcdLexicalFloorError, match="contiguous"):
        replace(water, occurrences=(replace(water.occurrences[0], start=99, end=100),) + water.occurrences[1:])
    stream = list(floor.stream)
    pipe_index = next(i for i, item in enumerate(stream) if item.kind == FUNCTION_KIND)
    stream[pipe_index] = replace(stream[pipe_index], start=0, end=1)
    with pytest.raises(XkcdLexicalFloorError, match="contiguous"):
        replace(floor, stream=tuple(stream))
    bogus = "ucns.gonol:sha256:" + "0" * 64
    with pytest.raises(XkcdLexicalFloorError, match="closed-word participant"):
        replace(
            floor,
            stream=(replace(floor.stream[0], participant_id=bogus),) + floor.stream[1:],
            carrier=_close((bogus,) + tuple(item.participant_id for item in floor.stream[1:])),
        )


def test_xkcd_floor_receipt_replays() -> None:
    corpus = _word_corpus()
    floor = reconstruct_xkcd_lexical_floor(load_xkcd_simplewriter(), corpus)
    replayed = replay_xkcd_lexical_floor(floor, corpus)
    assert replayed == floor
    assert replayed.receipt_id == floor.receipt_id
    assert replayed.receipt_id.startswith("ucns.xkcd-lexical-floor-receipt:sha256:")
    assert replayed.carrier.stable_identity == floor.carrier.stable_identity
    assert replayed.table_id is None
    table = _function_table()
    with pytest.raises(XkcdLexicalFloorError, match="absent table"):
        replay_xkcd_lexical_floor(floor, corpus, table)


def test_xkcd_floor_source_is_validated_before_receipt() -> None:
    source = load_xkcd_simplewriter()
    corpus = _word_corpus()
    with pytest.raises(XkcdLexicalFloorError, match="not valid for floor receipt"):
        reconstruct_xkcd_lexical_floor(replace(source, surface_forms=source.surface_forms[1:]), corpus)


def test_xkcd_floor_applications_require_explicit_context() -> None:
    table = _function_table()
    source = load_xkcd_simplewriter()
    corpus = _word_corpus()
    base = reconstruct_xkcd_lexical_floor(source, corpus, table)
    assert base.function_applications == ()
    first_pipe = next(
        item for item in base.stream
        if item.public_gonol_index == VERTICAL_LINE_INDEX
    )
    prior = base.stream[first_pipe.ordinal - 1]
    following = first_pipe.ordinal + 1
    plan = FunctionApplicationPlan(
        first_pipe.ordinal,
        AtomicFunctionState(prior.participant_id),
        (following,),
    )
    floor = reconstruct_xkcd_lexical_floor(source, corpus, table, (plan,))
    expected = apply_public_gonol_function(
        table,
        VERTICAL_LINE_INDEX,
        plan.current_state,
        (base.stream[following].participant_id,),
    )
    assert floor.function_applications == (expected,)
    bound = floor.as_payload()["function_applications"]
    assert bound == [{
        "stream_ordinal": first_pipe.ordinal,
        "function_id": expected.function_id,
        "result_atomic_gonol_id": expected.result_atomic_gonol_id,
        "context_ordinals": [following],
        "current_atomic_gonol_id": prior.participant_id,
    }]
    replayed = replay_xkcd_lexical_floor(floor, corpus, table)
    assert replayed == floor
    assert replayed.receipt_id == floor.receipt_id
    assert replayed.function_applications == (expected,)
    with pytest.raises(XkcdLexicalFloorError, match="same function table"):
        replay_xkcd_lexical_floor(floor, corpus)
    with pytest.raises(XkcdLexicalFloorError, match="plans require an explicit function table"):
        reconstruct_xkcd_lexical_floor(source, corpus, None, (plan,))
