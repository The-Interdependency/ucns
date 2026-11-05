# ratios: loc_comments=90:67 imports_exports=4:3 calls_definitions=48:9
# === MODULE_BUILD ===
# id: ucns_bit_circle_candidate
#   module_name: bit_circle
#   module_kind: engine
#   summary: exact binary states at individually identified finite-circle positions
#   owner: Erin Spencer
#   public_surface: BitCircle, read_bit_circle, read_binary_angle
#   internal_surface: exact frame and state validation
#   auth_boundary: none
#   storage_boundary: immutable in-memory geometry only
#   network_boundary: none
#   user_data_boundary: caller-supplied bits and origin remain in memory
#   admin_only: false
#   tests: tests/test_bit_circle.py
#   rollout: opt-in visible-circle candidate; no implicit attachment bearing
#   rollback: remove this module and its consumer imports; existing carriers are unchanged
#   requires: ucns_axis_circle_position_candidate
#   unresolved: recursive attachment law, native Mobius lift, domain relationship meanings
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: bit_circle_exact_recovery
#   given: a nonempty ordered binary state and explicit circle frame
#   then: every bit including zero has an exact native axis-circle address; unordered placed marks recover the complete ordered state
# id: bit_circle_frame_transport
#   given: the marks and their SPACE direction and orientation are transported together
#   then: exact readback and local address identities are preserved
# id: bit_circle_sum_is_projection
#   given: binary states under equal-v1 placement
#   then: the occupied local-angle sum is exact but need not distinguish states, even before reduction modulo one turn
# id: bit_circle_binary_boundary
#   given: binary-v1 placement with N bits at 1/2 through 1/2^N turns
#   then: the exact occupied-angle sum and width recover every bit; ordered concatenation has sum a + b/2^N for left width N
# id: bit_circle_rejects_incomplete_geometry
#   given: missing, duplicate, off-grid, inexact, or non-binary marks or an invalid frame
#   then: readback rejects rather than inventing bits or a reading order
# === END CONTRACTS ===
"""Binary state on an exact finite circumference; an unselected UCNS candidate.

GPT generated; context, prompt Erin Spencer.

Usage::

    circle = BitCircle('a' * 64, (1, 0, 0, 0, 0, 0, 0, 1))
    recovered = read_bit_circle(circle.marks, width=8)
    assert recovered == circle.bits

The origin SHA-256 identifies the caller's ordered carrier, not an inferred
meaning. equal-v1 uses k/N turns; binary-v1 uses 1/2^(k+1) turns, in descending
binary significance. These are separate named candidates. Byte/text meaning
belongs to the caller.
SPACE is an angular reference, not a stored bit or Structural Null. Every zero
is present explicitly. Angles are exact rational turns on the visible circle;
neither a native Mobius lift nor a closed-stack attachment is selected here.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction

from .axis_circle import AxisCirclePosition, build_axis_circle_position


def _exact(value):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError('exact integer or Fraction required')
    return Fraction(value)


def _frame(width, space, orientation, placement):
    if type(width) is not int or width <= 0:
        raise ValueError('positive integer width required')
    if type(orientation) is not int or orientation not in (-1, 1):
        raise ValueError('orientation must be +1 or -1')
    if placement not in ('equal-v1', 'binary-v1'):
        raise ValueError('placement must be equal-v1 or binary-v1')
    return _exact(space) % 1


def _bit(value):
    if type(value) is not int or value not in (0, 1):
        raise ValueError('bit state must be integer 0 or 1')
    return value


@dataclass(frozen=True, slots=True)
class BitCircle:
    """One explicit 0/1 state at each position of a declared finite bit carrier.

    Local address identity is independent of bit state and displayed frame.
    Changing the owner origin or width changes the address identities.
    """

    origin_sha256: str
    bits: tuple[int, ...]
    space: Fraction = Fraction(0)
    orientation: int = 1
    placement: str = 'equal-v1'
    positions: tuple[AxisCirclePosition, ...] = field(init=False)

    def __post_init__(self):
        if not isinstance(self.bits, tuple) or not self.bits:
            raise ValueError('nonempty immutable bit tuple required')
        width = len(self.bits)
        space = _frame(width, self.space, self.orientation, self.placement)
        for value in self.bits:
            _bit(value)
        count = width if self.placement == 'equal-v1' else 1 << width
        ordinals = range(width) if self.placement == 'equal-v1' else (
            1 << (width - i - 1) for i in range(width))
        positions = tuple(build_axis_circle_position(
            origin_sha256=self.origin_sha256,
            axis_count=count, axis_ordinal=i,
        ) for i in ordinals)
        object.__setattr__(self, 'space', space)
        object.__setattr__(self, 'positions', positions)

    @property
    def marks(self):
        """Exact placed (turn, bit) pairs, including unoccupied/zero states."""
        return tuple(((self.space + self.orientation * pos.turn) % 1, bit)
                     for pos, bit in zip(self.positions, self.bits))

    @property
    def occupied_turn_sum(self):
        """Sum local angles of 1 states; sufficiency depends on placement/width."""
        return sum((pos.turn for pos, bit in zip(self.positions, self.bits) if bit),
                   Fraction(0))


def read_bit_circle(marks, *, width, space=Fraction(0), orientation=1,
                    placement='equal-v1'):
    """Recover bits from a complete unordered set of exact placed circle marks.

    Supply the frame used to place the marks. Moving marks without their frame
    changes the read state. Missing zeros, duplicates, noncanonical turns, and
    marks between declared positions are errors; reading does not infer them.
    This reads state only. Preserve the owning origin separately for identity.
    """
    space = _frame(width, space, orientation, placement)
    if not isinstance(marks, tuple) or len(marks) != width:
        raise ValueError('one mark per declared position required')
    values = {}
    for mark in marks:
        if not isinstance(mark, tuple) or len(mark) != 2:
            raise ValueError('each mark must be a (turn, bit) tuple')
        turn, bit = mark
        turn, bit = _exact(turn), _bit(bit)
        if not 0 <= turn < 1:
            raise ValueError('mark turns must be canonical in [0, 1)')
        local = (turn - space) * orientation % 1
        if placement == 'equal-v1':
            ordinal = local * width
            if ordinal.denominator != 1:
                raise ValueError('mark is outside the declared circle grid')
            i = ordinal.numerator
        else:
            denominator = local.denominator
            i = denominator.bit_length() - 2
            if (local.numerator != 1 or denominator & (denominator - 1)
                    or not 0 <= i < width):
                raise ValueError('mark is outside the binary-weighted positions')
        if i in values:
            raise ValueError('duplicate circle position')
        values[i] = bit
    return tuple(values[i] for i in range(width))


def read_binary_angle(turn, *, width):
    """Recover binary-v1 state from its exact local sum and explicit bit width.

    This reads the local occupied-angle sum, not a world-frame direction.
    Example: read_binary_angle(Fraction(129, 256), width=8).
    Width preserves leading/trailing zero distinctions across carrier sizes.
    """
    _frame(width, 0, 1, 'binary-v1')
    turn = _exact(turn)
    if not 0 <= turn < 1:
        raise ValueError('binary sum must be in [0, 1)')
    number = turn * (1 << width)
    if number.denominator != 1:
        raise ValueError('sum is outside the declared binary grid')
    return tuple((number.numerator >> (width - i - 1)) & 1 for i in range(width))
# ratios: loc_comments=90:67 imports_exports=4:3 calls_definitions=48:9
