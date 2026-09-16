# === MODULE_BUILD ===
# id: ucns_lattice_carrier_candidate
#   module_name: lattice_carrier
#   module_kind: candidate
#   summary: abstract lattice/carrier primitive derived from existing UCNS primitives; the discrete address space in which UCNS structures and transitions are placed
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, LatticeCarrierError, LatticeAddress, LatticeCarrierRecord, build_lattice_address, derive_lattice_from_deck_translations, derive_lattice_from_modular_orbit, replay_lattice_carrier
#   internal_surface: canonical address normalization, deck and modular lattice derivation, canonical receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_lattice_carrier
#   rollout: executable candidate abstraction; the algebraic field Q(sqrt2,sqrt3,sqrt5) is explicitly out of scope as a UCNS primitive
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: directed_carrier_floor, ucns_modular_orbit_geometry
#   since: 2026-09-16
#   unresolved: ratification of the abstract lattice relation; the algebraic/Minkowski field remains a downstream implementation candidate
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: lattice_carrier_is_abstract_relation
#   given: the lattice/carrier primitive
#   then: it exposes the abstract lattice relation only, never a specific algebraic number field
#   class: doctrine
#   since: 2026-09-16
#
# id: lattice_carrier_derives_from_deck_translations
#   given: the lifted carrier deck translation
#   then: deck translations form a Z address lattice with two-lap complete return
#   class: correctness
#   requires: two_visible_laps_complete_return
#   since: 2026-09-16
#
# id: lattice_carrier_derives_from_modular_orbit
#   given: an exact modular orbit geometry
#   then: its residues form a Z/m address lattice with exact cycle decomposition
#   class: correctness
#   requires: modular_orbit_action_decomposes_exact_permutation
#   since: 2026-09-16
#
# id: lattice_carrier_fails_closed
#   given: malformed addresses, moduli, or receipts
#   then: construction or replay raises LatticeCarrierError rather than inventing a lattice
#   class: safety
#   since: 2026-09-16
# === END CONTRACTS ===

"""Abstract lattice/carrier primitive.

A discrete address space in which UCNS structures and transitions are placed.
This module exposes the abstract lattice relation only. The algebraic field
``Q(sqrt2, sqrt3, sqrt5)`` is one implementation candidate downstream, not a
UCNS primitive.

UCNS already derives lattice structure from existing primitives:

* the lifted-carrier deck translation forms a ``Z`` address lattice whose
  two-lap complete return is the ``Z/2`` quotient;
* the exact modular orbit forms a ``Z/m`` address lattice with a disjoint
  cycle decomposition.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any

from .modular_orbit import ModularOrbitError, build_modular_orbit_geometry

SCHEMA = "ucns.lattice-carrier-candidate"
VERSION = "0.1.0"

_HMMM = (
    "UCNS already derives lattice structure from deck translations and "
    "modular orbits; the abstract lattice relation is the deck/modular "
    "address lattice, and the algebraic field Q(sqrt2,sqrt3,sqrt5) remains "
    "a downstream implementation candidate, not a UCNS primitive"
)


class LatticeCarrierError(ValueError):
    """Raised when the lattice/carrier candidate fails closed."""


@dataclass(frozen=True)
class LatticeAddress:
    """One canonical abstract lattice address."""

    deck_winding: int
    modulus: int
    residue: int

    def as_dict(self) -> dict[str, int]:
        return {
            "deck_winding": self.deck_winding,
            "modulus": self.modulus,
            "residue": self.residue,
        }


@dataclass(frozen=True)
class LatticeCarrierRecord:
    schema: str
    version: str
    deck_lattice: dict[str, Any]
    modular_lattice: dict[str, Any]
    hmmm: str
    receipt_sha256: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "version": self.version,
            "deck_lattice": self.deck_lattice,
            "modular_lattice": self.modular_lattice,
            "hmmm": self.hmmm,
            "receipt_sha256": self.receipt_sha256,
        }

    def canonical_bytes(self) -> bytes:
        payload = self.as_dict()
        payload.pop("receipt_sha256", None)
        return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def receipt_bytes(self) -> bytes:
        return json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")


def build_lattice_address(
    deck_winding: int,
    modulus: int,
    residue: int,
) -> LatticeAddress:
    """Canonicalize one abstract lattice address."""

    if isinstance(deck_winding, bool) or not isinstance(deck_winding, int):
        raise LatticeCarrierError("deck_winding must be an integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1:
        raise LatticeCarrierError("modulus must be an integer greater than 1")
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise LatticeCarrierError("residue must be an integer")
    return LatticeAddress(
        deck_winding=deck_winding % 2,
        modulus=modulus,
        residue=residue % modulus,
    )


def derive_lattice_from_deck_translations() -> dict[str, Any]:
    """Return the deck-translation lattice derivation."""

    return {
        "group": "Z",
        "quotient": "Z/2 (two-lap complete return)",
        "generator": "one visible lap deck translation",
        "address": "deck_winding modulo 2",
    }


def derive_lattice_from_modular_orbit(modulus: int, multiplier: int) -> dict[str, Any]:
    """Return the modular-orbit lattice derivation for one exact action."""

    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1:
        raise LatticeCarrierError("modulus must be an integer greater than 1")
    if isinstance(multiplier, bool) or not isinstance(multiplier, int):
        raise LatticeCarrierError("multiplier must be an integer")
    try:
        geometry = build_modular_orbit_geometry(
            modulus=modulus,
            multiplier=multiplier,
            positions=range(modulus),
        )
    except ModularOrbitError as exc:
        raise LatticeCarrierError(str(exc)) from exc
    return {
        "group": f"Z/{modulus}",
        "modulus": modulus,
        "multiplier": multiplier % modulus,
        "cycles": [list(cycle) for cycle in geometry.orbits],
        "address": f"residue modulo {modulus}",
    }


def build_lattice_carrier(modulus: int = 157, multiplier: int = 1) -> LatticeCarrierRecord:
    """Derive the abstract lattice/carrier from existing primitives."""

    deck = derive_lattice_from_deck_translations()
    modular = derive_lattice_from_modular_orbit(modulus, multiplier)

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "deck_lattice": deck,
        "modular_lattice": modular,
        "hmmm": _HMMM,
    }
    receipt = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    return LatticeCarrierRecord(
        schema=SCHEMA,
        version=VERSION,
        deck_lattice=deck,
        modular_lattice=modular,
        hmmm=_HMMM,
        receipt_sha256=receipt,
    )


def replay_lattice_carrier(data: bytes) -> LatticeCarrierRecord:
    """Rebuild the lattice derivation record and verify it byte-for-byte."""

    if not isinstance(data, bytes):
        raise LatticeCarrierError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise LatticeCarrierError("receipt is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise LatticeCarrierError("receipt root must be an object")
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise LatticeCarrierError("receipt schema or version mismatch")

    record = build_lattice_carrier(
        modulus=obj["modular_lattice"]["modulus"],
        multiplier=obj["modular_lattice"]["multiplier"],
    )
    if record.receipt_sha256 != obj.get("receipt_sha256"):
        raise LatticeCarrierError("receipt digest does not match replayed lattice")
    if record.receipt_bytes() != data:
        raise LatticeCarrierError("receipt does not replay byte-identically")
    return record


__all__ = [
    "SCHEMA",
    "VERSION",
    "LatticeCarrierError",
    "LatticeAddress",
    "LatticeCarrierRecord",
    "build_lattice_address",
    "derive_lattice_from_deck_translations",
    "derive_lattice_from_modular_orbit",
    "build_lattice_carrier",
    "replay_lattice_carrier",
]
