"""Tests for ucns.similarity – metric functions."""

import math
import unittest

from ucns.similarity import arc_distance, hyperbolic_cosine, phase_cosine, top_k_overlap

_TAU = 2.0 * math.pi


class TestPhaseCosine(unittest.TestCase):
    def test_identical_gives_one(self):
        a = [0.1, 0.5, 1.2, 2.0]
        self.assertAlmostEqual(phase_cosine(a, a), 1.0, places=12)

    def test_opposite_gives_minus_one(self):
        a = [0.0]
        b = [math.pi]
        self.assertAlmostEqual(phase_cosine(a, b), -1.0, places=12)

    def test_quarter_turn_gives_zero(self):
        a = [0.0]
        b = [math.pi / 2]
        self.assertAlmostEqual(phase_cosine(a, b), 0.0, places=12)

    def test_symmetric(self):
        a = [0.1, 0.5, 1.0]
        b = [0.3, 0.7, 0.2]
        self.assertAlmostEqual(phase_cosine(a, b), phase_cosine(b, a), places=12)

    def test_empty_returns_zero(self):
        self.assertEqual(phase_cosine([], []), 0.0)

    def test_different_lengths_raises(self):
        with self.assertRaises(ValueError):
            phase_cosine([1.0], [1.0, 2.0])


class TestArcDistance(unittest.TestCase):
    def test_identical_gives_zero(self):
        a = [0.5, 1.0, 2.0]
        self.assertAlmostEqual(arc_distance(a, a), 0.0, places=12)

    def test_half_circle_gives_one(self):
        a = [0.0]
        b = [math.pi]
        self.assertAlmostEqual(arc_distance(a, b), 1.0, places=12)

    def test_short_arc_used(self):
        """Going 0 → 2π-0.1 should use short arc 0.1, not 2π-0.1."""
        a = [0.0]
        b = [_TAU - 0.1]
        result = arc_distance(a, b)
        self.assertAlmostEqual(result, 0.1 / math.pi, places=10)

    def test_symmetric(self):
        a = [0.3, 1.1, 2.5]
        b = [1.0, 0.5, 0.1]
        self.assertAlmostEqual(arc_distance(a, b), arc_distance(b, a), places=12)

    def test_result_in_range(self):
        import random
        rng = random.Random(42)
        a = [rng.uniform(0, _TAU) for _ in range(20)]
        b = [rng.uniform(0, _TAU) for _ in range(20)]
        result = arc_distance(a, b)
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 1.0)

    def test_empty_returns_zero(self):
        self.assertEqual(arc_distance([], []), 0.0)

    def test_different_lengths_raises(self):
        with self.assertRaises(ValueError):
            arc_distance([1.0], [1.0, 2.0])


class TestHyperbolicCosine(unittest.TestCase):
    def test_identical_gives_one(self):
        a = [0.1, 0.5, 1.2]
        self.assertAlmostEqual(hyperbolic_cosine(a, a), 1.0, places=10)

    def test_result_in_range(self):
        a = [0.0, 1.0, 2.0, 3.0]
        b = [math.pi, 0.5, 1.5, 2.5]
        result = hyperbolic_cosine(a, b)
        self.assertGreaterEqual(result, -1.0)
        self.assertLessEqual(result, 1.0)

    def test_symmetric(self):
        a = [0.3, 1.1]
        b = [1.0, 0.5]
        self.assertAlmostEqual(
            hyperbolic_cosine(a, b),
            hyperbolic_cosine(b, a),
            places=12,
        )

    def test_invalid_radius_raises(self):
        with self.assertRaises(ValueError):
            hyperbolic_cosine([0.0], [0.0], radius=0.0)
        with self.assertRaises(ValueError):
            hyperbolic_cosine([0.0], [0.0], radius=1.0)

    def test_empty_returns_zero(self):
        self.assertEqual(hyperbolic_cosine([], []), 0.0)

    def test_different_lengths_raises(self):
        with self.assertRaises(ValueError):
            hyperbolic_cosine([1.0], [1.0, 2.0])


class TestTopKOverlap(unittest.TestCase):
    def test_identical_amplitudes_gives_one(self):
        a = [3.0, 1.0, 2.0, 0.5]
        self.assertAlmostEqual(top_k_overlap(a, a, k=2), 1.0, places=12)

    def test_completely_different_gives_zero(self):
        a = [1.0, 0.0, 0.0, 0.0]
        b = [0.0, 0.0, 0.0, 1.0]
        self.assertAlmostEqual(top_k_overlap(a, b, k=1), 0.0, places=12)

    def test_result_in_range(self):
        a = [3.0, 1.0, 2.0, 4.0]
        b = [1.0, 4.0, 0.5, 2.0]
        result = top_k_overlap(a, b, k=2)
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 1.0)

    def test_k_larger_than_n(self):
        """k is clamped to len(amplitudes)."""
        a = [1.0, 2.0]
        b = [2.0, 1.0]
        # with k=100 (clamped to 2), both sets are the same → overlap = 1
        self.assertAlmostEqual(top_k_overlap(a, b, k=100), 1.0, places=12)

    def test_different_lengths_raises(self):
        with self.assertRaises(ValueError):
            top_k_overlap([1.0], [1.0, 2.0], k=1)


if __name__ == "__main__":
    unittest.main()
