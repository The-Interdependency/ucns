# === CHECKS ===
# id: check_recursive_cycle_modes
#   proves: recursive_cycles_require_explicit_policy
#   call: self::test_recursive_cycle_modes
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_shared_identity_reference
#   proves: shared_identity_references_are_retained
#   call: self::test_shared_identity_reference
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_traversal_budget_receipts
#   proves: traversal_budgets_emit_receipts
#   call: self::test_traversal_budget_receipts
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_fixed_point_requires_resolver
#   proves: fixed_point_traversal_requires_resolver
#   call: self::test_fixed_point_requires_resolver
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import pytest

from ucns import (
    CycleDetectedError,
    CycleMode,
    TraversalBudget,
    TraversalPolicy,
    traverse,
)


GRAPH = {"a": ("b",), "b": ("a",)}


def test_recursive_cycle_modes() -> None:
    with pytest.raises(CycleDetectedError):
        traverse(
            "a",
            children=lambda node: GRAPH[node],
            identity=lambda node: node,
            policy=TraversalPolicy("reject", CycleMode.REJECT),
        )

    referenced = traverse(
        "a",
        children=lambda node: GRAPH[node],
        identity=lambda node: node,
        policy=TraversalPolicy("reference", CycleMode.REFERENCE),
    )
    assert len(referenced.references) == 1
    assert referenced.references[0].first_path == ("a",)
    assert referenced.references[0].repeated_path == ("a", "b", "a")

    fixed = traverse(
        "a",
        children=lambda node: GRAPH[node],
        identity=lambda node: node,
        policy=TraversalPolicy(
            "fixed",
            CycleMode.FIXED_POINT,
            fixed_point_resolver=lambda node, path: (node, path),
            resolver_reference="tests.test_traversal:fixed-resolver",
        ),
    )
    assert fixed.fixed_points


def test_shared_identity_reference() -> None:
    shared_graph = {
        "root": ("left", "right"),
        "left": ("shared",),
        "right": ("shared",),
        "shared": (),
    }
    result = traverse(
        "root",
        children=lambda node: shared_graph[node],
        identity=lambda node: node,
        policy=TraversalPolicy("reference", CycleMode.REFERENCE),
    )
    assert tuple(visit.identity for visit in result.visits).count("shared") == 1
    assert len(result.references) == 1
    assert result.references[0].identity == "shared"
    assert result.references[0].first_path == ("root", "left", "shared")


def test_traversal_budget_receipts() -> None:
    unfolded = traverse(
        "a",
        children=lambda node: GRAPH[node],
        identity=lambda node: node,
        policy=TraversalPolicy(
            "depth",
            CycleMode.UNFOLD_TO_DEPTH,
            TraversalBudget(max_depth=2, max_nodes=10),
        ),
    )
    assert unfolded.truncations
    assert not unfolded.complete

    pulled: list[int] = []

    def children(node):
        if node != "root":
            return ()

        def stream():
            index = 0
            while True:
                pulled.append(index)
                yield f"child-{index}"
                index += 1

        return stream()

    bounded = traverse(
        "root",
        children=children,
        identity=lambda node: node,
        policy=TraversalPolicy(
            "node-budget",
            CycleMode.REJECT,
            TraversalBudget(max_depth=5, max_nodes=2),
        ),
    )
    assert pulled == [0]
    assert any(
        receipt.reason == "max-nodes-children"
        for receipt in bounded.truncations
    )


def test_fixed_point_requires_resolver() -> None:
    with pytest.raises(ValueError):
        TraversalPolicy("fixed", CycleMode.FIXED_POINT)
    with pytest.raises(ValueError):
        TraversalPolicy(
            "fixed",
            CycleMode.FIXED_POINT,
            fixed_point_resolver=lambda node, path: node,
        )
