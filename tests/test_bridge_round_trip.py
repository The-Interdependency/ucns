"""Round-trip and fail-closed tests for the official bridge surface."""

import copy
import json
import unittest
from fractions import Fraction

from ucns import (
    BRIDGE_SCHEMA,
    BRIDGE_SCHEMA_VERSION,
    BridgeImport,
    BridgeValidationError,
    UCNSObject,
    UNIT,
    export_bridge_record,
    import_bridge_record,
    stable_hash,
)

S2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
DEPTH1 = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 1])
DEPTH2 = UCNSObject(4, 4, [(Fraction(0), DEPTH1), (Fraction(1, 2), S2)], [0, 0])


class TestBridgeRoundTrip(unittest.TestCase):
    def test_round_trip_preserves_equality_and_stable_hash(self) -> None:
        for obj in (S2, DEPTH1, DEPTH2):
            with self.subTest(obj=repr(obj)):
                record = export_bridge_record(obj)
                imported = import_bridge_record(record)
                self.assertIsInstance(imported, BridgeImport)
                self.assertIsInstance(imported.obj, UCNSObject)
                self.assertEqual(imported.obj, obj)
                self.assertEqual(stable_hash(imported.obj), stable_hash(obj))

    def test_round_trip_preserves_declared_carrier(self) -> None:
        wide = UCNSObject(8, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        imported = import_bridge_record(export_bridge_record(wide))
        self.assertEqual(imported.obj.n_dec, 8)
        self.assertEqual(imported.obj, wide)

    def test_record_is_json_compatible(self) -> None:
        record = export_bridge_record(DEPTH2, provenance={"tag": "x"})
        rebuilt = json.loads(json.dumps(record))
        imported = import_bridge_record(rebuilt)
        self.assertEqual(imported.obj, DEPTH2)

    def test_provenance_and_canon_digest_survive_without_touching_identity(self) -> None:
        provenance = {"source_repo": "metapat", "module": "semantic/x"}
        record = export_bridge_record(
            DEPTH1, provenance=provenance, canon_digest="digest-1"
        )
        imported = import_bridge_record(record)
        self.assertEqual(imported.provenance, provenance)
        self.assertEqual(imported.canon_digest, "digest-1")
        bare = import_bridge_record(export_bridge_record(DEPTH1))
        self.assertEqual(imported.obj, bare.obj)
        self.assertEqual(stable_hash(imported.obj), stable_hash(bare.obj))

    def test_export_import_export_is_stable(self) -> None:
        record = export_bridge_record(DEPTH2, provenance={"a": 1})
        again = export_bridge_record(
            import_bridge_record(record).obj, provenance={"a": 1}
        )
        self.assertEqual(record, again)


class TestBridgeFailClosed(unittest.TestCase):
    def _valid_record(self) -> dict:
        return export_bridge_record(DEPTH1)

    def test_rejects_non_mapping_record(self) -> None:
        for bad in (None, [], "record", 7):
            with self.subTest(bad=bad):
                with self.assertRaises(BridgeValidationError):
                    import_bridge_record(bad)

    def test_rejects_unsupported_schema(self) -> None:
        record = self._valid_record()
        record["schema"] = "edcm-imitation-record"
        with self.assertRaisesRegex(BridgeValidationError, "unsupported schema"):
            import_bridge_record(record)

    def test_rejects_unsupported_schema_version(self) -> None:
        record = self._valid_record()
        record["schema_version"] = BRIDGE_SCHEMA_VERSION + 1
        with self.assertRaisesRegex(
            BridgeValidationError, "unsupported schema_version"
        ):
            import_bridge_record(record)

    def test_rejects_coerced_schema_version_types(self) -> None:
        """True and 1.0 compare equal to 1 in Python; the versioned
        bridge rejects them instead of normalizing into v1."""
        for version in (True, 1.0, "1", None):
            record = self._valid_record()
            record["schema_version"] = version
            with self.subTest(version=version):
                with self.assertRaisesRegex(
                    BridgeValidationError, "unsupported schema_version"
                ):
                    import_bridge_record(record)

    def test_rejects_unknown_top_level_keys(self) -> None:
        record = self._valid_record()
        record["negative_result_certified"] = True
        with self.assertRaisesRegex(BridgeValidationError, "unknown keys"):
            import_bridge_record(record)

    def test_rejects_missing_object(self) -> None:
        record = self._valid_record()
        del record["object"]
        with self.assertRaises(BridgeValidationError):
            import_bridge_record(record)

    def test_rejects_empty_cells(self) -> None:
        record = self._valid_record()
        record["object"]["cells"] = []
        with self.assertRaisesRegex(BridgeValidationError, "nonempty"):
            import_bridge_record(record)

    def test_rejects_invalid_carriers(self) -> None:
        for field, value in (("n_dec", 0), ("n_dec", -2), ("n_min", 0)):
            record = self._valid_record()
            record["object"][field] = value
            with self.subTest(field=field, value=value):
                with self.assertRaises(BridgeValidationError):
                    import_bridge_record(record)

    def test_rejects_non_multiple_declared_carrier(self) -> None:
        record = self._valid_record()
        record["object"]["n_dec"] = 3  # n_min of DEPTH1 is 2
        with self.assertRaisesRegex(
            BridgeValidationError, "rejected by UCNS construction"
        ):
            import_bridge_record(record)

    def test_rejects_invalid_faces(self) -> None:
        for face in (2, -1, "0", 0.5, None):
            record = self._valid_record()
            record["object"]["cells"][0]["face"] = face
            with self.subTest(face=face):
                with self.assertRaises(BridgeValidationError):
                    import_bridge_record(record)

    def test_rejects_invalid_angles(self) -> None:
        for angle in ({"num": 1}, {"num": 1, "den": 0}, {"num": "1", "den": 2}, 0.25):
            record = self._valid_record()
            record["object"]["cells"][0]["angle"] = angle
            with self.subTest(angle=angle):
                with self.assertRaises(BridgeValidationError):
                    import_bridge_record(record)

    def test_rejects_unreduced_angle_fractions(self) -> None:
        """{num: 2, den: 2} equals 1 but is not the exact v1 shape; the
        bridge rejects it instead of silently rewriting on re-export."""
        record = self._valid_record()
        cell = record["object"]["cells"][1]  # angle 1/1 on DEPTH1
        cell["angle"] = {
            "num": cell["angle"]["num"] * 2,
            "den": cell["angle"]["den"] * 2,
        }
        with self.assertRaisesRegex(
            BridgeValidationError, "not in reduced"
        ):
            import_bridge_record(record)

    def test_rejects_invalid_recursive_payload_records(self) -> None:
        record = self._valid_record()
        record["object"]["cells"][0]["payload"] = {"cells": []}
        with self.assertRaises(BridgeValidationError):
            import_bridge_record(record)

        record = self._valid_record()
        deep = copy.deepcopy(record["object"]["cells"][0]["payload"])
        deep["cells"][0]["face"] = 3
        record["object"]["cells"][0]["payload"] = deep
        with self.assertRaises(BridgeValidationError):
            import_bridge_record(record)

    def test_rejects_corrupted_intrinsic_carrier(self) -> None:
        """A positive-but-wrong n_min is canon drift, not normalizable."""
        record = self._valid_record()
        record["object"]["n_min"] = 1  # recomputed intrinsic carrier is 2
        with self.assertRaisesRegex(
            BridgeValidationError, "does not match the recomputed"
        ):
            import_bridge_record(record)

    def test_export_rejects_drifted_parallel_sequences(self) -> None:
        """A mutated object with mismatched A_plus/F_plus fails closed
        instead of being silently truncated by zip."""
        drifted = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
        drifted.F_plus = [0, 0, 1]
        with self.assertRaisesRegex(BridgeValidationError, "parallel"):
            export_bridge_record(drifted)

    def test_export_rejects_drifted_face_bits(self) -> None:
        """Same-length but invalid mutated face data fails closed
        instead of being coerced through int()."""
        for faces in (["0", 0], [0, 2], [0, None], [True, 0]):
            drifted = UCNSObject(
                2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0]
            )
            drifted.F_plus = faces
            with self.subTest(faces=faces):
                with self.assertRaisesRegex(
                    BridgeValidationError, "face bits"
                ):
                    export_bridge_record(drifted)

    def test_export_rejects_non_json_provenance(self) -> None:
        """Provenance that a JSON encoder would fail on or silently
        rewrite never enters the official record."""
        for provenance in (
            {"tags": {"x"}},            # set: not JSON-serializable
            {1: "x"},                   # non-string key: silently stringified
            {"pair": (1, 2)},           # tuple: silently rewritten to a list
            {"nan": float("nan")},      # NaN: not valid JSON
        ):
            with self.subTest(provenance=provenance):
                with self.assertRaises(BridgeValidationError):
                    export_bridge_record(DEPTH1, provenance=provenance)

    def test_export_rejects_non_objects(self) -> None:
        for bad in (None, "S2", 4, {"schema": BRIDGE_SCHEMA}):
            with self.subTest(bad=bad):
                with self.assertRaises(BridgeValidationError):
                    export_bridge_record(bad)

    def test_bridge_import_result_has_no_status_fields(self) -> None:
        """Successful construction or round trip carries no theorem status."""
        imported = import_bridge_record(self._valid_record())
        field_names = set(imported.__dataclass_fields__)
        self.assertEqual(field_names, {"obj", "provenance", "canon_digest"})
        for forbidden in (
            "status",
            "certified",
            "coverage",
            "theorem",
            "defended",
        ):
            for name in field_names:
                self.assertNotIn(forbidden, name.lower())


if __name__ == "__main__":
    unittest.main()
