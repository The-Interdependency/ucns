"""Constructor invariant tests for the recursive UCNS import surface."""

import unittest
from fractions import Fraction

from ucns_recursive.canonical import UCNSObject

UNIT = None


class TestUCNSObjectConstructorValidation(unittest.TestCase):
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
                [0, 2],
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
            [0, 1],
        )
        self.assertEqual(obj.F_plus, [0, 1])

    def test_rejects_empty_object_sequences(self) -> None:
        with self.assertRaisesRegex(ValueError, "A_plus must be nonempty"):
            UCNSObject(1, 1, [], [])

    def test_rejects_non_positive_declared_carrier(self) -> None:
        for n_dec in (0, -1):
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

    def test_rejects_non_ucns_recursive_payload_types(self) -> None:
        with self.assertRaisesRegex(TypeError, "payloads must be UCNSObject or None"):
            UCNSObject(2, 2, [(Fraction(0), object()), (Fraction(1), UNIT)], [0, 0])

    def test_valid_historical_fixture_still_constructs(self) -> None:
        # The compatibility surface keeps accepting valid historical
        # fixtures (S2 and a depth-1 object carrying it).
        s2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        depth1 = UCNSObject(2, 2, [(Fraction(0), s2), (Fraction(1), UNIT)], [0, 0])
        self.assertEqual(depth1.n_min, 2)
        self.assertEqual(len(depth1.A_plus), 2)


if __name__ == "__main__":
    unittest.main()
