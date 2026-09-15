# === CHECKS ===
# id: check_visible_displacement_channel_turns_are_exact
#   proves: visible_displacement_channel_turns_are_exact
#   call: self::test_channel_turns_are_exact_fractions
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_zero_channels_are_structural_null
#   proves: visible_displacement_zero_channels_are_structural_null
#   call: self::test_zero_channels_are_structural_null_and_deterministic
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_preserves_native_mobius_law
#   proves: visible_displacement_preserves_native_mobius_law
#   call: self::test_one_full_turn_flips_frame_and_two_restore
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_covering_degree_is_explicit
#   proves: visible_displacement_covering_degree_is_explicit
#   call: self::test_covering_degree_is_recorded_and_congruent
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_fails_closed_on_non_bijective_covering
#   proves: visible_displacement_fails_closed_on_non_bijective_covering
#   call: self::test_fails_closed_on_non_bijective_covering_degree
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_fails_closed_on_invalid_input
#   proves: visible_displacement_fails_closed_on_invalid_input
#   call: self::test_fails_closed_on_malformed_residues
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_replay_is_byte_identical
#   proves: visible_displacement_replay_is_byte_identical
#   call: self::test_replay_is_byte_identical
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_replay_detects_tamper
#   proves: visible_displacement_replay_detects_tamper
#   call: self::test_replay_detects_tamper
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_residues_wrap_on_the_carrier
#   proves: visible_displacement_residues_wrap_on_the_carrier
#   call: self::test_negative_residues_wrap_on_the_157_carrier
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_visible_displacement_remains_candidate
#   proves: visible_displacement_remains_candidate
#   call: self::test_candidate_standing_not_ratified
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_visible_displacement_candidate
#   proves: geometry_public_surface_includes_visible_displacement_candidate
#   call: self::test_facade_exports_candidate_surface
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

from fractions import Fraction

import pytest

import ucns
from ucns import (
    VISIBLE_DISPLACEMENT_SCHEMA,
    VISIBLE_DISPLACEMENT_VERSION,
    VisibleDisplacementError,
    build_visible_displacement,
    replay_visible_displacement,
)
from ucns.direct_mobius import NativeMobiusFrame


def test_zero_channels_are_structural_null_and_deterministic() -> None:
    record = build_visible_displacement(0, 0, 0)
    assert record.ordinal_turn == Fraction(0)
    assert record.semantic_turn == Fraction(0)
    assert record.context_turn == Fraction(0)
    assert record.total_turn == Fraction(0)
    assert record.mobius.phase_turns == Fraction(0)
    assert record.mobius.frame is NativeMobiusFrame.POSITIVE
    assert record.schema == VISIBLE_DISPLACEMENT_SCHEMA

    again = build_visible_displacement(0, 0, 0)
    assert again.receipt_sha256 == record.receipt_sha256
    assert again.receipt_bytes() == record.receipt_bytes()


def test_channel_turns_are_exact_fractions() -> None:
    record = build_visible_displacement(1, 2, 3)
    assert record.ordinal_turn == Fraction(1, 157)
    assert record.semantic_turn == Fraction(2, 157)
    assert record.context_turn == Fraction(3, 157)
    assert record.total_turn == Fraction(6, 157)
    assert record.mobius.phase_turns == Fraction(6, 157)


def test_one_full_turn_flips_frame_and_two_restore() -> None:
    one = build_visible_displacement(100, 57, 0)
    assert one.mobius.phase_turns == Fraction(0)
    assert one.mobius.frame is NativeMobiusFrame.REVERSED

    two = build_visible_displacement(156, 156, 2)
    assert two.mobius.phase_turns == Fraction(0)
    assert two.mobius.frame is NativeMobiusFrame.POSITIVE


def test_covering_degree_is_recorded_and_congruent() -> None:
    record = build_visible_displacement(1, 0, 0, covering_degree=158)
    assert record.covering_degree == 158
    assert record.covering_multiplier == 1

    doubled = build_visible_displacement(1, 0, 0, covering_degree=2)
    assert doubled.covering_multiplier == 2


def test_fails_closed_on_non_bijective_covering_degree() -> None:
    with pytest.raises(VisibleDisplacementError):
        build_visible_displacement(1, 0, 0, covering_degree=157)


@pytest.mark.parametrize("bad", [True, False, 1.5, "1", None])
def test_fails_closed_on_malformed_residues(bad: object) -> None:
    with pytest.raises(VisibleDisplacementError):
        build_visible_displacement(bad, 0, 0)  # type: ignore[arg-type]
    with pytest.raises(VisibleDisplacementError):
        build_visible_displacement(0, bad, 0)  # type: ignore[arg-type]
    with pytest.raises(VisibleDisplacementError):
        build_visible_displacement(0, 0, bad)  # type: ignore[arg-type]


def test_replay_is_byte_identical() -> None:
    record = build_visible_displacement(10, 20, 30, covering_degree=158)
    replayed = replay_visible_displacement(record.receipt_bytes())
    assert replayed == record
    assert replayed.receipt_bytes() == record.receipt_bytes()


def test_replay_detects_tamper() -> None:
    record = build_visible_displacement(10, 20, 30)
    receipt = bytearray(record.receipt_bytes())
    original = receipt[40]
    receipt[40] = original ^ 0x01
    with pytest.raises(VisibleDisplacementError):
        replay_visible_displacement(bytes(receipt))


def test_negative_residues_wrap_on_the_157_carrier() -> None:
    record = build_visible_displacement(-1, 0, 0)
    assert record.ordinal == 156
    assert record.ordinal_turn == Fraction(156, 157)


def test_candidate_standing_not_ratified() -> None:
    assert "candidate" in VISIBLE_DISPLACEMENT_SCHEMA
    record = build_visible_displacement(1, 2, 3)
    assert record.schema == VISIBLE_DISPLACEMENT_SCHEMA


def test_facade_exports_candidate_surface() -> None:
    assert hasattr(ucns, "build_visible_displacement")
    assert hasattr(ucns, "replay_visible_displacement")
    assert hasattr(ucns, "VisibleDisplacementError")
    assert hasattr(ucns, "VisibleDisplacementRecord")
    assert ucns.VISIBLE_DISPLACEMENT_SCHEMA == VISIBLE_DISPLACEMENT_SCHEMA
    assert ucns.VISIBLE_DISPLACEMENT_VERSION == VISIBLE_DISPLACEMENT_VERSION
