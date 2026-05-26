"""Public facade helpers for UCNS object inspection and factoring."""

from __future__ import annotations

from typing import List, Optional, Union

from ucns_recursive.canonical import UCNSObject
from ucns_recursive.factorization_result import FactorizationResult, factorization_result
from ucns_recursive.object_record import UCNSObjectRecord, object_record
from ucns_recursive.serialization import canonical_bytes, canonical_json, stable_hash


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
    """Return a scoped factorization result envelope for *obj*."""
    return factorization_result(obj, catalogue=catalogue)


__all__ = [
    "identity",
    "describe",
    "canonical",
    "factor",
    "UCNSObjectRecord",
    "FactorizationResult",
]
