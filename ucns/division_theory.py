# ratios: loc_comments=139:114 imports_exports=5:3 calls_definitions=57:6
"""
ucns.division_theory
====================
Complete left/right quotient *solution-set* enumeration for ``multiply``.

Division is the inverse problem of the ordered-concatenation product
``A ⊠ B``.  Because ⊠ is not commutative, it splits into two problems:

    left division    solve  A ⊠ X = P  for X, given A and P
    right division   solve  X ⊠ B = P  for X, given B and P

and because ⊠ is **not cancellative** (see ``docs/base-geometry.md`` §5
and ``formal/cancellativity-step1-findings.md``), a quotient — when it
exists — need not be unique.  The greedy single-candidate primitives in
``ucns.left_quotient`` are *sound* (a returned factor always verifies)
but **incomplete** on payload-absorption-ambiguous inputs: the mixed
payload branch of ⊠ (``S ⊗ None = S``) lets several distinct payloads
produce the same product cell, and a greedy row-0 recovery can pick one
that fails global verification.  Counterexample (2026-07-10):

    T = UCNSObject(1, 1, [(0, None)], [0])
    A = UCNSObject(4, 1, [(0, T), (2, None)], [0, 0])
    B = UCNSObject(1, 1, [(0, T)], [0])
    left_quotient(multiply(A, B), A) is None      # misses B

This module closes that gap constructively.  ``left_quotients`` /
``right_quotients`` return the **entire finite solution set**, derived
from three facts proved in ``docs/base-geometry.md`` §5:

    1. Forced host: the top-level angles and faces of any solution are
       uniquely determined by P and the divisor (first block for left
       division, block-leading positions for right division).
    2. Column/row payload systems: each payload slot of a solution must
       simultaneously satisfy one equation per divisor cell; slots are
       independent of each other, so the solution set is the product of
       the per-slot solution sets.
    3. Finiteness: per-slot solution sets are finite and enumerable by
       recursion on the target's payload depth.

Consequences packaged here:

    * solvability: solutions exist iff the length gate, host
      consistency, and every per-slot system are satisfiable;
    * multiplicity: ``len(left_quotients(P, A))`` is exactly the
      product of per-slot solution counts;
    * uniqueness: guaranteed when the divisor is flat (depth 1) —
      flat-divisor cancellativity, ``docs/base-geometry.md`` §5.3.

Solutions are returned as ``UCNSObject`` instances; the identity
solution, when present, appears as the canonical length-1 identity
object.  The ``None`` unit sentinel only appears for ``None`` inputs,
mirroring ``multiply``'s own convention.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: division_theory
#   module_name: division_theory
#   module_kind: engine
#   summary: left/right quotient solvability and multiplicity for multiply - complete finite solution-set enumeration
#   owner: Erin Spencer
#   public_surface: none
#   internal_surface: left_quotients, right_quotients, _left_payload_solutions, _right_payload_solutions, _dedup
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_quotient_solvability
#   rollout: this IS "division and the like"; importable, not re-exported from ucns/__init__
#   rollback: keep ucns.left_quotient greedy primitives as the standing surface
#   requires: ucns_canonical
#   since: 2026-07-10
#   unresolved: none for enumeration; AlignedComplete cancellativity proof remains a formal/ obligation
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: division_theory
#   given: normalized nonempty A, P (left) or B, P (right) of finite depth
#   then:  left_quotients/right_quotients return exactly the set of X with
#          multiply(A, X) == P (resp. multiply(X, B) == P); sound, complete
#          (exhaustively cross-checked on a closed 78-object universe),
#          multiplicity equals the product of per-slot solution counts, and
#          the v0.6 greedy-miss counterexample is recovered
#   class: correctness
#   call:  contracts.test_quotient_solvability.contract_division_theory
# === END CONTRACTS ===

from itertools import product as _iproduct
from typing import List, Optional

from .canonical import UCNSObject, multiply

__all__ = ["left_quotients", "right_quotients", "SolutionLimitExceeded"]

_DEFAULT_LIMIT = 10000


class SolutionLimitExceeded(RuntimeError):
    """The per-level assembled candidate count exceeded ``limit``.

    ``limit`` bounds how many candidate assemblies a single recursion
    level will enumerate; it is not a bound on total recursive work,
    which can still grow with payload nesting depth.  The theory is
    unaffected: solution sets are always finite
    (docs/base-geometry.md §5.2).  Research-scale tool, not a
    performance guarantee.
    """


def _dedup(items: List[Optional[UCNSObject]]) -> List[Optional[UCNSObject]]:
    out: List[Optional[UCNSObject]] = []
    for y in items:
        if any((y is None and z is None)
               or (y is not None and z is not None and y == z)
               for z in out):
            continue
        out.append(y)
    return out


def _left_payload_solutions(
    S: Optional[UCNSObject],
    target: Optional[UCNSObject],
    limit: int,
) -> List[Optional[UCNSObject]]:
    """All y (``None`` = unit payload) with ``S ⊗ y == target``.

    ``⊗`` is the payload-merge branch of ``multiply``: ``None`` acts as
    identity on either side, otherwise ``⊗ = multiply``.
    """
    if S is None:
        return [target]
    out: List[Optional[UCNSObject]] = []
    if target is not None and target == S:
        out.append(None)
    if target is not None:
        out.extend(left_quotients(target, S, limit=limit))
    return _dedup(out)


def _right_payload_solutions(
    S: Optional[UCNSObject],
    target: Optional[UCNSObject],
    limit: int,
) -> List[Optional[UCNSObject]]:
    """All y (``None`` = unit payload) with ``y ⊗ S == target``."""
    if S is None:
        return [target]
    out: List[Optional[UCNSObject]] = []
    if target is not None and target == S:
        out.append(None)
    if target is not None:
        out.extend(right_quotients(target, S, limit=limit))
    return _dedup(out)


def left_quotients(
    P: Optional[UCNSObject],
    A: Optional[UCNSObject],
    limit: int = _DEFAULT_LIMIT,
) -> List[Optional[UCNSObject]]:
    """Every X with ``multiply(A, X) == P``.

    Complete and sound on normalized nonempty finite-depth objects;
    raises :class:`SolutionLimitExceeded` if more than ``limit``
    candidate assemblies would be enumerated.
    """
    if P is None:
        return [None] if A is None else []
    if A is None:
        return [P]
    p, L = len(A.A_plus), len(P.A_plus)
    if p == 0 or L % p != 0:
        return []
    q = L // p
    if q == 0:
        return []

    # Forced host (docs/base-geometry.md §5.1): row k=0 of P is exactly
    # X's host data, gauge-corrected by A's leading face bit.
    x_angles = [angle for angle, _ in P.A_plus[:q]]
    x_faces = [f ^ A.F_plus[0] for f in P.F_plus[:q]]

    # Host consistency across every row.
    for k in range(p):
        alpha_k = A.A_plus[k][0]
        f_k = A.F_plus[k]
        for j in range(q):
            if P.A_plus[k * q + j][0] != (alpha_k + x_angles[j]) % 4:
                return []
            if P.F_plus[k * q + j] != f_k ^ x_faces[j]:
                return []

    # Column payload systems: slot j must satisfy one equation per row.
    columns: List[List[Optional[UCNSObject]]] = []
    for j in range(q):
        cand: Optional[List[Optional[UCNSObject]]] = None
        for k in range(p):
            S_k = A.A_plus[k][1]
            t_kj = P.A_plus[k * q + j][1]
            sols_k = _left_payload_solutions(S_k, t_kj, limit)
            if cand is None:
                cand = sols_k
            else:
                cand = [y for y in cand
                        if any((y is None and z is None)
                               or (y is not None and z is not None and y == z)
                               for z in sols_k)]
            if not cand:
                return []
        columns.append(cand if cand is not None else [])

    total = 1
    for col in columns:
        total *= len(col)
        if total > limit:
            raise SolutionLimitExceeded(
                f"more than {limit} candidate solutions"
            )

    results: List[Optional[UCNSObject]] = []
    for choice in _iproduct(*columns):
        x = UCNSObject(P.n_dec, 1, list(zip(x_angles, list(choice))), x_faces)
        if multiply(A, x) == P:
            results.append(x)
    return results


def right_quotients(
    P: Optional[UCNSObject],
    B: Optional[UCNSObject],
    limit: int = _DEFAULT_LIMIT,
) -> List[Optional[UCNSObject]]:
    """Every X with ``multiply(X, B) == P``.

    Exact dual of :func:`left_quotients`: hosts are forced by the
    block-leading positions ``k*q`` and payload systems run over rows.
    """
    if P is None:
        return [None] if B is None else []
    if B is None:
        return [P]
    q, L = len(B.A_plus), len(P.A_plus)
    if q == 0 or L % q != 0:
        return []
    p = L // q
    if p == 0:
        return []

    x_angles = [P.A_plus[k * q][0] for k in range(p)]
    x_faces = [P.F_plus[k * q] ^ B.F_plus[0] for k in range(p)]

    for k in range(p):
        for j in range(q):
            beta_j = B.A_plus[j][0]
            f_j = B.F_plus[j]
            if P.A_plus[k * q + j][0] != (x_angles[k] + beta_j) % 4:
                return []
            if P.F_plus[k * q + j] != x_faces[k] ^ f_j:
                return []

    rows: List[List[Optional[UCNSObject]]] = []
    for k in range(p):
        cand: Optional[List[Optional[UCNSObject]]] = None
        for j in range(q):
            S_j = B.A_plus[j][1]
            t_kj = P.A_plus[k * q + j][1]
            sols_j = _right_payload_solutions(S_j, t_kj, limit)
            if cand is None:
                cand = sols_j
            else:
                cand = [y for y in cand
                        if any((y is None and z is None)
                               or (y is not None and z is not None and y == z)
                               for z in sols_j)]
            if not cand:
                return []
        rows.append(cand if cand is not None else [])

    total = 1
    for row in rows:
        total *= len(row)
        if total > limit:
            raise SolutionLimitExceeded(
                f"more than {limit} candidate solutions"
            )

    results: List[Optional[UCNSObject]] = []
    for choice in _iproduct(*rows):
        x = UCNSObject(P.n_dec, 1, list(zip(x_angles, list(choice))), x_faces)
        if multiply(x, B) == P:
            results.append(x)
    return results
# ratios: loc_comments=139:114 imports_exports=5:3 calls_definitions=57:6
