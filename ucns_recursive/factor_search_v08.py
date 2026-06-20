"""
ucns_recursive.factor_search_v08
=================================
Witness-matrix recursive quotient solver.

    factor_search_v08(P) -> (A, B) | "SEQ-PRIME"

Algorithm
---------
For each non-trivial factorisation n = p * q of n = len(P.A_plus):

1. Host recovery - extract the A and B angle sequences from P
   (``host_recovery.recover_host_angles``).

2. Payload system construction - extract the p by q grid of target
   payloads from P and solve the coupled equations
       multiply(S_A[k], S_B[j]) == P_payloads[k][j]
   for all (k, j) simultaneously (``payload_system.solve_payload_system``).

3. Witness-matrix construction plus consistency check - build the full
   p by q witness matrix and call ``WitnessMatrix.globally_consistent()``.
   A candidate is only accepted if all witnesses verify and the matrix
   is row- and column-consistent.

4. Face recovery - enumerate valid face-bit assignments.

5. Exact recomposition verification - the final truth test:
       multiply(A_candidate, B_candidate) == P

   Factorizations where either A or B is in the multiplicative unit
   group (``is_multiplicative_unit`` returns True) are skipped. The
   unit group is broader than the identity: a length-1 object with
   UNIT payload and face bit f=1 is self-inverse, so admitting it as
   a factor would mark every length-at-least-2 product as composite via
   a trivial sign flip. Filtering the full unit group is what makes
   SEQ-PRIME a meaningful predicate.

Loop ordering
-------------
Non-left-singleton factorisations are tried first: p = 2..n. This
includes the right-singleton edge p = n, q = 1. The p=1 left-singleton
case is appended at the end. This ordering matters: for p=1 with
S_A=[None], solve_payload_system always finds a consistent solution
(S_B = P's payload row) via the face-flip path. If p=1 were tried
first it would preempt intended p>=2 factorisations for objects whose
left factor has length at least 2. For n=1 there are no non-trivial
splits.

Soundness
---------
    Unconditional (Theorem 8b): `factor_search_v08` returns `(A, B)` only
    when `multiply(A, B) == P`. Verified at step 5.

Completeness (Theorem N)
------------------------
    If the catalogue C contains every payload appearing recursively in
    some valid non-multiplicative-unit (A, B) with multiply(A, B) = P,
    then factor_search_v08(P, C) returns valid factors.

    In practice:
      - depth-2 targets: C = generate_payload_catalogue() (Lemma 7;
        depth-1 oracle atoms cover all payloads of depth-2 factors).
      - depth-3 asymmetric (depth-3 x depth-<=2): extend C with the
        depth-2 payloads of the depth-3 factor (Theorem 9; 6/6 empirical
        SUCCESS in milliseconds with minimal catalogues).
      - depth-k targets: extend C to include depth-(k-1) payloads of the
        factors. No depth-conditional algorithm changes needed.

    SEQ-PRIME is returned when no non-trivial factorization exists whose
    payloads are all in C.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_factor_search_v08
#   module_name: factor_search_v08
#   module_kind: engine
#   summary: Top-level witness-matrix recursive quotient solver; factor_search_v08(P) returns recovered factors (A, B) or the SEQ-PRIME sentinel.
#   owner: Erin Spencer
#   public_surface: factor_search_v08
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive.tests.test_depth2_oracle
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domains, ucns_host_recovery, ucns_payload_system, ucns_witness_matrix
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from typing import List, Optional, Tuple, Union

from .catalogue_pruning import prune_payload_catalogue
from .canonical import UCNSObject, multiply, is_multiplicative_unit
from .domains import generate_payload_catalogue
from .host_recovery import recover_host_angles, recover_face_structures
from .payload_system import solve_payload_system
from .witness_matrix import build_witness_matrix

__all__ = ["factor_search_v08"]

# Return type: either a factor pair or the primality sentinel
FactorResult = Union[Tuple[UCNSObject, UCNSObject], str]

SEQ_PRIME = "SEQ-PRIME"


def factor_search_v08(
    P: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
    prune: bool = True,
) -> FactorResult:
    """Search for a non-trivial factorisation P = A then B.

    Parameters
    ----------
    P:
        The UCNS object to factor.
    catalogue:
        Payload candidates to use. If ``None`` the frozen-domain
        catalogue from ``domains.generate_payload_catalogue`` is used.
        For depth-3+ targets, extend this catalogue with the depth-2+
        payloads of the expected factors (see Theorem N in
        ``ucns-theorem-n.md``).
    prune:
        When True (default), apply Carrier-LCM-Law payload pruning
        (``catalogue_pruning.prune_payload_catalogue``, Corollary 2 in
        ``docs/carrier-support-pruning.md``): candidates whose carrier
        prime support escapes the union of P's payload-carrier supports
        cannot serve as factor payloads and are dropped before search.
        Sound - completeness is unchanged. Pass ``prune=False`` to
        search the catalogue verbatim.

    Returns
    -------
    ``(A, B)`` if a non-trivial factorisation is found, otherwise the
    string sentinel ``"SEQ-PRIME"``.

    **Non-uniqueness:** the returned pair is the *first* valid
    factorisation found under the current loop ordering (non-left-
    singleton splits p >= 2 first, p = 1 last). Multiple valid
    factorisations may exist for the same ``P``; no canonical choice is
    made. Use ``store.factor_decompose`` with an explicit catalogue to
    enumerate all catalogue-bounded factorisations.
    """
    if catalogue is None:
        catalogue = generate_payload_catalogue()
    if prune:
        catalogue = prune_payload_catalogue(P, catalogue)

    n = len(P.A_plus)

    # Try non-left-singleton factorisations first, including the
    # right-singleton edge p=n, q=1, then the single-cell left factor
    # p=1 as an explicit fallback. See the module docstring for why
    # p=1 must remain last.
    split_candidates = list(range(2, n + 1))
    if n >= 2:
        split_candidates.append(1)

    for p in split_candidates:
        if n % p != 0:
            continue
        q = n // p

        # --- 1. Host recovery ---
        A_angles, B_angles = recover_host_angles(P, p, q)

        # --- 2. Payload system ---
        P_payloads = [
            [P.A_plus[k * q + j][1] for j in range(q)]
            for k in range(p)
        ]
        payload_result = solve_payload_system(P_payloads, p, q, catalogue)
        if payload_result is None:
            continue
        S_A, S_B = payload_result

        # --- 3. Witness-matrix consistency check ---
        wm = build_witness_matrix(S_A, S_B, P_payloads)
        if not wm.globally_consistent():
            continue

        # --- 4. Face recovery ---
        face_options = recover_face_structures(P, p, q)
        if not face_options:
            continue

        # --- 5. Exact recomposition verification ---
        for A_faces, B_faces in face_options:
            A_cand = UCNSObject(
                P.n_dec, P.n_min,
                list(zip(A_angles, S_A)),
                A_faces,
            )
            B_cand = UCNSObject(
                P.n_dec, P.n_min,
                list(zip(B_angles, S_B)),
                B_faces,
            )
            if is_multiplicative_unit(A_cand) or is_multiplicative_unit(B_cand):
                continue
            if multiply(A_cand, B_cand) == P:
                return A_cand, B_cand

    return SEQ_PRIME
