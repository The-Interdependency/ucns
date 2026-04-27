"""Tests for ucns.mobius – Möbius disk transformations."""

import cmath
import math
import unittest

from ucns.mobius import (
    MobiusTransform,
    circle_to_disk,
    disk_to_circle,
    poincare_distance,
)

_TAU = 2.0 * math.pi


class TestMobiusConstruction(unittest.TestCase):
    def test_valid_construction(self):
        t = MobiusTransform(0.5 + 0j)
        self.assertEqual(t.a, 0.5 + 0j)

    def test_a_on_boundary_raises(self):
        with self.assertRaises(ValueError):
            MobiusTransform(1.0 + 0j)

    def test_a_outside_disk_raises(self):
        with self.assertRaises(ValueError):
            MobiusTransform(1.5 + 0j)

    def test_phi_normalised(self):
        t = MobiusTransform(0j, phi=_TAU + 1.0)
        self.assertAlmostEqual(t.phi, 1.0, places=10)


class TestMobiusEvaluation(unittest.TestCase):
    def test_maps_a_to_zero(self):
        a = 0.3 + 0.2j
        t = MobiusTransform(a)
        result = t(a)
        self.assertAlmostEqual(abs(result), 0.0, places=12)

    def test_maps_zero_to_minus_a_rotated(self):
        a = 0.4 + 0j
        phi = 0.5
        t = MobiusTransform(a, phi=phi)
        expected = cmath.exp(1j * phi) * (-a)
        self.assertAlmostEqual(t(0j), expected, places=12)

    def test_preserves_unit_circle(self):
        """Points on ∂D should map to ∂D."""
        a = 0.3 + 0.1j
        t = MobiusTransform(a, phi=0.7)
        for angle in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]:
            z = cmath.exp(1j * angle)
            w = t(z)
            self.assertAlmostEqual(abs(w), 1.0, places=10,
                                   msg=f"Unit circle not preserved at angle={angle}")

    def test_maps_disk_to_disk(self):
        """Interior points should stay inside D."""
        a = 0.2 - 0.3j
        t = MobiusTransform(a, phi=1.2)
        for z in [0.1 + 0j, 0.5j, -0.4 - 0.4j]:
            self.assertLess(abs(t(z)), 1.0)


class TestMobiusInverse(unittest.TestCase):
    def test_inverse_roundtrip(self):
        a = 0.35 + 0.15j
        t = MobiusTransform(a, phi=0.9)
        t_inv = t.inverse()
        for z in [0j, 0.1 + 0.2j, -0.3 + 0.0j]:
            self.assertAlmostEqual(t_inv(t(z)), z, places=10)

    def test_identity_transform(self):
        t = MobiusTransform(0j, phi=0.0)
        for z in [0.3 + 0j, -0.5j, 0.1 + 0.1j]:
            self.assertAlmostEqual(t(z), z, places=12)


class TestPoincareDistance(unittest.TestCase):
    def test_distance_zero_with_itself(self):
        z = 0.3 + 0.2j
        self.assertAlmostEqual(poincare_distance(z, z), 0.0, places=12)

    def test_distance_positive(self):
        d = poincare_distance(0.1 + 0j, -0.1 + 0j)
        self.assertGreater(d, 0.0)

    def test_distance_symmetric(self):
        z = 0.2 + 0.1j
        w = -0.3 + 0.15j
        self.assertAlmostEqual(poincare_distance(z, w), poincare_distance(w, z), places=12)

    def test_distance_grows_near_boundary(self):
        """Points near the boundary should be "far" from the origin."""
        d_near = poincare_distance(0j, 0.1 + 0j)
        d_far = poincare_distance(0j, 0.99 + 0j)
        self.assertGreater(d_far, d_near)

    def test_outside_disk_raises(self):
        with self.assertRaises(ValueError):
            poincare_distance(1.5 + 0j, 0j)

    def test_on_boundary_raises(self):
        with self.assertRaises(ValueError):
            poincare_distance(1.0 + 0j, 0j)

    def test_mobius_isometry(self):
        """Möbius transform must preserve hyperbolic distance."""
        z = 0.3 + 0.1j
        w = -0.2 + 0.4j
        t = MobiusTransform(0.1 + 0.05j, phi=0.3)
        d_before = poincare_distance(z, w)
        d_after = poincare_distance(t(z), t(w))
        self.assertAlmostEqual(d_before, d_after, places=8)


class TestDiskCircleProjection(unittest.TestCase):
    def test_disk_to_circle_angle(self):
        theta = 1.2
        z = 0.7 * cmath.exp(1j * theta)
        self.assertAlmostEqual(disk_to_circle(z), theta, places=10)

    def test_disk_to_circle_zero(self):
        self.assertAlmostEqual(disk_to_circle(0j), 0.0, places=10)

    def test_circle_to_disk_modulus(self):
        z = circle_to_disk(1.0, r=0.5)
        self.assertAlmostEqual(abs(z), 0.5, places=12)

    def test_circle_to_disk_angle(self):
        theta = 2.5
        z = circle_to_disk(theta, r=0.3)
        self.assertAlmostEqual(cmath.phase(z), theta, places=10)

    def test_circle_to_disk_invalid_radius(self):
        with self.assertRaises(ValueError):
            circle_to_disk(1.0, r=0.0)
        with self.assertRaises(ValueError):
            circle_to_disk(1.0, r=1.0)


if __name__ == "__main__":
    unittest.main()
