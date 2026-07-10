"""Workstream 1 — exhaustive payload assignments and factor search.

Mandated tower regression: fails on the greedy solver, passes only
because alternative quotient assignments are explored.  Plus the
iterator-vs-brute-force oracle, determinism, dedup, and unit-skip
continuation tests required by codex-handoff/01.
"""

import itertools
from fractions import Fraction

from ucns import UCNSObject, UNIT, factor_search_v08, multiply
from ucns.payload_system import iter_payload_system_solutions, solve_payload_system

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
T2 = UCNSObject(1, 1, [(Fraction(0), E)], [0])
T3 = UCNSObject(1, 1, [(Fraction(0), T2)], [0])

S2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])


def _solution_set(iterator):
    return {
        (tuple(sa), tuple(sb))
        for sa, sb in iterator
    }


def _brute_force(P_payloads, p, q, catalogue):
    cands = []
    seen = []
    for c in [None] + [x for x in catalogue if x is not None]:
        if any((c is None and s is None)
               or (c is not None and s is not None and c == s)
               for s in seen):
            continue
        seen.append(c)
        cands.append(c)
    out = set()
    for sa in itertools.product(cands, repeat=p):
        for sb in itertools.product(cands, repeat=q):
            if all(
                multiply(sa[k], sb[j]) == P_payloads[k][j]
                for k in range(p)
                for j in range(q)
            ):
                out.add((tuple(sa), tuple(sb)))
    return out


def test_tower_false_negative_regression():
    """The handoff's mandated regression, verbatim up to API names."""
    A = UCNSObject(
        2, 2,
        [(Fraction(0), T3), (Fraction(1), UNIT)],
        [0, 0],
    )
    B = UCNSObject(
        2, 2,
        [(Fraction(0), T2), (Fraction(1), UNIT)],
        [0, 0],
    )
    P = multiply(A, B)

    result = factor_search_v08(P, [UNIT, E, T2, T3], prune=False)

    assert isinstance(result, tuple), (
        "greedy false negative: exhaustive search must find factors"
    )
    rec_A, rec_B = result
    assert multiply(rec_A, rec_B) == P


def test_iterator_equals_brute_force():
    """The payload iterator equals the Cartesian brute-force oracle on
    small grids generated from known S_A and S_B values."""
    catalogues = [
        [UNIT, E, T2, T3],
        [UNIT, E, S2],
        [UNIT, T2, T3, S2],
    ]
    shapes = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 2)]
    for catalogue in catalogues:
        cands = [c for c in catalogue]
        for p, q in shapes:
            for sa in itertools.product(cands, repeat=p):
                for sb in itertools.product(cands, repeat=q):
                    grid = [
                        [multiply(sa[k], sb[j]) for j in range(q)]
                        for k in range(p)
                    ]
                    got = _solution_set(
                        iter_payload_system_solutions(grid, p, q, catalogue)
                    )
                    want = _brute_force(grid, p, q, catalogue)
                    assert got == want, (
                        f"iterator != brute force for p={p} q={q}"
                    )


def test_every_yield_satisfies_grid():
    grid = [[T3, T3], [T2, None]]
    for sa, sb in iter_payload_system_solutions(grid, 2, 2, [UNIT, E, T2, T3]):
        for k in range(2):
            for j in range(2):
                assert multiply(sa[k], sb[j]) == grid[k][j]


def test_duplicate_catalogue_entries_do_not_duplicate():
    grid = [[T3, T3], [T2, None]]
    base = list(
        iter_payload_system_solutions(grid, 2, 2, [UNIT, E, T2, T3])
    )
    dup = list(
        iter_payload_system_solutions(
            grid, 2, 2, [UNIT, E, T2, T3, T2, E, UNIT, T3]
        )
    )
    assert _solution_set(iter(base)) == _solution_set(iter(dup))
    assert len(dup) == len(base), "duplicate entries duplicated assignments"


def test_deterministic_ordering():
    """The absorbing 1x1 tower grid admits many assignments; the
    enumeration order must be identical across runs."""
    grid = [[T3]]
    runs = [
        [
            (tuple(sa), tuple(sb))
            for sa, sb in iter_payload_system_solutions(
                grid, 1, 1, [UNIT, E, T2, T3]
            )
        ]
        for _ in range(3)
    ]
    assert runs[0] == runs[1] == runs[2]
    assert len(runs[0]) >= 5, "absorbing grid must admit multiple assignments"


def test_compat_wrapper_returns_first():
    grid = [[T3, T3], [T2, None]]
    first = next(
        iter_payload_system_solutions(grid, 2, 2, [UNIT, E, T2, T3])
    )
    got = solve_payload_system(grid, 2, 2, [UNIT, E, T2, T3])
    assert got is not None
    assert (tuple(got[0]), tuple(got[1])) == (
        tuple(first[0]), tuple(first[1])
    )
    assert solve_payload_system([[S2]], 1, 1, [UNIT, E]) is None


def test_continues_past_unit_factor():
    """A valid later assignment is reached after an earlier assignment
    reconstructs a multiplicative-unit factor: the tower regression's
    p=4 split yields only unit right-factors, and p=1/p=2 assignments
    that fail recomposition; the search must keep going."""
    A = UCNSObject(2, 2, [(Fraction(0), T3), (Fraction(1), UNIT)], [0, 0])
    B = UCNSObject(2, 2, [(Fraction(0), T2), (Fraction(1), UNIT)], [0, 0])
    P = multiply(A, B)
    result = factor_search_v08(P, [UNIT, E, T2, T3], prune=False)
    assert isinstance(result, tuple)
    rec_A, rec_B = result
    assert multiply(rec_A, rec_B) == P
    from ucns.canonical import is_multiplicative_unit
    assert not is_multiplicative_unit(rec_A)
    assert not is_multiplicative_unit(rec_B)


def test_prune_agrees_with_no_prune_on_existence():
    corpus = []
    for left in (E, T2, S2):
        for right in (E, T2, S2):
            corpus.append(multiply(left, right))
    corpus.append(S2)  # likely prime relative to this catalogue
    catalogue = [UNIT, E, T2, T3, S2]
    for P in corpus:
        pruned = factor_search_v08(P, list(catalogue), prune=True)
        raw = factor_search_v08(P, list(catalogue), prune=False)
        assert isinstance(pruned, tuple) == isinstance(raw, tuple), (
            "prune changed factor existence"
        )
        for res in (pruned, raw):
            if isinstance(res, tuple):
                assert multiply(res[0], res[1]) == P
