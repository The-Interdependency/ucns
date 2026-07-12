"""
ucns.bridge
===========
Official versioned cross-repository bridge surface.

This module is the single neutral interchange point between UCNS and
sibling repositories (METAPAT semantic-module adapters, EDCM geometry
consumers, interdependent-lib packaging). It defines one versioned,
JSON-compatible bridge record and an import/export adapter pair:

* ``export_bridge_record(obj)`` turns an actual :class:`ucns.UCNSObject`
  into a neutral record carrying declared and intrinsic carriers,
  normalized angles, face bits, and recursive payload records, plus
  optional external provenance tags and a source canon digest.
* ``import_bridge_record(record)`` validates the record fail-closed and
  reconstructs an actual :class:`ucns.UCNSObject` — never a sibling
  imitation object system.

Round trips preserve UCNS equality and the canonical stable hash.
External provenance and canon tags ride in the record only; they never
enter the object and never participate in UCNS equality (no ratified
rule declares otherwise).

Non-transfer rule: successful construction, import, export, or round
trip carries NO theorem status. A bridge record has no field that can
assert catalogue coverage, search provenance, or negative certification;
those live only in the evidence-bearing surfaces
(``ucns.factor_search_v08.factor_search_report``,
``ucns.factorization_result``) and cannot be forged from bridge
metadata. See ``docs/prime-quartet-discontinuity.md``.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_bridge
#   module_name: bridge
#   module_kind: adapter
#   summary: Versioned neutral bridge record plus fail-closed import/export adapter between actual UCNSObjects and sibling repositories, preserving equality and stable hash and carrying provenance without theorem status.
#   owner: Erin Spencer
#   public_surface: BRIDGE_SCHEMA, BRIDGE_SCHEMA_VERSION, BridgeValidationError, BridgeImport, export_bridge_record, import_bridge_record
#   internal_surface: _object_to_data, _object_from_data, _require
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_bridge_round_trip.py, tests/test_stack_contract_suite.py, tests/test_bridge_certification_boundary.py
#   rollout: default_enabled additive public API; sibling repos consume the record shape, not UCNS internals
#   rollback: remove module and its re-exports; sibling adapters fall back to repo-local encodings
#   requires: ucns_canonical, ucns_serialization
#   since: 2026-07-12
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass, field
from fractions import Fraction
from numbers import Integral
from typing import Any, Dict, List, Optional

from .canonical import UCNSObject

__all__ = [
    "BRIDGE_SCHEMA",
    "BRIDGE_SCHEMA_VERSION",
    "BridgeValidationError",
    "BridgeImport",
    "export_bridge_record",
    "import_bridge_record",
]

BRIDGE_SCHEMA = "ucns-bridge-record"
BRIDGE_SCHEMA_VERSION = 1

# Record keys that are algebraic identity input. Everything else in a
# record is either schema framing or external annotation.
_OBJECT_KEYS = frozenset({"n_dec", "n_min", "cells"})
_CELL_KEYS = frozenset({"angle", "face", "payload"})
_RECORD_KEYS = frozenset(
    {"schema", "schema_version", "object", "provenance", "canon_digest"}
)


class BridgeValidationError(ValueError):
    """A bridge record failed closed: malformed, unsupported, or invalid."""


@dataclass(frozen=True)
class BridgeImport:
    """Result of a successful bridge import.

    ``obj`` is an actual :class:`ucns.UCNSObject`. ``provenance`` and
    ``canon_digest`` are external annotations carried alongside the
    object; they are not part of UCNS equality and carry no theorem,
    coverage, or certification status. This type deliberately has no
    status field: consumers needing evidence vocabulary must use
    ``ucns.evidence``.
    """

    obj: UCNSObject
    provenance: Dict[str, Any] = field(default_factory=dict)
    canon_digest: Optional[str] = None


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise BridgeValidationError("Invalid bridge record: " + message)


def _object_to_data(obj: Optional[UCNSObject]) -> Optional[Dict[str, Any]]:
    """Serialize an object (or unit payload) into neutral record data."""
    if obj is None:
        return None
    if len(obj.A_plus) != len(obj.F_plus):
        raise BridgeValidationError(
            "Invalid bridge record: export requires parallel A_plus and "
            f"F_plus (got {len(obj.A_plus)} and {len(obj.F_plus)}); "
            "refusing to truncate a drifted object."
        )
    invalid_faces = [
        f
        for f in obj.F_plus
        if not isinstance(f, Integral)
        or isinstance(f, bool)
        or int(f) not in (0, 1)
    ]
    if invalid_faces:
        raise BridgeValidationError(
            "Invalid bridge record: export requires face bits 0 or 1 "
            f"(got {invalid_faces!r}); refusing to coerce a drifted object."
        )
    cells: List[Dict[str, Any]] = []
    for (angle, payload), face in zip(obj.A_plus, obj.F_plus):
        frac = angle if isinstance(angle, Fraction) else Fraction(angle)
        cells.append(
            {
                "angle": {"num": frac.numerator, "den": frac.denominator},
                "face": int(face),
                "payload": _object_to_data(payload),
            }
        )
    return {"n_dec": int(obj.n_dec), "n_min": int(obj.n_min), "cells": cells}


def _object_from_data(data: Any, path: str) -> UCNSObject:
    """Reconstruct an actual UCNSObject from record data, fail-closed."""
    _require(isinstance(data, dict), f"{path} must be an object mapping")
    unknown = set(data) - _OBJECT_KEYS
    _require(not unknown, f"{path} has unknown keys {sorted(unknown)!r}")
    _require(
        _OBJECT_KEYS <= set(data),
        f"{path} must carry n_dec, n_min, and cells",
    )

    n_dec = data["n_dec"]
    n_min = data["n_min"]
    for name, value in (("n_dec", n_dec), ("n_min", n_min)):
        _require(
            isinstance(value, Integral) and not isinstance(value, bool),
            f"{path}.{name} must be an integer",
        )

    cells = data["cells"]
    _require(isinstance(cells, list) and cells, f"{path}.cells must be a nonempty list")

    a_plus = []
    f_plus = []
    for index, cell in enumerate(cells):
        cell_path = f"{path}.cells[{index}]"
        _require(isinstance(cell, dict), f"{cell_path} must be an object mapping")
        unknown = set(cell) - _CELL_KEYS
        _require(not unknown, f"{cell_path} has unknown keys {sorted(unknown)!r}")
        _require(
            _CELL_KEYS <= set(cell),
            f"{cell_path} must carry angle, face, and payload",
        )

        angle = cell["angle"]
        _require(
            isinstance(angle, dict) and set(angle) == {"num", "den"},
            f"{cell_path}.angle must be {{num, den}}",
        )
        num, den = angle["num"], angle["den"]
        _require(
            isinstance(num, Integral)
            and isinstance(den, Integral)
            and not isinstance(num, bool)
            and not isinstance(den, bool),
            f"{cell_path}.angle num/den must be integers",
        )
        _require(int(den) > 0, f"{cell_path}.angle denominator must be positive")

        payload_data = cell["payload"]
        payload = (
            None
            if payload_data is None
            else _object_from_data(payload_data, f"{cell_path}.payload")
        )
        a_plus.append((Fraction(int(num), int(den)), payload))
        f_plus.append(cell["face"])

    try:
        constructed = UCNSObject(int(n_dec), int(n_min), a_plus, f_plus)
    except (TypeError, ValueError) as exc:
        raise BridgeValidationError(
            f"Invalid bridge record: {path} rejected by UCNS construction: {exc}"
        ) from exc
    # The v1 record explicitly carries the intrinsic carrier; a mismatch
    # against the recomputed value is fixture/canon drift and fails closed
    # rather than being silently normalized away.
    _require(
        constructed.n_min == int(n_min),
        f"{path}.n_min={int(n_min)} does not match the recomputed "
        f"intrinsic carrier {constructed.n_min}",
    )
    return constructed


def export_bridge_record(
    obj: UCNSObject,
    provenance: Optional[Dict[str, Any]] = None,
    canon_digest: Optional[str] = None,
) -> Dict[str, Any]:
    """Export an actual UCNSObject into the neutral versioned record.

    ``provenance`` is an optional mapping of external tags (source repo,
    module name, canon identifiers, ...). It is copied verbatim into the
    record and never affects the object's UCNS identity. It confers no
    theorem, coverage, or certification status. ``canon_digest``
    optionally pins the source canon/manifest digest.
    """
    if not isinstance(obj, UCNSObject):
        raise BridgeValidationError(
            "Invalid bridge record: export requires an actual UCNSObject "
            f"(got {type(obj).__name__}); the unit sentinel has no bridge "
            "record — transmit it as an explicit payload of a carrier "
            "object or by convention on the consumer side."
        )
    if provenance is not None and not isinstance(provenance, dict):
        raise BridgeValidationError(
            "Invalid bridge record: provenance must be a mapping when supplied"
        )
    if canon_digest is not None and not isinstance(canon_digest, str):
        raise BridgeValidationError(
            "Invalid bridge record: canon_digest must be a string when supplied"
        )
    record: Dict[str, Any] = {
        "schema": BRIDGE_SCHEMA,
        "schema_version": BRIDGE_SCHEMA_VERSION,
        "object": _object_to_data(obj),
    }
    if provenance:
        record["provenance"] = dict(provenance)
    if canon_digest is not None:
        record["canon_digest"] = canon_digest
    return record


def import_bridge_record(record: Any) -> BridgeImport:
    """Import a neutral bridge record into an actual UCNSObject.

    Validation is fail-closed: a malformed shape, an unsupported schema
    or version, invalid carriers, invalid faces, or an invalid recursive
    payload record raises :class:`BridgeValidationError`. A successful
    import proves construction only; it carries no theorem status, no
    catalogue coverage, no search provenance, and no negative
    certification, whatever the provenance tags claim.
    """
    _require(isinstance(record, dict), "record must be an object mapping")
    unknown = set(record) - _RECORD_KEYS
    _require(not unknown, f"record has unknown keys {sorted(unknown)!r}")
    _require(record.get("schema") == BRIDGE_SCHEMA, "unsupported schema")
    version = record.get("schema_version")
    _require(
        type(version) is int and version == BRIDGE_SCHEMA_VERSION,
        "unsupported schema_version",
    )
    _require("object" in record, "record must carry an object")

    provenance = record.get("provenance", {})
    _require(
        isinstance(provenance, dict),
        "provenance must be a mapping when present",
    )
    canon_digest = record.get("canon_digest")
    _require(
        canon_digest is None or isinstance(canon_digest, str),
        "canon_digest must be a string when present",
    )

    obj = _object_from_data(record["object"], "object")
    return BridgeImport(
        obj=obj,
        provenance=dict(provenance),
        canon_digest=canon_digest,
    )
