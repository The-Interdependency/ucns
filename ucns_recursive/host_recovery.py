"""
ucns_recursive.host_recovery
=============================
Recover the host angle and face structures from a product object P.

When P = multiply(A, B) with |A.A_plus| = p and |B.A_plus| = q, the
combined object P has p*q cells laid out in row-major order:

    P.A_plus[k*q + j]  ←  (alpha_k + beta_j) mod 4,  multiply(S_k^A, S_j^B)

where alpha_k = A.A_plus[k][0] and beta_j = B.A_plus[j][0] (with both
normalised so alpha_0 = beta_0 = 0).

``recover_host_angles`` extracts the angle sequences for candidate A and B.
``recover_face_structures`` enumerates the two valid face-bit assignments
(one degree of freedom: f_0^A ∈ {0, 1}).
"""

from __future__ import annotations

from fractions import Fraction
from typing import List, Optional, Tuple

from .canonical import UCNSObject

__all__ = ["recover_host_angles", "recover_face_structures"]


def recover_host_angles(
    P: UCNSObject, p: int, q: int
) -> Tuple[List[Fraction], List[Fraction]]:
    """Extract the A and B host angle sequences from a normalised P.

    Returns
    -------
    (A_angles, B_angles):
        A_angles[k] = P.A_plus[k*q][0]   for k in range(p)
        B_angles[j] = P.A_plus[j][0]     for j in range(q)

    Both sequences start at 0 (because P is normalised).
    """
    A_angles = [P.A_plus[k * q][0] for k in range(p)]
    B_angles = [P.A_plus[j][0] for j in range(q)]
    return A_angles, B_angles


def recover_face_structures(
    P: UCNSObject, p: int, q: int
) -> List[Tuple[List[int], List[int]]]:
    """Enumerate consistent (A_faces, B_faces) pairs for a given (p, q).

    The face bits satisfy  P.F_plus[k*q + j] = f_k^A XOR f_j^B.
    There is one free bit (f_0^A ∈ {0, 1}), giving at most two solutions.

    Returns a list of (A_faces, B_faces) pairs that are consistent with
    every cell of P.F_plus.  The list may be empty (no consistent
    assignment) or contain 1–2 entries.
    """
    results: List[Tuple[List[int], List[int]]] = []

    for f0_A in (0, 1):
        f0_B = P.F_plus[0] ^ f0_A
        B_faces = [P.F_plus[j] ^ f0_A for j in range(q)]
        A_faces = [P.F_plus[k * q] ^ f0_B for k in range(p)]

        # Verify all p*q face entries
        ok = True
        for k in range(p):
            for j in range(q):
                if (A_faces[k] ^ B_faces[j]) != P.F_plus[k * q + j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            results.append((A_faces, B_faces))

    return results
