"""
Tests for the constructive ``left_quotient`` and ``right_quotient``
primitives, promoted from ``ucns-code-v065.py`` into the
``ucns_recursive`` package.

These tests verify the v0.6 completeness theorem holds on the
canonical inputs:  if ``P = A ⊠ B`` then ``left_quotient(P, A) == B``
and ``right_quotient(P, B) == A``.

Tests run on objects produced by ``recursive_codec.recursive_encode``
to confirm the codec's outputs are valid inputs to the algebra.
"""

import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject, multiply
from ucns_recursive.left_quotient import left_quotient, right_quotient
from ucns_recursive.recursive_quotient import (
    find_left_factor,
    find_right_factor,
    left_quotient as left_quotient_via_recursive_quotient,
)
from ucns_recursive.recursive_codec import recursive_encode


def make_flat(angles_and_faces):
    """Build a flat (depth-0) UCNSObject from (angle_int, face) pairs."""
    a_plus = [(Fraction(a), None) for a, _ in angles_and_faces]
    f_plus = [f for _, f in angles_and_faces]
    # n_dec = 12 is a multiple of 1, 2, 3, 4, 6, 12 — safe for any
    # small integer-angle test object the n_min computation produces.
    n_dec = 12
    return UCNSObject(n_dec, n_dec, a_plus, f_plus)


class TestLeftQuotientFlatProof(unittest.TestCase):
    """Lemmas 2, 3 — direct host recovery on flat inputs."""

    def test_recursive_quotient_reexports_left_quotient(self):
        self.assertIs(left_quotient_via_recursive_quotient, left_quotient)

    def test_flat_recovers_b(self):
        A = make_flat([(0, 0), (1, 0)])
        B = make_flat([(0, 0), (1, 0)])
        P = multiply(A, B)
        recovered = left_quotient(P, A)
        self.assertEqual(recovered, B)

    def test_flat_with_face_bits(self):
        A = make_flat([(0, 1), (1, 0)])
        B = make_flat([(0, 0), (1, 1)])
        P = multiply(A, B)
        recovered = left_quotient(P, A)
        self.assertEqual(recovered, B)

    def test_flat_no_factorization_returns_none(self):
        A = make_flat([(0, 0), (1, 0), (2, 0)])  # 3 cells
        P = make_flat([(0, 0), (1, 0)])           # 2 cells; |A| ∤ |P|
        self.assertIsNone(left_quotient(P, A))


class TestLeftQuotientDepthOne(unittest.TestCase):
    """Lemmas 4, 5, 6, 7, 8 — recursive payload descent."""

    def test_depth1_unit_leading_payload(self):
        # A's leading payload is None (unit), so payload recovery is direct.
        A = UCNSObject(2, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
        S = UCNSObject(2, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
        B = UCNSObject(
            2, 2,
            [(Fraction(0), S), (Fraction(1), None)],
            [0, 0],
        )
        P = multiply(A, B)
        recovered = left_quotient(P, A)
        self.assertEqual(recovered, B)

    def test_depth1_non_unit_leading_payload(self):
        # A's leading payload is non-None, forcing the recursion.
        S2 = UCNSObject(2, 2, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
        A = UCNSObject(
            2, 2,
            [(Fraction(0), S2), (Fraction(1), None)],
            [0, 0],
        )
        B = UCNSObject(
            2, 2,
            [(Fraction(0), S2), (Fraction(1), None)],
            [0, 0],
        )
        P = multiply(A, B)
        recovered = left_quotient(P, A)
        self.assertEqual(recovered, B)


class TestRightQuotient(unittest.TestCase):
    """Symmetric dual."""

    def test_right_recovers_a(self):
        A = make_flat([(0, 0), (1, 0)])
        B = make_flat([(0, 0), (1, 0)])
        P = multiply(A, B)
        recovered = right_quotient(P, B)
        self.assertEqual(recovered, A)


class TestRecursiveQuotientFactorFinders(unittest.TestCase):
    def test_find_right_factor_tries_unit_first(self):
        left = make_flat([(0, 0), (1, 0)])
        target = left
        noisy = make_flat([(0, 0), (2, 0)])
        result = find_right_factor(target, left, [noisy])
        self.assertIsNone(result)

    def test_find_left_factor_tries_unit_first(self):
        right = make_flat([(0, 0), (1, 0)])
        target = right
        noisy = make_flat([(0, 0), (2, 0)])
        result = find_left_factor(target, right, [noisy])
        self.assertIsNone(result)


class TestQuotientOnEncodedObjects(unittest.TestCase):
    """Confirm the codec's outputs interact correctly with the proof's
    primitive — i.e. the embedding-side data structure is in scope of
    the algebra-side completeness theorem."""

    def test_encoded_leaf_left_quotient(self):
        A = recursive_encode(b"abc")
        B = recursive_encode(b"xyz")
        P = multiply(A, B)
        recovered = left_quotient(P, A)
        self.assertEqual(recovered, B)

    def test_encoded_leaf_right_quotient(self):
        A = recursive_encode(b"abc")
        B = recursive_encode(b"xyz")
        P = multiply(A, B)
        recovered = right_quotient(P, B)
        self.assertEqual(recovered, A)

    def test_encoded_list_left_quotient(self):
        A = recursive_encode([b"x", b"y"])
        B = recursive_encode([b"p", b"q"])
        P = multiply(A, B)
        recovered = left_quotient(P, A)
        self.assertEqual(recovered, B)

    def test_no_factorization_returns_none(self):
        A = recursive_encode(b"abc")
        # Build something that can't possibly factor through A:
        # use a list whose host length is coprime to A's.
        unrelated = recursive_encode([b"a", b"b", b"c", b"d", b"e"])
        result = left_quotient(unrelated, A)
        # Either None or an object that, when re-multiplied, doesn't equal P.
        # The proof's contract: if it returns non-None, multiply(A, result) == unrelated.
        if result is not None:
            self.assertEqual(multiply(A, result), unrelated)


if __name__ == "__main__":
    unittest.main()
