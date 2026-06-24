"""
Tests for ucns_recursive.geometry_bridge.

Verifies the three proved homomorphism invariants:
    r:       log-depth additive under multiply
    theta:   circular mean angle additive (mod 4π) under multiply (non-degenerate)
    (z, w):  two-bit chirality correct under multiply (XOR outer-product rule)

Also tests GeometricPoint, compose, homomorphism_check, check_injectivity.
"""

import math
import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject, multiply
from ucns_recursive.geometry_bridge import (
    GeometricPoint,
    HomomorphismResult,
    check_injectivity,
    compose,
    homomorphism_check,
    ucns_a_to_g,
)

_TAU4 = 4.0 * math.pi
_TOL = 1e-9


def flat(angles_and_faces):
    a_plus = [(Fraction(a), None) for a, _ in angles_and_faces]
    f_plus = [f for _, f in angles_and_faces]
    return UCNSObject(12, 12, a_plus, f_plus)


def angle_close(a, b, tol=_TOL):
    diff = abs(a - b) % _TAU4
    return min(diff, _TAU4 - diff) < tol


class TestGeometricPoint(unittest.TestCase):

    def test_basic_construction(self):
        p = GeometricPoint(r=1.0, theta=math.pi, z=0, w=1)
        self.assertAlmostEqual(p.r, 1.0)
        self.assertAlmostEqual(p.theta, math.pi)
        self.assertEqual(p.z, 0)
        self.assertEqual(p.w, 1)

    def test_theta_normalised_mod_4pi(self):
        p = GeometricPoint(r=0.0, theta=5 * math.pi, z=0, w=0)
        self.assertTrue(angle_close(p.theta, math.pi))

    def test_theta_none_degenerate(self):
        p = GeometricPoint(r=0.0, theta=None, z=1, w=0)
        self.assertTrue(p.is_degenerate)

    def test_invalid_z(self):
        with self.assertRaises(ValueError):
            GeometricPoint(r=1.0, theta=0.0, z=2, w=0)

    def test_invalid_w(self):
        with self.assertRaises(ValueError):
            GeometricPoint(r=1.0, theta=0.0, z=0, w=2)

    def test_invalid_r(self):
        with self.assertRaises(ValueError):
            GeometricPoint(r=-1.0, theta=0.0, z=0, w=0)

    def test_chirality_property(self):
        p = GeometricPoint(r=0.0, theta=0.0, z=0, w=0)
        self.assertEqual(p.chirality, 1)
        q = GeometricPoint(r=0.0, theta=0.0, z=1, w=0)
        self.assertEqual(q.chirality, -1)

    def test_equality(self):
        p = GeometricPoint(r=1.0, theta=math.pi, z=0, w=1)
        q = GeometricPoint(r=1.0, theta=math.pi + 1e-11, z=0, w=1)
        self.assertEqual(p, q)

    def test_unhashable(self):
        p = GeometricPoint(r=1.0, theta=math.pi, z=0, w=1)
        with self.assertRaises(TypeError):
            hash(p)

    def test_inequality_z(self):
        p = GeometricPoint(r=1.0, theta=math.pi, z=0, w=0)
        q = GeometricPoint(r=1.0, theta=math.pi, z=1, w=0)
        self.assertNotEqual(p, q)

    def test_inequality_w(self):
        p = GeometricPoint(r=1.0, theta=math.pi, z=0, w=0)
        q = GeometricPoint(r=1.0, theta=math.pi, z=0, w=1)
        self.assertNotEqual(p, q)


class TestRInvariant(unittest.TestCase):

    def _check_r(self, a, b):
        ab = multiply(a, b)
        result = homomorphism_check(a, b, multiply_fn=multiply)
        self.assertTrue(result.r_match, msg=f"r mismatch: {result}")

    def test_r_2x2(self):
        self._check_r(flat([(0,0),(1,0)]), flat([(0,0),(1,0)]))

    def test_r_2x3(self):
        self._check_r(flat([(0,0),(1,0)]), flat([(0,0),(1,1),(2,0)]))

    def test_r_3x3(self):
        self._check_r(flat([(0,0),(2,0),(1,0)]), flat([(0,0),(1,1),(3,0)]))

    def test_r_4x2(self):
        self._check_r(flat([(0,0),(1,0),(2,1),(3,0)]), flat([(0,0),(2,1)]))

    def test_r_is_log_len(self):
        obj = flat([(0,0),(1,0),(2,0)])
        self.assertAlmostEqual(ucns_a_to_g(obj).r, math.log(3))

    def test_r_single_element(self):
        obj = flat([(0,0)])
        self.assertAlmostEqual(ucns_a_to_g(obj).r, 0.0)  # log(1) = 0


class TestZWInvariant(unittest.TestCase):

    def _check_zw(self, a, b):
        result = homomorphism_check(a, b, multiply_fn=multiply)
        self.assertTrue(result.zw_match, msg=f"zw mismatch: {result}")

    def test_all_zero_faces(self):
        self._check_zw(flat([(0,0),(1,0)]), flat([(0,0),(1,0)]))

    def test_one_flip_in_b(self):
        self._check_zw(flat([(0,0),(1,0)]), flat([(0,0),(2,1)]))

    def test_flip_in_both(self):
        self._check_zw(flat([(0,1),(1,0)]), flat([(0,0),(2,1)]))

    def test_multiple_flips(self):
        self._check_zw(flat([(0,0),(1,1),(2,0)]), flat([(0,1),(1,0),(2,1)]))

    def test_3x2(self):
        self._check_zw(flat([(0,0),(2,0),(1,0)]), flat([(0,0),(1,1)]))

    def test_compose_z_formula(self):
        # z(AB) = (z_A * w_B + w_A * z_B) mod 2
        p = GeometricPoint(r=0.0, theta=0.0, z=0, w=1)  # len odd, no flips
        q = GeometricPoint(r=0.0, theta=0.0, z=1, w=0)  # len even, one flip
        c = compose(p, q)
        expected_z = (0 * 0 + 1 * 1) % 2  # = 1
        expected_w = (1 * 0) % 2           # = 0
        self.assertEqual(c.z, expected_z)
        self.assertEqual(c.w, expected_w)

    def test_compose_w_multiplicative(self):
        # w(AB) = w_A * w_B mod 2: odd * odd = odd, else even
        p = GeometricPoint(r=0.0, theta=0.0, z=0, w=1)
        q = GeometricPoint(r=0.0, theta=0.0, z=0, w=1)
        c = compose(p, q)
        self.assertEqual(c.w, 1)  # odd * odd = odd
        q2 = GeometricPoint(r=0.0, theta=0.0, z=0, w=0)
        c2 = compose(p, q2)
        self.assertEqual(c2.w, 0)  # odd * even = even


class TestThetaInvariant(unittest.TestCase):

    def _check_theta(self, a, b):
        result = homomorphism_check(a, b, multiply_fn=multiply)
        if result.degenerate:
            return  # degenerate theta is well-handled; not a failure
        self.assertTrue(result.theta_match, msg=f"theta mismatch: {result}")

    def test_theta_simple(self):
        self._check_theta(flat([(0,0),(1,0)]), flat([(0,0),(1,0)]))

    def test_theta_2x2_different(self):
        self._check_theta(flat([(0,0),(1,0)]), flat([(0,0),(2,1)]))

    def test_theta_3x2(self):
        self._check_theta(flat([(0,0),(2,0),(1,0)]), flat([(0,0),(1,1)]))

    def test_theta_3x3(self):
        self._check_theta(flat([(0,0),(3,0),(1,0)]), flat([(0,0),(2,1),(1,0)]))

    def test_theta_with_faces(self):
        self._check_theta(flat([(0,1),(2,0),(1,1)]), flat([(0,0),(1,1),(3,0)]))

    def test_theta_degenerate_flagged(self):
        # Angles 0 and 2 (opposite on spinor circle) → mean vector cancels
        obj = flat([(0,0),(2,0)])
        g = ucns_a_to_g(obj)
        self.assertTrue(g.is_degenerate)

    def test_theta_in_range(self):
        obj = flat([(0,0),(3,0),(1,0)])
        g = ucns_a_to_g(obj)
        if not g.is_degenerate:
            self.assertGreaterEqual(g.theta, 0.0)
            self.assertLess(g.theta, _TAU4)

    def test_theta_compose_mod_4pi(self):
        p = GeometricPoint(r=0.0, theta=3 * math.pi, z=0, w=0)
        q = GeometricPoint(r=0.0, theta=2 * math.pi, z=0, w=0)
        c = compose(p, q)
        self.assertTrue(angle_close(c.theta, math.pi))  # 5π mod 4π = π


class TestHomomorphismCheck(unittest.TestCase):

    def test_holds_simple(self):
        a = flat([(0,0),(1,0)])
        b = flat([(0,0),(1,0)])
        result = homomorphism_check(a, b, multiply_fn=multiply)
        self.assertTrue(result.holds or result.degenerate, msg=repr(result))

    def test_holds_with_default_multiply(self):
        a = flat([(0, 0), (1, 0)])
        b = flat([(0, 0), (1, 0)])
        result = homomorphism_check(a, b)
        self.assertTrue(result.holds or result.degenerate, msg=repr(result))

    def test_holds_with_faces(self):
        a = flat([(0,1),(1,0)])
        b = flat([(0,0),(2,1)])
        result = homomorphism_check(a, b, multiply_fn=multiply)
        self.assertTrue(result.holds or result.degenerate, msg=repr(result))

    def test_result_fields(self):
        a = flat([(0,0),(1,0)])
        b = flat([(0,0),(2,0)])
        result = homomorphism_check(a, b, multiply_fn=multiply)
        self.assertIsInstance(result.lhs, GeometricPoint)
        self.assertIsInstance(result.rhs, GeometricPoint)
        self.assertIsInstance(result.r_match, bool)
        self.assertIsInstance(result.zw_match, bool)

    def test_bulk_random(self):
        """Homomorphism holds across 200 random flat object pairs."""
        import random
        rng = random.Random(42)
        failures = []
        for _ in range(200):
            n_a = rng.randint(2, 4)
            n_b = rng.randint(2, 4)
            af = [(rng.randint(0, 3), rng.randint(0, 1)) for _ in range(n_a)]
            bf = [(rng.randint(0, 3), rng.randint(0, 1)) for _ in range(n_b)]
            a = flat(af)
            b = flat(bf)
            result = homomorphism_check(a, b, multiply_fn=multiply)
            if not result.degenerate and not result.holds:
                failures.append(result)
        self.assertEqual(len(failures), 0,
            msg=f"{len(failures)} non-degenerate failures: {failures[:3]}")


class TestCompose(unittest.TestCase):

    def test_r_additive(self):
        p = GeometricPoint(r=1.0, theta=math.pi, z=0, w=0)
        q = GeometricPoint(r=2.0, theta=math.pi, z=0, w=0)
        c = compose(p, q)
        self.assertAlmostEqual(c.r, 3.0)

    def test_theta_additive_mod_4pi(self):
        p = GeometricPoint(r=0.0, theta=3 * math.pi, z=0, w=0)
        q = GeometricPoint(r=0.0, theta=2 * math.pi, z=0, w=0)
        c = compose(p, q)
        self.assertTrue(angle_close(c.theta, math.pi))

    def test_degenerate_propagates(self):
        p = GeometricPoint(r=1.0, theta=None, z=0, w=0)
        q = GeometricPoint(r=1.0, theta=math.pi, z=0, w=0)
        c = compose(p, q)
        self.assertTrue(c.is_degenerate)


class TestCheckInjectivity(unittest.TestCase):

    def test_single_object_injective(self):
        result = check_injectivity([flat([(0,0),(1,0)])])
        self.assertTrue(result["injective"])

    def test_identical_objects_collide(self):
        a = flat([(0,0),(1,0)])
        b = flat([(0,0),(1,0)])
        result = check_injectivity([a, b])
        self.assertFalse(result["injective"])
        self.assertEqual(len(result["collisions"]), 1)

    def test_distinct_objects_result_structure(self):
        objects = [flat([(0,0),(1,0)]), flat([(0,0),(2,0)]), flat([(0,0),(3,0)])]
        result = check_injectivity(objects)
        self.assertIn("injective", result)
        self.assertIn("total", result)
        self.assertIn("collisions", result)


if __name__ == "__main__":
    unittest.main()
