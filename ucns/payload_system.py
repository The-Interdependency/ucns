"""
ucns.payload_system
==============================
Coupled payload equation solver.

Given a p×q grid of target payload objects  P_payloads[k][j]  (the
payloads extracted from a product object P), this module finds lists
S_A = [S_0^A, …, S_{p-1}^A] and S_B = [S_0^B, …, S_{q-1}^B] such that

    multiply(S_A[k], S_B[j]) == P_payloads[k][j]   for all k, j.

This is a small finite constraint-satisfaction problem over the catalogue
of depth-0 payload objects from the frozen domain D'.

Algorithm
---------
1.  For each candidate S_0^A from the catalogue (including None/unit):
    a.  Recover S_B[j] for each j from row k=0:
            find R such that  multiply(S_0^A, R) == P_payloads[0][j]
    b.  If row 0 is solvable, recover S_A[k] for each k > 0 from
        column j=0:
            find L such that  multiply(L, S_B[0]) == P_payloads[k][0]
    c.  Global consistency check:
            for all k, j:  multiply(S_A[k], S_B[j]) == P_payloads[k][j]
    d.  If consistent, return (S_A, S_B).
2.  Return None if no consistent assignment exists.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_payload_system
#   module_name: payload_system
#   module_kind: engine
#   summary: Solves the p×q coupled payload equation system, recovering (S_A, S_B) such that multiply(S_A[k], S_B[j]) matches every product payload cell.
#   owner: Erin Spencer
#   public_surface: solve_payload_system
#   internal_surface: _globally_consistent
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive/tests/test_depth2_full_domain.py
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_quotient
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from typing import List, Optional, Tuple

from .canonical import UCNSObject, multiply
from .recursive_quotient import (
    find_right_factor_or_sentinel,
    find_left_factor_or_sentinel,
    _NO_SOLUTION,
)

__all__ = ["solve_payload_system"]


def solve_payload_system(
    P_payloads: List[List[Optional[UCNSObject]]],
    p: int,
    q: int,
    catalogue: List[Optional[UCNSObject]],
) -> Optional[Tuple[List[Optional[UCNSObject]], List[Optional[UCNSObject]]]]:
    """Find (S_A, S_B) satisfying all coupled payload equations.

    Parameters
    ----------
    P_payloads:
        2-D list of shape (p, q): P_payloads[k][j] is the payload at
        position k*q + j in the product object P.
    p, q:
        Dimensions of the host factorisation being tried.
    catalogue:
        Payload candidates to enumerate.  Should include None (unit).

    Returns
    -------
    (S_A, S_B) if a globally consistent assignment exists, or ``None``.
    """
    for S0_A in catalogue:
        # --- Step 1: recover S_B from row k=0 ---
        S_B: List[Optional[UCNSObject]] = []
        row_ok = True
        for j in range(q):
            target = P_payloads[0][j]
            result = find_right_factor_or_sentinel(target, S0_A, catalogue)
            if result is _NO_SOLUTION:
                row_ok = False
                break
            S_B.append(result)  # type: ignore[arg-type]
        if not row_ok:
            continue

        # --- Step 2: recover S_A[k] for k > 0 from column j=0 ---
        S_A: List[Optional[UCNSObject]] = [S0_A]
        col_ok = True
        for k in range(1, p):
            target = P_payloads[k][0]
            result = find_left_factor_or_sentinel(target, S_B[0], catalogue)
            if result is _NO_SOLUTION:
                col_ok = False
                break
            S_A.append(result)  # type: ignore[arg-type]
        if not col_ok:
            continue

        # --- Step 3: global consistency check ---
        if _globally_consistent(S_A, S_B, P_payloads, p, q):
            return S_A, S_B

    return None


def _globally_consistent(
    S_A: List[Optional[UCNSObject]],
    S_B: List[Optional[UCNSObject]],
    P_payloads: List[List[Optional[UCNSObject]]],
    p: int,
    q: int,
) -> bool:
    """Return True iff multiply(S_A[k], S_B[j]) == P_payloads[k][j] for all k, j."""
    for k in range(p):
        for j in range(q):
            if multiply(S_A[k], S_B[j]) != P_payloads[k][j]:
                return False
    return True
