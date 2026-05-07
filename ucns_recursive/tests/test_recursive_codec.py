"""
Round-trip tests for ``recursive_codec``.

Each test encodes a Python value, decodes it back, and verifies the
result matches the documented round-trip contract.
"""

import unittest

from ucns_recursive.canonical import UCNSObject, multiply
from ucns_recursive.recursive_codec import (
    EncodingError,
    recursive_decode,
    recursive_encode,
)


class TestLeafRoundTrip(unittest.TestCase):
    def test_empty_bytes(self):
        obj = recursive_encode(b"")
        self.assertEqual(recursive_decode(obj), b"")

    def test_single_byte(self):
        for b in [0, 1, 64, 127, 128, 255]:
            with self.subTest(byte=b):
                obj = recursive_encode(bytes([b]))
                self.assertEqual(recursive_decode(obj), bytes([b]))

    def test_byte_string(self):
        original = b"hello world"
        obj = recursive_encode(original)
        self.assertEqual(recursive_decode(obj), original)

    def test_all_byte_values(self):
        original = bytes(range(256))
        obj = recursive_encode(original)
        self.assertEqual(recursive_decode(obj), original)

    def test_str_coerces_to_bytes(self):
        obj = recursive_encode("hello")
        self.assertEqual(recursive_decode(obj), b"hello")

    def test_str_unicode(self):
        obj = recursive_encode("héllo 世界")
        self.assertEqual(recursive_decode(obj), "héllo 世界".encode("utf-8"))

    def test_int_coerces_to_bytes(self):
        obj = recursive_encode(42)
        self.assertEqual(recursive_decode(obj), b"42")

    def test_int_negative(self):
        obj = recursive_encode(-17)
        self.assertEqual(recursive_decode(obj), b"-17")

    def test_float_coerces_to_bytes(self):
        obj = recursive_encode(3.14)
        self.assertEqual(recursive_decode(obj), b"3.14")

    def test_bytearray_coerces(self):
        obj = recursive_encode(bytearray(b"hi"))
        self.assertEqual(recursive_decode(obj), b"hi")

    def test_bool_coerces(self):
        self.assertEqual(recursive_decode(recursive_encode(True)), b"1")
        self.assertEqual(recursive_decode(recursive_encode(False)), b"0")


class TestListRoundTrip(unittest.TestCase):
    def test_list_of_bytes(self):
        original = [b"a", b"b", b"c"]
        obj = recursive_encode(original)
        self.assertEqual(recursive_decode(obj), original)

    def test_list_of_strings_round_trips_as_bytes(self):
        obj = recursive_encode(["alpha", "beta"])
        self.assertEqual(recursive_decode(obj), [b"alpha", b"beta"])

    def test_list_of_ints(self):
        obj = recursive_encode([1, 2, 3])
        self.assertEqual(recursive_decode(obj), [b"1", b"2", b"3"])

    def test_nested_list(self):
        obj = recursive_encode([b"a", [b"b", b"c"], b"d"])
        self.assertEqual(recursive_decode(obj), [b"a", [b"b", b"c"], b"d"])

    def test_tuple_round_trips_as_list(self):
        obj = recursive_encode((b"a", b"b"))
        self.assertEqual(recursive_decode(obj), [b"a", b"b"])

    def test_singleton_list(self):
        obj = recursive_encode([b"only"])
        self.assertEqual(recursive_decode(obj), [b"only"])

    def test_empty_list(self):
        obj = recursive_encode([])
        self.assertEqual(recursive_decode(obj), [])

    def test_deeply_nested(self):
        original = [[[b"deep"]]]
        obj = recursive_encode(original)
        self.assertEqual(recursive_decode(obj), original)


class TestDictRoundTrip(unittest.TestCase):
    def test_simple_dict(self):
        original = {b"a": b"1", b"b": b"2"}
        obj = recursive_encode(original)
        self.assertEqual(recursive_decode(obj), original)

    def test_dict_string_keys_coerce_to_bytes(self):
        obj = recursive_encode({"name": "Erin", "role": "architect"})
        self.assertEqual(
            recursive_decode(obj),
            {b"name": b"Erin", b"role": b"architect"},
        )

    def test_empty_dict(self):
        obj = recursive_encode({})
        self.assertEqual(recursive_decode(obj), {})

    def test_singleton_dict(self):
        obj = recursive_encode({b"k": b"v"})
        self.assertEqual(recursive_decode(obj), {b"k": b"v"})

    def test_nested_dict(self):
        original = {b"outer": {b"inner": b"value"}}
        obj = recursive_encode(original)
        self.assertEqual(recursive_decode(obj), original)

    def test_dict_with_list_value(self):
        original = {b"items": [b"a", b"b", b"c"]}
        obj = recursive_encode(original)
        self.assertEqual(recursive_decode(obj), original)

    def test_dict_insertion_order_preserved(self):
        d1 = {b"a": b"1", b"b": b"2"}
        d2 = {b"b": b"2", b"a": b"1"}
        obj1 = recursive_encode(d1)
        obj2 = recursive_encode(d2)
        # Different presentation order → different encoding (by design).
        self.assertNotEqual(obj1, obj2)
        decoded1 = recursive_decode(obj1)
        decoded2 = recursive_decode(obj2)
        self.assertEqual(list(decoded1.keys()), [b"a", b"b"])
        self.assertEqual(list(decoded2.keys()), [b"b", b"a"])


class TestDistinguishability(unittest.TestCase):
    """Empty leaf, empty list, empty dict are distinct objects."""

    def test_empty_distinguishability(self):
        empty_leaf = recursive_encode(b"")
        empty_list = recursive_encode([])
        empty_dict = recursive_encode({})
        self.assertEqual(len(empty_leaf.A_plus), 1)
        self.assertEqual(len(empty_list.A_plus), 2)
        self.assertEqual(len(empty_dict.A_plus), 3)
        self.assertNotEqual(empty_leaf, empty_list)
        self.assertNotEqual(empty_list, empty_dict)
        self.assertNotEqual(empty_leaf, empty_dict)


class TestFaceBitPresence(unittest.TestCase):
    """Item 4: face bits encode presence (1 = real, 0 = sentinel/padding)."""

    def test_leaf_sentinel_then_content(self):
        obj = recursive_encode(b"abc")
        # 1 sentinel face=0, 3 byte cells face=1
        self.assertEqual(obj.F_plus, [0, 1, 1, 1])

    def test_empty_leaf_one_sentinel(self):
        obj = recursive_encode(b"")
        self.assertEqual(obj.F_plus, [0])

    def test_list_two_sentinels(self):
        obj = recursive_encode([b"x", b"y"])
        self.assertEqual(obj.F_plus, [0, 0, 1, 1])

    def test_dict_three_sentinels(self):
        obj = recursive_encode({b"k": b"v"})
        self.assertEqual(obj.F_plus, [0, 0, 0, 1, 1])


class TestStructuralSanity(unittest.TestCase):
    """Confirm encoded objects are valid UCNSObjects that interact with
    the algebra (multiply doesn't crash, normalization doesn't corrupt)."""

    def test_encoded_objects_are_ucns_objects(self):
        for value in [b"abc", [b"x", b"y"], {b"k": b"v"}, b""]:
            with self.subTest(value=value):
                obj = recursive_encode(value)
                self.assertIsInstance(obj, UCNSObject)

    def test_multiply_with_self_does_not_crash(self):
        obj = recursive_encode(b"abc")
        product = multiply(obj, obj)
        self.assertIsInstance(product, UCNSObject)

    def test_encoded_list_has_expected_cell_count(self):
        obj = recursive_encode([b"a", b"b", b"c"])
        self.assertEqual(len(obj.A_plus), 5)  # 2 sentinels + 3 items

    def test_encoded_dict_has_expected_cell_count(self):
        obj = recursive_encode({b"k1": b"v1", b"k2": b"v2"})
        self.assertEqual(len(obj.A_plus), 7)  # 3 sentinels + 4 (alt k/v)

    def test_normalization_does_not_corrupt_leaf_bytes(self):
        # Regression: without the leading sentinel, the first byte's
        # value would be lost to normalization shifting theta0 to 0.
        for first_byte in [1, 65, 200, 255]:
            with self.subTest(first_byte=first_byte):
                original = bytes([first_byte, 50, 100])
                self.assertEqual(recursive_decode(recursive_encode(original)), original)


class TestErrors(unittest.TestCase):
    def test_unsupported_type_raises(self):
        with self.assertRaises(EncodingError):
            recursive_encode(object())

    def test_set_not_supported(self):
        with self.assertRaises(EncodingError):
            recursive_encode({1, 2, 3})


if __name__ == "__main__":
    unittest.main()
