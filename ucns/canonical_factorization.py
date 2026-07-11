"""
Canonical factor selection over catalogue-bounded factorizations.

Fills the hole declared in ``UCNSStore.factor_decompose``'s docstring
("no canonical ordering is defined") with a deterministic, total
selection rule, justified in docs/canonical-factor-selection.md.

Scope discipline (read before extending):

- Enumeration here is LEFT-FACTOR-catalogue-bounded, mirroring
  ``factor_decompose``: candidates ``A`` are drawn from the catalogue
  and every ``B`` in the complete solution set
  ``division_theory.left_quotients(P, A)``. This is COMPLETE for the
  given catalogue by the solution-set enumeration of
  ``docs/base-geometry.md`` §5 (the greedy v0.6 path is retired).
- This is a DIFFERENT catalogue semantics from ``factor_search_v08``,
  whose catalogue holds PAYLOAD candidates and assembles factors.
  Canonical selection under payload-catalogue semantics would require
  an enumerating variant of the search engine and remains FRONTIER.
"""

# === MODULE_BUILD ===
# id: ucns_canonical_factor_selection
#   module_name: canonical_factorization
#   module_kind: service
#   summary: Deterministic canonical choice among all catalogue-bounded left-factor factorizations of P, selected by lexicographic canonical-bytes order over the complete division_theory solution-set enumeration.
#   owner: Erin Spencer
#   public_surface: enumerate_factorizations, canonical_factorization, canonical_key, SEQ_PRIME
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_canonical_factorization
#   rollout: additive module; no existing surface modified
#   rollback: remove module and its re-exports
#   requires: ucns_carrier_support_pruning
#   since: 2026-06-10
#   unresolved: canonical selection under payload-catalogue (factor_search_v08) semantics
# === END MODULE_BUILD ===

from typing import Iterable, Iterator, List, Optional, Tuple, Union

from .canonical import UCNSObject, is_multiplicative_unit, multiply
from .catalogue_pruning import prune_catalogue
from .canonical import is_unit
from .division_theory import left_quotients
from .factor_search_v08 import SEQ_PRIME
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
    """Yield every (A, B) with ``A`` in *catalogue*, ``B`` in the
    complete left-quotient solution set of ``P`` by ``A``, and
    ``multiply(A, B) == P``.

    Mirrors ``UCNSStore.factor_decompose`` (complete for the given
    catalogue via ``division_theory.left_quotients``) as a store-free
    generator, with two additions:

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
    seen: list = []
    for A in cands:
        if A is None:
            continue
        # Complete solution set per candidate A (codex-handoff/04): a
        # single A may admit multiple valid Bs under non-cancellative ⊠.
        for B in left_quotients(P, A):
            if B is None or is_unit(B):
                continue
            if multiply(A, B) != P:
                continue
            if not include_trivial and (
                is_multiplicative_unit(A) or is_multiplicative_unit(B)
            ):
                continue
            if any(A == sa and B == sb for sa, sb in seen):
                continue
            seen.append((A, B))
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
