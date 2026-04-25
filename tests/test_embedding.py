"""Tests for ucns.embedding – UCNEmbedding API."""

import math
import struct
import unittest

from ucns.embedding import UCNEmbedding

_TAU = 2.0 * math.pi


class TestUCNEmbeddingConstruction(unittest.TestCase):
    def test_dim_power_of_two(self):
        emb = UCNEmbedding(dim=64)
        self.assertEqual(emb.dim, 64)

    def test_dim_rounded_up(self):
        emb = UCNEmbedding(dim=50)
        self.assertEqual(emb.dim, 64)

    def test_dim_one(self):
        emb = UCNEmbedding(dim=1)
        self.assertEqual(emb.dim, 1)

    def test_dim_zero_raises(self):
        with self.assertRaises(ValueError):
            UCNEmbedding(dim=0)

    def test_repr_contains_dim(self):
        emb = UCNEmbedding(dim=32)
        self.assertIn("32", repr(emb))


class TestUCNEmbeddingEncode(unittest.TestCase):
    def setUp(self):
        self.emb = UCNEmbedding(dim=16)

    def test_encode_returns_list(self):
        v = self.emb.encode("hello")
        self.assertIsInstance(v, list)

    def test_encode_correct_length(self):
        v = self.emb.encode("hello")
        self.assertEqual(len(v), self.emb.dim)

    def test_encode_angles_in_range(self):
        for data in ["hello", [1.0, 2.0, 3.0], 42.0, b"abc"]:
            v = self.emb.encode(data)
            for angle in v:
                self.assertGreaterEqual(angle, 0.0)
                self.assertLess(angle, _TAU + 1e-9)

    def test_encode_deterministic(self):
        v1 = self.emb.encode("hello world")
        v2 = self.emb.encode("hello world")
        self.assertEqual(v1, v2)

    def test_encode_string(self):
        v = self.emb.encode("abc")
        self.assertEqual(len(v), self.emb.dim)

    def test_encode_float(self):
        v = self.emb.encode(3.14)
        self.assertEqual(len(v), self.emb.dim)

    def test_encode_int(self):
        v = self.emb.encode(42)
        self.assertEqual(len(v), self.emb.dim)

    def test_encode_list(self):
        v = self.emb.encode([1.0, 2.0, 3.0])
        self.assertEqual(len(v), self.emb.dim)

    def test_encode_bytes(self):
        v = self.emb.encode(b"\x00\xff\x80")
        self.assertEqual(len(v), self.emb.dim)

    def test_encode_unsupported_type_raises(self):
        with self.assertRaises(TypeError):
            self.emb.encode({"key": "value"})

    def test_encode_long_signal_truncated(self):
        long_signal = list(range(self.emb.dim * 3))
        v = self.emb.encode(long_signal)
        self.assertEqual(len(v), self.emb.dim)

    def test_encode_empty_string(self):
        v = self.emb.encode("")
        self.assertEqual(len(v), self.emb.dim)


class TestUCNEmbeddingPackedSerialization(unittest.TestCase):
    def setUp(self):
        self.emb = UCNEmbedding(dim=16)

    def test_packed_length(self):
        packed = self.emb.encode_packed("hello")
        self.assertEqual(len(packed), self.emb.dim * 2)

    def test_pack_unpack_roundtrip(self):
        v = self.emb.encode("hello world")
        packed = self.emb.encode_packed("hello world")
        unpacked = UCNEmbedding.unpack(packed)
        for orig, rec in zip(v, unpacked):
            self.assertAlmostEqual(orig, rec, delta=_TAU / 65535 + 1e-6)

    def test_packed_is_bytes(self):
        self.assertIsInstance(self.emb.encode_packed("test"), bytes)


class TestUCNEmbeddingSimilarity(unittest.TestCase):
    def setUp(self):
        self.emb = UCNEmbedding(dim=32)

    def test_similarity_self(self):
        v = self.emb.encode("hello")
        self.assertAlmostEqual(self.emb.similarity(v, v), 1.0, places=10)

    def test_similarity_in_range(self):
        v1 = self.emb.encode("hello")
        v2 = self.emb.encode("world")
        s = self.emb.similarity(v1, v2)
        self.assertGreaterEqual(s, -1.0)
        self.assertLessEqual(s, 1.0)

    def test_similarity_symmetric(self):
        v1 = self.emb.encode("foo")
        v2 = self.emb.encode("bar")
        self.assertAlmostEqual(
            self.emb.similarity(v1, v2),
            self.emb.similarity(v2, v1),
            places=12,
        )

    def test_similarity_different_lengths_raises(self):
        with self.assertRaises(ValueError):
            self.emb.similarity([1.0, 2.0], [1.0])

    def test_similar_inputs_higher_score(self):
        v1 = self.emb.encode("the cat sat")
        v2 = self.emb.encode("the cat sat")  # identical
        v3 = self.emb.encode("completely different xyz 999")
        s_same = self.emb.similarity(v1, v2)
        s_diff = self.emb.similarity(v1, v3)
        self.assertGreater(s_same, s_diff)


class TestUCNEmbeddingNearest(unittest.TestCase):
    def setUp(self):
        self.emb = UCNEmbedding(dim=32)

    def test_nearest_finds_identical(self):
        query = self.emb.encode("apple")
        corpus = [
            self.emb.encode("banana"),
            self.emb.encode("apple"),
            self.emb.encode("cherry"),
        ]
        idx, score = self.emb.nearest(query, corpus)
        self.assertEqual(idx, 1)
        self.assertAlmostEqual(score, 1.0, places=10)

    def test_nearest_empty_corpus_raises(self):
        query = self.emb.encode("hello")
        with self.assertRaises(ValueError):
            self.emb.nearest(query, [])

    def test_nearest_returns_valid_index(self):
        query = self.emb.encode("test")
        corpus = [self.emb.encode(str(i)) for i in range(10)]
        idx, score = self.emb.nearest(query, corpus)
        self.assertGreaterEqual(idx, 0)
        self.assertLess(idx, 10)


class TestUCNEmbeddingToSignal(unittest.TestCase):
    def test_int_gives_one_element(self):
        sig = UCNEmbedding._to_signal(5)
        self.assertEqual(sig, [5.0])

    def test_float_gives_one_element(self):
        sig = UCNEmbedding._to_signal(3.14)
        self.assertAlmostEqual(sig[0], 3.14)

    def test_str_encodes_ordinals(self):
        sig = UCNEmbedding._to_signal("AB")
        self.assertAlmostEqual(sig[0], 65.0)
        self.assertAlmostEqual(sig[1], 66.0)

    def test_bytes_encodes_byte_values(self):
        sig = UCNEmbedding._to_signal(b"\x00\x01\xff")
        self.assertAlmostEqual(sig[0], 0.0)
        self.assertAlmostEqual(sig[1], 1.0)
        self.assertAlmostEqual(sig[2], 255.0)

    def test_list_passthrough(self):
        sig = UCNEmbedding._to_signal([1.5, 2.5])
        self.assertEqual(sig, [1.5, 2.5])


if __name__ == "__main__":
    unittest.main()
