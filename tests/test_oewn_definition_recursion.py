# === CHECKS ===
# id: oewn_definition_complete_fixture_check
#   proves: oewn_definition_scope_is_complete, oewn_definition_relationships_enter_gonols, oewn_morphology_uses_only_explicit_source_forms, oewn_definition_fixed_point_is_source_exhaustion
#   call: self::test_complete_fixture_preserves_source_and_intrinsic_relations
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: oewn_definition_function_participant_check
#   proves: oewn_functions_are_not_absorbed_into_inscriptions, oewn_function_occurrence_matches_source_glyph
#   call: self::test_public_gonol_functions_are_not_absorbed_into_inscriptions
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: oewn_definition_closed_word_check
#   proves: oewn_preserves_closed_word_gonols
#   call: self::test_definition_preserves_closed_word_gonols
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: oewn_definition_exact_replay_check
#   proves: oewn_definition_layer_replays_byte_exactly
#   call: self::test_replay_is_byte_exact_and_tamper_fails
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.oewn_core import OEWNCoreSnapshot, OEWNLexicalEntry, OEWNSense, OEWNSynset
from ucns.public_gonol_functions import FUNCTIONAL_INDEX_NAMES
from ucns.oewn_definition_recursion import (
    CLOSED_WORD_KIND,
    FUNCTION_KIND,
    INSCRIPTION_KIND,
    OEWNDefinitionOccurrence,
    OEWNDefinitionRecursionError,
    OEWNInscriptionGonol,
    build_oewn_definition_layer,
    definition_layer_bytes,
    replay_oewn_definition_layer,
)


def _snapshot() -> OEWNCoreSnapshot:
    receipt = "ucns.oewn-core-receipt:sha256:" + "1" * 64
    return OEWNCoreSnapshot(
        receipt,
        (
            OEWNLexicalEntry("branch", "n", ("branches",), (
                OEWNSense("branch%1", "s1", (("antonym", ("root%1",)),), (), None),
            )),
            OEWNLexicalEntry("root", "n", (), (
                OEWNSense("root%1", "s2", (), (), None),
            )),
            OEWNLexicalEntry("don't", "v", (), (
                OEWNSense("dont%1", "s3", (), (), None),
            )),
        ),
        (
            OEWNSynset("s1", "n", ("branch",), ("a part  of a tree",), (("hypernym", ("s2",)),)),
            OEWNSynset("s2", "n", ("root",), ("part under earth", "source of a branch"), ()),
            OEWNSynset("s3", "v", ("don't",), ("don't cut.",), ()),
        ),
    )


def test_complete_fixture_preserves_source_and_intrinsic_relations() -> None:
    layer = build_oewn_definition_layer(_snapshot())
    assert len(layer.morphology_gonols) == 1
    assert len(layer.definition_gonols) == 4
    assert layer.source_native_relation_occurrence_count == 2
    assert layer.native_relation_mechanism_selected is False
    assert layer.final_morphology_law_selected is False
    assert layer.new_identities_on_final_pass == 0
    first = layer.definition_gonols[0]
    assert first.exact_gloss == "a part  of a tree"
    assert [first.exact_gloss[x.start:x.end] for x in first.occurrences] == ["a", "part", "of", "a", "tree"]
    assert first.exact_space_boundaries == ((1, 2, " "), (6, 8, "  "), (10, 11, " "), (12, 13, " "))
    assert [edge.relation for edge in first.carrier.edges] == [0, 0, 0, 0, 0]
    assert len({x.inscription_gonol_id for x in first.occurrences}) == 4
    aliased = OEWNDefinitionOccurrence(
        first.occurrences[0].ordinal,
        first.occurrences[0].start,
        first.occurrences[0].end,
        inscription_gonol_id=first.occurrences[0].participant_id,
        kind=first.occurrences[0].kind,
    )
    assert aliased.participant_id == first.occurrences[0].participant_id
    bogus = replace(first.occurrences[0], participant_id="bogus")
    tampered = replace(first, occurrences=(bogus,) + first.occurrences[1:])
    with pytest.raises(OEWNDefinitionRecursionError, match="not in the layer inventory"):
        replace(layer, definition_gonols=(tampered,) + layer.definition_gonols[1:])


def test_replay_is_byte_exact_and_tamper_fails() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    assert definition_layer_bytes(replay_oewn_definition_layer(layer, snapshot)) == definition_layer_bytes(layer)
    tampered = replace(layer, source_definition_count=99)
    with pytest.raises(OEWNDefinitionRecursionError, match="replay mismatch"):
        replay_oewn_definition_layer(tampered, snapshot)


def test_public_gonol_functions_are_not_absorbed_into_inscriptions() -> None:
    layer = build_oewn_definition_layer(_snapshot())
    punctuated = next(item for item in layer.definition_gonols if item.exact_gloss == "don't cut.")
    texts = [punctuated.exact_gloss[item.start:item.end] for item in punctuated.occurrences]
    assert texts == ["don't", "cut", "."]
    assert [item.kind for item in punctuated.occurrences] == [
        CLOSED_WORD_KIND, INSCRIPTION_KIND, FUNCTION_KIND,
    ]
    period = punctuated.occurrences[-1]
    assert period.kind == FUNCTION_KIND
    period_index = next(index for index, glyph, _ in FUNCTIONAL_INDEX_NAMES if glyph == ".")
    assert period.public_gonol_index == period_index
    assert punctuated.exact_gloss[period.start:period.end] == "."
    assert all("'" not in item.text and "." not in item.text for item in layer.inscriptions)
    lemma_id = dict(layer.closed_word_pairs)["don't"]
    assert punctuated.occurrences[0].participant_id == lemma_id
    mismatched = replace(period, public_gonol_index=0)
    with pytest.raises(OEWNDefinitionRecursionError, match="does not match the source glyph"):
        replace(punctuated, occurrences=punctuated.occurrences[:-1] + (mismatched,))
    with pytest.raises(OEWNDefinitionRecursionError, match="Public Gonol function"):
        OEWNInscriptionGonol(
            "don't",
            "ucns.oewn-core-receipt:sha256:" + "1" * 64,
            tuple((ord(ch), None) for ch in "don't"),
        )


def test_definition_preserves_closed_word_gonols() -> None:
    layer = build_oewn_definition_layer(_snapshot())
    punctuated = next(item for item in layer.definition_gonols if item.exact_gloss == "don't cut.")
    lemma_id = dict(layer.closed_word_pairs)["don't"]
    assert punctuated.occurrences[0].kind == CLOSED_WORD_KIND
    assert punctuated.occurrences[0].participant_id == lemma_id
    receipt = "ucns.oewn-core-receipt:sha256:" + "3" * 64
    snapshot = OEWNCoreSnapshot(
        receipt,
        (
            OEWNLexicalEntry("a", "n", (), (OEWNSense("a%1", "s1", (), (), None),)),
        ),
        (
            OEWNSynset("s1", "n", ("a",), ("about one.",), ()),
        ),
    )
    prefix_layer = build_oewn_definition_layer(snapshot)
    about = next(item for item in prefix_layer.definition_gonols if item.exact_gloss == "about one.")
    texts = [about.exact_gloss[item.start:item.end] for item in about.occurrences]
    assert texts == ["about", "one", "."]
    assert [item.kind for item in about.occurrences] == [
        INSCRIPTION_KIND, INSCRIPTION_KIND, FUNCTION_KIND,
    ]
    closed = dict(prefix_layer.closed_word_pairs)
    about_word = next(item for item in prefix_layer.inscriptions if item.text == "about")
    assert about.occurrences[0].participant_id == about_word.gonol_id
    assert about.occurrences[0].participant_id != closed["a"]
    suffix = OEWNCoreSnapshot(
        "ucns.oewn-core-receipt:sha256:" + "4" * 64,
        (
            OEWNLexicalEntry("a", "n", (), (OEWNSense("a%1", "s1", (), (), None),)),
            OEWNLexicalEntry("out", "r", (), (OEWNSense("out%1", "s2", (), (), None),)),
        ),
        (
            OEWNSynset("s1", "n", ("a",), ("about outside.",), ()),
            OEWNSynset("s2", "r", ("out",), ("without one.",), ()),
        ),
    )
    suffix_layer = build_oewn_definition_layer(suffix)
    about_out = next(item for item in suffix_layer.definition_gonols if item.exact_gloss == "about outside.")
    without = next(item for item in suffix_layer.definition_gonols if item.exact_gloss == "without one.")
    assert [about_out.exact_gloss[item.start:item.end] for item in about_out.occurrences] == [
        "about", "outside", ".",
    ]
    assert [without.exact_gloss[item.start:item.end] for item in without.occurrences] == [
        "without", "one", ".",
    ]
    assert [item.kind for item in about_out.occurrences] == [
        INSCRIPTION_KIND, INSCRIPTION_KIND, FUNCTION_KIND,
    ]
    assert [item.kind for item in without.occurrences] == [
        INSCRIPTION_KIND, INSCRIPTION_KIND, FUNCTION_KIND,
    ]
    out_id = dict(suffix_layer.closed_word_pairs)["out"]
    assert about_out.occurrences[0].participant_id != out_id
    assert without.occurrences[0].participant_id != out_id
