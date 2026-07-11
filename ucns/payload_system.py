"""
ucns.payload_system
==============================
Exhaustive catalogue-bounded coupled payload equation solver.

Given a p×q grid of target payloads, enumerate every pair S_A, S_B drawn
from the normalized payload catalogue such that

    multiply(S_A[k], S_B[j]) == P_payloads[k][j]

for every cell. The legacy ``solve_payload_system`` API remains as a
first-solution compatibility wrapper.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_payload_system
#   module_name: payload_system
#   module_kind: engine
#   summary: Normalizes payload catalogues and exhaustively enumerates every assignment satisfying the coupled product equations, with a first-solution compatibility wrapper.
#   owner: Erin Spencer
#   public_surface: normalize_payload_catalogue, iter_payload_system_solutions, solve_payload_system
#   internal_surface: _globally_consistent
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_exhaustive_factor_search.py, tests/test_factor_search_provenance.py, ucns_recursive/tests/test_depth2_full_domain.py
#   rollout: default_enabled
#   rollback: restore the greedy first-quotient solver
#   requires: ucns_canonical
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from itertools import product as _iproduct
from typing import Iterator, List, Optional, Tuple

from .canonical import UCNSObject, multiply

__all__ = [
    "normalize_payload_catalogue",
    "iter_payload_system_solutions",
    "solve_payload_system",
]

PayloadAssignment = Tuple[
    List[Optional[UCNSObject]], List[Optional[UCNSObject]]
]


def normalize_payload_catalogue(
    catalogue: List[Optional[UCNSObject]],
) -> List[Optional[UCNSObject]]:
    """Return the exact deterministic candidate sequence searched.

    The unit payload ``None`` appears exactly once and first. Remaining
    candidates preserve caller order with structural duplicates removed.
    The operation is idempotent, so provenance code can fingerprint the
    returned sequence before passing it to the solver.
    """
    normalized: List[Optional[UCNSObject]] = [None]
    for candidate in catalogue:
        if candidate is None:
            continue
        if any(
            previous is not None and previous == candidate
            for previous in normalized
        ):
            continue
        normalized.append(candidate)
    return normalized


def iter_payload_system_solutions(
    P_payloads: List[List[Optional[UCNSObject]]],
    p: int,
    q: int,
    catalogue: List[Optional[UCNSObject]],
) -> Iterator[PayloadAssignment]:
    """Yield every normalized-catalogue assignment satisfying the grid."""
    candidates = normalize_payload_catalogue(catalogue)

    for s0_a in candidates:
        column_domains: List[List[Optional[UCNSObject]]] = []
        feasible = True
        for j in range(q):
            target = P_payloads[0][j]
            domain = [
                candidate
                for candidate in candidates
                if multiply(s0_a, candidate) == target
            ]
            if not domain:
                feasible = False
                break
            column_domains.append(domain)
        if not feasible:
            continue

        for s_b_tuple in _iproduct(*column_domains):
            row_domains: List[List[Optional[UCNSObject]]] = []
            rows_ok = True
            for k in range(1, p):
                domain = [
                    candidate
                    for candidate in candidates
                    if all(
                        multiply(candidate, s_b_tuple[j]) == P_payloads[k][j]
                        for j in range(q)
                    )
                ]
                if not domain:
                    rows_ok = False
                    break
                row_domains.append(domain)
            if not rows_ok:
                continue

            for s_a_rest in _iproduct(*row_domains):
                s_a = [s0_a] + list(s_a_rest)
                s_b = list(s_b_tuple)
                if _globally_consistent(s_a, s_b, P_payloads, p, q):
                    yield s_a, s_b


def solve_payload_system(
    P_payloads: List[List[Optional[UCNSObject]]],
    p: int,
    q: int,
    catalogue: List[Optional[UCNSObject]],
) -> Optional[PayloadAssignment]:
    """Return the first deterministic solution, or ``None`` when absent."""
    for solution in iter_payload_system_solutions(P_payloads, p, q, catalogue):
        return solution
    return None


def _globally_consistent(
    S_A: List[Optional[UCNSObject]],
    S_B: List[Optional[UCNSObject]],
    P_payloads: List[List[Optional[UCNSObject]]],
    p: int,
    q: int,
) -> bool:
    """Return True iff every coupled payload equation is satisfied."""
    for k in range(p):
        for j in range(q):
            if multiply(S_A[k], S_B[j]) != P_payloads[k][j]:
                return False
    return True
