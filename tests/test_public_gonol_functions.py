# === CHECKS ===
# id: public_gonol_function_table_exact_index_check
#   proves: public_gonol_indices_are_function_table_authority, public_gonol_functions_are_definition_bound
#   call: self::test_every_functional_index_is_definition_bound_without_parallel_grammar
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: public_gonol_contextual_function_application_check
#   proves: public_gonol_function_application_is_contextual_closure, public_gonol_function_table_replays_exactly
#   call: self::test_contextual_application_closes_and_replays
#   timeout: 20
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.oewn_core import OEWNCoreSnapshot, OEWNLexicalEntry, OEWNSense, OEWNSynset
from ucns.oewn_definition_recursion import build_oewn_definition_layer
from ucns.public_gonol_functions import (
    AtomicFunctionState,
    FUNCTIONAL_INDEX_NAMES,
    PublicGonolFunctionError,
    apply_public_gonol_function,
    build_public_gonol_function_table,
    function_table_bytes,
)


def _snapshot() -> OEWNCoreSnapshot:
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
    return OEWNCoreSnapshot(receipt, tuple(entries), tuple(synsets))


def test_every_functional_index_is_definition_bound_without_parallel_grammar() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    table = build_public_gonol_function_table(snapshot, layer)
    assert len(table.functions) == len(FUNCTIONAL_INDEX_NAMES)
    assert tuple(item.public_gonol_index for item in table.functions) == tuple(
        item[0] for item in FUNCTIONAL_INDEX_NAMES
    )
    assert all(item.bindings for item in table.functions)
    assert not any(item.independent_punctuation_grammar_attached for item in table.functions)
    assert table.canonical_key == "public-gonol-index"


def test_contextual_application_closes_and_replays() -> None:
    snapshot = _snapshot()
    layer = build_oewn_definition_layer(snapshot)
    first = build_public_gonol_function_table(snapshot, layer)
    second = build_public_gonol_function_table(snapshot, layer)
    assert function_table_bytes(first) == function_table_bytes(second)
    state = AtomicFunctionState("ucns.atomic-word-gonol:sha256:" + "a" * 64)
    application = apply_public_gonol_function(
        first, FUNCTIONAL_INDEX_NAMES[0][0], state,
        ("ucns.atomic-word-gonol:sha256:" + "b" * 64,),
    )
    replay = apply_public_gonol_function(
        second, FUNCTIONAL_INDEX_NAMES[0][0], state,
        ("ucns.atomic-word-gonol:sha256:" + "b" * 64,),
    )
    assert application == replay
    assert application.next_state.application_depth == 1
    assert application.next_state.atomic_gonol_id == application.result_atomic_gonol_id
    with pytest.raises(PublicGonolFunctionError, match="not a bound"):
        apply_public_gonol_function(first, 14, state)
    with pytest.raises(PublicGonolFunctionError, match="canonical index"):
        replace(first.functions[0], public_gonol_index=14)
