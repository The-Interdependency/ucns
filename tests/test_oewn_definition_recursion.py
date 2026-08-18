# === CHECKS ===
# id: oewn_definition_complete_fixture_check
#   proves: oewn_definition_scope_is_complete, oewn_definition_relationships_enter_gonols, oewn_morphology_uses_only_explicit_source_forms, oewn_definition_fixed_point_is_source_exhaustion
#   call: self::test_complete_fixture_preserves_source_and_intrinsic_relations
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: oewn_definition_exact_replay_check
#   proves: oewn_definition_layer_replays_byte_exactly
#   call: self::test_replay_is_byte_exact_and_tamper_fails
#   timeout: 20
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.oewn_core import OEWNCoreSnapshot, OEWNLexicalEntry, OEWNSense, OEWNSynset
from ucns.oewn_definition_recursion import (
    OEWNDefinitionRecursionError,
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
        ),
        (
            OEWNSynset("s1", "n", ("branch",), ("a part  of a tree",), (("hypernym", ("s2",)),)),
            OEWNSynset("s2", "n", ("root",), ("part under earth", "source of a branch"), ()),
        ),
    )


def test_complete_fixture_preserves_source_and_intrinsic_relations() -> None:
    layer = build_oewn_definition_layer(_snapshot())
    assert len(layer.morphology_gonols) == 1
    assert len(layer.definition_gonols) == 3
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


def test_replay_is_byte_exact_and_tamper_fails() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    assert definition_layer_bytes(replay_oewn_definition_layer(layer, snapshot)) == definition_layer_bytes(layer)
    tampered = replace(layer, source_definition_count=99)
    with pytest.raises(OEWNDefinitionRecursionError, match="replay mismatch"):
        replay_oewn_definition_layer(tampered, snapshot)
