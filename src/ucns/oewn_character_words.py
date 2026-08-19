# === MODULE_BUILD ===
# id: ucns_oewn_character_word_gonols
#   module_name: oewn_character_words
#   module_kind: engine
#   summary: applies generic affixiation to full OEWN character traversal so corpus-wide history determines admissible paths and closes word gonols
#   owner: Erin Spencer
#   public_surface: CharacterWordCorpus, CharacterWordError, build_character_word_corpus, build_oewn_character_word_corpus, replay_oewn_character_word_corpus, character_word_corpus_bytes, oewn_word_surfaces
#   internal_surface: _tokens, _source_potential, _letter_axes, _function_gonol, _character_gonol, _close_token, _close_composite
#   auth_boundary: requires an exact receipt-bound OEWN Core snapshot or an explicit surface list
#   storage_boundary: immutable in-memory construction and canonical receipt bytes
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_oewn_character_words
#   rollout: declared candidate after the generic affixiate primitive; not selected canon
#   rollback: remove this producer without rewriting historical xkcd-floor or definition receipts
#   requires: ucns_generic_gonol_affixiation, ucns_oewn_2025_core, ucns_current_lexical_word_gonols, ucns_public_gonol_function_table
#   since: 2026-08-19
#   unresolved: selection as canon, complete morphology law, xkcd 3634-to-1000 family mapping
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: oewn_character_history_is_corpus_wide
#   given: OEWN lemmas and forms are closed as word gonols
#   then: each character step's admissible next glyphs are the corpus-wide continuations of that realized prefix
#   class: doctrine
#   since: 2026-08-19
#
# id: oewn_character_words_use_affixiate
#   given: a token or composite surface is closed
#   then: character, function, and word identities are produced by affixiate and are Gonol values
#   class: doctrine
#   since: 2026-08-19
#
# id: oewn_closed_words_are_atomic
#   given: a word gonol is completed
#   then: it is reused by exact surface identity and is atomic at the next scale
#   class: correctness
#   since: 2026-08-19
#
# id: oewn_character_words_replay
#   given: a completed corpus is independently reconstructed from the same snapshot
#   then: receipt bytes agree exactly or replay fails closed
#   class: evidence
#   since: 2026-08-19
# === END CONTRACTS ===

"""OEWN corpus-wide character traversal and word closure.

Usage::

    corpus = build_oewn_character_word_corpus(snapshot)
    water = corpus.word("water")
    assert [item.exact_text for item in corpus.token_participants(water)][-1] == "water"
    replay_oewn_character_word_corpus(corpus, snapshot)

Admissible paths come from the complete OEWN lemma/form token inventory, not
from a later explanatory-floor subset. Historical receipts are not rewritten.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
import json
from types import MappingProxyType
from typing import Mapping

from .edcm import EDCM_SPACE_CODE_POINTS, PUBLIC_GONOL_SHA256, edcm_carrier_position
from .gonol_affixiation import (
    AFFIXIATE_CONSTRUCTOR_ID,
    CHARACTER_STEP_RELATION_CODE,
    CHARACTER_STEP_RELATION_LABEL,
    AffixiationClosure,
    AffixiationRelation,
    AffixiationSource,
    Gonol,
    affixiate,
)
from .lexical_word_gonols import GlyphAxis
from .oewn_core import OEWNCoreSnapshot

TRAVERSAL_ORIGIN = "ucns.lexical-traversal-origin"
WORD_CLOSURE_RELATION_CODE = 6
WORD_CLOSURE_RELATION_LABEL = "ordered-character-word-closure"
COMPOSITION_RELATION_CODE = 2
COMPOSITE_WORD_RELATION_LABEL = "exact-multi-token-word-composition"
FUNCTION_RELATION_CODE = 3
FUNCTION_PARTICIPANT_RELATION_LABEL = "public-gonol-function-participant"
CHARACTER_WORD_STANDING = "oewn-character-word-corpus-candidate"
OEWN_ARTIFACT = "oewn-2025-core"
_SPACE = frozenset(EDCM_SPACE_CODE_POINTS)


@lru_cache(maxsize=1)
def _function_by_glyph() -> Mapping[str, tuple[int, str]]:
    from .public_gonol_functions import FUNCTIONAL_INDEX_NAMES

    return {glyph: (index, name) for index, glyph, name in FUNCTIONAL_INDEX_NAMES}


class CharacterWordError(ValueError):
    """Raised when OEWN character/word construction loses source or history."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"


def _identity(prefix: str, value: object) -> str:
    return prefix + sha256(_canonical_bytes(value)).hexdigest()


def _glyph_sort_key(glyph: str) -> tuple[int, int]:
    position = edcm_carrier_position(glyph)
    return (position if position is not None else 10_000, ord(glyph))


def _tokens(text: str) -> tuple[str, ...]:
    if not text:
        raise CharacterWordError("source text must be nonempty")
    parts: list[str] = []
    cursor = 0
    while cursor < len(text):
        if text[cursor] in _SPACE:
            end = cursor + 1
            while end < len(text) and text[end] in _SPACE:
                end += 1
            cursor = end
            continue
        end = cursor + 1
        while end < len(text) and text[end] not in _SPACE:
            end += 1
        parts.append(text[cursor:end])
        cursor = end
    if not parts:
        raise CharacterWordError("source text has no non-SPACE token")
    return tuple(parts)


def oewn_word_surfaces(snapshot: OEWNCoreSnapshot) -> tuple[str, ...]:
    """Return unique OEWN lemma and form surfaces in first-seen source order."""

    if not isinstance(snapshot, OEWNCoreSnapshot):
        raise TypeError("snapshot must be an OEWNCoreSnapshot")
    surfaces: list[str] = []
    seen: set[str] = set()
    for entry in snapshot.lexical_entries:
        for text in (entry.lemma, *entry.forms):
            if text in seen:
                continue
            seen.add(text)
            surfaces.append(text)
    return tuple(surfaces)


def _source_potential(tokens: tuple[str, ...]) -> tuple[dict[str, tuple[str, ...]], frozenset[str]]:
    children: dict[str, set[str]] = {}
    for token in tokens:
        for index, glyph in enumerate(token):
            children.setdefault(token[:index], set()).add(glyph)
    potential = {
        prefix: tuple(sorted(next_glyphs, key=_glyph_sort_key))
        for prefix, next_glyphs in children.items()
    }
    return potential, frozenset(tokens)


def _letter_axes(tokens: tuple[str, ...]) -> tuple[GlyphAxis, ...]:
    letters = sorted(
        {glyph for token in tokens for glyph in token if "a" <= glyph <= "z"},
        key=_glyph_sort_key,
    )
    return tuple(
        GlyphAxis(glyph, ord(glyph), edcm_carrier_position(glyph))  # type: ignore[arg-type]
        for glyph in letters
    )


@dataclass(frozen=True, slots=True)
class CharacterWordCorpus:
    """Closed word gonols whose character history is corpus-wide."""

    source: AffixiationSource
    surfaces: tuple[str, ...]
    tokens: tuple[str, ...]
    axes: tuple[GlyphAxis, ...]
    words: tuple[Gonol, ...]
    by_surface: Mapping[str, Gonol]
    by_id: Mapping[str, Gonol]
    potential: Mapping[str, tuple[str, ...]]
    terminals: frozenset[str]
    standing: str = CHARACTER_WORD_STANDING
    constructor_id: str = AFFIXIATE_CONSTRUCTOR_ID
    selected: bool = False

    def __post_init__(self) -> None:
        if self.standing != CHARACTER_WORD_STANDING:
            raise CharacterWordError("character-word corpus standing cannot be promoted")
        if self.selected:
            raise CharacterWordError("character-word corpus cannot be selected as canon")
        if len(self.words) != len(self.surfaces) or len(self.by_surface) != len(self.surfaces):
            raise CharacterWordError("word gonols must cover each unique surface once")
        if tuple(item.exact_text for item in self.words) != self.surfaces:
            raise CharacterWordError("word gonols are not in surface order")
        if any(item.scale != "word" or not item.atomic_at_next_scale for item in self.words):
            raise CharacterWordError("closed word gonols must be atomic word-scale gonols")

    def word(self, surface: str) -> Gonol:
        try:
            return self.by_surface[surface]
        except KeyError as exc:
            raise CharacterWordError("surface is not a closed word in this corpus") from exc

    def token_participants(self, word: Gonol) -> tuple[Gonol, ...]:
        if word.scale != "word":
            raise CharacterWordError("token participants require a word gonol")
        return tuple(self.by_id[item] for item in word.participant_ids)

    @property
    def corpus_id(self) -> str:
        return _identity("ucns.character-word-corpus:sha256:", _corpus_payload(self))


def _corpus_payload(corpus: CharacterWordCorpus) -> dict[str, object]:
    word_ids = [item.gonol_id for item in corpus.words]
    return {
        "constructor_id": corpus.constructor_id,
        "standing": corpus.standing,
        "selected": corpus.selected,
        "source_receipt_id": corpus.source.receipt_id,
        "source_artifact": corpus.source.artifact,
        "surface_count": len(corpus.surfaces),
        "token_count": len(corpus.tokens),
        "axis_ids": [item.axis_id for item in corpus.axes],
        "word_gonol_ids_sha256": sha256(_canonical_bytes(word_ids)).hexdigest(),
    }


def character_word_corpus_bytes(corpus: CharacterWordCorpus) -> bytes:
    """Serialize the corpus receipt, not expanded word prose."""

    if not isinstance(corpus, CharacterWordCorpus):
        raise TypeError("corpus must be a CharacterWordCorpus")
    return _canonical_bytes({"corpus_id": corpus.corpus_id, **_corpus_payload(corpus)})


def _function_gonol(glyph: str, source: AffixiationSource, cache: dict[str, Gonol]) -> Gonol:
    try:
        index, name = _function_by_glyph()[glyph]
    except KeyError as exc:
        raise CharacterWordError("glyph is not a Public Gonol function") from exc
    extras = (
        ("kind", "public-gonol-function"),
        ("public_gonol_index", index),
        ("unicode_name", name),
        ("public_gonol_sha256", PUBLIC_GONOL_SHA256),
    )
    gonol = affixiate(
        (),
        AffixiationRelation(FUNCTION_RELATION_CODE, FUNCTION_PARTICIPANT_RELATION_LABEL),
        source,
        "character",
        AffixiationClosure(exact_text=glyph, extras=extras),
    )
    existing = cache.get(gonol.gonol_id)
    if existing is not None:
        return existing
    cache[gonol.gonol_id] = gonol
    return gonol


def _character_gonol(
    *,
    glyph: str,
    prefix: str,
    step_index: int,
    prior_id: str,
    potential: Mapping[str, tuple[str, ...]],
    terminals: frozenset[str],
    axis_by_glyph: Mapping[str, GlyphAxis],
    source: AffixiationSource,
    cache: dict[str, Gonol],
) -> Gonol:
    if not ("a" <= glyph <= "z"):
        extras = (
            ("kind", "residual-character"),
            ("code_point", ord(glyph)),
            ("carrier_position", edcm_carrier_position(glyph)),
            ("realized_prefix", prefix),
            ("step_index", step_index),
            ("prior_state_id", prior_id),
            ("admissible_next_glyphs", list(potential.get(prefix, ()))),
            ("space_boundary_available", prefix in terminals),
        )
        participants: tuple[str, ...] = () if prior_id == TRAVERSAL_ORIGIN else (prior_id,)
        gonol = affixiate(
            participants,
            AffixiationRelation(CHARACTER_STEP_RELATION_CODE, CHARACTER_STEP_RELATION_LABEL),
            source,
            "character",
            AffixiationClosure(exact_text=glyph, extras=extras),
        )
        existing = cache.get(gonol.gonol_id)
        if existing is not None:
            return existing
        cache[gonol.gonol_id] = gonol
        return gonol
    axis = axis_by_glyph[glyph]
    extras = (
        ("kind", "character-gonol"),
        ("realized_prefix", prefix),
        ("step_index", step_index),
        ("selected_axis_id", axis.axis_id),
        ("selected_glyph", glyph),
        ("selected_carrier_position", axis.carrier_position),
        ("prior_state_id", prior_id),
        ("admissible_next_glyphs", list(potential.get(prefix, ()))),
        ("space_boundary_available", prefix in terminals),
    )
    participants = () if prior_id == TRAVERSAL_ORIGIN else (prior_id,)
    gonol = affixiate(
        participants,
        AffixiationRelation(CHARACTER_STEP_RELATION_CODE, CHARACTER_STEP_RELATION_LABEL),
        source,
        "character",
        AffixiationClosure(exact_text=glyph, extras=extras),
    )
    existing = cache.get(gonol.gonol_id)
    if existing is not None:
        return existing
    cache[gonol.gonol_id] = gonol
    return gonol


def _close_token(
    token: str,
    *,
    potential: Mapping[str, tuple[str, ...]],
    terminals: frozenset[str],
    axis_by_glyph: Mapping[str, GlyphAxis],
    source: AffixiationSource,
    cache: dict[str, Gonol],
    words: dict[str, Gonol],
) -> Gonol:
    existing = words.get(token)
    if existing is not None:
        return existing
    participants: list[Gonol] = []
    prior = TRAVERSAL_ORIGIN
    for index, glyph in enumerate(token):
        prefix = token[: index + 1]
        if glyph in _function_by_glyph():
            gonol = _function_gonol(glyph, source, cache)
        else:
            gonol = _character_gonol(
                glyph=glyph,
                prefix=prefix,
                step_index=index,
                prior_id=prior,
                potential=potential,
                terminals=terminals,
                axis_by_glyph=axis_by_glyph,
                source=source,
                cache=cache,
            )
        participants.append(gonol)
        prior = gonol.gonol_id
    word = affixiate(
        participants,
        AffixiationRelation(WORD_CLOSURE_RELATION_CODE, WORD_CLOSURE_RELATION_LABEL),
        source,
        "word",
        AffixiationClosure(exact_text=token, extras=(("kind", "closed-word"),)),
    )
    words[token] = word
    cache[word.gonol_id] = word
    return word


def _close_composite(
    surface: str,
    tokens: tuple[str, ...],
    *,
    potential: Mapping[str, tuple[str, ...]],
    terminals: frozenset[str],
    axis_by_glyph: Mapping[str, GlyphAxis],
    source: AffixiationSource,
    cache: dict[str, Gonol],
    words: dict[str, Gonol],
) -> Gonol:
    existing = words.get(surface)
    if existing is not None:
        return existing
    if len(tokens) == 1 and tokens[0] == surface:
        return _close_token(
            surface,
            potential=potential,
            terminals=terminals,
            axis_by_glyph=axis_by_glyph,
            source=source,
            cache=cache,
            words=words,
        )
    components = [
        _close_token(
            token,
            potential=potential,
            terminals=terminals,
            axis_by_glyph=axis_by_glyph,
            source=source,
            cache=cache,
            words=words,
        )
        for token in tokens
    ]
    word = affixiate(
        components,
        AffixiationRelation(COMPOSITION_RELATION_CODE, COMPOSITE_WORD_RELATION_LABEL),
        source,
        "word",
        AffixiationClosure(
            exact_text=surface,
            extras=(("kind", "closed-composite-word"), ("tokens", list(tokens))),
        ),
    )
    words[surface] = word
    cache[word.gonol_id] = word
    return word


def build_character_word_corpus(
    surfaces: tuple[str, ...],
    source: AffixiationSource,
) -> CharacterWordCorpus:
    """Close unique surfaces from corpus-wide character history via affixiate."""

    if not surfaces:
        raise CharacterWordError("character-word corpus requires at least one surface")
    if len(set(surfaces)) != len(surfaces):
        raise CharacterWordError("character-word surfaces must be unique")
    token_list: list[str] = []
    seen_tokens: set[str] = set()
    token_map = {surface: _tokens(surface) for surface in surfaces}
    for parts in token_map.values():
        for token in parts:
            if token in seen_tokens:
                continue
            seen_tokens.add(token)
            token_list.append(token)
    tokens = tuple(token_list)
    potential, terminals = _source_potential(tokens)
    axes = _letter_axes(tokens)
    axis_by_glyph = {item.glyph: item for item in axes}
    cache: dict[str, Gonol] = {}
    words: dict[str, Gonol] = {}
    closed = []
    for surface in surfaces:
        closed.append(_close_composite(
            surface,
            token_map[surface],
            potential=potential,
            terminals=terminals,
            axis_by_glyph=axis_by_glyph,
            source=source,
            cache=cache,
            words=words,
        ))
    return CharacterWordCorpus(
        source,
        surfaces,
        tokens,
        axes,
        tuple(closed),
        MappingProxyType({item.exact_text: item for item in closed if item.exact_text is not None}),
        MappingProxyType(cache),
        MappingProxyType(potential),
        terminals,
    )


def close_additional_word(
    corpus: CharacterWordCorpus,
    surface: str,
    word_source: AffixiationSource,
    cache: dict[str, Gonol] | None = None,
) -> Gonol:
    """Close a non-corpus surface using corpus-wide character history.

    Shared prefixes reuse corpus character gonols. The word gonol uses
    ``word_source``. This does not invent a family map.
    """

    if not isinstance(corpus, CharacterWordCorpus):
        raise TypeError("corpus must be a CharacterWordCorpus")
    existing = corpus.by_surface.get(surface)
    if existing is not None:
        return existing
    working = dict(corpus.by_id) if cache is None else cache
    axis_by_glyph = {item.glyph: item for item in corpus.axes}
    return _close_additional(
        surface,
        _tokens(surface),
        corpus,
        word_source,
        working,
        axis_by_glyph,
    )


def _close_additional(
    surface: str,
    tokens: tuple[str, ...],
    corpus: CharacterWordCorpus,
    word_source: AffixiationSource,
    cache: dict[str, Gonol],
    axis_by_glyph: Mapping[str, GlyphAxis],
) -> Gonol:
    if len(tokens) == 1 and tokens[0] == surface:
        participants: list[Gonol] = []
        prior = TRAVERSAL_ORIGIN
        for index, glyph in enumerate(surface):
            prefix = surface[: index + 1]
            if glyph in _function_by_glyph():
                gonol = _function_gonol(glyph, corpus.source, cache)
            else:
                gonol = _character_gonol(
                    glyph=glyph,
                    prefix=prefix,
                    step_index=index,
                    prior_id=prior,
                    potential=corpus.potential,
                    terminals=corpus.terminals,
                    axis_by_glyph=axis_by_glyph,
                    source=corpus.source,
                    cache=cache,
                )
            participants.append(gonol)
            prior = gonol.gonol_id
        word = affixiate(
            participants,
            AffixiationRelation(WORD_CLOSURE_RELATION_CODE, WORD_CLOSURE_RELATION_LABEL),
            word_source,
            "word",
            AffixiationClosure(
                exact_text=surface,
                extras=(("kind", "closed-word"), ("absent_from_oewn_inventory", True)),
            ),
        )
        cache[word.gonol_id] = word
        return word
    components = [
        close_additional_word(corpus, token, word_source, cache)
        for token in tokens
    ]
    word = affixiate(
        components,
        AffixiationRelation(COMPOSITION_RELATION_CODE, COMPOSITE_WORD_RELATION_LABEL),
        word_source,
        "word",
        AffixiationClosure(
            exact_text=surface,
            extras=(
                ("kind", "closed-composite-word"),
                ("tokens", list(tokens)),
                ("absent_from_oewn_inventory", True),
            ),
        ),
    )
    cache[word.gonol_id] = word
    return word


def build_oewn_character_word_corpus(snapshot: OEWNCoreSnapshot) -> CharacterWordCorpus:
    """Close every unique OEWN lemma and form from corpus-wide character history."""

    if not isinstance(snapshot, OEWNCoreSnapshot):
        raise TypeError("snapshot must be an OEWNCoreSnapshot")
    return build_character_word_corpus(
        oewn_word_surfaces(snapshot),
        AffixiationSource(snapshot.source_receipt_id, OEWN_ARTIFACT),
    )


def replay_oewn_character_word_corpus(
    corpus: CharacterWordCorpus,
    snapshot: OEWNCoreSnapshot,
) -> CharacterWordCorpus:
    """Independently rebuild the OEWN character-word corpus and compare receipts."""

    rebuilt = build_oewn_character_word_corpus(snapshot)
    if character_word_corpus_bytes(rebuilt) != character_word_corpus_bytes(corpus):
        raise CharacterWordError("OEWN character-word corpus replay mismatch")
    return rebuilt


@lru_cache(maxsize=1)
def _load_snapshot_from_env() -> OEWNCoreSnapshot:
    import os
    from pathlib import Path

    from .lexical_sources import verify_oewn_2025_core
    from .oewn_core import load_oewn_core

    root = os.environ.get("UCNS_OEWN_2025_CORE_ROOT")
    if not root:
        raise CharacterWordError("UCNS_OEWN_2025_CORE_ROOT is required for the official OEWN word corpus")
    path = Path(root)
    receipt = verify_oewn_2025_core(path)
    return load_oewn_core(path, receipt)


def load_oewn_character_word_corpus() -> CharacterWordCorpus:
    """Load the official OEWN character-word corpus from the pinned checkout."""

    return build_oewn_character_word_corpus(_load_snapshot_from_env())


__all__ = [
    "CHARACTER_WORD_STANDING",
    "TRAVERSAL_ORIGIN",
    "WORD_CLOSURE_RELATION_CODE",
    "CharacterWordCorpus",
    "CharacterWordError",
    "build_character_word_corpus",
    "build_oewn_character_word_corpus",
    "character_word_corpus_bytes",
    "close_additional_word",
    "load_oewn_character_word_corpus",
    "oewn_word_surfaces",
    "replay_oewn_character_word_corpus",
]
