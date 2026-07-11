"""
ucns.store
====================
``UCNSStore`` — proof-backed retrieval over recursively encoded data.

Item 5 of the depth-2-walk roadmap delivered the v0.1 surface (any
input accepted; verified-domain claim limited to depth-1).  Item 6
extends the surface with depth-2 oracle dispatch:

- The store can optionally enforce the verified domain at insert
  time via the ``enforce_verified_domain`` constructor flag.
- ``UCNSStore.domain_status_of`` exposes the per-key status string
  (``"depth-0"``, ``"depth-1"``, ``"depth-2-oracle"``,
  ``"depth-2-non-oracle"``, ``"depth-3+"``).
- Out-of-domain inserts under enforcement raise
  :class:`OutOfDomainError`.

What this is
------------
A keyed corpus of ``UCNSObject``\\s (produced by
:func:`ucns.recursive_codec.recursive_encode`) plus
algebraic retrieval primitives backed by the v0.6 / v0.8.1
completeness theorems.

The flagship operation is :meth:`left_factors`, which returns every
stored object ``P`` for which the query ``Q`` is a *left factor* —
together with the *remainder* ``B`` such that ``Q ⊠ B == P``.  Unlike
cosine similarity, this is a structural-divisibility decision, not a
threshold-tuned ranking:

- If the answer is "yes," the remainder is a first-class object
  callers can encode further questions against.
- If the answer is "no," it is "no" — there is no false-positive
  threshold to tune.

Correctness scope
-----------------
Retrieval consumes the **complete quotient solution sets** from
``ucns.division_theory`` (codex-handoff/04; theory in
``docs/base-geometry.md`` §5):

    For every stored P and query Q, ``left_factors`` returns
    ``(key, remainder)`` for **every** valid remainder — multiplicity
    included.  No false positives (each remainder recomposes exactly);
    no greedy single-quotient path remains on any completeness-claiming
    surface.

The historical verified-domain taxonomy (depth-0 / depth-1 /
depth-2-oracle from the v0.6 and v0.8.1 packets) is retained for
insert-time domain *status* reporting and enforcement, not as the
completeness boundary of retrieval.  By default the store accepts any
input and reports status via :meth:`domain_status_of`.  Pass
``enforce_verified_domain=True`` to the constructor to make insertion
fail loudly for out-of-domain inputs.

Retrieval cost
--------------
Linear in corpus size: every query runs ``left_quotient`` against
every stored object.  For small corpora this is fine and honest
about the cost.  Indexing schemes (e.g. hashing on host-angle
prefixes) are deferred until corpus size demands them.

References
----------
- Items 5 and 6 of the depth-2-walk roadmap (May 2026).
- ``ucns-v06-completeness-proof.md`` (Theorem + Decision Corollary).
- ``code/v081-depth2-oracle-theorem.py`` (oracle theorem statement).
- ``recursive_codec`` for the encode/decode pair.
- ``left_quotient`` for the proof-defended primitive.
- ``domains.is_in_oracle_class`` / ``verified_domain_status``.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_store
#   module_name: store
#   module_kind: engine
#   summary: UCNSStore - an in-memory keyed corpus of UCNSObjects with proof-backed algebraic retrieval (left_factors, is_left_factor, factor_decompose) and optional verified-domain enforcement.
#   owner: Erin Spencer
#   public_surface: UCNSStore, Match, OutOfDomainError
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_store
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domains, ucns_left_quotient, ucns_codec
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple

from .canonical import UCNSObject, is_unit, multiply
from .division_theory import left_quotients, right_quotients
from .domains import is_in_oracle_class, verified_domain_status
from .recursive_codec import recursive_decode, recursive_encode

__all__ = ["UCNSStore", "Match", "OutOfDomainError"]


# A retrieval result: the key of a matching object plus the remainder
# B such that  query ⊠ B == matched_object  (for left_factors).
Match = Tuple[Any, Optional[UCNSObject]]


# The verified-domain status strings that pass the enforced insert
# gate.  Out-of-domain statuses (``"depth-2-non-oracle"``,
# ``"depth-3+"``) are rejected.
_VERIFIED_STATUSES = frozenset({"depth-0", "depth-1", "depth-2-oracle"})


class OutOfDomainError(ValueError):
    """Raised by :meth:`UCNSStore.insert` when ``enforce_verified_domain``
    is ``True`` and the encoded object falls outside the verified domain.

    The exception carries the failing key, the encoded object, and the
    status string for callers that want to handle the rejection
    programmatically.
    """

    def __init__(
        self,
        key: Any,
        obj: UCNSObject,
        status: str,
    ) -> None:
        self.key = key
        self.obj = obj
        self.status = status
        super().__init__(
            f"Object for key {key!r} has verified-domain status "
            f"{status!r}; v0.2 enforced inserts accept only "
            f"{sorted(_VERIFIED_STATUSES)}."
        )


class UCNSStore:
    """Keyed corpus of recursively encoded ``UCNSObject``\\s with
    algebraic retrieval.

    Parameters
    ----------
    enforce_verified_domain:
        If ``True``, :meth:`insert` raises :class:`OutOfDomainError`
        for any value whose encoding falls outside the verified
        domain (i.e., depth-2 non-oracle or depth ≥ 3).  Default is
        ``False``, which preserves v0.1 behaviour: any input is
        accepted, with the user responsible for interpreting query
        results outside the verified domain.

    Examples
    --------
    >>> store = UCNSStore()
    >>> store.insert("doc1", b"hello world")
    >>> store.insert("doc2", b"hello there")
    >>> matches = store.left_factors(b"hello ")
    >>> [key for key, _remainder in matches]
    ['doc1', 'doc2']
    """

    def __init__(self, *, enforce_verified_domain: bool = False) -> None:
        self._objects: Dict[Any, UCNSObject] = {}
        self._originals: Dict[Any, Any] = {}
        self._enforce_verified_domain: bool = enforce_verified_domain

    # ------------------------------------------------------------------
    # Insertion / removal
    # ------------------------------------------------------------------

    def insert(self, key: Any, data: Any) -> None:
        """Encode *data* and store it under *key*.  Re-inserting the
        same key overwrites.

        If the store was constructed with
        ``enforce_verified_domain=True``, raises
        :class:`OutOfDomainError` when the encoded object's
        verified-domain status is not in ``{"depth-0", "depth-1",
        "depth-2-oracle"}``.
        """
        obj = recursive_encode(data)
        if self._enforce_verified_domain:
            status = verified_domain_status(obj)
            if status not in _VERIFIED_STATUSES:
                raise OutOfDomainError(key, obj, status)
        self._objects[key] = obj
        self._originals[key] = data

    def remove(self, key: Any) -> None:
        """Remove the entry under *key*.  Raises KeyError if absent."""
        del self._objects[key]
        del self._originals[key]

    def __len__(self) -> int:
        return len(self._objects)

    def __contains__(self, key: Any) -> bool:
        return key in self._objects

    def __iter__(self) -> Iterator[Any]:
        return iter(self._objects)

    def keys(self) -> Iterable[Any]:
        return self._objects.keys()

    # ------------------------------------------------------------------
    # Direct access
    # ------------------------------------------------------------------

    def get_object(self, key: Any) -> UCNSObject:
        """Return the raw ``UCNSObject`` stored under *key*."""
        return self._objects[key]

    def get_decoded(self, key: Any) -> Any:
        """Return the round-trip decoded value stored under *key*.

        Note: round-trip applies the documented codec coercions
        (``str`` round-trips as ``bytes``, etc.).  For the original
        unmodified input, use :meth:`get_original`.
        """
        return recursive_decode(self._objects[key])

    def get_original(self, key: Any) -> Any:
        """Return the original (uncoerced) value passed to
        :meth:`insert`."""
        return self._originals[key]

    def domain_status_of(self, key: Any) -> str:
        """Return the verified-domain status of the object under *key*.

        See :func:`ucns.domains.verified_domain_status` for
        the full status taxonomy.  Useful for auditing what a stored
        corpus actually contains relative to the proof's coverage.
        """
        return verified_domain_status(self._objects[key])

    def is_enforcing_verified_domain(self) -> bool:
        """Return whether this store was configured to reject out-of-domain
        inserts."""
        return self._enforce_verified_domain

    # ------------------------------------------------------------------
    # Algebraic retrieval — the v0.1 deployable surface
    # ------------------------------------------------------------------

    def left_factors(self, query: Any) -> List[Match]:
        """Return every stored object for which *query* is a left factor,
        with **every** valid remainder.

        Each match is ``(key, remainder)`` where ``remainder`` is a
        complementary right factor: ``encode(query) ⊠ remainder ==
        stored_object``.  The complete solution set
        (``ucns.division_theory.left_quotients``) is consumed, so a
        stored key with multiple valid remainders appears once **per
        remainder**, in the enumerators' deterministic order; repeated
        keys are expected and documented.  The unit remainder is
        represented as ``None`` (the query equals the stored object).

        ``SolutionLimitExceeded`` propagates; it is never converted
        into "no match".
        """
        Q = recursive_encode(query)
        matches: List[Match] = []
        for key, P in self._objects.items():
            for B in left_quotients(P, Q):
                if B is None or is_unit(B):
                    matches.append((key, None))
                else:
                    matches.append((key, B))
        return matches

    def right_factors(self, query: Any) -> List[Match]:
        """Return every stored object for which *query* is a right factor,
        with **every** valid remainder.

        Each match is ``(key, remainder)`` where ``remainder ⊠
        encode(query) == stored_object``.  Complete via
        ``ucns.division_theory.right_quotients`` (the exact dual of the
        left enumeration — the historical asserted-by-symmetry greedy
        path is retired); repeated keys carry the multiplicity, and the
        unit remainder is represented as ``None``.
        """
        Q = recursive_encode(query)
        matches: List[Match] = []
        for key, P in self._objects.items():
            for A in right_quotients(P, Q):
                if A is None or is_unit(A):
                    matches.append((key, None))
                else:
                    matches.append((key, A))
        return matches

    def is_left_factor(self, query: Any, target_key: Any) -> bool:
        """``True`` iff *query* is a left factor of the object stored
        under *target_key* — including the unit case (query equals the
        stored object).  Decided on the complete solution set."""
        Q = recursive_encode(query)
        P = self._objects[target_key]
        return bool(left_quotients(P, Q))

    # ------------------------------------------------------------------
    # Catalogue-driven decomposition (Item 5 / E10.8)
    # ------------------------------------------------------------------

    def factor_decompose(
        self,
        target_key: Any,
        catalogue: Iterable[UCNSObject],
    ) -> List[Tuple[UCNSObject, UCNSObject]]:
        """For the object under *target_key*, try every ``A`` in
        *catalogue* and return all ``(A, B)`` pairs with ``A ⊠ B ==
        target``.

        This is the catalogue-bounded form of ``factor_search``.  Per
        the v0.6 proof (§"What This Closes"), catalogue-bounded
        ``factor_search`` is complete up to the catalogue's coverage —
        an "ordinary catalogue-coverage question, not an algebraic
        one."

        **Non-uniqueness:** factorization is generally not unique —
        the same ``P`` may admit multiple valid ``(A, B)`` pairs, and a
        single ``A`` may admit multiple valid ``B``s (⊠ is not
        cancellative).  This method consumes the complete right-factor
        solution set per candidate ``A``
        (``ucns.division_theory.left_quotients``) and returns every
        catalogue-bounded nontrivial pair, structurally deduplicated,
        in deterministic order.  The caller is responsible for choosing
        among them; no canonical choice is defined.

        Building a covering catalogue is the responsibility of the
        caller; ``ucns.catalogue`` provides enumeration
        helpers for the depth-1 verified domain.
        """
        P = self._objects[target_key]
        decompositions: List[Tuple[UCNSObject, UCNSObject]] = []
        for A in catalogue:
            for B in left_quotients(P, A):
                if B is None or is_unit(B):
                    continue  # nontrivial pairs only, as before
                if multiply(A, B) != P:
                    continue
                if any(
                    A == seen_a and B == seen_b
                    for seen_a, seen_b in decompositions
                ):
                    continue  # structural dedup across catalogue entries
                decompositions.append((A, B))
        return decompositions

    # ------------------------------------------------------------------
    # Repr
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"UCNSStore(n={len(self._objects)})"
