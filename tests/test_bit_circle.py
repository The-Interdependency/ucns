# ratios: loc_comments=143:61 imports_exports=4:7 calls_definitions=102:7
# === CHECKS ===
# id: check_bit_circle_all_bytes
#   proves: bit_circle_exact_recovery, bit_circle_frame_transport
#   call: self::test_all_bytes_recover_from_unordered_marks_in_both_orientations
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_bit_circle_sums
#   proves: bit_circle_sum_is_projection
#   call: self::test_byte_sum_census_and_equal_sum_counterexample
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_bit_circle_addresses
#   proves: bit_circle_exact_recovery, bit_circle_frame_transport
#   call: self::test_address_identity_and_non_byte_widths
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_bit_circle_frame_loss
#   proves: bit_circle_frame_transport
#   call: self::test_moving_marks_without_frame_changes_readback
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_bit_circle_invalid
#   proves: bit_circle_rejects_incomplete_geometry
#   call: self::test_invalid_geometry_is_rejected
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_bit_circle_binary_boundary
#   proves: bit_circle_binary_boundary, bit_circle_exact_recovery, bit_circle_frame_transport, bit_circle_rejects_incomplete_geometry
#   call: self::test_binary_weighted_locations_and_sum_readback
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_bit_circle_binary_concatenation
#   proves: bit_circle_binary_boundary
#   call: self::test_binary_sum_concatenation_preserves_order_and_grouping
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# === END CHECKS ===
"""Geometric byte census. Run: python -m pytest tests/test_bit_circle.py.

GPT generated; context, prompt Erin Spencer.
These tests establish exact finite-circle placement/readback and deliberately
falsify uniqueness of the summed-angle projection. They do not test program
semantics, compression, physical memory, or a recursive attachment law.
"""
from fractions import Fraction as F
from itertools import product

import pytest

from ucns.bit_circle import BitCircle, read_bit_circle, read_binary_angle


def test_all_bytes_recover_from_unordered_marks_in_both_orientations():
    seen = set()
    for number in range(256):
        bits = tuple((number >> (7 - i)) & 1 for i in range(8))
        for orientation in (-1, 1):
            for space in (F(0), F(1, 7), F(7, 8)):
                circle = BitCircle('a' * 64, bits, space, orientation)
                # Serialize only geometry/state, reorder it, and read without
                # passing the source bits or stored axis ordinals to the reader.
                marks = tuple(sorted(circle.marks, reverse=True))
                recovered = read_bit_circle(marks, width=8, space=space,
                                            orientation=orientation)
                assert recovered == bits
                assert sum(bit << (7 - i) for i, bit in enumerate(recovered)) == number
                assert {t for t, _ in marks} == {
                    (space + orientation * F(i, 8)) % 1 for i in range(8)}
        seen.add(circle.bits)
    assert len(seen) == 256


def test_byte_sum_census_and_equal_sum_counterexample():
    sums, bearings = set(), set()
    for bits in product((0, 1), repeat=8):
        circle = BitCircle('a' * 64, bits)
        total = circle.occupied_turn_sum
        assert total == F(sum(i * bits[i] for i in range(8)), 8)
        sums.add(total)
        bearings.add(total % 1)
    assert len(sums) == 29
    assert len(bearings) == 8
    a = BitCircle('a' * 64, (1, 0, 0, 0, 0, 0, 0, 1))
    b = BitCircle('a' * 64, (0, 1, 0, 0, 0, 0, 1, 0))
    assert a.occupied_turn_sum == b.occupied_turn_sum == F(7, 8)
    assert a.marks != b.marks and a.positions == b.positions
    assert read_bit_circle(a.marks, width=8) != read_bit_circle(b.marks, width=8)


def test_address_identity_and_non_byte_widths():
    a = BitCircle('a' * 64, (0, 0, 0))
    b = BitCircle('a' * 64, (1, 1, 1), F(1, 9), -1)
    assert a.positions == b.positions
    assert a.positions[2].turn == F(2, 3)
    assert a.positions[0].identity_sha256 != BitCircle('b' * 64, a.bits).positions[0].identity_sha256
    assert a.positions[0].identity_sha256 != BitCircle('a' * 64, (0, 0)).positions[0].identity_sha256
    for width in (1, 2, 3, 16, 64):
        bits = tuple(i % 2 for i in range(width))
        circle = BitCircle('a' * 64, bits, F(-2, 7), -1)
        assert read_bit_circle(tuple(reversed(circle.marks)), width=width,
                               space=F(-2, 7), orientation=-1) == bits


def test_moving_marks_without_frame_changes_readback():
    bits = (1, 0, 0, 1, 0, 0, 0, 0)
    circle = BitCircle('a' * 64, bits)
    moved = tuple(((t + F(1, 8)) % 1, v) for t, v in circle.marks)
    assert read_bit_circle(moved, width=8, space=F(1, 8)) == bits
    assert read_bit_circle(moved, width=8) == (0,) + bits[:-1]
    reflected = tuple((-t % 1, v) for t, v in circle.marks)
    assert read_bit_circle(reflected, width=8, orientation=-1) == bits
    assert read_bit_circle(reflected, width=8) == bits[:1] + bits[:0:-1]
    assert read_bit_circle(reflected, width=8) != bits


def test_invalid_geometry_is_rejected():
    for bits in ((), [0, 1], (True,), (0.0,), (2,), ('1',)):
        with pytest.raises(ValueError):
            BitCircle('a' * 64, bits)
    with pytest.raises(ValueError):
        BitCircle('unbound-origin', (0, 1))
    for orientation in (0, 2, True, 1.0):
        with pytest.raises(ValueError):
            BitCircle('a' * 64, (0, 1), orientation=orientation)
        with pytest.raises(ValueError):
            read_bit_circle(((0, 0), (F(1, 2), 1)), width=2, orientation=orientation)
    for space in (True, 0.0, '0'):
        with pytest.raises(ValueError):
            BitCircle('a' * 64, (0, 1), space=space)
        with pytest.raises(ValueError):
            read_bit_circle(((0, 0), (F(1, 2), 1)), width=2, space=space)
    for width in (0, -1, True, 2.0):
        with pytest.raises(ValueError):
            read_bit_circle((), width=width)
    for marks in (
        ((0, 1),),
        ((0, 1), (0, 0)),
        ((0, 1), (F(1, 3), 0)),
        ((0, 1), (1, 0)),
        ((0, 1), (F(-1, 2), 0)),
        ((0, 1), (0.5, 0)),
        ((True, 1), (F(1, 2), 0)),
        ((0, 1), (F(1, 2), True)),
        ((0, 1), (F(1, 2), 2)),
        ((0, 1), (F(1, 2),)),
        [(0, 1), (F(1, 2), 0)],
    ):
        with pytest.raises(ValueError):
            read_bit_circle(marks, width=2)


def test_binary_weighted_locations_and_sum_readback():
    sums = set()
    for number in range(256):
        bits = tuple((number >> (7 - i)) & 1 for i in range(8))
        for orientation in (-1, 1):
            circle = BitCircle('a' * 64, bits, F(1, 7), orientation, 'binary-v1')
            assert tuple(p.turn for p in circle.positions) == tuple(F(1, 2 ** (i + 1)) for i in range(8))
            assert circle.occupied_turn_sum == F(number, 256)
            assert read_binary_angle(circle.occupied_turn_sum, width=8) == bits
            assert read_bit_circle(tuple(reversed(circle.marks)), width=8,
                                   space=F(1, 7), orientation=orientation,
                                   placement='binary-v1') == bits
        sums.add(circle.occupied_turn_sum)
    assert len(sums) == 256
    assert read_binary_angle(F(1, 2), width=1) == (1,)
    assert read_binary_angle(F(1, 2), width=2) == (1, 0)
    for turn in (F(1, 3), F(1, 512), -1, 1, True, 0.5):
        with pytest.raises(ValueError):
            read_binary_angle(turn, width=8)
    for width in (0, -1, True, 2.0):
        with pytest.raises(ValueError):
            read_binary_angle(0, width=width)
    for marks in (((0, 0), (F(1, 2), 1)),
                  ((F(1, 2), 0), (F(1, 8), 1)),
                  ((F(1, 2), 0), (F(1, 3), 1))):
        with pytest.raises(ValueError):
            read_bit_circle(marks, width=2, placement='binary-v1')
    for placement in ('automatic', '', None):
        with pytest.raises(ValueError):
            BitCircle('a' * 64, (0, 1), placement=placement)
        with pytest.raises(ValueError):
            read_bit_circle(((0, 0), (F(1, 2), 1)), width=2, placement=placement)


def test_binary_sum_concatenation_preserves_order_and_grouping():
    # Freeze the byte summaries from the geometric producer, then recover every
    # ordered byte pair from the scale-composed boundary without their marks.
    circles = [BitCircle('a' * 64, tuple((n >> (7 - i)) & 1 for i in range(8)),
                         placement='binary-v1') for n in range(256)]
    sums = [c.occupied_turn_sum for c in circles]
    for a, b in product(range(256), repeat=2):
        combined = sums[a] + sums[b] / 256
        assert read_binary_angle(combined, width=16) == circles[a].bits + circles[b].bits
        assert combined == F((a << 8) | b, 65536)
    a = BitCircle('a' * 64, (1, 0), placement='binary-v1')
    b = BitCircle('b' * 64, (0, 1), placement='binary-v1')
    c = BitCircle('c' * 64, (1, 1, 0), placement='binary-v1')
    x, y, z = a.occupied_turn_sum, b.occupied_turn_sum, c.occupied_turn_sum
    assert x + y / 4 == F(9, 16)
    assert y + x / 4 == F(6, 16)
    left_grouped = (x + y / 4) + z / 16
    right_grouped = x + (y + z / 4) / 4
    assert left_grouped == right_grouped
    parent = BitCircle('d' * 64, a.bits + b.bits + c.bits, placement='binary-v1')
    assert parent.occupied_turn_sum == left_grouped
    assert read_binary_angle(left_grouped, width=7) == parent.bits
# ratios: loc_comments=143:61 imports_exports=4:7 calls_definitions=102:7
