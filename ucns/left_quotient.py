"""
ucns.left_quotient
============================
Constructive left/right quotient primitives.

Promoted from the v0.6.5 reference snapshot (``ucns-code-v065.py``)
into the canonical package so that callers can query encoded objects
(see ``recursive_codec``) without importing from the snapshot file.

Theorem reference — SCOPE-CORRECTED 2026-07-10
----------------------------------------------
``ucns-v06-completeness-proof.md`` (and its near-identical twin
``ucns-v06-left-quotient-completeness.md``) state:

    Theorem (Left-Quotient Completeness).  Let P, A be normalized
    UCNS objects of finite nesting depth.  If there exists B with
    ``A ⊠ B ≡_seq P``, then ``left_quotient(P, A, catalogue=None)``
    returns an object equivalent to B.

**That statement is false as written.**  It depends on E10.4
cancellativity, which fails for divisors of depth >= 2 (payload
absorption: ``S ⊗ None = S``).  Counterexample (permanent regression in
``contracts/test_quotient_solvability.py``)::

    T = UCNSObject(1, 1, [(0, None)], [0])
    A = UCNSObject(4, 1, [(0, T), (2, None)], [0, 0])
    B = UCNSObject(1, 1, [(0, T)], [0])
    left_quotient(multiply(A, B), A)   # None — misses B

Corrected scope (proofs in ``docs/base-geometry.md`` §5):

- ``left_quotient`` is **sound** unconditionally (phase-3 verification)
  and **complete for flat (depth-1) divisors** — flat-divisor
  cancellativity makes the greedy recovery forced.
- On deeper divisors quotients may be non-unique and the greedy row-0
  payload recovery can pick a candidate that fails global verification.
  Complete solution-set enumeration lives in
  ``ucns.division_theory.left_quotients`` / ``right_quotients``.

Eight lemmas underwrite the original result; Lemma 7 bounds the
recursion at ``1 + d(A)`` stack frames where ``d`` is nesting depth.

Caveats
-------
- ``right_quotient`` is the symmetric dual.  The dual proof was
  asserted-by-symmetry and never written out; in addition to the scope
  correction above, the implementation recovers payloads with the
  *left*-quotient helper where the dual equation needs a right
  quotient, so it misses further solvable instances (observed
  empirically 2026-07-10).  It remains sound.

- ``catalogue`` is optional.  When ``None``, the recursion handles
  finite-depth objects by itself (the proof's claim).  Catalogue
  fallback is an escape hatch for the carrier-widening line and is
  not load-bearing on the proof's verified domain.

This module is intentionally a faithful copy of the snapshot's
primitives — no algorithmic changes — so that anything proved about
the snapshot transfers directly here.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_left_quotient
#   module_name: left_quotient
#   module_kind: engine
#   summary: Constructive left/right quotient primitives implementing the v0.6 left-quotient completeness theorem; recovers B (or A) from a product, else None.
#   owner: Erin Spencer
#   public_surface: left_quotient, right_quotient
#   internal_surface: _left_quotient_payload
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_left_quotient
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical
#   since: 2026-06-02
#   unresolved: v0.6 completeness scope-corrected 2026-07-10 (counterexample; complete on flat divisors only; full enumeration in ucns.division_theory); right_quotient dual additionally uses the left payload helper and misses more
# === END MODULE_BUILD ===

from typing import List, Optional

from .canonical import UCNSObject, is_unit, multiply

__all__ = ["left_quotient", "right_quotient"]


def left_quotient(
    P: Optional[UCNSObject],
    A: Optional[UCNSObject],
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
) -> Optional[UCNSObject]:
    """Constructive left quotient: B such that ``A ⊠ B ≡_seq P``.

    Returns the recovered B if one exists, else ``None``.

    Note: a ``None`` return is *also* the algebraic answer "B = unit"
    in the case where ``A == P`` and the unit is the answer.  Callers
    that need to distinguish "no solution" from "unit is the solution"
    should pre-check ``A == P`` themselves.
    """
    if P is None:
        return None  # no nontrivial factorization of the unit
    if A is None:
        # A is unit: A ⊠ B = B = P, so B = P.
        return P

    p = len(A.A_plus)
    L = len(P.A_plus)
    if p == 0 or L % p != 0:
        return None
    q = L // p

    # Phase 1 — direct host recovery (Lemmas 2, 3 of the proof).
    # Since A's first angle is 0 after normalization, the first block
    # of P (indices 0..q-1) is exactly B's host data.
    B_angles = [angle for angle, _ in P.A_plus[0:q]]
    B_payloads_raw = [payload for _, payload in P.A_plus[0:q]]
    B_faces_raw = P.F_plus[0:q]

    a0_f = A.F_plus[0]
    B_faces = [f ^ a0_f for f in B_faces_raw]

    # Phase 2 — payload recovery (Lemmas 4, 5, 6, 7, 8).
    # For each j, recover S^B_j from P^+[j].payload = S^A_0 ⊠ S^B_j.
    B_payloads: List[Optional[UCNSObject]] = []
    S0_A = A.A_plus[0][1]
    for target in B_payloads_raw:
        if S0_A is None:
            # Lemma 5 base case: unit-leading short-circuit.
            B_payloads.append(target)
        else:
            sub_B = _left_quotient_payload(target, S0_A, catalogue)
            if sub_B is None:
                if target == S0_A:
                    # S^A_0 ⊠ unit = S^A_0; so S^B_j = unit.
                    B_payloads.append(None)
                else:
                    return None
            else:
                B_payloads.append(sub_B)

    # Phase 3 — verification (cancellativity, E10.4).
    B_cand = UCNSObject(P.n_dec, P.n_min, list(zip(B_angles, B_payloads)), B_faces)
    if multiply(A, B_cand) == P:
        if is_unit(B_cand):
            return None
        return B_cand
    return None


def right_quotient(
    P: Optional[UCNSObject],
    B: Optional[UCNSObject],
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
) -> Optional[UCNSObject]:
    """Constructive right quotient: A such that ``A ⊠ B ≡_seq P``.

    Symmetric dual of :func:`left_quotient`.  The dual proof is
    asserted-by-symmetry in the v0.6 packet but not yet written out
    in long form; treat as conjecturally complete.
    """
    if P is None:
        return None
    if B is None:
        return P

    q = len(B.A_plus)
    L = len(P.A_plus)
    if q == 0 or L % q != 0:
        return None
    p = L // q

    # Right quotient: use block-leading positions (j=0) for A.
    A_angles = [P.A_plus[k * q][0] for k in range(p)]
    A_payloads_raw = [P.A_plus[k * q][1] for k in range(p)]
    A_faces_raw = [P.F_plus[k * q] for k in range(p)]

    b0_f = B.F_plus[0]
    A_faces = [f ^ b0_f for f in A_faces_raw]

    A_payloads: List[Optional[UCNSObject]] = []
    S0_B = B.A_plus[0][1]
    for target in A_payloads_raw:
        if S0_B is None:
            A_payloads.append(target)
        else:
            sub_A = _left_quotient_payload(target, S0_B, catalogue)
            if sub_A is None:
                if target == S0_B:
                    A_payloads.append(None)
                else:
                    return None
            else:
                A_payloads.append(sub_A)

    A_cand = UCNSObject(P.n_dec, P.n_min, list(zip(A_angles, A_payloads)), A_faces)
    if multiply(A_cand, B) == P:
        if is_unit(A_cand):
            return None
        return A_cand
    return None


# ---------------------------------------------------------------------
# Internal helper
# ---------------------------------------------------------------------


def _left_quotient_payload(
    target: Optional[UCNSObject],
    S: Optional[UCNSObject],
    catalogue: Optional[List[Optional[UCNSObject]]],
) -> Optional[UCNSObject]:
    """Payload-level quotient: recursive descent with bounded
    catalogue fallback.  See ``left_quotient_payload`` in
    ``ucns-code-v065.py``."""
    if S is None:
        return target
    if catalogue is None:
        catalogue = []
    candidate = left_quotient(target, S, catalogue) if target is not None else None
    if candidate is not None:
        return candidate
    for cand in list(catalogue) + [None]:
        if S is not None and cand is not None:
            prod = multiply(S, cand)
        elif cand is None:
            prod = S
        else:
            prod = cand
        if prod == target:
            return cand
    return None
