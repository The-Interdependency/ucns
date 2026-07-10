"""
ucns.factor_search_v08
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
#   public_surface: factor_search_v08, factor_search_report, FactorSearchReport
#   internal_surface: _search_exhaustive
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_depth2_oracle
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domains, ucns_host_recovery, ucns_payload_system, ucns_witness_matrix
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

from .catalogue_pruning import (
    PRUNING_PRESERVES_COVERAGE,
    PRUNING_RULE_NAME,
    PRUNING_RULE_VERSION,
    prune_payload_catalogue,
)
from .canonical import UCNSObject, multiply, is_multiplicative_unit
from .catalogue_certificate import catalogue_fingerprint
from .domains import generate_payload_catalogue
from .host_recovery import recover_host_angles, recover_face_structures
from .payload_system import iter_payload_system_solutions
from .witness_matrix import build_witness_matrix

__all__ = ["factor_search_v08", "factor_search_report", "FactorSearchReport"]

# Return type: either a factor pair or the primality sentinel
FactorResult = Union[Tuple[UCNSObject, UCNSObject], str]

SEQ_PRIME = "SEQ-PRIME"


@dataclass(frozen=True)
class FactorSearchReport:
    """Raw search outcome plus exhaustion and provenance metadata.

    ``search_exhausted`` is True only when every host split, every
    catalogue-bounded payload assignment, and every face assignment was
    tried and rejected — i.e. exactly the ``SEQ-PRIME`` path.  There is
    no truncation path in the search: any exception propagates and is
    never converted into a negative result.

    The fingerprints bind to the exact catalogue supplied to the search
    (``supplied_catalogue_fingerprint``) and to the post-pruning
    catalogue actually enumerated (``effective_catalogue_fingerprint``).
    """

    kind: str  # "FACTORS" | "SEQ-PRIME"
    factors: Optional[Tuple[UCNSObject, UCNSObject]]
    search_exhausted: bool
    catalogue_source: str  # "default-canonical" | "caller"
    supplied_catalogue_fingerprint: str
    effective_catalogue_fingerprint: str
    pruning_applied: bool
    pruning_rule: str
    pruning_rule_version: str
    pruning_preserves_coverage: bool


def factor_search_report(
    P: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
    prune: bool = True,
) -> FactorSearchReport:
    """Run the exhaustive search and return a provenance-bearing report.

    Same search as :func:`factor_search_v08` (which is a compatibility
    wrapper over this function), with the exhaustion and catalogue
    provenance needed by ``ucns.factorization_result`` for
    negative-result certification.
    """
    source = "default-canonical" if catalogue is None else "caller"
    supplied: List[Optional[UCNSObject]] = (
        generate_payload_catalogue() if catalogue is None else list(catalogue)
    )
    supplied_fp = catalogue_fingerprint(supplied)

    if prune:
        effective = prune_payload_catalogue(P, supplied)
    else:
        effective = supplied
    effective_fp = catalogue_fingerprint(effective)

    raw = _search_exhaustive(P, effective)

    return FactorSearchReport(
        kind="FACTORS" if raw is not None else SEQ_PRIME,
        factors=raw,
        search_exhausted=raw is None,
        catalogue_source=source,
        supplied_catalogue_fingerprint=supplied_fp,
        effective_catalogue_fingerprint=effective_fp,
        pruning_applied=prune,
        pruning_rule=PRUNING_RULE_NAME if prune else "",
        pruning_rule_version=PRUNING_RULE_VERSION if prune else "",
        pruning_preserves_coverage=PRUNING_PRESERVES_COVERAGE if prune else True,
    )


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
    singleton splits p >= 2 first, p = 1 last; payload assignments in
    the deterministic order of ``iter_payload_system_solutions``).
    Multiple valid factorisations may exist for the same ``P``; no
    canonical choice is made. Use ``store.factor_decompose`` with an
    explicit catalogue to enumerate all catalogue-bounded
    factorisations.
    """
    report = factor_search_report(P, catalogue=catalogue, prune=prune)
    if report.factors is not None:
        return report.factors
    return SEQ_PRIME


def _search_exhaustive(
    P: UCNSObject,
    catalogue: List[Optional[UCNSObject]],
) -> Optional[Tuple[UCNSObject, UCNSObject]]:
    """Exhaustive core: every host split × payload assignment × face
    assignment.  Returns the first valid factor pair, or ``None`` after
    demonstrable exhaustion."""
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

        # --- 4 (hoisted). Face recovery: independent of the payload
        # assignment, so enumerate once per host split.
        face_options = recover_face_structures(P, p, q)
        if not face_options:
            continue

        # --- 2. Payload system: iterate EVERY catalogue-bounded
        # assignment.  A rejected candidate (witness inconsistency,
        # unit factor, failed recomposition, …) must never end the
        # split early — the next assignment may succeed.
        P_payloads = [
            [P.A_plus[k * q + j][1] for j in range(q)]
            for k in range(p)
        ]
        for S_A, S_B in iter_payload_system_solutions(
            P_payloads, p, q, catalogue
        ):
            # --- 3. Witness-matrix consistency check ---
            wm = build_witness_matrix(S_A, S_B, P_payloads)
            if not wm.globally_consistent():
                continue

            # --- 5. Exact recomposition verification, over every
            # face assignment for this payload assignment.
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

    # Reached only after every host split, every catalogue-bounded
    # payload assignment, and every face assignment was tried and
    # rejected: a negative here is demonstrable exhaustion, never
    # truncation.
    return None
