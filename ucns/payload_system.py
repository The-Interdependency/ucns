"""
ucns.payload_system
==============================
Coupled payload equation solver — exhaustive, catalogue-bounded.

Given a p×q grid of target payload objects  P_payloads[k][j]  (the
payloads extracted from a product object P), this module enumerates
**every** pair of lists S_A = [S_0^A, …, S_{p-1}^A] and
S_B = [S_0^B, …, S_{q-1}^B] drawn from the supplied catalogue such that

    multiply(S_A[k], S_B[j]) == P_payloads[k][j]   for all k, j.

This is a small finite constraint-satisfaction problem over the
catalogue of candidate payload objects.

Why exhaustive
--------------
⊠ is not cancellative (docs/base-geometry.md §5), so a local equation
``multiply(X, R) == target`` may have several catalogue solutions.  The
pre-v1.0 solver committed to the first quotient per row-zero /
column-zero cell; a first local choice can fail global consistency even
though a later choice yields a valid factorization, producing false
``SEQ-PRIME`` results.  ``iter_payload_system_solutions`` explores the
full assignment space instead (codex-handoff/01).

Algorithm
---------
1.  Normalize the catalogue: the ``None`` unit exactly once and first,
    then the remaining candidates deduplicated structurally in their
    original order (deterministic).
2.  For each candidate S_0^A in normalized order:
    a.  Column domains: for each j, the catalogue subset satisfying
        row zero, ``multiply(S_0^A, R) == P_payloads[0][j]``.
    b.  Backtrack through every combination of the S_B column domains
        (column order, domain order — deterministic).
    c.  For each remaining row k, intersect the catalogue candidates
        satisfying ``multiply(L, S_B[j]) == P_payloads[k][j]`` for
        every j against the chosen S_B values.
    d.  Backtrack through all nonempty S_A[k] domains.
    e.  Run a final full-grid consistency check before yielding.

Every yielded assignment satisfies the full grid; the enumeration is
complete over the supplied catalogue and deterministic, so the legacy
"first returned factorization" remains reproducible.  There is no
internal solution-count limit and no truncation path.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_payload_system
#   module_name: payload_system
#   module_kind: engine
#   summary: Exhaustively enumerates every catalogue-bounded (S_A, S_B) assignment satisfying the p x q coupled payload equations, with a first-solution compatibility wrapper.
#   owner: Erin Spencer
#   public_surface: iter_payload_system_solutions, solve_payload_system
#   internal_surface: _normalized_candidates, _globally_consistent
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_v1_ws1_exhaustive_factor_search, ucns_recursive/tests/test_depth2_full_domain.py
#   rollout: default_enabled
#   rollback: revert to the greedy first-quotient solver (reintroduces false SEQ-PRIME)
#   requires: ucns_canonical
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from itertools import product as _iproduct
from typing import Iterator, List, Optional, Tuple

from .canonical import UCNSObject, multiply

__all__ = ["iter_payload_system_solutions", "solve_payload_system"]

PayloadAssignment = Tuple[
    List[Optional[UCNSObject]], List[Optional[UCNSObject]]
]


def _normalized_candidates(
    catalogue: List[Optional[UCNSObject]],
) -> List[Optional[UCNSObject]]:
    """Deterministic unit-first candidate order.

    ``None`` (the unit) appears exactly once and first; remaining
    candidates keep their original relative order with structural
    duplicates removed.  Structural equality, not object identity,
    decides duplication.
    """
    out: List[Optional[UCNSObject]] = [None]
    for cand in catalogue:
        if cand is None:
            continue
        if any(prev is not None and prev == cand for prev in out):
            continue
        out.append(cand)
    return out


def iter_payload_system_solutions(
    P_payloads: List[List[Optional[UCNSObject]]],
    p: int,
    q: int,
    catalogue: List[Optional[UCNSObject]],
) -> Iterator[PayloadAssignment]:
    """Yield every catalogue-bounded (S_A, S_B) satisfying all cells.

    Deterministic and complete over the normalized catalogue; every
    yielded assignment has passed a final full-grid consistency check.
    """
    candidates = _normalized_candidates(catalogue)

    for s0_a in candidates:
        # Column domains from row zero.
        column_domains: List[List[Optional[UCNSObject]]] = []
        feasible = True
        for j in range(q):
            target = P_payloads[0][j]
            domain = [
                cand for cand in candidates
                if multiply(s0_a, cand) == target
            ]
            if not domain:
                feasible = False
                break
            column_domains.append(domain)
        if not feasible:
            continue

        for s_b in _iproduct(*column_domains):
            # Row domains against the chosen S_B values.
            row_domains: List[List[Optional[UCNSObject]]] = []
            rows_ok = True
            for k in range(1, p):
                domain = [
                    cand for cand in candidates
                    if all(
                        multiply(cand, s_b[j]) == P_payloads[k][j]
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
                s_b_list = list(s_b)
                if _globally_consistent(s_a, s_b_list, P_payloads, p, q):
                    yield s_a, s_b_list


def solve_payload_system(
    P_payloads: List[List[Optional[UCNSObject]]],
    p: int,
    q: int,
    catalogue: List[Optional[UCNSObject]],
) -> Optional[PayloadAssignment]:
    """First solution under the deterministic enumeration, or ``None``.

    Compatibility wrapper over :func:`iter_payload_system_solutions`.
    Callers that need completeness must iterate the full iterator; a
    single assignment is never evidence of exhaustion.
    """
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
    """Return True iff multiply(S_A[k], S_B[j]) == P_payloads[k][j] for all k, j."""
    for k in range(p):
        for j in range(q):
            if multiply(S_A[k], S_B[j]) != P_payloads[k][j]:
                return False
    return True
