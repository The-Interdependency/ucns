# === MODULE_BUILD ===
# id: ucns_lexical_definition_gonols
#   module_name: lexical_definition_gonols
#   module_kind: engine
#   summary: constructs source-bound closed floor-definition gonols as the first UCNS lexical deep-recursion layer
#   owner: Erin Spencer
#   public_surface: DefinitionSourceReceipt, FloorDefinitionEvidence, DefinitionOccurrence, FloorDefinitionGonol, DefinitionLayerReceipt, build_floor_definition_gonol, build_complete_definition_layer, definition_layer_receipt_bytes
#   internal_surface: _canonical_bytes, _digest, _validate_identity
#   auth_boundary: caller supplies a source receipt and already-resolved floor-gonol identities; UCNS validates closure and constructs the gonols
#   storage_boundary: immutable values and canonical receipt bytes only
#   network_boundary: none
#   user_data_boundary: no user data; arbitrary source prose is represented only by an exact digest
#   admin_only: false
#   tests: tests.test_lexical_definition_gonols
#   rollout: historical NGSL closed-floor producer only; not part of the public ucns surface
#   rollback: remove this candidate layer without altering the punctuation-aware xkcd floor or OEWN producer
#   requires: ucns_lexical_floor, ucns_relational_carrier
#   since: 2026-08-18
#   deprecated: 2026-08-19 superseded by punctuation-aware xkcd floor reconstruction and OEWN definition recursion
#   unresolved: an authorized complete closed definition corpus, semantic efficacy, geometry, measurement, and recursion above depth one
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: floor_definition_support_is_closed
#   given: a floor-definition gonol is constructed
#   then: its target and every ordered constituent are exact gonol identities in the fixed supplied lexical floor
#   class: correctness
#   since: 2026-08-18
#
# id: floor_definition_order_multiplicity_and_sense_are_exact
#   given: constituent order, repetition, target, sense, context, source, or provenance differs
#   then: occurrence evidence and the definition-gonol identity differ without normalization, sorting, or deduplication
#   class: correctness
#   since: 2026-08-18
#
# id: complete_definition_layer_covers_every_floor_gonol
#   given: a complete definition layer is receipted
#   then: every admitted floor word gonol is targeted by at least one separately identified closed definition sense and no proposed evidence is silently rejected
#   class: evidence
#   since: 2026-08-18
#
# id: definition_gonols_are_first_recursion_not_measurement
#   given: a closed definition layer is constructed
#   then: its definition gonols are depth-one UCNS relational objects with no geometry, metric, EDCM measurement, semantic efficacy, or canon promotion
#   class: doctrine
#   since: 2026-08-18
# === END CONTRACTS ===

"""Closed floor-definition gonols for UCNS lexical deep recursion.

This module intentionally accepts resolved floor-gonol identities rather than
text or tokenizer output. Source owners may retain prose for custody, but UCNS
constructs a definition gonol only from already admitted lexical gonols.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
import re
from typing import Iterable

from .lexical_floor import LexicalHyperspacePotential, LexicalSourceReceipt
from .relational_carrier import RelationalCarrier, build_relational_carrier

DEFINITION_SOURCE_STANDING = "source-bound-definition-evidence"
DEFINITION_GONOL_STANDING = "closed-floor-definition-gonol-candidate"
DEFINITION_LAYER_STANDING = "complete-closed-first-recursion-candidate"
DEFINITION_RELATION_CODE = 0
DEFINITION_SOURCE_PREFIX = "ucns.definition-source-receipt:sha256:"
DEFINITION_GONOL_PREFIX = "ucns.floor-definition-gonol:sha256:"
DEFINITION_LAYER_PREFIX = "ucns.definition-layer-receipt:sha256:"
_HEX_64 = re.compile(r"[0-9a-f]{64}")


class LexicalDefinitionError(ValueError):
    """Raised when definition evidence crosses the fixed floor boundary."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"


def _digest(value: object) -> str:
    return sha256(_canonical_bytes(value)).hexdigest()


def _validate_nonempty(name: str, value: object) -> str:
    if not isinstance(value, str) or not value:
        raise LexicalDefinitionError(f"{name} must be a nonempty string")
    return value


@dataclass(frozen=True, slots=True)
class DefinitionSourceReceipt:
    """Exact custody identity for one externally authored definition corpus."""

    source_identity: str
    source_version: str
    license_identity: str
    content_sha256: str
    record_count: int
    provenance: str
    standing: str = DEFINITION_SOURCE_STANDING

    def __post_init__(self) -> None:
        for name in (
            "source_identity", "source_version", "license_identity", "provenance",
        ):
            _validate_nonempty(name, getattr(self, name))
        if not isinstance(self.content_sha256, str) or not _HEX_64.fullmatch(self.content_sha256):
            raise LexicalDefinitionError("definition source content digest is malformed")
        if isinstance(self.record_count, bool) or not isinstance(self.record_count, int) or self.record_count < 0:
            raise LexicalDefinitionError("definition source record count is invalid")
        if self.standing != DEFINITION_SOURCE_STANDING:
            raise LexicalDefinitionError("definition source standing cannot be promoted")

    @property
    def receipt_id(self) -> str:
        return DEFINITION_SOURCE_PREFIX + _digest((
            self.source_identity, self.source_version, self.license_identity,
            self.content_sha256, self.record_count, self.provenance, self.standing,
        ))


@dataclass(frozen=True, slots=True)
class FloorDefinitionEvidence:
    """One source sense already resolved to ordered fixed-floor gonol identities."""

    target_gonol_id: str
    sense_identity: str
    context_identity: str
    source_record_identity: str
    source_text_sha256: str
    constituent_gonol_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        for name in (
            "target_gonol_id", "sense_identity", "context_identity",
            "source_record_identity",
        ):
            _validate_nonempty(name, getattr(self, name))
        if not isinstance(self.source_text_sha256, str) or not _HEX_64.fullmatch(self.source_text_sha256):
            raise LexicalDefinitionError("definition source-text digest is malformed")
        if not isinstance(self.constituent_gonol_ids, tuple) or not self.constituent_gonol_ids:
            raise LexicalDefinitionError("a floor definition requires ordered constituents")
        for identity in self.constituent_gonol_ids:
            _validate_nonempty("constituent gonol identity", identity)


@dataclass(frozen=True, slots=True)
class DefinitionOccurrence:
    """One ordered occurrence relation from target to a constituent gonol."""

    position: int
    target_gonol_id: str
    constituent_gonol_id: str
    relation_code: int = DEFINITION_RELATION_CODE

    def __post_init__(self) -> None:
        if isinstance(self.position, bool) or not isinstance(self.position, int) or self.position < 0:
            raise LexicalDefinitionError("definition occurrence position is invalid")
        _validate_nonempty("target gonol identity", self.target_gonol_id)
        _validate_nonempty("constituent gonol identity", self.constituent_gonol_id)
        if self.relation_code != DEFINITION_RELATION_CODE:
            raise LexicalDefinitionError("definition relation code cannot be substituted")


@dataclass(frozen=True, slots=True)
class FloorDefinitionGonol:
    """One first-recursion object constituted by closed ordered relationships."""

    evidence: FloorDefinitionEvidence
    source_receipt_id: str
    floor_source_receipt_id: str
    occurrences: tuple[DefinitionOccurrence, ...]
    carrier: RelationalCarrier
    standing: str = DEFINITION_GONOL_STANDING
    geometry_attached: bool = False
    measurement_attached: bool = False

    def __post_init__(self) -> None:
        if not self.source_receipt_id.startswith(DEFINITION_SOURCE_PREFIX):
            raise LexicalDefinitionError("definition source receipt identity mismatch")
        if not self.floor_source_receipt_id.startswith("ucns.lexical-source-receipt:sha256:"):
            raise LexicalDefinitionError("lexical floor source receipt identity mismatch")
        expected = tuple(
            DefinitionOccurrence(index, self.evidence.target_gonol_id, identity)
            for index, identity in enumerate(self.evidence.constituent_gonol_ids)
        )
        if self.occurrences != expected:
            raise LexicalDefinitionError("definition occurrence order or multiplicity mismatch")
        expected_carrier = build_relational_carrier(
            1 + len(expected),
            tuple((0, DEFINITION_RELATION_CODE, index + 1) for index in range(len(expected))),
        )
        if self.carrier != expected_carrier:
            raise LexicalDefinitionError("definition intrinsic carrier mismatch")
        if self.standing != DEFINITION_GONOL_STANDING:
            raise LexicalDefinitionError("definition gonol standing cannot be promoted")
        if type(self.geometry_attached) is not bool or type(self.measurement_attached) is not bool:
            raise LexicalDefinitionError("definition transfer flags must be exact booleans")
        if self.geometry_attached or self.measurement_attached:
            raise LexicalDefinitionError("definition gonols attach no geometry or measurement")

    @property
    def gonol_id(self) -> str:
        return DEFINITION_GONOL_PREFIX + _digest({
            "target_gonol_id": self.evidence.target_gonol_id,
            "sense_identity": self.evidence.sense_identity,
            "context_identity": self.evidence.context_identity,
            "source_record_identity": self.evidence.source_record_identity,
            "source_text_sha256": self.evidence.source_text_sha256,
            "constituent_gonol_ids": list(self.evidence.constituent_gonol_ids),
            "source_receipt_id": self.source_receipt_id,
            "floor_source_receipt_id": self.floor_source_receipt_id,
            "occurrences": [
                [item.position, item.target_gonol_id, item.constituent_gonol_id,
                 item.relation_code]
                for item in self.occurrences
            ],
            "carrier": self.carrier.as_payload(),
            "standing": self.standing,
        })


@dataclass(frozen=True, slots=True)
class DefinitionLayerReceipt:
    """Replay receipt for a complete closed definition layer over one fixed floor."""

    floor_source_receipt_id: str
    definition_source_receipt_id: str
    floor_gonol_count: int
    definition_gonols: tuple[FloorDefinitionGonol, ...]
    definition_gonol_ids: tuple[str, ...]
    covered_target_gonol_ids: tuple[str, ...]
    standing: str = DEFINITION_LAYER_STANDING
    geometry_attached: bool = False
    measurement_attached: bool = False

    def __post_init__(self) -> None:
        if not self.floor_source_receipt_id.startswith("ucns.lexical-source-receipt:sha256:"):
            raise LexicalDefinitionError("definition layer floor receipt mismatch")
        if not self.definition_source_receipt_id.startswith(DEFINITION_SOURCE_PREFIX):
            raise LexicalDefinitionError("definition layer source receipt mismatch")
        if isinstance(self.floor_gonol_count, bool) or not isinstance(self.floor_gonol_count, int) or self.floor_gonol_count <= 0:
            raise LexicalDefinitionError("definition layer floor count is invalid")
        expected_ids = tuple(item.gonol_id for item in self.definition_gonols)
        if self.definition_gonol_ids != expected_ids:
            raise LexicalDefinitionError("definition layer gonol identities do not replay")
        expected_targets = tuple(sorted({item.evidence.target_gonol_id for item in self.definition_gonols}))
        if self.covered_target_gonol_ids != expected_targets:
            raise LexicalDefinitionError("definition layer target inventory mismatch")
        if len(expected_targets) != self.floor_gonol_count:
            raise LexicalDefinitionError("definition layer does not cover every floor gonol")
        identities = [
            (item.evidence.target_gonol_id, item.evidence.sense_identity,
             item.evidence.context_identity, item.evidence.source_record_identity)
            for item in self.definition_gonols
        ]
        if len(set(identities)) != len(identities):
            raise LexicalDefinitionError("definition layer contains duplicate sense evidence")
        if self.standing != DEFINITION_LAYER_STANDING:
            raise LexicalDefinitionError("definition layer standing cannot be promoted")
        if type(self.geometry_attached) is not bool or type(self.measurement_attached) is not bool:
            raise LexicalDefinitionError("definition layer transfer flags must be exact booleans")
        if self.geometry_attached or self.measurement_attached:
            raise LexicalDefinitionError("definition layer attaches no geometry or measurement")

    @property
    def receipt_id(self) -> str:
        return DEFINITION_LAYER_PREFIX + _digest(self.as_payload())

    def as_payload(self) -> dict[str, object]:
        return {
            "schema": "ucns.lexical-definition-layer-receipt",
            "version": "1.0.0",
            "floor_source_receipt_id": self.floor_source_receipt_id,
            "definition_source_receipt_id": self.definition_source_receipt_id,
            "floor_gonol_count": self.floor_gonol_count,
            "definition_gonol_ids": list(self.definition_gonol_ids),
            "covered_target_gonol_ids": list(self.covered_target_gonol_ids),
            "standing": self.standing,
            "geometry_attached": self.geometry_attached,
            "measurement_attached": self.measurement_attached,
        }


def build_floor_definition_gonol(
    potential: LexicalHyperspacePotential,
    floor_source_receipt: LexicalSourceReceipt,
    definition_source_receipt: DefinitionSourceReceipt,
    evidence: FloorDefinitionEvidence,
) -> FloorDefinitionGonol:
    """Construct one exact closed definition or reject the whole proposal."""

    known = {gonol.gonol_id for gonol in potential.word_gonols}
    if floor_source_receipt.word_count != len(known):
        raise LexicalDefinitionError("floor potential and source receipt count mismatch")
    if evidence.target_gonol_id not in known:
        raise LexicalDefinitionError("definition target is outside the fixed lexical floor")
    missing = tuple(identity for identity in evidence.constituent_gonol_ids if identity not in known)
    if missing:
        raise LexicalDefinitionError("definition constituent is outside the fixed lexical floor")
    occurrences = tuple(
        DefinitionOccurrence(index, evidence.target_gonol_id, identity)
        for index, identity in enumerate(evidence.constituent_gonol_ids)
    )
    carrier = build_relational_carrier(
        1 + len(occurrences),
        tuple((0, DEFINITION_RELATION_CODE, index + 1) for index in range(len(occurrences))),
    )
    return FloorDefinitionGonol(
        evidence=evidence,
        source_receipt_id=definition_source_receipt.receipt_id,
        floor_source_receipt_id=floor_source_receipt.receipt_id,
        occurrences=occurrences,
        carrier=carrier,
    )


def build_complete_definition_layer(
    potential: LexicalHyperspacePotential,
    floor_source_receipt: LexicalSourceReceipt,
    definition_source_receipt: DefinitionSourceReceipt,
    evidence: Iterable[FloorDefinitionEvidence],
) -> DefinitionLayerReceipt:
    """Construct all proposals and fail unless every fixed-floor gonol is covered."""

    proposals = tuple(evidence)
    if definition_source_receipt.record_count != len(proposals):
        raise LexicalDefinitionError("definition source receipt record count mismatch")
    gonols = tuple(
        build_floor_definition_gonol(
            potential, floor_source_receipt, definition_source_receipt, item
        )
        for item in proposals
    )
    known_targets = tuple(sorted(gonol.gonol_id for gonol in potential.word_gonols))
    covered_targets = tuple(sorted({item.evidence.target_gonol_id for item in gonols}))
    if covered_targets != known_targets:
        raise LexicalDefinitionError("complete definition layer is missing floor targets")
    return DefinitionLayerReceipt(
        floor_source_receipt_id=floor_source_receipt.receipt_id,
        definition_source_receipt_id=definition_source_receipt.receipt_id,
        floor_gonol_count=len(known_targets),
        definition_gonols=gonols,
        definition_gonol_ids=tuple(item.gonol_id for item in gonols),
        covered_target_gonol_ids=covered_targets,
    )


def definition_layer_receipt_bytes(receipt: DefinitionLayerReceipt) -> bytes:
    """Serialize the canonical replay identity of one complete definition layer."""

    if not isinstance(receipt, DefinitionLayerReceipt):
        raise TypeError("receipt must be a DefinitionLayerReceipt")
    return _canonical_bytes(receipt.as_payload())


__all__ = [
    "DEFINITION_GONOL_STANDING", "DEFINITION_LAYER_STANDING",
    "DEFINITION_RELATION_CODE", "DEFINITION_SOURCE_STANDING",
    "DefinitionLayerReceipt", "DefinitionOccurrence", "DefinitionSourceReceipt",
    "FloorDefinitionEvidence", "FloorDefinitionGonol", "LexicalDefinitionError",
    "build_complete_definition_layer", "build_floor_definition_gonol",
    "definition_layer_receipt_bytes",
]
