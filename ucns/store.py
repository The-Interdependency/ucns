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
Within the verified domain the completeness theorem (see
``ucns-v06-completeness-proof.md`` and the v0.8.1 oracle theorem)
guarantees:

    For every stored P and query Q, ``left_factors`` returns
    ``(key, remainder)`` for every stored object whose factorization
    includes Q on the left.  No false positives.  No false negatives.

The verified domain is the union of:

    - depth-0 (UNIT)
    - depth-1 (any object): v0.6 left-quotient completeness
    - depth-2 oracle class: v0.8.1 oracle theorem

Outside the verified domain (depth-2 non-oracle, depth ≥ 3),
soundness is preserved but completeness is not proven.  By default
the store accepts any input and reports status via
:meth:`domain_status_of`.  Pass ``enforce_verified_domain=True`` to
the constructor to make insertion fail loudly for out-of-domain
inputs.

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

from .canonical import UCNSObject, multiply
from .domains import is_in_oracle_class, verified_domain_status
from .left_quotient import left_quotient, right_quotient
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
        """Return every stored object for which *query* is a left factor.

        Each match is ``(key, remainder)`` where ``remainder`` is the
        complementary right factor: ``encode(query) ⊠ remainder ==
        stored_object``.  ``remainder`` is ``None`` when the query
        equals the stored object exactly (the unit case).
        """
        Q = recursive_encode(query)
        matches: List[Match] = []
        for key, P in self._objects.items():
            B = left_quotient(P, Q)
            # left_quotient returns None for both "no factorization"
            # and "B is the unit (Q == P)".  Distinguish:
            if B is None:
                if Q == P:
                    matches.append((key, None))
                continue
            matches.append((key, B))
        return matches

    def right_factors(self, query: Any) -> List[Match]:
        """Return every stored object for which *query* is a right factor.

        Each match is ``(key, remainder)`` where ``remainder ⊠
        encode(query) == stored_object``.

        Note: ``right_quotient`` is asserted-by-symmetry in the v0.6
        proof packet but the dual proof is not yet written out.
        Empirically verified on the same domain as left_quotient.
        """
        Q = recursive_encode(query)
        matches: List[Match] = []
        for key, P in self._objects.items():
            A = right_quotient(P, Q)
            if A is None:
                if Q == P:
                    matches.append((key, None))
                continue
            matches.append((key, A))
        return matches

    def is_left_factor(self, query: Any, target_key: Any) -> bool:
        """``True`` iff *query* is a left factor of the object stored
        under *target_key*."""
        Q = recursive_encode(query)
        P = self._objects[target_key]
        if Q == P:
            return True
        return left_quotient(P, Q) is not None

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
        the same ``P`` may admit multiple valid ``(A, B)`` pairs.
        This method returns *all* pairs found for the given catalogue,
        making non-uniqueness explicit in the result.  The caller is
        responsible for choosing among them; no canonical ordering is
        defined.

        Building a covering catalogue is the responsibility of the
        caller; ``ucns.catalogue`` provides enumeration
        helpers for the depth-1 verified domain.
        """
        P = self._objects[target_key]
        decompositions: List[Tuple[UCNSObject, UCNSObject]] = []
        for A in catalogue:
            B = left_quotient(P, A)
            if B is not None and multiply(A, B) == P:
                decompositions.append((A, B))
        return decompositions

    # ------------------------------------------------------------------
    # Repr
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"UCNSStore(n={len(self._objects)})"
