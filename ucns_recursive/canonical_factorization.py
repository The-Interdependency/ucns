"""
Canonical factor selection over catalogue-bounded factorizations.

Fills the hole declared in ``UCNSStore.factor_decompose``'s docstring
("no canonical ordering is defined") with a deterministic, total
selection rule, justified in docs/canonical-factor-selection.md.

Scope discipline (read before extending):

- Enumeration here is LEFT-FACTOR-catalogue-bounded, mirroring
  ``factor_decompose``: candidates ``A`` are drawn from the catalogue
  and ``B = left_quotient(P, A)``. This is COMPLETE for the given
  catalogue per the v0.6 left-quotient completeness result
  (ucns-v06-left-quotient-completeness.md).
- This is a DIFFERENT catalogue semantics from ``factor_search_v08``,
  whose catalogue holds PAYLOAD candidates and assembles factors.
  Canonical selection under payload-catalogue semantics would require
  an enumerating variant of the search engine and remains FRONTIER.
"""

# === MODULE_BUILD ===
# id: ucns_canonical_factor_selection
#   module_name: canonical_factorization
#   module_kind: service
#   summary: Deterministic canonical choice among all catalogue-bounded left-factor factorizations of P, selected by lexicographic canonical-bytes order over a v0.6-complete enumeration.
#   owner: Erin Spencer
#   public_surface: enumerate_factorizations, canonical_factorization, canonical_key, SEQ_PRIME
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive.tests.test_canonical_factorization
#   rollout: additive module; no existing surface modified
#   rollback: remove module and its re-exports
#   requires: ucns_carrier_support_pruning
#   since: 2026-06-10
#   unresolved: canonical selection under payload-catalogue (factor_search_v08) semantics
# === END MODULE_BUILD ===

from typing import Iterable, Iterator, List, Optional, Tuple, Union

from .canonical import UCNSObject, multiply
from .catalogue_pruning import prune_catalogue
from .factor_search_v08 import SEQ_PRIME, is_multiplicative_unit
from .recursive_quotient import left_quotient
from .serialization import canonical_bytes

__all__ = [
    "enumerate_factorizations",
    "canonical_factorization",
    "canonical_key",
]

FactorPair = Tuple[UCNSObject, UCNSObject]


def enumerate_factorizations(
    P: UCNSObject,
    catalogue: Iterable[Optional[UCNSObject]],
    include_trivial: bool = False,
    prune: bool = True,
) -> Iterator[FactorPair]:
    """Yield every (A, B) with ``A`` in *catalogue*, ``B = P / A`` (left
    quotient), and ``multiply(A, B) == P``.

    Mirrors ``UCNSStore.factor_decompose`` (complete for the given
    catalogue per the v0.6 left-quotient completeness result) as a
    store-free generator, with two additions:

    - ``include_trivial=False`` (default) skips pairs where either
      factor is a multiplicative unit, matching the non-triviality
      convention of ``factor_search_v08``. ``factor_decompose`` itself
      does not filter; pass ``include_trivial=True`` for parity with it.
    - ``prune=True`` (default) applies the Carrier-LCM Law pre-filter
      (``catalogue_pruning.prune_catalogue``): sound by the Law, since
      any left factor's carrier support is contained in P's.
    """
    cands: Iterable[Optional[UCNSObject]] = (
        prune_catalogue(P, catalogue) if prune else catalogue
    )
    for A in cands:
        if A is None:
            continue
        B = left_quotient(P, A)
        if B is None:
            continue
        if multiply(A, B) != P:
            continue
        if not include_trivial and (
            is_multiplicative_unit(A) or is_multiplicative_unit(B)
        ):
            continue
        yield A, B


def canonical_key(pair: FactorPair) -> Tuple[bytes, bytes]:
    """Total, equality-respecting order key for a factor pair:
    lexicographic on (canonical_bytes(A), canonical_bytes(B)).

    Canonical serialization mirrors UCNSObject equality (see
    serialization module header), so equal objects get equal keys and
    distinct objects get distinct keys — the order is total and
    collision-free without hashing caveats.
    """
    A, B = pair
    return (canonical_bytes(A), canonical_bytes(B))


def canonical_factorization(
    P: UCNSObject,
    catalogue: Iterable[Optional[UCNSObject]],
    include_trivial: bool = False,
) -> Union[FactorPair, str]:
    """Return THE canonical factorization of ``P`` for the given
    catalogue: the minimum of ``enumerate_factorizations`` under
    ``canonical_key``; ``SEQ_PRIME`` if no factorization exists.

    Determinism (proved in docs/canonical-factor-selection.md): the
    enumerated set is finite and depends only on the catalogue's
    *contents* (pruning and quotienting are pointwise), and the key
    order is total, so the minimum is unique and independent of
    catalogue ordering, iteration order, and process state.
    """
    best: Optional[FactorPair] = None
    best_key: Optional[Tuple[bytes, bytes]] = None
    for pair in enumerate_factorizations(
        P, catalogue, include_trivial=include_trivial
    ):
        k = canonical_key(pair)
        if best_key is None or k < best_key:
            best, best_key = pair, k
    return best if best is not None else SEQ_PRIME
