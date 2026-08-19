# === MODULE_BUILD ===
# id: ucns_xkcd_lexical_floor
#   module_name: lexical_xkcd_floor
#   module_kind: engine
#   summary: reconstructs the xkcd Simple Writer 0.2.1 floor so Public Gonol punctuation/symbol functions participate intrinsically with exact source order, occurrence, and multiplicity
#   owner: Erin Spencer
#   public_surface: XkcdLexicalFloor, XkcdLexicalFloorError, FloorOccurrence, ClosedSurfaceGonol, FunctionApplicationPlan, XKCD_LEXICAL_FLOOR_ID, XKCD_LEXICAL_FLOOR_VERSION, XKCD_LEXICAL_FLOOR_STANDING, official_xkcd_source_payload, reconstruct_xkcd_lexical_floor, load_xkcd_lexical_floor, replay_xkcd_lexical_floor
#   internal_surface: _canonical_bytes, _identity, _segment, _function_meta, _letter_run_id, _function_participant_id, _close, _execute_plans
#   auth_boundary: none
#   storage_boundary: read packaged xkcd bytes through the existing source adapter; optional caller-supplied Public Gonol function table
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_lexical_xkcd_floor
#   rollout: punctuation-aware reconstruction candidate on PR 213; not selected canon and not a closed definition corpus
#   rollback: remove this reconstruction and public exports while retaining lexical_sources, public_gonol_functions, and deprecated NGSL artifacts
#   requires: ucns_current_lexical_sources, ucns_public_gonol_function_table, ucns_relational_carrier
#   since: 2026-08-19
#   unresolved: authoritative 3634-to-1000 family mapping, artifact-specific license applicability, whether this floor later constrains any definition corpus, geometry of function application
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: xkcd_floor_reconstructs_official_source_payload
#   given: the xkcd floor is reconstructed
#   then: the official quoted Simple Writer payload is restored as ordered word letter-runs plus every source VERTICAL LINE with exact multiplicity
#   class: evidence
#   since: 2026-08-19
#
# id: xkcd_floor_functions_are_public_gonol_participants
#   given: a source glyph occupies a Public Gonol punctuation or symbol index
#   then: that occurrence is a function participant keyed by the canonical Public Gonol index, not a letter-run character
#   class: doctrine
#   since: 2026-08-19
#
# id: xkcd_floor_preserves_order_occurrence_and_multiplicity
#   given: the reconstructed floor and official payload are compared
#   then: occurrence order, spans, exact text, and repeated function/letter-run identities reconstruct the payload without normalization
#   class: correctness
#   since: 2026-08-19
#
# id: xkcd_floor_closes_relations_without_invented_grammar
#   given: a surface or the full source stream is closed
#   then: ordered participants enter one intrinsic relational carrier and no independent punctuation grammar is attached
#   class: safety
#   since: 2026-08-19
#
# id: xkcd_floor_does_not_invent_family_mapping
#   given: the floor is inspected
#   then: the declared family count remains 1000, family_mapping_available remains false, and no family lookup is supplied
#   class: safety
#   since: 2026-08-19
#
# id: xkcd_floor_does_not_close_definitions
#   given: the floor is inspected
#   then: closed_definition_support remains false and the module supplies no closed-definition constructor
#   class: doctrine
#   since: 2026-08-19
#
# id: xkcd_floor_receipt_replays
#   given: a reconstructed floor is replayed from packaged source
#   then: receipt identity, source identity, stream identity, table identity, application evidence, and floor equality agree or replay fails closed
#   class: evidence
#   since: 2026-08-19
#
# id: xkcd_floor_source_is_validated_before_receipt
#   given: a floor receipt is minted
#   then: the receipt is refused unless the source matches packaged official bytes and the official quoted payload
#   class: evidence
#   since: 2026-08-19
#
# id: xkcd_floor_applications_require_explicit_context
#   given: a function application is requested
#   then: current state and occurrence-addressed context are caller-supplied; neighboring stream participants are not inferred
#   class: safety
#   since: 2026-08-19
#
# id: xkcd_floor_receipt_binds_application_identities
#   given: explicit function applications are included
#   then: the floor receipt binds each application's ordered identity, result, function, and occurrence addresses
#   class: evidence
#   since: 2026-08-19
# === END CONTRACTS ===

"""Punctuation-aware xkcd floor reconstruction.

Usage::

    from ucns import (
        FunctionApplicationPlan,
        load_xkcd_lexical_floor,
        reconstruct_xkcd_lexical_floor,
        replay_xkcd_lexical_floor,
    )

    floor = load_xkcd_lexical_floor()
    assert floor.contains("don't")
    surface = floor.closed_surface("don't")
    assert any(item.kind == "public-gonol-function" for item in surface.occurrences)
    replay_xkcd_lexical_floor(floor)

    # Function application context is caller-supplied, never inferred:
    # reconstruct_xkcd_lexical_floor(source, table, (FunctionApplicationPlan(...),))

The official Simple Writer payload is the quoted ``word|word|...`` string.
Letter-runs stay lexical. Public Gonol punctuation and symbol glyphs, including
intra-word apostrophes and every source VERTICAL LINE, are function
participants. Relations enter a closed carrier. This is a reconstruction
candidate, not selected canon and not a closed definition set.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
import json
from typing import Mapping

from .edcm import PUBLIC_GONOL_SHA256
from .lexical_sources import (
    XKCD_DECLARED_FAMILY_COUNT,
    XKCD_STANDING,
    XKCD_SURFACE_COUNT,
    XKCD_VERSION,
    LexicalSourceError,
    XKCDSimpleWriterReceipt,
    load_xkcd_simplewriter,
    quoted_xkcd_payload,
)
from .public_gonol_functions import (
    FUNCTIONAL_INDEX_NAMES,
    AtomicFunctionState,
    ContextualFunctionApplication,
    PublicGonolFunctionTable,
    apply_public_gonol_function,
)
from .relational_carrier import RelationalCarrier, build_relational_carrier

XKCD_LEXICAL_FLOOR_ID = "ucns.lexical-floor.xkcd-simplewriter-0.2.1"
XKCD_LEXICAL_FLOOR_VERSION = "1.2.0"
XKCD_LEXICAL_FLOOR_STANDING = "punctuation-aware-xkcd-floor-reconstruction-candidate"
XKCD_FLOOR_RECEIPT_PREFIX = "ucns.xkcd-lexical-floor-receipt:sha256:"
LETTER_RUN_KIND = "letter-run"
FUNCTION_KIND = "public-gonol-function"
LETTER_RUN_STANDING = "xkcd-letter-run-gonol-candidate"
FUNCTION_PARTICIPANT_STANDING = "public-gonol-function-participant-in-xkcd-floor"
CLOSED_SURFACE_STANDING = "punctuation-aware-xkcd-surface-closure-candidate"
FLOOR_OCCURRENCE_RELATION_CODE = 6
VERTICAL_LINE_INDEX = 47
_FUNCTION_BY_GLYPH: Mapping[str, tuple[int, str]] = {
    glyph: (index, name) for index, glyph, name in FUNCTIONAL_INDEX_NAMES
}


class XkcdLexicalFloorError(ValueError):
    """Raised when punctuation-aware xkcd reconstruction loses source identity."""


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


def official_xkcd_source_payload(source: XKCDSimpleWriterReceipt) -> str:
    """Return the official quoted payload after packaged-byte validation."""

    try:
        return quoted_xkcd_payload(source)
    except (LexicalSourceError, TypeError) as exc:
        raise XkcdLexicalFloorError("xkcd source is not valid for floor receipt minting") from exc


def _function_meta(glyph: str) -> tuple[int, str]:
    try:
        return _FUNCTION_BY_GLYPH[glyph]
    except KeyError as exc:
        raise XkcdLexicalFloorError(
            "glyph is not a Public Gonol punctuation or symbol function"
        ) from exc


def _segment(text: str) -> tuple[tuple[int, int, str], ...]:
    if not text:
        raise XkcdLexicalFloorError("source text must be nonempty")
    spans: list[tuple[int, int, str]] = []
    cursor = 0
    while cursor < len(text):
        glyph = text[cursor]
        if glyph in _FUNCTION_BY_GLYPH:
            spans.append((cursor, cursor + 1, FUNCTION_KIND))
            cursor += 1
            continue
        if "a" <= glyph <= "z":
            end = cursor + 1
            while end < len(text) and "a" <= text[end] <= "z":
                end += 1
            spans.append((cursor, end, LETTER_RUN_KIND))
            cursor = end
            continue
        raise XkcdLexicalFloorError("source contains a glyph that is neither a letter-run nor a Public Gonol function")
    return tuple(spans)


def _letter_run_id(text: str, source_receipt_id: str) -> str:
    if not text or any(not ("a" <= glyph <= "z") for glyph in text):
        raise XkcdLexicalFloorError("letter-run must be a nonempty ASCII letter sequence")
    return _identity("ucns.xkcd-letter-run-gonol:sha256:", {
        "text": text,
        "source_receipt_id": source_receipt_id,
        "glyphs": list(text),
        "standing": LETTER_RUN_STANDING,
    })


def _function_participant_id(
    index: int,
    glyph: str,
    unicode_name: str,
    table_function_id: str | None,
) -> str:
    expected_index, expected_name = _function_meta(glyph)
    if index != expected_index or unicode_name != expected_name:
        raise XkcdLexicalFloorError("function participant is not the canonical Public Gonol function")
    return _identity("ucns.xkcd-function-participant:sha256:", {
        "public_gonol_index": index,
        "glyph": glyph,
        "unicode_name": unicode_name,
        "public_gonol_sha256": PUBLIC_GONOL_SHA256,
        "table_function_id": table_function_id,
        "standing": FUNCTION_PARTICIPANT_STANDING,
    })


def _close(participant_ids: tuple[str, ...]) -> RelationalCarrier:
    if not participant_ids:
        raise XkcdLexicalFloorError("closure requires at least one participant")
    return build_relational_carrier(
        1 + len(participant_ids),
        ((0, FLOOR_OCCURRENCE_RELATION_CODE, offset)
         for offset in range(1, len(participant_ids) + 1)),
    )


@dataclass(frozen=True, slots=True)
class FloorOccurrence:
    """One exact source span: a letter-run or a Public Gonol function."""

    ordinal: int
    start: int
    end: int
    kind: str
    exact_text: str
    participant_id: str
    public_gonol_index: int | None = None
    function_id: str | None = None

    def __post_init__(self) -> None:
        if self.ordinal < 0 or not (0 <= self.start < self.end):
            raise XkcdLexicalFloorError("occurrence addresses must be ordered and nonempty")
        if self.kind == LETTER_RUN_KIND:
            if self.public_gonol_index is not None or self.function_id is not None:
                raise XkcdLexicalFloorError("letter-run cannot carry a function identity")
            if any(not ("a" <= glyph <= "z") for glyph in self.exact_text):
                raise XkcdLexicalFloorError("letter-run text must be ASCII letters only")
            return
        if self.kind != FUNCTION_KIND:
            raise XkcdLexicalFloorError("occurrence kind must be letter-run or public-gonol-function")
        if len(self.exact_text) != 1 or self.public_gonol_index is None:
            raise XkcdLexicalFloorError("function occurrence requires one canonical Public Gonol glyph")
        index, _name = _function_meta(self.exact_text)
        if index != self.public_gonol_index:
            raise XkcdLexicalFloorError("function occurrence index is not the Public Gonol function")


@dataclass(frozen=True, slots=True)
class ClosedSurfaceGonol:
    """One xkcd surface closed after letter-runs and intra-surface functions enter it."""

    surface: str
    occurrences: tuple[FloorOccurrence, ...]
    carrier: RelationalCarrier
    atomic_at_next_scale: bool = True
    independent_punctuation_grammar_attached: bool = False
    standing: str = CLOSED_SURFACE_STANDING

    def __post_init__(self) -> None:
        if tuple(item.ordinal for item in self.occurrences) != tuple(range(len(self.occurrences))):
            raise XkcdLexicalFloorError("surface occurrences must be dense and ordered")
        reconstructed = "".join(item.exact_text for item in self.occurrences)
        if reconstructed != self.surface:
            raise XkcdLexicalFloorError("surface occurrences do not reconstruct the exact surface")
        participant_ids = tuple(item.participant_id for item in self.occurrences)
        if self.carrier != _close(participant_ids):
            raise XkcdLexicalFloorError("surface relations must enter the closure carrier")
        if not self.atomic_at_next_scale or self.independent_punctuation_grammar_attached:
            raise XkcdLexicalFloorError("surface closure cannot attach an independent grammar")
        if self.standing != CLOSED_SURFACE_STANDING:
            raise XkcdLexicalFloorError("surface standing cannot be promoted")

    @property
    def gonol_id(self) -> str:
        return _identity("ucns.xkcd-closed-surface-gonol:sha256:", {
            "surface": self.surface,
            "occurrence_ids": [item.participant_id for item in self.occurrences],
            "kinds": [item.kind for item in self.occurrences],
            "carrier_id": self.carrier.stable_identity,
            "atomic_at_next_scale": self.atomic_at_next_scale,
            "independent_punctuation_grammar_attached": self.independent_punctuation_grammar_attached,
            "standing": self.standing,
        })


def _table_function_id(
    table: PublicGonolFunctionTable | None,
    index: int,
) -> str | None:
    if table is None:
        return None
    try:
        return table.by_index[index].function_id
    except KeyError as exc:
        raise XkcdLexicalFloorError("function table lacks a required Public Gonol index") from exc


def _occurrences_for(
    text: str,
    source_receipt_id: str,
    table: PublicGonolFunctionTable | None,
) -> tuple[FloorOccurrence, ...]:
    built: list[FloorOccurrence] = []
    for ordinal, (start, end, kind) in enumerate(_segment(text)):
        exact = text[start:end]
        if kind == LETTER_RUN_KIND:
            built.append(FloorOccurrence(
                ordinal, start, end, kind, exact,
                _letter_run_id(exact, source_receipt_id),
            ))
            continue
        index, name = _function_meta(exact)
        function_id = _table_function_id(table, index)
        built.append(FloorOccurrence(
            ordinal, start, end, kind, exact,
            _function_participant_id(index, exact, name, function_id),
            index, function_id,
        ))
    return tuple(built)


@dataclass(frozen=True, slots=True)
class FunctionApplicationPlan:
    """Caller-supplied, occurrence-addressed function application."""

    stream_ordinal: int
    current_state: AtomicFunctionState
    context_ordinals: tuple[int, ...] = ()

    def __post_init__(self) -> None:
        if self.stream_ordinal < 0:
            raise XkcdLexicalFloorError("application stream ordinal must be nonnegative")
        if any(ordinal < 0 for ordinal in self.context_ordinals):
            raise XkcdLexicalFloorError("application context ordinals must be nonnegative")


def _execute_plans(
    table: PublicGonolFunctionTable | None,
    stream: tuple[FloorOccurrence, ...],
    plans: tuple[FunctionApplicationPlan, ...],
) -> tuple[ContextualFunctionApplication, ...]:
    if not plans:
        return ()
    if table is None:
        raise XkcdLexicalFloorError("function application plans require an explicit function table")
    applications = []
    for plan in plans:
        if plan.stream_ordinal >= len(stream):
            raise XkcdLexicalFloorError("application stream ordinal is outside the source stream")
        occurrence = stream[plan.stream_ordinal]
        if occurrence.kind != FUNCTION_KIND or occurrence.public_gonol_index is None:
            raise XkcdLexicalFloorError("application target is not a function occurrence")
        context_ids = []
        for ordinal in plan.context_ordinals:
            if ordinal >= len(stream):
                raise XkcdLexicalFloorError("application context ordinal is outside the source stream")
            context_ids.append(stream[ordinal].participant_id)
        applications.append(apply_public_gonol_function(
            table,
            occurrence.public_gonol_index,
            plan.current_state,
            tuple(context_ids),
        ))
    return tuple(applications)


@dataclass(frozen=True, slots=True)
class XkcdLexicalFloor:
    """Punctuation-aware reconstruction of the xkcd source stream."""

    source: XKCDSimpleWriterReceipt
    payload: str
    surfaces: tuple[ClosedSurfaceGonol, ...]
    stream: tuple[FloorOccurrence, ...]
    carrier: RelationalCarrier
    table_id: str | None
    application_plans: tuple[FunctionApplicationPlan, ...]
    function_applications: tuple[ContextualFunctionApplication, ...]
    floor_id: str = XKCD_LEXICAL_FLOOR_ID
    version: str = XKCD_LEXICAL_FLOOR_VERSION
    standing: str = XKCD_LEXICAL_FLOOR_STANDING
    closed_definition_support: bool = False
    family_mapping_available: bool = False
    all_pairs_graph_materialized: bool = False
    independent_punctuation_grammar_attached: bool = False
    punctuation_functions_intrinsic: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.source, XKCDSimpleWriterReceipt):
            raise XkcdLexicalFloorError("floor source must be the xkcd Simple Writer receipt")
        if self.source.version != XKCD_VERSION or self.source.standing != XKCD_STANDING:
            raise XkcdLexicalFloorError("xkcd source identity mismatch")
        if len(self.source.surface_forms) != XKCD_SURFACE_COUNT:
            raise XkcdLexicalFloorError("xkcd surface inventory mismatch")
        if self.source.family_count != XKCD_DECLARED_FAMILY_COUNT:
            raise XkcdLexicalFloorError("xkcd declared family count mismatch")
        if self.source.family_mapping_available or self.family_mapping_available:
            raise XkcdLexicalFloorError("xkcd family mapping cannot be invented")
        if self.payload != official_xkcd_source_payload(self.source):
            raise XkcdLexicalFloorError("floor payload is not the official source string")
        if tuple(item.surface for item in self.surfaces) != self.source.surface_forms:
            raise XkcdLexicalFloorError("closed surfaces are not in source order")
        reconstructed = "".join(item.exact_text for item in self.stream)
        if reconstructed != self.payload:
            raise XkcdLexicalFloorError("stream occurrences do not reconstruct the official payload")
        if tuple(item.ordinal for item in self.stream) != tuple(range(len(self.stream))):
            raise XkcdLexicalFloorError("stream occurrences must be dense and ordered")
        pipe_count = sum(
            1 for item in self.stream
            if item.kind == FUNCTION_KIND and item.public_gonol_index == VERTICAL_LINE_INDEX
        )
        if pipe_count != XKCD_SURFACE_COUNT - 1:
            raise XkcdLexicalFloorError("source VERTICAL LINE multiplicity is not preserved")
        for item in self.stream:
            if self.payload[item.start:item.end] != item.exact_text:
                raise XkcdLexicalFloorError("stream occurrence does not match official payload span")
            if item.kind == FUNCTION_KIND:
                index, _name = _function_meta(item.exact_text)
                if item.public_gonol_index != index:
                    raise XkcdLexicalFloorError("function occurrence does not match the source glyph")
        if len(self.application_plans) != len(self.function_applications):
            raise XkcdLexicalFloorError("function application evidence is incomplete")
        for plan, application in zip(self.application_plans, self.function_applications):
            if plan.stream_ordinal >= len(self.stream):
                raise XkcdLexicalFloorError("application stream ordinal is outside the source stream")
            occurrence = self.stream[plan.stream_ordinal]
            if occurrence.kind != FUNCTION_KIND or occurrence.public_gonol_index is None:
                raise XkcdLexicalFloorError("application target is not a function occurrence")
            if not isinstance(application, ContextualFunctionApplication):
                raise XkcdLexicalFloorError("function application evidence is incomplete")
            context_ids = []
            for ordinal in plan.context_ordinals:
                if ordinal >= len(self.stream):
                    raise XkcdLexicalFloorError("application context ordinal is outside the source stream")
                context_ids.append(self.stream[ordinal].participant_id)
            if (
                application.public_gonol_index != occurrence.public_gonol_index
                or application.prior_atomic_gonol_id != plan.current_state.atomic_gonol_id
                or application.prior_application_depth != plan.current_state.application_depth
                or application.ordered_context_gonol_ids != tuple(context_ids)
            ):
                raise XkcdLexicalFloorError("function application evidence is incomplete")
        if self.carrier != _close(tuple(item.participant_id for item in self.stream)):
            raise XkcdLexicalFloorError("floor relations must enter the closure carrier")
        if (
            self.closed_definition_support
            or self.all_pairs_graph_materialized
            or self.independent_punctuation_grammar_attached
            or not self.punctuation_functions_intrinsic
        ):
            raise XkcdLexicalFloorError("floor nonclaims cannot be inverted")
        if self.floor_id != XKCD_LEXICAL_FLOOR_ID or self.version != XKCD_LEXICAL_FLOOR_VERSION:
            raise XkcdLexicalFloorError("floor identity cannot be retargeted")
        if self.standing != XKCD_LEXICAL_FLOOR_STANDING:
            raise XkcdLexicalFloorError("floor standing cannot be promoted")

    def contains(self, surface: str) -> bool:
        if not isinstance(surface, str) or not surface:
            raise XkcdLexicalFloorError("floor membership requires a nonempty exact surface")
        return any(item.surface == surface for item in self.surfaces)

    def closed_surface(self, surface: str) -> ClosedSurfaceGonol:
        for item in self.surfaces:
            if item.surface == surface:
                return item
        raise XkcdLexicalFloorError("surface is not an exact xkcd floor admission")

    def word_gonol(self, surface: str) -> ClosedSurfaceGonol:
        """Return the closed surface gonol. Kept as a compatibility alias."""

        return self.closed_surface(surface)

    def function_occurrences(self) -> tuple[FloorOccurrence, ...]:
        return tuple(item for item in self.stream if item.kind == FUNCTION_KIND)

    def as_payload(self) -> dict[str, object]:
        return {
            "floor_id": self.floor_id,
            "version": self.version,
            "standing": self.standing,
            "source_receipt_id": self.source.receipt_id,
            "official_payload_sha256": sha256(self.payload.encode("utf-8")).hexdigest(),
            "surface_ids": [item.gonol_id for item in self.surfaces],
            "stream_participant_ids": [item.participant_id for item in self.stream],
            "stream_kinds": [item.kind for item in self.stream],
            "carrier_id": self.carrier.stable_identity,
            "table_id": self.table_id,
            "function_application_plans": [
                {
                    "stream_ordinal": plan.stream_ordinal,
                    "current_atomic_gonol_id": plan.current_state.atomic_gonol_id,
                    "current_application_depth": plan.current_state.application_depth,
                    "context_ordinals": list(plan.context_ordinals),
                }
                for plan in self.application_plans
            ],
            "function_applications": [
                {
                    "stream_ordinal": plan.stream_ordinal,
                    "function_id": getattr(application, "function_id", None),
                    "result_atomic_gonol_id": getattr(application, "result_atomic_gonol_id", None),
                    "context_ordinals": list(plan.context_ordinals),
                    "current_atomic_gonol_id": plan.current_state.atomic_gonol_id,
                }
                for plan, application in zip(self.application_plans, self.function_applications)
            ],
            "surface_count": len(self.surfaces),
            "declared_family_count": self.source.family_count,
            "family_mapping_available": self.family_mapping_available,
            "closed_definition_support": self.closed_definition_support,
            "punctuation_functions_intrinsic": self.punctuation_functions_intrinsic,
            "independent_punctuation_grammar_attached": self.independent_punctuation_grammar_attached,
            "all_pairs_graph_materialized": self.all_pairs_graph_materialized,
        }

    @property
    def receipt_id(self) -> str:
        return _identity(XKCD_FLOOR_RECEIPT_PREFIX, self.as_payload())


def reconstruct_xkcd_lexical_floor(
    source: XKCDSimpleWriterReceipt,
    table: PublicGonolFunctionTable | None = None,
    application_plans: tuple[FunctionApplicationPlan, ...] = (),
) -> XkcdLexicalFloor:
    """Reconstruct the official payload with intrinsic Public Gonol functions."""

    if not isinstance(source, XKCDSimpleWriterReceipt):
        raise TypeError("source must be an XKCDSimpleWriterReceipt")
    payload = official_xkcd_source_payload(source)
    receipt_id = source.receipt_id
    surfaces = []
    for surface in source.surface_forms:
        surface_occurrences = _occurrences_for(surface, receipt_id, table)
        surfaces.append(ClosedSurfaceGonol(
            surface,
            surface_occurrences,
            _close(tuple(item.participant_id for item in surface_occurrences)),
        ))
    surfaces = tuple(surfaces)
    stream = _occurrences_for(payload, receipt_id, table)
    applications = _execute_plans(table, stream, application_plans)
    return XkcdLexicalFloor(
        source, payload, surfaces, stream,
        _close(tuple(item.participant_id for item in stream)),
        None if table is None else table.table_id,
        application_plans,
        applications,
    )


@lru_cache(maxsize=1)
def load_xkcd_lexical_floor() -> XkcdLexicalFloor:
    """Load the punctuation-aware reconstruction from packaged xkcd bytes."""

    return reconstruct_xkcd_lexical_floor(load_xkcd_simplewriter())


def replay_xkcd_lexical_floor(
    floor: XkcdLexicalFloor,
    table: PublicGonolFunctionTable | None = None,
    application_plans: tuple[FunctionApplicationPlan, ...] | None = None,
) -> XkcdLexicalFloor:
    """Independently rebuild the floor from the same source, table, and plans."""

    plans = floor.application_plans if application_plans is None else application_plans
    if floor.table_id is None:
        if table is not None:
            raise XkcdLexicalFloorError("replay table does not match the floor's absent table")
    elif table is None or table.table_id != floor.table_id:
        raise XkcdLexicalFloorError("replay requires the same function table")
    rebuilt = reconstruct_xkcd_lexical_floor(load_xkcd_simplewriter(), table, plans)
    if (
        rebuilt != floor
        or rebuilt.receipt_id != floor.receipt_id
        or rebuilt.source.receipt_id != floor.source.receipt_id
        or rebuilt.carrier.stable_identity != floor.carrier.stable_identity
        or rebuilt.table_id != floor.table_id
    ):
        raise XkcdLexicalFloorError("xkcd lexical floor replay mismatch")
    return rebuilt


__all__ = [
    "CLOSED_SURFACE_STANDING",
    "FLOOR_OCCURRENCE_RELATION_CODE",
    "FUNCTION_KIND",
    "LETTER_RUN_KIND",
    "XKCD_FLOOR_RECEIPT_PREFIX",
    "XKCD_LEXICAL_FLOOR_ID",
    "XKCD_LEXICAL_FLOOR_STANDING",
    "XKCD_LEXICAL_FLOOR_VERSION",
    "ClosedSurfaceGonol",
    "FloorOccurrence",
    "FunctionApplicationPlan",
    "XkcdLexicalFloor",
    "XkcdLexicalFloorError",
    "load_xkcd_lexical_floor",
    "official_xkcd_source_payload",
    "reconstruct_xkcd_lexical_floor",
    "replay_xkcd_lexical_floor",
]
