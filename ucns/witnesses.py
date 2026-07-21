"""
Separation witnesses for the parallel valuation triad (Chapter 1.9).

A conforming implementation must exhibit:

1. Non-null A, C with W(A) = W(C) yet M(A) ≠ M(C)
   → M is not a function of W.

2. Non-null D, E with M(D) = M(E) yet W(D) ≠ W(E)
   → W is not a function of M.

M is now derived primarily from the product of cell supports µ(c).
Different partitions of the same total support therefore yield different M
while W stays identical. Collections of pure unit-support cells all share
M = 1 and therefore give the opposite direction for free.

The residual m_contrib (default 1) remains available for future typed
grading but is no longer required for separation.
"""

from __future__ import annotations

from .core import Carrier, Cell, N, is_null, pair, support_weight, product_character


def witness_same_W_different_M() -> tuple[Carrier, Carrier]:
    """
    Same total support, different product of supports.
    A: two unit cells  → W=2, M=1×1=1
    C: one cell µ=2    → W=2, M=2
    """
    A = Carrier(cells=(Cell(mu=1.0), Cell(mu=1.0)))
    C = Carrier(cells=(Cell(mu=2.0),))
    assert not is_null(A) and not is_null(C)
    assert support_weight(A) == support_weight(C) == 2.0
    assert product_character(A) != product_character(C)
    return A, C


def witness_same_M_different_W() -> tuple[Carrier, Carrier]:
    """
    Pure unit-support cells always give product M=1.
    Different cardinalities therefore give different W at identical M.
    """
    D = Carrier(cells=(Cell(mu=1.0),))
    E = Carrier(cells=(Cell(mu=1.0), Cell(mu=1.0), Cell(mu=1.0)))
    assert not is_null(D) and not is_null(E)
    assert product_character(D) == product_character(E) == 1.0
    assert support_weight(D) != support_weight(E)
    return D, E


def verify_separation() -> bool:
    """Run both directions and confirm they survive pairing with the unit."""
    A, C = witness_same_W_different_M()
    D, E = witness_same_M_different_W()

    from .core import unit
    u = unit()
    # pairing multiplies both W and M; the inequalities are preserved
    assert support_weight(pair(A, u)) == support_weight(pair(C, u))
    assert product_character(pair(A, u)) != product_character(pair(C, u))

    assert product_character(pair(D, u)) == product_character(pair(E, u))
    assert support_weight(pair(D, u)) != support_weight(pair(E, u))

    assert is_null(pair(N, A))
    return True


if __name__ == "__main__":
    verify_separation()
    print("Separation witnesses verified (both directions + pairing).")
