# === CHECKS ===
# id: check_axis_circle_position_is_exact
#   proves: axis_circle_position_is_exact
#   call: self::test_axis_circle_position_is_exact
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_axis_circle_identity_is_label_independent
#   proves: axis_circle_identity_is_label_independent
#   call: self::test_axis_circle_identity_is_label_independent
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_axis_circle_origin_change_changes_identity
#   proves: axis_circle_origin_change_changes_identity
#   call: self::test_axis_circle_origin_change_changes_identity
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_axis_circle_fails_closed
#   proves: axis_circle_fails_closed
#   call: self::test_axis_circle_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction
import json

import pytest

from ucns.axis_circle import (
    AxisCircleError,
    build_axis_circle_position,
    replay_axis_circle_position,
)


ORIGIN_A = "a" * 64
ORIGIN_B = "b" * 64


def test_axis_circle_position_is_exact() -> None:
    position = build_axis_circle_position(
        origin_sha256=ORIGIN_A,
        axis_count=9,
        axis_ordinal=4,
    )
    assert position.turn == Fraction(4, 9)
    assert position.as_dict()["turn"] == {"numerator": 4, "denominator": 9}
    assert replay_axis_circle_position(position.receipt_bytes()) == position


def test_axis_circle_identity_is_label_independent() -> None:
    # Labels are deliberately external. The same geometric inputs reconstruct
    # exactly the same identity whether a consumer calls it heart, cardiac,
    # corazon, or anything else.
    first = build_axis_circle_position(
        origin_sha256=ORIGIN_A,
        axis_count=3,
        axis_ordinal=1,
    )
    second = build_axis_circle_position(
        origin_sha256=ORIGIN_A,
        axis_count=3,
        axis_ordinal=1,
    )
    assert first == second
    serialized = json.dumps(first.as_dict(), sort_keys=True)
    for forbidden in ("heart", "cardiac", "corazon", "label", "language"):
        assert forbidden not in serialized.lower()


def test_axis_circle_origin_change_changes_identity() -> None:
    first = build_axis_circle_position(
        origin_sha256=ORIGIN_A,
        axis_count=3,
        axis_ordinal=1,
    )
    changed_origin = build_axis_circle_position(
        origin_sha256=ORIGIN_B,
        axis_count=3,
        axis_ordinal=1,
    )
    changed_axis = build_axis_circle_position(
        origin_sha256=ORIGIN_A,
        axis_count=3,
        axis_ordinal=2,
    )
    assert first.identity_sha256 != changed_origin.identity_sha256
    assert first.identity_sha256 != changed_axis.identity_sha256


def test_axis_circle_fails_closed() -> None:
    for kwargs in (
        {"origin_sha256": "x" * 64, "axis_count": 3, "axis_ordinal": 1},
        {"origin_sha256": ORIGIN_A, "axis_count": 0, "axis_ordinal": 0},
        {"origin_sha256": ORIGIN_A, "axis_count": 3, "axis_ordinal": 3},
        {"origin_sha256": ORIGIN_A, "axis_count": 3, "axis_ordinal": True},
    ):
        with pytest.raises(AxisCircleError):
            build_axis_circle_position(**kwargs)

    valid = build_axis_circle_position(
        origin_sha256=ORIGIN_A,
        axis_count=3,
        axis_ordinal=1,
    )
    with pytest.raises(AxisCircleError):
        replace(valid, turn=Fraction(2, 3))
    with pytest.raises(AxisCircleError):
        replace(valid, identity_sha256="0" * 64)

    obj = json.loads(valid.receipt_bytes())
    obj["axis_ordinal"] = 2
    tampered = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with pytest.raises(AxisCircleError):
        replay_axis_circle_position(tampered)
