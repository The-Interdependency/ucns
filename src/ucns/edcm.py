# === MODULE_BUILD ===
# id: edcm_word_gonol_profile
#   module_name: edcm
#   module_kind: schema
#   summary: exact EDCM observation profile with word gonols, source-preserving SPACE-origin nesting boundaries, and one unit of support per speaker turn
#   owner: Erin Spencer
#   public_surface: EdcmWordGonolProfile, EdcmTurnObservation, EdcmWordGonol, SuperpositionedSpaceBoundary, EdcmTokenObservation, PUBLIC_GONOL_157, EDCM_SOURCE_DOMAIN, EDCM_SPACE_CODE_POINTS, EDCM_SPACE_ASSIGNMENT_POLICY, edcm_carrier_position
#   internal_surface: _token_observation
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: source text remains exact; pinned Unicode White_Space manifestations retain their raw source identity while assigning to carrier origin; non-SPACE out-of-alphabet code points are retained and reported
#   admin_only: false
#   tests: tests/test_edcm_profile.py
#   rollout: experimental EDCM-only corpus observation profile; no universal UCNS or METAPAT selection
#   rollback: remove this profile without changing the combined compatibility profile
#   since: 2026-07-25
#   unresolved: formal Mobius carrier coordinates, higher-gonol composition laws, and treatment of non-SPACE out-of-alphabet evidence
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: edcm_public_gonol_fixture_is_exact
#   given: the EDCM token alphabet is imported
#   then: all 157 unique one-code-point tokens, SPACE at position zero, digit zero away from the origin, source provenance, and digest match exactly
#   class: correctness
#   since: 2026-07-25
#
# id: edcm_source_text_is_not_normalized
#   given: UTF-8 corpus bytes or a Unicode speaker turn enter the profile
#   then: decoding is strict, source code points remain byte-round-trippable, and the SPACE-origin carrier assignment never rewrites, normalizes, collapses, or folds source text
#   class: evidence
#   since: 2026-07-25
#
# id: edcm_space_manifestations_assign_to_origin
#   given: a source code point belongs to the profile-pinned Unicode White_Space set
#   then: its exact source value, code point, and offset are preserved while its carrier token is U+0020 SPACE at public-gonol position zero
#   class: doctrine
#   since: 2026-07-28
#
# id: edcm_word_is_the_smallest_gonol
#   given: a speaker turn contains SPACE manifestations and non-SPACE code points
#   then: maximal ordered non-SPACE sequences initiate word gonols through the declared Mobius twist and every SPACE manifestation remains an explicit superpositioned nesting boundary
#   class: doctrine
#   since: 2026-07-25
#
# id: edcm_speaker_turn_has_unit_support
#   given: any speaker turn, including an empty or alphabet-incomplete turn
#   then: the complete turn has support one while token and word counts do not alter support
#   class: doctrine
#   since: 2026-07-25
#
# id: edcm_alphabet_failure_is_positive_evidence
#   given: a non-SPACE corpus code point has no assignment in the exact 157-position carrier
#   then: it remains in position as out-of-alphabet evidence and is never dropped, replaced, coerced, or used to silently reject the turn
#   class: safety
#   since: 2026-07-25
# === END CONTRACTS ===

"""EDCM-specific word-gonol corpus observation profile.

This module makes the smallest currently lawful EDCM structure executable:

* the exact public 157-position gonol is the token alphabet;
* source Unicode scalar values are preserved without normalization and
  surrogates are rejected;
* a profile-pinned Unicode White_Space set assigns to the U+0020 origin without
  rewriting source code points;
* maximal non-SPACE sequences are word gonols;
* every SPACE manifestation remains an explicit superpositioned nesting boundary;
* each new word gonol records the initiating Möbius twist;
* one complete speaker turn has one unit of support; and
* non-SPACE out-of-alphabet code points are retained as failures of alphabet
  coverage.

It does not invent the unresolved Möbius coordinate construction or higher-gonol
composition law. Recording an initiation event is not a claim that those
mathematics have been supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Iterable, Iterator, TypeAlias


EDCM_PROFILE_ID = "ucns.profile.edcm-word-gonol"
EDCM_PROFILE_VERSION = "0.2.0"
EDCM_PROFILE_SCOPE = "edcm-only"
EDCM_NORMALIZATION_POLICY = "none-preserve-source"
EDCM_SUPPORT_POLICY = "one-unit-per-speaker-turn"
EDCM_CORPUS_EXECUTION = "full-corpus"
EDCM_SMALLEST_GONOL = "word"
EDCM_GONOL_INITIATION = "mobius-twist"
EDCM_SOURCE_DOMAIN = "unicode-scalar-values"
EDCM_SPACE_ASSIGNMENT_POLICY = "unicode-white-space-origin-v1"

PUBLIC_GONOL_SOURCE_REPOSITORY = "The-Interdependency/a0-betatest"
PUBLIC_GONOL_SOURCE_COMMIT = "7af8debf6ef3905f01baff02b43d8c3bee16ccbc"
PUBLIC_GONOL_SOURCE_PATH = "backend/interdependent_lib/gonal/gonal.py"
PUBLIC_GONOL_SHA256 = (
    "55d10c84529a4d7bc7714786357e977b68d9df2ac3f73d20e229580b552c2ef5"
)

PUBLIC_GONOL_157: tuple[str, ...] = (
    " ", "A", "!", '"', "B", "#", "$", "C", "%", "(", "D", "&", "'", "E", "1", "*",
    "F", "+", "[", "G", ",", "-", "H", ".", "/", "I", "3", "{", "J", ":", ";", "K",
    "=", "?", "L", "<", "@", "M", "5", "\\", "N", "^", "_", "O", "‘", "`", "P", "|",
    "~", "Q", "7", "…", "R", "“", "—", "S", "–", "·", "T", "°", "«", "U", "9", "±",
    "V", "×", "÷", "W", "√", "∂", "X", "∫", "∑", "Y", "∏", "∇", "Z", "∞", "≈", "≠",
    "a", "≤", "≥", "b", "→", "←", "c", ")", "↑", "d", "↓", "2", "e", "↔", "⊕", "f",
    "]", "⊗", "g", "⊙", "⊘", "h", "∈", "4", "i", "}", "∉", "j", "⊂", "⊃", "k", "⊆",
    ">", "l", "⊇", "6", "m", "∩", "∪", "n", "∧", "’", "o", "∨", "¬", "p", "∀", "8",
    "q", "∃", "”", "r", "⊢", "⊨", "s", "∴", "∵", "t", "»", "0", "u", "≡", "ψ", "v",
    "φ", "ω", "w", "α", "β", "x", "γ", "δ", "y", "λ", "π", "z", "σ",
)

_ALPHABET_POSITION = {
    token: position for position, token in enumerate(PUBLIC_GONOL_157)
}

# This is a profile-owned, deterministic pin of the Unicode White_Space
# property. Runtime ``str.isspace()`` behavior is intentionally not authority.
# The tuple holds source code points, not normalized carrier tokens.
EDCM_SPACE_CODE_POINTS: tuple[str, ...] = (
    "\u0009",
    "\u000A",
    "\u000B",
    "\u000C",
    "\u000D",
    "\u0020",
    "\u0085",
    "\u00A0",
    "\u1680",
    "\u2000",
    "\u2001",
    "\u2002",
    "\u2003",
    "\u2004",
    "\u2005",
    "\u2006",
    "\u2007",
    "\u2008",
    "\u2009",
    "\u200A",
    "\u2028",
    "\u2029",
    "\u202F",
    "\u205F",
    "\u3000",
)
_EDCM_SPACE_CODE_POINT_SET = frozenset(EDCM_SPACE_CODE_POINTS)

EDCM_PROFILE_OPTIONS: tuple[tuple[str, str], ...] = tuple(
    sorted(
        {
            "carrier_requirement": "mobius-origin-hidden-zero",
            "corpus_execution": EDCM_CORPUS_EXECUTION,
            "gonol_initiation": EDCM_GONOL_INITIATION,
            "nesting_boundary": "superpositioned-space",
            "normalization": EDCM_NORMALIZATION_POLICY,
            "occurrence_operation": "ordered-concatenation",
            "out_of_alphabet": "retain-and-report",
            "profile_scope": EDCM_PROFILE_SCOPE,
            "source_domain": EDCM_SOURCE_DOMAIN,
            "space_assignment": EDCM_SPACE_ASSIGNMENT_POLICY,
            "smallest_gonol": EDCM_SMALLEST_GONOL,
            "support": EDCM_SUPPORT_POLICY,
            "token_alphabet": "public-gonol-157",
            "token_identity": "unicode-code-point",
        }.items()
    )
)


class EdcmProfileError(ValueError):
    """Raised when the fixed EDCM observation profile is violated."""


def public_gonol_sha256(
    arrangement: tuple[str, ...] = PUBLIC_GONOL_157,
) -> str:
    """Return the source-compatible digest for an exact token arrangement."""

    payload = json.dumps(
        tuple(arrangement), ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return sha256(payload).hexdigest()


def decode_utf8_exact(source: bytes) -> str:
    """Decode corpus bytes without replacement or normalization."""

    if not isinstance(source, bytes):
        raise TypeError("source must be bytes")
    return source.decode("utf-8", errors="strict")


def _is_unicode_scalar(value: str) -> bool:
    return len(value) == 1 and not 0xD800 <= ord(value) <= 0xDFFF


if len(PUBLIC_GONOL_157) != 157:
    raise RuntimeError("public gonol arity mismatch")
if len(set(PUBLIC_GONOL_157)) != 157:
    raise RuntimeError("public gonol tokens must be unique")
if not all(_is_unicode_scalar(token) for token in PUBLIC_GONOL_157):
    raise RuntimeError("every public gonol token must be one Unicode scalar")
if PUBLIC_GONOL_157[0] != " ":
    raise RuntimeError("SPACE must occupy public gonol position zero")
if PUBLIC_GONOL_157.index("0") == 0:
    raise RuntimeError("digit zero cannot be the public gonol origin")
if public_gonol_sha256() != PUBLIC_GONOL_SHA256:
    raise RuntimeError("public gonol source fixture digest mismatch")
if len(EDCM_SPACE_CODE_POINTS) != 25:
    raise RuntimeError("EDCM SPACE manifestation pin must contain 25 code points")
if len(_EDCM_SPACE_CODE_POINT_SET) != len(EDCM_SPACE_CODE_POINTS):
    raise RuntimeError("EDCM SPACE manifestation pin must be unique")
if EDCM_SPACE_CODE_POINTS[5] != PUBLIC_GONOL_157[0]:
    raise RuntimeError("U+0020 must remain the public-gonol origin manifestation")


def edcm_carrier_position(value: str) -> int | None:
    """Return the fixed carrier position for one exact source code point.

    The source value is not changed. Every profile-pinned SPACE manifestation
    assigns to the U+0020 carrier origin; other source values use exact
    public-gonol membership.
    """

    if not _is_unicode_scalar(value):
        raise EdcmProfileError("carrier assignment requires one Unicode scalar")
    if value in _EDCM_SPACE_CODE_POINT_SET:
        return 0
    return _ALPHABET_POSITION.get(value)


@dataclass(frozen=True, slots=True)
class EdcmTokenObservation:
    """One exact source code point and its optional 157-gonol position."""

    value: str
    codepoint_offset: int
    alphabet_position: int | None

    def __post_init__(self) -> None:
        if not _is_unicode_scalar(self.value):
            raise EdcmProfileError("token observation requires one Unicode scalar")
        if self.codepoint_offset < 0:
            raise EdcmProfileError("codepoint_offset must be nonnegative")
        expected = edcm_carrier_position(self.value)
        if self.alphabet_position != expected:
            raise EdcmProfileError("alphabet position does not match carrier assignment")

    @property
    def code_point(self) -> str:
        return f"U+{ord(self.value):04X}"

    @property
    def in_alphabet(self) -> bool:
        """Backward-compatible alias for ``has_carrier_assignment``.

        Under profile 0.2.0 a source-preserved SPACE manifestation can have a
        carrier assignment without being a literal token in the 157 fixture.
        """

        return self.has_carrier_assignment

    @property
    def has_carrier_assignment(self) -> bool:
        """Whether the exact source code point has a fixed carrier position."""

        return self.alphabet_position is not None

    @property
    def is_public_gonol_token(self) -> bool:
        """Whether the raw source value is literally one of the 157 tokens."""

        return self.value in _ALPHABET_POSITION

    @property
    def carrier_token(self) -> str | None:
        """Return the exact public-gonol token at the assigned carrier position."""

        if self.alphabet_position is None:
            return None
        return PUBLIC_GONOL_157[self.alphabet_position]

    @property
    def is_space(self) -> bool:
        """Whether this exact source code point manifests the SPACE origin."""

        return self.alphabet_position == 0


@dataclass(frozen=True, slots=True)
class SuperpositionedSpaceBoundary:
    """One exact source SPACE manifestation acting as boundary and interface."""

    token: EdcmTokenObservation
    roles: tuple[str, ...] = (
        "token",
        "word-boundary",
        "superpositioned-nesting-interface",
    )

    def __post_init__(self) -> None:
        if not self.token.is_space:
            raise EdcmProfileError("nesting boundary must assign to position-zero SPACE")

    @property
    def raw_text(self) -> str:
        return self.token.value


@dataclass(frozen=True, slots=True)
class EdcmWordGonol:
    """The smallest EDCM gonol: one ordered maximal non-SPACE token sequence."""

    word_index: int
    tokens: tuple[EdcmTokenObservation, ...]
    source_start: int
    source_end: int
    initiation_event: str = EDCM_GONOL_INITIATION

    def __post_init__(self) -> None:
        if self.word_index < 0:
            raise EdcmProfileError("word_index must be nonnegative")
        if not self.tokens:
            raise EdcmProfileError("a word gonol requires at least one token")
        if any(token.is_space for token in self.tokens):
            raise EdcmProfileError("SPACE is a nesting boundary, not a word token")
        if self.source_start < 0 or self.source_end <= self.source_start:
            raise EdcmProfileError("word gonol source span is invalid")
        offsets = tuple(token.codepoint_offset for token in self.tokens)
        if offsets != tuple(range(self.source_start, self.source_end)):
            raise EdcmProfileError("word gonol tokens must preserve contiguous order")
        if self.initiation_event != EDCM_GONOL_INITIATION:
            raise EdcmProfileError("a new EDCM gonol must initiate through the Mobius twist")

    @property
    def raw_text(self) -> str:
        return "".join(token.value for token in self.tokens)

    @property
    def carrier_unassigned(self) -> tuple[EdcmTokenObservation, ...]:
        """Return exact non-SPACE source tokens without a carrier assignment."""

        return tuple(token for token in self.tokens if not token.has_carrier_assignment)

    @property
    def out_of_alphabet(self) -> tuple[EdcmTokenObservation, ...]:
        """Backward-compatible alias for ``carrier_unassigned``."""

        return self.carrier_unassigned


EdcmSegment: TypeAlias = EdcmWordGonol | SuperpositionedSpaceBoundary


@dataclass(frozen=True, slots=True)
class EdcmTurnObservation:
    """One complete speaker turn with exact ordered nested evidence."""

    speaker_id: str
    turn_index: int
    raw_text: str
    segments: tuple[EdcmSegment, ...]
    source_id: str | None = None
    unit_support: float = 1.0

    def __post_init__(self) -> None:
        if not self.speaker_id:
            raise EdcmProfileError("speaker_id must be nonempty")
        if self.turn_index < 0:
            raise EdcmProfileError("turn_index must be nonnegative")
        if not isinstance(self.raw_text, str):
            raise TypeError("raw_text must be str")
        if self.unit_support != 1.0:
            raise EdcmProfileError("one speaker turn must have unit support")
        reconstructed = "".join(segment.raw_text for segment in self.segments)
        if reconstructed != self.raw_text:
            raise EdcmProfileError("segments must reconstruct exact source text")

    @property
    def word_gonols(self) -> tuple[EdcmWordGonol, ...]:
        return tuple(
            segment
            for segment in self.segments
            if isinstance(segment, EdcmWordGonol)
        )

    @property
    def nesting_boundaries(self) -> tuple[SuperpositionedSpaceBoundary, ...]:
        return tuple(
            segment
            for segment in self.segments
            if isinstance(segment, SuperpositionedSpaceBoundary)
        )

    @property
    def tokens(self) -> tuple[EdcmTokenObservation, ...]:
        ordered: list[EdcmTokenObservation] = []
        for segment in self.segments:
            if isinstance(segment, EdcmWordGonol):
                ordered.extend(segment.tokens)
            else:
                ordered.append(segment.token)
        return tuple(ordered)

    @property
    def carrier_unassigned(self) -> tuple[EdcmTokenObservation, ...]:
        """Return exact non-SPACE source tokens without a carrier assignment."""

        return tuple(token for token in self.tokens if not token.has_carrier_assignment)

    @property
    def out_of_alphabet(self) -> tuple[EdcmTokenObservation, ...]:
        """Backward-compatible alias for ``carrier_unassigned``."""

        return self.carrier_unassigned

    @property
    def has_complete_alphabet_coverage(self) -> bool:
        """Backward-compatible carrier-assignment alias for profile 0.2.0."""

        return self.has_complete_carrier_assignment

    @property
    def has_complete_carrier_assignment(self) -> bool:
        """Whether every exact source code point has a fixed carrier position."""

        return not self.carrier_unassigned


def _token_observation(value: str, codepoint_offset: int) -> EdcmTokenObservation:
    return EdcmTokenObservation(
        value=value,
        codepoint_offset=codepoint_offset,
        alphabet_position=edcm_carrier_position(value),
    )


@dataclass(frozen=True, slots=True)
class EdcmWordGonolProfile:
    """Fixed EDCM-only profile for exact full-corpus turn observation."""

    profile_id: str = EDCM_PROFILE_ID
    version: str = EDCM_PROFILE_VERSION
    scope: str = EDCM_PROFILE_SCOPE
    options: tuple[tuple[str, str], ...] = EDCM_PROFILE_OPTIONS

    def __post_init__(self) -> None:
        if self.profile_id != EDCM_PROFILE_ID or self.version != EDCM_PROFILE_VERSION:
            raise EdcmProfileError("EDCM profile identity mismatch")
        if self.scope != EDCM_PROFILE_SCOPE:
            raise EdcmProfileError("EDCM profile scope must remain EDCM-only")
        if self.options != EDCM_PROFILE_OPTIONS:
            raise EdcmProfileError("EDCM profile options are fixed and fail closed")

    def observe_turn(
        self,
        *,
        speaker_id: str,
        turn_index: int,
        text: str,
        source_id: str | None = None,
    ) -> EdcmTurnObservation:
        """Preserve one turn as ordered word gonols and exact SPACE boundaries."""

        if not isinstance(text, str):
            raise TypeError("text must be str")

        segments: list[EdcmSegment] = []
        word_tokens: list[EdcmTokenObservation] = []
        word_start = 0
        word_index = 0

        def close_word(source_end: int) -> None:
            nonlocal word_tokens, word_index
            if not word_tokens:
                return
            segments.append(
                EdcmWordGonol(
                    word_index=word_index,
                    tokens=tuple(word_tokens),
                    source_start=word_start,
                    source_end=source_end,
                )
            )
            word_tokens = []
            word_index += 1

        for offset, value in enumerate(text):
            token = _token_observation(value, offset)
            if token.is_space:
                close_word(offset)
                segments.append(SuperpositionedSpaceBoundary(token=token))
                continue
            if not word_tokens:
                word_start = offset
            word_tokens.append(token)
        close_word(len(text))

        return EdcmTurnObservation(
            speaker_id=speaker_id,
            turn_index=turn_index,
            raw_text=text,
            segments=tuple(segments),
            source_id=source_id,
        )

    def observe_corpus(
        self,
        turns: Iterable[tuple[str, str]],
        *,
        source_id: str | None = None,
    ) -> Iterator[EdcmTurnObservation]:
        """Observe every supplied speaker turn in order; no sampling is performed."""

        for turn_index, turn in enumerate(turns):
            if not isinstance(turn, tuple) or len(turn) != 2:
                raise EdcmProfileError("each corpus turn must be (speaker_id, text)")
            speaker_id, text = turn
            yield self.observe_turn(
                speaker_id=speaker_id,
                turn_index=turn_index,
                text=text,
                source_id=source_id,
            )


__all__ = [
    "EDCM_CORPUS_EXECUTION",
    "EDCM_GONOL_INITIATION",
    "EDCM_NORMALIZATION_POLICY",
    "EDCM_PROFILE_ID",
    "EDCM_PROFILE_OPTIONS",
    "EDCM_PROFILE_SCOPE",
    "EDCM_PROFILE_VERSION",
    "EDCM_SMALLEST_GONOL",
    "EDCM_SOURCE_DOMAIN",
    "EDCM_SPACE_ASSIGNMENT_POLICY",
    "EDCM_SPACE_CODE_POINTS",
    "EDCM_SUPPORT_POLICY",
    "PUBLIC_GONOL_157",
    "PUBLIC_GONOL_SHA256",
    "PUBLIC_GONOL_SOURCE_COMMIT",
    "PUBLIC_GONOL_SOURCE_PATH",
    "PUBLIC_GONOL_SOURCE_REPOSITORY",
    "EdcmProfileError",
    "EdcmTokenObservation",
    "EdcmTurnObservation",
    "EdcmWordGonol",
    "EdcmWordGonolProfile",
    "SuperpositionedSpaceBoundary",
    "decode_utf8_exact",
    "edcm_carrier_position",
    "public_gonol_sha256",
]
