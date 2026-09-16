# === CHECKS ===
# id: check_displacement_law_enumerates_declared_candidates
#   proves: displacement_law_enumerates_declared_candidates
#   call: self::test_enumerates_declared_candidates
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_displacement_law_records_every_candidate_subresult
#   proves: displacement_law_records_every_candidate_subresult
#   call: self::test_records_every_candidate_subresult
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_displacement_law_preserves_frame_components
#   proves: displacement_law_preserves_frame_components
#   call: self::test_preserves_frame_components
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_displacement_law_covering_degree_is_explicit
#   proves: displacement_law_covering_degree_is_explicit
#   call: self::test_covering_degree_is_explicit
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_displacement_law_remains_candidate
#   proves: displacement_law_remains_candidate
#   call: self::test_remains_candidate
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_displacement_law_fails_closed
#   proves: displacement_law_fails_closed
#   call: self::test_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_displacement_law_candidates
#   proves: geometry_public_surface_includes_displacement_law_candidates
#   call: self::test_facade_exports_displacement_law
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

from fractions import Fraction

import pytest

from ucns import (
    DISPLACEMENT_LAW_CANDIDATES,
    DISPLACEMENT_LAW_SCHEMA,
    DisplacementLawError,
    build_displacement,
    replay_displacement,
)


def test_enumerates_declared_candidates() -> None:
    assert set(DISPLACEMENT_LAW_CANDIDATES) == {
        "ordered-concatenation",
        "placement-frame",
        "composite-displacement",
    }
    for record in DISPLACEMENT_LAW_CANDIDATES.values():
        assert record["standing"] == "candidate"


def test_records_every_candidate_subresult() -> None:
    record = build_displacement(10, 20, 30)
    concatenation = record.ordered_concatenation
    frame = record.placement_frame

    # ordered concatenation: all three channels contribute turns
    assert concatenation.total_turn == Fraction(60, 157)
    # placement frame: only ordinal carries angle
    assert frame.angle_turn == Fraction(10, 157)
    # both candidate receipts are inside the composite receipt
    assert concatenation.receipt_sha256 in record.receipt_bytes().decode()
    assert frame.receipt_sha256 in record.receipt_bytes().decode()


def test_preserves_frame_components() -> None:
    record = build_displacement(10, 5, 1)
    assert record.placement_frame.radius == pytest.approx(
        1 - __import__("math").exp(-5.0)
    )
    assert record.placement_frame.layer == 1


def test_covering_degree_is_explicit() -> None:
    record = build_displacement(1, 0, 0, covering_degree=158)
    assert record.ordered_concatenation.covering_degree == 158
    assert record.ordered_concatenation.covering_multiplier == 1

    with pytest.raises(DisplacementLawError):
        build_displacement(1, 0, 0, covering_degree=157)


def test_remains_candidate() -> None:
    record = build_displacement(1, 2, 3)
    assert "candidate" in DISPLACEMENT_LAW_SCHEMA
    assert "none of the enumerated displacement-law candidates is ratified" in record.hmmm


def test_fails_closed() -> None:
    with pytest.raises(DisplacementLawError):
        build_displacement(True, 0, 0)  # type: ignore[arg-type]
    with pytest.raises(DisplacementLawError):
        replay_displacement(b"not json")

    record = build_displacement(10, 20, 30, covering_degree=158)
    replayed = replay_displacement(record.receipt_bytes())
    assert replayed == record

    tampered = bytearray(record.receipt_bytes())
    tampered[40] ^= 0x01
    with pytest.raises(DisplacementLawError):
        replay_displacement(bytes(tampered))


def test_facade_exports_displacement_law() -> None:
    import ucns

    assert hasattr(ucns, "build_displacement")
    assert hasattr(ucns, "replay_displacement")
    assert hasattr(ucns, "DISPLACEMENT_LAW_CANDIDATES")
    assert ucns.DISPLACEMENT_LAW_SCHEMA == DISPLACEMENT_LAW_SCHEMA
