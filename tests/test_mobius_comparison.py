# === CHECKS ===
# id: check_mobius_comparison_complete_grid
#   proves: mobius_comparison_reconstructs_complete_target, mobius_comparison_is_native_chart_covariant
#   call: self::test_complete_eighth_turn_grid
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_mobius_comparison_chart_changes
#   proves: mobius_comparison_is_native_chart_covariant
#   call: self::test_exact_rational_chart_changes
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_mobius_comparison_composition
#   proves: mobius_comparison_composes_exactly
#   call: self::test_composition_inverse_and_cocycle
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_mobius_comparison_ablations
#   proves: mobius_comparison_reconstructs_complete_target, mobius_comparison_is_native_chart_covariant, mobius_comparison_preserves_evidence_boundary
#   call: self::test_seam_and_phase_only_ablations
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_mobius_comparison_rejections
#   proves: mobius_comparison_rejects_inexact_inputs
#   call: self::test_invalid_inputs_and_immutability
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_mobius_comparison_winding_boundary
#   proves: mobius_comparison_preserves_evidence_boundary, mobius_comparison_reconstructs_complete_target
#   call: self::test_one_turn_two_turn_and_winding_boundary
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

"""Exact comparison witnesses. Usage: run the complete README geometry gate.

The eight-phase grid exhausts BOTH frames, all ordered endpoint pairs, and all
33 declared signed motions. Other rational witnesses complement, rather than
replace, the general algebraic proof in docs/native-mobius-comparison.md.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError
from fractions import Fraction
from itertools import product

import pytest

from ucns.direct_mobius import NativeMobiusFrame, NativeMobiusState, native_mobius_state
from ucns.mobius_comparison import (
    MobiusComparisonError,
    NativeMobiusComparison,
    compare_native_mobius,
)


def _grid() -> tuple[NativeMobiusState, ...]:
    return tuple(NativeMobiusState(Fraction(k, 8), frame) for k in range(8) for frame in NativeMobiusFrame)


def test_complete_eighth_turn_grid() -> None:
    states = _grid()
    motions = tuple(Fraction(k, 8) for k in range(-16, 17))
    checks = 0
    raw_changes = 0
    for source, target in product(states, repeat=2):
        relation = compare_native_mobius(source, target)
        assert relation.transport(source) == target
        assert relation.inverse().transport(target) == source
        visible = (target.phase_turns - source.phase_turns) % 1
        seam_carry = int(target.phase_turns < source.phase_turns)
        transported_sign = source.frame.sign * target.frame.sign * (-1) ** seam_carry
        assert relation.phase_turns == visible
        assert relation.frame_sign == transported_sign
        for motion in motions:
            moved_source = source.advance(motion)
            moved_target = target.advance(motion)
            assert compare_native_mobius(moved_source, moved_target) == relation
            raw_changes += int(source.frame.sign * target.frame.sign != moved_source.frame.sign * moved_target.frame.sign)
            checks += 1
    assert checks == 8448
    assert raw_changes == 2688


def test_exact_rational_chart_changes() -> None:
    phases = (Fraction(0), Fraction(1, 3), Fraction(2, 5), Fraction(6, 7), Fraction(10**80 - 1, 10**80))
    states = tuple(NativeMobiusState(phase, frame) for phase in phases for frame in NativeMobiusFrame)
    motions = (Fraction(-10**80, 7), Fraction(-19, 3), Fraction(-1, 10**80), Fraction(0), Fraction(1, 10**80), Fraction(37, 13), Fraction(10**80, 11))
    for source, target in product(states, repeat=2):
        relation = compare_native_mobius(source, target)
        assert relation.transport(source) == target
        for motion in motions:
            assert compare_native_mobius(source.advance(motion), target.advance(motion)) == relation
        reflected_source = native_mobius_state(-source.phase_turns, source.frame)
        reflected_target = native_mobius_state(-target.phase_turns, target.frame)
        assert compare_native_mobius(reflected_source, reflected_target) == relation.inverse()
        for source_shift, target_shift in product(range(-2, 3), repeat=2):
            source_frame = source.frame.flipped() if source_shift % 2 else source.frame
            target_frame = target.frame.flipped() if target_shift % 2 else target.frame
            equivalent_source = native_mobius_state(source.phase_turns + source_shift, source_frame)
            equivalent_target = native_mobius_state(target.phase_turns + target_shift, target_frame)
            assert equivalent_source == source and equivalent_target == target
            assert compare_native_mobius(equivalent_source, equivalent_target) == relation


def test_composition_inverse_and_cocycle() -> None:
    states = _grid()
    identity = NativeMobiusComparison(Fraction(0))
    for a, b, c in product(states, repeat=3):
        ab = compare_native_mobius(a, b)
        bc = compare_native_mobius(b, c)
        ac = compare_native_mobius(a, c)
        assert ab.then(bc) == ac
        assert ab.then(bc).transport(a) == bc.transport(ab.transport(a)) == c
        assert ab.then(ab.inverse()) == identity
        assert identity.then(ab) == ab.then(identity) == ab
        assert ab.inverse() == compare_native_mobius(b, a)
        carry = (ab.phase_turns + bc.phase_turns) // 1
        assert ac.frame_sign == ab.frame_sign * bc.frame_sign * (-1) ** carry
    for a, b, c, d in product(states[::4], repeat=4):
        ab, bc, cd = compare_native_mobius(a, b), compare_native_mobius(b, c), compare_native_mobius(c, d)
        assert ab.then(bc).then(cd) == ab.then(bc.then(cd))


def test_seam_and_phase_only_ablations() -> None:
    a = native_mobius_state(Fraction(3, 4))
    b = native_mobius_state(Fraction(1, 4))
    aa, bb = a.advance(Fraction(1, 2)), b.advance(Fraction(1, 2))
    assert a.frame.sign * b.frame.sign == 1
    assert aa.frame.sign * bb.frame.sign == -1
    relation = compare_native_mobius(a, b)
    assert relation == compare_native_mobius(aa, bb)
    assert relation.relative_turns == Fraction(3, 2)
    assert relation.frame_sign == -1
    assert relation.transport(a) == b
    assert a.advance(relation.phase_turns) != b  # Removing the frame bit loses the target.
    opposite = b.advance(1)
    assert compare_native_mobius(a, opposite).phase_turns == relation.phase_turns
    assert compare_native_mobius(a, opposite) != relation


def test_invalid_inputs_and_immutability() -> None:
    for value in (0, 1, True, False, 0.5, float("nan"), float("inf"), "0", None, Fraction(-1, 8), Fraction(2), Fraction(17, 8)):
        with pytest.raises(MobiusComparisonError):
            NativeMobiusComparison(value)
    origin = native_mobius_state()
    relation = compare_native_mobius(origin, origin)
    for value in (None, True, 0, "state", object()):
        with pytest.raises(MobiusComparisonError):
            compare_native_mobius(value, origin)
        with pytest.raises(MobiusComparisonError):
            compare_native_mobius(origin, value)
        with pytest.raises(MobiusComparisonError):
            relation.transport(value)
        with pytest.raises(MobiusComparisonError):
            relation.then(value)
    with pytest.raises(FrozenInstanceError):
        relation.relative_turns = Fraction(1)


def test_one_turn_two_turn_and_winding_boundary() -> None:
    for source in _grid():
        assert compare_native_mobius(source, source.advance(1)).relative_turns == 1
        assert compare_native_mobius(source, source.advance(2)).relative_turns == 0
        assert source.advance(1) != source
        assert source.advance(2) == source
        assert compare_native_mobius(source, source.advance(1)) == compare_native_mobius(source, source.advance(3))
        assert compare_native_mobius(source, source.advance(-1)) == compare_native_mobius(source, source.advance(1))
