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
        self.assertEqual(obj.F_plus, (1, 0))  # canonical tuples (immutable value model)


if __name__ == "__main__":
    unittest.main()
