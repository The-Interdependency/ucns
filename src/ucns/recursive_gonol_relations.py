# === MODULE_BUILD ===
# id: ucns_source_native_recursive_gonols
#   module_name: recursive_gonol_relations
#   module_kind: engine
#   summary: constructs a declared source-native OEWN recursive-gonol candidate from already-closed word and definition gonols without selecting that candidate as canon
#   owner: Erin Spencer
#   public_surface: RecursiveGonol, RecursiveGonolLayer, RecursiveGonolError, SOURCE_NATIVE_RELATION_CODE, RECURSIVE_GONOL_CONSTRUCTOR_ID, build_source_native_recursive_gonols, recursive_gonol_layer_bytes, replay_source_native_recursive_gonols
#   internal_surface: _canonical_bytes, _identity, _index_layer, _resolve_word, _sense_participants, _synset_participants, _join
#   auth_boundary: requires an exact OEWN Core snapshot and its matching punctuation-aware definition layer
#   storage_boundary: immutable in-memory construction and canonical receipt bytes
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_recursive_gonol_relations
#   rollout: declared candidate after the punctuation-aware definition layer; selection remains unresolved
#   rollback: remove this candidate module and public exports without rewriting sealed definition-layer receipts
#   requires: ucns_oewn_2025_core, ucns_oewn_definition_recursion, ucns_relational_carrier
#   since: 2026-08-19
#   unresolved: whether this candidate later becomes selected canon, whether another source-backed relation set should be constructed next
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: recursive_gonol_is_declared_candidate
#   given: a recursive gonol layer is constructed
#   then: constructor identity, frozen participant-assembly choice, and selected=false are bound and standing cannot be promoted
#   class: doctrine
#   since: 2026-08-19
#
# id: recursive_gonol_preserves_closed_lower_gonols
#   given: a recursive gonol is constructed from a definition layer
#   then: every participant is an already-closed word or definition gonol identity from that layer
#   class: doctrine
#   since: 2026-08-19
#
# id: recursive_gonol_binds_each_source_relation
#   given: an OEWN snapshot and matching definition layer are constructed
#   then: every source-native sense and synset relation occurrence becomes one recursive gonol with the exact source label and source order
#   class: evidence
#   since: 2026-08-19
#
# id: recursive_gonol_refuses_invented_pairing
#   given: a source or target has multiple definition gonols
#   then: those gonols participate as an ordered list in one occurrence and are not expanded into a cartesian product
#   class: safety
#   since: 2026-08-19
#
# id: recursive_gonol_layer_replays_byte_exactly
#   given: a completed candidate layer and the same snapshot and definition layer are independently reconstructed
#   then: canonical receipt bytes agree exactly or replay fails closed
#   class: evidence
#   since: 2026-08-19
# === END CONTRACTS ===

"""Declared source-native recursive gonol candidate.

Usage::

    recursive = build_source_native_recursive_gonols(snapshot, definition_layer)
    replay_source_native_recursive_gonols(recursive, snapshot, definition_layer)

This is a falsifiable candidate. It does not select native OEWN relations as
canon and does not reopen closed word or definition gonols.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json

from .gonol_affixiation import AffixiationClosure, AffixiationRelation, AffixiationSource, affixiate
from .oewn_core import OEWNCoreSnapshot
from .oewn_definition_recursion import (
    OEWNDefinitionGonol,
    OEWNDefinitionLayer,
    OEWNDefinitionRecursionError,
    _function_participant_id,
)
from .relational_carrier import RelationalCarrier, build_relational_carrier

RECURSIVE_GONOL_CONSTRUCTOR_ID = "ucns.recursive-gonol.source-native-oewn-relations"
RECURSIVE_GONOL_VERSION = "0.1.0"
RECURSIVE_GONOL_STANDING = "source-native-recursive-gonol-candidate"
PARTICIPANT_ASSEMBLY = (
    "source-word+source-definition-gonols+target-word+target-definition-gonols;"
    "synset-members-in-source-order;no-cartesian-definition-pairing"
)
SOURCE_NATIVE_RELATION_CODE = 7
SENSE_ADDRESS_KIND = "sense"
SYNSET_ADDRESS_KIND = "synset"
WORD_PARTICIPANT_KIND = "closed-word"
DEFINITION_PARTICIPANT_KIND = "closed-definition"


class RecursiveGonolError(ValueError):
    """Raised when the declared recursive-gonol candidate cannot replay exactly."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"


def _identity(prefix: str, value: object) -> str:
    return prefix + sha256(_canonical_bytes(value)).hexdigest()


@dataclass(frozen=True, slots=True)
class RecursiveParticipant:
    ordinal: int
    gonol_id: str
    kind: str

    def __post_init__(self) -> None:
        if self.ordinal < 0:
            raise RecursiveGonolError("participant ordinal must be nonnegative")
        if not self.gonol_id:
            raise RecursiveGonolError("participant requires a closed gonol identity")
        if self.kind not in {WORD_PARTICIPANT_KIND, DEFINITION_PARTICIPANT_KIND}:
            raise RecursiveGonolError("participant kind must be closed-word or closed-definition")


@dataclass(frozen=True, slots=True)
class RecursiveGonol:
    ordinal: int
    address_kind: str
    source_address: str
    target_address: str
    relation_label: str
    participants: tuple[RecursiveParticipant, ...]
    source_receipt_id: str
    definition_layer_id: str
    carrier: RelationalCarrier
    atomic_at_next_scale: bool = True
    standing: str = RECURSIVE_GONOL_STANDING

    def __post_init__(self) -> None:
        if self.ordinal < 0:
            raise RecursiveGonolError("recursive gonol ordinal must be nonnegative")
        if self.address_kind not in {SENSE_ADDRESS_KIND, SYNSET_ADDRESS_KIND}:
            raise RecursiveGonolError("address kind must be sense or synset")
        if not self.source_address or not self.target_address or not self.relation_label:
            raise RecursiveGonolError("source-native relation identity is incomplete")
        if tuple(item.ordinal for item in self.participants) != tuple(range(len(self.participants))):
            raise RecursiveGonolError("recursive participants must be dense and ordered")
        if not self.participants:
            raise RecursiveGonolError("recursive gonol requires at least one closed participant")
        expected = build_relational_carrier(
            1 + len(self.participants),
            ((0, SOURCE_NATIVE_RELATION_CODE, index + 1) for index in range(len(self.participants))),
        )
        if self.carrier != expected:
            raise RecursiveGonolError("source-native relation must enter the recursive carrier")
        if not self.atomic_at_next_scale or self.standing != RECURSIVE_GONOL_STANDING:
            raise RecursiveGonolError("recursive gonol standing cannot be promoted")

    @property
    def gonol_id(self) -> str:
        return _identity("ucns.recursive-gonol:sha256:", {
            "constructor_id": RECURSIVE_GONOL_CONSTRUCTOR_ID,
            "ordinal": self.ordinal,
            "address_kind": self.address_kind,
            "source_address": self.source_address,
            "target_address": self.target_address,
            "relation_label": self.relation_label,
            "participants": [[item.ordinal, item.gonol_id, item.kind] for item in self.participants],
            "source_receipt_id": self.source_receipt_id,
            "definition_layer_id": self.definition_layer_id,
            "carrier_id": self.carrier.stable_identity,
            "atomic_at_next_scale": self.atomic_at_next_scale,
            "standing": self.standing,
        })


@dataclass(frozen=True, slots=True)
class RecursiveGonolLayer:
    source_receipt_id: str
    definition_layer_id: str
    gonols: tuple[RecursiveGonol, ...]
    source_native_relation_occurrence_count: int
    constructor_id: str = RECURSIVE_GONOL_CONSTRUCTOR_ID
    version: str = RECURSIVE_GONOL_VERSION
    participant_assembly: str = PARTICIPANT_ASSEMBLY
    selected: bool = False
    native_relation_mechanism_selected: bool = False
    all_pairs_graph_materialized: bool = False
    standing: str = RECURSIVE_GONOL_STANDING

    def __post_init__(self) -> None:
        if self.constructor_id != RECURSIVE_GONOL_CONSTRUCTOR_ID or self.version != RECURSIVE_GONOL_VERSION:
            raise RecursiveGonolError("recursive constructor identity cannot be retargeted")
        if self.participant_assembly != PARTICIPANT_ASSEMBLY:
            raise RecursiveGonolError("participant-assembly choice cannot be rewritten")
        if (
            self.selected
            or self.native_relation_mechanism_selected
            or self.all_pairs_graph_materialized
        ):
            raise RecursiveGonolError("recursive candidate cannot be promoted or expanded into all-pairs")
        if self.standing != RECURSIVE_GONOL_STANDING:
            raise RecursiveGonolError("recursive layer standing cannot be promoted")
        if tuple(item.ordinal for item in self.gonols) != tuple(range(len(self.gonols))):
            raise RecursiveGonolError("recursive gonols must be dense and ordered")
        if len(self.gonols) != self.source_native_relation_occurrence_count:
            raise RecursiveGonolError("recursive gonol count does not match source relation occurrences")
        if len({item.gonol_id for item in self.gonols}) != len(self.gonols):
            raise RecursiveGonolError("recursive gonol identities must be unique")

    @property
    def layer_id(self) -> str:
        return _identity("ucns.recursive-gonol-layer:sha256:", _layer_payload(self))


def _layer_payload(layer: RecursiveGonolLayer) -> dict[str, object]:
    gonol_ids = [item.gonol_id for item in layer.gonols]
    return {
        "constructor_id": layer.constructor_id,
        "version": layer.version,
        "standing": layer.standing,
        "selected": layer.selected,
        "native_relation_mechanism_selected": layer.native_relation_mechanism_selected,
        "all_pairs_graph_materialized": layer.all_pairs_graph_materialized,
        "participant_assembly": layer.participant_assembly,
        "source_receipt_id": layer.source_receipt_id,
        "definition_layer_id": layer.definition_layer_id,
        "source_native_relation_occurrence_count": layer.source_native_relation_occurrence_count,
        "recursive_gonol_count": len(layer.gonols),
        "recursive_gonol_ids_sha256": sha256(_canonical_bytes(gonol_ids)).hexdigest(),
    }


@dataclass(frozen=True, slots=True)
class _SenseIndex:
    word_gonol_id: str
    definitions: tuple[OEWNDefinitionGonol, ...]


def _word_index(layer: OEWNDefinitionLayer) -> dict[str, str]:
    by_text: dict[str, str] = dict(layer.closed_word_pairs)
    for item in layer.composite_words:
        by_text.setdefault(item.exact_text, item.gonol_id)
    for item in layer.inscriptions:
        by_text.setdefault(item.text, item.gonol_id)
    return by_text


def _resolve_word(by_text: dict[str, str], layer: OEWNDefinitionLayer, text: str) -> str:
    existing = by_text.get(text)
    if existing is not None:
        return existing
    if len(text) == 1:
        try:
            identifier = _function_participant_id(text, layer.source_receipt_id)
        except OEWNDefinitionRecursionError as exc:
            raise RecursiveGonolError(f"unresolved closed-word participant {text!r}") from exc
        by_text[text] = identifier
        return identifier
    raise RecursiveGonolError(f"unresolved closed-word participant {text!r}")


def _index_layer(
    snapshot: OEWNCoreSnapshot,
    layer: OEWNDefinitionLayer,
) -> tuple[dict[str, _SenseIndex], dict[str, tuple[str, ...]], dict[str, tuple[OEWNDefinitionGonol, ...]]]:
    words = _word_index(layer)
    senses: dict[str, _SenseIndex] = {}
    grouped: dict[str, list[OEWNDefinitionGonol]] = {}
    for item in layer.definition_gonols:
        grouped.setdefault(item.sense_id, []).append(item)
    for sense_id, definitions in grouped.items():
        word_ids = {item.target_gonol_id for item in definitions}
        if len(word_ids) != 1:
            raise RecursiveGonolError(f"sense {sense_id} closed-word identity drifted")
        senses[sense_id] = _SenseIndex(next(iter(word_ids)), tuple(definitions))
    synset_definitions: dict[str, list[OEWNDefinitionGonol]] = {}
    for item in layer.definition_gonols:
        synset_definitions.setdefault(item.synset_id, []).append(item)
    synset_members: dict[str, tuple[str, ...]] = {}
    for synset in snapshot.synsets:
        synset_members[synset.synset_id] = tuple(
            _resolve_word(words, layer, member) for member in synset.members
        )
    return senses, synset_members, {key: tuple(value) for key, value in synset_definitions.items()}


def _participants_from(
    word_ids: tuple[str, ...],
    definitions: tuple[OEWNDefinitionGonol, ...],
) -> tuple[RecursiveParticipant, ...]:
    built: list[RecursiveParticipant] = []
    for word_id in word_ids:
        built.append(RecursiveParticipant(len(built), word_id, WORD_PARTICIPANT_KIND))
    for item in definitions:
        built.append(RecursiveParticipant(len(built), item.gonol_id, DEFINITION_PARTICIPANT_KIND))
    return tuple(built)


def _sense_participants(
    sense_id: str,
    senses: dict[str, _SenseIndex],
) -> tuple[RecursiveParticipant, ...]:
    try:
        record = senses[sense_id]
    except KeyError as exc:
        raise RecursiveGonolError(f"relation references absent sense {sense_id}") from exc
    return _participants_from((record.word_gonol_id,), record.definitions)


def _synset_participants(
    synset_id: str,
    members: dict[str, tuple[str, ...]],
    definitions: dict[str, tuple[OEWNDefinitionGonol, ...]],
) -> tuple[RecursiveParticipant, ...]:
    try:
        words = members[synset_id]
    except KeyError as exc:
        raise RecursiveGonolError(f"relation references absent synset {synset_id}") from exc
    return _participants_from(words, definitions.get(synset_id, ()))


def _join(
    left: tuple[RecursiveParticipant, ...],
    right: tuple[RecursiveParticipant, ...],
) -> tuple[RecursiveParticipant, ...]:
    joined = list(left)
    for item in right:
        joined.append(RecursiveParticipant(len(joined), item.gonol_id, item.kind))
    return tuple(joined)


def _close(
    participants: tuple[RecursiveParticipant, ...],
    *,
    source: AffixiationSource,
    relation_label: str,
    address_kind: str,
    source_address: str,
    target_address: str,
) -> RelationalCarrier:
    closed = affixiate(
        tuple(item.gonol_id for item in participants),
        AffixiationRelation(SOURCE_NATIVE_RELATION_CODE, relation_label),
        source,
        "relation",
        AffixiationClosure(
            extras=(
                ("address_kind", address_kind),
                ("source_address", source_address),
                ("target_address", target_address),
            ),
        ),
    )
    return closed.carrier


def build_source_native_recursive_gonols(
    snapshot: OEWNCoreSnapshot,
    definition_layer: OEWNDefinitionLayer,
) -> RecursiveGonolLayer:
    """Close one candidate recursive gonol per source-native OEWN relation."""

    if not isinstance(snapshot, OEWNCoreSnapshot):
        raise TypeError("snapshot must be an OEWNCoreSnapshot")
    if not isinstance(definition_layer, OEWNDefinitionLayer):
        raise TypeError("definition_layer must be an OEWNDefinitionLayer")
    if definition_layer.source_receipt_id != snapshot.source_receipt_id:
        raise RecursiveGonolError("definition layer and OEWN snapshot differ")
    senses, synset_members, synset_definitions = _index_layer(snapshot, definition_layer)
    gonols: list[RecursiveGonol] = []
    receipt_id = snapshot.source_receipt_id
    layer_id = definition_layer.layer_id
    source = AffixiationSource(receipt_id, "oewn-2025-core")

    def add(
        address_kind: str,
        source_address: str,
        target_address: str,
        relation_label: str,
        participants: tuple[RecursiveParticipant, ...],
    ) -> None:
        gonols.append(RecursiveGonol(
            len(gonols), address_kind, source_address, target_address, relation_label,
            participants, receipt_id, layer_id, _close(
                participants,
                source=source,
                relation_label=relation_label,
                address_kind=address_kind,
                source_address=source_address,
                target_address=target_address,
            ),
        ))

    for entry in snapshot.lexical_entries:
        for sense in entry.senses:
            source_parts = _sense_participants(sense.sense_id, senses)
            for relation_label, targets in sense.relations:
                for target in targets:
                    add(
                        SENSE_ADDRESS_KIND, sense.sense_id, target, relation_label,
                        _join(source_parts, _sense_participants(target, senses)),
                    )
    for synset in snapshot.synsets:
        source_parts = _synset_participants(synset.synset_id, synset_members, synset_definitions)
        for relation_label, targets in synset.relations:
            for target in targets:
                add(
                    SYNSET_ADDRESS_KIND, synset.synset_id, target, relation_label,
                    _join(source_parts, _synset_participants(target, synset_members, synset_definitions)),
                )
    return RecursiveGonolLayer(
        receipt_id, layer_id, tuple(gonols), snapshot.relation_occurrence_count,
    )


def recursive_gonol_layer_bytes(layer: RecursiveGonolLayer) -> bytes:
    """Serialize the candidate-layer receipt, not expanded relation prose."""

    if not isinstance(layer, RecursiveGonolLayer):
        raise TypeError("layer must be a RecursiveGonolLayer")
    return _canonical_bytes({"layer_id": layer.layer_id, **_layer_payload(layer)})


def replay_source_native_recursive_gonols(
    layer: RecursiveGonolLayer,
    snapshot: OEWNCoreSnapshot,
    definition_layer: OEWNDefinitionLayer,
) -> RecursiveGonolLayer:
    """Independently rebuild the candidate layer and compare canonical receipts."""

    rebuilt = build_source_native_recursive_gonols(snapshot, definition_layer)
    if recursive_gonol_layer_bytes(rebuilt) != recursive_gonol_layer_bytes(layer):
        raise RecursiveGonolError("recursive gonol-layer replay mismatch")
    return rebuilt


__all__ = [
    "DEFINITION_PARTICIPANT_KIND",
    "PARTICIPANT_ASSEMBLY",
    "RECURSIVE_GONOL_CONSTRUCTOR_ID",
    "RECURSIVE_GONOL_STANDING",
    "RECURSIVE_GONOL_VERSION",
    "SOURCE_NATIVE_RELATION_CODE",
    "WORD_PARTICIPANT_KIND",
    "RecursiveGonol",
    "RecursiveGonolError",
    "RecursiveGonolLayer",
    "RecursiveParticipant",
    "build_source_native_recursive_gonols",
    "recursive_gonol_layer_bytes",
    "replay_source_native_recursive_gonols",
]
