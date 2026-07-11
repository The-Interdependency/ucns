"""Workstream 6 — collision-safe typed dictionary keys.

No supported dictionary can lose or overwrite a key because two key
encodings decode identically (codex-handoff/06).
"""

from fractions import Fraction

import pytest

from ucns import EncodingError, UCNSObject, recursive_decode, recursive_encode
from ucns.recursive_codec import (
    _DICT_SENTINELS,
    _key_capsule,
    _make_sentinel_cells,
    _safe_n_dec,
)


def _roundtrip(d):
    return recursive_decode(recursive_encode(d))


def test_int_str_bytes_keys_coexist_distinctly():
    d = {1: b"int", "1": b"str", b"1": b"bytes"}
    got = _roundtrip(d)
    assert got == d
    assert sorted(type(k).__name__ for k in got) == ["bytes", "int", "str"]


def test_supported_key_types_roundtrip_exactly():
    d = {
        "s": b"a",
        b"b": b"b",
        7: b"c",
        -12: b"d",
        True: b"e",
        False: b"f",
        2.5: b"g",
        (): b"h",
        (1, "x"): b"i",
        ((b"n", 3.5), False): b"j",
    }
    got = _roundtrip(d)
    assert got == d
    for k in d:
        match = [g for g in got if g == k]
        assert match and type(match[0]) is type(k), f"type drift on {k!r}"
    assert isinstance([g for g in got if g == (1, "x")][0], tuple)


@pytest.mark.parametrize(
    "bad_key",
    [float("nan"), float("inf"), float("-inf"), frozenset({1}), None],
)
def test_unsupported_hashable_keys_raise_at_encode(bad_key):
    with pytest.raises(EncodingError):
        recursive_encode({bad_key: b"v"})


@pytest.mark.parametrize(
    "bad_key",
    [bytearray(b"x"), [1], {"a": 1}, {1}, (1, [2]), (1, bytearray(b"y"))],
)
def test_unsupported_key_shapes_raise_in_capsule(bad_key):
    """bytearray, lists, dicts, sets, and tuples containing unsupported
    elements are rejected by the key layer itself (Python already bars
    the unhashable ones from being dict keys at all)."""
    with pytest.raises(EncodingError):
        _key_capsule(bad_key)


def test_malformed_tag_and_unknown_version_raise_at_decode():
    def dict_of_raw_key(raw_key_value):
        n = 1
        total = _DICT_SENTINELS + 2 * n
        n_dec = _safe_n_dec(total)
        sa, sf = _make_sentinel_cells(_DICT_SENTINELS)
        a_plus = list(sa)
        f_plus = list(sf)
        a_plus.append((Fraction(4 * _DICT_SENTINELS, total),
                       recursive_encode(raw_key_value)))
        a_plus.append((Fraction(4 * (_DICT_SENTINELS + 1), total),
                       recursive_encode(b"v")))
        f_plus.extend([1, 1])
        return UCNSObject(n_dec, n_dec, a_plus, f_plus)

    with pytest.raises(EncodingError):
        recursive_decode(dict_of_raw_key([b"__ucns_key_v1__", b"nope", b"x"]))
    with pytest.raises(EncodingError):
        recursive_decode(dict_of_raw_key([b"__ucns_key_v9__", b"int", b"1"]))
    with pytest.raises(EncodingError):
        recursive_decode(dict_of_raw_key([b"__ucns_key_v1__", b"int", b"1x"]))
    with pytest.raises(EncodingError):
        recursive_decode(dict_of_raw_key([b"__ucns_key_v1__", b"bool", b"maybe"]))
    with pytest.raises(EncodingError):
        recursive_decode(dict_of_raw_key([b"__ucns_key_v1__", b"float", b"inf"]))


def test_duplicate_decoded_keys_raise_not_overwrite():
    n = 2
    total = _DICT_SENTINELS + 2 * n
    n_dec = _safe_n_dec(total)
    sa, sf = _make_sentinel_cells(_DICT_SENTINELS)
    a_plus = list(sa)
    f_plus = list(sf)
    for i, value in enumerate((b"first", b"second")):
        a_plus.append((Fraction(4 * (_DICT_SENTINELS + 2 * i), total),
                       recursive_encode(_key_capsule("same"))))
        a_plus.append((Fraction(4 * (_DICT_SENTINELS + 2 * i + 1), total),
                       recursive_encode(value)))
        f_plus.extend([1, 1])
    hand_built = UCNSObject(n_dec, n_dec, a_plus, f_plus)
    with pytest.raises(EncodingError):
        recursive_decode(hand_built)


def test_legacy_byte_key_dictionaries_still_decode():
    """A dict encoded with the pre-capsule layout (keys as plain
    values) decodes with the historical bytes coercion."""
    n = 1
    total = _DICT_SENTINELS + 2 * n
    n_dec = _safe_n_dec(total)
    sa, sf = _make_sentinel_cells(_DICT_SENTINELS)
    a_plus = list(sa)
    f_plus = list(sf)
    a_plus.append((Fraction(4 * _DICT_SENTINELS, total),
                   recursive_encode("legacy")))
    a_plus.append((Fraction(4 * (_DICT_SENTINELS + 1), total),
                   recursive_encode(b"value")))
    f_plus.extend([1, 1])
    legacy = UCNSObject(n_dec, n_dec, a_plus, f_plus)
    got = recursive_decode(legacy)
    assert got == {b"legacy": b"value"}


def test_legacy_unhashable_key_raises_cleanly():
    n = 1
    total = _DICT_SENTINELS + 2 * n
    n_dec = _safe_n_dec(total)
    sa, sf = _make_sentinel_cells(_DICT_SENTINELS)
    a_plus = list(sa)
    f_plus = list(sf)
    a_plus.append((Fraction(4 * _DICT_SENTINELS, total),
                   recursive_encode([b"a", b"b"])))
    a_plus.append((Fraction(4 * (_DICT_SENTINELS + 1), total),
                   recursive_encode(b"value")))
    f_plus.extend([1, 1])
    legacy = UCNSObject(n_dec, n_dec, a_plus, f_plus)
    with pytest.raises(EncodingError):
        recursive_decode(legacy)


def test_nested_dicts_and_values_unchanged():
    d = {"outer": {"inner": [1, 2, {"deep": b"x"}]}}
    got = _roundtrip(d)
    assert got == {
        "outer": {"inner": [b"1", b"2", {"deep": b"x"}]}
    }
    assert type(list(got)[0]) is str
