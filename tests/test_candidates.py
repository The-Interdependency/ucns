# === CHECKS ===
# id: check_candidate_family_coexistence
#   proves: first_candidate_families_coexist_without_selection
#   call: self::test_candidate_family_coexistence
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_cell_candidate_scope_failure
#   proves: cell_only_candidates_fail_outside_scope
#   call: self::test_cell_candidate_scope_failure
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_initial_product_multiplicativity
#   proves: initial_product_candidates_multiply_under_actual_pairing
#   call: self::test_initial_product_multiplicativity
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_candidate_nonpromotion
#   proves: candidate_constructors_do_not_promote_canon
#   call: self::test_candidate_nonpromotion
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import pytest

from ucns import (
    STRUCTURAL_NULL,
    CandidateScopeError,
    Carrier,
    Cell,
    EvaluatorKind,
    LawSuite,
    RetainedLayer,
    RetainedStructure,
    cell_log_support_breadth_candidate,
    combined_comparison_policy,
    finite_nonnegative_law,
    geometric_mean_product_candidate,
    maximum_support_product_candidate,
    minimum_support_product_candidate,
    null_zero_law,
    pair_multiplicative_law,
    retained_presence_breadth_candidate,
)


def carriers():
    return (
        Carrier(
            (
                Cell(coordinate="a", mu=2.0),
                Cell(coordinate="b", mu=8.0),
            )
        ),
        Carrier(
            (
                Cell(coordinate="c", mu=3.0),
                Cell(coordinate="d", mu=12.0),
            )
        ),
    )


def test_candidate_family_coexistence() -> None:
    candidates = (
        geometric_mean_product_candidate(),
        maximum_support_product_candidate(),
        minimum_support_product_candidate(),
        cell_log_support_breadth_candidate(),
        retained_presence_breadth_candidate(),
    )
    assert len({candidate.name for candidate in candidates}) == len(
        candidates
    )
    assert all(
        candidate.version
        and candidate.code_reference
        and candidate.scope
        for candidate in candidates
    )


def test_cell_candidate_scope_failure() -> None:
    receipt_only = RetainedStructure(
        STRUCTURAL_NULL,
        (RetainedLayer("receipt", "r"),),
    )
    with pytest.raises(CandidateScopeError):
        cell_log_support_breadth_candidate().evaluate(receipt_only)
    assert retained_presence_breadth_candidate().evaluate(
        receipt_only
    ) > 0.0


def test_initial_product_multiplicativity() -> None:
    left, right = carriers()
    comparison = combined_comparison_policy(
        rel_tol=1e-12, abs_tol=1e-12
    )
    for candidate in (
        geometric_mean_product_candidate(),
        maximum_support_product_candidate(),
        minimum_support_product_candidate(),
    ):
        suite = LawSuite(
            f"{candidate.name}-laws",
            (
                null_zero_law(),
                finite_nonnegative_law((left, right)),
                pair_multiplicative_law(((left, right),)),
            ),
            comparison,
        )
        assert suite.evaluate(candidate).all_passed


def test_candidate_nonpromotion() -> None:
    candidate = geometric_mean_product_candidate()
    assert candidate.kind is EvaluatorKind.PRODUCT_CHARACTER
    assert not hasattr(candidate, "canonical")
    assert not hasattr(candidate, "winner")
