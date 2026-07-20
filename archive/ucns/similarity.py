"""Metrics for legacy local 2π phase-vector embeddings.

These functions operate on phase vectors produced by ``UCNEmbedding`` and
``EpicycleDecomposition``. They are not metrics on the canonical public gonol,
do not preserve its Möbius orientation state, and do not define a semantic or
theorem-backed UCNS distance.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_similarity
#   module_name: similarity
#   module_kind: adapter
#   summary: similarity and distance helpers for legacy local 2pi phase-vector embeddings; not public-gonol geometry
#   owner: Erin Spencer
#   public_surface: phase_cosine, arc_distance, hyperbolic_cosine, top_k_overlap
#   internal_surface: _check_same_length
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: read
#   admin_only: false
#   tests: tests.test_similarity
#   rollout: compatibility_only
#   rollback: remove after legacy embedding consumers migrate
#   requires: none
#   since: 2026-06-02
#   unresolved: no public-gonol or semantic metric bridge is defined
# === END MODULE_BUILD ===

import cmath
import math
from typing import Sequence

__all__ = [
    "phase_cosine",
    "arc_distance",
    "hyperbolic_cosine",
    "top_k_overlap",
]

_TAU = 2.0 * math.pi


def _check_same_length(a: Sequence[float], b: Sequence[float]) -> int:
    if len(a) != len(b):
        raise ValueError(
            f"Embeddings must have the same length; got {len(a)} and {len(b)}"
        )
    return len(a)


def phase_cosine(a: Sequence[float], b: Sequence[float]) -> float:
    """Mean cosine similarity for equal-length local phase vectors."""

    n = _check_same_length(a, b)
    if n == 0:
        return 0.0
    return sum(math.cos(ai - bi) for ai, bi in zip(a, b)) / n


def arc_distance(a: Sequence[float], b: Sequence[float]) -> float:
    """Mean normalized shortest-arc distance on a conventional 2π circle."""

    n = _check_same_length(a, b)
    if n == 0:
        return 0.0
    total = 0.0
    for ai, bi in zip(a, b):
        diff = abs(ai - bi) % _TAU
        total += min(diff, _TAU - diff)
    return total / (n * math.pi)


def hyperbolic_cosine(
    a: Sequence[float],
    b: Sequence[float],
    *,
    radius: float = 0.5,
) -> float:
    """Poincaré-disk similarity of local phase-vector coordinates.

    This is an experimental metric for the legacy embedding representation. It
    does not establish hierarchy, semantics, or public-gonol distance.
    """

    if not (0.0 < radius < 1.0):
        raise ValueError("radius must be in (0, 1)")
    n = _check_same_length(a, b)
    if n == 0:
        return 0.0
    total = 0.0
    for ai, bi in zip(a, b):
        za = radius * cmath.exp(1j * ai)
        zb = radius * cmath.exp(1j * bi)
        denom = 1.0 - zb.conjugate() * za
        if abs(denom) < 1e-15:
            distance = 0.0
        else:
            rho = abs((za - zb) / denom)
            rho = min(rho, 1.0 - 1e-15)
            distance = 2.0 * math.atanh(rho)
        total += math.cos(distance)
    return total / n


def top_k_overlap(
    amplitudes_a: Sequence[float],
    amplitudes_b: Sequence[float],
    *,
    k: int = 8,
) -> float:
    """Jaccard overlap of dominant FFT component indices."""

    _check_same_length(amplitudes_a, amplitudes_b)
    k = max(1, min(k, len(amplitudes_a)))

    def top_k_indices(amplitudes: Sequence[float]) -> set[int]:
        return set(
            sorted(
                range(len(amplitudes)),
                key=lambda index: amplitudes[index],
                reverse=True,
            )[:k]
        )

    left = top_k_indices(amplitudes_a)
    right = top_k_indices(amplitudes_b)
    union = len(left | right)
    return len(left & right) / union if union else 0.0
