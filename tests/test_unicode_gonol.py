# === CHECKS ===
# id: unicode_space_relative_bearing_check
#   proves: unicode_scalar_has_one_space_relative_bearing
#   call: self::test_space_relative_bearings_are_exact_and_distinct
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_utf8_dual_view_check
#   proves: unicode_scalar_and_utf8_views_are_both_retained
#   call: self::test_scalar_and_utf8_views_are_both_retained
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_no_normalization_check
#   proves: unicode_scalar_sequence_is_not_normalized
#   call: self::test_precomposed_and_decomposed_sequences_remain_distinct
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_equal_radius_check
#   proves: unicode_scalar_frame_is_equal_radius
#   call: self::test_every_occurrence_uses_the_same_radius
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_fixed_bit_radius_check
#   proves: unicode_gonol_fixed_bit_radius
#   call: self::test_fixed_bit_radius_and_big_endian_diameter
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_big_endian_round_trip_check
#   proves: unicode_gonol_big_endian_round_trip
#   call: self::test_big_endian_diameter_recovery_and_rejection
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_width_placement_independence_check
#   proves: unicode_bit_radius_is_independent_of_placement
#   call: self::test_bit_radius_does_not_change_placement_or_truncate_text
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_ascii_anatomy_check
#   proves: unicode_scalar_and_utf8_views_are_both_retained, unicode_gonol_fixed_bit_radius
#   call: self::test_ascii_scalar_value_equals_single_utf8_byte
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_occurrence_order_check
#   proves: unicode_scalar_frame_is_equal_radius
#   call: self::test_repeated_occurrences_remain_separate
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_surrogate_rejection_check
#   proves: unicode_scalar_has_one_space_relative_bearing
#   call: self::test_surrogates_refuse
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_frame_input_rejection_check
#   proves: unicode_scalar_frame_is_equal_radius
#   call: self::test_empty_or_nontext_refuses
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_frame_exact_radius_check
#   proves: unicode_scalar_frame_is_equal_radius
#   call: self::test_nonexact_radius_refuses
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_record_boundary_check
#   proves: unicode_scalar_sequence_is_not_normalized
#   call: self::test_records_state_no_normalization_and_unresolved_next_scale_bearing
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# === END CHECKS ===
from fractions import Fraction

import pytest

from ucns.unicode_gonol import (
    UnicodeGlyphGonol,
    SPACE_SCALAR,
    UNICODE_SCALAR_MODULUS,
    build_unicode_scalar_frame,
    unicode_glyph_gonol,
    unicode_scalar_turn,
)


def test_space_relative_bearings_are_exact_and_distinct():
    assert unicode_scalar_turn(" ") == 0
    assert unicode_scalar_turn("!") == Fraction(1, UNICODE_SCALAR_MODULUS)
    assert unicode_scalar_turn("e") != unicode_scalar_turn("ë")
    assert unicode_scalar_turn(chr(0)) == Fraction(
        (-SPACE_SCALAR) % UNICODE_SCALAR_MODULUS, UNICODE_SCALAR_MODULUS
    )
    assert unicode_scalar_turn(chr(0x10FFFF)) == Fraction(
        (0x10FFFF - SPACE_SCALAR) % UNICODE_SCALAR_MODULUS,
        UNICODE_SCALAR_MODULUS,
    )


def test_ascii_scalar_value_equals_single_utf8_byte():
    for value in range(0x80):
        glyph = unicode_glyph_gonol(chr(value))
        assert glyph.scalar == value
        assert glyph.utf8 == bytes((value,))
        assert glyph.utf32_be == b"\x00\x00\x00" + bytes((value,))


def test_scalar_and_utf8_views_are_both_retained():
    e_diaeresis = unicode_glyph_gonol("ë")
    assert e_diaeresis.scalar == 0x00EB
    assert e_diaeresis.codepoint == "U+00EB"
    assert e_diaeresis.utf8 == bytes.fromhex("C3 AB")
    assert e_diaeresis.utf8_bits == ("11000011", "10101011")

    gothic = unicode_glyph_gonol("𐍈")
    assert gothic.scalar == 0x10348
    assert gothic.utf8 == bytes.fromhex("F0 90 8D 88")


def test_precomposed_and_decomposed_sequences_remain_distinct():
    precomposed = build_unicode_scalar_frame("é")
    decomposed = build_unicode_scalar_frame("e\u0301")
    assert precomposed.scalar_sequence == (0x00E9,)
    assert decomposed.scalar_sequence == (0x0065, 0x0301)
    assert precomposed.utf8 != decomposed.utf8
    assert precomposed.receipt != decomposed.receipt
    assert precomposed.recover() == "é"
    assert decomposed.recover() == "e\u0301"


def test_every_occurrence_uses_the_same_radius():
    frame = build_unicode_scalar_frame("eëé", radius=Fraction(7, 3))
    assert [placement.radius for placement in frame.placements] == [
        Fraction(7, 3),
        Fraction(7, 3),
        Fraction(7, 3),
    ]
    assert [placement.turn for placement in frame.placements] == [
        unicode_scalar_turn("e"),
        unicode_scalar_turn("ë"),
        unicode_scalar_turn("é"),
    ]


def test_repeated_occurrences_remain_separate():
    frame = build_unicode_scalar_frame("aaa")
    assert [p.ordinal for p in frame.placements] == [0, 1, 2]
    assert len(frame.glyphs) == 3
    assert frame.recover() == "aaa"


@pytest.mark.parametrize("text", ["\ud800", "\udfff"])
def test_surrogates_refuse(text):
    with pytest.raises(ValueError):
        build_unicode_scalar_frame(text)


@pytest.mark.parametrize("text", ["", None, 7])
def test_empty_or_nontext_refuses(text):
    with pytest.raises((ValueError, TypeError)):
        build_unicode_scalar_frame(text)


def test_nonexact_radius_refuses():
    with pytest.raises(ValueError):
        build_unicode_scalar_frame("A", radius=0.5)


def test_records_state_no_normalization_and_unresolved_next_scale_bearing():
    record = build_unicode_scalar_frame("A").record()
    assert record["normalization"] == "none"
    assert record["next_scale_bearing"] == "hmmm"


def test_fixed_bit_radius_and_big_endian_diameter():
    for value in (0, 0x7F, 0x80, 0x7FF, 0x800, 0xD7FF, 0xE000,
                  0xFEFF, 0xFFFF, 0x10000, 0x10348, 0x10FFFF):
        glyph = unicode_glyph_gonol(chr(value))
        assert glyph.bit_radius == 16
        assert glyph.bit_diameter == 32
        assert len(glyph.diameter_bits) == 32
        assert int(glyph.diameter_bits, 2) == value
        assert glyph.utf32_be == chr(value).encode("utf-32-be")
        assert len(glyph.utf32_be) == 4
        assert glyph.utf8.decode("utf-8") == chr(value)
        record = glyph.record()
        assert record["schema"] == "ucns.unicode-gonol.v2"
        assert (record["bit_radius"], record["bit_diameter"]) == (16, 32)
        assert record["diameter_encoding"] == "UTF-32BE"
        assert bytes(record["utf32_be_bytes"]) == glyph.utf32_be
        assert bytes.fromhex(record["utf32_be_hex"]) == glyph.utf32_be
        assert record["diameter_bits"] == glyph.diameter_bits
    assert unicode_glyph_gonol("ë").utf32_be == bytes.fromhex("00 00 00 EB")
    assert unicode_glyph_gonol("𐍈").utf32_be == bytes.fromhex("00 01 03 48")


def test_big_endian_diameter_recovery_and_rejection():
    for text in ("\x00", "A", "ë", "\u0301", "\ufeff", "𐍈", chr(0x10FFFF)):
        original = unicode_glyph_gonol(text)
        restored = UnicodeGlyphGonol.from_utf32_be(original.utf32_be)
        assert restored == original
        assert restored.record() == original.record()
    for data in (b"", b"A", bytes(3), bytes(5), bytes(8),
                 bytes.fromhex("00 00 D8 00"), bytes.fromhex("00 00 DF FF"),
                 bytes.fromhex("00 11 00 00"), bytes.fromhex("FF FF FF FF")):
        with pytest.raises(ValueError):
            UnicodeGlyphGonol.from_utf32_be(data)
    with pytest.raises(TypeError):
        UnicodeGlyphGonol.from_utf32_be("00000041")


def test_bit_radius_does_not_change_placement_or_truncate_text():
    text = "Aë𐍈e\u0301\x00" * 20
    small = build_unicode_scalar_frame(text, radius=Fraction(1, 3))
    large = build_unicode_scalar_frame(text, radius=Fraction(99))
    assert small.glyphs == large.glyphs
    assert all(g.bit_radius == 16 and g.bit_diameter == 32 for g in small.glyphs)
    assert all(p.radius == Fraction(1, 3) for p in small.placements)
    assert all(p.radius == Fraction(99) for p in large.placements)
    assert small.utf32_be == text.encode("utf-32-be")
    assert len(small.utf32_be) == 4 * len(text)
    assert small.recover() == text == large.recover()
    record = small.record()
    assert record["schema"] == "ucns.unicode-scalar-frame.v2"
    assert record["glyph_bit_radius"] == 16
    assert record["glyph_bit_diameter"] == 32
    assert bytes.fromhex(record["utf32_be_hex"]).decode("utf-32-be") == text
