# === MODULE_BUILD ===
# id: ucns_public_gonol_function_table
#   module_name: public_gonol_functions
#   module_kind: engine
#   summary: binds each functional non-letter Public Gonol index to OEWN definition gonols and applies those bindings to caller-supplied atomic context
#   owner: Erin Spencer
#   public_surface: FunctionDefinitionBinding, PublicGonolFunction, PublicGonolFunctionTable, AtomicFunctionState, ContextualFunctionApplication, build_public_gonol_function_table, apply_public_gonol_function, function_table_bytes
#   internal_surface: _canonical_bytes, _identity, _source_terms, _definition_index
#   auth_boundary: exact Public Gonol fixture plus receipt-bound OEWN definition layer
#   storage_boundary: immutable values and canonical receipt bytes
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol_functions
#   rollout: after the complete OEWN first-recursion layer; index bindings remain candidate evidence
#   rollback: remove the table and application surface without altering Public Gonol or OEWN gonols
#   requires: edcm_word_gonol_profile, ucns_oewn_definition_recursion
#   since: 2026-08-18
#   unresolved: empirical contextual efficacy, definitions absent from OEWN Core, syntax above caller-supplied context, geometry of contextual application
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: public_gonol_indices_are_function_table_authority
#   given: the function table is built
#   then: every Public Gonol punctuation or symbol occupies its original exact index exactly once and no secondary symbol numbering exists
#   class: correctness
#   since: 2026-08-18
#
# id: public_gonol_functions_are_definition_bound
#   given: a functional non-letter index is admitted
#   then: all function bindings point to already-constructed OEWN definition gonols selected through frozen source-name terms and no independent punctuation grammar is attached
#   class: safety
#   since: 2026-08-18
#
# id: public_gonol_function_application_is_contextual_closure
#   given: a bound index is applied to a current atomic gonol state with caller-supplied ordered context
#   then: the prior atomic identity, definition-gonol functions, exact Public Gonol index, and context enter one closed application state that is atomic for subsequent application
#   class: correctness
#   since: 2026-08-18
#
# id: public_gonol_function_table_replays_exactly
#   given: identical Public Gonol and OEWN source evidence
#   then: table and contextual application identities reproduce exactly without normalization, inferred syntax, or ordering loss
#   class: evidence
#   since: 2026-08-18
# === END CONTRACTS ===

"""Definition-derived contextual functions at canonical Public Gonol indices.

Character names locate lexical evidence.  They do not define an operational
grammar.  The associated OEWN definition gonols are the function authority,
and callers supply the atomic context in which a function is coupled.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import argparse
import json
from pathlib import Path
import re
import sys
from typing import Mapping

from .edcm import PUBLIC_GONOL_157, PUBLIC_GONOL_SHA256
from .oewn_core import OEWNCoreSnapshot
from .lexical_sources import verify_oewn_2025_core
from .oewn_core import load_oewn_core
from .oewn_definition_recursion import (
    OEWNDefinitionLayer, build_oewn_definition_layer, oewn_entry_key,
)
from .relational_carrier import RelationalCarrier, build_relational_carrier

FUNCTION_RELATION_CODE = 3
CONTEXT_RELATION_CODE = 4
FUNCTION_NAME_SOURCE = "Unicode-15.0.0-character-name"
FUNCTION_TABLE_STANDING = "definition-derived-public-gonol-function-table-candidate"
APPLICATION_STANDING = "definition-derived-contextual-function-closure-candidate"

# Frozen Unicode 15.0 character names for Public Gonol punctuation and symbol
# positions.  Digits are quantities, not admitted as functional non-letters by
# this table.  Letters in every script remain lexical glyphs.
FUNCTIONAL_INDEX_NAMES: tuple[tuple[int, str, str], ...] = (
    (2, '!', 'EXCLAMATION MARK'),
    (3, '"', 'QUOTATION MARK'),
    (5, '#', 'NUMBER SIGN'),
    (6, '$', 'DOLLAR SIGN'),
    (8, '%', 'PERCENT SIGN'),
    (9, '(', 'LEFT PARENTHESIS'),
    (11, '&', 'AMPERSAND'),
    (12, "'", 'APOSTROPHE'),
    (15, '*', 'ASTERISK'),
    (17, '+', 'PLUS SIGN'),
    (18, '[', 'LEFT SQUARE BRACKET'),
    (20, ',', 'COMMA'),
    (21, '-', 'HYPHEN-MINUS'),
    (23, '.', 'FULL STOP'),
    (24, '/', 'SOLIDUS'),
    (27, '{', 'LEFT CURLY BRACKET'),
    (29, ':', 'COLON'),
    (30, ';', 'SEMICOLON'),
    (32, '=', 'EQUALS SIGN'),
    (33, '?', 'QUESTION MARK'),
    (35, '<', 'LESS-THAN SIGN'),
    (36, '@', 'COMMERCIAL AT'),
    (39, '\\', 'REVERSE SOLIDUS'),
    (41, '^', 'CIRCUMFLEX ACCENT'),
    (42, '_', 'LOW LINE'),
    (44, '‘', 'LEFT SINGLE QUOTATION MARK'),
    (45, '`', 'GRAVE ACCENT'),
    (47, '|', 'VERTICAL LINE'),
    (48, '~', 'TILDE'),
    (51, '…', 'HORIZONTAL ELLIPSIS'),
    (53, '“', 'LEFT DOUBLE QUOTATION MARK'),
    (54, '—', 'EM DASH'),
    (56, '–', 'EN DASH'),
    (57, '·', 'MIDDLE DOT'),
    (59, '°', 'DEGREE SIGN'),
    (60, '«', 'LEFT-POINTING DOUBLE ANGLE QUOTATION MARK'),
    (63, '±', 'PLUS-MINUS SIGN'),
    (65, '×', 'MULTIPLICATION SIGN'),
    (66, '÷', 'DIVISION SIGN'),
    (68, '√', 'SQUARE ROOT'),
    (69, '∂', 'PARTIAL DIFFERENTIAL'),
    (71, '∫', 'INTEGRAL'),
    (72, '∑', 'N-ARY SUMMATION'),
    (74, '∏', 'N-ARY PRODUCT'),
    (75, '∇', 'NABLA'),
    (77, '∞', 'INFINITY'),
    (78, '≈', 'ALMOST EQUAL TO'),
    (79, '≠', 'NOT EQUAL TO'),
    (81, '≤', 'LESS-THAN OR EQUAL TO'),
    (82, '≥', 'GREATER-THAN OR EQUAL TO'),
    (84, '→', 'RIGHTWARDS ARROW'),
    (85, '←', 'LEFTWARDS ARROW'),
    (87, ')', 'RIGHT PARENTHESIS'),
    (88, '↑', 'UPWARDS ARROW'),
    (90, '↓', 'DOWNWARDS ARROW'),
    (93, '↔', 'LEFT RIGHT ARROW'),
    (94, '⊕', 'CIRCLED PLUS'),
    (96, ']', 'RIGHT SQUARE BRACKET'),
    (97, '⊗', 'CIRCLED TIMES'),
    (99, '⊙', 'CIRCLED DOT OPERATOR'),
    (100, '⊘', 'CIRCLED DIVISION SLASH'),
    (102, '∈', 'ELEMENT OF'),
    (105, '}', 'RIGHT CURLY BRACKET'),
    (106, '∉', 'NOT AN ELEMENT OF'),
    (108, '⊂', 'SUBSET OF'),
    (109, '⊃', 'SUPERSET OF'),
    (111, '⊆', 'SUBSET OF OR EQUAL TO'),
    (112, '>', 'GREATER-THAN SIGN'),
    (114, '⊇', 'SUPERSET OF OR EQUAL TO'),
    (117, '∩', 'INTERSECTION'),
    (118, '∪', 'UNION'),
    (120, '∧', 'LOGICAL AND'),
    (121, '’', 'RIGHT SINGLE QUOTATION MARK'),
    (123, '∨', 'LOGICAL OR'),
    (124, '¬', 'NOT SIGN'),
    (126, '∀', 'FOR ALL'),
    (129, '∃', 'THERE EXISTS'),
    (130, '”', 'RIGHT DOUBLE QUOTATION MARK'),
    (132, '⊢', 'RIGHT TACK'),
    (133, '⊨', 'TRUE'),
    (135, '∴', 'THEREFORE'),
    (136, '∵', 'BECAUSE'),
    (138, '»', 'RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK'),
    (141, '≡', 'IDENTICAL TO'),
)

_TOKEN = re.compile(r"[a-z]+")
_ALIASES: Mapping[str, tuple[str, ...]] = {
    "nabla": ("gradient",),
    "superset of": ("set",),
    "because": ("reason", "cause"),
}


class PublicGonolFunctionError(ValueError):
    """Raised when indexed lexical function authority is incomplete or altered."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8") + b"\n"


def _identity(prefix: str, value: object) -> str:
    return prefix + sha256(_canonical_bytes(value)).hexdigest()


@dataclass(frozen=True, slots=True)
class FunctionDefinitionBinding:
    lexical_term: str
    lexical_entry_keys: tuple[str, ...]
    definition_gonol_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.lexical_term or not self.lexical_entry_keys or not self.definition_gonol_ids:
            raise PublicGonolFunctionError("function binding requires lexical definition evidence")
        if len(set(self.definition_gonol_ids)) != len(self.definition_gonol_ids):
            raise PublicGonolFunctionError("definition gonols cannot be duplicated")

    @property
    def binding_id(self) -> str:
        return _identity("ucns.public-function-binding:sha256:", {
            "lexical_term": self.lexical_term,
            "lexical_entry_keys": list(self.lexical_entry_keys),
            "definition_gonol_ids": list(self.definition_gonol_ids),
        })


@dataclass(frozen=True, slots=True)
class PublicGonolFunction:
    public_gonol_index: int
    glyph: str
    unicode_name: str
    bindings: tuple[FunctionDefinitionBinding, ...]
    public_gonol_sha256: str = PUBLIC_GONOL_SHA256
    independent_punctuation_grammar_attached: bool = False

    def __post_init__(self) -> None:
        if not (0 <= self.public_gonol_index < len(PUBLIC_GONOL_157)):
            raise PublicGonolFunctionError("function index outside Public Gonol")
        if PUBLIC_GONOL_157[self.public_gonol_index] != self.glyph:
            raise PublicGonolFunctionError("function glyph is not at canonical index")
        if not self.bindings:
            raise PublicGonolFunctionError("functional index lacks lexical definitions")
        if self.public_gonol_sha256 != PUBLIC_GONOL_SHA256:
            raise PublicGonolFunctionError("Public Gonol identity mismatch")
        if self.independent_punctuation_grammar_attached:
            raise PublicGonolFunctionError("independent punctuation grammar is forbidden")

    @property
    def function_id(self) -> str:
        return _identity("ucns.public-gonol-function:sha256:", {
            "public_gonol_index": self.public_gonol_index, "glyph": self.glyph,
            "unicode_name": self.unicode_name,
            "binding_ids": [item.binding_id for item in self.bindings],
            "public_gonol_sha256": self.public_gonol_sha256,
            "independent_punctuation_grammar_attached": self.independent_punctuation_grammar_attached,
        })


@dataclass(frozen=True, slots=True)
class PublicGonolFunctionTable:
    source_receipt_id: str
    definition_layer_id: str
    functions: tuple[PublicGonolFunction, ...]
    public_gonol_sha256: str = PUBLIC_GONOL_SHA256
    canonical_key: str = "public-gonol-index"
    standing: str = FUNCTION_TABLE_STANDING

    def __post_init__(self) -> None:
        expected = tuple(index for index, _, _ in FUNCTIONAL_INDEX_NAMES)
        actual = tuple(item.public_gonol_index for item in self.functions)
        if actual != expected or len(set(actual)) != len(actual):
            raise PublicGonolFunctionError("function table must cover canonical functional indices exactly")
        if self.public_gonol_sha256 != PUBLIC_GONOL_SHA256 or self.canonical_key != "public-gonol-index":
            raise PublicGonolFunctionError("function table invented a secondary index")
        if self.standing != FUNCTION_TABLE_STANDING:
            raise PublicGonolFunctionError("function table standing cannot be promoted")

    @property
    def table_id(self) -> str:
        return _identity("ucns.public-gonol-function-table:sha256:", {
            "source_receipt_id": self.source_receipt_id,
            "definition_layer_id": self.definition_layer_id,
            "function_ids": [item.function_id for item in self.functions],
            "public_gonol_sha256": self.public_gonol_sha256,
            "canonical_key": self.canonical_key, "standing": self.standing,
        })

    @property
    def by_index(self) -> Mapping[int, PublicGonolFunction]:
        return {item.public_gonol_index: item for item in self.functions}


@dataclass(frozen=True, slots=True)
class AtomicFunctionState:
    atomic_gonol_id: str
    application_depth: int = 0

    def __post_init__(self) -> None:
        if not self.atomic_gonol_id or self.application_depth < 0:
            raise PublicGonolFunctionError("current function state must be an atomic gonol")


@dataclass(frozen=True, slots=True)
class ContextualFunctionApplication:
    prior_atomic_gonol_id: str
    prior_application_depth: int
    public_gonol_index: int
    function_id: str
    definition_gonol_ids: tuple[str, ...]
    ordered_context_gonol_ids: tuple[str, ...]
    carrier: RelationalCarrier
    atomic_at_next_application: bool = True
    standing: str = APPLICATION_STANDING

    def __post_init__(self) -> None:
        node_count = 1 + len(self.definition_gonol_ids) + len(self.ordered_context_gonol_ids)
        edges = [
            (0, FUNCTION_RELATION_CODE, index + 1)
            for index in range(len(self.definition_gonol_ids))
        ]
        offset = 1 + len(self.definition_gonol_ids)
        edges.extend((0, CONTEXT_RELATION_CODE, offset + index)
                     for index in range(len(self.ordered_context_gonol_ids)))
        if self.carrier != build_relational_carrier(node_count, edges):
            raise PublicGonolFunctionError("function and context must enter application closure")
        if not self.atomic_at_next_application or self.standing != APPLICATION_STANDING:
            raise PublicGonolFunctionError("contextual application must close atomically")

    @property
    def result_atomic_gonol_id(self) -> str:
        return _identity("ucns.contextual-function-application:sha256:", {
            "prior_atomic_gonol_id": self.prior_atomic_gonol_id,
            "prior_application_depth": self.prior_application_depth,
            "public_gonol_index": self.public_gonol_index,
            "function_id": self.function_id,
            "definition_gonol_ids": list(self.definition_gonol_ids),
            "ordered_context_gonol_ids": list(self.ordered_context_gonol_ids),
            "carrier_id": self.carrier.stable_identity,
            "atomic_at_next_application": self.atomic_at_next_application,
            "standing": self.standing,
        })

    @property
    def next_state(self) -> AtomicFunctionState:
        return AtomicFunctionState(self.result_atomic_gonol_id, self.prior_application_depth + 1)


def _source_terms(unicode_name: str, available: frozenset[str]) -> tuple[str, ...]:
    words = tuple(_TOKEN.findall(unicode_name.lower()))
    selected: list[str] = []
    cursor = 0
    while cursor < len(words):
        match = None
        for end in range(len(words), cursor, -1):
            phrase = " ".join(words[cursor:end])
            if phrase in available or phrase.replace(" ", "_") in available:
                match = (phrase, end)
                break
        if match is None:
            cursor += 1
        else:
            selected.append(match[0])
            cursor = match[1]
    if not selected:
        selected.extend(_ALIASES.get(unicode_name.lower(), ()))
    return tuple(selected)


def build_public_gonol_function_table(
    snapshot: OEWNCoreSnapshot,
    definition_layer: OEWNDefinitionLayer,
) -> PublicGonolFunctionTable:
    """Bind every frozen functional Public Gonol index to OEWN definitions."""

    if definition_layer.source_receipt_id != snapshot.source_receipt_id:
        raise PublicGonolFunctionError("definition layer and OEWN snapshot differ")
    definitions_by_key: dict[str, list[str]] = {}
    for item in definition_layer.definition_gonols:
        definitions_by_key.setdefault(item.entry_key, []).append(item.gonol_id)
    entries_by_lemma: dict[str, list[str]] = {}
    for entry in snapshot.lexical_entries:
        if not entry.senses:
            continue
        normalized_lemma = re.sub(r"[-_]+", " ", entry.lemma.lower())
        entries_by_lemma.setdefault(normalized_lemma, []).append(
            oewn_entry_key(entry.lemma, entry.part_of_speech)
        )
    available = frozenset(entries_by_lemma)
    functions: list[PublicGonolFunction] = []
    for index, glyph, unicode_name in FUNCTIONAL_INDEX_NAMES:
        bindings: list[FunctionDefinitionBinding] = []
        for term in _source_terms(unicode_name, available):
            keys = tuple(entries_by_lemma.get(term, ()))
            ids = tuple(identifier for key in keys for identifier in definitions_by_key.get(key, ()))
            if ids:
                bindings.append(FunctionDefinitionBinding(term, keys, ids))
        if not bindings:
            raise PublicGonolFunctionError(
                f"Public Gonol index {index} {glyph!r} has no OEWN definition binding"
            )
        functions.append(PublicGonolFunction(index, glyph, unicode_name, tuple(bindings)))
    return PublicGonolFunctionTable(
        snapshot.source_receipt_id, definition_layer.layer_id, tuple(functions),
    )


def apply_public_gonol_function(
    table: PublicGonolFunctionTable,
    public_gonol_index: int,
    current_state: AtomicFunctionState,
    ordered_context_gonol_ids: tuple[str, ...] = (),
) -> ContextualFunctionApplication:
    """Couple definition-derived functions to caller-supplied atomic context."""

    function = table.by_index.get(public_gonol_index)
    if function is None:
        raise PublicGonolFunctionError("index is not a bound functional non-letter")
    if any(not item for item in ordered_context_gonol_ids):
        raise PublicGonolFunctionError("context identities must be nonempty")
    definition_ids = tuple(
        identifier for binding in function.bindings
        for identifier in binding.definition_gonol_ids
    )
    node_count = 1 + len(definition_ids) + len(ordered_context_gonol_ids)
    edges = [(0, FUNCTION_RELATION_CODE, i + 1) for i in range(len(definition_ids))]
    offset = 1 + len(definition_ids)
    edges.extend((0, CONTEXT_RELATION_CODE, offset + i)
                 for i in range(len(ordered_context_gonol_ids)))
    return ContextualFunctionApplication(
        current_state.atomic_gonol_id, current_state.application_depth,
        public_gonol_index, function.function_id, definition_ids,
        ordered_context_gonol_ids, build_relational_carrier(node_count, edges),
    )


def function_table_bytes(table: PublicGonolFunctionTable) -> bytes:
    """Return a compact canonical table receipt."""

    return _canonical_bytes({
        "table_id": table.table_id,
        "source_receipt_id": table.source_receipt_id,
        "definition_layer_id": table.definition_layer_id,
        "public_gonol_sha256": table.public_gonol_sha256,
        "canonical_key": table.canonical_key,
        "function_count": len(table.functions),
        "functional_indices": [item.public_gonol_index for item in table.functions],
        "function_ids_sha256": sha256(_canonical_bytes(
            [item.function_id for item in table.functions]
        )).hexdigest(),
        "function_name_source": FUNCTION_NAME_SOURCE,
        "standing": table.standing,
    })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_repo")
    parser.add_argument("output")
    args = parser.parse_args()
    source_receipt = verify_oewn_2025_core(args.source_repo)
    snapshot = load_oewn_core(args.source_repo, source_receipt)
    definition_layer = build_oewn_definition_layer(snapshot)
    table = build_public_gonol_function_table(snapshot, definition_layer)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(function_table_bytes(table))
    return 0


__all__ = [
    "APPLICATION_STANDING", "AtomicFunctionState", "CONTEXT_RELATION_CODE",
    "ContextualFunctionApplication", "FUNCTIONAL_INDEX_NAMES", "FUNCTION_RELATION_CODE",
    "FunctionDefinitionBinding", "PublicGonolFunction", "PublicGonolFunctionError",
    "PublicGonolFunctionTable", "apply_public_gonol_function",
    "build_public_gonol_function_table", "function_table_bytes",
]


if __name__ == "__main__":  # pragma: no cover - full corpus receipt command
    sys.exit(main())
