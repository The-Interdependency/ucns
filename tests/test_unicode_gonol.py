# ratios: loc_comments=75:72 imports_exports=3:10 calls_definitions=35:10
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
# id: unicode_ascii_utf8_identity_check
#   proves: unicode_scalar_and_utf8_views_are_both_retained
#   call: self::test_ascii_scalar_value_equals_single_utf8_byte
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_repeated_occurrences_check
#   proves: unicode_scalar_and_utf8_views_are_both_retained
#   call: self::test_repeated_occurrences_remain_separate
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_surrogate_refusal_check
#   proves: unicode_scalar_frame_rejects_invalid_text
#   call: self::test_surrogates_refuse
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_invalid_text_refusal_check
#   proves: unicode_scalar_frame_rejects_invalid_text
#   call: self::test_empty_or_nontext_refuses
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_inexact_radius_refusal_check
#   proves: unicode_scalar_frame_rejects_inexact_radius
#   call: self::test_nonexact_radius_refuses
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_unresolved_bearing_record_check
#   proves: unicode_scalar_frame_preserves_unresolved_bearing
#   call: self::test_records_state_no_normalization_and_unresolved_next_scale_bearing
#   requires: python3, pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# === END CHECKS ===
from fractions import Fraction

import pytest

from ucns.unicode_gonol import (
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
# ratios: loc_comments=75:72 imports_exports=3:10 calls_definitions=35:10
