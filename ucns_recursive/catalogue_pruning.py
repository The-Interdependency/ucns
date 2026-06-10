"""
Carrier-support catalogue pruning for the recursive factorization engine.

Implements the Carrier-LCM Law corollary (docs/carrier-support-pruning.md):
for normalized A, B with P = multiply(A, B),

    n_min(P) = lcm(n_min(A), n_min(B))            (Carrier-LCM Law)

hence  n_min(A) | n_min(P)  and  n_min(B) | n_min(P), so the prime support
of any factor's carrier is contained in the prime support of the product's
carrier.  A payload/factor candidate whose carrier has a prime outside
supp(n_min(P)) can never participate in a valid factorization of P and may
be removed from the search catalogue without affecting completeness.
"""

# === MODULE_BUILD ===
# id: ucns_carrier_support_pruning
#   module_name: catalogue_pruning
#   module_kind: service
#   summary: Sound catalogue pre-filter removing factor candidates whose carrier prime support escapes the product carrier's prime support, justified by the Carrier-LCM Law.
#   owner: Erin Spencer
#   public_surface: prime_support, carrier_lcm, prune_catalogue
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive.tests.test_catalogue_pruning
#   rollout: opt-in (callers pass the pruned catalogue to factor_search_v08; default behavior unchanged)
#   rollback: remove module and its re-exports; factor_search_v08 is untouched
#   requires: none
#   since: 2026-06-09
#   unresolved: none
# === END MODULE_BUILD ===

from math import lcm
from typing import Iterable, List, Optional, Set

from .canonical import UCNSObject

__all__ = ["prime_support", "carrier_lcm", "prune_catalogue"]


def prime_support(n: int) -> Set[int]:
    """Return the set of prime divisors of ``n`` (empty for n == 1)."""
    if n < 1:
        raise ValueError(f"carrier must be a positive integer, got {n}")
    support: Set[int] = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            support.add(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        support.add(n)
    return support


def carrier_lcm(A: Optional[UCNSObject], B: Optional[UCNSObject]) -> int:
    """lcm of operand carriers; the Carrier-LCM Law says this equals
    ``multiply(A, B).n_min`` for normalized operands (unit -> carrier 1)."""
    a = 1 if A is None else A.n_min
    b = 1 if B is None else B.n_min
    return lcm(a, b)


def prune_catalogue(
    P: UCNSObject,
    catalogue: Iterable[Optional[UCNSObject]],
) -> List[Optional[UCNSObject]]:
    """Return the sub-catalogue of candidates usable in a factorization of P.

    A candidate ``C`` survives iff ``supp(n_min(C)) <= supp(n_min(P))``,
    i.e. iff its carrier divides some power of ``n_min(P)``.  The unit
    payload (``None``, carrier 1, empty support) always survives.

    Soundness (no valid factorization is lost) is the corollary of the
    Carrier-LCM Law proved in docs/carrier-support-pruning.md.
    """
    p_support = prime_support(P.n_min)
    kept: List[Optional[UCNSObject]] = []
    for cand in catalogue:
        if cand is None:
            kept.append(cand)
            continue
        if prime_support(cand.n_min) <= p_support:
            kept.append(cand)
    return kept
