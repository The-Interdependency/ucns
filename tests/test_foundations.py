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
