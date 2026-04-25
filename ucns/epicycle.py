"""
ucns.epicycle
=============
Epicycle decomposition via the Fast Fourier Transform (FFT).

**What are epicycles?**
In the Ptolemaic model of the solar system, planets move on small circles
(epicycles) whose centres trace larger circles.  Mathematically this is
equivalent to a finite Fourier series: any smooth periodic signal can be
written as a superposition of circular motions at integer multiples of a
fundamental frequency.

**Why epicycles for UCNS?**
The unit circle supports exactly this structure.  A signal of length *n* is
fully characterised by *n* complex Fourier coefficients.  Each coefficient
describes *one epicycle*:

    amplitude  = radius of the epicycle
    frequency  = how many full turns per signal period
    phase      = UCN angle at which that epicycle starts

Storing only the *phases* (and discarding amplitude information) gives a
compact angular "fingerprint" of the signal.  Including amplitudes allows
exact reconstruction (the full DFT is invertible).

**Efficiency**
This module implements a pure-Python Cooley–Tukey radix-2 FFT so that large
signals are handled in O(n log n) time rather than the O(n²) naive DFT.
Inputs whose length is not a power of two are zero-padded automatically.
"""

from __future__ import annotations

import cmath
import math
import struct

__all__ = [
    "fft",
    "ifft",
    "EpicycleDecomposition",
]

_TAU = 2.0 * math.pi


# ------------------------------------------------------------------
# Low-level FFT (radix-2 Cooley–Tukey, in-place)
# ------------------------------------------------------------------


def _next_pow2(n: int) -> int:
    """Return the smallest power of two ≥ *n*."""
    p = 1
    while p < n:
        p <<= 1
    return p


def fft(signal: list[float | complex]) -> list[complex]:
    """Compute the 1-D Discrete Fourier Transform using the Cooley–Tukey
    radix-2 FFT algorithm.

    Parameters
    ----------
    signal:
        Sequence of real or complex samples.  If its length is not a power of
        two it is **zero-padded** to the next power of two.

    Returns
    -------
    list[complex]
        Length-*N* list of complex frequency-domain coefficients where
        ``N = next_pow2(len(signal))``.  The *k*-th entry equals

            X[k] = Σ_{j=0}^{N-1}  x[j] · e^{−2πi·j·k/N}.
    """
    n = _next_pow2(len(signal))
    x: list[complex] = [complex(v) for v in signal]
    x += [0j] * (n - len(x))  # zero-pad
    _fft_inplace(x, inverse=False)
    return x


def ifft(spectrum: list[complex]) -> list[complex]:
    """Compute the inverse DFT (normalised so that ``ifft(fft(x)) ≈ x``).

    Parameters
    ----------
    spectrum:
        Length-*N* sequence of complex frequency coefficients
        (``N`` must be a power of two).

    Returns
    -------
    list[complex]
        Length-*N* list of complex time-domain samples.
    """
    n = len(spectrum)
    if n == 0:
        return []
    x = [complex(v) for v in spectrum]
    _fft_inplace(x, inverse=True)
    inv_n = 1.0 / n
    return [v * inv_n for v in x]


def _fft_inplace(x: list[complex], *, inverse: bool) -> None:
    """Cooley–Tukey iterative FFT (bit-reversal permutation + butterfly).

    Operates in-place on list *x* whose length **must** be a power of two.
    """
    n = len(x)
    if n <= 1:
        return

    # Bit-reversal permutation
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            x[i], x[j] = x[j], x[i]

    # Butterfly passes
    sign = 1.0 if inverse else -1.0
    length = 2
    while length <= n:
        half = length >> 1
        w_n = cmath.exp(1j * sign * _TAU / length)
        for i in range(0, n, length):
            w = 1.0 + 0j
            for k in range(half):
                u = x[i + k]
                v = x[i + k + half] * w
                x[i + k] = u + v
                x[i + k + half] = u - v
                w *= w_n
        length <<= 1


# ------------------------------------------------------------------
# High-level epicycle decomposition
# ------------------------------------------------------------------


class EpicycleDecomposition:
    """Represent a real signal as a set of weighted unit-circle rotations.

    After construction, the signal is fully described by three parallel arrays:

    * ``amplitudes[k]`` – radius of the *k*-th epicycle (≥ 0).
    * ``phases[k]``     – UCN angle of the *k*-th epicycle ∈ [0, τ).
    * ``frequencies[k]`` – integer frequency index (0, 1, …, N−1).

    Parameters
    ----------
    signal:
        1-D sequence of real (or complex) numbers.
    """

    __slots__ = ("_n_orig", "_n", "amplitudes", "phases", "frequencies")

    def __init__(self, signal: list[float | complex]) -> None:
        if not signal:
            raise ValueError("signal must be non-empty")
        self._n_orig: int = len(signal)
        spectrum = fft(signal)
        n = len(spectrum)
        self._n: int = n
        self.frequencies: list[int] = list(range(n))
        self.amplitudes: list[float] = [abs(c) / n for c in spectrum]
        self.phases: list[float] = [
            cmath.phase(c) % _TAU if abs(c) > 1e-12 else 0.0
            for c in spectrum
        ]

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def n(self) -> int:
        """Length of the (possibly padded) transform."""
        return self._n

    @property
    def phase_vector(self) -> list[float]:
        """All epicycle phases as a flat list of angles in ``[0, τ)``."""
        return list(self.phases)

    @property
    def dominant_frequency(self) -> int:
        """Index of the epicycle with the largest amplitude."""
        return max(range(self._n), key=lambda k: self.amplitudes[k])

    # ------------------------------------------------------------------
    # Reconstruction
    # ------------------------------------------------------------------

    def reconstruct(self) -> list[float]:
        """Reconstruct the original signal (first ``n_orig`` samples).

        Reconstruction is lossless when the input length was already a power
        of two; otherwise only the first ``n_orig`` values are meaningful.
        """
        n = self._n
        spectrum = [
            self.amplitudes[k] * n * cmath.exp(1j * self.phases[k])
            for k in range(n)
        ]
        samples = ifft(spectrum)
        return [s.real for s in samples[: self._n_orig]]

    # ------------------------------------------------------------------
    # Similarity
    # ------------------------------------------------------------------

    def phase_similarity(self, other: "EpicycleDecomposition") -> float:
        """Amplitude-weighted phase-cosine similarity ∈ [−1, 1].

        Computes

            sim = Σ_k  (A_k · B_k · cos(φ_k − ψ_k))  /  (‖A‖₂ · ‖B‖₂)

        where *A_k*, *B_k* are the amplitudes and *φ_k*, *ψ_k* are the phases
        of the two decompositions.  Uses only the shared frequency bands when
        the two transforms have different lengths.
        """
        n = min(self._n, other._n)
        total = sum(
            self.amplitudes[k] * other.amplitudes[k]
            * math.cos(self.phases[k] - other.phases[k])
            for k in range(n)
        )
        norm_a = math.sqrt(sum(a * a for a in self.amplitudes[:n])) or 1.0
        norm_b = math.sqrt(sum(b * b for b in other.amplitudes[:n])) or 1.0
        return total / (norm_a * norm_b)

    # ------------------------------------------------------------------
    # Compact serialisation
    # ------------------------------------------------------------------

    def pack(self) -> bytes:
        """Serialise phases as 16-bit unsigned integers (2 bytes each).

        Provides ~0.0001 rad resolution with 2 bytes per dimension, giving a
        **2× compression** vs. 32-bit floats for the same angular data.
        """
        scale = 65535.0 / _TAU
        ints = [min(65535, int(p * scale)) for p in self.phases]
        return struct.pack(f"<{len(ints)}H", *ints)

    @classmethod
    def unpack_phases(cls, data: bytes) -> list[float]:
        """Deserialise 16-bit integer phases back to floats in ``[0, τ)``."""
        n = len(data) // 2
        ints = struct.unpack(f"<{n}H", data)
        scale = _TAU / 65535.0
        return [v * scale for v in ints]

    # ------------------------------------------------------------------
    # Dunder
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        dom = self.dominant_frequency
        return (
            f"EpicycleDecomposition(n={self._n}, "
            f"dominant_freq={dom}, "
            f"dominant_amplitude={self.amplitudes[dom]:.4f})"
        )

    def __len__(self) -> int:
        return self._n
