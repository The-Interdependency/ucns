# === CHECKS ===
# id: check_evaluator_registry_choices
#   proves: evaluator_registry_has_no_implicit_winner
#   call: self::test_evaluator_registry_choices
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_evaluator_replacement
#   proves: evaluator_replacement_is_explicit
#   call: self::test_evaluator_replacement
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_evaluator_identity
#   proves: evaluator_candidate_identity_is_explicit
#   call: self::test_evaluator_identity
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_explicit_law_comparison
#   proves: law_suites_require_named_comparison_policy
#   call: self::test_explicit_law_comparison
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_law_suite_evidence
#   proves: law_suites_capture_failures_and_errors
#   call: self::test_law_suite_evidence
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_candidate_comparison
#   proves: candidate_comparison_exposes_disagreement_without_ranking
#   call: self::test_candidate_comparison
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_separation_law_builders
#   proves: law_suites_capture_failures_and_errors
#   call: self::test_separation_law_builders
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import pytest

from ucns import (
    STRUCTURAL_NULL,
    Carrier,
    Cell,
    combined_comparison_policy,
    exact_comparison_policy,
    pair,
    support_weight,
)
from ucns.laboratory import (
    EvaluatorCandidate,
    EvaluatorKind,
    EvaluatorRegistry,
    LawSuite,
    Witness,
    compare_candidates,
    finite_nonnegative_law,
    null_zero_law,
    pair_multiplicative_law,
    same_candidate_different_reference_law,
    same_reference_different_candidate_law,
)


def candidate(name, kind, evaluator):
    return EvaluatorCandidate(
        name,
        kind,
        evaluator,
        version="test-1",
        code_reference=f"tests.test_laboratory:{name}",
        scope="test fixtures",
    )


def _cell_count(subject):
    return 0 if subject is STRUCTURAL_NULL else len(subject.cells)


def test_evaluator_registry_choices() -> None:
    registry = EvaluatorRegistry()
    support = EvaluatorCandidate(
        "cell-support",
        EvaluatorKind.FAITHFUL_BREADTH,
        support_weight,
        policy_dependencies=("ordered-sequence",),
        version="test-1",
        code_reference="tests.test_laboratory:cell-support",
        scope="cell carrier",
    )
    count = candidate(
        "cell-count", EvaluatorKind.FAITHFUL_BREADTH, _cell_count
    )
    registry.register(support)
    registry.register(count)

    assert registry.names(EvaluatorKind.FAITHFUL_BREADTH) == (
        "cell-support",
        "cell-count",
    )
    assert (
        registry.resolve(
            EvaluatorKind.FAITHFUL_BREADTH, "cell-support"
        )
        is support
    )
    assert registry.candidates(EvaluatorKind.FAITHFUL_BREADTH) == (
        support,
        count,
    )
    assert not hasattr(registry, "default")
    assert not hasattr(registry, "best")


def test_evaluator_replacement() -> None:
    registry = EvaluatorRegistry()
    first = candidate(
        "candidate", EvaluatorKind.EQUIVALENCE, lambda value: value
    )
    second = candidate(
        "candidate", EvaluatorKind.EQUIVALENCE, lambda value: not value
    )
    registry.register(first)
    with pytest.raises(ValueError):
        registry.register(second)
    registry.register(second, replace=True)
    assert (
        registry.resolve(EvaluatorKind.EQUIVALENCE, "candidate")
        is second
    )


def test_evaluator_identity() -> None:
    value = candidate(
        "identity", EvaluatorKind.EQUIVALENCE, lambda subject: subject
    )
    assert value.version == "test-1"
    assert value.code_reference.endswith(":identity")
    assert value.scope == "test fixtures"


def test_explicit_law_comparison() -> None:
    with pytest.raises(TypeError):
        LawSuite("missing", (null_zero_law(),), None)
    suite = LawSuite(
        "exact",
        (null_zero_law(),),
        exact_comparison_policy(),
    )
    assert suite.comparison.name == "exact"


def test_law_suite_evidence() -> None:
    left = Carrier(
        (
            Cell(coordinate="a", mu=2.0),
            Cell(coordinate="b", mu=3.0),
        )
    )
    right = Carrier((Cell(coordinate="c", mu=5.0),))
    subjects = (STRUCTURAL_NULL, left, right, pair(left, right))
    suite = LawSuite(
        "support-laws",
        (
            null_zero_law(),
            finite_nonnegative_law(subjects),
            pair_multiplicative_law(((left, right),)),
        ),
        combined_comparison_policy(rel_tol=1e-12, abs_tol=1e-12),
    )

    good = candidate(
        "support", EvaluatorKind.PRODUCT_CHARACTER, support_weight
    )
    report = suite.evaluate(good)
    assert report.all_passed
    assert report.comparison_policy_name == "combined"
    assert len(report.results) == 3

    constant = candidate(
        "constant",
        EvaluatorKind.PRODUCT_CHARACTER,
        lambda subject: 1.0,
    )
    failed = suite.evaluate(constant)
    assert not failed.all_passed
    assert any(
        not result.passed and result.error is None
        for result in failed.results
    )

    exploding = candidate(
        "exploding",
        EvaluatorKind.PRODUCT_CHARACTER,
        lambda subject: (_ for _ in ()).throw(RuntimeError("boom")),
    )
    errored = suite.evaluate(exploding)
    assert not errored.all_passed
    assert len(errored.results) == 3
    assert all(result.error is not None for result in errored.results)


def test_candidate_comparison() -> None:
    subject = Carrier((Cell(coordinate="a", mu=2.0),))
    candidates = (
        candidate(
            "support", EvaluatorKind.FAITHFUL_BREADTH, support_weight
        ),
        candidate(
            "count", EvaluatorKind.FAITHFUL_BREADTH, _cell_count
        ),
    )
    comparison = compare_candidates(
        candidates,
        (subject,),
        comparison=exact_comparison_policy(),
    )[0]
    assert comparison.disagreement
    assert comparison.comparison_policy_name == "exact"
    assert tuple(
        output.candidate_name for output in comparison.outputs
    ) == ("support", "count")
    assert tuple(output.output for output in comparison.outputs) == (
        2.0,
        1,
    )
    assert not hasattr(comparison, "winner")

    with pytest.raises(ValueError):
        compare_candidates(
            (),
            (subject,),
            comparison=exact_comparison_policy(),
        )
    with pytest.raises(ValueError):
        compare_candidates(
            (
                candidates[0],
                candidate(
                    "other",
                    EvaluatorKind.EQUIVALENCE,
                    lambda value: value,
                ),
            ),
            (subject,),
            comparison=exact_comparison_policy(),
        )


def test_separation_law_builders() -> None:
    same_w_left = Carrier(
        (
            Cell(coordinate="a", mu=1.0),
            Cell(coordinate="b", mu=1.0),
        )
    )
    same_w_right = Carrier((Cell(coordinate="c", mu=2.0),))
    same_candidate_left = Carrier(
        (Cell(coordinate="d", mu=1.0),)
    )
    same_candidate_right = Carrier(
        (Cell(coordinate="e", mu=3.0),)
    )

    count = candidate(
        "count", EvaluatorKind.PRODUCT_CHARACTER, _cell_count
    )
    suite = LawSuite(
        "separation",
        (
            same_reference_different_candidate_law(
                support_weight,
                (
                    Witness(
                        "same-W-different-count",
                        (same_w_left, same_w_right),
                        "W equal and candidate distinct",
                    ),
                ),
            ),
            same_candidate_different_reference_law(
                support_weight,
                (
                    Witness(
                        "same-count-different-W",
                        (same_candidate_left, same_candidate_right),
                        "candidate equal and W distinct",
                    ),
                ),
            ),
        ),
        exact_comparison_policy(),
    )
    assert suite.evaluate(count).all_passed
