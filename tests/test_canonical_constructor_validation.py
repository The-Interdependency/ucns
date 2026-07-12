"""Constructor invariant tests for the public ucns import surface."""

import unittest
from fractions import Fraction

from ucns import UCNSObject, UNIT


class TestPublicUCNSObjectConstructorValidation(unittest.TestCase):
    def test_rejects_mismatched_angle_and_face_lengths(self) -> None:
        with self.assertRaisesRegex(ValueError, "A_plus and F_plus must have the same length"):
            UCNSObject(
                2,
                2,
                [(Fraction(0), UNIT), (Fraction(1), UNIT)],
                [0],
            )

    def test_rejects_non_binary_face_values(self) -> None:
        with self.assertRaisesRegex(ValueError, "F_plus entries must be face bits 0 or 1"):
            UCNSObject(
                2,
                2,
                [(Fraction(0), UNIT), (Fraction(1), UNIT)],
                [0, -1],
            )

    def test_rejects_non_integer_face_values(self) -> None:
        for faces in ([0.0, 1.0], [Fraction(0), Fraction(1)]):
            with self.subTest(faces=faces):
                with self.assertRaisesRegex(
                    ValueError, "F_plus entries must be face bits 0 or 1"
                ):
                    UCNSObject(
                        2,
                        2,
                        [(Fraction(0), UNIT), (Fraction(1), UNIT)],
                        faces,
                    )

    def test_accepts_parallel_binary_faces(self) -> None:
        obj = UCNSObject(
            2,
            2,
            [(Fraction(0), UNIT), (Fraction(1), UNIT)],
            [1, 0],
        )
        self.assertEqual(obj.F_plus, [1, 0])

    def test_rejects_empty_object_sequences(self) -> None:
        with self.assertRaisesRegex(ValueError, "A_plus must be nonempty"):
            UCNSObject(1, 1, [], [])

    def test_rejects_non_positive_declared_carrier(self) -> None:
        for n_dec in (0, -1, -4):
            with self.subTest(n_dec=n_dec):
                with self.assertRaisesRegex(
                    ValueError, "n_dec must be a positive integer"
                ):
                    UCNSObject(n_dec, 1, [(Fraction(0), UNIT)], [0])

    def test_rejects_non_integral_declared_carrier(self) -> None:
        for n_dec in (2.0, Fraction(2), "2"):
            with self.subTest(n_dec=n_dec):
                with self.assertRaisesRegex(
                    ValueError, "n_dec must be a positive integer"
                ):
                    UCNSObject(n_dec, 1, [(Fraction(0), UNIT)], [0])

    def test_rejects_non_positive_supplied_intrinsic_carrier(self) -> None:
        for n_min in (0, -2):
            with self.subTest(n_min=n_min):
                with self.assertRaisesRegex(
                    ValueError, "n_min must be a positive integer"
                ):
                    UCNSObject(2, n_min, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])

    def test_supplied_intrinsic_carrier_is_recomputed_not_trusted(self) -> None:
        # A wrong-but-positive n_min is repaired by normalization.
        obj = UCNSObject(2, 1, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        self.assertEqual(obj.n_min, 2)

    def test_rejects_declared_carrier_not_multiple_of_intrinsic(self) -> None:
        with self.assertRaisesRegex(ValueError, "not multiple of n_min"):
            UCNSObject(3, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])

    def test_rejects_non_ucns_recursive_payload_types(self) -> None:
        for payload in (object(), 7, "S2", [(Fraction(0), None)], {"cells": []}):
            with self.subTest(payload=payload):
                with self.assertRaisesRegex(
                    TypeError, "payloads must be UCNSObject or None"
                ):
                    UCNSObject(2, 2, [(Fraction(0), payload), (Fraction(1), UNIT)], [0, 0])

    def test_integer_angles_are_coerced_to_exact_fractions(self) -> None:
        # The documented int-angle contract must actually construct:
        # normalization's circle-fraction arithmetic needs exact types.
        from_ints = UCNSObject(2, 2, [(0, UNIT), (1, UNIT)], [0, 0])
        from_fractions = UCNSObject(
            2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0]
        )
        self.assertEqual(from_ints, from_fractions)
        self.assertEqual(from_ints.n_min, 2)
        for angle, _ in from_ints.A_plus:
            self.assertIsInstance(angle, Fraction)

    def test_rejects_inexact_angle_types(self) -> None:
        for angle in (0.5, "1", True, None):
            with self.subTest(angle=angle):
                with self.assertRaisesRegex(
                    TypeError, "angles must be Fraction or plain integers"
                ):
                    UCNSObject(2, 2, [(Fraction(0), UNIT), (angle, UNIT)], [0, 0])

    def test_accepts_recursive_ucns_payloads(self) -> None:
        inner = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        obj = UCNSObject(2, 2, [(Fraction(0), inner), (Fraction(1), UNIT)], [0, 0])
        payload = obj.A_plus[0][1]
        self.assertIsInstance(payload, UCNSObject)
        self.assertEqual(payload, inner)
        # Payloads are deep-copied: the constructed object is isolated
        # from later mutation of the input payload.
        self.assertIsNot(payload, inner)


if __name__ == "__main__":
    unittest.main()
