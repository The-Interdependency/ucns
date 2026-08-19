# === MODULE_BUILD ===
# id: ucns_xkcd_lexical_floor
#   module_name: lexical_xkcd_floor
#   module_kind: adapter
#   summary: binds the pinned xkcd Simple Writer 0.2.1 source to atomic history-bearing word gonols as the current UCNS lexical-floor candidate
#   owner: Erin Spencer
#   public_surface: XkcdLexicalFloor, XkcdLexicalFloorError, XKCD_LEXICAL_FLOOR_ID, XKCD_LEXICAL_FLOOR_VERSION, XKCD_LEXICAL_FLOOR_STANDING, load_xkcd_lexical_floor, replay_xkcd_lexical_floor
#   internal_surface: _canonical_bytes, _identity
#   auth_boundary: none
#   storage_boundary: read packaged xkcd bytes through the existing source adapter
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_lexical_xkcd_floor
#   rollout: current lexical-floor candidate after source and word-gonol constructors; does not replace OEWN definition recursion or historical NGSL evidence
#   rollback: remove this floor binder and public exports while retaining lexical_sources, lexical_word_gonols, and deprecated NGSL artifacts
#   requires: ucns_current_lexical_sources, ucns_current_lexical_word_gonols
#   since: 2026-08-18
#   unresolved: authoritative 3634-to-1000 family mapping, artifact-specific license applicability, whether this floor later constrains any definition corpus
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: xkcd_floor_binds_exact_source_and_atomic_corpus
#   given: the current xkcd lexical floor is loaded
#   then: it binds the exact Simple Writer 0.2.1 receipt to 3634 source-ordered atomic word gonols with matching receipt identities and no all-pairs graph
#   class: evidence
#   since: 2026-08-18
#
# id: xkcd_floor_membership_is_exact_surface_identity
#   given: a surface is asked of the floor
#   then: membership and lookup use the exact source spelling only; unknown, casefolded, or normalized surfaces fail closed
#   class: correctness
#   since: 2026-08-18
#
# id: xkcd_floor_does_not_invent_family_mapping
#   given: the floor is inspected
#   then: the declared family count remains 1000, family_mapping_available remains false, and no family lookup is supplied
#   class: safety
#   since: 2026-08-18
#
# id: xkcd_floor_does_not_close_definitions
#   given: the floor is inspected
#   then: closed_definition_support remains false and the module supplies no closed-definition constructor
#   class: doctrine
#   since: 2026-08-18
#
# id: xkcd_floor_receipt_replays
#   given: a loaded floor is replayed from packaged source
#   then: receipt identity, source identity, corpus identity, and floor equality agree or replay fails closed
#   class: evidence
#   since: 2026-08-18
# === END CONTRACTS ===

"""Current UCNS lexical-floor candidate from pinned xkcd Simple Writer 0.2.1.

Usage::

    from ucns import load_xkcd_lexical_floor

    floor = load_xkcd_lexical_floor()
    assert floor.contains("branch")
    word = floor.word_gonol("branch")
    replay_xkcd_lexical_floor(floor)

This floor admits exact source surfaces as atomic word gonols. It does not
invent the missing 1,000-family map, does not close OEWN or any other
definition corpus, and does not replace historical NGSL evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
import json

from .lexical_sources import (
    XKCD_DECLARED_FAMILY_COUNT,
    XKCD_STANDING,
    XKCD_SURFACE_COUNT,
    XKCD_VERSION,
    XKCDSimpleWriterReceipt,
    load_xkcd_simplewriter,
)
from .lexical_word_gonols import (
    CORPUS_STANDING,
    LexicalWordGonolCorpus,
    construct_xkcd_word_gonols,
)

XKCD_LEXICAL_FLOOR_ID = "ucns.lexical-floor.xkcd-simplewriter-0.2.1"
XKCD_LEXICAL_FLOOR_VERSION = "1.0.0"
XKCD_LEXICAL_FLOOR_STANDING = "source-pinned-lexical-floor-candidate"
XKCD_FLOOR_RECEIPT_PREFIX = "ucns.xkcd-lexical-floor-receipt:sha256:"


class XkcdLexicalFloorError(ValueError):
    """Raised when the xkcd lexical floor loses source identity or overclaims."""


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


@dataclass(frozen=True, slots=True)
class XkcdLexicalFloor:
    """Exact xkcd source plus its atomic word-gonol corpus."""

    source: XKCDSimpleWriterReceipt
    corpus: LexicalWordGonolCorpus
    floor_id: str = XKCD_LEXICAL_FLOOR_ID
    version: str = XKCD_LEXICAL_FLOOR_VERSION
    standing: str = XKCD_LEXICAL_FLOOR_STANDING
    closed_definition_support: bool = False
    family_mapping_available: bool = False
    all_pairs_graph_materialized: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.source, XKCDSimpleWriterReceipt):
            raise XkcdLexicalFloorError("floor source must be the xkcd Simple Writer receipt")
        if self.source.version != XKCD_VERSION or self.source.standing != XKCD_STANDING:
            raise XkcdLexicalFloorError("xkcd source identity mismatch")
        if len(self.source.surface_forms) != XKCD_SURFACE_COUNT:
            raise XkcdLexicalFloorError("xkcd surface inventory mismatch")
        if self.source.family_count != XKCD_DECLARED_FAMILY_COUNT:
            raise XkcdLexicalFloorError("xkcd declared family count mismatch")
        if self.source.family_mapping_available:
            raise XkcdLexicalFloorError("xkcd family mapping must remain unavailable")
        if self.corpus.source_receipt_id != self.source.receipt_id:
            raise XkcdLexicalFloorError("word-gonol corpus is not bound to this source receipt")
        if len(self.corpus.word_gonols) != XKCD_SURFACE_COUNT:
            raise XkcdLexicalFloorError("floor corpus does not cover every source surface")
        surfaces = tuple(item.surface for item in self.corpus.word_gonols)
        if surfaces != self.source.surface_forms:
            raise XkcdLexicalFloorError("floor corpus order is not source order")
        if self.corpus.standing != CORPUS_STANDING:
            raise XkcdLexicalFloorError("floor corpus standing cannot be promoted")
        if self.floor_id != XKCD_LEXICAL_FLOOR_ID or self.version != XKCD_LEXICAL_FLOOR_VERSION:
            raise XkcdLexicalFloorError("floor identity cannot be retargeted")
        if self.standing != XKCD_LEXICAL_FLOOR_STANDING:
            raise XkcdLexicalFloorError("floor standing cannot be promoted")
        if self.closed_definition_support:
            raise XkcdLexicalFloorError("xkcd floor does not close definition support")
        if self.family_mapping_available:
            raise XkcdLexicalFloorError("xkcd family mapping cannot be invented")
        if self.all_pairs_graph_materialized or self.corpus.all_pairs_graph_materialized:
            raise XkcdLexicalFloorError("authoritative all-pairs lexical graph is forbidden")

    def contains(self, surface: str) -> bool:
        """Return whether the exact source spelling is an admitted floor surface."""

        if not isinstance(surface, str) or not surface:
            raise XkcdLexicalFloorError("floor membership requires a nonempty exact surface")
        return surface in self.corpus.by_surface

    def word_gonol(self, surface: str):
        """Return the atomic word gonol for one exact admitted surface."""

        if not self.contains(surface):
            raise XkcdLexicalFloorError("surface is not an exact xkcd floor admission")
        return self.corpus.by_surface[surface]

    def as_payload(self) -> dict[str, object]:
        return {
            "floor_id": self.floor_id,
            "version": self.version,
            "standing": self.standing,
            "source_receipt_id": self.source.receipt_id,
            "corpus_id": self.corpus.corpus_id,
            "surface_count": len(self.source.surface_forms),
            "declared_family_count": self.source.family_count,
            "family_mapping_available": self.family_mapping_available,
            "closed_definition_support": self.closed_definition_support,
            "all_pairs_graph_materialized": self.all_pairs_graph_materialized,
        }

    @property
    def receipt_id(self) -> str:
        return _identity(XKCD_FLOOR_RECEIPT_PREFIX, self.as_payload())


@lru_cache(maxsize=1)
def load_xkcd_lexical_floor() -> XkcdLexicalFloor:
    """Load the current xkcd lexical-floor candidate from packaged source bytes."""

    source = load_xkcd_simplewriter()
    return XkcdLexicalFloor(source, construct_xkcd_word_gonols(source))


def replay_xkcd_lexical_floor(floor: XkcdLexicalFloor) -> XkcdLexicalFloor:
    """Independently rebuild the floor from packaged source and compare."""

    source = load_xkcd_simplewriter()
    rebuilt = XkcdLexicalFloor(source, construct_xkcd_word_gonols(source))
    if (
        rebuilt != floor
        or rebuilt.receipt_id != floor.receipt_id
        or rebuilt.source.receipt_id != floor.source.receipt_id
        or rebuilt.corpus.corpus_id != floor.corpus.corpus_id
    ):
        raise XkcdLexicalFloorError("xkcd lexical floor replay mismatch")
    return rebuilt


__all__ = [
    "XKCD_FLOOR_RECEIPT_PREFIX",
    "XKCD_LEXICAL_FLOOR_ID",
    "XKCD_LEXICAL_FLOOR_STANDING",
    "XKCD_LEXICAL_FLOOR_VERSION",
    "XkcdLexicalFloor",
    "XkcdLexicalFloorError",
    "load_xkcd_lexical_floor",
    "replay_xkcd_lexical_floor",
]
