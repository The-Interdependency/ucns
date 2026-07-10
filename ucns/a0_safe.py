"""Public facade helpers for UCNS object inspection and factoring."""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_a0_safe
#   module_name: a0_safe
#   module_kind: adapter
#   summary: A0-safe public facade for inspecting, identifying, canonicalizing, and factoring UCNS objects via scoped envelopes.
#   owner: Erin Spencer
#   public_surface: identity, describe, canonical, factor, UCNSObjectRecord, FactorizationResult
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive/tests/test_a0_safe.py
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_object_record, ucns_factorization_result, ucns_serialization, ucns_canonical
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from typing import List, Optional, Union

from .canonical import UCNSObject
from .factorization_result import FactorizationResult, factorization_result
from .object_record import UCNSObjectRecord, object_record
from .serialization import canonical_bytes, canonical_json, stable_hash


def identity(obj: Optional[UCNSObject]) -> str:
    """Return the stable canonical hash for *obj*."""
    return stable_hash(obj)


def describe(obj: Optional[UCNSObject]) -> UCNSObjectRecord:
    """Return an object record for *obj* without running factorization."""
    return object_record(obj)


def canonical(obj: Optional[UCNSObject], *, as_bytes: bool = False) -> Union[str, bytes]:
    """Return canonical JSON text or bytes for *obj*."""
    return canonical_bytes(obj) if as_bytes else canonical_json(obj)


def factor(
    obj: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
) -> FactorizationResult:
    """Return a scoped, certified factorization result envelope.

    The envelope carries the machine-derived certification metadata
    (``negative_result_certified``, ``search_exhausted``,
    ``catalogue_coverage_status``, ``catalogue_fingerprint``,
    ``uncertified_reasons``, …).  There is deliberately no parameter by
    which a caller can assert catalogue completeness: coverage is
    recomputed from the exact catalogue by
    ``ucns.catalogue_certificate``.
    """
    return factorization_result(obj, catalogue=catalogue)


__all__ = [
    "identity",
    "describe",
    "canonical",
    "factor",
    "UCNSObjectRecord",
    "FactorizationResult",
]
