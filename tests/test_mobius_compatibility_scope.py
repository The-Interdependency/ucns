"""Keep classical disk transforms separate from the public-gonol twist canon."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_legacy_mobius_disk_surface_is_explicitly_noncanonical():
    source = (ROOT / "ucns/mobius.py").read_text(encoding="utf-8")
    required = (
        "classical complex-analytic Möbius transformations",
        "does **not** model the canonical public-gonol Möbius twist",
        "not a public-gonol position",
        "does not preserve the 720-degree orientation return",
        "compatibility_only",
    )
    for phrase in required:
        assert phrase in source


def test_legacy_disk_surface_cannot_reclaim_ucns_frame_authority():
    source = (ROOT / "ucns/mobius.py").read_text(encoding="utf-8")
    forbidden = (
        "home of every UCN",
        "gives the UCN associated with",
        "yields a multi-scale embedding space",
        "models the canonical public-gonol Möbius twist",
    )
    for phrase in forbidden:
        assert phrase not in source
