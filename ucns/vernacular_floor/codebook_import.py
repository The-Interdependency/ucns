# === RATIOS ===
# loc_comments: hmmm
# unresolved: upstream_a0_betatest_checkout_path, construction_hash
# === END RATIOS ===
"""Read-only import boundary for the upstream a0-betatest public gonol glyph codebook."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable, Optional, Tuple, Union

PathLike = Union[str, Path]

from .a0_public_gonol import A0PublicGonolConstruction, import_a0_public_gonol

EXPECTED_PUBLIC_GLYPH_COUNT = (100 + 50 + 7)


def load_codebook(path: Optional[PathLike] = None) -> Tuple[str, ...]:
    """Import glyphs from a0-betatest's public gonol construction.

    ``path`` may point at an a0-betatest checkout or backend directory.  When it
    is omitted, the active Python path must already expose a0-betatest's
    ``interdependent_lib`` package.
    """

    construction = import_a0_public_gonol(path)
    return codebook_from_construction(construction)


def codebook_from_construction(construction: A0PublicGonolConstruction) -> Tuple[str, ...]:
    """Extract and validate the glyph codebook from confirmed construction metadata."""

    construction.confirm_a0_betatest()
    validate_codebook(construction.glyphs)
    return construction.glyphs


def validate_codebook(glyphs: Iterable[str]) -> None:
    """Assert imported glyph cardinality, uniqueness, invertibility, and primality."""

    items = tuple(glyphs)
    if len(items) != EXPECTED_PUBLIC_GLYPH_COUNT:
        raise ValueError("imported public glyph count does not match the field cardinality")
    if len(set(items)) != len(items):
        raise ValueError("imported public glyph codebook contains duplicate entries")
    if any(item == "" for item in items):
        raise ValueError("glyph entries must be explicit; use a literal space for the origin")
    if not is_prime(len(items)):
        raise ValueError("imported public glyph count is not prime")


def is_prime(n: int) -> bool:
    """Return True when *n* is prime using a small deterministic check."""

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for candidate in range(3, limit + 1, 2):
        if n % candidate == 0:
            return False
    return True


# === RATIOS ===
# loc_comments: hmmm
# unresolved: upstream_a0_betatest_checkout_path, construction_hash
# === END RATIOS ===
