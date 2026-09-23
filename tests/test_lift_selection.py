# === CHECKS ===
# id: check_lift_selection_candidates_are_congruent
#   proves: lift_selection_candidates_are_congruent
#   call: self::test_candidates_are_congruent
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_lift_selection_provenance_interval_uses_source_deck
#   proves: lift_selection_provenance_interval_uses_source_deck
#   call: self::test_provenance_interval_uses_source_deck
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_lift_selection_canonical_witness_is_trace_valid
#   proves: lift_selection_canonical_witness_is_trace_valid
#   call: self::test_canonical_witness_is_trace_valid
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_lift_selection_candidates_are_replayable
#   proves: lift_selection_candidates_are_replayable
#   call: self::test_candidates_are_replayable
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: check_lift_selection_gate_selects_provenance_only
#   proves: lift_selection_gate_selects_provenance_only
#   call: self::test_selection_gate_selects_provenance_only
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_geometry_public_surface_includes_lift_selection_candidates
#   proves: geometry_public_surface_includes_lift_selection_candidates
#   call: self::test_facade_exports_lift_selection
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

import json

import pytest

from ucns import (
    replay_lift_selection_gate,
    run_lift_selection_gate,
    LiftSelectionError,
    build_canonical_witness_lift,
    build_provenance_interval_lift,
    run_lift_selection_controls,
)


def test_candidates_are_congruent() -> None:
    for a in (1, 2, 3, 156):
        provenance = build_provenance_interval_lift(300, a)
        witness = build_canonical_witness_lift(a)
        assert provenance["lift"] % 157 == a % 157
        assert witness["lift"] % 157 == a % 157
    with pytest.raises(LiftSelectionError):
        build_provenance_interval_lift(300, 157)
    with pytest.raises(LiftSelectionError):
        build_canonical_witness_lift(157)


def test_provenance_interval_uses_source_deck() -> None:
    low = build_provenance_interval_lift(13, 1)
    high = build_provenance_interval_lift(13 + 157, 1)
    assert high["lift"] == low["lift"] + 157
    assert low["lift"] == 1
    assert build_provenance_interval_lift(158, 1)["lift"] == 158


def test_canonical_witness_is_trace_valid() -> None:
    record = build_canonical_witness_lift(1)
    assert record["lift"] == 158
    assert build_canonical_witness_lift(2)["lift"] == 159


def test_candidates_are_replayable() -> None:
    report = run_lift_selection_controls()
    assert report["survivors"] == ["provenance-interval", "canonical-witness"]
    assert report["selected"] == []
    data = json.dumps(report, sort_keys=True, separators=(",", ":")).encode("utf-8")
    again = run_lift_selection_controls()
    assert again["receipt_sha256"] == report["receipt_sha256"]

    record = build_provenance_interval_lift(300, 7)
    tampered = json.loads(json.dumps(record))
    tampered["lift"] = 999
    import hashlib

    tampered_receipt = hashlib.sha256(
        json.dumps(tampered, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    assert tampered_receipt != record["receipt_sha256"]


def test_facade_exports_lift_selection() -> None:
    import ucns

    assert hasattr(ucns, "build_provenance_interval_lift")
    assert hasattr(ucns, "build_canonical_witness_lift")
    assert hasattr(ucns, "run_lift_selection_controls")
    assert ucns.LIFT_SELECTION_SCHEMA == "ucns.lift-selection-candidate"


def test_selection_gate_selects_provenance_only() -> None:
    from ucns import replay_lift_selection_gate, run_lift_selection_gate

    gate = run_lift_selection_gate()
    assert gate["selected"] == ["provenance-interval"]
    assert gate["decision"]["canonical-witness"]["derived"] is True
    data = json.dumps(gate, sort_keys=True, separators=(",", ":")).encode("utf-8")
    replayed = replay_lift_selection_gate(data)
    assert replayed["receipt_sha256"] == gate["receipt_sha256"]

    tampered = bytearray(data)
    tampered[30] ^= 0x01
    import pytest

    with pytest.raises(Exception):
        replay_lift_selection_gate(bytes(tampered))
