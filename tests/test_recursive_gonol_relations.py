# === CHECKS ===
# id: recursive_gonol_candidate_check
#   proves: recursive_gonol_is_declared_candidate
#   call: self::test_recursive_gonol_is_declared_candidate
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: recursive_gonol_closed_participant_check
#   proves: recursive_gonol_preserves_closed_lower_gonols, recursive_gonol_refuses_invented_pairing
#   call: self::test_recursive_gonol_preserves_closed_lower_gonols
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: recursive_gonol_source_relation_check
#   proves: recursive_gonol_binds_each_source_relation
#   call: self::test_recursive_gonol_binds_each_source_relation
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: recursive_gonol_replay_check
#   proves: recursive_gonol_layer_replays_byte_exactly
#   call: self::test_recursive_gonol_layer_replays
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: recursive_gonol_definition_evidence_check
#   proves: recursive_gonol_layer_replays_byte_exactly
#   call: self::test_recursive_gonol_rejects_counterfeit_definition_layer
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: recursive_gonol_child_binding_check
#   proves: recursive_gonol_preserves_closed_lower_gonols
#   call: self::test_recursive_gonol_rejects_child_evidence_drift
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: recursive_gonol_synset_member_check
#   proves: recursive_gonol_preserves_closed_lower_gonols
#   call: self::test_recursive_gonol_does_not_resolve_members_from_gloss_inscriptions
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: recursive_gonol_code_reference_check
#   proves: recursive_gonol_layer_replays_byte_exactly
#   call: self::test_recursive_gonol_receipt_binds_producer_code_reference
#   requires: python3
#   timeout: 20
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.oewn_core import OEWNCoreSnapshot, OEWNLexicalEntry, OEWNSense, OEWNSynset
from ucns.oewn_definition_recursion import build_oewn_definition_layer
from ucns.recursive_gonol_relations import (
    DEFINITION_PARTICIPANT_KIND,
    RECURSIVE_GONOL_CONSTRUCTOR_ID,
    RECURSIVE_GONOL_STANDING,
    WORD_PARTICIPANT_KIND,
    RecursiveGonolError,
    build_source_native_recursive_gonols,
    recursive_gonol_layer_bytes,
    replay_source_native_recursive_gonols,
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


def test_recursive_gonol_is_declared_candidate() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    recursive = build_source_native_recursive_gonols(snapshot, layer)
    assert recursive.constructor_id == RECURSIVE_GONOL_CONSTRUCTOR_ID
    assert recursive.selected is False
    assert recursive.native_relation_mechanism_selected is False
    assert recursive.standing == RECURSIVE_GONOL_STANDING
    with pytest.raises(RecursiveGonolError, match="cannot be promoted"):
        replace(recursive, selected=True)
    with pytest.raises(RecursiveGonolError, match="standing"):
        replace(recursive, standing="selected-recursive-gonol-canon")


def test_recursive_gonol_preserves_closed_lower_gonols() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    recursive = build_source_native_recursive_gonols(snapshot, layer)
    closed_words = {gonol_id for _text, gonol_id in layer.closed_word_pairs}
    closed_words.update(item.gonol_id for item in layer.inscriptions)
    closed_words.update(item.gonol_id for item in layer.composite_words)
    closed_definitions = {item.gonol_id for item in layer.definition_gonols}
    dont_id = dict(layer.closed_word_pairs)["don't"]
    for gonol in recursive.gonols:
        assert gonol.participants
        for participant in gonol.participants:
            if participant.kind == WORD_PARTICIPANT_KIND:
                assert participant.gonol_id in closed_words
            else:
                assert participant.kind == DEFINITION_PARTICIPANT_KIND
                assert participant.gonol_id in closed_definitions
    assert all(
        dont_id not in {item.gonol_id for item in gonol.participants}
        for gonol in recursive.gonols
    )
    antonym = recursive.gonols[0]
    assert antonym.relation_label == "antonym"
    kinds = [item.kind for item in antonym.participants]
    assert kinds.count(DEFINITION_PARTICIPANT_KIND) == 3
    assert kinds[0] == WORD_PARTICIPANT_KIND
    assert len(antonym.participants) == 5


def test_recursive_gonol_binds_each_source_relation() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    recursive = build_source_native_recursive_gonols(snapshot, layer)
    assert len(recursive.gonols) == snapshot.relation_occurrence_count == 2
    assert [item.relation_label for item in recursive.gonols] == ["antonym", "hypernym"]
    assert [item.address_kind for item in recursive.gonols] == ["sense", "synset"]
    assert recursive.gonols[0].source_address == "branch%1"
    assert recursive.gonols[0].target_address == "root%1"
    assert recursive.gonols[1].source_address == "s1"
    assert recursive.gonols[1].target_address == "s2"
    missing = OEWNCoreSnapshot(
        snapshot.source_receipt_id,
        snapshot.lexical_entries,
        (
            replace(snapshot.synsets[0], relations=(("hypernym", ("absent",)),)),
            *snapshot.synsets[1:],
        ),
    )
    with pytest.raises(RecursiveGonolError, match="absent synset"):
        build_source_native_recursive_gonols(missing, layer)


def test_recursive_gonol_layer_replays() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    recursive = build_source_native_recursive_gonols(snapshot, layer)
    replayed = replay_source_native_recursive_gonols(recursive, snapshot, layer)
    assert recursive_gonol_layer_bytes(replayed) == recursive_gonol_layer_bytes(recursive)
    with pytest.raises(RecursiveGonolError, match="does not match source"):
        replace(recursive, source_native_relation_occurrence_count=99)
    changed = replace(recursive.gonols[0], relation_label="counterfeit-label")
    counterfeit = replace(recursive, gonols=(changed, *recursive.gonols[1:]))
    with pytest.raises(RecursiveGonolError, match="replay mismatch"):
        replay_source_native_recursive_gonols(counterfeit, snapshot, layer)


def test_recursive_gonol_rejects_counterfeit_definition_layer() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    counterfeit = replace(layer, source_definition_count=layer.source_definition_count + 1)
    assert counterfeit.source_receipt_id == snapshot.source_receipt_id
    with pytest.raises(RecursiveGonolError, match="deterministic snapshot replay"):
        build_source_native_recursive_gonols(snapshot, counterfeit)


def test_recursive_gonol_rejects_child_evidence_drift() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    recursive = build_source_native_recursive_gonols(snapshot, layer)
    rebound_source = replace(
        recursive.gonols[0],
        source_receipt_id=recursive.source_receipt_id + "x",
    )
    with pytest.raises(RecursiveGonolError, match="evidence bindings"):
        replace(recursive, gonols=(rebound_source, *recursive.gonols[1:]))
    rebound_layer = replace(
        recursive.gonols[0],
        definition_layer_id=recursive.definition_layer_id + "x",
    )
    with pytest.raises(RecursiveGonolError, match="evidence bindings"):
        replace(recursive, gonols=(rebound_layer, *recursive.gonols[1:]))


def test_recursive_gonol_does_not_resolve_members_from_gloss_inscriptions() -> None:
    snapshot = _snapshot()
    orphan = OEWNCoreSnapshot(
        snapshot.source_receipt_id,
        snapshot.lexical_entries,
        (
            replace(snapshot.synsets[0], members=("ghost",), definitions=("a ghost",)),
            *snapshot.synsets[1:],
        ),
    )
    layer = build_oewn_definition_layer(orphan)
    assert any(item.text == "ghost" for item in layer.inscriptions)
    assert "ghost" not in dict(layer.closed_word_pairs)
    with pytest.raises(RecursiveGonolError, match="unresolved closed-word participant 'ghost'"):
        build_source_native_recursive_gonols(orphan, layer)


def test_recursive_gonol_receipt_binds_producer_code_reference() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    recursive = build_source_native_recursive_gonols(snapshot, layer)
    assert recursive.producer_code_reference.startswith("ucns.python-source-normalized-sha256:")
    assert b'"producer_code_reference":' in recursive_gonol_layer_bytes(recursive)
    with pytest.raises(RecursiveGonolError, match="producer code reference"):
        replace(
            recursive,
            producer_code_reference="ucns.python-source-normalized-sha256:" + "0" * 64,
        )
