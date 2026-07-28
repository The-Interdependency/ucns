# === CHECKS ===
# id: check_exact_public_gonol_fixture
#   proves: edcm_public_gonol_fixture_is_exact
#   call: self::test_public_gonol_fixture_is_exact
#   mutates: none
#   cleanup: none
#
# id: check_no_source_normalization
#   proves: edcm_source_text_is_not_normalized
#   call: self::test_source_text_is_exact_and_out_of_alphabet_is_retained
#   mutates: none
#   cleanup: none
#
# id: check_word_gonol_nesting
#   proves: edcm_word_is_the_smallest_gonol
#   call: self::test_words_are_gonols_and_each_space_is_a_nesting_boundary
#   mutates: none
#   cleanup: none
#
# id: check_space_manifestations_assign_to_origin
#   proves: edcm_space_manifestations_assign_to_origin
#   call: self::test_pinned_unicode_white_space_manifestations_assign_to_origin
#   mutates: none
#   cleanup: none
#
# id: check_space_origin_segmentation_preserves_source
#   proves: edcm_space_manifestations_assign_to_origin
#   call: self::test_space_manifestations_split_words_without_rewriting_source
#   mutates: none
#   cleanup: none
#
# id: check_space_assignment_pin_is_runtime_independent
#   proves: edcm_space_manifestations_assign_to_origin
#   call: self::test_runtime_isspace_does_not_expand_the_pinned_profile
#   mutates: none
#   cleanup: none
#
# id: check_turn_unit_support
#   proves: edcm_speaker_turn_has_unit_support
#   call: self::test_one_turn_is_one_unit_regardless_of_text_extent
#   mutates: none
#   cleanup: none
#
# id: check_full_corpus_iteration
#   proves: edcm_alphabet_failure_is_positive_evidence
#   call: self::test_observe_corpus_runs_every_turn_without_sampling
#   mutates: none
#   cleanup: none
#
# id: check_profile_options_fail_closed
#   proves: edcm_source_text_is_not_normalized
#   call: self::test_profile_options_fail_closed
#   mutates: none
#   cleanup: none
#
# id: check_strict_utf8_decoding
#   proves: edcm_source_text_is_not_normalized
#   call: self::test_utf8_decoding_is_strict
#   mutates: none
#   cleanup: none
#
# id: check_carrier_assignment_terms
#   proves: edcm_space_manifestations_assign_to_origin
#   call: self::test_carrier_assignment_terms_distinguish_fixture_membership
#   mutates: none
#   cleanup: none
#
# id: check_valid_unassigned_scalars_are_retained
#   proves: edcm_alphabet_failure_is_positive_evidence
#   call: self::test_non_space_unicode_scalars_remain_exact_unassigned_evidence
#   mutates: none
#   cleanup: none
#
# id: check_surrogates_fail_closed
#   proves: edcm_source_text_is_not_normalized
#   call: self::test_surrogate_code_points_are_rejected_at_text_boundaries
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import unicodedata

import pytest

from ucns.edcm import (
    EDCM_CORPUS_EXECUTION,
    EDCM_GONOL_INITIATION,
    EDCM_NORMALIZATION_POLICY,
    EDCM_PROFILE_OPTIONS,
    EDCM_PROFILE_VERSION,
    EDCM_SOURCE_DOMAIN,
    EDCM_SPACE_ASSIGNMENT_POLICY,
    EDCM_SPACE_CODE_POINTS,
    PUBLIC_GONOL_157,
    PUBLIC_GONOL_SHA256,
    EdcmProfileError,
    EdcmWordGonolProfile,
    SuperpositionedSpaceBoundary,
    decode_utf8_exact,
    edcm_carrier_position,
    public_gonol_sha256,
)


def test_public_gonol_fixture_is_exact() -> None:
    assert EDCM_PROFILE_VERSION == "0.2.0"
    assert EDCM_SOURCE_DOMAIN == "unicode-scalar-values"
    assert len(EDCM_PROFILE_OPTIONS) == 14
    assert len(PUBLIC_GONOL_157) == 157
    assert len(set(PUBLIC_GONOL_157)) == 157
    assert all(len(token) == 1 for token in PUBLIC_GONOL_157)
    assert PUBLIC_GONOL_157[0] == " "
    assert PUBLIC_GONOL_157.index("0") == 139
    assert public_gonol_sha256() == PUBLIC_GONOL_SHA256
    assert all(unicodedata.normalize("NFC", token) == token for token in PUBLIC_GONOL_157)


def test_source_text_is_exact_and_out_of_alphabet_is_retained() -> None:
    profile = EdcmWordGonolProfile()
    text = decode_utf8_exact("café 👩‍💻".encode("utf-8"))
    observed = profile.observe_turn(speaker_id="speaker", turn_index=0, text=text)
    assert observed.raw_text == text
    assert "".join(token.value for token in observed.tokens) == text
    assert tuple(word.raw_text for word in observed.word_gonols) == (
        "café",
        "👩\u200d💻",
    )
    assert tuple(
        token.value for token in observed.word_gonols[1].carrier_unassigned
    ) == ("👩", "\u200d", "💻")
    assert [token.value for token in observed.out_of_alphabet] == ["é", "👩", "\u200d", "💻"]
    assert unicodedata.normalize("NFD", text) != text


def test_words_are_gonols_and_each_space_is_a_nesting_boundary() -> None:
    observed = EdcmWordGonolProfile().observe_turn(
        speaker_id="speaker",
        turn_index=0,
        text="Alpha  beta",
    )
    assert [word.raw_text for word in observed.word_gonols] == ["Alpha", "beta"]
    assert all(
        word.initiation_event == EDCM_GONOL_INITIATION
        for word in observed.word_gonols
    )
    assert len(observed.nesting_boundaries) == 2
    assert all(
        isinstance(boundary, SuperpositionedSpaceBoundary)
        for boundary in observed.nesting_boundaries
    )
    assert [segment.raw_text for segment in observed.segments] == [
        "Alpha",
        " ",
        " ",
        "beta",
    ]


def test_pinned_unicode_white_space_manifestations_assign_to_origin() -> None:
    expected_code_points = (
        "U+0009",
        "U+000A",
        "U+000B",
        "U+000C",
        "U+000D",
        "U+0020",
        "U+0085",
        "U+00A0",
        "U+1680",
        "U+2000",
        "U+2001",
        "U+2002",
        "U+2003",
        "U+2004",
        "U+2005",
        "U+2006",
        "U+2007",
        "U+2008",
        "U+2009",
        "U+200A",
        "U+2028",
        "U+2029",
        "U+202F",
        "U+205F",
        "U+3000",
    )
    assert EDCM_SPACE_ASSIGNMENT_POLICY == "unicode-white-space-origin-v1"
    assert tuple(f"U+{ord(value):04X}" for value in EDCM_SPACE_CODE_POINTS) == (
        expected_code_points
    )

    text = "".join(EDCM_SPACE_CODE_POINTS)
    observed = EdcmWordGonolProfile().observe_turn(
        speaker_id="speaker",
        turn_index=0,
        text=text,
    )
    assert observed.raw_text == text
    assert "".join(token.value for token in observed.tokens) == text
    assert len(observed.nesting_boundaries) == len(EDCM_SPACE_CODE_POINTS)
    assert not observed.word_gonols
    assert not observed.out_of_alphabet
    assert all(token.alphabet_position == 0 for token in observed.tokens)
    assert all(token.has_carrier_assignment for token in observed.tokens)
    assert all(token.carrier_token == " " for token in observed.tokens)
    assert all(token.is_space for token in observed.tokens)
    assert [token.code_point for token in observed.tokens] == list(
        expected_code_points
    )
    assert [token.codepoint_offset for token in observed.tokens] == list(
        range(len(EDCM_SPACE_CODE_POINTS))
    )
    assert all(edcm_carrier_position(value) == 0 for value in EDCM_SPACE_CODE_POINTS)
    assert observed.has_complete_carrier_assignment
    assert observed.has_complete_alphabet_coverage


def test_carrier_assignment_terms_distinguish_fixture_membership() -> None:
    observed = EdcmWordGonolProfile().observe_turn(
        speaker_id="speaker",
        turn_index=0,
        text=" \u00a0",
    )
    ascii_space, no_break_space = observed.tokens
    assert ascii_space.is_public_gonol_token
    assert no_break_space.has_carrier_assignment
    assert no_break_space.in_alphabet
    assert not no_break_space.is_public_gonol_token
    assert no_break_space.carrier_token == " "
    assert observed.has_complete_carrier_assignment
    assert observed.has_complete_alphabet_coverage
    assert observed.carrier_unassigned == observed.out_of_alphabet == ()


def test_space_manifestations_split_words_without_rewriting_source() -> None:
    text = "alpha\tbeta\ngamma\u00a0delta"
    observed = EdcmWordGonolProfile().observe_turn(
        speaker_id="speaker",
        turn_index=0,
        text=text,
    )
    assert [word.raw_text for word in observed.word_gonols] == [
        "alpha",
        "beta",
        "gamma",
        "delta",
    ]
    assert [boundary.raw_text for boundary in observed.nesting_boundaries] == [
        "\t",
        "\n",
        "\u00a0",
    ]
    assert [
        boundary.token.codepoint_offset
        for boundary in observed.nesting_boundaries
    ] == [
        5,
        10,
        16,
    ]
    assert "".join(segment.raw_text for segment in observed.segments) == text
    assert not observed.out_of_alphabet


def test_runtime_isspace_does_not_expand_the_pinned_profile() -> None:
    # Python classifies U+001C as whitespace, but Unicode White_Space does not.
    source_separator = "\u001c"
    assert source_separator.isspace()
    assert source_separator not in EDCM_SPACE_CODE_POINTS
    assert edcm_carrier_position(source_separator) is None
    observed = EdcmWordGonolProfile().observe_turn(
        speaker_id="speaker",
        turn_index=0,
        text=f"a{source_separator}b",
    )
    assert [word.raw_text for word in observed.word_gonols] == [
        f"a{source_separator}b"
    ]
    assert [token.value for token in observed.out_of_alphabet] == [source_separator]


def test_non_space_unicode_scalars_remain_exact_unassigned_evidence() -> None:
    source_values = ("\uE000", "\u0378", "\uFDD0")
    text = "".join(source_values)
    observed = EdcmWordGonolProfile().observe_turn(
        speaker_id="speaker",
        turn_index=0,
        text=text,
    )
    assert observed.raw_text == text
    assert "".join(token.value for token in observed.tokens) == text
    assert tuple(token.value for token in observed.carrier_unassigned) == source_values
    assert observed.carrier_unassigned == observed.out_of_alphabet
    assert not observed.has_complete_carrier_assignment
    assert not observed.has_complete_alphabet_coverage
    assert len(observed.word_gonols) == 1
    assert observed.word_gonols[0].carrier_unassigned == (
        observed.word_gonols[0].out_of_alphabet
    )
    assert all(not token.has_carrier_assignment for token in observed.tokens)
    assert all(not token.in_alphabet for token in observed.tokens)
    assert all(not token.is_public_gonol_token for token in observed.tokens)
    assert all(token.carrier_token is None for token in observed.tokens)
    assert all(not token.is_space for token in observed.tokens)


def test_surrogate_code_points_are_rejected_at_text_boundaries() -> None:
    surrogate = "\uD800"
    with pytest.raises(EdcmProfileError, match="Unicode scalar"):
        edcm_carrier_position(surrogate)
    with pytest.raises(EdcmProfileError, match="Unicode scalar"):
        EdcmWordGonolProfile().observe_turn(
            speaker_id="speaker",
            turn_index=0,
            text=surrogate,
        )
    with pytest.raises(UnicodeDecodeError):
        decode_utf8_exact(b"\xED\xA0\x80")


def test_one_turn_is_one_unit_regardless_of_text_extent() -> None:
    profile = EdcmWordGonolProfile()
    empty = profile.observe_turn(speaker_id="a", turn_index=0, text="")
    long = profile.observe_turn(speaker_id="b", turn_index=1, text="a b c d")
    assert empty.unit_support == long.unit_support == 1.0
    assert len(empty.word_gonols) == 0
    assert len(long.word_gonols) == 4


def test_observe_corpus_runs_every_turn_without_sampling() -> None:
    turns = [("a", "one"), ("b", "two"), ("a", "three")]
    observed = list(EdcmWordGonolProfile().observe_corpus(turns, source_id="fixture"))
    assert EDCM_CORPUS_EXECUTION == "full-corpus"
    assert len(observed) == len(turns)
    assert [turn.turn_index for turn in observed] == [0, 1, 2]
    assert [turn.source_id for turn in observed] == ["fixture"] * 3


def test_profile_options_fail_closed() -> None:
    options = dict(EDCM_PROFILE_OPTIONS)
    options["normalization"] = "NFKC"
    with pytest.raises(EdcmProfileError, match="options"):
        EdcmWordGonolProfile(options=tuple(sorted(options.items())))


def test_utf8_decoding_is_strict() -> None:
    assert EDCM_NORMALIZATION_POLICY == "none-preserve-source"
    with pytest.raises(UnicodeDecodeError):
        decode_utf8_exact(b"\xff")
