"""Tests for ucns.epicycle – FFT and EpicycleDecomposition."""

import cmath
import math
import unittest

from ucns.epicycle import EpicycleDecomposition, fft, ifft, _next_pow2

_TAU = 2.0 * math.pi


class TestNextPow2(unittest.TestCase):
    def test_exact_power_of_two(self):
        for p in [1, 2, 4, 8, 16, 32, 64]:
            self.assertEqual(_next_pow2(p), p)

    def test_non_power_of_two(self):
        self.assertEqual(_next_pow2(3), 4)
        self.assertEqual(_next_pow2(5), 8)
        self.assertEqual(_next_pow2(100), 128)


class TestFFT(unittest.TestCase):
    def _slow_dft(self, x):
        n = len(x)
        return [
            sum(x[j] * cmath.exp(-1j * _TAU * k * j / n) for j in range(n))
            for k in range(n)
        ]

    def test_fft_equals_dft_n4(self):
        signal = [1.0, 2.0, 3.0, 4.0]
        fast = fft(signal)
        slow = self._slow_dft(signal)
        for a, b in zip(fast, slow):
            self.assertAlmostEqual(a, b, places=10)

    def test_fft_equals_dft_n8(self):
        import math
        signal = [math.sin(_TAU * k / 8) for k in range(8)]
        fast = fft(signal)
        slow = self._slow_dft(signal)
        for a, b in zip(fast, slow):
            self.assertAlmostEqual(a, b, places=10)

    def test_fft_zero_pads(self):
        # Length 3 → padded to 4
        result = fft([1.0, 2.0, 3.0])
        self.assertEqual(len(result), 4)

    def test_fft_single_element(self):
        result = fft([5.0])
        self.assertAlmostEqual(result[0], 5.0, places=12)

    def test_fft_dc_component(self):
        """DC component (k=0) should equal sum of the signal."""
        signal = [1.0, 2.0, 3.0, 4.0]
        result = fft(signal)
        self.assertAlmostEqual(result[0].real, sum(signal), places=10)

    def test_ifft_fft_roundtrip(self):
        signal = [1.0, -2.0, 3.5, -0.5, 0.0, 1.0, 2.0, -3.0]
        restored = ifft(fft(signal))
        for orig, rec in zip(signal, restored):
            self.assertAlmostEqual(orig, rec.real, places=10)
            self.assertAlmostEqual(rec.imag, 0.0, places=10)

    def test_ifft_empty(self):
        self.assertEqual(ifft([]), [])

    def test_parseval_theorem(self):
        """Energy in time domain == energy in frequency domain / N."""
        signal = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
        spectrum = fft(signal)
        n = len(spectrum)
        energy_time = sum(x * x for x in signal)
        energy_freq = sum(abs(X) ** 2 for X in spectrum) / n
        self.assertAlmostEqual(energy_time, energy_freq, places=8)


class TestEpicycleDecomposition(unittest.TestCase):
    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            EpicycleDecomposition([])

    def test_lengths(self):
        d = EpicycleDecomposition([1.0, 2.0, 3.0, 4.0])
        self.assertEqual(len(d.amplitudes), d.n)
        self.assertEqual(len(d.phases), d.n)
        self.assertEqual(len(d.frequencies), d.n)

    def test_n_is_power_of_two(self):
        d = EpicycleDecomposition([1.0, 2.0, 3.0])
        self.assertEqual(d.n, 4)

    def test_amplitudes_nonnegative(self):
        d = EpicycleDecomposition([1.0, -2.0, 3.0, -4.0])
        for a in d.amplitudes:
            self.assertGreaterEqual(a, 0.0)

    def test_phases_in_range(self):
        d = EpicycleDecomposition([1.5, 2.5, 0.5, -1.0])
        for p in d.phases:
            self.assertGreaterEqual(p, 0.0)
            self.assertLess(p, _TAU + 1e-9)

    def test_reconstruction_lossless(self):
        signal = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
        d = EpicycleDecomposition(signal)
        rec = d.reconstruct()
        for orig, r in zip(signal, rec):
            self.assertAlmostEqual(orig, r, places=8)

    def test_reconstruction_padded(self):
        """Non-power-of-2 input: first n_orig values should reconstruct."""
        signal = [3.0, 1.0, 4.0, 1.0, 5.0]  # length 5 → padded to 8
        d = EpicycleDecomposition(signal)
        rec = d.reconstruct()
        self.assertEqual(len(rec), len(signal))
        for orig, r in zip(signal, rec):
            self.assertAlmostEqual(orig, r, places=8)

    def test_phase_vector_length(self):
        d = EpicycleDecomposition([1.0, 2.0, 3.0, 4.0])
        self.assertEqual(len(d.phase_vector), d.n)

    def test_phase_similarity_self(self):
        d = EpicycleDecomposition([1.0, 2.0, 3.0, 4.0])
        self.assertAlmostEqual(d.phase_similarity(d), 1.0, places=10)

    def test_phase_similarity_range(self):
        d1 = EpicycleDecomposition([1.0, 0.0, -1.0, 0.0])
        d2 = EpicycleDecomposition([0.0, 1.0, 0.0, -1.0])
        sim = d1.phase_similarity(d2)
        self.assertGreaterEqual(sim, -1.0)
        self.assertLessEqual(sim, 1.0)

    def test_pack_unpack_roundtrip(self):
        signal = [1.0, 2.0, -1.0, 0.5, 0.0, -0.5, 1.5, -2.0]
        d = EpicycleDecomposition(signal)
        packed = d.pack()
        self.assertEqual(len(packed), d.n * 2)
        unpacked = EpicycleDecomposition.unpack_phases(packed)
        for orig, rec in zip(d.phases, unpacked):
            self.assertAlmostEqual(orig, rec, delta=_TAU / 65535 + 1e-6)

    def test_dominant_frequency(self):
        """Pure sine at frequency k should give dominant_frequency ≈ k."""
        n = 16
        k = 3
        signal = [math.sin(_TAU * k * j / n) for j in range(n)]
        d = EpicycleDecomposition(signal)
        self.assertIn(d.dominant_frequency, {k, n - k})

    def test_repr(self):
        d = EpicycleDecomposition([1.0, 2.0, 3.0, 4.0])
        self.assertIn("EpicycleDecomposition", repr(d))

    def test_len(self):
        d = EpicycleDecomposition([1.0, 2.0])
        self.assertEqual(len(d), d.n)


if __name__ == "__main__":
    unittest.main()
