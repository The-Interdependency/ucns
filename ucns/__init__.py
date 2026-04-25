"""
ucns – Unit Circle Number System
=================================
A zero-dependency Python library for creating compact, efficient embeddings
using a novel **Unit Circle Number System (UCNS)**.

Overview
--------
Every number in UCNS is an *angle* θ ∈ [0, 2π) that identifies a point on the
unit circle e^(iθ).  A sequence of such angles forms a UCNS embedding:

* **Compact** – angles stored as ``uint16`` use only 2 bytes per dimension
  (2× smaller than float32).
* **Fast similarity** – inner product = mean of cos(θᵢ − φᵢ); no length
  normalisation required.
* **Hierarchical** – the recursive epicycle (FFT) structure captures
  multi-scale patterns; the Möbius disk geometry supports hyperbolic
  (tree-like) relationships.
* **Zero dependencies** – pure Python standard library only.

Quick start
-----------
>>> from ucns import UCNEmbedding
>>> emb = UCNEmbedding(dim=64)
>>> v1 = emb.encode("hello world")
>>> v2 = emb.encode("hello world")
>>> emb.similarity(v1, v2)
1.0
>>> packed = emb.encode_packed("hello world")
>>> len(packed)   # 64 angles × 2 bytes
128

Building blocks
---------------
``UCN``
    Single unit-circle number (angle + arithmetic).
``EpicycleDecomposition``
    Decompose any signal into weighted unit-circle rotations via FFT.
``MobiusTransform``
    Conformal automorphism of the Poincaré disk.
``UCNEmbedding``
    High-level embedding API.
Similarity functions
    ``phase_cosine``, ``arc_distance``, ``hyperbolic_cosine``,
    ``top_k_overlap``.
"""

from .core import UCN, TAU
from .epicycle import EpicycleDecomposition, fft, ifft
from .embedding import UCNEmbedding
from .mobius import MobiusTransform, poincare_distance, disk_to_circle, circle_to_disk
from .similarity import phase_cosine, arc_distance, hyperbolic_cosine, top_k_overlap

__all__ = [
    # Core number type
    "UCN",
    "TAU",
    # Epicycle / FFT
    "EpicycleDecomposition",
    "fft",
    "ifft",
    # Möbius disk
    "MobiusTransform",
    "poincare_distance",
    "disk_to_circle",
    "circle_to_disk",
    # Embedding
    "UCNEmbedding",
    # Similarity metrics
    "phase_cosine",
    "arc_distance",
    "hyperbolic_cosine",
    "top_k_overlap",
]

__version__ = "0.1.0"
