# === MODULE_BUILD ===
# id: ngsl_lexical_floor
#   module_name: lexical_floor
#   module_kind: domain
#   summary: unique NGSL word gonols, character-relationship hyperspace potential, layered affixiation, compounding, and contextual-definition snapshots
#   owner: Erin Spencer
#   public_surface: GlyphDefinition, LexicalWordGonol, CharacterRelationship, LexicalHyperspacePotential, AffixiationCandidate, CompoundCandidate, DefinitionSense, LexicalLayerSnapshot, load_ngsl_words, define_glyphs, create_word_gonols, create_hyperspace_potential, derive_affixiation_candidates, derive_compound_candidates, create_definition_layer, snapshot_layers
#   internal_surface: _canonical_digest, _word_sort_key, _edit_distance
#   auth_boundary: none
#   storage_boundary: packaged immutable text source and caller-selected snapshot output
#   network_boundary: none
#   user_data_boundary: no user data; source spellings remain exact and definitions require explicit context and source identity
#   admin_only: false
#   tests: tests/test_lexical_floor.py
#   rollout: experimental lexical-floor producer; no hyperdimensional embedding or linguistic canon selection
#   rollback: remove this module and packaged NGSL artifacts without altering the existing EDCM word-gonol profile
#   since: 2026-08-04
#   unresolved: attested affix authority, compound adjudication, contextual definition custody, and the deep-recursion hyperdimensional embedding law
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: lexical_floor_words_are_unique_exact_glyph_sets
#   given: the packaged NGSL word-only source is loaded
#   then: exactly 2809 nonempty exact spellings exist, no two spellings share one identical ordered glyph tuple, and no normalization or case folding changes identity
#   class: correctness
#   since: 2026-08-04
#
# id: lexical_floor_order_is_serialization_only
#   given: the source collection is serialized
#   then: deterministic casefold-plus-exact-codepoint order supports reproducible builds but contributes no rank, frequency, meaning, or gonol identity
#   class: doctrine
#   since: 2026-08-04
#
# id: lexical_floor_reuses_canonical_glyph_assignment
#   given: a source spelling is converted to a word gonol
#   then: each exact Unicode scalar occurrence uses the existing EDCM carrier assignment and retains its value, position, multiplicity, and order
#   class: evidence
#   since: 2026-08-04
#
# id: lexical_hyperspace_is_projection_not_embedding
#   given: two word gonols are compared
#   then: exact character-derived relations are projectable without claiming semantic relation, linguistic derivation, geometric proximity, or the unresolved hyperdimensional embedding law
#   class: safety
#   since: 2026-08-04
#
# id: affixiation_and_compounding_are_candidate_layers
#   given: character decomposition finds a retained base or two retained component words
#   then: the result is labeled orthographic-candidate until independently attested and never rewrites the word gonol
#   class: doctrine
#   since: 2026-08-04
#
# id: definitions_are_context_plural
#   given: definitions are added to one word gonol
#   then: multiple senses may coexist when each retains distinct context and source identity; no duplicate word gonol is created
#   class: evidence
#   since: 2026-08-04
#
# id: every_added_layer_has_a_snapshot
#   given: words, glyphs, gonols, hyperspace potential, affixiation, compounding, or definitions are materialized
#   then: an ordered snapshot records its parent, count, digest, standing, and unresolved boundary
#   class: correctness
#   since: 2026-08-04
# === END CONTRACTS ===

"""Executable NGSL 1.2 lexical floor for UCNS.

The exact word spelling is the word-gonol identity. Serialization order exists
only to make builds reproducible. Character relationships, affixiation
candidates, compound candidates, and contextual definitions are appended as
separate projection layers and never rewrite the underlying word gonol.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, is_dataclass
from hashlib import sha256
from importlib.resources import files
import json
from typing import Iterable, Mapping, Sequence

from .edcm import edcm_carrier_position


LEXICAL_FLOOR_ID = "ucns.lexical-floor.ngsl-1.2"
LEXICAL_FLOOR_VERSION = "0.1.0"
NGSL_WORD_COUNT = 2809
NGSL_WORD_RESOURCE = "data/ngsl_1_2_words.txt"
SERIALIZATION_ORDER = "unicode-casefold-then-exact-codepoint"
WORD_ID_POLICY = "exact-ordered-unicode-scalar-sequence"
ORTHOGRAPHIC_CANDIDATE_STANDING = "orthographic-candidate"
DEFINITION_STANDING = "context-sourced-definition"


class LexicalFloorError(ValueError):
    """Raised when a lexical-floor invariant is violated."""


def _word_sort_key(word: str) -> tuple[str, tuple[int, ...]]:
    return (word.casefold(), tuple(ord(glyph) for glyph in word))


def _is_unicode_scalar(glyph: str) -> bool:
    return len(glyph) == 1 and not 0xD800 <= ord(glyph) <= 0xDFFF


def _canonical_value(value: object) -> object:
    if is_dataclass(value):
        return _canonical_value(asdict(value))
    if isinstance(value, Mapping):
        return {
            str(key): _canonical_value(item)
            for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))
        }
    if isinstance(value, (tuple, list)):
        return [_canonical_value(item) for item in value]
    return value


def _canonical_digest(value: object) -> str:
    payload = json.dumps(
        _canonical_value(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return sha256(payload).hexdigest()


def load_ngsl_words() -> tuple[str, ...]:
    """Load and validate the exact word-only NGSL 1.2 collection."""

    resource = files("ucns").joinpath(NGSL_WORD_RESOURCE)
    words = tuple(resource.read_text(encoding="utf-8").splitlines())
    _validate_words(words, expected_count=NGSL_WORD_COUNT)
    return words


def _validate_words(
    words: Sequence[str],
    *,
    expected_count: int | None = None,
) -> None:
    if expected_count is not None and len(words) != expected_count:
        raise LexicalFloorError(
            f"expected {expected_count} words, received {len(words)}"
        )
    if any(not word for word in words):
        raise LexicalFloorError("word spellings must be nonempty")
    if any(any(not _is_unicode_scalar(glyph) for glyph in word) for word in words):
        raise LexicalFloorError("word spellings must contain Unicode scalars only")
    if any(any(glyph.isspace() for glyph in word) for word in words):
        raise LexicalFloorError("word spellings cannot contain whitespace")
    if len(set(words)) != len(words):
        raise LexicalFloorError("duplicate exact word spellings are prohibited")
    if tuple(sorted(words, key=_word_sort_key)) != tuple(words):
        raise LexicalFloorError(
            "word serialization must use deterministic casefold/exact ordering"
        )


@dataclass(frozen=True, slots=True)
class GlyphDefinition:
    """One exact glyph already governed by the canonical EDCM carrier."""

    value: str
    code_point: str
    carrier_position: int | None

    def __post_init__(self) -> None:
        if not _is_unicode_scalar(self.value):
            raise LexicalFloorError("a glyph definition requires one Unicode scalar")
        if self.code_point != f"U+{ord(self.value):04X}":
            raise LexicalFloorError("glyph code point does not match its value")
        if self.carrier_position != edcm_carrier_position(self.value):
            raise LexicalFloorError(
                "glyph carrier position does not match the EDCM profile"
            )


@dataclass(frozen=True, slots=True)
class LexicalWordGonol:
    """One unique source word represented by its exact ordered glyph sequence."""

    word: str
    glyphs: tuple[str, ...]
    gonol_id: str

    def __post_init__(self) -> None:
        if not self.word or tuple(self.word) != self.glyphs:
            raise LexicalFloorError("word and ordered glyph sequence must match")
        if self.gonol_id != word_gonol_id(self.word):
            raise LexicalFloorError("word gonol identity mismatch")


def word_gonol_id(word: str) -> str:
    if not word or any(not _is_unicode_scalar(glyph) for glyph in word):
        raise LexicalFloorError("word identity requires nonempty Unicode scalars")
    return f"word-gonol:sha256:{_canonical_digest(tuple(word))}"


def define_glyphs(words: Sequence[str]) -> tuple[GlyphDefinition, ...]:
    _validate_words(words)
    glyphs = sorted({glyph for word in words for glyph in word}, key=ord)
    return tuple(
        GlyphDefinition(
            value=glyph,
            code_point=f"U+{ord(glyph):04X}",
            carrier_position=edcm_carrier_position(glyph),
        )
        for glyph in glyphs
    )


def create_word_gonols(words: Sequence[str]) -> tuple[LexicalWordGonol, ...]:
    _validate_words(words)
    return tuple(
        LexicalWordGonol(
            word=word,
            glyphs=tuple(word),
            gonol_id=word_gonol_id(word),
        )
        for word in words
    )


def _common_prefix_length(left: str, right: str) -> int:
    count = 0
    for left_glyph, right_glyph in zip(left, right):
        if left_glyph != right_glyph:
            break
        count += 1
    return count


def _common_suffix_length(left: str, right: str) -> int:
    count = 0
    for left_glyph, right_glyph in zip(reversed(left), reversed(right)):
        if left_glyph != right_glyph:
            break
        count += 1
    return count


def _edit_distance(left: str, right: str) -> int:
    previous = list(range(len(right) + 1))
    for left_index, left_glyph in enumerate(left, start=1):
        current = [left_index]
        for right_index, right_glyph in enumerate(right, start=1):
            current.append(
                min(
                    current[-1] + 1,
                    previous[right_index] + 1,
                    previous[right_index - 1] + (left_glyph != right_glyph),
                )
            )
        previous = current
    return previous[-1]


@dataclass(frozen=True, slots=True)
class CharacterRelationship:
    """An exact orthographic projection between two retained word gonols."""

    left_gonol_id: str
    right_gonol_id: str
    shared_glyphs: tuple[str, ...]
    common_prefix_length: int
    common_suffix_length: int
    left_contains_right: bool
    right_contains_left: bool
    edit_distance: int
    standing: str = "character-derived-projection"


@dataclass(frozen=True, slots=True)
class LexicalHyperspacePotential:
    """A non-geometric potential that can project exact character relations."""

    word_gonols: tuple[LexicalWordGonol, ...]
    _by_word: Mapping[str, LexicalWordGonol]

    def __post_init__(self) -> None:
        if len(self.word_gonols) != len(self._by_word):
            raise LexicalFloorError("hyperspace words must remain unique")
        for gonol in self.word_gonols:
            if self._by_word.get(gonol.word) != gonol:
                raise LexicalFloorError("hyperspace word index mismatch")

    def gonol(self, word: str) -> LexicalWordGonol:
        try:
            return self._by_word[word]
        except KeyError as error:
            raise LexicalFloorError(
                f"word is outside the lexical floor: {error.args[0]}"
            ) from error

    def project(self, left_word: str, right_word: str) -> CharacterRelationship:
        left = self.gonol(left_word)
        right = self.gonol(right_word)
        return CharacterRelationship(
            left_gonol_id=left.gonol_id,
            right_gonol_id=right.gonol_id,
            shared_glyphs=tuple(sorted(set(left.word) & set(right.word), key=ord)),
            common_prefix_length=_common_prefix_length(left.word, right.word),
            common_suffix_length=_common_suffix_length(left.word, right.word),
            left_contains_right=right.word in left.word,
            right_contains_left=left.word in right.word,
            edit_distance=_edit_distance(left.word, right.word),
        )


def create_hyperspace_potential(
    word_gonols: Sequence[LexicalWordGonol],
) -> LexicalHyperspacePotential:
    ordered = tuple(word_gonols)
    by_word = {gonol.word: gonol for gonol in ordered}
    if len(by_word) != len(ordered):
        raise LexicalFloorError("one word gonol per exact glyph set is required")
    return LexicalHyperspacePotential(ordered, by_word)


@dataclass(frozen=True, slots=True)
class AffixiationCandidate:
    """An orthographic base-plus-affix candidate, not attested morphology."""

    base_gonol_id: str
    derived_gonol_id: str
    base_word: str
    derived_word: str
    affix: str
    side: str
    standing: str = ORTHOGRAPHIC_CANDIDATE_STANDING

    def __post_init__(self) -> None:
        if not self.affix:
            raise LexicalFloorError("affixiation candidate requires an affix")
        if self.side not in {"prefix", "suffix"}:
            raise LexicalFloorError("affixiation side must be prefix or suffix")
        expected = (
            self.affix + self.base_word
            if self.side == "prefix"
            else self.base_word + self.affix
        )
        if expected != self.derived_word:
            raise LexicalFloorError("affixiation decomposition mismatch")


def derive_affixiation_candidates(
    potential: LexicalHyperspacePotential,
) -> tuple[AffixiationCandidate, ...]:
    words = potential._by_word
    candidates: list[AffixiationCandidate] = []
    for derived in potential.word_gonols:
        for split in range(1, len(derived.word)):
            left = derived.word[:split]
            right = derived.word[split:]
            if right in words:
                base = words[right]
                candidates.append(
                    AffixiationCandidate(
                        base_gonol_id=base.gonol_id,
                        derived_gonol_id=derived.gonol_id,
                        base_word=base.word,
                        derived_word=derived.word,
                        affix=left,
                        side="prefix",
                    )
                )
            if left in words:
                base = words[left]
                candidates.append(
                    AffixiationCandidate(
                        base_gonol_id=base.gonol_id,
                        derived_gonol_id=derived.gonol_id,
                        base_word=base.word,
                        derived_word=derived.word,
                        affix=right,
                        side="suffix",
                    )
                )
    return tuple(
        sorted(
            set(candidates),
            key=lambda item: (
                _word_sort_key(item.derived_word),
                item.side,
                _word_sort_key(item.base_word),
                item.affix,
            ),
        )
    )


@dataclass(frozen=True, slots=True)
class CompoundCandidate:
    """An exact two-word decomposition candidate."""

    compound_gonol_id: str
    left_gonol_id: str
    right_gonol_id: str
    compound_word: str
    left_word: str
    right_word: str
    split_offset: int
    standing: str = ORTHOGRAPHIC_CANDIDATE_STANDING

    def __post_init__(self) -> None:
        if self.left_word + self.right_word != self.compound_word:
            raise LexicalFloorError("compound decomposition mismatch")
        if self.split_offset != len(self.left_word):
            raise LexicalFloorError("compound split offset mismatch")


def derive_compound_candidates(
    potential: LexicalHyperspacePotential,
) -> tuple[CompoundCandidate, ...]:
    words = potential._by_word
    candidates: list[CompoundCandidate] = []
    for compound in potential.word_gonols:
        for split in range(1, len(compound.word)):
            left_word = compound.word[:split]
            right_word = compound.word[split:]
            if left_word not in words or right_word not in words:
                continue
            left = words[left_word]
            right = words[right_word]
            candidates.append(
                CompoundCandidate(
                    compound_gonol_id=compound.gonol_id,
                    left_gonol_id=left.gonol_id,
                    right_gonol_id=right.gonol_id,
                    compound_word=compound.word,
                    left_word=left.word,
                    right_word=right.word,
                    split_offset=split,
                )
            )
    return tuple(candidates)


@dataclass(frozen=True, slots=True)
class DefinitionSense:
    """One context-derived definition attached to an existing word gonol."""

    word_gonol_id: str
    context_identity: str
    definition: str
    source_identity: str
    standing: str = DEFINITION_STANDING

    def __post_init__(self) -> None:
        if not all(
            (
                self.word_gonol_id,
                self.context_identity,
                self.definition,
                self.source_identity,
            )
        ):
            raise LexicalFloorError(
                "definition senses require gonol, context, text, and source identity"
            )


def create_definition_layer(
    potential: LexicalHyperspacePotential,
    senses: Iterable[DefinitionSense],
) -> Mapping[str, tuple[DefinitionSense, ...]]:
    known_ids = {gonol.gonol_id for gonol in potential.word_gonols}
    grouped: dict[str, list[DefinitionSense]] = {}
    seen: set[tuple[str, str, str]] = set()
    for sense in senses:
        if sense.word_gonol_id not in known_ids:
            raise LexicalFloorError("definition references an unknown word gonol")
        identity = (
            sense.word_gonol_id,
            sense.context_identity,
            sense.source_identity,
        )
        if identity in seen:
            raise LexicalFloorError("duplicate contextual definition identity")
        seen.add(identity)
        grouped.setdefault(sense.word_gonol_id, []).append(sense)
    return {
        gonol_id: tuple(values)
        for gonol_id, values in sorted(grouped.items())
    }


@dataclass(frozen=True, slots=True)
class LexicalLayerSnapshot:
    """One immutable digest boundary in the append-only lexical layer sequence."""

    layer_id: str
    parent_snapshot_id: str | None
    item_count: int
    content_digest: str
    standing: str
    hmmm: str

    @property
    def snapshot_id(self) -> str:
        return (
            f"{self.layer_id}:sha256:"
            f"{_canonical_digest((self.parent_snapshot_id, self.item_count, self.content_digest, self.standing, self.hmmm))}"
        )


def snapshot_layers(
    words: Sequence[str],
    *,
    definitions: Iterable[DefinitionSense] = (),
) -> tuple[LexicalLayerSnapshot, ...]:
    """Materialize a snapshot after every currently declared layer."""

    _validate_words(words)
    glyphs = define_glyphs(words)
    gonols = create_word_gonols(words)
    potential = create_hyperspace_potential(gonols)
    affixiation = derive_affixiation_candidates(potential)
    compounds = derive_compound_candidates(potential)
    definition_layer = create_definition_layer(potential, definitions)
    flattened_definitions = tuple(
        sense
        for senses in definition_layer.values()
        for sense in senses
    )

    payloads: tuple[
        tuple[str, object, int, str, str],
        ...,
    ] = (
        (
            "00-words",
            tuple(words),
            len(words),
            "source-admitted-word-only",
            "Official-source checksum reconciliation remains required before canonical promotion.",
        ),
        (
            "01-glyphs",
            glyphs,
            len(glyphs),
            "existing-glyph-canon-applied",
            "No new glyph law is asserted by this lexical floor.",
        ),
        (
            "02-word-gonols",
            gonols,
            len(gonols),
            "implemented-exact-word-gonols",
            "The source-to-hyperdimensional-coordinate law remains unresolved.",
        ),
        (
            "03-character-hyperspace-potential",
            (("projection-schema", "character-relationship-v1"), gonols),
            len(gonols),
            "implemented-on-demand-character-projection",
            "Projection capability is not a geometric embedding or semantic relation.",
        ),
        (
            "04-affixiation",
            affixiation,
            len(affixiation),
            ORTHOGRAPHIC_CANDIDATE_STANDING,
            "Linguistic affix authority and allomorphy remain unadjudicated.",
        ),
        (
            "05-compounding",
            compounds,
            len(compounds),
            ORTHOGRAPHIC_CANDIDATE_STANDING,
            "Orthographic decomposition is not yet an attested compound judgment.",
        ),
        (
            "06-definitions",
            flattened_definitions,
            len(flattened_definitions),
            DEFINITION_STANDING,
            "Definition custody, sense boundaries, and context corpus admission remain open.",
        ),
    )

    snapshots: list[LexicalLayerSnapshot] = []
    parent: str | None = None
    for layer_id, payload, item_count, standing, hmmm in payloads:
        digest = _canonical_digest(payload)
        snapshot = LexicalLayerSnapshot(
            layer_id=layer_id,
            parent_snapshot_id=parent,
            item_count=item_count,
            content_digest=digest,
            standing=standing,
            hmmm=hmmm,
        )
        snapshots.append(snapshot)
        parent = snapshot.snapshot_id
    return tuple(snapshots)
