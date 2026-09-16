# === CHECKS ===
# id: check_lattice_carrier_is_abstract_relation
#   proves: lattice_carrier_is_abstract_relation
#   call: self::test_is_abstract_relation
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_lattice_carrier_derives_from_deck_translations
#   proves: lattice_carrier_derives_from_deck_translations
#   call: self::test_derives_from_deck_translations
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_lattice_carrier_derives_from_modular_orbit
#   proves: lattice_carrier_derives_from_modular_orbit
#   call: self::test_derives_from_modular_orbit
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_lattice_carrier_fails_closed
#   proves: lattice_carrier_fails_closed
#   call: self::test_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_lattice_carrier_candidate
#   proves: geometry_public_surface_includes_lattice_carrier_candidate
#   call: self::test_facade_exports_lattice_carrier
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

import pytest

from ucns import (
    LATTICE_CARRIER_SCHEMA,
    LatticeCarrierError,
    build_lattice_address,
    build_lattice_carrier,
    derive_lattice_from_deck_translations,
    derive_lattice_from_modular_orbit,
    replay_lattice_carrier,
)


def test_is_abstract_relation() -> None:
    record = build_lattice_carrier()
    assert record.schema == LATTICE_CARRIER_SCHEMA
    assert "Q(sqrt2,sqrt3,sqrt5)" in record.hmmm
    assert "abstract" in record.hmmm or "abstract" in LATTICE_CARRIER_SCHEMA


def test_derives_from_deck_translations() -> None:
    derivation = derive_lattice_from_deck_translations()
    assert derivation["group"] == "Z"
    assert derivation["quotient"].startswith("Z/2")
    address = build_lattice_address(5, 157, 160)
    assert address.deck_winding == 1  # 5 mod 2
    assert address.residue == 3  # 160 mod 157


def test_derives_from_modular_orbit() -> None:
    derivation = derive_lattice_from_modular_orbit(157, 1)
    assert derivation["group"] == "Z/157"
    assert derivation["modulus"] == 157
    assert len(derivation["cycles"]) == 157  # identity permutation


def test_fails_closed() -> None:
    with pytest.raises(LatticeCarrierError):
        build_lattice_address(0, 1, 0)
    with pytest.raises(LatticeCarrierError):
        replay_lattice_carrier(b"not json")

    record = build_lattice_carrier(modulus=157, multiplier=1)
    replayed = replay_lattice_carrier(record.receipt_bytes())
    assert replayed == record

    tampered = bytearray(record.receipt_bytes())
    tampered[25] ^= 0x01
    with pytest.raises(LatticeCarrierError):
        replay_lattice_carrier(bytes(tampered))


def test_facade_exports_lattice_carrier() -> None:
    import ucns

    assert hasattr(ucns, "build_lattice_carrier")
    assert hasattr(ucns, "replay_lattice_carrier")
    assert ucns.LATTICE_CARRIER_SCHEMA == LATTICE_CARRIER_SCHEMA
