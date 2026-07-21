"""Minimal contract tests for the sealed Chapter 1 foundations."""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ucns import (
    N,
    Carrier,
    Cell,
    is_null,
    faithful_breadth,
    radius,
    support_weight,
    product_character,
    prune,
    pair,
    collapse,
    unit,
    from_payload,
)
from ucns.core import StructuralNull


def test_null_is_unique_and_zero():
    assert is_null(N)
    assert faithful_breadth(N) == 0.0
    assert radius(N) == 0.0
    assert support_weight(N) == 0.0
    assert product_character(N) == 0.0
    assert N is StructuralNull()  # singleton


def test_unit_and_radius():
    u = unit()
    assert not is_null(u)
    assert product_character(u) == 1.0
    assert support_weight(u) > 0.0
    assert faithful_breadth(u) > 0.0
    a = radius(u)
    assert 0.0 < a < 1.0
    # a = 1 - exp(-B)
    assert abs(a - (1.0 - math.exp(-faithful_breadth(u)))) < 1e-12


def test_algebraic_zero_not_null():
    z = from_payload(0, mu=1.0)
    assert not is_null(z)
    assert support_weight(z) > 0.0
    assert faithful_breadth(z) > 0.0


def test_pairing_multiplicative_and_absorbing():
    u = unit()
    p = pair(u, u)
    assert not is_null(p)
    assert abs(support_weight(p) - support_weight(u) ** 2) < 1e-12
    assert abs(product_character(p) - product_character(u) ** 2) < 1e-12
    assert is_null(pair(N, u))
    assert is_null(pair(u, N))


def test_rectangular_zero_prune():
    dead = Carrier(cells=(Cell(mu=0.0), Cell(payload=1, mu=1.0)))
    pruned = prune(dead)
    assert not is_null(pruned)
    assert len(pruned.cells) == 1
    assert is_null(prune(Carrier(cells=(Cell(mu=0.0),))))


def test_collapse_requires_complete_absence():
    # algebraic zero alone does not collapse
    z = from_payload(0, mu=1.0)
    assert not is_null(collapse(z))
    # only after complete structural erasure
    empty = Carrier(cells=())
    assert is_null(collapse(empty))


def test_separation_witnesses():
    from ucns import (
        witness_same_W_different_M,
        witness_same_M_different_W,
        verify_separation,
        support_weight,
        product_character,
    )
    A, C = witness_same_W_different_M()
    assert support_weight(A) == support_weight(C)
    assert product_character(A) != product_character(C)

    D, E = witness_same_M_different_W()
    assert product_character(D) == product_character(E)
    assert support_weight(D) != support_weight(E)

    assert verify_separation() is True


def test_B_invariance_under_cell_reordering():
    """B must not depend on the order of cells with identical support."""
    from ucns import Carrier, Cell, faithful_breadth
    c1 = Cell(mu=1.0, payload="a")
    c2 = Cell(mu=1.0, payload="b")
    left  = Carrier(cells=(c1, c2))
    right = Carrier(cells=(c2, c1))
    assert abs(faithful_breadth(left) - faithful_breadth(right)) < 1e-12


def test_B_invariance_under_equivalent_receipts():
    """Identical receipt multisets (order-insensitive for now) give same B."""
    from ucns import Carrier, Cell, faithful_breadth
    base = (Cell(mu=1.0),)
    a = Carrier(cells=base, receipts=("r1", "r2"))
    b = Carrier(cells=base, receipts=("r2", "r1"))
    assert abs(faithful_breadth(a) - faithful_breadth(b)) < 1e-12


def test_M_is_multiplicative_under_pairing():
    from ucns import unit, pair, product_character
    u = unit()
    p = pair(u, u)
    assert abs(product_character(p) - product_character(u)**2) < 1e-12
