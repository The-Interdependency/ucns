"""Workstream 4 — complete quotient consumers.

The plural solution-set APIs are the authoritative complete surface;
singular quotients are deterministic compatibility selectors; every
completeness-claiming consumer uses the complete sets
(codex-handoff/04).
"""

from fractions import Fraction

import pytest

from ucns import (
    UCNSObject,
    UNIT,
    SolutionLimitExceeded,
    UCNSStore,
    left_quotient,
    left_quotients,
    multiply,
    right_quotient,
    right_quotients,
)
from ucns.canonical import is_unit

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
T2 = UCNSObject(1, 1, [(Fraction(0), E)], [0])
T3 = UCNSObject(1, 1, [(Fraction(0), T2)], [0])
T4 = UCNSObject(1, 1, [(Fraction(0), T3)], [0])
W = UCNSObject(24, 1, [(Fraction(0), None), (Fraction(1), None)], [0, 0])
V = UCNSObject(24, 1, [(Fraction(0), None), (Fraction(2), None)], [0, 0])


def test_public_exports_and_compat_mirror():
    import ucns
    import ucns_recursive

    for name in ("left_quotients", "right_quotients", "SolutionLimitExceeded"):
        assert hasattr(ucns, name)
        assert hasattr(ucns_recursive, name)


def test_recursive_noncommutative_right_quotient():
    """Fails if the right-quotient payload recursion swaps direction:
    the payload equation is y ⊗ W = V⊠W, solvable only by y = V on the
    right; the left-direction equation W ⊠ y' = V⊠W has no solution."""
    X = UCNSObject(24, 1, [(Fraction(0), V)], [0])
    B = UCNSObject(24, 1, [(Fraction(0), W)], [0])
    P = multiply(X, B)
    got = right_quotient(P, B)
    assert got is not None and got == X
    sols = right_quotients(P, B)
    assert any(s is not None and s == X for s in sols)
    # the swapped-direction equation really is unsolvable:
    assert all(
        multiply(W, y) != multiply(V, W)
        for y in (None, E, V, W, T2)
    )


def test_singular_wrapper_skips_unit_solution():
    """When the first algebraic solution is the unit (or an absorbing
    alternative), the singular wrapper still recovers a non-unit
    solution."""
    got = left_quotient(T3, T3)
    assert got is not None and not is_unit(got)
    assert multiply(T3, got) == T3
    got_r = right_quotient(T3, T3)
    assert got_r is not None and not is_unit(got_r)
    assert multiply(got_r, T3) == T3


def test_singular_wrapper_none_when_only_unit_solution():
    """Legacy ambiguity preserved: None when no NON-unit solution
    exists — here the only solution of W ⊠ x = W is the unit."""
    assert left_quotients(W, W) and all(
        s is None or is_unit(s) for s in left_quotients(W, W)
    )
    assert left_quotient(W, W) is None


def test_plural_apis_deterministic_no_duplicates():
    runs = [left_quotients(T4, T4) for _ in range(3)]
    assert all(len(r) == 4 for r in runs)
    for r in runs[1:]:
        assert all(x == y for x, y in zip(runs[0], r))
    first = runs[0]
    for i, s in enumerate(first):
        assert not any(s == other for other in first[:i]), "duplicate solution"


def test_store_surfaces_every_remainder():
    """A stored key with multiple valid remainders appears once per
    remainder (repeated keys documented)."""
    import ucns.store as store_module

    original_encode = store_module.recursive_encode

    def passthrough(value):
        if isinstance(value, UCNSObject):
            return value
        return original_encode(value)

    store_module.recursive_encode = passthrough
    try:
        store = UCNSStore()
        store._objects["k"] = T3
        store._originals["k"] = T3
        matches = store.left_factors(T3)
        keys = [k for k, _ in matches]
        assert keys.count("k") == 3, "T3/T3 has exactly 3 remainders"
        remainders = [r for _, r in matches]
        assert remainders.count(None) == 1, "unit remainder reported as None"
        non_unit = [r for r in remainders if r is not None]
        assert all(multiply(T3, r) == T3 for r in non_unit)
        assert store.is_left_factor(T3, "k")
        right_matches = store.right_factors(T3)
        assert len(right_matches) == 3
    finally:
        store_module.recursive_encode = original_encode


def test_factor_decompose_matches_brute_force():
    import ucns.store as store_module

    original_encode = store_module.recursive_encode
    store_module.recursive_encode = (
        lambda v: v if isinstance(v, UCNSObject) else original_encode(v)
    )
    try:
        store = UCNSStore()
        store._objects["p"] = T3
        store._originals["p"] = T3
        catalogue = [T2, T3, W]
        got = store.factor_decompose("p", catalogue)
        universe = [E, T2, T3, T4, W, V]
        brute = []
        for A in catalogue:
            for B in universe:
                if is_unit(B):
                    continue
                if multiply(A, B) == T3:
                    if not any(A == ga and B == gb for ga, gb in brute):
                        brute.append((A, B))
        assert len(got) == len(brute)
        for pair in brute:
            assert any(pair[0] == a and pair[1] == b for a, b in got)
    finally:
        store_module.recursive_encode = original_encode


def test_limit_exception_propagates():
    with pytest.raises(SolutionLimitExceeded):
        left_quotients(T4, T4, limit=2)
    with pytest.raises(SolutionLimitExceeded):
        right_quotients(T4, T4, limit=2)


def test_import_boundary_untouched():
    import subprocess
    import sys

    code = (
        "import sys; import ucns; "
        "assert 'ucns_recursive' not in sys.modules, 'boundary violated'; "
        "print('ok')"
    )
    proc = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
