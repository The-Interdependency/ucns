# === MODULE_BUILD ===
# id: ucns_oewn_2025_core
#   module_name: oewn_core
#   module_kind: adapter
#   summary: ingests the exact verified OEWN 2025 Core YAML tree into deterministic lexical-entry, sense, synset, definition, relation, and morphology-evidence records
#   owner: Erin Spencer
#   public_surface: OEWNSense, OEWNLexicalEntry, OEWNSynset, OEWNCoreSnapshot, OEWNMorphologyInventory, load_oewn_core, inventory_oewn_morphology
#   internal_surface: _load_yaml, _relations, _entry_files, _synset_files
#   auth_boundary: requires an exact OEWNCoreReceipt verified against the same checkout
#   storage_boundary: reads exact Core YAML only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_oewn_core
#   rollout: current lexical construction after source receipt; morphology inventory precedes any morphology-law selection
#   rollback: remove adapter and derived inventory while retaining exact source receipt
#   requires: ucns_current_lexical_sources
#   since: 2026-08-18
#   unresolved: final morphology law, meaning of native semantic relations in later recursion, multi-inscription lexical-entry composition
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: oewn_core_ingestion_is_complete_and_deterministic
#   given: the exact verified OEWN 2025 Core checkout is loaded
#   then: every Core lexical entry, form, sense, synset, definition, and native relation occurrence is retained in deterministic source-derived records
#   class: evidence
#   since: 2026-08-18
#
# id: oewn_morphology_inventory_precedes_law
#   given: OEWN morphology evidence is inventoried
#   then: explicit source forms, spelling structure, parts of speech, multi-inscription entries, character coverage, and absence of an explicit decomposition law are reported without selecting roots, stems, affixes, or transformations
#   class: doctrine
#   since: 2026-08-18
# === END CONTRACTS ===

"""Deterministic Open English WordNet 2025 Core ingestion and inventory.

Usage::

    receipt = verify_oewn_2025_core(checkout)
    snapshot = load_oewn_core(checkout, receipt)
    inventory = inventory_oewn_morphology(snapshot)
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Mapping

from .edcm import edcm_carrier_position
from .lexical_sources import OEWNCoreReceipt, verify_oewn_2025_core

_ENTRY_NON_RELATIONS = {"id", "synset", "sent", "subcat", "adjposition"}
_SYNSET_NON_RELATIONS = {
    "ili", "partOfSpeech", "definition", "example", "members", "source",
    "wikidata",
}


class OEWNCoreError(ValueError):
    """Raised when OEWN Core evidence is malformed or not receipt-bound."""


@dataclass(frozen=True, slots=True)
class OEWNSense:
    sense_id: str
    synset_id: str
    relations: tuple[tuple[str, tuple[str, ...]], ...]
    subcategories: tuple[str, ...]
    adjective_position: str | None


@dataclass(frozen=True, slots=True)
class OEWNLexicalEntry:
    lemma: str
    part_of_speech: str
    forms: tuple[str, ...]
    senses: tuple[OEWNSense, ...]


@dataclass(frozen=True, slots=True)
class OEWNSynset:
    synset_id: str
    part_of_speech: str
    members: tuple[str, ...]
    definitions: tuple[str, ...]
    relations: tuple[tuple[str, tuple[str, ...]], ...]


@dataclass(frozen=True, slots=True)
class OEWNCoreSnapshot:
    source_receipt_id: str
    lexical_entries: tuple[OEWNLexicalEntry, ...]
    synsets: tuple[OEWNSynset, ...]

    @property
    def sense_count(self) -> int:
        return sum(len(item.senses) for item in self.lexical_entries)

    @property
    def definition_count(self) -> int:
        return sum(len(item.definitions) for item in self.synsets)

    @property
    def relation_occurrence_count(self) -> int:
        return sum(
            len(targets)
            for entry in self.lexical_entries
            for sense in entry.senses
            for _, targets in sense.relations
        ) + sum(
            len(targets)
            for synset in self.synsets
            for _, targets in synset.relations
        )


@dataclass(frozen=True, slots=True)
class OEWNMorphologyInventory:
    source_receipt_id: str
    lexical_entry_count: int
    explicit_form_count: int
    entries_with_forms: int
    unique_lemma_count: int
    single_inscription_entry_count: int
    multi_inscription_entry_count: int
    part_of_speech_counts: tuple[tuple[str, int], ...]
    character_counts: tuple[tuple[str, int], ...]
    public_carrier_unassigned_characters: tuple[str, ...]
    explicit_decomposition_records: int
    final_morphology_law_selected: bool = False
    standing: str = "complete-source-morphology-inventory"

    @property
    def inventory_id(self) -> str:
        payload = {
            "source_receipt_id": self.source_receipt_id,
            "lexical_entry_count": self.lexical_entry_count,
            "explicit_form_count": self.explicit_form_count,
            "entries_with_forms": self.entries_with_forms,
            "unique_lemma_count": self.unique_lemma_count,
            "single_inscription_entry_count": self.single_inscription_entry_count,
            "multi_inscription_entry_count": self.multi_inscription_entry_count,
            "part_of_speech_counts": [list(item) for item in self.part_of_speech_counts],
            "character_counts": [list(item) for item in self.character_counts],
            "public_carrier_unassigned_characters": list(self.public_carrier_unassigned_characters),
            "explicit_decomposition_records": self.explicit_decomposition_records,
            "final_morphology_law_selected": self.final_morphology_law_selected,
            "standing": self.standing,
        }
        encoded = json.dumps(
            payload, ensure_ascii=False, allow_nan=False, sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8") + b"\n"
        return "ucns.oewn-morphology-inventory:sha256:" + sha256(encoded).hexdigest()


def _load_yaml(path: Path) -> Mapping[str, Any]:
    try:
        import yaml
    except ImportError as exc:  # pragma: no cover - optional construction dependency
        raise RuntimeError("PyYAML is required for OEWN Core construction") from exc
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    value = yaml.load(path.read_text(encoding="utf-8"), Loader=loader)
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise OEWNCoreError(f"expected YAML mapping in {path}")
    return value


def _relations(
    value: Mapping[str, Any], excluded: set[str],
) -> tuple[tuple[str, tuple[str, ...]], ...]:
    result = []
    for key, targets in value.items():
        if key in excluded or not isinstance(targets, list):
            continue
        retained = tuple(str(item) for item in targets if isinstance(item, (str, int)))
        if retained:
            result.append((str(key), retained))
    return tuple(result)


def load_oewn_core(
    source_repo: str | Path,
    receipt: OEWNCoreReceipt,
) -> OEWNCoreSnapshot:
    """Load every record from the exact receipt-bound Core YAML tree."""

    if not isinstance(receipt, OEWNCoreReceipt):
        raise TypeError("receipt must be an OEWNCoreReceipt")
    current = verify_oewn_2025_core(source_repo)
    if current != receipt:
        raise OEWNCoreError("OEWN Core receipt is stale or forged")
    root = Path(source_repo).resolve() / "src" / "yaml"
    entries: list[OEWNLexicalEntry] = []
    for path in sorted(root.rglob("entries-*.yaml")):
        for raw_lemma, raw_pos_map in _load_yaml(path).items():
            if not isinstance(raw_pos_map, Mapping):
                continue
            for raw_pos, raw_entry in raw_pos_map.items():
                if not isinstance(raw_entry, Mapping):
                    continue
                senses = []
                for raw_sense in raw_entry.get("sense", ()) or ():
                    if not isinstance(raw_sense, Mapping):
                        continue
                    sense_id = str(raw_sense.get("id", ""))
                    synset_id = str(raw_sense.get("synset", ""))
                    if not sense_id or not synset_id:
                        raise OEWNCoreError(f"incomplete sense in {path}")
                    subcategories_raw = raw_sense.get("subcat", ()) or ()
                    subcategories = (
                        (subcategories_raw,)
                        if isinstance(subcategories_raw, str)
                        else tuple(str(item) for item in subcategories_raw)
                    )
                    senses.append(OEWNSense(
                        sense_id, synset_id,
                        _relations(raw_sense, _ENTRY_NON_RELATIONS),
                        subcategories,
                        None if raw_sense.get("adjposition") is None else str(raw_sense["adjposition"]),
                    ))
                entries.append(OEWNLexicalEntry(
                    str(raw_lemma), str(raw_pos),
                    tuple(str(item) for item in (raw_entry.get("form", ()) or ())),
                    tuple(senses),
                ))
    synsets: list[OEWNSynset] = []
    for path in sorted(root.rglob("*.yaml")):
        if path.name == "frames.yaml" or path.name.startswith("entries-"):
            continue
        for raw_id, raw_synset in _load_yaml(path).items():
            if not isinstance(raw_synset, Mapping):
                continue
            definitions = tuple(
                str(item.get("text", "")) if isinstance(item, Mapping) else str(item)
                for item in (raw_synset.get("definition", ()) or ())
            )
            synsets.append(OEWNSynset(
                str(raw_id), str(raw_synset.get("partOfSpeech", "")),
                tuple(str(item) for item in (raw_synset.get("members", ()) or ())),
                definitions, _relations(raw_synset, _SYNSET_NON_RELATIONS),
            ))
    return OEWNCoreSnapshot(receipt.receipt_id, tuple(entries), tuple(synsets))


def inventory_oewn_morphology(snapshot: OEWNCoreSnapshot) -> OEWNMorphologyInventory:
    """Inventory explicit source evidence without proposing a decomposition law."""

    entries = snapshot.lexical_entries
    characters = Counter(
        character
        for entry in entries
        for spelling in (entry.lemma, *entry.forms)
        for character in spelling
    )
    pos = Counter(entry.part_of_speech for entry in entries)
    multi = sum("_" in entry.lemma or " " in entry.lemma for entry in entries)
    return OEWNMorphologyInventory(
        source_receipt_id=snapshot.source_receipt_id,
        lexical_entry_count=len(entries),
        explicit_form_count=sum(len(entry.forms) for entry in entries),
        entries_with_forms=sum(bool(entry.forms) for entry in entries),
        unique_lemma_count=len({entry.lemma for entry in entries}),
        single_inscription_entry_count=len(entries) - multi,
        multi_inscription_entry_count=multi,
        part_of_speech_counts=tuple(sorted(pos.items())),
        character_counts=tuple(sorted(characters.items(), key=lambda item: ord(item[0]))),
        public_carrier_unassigned_characters=tuple(
            character for character in sorted(characters, key=ord)
            if edcm_carrier_position(character) is None
        ),
        explicit_decomposition_records=0,
    )


__all__ = [
    "OEWNCoreError", "OEWNCoreSnapshot", "OEWNLexicalEntry",
    "OEWNMorphologyInventory", "OEWNSense", "OEWNSynset",
    "inventory_oewn_morphology", "load_oewn_core",
]
