"""Structural checks for human-facing visualization boundary artifacts.

These checks keep the visualization demo connected to documented research
boundaries without claiming formal proof status.
"""

from pathlib import Path
import csv
import subprocess
import sys
import tempfile
import unittest


class TestVisualizationBoundaryArtifacts(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[2]
        self.visual_dir = self.repo_root / "examples" / "visualization"
        self.readme = self.visual_dir / "README.md"
        self.demo = self.visual_dir / "seed53.html"
        self.unitcircle_dir = self.visual_dir / "unitcircle_prime_geometry"
        self.unitcircle_readme = self.unitcircle_dir / "README.md"
        self.unitcircle_script = self.unitcircle_dir / "gonal_mobius_embedding.py"

    def test_visualization_files_exist(self):
        self.assertTrue(self.visual_dir.is_dir())
        self.assertTrue(self.readme.is_file())
        self.assertTrue(self.demo.is_file())
        self.assertTrue(self.unitcircle_readme.is_file())
        self.assertTrue(self.unitcircle_script.is_file())

    def test_visualization_readme_declares_boundaries(self):
        text = self.readme.read_text(encoding="utf-8")
        self.assertIn("Claim linkage", text)
        self.assertIn("does **not** prove", text)
        self.assertIn("Boundary-object role", text)
        self.assertIn("unresolved constraints", text)

    def test_seed53_demo_has_expected_controls(self):
        html = self.demo.read_text(encoding="utf-8")
        expected_ids = [
            'id="skip"',
            'id="radius"',
            'id="showHepta"',
            'id="showChords"',
            'id="showHull"',
            'id="wrapMode"',
            'id="exportSvg"',
            'id="randomize"',
            'id="ring"',
            'id="unwrap"',
        ]
        for marker in expected_ids:
            with self.subTest(marker=marker):
                self.assertIn(marker, html)

    def test_unitcircle_example_declares_boundaries(self):
        text = self.unitcircle_readme.read_text(encoding="utf-8")
        self.assertIn("What it illustrates", text)
        self.assertIn("What it does not prove", text)
        self.assertIn("does **not** prove", text)
        self.assertIn("UCNS-G / EDCM", text)
        self.assertIn("flip_law_holds", text)

    def test_unitcircle_example_smoke_generates_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "gonal.csv"
            subprocess.run(
                [
                    sys.executable,
                    str(self.unitcircle_script),
                    "--max-value",
                    "12",
                    "--out",
                    str(out),
                ],
                check=True,
                cwd=self.repo_root,
                capture_output=True,
                text=True,
            )
            self.assertTrue(out.is_file())
            with out.open(newline="") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(rows), 11)
            self.assertIn("basin_p3", rows[0])
            self.assertIn("face", rows[0])


if __name__ == "__main__":
    unittest.main()
