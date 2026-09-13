# === CHECKS ===
# id: check_singleton_axis_admits_exactly_once
#   proves: singleton_axis_admits_exactly_one_record_per_identity
#   call: self::test_singleton_axis_admits_exactly_once
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_occurrence_ledger_ordinal_provenance
#   proves: occurrence_records_are_ordinal_and_provenance_bearing
#   call: self::test_occurrence_ledger_records_ordinal_provenance
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_closure_graph_detects_cycles
#   proves: closure_graph_is_finite_and_deterministic
#   call: self::test_closure_graph_detects_self_loop_and_two_cycle
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_closure_graph_deterministic
#   proves: closure_graph_is_finite_and_deterministic
#   call: self::test_closure_graph_is_deterministic_and_edge_sorted
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_closure_graph_rejects_empty_identity
#   proves: closure_graph_is_finite_and_deterministic
#   call: self::test_closure_graph_rejects_empty_identity
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_unit_circle_relation_exact_turns
#   proves: unit_circle_relation_positions_are_exact_turns
#   call: self::test_unit_circle_relation_exact_positions_and_density
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_unit_circle_relation_rejects_bad_residue
#   proves: unit_circle_relation_positions_are_exact_turns
#   call: self::test_unit_circle_relation_rejects_out_of_range_residue
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_tangency_exact_when_declared
#   proves: tangency_never_invents_undeclared_geometry
#   call: self::test_tangency_is_exact_when_geometry_is_declared
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_tangency_hmmm_when_undeclared
#   proves: tangency_never_invents_undeclared_geometry
#   call: self::test_tangency_is_hmmm_without_declared_geometry
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_mobius_frame_return_law
#   proves: mobius_frame_preserves_native_return_law
#   call: self::test_mobius_frame_preserves_native_return_law
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_construct_canonical_replay
#   proves: singleton_construct_serializes_canonically_and_replays_byte_identically
#   call: self::test_construct_serializes_canonically_and_replays_byte_identically
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_construct_canonical_axis_order
#   proves: singleton_construct_serializes_canonically_and_replays_byte_identically
#   call: self::test_construct_builder_axis_order_is_canonical
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_facade_exports_singleton_geometry
#   proves: geometry_public_surface_includes_singleton_axis_geometry
#   call: self::test_facade_exports_singleton_geometry
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from fractions import Fraction

import pytest

from ucns.singleton_geometry import (
    SCHEMA,
    VERSION,
    SingletonGeometryError,
    SingletonAxis,
    OccurrenceLedger,
    ClosureEdge,
    ClosureGraph,
    UnitCircleRelation,
    TangencyRecord,
    relation_tangency,
    AttentionFrame,
    MobiusFrameRecord,
    build_mobius_frame,
    advance_mobius_frame,
    SingletonConstructBuilder,
)
from ucns.direct_mobius import NativeMobiusFrame


def test_singleton_axis_admits_exactly_once() -> None:
    axis = SingletonAxis("character")
    first = axis.admit("a")
    again = axis.admit("a")
    second = axis.admit("b")

    assert first is again
    assert first.ordinal == 0
    assert second.ordinal == 1
    assert len(axis) == 2
    assert axis.singleton("a") is first
    assert axis.singleton("missing") is None
    assert [record.identity for record in axis.records] == ["a", "b"]


def test_occurrence_ledger_records_ordinal_provenance() -> None:
    ledger = OccurrenceLedger()
    first = ledger.record("character", "a", ("corpus", "sentence-1", "offset-0"))
    second = ledger.record("character", "a", ("corpus", "sentence-1", "offset-4"))
    other = ledger.record("word", "cat", ("corpus", "sentence-1"))

    assert first.ordinal == 1
    assert second.ordinal == 2
    assert other.ordinal == 1
    assert first.provenance == ("corpus", "sentence-1", "offset-0")
    assert ledger.occurrence_count("character") == 2
    assert ledger.occurrence_count("word") == 1


def test_closure_graph_detects_self_loop_and_two_cycle() -> None:
    graph = ClosureGraph.build(
        [
            ClosureEdge("word", "w", "reuses", "word", "w"),
            ClosureEdge("word", "a", "follows", "word", "b"),
            ClosureEdge("word", "b", "follows", "word", "a"),
        ]
    )

    assert graph.closed is True
    assert ("word", "w") in graph.cyclic_nodes
    assert ("word", "a") in graph.cyclic_nodes
    assert ("word", "b") in graph.cyclic_nodes
    assert (("word", "w"), ("word", "w")) in graph.cycles
    assert (("word", "a"), ("word", "b"), ("word", "a")) in graph.cycles


def test_closure_graph_is_deterministic_and_edge_sorted() -> None:
    edges = [
        ClosureEdge("z", "z", "r", "a", "a"),
        ClosureEdge("a", "a", "r", "z", "z"),
    ]
    first = ClosureGraph.build(edges)
    second = ClosureGraph.build(reversed(edges))

    assert first.edges == second.edges
    assert first.nodes == second.nodes
    assert first.cycles == second.cycles


def test_closure_graph_rejects_empty_identity() -> None:
    with pytest.raises(SingletonGeometryError):
        ClosureEdge("axis", "", "relation", "axis", "target")


def test_unit_circle_relation_exact_positions_and_density() -> None:
    circle = UnitCircleRelation("word:cat", modulus=157, positions=[5, 9, 5])

    assert circle.positions == (5, 9)
    assert circle.density == Fraction(2, 157)
    assert circle.exact_positions == (Fraction(5, 157), Fraction(9, 157))


def test_unit_circle_relation_rejects_out_of_range_residue() -> None:
    with pytest.raises(SingletonGeometryError):
        UnitCircleRelation("bad", modulus=10, positions=[10])


def test_tangency_is_exact_when_geometry_is_declared() -> None:
    external_a = UnitCircleRelation(
        "a", modulus=10, positions=(0,), center_turns=Fraction(0), radius_turns=Fraction(1, 10)
    )
    external_b = UnitCircleRelation(
        "b", modulus=10, positions=(2,), center_turns=Fraction(2, 10), radius_turns=Fraction(1, 10)
    )
    verdict = relation_tangency(external_a, external_b)
    assert verdict is not None
    assert verdict.status == "external"
    assert verdict.center_distance_turns == Fraction(2, 10)

    internal_a = UnitCircleRelation(
        "inner", modulus=10, positions=(0,), center_turns=Fraction(2, 10), radius_turns=Fraction(1, 10)
    )
    internal_b = UnitCircleRelation(
        "outer", modulus=10, positions=(0,), center_turns=Fraction(4, 10), radius_turns=Fraction(3, 10)
    )
    verdict = relation_tangency(internal_a, internal_b)
    assert verdict is not None
    assert verdict.status == "internal"
    assert verdict.center_distance_turns == Fraction(2, 10)

    not_tangent = UnitCircleRelation(
        "far", modulus=10, positions=(0,), center_turns=Fraction(0), radius_turns=Fraction(1, 10)
    )
    assert relation_tangency(external_a, not_tangent) is None


def test_tangency_is_hmmm_without_declared_geometry() -> None:
    bare_a = UnitCircleRelation("a", modulus=157, positions=(1,))
    bare_b = UnitCircleRelation("b", modulus=157, positions=(2,))

    verdict = relation_tangency(bare_a, bare_b)
    assert verdict is not None
    assert verdict.status == "hmmm"
    assert "undeclared" in verdict.reason


def test_mobius_frame_preserves_native_return_law() -> None:
    record = build_mobius_frame("view-1", "attention-1")

    one_turn = advance_mobius_frame(record, Fraction(1))
    assert one_turn.phase_turns == Fraction(0)
    assert one_turn.frame is NativeMobiusFrame.REVERSED

    two_turns = advance_mobius_frame(record, Fraction(2))
    assert two_turns.phase_turns == Fraction(0)
    assert two_turns.frame is NativeMobiusFrame.POSITIVE


def test_construct_serializes_canonically_and_replays_byte_identically() -> None:
    def build() -> bytes:
        builder = SingletonConstructBuilder(hmmm=["no invented geometry"])
        builder.admit("character", "a")
        builder.admit("character", "b")
        builder.record_occurrence("character", "a", ("corpus", "sentence-1"))
        builder.record_occurrence("character", "a", ("corpus", "sentence-1"))
        builder.add_edge("word", "ab", "reuses", "character", "a")
        builder.add_edge("word", "ab", "reuses", "character", "b")
        builder.add_edge("character", "a", "precedes", "character", "b")
        builder.add_edge("character", "b", "precedes", "character", "a")
        builder.add_relation_circle("word:ab", modulus=157, positions=[1, 2])
        circle_a = UnitCircleRelation(
            "circle:a", modulus=157, positions=(1,), center_turns=Fraction(0), radius_turns=Fraction(1, 157)
        )
        circle_b = UnitCircleRelation(
            "circle:b", modulus=157, positions=(2,), center_turns=Fraction(2, 157), radius_turns=Fraction(1, 157)
        )
        builder.add_relation_circle("circle:a", 157, [1], center_turns=Fraction(0), radius_turns=Fraction(1, 157))
        builder.add_relation_circle("circle:b", 157, [2], center_turns=Fraction(2, 157), radius_turns=Fraction(1, 157))
        verdict = relation_tangency(circle_a, circle_b)
        assert verdict is not None
        builder.add_tangency(verdict)
        builder.add_attention_frame(
            AttentionFrame(
                frame_id="view-1",
                axis_ids=("character", "word"),
                relation_ids=("word:ab",),
                projected_fields=(("coverage", "2/2"),),
                nonclaims=("not a semantic claim",),
            )
        )
        builder.add_mobius_frame(build_mobius_frame("mobius-1", "view-1"))
        construct = builder.build()
        return construct.canonical_bytes(), construct.receipt_sha256()

    first_bytes, first_receipt = build()
    second_bytes, second_receipt = build()

    assert first_bytes == second_bytes
    assert first_receipt == second_receipt
    assert len(first_receipt) == 64


def test_construct_builder_axis_order_is_canonical() -> None:
    builder = SingletonConstructBuilder()
    builder.admit("z-axis", "z")
    builder.admit("a-axis", "a")
    construct = builder.build()

    assert construct.axes[0][0] == "a-axis"
    assert construct.axes[1][0] == "z-axis"
    assert construct.receipt_sha256() != ""


def test_facade_exports_singleton_geometry() -> None:
    import ucns

    for name in (
        "SingletonGeometryError",
        "SingletonRecord",
        "SingletonAxis",
        "OccurrenceRecord",
        "OccurrenceLedger",
        "ClosureEdge",
        "ClosureGraph",
        "UnitCircleRelation",
        "TangencyRecord",
        "relation_tangency",
        "AttentionFrame",
        "MobiusFrameRecord",
        "build_mobius_frame",
        "advance_mobius_frame",
        "SingletonConstruct",
        "SingletonConstructBuilder",
    ):
        assert name in ucns.__all__
