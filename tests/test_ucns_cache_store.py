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


def test_structural_hit_path():
    store = UCNSCacheStore()
    first = obj(0)
    second = obj(1)
    first_key = make_ucns_cache_key(first)
    second_key = make_ucns_cache_key(second)
    if first_key.braider_hash != second_key.braider_hash or first_key.canonical_hash == second_key.canonical_hash:
        import pytest
        pytest.xfail("awaiting stable UCNS fixture for shared braid / distinct identity")
    store.put_by_object(first, "value")
    result = store.get_by_object(second)
    assert result.structural_hit
