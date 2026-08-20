# === MODULE_BUILD ===
# id: ucns_oewn_definition_recursion
#   module_name: oewn_definition_recursion
#   module_kind: engine
#   summary: constructs the complete OEWN 2025 Core first deep-recursion layer as closed source-bound definition gonols
#   owner: Erin Spencer
#   public_surface: OEWNInscriptionGonol, OEWNCompositeWordGonol, OEWNDefinitionOccurrence, OEWNDefinitionGonol, OEWNMorphologyGonol, OEWNDefinitionLayer, CLOSED_WORD_KIND, oewn_entry_key, build_oewn_definition_layer, definition_layer_bytes, replay_oewn_definition_layer
#   internal_surface: _canonical_bytes, _identity, _segments, _definition_spans, _longest_closed_word, _inscription
#   auth_boundary: requires an exact receipt-bound OEWN Core snapshot
#   storage_boundary: immutable in-memory construction and canonical receipt bytes
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_oewn_definition_recursion
#   rollout: after exact sources, word construction, and source morphology inventory
#   rollback: remove current OEWN producer while preserving source receipts and historical NGSL evidence
#   requires: ucns_oewn_2025_core, ucns_relational_carrier, edcm_word_gonol_profile
#   since: 2026-08-18
#   unresolved: final root/affix decomposition law, geometry for carrier-unassigned scalars, native OEWN relation participation, semantic efficacy, recursion above the sealed first punctuation-aware layer
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: oewn_definition_scope_is_complete
#   given: the exact OEWN 2025 Core snapshot is constructed
#   then: every source sense-definition pairing is represented once with exact source identity, gloss, order, multiplicity, occurrence, and provenance
#   class: evidence
#   since: 2026-08-18
#
# id: oewn_definition_relationships_enter_gonols
#   given: one source sense-definition pairing is constructed
#   then: its target and ordered participants are nodes of an intrinsic relation carrier inside one closed definition gonol that is atomic at the next scale
#   class: correctness
#   since: 2026-08-18
#
# id: oewn_functions_are_not_absorbed_into_inscriptions
#   given: a lemma, form, or gloss contains a Public Gonol punctuation or symbol glyph
#   then: that glyph is a function participant with exact span and multiplicity and is not part of an inscription identity
#   class: doctrine
#   since: 2026-08-19
#
# id: oewn_preserves_closed_word_gonols
#   given: a definition gloss contains an already-closed lemma or form
#   then: the definition uses that closed word gonol as one participant and does not reopen its character/function construction
#   class: doctrine
#   since: 2026-08-19
#
# id: oewn_function_occurrence_matches_source_glyph
#   given: a definition occurrence is a Public Gonol function
#   then: its index and participant identity correspond to the exact source glyph at that span
#   class: evidence
#   since: 2026-08-19
#
# id: oewn_morphology_uses_only_explicit_source_forms
#   given: OEWN morphology is materialized before definitions
#   then: each declared form closes with its lexical entry in a source-bound morphology gonol while no root, stem, affix, or transformation decomposition is inferred
#   class: safety
#   since: 2026-08-18
#
# id: oewn_definition_fixed_point_is_source_exhaustion
#   given: a complete construction pass has incorporated all source sense-definition relationships
#   then: a second pass adds zero identities or relationships and cycles reuse atomic identities rather than expanding text recursively
#   class: correctness
#   since: 2026-08-18
#
# id: oewn_definition_layer_replays_byte_exactly
#   given: a completed layer and the same exact source snapshot are independently reconstructed
#   then: canonical receipt bytes and the complete layer identity agree exactly or replay fails closed
#   class: evidence
#   since: 2026-08-18
# === END CONTRACTS ===

"""Complete source-bound OEWN Core definition recursion.

SPACE manifestations remain ordered boundaries. Already-closed lemmas and
forms participate as closed word gonols. Public Gonol punctuation and symbol
glyphs that are not already inside a closed word are function participants.
Residual non-SPACE, non-function, non-closed-word runs are inscriptions. No
normalization is performed.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
import argparse
import json
from pathlib import Path
import sys
from typing import Iterable, Mapping

from .edcm import EDCM_SPACE_CODE_POINTS, PUBLIC_GONOL_SHA256, edcm_carrier_position
from .gonol_affixiation import AffixiationClosure, AffixiationRelation, AffixiationSource, affixiate
from .oewn_character_words import CharacterWordCorpus, CharacterWordError, build_oewn_character_word_corpus
from .oewn_core import OEWNCoreSnapshot
from .lexical_sources import verify_oewn_2025_core
from .oewn_core import load_oewn_core
from .relational_carrier import RelationalCarrier, build_relational_carrier

DEFINITION_RELATION_CODE = 0
MORPHOLOGY_FORM_RELATION_CODE = 1
COMPOSITION_RELATION_CODE = 2
INSCRIPTION_STANDING = "exact-source-inscription-gonol-candidate"
FUNCTION_PARTICIPANT_STANDING = "public-gonol-function-participant-in-oewn-definition"
MORPHOLOGY_STANDING = "explicit-oewn-form-morphology-gonol-candidate"
DEFINITION_STANDING = "closed-oewn-definition-gonol-candidate"
LAYER_STANDING = "punctuation-aware-oewn-core-first-recursion-candidate"
INSCRIPTION_KIND = "inscription"
FUNCTION_KIND = "public-gonol-function"
CLOSED_WORD_KIND = "closed-word"
SPACE_KIND = "space"
_SPACE = frozenset(EDCM_SPACE_CODE_POINTS)


@lru_cache(maxsize=1)
def _function_by_glyph() -> dict[str, tuple[int, str]]:
    from .public_gonol_functions import FUNCTIONAL_INDEX_NAMES

    return {glyph: (index, name) for index, glyph, name in FUNCTIONAL_INDEX_NAMES}


class OEWNDefinitionRecursionError(ValueError):
    """Raised when complete source-bound recursion cannot replay exactly."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8") + b"\n"


def _identity(prefix: str, value: object) -> str:
    return prefix + sha256(_canonical_bytes(value)).hexdigest()


@dataclass(frozen=True, slots=True)
class OEWNInscriptionGonol:
    text: str
    source_receipt_id: str
    glyph_evidence: tuple[tuple[int, int | None], ...]
    public_gonol_sha256: str = PUBLIC_GONOL_SHA256
    atomic_at_next_scale: bool = True
    standing: str = INSCRIPTION_STANDING

    def __post_init__(self) -> None:
        if not self.text or any(ch in _SPACE for ch in self.text):
            raise OEWNDefinitionRecursionError("inscription must be one non-SPACE sequence")
        if any(ch in _function_by_glyph() for ch in self.text):
            raise OEWNDefinitionRecursionError("inscription cannot absorb a Public Gonol function")
        expected = tuple((ord(ch), edcm_carrier_position(ch)) for ch in self.text)
        if self.glyph_evidence != expected:
            raise OEWNDefinitionRecursionError("inscription glyph evidence mismatch")
        if self.public_gonol_sha256 != PUBLIC_GONOL_SHA256:
            raise OEWNDefinitionRecursionError("public gonol identity mismatch")
        if not self.atomic_at_next_scale or self.standing != INSCRIPTION_STANDING:
            raise OEWNDefinitionRecursionError("inscription standing cannot be promoted")

    @property
    def gonol_id(self) -> str:
        return _identity("ucns.oewn-inscription-gonol:sha256:", {
            "text": self.text, "source_receipt_id": self.source_receipt_id,
            "glyph_evidence": [list(item) for item in self.glyph_evidence],
            "public_gonol_sha256": self.public_gonol_sha256,
            "atomic_at_next_scale": self.atomic_at_next_scale,
            "standing": self.standing,
        })

    @property
    def carrier_unassigned_code_points(self) -> tuple[int, ...]:
        return tuple(code for code, position in self.glyph_evidence if position is None)


@dataclass(frozen=True, slots=True)
class OEWNCompositeWordGonol:
    exact_text: str
    component_gonol_ids: tuple[str, ...]
    exact_space_boundaries: tuple[tuple[int, int, str], ...]
    source_receipt_id: str
    carrier: RelationalCarrier
    atomic_at_next_scale: bool = True
    standing: str = "exact-multi-inscription-word-gonol-candidate"

    def __post_init__(self) -> None:
        expected = build_relational_carrier(
            len(self.component_gonol_ids),
            ((index, COMPOSITION_RELATION_CODE, index + 1)
             for index in range(len(self.component_gonol_ids) - 1)),
        )
        if len(self.component_gonol_ids) < 2 or self.carrier != expected:
            raise OEWNDefinitionRecursionError("composite word relation must be intrinsic")
        if not self.atomic_at_next_scale:
            raise OEWNDefinitionRecursionError("composite word must close atomically")

    @property
    def gonol_id(self) -> str:
        return _identity("ucns.oewn-composite-word-gonol:sha256:", {
            "exact_text": self.exact_text,
            "component_gonol_ids": list(self.component_gonol_ids),
            "exact_space_boundaries": [list(item) for item in self.exact_space_boundaries],
            "source_receipt_id": self.source_receipt_id,
            "carrier_id": self.carrier.stable_identity,
            "atomic_at_next_scale": self.atomic_at_next_scale,
            "standing": self.standing,
        })


@dataclass(frozen=True, slots=True)
class OEWNMorphologyGonol:
    entry_key: str
    lemma_gonol_id: str
    form_gonol_id: str
    form_ordinal: int
    source_receipt_id: str
    carrier: RelationalCarrier
    atomic_at_next_scale: bool = True
    inferred_decomposition: bool = False
    standing: str = MORPHOLOGY_STANDING

    def __post_init__(self) -> None:
        if self.carrier != build_relational_carrier(
            3, ((0, MORPHOLOGY_FORM_RELATION_CODE, 1), (0, MORPHOLOGY_FORM_RELATION_CODE, 2)),
        ):
            raise OEWNDefinitionRecursionError("morphology relation must be intrinsic")
        if self.form_ordinal < 0 or self.inferred_decomposition:
            raise OEWNDefinitionRecursionError("morphology cannot infer decomposition")
        if not self.atomic_at_next_scale or self.standing != MORPHOLOGY_STANDING:
            raise OEWNDefinitionRecursionError("morphology standing cannot be promoted")

    @property
    def gonol_id(self) -> str:
        return _identity("ucns.oewn-morphology-gonol:sha256:", {
            "entry_key": self.entry_key, "lemma_gonol_id": self.lemma_gonol_id,
            "form_gonol_id": self.form_gonol_id, "form_ordinal": self.form_ordinal,
            "source_receipt_id": self.source_receipt_id,
            "carrier_id": self.carrier.stable_identity,
            "atomic_at_next_scale": self.atomic_at_next_scale,
            "inferred_decomposition": self.inferred_decomposition,
            "standing": self.standing,
        })


@dataclass(frozen=True, slots=True)
class OEWNDefinitionOccurrence:
    ordinal: int
    start: int
    end: int
    participant_id: str
    kind: str = INSCRIPTION_KIND
    public_gonol_index: int | None = None

    def __init__(
        self,
        ordinal: int,
        start: int,
        end: int,
        participant_id: str | None = None,
        kind: str = INSCRIPTION_KIND,
        public_gonol_index: int | None = None,
        inscription_gonol_id: str | None = None,
    ) -> None:
        if participant_id is None:
            participant_id = inscription_gonol_id
        if not participant_id:
            raise OEWNDefinitionRecursionError("occurrence requires a participant identity")
        object.__setattr__(self, "ordinal", ordinal)
        object.__setattr__(self, "start", start)
        object.__setattr__(self, "end", end)
        object.__setattr__(self, "participant_id", participant_id)
        object.__setattr__(self, "kind", kind)
        object.__setattr__(self, "public_gonol_index", public_gonol_index)
        self.__post_init__()

    def __post_init__(self) -> None:
        if self.kind in {INSCRIPTION_KIND, CLOSED_WORD_KIND}:
            if self.public_gonol_index is not None:
                raise OEWNDefinitionRecursionError("word or inscription occurrence cannot carry a function index")
            return
        if self.kind != FUNCTION_KIND:
            raise OEWNDefinitionRecursionError("occurrence kind must be closed-word, inscription, or public-gonol-function")
        if self.public_gonol_index is None:
            raise OEWNDefinitionRecursionError("function occurrence requires a Public Gonol index")

    @property
    def inscription_gonol_id(self) -> str:
        return self.participant_id


@dataclass(frozen=True, slots=True)
class OEWNDefinitionGonol:
    entry_key: str
    target_gonol_id: str
    part_of_speech: str
    sense_id: str
    synset_id: str
    definition_ordinal: int
    exact_gloss: str
    occurrences: tuple[OEWNDefinitionOccurrence, ...]
    exact_space_boundaries: tuple[tuple[int, int, str], ...]
    source_receipt_id: str
    carrier: RelationalCarrier
    atomic_at_next_scale: bool = True
    standing: str = DEFINITION_STANDING

    def __post_init__(self) -> None:
        if self.definition_ordinal < 0:
            raise OEWNDefinitionRecursionError("definition ordinal must be nonnegative")
        if tuple(item.ordinal for item in self.occurrences) != tuple(range(len(self.occurrences))):
            raise OEWNDefinitionRecursionError("definition occurrences must be dense and ordered")
        expected = build_relational_carrier(
            1 + len(self.occurrences),
            ((0, DEFINITION_RELATION_CODE, index + 1) for index in range(len(self.occurrences))),
        )
        if self.carrier != expected:
            raise OEWNDefinitionRecursionError("definition semantic relation must be intrinsic")
        reconstructed = [""] * len(self.exact_gloss)
        for item in self.occurrences:
            if not (0 <= item.start < item.end <= len(self.exact_gloss)):
                raise OEWNDefinitionRecursionError("occurrence span outside gloss")
            reconstructed[item.start:item.end] = self.exact_gloss[item.start:item.end]
        for start, end, value in self.exact_space_boundaries:
            if value != self.exact_gloss[start:end] or any(ch not in _SPACE for ch in value):
                raise OEWNDefinitionRecursionError("SPACE boundary evidence mismatch")
            reconstructed[start:end] = value
        if "".join(reconstructed) != self.exact_gloss:
            raise OEWNDefinitionRecursionError("occurrences and SPACE boundaries do not reconstruct gloss")
        for item in self.occurrences:
            span = self.exact_gloss[item.start:item.end]
            if item.kind == FUNCTION_KIND:
                try:
                    index, _name = _function_by_glyph()[span]
                except KeyError as exc:
                    raise OEWNDefinitionRecursionError("function occurrence source glyph is not a Public Gonol function") from exc
                if item.public_gonol_index != index:
                    raise OEWNDefinitionRecursionError("function occurrence index does not match the source glyph")
                if item.participant_id != _function_participant_id(span, self.source_receipt_id):
                    raise OEWNDefinitionRecursionError("function participant does not match the source glyph")
        if not self.atomic_at_next_scale or self.standing != DEFINITION_STANDING:
            raise OEWNDefinitionRecursionError("definition standing cannot be promoted")

    @property
    def gonol_id(self) -> str:
        return _identity("ucns.oewn-definition-gonol:sha256:", {
            "entry_key": self.entry_key, "target_gonol_id": self.target_gonol_id,
            "part_of_speech": self.part_of_speech, "sense_id": self.sense_id,
            "synset_id": self.synset_id, "definition_ordinal": self.definition_ordinal,
            "exact_gloss": self.exact_gloss,
            "occurrences": [[x.ordinal, x.start, x.end, x.participant_id, x.kind, x.public_gonol_index]
                            for x in self.occurrences],
            "exact_space_boundaries": [list(x) for x in self.exact_space_boundaries],
            "source_receipt_id": self.source_receipt_id,
            "carrier_id": self.carrier.stable_identity,
            "atomic_at_next_scale": self.atomic_at_next_scale,
            "standing": self.standing,
        })


@dataclass(frozen=True, slots=True)
class OEWNDefinitionLayer:
    source_receipt_id: str
    inscriptions: tuple[OEWNInscriptionGonol, ...]
    composite_words: tuple[OEWNCompositeWordGonol, ...]
    morphology_gonols: tuple[OEWNMorphologyGonol, ...]
    definition_gonols: tuple[OEWNDefinitionGonol, ...]
    source_lexical_entry_count: int
    source_sense_count: int
    source_synset_count: int
    source_definition_count: int
    source_native_relation_occurrence_count: int
    closed_word_pairs: tuple[tuple[str, str], ...] = ()
    construction_passes: int = 2
    new_identities_on_final_pass: int = 0
    new_relationships_on_final_pass: int = 0
    all_pairs_graph_materialized: bool = False
    native_relation_mechanism_selected: bool = False
    final_morphology_law_selected: bool = False
    standing: str = LAYER_STANDING

    def __post_init__(self) -> None:
        if len({item.gonol_id for item in self.inscriptions}) != len(self.inscriptions):
            raise OEWNDefinitionRecursionError("inscription identities must be reused")
        if len({item.gonol_id for item in self.composite_words}) != len(self.composite_words):
            raise OEWNDefinitionRecursionError("composite word identities must be reused")
        if self.construction_passes != 2 or self.new_identities_on_final_pass != 0 or self.new_relationships_on_final_pass != 0:
            raise OEWNDefinitionRecursionError("fixed point requires an exhaustive zero-change replay pass")
        if self.all_pairs_graph_materialized or self.native_relation_mechanism_selected or self.final_morphology_law_selected:
            raise OEWNDefinitionRecursionError("unselected mechanisms cannot be promoted")
        if self.standing != LAYER_STANDING:
            raise OEWNDefinitionRecursionError("layer standing cannot be promoted")
        inscription_ids = {item.gonol_id for item in self.inscriptions}
        closed_ids = {gonol_id for _text, gonol_id in self.closed_word_pairs}
        closed_ids.update(item.gonol_id for item in self.composite_words)
        closed_ids.update(inscription_ids)
        for definition in self.definition_gonols:
            if definition.target_gonol_id not in closed_ids:
                raise OEWNDefinitionRecursionError("definition target is not a closed word in this layer")
            for occurrence in definition.occurrences:
                if occurrence.kind == INSCRIPTION_KIND:
                    if occurrence.participant_id not in inscription_ids:
                        raise OEWNDefinitionRecursionError("inscription participant is not in the layer inventory")
                elif occurrence.kind == CLOSED_WORD_KIND:
                    if occurrence.participant_id not in closed_ids:
                        raise OEWNDefinitionRecursionError("closed-word participant is not in the layer inventory")

    @property
    def layer_id(self) -> str:
        return _identity("ucns.oewn-definition-layer:sha256:", _layer_payload(self))


def _inscription(text: str, receipt_id: str) -> OEWNInscriptionGonol:
    return OEWNInscriptionGonol(
        text, receipt_id, tuple((ord(ch), edcm_carrier_position(ch)) for ch in text),
    )


def _function_participant_id(glyph: str, source_receipt_id: str) -> str:
    try:
        index, name = _function_by_glyph()[glyph]
    except KeyError as exc:
        raise OEWNDefinitionRecursionError("glyph is not a Public Gonol function") from exc
    return _identity("ucns.oewn-function-participant:sha256:", {
        "public_gonol_index": index,
        "glyph": glyph,
        "unicode_name": name,
        "public_gonol_sha256": PUBLIC_GONOL_SHA256,
        "source_receipt_id": source_receipt_id,
        "standing": FUNCTION_PARTICIPANT_STANDING,
    })


def _segments(text: str) -> tuple[tuple[int, int, str], ...]:
    if not text:
        return ()
    functions = _function_by_glyph()
    result: list[tuple[int, int, str]] = []
    cursor = 0
    while cursor < len(text):
        glyph = text[cursor]
        if glyph in _SPACE:
            end = cursor + 1
            while end < len(text) and text[end] in _SPACE:
                end += 1
            result.append((cursor, end, SPACE_KIND))
            cursor = end
            continue
        if glyph in functions:
            result.append((cursor, cursor + 1, FUNCTION_KIND))
            cursor += 1
            continue
        end = cursor + 1
        while end < len(text) and text[end] not in _SPACE and text[end] not in functions:
            end += 1
        result.append((cursor, end, INSCRIPTION_KIND))
        cursor = end
    return tuple(result)


def _longest_closed_word(
    token: str,
    closed_words: Mapping[str, str],
    functions: Mapping[str, object],
) -> str | None:
    for length in range(len(token), 0, -1):
        candidate = token[:length]
        if candidate not in closed_words:
            continue
        remainder = token[length:]
        if not remainder or remainder[0] in functions:
            return candidate
    return None


def _definition_spans(
    gloss: str,
    closed_words: Mapping[str, str],
) -> tuple[tuple[int, int, str], ...]:
    functions = _function_by_glyph()
    result: list[tuple[int, int, str]] = []
    cursor = 0
    while cursor < len(gloss):
        if gloss[cursor] in _SPACE:
            end = cursor + 1
            while end < len(gloss) and gloss[end] in _SPACE:
                end += 1
            result.append((cursor, end, SPACE_KIND))
            cursor = end
            continue
        token_end = cursor + 1
        while token_end < len(gloss) and gloss[token_end] not in _SPACE:
            token_end += 1
        token = gloss[cursor:token_end]
        pos = 0
        while pos < len(token):
            absolute = cursor + pos
            closed = _longest_closed_word(token[pos:], closed_words, functions)
            if closed is not None:
                result.append((absolute, absolute + len(closed), CLOSED_WORD_KIND))
                pos += len(closed)
                continue
            glyph = token[pos]
            if glyph in functions:
                result.append((absolute, absolute + 1, FUNCTION_KIND))
                pos += 1
                continue
            end = pos + 1
            while end < len(token) and token[end] not in functions:
                end += 1
            result.append((absolute, cursor + end, INSCRIPTION_KIND))
            pos = end
        cursor = token_end
    return tuple(result)


def oewn_entry_key(lemma: str, part_of_speech: str) -> str:
    """Return the stable source lexical-entry key used by definition gonols."""

    return _identity("ucns.oewn-entry:sha256:", {"lemma": lemma, "part_of_speech": part_of_speech})


def build_oewn_definition_layer(
    snapshot: OEWNCoreSnapshot,
    word_corpus: CharacterWordCorpus | None = None,
) -> OEWNDefinitionLayer:
    """Construct all explicit forms and every OEWN sense-definition relation."""

    if not isinstance(snapshot, OEWNCoreSnapshot):
        raise TypeError("snapshot must be an OEWNCoreSnapshot")
    receipt_id = snapshot.source_receipt_id
    corpus = word_corpus if word_corpus is not None else build_oewn_character_word_corpus(snapshot)
    if corpus.source.receipt_id != receipt_id:
        raise OEWNDefinitionRecursionError("word corpus and OEWN snapshot differ")
    source = AffixiationSource(receipt_id, "oewn-2025-core")
    inscription_by_text: dict[str, OEWNInscriptionGonol] = {}
    composite_by_text: dict[str, OEWNCompositeWordGonol] = {}
    closed_words: dict[str, str] = {}

    def admitted(text: str) -> OEWNInscriptionGonol:
        if not text or any(ch in _SPACE for ch in text):
            raise OEWNDefinitionRecursionError("only exact non-SPACE inscriptions are admitted")
        if any(ch in _function_by_glyph() for ch in text):
            raise OEWNDefinitionRecursionError("inscription cannot absorb a Public Gonol function")
        existing = inscription_by_text.get(text)
        if existing is not None:
            return existing
        constructed = _inscription(text, receipt_id)
        inscription_by_text[text] = constructed
        return constructed

    def admitted_participant(text: str, kind: str) -> str:
        if kind == FUNCTION_KIND:
            return _function_participant_id(text, receipt_id)
        return admitted(text).gonol_id

    def admitted_word(text: str) -> str:
        segments = _segments(text)
        participants = [(start, end, kind) for start, end, kind in segments if kind != SPACE_KIND]
        if len(participants) == 1 and participants[0] == (0, len(text), INSCRIPTION_KIND):
            return admitted(text).gonol_id
        if len(participants) == 1 and participants[0][2] == FUNCTION_KIND:
            return _function_participant_id(text, receipt_id)
        existing = composite_by_text.get(text)
        if existing is not None:
            return existing.gonol_id
        components = tuple(
            admitted_participant(text[start:end], kind) for start, end, kind in participants
        )
        boundaries = tuple(
            (start, end, text[start:end]) for start, end, kind in segments if kind == SPACE_KIND
        )
        composite = OEWNCompositeWordGonol(
            text, components, boundaries, receipt_id,
            build_relational_carrier(
                len(components),
                ((index, COMPOSITION_RELATION_CODE, index + 1)
                 for index in range(len(components) - 1)),
            ),
        )
        composite_by_text[text] = composite
        return composite.gonol_id

    def register_closed_word(text: str) -> str:
        try:
            gonol_id = corpus.word(text).gonol_id
        except CharacterWordError:
            gonol_id = admitted_word(text)
        existing = closed_words.get(text)
        if existing is None:
            closed_words[text] = gonol_id
        elif existing != gonol_id:
            raise OEWNDefinitionRecursionError("closed word identity drifted")
        return gonol_id

    morphology: list[OEWNMorphologyGonol] = []
    sense_targets: dict[str, tuple[str, str, str, str]] = {}
    for entry in snapshot.lexical_entries:
        key = oewn_entry_key(entry.lemma, entry.part_of_speech)
        lemma_id = register_closed_word(entry.lemma)
        for ordinal, form_text in enumerate(entry.forms):
            form_id = register_closed_word(form_text)
            closed = affixiate(
                (lemma_id, form_id),
                AffixiationRelation(MORPHOLOGY_FORM_RELATION_CODE, "explicit-oewn-form"),
                source,
                "morphology",
                AffixiationClosure(
                    extras=(("entry_key", key), ("form_ordinal", ordinal)),
                ),
            )
            morphology.append(OEWNMorphologyGonol(
                key, lemma_id, form_id, ordinal, receipt_id, closed.carrier,
            ))
        for sense in entry.senses:
            if sense.sense_id in sense_targets:
                raise OEWNDefinitionRecursionError("duplicate OEWN sense identity")
            sense_targets[sense.sense_id] = (key, lemma_id, entry.part_of_speech, sense.synset_id)

    synset_by_id = {item.synset_id: item for item in snapshot.synsets}
    definitions: list[OEWNDefinitionGonol] = []
    for sense_id, (key, target_id, pos, synset_id) in sense_targets.items():
        synset = synset_by_id.get(synset_id)
        if synset is None:
            raise OEWNDefinitionRecursionError(f"sense references absent synset {synset_id}")
        for definition_ordinal, gloss in enumerate(synset.definitions):
            occurrences: list[OEWNDefinitionOccurrence] = []
            boundaries: list[tuple[int, int, str]] = []
            for start, end, kind in _definition_spans(gloss, closed_words):
                text = gloss[start:end]
                if kind == SPACE_KIND:
                    boundaries.append((start, end, text))
                    continue
                if kind == CLOSED_WORD_KIND:
                    occurrences.append(OEWNDefinitionOccurrence(
                        len(occurrences), start, end, closed_words[text], CLOSED_WORD_KIND,
                    ))
                    continue
                if kind == FUNCTION_KIND:
                    index, _name = _function_by_glyph()[text]
                    occurrences.append(OEWNDefinitionOccurrence(
                        len(occurrences), start, end,
                        _function_participant_id(text, receipt_id),
                        FUNCTION_KIND, index,
                    ))
                    continue
                word = admitted(text)
                occurrences.append(OEWNDefinitionOccurrence(
                    len(occurrences), start, end, word.gonol_id, INSCRIPTION_KIND,
                ))
            closed = affixiate(
                tuple(item.participant_id for item in occurrences),
                AffixiationRelation(DEFINITION_RELATION_CODE, "oewn-sense-definition"),
                source,
                "definition",
                AffixiationClosure(
                    exact_text=gloss,
                    extras=(
                        ("sense_id", sense_id),
                        ("synset_id", synset_id),
                        ("definition_ordinal", definition_ordinal),
                    ),
                ),
            )
            definitions.append(OEWNDefinitionGonol(
                key, target_id, pos, sense_id, synset_id, definition_ordinal,
                gloss, tuple(occurrences), tuple(boundaries), receipt_id,
                closed.carrier,
            ))
    layer = OEWNDefinitionLayer(
        receipt_id, tuple(inscription_by_text.values()), tuple(composite_by_text.values()),
        tuple(morphology), tuple(definitions),
        len(snapshot.lexical_entries), snapshot.sense_count, len(snapshot.synsets),
        snapshot.definition_count, snapshot.relation_occurrence_count,
        tuple(sorted(closed_words.items())),
    )
    expected_definition_gonols = sum(
        len(synset_by_id[sense.synset_id].definitions)
        for entry in snapshot.lexical_entries for sense in entry.senses
    )
    if len(layer.definition_gonols) != expected_definition_gonols:
        raise OEWNDefinitionRecursionError("source sense-definition scope is incomplete")
    return layer


def _layer_payload(layer: OEWNDefinitionLayer) -> dict[str, object]:
    unassigned = sorted({code for item in layer.inscriptions for code in item.carrier_unassigned_code_points})
    inscription_ids = [item.gonol_id for item in layer.inscriptions]
    composite_ids = [item.gonol_id for item in layer.composite_words]
    morphology_ids = [item.gonol_id for item in layer.morphology_gonols]
    definition_ids = [item.gonol_id for item in layer.definition_gonols]
    return {
        "source_receipt_id": layer.source_receipt_id,
        "inscription_count": len(layer.inscriptions),
        "inscription_gonol_ids_sha256": sha256(_canonical_bytes(inscription_ids)).hexdigest(),
        "composite_word_count": len(layer.composite_words),
        "composite_word_gonol_ids_sha256": sha256(_canonical_bytes(composite_ids)).hexdigest(),
        "morphology_gonol_count": len(layer.morphology_gonols),
        "morphology_gonol_ids_sha256": sha256(_canonical_bytes(morphology_ids)).hexdigest(),
        "definition_gonol_count": len(layer.definition_gonols),
        "definition_gonol_ids_sha256": sha256(_canonical_bytes(definition_ids)).hexdigest(),
        "source_lexical_entry_count": layer.source_lexical_entry_count,
        "source_sense_count": layer.source_sense_count,
        "source_synset_count": layer.source_synset_count,
        "source_definition_count": layer.source_definition_count,
        "source_native_relation_occurrence_count": layer.source_native_relation_occurrence_count,
        "carrier_unassigned_code_points": unassigned,
        "construction_passes": layer.construction_passes,
        "new_identities_on_final_pass": layer.new_identities_on_final_pass,
        "new_relationships_on_final_pass": layer.new_relationships_on_final_pass,
        "all_pairs_graph_materialized": layer.all_pairs_graph_materialized,
        "native_relation_mechanism_selected": layer.native_relation_mechanism_selected,
        "final_morphology_law_selected": layer.final_morphology_law_selected,
        "standing": layer.standing,
    }


def definition_layer_bytes(layer: OEWNDefinitionLayer) -> bytes:
    """Serialize the immutable complete-layer receipt, not expanded source prose."""

    if not isinstance(layer, OEWNDefinitionLayer):
        raise TypeError("layer must be an OEWNDefinitionLayer")
    return _canonical_bytes({"layer_id": layer.layer_id, **_layer_payload(layer)})


def replay_oewn_definition_layer(layer: OEWNDefinitionLayer, snapshot: OEWNCoreSnapshot) -> OEWNDefinitionLayer:
    """Independently rebuild the complete layer and compare canonical receipts."""

    rebuilt = build_oewn_definition_layer(snapshot)
    if definition_layer_bytes(rebuilt) != definition_layer_bytes(layer):
        raise OEWNDefinitionRecursionError("OEWN definition-layer replay mismatch")
    return rebuilt


def main(argv: Iterable[str] | None = None) -> int:
    """Build one exact complete-layer receipt from a verified OEWN checkout."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_repo")
    parser.add_argument("output")
    args = parser.parse_args(tuple(argv) if argv is not None else None)
    receipt = verify_oewn_2025_core(args.source_repo)
    snapshot = load_oewn_core(args.source_repo, receipt)
    layer = build_oewn_definition_layer(snapshot)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(definition_layer_bytes(layer))
    return 0


__all__ = [
    "CLOSED_WORD_KIND", "DEFINITION_RELATION_CODE", "FUNCTION_KIND",
    "INSCRIPTION_KIND",
    "MORPHOLOGY_FORM_RELATION_CODE",
    "OEWNCompositeWordGonol", "OEWNDefinitionGonol", "OEWNDefinitionLayer", "OEWNDefinitionOccurrence",
    "OEWNDefinitionRecursionError", "OEWNInscriptionGonol", "OEWNMorphologyGonol",
    "build_oewn_definition_layer", "definition_layer_bytes", "oewn_entry_key",
    "replay_oewn_definition_layer",
]


if __name__ == "__main__":  # pragma: no cover - exercised by full corpus receipt build
    sys.exit(main())
