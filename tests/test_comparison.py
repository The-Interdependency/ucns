# === CHECKS ===
# id: check_explicit_comparison_policies
#   proves: evaluator_equality_requires_explicit_comparison_policy
#   call: self::test_explicit_comparison_policies
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_comparison_registry_choices
#   proves: comparison_registry_preserves_multiple_policies
#   call: self::test_comparison_registry_choices
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_comparison_replacement
#   proves: comparison_policy_replacement_is_explicit
#   call: self::test_comparison_replacement
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_custom_comparison_identity
#   proves: custom_comparison_identity_is_explicit
#   call: self::test_custom_comparison_identity
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from math import nextafter

import pytest

from ucns import (
    ComparisonRegistry,
    absolute_comparison_policy,
    combined_comparison_policy,
    custom_comparison_policy,
    exact_comparison_policy,
    interval_overlap_policy,
    relative_comparison_policy,
    ulp_comparison_policy,
)


def test_explicit_comparison_policies() -> None:
    assert exact_comparison_policy().matches("a", "a")
    assert absolute_comparison_policy(0.1).matches(1.0, 1.05)
    assert not absolute_comparison_policy(0.1).matches(1.0, 1.2)
    assert relative_comparison_policy(0.1).matches(100.0, 105.0)
    assert combined_comparison_policy(
        rel_tol=1e-6, abs_tol=1e-6
    ).matches(1.0, 1.0000001)
    assert ulp_comparison_policy(1).matches(
        1.0, nextafter(1.0, 2.0)
    )
    assert ulp_comparison_policy(0).matches(-0.0, 0.0)
    assert not ulp_comparison_policy(
        0, signed_zero_equal=False
    ).matches(-0.0, 0.0)
    intervals = interval_overlap_policy()
    assert intervals.matches((0.0, 1.0), (0.5, 2.0))
    assert not intervals.matches((0.0, 1.0), (2.0, 3.0))


def test_comparison_registry_choices() -> None:
    registry = ComparisonRegistry()
    exact = exact_comparison_policy()
    relative = relative_comparison_policy(1e-9)
    registry.register(exact)
    registry.register(relative)
    assert registry.names() == ("exact", "relative")
    assert registry.resolve("exact") is exact
    assert not hasattr(registry, "default")


def test_comparison_replacement() -> None:
    registry = ComparisonRegistry()
    registry.register(exact_comparison_policy())
    with pytest.raises(ValueError):
        registry.register(exact_comparison_policy(version="2"))
    replacement = exact_comparison_policy(version="2")
    registry.register(replacement, replace=True)
    assert registry.resolve("exact") is replacement


def test_custom_comparison_identity() -> None:
    with pytest.raises(TypeError):
        custom_comparison_policy(
            "custom",
            lambda left, right: left == right,
            version="1",
        )
    first = custom_comparison_policy(
        "custom",
        lambda left, right: left == right,
        version="1",
        code_reference="tests.test_comparison:equal",
    )
    second = custom_comparison_policy(
        "custom",
        lambda left, right: left != right,
        version="1",
        code_reference="tests.test_comparison:not-equal",
    )
    assert first.code_reference != second.code_reference
