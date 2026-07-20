from fractions import Fraction

from ucns import UCNSObject
from ucns_cache.keys import make_ucns_cache_key
from ucns_cache.store import UCNSCacheStore


def obj(face=0):
    return UCNSObject(4, 2, [(Fraction(0), None), (Fraction(1, 2), None)], [face, face])


def test_store_exact_hit():
    store = UCNSCacheStore()
    store.put_by_object(obj(), "value", value_kind="fixture")
    result = store.get_by_object(obj())
    assert result.hit
    assert result.exact_hit
    assert result.entry.value == "value"


def structural_pair():
    return (
        UCNSObject(2, 1, [(Fraction(0), None), (Fraction(2), None), (Fraction(0), None)], [0, 0, 0]),
        UCNSObject(6, 3, [(Fraction(0), None), (Fraction(2, 3), None), (Fraction(4, 3), None)], [0, 0, 0]),
    )


def test_structural_fixture_has_shared_braid_and_distinct_identity():
    first, second = structural_pair()
    first_key = make_ucns_cache_key(first)
    second_key = make_ucns_cache_key(second)
    assert first_key.braider_hash == second_key.braider_hash
    assert first_key.canonical_hash != second_key.canonical_hash


def test_structural_hit_path():
    store = UCNSCacheStore()
    first, second = structural_pair()
    store.put_by_object(first, "value")
    result = store.get_by_object(second)
    assert result.hit
    assert result.structural_hit
    assert not result.exact_hit
    assert result.entry.value == "value"
