"""
Tests for ``UCNSStore`` — the v0.1 deployable retrieval surface.
"""

import unittest

from ucns_recursive.canonical import multiply
from ucns_recursive.recursive_codec import recursive_encode
from ucns_recursive.store import UCNSStore


class TestStoreBasics(unittest.TestCase):
    def test_insert_and_contains(self):
        store = UCNSStore()
        store.insert("a", b"hello")
        self.assertIn("a", store)
        self.assertEqual(len(store), 1)

    def test_remove(self):
        store = UCNSStore()
        store.insert("a", b"hello")
        store.remove("a")
        self.assertNotIn("a", store)
        self.assertEqual(len(store), 0)

    def test_remove_missing_raises(self):
        store = UCNSStore()
        with self.assertRaises(KeyError):
            store.remove("nope")

    def test_get_decoded_round_trips(self):
        store = UCNSStore()
        store.insert("a", b"hello")
        self.assertEqual(store.get_decoded("a"), b"hello")

    def test_get_original_preserves_uncoerced(self):
        store = UCNSStore()
        store.insert("a", "hello")
        self.assertEqual(store.get_original("a"), "hello")
        self.assertEqual(store.get_decoded("a"), b"hello")

    def test_keys(self):
        store = UCNSStore()
        store.insert("a", b"x")
        store.insert("b", b"y")
        self.assertEqual(set(store.keys()), {"a", "b"})

    def test_overwrite(self):
        store = UCNSStore()
        store.insert("a", b"first")
        store.insert("a", b"second")
        self.assertEqual(store.get_decoded("a"), b"second")
        self.assertEqual(len(store), 1)


class TestLeftFactors(unittest.TestCase):
    def test_self_match_returns_unit_remainder(self):
        store = UCNSStore()
        store.insert("a", b"abc")
        matches = store.left_factors(b"abc")
        self.assertEqual(len(matches), 1)
        key, remainder = matches[0]
        self.assertEqual(key, "a")
        self.assertIsNone(remainder)

    def test_factor_match_returns_complementary_remainder(self):
        A = recursive_encode(b"left")
        B = recursive_encode(b"right")
        P = multiply(A, B)

        store = UCNSStore()
        store._objects["product"] = P
        store._originals["product"] = "constructed"

        matches = store.left_factors(b"left")
        keys = {k for k, _ in matches}
        self.assertIn("product", keys)
        for k, remainder in matches:
            if k == "product":
                self.assertEqual(remainder, B)

    def test_no_match_when_query_unrelated(self):
        store = UCNSStore()
        store.insert("a", b"abc")
        matches = store.left_factors(b"completely-different-thing")
        # Verify any returned matches are real (sanity).
        for key, remainder in matches:
            P = store.get_object(key)
            Q = recursive_encode(b"completely-different-thing")
            if remainder is None:
                self.assertEqual(Q, P)
            else:
                self.assertEqual(multiply(Q, remainder), P)

    def test_multiple_stored_objects(self):
        A = recursive_encode(b"hi")
        B1 = recursive_encode(b"there")
        B2 = recursive_encode(b"world")
        P1 = multiply(A, B1)
        P2 = multiply(A, B2)

        store = UCNSStore()
        store._objects["doc1"] = P1
        store._originals["doc1"] = "doc1"
        store._objects["doc2"] = P2
        store._originals["doc2"] = "doc2"

        matches = store.left_factors(b"hi")
        keys = {k for k, _ in matches}
        self.assertEqual(keys, {"doc1", "doc2"})


class TestIsLeftFactor(unittest.TestCase):
    def test_self_is_left_factor(self):
        store = UCNSStore()
        store.insert("a", b"abc")
        self.assertTrue(store.is_left_factor(b"abc", "a"))


class TestFactorDecompose(unittest.TestCase):
    def test_decomposes_known_product(self):
        A = recursive_encode(b"x")
        B = recursive_encode(b"y")
        P = multiply(A, B)

        store = UCNSStore()
        store._objects["p"] = P
        store._originals["p"] = "p"

        catalogue = [A, recursive_encode(b"unrelated")]
        decomps = store.factor_decompose("p", catalogue)
        self.assertEqual(len(decomps), 1)
        Acand, Bcand = decomps[0]
        self.assertEqual(Acand, A)
        self.assertEqual(Bcand, B)


class TestStoreOnEncodedContainers(unittest.TestCase):
    def test_list_self_match(self):
        store = UCNSStore()
        store.insert("doc", [b"first", b"second"])
        matches = store.left_factors([b"first", b"second"])
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0][0], "doc")

    def test_dict_round_trip_through_store(self):
        store = UCNSStore()
        d = {b"name": b"Erin", b"role": b"architect"}
        store.insert("rec", d)
        self.assertEqual(store.get_decoded("rec"), d)


if __name__ == "__main__":
    unittest.main()
