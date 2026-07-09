# === RATIOS ===
# loc_comments: hmmm
# unresolved: glyph_axis_weight_law
# === END RATIOS ===
"""Ambient glyph-axis construction from the imported a0-betatest codebook."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Mapping, Tuple

from .assignment import FloorGonol
from .codebook_import import validate_codebook

TAU4 = 4.0 * math.pi


@dataclass(frozen=True)
class GlyphAxis:
    """A glyph's ambient circular axis, inherited from imported codebook order."""

    glyph: str
    index: int
    theta: float

    def as_gonol(self) -> FloorGonol:
        """Represent this glyph axis as a primitive floor gonol."""

        return FloorGonol(label=self.glyph, r=0.0, theta=self.theta)


def glyph_axes_from_codebook(glyphs: Iterable[str]) -> Tuple[GlyphAxis, ...]:
    """Map imported codebook order to evenly spaced axes on R/4πZ.

    This function does not choose membership and does not reconstruct the
    codebook.  It treats the upstream order as the public quantizer and maps
    index 0 — the space/origin glyph — to θ=0.
    """

    codebook = tuple(glyphs)
    validate_codebook(codebook)
    if codebook[0] != " ":
        raise ValueError("imported a0 public gonol must place space at origin index 0")
    count = len(codebook)
    return tuple(
        GlyphAxis(glyph=glyph, index=index, theta=(index * TAU4) / count)
        for index, glyph in enumerate(codebook)
    )


def glyph_gonols_from_codebook(glyphs: Iterable[str]) -> Mapping[str, FloorGonol]:
    """Return glyph→gonol primitives for every imported codebook axis."""

    return {axis.glyph: axis.as_gonol() for axis in glyph_axes_from_codebook(glyphs)}


# === RATIOS ===
# loc_comments: hmmm
# unresolved: glyph_axis_weight_law
# === END RATIOS ===
