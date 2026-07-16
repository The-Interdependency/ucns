"""Legacy FFT/epicycle signal decomposition.

This module is a conventional 2π Fourier-analysis utility. It does not define
the UCNS public gonol, the fixed SPACE/ZERO twist origin, or the 720-degree
complete return. Its phases are local signal-analysis coordinates and are not
public-gonol positions.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_epicycle
#   module_name: epicycle
#   module_kind: adapter
#   summary: legacy radix-2 FFT and epicycle signal decomposition over local 2pi phases; not the public-gonol frame
#   owner: Erin Spencer
#   public_surface: fft, ifft, EpicycleDecomposition
#   internal_surface: _next_pow2, _fft_inplace
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: read
#   admin_only: false
#   tests: tests.test_epicycle
#   rollout: compatibility_only
#   rollback: remove after legacy FFT embedding consumers migrate
#   requires: none
#   since: 2026-06-02
#   unresolved: no public-gonol bridge is defined
# === END MODULE_BUILD ===

import cmath
import math
import struct

__all__ = ["fft", "ifft", "EpicycleDecomposition"]

_TAU = 2.0 * math.pi


def _next_pow2(n: int) -> int:
    """Return the smallest power of two greater than or equal to ``n``."""

    p = 1
    while p < n:
        p <<= 1
    return p


def fft(signal: list[float | complex]) -> list[complex]:
    """Compute a zero-padded radix-2 discrete Fourier transform."""

    n = _next_pow2(len(signal))
    values = [complex(v) for v in signal]
    values += [0j] * (n - len(values))
    _fft_inplace(values, inverse=False)
    return values


def ifft(spectrum: list[complex]) -> list[complex]:
    """Compute the normalized inverse radix-2 transform."""

    n = len(spectrum)
    if n == 0:
        return []
    values = [complex(v) for v in spectrum]
    _fft_inplace(values, inverse=True)
    inv_n = 1.0 / n
    return [v * inv_n for v in values]


def _fft_inplace(values: list[complex], *, inverse: bool) -> None:
    """Iterative Cooley–Tukey FFT on a power-of-two list."""

    n = len(values)
    if n <= 1:
        return

    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            values[i], values[j] = values[j], values[i]

    sign = 1.0 if inverse else -1.0
    length = 2
    while length <= n:
        half = length >> 1
        w_n = cmath.exp(1j * sign * _TAU / length)
        for i in range(0, n, length):
            w = 1.0 + 0j
            for k in range(half):
                u = values[i + k]
                v = values[i + k + half] * w
                values[i + k] = u + v
                values[i + k + half] = u - v
                w *= w_n
        length <<= 1


class EpicycleDecomposition:
    """Represent a signal by Fourier amplitudes and local 2π phases.

    The phases intentionally identify one conventional 360-degree period and
    therefore do not preserve the public Möbius orientation state. This class is
    for signal analysis and legacy embedding compatibility only.
    """

    __slots__ = ("_n_orig", "_n", "amplitudes", "phases", "frequencies")

    def __init__(self, signal: list[float | complex]) -> None:
        if not signal:
            raise ValueError("signal must be non-empty")
        self._n_orig = len(signal)
        spectrum = fft(signal)
        n = len(spectrum)
        self._n = n
        self.frequencies = list(range(n))
        self.amplitudes = [abs(c) / n for c in spectrum]
        self.phases = [
            cmath.phase(c) % _TAU if abs(c) > 1e-12 else 0.0
            for c in spectrum
        ]

    @property
    def n(self) -> int:
        """Length of the padded transform."""

        return self._n

    @property
    def phase_vector(self) -> list[float]:
        """Return local phases in ``[0, 2π)``."""

        return list(self.phases)

    @property
    def dominant_frequency(self) -> int:
        """Return the index with greatest Fourier amplitude."""

        return max(range(self._n), key=lambda k: self.amplitudes[k])

    def reconstruct(self) -> list[float]:
        """Reconstruct the original signal samples represented by the full FFT."""

        n = self._n
        spectrum = [
            self.amplitudes[k] * n * cmath.exp(1j * self.phases[k])
            for k in range(n)
        ]
        samples = ifft(spectrum)
        return [sample.real for sample in samples[: self._n_orig]]

    def phase_similarity(self, other: "EpicycleDecomposition") -> float:
        """Amplitude-weighted local phase-cosine similarity."""

        n = min(self._n, other._n)
        total = sum(
            self.amplitudes[k]
            * other.amplitudes[k]
            * math.cos(self.phases[k] - other.phases[k])
            for k in range(n)
        )
        norm_a = math.sqrt(sum(a * a for a in self.amplitudes[:n])) or 1.0
        norm_b = math.sqrt(sum(b * b for b in other.amplitudes[:n])) or 1.0
        return total / (norm_a * norm_b)

    def pack(self) -> bytes:
        """Quantize local phases to unsigned 16-bit values."""

        scale = 65535.0 / _TAU
        ints = [min(65535, int(p * scale)) for p in self.phases]
        return struct.pack(f"<{len(ints)}H", *ints)

    @classmethod
    def unpack_phases(cls, data: bytes) -> list[float]:
        """Deserialize unsigned 16-bit values as local phases."""

        n = len(data) // 2
        ints = struct.unpack(f"<{n}H", data)
        scale = _TAU / 65535.0
        return [v * scale for v in ints]

    def __repr__(self) -> str:
        dominant = self.dominant_frequency
        return (
            f"EpicycleDecomposition(n={self._n}, "
            f"dominant_freq={dominant}, "
            f"dominant_amplitude={self.amplitudes[dominant]:.4f})"
        )

    def __len__(self) -> int:
        return self._n
