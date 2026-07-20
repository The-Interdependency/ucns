"""Legacy FFT phase-vector embedding compatibility surface.

``UCNEmbedding`` converts input data into a conventional 2π phase vector through
an FFT. It is an experimental/local embedding utility, not the canonical public
gonol, not a lossless public-gonol text encoding, and not a proof-backed UCNS
semantic embedding.

Strings are converted to Unicode ordinal signals; they do not use the canonical
157-position public arrangement or lifted traversal. Consequently this module
must not be cited as preserving the fixed SPACE/ZERO twist origin, 720-degree
return, public faces/chirality, or public-gonol identity.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_embedding
#   module_name: embedding
#   module_kind: adapter
#   summary: legacy FFT phase-vector embedding over local 2pi coordinates; explicitly not the public-gonol encoder or a semantic/theorem surface
#   owner: Erin Spencer
#   public_surface: UCNEmbedding
#   internal_surface: _to_signal
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: read
#   admin_only: false
#   tests: tests.test_embedding
#   rollout: compatibility_only
#   rollback: remove after legacy consumers migrate to explicitly named embedding surfaces
#   requires: ucns_epicycle
#   since: 2026-06-02
#   unresolved: no public-gonol or semantic bridge is defined
# === END MODULE_BUILD ===

import math
import struct
from typing import Union

from .epicycle import EpicycleDecomposition, _next_pow2

__all__ = ["UCNEmbedding"]

_TAU = 2.0 * math.pi

Encodable = Union[int, float, str, bytes, list, tuple]


class UCNEmbedding:
    """Generate and compare legacy FFT phase-vector embeddings.

    The returned values are local phases in ``[0, 2π)``. They are not
    public-gonol positions and do not retain the Möbius orientation state.

    Parameters
    ----------
    dim:
        Requested phase-vector dimension. The actual dimension is the next power
        of two because the implementation uses a radix-2 FFT.
    """

    def __init__(self, dim: int = 64) -> None:
        if dim < 1:
            raise ValueError("dim must be at least 1")
        self._dim_requested = dim
        self._dim = _next_pow2(dim)

    @property
    def dim(self) -> int:
        """Actual FFT dimension."""

        return self._dim

    def encode(self, data: Encodable) -> list[float]:
        """Encode data as deterministic local FFT phases.

        For strings, Unicode code points are used as a numeric signal. This is
        deliberately distinct from ``ucns.encode_text_path``.
        """

        signal = self._to_signal(data)
        if len(signal) < self._dim:
            signal = signal + [0.0] * (self._dim - len(signal))
        else:
            signal = signal[: self._dim]
        return EpicycleDecomposition(signal).phase_vector

    def encode_packed(self, data: Encodable) -> bytes:
        """Encode and quantize local phases to unsigned 16-bit values."""

        phases = self.encode(data)
        scale = 65535.0 / _TAU
        ints = [min(65535, int(p * scale)) for p in phases]
        return struct.pack(f"<{len(ints)}H", *ints)

    @staticmethod
    def unpack(data: bytes) -> list[float]:
        """Unpack unsigned 16-bit values as local 2π phases."""

        n = len(data) // 2
        ints = struct.unpack(f"<{n}H", data)
        scale = _TAU / 65535.0
        return [v * scale for v in ints]

    def similarity(self, a: list[float], b: list[float]) -> float:
        """Mean phase-cosine similarity for this local embedding representation."""

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
        """Return the highest-scoring candidate under local phase similarity."""

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

    @staticmethod
    def _to_signal(data: Encodable) -> list[float]:
        """Convert supported input types to a numerical FFT signal."""

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

    def __repr__(self) -> str:
        return (
            f"UCNEmbedding(dim={self._dim}, "
            f"bytes_per_embedding={self._dim * 2})"
        )
