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

**That statement is false as written for the pre-v1.0 greedy
implementation.**  It depended on E10.4 cancellativity, which fails for
divisors of depth >= 2 (payload absorption: ``S ⊗ None = S``).
Counterexample (permanent regression in
``contracts/test_quotient_solvability.py``)::

    T = UCNSObject(1, 1, [(0, None)], [0])
    A = UCNSObject(4, 1, [(0, T), (2, None)], [0, 0])
    B = UCNSObject(1, 1, [(0, T)], [0])
    # pre-v1.0 greedy: left_quotient(multiply(A, B), A) was None

Current implementation (2026-07-10, codex-handoff/04): the singular
functions here are **compatibility selectors** over the complete
solution-set enumerators ``ucns.division_theory.left_quotients`` /
``right_quotients`` (docs/base-geometry.md §5).  They return the first
non-unit solution under the documented deterministic ordering, so the
counterexample above is now recovered; the legacy ``None`` ambiguity
between "no solution" and "only the unit solution" is preserved at this
compatibility boundary.  Callers needing multiplicity use the plural
API.

Caveats
-------
- The pre-v1.0 ``right_quotient`` additionally recovered payloads with
  the *left*-quotient helper where the dual equation needs a right
  quotient; the selector over ``right_quotients`` retires that defect.

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
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_left_quotient
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, division_theory
#   since: 2026-06-02
#   unresolved: none - singular functions are compatibility selectors over ucns.division_theory complete solution sets (codex-handoff/04); the greedy-era scope correction is preserved above as history
# === END MODULE_BUILD ===

from typing import List, Optional

from .canonical import UCNSObject, is_unit
from .division_theory import left_quotients, right_quotients

__all__ = ["left_quotient", "right_quotient"]


def left_quotient(
    P: Optional[UCNSObject],
    A: Optional[UCNSObject],
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
) -> Optional[UCNSObject]:
    """Compatibility left quotient: one B such that ``A ⊠ B ≡_seq P``.

    Reimplemented (2026-07-10, codex-handoff/04) as a deterministic
    selector over the complete solution set
    ``ucns.division_theory.left_quotients``: it returns the **first
    non-unit solution** under the documented solution ordering, or
    ``None`` when no non-unit solution exists.

    Legacy semantics preserved deliberately: a ``None`` return is *also*
    the algebraic answer "B = unit" in the case where ``A == P``.
    Callers that need multiplicity, or the distinction between "no
    solution" and "only the unit solution", must use the plural API
    ``left_quotients`` (re-exported from ``ucns``).

    ``catalogue`` is accepted for signature compatibility and ignored:
    the complete enumeration needs no catalogue fallback.
    ``SolutionLimitExceeded`` from the underlying enumeration
    propagates; it is never converted into ``None``.
    """
    del catalogue  # compatibility only; complete enumeration needs none
    if P is None:
        return None  # no nontrivial factorization of the unit
    if A is None:
        # A is unit: A ⊠ B = B = P, so B = P.
        return P
    for solution in left_quotients(P, A):
        if solution is not None and not is_unit(solution):
            return solution
    return None


def right_quotient(
    P: Optional[UCNSObject],
    B: Optional[UCNSObject],
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
) -> Optional[UCNSObject]:
    """Compatibility right quotient: one A such that ``A ⊠ B ≡_seq P``.

    Exact dual of :func:`left_quotient`, selecting from
    ``ucns.division_theory.right_quotients``.  This retires the
    pre-v1.0 implementation, which recovered payloads with the *left*
    quotient helper where the dual equation needs a right quotient and
    therefore missed solvable instances.
    """
    del catalogue  # compatibility only; complete enumeration needs none
    if P is None:
        return None
    if B is None:
        return P
    for solution in right_quotients(P, B):
        if solution is not None and not is_unit(solution):
            return solution
    return None
