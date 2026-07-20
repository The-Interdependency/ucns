"""Shared UCNS/METAPAT/EDCM stack contract suite.

Deterministic fixtures for the cross-repository contract: METAPAT
semantic modules and EDCM geometry consumers interoperate with UCNS
only through the official bridge record, and no step of that
interoperation transfers theorem status.

The canonical fixture data lives in
``tests/fixtures/ucns_stack_contract_fixtures.json`` and is owned by
this repository. Sibling repositories may mirror the fixture data only
with a pinned source commit and a drift check against
``expected_stable_hash`` (the drift check is the same recomputation
performed by ``test_fixture_drift_check`` below).

hmmm: ``NA`` at the EDCM boundary is interpreted here as the anchor
count ``len(obj.A_plus)`` (the number of top-level angle anchors the
geometry consumes). This is guaranteed nonzero by the UCNS constructor
invariant that rejects empty object sequences. If EDCM ratifies a
different meaning for ``NA``, update this suite rather than inferring
silently.
"""

import hashlib
import json
import unittest
from pathlib import Path

from ucns import (
    BridgeValidationError,
    UCNSObject,
    evidence_from_bridge_import,
    export_bridge_record,
    import_bridge_record,
    stable_hash,
    ucns_a_to_g,
)
from ucns.geometry_bridge import ThetaDegenerate

FIXTURE_PATH = (
    Path(__file__).parent / "fixtures" / "ucns_stack_contract_fixtures.json"
)

THEOREM_STATUS_VOCABULARY = {
    "DEFENDED",
    "IMPLEMENTED",
    "TEST-BACKED",
    "TEST_BACKED",
    "ORACLE-COMPLETE",
    "ORACLE_COMPLETE",
    "FRONTIER",
    "EXPERIMENTAL",
    "SEQ-PRIME",
}


def _load_fixture() -> dict:
    with FIXTURE_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def _case(name: str) -> dict:
    for case in _load_fixture()["cases"]:
        if case["name"] == name:
            return case
    raise AssertionError(f"fixture case {name!r} missing")


def _record_digest(record: dict) -> str:
    """Provenance-inclusive identity of a bridge record as transmitted."""
    payload = json.dumps(record, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _edcm_boundary_readout(obj: UCNSObject) -> dict:
    """Minimal EDCM-boundary measurement readout from an actual object.

    Mirrors what an EDCM consumer may compute from the public geometry
    surface: the (r, theta, z, w) coordinates plus the anchor count NA.
    Deliberately contains no theorem-status vocabulary.
    """
    try:
        point = ucns_a_to_g(obj)
        theta = point.theta
    except ThetaDegenerate:
        point = None
        theta = None
    readout = {
        "NA": len(obj.A_plus),
        "theta": theta,
        "object_hash": stable_hash(obj),
    }
    if point is not None:
        readout.update({"r": point.r, "z": point.z, "w": point.w})
    return readout


class TestStackContractSuite(unittest.TestCase):
    def test_fixture_is_owned_and_versioned(self) -> None:
        fixture = _load_fixture()
        self.assertEqual(fixture["fixture_schema"], "ucns-stack-contract-fixtures")
        self.assertEqual(fixture["fixture_version"], 1)
        self.assertEqual(fixture["owner"], "The-Interdependency/ucns")

    def test_fixture_drift_check(self) -> None:
        """The drift check sibling mirrors must run: recomputed identity
        matches the pinned expected identity for every case."""
        for case in _load_fixture()["cases"]:
            with self.subTest(case=case["name"]):
                imported = import_bridge_record(case["record"])
                self.assertEqual(
                    stable_hash(imported.obj), case["expected_stable_hash"]
                )
                self.assertEqual(
                    len(imported.obj.A_plus), case["expected_width"]
                )

    def test_metapat_semantic_module_through_official_bridge(self) -> None:
        """(1) A METAPAT semantic module is represented through the
        official bridge and becomes an actual UCNSObject."""
        case = _case("metapat-semantic-module")
        imported = import_bridge_record(case["record"])
        self.assertIs(type(imported.obj), UCNSObject)
        self.assertEqual(
            imported.provenance["source_repo"], "The-Interdependency/metapat"
        )
        self.assertEqual(
            imported.provenance["module"], "semantic-module/coherence-anchor"
        )

    def test_round_trip_preserves_equality_and_stable_hash(self) -> None:
        """(2) Bridge round trip preserves UCNS equality and stable hash."""
        for case in _load_fixture()["cases"]:
            with self.subTest(case=case["name"]):
                first = import_bridge_record(case["record"])
                record_again = export_bridge_record(
                    first.obj,
                    provenance=first.provenance or None,
                    canon_digest=first.canon_digest,
                )
                second = import_bridge_record(record_again)
                self.assertEqual(first.obj, second.obj)
                self.assertEqual(
                    stable_hash(first.obj), stable_hash(second.obj)
                )
                self.assertEqual(record_again, case["record"])

    def test_provenance_survives_without_entering_equality(self) -> None:
        """(3) External canon/provenance fields survive the round trip and
        never alter UCNS equality."""
        case = _case("metapat-semantic-module")
        imported = import_bridge_record(case["record"])
        stripped = import_bridge_record(export_bridge_record(imported.obj))
        self.assertEqual(imported.provenance["canon"], "metapat-canon-2026-07")
        self.assertEqual(imported.canon_digest, "canon-digest-v1")
        self.assertEqual(stripped.provenance, {})
        self.assertEqual(imported.obj, stripped.obj)
        self.assertEqual(stable_hash(imported.obj), stable_hash(stripped.obj))

    def test_edcm_constructs_geometry_from_actual_object(self) -> None:
        """(4) EDCM builds its geometry/readout from the actual UCNSObject
        delivered by the bridge, not from a sibling imitation."""
        case = _case("edcm-geometry-seed")
        imported = import_bridge_record(case["record"])
        readout = _edcm_boundary_readout(imported.obj)
        self.assertEqual(readout["object_hash"], case["expected_stable_hash"])
        self.assertIn("r", readout)
        self.assertIn(readout["z"], (0, 1))
        self.assertIn(readout["w"], (0, 1))

    def test_na_is_nonzero_at_the_edcm_boundary(self) -> None:
        """(5) NA != 0 at the EDCM boundary, guaranteed by the nonempty
        constructor invariant (see module hmmm for the NA interpretation)."""
        for case in _load_fixture()["cases"]:
            with self.subTest(case=case["name"]):
                imported = import_bridge_record(case["record"])
                readout = _edcm_boundary_readout(imported.obj)
                self.assertGreater(readout["NA"], 0)

    def test_no_theorem_status_transfer_into_edcm_output(self) -> None:
        """(6) No UCNS theorem status appears in EDCM measurement output
        merely because UCNS geometry was used."""
        case = _case("metapat-semantic-module")
        imported = import_bridge_record(case["record"])
        readout = _edcm_boundary_readout(imported.obj)
        for key in readout:
            self.assertNotIn(key.upper(), THEOREM_STATUS_VOCABULARY)
            for token in ("status", "certified", "defended", "theorem"):
                self.assertNotIn(token, key.lower())
        for value in readout.values():
            if isinstance(value, str):
                self.assertNotIn(value.upper(), THEOREM_STATUS_VOCABULARY)
        evidence = evidence_from_bridge_import(imported)
        self.assertFalse(evidence.proof_status_attached)

    def test_invalid_bridge_records_fail_closed(self) -> None:
        """(7) Malformed or forged records are rejected fail-closed."""
        base = _case("flat-s2")["record"]
        mutations = [
            {**base, "schema": "not-ucns"},
            {**base, "schema_version": 999},
            {**base, "object": {**base["object"], "cells": []}},
            {**base, "object": {**base["object"], "n_dec": 0}},
            {**base, "theorem_status": "DEFENDED"},
        ]
        for index, bad in enumerate(mutations):
            with self.subTest(index=index):
                with self.assertRaises(BridgeValidationError):
                    import_bridge_record(bad)

    def test_canon_digest_change_is_visible_in_provenance_identity(self) -> None:
        """(8) A manifest/canon digest change changes the transmitted
        record's provenance identity while leaving UCNS identity fixed."""
        case = _case("metapat-semantic-module")
        original = case["record"]
        redigested = dict(original)
        redigested["canon_digest"] = "canon-digest-v2"
        self.assertNotEqual(_record_digest(original), _record_digest(redigested))
        a = import_bridge_record(original)
        b = import_bridge_record(redigested)
        self.assertEqual(a.obj, b.obj)
        self.assertEqual(stable_hash(a.obj), stable_hash(b.obj))
        self.assertNotEqual(a.canon_digest, b.canon_digest)


if __name__ == "__main__":
    unittest.main()
