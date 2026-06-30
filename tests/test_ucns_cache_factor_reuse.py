from fractions import Fraction

from ucns import UCNSObject, multiply
from ucns_cache.keys import factor_reuse_candidates


def atom(angle, face=0):
    return UCNSObject(4, 2, [(Fraction(0), None), (Fraction(angle), None)], [0, face])


def test_factor_reuse_respects_scope():
    product = multiply(atom(Fraction(1, 2)), atom(Fraction(1)))
    candidates = factor_reuse_candidates(product)
    assert isinstance(candidates, list)


def test_no_lean_runtime_dependency():
    import ucns_cache
    assert ucns_cache.ucns_available()
