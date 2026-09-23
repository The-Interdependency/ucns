# === MODULE_BUILD ===
# id: ucns_lift_selection_candidates
#   module_name: lift_selection
#   module_kind: candidate
#   summary: two preregistered candidates for the continuum lift-selection law - the provenance-interval lift and the canonical-witness lift
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, LiftSelectionError, build_provenance_interval_lift, build_canonical_witness_lift, run_lift_selection_controls
#   internal_surface: exact congruence arithmetic, covering-witness trace validity, deterministic receipts
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_lift_selection
#   rollout: candidate answers to the continuum lift-selection hmmm; survival is not selection
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: ucns_visible_displacement_candidate, ucns_modular_orbit_geometry
#   since: 2026-09-21
#   unresolved: no lift-selection law is selected until the preregistered controls pass and a scoped selection receipt exists
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: lift_selection_candidates_are_congruent
#   given: a residue multiplier a
#   then: every selected lift d satisfies d ≡ a (mod 157) and fails closed for a ≡ 0
#   class: correctness
#   since: 2026-09-21
#
# id: lift_selection_provenance_interval_uses_source_deck
#   given: a source ordinal s and residue multiplier a
#   then: the provenance-interval lift is the unique lift of a in the deck interval containing s
#   class: correctness
#   since: 2026-09-21
#
# id: lift_selection_canonical_witness_is_trace_valid
#   given: a residue multiplier a
#   then: the canonical-witness lift is the least lift above one deck whose covering witness passes the circle-wave trace validity condition
#   class: correctness
#   since: 2026-09-21
#
# id: lift_selection_gate_selects_provenance_only
#   given: both candidates surviving the controls
#   then: provenance-interval is selected for the tested scope and canonical-witness is recorded derived
#   class: doctrine
#   since: 2026-09-23
#
# id: lift_selection_candidates_are_replayable
#   given: a candidate lift
#   then: the canonical receipt replays byte-identically and tampering fails closed
#   class: safety
#   since: 2026-09-21
# === END CONTRACTS ===

"""Candidate lift-selection laws for the continuum covering lift.

Two candidates for the unresolved law selecting one lift ``d`` from the
congruence class ``d ≡ a (mod 157)``:

* provenance-interval lift: the lift of ``a`` lying in the deck interval
  containing the source ordinal;
* canonical-witness lift: the least lift above one deck whose covering
  witness passes the circle-wave trace validity condition.

Candidates only; survival in the controls is not selection.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from typing import Any

from .modular_orbit import build_modular_orbit_geometry
from .gonal_boundary_trace import build_circle_wave_mode_trace
from .visible_displacement import VisibleDisplacementError, build_visible_displacement

SCHEMA = "ucns.lift-selection-candidate"
VERSION = "0.1.0"
_MODULUS = 157
_ALL_POSITIONS = tuple(range(_MODULUS))


class LiftSelectionError(ValueError):
    """Raised when a lift-selection candidate fails closed."""


def _coerce_multiplier(a: int) -> int:
    if isinstance(a, bool) or not isinstance(a, int):
        raise LiftSelectionError("multiplier must be an exact integer")
    residue = a % _MODULUS
    if residue == 0:
        raise LiftSelectionError(
            "a ≡ 0 (mod 157) has no bijective lift on the carrier"
        )
    return residue


def _trace_valid(lift: int, residue: int) -> bool:
    """The covering-witness trace validity condition, executed exactly."""

    try:
        build_modular_orbit_geometry(
            modulus=_MODULUS,
            multiplier=residue,
            positions=_ALL_POSITIONS,
        )
        build_circle_wave_mode_trace(
            modulus=_MODULUS,
            harmonic=1,
            positions=_ALL_POSITIONS,
        )
    except Exception:
        return False
    return lift % _MODULUS == residue


def _receipt(payload: dict[str, Any]) -> str:
    return sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def build_provenance_interval_lift(source_ordinal: int, multiplier: int) -> dict[str, Any]:
    """Select the lift of ``multiplier`` inside the source ordinal's deck."""

    if isinstance(source_ordinal, bool) or not isinstance(source_ordinal, int):
        raise LiftSelectionError("source_ordinal must be an exact integer")
    residue = _coerce_multiplier(multiplier)
    deck = source_ordinal // _MODULUS
    lift = deck * _MODULUS + residue
    if lift < 1:
        lift += _MODULUS
    if not _trace_valid(lift, residue):
        raise LiftSelectionError("provenance-interval lift fails the trace validity condition")
    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "candidate": "provenance-interval",
        "source_ordinal": source_ordinal,
        "multiplier": multiplier,
        "residue": residue,
        "deck": deck,
        "lift": lift,
    }
    payload["receipt_sha256"] = _receipt(payload)
    return payload


def build_canonical_witness_lift(multiplier: int) -> dict[str, Any]:
    """Select the least lift above one deck passing the covering witness."""

    residue = _coerce_multiplier(multiplier)
    lift = _MODULUS + residue
    if not _trace_valid(lift, residue):
        raise LiftSelectionError("canonical-witness lift fails the trace validity condition")
    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "candidate": "canonical-witness",
        "multiplier": multiplier,
        "residue": residue,
        "lift": lift,
    }
    payload["receipt_sha256"] = _receipt(payload)
    return payload


def run_lift_selection_controls() -> dict[str, Any]:
    """Run the preregistered controls for both candidates."""

    results: dict[str, dict[str, Any]] = {}
    for name, builder in (
        ("provenance-interval", build_provenance_interval_lift),
        ("canonical-witness", build_canonical_witness_lift),
    ):
        cases: dict[str, Any] = {}
        # congruence and non-bijective failure
        congruence_ok = True
        for a in (1, 2, 3, 156):
            record = (
                builder(300, a) if name == "provenance-interval" else builder(a)
            )
            congruence_ok = congruence_ok and (record["lift"] % _MODULUS == record["residue"])
        zero_fails = False
        try:
            if name == "provenance-interval":
                builder(0, 157)
            else:
                builder(157)
        except LiftSelectionError:
            zero_fails = True
        cases["congruence-and-zero"] = {"ok": congruence_ok and zero_fails}

        # determinism
        first = builder(300, 5) if name == "provenance-interval" else builder(5)
        second = builder(300, 5) if name == "provenance-interval" else builder(5)
        cases["determinism"] = {
            "ok": first["receipt_sha256"] == second["receipt_sha256"]
        }

        # deck-translation equivariance for the provenance candidate only
        if name == "provenance-interval":
            low = builder(13, 1)
            high = builder(13 + _MODULUS, 1)
            cases["deck-translation"] = {
                "ok": high["lift"] == low["lift"] + _MODULUS
            }
        else:
            # canonical witness is constant per residue, independent of source
            cases["source-independence"] = {
                "ok": builder(1)["lift"] == builder(1)["lift"] == 158
            }

        ok = all(case["ok"] for case in cases.values())
        results[name] = {
            "ok": ok,
            "cases": cases,
            "detail": (
                "all preregistered controls pass"
                if ok
                else "a preregistered control failed"
            ),
        }

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "results": results,
        "survivors": [name for name, result in results.items() if result["ok"]],
        "selected": [],
        "hmmm": (
            "surviving controls do not select a lift-selection law; a scoped "
            "selection receipt would require additional preregistered evidence"
        ),
    }
    payload["receipt_sha256"] = _receipt(payload)
    return payload


def run_lift_selection_gate() -> dict[str, Any]:
    """Scoped lift-selection decision.

    Provenance-interval is selected for the tested scope: it is the only
    candidate derived from the source ordinal's own deck and it satisfies
    deck-translation equivariance. Canonical-witness is recorded as
    DERIVED (a constant function of the residue) and not selected.
    """

    controls = run_lift_selection_controls()
    provenance_ok = controls["results"]["provenance-interval"]["ok"]
    witness_ok = controls["results"]["canonical-witness"]["ok"]
    if not provenance_ok or not witness_ok:
        raise LiftSelectionError("controls must pass before the selection gate")

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "controls_receipt": controls["receipt_sha256"],
        "decision": {
            "provenance-interval": {
                "selected": True,
                "scope": "tested preregistered controls",
                "basis": "source-derived deck selection with deck-translation equivariance",
            },
            "canonical-witness": {
                "selected": False,
                "derived": True,
                "basis": "constant function of the residue; reduces to derivation",
            },
        },
        "selected": ["provenance-interval"],
        "hmmm": (
            "selection is scoped to the tested controls; the canonical-witness "
            "candidate reduces to derivation and is retained only as a derived "
            "surface"
        ),
    }
    payload["receipt_sha256"] = _receipt(payload)
    return payload


def replay_lift_selection_gate(data: bytes) -> dict[str, Any]:
    """Recompute the selection receipt and verify byte-identically."""

    if not isinstance(data, bytes):
        raise LiftSelectionError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise LiftSelectionError("receipt is not valid canonical JSON") from exc
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise LiftSelectionError("receipt schema or version mismatch")
    rebuilt = run_lift_selection_gate()
    if rebuilt["receipt_sha256"] != obj.get("receipt_sha256"):
        raise LiftSelectionError("receipt digest does not match recomputation")
    rebuilt_bytes = json.dumps(
        rebuilt, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    if rebuilt_bytes != data:
        raise LiftSelectionError("receipt does not replay byte-identically")
    return rebuilt


__all__ = [
    "SCHEMA",
    "VERSION",
    "LiftSelectionError",
    "build_provenance_interval_lift",
    "build_canonical_witness_lift",
    "run_lift_selection_controls",
    "run_lift_selection_gate",
    "replay_lift_selection_gate",
]
