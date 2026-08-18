# === CHECKS ===
# id: lexical_definition_gonol_closure_check
#   proves: floor_definition_support_is_closed, floor_definition_order_multiplicity_and_sense_are_exact, definition_gonols_are_first_recursion_not_measurement
#   call: self::test_floor_definition_gonol_is_closed_ordered_and_replayable
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: complete_lexical_definition_layer_check
#   proves: complete_definition_layer_covers_every_floor_gonol
#   call: self::test_complete_layer_requires_and_covers_every_packaged_floor_gonol
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: lexical_definition_identity_substitution_check
#   proves: floor_definition_support_is_closed, floor_definition_order_multiplicity_and_sense_are_exact
#   call: self::test_source_and_evidence_identity_substitution_fail_closed
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from hashlib import sha256

import pytest

from ucns.lexical_definition_gonols import (
    DEFINITION_GONOL_STANDING,
    DefinitionSourceReceipt,
    FloorDefinitionEvidence,
    LexicalDefinitionError,
    build_complete_definition_layer,
    build_floor_definition_gonol,
    definition_layer_receipt_bytes,
)
from ucns.lexical_floor import (
    create_hyperspace_potential,
    create_word_gonols,
    load_ngsl_source_receipt,
    load_ngsl_words,
)


def _source(record_count: int) -> DefinitionSourceReceipt:
    return DefinitionSourceReceipt(
        source_identity="fixture:defining-relations",
        source_version="1",
        license_identity="fixture-only",
        content_sha256=sha256(b"fixture:defining-relations:v1").hexdigest(),
        record_count=record_count,
        provenance="test-authored exact resolved gonol identities",
    )


def _fixture_floor():
    words = load_ngsl_words()
    gonols = create_word_gonols(words)
    return create_hyperspace_potential(gonols), load_ngsl_source_receipt()


def test_floor_definition_gonol_is_closed_ordered_and_replayable() -> None:
    potential, floor_receipt = _fixture_floor()
    target = potential.gonol("kind").gonol_id
    constituent = potential.gonol("good").gonol_id
    evidence = FloorDefinitionEvidence(
        target_gonol_id=target,
        sense_identity="kind:fixture-sense-1",
        context_identity="fixture-context",
        source_record_identity="fixture-record-1",
        source_text_sha256=sha256(b"good good").hexdigest(),
        constituent_gonol_ids=(constituent, constituent),
    )
    gonol = build_floor_definition_gonol(
        potential, floor_receipt, _source(1), evidence
    )
    assert [item.position for item in gonol.occurrences] == [0, 1]
    assert [item.constituent_gonol_id for item in gonol.occurrences] == [constituent, constituent]
    assert [(edge.source, edge.relation, edge.target) for edge in gonol.carrier.edges] == [
        (0, 0, 1), (0, 0, 2),
    ]
    assert gonol.geometry_attached is False and gonol.measurement_attached is False
    assert gonol.gonol_id == build_floor_definition_gonol(
        potential, floor_receipt, _source(1), evidence
    ).gonol_id
    reordered = replace(evidence, constituent_gonol_ids=(target, constituent))
    assert build_floor_definition_gonol(
        potential, floor_receipt, _source(1), reordered
    ).gonol_id != gonol.gonol_id
    with pytest.raises(LexicalDefinitionError, match="outside the fixed lexical floor"):
        build_floor_definition_gonol(
            potential, floor_receipt, _source(1),
            replace(evidence, constituent_gonol_ids=("word-gonol:sha256:" + "0" * 64,)),
        )
    with pytest.raises(LexicalDefinitionError, match="standing"):
        replace(gonol, standing="canonical")


def test_complete_layer_requires_and_covers_every_packaged_floor_gonol() -> None:
    potential, floor_receipt = _fixture_floor()
    evidence = tuple(
        FloorDefinitionEvidence(
            target_gonol_id=gonol.gonol_id,
            sense_identity=f"self:{index}",
            context_identity="complete-fixture-context",
            source_record_identity=f"fixture:{index}",
            source_text_sha256=sha256(gonol.word.encode("utf-8")).hexdigest(),
            constituent_gonol_ids=(gonol.gonol_id,),
        )
        for index, gonol in enumerate(potential.word_gonols)
    )
    receipt = build_complete_definition_layer(
        potential, floor_receipt, _source(len(evidence)), evidence
    )
    assert receipt.floor_gonol_count == len(evidence) == 2809
    assert len(receipt.covered_target_gonol_ids) == 2809
    assert len(receipt.definition_gonol_ids) == 2809
    assert definition_layer_receipt_bytes(receipt).endswith(b"\n")
    assert receipt.receipt_id.startswith("ucns.definition-layer-receipt:sha256:")
    with pytest.raises(LexicalDefinitionError, match="missing floor targets"):
        build_complete_definition_layer(
            potential, floor_receipt, _source(len(evidence) - 1), evidence[:-1]
        )
    with pytest.raises(LexicalDefinitionError, match="record count"):
        build_complete_definition_layer(
            potential, floor_receipt, _source(len(evidence) - 1), evidence
        )


def test_source_and_evidence_identity_substitution_fail_closed() -> None:
    with pytest.raises(LexicalDefinitionError, match="digest"):
        DefinitionSourceReceipt("source", "1", "license", "x", 1, "provenance")
    with pytest.raises(LexicalDefinitionError, match="ordered constituents"):
        FloorDefinitionEvidence(
            "target", "sense", "context", "record", "0" * 64, ()
        )
