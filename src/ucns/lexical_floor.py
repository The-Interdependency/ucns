# === MODULE_BUILD ===
# id: ngsl_lexical_floor
#   module_name: lexical_floor
#   module_kind: domain
#   summary: source-bound NGSL word gonols, occurrence-addressed character relationships, layered affixiation, compounding, contextual definitions, and immutable snapshots
#   owner: Erin Spencer
#   public_surface: GlyphDefinition, LexicalSourceReceipt, LexicalWordGonol, SharedGlyphOccurrence, GlyphTypeSetProjection, CharacterRelationship, LexicalHyperspacePotential, AffixiationCandidate, CompoundCandidate, DefinitionSense, LexicalLayerSnapshot, load_ngsl_source_receipt, load_ngsl_words, define_glyphs, create_word_gonols, create_hyperspace_potential, derive_affixiation_candidates, derive_compound_candidates, create_definition_layer, snapshot_layers, validate_snapshot_chain, word_gonol_id
#   internal_surface: _canonical_digest, _word_sort_key, _edit_distance, _load_source_bundle, _git_blob_sha1
#   auth_boundary: none
#   storage_boundary: packaged immutable text and JSON source evidence; caller-selected snapshot output
#   network_boundary: none
#   user_data_boundary: no user data; exact source spellings remain unchanged and definitions require explicit context and source identity
#   admin_only: false
#   tests: tests/test_lexical_floor.py
#   rollout: deprecated historical evidence only; current floor is ucns_xkcd_lexical_floor
#   rollback: remove this module and packaged NGSL artifacts without altering the existing EDCM word-gonol profile
#   since: 2026-08-04
#   deprecated: 2026-08-17 NGSL closed floor; current candidate is ucns.lexical-floor.xkcd-simplewriter-0.2.1
#   unresolved: independent official-source checksum custody, attested affix authority, compound adjudication, contextual definition custody, and the deep-recursion hyperdimensional embedding law
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: lexical_floor_source_receipt_binds_packaged_bytes
#   given: the packaged NGSL source metadata and word file are loaded
#   then: exact schema, collection, attribution notice, serialization, count, Git blob, byte digests, word-sequence digest, and unresolved custody boundary are retained in one immutable source receipt
#   class: evidence
#   since: 2026-08-06
#
# id: lexical_floor_words_are_unique_exact_glyph_sets
#   given: any public word-gonol construction path is used
#   then: the word is nonempty, contains only assigned Unicode scalars, contains no profile-pinned SPACE manifestation, preserves exact case and order, and cannot duplicate another exact spelling in one floor
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
# id: lexical_hyperspace_is_occurrence_preserving_projection_not_embedding
#   given: two word gonols are compared
#   then: exact cross-word glyph occurrence addresses, prefix, suffix, containment, and edit distance are retained; any glyph-type set view names its identity policy and information loss; no semantic, morphological, geometric, or embedding standing follows
#   class: safety
#   since: 2026-08-06
#
# id: affixiation_and_compounding_are_candidate_layers
#   given: character decomposition finds a retained base or two retained component words
#   then: the result is constructor-bound to exact word identities and labeled orthographic-candidate until independently attested; it never rewrites the word gonol
#   class: doctrine
#   since: 2026-08-04
#
# id: definitions_are_context_plural_and_immutable
#   given: definitions are added to retained word gonols
#   then: multiple senses may coexist with distinct context and source identity, authority standing is fixed, and the returned layer cannot be mutated in place
#   class: evidence
#   since: 2026-08-06
#
# id: every_added_layer_has_a_source_bound_snapshot
#   given: words, glyphs, gonols, hyperspace potential, affixiation, compounding, or definitions are materialized
#   then: the exact ordered snapshot chain records the source receipt, producer, parent, count, digest, fixed standing, and unresolved boundary; a changed source or parent fails validation
#   class: correctness
#   since: 2026-08-06
# === END CONTRACTS ===

"""Executable, source-bound NGSL 1.2 lexical floor for UCNS.

The exact spelling is the word-gonol identity. Serialization order exists only
for reproducible builds. Character relationships retain occurrence addresses;
the optional glyph-type set projection names its identity policy and declared
loss. Affixiation candidates, compound candidates, and contextual definitions
are append-only layers that never rewrite the source word gonol.
"""

from __future__ import annotations

from dataclasses import dataclass, field, fields, is_dataclass
from functools import lru_cache
from hashlib import sha1, sha256
from importlib.resources import files
import json
import re
from types import MappingProxyType
from typing import Iterable, Mapping, Sequence

from .edcm import edcm_carrier_position


LEXICAL_FLOOR_ID = "ucns.lexical-floor.ngsl-1.2"
LEXICAL_FLOOR_VERSION = "0.2.0"
LEXICAL_PRODUCER_ID = f"{LEXICAL_FLOOR_ID}/{LEXICAL_FLOOR_VERSION}"
LEXICAL_SOURCE_SCHEMA_ID = "ucns.lexical-source/0.1.0"
LEXICAL_COLLECTION_ID = "ngsl-1.2-general-english-2809"
LEXICAL_SOURCE_STANDING = "source-admitted-candidate"
LEXICAL_SOURCE_RECEIPT_PREFIX = "ucns.lexical-source-receipt:sha256:"
NGSL_WORD_COUNT = 2809
NGSL_WORD_RESOURCE = "data/ngsl_1_2_words.txt"
NGSL_SOURCE_RESOURCE = "data/ngsl_1_2_source.json"
NGSL_ATTRIBUTION_RESOURCE = "data/NGSL_1_2_ATTRIBUTION.txt"
SERIALIZATION_ORDER = "unicode-casefold-then-exact-codepoint"
WORD_ID_POLICY = "exact-ordered-unicode-scalar-sequence"
CHARACTER_RELATIONSHIP_STANDING = "character-derived-occurrence-projection"
GLYPH_TYPE_SET_STANDING = "declared-loss-glyph-type-set-projection"
GLYPH_TYPE_SET_IDENTITY_POLICY = "unicode-scalar-value"
GLYPH_TYPE_SET_INFORMATION_LOSS = (
    "left and right occurrence offsets are omitted",
    "occurrence multiplicity is omitted",
    "cross-word occurrence pairing is omitted",
)
ORTHOGRAPHIC_CANDIDATE_STANDING = "orthographic-candidate"
DEFINITION_STANDING = "context-sourced-definition"

_HEX_40 = re.compile(r"^[0-9a-f]{40}$")
_HEX_64 = re.compile(r"^[0-9a-f]{64}$")

_LAYER_SPECS: tuple[tuple[str, str, str], ...] = (
    (
        "00-words",
        "source-admitted-word-only",
        "Independent official-source checksum custody remains required before canonical promotion.",
    ),
    (
        "01-glyphs",
        "existing-glyph-canon-applied",
        "No new glyph law is asserted by this lexical floor.",
    ),
    (
        "02-word-gonols",
        "implemented-exact-word-gonols",
        "The source-to-hyperdimensional-coordinate law remains unresolved.",
    ),
    (
        "03-character-hyperspace-potential",
        "implemented-occurrence-addressed-character-projection",
        "Projection capability is not a geometric embedding or semantic relation.",
    ),
    (
        "04-affixiation",
        ORTHOGRAPHIC_CANDIDATE_STANDING,
        "Linguistic affix authority and allomorphy remain unadjudicated.",
    ),
    (
        "05-compounding",
        ORTHOGRAPHIC_CANDIDATE_STANDING,
        "Orthographic decomposition is not yet an attested compound judgment.",
    ),
    (
        "06-definitions",
        DEFINITION_STANDING,
        "Definition custody, sense boundaries, and context-corpus admission remain open.",
    ),
)
_LAYER_INDEX = {layer_id: index for index, (layer_id, _, _) in enumerate(_LAYER_SPECS)}


class LexicalFloorError(ValueError):
    """Raised when a lexical-floor invariant is violated."""


def _word_sort_key(word: str) -> tuple[str, tuple[int, ...]]:
    return (word.casefold(), tuple(ord(glyph) for glyph in word))


def _is_unicode_scalar(glyph: str) -> bool:
    return isinstance(glyph, str) and len(glyph) == 1 and not 0xD800 <= ord(glyph) <= 0xDFFF


def _canonical_value(value: object) -> object:
    if is_dataclass(value):
        return {
            item.name: _canonical_value(getattr(value, item.name))
            for item in fields(value)
            if item.repr or item.compare
        }
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


def _git_blob_sha1(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def _require_exact_keys(value: Mapping[str, object], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise LexicalFloorError(
            f"{label} keys mismatch; missing={missing}, extra={extra}"
        )


def _require_nonempty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise LexicalFloorError(f"{label} must be a nonempty string")
    return value


def _validate_word(word: str) -> None:
    if not isinstance(word, str) or not word:
        raise LexicalFloorError("word spellings must be nonempty strings")
    for glyph in word:
        if not _is_unicode_scalar(glyph):
            raise LexicalFloorError("word spellings must contain Unicode scalars only")
        position = edcm_carrier_position(glyph)
        if position == 0:
            raise LexicalFloorError(
                "word spellings cannot cross a profile-pinned SPACE boundary"
            )
        if position is None:
            raise LexicalFloorError(
                f"word glyph lacks a Public Gonol carrier assignment: U+{ord(glyph):04X}"
            )


def _validate_words(
    words: Sequence[str],
    *,
    expected_count: int | None = None,
) -> None:
    if expected_count is not None and len(words) != expected_count:
        raise LexicalFloorError(
            f"expected {expected_count} words, received {len(words)}"
        )
    for word in words:
        _validate_word(word)
    if len(set(words)) != len(words):
        raise LexicalFloorError("duplicate exact word spellings are prohibited")
    if tuple(sorted(words, key=_word_sort_key)) != tuple(words):
        raise LexicalFloorError(
            "word serialization must use deterministic casefold/exact ordering"
        )


@dataclass(frozen=True, slots=True)
class LexicalSourceReceipt:
    """Producer-issued evidence binding metadata to the exact packaged word bytes."""

    schema_id: str
    collection_id: str
    title: str
    creators: tuple[str, ...]
    license: str
    official_source: str
    word_count: int
    word_file: str
    attribution_file: str
    attribution_sha256: str
    mirror_repository: str
    mirror_commit: str
    mirror_path: str
    mirror_git_blob: str
    target_git_blob: str
    metadata_sha256: str
    word_file_sha256: str
    word_sequence_sha256: str
    identity_policy: str
    serialization_order: str
    file_serialization: str
    standing: str
    hmmm: str
    producer_id: str = LEXICAL_PRODUCER_ID

    def __post_init__(self) -> None:
        if self.schema_id != LEXICAL_SOURCE_SCHEMA_ID:
            raise LexicalFloorError("lexical source schema identity mismatch")
        if self.collection_id != LEXICAL_COLLECTION_ID:
            raise LexicalFloorError("lexical collection identity mismatch")
        if not isinstance(self.title, str) or not self.title:
            raise LexicalFloorError("source title must remain explicit")
        if not self.creators or not all(
            isinstance(creator, str) and creator for creator in self.creators
        ):
            raise LexicalFloorError("source creators must remain explicit strings")
        if not isinstance(self.license, str) or not self.license:
            raise LexicalFloorError("source license is required")
        if not isinstance(self.official_source, str) or not self.official_source:
            raise LexicalFloorError("official source is required")
        if self.word_count != NGSL_WORD_COUNT:
            raise LexicalFloorError("source receipt word count mismatch")
        if self.word_file != NGSL_WORD_RESOURCE.rsplit("/", 1)[-1]:
            raise LexicalFloorError("source receipt word file mismatch")
        if self.attribution_file != NGSL_ATTRIBUTION_RESOURCE.rsplit("/", 1)[-1]:
            raise LexicalFloorError("source receipt attribution file mismatch")
        if not _HEX_64.fullmatch(self.attribution_sha256):
            raise LexicalFloorError("attribution digest must be lowercase SHA-256")
        if not self.mirror_repository or not self.mirror_path:
            raise LexicalFloorError("mirror repository and path are required")
        if not _HEX_40.fullmatch(self.mirror_commit):
            raise LexicalFloorError("mirror commit must be a full Git SHA")
        if not _HEX_40.fullmatch(self.mirror_git_blob):
            raise LexicalFloorError("mirror Git blob must be a full SHA")
        if not _HEX_40.fullmatch(self.target_git_blob):
            raise LexicalFloorError("target Git blob must be a full SHA")
        for digest_name, digest in (
            ("metadata", self.metadata_sha256),
            ("word file", self.word_file_sha256),
            ("word sequence", self.word_sequence_sha256),
        ):
            if not _HEX_64.fullmatch(digest):
                raise LexicalFloorError(f"{digest_name} digest must be lowercase SHA-256")
        if self.identity_policy != WORD_ID_POLICY:
            raise LexicalFloorError("source receipt word identity policy mismatch")
        if self.serialization_order != SERIALIZATION_ORDER:
            raise LexicalFloorError("source receipt serialization order mismatch")
        if self.file_serialization != "utf-8-lf-terminal-newline":
            raise LexicalFloorError("source file serialization mismatch")
        if self.standing != LEXICAL_SOURCE_STANDING:
            raise LexicalFloorError("source receipt standing cannot be promoted")
        if not self.hmmm:
            raise LexicalFloorError("source receipt must retain an unresolved boundary")
        if self.producer_id != LEXICAL_PRODUCER_ID:
            raise LexicalFloorError("source receipt producer mismatch")

    @property
    def receipt_id(self) -> str:
        return f"{LEXICAL_SOURCE_RECEIPT_PREFIX}{_canonical_digest(self)}"


def _parse_source_bundle(
    metadata_payload: bytes,
    word_payload: bytes,
    attribution_payload: bytes,
) -> tuple[LexicalSourceReceipt, tuple[str, ...]]:
    try:
        metadata_text = metadata_payload.decode("utf-8", errors="strict")
        metadata = json.loads(metadata_text)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise LexicalFloorError("lexical source metadata must be strict UTF-8 JSON") from error
    if not isinstance(metadata, dict):
        raise LexicalFloorError("lexical source metadata must be a JSON object")

    _require_exact_keys(
        metadata,
        {
            "schema_id",
            "collection_id",
            "title",
            "creators",
            "license",
            "official_source",
            "word_count",
            "word_file",
            "attribution_file",
            "attribution_sha256",
            "acquisition",
            "identity_policy",
            "file_serialization",
            "standing",
            "hmmm",
        },
        "lexical source metadata",
    )
    acquisition = metadata["acquisition"]
    identity = metadata["identity_policy"]
    file_serialization = metadata["file_serialization"]
    if not isinstance(acquisition, dict) or not isinstance(identity, dict) or not isinstance(file_serialization, dict):
        raise LexicalFloorError("source acquisition, identity, and serialization must be objects")
    _require_exact_keys(
        acquisition,
        {
            "mirror_repository",
            "mirror_commit",
            "mirror_path",
            "mirror_git_blob",
            "target_git_blob",
        },
        "source acquisition",
    )
    _require_exact_keys(
        identity,
        {
            "word_identity",
            "normalization",
            "case_folding",
            "duplicate_policy",
            "source_rank_retained",
            "frequency_retained",
            "serialization_order",
        },
        "source identity policy",
    )
    _require_exact_keys(
        file_serialization,
        {"encoding", "line_separator", "terminal_newline"},
        "source file serialization",
    )

    for key in (
        "schema_id",
        "collection_id",
        "title",
        "license",
        "official_source",
        "word_file",
        "attribution_file",
        "attribution_sha256",
        "standing",
        "hmmm",
    ):
        _require_nonempty_string(metadata[key], f"source metadata {key}")
    creators = metadata["creators"]
    if not isinstance(creators, list) or not creators or not all(
        isinstance(creator, str) and creator for creator in creators
    ):
        raise LexicalFloorError("source metadata creators must be a nonempty string list")
    if not isinstance(metadata["word_count"], int) or isinstance(metadata["word_count"], bool):
        raise LexicalFloorError("source metadata word_count must be an integer")
    for key in acquisition:
        _require_nonempty_string(acquisition[key], f"source acquisition {key}")

    if metadata["schema_id"] != LEXICAL_SOURCE_SCHEMA_ID:
        raise LexicalFloorError("source schema identity mismatch")
    if metadata["collection_id"] != LEXICAL_COLLECTION_ID:
        raise LexicalFloorError("source collection identity mismatch")
    if metadata["word_count"] != NGSL_WORD_COUNT:
        raise LexicalFloorError("source metadata word count mismatch")
    if metadata["word_file"] != NGSL_WORD_RESOURCE.rsplit("/", 1)[-1]:
        raise LexicalFloorError("source metadata word file mismatch")
    if metadata["attribution_file"] != NGSL_ATTRIBUTION_RESOURCE.rsplit("/", 1)[-1]:
        raise LexicalFloorError("source metadata attribution file mismatch")
    if not _HEX_64.fullmatch(metadata["attribution_sha256"]):
        raise LexicalFloorError("source metadata attribution digest is malformed")
    if metadata["standing"] != LEXICAL_SOURCE_STANDING:
        raise LexicalFloorError("source metadata standing cannot be promoted")
    if not isinstance(metadata["hmmm"], str) or not metadata["hmmm"]:
        raise LexicalFloorError("source metadata must retain hmmm")
    if identity != {
        "word_identity": "exact ordered Unicode scalar sequence",
        "normalization": "none",
        "case_folding": "none",
        "duplicate_policy": "reject exact duplicate spellings",
        "source_rank_retained": False,
        "frequency_retained": False,
        "serialization_order": "Unicode casefold key, then exact code-point tuple; ordering has no semantic standing",
    }:
        raise LexicalFloorError("source identity policy mismatch")
    if file_serialization != {
        "encoding": "UTF-8",
        "line_separator": "LF",
        "terminal_newline": True,
    }:
        raise LexicalFloorError("source file serialization declaration mismatch")

    if not attribution_payload.endswith(b"\n") or b"\r" in attribution_payload:
        raise LexicalFloorError("attribution file must use LF and retain one terminal newline")
    try:
        attribution_text = attribution_payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise LexicalFloorError("attribution file must be strict UTF-8") from error
    if attribution_text.startswith("\ufeff"):
        raise LexicalFloorError("attribution file cannot contain a UTF-8 BOM")
    if sha256(attribution_payload).hexdigest() != metadata["attribution_sha256"]:
        raise LexicalFloorError("packaged attribution does not match its declared digest")
    required_attribution = (
        "New General Service List 1.2",
        "Charles Browne; Brent Culligan; Joseph Phillips",
        "CC BY-SA 4.0",
        metadata["official_source"],
        "independently reconciled",
    )
    if not all(fragment in attribution_text for fragment in required_attribution):
        raise LexicalFloorError("attribution file omits required source or custody evidence")

    if not word_payload.endswith(b"\n") or b"\r" in word_payload:
        raise LexicalFloorError("word file must use LF and retain one terminal newline")
    try:
        word_text = word_payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise LexicalFloorError("word file must be strict UTF-8") from error
    if word_text.startswith("\ufeff"):
        raise LexicalFloorError("word file cannot contain a UTF-8 BOM")
    words = tuple(word_text[:-1].split("\n"))
    _validate_words(words, expected_count=NGSL_WORD_COUNT)

    target_blob = _git_blob_sha1(word_payload)
    if acquisition["target_git_blob"] != target_blob:
        raise LexicalFloorError("packaged word bytes do not match the declared Git blob")

    receipt = LexicalSourceReceipt(
        schema_id=str(metadata["schema_id"]),
        collection_id=str(metadata["collection_id"]),
        title=metadata["title"],
        creators=tuple(metadata["creators"]),
        license=metadata["license"],
        official_source=metadata["official_source"],
        word_count=metadata["word_count"],
        word_file=metadata["word_file"],
        attribution_file=metadata["attribution_file"],
        attribution_sha256=metadata["attribution_sha256"],
        mirror_repository=acquisition["mirror_repository"],
        mirror_commit=acquisition["mirror_commit"],
        mirror_path=acquisition["mirror_path"],
        mirror_git_blob=acquisition["mirror_git_blob"],
        target_git_blob=target_blob,
        metadata_sha256=sha256(metadata_payload).hexdigest(),
        word_file_sha256=sha256(word_payload).hexdigest(),
        word_sequence_sha256=_canonical_digest(words),
        identity_policy=WORD_ID_POLICY,
        serialization_order=SERIALIZATION_ORDER,
        file_serialization="utf-8-lf-terminal-newline",
        standing=metadata["standing"],
        hmmm=metadata["hmmm"],
    )
    return receipt, words


@lru_cache(maxsize=1)
def _load_source_bundle() -> tuple[LexicalSourceReceipt, tuple[str, ...]]:
    package = files("ucns")
    metadata_payload = package.joinpath(NGSL_SOURCE_RESOURCE).read_bytes()
    word_payload = package.joinpath(NGSL_WORD_RESOURCE).read_bytes()
    attribution_payload = package.joinpath(NGSL_ATTRIBUTION_RESOURCE).read_bytes()
    return _parse_source_bundle(metadata_payload, word_payload, attribution_payload)


def load_ngsl_source_receipt() -> LexicalSourceReceipt:
    """Load the immutable receipt binding metadata to exact packaged bytes."""

    return _load_source_bundle()[0]


def load_ngsl_words() -> tuple[str, ...]:
    """Load the exact source-receipted NGSL 1.2 word-only collection."""

    return _load_source_bundle()[1]


@dataclass(frozen=True, slots=True)
class GlyphDefinition:
    """One exact glyph governed by the fixed Public Gonol carrier."""

    value: str
    code_point: str
    carrier_position: int

    def __post_init__(self) -> None:
        if not _is_unicode_scalar(self.value):
            raise LexicalFloorError("a glyph definition requires one Unicode scalar")
        if self.code_point != f"U+{ord(self.value):04X}":
            raise LexicalFloorError("glyph code point does not match its value")
        expected = edcm_carrier_position(self.value)
        if expected is None or expected == 0:
            raise LexicalFloorError("lexical glyph must be assigned and non-SPACE")
        if self.carrier_position != expected:
            raise LexicalFloorError("glyph carrier position does not match the EDCM profile")


@dataclass(frozen=True, slots=True)
class LexicalWordGonol:
    """One unique source word represented by its exact ordered glyph sequence."""

    word: str
    glyphs: tuple[str, ...]
    gonol_id: str

    def __post_init__(self) -> None:
        _validate_word(self.word)
        if tuple(self.word) != self.glyphs:
            raise LexicalFloorError("word and ordered glyph sequence must match")
        if self.gonol_id != word_gonol_id(self.word):
            raise LexicalFloorError("word gonol identity mismatch")


def word_gonol_id(word: str) -> str:
    _validate_word(word)
    evidence = (WORD_ID_POLICY, tuple(ord(glyph) for glyph in word))
    return f"word-gonol:sha256:{_canonical_digest(evidence)}"


def define_glyphs(words: Sequence[str]) -> tuple[GlyphDefinition, ...]:
    _validate_words(words)
    glyphs = sorted({glyph for word in words for glyph in word}, key=ord)
    return tuple(
        GlyphDefinition(
            value=glyph,
            code_point=f"U+{ord(glyph):04X}",
            carrier_position=int(edcm_carrier_position(glyph)),
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
class SharedGlyphOccurrence:
    """One exact matching glyph pair with both source occurrence addresses."""

    glyph: str
    left_offset: int
    right_offset: int

    def __post_init__(self) -> None:
        if not _is_unicode_scalar(self.glyph):
            raise LexicalFloorError("shared occurrence requires one Unicode scalar")
        if self.left_offset < 0 or self.right_offset < 0:
            raise LexicalFloorError("shared occurrence offsets must be nonnegative")


@dataclass(frozen=True, slots=True)
class GlyphTypeSetProjection:
    """A declared-loss set view over shared occurrence evidence."""

    glyphs: tuple[str, ...]
    identity_policy: str = GLYPH_TYPE_SET_IDENTITY_POLICY
    information_loss: tuple[str, ...] = GLYPH_TYPE_SET_INFORMATION_LOSS
    standing: str = GLYPH_TYPE_SET_STANDING

    def __post_init__(self) -> None:
        if any(not _is_unicode_scalar(glyph) for glyph in self.glyphs):
            raise LexicalFloorError("glyph-type projection requires Unicode scalars")
        if tuple(sorted(set(self.glyphs), key=ord)) != self.glyphs:
            raise LexicalFloorError("glyph-type projection must be unique and code-point ordered")
        if self.identity_policy != GLYPH_TYPE_SET_IDENTITY_POLICY:
            raise LexicalFloorError("glyph-type set identity policy mismatch")
        if self.information_loss != GLYPH_TYPE_SET_INFORMATION_LOSS:
            raise LexicalFloorError("glyph-type set information loss cannot be omitted")
        if self.standing != GLYPH_TYPE_SET_STANDING:
            raise LexicalFloorError("glyph-type set standing cannot be promoted")


def _shared_occurrences(left: str, right: str) -> tuple[SharedGlyphOccurrence, ...]:
    return tuple(
        SharedGlyphOccurrence(glyph, left_offset, right_offset)
        for left_offset, glyph in enumerate(left)
        for right_offset, right_glyph in enumerate(right)
        if glyph == right_glyph
    )


def _shared_glyph_type_projection(left: str, right: str) -> GlyphTypeSetProjection:
    return GlyphTypeSetProjection(tuple(sorted(set(left) & set(right), key=ord)))


@dataclass(frozen=True, slots=True)
class CharacterRelationship:
    """An exact orthographic projection between two retained word gonols."""

    left_word: str
    right_word: str
    left_gonol_id: str
    right_gonol_id: str
    shared_occurrences: tuple[SharedGlyphOccurrence, ...]
    shared_glyph_type_set: GlyphTypeSetProjection
    common_prefix_length: int
    common_suffix_length: int
    left_contains_right: bool
    right_contains_left: bool
    edit_distance: int
    standing: str = CHARACTER_RELATIONSHIP_STANDING

    def __post_init__(self) -> None:
        _validate_word(self.left_word)
        _validate_word(self.right_word)
        if self.left_gonol_id != word_gonol_id(self.left_word):
            raise LexicalFloorError("left relationship gonol identity mismatch")
        if self.right_gonol_id != word_gonol_id(self.right_word):
            raise LexicalFloorError("right relationship gonol identity mismatch")
        if self.shared_occurrences != _shared_occurrences(self.left_word, self.right_word):
            raise LexicalFloorError("shared glyph occurrence evidence mismatch")
        if self.shared_glyph_type_set != _shared_glyph_type_projection(self.left_word, self.right_word):
            raise LexicalFloorError("shared glyph-type projection mismatch")
        if self.common_prefix_length != _common_prefix_length(self.left_word, self.right_word):
            raise LexicalFloorError("common prefix evidence mismatch")
        if self.common_suffix_length != _common_suffix_length(self.left_word, self.right_word):
            raise LexicalFloorError("common suffix evidence mismatch")
        if self.left_contains_right is not (self.right_word in self.left_word):
            raise LexicalFloorError("left containment evidence mismatch")
        if self.right_contains_left is not (self.left_word in self.right_word):
            raise LexicalFloorError("right containment evidence mismatch")
        if self.edit_distance != _edit_distance(self.left_word, self.right_word):
            raise LexicalFloorError("edit-distance evidence mismatch")
        if self.standing != CHARACTER_RELATIONSHIP_STANDING:
            raise LexicalFloorError("character relationship standing cannot be promoted")


@dataclass(frozen=True, slots=True)
class LexicalHyperspacePotential:
    """An immutable non-geometric potential for exact character projections."""

    word_gonols: tuple[LexicalWordGonol, ...]
    _by_word: Mapping[str, LexicalWordGonol] = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        ordered = tuple(self.word_gonols)
        if not ordered:
            raise LexicalFloorError("hyperspace potential requires word gonols")
        _validate_words(tuple(gonol.word for gonol in ordered))
        if len({gonol.word for gonol in ordered}) != len(ordered):
            raise LexicalFloorError("hyperspace words must remain unique")
        if len({gonol.gonol_id for gonol in ordered}) != len(ordered):
            raise LexicalFloorError("hyperspace gonol identities must remain unique")
        object.__setattr__(self, "word_gonols", ordered)
        object.__setattr__(
            self,
            "_by_word",
            MappingProxyType({gonol.word: gonol for gonol in ordered}),
        )

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
            left_word=left.word,
            right_word=right.word,
            left_gonol_id=left.gonol_id,
            right_gonol_id=right.gonol_id,
            shared_occurrences=_shared_occurrences(left.word, right.word),
            shared_glyph_type_set=_shared_glyph_type_projection(left.word, right.word),
            common_prefix_length=_common_prefix_length(left.word, right.word),
            common_suffix_length=_common_suffix_length(left.word, right.word),
            left_contains_right=right.word in left.word,
            right_contains_left=left.word in right.word,
            edit_distance=_edit_distance(left.word, right.word),
        )


def create_hyperspace_potential(
    word_gonols: Sequence[LexicalWordGonol],
) -> LexicalHyperspacePotential:
    return LexicalHyperspacePotential(tuple(word_gonols))


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
        _validate_word(self.base_word)
        _validate_word(self.derived_word)
        if self.base_gonol_id != word_gonol_id(self.base_word):
            raise LexicalFloorError("affixiation base identity mismatch")
        if self.derived_gonol_id != word_gonol_id(self.derived_word):
            raise LexicalFloorError("affixiation derived identity mismatch")
        if not self.affix:
            raise LexicalFloorError("affixiation candidate requires an affix")
        if self.side not in {"prefix", "suffix"}:
            raise LexicalFloorError("affixiation side must be prefix or suffix")
        expected = self.affix + self.base_word if self.side == "prefix" else self.base_word + self.affix
        if expected != self.derived_word:
            raise LexicalFloorError("affixiation decomposition mismatch")
        if self.standing != ORTHOGRAPHIC_CANDIDATE_STANDING:
            raise LexicalFloorError("affixiation standing cannot be promoted")


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
        _validate_word(self.compound_word)
        _validate_word(self.left_word)
        _validate_word(self.right_word)
        if self.compound_gonol_id != word_gonol_id(self.compound_word):
            raise LexicalFloorError("compound identity mismatch")
        if self.left_gonol_id != word_gonol_id(self.left_word):
            raise LexicalFloorError("left compound identity mismatch")
        if self.right_gonol_id != word_gonol_id(self.right_word):
            raise LexicalFloorError("right compound identity mismatch")
        if self.left_word + self.right_word != self.compound_word:
            raise LexicalFloorError("compound decomposition mismatch")
        if self.split_offset != len(self.left_word):
            raise LexicalFloorError("compound split offset mismatch")
        if self.standing != ORTHOGRAPHIC_CANDIDATE_STANDING:
            raise LexicalFloorError("compound standing cannot be promoted")


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
            isinstance(value, str) and value
            for value in (
                self.word_gonol_id,
                self.context_identity,
                self.definition,
                self.source_identity,
            )
        ):
            raise LexicalFloorError(
                "definition senses require gonol, context, text, and source identity"
            )
        prefix = "word-gonol:sha256:"
        if not self.word_gonol_id.startswith(prefix) or not _HEX_64.fullmatch(
            self.word_gonol_id.removeprefix(prefix)
        ):
            raise LexicalFloorError("definition must reference a complete word-gonol identity")
        if self.standing != DEFINITION_STANDING:
            raise LexicalFloorError("definition standing cannot be promoted")


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
    immutable = {
        gonol_id: tuple(values)
        for gonol_id, values in sorted(grouped.items())
    }
    return MappingProxyType(immutable)


@dataclass(frozen=True, slots=True)
class LexicalLayerSnapshot:
    """One immutable, source-bound digest boundary in the lexical layer chain."""

    layer_index: int
    layer_id: str
    source_receipt_id: str
    parent_snapshot_id: str | None
    item_count: int
    content_digest: str
    standing: str
    hmmm: str
    producer_id: str = LEXICAL_PRODUCER_ID

    def __post_init__(self) -> None:
        if not 0 <= self.layer_index < len(_LAYER_SPECS):
            raise LexicalFloorError("snapshot layer index is outside the declared sequence")
        expected_id, expected_standing, expected_hmmm = _LAYER_SPECS[self.layer_index]
        if self.layer_id != expected_id:
            raise LexicalFloorError("snapshot layer identity mismatch")
        if self.standing != expected_standing:
            raise LexicalFloorError("snapshot standing cannot be promoted")
        if self.hmmm != expected_hmmm:
            raise LexicalFloorError("snapshot unresolved boundary cannot be erased or replaced")
        if not self.source_receipt_id.startswith(LEXICAL_SOURCE_RECEIPT_PREFIX):
            raise LexicalFloorError("snapshot source receipt identity mismatch")
        if not _HEX_64.fullmatch(self.source_receipt_id.removeprefix(LEXICAL_SOURCE_RECEIPT_PREFIX)):
            raise LexicalFloorError("snapshot source receipt digest is malformed")
        if self.layer_index == 0:
            if self.parent_snapshot_id is not None:
                raise LexicalFloorError("root lexical snapshot cannot have a parent")
        else:
            previous_id = _LAYER_SPECS[self.layer_index - 1][0]
            expected_prefix = f"{previous_id}:sha256:"
            if not isinstance(self.parent_snapshot_id, str) or not self.parent_snapshot_id.startswith(expected_prefix):
                raise LexicalFloorError("snapshot parent layer identity mismatch")
            if not _HEX_64.fullmatch(self.parent_snapshot_id.removeprefix(expected_prefix)):
                raise LexicalFloorError("snapshot parent digest is malformed")
        if self.item_count < 0:
            raise LexicalFloorError("snapshot item count must be nonnegative")
        if not _HEX_64.fullmatch(self.content_digest):
            raise LexicalFloorError("snapshot content digest must be lowercase SHA-256")
        if self.producer_id != LEXICAL_PRODUCER_ID:
            raise LexicalFloorError("snapshot producer mismatch")

    @property
    def snapshot_id(self) -> str:
        evidence = (
            self.producer_id,
            self.layer_index,
            self.layer_id,
            self.source_receipt_id,
            self.parent_snapshot_id,
            self.item_count,
            self.content_digest,
            self.standing,
            self.hmmm,
        )
        return f"{self.layer_id}:sha256:{_canonical_digest(evidence)}"


def validate_snapshot_chain(
    snapshots: Sequence[LexicalLayerSnapshot],
    source_receipt: LexicalSourceReceipt,
) -> tuple[LexicalLayerSnapshot, ...]:
    """Fail closed unless the complete current source-bound layer chain is intact."""

    chain = tuple(snapshots)
    if len(chain) != len(_LAYER_SPECS):
        raise LexicalFloorError("snapshot chain must contain every declared lexical layer")
    parent: str | None = None
    seen_ids: set[str] = set()
    for index, snapshot in enumerate(chain):
        if snapshot.layer_index != index:
            raise LexicalFloorError("snapshot chain order mismatch")
        if snapshot.source_receipt_id != source_receipt.receipt_id:
            raise LexicalFloorError("snapshot chain source receipt mismatch")
        if snapshot.parent_snapshot_id != parent:
            raise LexicalFloorError("snapshot chain parent mismatch")
        if snapshot.snapshot_id in seen_ids:
            raise LexicalFloorError("snapshot identities must remain unique")
        seen_ids.add(snapshot.snapshot_id)
        parent = snapshot.snapshot_id
    return chain


def snapshot_layers(
    words: Sequence[str],
    *,
    definitions: Iterable[DefinitionSense] = (),
) -> tuple[LexicalLayerSnapshot, ...]:
    """Materialize the complete source-bound snapshot sequence."""

    ordered_words = tuple(words)
    _validate_words(ordered_words)
    source_receipt, packaged_words = _load_source_bundle()
    if ordered_words != packaged_words:
        raise LexicalFloorError(
            "snapshot source does not match the exact packaged source receipt"
        )

    glyphs = define_glyphs(ordered_words)
    gonols = create_word_gonols(ordered_words)
    potential = create_hyperspace_potential(gonols)
    affixiation = derive_affixiation_candidates(potential)
    compounds = derive_compound_candidates(potential)
    definition_layer = create_definition_layer(potential, definitions)
    flattened_definitions = tuple(
        sense
        for senses in definition_layer.values()
        for sense in senses
    )

    payloads: tuple[tuple[object, int], ...] = (
        ((source_receipt, ordered_words), len(ordered_words)),
        (glyphs, len(glyphs)),
        (gonols, len(gonols)),
        (
            (
                ("projection-schema", "character-relationship-occurrence-v2"),
                ("glyph-type-set-policy", GLYPH_TYPE_SET_IDENTITY_POLICY),
                ("glyph-type-set-loss", GLYPH_TYPE_SET_INFORMATION_LOSS),
                gonols,
            ),
            len(gonols),
        ),
        (affixiation, len(affixiation)),
        (compounds, len(compounds)),
        (flattened_definitions, len(flattened_definitions)),
    )

    snapshots: list[LexicalLayerSnapshot] = []
    parent: str | None = None
    for layer_index, ((layer_id, standing, hmmm), (payload, item_count)) in enumerate(
        zip(_LAYER_SPECS, payloads, strict=True)
    ):
        snapshot = LexicalLayerSnapshot(
            layer_index=layer_index,
            layer_id=layer_id,
            source_receipt_id=source_receipt.receipt_id,
            parent_snapshot_id=parent,
            item_count=item_count,
            content_digest=_canonical_digest(payload),
            standing=standing,
            hmmm=hmmm,
        )
        snapshots.append(snapshot)
        parent = snapshot.snapshot_id
    return validate_snapshot_chain(snapshots, source_receipt)
