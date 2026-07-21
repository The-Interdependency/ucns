# === CHECKS ===
# id: check_recursive_cycle_modes
#   proves: recursive_cycles_require_explicit_policy
#   call: self::test_recursive_cycle_modes
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

    fixed = traverse(
        "a",
        children=lambda node: GRAPH[node],
        identity=lambda node: node,
        policy=TraversalPolicy(
            "fixed",
            CycleMode.FIXED_POINT,
            fixed_point_resolver=lambda node, path: (node, path),
        ),
    )
    assert fixed.fixed_points


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


def test_fixed_point_requires_resolver() -> None:
    with pytest.raises(ValueError):
        TraversalPolicy("fixed", CycleMode.FIXED_POINT)
