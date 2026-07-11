"""Regressions for exhaustive catalogue-bounded factor search."""

import itertools
from fractions import Fraction

from ucns import UCNSObject, UNIT, factor_search_v08, multiply
from ucns.canonical import is_multiplicative_unit
from ucns.payload_system import iter_payload_system_solutions

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
T2 = UCNSObject(1, 1, [(Fraction(0), E)], [0])
T3 = UCNSObject(1, 1, [(Fraction(0), T2)], [0])


def _solution_set(iterator):
    return {(tuple(left), tuple(right)) for left, right in iterator}


def _brute_force(grid, p, q, catalogue):
    candidates = [None]
    for candidate in catalogue:
        if candidate is None:
            continue
        if any(existing is not None and existing == candidate for existing in candidates):
            continue
        candidates.append(candidate)

    solutions = set()
    for left in itertools.product(candidates, repeat=p):
        for right in itertools.product(candidates, repeat=q):
            if all(
                multiply(left[k], right[j]) == grid[k][j]
                for k in range(p)
                for j in range(q)
            ):
                solutions.add((tuple(left), tuple(right)))
    return solutions


def test_one_cell_recursive_composite_is_found():
    product = multiply(T2, T2)
    assert product == T2
    assert not is_multiplicative_unit(T2)

    result = factor_search_v08(T2, [UNIT, E], prune=False)

    assert isinstance(result, tuple)
    assert multiply(result[0], result[1]) == T2
    assert not is_multiplicative_unit(result[0])
    assert not is_multiplicative_unit(result[1])


def test_greedy_tower_false_negative_is_repaired():
    left = UCNSObject(
        2,
        2,
        [(Fraction(0), T3), (Fraction(1), UNIT)],
        [0, 0],
    )
    right = UCNSObject(
        2,
        2,
        [(Fraction(0), T2), (Fraction(1), UNIT)],
        [0, 0],
    )
    product = multiply(left, right)

    result = factor_search_v08(product, [UNIT, E, T2, T3], prune=False)

    assert isinstance(result, tuple)
    assert multiply(result[0], result[1]) == product


def test_payload_iterator_equals_brute_force_on_small_universe():
    catalogue = [UNIT, E, T2]
    for p, q in ((1, 1), (1, 2), (2, 1), (2, 2)):
        for left in itertools.product(catalogue, repeat=p):
            for right in itertools.product(catalogue, repeat=q):
                grid = [
                    [multiply(left[k], right[j]) for j in range(q)]
                    for k in range(p)
                ]
                observed = _solution_set(
                    iter_payload_system_solutions(grid, p, q, catalogue)
                )
                expected = _brute_force(grid, p, q, catalogue)
                assert observed == expected


def test_duplicate_catalogue_entries_do_not_duplicate_assignments():
    grid = [[T3]]
    base = list(iter_payload_system_solutions(grid, 1, 1, [UNIT, E, T2, T3]))
    duplicate = list(
        iter_payload_system_solutions(
            grid,
            1,
            1,
            [UNIT, E, T2, T3, E, T2, UNIT, T3],
        )
    )
    assert _solution_set(iter(base)) == _solution_set(iter(duplicate))
    assert len(base) == len(duplicate)


def test_payload_assignment_order_is_deterministic():
    grid = [[T3]]
    runs = [
        list(iter_payload_system_solutions(grid, 1, 1, [UNIT, E, T2, T3]))
        for _ in range(3)
    ]
    assert runs[0] == runs[1] == runs[2]
