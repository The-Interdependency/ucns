# === CHECKS ===
# id: check_policy_registry_choices
#   proves: policy_registry_preserves_multiple_choices
#   call: self::test_policy_registry_choices
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_projection_loss_evidence
#   proves: projection_retains_source_and_declares_loss
#   call: self::test_projection_loss_evidence
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_explicit_policy_keys
#   proves: lossy_builtin_policies_require_explicit_keys
#   call: self::test_explicit_policy_keys
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_unknown_policy_failure
#   proves: unknown_policy_names_fail_closed
#   call: self::test_unknown_policy_failure
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import pytest

from ucns.policy import (
    PolicyRegistry,
    StructurePolicy,
    apply_policy,
    ordered_sequence_policy,
    set_policy,
    unordered_multiset_policy,
)


def test_policy_registry_choices() -> None:
    registry = PolicyRegistry()
    ordered = ordered_sequence_policy()
    multiset = unordered_multiset_policy(lambda value: value)
    distinct = set_policy(lambda value: value)

    registry.register(ordered)
    registry.register(multiset)
    registry.register(distinct)
    assert registry.names() == ("ordered-sequence", "unordered-multiset", "set")
    assert registry.resolve("ordered-sequence") is ordered
    assert registry.policies() == (ordered, multiset, distinct)
    assert not hasattr(registry, "default")

    with pytest.raises(ValueError):
        registry.register(ordered)
    replacement = StructurePolicy("ordered-sequence", "replacement view", tuple)
    registry.register(replacement, replace=True)
    assert registry.resolve("ordered-sequence") is replacement


def test_projection_loss_evidence() -> None:
    source = ("b", "a", "a")
    ordered = apply_policy(source, ordered_sequence_policy())
    assert ordered.source is source
    assert ordered.view == source
    assert not ordered.is_lossy

    multiset = apply_policy(source, unordered_multiset_policy(lambda value: value))
    assert multiset.source is source
    assert [group.count for group in multiset.view] == [1, 2]
    assert tuple(loss.dimension for loss in multiset.losses) == ("order",)
    assert multiset.recoverable

    distinct = apply_policy(source, set_policy(lambda value: value))
    assert distinct.source is source
    assert len(distinct.view) == 2
    assert tuple(loss.dimension for loss in distinct.losses) == ("order", "multiplicity")
    assert distinct.recoverable


def test_explicit_policy_keys() -> None:
    with pytest.raises(TypeError):
        unordered_multiset_policy(None)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        set_policy(None)  # type: ignore[arg-type]

    bad_key = unordered_multiset_policy(lambda value: [value])
    with pytest.raises(TypeError):
        apply_policy(("a",), bad_key)


def test_unknown_policy_failure() -> None:
    registry = PolicyRegistry()
    registry.register(ordered_sequence_policy())
    with pytest.raises(KeyError):
        apply_policy((1, 2), "missing", registry=registry)
    with pytest.raises(ValueError):
        apply_policy((1, 2), "ordered-sequence")
