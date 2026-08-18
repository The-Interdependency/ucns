# === MODULE_BUILD ===
# id: ucns_current_lexical_word_gonols
#   module_name: lexical_word_gonols
#   module_kind: engine
#   summary: constructs atomic xkcd floor-candidate word gonols through source-constrained history-bearing Möbius glyph-axis traversal
#   owner: Erin Spencer
#   public_surface: GlyphAxis, GlyphTraversalState, AtomicWordGonol, LexicalWordGonolCorpus, construct_xkcd_word_gonols, replay_word_gonol
#   internal_surface: _canonical_bytes, _identity, _next_potential
#   auth_boundary: requires an exact validated xkcd source receipt
#   storage_boundary: immutable in-memory construction and canonical identities only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_lexical_word_gonols
#   rollout: after both current lexical sources are pinned; prerequisite for morphology and definitions
#   rollback: remove current word-gonol candidate without altering source receipts or deprecated NGSL evidence
#   requires: ucns_current_lexical_sources, ucns_edcm_profile
#   since: 2026-08-18
#   unresolved: complete continuous spiral coordinates, morphological family mapping, final morphology law, direct distant interscale coupling
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: glyph_axis_is_mobius_and_public_carrier_bound
#   given: a glyph participates in a current lexical word gonol
#   then: its exact Unicode scalar and public-gonol carrier tic identify one intrinsic one-sided Möbius glyph axis without claiming complete continuous coordinates
#   class: correctness
#   since: 2026-08-18
#
# id: lexical_traversal_history_constrains_future
#   given: a source spelling is traversed
#   then: every state retains the complete realized prefix, selected glyph, prior state identity, exact source-admissible next glyphs, and closure availability so equal current glyphs after different histories remain distinct
#   class: correctness
#   since: 2026-08-18
#
# id: completed_word_gonols_are_atomic_and_reused
#   given: every exact xkcd accepted surface is constructed
#   then: each unique completed word gonol is materialized once, content-addressed by its intrinsic traversal, and consumed atomically at higher scales without an authoritative all-pairs sidecar graph
#   class: evidence
#   since: 2026-08-18
#
# id: lexical_word_gonols_replay_exactly
#   given: a completed word gonol and the exact source receipt are replayed
#   then: every axis, traversal state, potential, boundary, atomic identity, and corpus identity is restored exactly or replay fails closed
#   class: evidence
#   since: 2026-08-18
# === END CONTRACTS ===

"""Current source-constrained lexical word-gonol construction.

Usage::

    receipt = load_xkcd_simplewriter()
    corpus = construct_xkcd_word_gonols(receipt)
    branch = corpus.by_surface["branch"]
    assert replay_word_gonol(branch, receipt) == branch

The prefix index is an implementation aid. Authority remains the exact source
receipt plus each word gonol's intrinsic history-bearing construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from types import MappingProxyType
from typing import Mapping

from .edcm import PUBLIC_GONOL_SHA256, edcm_carrier_position
from .lexical_sources import XKCDSimpleWriterReceipt, XKCD_STANDING

GLYPH_AXIS_STANDING = "intrinsic-mobius-glyph-axis-candidate"
TRAVERSAL_STANDING = "source-constrained-history-bearing-traversal"
WORD_GONOL_STANDING = "atomic-xkcd-floor-word-gonol-candidate"
CORPUS_STANDING = "complete-xkcd-surface-word-gonol-candidate"
SPACE_BOUNDARY = "SPACE"


class LexicalWordGonolError(ValueError):
    """Raised when current lexical word construction loses source or history."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"


def _identity(prefix: str, value: object) -> str:
    return prefix + sha256(_canonical_bytes(value)).hexdigest()


@dataclass(frozen=True, slots=True)
class GlyphAxis:
    glyph: str
    code_point: int
    carrier_position: int
    public_gonol_sha256: str = PUBLIC_GONOL_SHA256
    topology: str = "mobius-one-sided-axis"
    glyph_role: str = "tic-on-axis"
    standing: str = GLYPH_AXIS_STANDING
    continuous_coordinates_exposed: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.glyph, str) or len(self.glyph) != 1:
            raise LexicalWordGonolError("glyph axis requires one Unicode scalar")
        if ord(self.glyph) != self.code_point:
            raise LexicalWordGonolError("glyph axis code point mismatch")
        expected = edcm_carrier_position(self.glyph)
        if expected is None or expected == 0 or self.carrier_position != expected:
            raise LexicalWordGonolError("glyph axis public carrier tic mismatch")
        if self.public_gonol_sha256 != PUBLIC_GONOL_SHA256:
            raise LexicalWordGonolError("glyph axis public gonol identity mismatch")
        if self.topology != "mobius-one-sided-axis" or self.glyph_role != "tic-on-axis":
            raise LexicalWordGonolError("glyph axis topology or tic role mismatch")
        if self.standing != GLYPH_AXIS_STANDING:
            raise LexicalWordGonolError("glyph axis standing cannot be promoted")
        if type(self.continuous_coordinates_exposed) is not bool or self.continuous_coordinates_exposed:
            raise LexicalWordGonolError("complete continuous glyph-axis coordinates remain unresolved")

    @property
    def axis_id(self) -> str:
        return _identity("ucns.glyph-axis:sha256:", {
            "glyph": self.glyph, "code_point": self.code_point,
            "carrier_position": self.carrier_position,
            "public_gonol_sha256": self.public_gonol_sha256,
            "topology": self.topology, "glyph_role": self.glyph_role,
            "standing": self.standing,
            "continuous_coordinates_exposed": self.continuous_coordinates_exposed,
        })


@dataclass(frozen=True, slots=True)
class GlyphTraversalState:
    step_index: int
    realized_prefix: str
    selected_axis_id: str
    selected_glyph: str
    selected_carrier_position: int
    prior_state_id: str
    admissible_next_glyphs: tuple[str, ...]
    space_boundary_available: bool
    source_receipt_id: str
    standing: str = TRAVERSAL_STANDING

    def __post_init__(self) -> None:
        if self.step_index < 0 or self.step_index != len(self.realized_prefix) - 1:
            raise LexicalWordGonolError("traversal step and prefix length mismatch")
        if not self.realized_prefix or self.realized_prefix[-1] != self.selected_glyph:
            raise LexicalWordGonolError("selected glyph does not close the realized prefix")
        if edcm_carrier_position(self.selected_glyph) != self.selected_carrier_position:
            raise LexicalWordGonolError("traversal selected carrier tic mismatch")
        if not self.selected_axis_id.startswith("ucns.glyph-axis:sha256:"):
            raise LexicalWordGonolError("traversal selected axis identity mismatch")
        expected_prior = "ucns.lexical-traversal-origin" if self.step_index == 0 else "ucns.glyph-traversal-state:sha256:"
        if not self.prior_state_id.startswith(expected_prior):
            raise LexicalWordGonolError("traversal prior state identity mismatch")
        if len(set(self.admissible_next_glyphs)) != len(self.admissible_next_glyphs):
            raise LexicalWordGonolError("traversal future potential contains duplicates")
        if type(self.space_boundary_available) is not bool:
            raise LexicalWordGonolError("SPACE boundary availability must be exact boolean")
        if not self.source_receipt_id.startswith("ucns.xkcd-simplewriter-receipt:sha256:"):
            raise LexicalWordGonolError("traversal source receipt identity mismatch")
        if self.standing != TRAVERSAL_STANDING:
            raise LexicalWordGonolError("traversal standing cannot be promoted")

    @property
    def state_id(self) -> str:
        return _identity("ucns.glyph-traversal-state:sha256:", {
            "step_index": self.step_index,
            "realized_prefix": self.realized_prefix,
            "selected_axis_id": self.selected_axis_id,
            "selected_glyph": self.selected_glyph,
            "selected_carrier_position": self.selected_carrier_position,
            "prior_state_id": self.prior_state_id,
            "admissible_next_glyphs": list(self.admissible_next_glyphs),
            "space_boundary_available": self.space_boundary_available,
            "source_receipt_id": self.source_receipt_id,
            "standing": self.standing,
        })


@dataclass(frozen=True, slots=True)
class AtomicWordGonol:
    surface: str
    source_receipt_id: str
    traversal: tuple[GlyphTraversalState, ...]
    terminal_state_id: str
    boundary: str = SPACE_BOUNDARY
    atomic_at_next_scale: bool = True
    standing: str = WORD_GONOL_STANDING

    def __post_init__(self) -> None:
        if not self.surface or "".join(item.selected_glyph for item in self.traversal) != self.surface:
            raise LexicalWordGonolError("word gonol traversal does not reconstruct surface")
        if tuple(item.step_index for item in self.traversal) != tuple(range(len(self.traversal))):
            raise LexicalWordGonolError("word gonol traversal is not occurrence ordered")
        if self.terminal_state_id != self.traversal[-1].state_id:
            raise LexicalWordGonolError("word gonol terminal state mismatch")
        if not self.traversal[-1].space_boundary_available or self.boundary != SPACE_BOUNDARY:
            raise LexicalWordGonolError("word gonol must close at a source-admissible SPACE boundary")
        if type(self.atomic_at_next_scale) is not bool or not self.atomic_at_next_scale:
            raise LexicalWordGonolError("completed word gonol must be atomic at the next scale")
        if self.standing != WORD_GONOL_STANDING:
            raise LexicalWordGonolError("word gonol standing cannot be promoted")

    @property
    def gonol_id(self) -> str:
        return _identity("ucns.atomic-word-gonol:sha256:", {
            "surface": self.surface,
            "source_receipt_id": self.source_receipt_id,
            "traversal_state_ids": [item.state_id for item in self.traversal],
            "terminal_state_id": self.terminal_state_id,
            "boundary": self.boundary,
            "atomic_at_next_scale": self.atomic_at_next_scale,
            "standing": self.standing,
        })


@dataclass(frozen=True, slots=True)
class LexicalWordGonolCorpus:
    source_receipt_id: str
    axes: tuple[GlyphAxis, ...]
    word_gonols: tuple[AtomicWordGonol, ...]
    standing: str = CORPUS_STANDING
    all_pairs_graph_materialized: bool = False

    def __post_init__(self) -> None:
        if len({item.axis_id for item in self.axes}) != len(self.axes):
            raise LexicalWordGonolError("lexical corpus glyph axes are duplicated")
        if len({item.surface for item in self.word_gonols}) != len(self.word_gonols):
            raise LexicalWordGonolError("lexical corpus word surfaces are duplicated")
        if len({item.gonol_id for item in self.word_gonols}) != len(self.word_gonols):
            raise LexicalWordGonolError("lexical corpus word gonol identities are duplicated")
        if any(item.source_receipt_id != self.source_receipt_id for item in self.word_gonols):
            raise LexicalWordGonolError("lexical corpus source receipt mismatch")
        if self.standing != CORPUS_STANDING:
            raise LexicalWordGonolError("lexical corpus standing cannot be promoted")
        if type(self.all_pairs_graph_materialized) is not bool or self.all_pairs_graph_materialized:
            raise LexicalWordGonolError("authoritative all-pairs lexical graph is forbidden")

    @property
    def by_surface(self) -> Mapping[str, AtomicWordGonol]:
        return MappingProxyType({item.surface: item for item in self.word_gonols})

    @property
    def corpus_id(self) -> str:
        return _identity("ucns.lexical-word-gonol-corpus:sha256:", {
            "source_receipt_id": self.source_receipt_id,
            "axis_ids": [item.axis_id for item in self.axes],
            "word_gonol_ids": [item.gonol_id for item in self.word_gonols],
            "standing": self.standing,
            "all_pairs_graph_materialized": self.all_pairs_graph_materialized,
        })


def _next_potential(prefix: str, surfaces: tuple[str, ...]) -> tuple[tuple[str, ...], bool]:
    next_glyphs = {
        surface[len(prefix)]
        for surface in surfaces
        if surface.startswith(prefix) and len(surface) > len(prefix)
    }
    ordered = tuple(sorted(
        next_glyphs,
        key=lambda glyph: (edcm_carrier_position(glyph), ord(glyph)),
    ))
    return ordered, prefix in surfaces


def construct_xkcd_word_gonols(
    source_receipt: XKCDSimpleWriterReceipt,
) -> LexicalWordGonolCorpus:
    """Construct every exact accepted surface in source order as one atomic gonol."""

    if not isinstance(source_receipt, XKCDSimpleWriterReceipt):
        raise TypeError("source_receipt must be an XKCDSimpleWriterReceipt")
    if source_receipt.standing != XKCD_STANDING:
        raise LexicalWordGonolError("xkcd source standing mismatch")
    surfaces = source_receipt.surface_forms
    glyphs = tuple(sorted(
        set("".join(surfaces)),
        key=lambda glyph: (edcm_carrier_position(glyph), ord(glyph)),
    ))
    axes = tuple(
        GlyphAxis(glyph, ord(glyph), edcm_carrier_position(glyph))  # type: ignore[arg-type]
        for glyph in glyphs
    )
    axis_by_glyph = {item.glyph: item for item in axes}
    receipt_id = source_receipt.receipt_id
    terminal_prefixes = set(surfaces)
    prefix_children: dict[str, set[str]] = {}
    for candidate in surfaces:
        for index, glyph in enumerate(candidate):
            prefix_children.setdefault(candidate[:index], set()).add(glyph)
    potential = {
        prefix: tuple(sorted(
            children,
            key=lambda glyph: (edcm_carrier_position(glyph), ord(glyph)),
        ))
        for prefix, children in prefix_children.items()
    }
    word_gonols: list[AtomicWordGonol] = []
    for surface in surfaces:
        traversal: list[GlyphTraversalState] = []
        prior = "ucns.lexical-traversal-origin"
        for index, glyph in enumerate(surface):
            prefix = surface[:index + 1]
            next_glyphs = potential.get(prefix, ())
            can_close = prefix in terminal_prefixes
            axis = axis_by_glyph[glyph]
            state = GlyphTraversalState(
                step_index=index,
                realized_prefix=prefix,
                selected_axis_id=axis.axis_id,
                selected_glyph=glyph,
                selected_carrier_position=axis.carrier_position,
                prior_state_id=prior,
                admissible_next_glyphs=next_glyphs,
                space_boundary_available=can_close,
                source_receipt_id=receipt_id,
            )
            traversal.append(state)
            prior = state.state_id
        word_gonols.append(AtomicWordGonol(
            surface=surface,
            source_receipt_id=receipt_id,
            traversal=tuple(traversal),
            terminal_state_id=traversal[-1].state_id,
        ))
    return LexicalWordGonolCorpus(receipt_id, axes, tuple(word_gonols))


def replay_word_gonol(
    word_gonol: AtomicWordGonol,
    source_receipt: XKCDSimpleWriterReceipt,
) -> AtomicWordGonol:
    """Independently reconstruct one word from exact source inventory and compare."""

    if word_gonol.surface not in source_receipt.surface_forms:
        raise LexicalWordGonolError("word gonol surface is absent from exact source")
    rebuilt = construct_xkcd_word_gonols(source_receipt).by_surface[word_gonol.surface]
    if rebuilt != word_gonol:
        raise LexicalWordGonolError("word gonol replay mismatch")
    return rebuilt


__all__ = [
    "AtomicWordGonol", "GlyphAxis", "GlyphTraversalState",
    "LexicalWordGonolCorpus", "LexicalWordGonolError",
    "construct_xkcd_word_gonols", "replay_word_gonol",
]
