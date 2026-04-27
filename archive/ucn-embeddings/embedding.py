"""
ucns.embedding
==============
High-level embedding API built on the Unit Circle Number System.

**Why UCNS embeddings?**

Traditional neural embeddings (e.g. word2vec, BERT, OpenAI Ada) produce
*dense float32 vectors* of 384–3072 dimensions.  UCNS embeddings offer three
concrete advantages:

1. **Compact storage** – angles are quantised to ``uint16`` (2 bytes), giving
   a 2× space saving over ``float32`` with negligible information loss
   (≈0.0001 rad angular resolution).

2. **Fast similarity** – the inner product ``cos(θᵢ − φᵢ)`` is computed with
   a single subtraction and cosine lookup per dimension.  No square root for
   normalisation is needed because all embeddings already live on the unit
   torus (‖embedding‖ = 1 by construction).

3. **Zero dependencies** – implemented entirely in the Python standard library
   (``math``, ``cmath``, ``struct``).

Architecture
------------
``UCNEmbedding`` uses ``EpicycleDecomposition`` under the hood:

    input data  →  real-valued signal  →  FFT  →  phases  =  embedding

The embedding dimension is always a power of two (the next power-of-two ≥
*dim*) because the FFT requires it.  Extra dimensions are zeroed out.

Supported input types
---------------------
* ``float`` / ``int`` – single-element signal.
* ``str`` – ordinal encoding of Unicode code points.
* ``list[float]`` / ``tuple[float]`` – arbitrary real-valued signal.
* ``bytes`` – unsigned byte values as signal.
"""

from __future__ import annotations

import math
import struct
from typing import Union

from .epicycle import EpicycleDecomposition, _next_pow2

__all__ = ["UCNEmbedding"]

_TAU = 2.0 * math.pi

# Type accepted by UCNEmbedding.encode
Encodable = Union[int, float, str, bytes, list, tuple]


class UCNEmbedding:
    """Generate and compare Unit Circle Number System embeddings.

    Parameters
    ----------
    dim:
        Desired embedding dimension.  The actual dimension used is the next
        power of two ≥ *dim* (because the FFT requires it).

    Examples
    --------
    >>> emb = UCNEmbedding(dim=16)
    >>> v1 = emb.encode("hello")
    >>> v2 = emb.encode("hello")
    >>> emb.similarity(v1, v2)
    1.0
    >>> v3 = emb.encode("world")
    >>> -1.0 <= emb.similarity(v1, v3) <= 1.0
    True
    """

    def __init__(self, dim: int = 64) -> None:
        if dim < 1:
            raise ValueError("dim must be at least 1")
        self._dim_requested: int = dim
        self._dim: int = _next_pow2(dim)

    @property
    def dim(self) -> int:
        """Actual embedding dimension (next power of two ≥ the requested dim)."""
        return self._dim

    # ------------------------------------------------------------------
    # Encoding
    # ------------------------------------------------------------------

    def encode(self, data: Encodable) -> list[float]:
        """Encode *data* as a UCNS embedding vector.

        Returns a list of ``dim`` angles in ``[0, τ)``.  Identical data always
        produces identical embeddings.

        Parameters
        ----------
        data:
            Input to encode.  See module docstring for supported types.
        """
        signal = self._to_signal(data)
        # Pad / truncate to self._dim
        if len(signal) < self._dim:
            signal = signal + [0.0] * (self._dim - len(signal))
        else:
            signal = signal[: self._dim]
        decomp = EpicycleDecomposition(signal)
        return decomp.phase_vector

    def encode_packed(self, data: Encodable) -> bytes:
        """Encode and immediately serialise to compact ``uint16`` bytes.

        Each of the ``dim`` angles is stored as a 16-bit unsigned integer,
        giving ``2 * dim`` bytes total (vs. ``4 * dim`` for float32).
        """
        phases = self.encode(data)
        scale = 65535.0 / _TAU
        ints = [min(65535, int(p * scale)) for p in phases]
        return struct.pack(f"<{len(ints)}H", *ints)

    @staticmethod
    def unpack(data: bytes) -> list[float]:
        """Unpack ``uint16`` bytes back to a list of float angles."""
        n = len(data) // 2
        ints = struct.unpack(f"<{n}H", data)
        scale = _TAU / 65535.0
        return [v * scale for v in ints]

    # ------------------------------------------------------------------
    # Similarity
    # ------------------------------------------------------------------

    def similarity(self, a: list[float], b: list[float]) -> float:
        """Mean phase-cosine similarity between two embeddings ∈ [−1, 1].

        This is the canonical UCNS inner product:

            sim(a, b) = (1/dim) · Σᵢ cos(aᵢ − bᵢ)

        All embedding vectors have unit "norm" under this metric, so the
        result is a pure cosine without any length normalisation step.
        """
        if len(a) != len(b):
            raise ValueError(
                f"Embeddings must have equal length; got {len(a)} and {len(b)}"
            )
        if not a:
            return 0.0
        return sum(math.cos(ai - bi) for ai, bi in zip(a, b)) / len(a)

    def nearest(
        self,
        query: list[float],
        corpus: list[list[float]],
    ) -> tuple[int, float]:
        """Find the index and score of the most similar embedding in *corpus*.

        Parameters
        ----------
        query:
            Query embedding (list of angles).
        corpus:
            List of candidate embeddings to compare against.

        Returns
        -------
        (index, score):
            Index of the best match and its similarity score in ``[−1, 1]``.
        """
        if not corpus:
            raise ValueError("corpus is empty")
        best_idx = 0
        best_score = self.similarity(query, corpus[0])
        for i, candidate in enumerate(corpus[1:], start=1):
            score = self.similarity(query, candidate)
            if score > best_score:
                best_score = score
                best_idx = i
        return best_idx, best_score

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _to_signal(data: Encodable) -> list[float]:
        """Convert supported input types to a list of floats."""
        if isinstance(data, (int, float)):
            return [float(data)]
        if isinstance(data, str):
            return [float(ord(c)) for c in data]
        if isinstance(data, bytes):
            return [float(b) for b in data]
        if isinstance(data, (list, tuple)):
            return [float(x) for x in data]
        raise TypeError(
            f"Unsupported type {type(data).__name__!r}. "
            "Expected int, float, str, bytes, list, or tuple."
        )

    # ------------------------------------------------------------------
    # Dunder
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"UCNEmbedding(dim={self._dim}, "
            f"bytes_per_embedding={self._dim * 2})"
        )
