# === RATIOS ===
# loc_comments: hmmm
# unresolved: word_membership_rule, angular_assignment_law
# === END RATIOS ===
"""End-to-end vernacular floor build over imported codebook and relation graphs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Optional, Tuple

from .assignment import FloorGonol, assign_from_relations
from .codebook_import import load_codebook
from .glyph_axes import GlyphAxis, glyph_axes_from_codebook
from .manifest import MembershipPredicate
from .oewn_ingest import RelationGraph


@dataclass(frozen=True)
class FloorBuildResult:
    """Resolved build output for a supplied membership predicate and graph set."""

    codebook: Tuple[str, ...]
    glyph_axes: Tuple[GlyphAxis, ...]
    floor: Tuple[FloorGonol, ...]


def build_floor(
    relation_graphs: Iterable[RelationGraph],
    membership_predicate: MembershipPredicate,
    a0_betatest_path: Optional[str] = None,
) -> FloorBuildResult:
    """Build a floor artifact from declared inputs without guessing membership.

    The caller must provide the membership predicate.  This makes the remaining
    hmmm explicit while still resolving the executable path from upstream a0
    gonol import through relation-derived floor gonols.
    """

    codebook = load_codebook(a0_betatest_path)
    axes = glyph_axes_from_codebook(codebook)
    floor = []
    for graph in relation_graphs:
        metadata = {"edges": graph.edges}
        if membership_predicate(graph.lemma, metadata):
            floor.append(assign_from_relations(graph.lemma, graph.edges))
    return FloorBuildResult(codebook=codebook, glyph_axes=axes, floor=tuple(floor))


# === RATIOS ===
# loc_comments: hmmm
# unresolved: word_membership_rule, angular_assignment_law
# === END RATIOS ===
