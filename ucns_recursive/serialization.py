"""
ucns_recursive.serialization
============================
Canonical serialization and stable hashing for UCNS recursive objects.

This module mirrors the current UCNSObject equality policy:

- ``n_min`` is part of identity.
- ``n_dec`` is intentionally excluded from identity.
- traversal order is preserved.
- face-state order is preserved.
- payloads are serialized recursively.
- ``None`` is the unit payload/object.

The output is deterministic JSON bytes suitable for storage, audit logs,
content addressing, and A0-facing identity checks.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from typing import Any, Dict, List, Optional

from .canonical import UCNSObject

CANONICAL_SERIALIZATION_VERSION = "ucns-canonical-json-v1"
DEFAULT_HASH_ALGORITHM = "sha256"


def _fraction_to_data(value: Fraction) -> Dict[str, int]:
    """Return a deterministic JSON-compatible representation of a Fraction."""
    if not isinstance(value, Fraction):
        value = Fraction(value)
    return {"num": value.numerator, "den": value.denominator}


def canonical_data(obj: Optional[UCNSObject]) -> Dict[str, Any]:
    """Return canonical JSON-compatible data for *obj*.

    The shape intentionally follows UCNSObject equality rather than object
    construction parameters.  In particular, ``n_dec`` is omitted because
    current equality ignores declared carrier and compares normalized
    intrinsic structure.
    """
    if obj is None:
        return {
            "version": CANONICAL_SERIALIZATION_VERSION,
            "kind": "unit",
        }

    cells: List[Dict[str, Any]] = []
    for index, ((angle, payload), face) in enumerate(zip(obj.A_plus, obj.F_plus)):
        cells.append(
            {
                "index": index,
                "angle": _fraction_to_data(angle),
                "face": int(face),
                "payload": canonical_data(payload),
            }
        )

    return {
        "version": CANONICAL_SERIALIZATION_VERSION,
        "kind": "object",
        "n_min": int(obj.n_min),
        "cells": cells,
    }


def canonical_json(obj: Optional[UCNSObject]) -> str:
    """Return canonical JSON text for *obj*."""
    return json.dumps(
        canonical_data(obj),
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
    )


def canonical_bytes(obj: Optional[UCNSObject]) -> bytes:
    """Return canonical UTF-8 JSON bytes for *obj*."""
    return canonical_json(obj).encode("utf-8")


def stable_hash(
    obj: Optional[UCNSObject],
    algorithm: str = DEFAULT_HASH_ALGORITHM,
) -> str:
    """Return a stable hexadecimal digest for *obj*.

    The default algorithm is SHA-256.  Any hashlib-supported algorithm may be
    supplied by name.
    """
    try:
        h = hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}") from exc
    h.update(canonical_bytes(obj))
    return h.hexdigest()


def stable_hash_bytes(
    obj: Optional[UCNSObject],
    algorithm: str = DEFAULT_HASH_ALGORITHM,
) -> bytes:
    """Return a stable raw digest for *obj*."""
    try:
        h = hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}") from exc
    h.update(canonical_bytes(obj))
    return h.digest()


__all__ = [
    "CANONICAL_SERIALIZATION_VERSION",
    "DEFAULT_HASH_ALGORITHM",
    "canonical_data",
    "canonical_json",
    "canonical_bytes",
    "stable_hash",
    "stable_hash_bytes",
]
