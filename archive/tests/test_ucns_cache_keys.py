from fractions import Fraction

import pytest

from ucns import UCNSObject
from ucns_cache.dependencies import require_ucns, ucns_dependency_report
from ucns_cache.keys import make_ucns_cache_key


def sample_obj():
    return UCNSObject(4, 2, [(Fraction(0), None), (Fraction(1, 2), None)], [0, 1])


def test_ucns_dependency_required():
    report = ucns_dependency_report()
    assert report["available"] is True
    assert require_ucns() is not None


def test_same_object_same_key():
    obj = sample_obj()
    assert make_ucns_cache_key(obj) == make_ucns_cache_key(obj)


def test_key_has_scope_note():
    key = make_ucns_cache_key(sample_obj())
    assert key.scope_note
    assert key.domain_label
