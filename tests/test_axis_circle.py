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
#
# id: check_axis_circle_replay_normalizes_json_integer_limit_failure
#   proves: axis_circle_fails_closed
#   call: self::test_axis_circle_replay_normalizes_json_integer_limit_failure
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_axis_circle_replay_normalizes_json_recursion_failure
#   proves: axis_circle_fails_closed
#   call: self::test_axis_circle_replay_normalizes_json_recursion_failure
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_axis_circle_large_integer_transport
#   proves: axis_circle_position_is_exact, axis_circle_fails_closed
#   call: self::test_axis_circle_large_integer_transport_ignores_process_digit_limit
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_axis_circle_work_graph_skill_authority
#   proves: axis_circle_work_graph_binds_enforced_skill_authority
#   call: self::test_axis_circle_work_graph_uses_enforced_skill_source
#   requires: python3
#   timeout: 10
#   mutates: filesystem_read
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

import pytest

from ucns.axis_circle import (
    AxisCircleError,
    build_axis_circle_position,
    replay_axis_circle_position,
)


def test_axis_circle_position_is_exact() -> None:
    position = build_axis_circle_position(
        origin_sha256="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
        origin_sha256="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        axis_count=3,
        axis_ordinal=1,
    )
    second = build_axis_circle_position(
        origin_sha256="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        axis_count=3,
        axis_ordinal=1,
    )
    assert first == second
    serialized = json.dumps(first.as_dict(), sort_keys=True)
    for forbidden in ("heart", "cardiac", "corazon", "label", "language"):
        assert forbidden not in serialized.lower()


def test_axis_circle_origin_change_changes_identity() -> None:
    first = build_axis_circle_position(
        origin_sha256="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        axis_count=3,
        axis_ordinal=1,
    )
    changed_origin = build_axis_circle_position(
        origin_sha256="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        axis_count=3,
        axis_ordinal=1,
    )
    changed_axis = build_axis_circle_position(
        origin_sha256="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        axis_count=3,
        axis_ordinal=2,
    )
    assert first.identity_sha256 != changed_origin.identity_sha256
    assert first.identity_sha256 != changed_axis.identity_sha256


def test_axis_circle_fails_closed() -> None:
    for kwargs in (
        {"origin_sha256": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "axis_count": 3, "axis_ordinal": 1},
        {"origin_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "axis_count": 0, "axis_ordinal": 0},
        {"origin_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "axis_count": 3, "axis_ordinal": 3},
        {"origin_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "axis_count": 3, "axis_ordinal": True},
    ):
        with pytest.raises(AxisCircleError):
            build_axis_circle_position(**kwargs)

    valid = build_axis_circle_position(
        origin_sha256="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        axis_count=3,
        axis_ordinal=1,
    )
    with pytest.raises(AxisCircleError):
        replace(valid, turn=Fraction(2, 3))
    with pytest.raises(AxisCircleError):
        replace(valid, identity_sha256="0000000000000000000000000000000000000000000000000000000000000000")

    obj = json.loads(valid.receipt_bytes())
    obj["axis_ordinal"] = 2
    tampered = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with pytest.raises(AxisCircleError):
        replay_axis_circle_position(tampered)


def test_axis_circle_replay_normalizes_json_integer_limit_failure() -> None:
    oversized = (b'{"schema":"ucns.axis-circle-position-candidate","version":"0.1.0","origin_sha256":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","axis_count":' + b"9" * 5000 + b',"axis_ordinal":1,"turn":{"numerator":1,"denominator":3},"identity_sha256":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}')
    with pytest.raises(AxisCircleError):
        replay_axis_circle_position(oversized)


def test_axis_circle_replay_normalizes_json_recursion_failure() -> None:
    deeply_nested = b"[" * 2000 + b"0" + b"]" * 2000
    with pytest.raises(AxisCircleError):
        replay_axis_circle_position(deeply_nested)


def test_axis_circle_large_integer_transport_ignores_process_digit_limit() -> None:
    if not hasattr(sys, "set_int_max_str_digits"):
        pytest.skip("interpreter has no integer conversion digit limit")
    prior = sys.get_int_max_str_digits()
    try:
        sys.set_int_max_str_digits(640)
        position = build_axis_circle_position(
            origin_sha256="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            axis_count=1 << 4095,
            axis_ordinal=1,
        )
        assert position.axis_count.bit_length() == 4096
        assert replay_axis_circle_position(position.receipt_bytes()) == position
    finally:
        sys.set_int_max_str_digits(prior)


def test_axis_circle_work_graph_uses_enforced_skill_source() -> None:
    root = Path(__file__).resolve().parents[1]
    graph = json.loads((root / "docs/work-graphs/polyglot-circle-identity-v0.json").read_text(encoding="utf-8"))
    expected = sha256(json.dumps(
        {key: graph[key] for key in ("repositories", "boundaries")},
        sort_keys=True, separators=(",", ":"),
    ).encode()).hexdigest()
    assert graph["work_graph_sha256"] == expected
    readme = (root / ".agents/skills/README.md").read_text(encoding="utf-8")
    match = re.search(r"Source commit: `([0-9a-f]{40})`", readme)
    assert match is not None
    skill = next(row for row in graph["repositories"] if row["repository"] == "The-Interdependency/skill-lib")
    assert skill["commit"] == match.group(1)
