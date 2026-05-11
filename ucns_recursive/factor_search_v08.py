"""
ucns_recursive.factor_search_v08
=================================
Witness-matrix recursive quotient solver.

    factor_search_v08(P)  →  (A, B) | "SEQ-PRIME"

Algorithm
---------
For each non-trivial factorisation  n = p × q  of  n = len(P.A_plus):

1.  **Host recovery** – extract the A and B angle sequences from P
    (``host_recovery.recover_host_angles``).

2.  **Payload system construction** – extract the p×q grid of target
    payloads from P and solve the coupled equations
        multiply(S_A[k], S_B[j]) == P_payloads[k][j]
    for all (k, j) simultaneously (``payload_system.solve_payload_system``).

3.  **Witness-matrix construction + consistency check** – build the full
    p×q witness matrix and call ``WitnessMatrix.globally_consistent()``.
    A candidate is only accepted if all witnesses verify and the matrix
    is row- and column-consistent.

4.  **Face recovery** – enumerate valid face-bit assignments.

5.  **Exact recomposition verification** – the final truth test:
        multiply(A_candidate, B_candidate) == P

    Factorizations where either A or B is the unit (``is_unit`` returns
    True) are skipped; the loop covers p=1 and p=n-1 so that non-unit
    single-cell factors are reachable.

Completeness
------------
    factor_search_v08 — soundness on all UCNS inputs (Theorem 8b).
    Completeness:
      - depth-2 oracle class: unconditional (Lemma 7).
        Catalogue: generate_payload_catalogue() (depth-1 oracle atoms).
      - depth-n multiplicative class (∀n ≥ 2): unconditional (Theorem N).
        Catalogue: the depth-(n-2) oracle catalogue.
    SEQ-PRIME is returned for objects outside these classes, and for
    objects whose factorizations require a catalogue the caller did
    not provide.
"""

from __future__ import annotations

from typing import List, Optional, Tuple, Union

from .canonical import UCNSObject, multiply, is_unit
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
) -> FactorResult:
    """Search for a non-trivial factorisation  P = A ⨠ B.

    Parameters
    ----------
    P:
        The UCNS object to factor.
    catalogue:
        Payload candidates to use.  If ``None`` the frozen-domain
        catalogue from ``domains.generate_payload_catalogue`` is used.

    Returns
    -------
    ``(A, B)`` if a non-trivial factorisation is found, otherwise the
    string sentinel ``"SEQ-PRIME"``.
    """
    if catalogue is None:
        catalogue = generate_payload_catalogue()

    n = len(P.A_plus)

    # Try all factorisations p*q = n, including p=1 (single-cell factor A).
    # Non-unit filtering is handled by the is_unit check at step 5;
    # starting at p=1 ensures non-unit single-cell objects are reachable.
    for p in range(1, n):
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
            if is_unit(A_cand) or is_unit(B_cand):
                continue
            if multiply(A_cand, B_cand) == P:
                return A_cand, B_cand

    return SEQ_PRIME
