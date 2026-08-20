# === MODULE_BUILD ===
# id: ucns_generic_gonol_affixiation
#   module_name: gonol_affixiation
#   module_kind: engine
#   summary: one generic candidate constructor affixiate(gonols, relation, source, scale, closure) used at every scale context
#   owner: Erin Spencer
#   public_surface: Gonol, AffixiationRelation, AffixiationSource, AffixiationClosure, AffixiationError, SCALE_CONTEXTS, AFFIXIATE_CONSTRUCTOR_ID, AFFIXIATE_VERSION, AFFIXIATE_STANDING, affixiate
#   internal_surface: _canonical_bytes, _identity, _carrier, _participant_id
#   auth_boundary: none
#   storage_boundary: immutable in-memory construction and canonical identities only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_gonol_affixiation
#   rollout: declared candidate constructor; selection remains unresolved
#   rollback: remove this primitive and migrate call sites back to source-specific closures without rewriting historical receipts
#   requires: ucns_relational_carrier
#   since: 2026-08-19
#   unresolved: selection of this constructor as canon, complete English morphology law, sentence/paragraph/chapter/work source construction, whether recursive relations later deserve a distinct scale-context name
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: affixiate_is_one_generic_constructor
#   given: gonols, relation, source, scale, and closure are supplied
#   then: exactly one Gonol is returned whose identity binds those arguments and whose standing cannot be promoted to selected canon
#   class: doctrine
#   since: 2026-08-19
#
# id: affixiate_scale_is_context_not_type
#   given: the same constructor is used at two declared scale contexts
#   then: both results are Gonol values; scale is a bound context field, not a distinct object type
#   class: doctrine
#   since: 2026-08-19
#
# id: affixiate_relation_enters_the_gonol
#   given: ordered participant gonols and a relation are affixiated
#   then: the relation enters one intrinsic carrier and the completed gonol is atomic at the next scale
#   class: correctness
#   since: 2026-08-19
#
# id: affixiate_reuses_completed_identity
#   given: the same participants, relation, source, scale, and closure are affixiated twice
#   then: the gonol identities are identical
#   class: correctness
#   since: 2026-08-19
#
# id: affixiate_refuses_invented_scale_or_selection
#   given: an undeclared scale context or selected=true is requested
#   then: construction fails closed
#   class: safety
#   since: 2026-08-19
#
# id: affixiate_characters_are_gonols
#   given: a character-scale affixiation completes
#   then: the result is a Gonol; empty participants are allowed only for an atomic character-scale glyph gonol
#   class: doctrine
#   since: 2026-08-19
# === END CONTRACTS ===

"""Generic scale-invariant gonol constructor.

Usage::

    from ucns.gonol_affixiation import (
        AffixiationClosure,
        AffixiationRelation,
        AffixiationSource,
        affixiate,
    )

    glyph = affixiate(
        (),
        AffixiationRelation(9, "character-glyph"),
        AffixiationSource("ucns.oewn-core-receipt:sha256:" + "a" * 64, "oewn-2025-core"),
        "character",
        AffixiationClosure(exact_text="w", extras=(("kind", "character"),)),
    )
    letter = affixiate(
        (glyph,),
        AffixiationRelation(8, "history-bearing-character-step"),
        glyph.source,
        "character",
        AffixiationClosure(exact_text="w", extras=(("realized_prefix", "w"),)),
    )
    word = affixiate(
        (letter,),
        AffixiationRelation(6, "ordered-character-word-closure"),
        letter.source,
        "word",
        AffixiationClosure(exact_text="w"),
    )
    assert word.scale == "word"
    assert word.selected is False

This is a declared candidate. Selection as canon remains unresolved.
Character, word, morphology, definition, relation, sentence, paragraph,
chapter, and work are scale contexts, not different object types.
Sentence, paragraph, chapter, and work construction are declared contexts
without a source in this change.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Sequence

from .relational_carrier import RelationalCarrier, build_relational_carrier

AFFIXIATE_CONSTRUCTOR_ID = "ucns.gonol.affixiate"
AFFIXIATE_VERSION = "0.1.0"
AFFIXIATE_STANDING = "generic-affixiation-candidate"
SCALE_CONTEXTS = (
    "character",
    "word",
    "morphology",
    "definition",
    "relation",
    "sentence",
    "paragraph",
    "chapter",
    "work",
)
CHARACTER_STEP_RELATION_CODE = 8
CHARACTER_STEP_RELATION_LABEL = "history-bearing-character-step"
CHARACTER_GLYPH_RELATION_CODE = 9
CHARACTER_GLYPH_RELATION_LABEL = "character-glyph"


class AffixiationError(ValueError):
    """Raised when generic affixiation loses identity, scale context, or closure."""


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


def _carrier(participant_ids: tuple[str, ...], relation_code: int) -> RelationalCarrier:
    return build_relational_carrier(
        1 + len(participant_ids),
        ((0, relation_code, offset) for offset in range(1, len(participant_ids) + 1)),
    )


def _freeze_extra(value: object) -> object:
    if isinstance(value, dict):
        return tuple(sorted((str(key), _freeze_extra(item)) for key, item in value.items()))
    if isinstance(value, (list, tuple)):
        return tuple(_freeze_extra(item) for item in value)
    return value


def _participant_id(item: Gonol | str) -> str:
    if isinstance(item, Gonol):
        return item.gonol_id
    if isinstance(item, str) and item:
        return item
    raise AffixiationError("participants must be gonols or nonempty gonol identities")


@dataclass(frozen=True, slots=True)
class AffixiationRelation:
    """The relation that enters the resulting gonol."""

    code: int
    label: str

    def __post_init__(self) -> None:
        if isinstance(self.code, bool) or not isinstance(self.code, int) or self.code < 0:
            raise AffixiationError("relation code must be a nonnegative integer")
        if not self.label:
            raise AffixiationError("relation label must be nonempty")


@dataclass(frozen=True, slots=True)
class AffixiationSource:
    """Exact source identity for one affixiation."""

    receipt_id: str
    artifact: str = ""

    def __post_init__(self) -> None:
        if not self.receipt_id:
            raise AffixiationError("source receipt identity is required")


@dataclass(frozen=True, slots=True)
class AffixiationClosure:
    """Closure record bound into the completed gonol."""

    atomic: bool = True
    exact_text: str | None = None
    extras: tuple[tuple[str, object], ...] = ()

    def __post_init__(self) -> None:
        if type(self.atomic) is not bool or not self.atomic:
            raise AffixiationError("affixiation closure must be atomic at the next scale")
        if self.exact_text is not None and not isinstance(self.exact_text, str):
            raise AffixiationError("closure exact_text must be a string or None")
        names = [name for name, _value in self.extras]
        if len(set(names)) != len(names):
            raise AffixiationError("closure extras names must be unique")
        object.__setattr__(self, "extras", tuple((name, _freeze_extra(value)) for name, value in self.extras))


@dataclass(frozen=True, slots=True)
class Gonol:
    """One completed gonol. Scale is context, not a distinct type."""

    participant_ids: tuple[str, ...]
    relation: AffixiationRelation
    source: AffixiationSource
    scale: str
    closure: AffixiationClosure
    carrier: RelationalCarrier
    standing: str = AFFIXIATE_STANDING
    constructor_id: str = AFFIXIATE_CONSTRUCTOR_ID
    version: str = AFFIXIATE_VERSION
    selected: bool = False

    def __post_init__(self) -> None:
        if self.scale not in SCALE_CONTEXTS:
            raise AffixiationError("scale is not a declared scale context")
        if self.constructor_id != AFFIXIATE_CONSTRUCTOR_ID or self.version != AFFIXIATE_VERSION:
            raise AffixiationError("generic affixiation constructor identity cannot be retargeted")
        if self.standing != AFFIXIATE_STANDING:
            raise AffixiationError("generic affixiation standing cannot be promoted")
        if self.selected:
            raise AffixiationError("generic affixiation constructor cannot be selected as canon")
        if self.carrier != _carrier(self.participant_ids, self.relation.code):
            raise AffixiationError("relation must enter the affixiation carrier")
        if not self.participant_ids and self.scale != "character":
            raise AffixiationError("only an atomic character-scale glyph gonol may have no smaller gonol participants")

    @property
    def gonol_id(self) -> str:
        return _identity("ucns.gonol:sha256:", {
            "constructor_id": self.constructor_id,
            "version": self.version,
            "standing": self.standing,
            "selected": self.selected,
            "participant_ids": list(self.participant_ids),
            "relation_code": self.relation.code,
            "relation_label": self.relation.label,
            "source_receipt_id": self.source.receipt_id,
            "source_artifact": self.source.artifact,
            "scale": self.scale,
            "atomic": self.closure.atomic,
            "exact_text": self.closure.exact_text,
            "extras": [list(item) for item in self.closure.extras],
            "carrier_id": self.carrier.stable_identity,
        })

    @property
    def exact_text(self) -> str | None:
        return self.closure.exact_text

    @property
    def atomic_at_next_scale(self) -> bool:
        return self.closure.atomic

    def extra(self, name: str) -> object:
        for key, value in self.closure.extras:
            if key == name:
                return _freeze_extra(value)
        raise AffixiationError(f"closure extra {name!r} is absent")


def affixiate(
    gonols: Sequence[Gonol | str],
    relation: AffixiationRelation,
    source: AffixiationSource,
    scale: str,
    closure: AffixiationClosure,
) -> Gonol:
    """Close ordered gonols and an explicit relation into one gonol.

    Scale is a declared context. This constructor is a candidate; it is not
    selected canon.
    """

    if not isinstance(relation, AffixiationRelation):
        raise TypeError("relation must be an AffixiationRelation")
    if not isinstance(source, AffixiationSource):
        raise TypeError("source must be an AffixiationSource")
    if not isinstance(closure, AffixiationClosure):
        raise TypeError("closure must be an AffixiationClosure")
    if scale not in SCALE_CONTEXTS:
        raise AffixiationError("scale is not a declared scale context")
    participant_ids = tuple(_participant_id(item) for item in gonols)
    return Gonol(
        participant_ids,
        relation,
        source,
        scale,
        closure,
        _carrier(participant_ids, relation.code),
    )


__all__ = [
    "AFFIXIATE_CONSTRUCTOR_ID",
    "AFFIXIATE_STANDING",
    "AFFIXIATE_VERSION",
    "CHARACTER_GLYPH_RELATION_CODE",
    "CHARACTER_GLYPH_RELATION_LABEL",
    "CHARACTER_STEP_RELATION_CODE",
    "CHARACTER_STEP_RELATION_LABEL",
    "SCALE_CONTEXTS",
    "AffixiationClosure",
    "AffixiationError",
    "AffixiationRelation",
    "AffixiationSource",
    "Gonol",
    "affixiate",
]
