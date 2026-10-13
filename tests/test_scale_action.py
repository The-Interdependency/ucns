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
#
# id: check_scale_action_invalid_public_inputs
#   proves: scale_action_inputs_fail_closed
#   call: self::test_scale_action_invalid_public_inputs
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_scale_action_canonical_record_types
#   proves: scale_action_inputs_fail_closed
#   call: self::test_scale_action_canonical_record_types
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_scale_action_encoding_limits
#   proves: scale_action_inputs_fail_closed
#   call: self::test_scale_action_encoding_limits
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_scale_action_malformed_receipts
#   proves: scale_action_inputs_fail_closed
#   call: self::test_scale_action_malformed_receipts
#   requires: python3
#   timeout: 30
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


def test_scale_action_invalid_public_inputs() -> None:
    action = build_scale_action((1,), 2)
    for value in (None, 1, True, 1.5):
        for call in (
            lambda: build_scale_action(value, 1),
            lambda: action.apply(value),
            lambda: action.monomial_weight(value),
            lambda: monomial_value(value, (1,)),
            lambda: monomial_value((1,), value),
        ):
            with pytest.raises(ScaleActionError):
                call()
    for value in (True, 1.5, "1", 0, -1):
        with pytest.raises(ScaleActionError):
            build_scale_action((1,), value)
        with pytest.raises(ScaleActionError):
            action.apply((value,))
    for powers in ((True,), (1.5,), (), (1, 2)):
        with pytest.raises(ScaleActionError):
            action.monomial_weight(powers)
    assert monomial_value((), ()) == 1
    assert monomial_value(iter((2, 3)), iter((1, -1))) == Fraction(2, 3)
    with pytest.raises(ScaleActionError):
        action.compose(None)


def test_scale_action_canonical_record_types() -> None:
    from ucns import ScaleActionRecord

    record = build_scale_action_record((1,), 2, (3,))
    for source, target in (((3,), record.target), (record.source, (6,))):
        with pytest.raises(ScaleActionError, match="canonical Fractions"):
            ScaleActionRecord(record.action, source, target, record.receipt_sha256)
    assert ScaleActionRecord(record.action, record.source, record.target, record.receipt_sha256) == record


def test_scale_action_encoding_limits() -> None:
    import sys
    from unittest.mock import patch

    prior = sys.get_int_max_str_digits()
    try:
        sys.set_int_max_str_digits(640)
        huge = 10 ** 700
        for weights, factor, source in (((huge,), 1, (1,)), ((0,), huge, (1,)), ((0,), 1, (huge,)), ((1,), 10, (10 ** 639,))):
            with pytest.raises(ScaleActionError):
                build_scale_action_record(weights, factor, source)
        with pytest.raises(ScaleActionError):
            replay_scale_action_record(b'{"weights":[' + b'9' * 641 + b']}')
        with pytest.raises(ScaleActionError):
            replay_scale_action_record(b'{"action":{"weights":[0],"factor":"' + b'9' * 641 + b'"}}')
    finally:
        sys.set_int_max_str_digits(prior)
    with patch("ucns.scale_action.json.loads", side_effect=RecursionError("parser limit")):
        with pytest.raises(ScaleActionError):
            replay_scale_action_record(b"{}")
    with patch("ucns.scale_action.json.dumps", side_effect=RuntimeError("fault")):
        with pytest.raises(RuntimeError, match="fault"):
            build_scale_action_record((1,), 2, (3,))


def test_scale_action_malformed_receipts() -> None:
    record = build_scale_action_record((1,), 2, (3,))
    for data in (None, "{}", b"{", b"\xff", b"[]", b"[" * 10000 + b"0" + b"]" * 10000):
        with pytest.raises(ScaleActionError):
            replay_scale_action_record(data)
    for path, value in (("factor", "2/1"), ("factor", "2.0"), ("factor", "0"), ("factor", "1/0"), ("factor", "\ud800"), ("factor", True), ("weights", [True]), ("weights", [1.0]), ("weights", [])):
        obj = record.as_dict()
        obj["action"][path] = value
        with pytest.raises(ScaleActionError):
            replay_scale_action_record(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode())
    for key, value in (("source", [True]), ("target", ["7"]), ("standing", "ratified"), ("receipt_sha256", None)):
        obj = record.as_dict()
        obj[key] = value
        with pytest.raises(ScaleActionError):
            replay_scale_action_record(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode())
    with pytest.raises(ScaleActionError):
        replay_scale_action_record(record.receipt_bytes() + b"\n")
