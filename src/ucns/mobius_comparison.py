# === MODULE_BUILD ===
# id: ucns_native_mobius_comparison
#   module_name: mobius_comparison
#   module_kind: experiment
#   summary: exact relative complete-state displacement derived from the existing framed root-loop quotient
#   owner: Erin Spencer
#   public_surface: NativeMobiusComparison, MobiusComparisonError, compare_native_mobius
#   internal_surface: _state_coordinate, _require_state
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_mobius_comparison.py
#   rollout: opt-in derived geometry module; no change to the native motion law or selected UCNS canon
#   rollback: remove this module, its tests, and its documentation
#   requires: ucns_native_mobius_geometry
#   since: 2026-09-25
#   unresolved: alignment of independently rooted charts and path winding beyond complete-state equivalence
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: mobius_comparison_reconstructs_complete_target
#   given: two exact native states in the same identified root-loop chart
#   then: their comparison transports the source to the complete target and retains one-turn frame reversal
#   class: correctness
#
# id: mobius_comparison_is_native_chart_covariant
#   given: common exact motion, equivalent quotient representatives, or a reversal of native chart orientation
#   then: comparison is invariant in the first two cases and negates modulo two under orientation reversal
#   class: correctness
#
# id: mobius_comparison_composes_exactly
#   given: three states in one native chart and their pairwise comparisons
#   then: composition, identity, inverse, and the visible-phase carry cocycle agree exactly
#   class: correctness
#
# id: mobius_comparison_rejects_inexact_inputs
#   given: invalid states or a noncanonical or inexact relative displacement
#   then: construction and application fail explicitly without coercing floats or booleans
#   class: safety
#
# id: mobius_comparison_preserves_evidence_boundary
#   given: endpoints rather than a path witness
#   then: comparison records displacement modulo two only and supplies neither absolute winding nor cross-origin alignment
#   class: evidence
# === END CONTRACTS ===

"""Comparison on the existing exact framed root loop, not a new wire law.

Usage::

    from fractions import Fraction
    from ucns.direct_mobius import native_mobius_state
    from ucns.mobius_comparison import compare_native_mobius

    a = native_mobius_state(Fraction(3, 4))
    b = native_mobius_state(Fraction(1, 4))
    relation = compare_native_mobius(a, b)
    assert relation.relative_turns == Fraction(3, 2)
    assert relation.transport(a) == b
    assert relation == compare_native_mobius(a.advance(1), b.advance(1))

States must already share an identified native root-loop chart. This module
cannot authorize comparison across independently rooted consumer objects.
The result is a displacement class modulo two turns, not a recovered path or
an assertion about total winding. See docs/native-mobius-comparison.md for the
exact derivation, covariance scope, falsifiers, and non-transfer boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .direct_mobius import NativeMobiusFrame, NativeMobiusState

COMPARISON_LAW_ID = "ucns.native-mobius-comparison"
COMPARISON_LAW_VERSION = "1.0.0"
COMPARISON_STANDING = "derived-root-loop-comparison; not selected full UCNS geometry"


class MobiusComparisonError(ValueError):
    """Input is outside the exact native comparison domain."""


def _require_state(state: NativeMobiusState) -> None:
    if not isinstance(state, NativeMobiusState):
        raise MobiusComparisonError("comparison requires a NativeMobiusState")


def _state_coordinate(state: NativeMobiusState) -> Fraction:
    _require_state(state)
    return state.phase_turns + int(state.frame is NativeMobiusFrame.REVERSED)


@dataclass(frozen=True, slots=True)
class NativeMobiusComparison:
    """A canonical element of Q / 2Z acting on complete native states.

    Construct with an exact Fraction in [0, 2), or use compare_native_mobius.
    The frame comparison is measured after transport along the nonnegative
    visible arc; it is not the naive product of the endpoint frame signs.
    """

    relative_turns: Fraction

    def __post_init__(self) -> None:
        if not isinstance(self.relative_turns, Fraction):
            raise MobiusComparisonError("relative_turns must be an exact Fraction")
        if not Fraction(0) <= self.relative_turns < Fraction(2):
            raise MobiusComparisonError("relative_turns must lie in [0, 2)")

    @property
    def phase_turns(self) -> Fraction:
        """Return the relative visible phase, retaining the full state separately."""
        return self.relative_turns % 1

    @property
    def frame_sign(self) -> int:
        """Compare target frame with source frame transported over the visible arc."""
        return -1 if self.relative_turns >= 1 else 1

    def transport(self, source: NativeMobiusState) -> NativeMobiusState:
        """Apply this displacement class using the unchanged native motion law."""
        _require_state(source)
        return source.advance(self.relative_turns)

    def inverse(self) -> NativeMobiusComparison:
        """Return the inverse displacement class, not an inferred reverse path."""
        return NativeMobiusComparison((-self.relative_turns) % 2)

    def then(self, after: NativeMobiusComparison) -> NativeMobiusComparison:
        """Compose displacement classes; callers own endpoint/chart compatibility."""
        if not isinstance(after, NativeMobiusComparison):
            raise MobiusComparisonError("composition requires a NativeMobiusComparison")
        return NativeMobiusComparison((self.relative_turns + after.relative_turns) % 2)


def compare_native_mobius(
    source: NativeMobiusState,
    target: NativeMobiusState,
) -> NativeMobiusComparison:
    """Return the unique complete-state displacement class from source to target.

    Both states must already use the same identified native chart. No origin
    label, authorization, event, wire field, or transport edge is inferred.
    """
    return NativeMobiusComparison((_state_coordinate(target) - _state_coordinate(source)) % 2)


__all__ = [
    "COMPARISON_LAW_ID",
    "COMPARISON_LAW_VERSION",
    "COMPARISON_STANDING",
    "MobiusComparisonError",
    "NativeMobiusComparison",
    "compare_native_mobius",
]
