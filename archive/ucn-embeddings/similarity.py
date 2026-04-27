"""
ucns.similarity
===============
Similarity and distance metrics for Unit Circle Number embeddings.

All functions operate on plain Python lists of angles (floats in [0, τ)) as
returned by ``UCNEmbedding.encode``.  No external libraries required.

Metric catalogue
----------------
``phase_cosine``
    Mean of cos(θᵢ − φᵢ) – the natural "dot product" on the torus.
    Range: [−1, 1].  Value 1 means identical embeddings.

``arc_distance``
    Mean minimum arc length |θᵢ − φᵢ|_circle, normalised to [0, 1].
    Value 0 means identical; value 1 means diametrically opposite.

``hyperbolic_cosine``
    Uses the Poincaré disk: maps each angle to an interior point of the
    unit disk and computes hyperbolic cosine similarity.  Sensitive to
    hierarchical structure (high-frequency vs low-frequency components).

``top_k_overlap``
    Jaccard-like overlap of the *k* dominant frequency indices.  Good for
    sparse or categorical data.
"""

from __future__ import annotations

import math
import cmath
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
    """Mean angular cosine similarity between two UCNS embeddings.

    Parameters
    ----------
    a, b:
        Lists of angles (radians) of equal length.

    Returns
    -------
    float
        Value in ``[−1, 1]``.  A value of 1 indicates identical phase
        patterns; −1 indicates perfectly anti-phase patterns.
    """
    n = _check_same_length(a, b)
    if n == 0:
        return 0.0
    return sum(math.cos(ai - bi) for ai, bi in zip(a, b)) / n


def arc_distance(a: Sequence[float], b: Sequence[float]) -> float:
    """Mean normalised arc distance between two UCNS embeddings.

    Each per-dimension distance is the shorter arc between the two angles,
    normalised by π so the result lies in ``[0, 1]``.

    Parameters
    ----------
    a, b:
        Lists of angles (radians) of equal length.

    Returns
    -------
    float
        Value in ``[0, 1]``.  0 means identical; 1 means maximally different.
    """
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
    """Similarity via per-dimension hyperbolic cosine in the Poincaré disk.

    Each angle θ is embedded at ``r·e^(iθ)`` inside the unit disk.  The
    hyperbolic distance between the two disk points is converted to a cosine:

        sim = mean_k( cos( d_hyp(r·e^{iθ_k}, r·e^{iφ_k}) ) )

    This metric is more sensitive to *low-frequency* (large-amplitude)
    components than ``phase_cosine`` and captures hierarchical relationships.

    Parameters
    ----------
    a, b:
        Lists of angles (radians) of equal length.
    radius:
        Radial depth in ``(0, 1)`` for the disk embedding.  Smaller values
        compress the hyperbolic scale; larger values expand it.

    Returns
    -------
    float
        Value in ``[−1, 1]``.
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
            d = 0.0
        else:
            rho = abs((za - zb) / denom)
            rho = min(rho, 1.0 - 1e-15)
            d = 2.0 * math.atanh(rho)
        total += math.cos(d)
    return total / n


def top_k_overlap(
    amplitudes_a: Sequence[float],
    amplitudes_b: Sequence[float],
    *,
    k: int = 8,
) -> float:
    """Jaccard-like overlap of the *k* most energetic frequency components.

    Parameters
    ----------
    amplitudes_a, amplitudes_b:
        Amplitude arrays (as from ``EpicycleDecomposition.amplitudes``).
    k:
        Number of top components to compare.

    Returns
    -------
    float
        Value in ``[0, 1]``.  1 means the top-*k* frequency sets are
        identical; 0 means completely disjoint.
    """
    _check_same_length(amplitudes_a, amplitudes_b)
    k = max(1, min(k, len(amplitudes_a)))

    def top_k_indices(amps: Sequence[float]) -> set:
        return set(
            sorted(range(len(amps)), key=lambda i: amps[i], reverse=True)[:k]
        )

    sa = top_k_indices(amplitudes_a)
    sb = top_k_indices(amplitudes_b)
    intersection = len(sa & sb)
    union = len(sa | sb)
    return intersection / union if union else 0.0
