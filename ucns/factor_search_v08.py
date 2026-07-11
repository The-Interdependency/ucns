"""
ucns.factor_search_v08
=================================
Witness-matrix recursive quotient solver.

The search is exhaustive over the finite supplied payload catalogue.  For
each host split it iterates every coupled payload assignment and every face
assignment, accepting a factor pair only after exact recomposition.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_factor_search_v08
#   module_name: factor_search_v08
#   module_kind: engine
#   summary: Top-level exhaustive catalogue-bounded witness-matrix factorization solver.
#   owner: Erin Spencer
#   public_surface: factor_search_v08
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_exhaustive_factor_search.py, ucns_recursive/tests/test_depth2_oracle.py
#   rollout: default_enabled
#   rollback: restore the greedy single-assignment solver
#   requires: ucns_canonical, ucns_domains, ucns_host_recovery, ucns_payload_system, ucns_witness_matrix
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from typing import List, Optional, Tuple, Union

from .catalogue_pruning import prune_payload_catalogue
from .canonical import UCNSObject, is_multiplicative_unit, multiply
from .domains import generate_payload_catalogue
from .host_recovery import recover_face_structures, recover_host_angles
from .payload_system import iter_payload_system_solutions
from .witness_matrix import build_witness_matrix

__all__ = ["factor_search_v08"]

FactorResult = Union[Tuple[UCNSObject, UCNSObject], str]
SEQ_PRIME = "SEQ-PRIME"


def factor_search_v08(
    P: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
    prune: bool = True,
) -> FactorResult:
    """Return one exact non-trivial factorization, else ``SEQ-PRIME``.

    ``SEQ-PRIME`` is catalogue-relative.  It is reached only after every
    valid host split, every catalogue-bounded payload assignment, and every
    face assignment has been exhausted.  The length-one split ``1 × 1`` is
    included because recursive non-unit one-cell objects can be composite.
    """
    if catalogue is None:
        catalogue = generate_payload_catalogue()
    if prune:
        catalogue = prune_payload_catalogue(P, catalogue)

    n = len(P.A_plus)

    # Prefer non-left-singleton splits so the historical p=1 fallback does
    # not preempt larger factors.  Always include p=1: when n=1 it is the
    # only split and can contain two recursive non-unit factors.
    split_candidates = list(range(2, n + 1))
    split_candidates.append(1)

    for p in split_candidates:
        if n % p != 0:
            continue
        q = n // p

        A_angles, B_angles = recover_host_angles(P, p, q)
        face_options = recover_face_structures(P, p, q)
        if not face_options:
            continue

        P_payloads = [
            [P.A_plus[k * q + j][1] for j in range(q)]
            for k in range(p)
        ]

        for S_A, S_B in iter_payload_system_solutions(
            P_payloads, p, q, catalogue
        ):
            witness_matrix = build_witness_matrix(S_A, S_B, P_payloads)
            if not witness_matrix.globally_consistent():
                continue

            for A_faces, B_faces in face_options:
                A_candidate = UCNSObject(
                    P.n_dec,
                    P.n_min,
                    list(zip(A_angles, S_A)),
                    A_faces,
                )
                B_candidate = UCNSObject(
                    P.n_dec,
                    P.n_min,
                    list(zip(B_angles, S_B)),
                    B_faces,
                )
                if (
                    is_multiplicative_unit(A_candidate)
                    or is_multiplicative_unit(B_candidate)
                ):
                    continue
                if multiply(A_candidate, B_candidate) == P:
                    return A_candidate, B_candidate

    return SEQ_PRIME
