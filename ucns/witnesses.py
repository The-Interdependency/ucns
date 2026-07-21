"""
Separation witnesses for the parallel valuation triad (Chapter 1.9).

A conforming implementation must exhibit:

1. Non-null A, C with W(A) = W(C) yet M(A) ≠ M(C)
   → M is not a function of W.

2. Non-null D, E with M(D) = M(E) yet W(D) ≠ W(E)
   → W is not a function of M.

These witnesses use the independent product-character contribution
(m_contrib) together with support weights μ.  The parameter is part of
the object model precisely so that combinatorial grading can differ from
raw support; later concrete evaluators may derive m_contrib from richer
structure while preserving the same separation.

The witnesses are minimal and survive pairing and the null floor.
"""

from __future__ import annotations

from .core import Carrier, Cell, N, is_null, pair, support_weight, product_character


def witness_same_W_different_M() -> tuple[Carrier, Carrier]:
    """
    A and C are non-null, W(A) = W(C) = 1, but M(A) = 1 ≠ 3 = M(C).
    """
    A = Carrier(cells=(Cell(mu=1.0),), m_contrib=1.0)
    C = Carrier(cells=(Cell(mu=1.0),), m_contrib=3.0)
    assert not is_null(A) and not is_null(C)
    assert support_weight(A) == support_weight(C) == 1.0
    assert product_character(A) != product_character(C)
    return A, C


def witness_same_M_different_W() -> tuple[Carrier, Carrier]:
    """
    D and E are non-null, M(D) = M(E) = 1, but W(D) = 1 ≠ 2 = W(E).
    """
    D = Carrier(cells=(Cell(mu=1.0),), m_contrib=1.0)
    E = Carrier(cells=(Cell(mu=1.0), Cell(mu=1.0)), m_contrib=1.0)
    assert not is_null(D) and not is_null(E)
    assert product_character(D) == product_character(E) == 1.0
    assert support_weight(D) != support_weight(E)
    return D, E


def verify_separation() -> bool:
    """Run both directions and confirm they survive pairing with the unit."""
    A, C = witness_same_W_different_M()
    D, E = witness_same_M_different_W()

    # pairing with unit preserves the inequalities
    from .core import unit
    u = unit()
    assert support_weight(pair(A, u)) == support_weight(pair(C, u))
    assert product_character(pair(A, u)) != product_character(pair(C, u))

    assert product_character(pair(D, u)) == product_character(pair(E, u))
    assert support_weight(pair(D, u)) != support_weight(pair(E, u))

    # Null still absorbs
    assert is_null(pair(N, A))
    return True


if __name__ == "__main__":
    verify_separation()
    print("Separation witnesses verified (both directions + pairing).")
