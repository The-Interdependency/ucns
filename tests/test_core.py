"""Tests for ucns.core – Unit Circle Number arithmetic."""

import math
import struct
import unittest

from ucns.core import UCN, TAU


class TestUCNConstruction(unittest.TestCase):
    def test_theta_normalised_positive(self):
        u = UCN(3 * TAU + 1.0)
        self.assertAlmostEqual(u.theta, 1.0, places=10)

    def test_theta_normalised_negative(self):
        u = UCN(-0.5)
        self.assertAlmostEqual(u.theta, TAU - 0.5, places=10)

    def test_theta_zero(self):
        self.assertAlmostEqual(UCN(0.0).theta, 0.0)

    def test_theta_tau_wraps_to_zero(self):
        self.assertAlmostEqual(UCN(TAU).theta, 0.0, places=10)

    def test_from_complex_unit_circle(self):
        import cmath
        z = cmath.exp(1j * 1.23)
        u = UCN.from_complex(z)
        self.assertAlmostEqual(u.theta, 1.23, places=10)

    def test_from_complex_non_unit(self):
        # phase is preserved regardless of magnitude
        u = UCN.from_complex(2.0 + 2.0j)
        self.assertAlmostEqual(u.theta, math.pi / 4, places=10)

    def test_from_real_midpoint(self):
        u = UCN.from_real(0.0, -1.0, 1.0)
        self.assertAlmostEqual(u.theta, TAU / 2, places=10)

    def test_from_real_lo(self):
        u = UCN.from_real(-1.0, -1.0, 1.0)
        self.assertAlmostEqual(u.theta, 0.0, places=10)

    def test_from_real_hi(self):
        u = UCN.from_real(1.0, -1.0, 1.0)
        # t=1.0 → theta=τ, which normalises to 0
        self.assertAlmostEqual(u.theta, 0.0, places=10)

    def test_from_real_clamping(self):
        u_lo = UCN.from_real(-999.0, -1.0, 1.0)
        u_hi = UCN.from_real(999.0, -1.0, 1.0)
        self.assertAlmostEqual(u_lo.theta, 0.0, places=10)
        self.assertAlmostEqual(u_hi.theta, 0.0, places=10)  # 1.0 wraps to 0

    def test_from_real_equal_lo_hi_raises(self):
        with self.assertRaises(ValueError):
            UCN.from_real(0.0, lo=1.0, hi=1.0)


class TestUCNProperties(unittest.TestCase):
    def test_real_imag(self):
        theta = math.pi / 3
        u = UCN(theta)
        self.assertAlmostEqual(u.real, math.cos(theta))
        self.assertAlmostEqual(u.imag, math.sin(theta))

    def test_complex_on_unit_circle(self):
        u = UCN(1.1)
        self.assertAlmostEqual(abs(u.complex), 1.0, places=12)


class TestUCNArithmetic(unittest.TestCase):
    def test_multiplication_adds_angles(self):
        u = UCN(1.0)
        v = UCN(2.0)
        self.assertAlmostEqual((u * v).theta, 3.0, places=10)

    def test_multiplication_wraps(self):
        u = UCN(TAU - 0.1)
        v = UCN(0.2)
        expected = (TAU - 0.1 + 0.2) % TAU
        self.assertAlmostEqual((u * v).theta, expected, places=10)

    def test_division_subtracts_angles(self):
        u = UCN(3.0)
        v = UCN(1.0)
        self.assertAlmostEqual((u / v).theta, 2.0, places=10)

    def test_conjugate(self):
        u = UCN(1.0)
        c = u.conjugate()
        self.assertAlmostEqual(c.theta, TAU - 1.0, places=10)

    def test_conjugate_of_zero(self):
        u = UCN(0.0)
        self.assertAlmostEqual(u.conjugate().theta, 0.0, places=10)

    def test_mul_div_roundtrip(self):
        u = UCN(1.5)
        v = UCN(0.7)
        self.assertAlmostEqual(((u * v) / v).theta, u.theta, places=10)

    def test_identity_element(self):
        u = UCN(1.23)
        identity = UCN(0.0)
        self.assertAlmostEqual((u * identity).theta, u.theta, places=10)


class TestUCNMetrics(unittest.TestCase):
    def test_dot_identical(self):
        u = UCN(1.0)
        self.assertAlmostEqual(u.dot(u), 1.0, places=10)

    def test_dot_opposite(self):
        u = UCN(0.0)
        v = UCN(math.pi)
        self.assertAlmostEqual(u.dot(v), -1.0, places=10)

    def test_dot_quarter_turn(self):
        u = UCN(0.0)
        v = UCN(math.pi / 2)
        self.assertAlmostEqual(u.dot(v), 0.0, places=10)

    def test_arc_distance_same(self):
        u = UCN(1.0)
        self.assertAlmostEqual(u.arc_distance(u), 0.0, places=10)

    def test_arc_distance_half_circle(self):
        u = UCN(0.0)
        v = UCN(math.pi)
        self.assertAlmostEqual(u.arc_distance(v), math.pi, places=10)

    def test_arc_distance_symmetry(self):
        u = UCN(0.3)
        v = UCN(2.7)
        self.assertAlmostEqual(u.arc_distance(v), v.arc_distance(u), places=10)

    def test_arc_distance_short_arc(self):
        u = UCN(0.1)
        v = UCN(TAU - 0.1)
        self.assertAlmostEqual(u.arc_distance(v), 0.2, places=10)


class TestUCNSerialisation(unittest.TestCase):
    def test_int16_roundtrip(self):
        for theta in [0.0, 1.0, math.pi, TAU * 0.75]:
            u = UCN(theta)
            v = UCN.from_int16(u.to_int16())
            self.assertAlmostEqual(u.theta, v.theta, delta=TAU / 65535 + 1e-9)

    def test_bytes_roundtrip(self):
        u = UCN(2.718)
        v = UCN.from_bytes(u.to_bytes())
        self.assertAlmostEqual(u.theta, v.theta, delta=TAU / 65535 + 1e-9)

    def test_bytes_length(self):
        self.assertEqual(len(UCN(1.0).to_bytes()), 2)


class TestUCNDunder(unittest.TestCase):
    def test_repr(self):
        r = repr(UCN(1.23456))
        self.assertIn("UCN", r)
        self.assertIn("1.23456", r)

    def test_equality(self):
        self.assertEqual(UCN(1.0), UCN(1.0 + TAU))

    def test_inequality(self):
        self.assertNotEqual(UCN(1.0), UCN(2.0))

    def test_hash_consistent_with_eq(self):
        self.assertEqual(hash(UCN(1.0)), hash(UCN(1.0 + TAU)))

    def test_float_conversion(self):
        u = UCN(1.23)
        self.assertAlmostEqual(float(u), 1.23, places=10)

    def test_lt(self):
        self.assertLess(UCN(0.5), UCN(1.5))


if __name__ == "__main__":
    unittest.main()
