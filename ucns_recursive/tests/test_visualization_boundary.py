"""Structural checks for human-facing visualization boundary artifacts.

These checks keep the visualization demo connected to documented research
boundaries without claiming formal proof status.
"""

from pathlib import Path
import unittest


class TestVisualizationBoundaryArtifacts(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[2]
        self.visual_dir = self.repo_root / "examples" / "visualization"
        self.readme = self.visual_dir / "README.md"
        self.demo = self.visual_dir / "seed53.html"

    def test_visualization_files_exist(self):
        self.assertTrue(self.visual_dir.is_dir())
        self.assertTrue(self.readme.is_file())
        self.assertTrue(self.demo.is_file())

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


if __name__ == "__main__":
    unittest.main()
