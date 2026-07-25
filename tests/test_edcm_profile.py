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
# === END CHECKS ===

import unicodedata

import pytest

from ucns.edcm import (
    EDCM_CORPUS_EXECUTION,
    EDCM_GONOL_INITIATION,
    EDCM_NORMALIZATION_POLICY,
    EDCM_PROFILE_OPTIONS,
    PUBLIC_GONOL_157,
    PUBLIC_GONOL_SHA256,
    EdcmProfileError,
    EdcmWordGonolProfile,
    SuperpositionedSpaceBoundary,
    decode_utf8_exact,
    public_gonol_sha256,
)


def test_public_gonol_fixture_is_exact() -> None:
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
