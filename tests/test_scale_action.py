# === CHECKS ===
# id: check_scale_action_applies_integer_weights_exactly
#   proves: scale_action_applies_integer_weights_exactly
#   call: self::test_scale_action_applies_integer_weights_exactly
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_scale_action_composes_multiplicatively
#   proves: scale_action_composes_multiplicatively
#   call: self::test_scale_action_composes_multiplicatively
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_scale_action_monomial_invariants_are_weight_kernel
#   proves: scale_action_monomial_invariants_are_weight_kernel
#   call: self::test_scale_action_monomial_invariants_are_weight_kernel
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_scale_action_core_is_domain_agnostic
#   proves: scale_action_core_is_domain_agnostic
#   call: self::test_scale_action_core_is_domain_agnostic
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_scale_action_receipts_replay_exactly
#   proves: scale_action_receipts_replay_exactly
#   call: self::test_scale_action_receipts_replay_exactly
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_scale_action_candidate
#   proves: geometry_public_surface_includes_scale_action_candidate
#   call: self::test_facade_exports_scale_action
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

from fractions import Fraction
import json

import pytest

from ucns import (
    SCALE_ACTION_SCHEMA,
    MultiplicativeScaleAction,
    ScaleActionError,
    build_scale_action,
    build_scale_action_record,
    monomial_value,
    replay_scale_action_record,
)


def test_scale_action_applies_integer_weights_exactly() -> None:
    action = build_scale_action((1, 0, -1, 2), Fraction(3, 2))
    source = (Fraction(2), Fraction(3), Fraction(5), Fraction(7))
    assert action.apply(source) == (
        Fraction(3),
        Fraction(3),
        Fraction(10, 3),
        Fraction(63, 4),
    )
    assert action.arity == 4


def test_scale_action_composes_multiplicatively() -> None:
    weights = (1, -1, 2)
    source = (Fraction(2), Fraction(3), Fraction(5))
    q = build_scale_action(weights, Fraction(3, 2))
    p = build_scale_action(weights, Fraction(5, 3))

    composed = q.compose(p)
    assert composed.factor == Fraction(5, 2)
    assert p.apply(q.apply(source)) == composed.apply(source)

    identity = build_scale_action(weights, 1)
    assert identity.apply(source) == source
    assert q.inverse().apply(q.apply(source)) == source

    with pytest.raises(ScaleActionError):
        q.compose(build_scale_action((1, -1, 1), 2))


def test_scale_action_monomial_invariants_are_weight_kernel() -> None:
    # External fixtures may bind meanings to these six ordered axes.
    # UCNS sees only the exact weight vector.
    action = build_scale_action((1, 1, -1, 1, 2, 0), Fraction(7, 5))
    state = tuple(Fraction(value) for value in (2, 3, 5, 7, 11, 13))

    invariant_powers = (
        (-1, 1, 0, 0, 0, 0),
        (0, 0, 1, 1, 0, 0),
        (0, 0, 2, 0, 1, 0),
        (0, 0, -1, 1, -1, 0),
        (0, 0, 1, -1, 1, 1),
    )
    for powers in invariant_powers:
        assert action.monomial_weight(powers) == 0
        assert action.is_invariant(powers)
        assert action.preserves_monomial(state, powers)
        assert monomial_value(state, powers) == monomial_value(action.apply(state), powers)

    noninvariant = (1, 1, 0, 0, 0, 0)
    assert action.monomial_weight(noninvariant) == 2
    assert not action.is_invariant(noninvariant)
    assert not action.preserves_monomial(state, noninvariant)


def test_scale_action_core_is_domain_agnostic() -> None:
    record = build_scale_action_record(
        (1, 1, -1, 1, 2, 0),
        Fraction(3, 2),
        (2, 3, 5, 7, 11, 13),
    )
    payload = record.as_dict()
    assert set(payload["action"]) == {"weights", "factor"}
    serialized = json.dumps(payload, sort_keys=True)
    for forbidden in ("epsilon", "permittivity", "permeability", "mass", "hbar", "charge", "consciousness"):
        assert forbidden not in serialized.lower()


def test_scale_action_receipts_replay_exactly() -> None:
    record = build_scale_action_record(
        (1, -1, 2),
        Fraction(5, 3),
        (2, 3, 7),
    )
    assert replay_scale_action_record(record.receipt_bytes()) == record

    obj = json.loads(record.receipt_bytes())
    obj["target"][0] = "999"
    tampered = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with pytest.raises(ScaleActionError):
        replay_scale_action_record(tampered)

    with pytest.raises(ScaleActionError):
        build_scale_action((), 1)
    with pytest.raises(ScaleActionError):
        build_scale_action((1,), 0)
    with pytest.raises(ScaleActionError):
        MultiplicativeScaleAction((1,), 1)  # canonical constructor requires Fraction


def test_facade_exports_scale_action() -> None:
    import ucns

    assert ucns.SCALE_ACTION_SCHEMA == SCALE_ACTION_SCHEMA
    assert hasattr(ucns, "build_scale_action")
    assert hasattr(ucns, "build_scale_action_record")
    assert hasattr(ucns, "replay_scale_action_record")
