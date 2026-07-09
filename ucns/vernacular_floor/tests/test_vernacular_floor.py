# === RATIOS ===
# loc_comments: hmmm
# unresolved: corpus_backed_affix_tests
# === END RATIOS ===
"""Contract tests for the vernacular floor scaffold."""

from __future__ import annotations

import inspect
import sys
import tempfile
import textwrap
import unittest

from ucns.vernacular_floor.a0_public_gonol import A0PublicGonolConstruction, import_a0_public_gonol
from ucns.vernacular_floor.assignment import FloorGonol, assign_from_relations, compose_sentence, identity_holds, origin
from ucns.vernacular_floor.codebook_import import EXPECTED_PUBLIC_GLYPH_COUNT, codebook_from_construction, is_prime, validate_codebook
from ucns.vernacular_floor.floor_artifact import load_floor, write_floor
from ucns.vernacular_floor.floor_build import build_floor
from ucns.vernacular_floor.glyph_axes import glyph_axes_from_codebook, glyph_gonols_from_codebook
from ucns.vernacular_floor.manifest import floor_manifest, unresolved_membership_rule
from ucns.vernacular_floor.oewn_ingest import normalize_edges
from ucns.vernacular_floor.transformation_assembly import OperatorName, emit, recognize, round_trip


class VernacularFloorTests(unittest.TestCase):
    def test_manifest_keeps_membership_hmmm(self) -> None:
        self.assertEqual(floor_manifest().membership_rule, "hmmm")
        with self.assertRaises(NotImplementedError):
            unresolved_membership_rule("run")

    def test_codebook_count_and_primality_are_asserted_after_a0_import(self) -> None:
        glyphs = tuple(chr(0x2500 + i) for i in range(157))
        construction = A0PublicGonolConstruction(
            source_repo="a0-betatest",
            construction_id="EXAMPLE_157",
            glyphs=glyphs,
        )
        self.assertEqual(codebook_from_construction(construction), glyphs)
        self.assertEqual(EXPECTED_PUBLIC_GLYPH_COUNT, 157)
        self.assertTrue(is_prime(len(glyphs)))

    def test_non_a0_codebook_provenance_is_rejected(self) -> None:
        glyphs = tuple(chr(0x2600 + i) for i in range(157))
        construction = A0PublicGonolConstruction(
            source_repo="local-reconstruction",
            construction_id="not-upstream",
            glyphs=glyphs,
        )
        with self.assertRaises(ValueError):
            codebook_from_construction(construction)

    def test_imports_public_gonol_from_a0_betatest_module(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            backend = self._write_fake_a0_backend(tmp)
            for name in list(sys.modules):
                if name == "interdependent_lib" or name.startswith("interdependent_lib."):
                    del sys.modules[name]
            construction = import_a0_public_gonol(backend)
            self.assertEqual(construction.source_module, "interdependent_lib.gonal.gonal")
            self.assertEqual(construction.construction_id, "EXAMPLE_157")
            self.assertEqual(codebook_from_construction(construction), construction.glyphs)

    def _write_fake_a0_backend(self, tmp: str) -> str:
        backend = f"{tmp}/backend"
        package = f"{backend}/interdependent_lib/gonal"
        import os
        os.makedirs(package)
        open(f"{backend}/interdependent_lib/__init__.py", "w", encoding="utf-8").close()
        open(f"{package}/__init__.py", "w", encoding="utf-8").close()
        with open(f"{package}/gonal.py", "w", encoding="utf-8") as handle:
            handle.write(textwrap.dedent(
                """
                EXAMPLE_157 = (" ",) + tuple(chr(0x2700 + i) for i in range(1, 157))
                """
            ))
        return backend

    def test_static_membership_path_has_no_literal_count(self) -> None:
        source = inspect.getsource(unresolved_membership_rule)
        self.assertNotIn("157", source)

    def test_glyph_axes_place_space_at_origin(self) -> None:
        glyphs = (" ",) + tuple(chr(0x2800 + i) for i in range(1, 157))
        axes = glyph_axes_from_codebook(glyphs)
        gonols = glyph_gonols_from_codebook(glyphs)
        self.assertEqual(axes[0].glyph, " ")
        self.assertEqual(axes[0].theta, 0.0)
        self.assertEqual(gonols[" "], origin())
        self.assertEqual(len(axes), 157)

    def test_glyph_axes_reject_missing_origin_space(self) -> None:
        glyphs = tuple(chr(0x2900 + i) for i in range(157))
        with self.assertRaises(ValueError):
            glyph_axes_from_codebook(glyphs)

    def test_origin_identity_and_closure(self) -> None:
        run = assign_from_relations("run", {"hypernym": ["move"], "antonym": ["stop"]})
        speak = FloorGonol("speak", 1.0, 2.0)
        self.assertTrue(identity_holds([run, speak]))
        sentence = compose_sentence([run, speak, origin()])
        self.assertIsInstance(sentence, FloorGonol)

    def test_build_floor_resolves_with_supplied_membership_predicate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            backend = self._write_fake_a0_backend(tmp)
            for name in list(sys.modules):
                if name == "interdependent_lib" or name.startswith("interdependent_lib."):
                    del sys.modules[name]
            graphs = [
                normalize_edges("run", {"hypernym": ["move"]}),
                normalize_edges("quark", {"hypernym": ["particle"]}),
            ]
            result = build_floor(
                graphs,
                lambda lemma, metadata: lemma == "run",
                a0_betatest_path=backend,
            )
            self.assertEqual(len(result.codebook), 157)
            self.assertEqual(result.glyph_axes[0].glyph, " ")
            self.assertEqual([gonol.label for gonol in result.floor], ["run"])

    def test_artifact_round_trip(self) -> None:
        gonols = [FloorGonol("run", 1.0, 2.0), FloorGonol(" ", 0.0, 0.0)]
        with tempfile.NamedTemporaryFile() as handle:
            write_floor(handle.name, gonols)
            self.assertEqual(list(load_floor(handle.name)), gonols)

    def test_operator_variants_are_independent(self) -> None:
        im = OperatorName("im", selection_prefixes=("p", "b", "m"))
        il = OperatorName("il", selection_prefixes=("l",))
        self.assertEqual(emit("proper", [im]), "improper")
        with self.assertRaises(ValueError):
            emit("proper", [il])
        root, ops = recognize("improper", [im, il], ["proper"])
        self.assertEqual(root, "proper")
        self.assertEqual(ops, (im,))
        self.assertTrue(round_trip("improper", [im, il], ["proper"]))


if __name__ == "__main__":
    unittest.main()

# === RATIOS ===
# loc_comments: hmmm
# unresolved: corpus_backed_affix_tests
# === END RATIOS ===
