from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_public_gonol_canon_is_stated_on_authoritative_surfaces():
    required = {
        "README.md": (
            "Public gonol canon",
            "Position `0` is SPACE/ZERO",
            "fixed origin for the entire system",
        ),
        "docs/public-gonol.md": (
            "SPACE",
            "ZERO",
            "Möbius twist point",
            "the seam",
            "the origin",
            "only always-known character",
            "perm[0] == 0",
        ),
        "docs/base-geometry.md": (
            "The carrier in this proof surface is not the public gonol",
            "Object-relative first-angle normalization does not act on, move, or",
            "public-gonol SPACE/ZERO twist origin",
        ),
        "ucns-spec.md": (
            "The public gonol implemented in `a0-betatest@7af8deb` is canon for UCNS",
            "position `0` is SPACE/ZERO",
            "No continuous-angle bridge from the public gonol is established here",
        ),
        "docs/claims-ledger.md": (
            "The public gonol is the canonical 157-position UCNS carrier",
            "Position `0` is SPACE/ZERO",
            "Unratified formulas such as `k/157` or `2k/157`",
        ),
    }
    for path, phrases in required.items():
        text = _text(path)
        for phrase in phrases:
            assert phrase in text, f"{path} lost public-gonol canon phrase: {phrase!r}"


def test_superseded_origin_and_angle_claims_cannot_reappear():
    forbidden = {
        "docs/base-geometry.md": (
            "external glyph codebook is out of this repo's scope",
            "θ=0 origin ↔ external 157-glyph codebook linkage",
        ),
        "contracts/test_identity_two_sided.py": (
            "theta=0 origin (space/zero)",
            "cross-repo 157-glyph codebook is out of this repo",
        ),
        "ucns/canonical.py": (
            "the theta=0 origin e =",
        ),
        "ucns-spec.md": (
            "located at the half-revolution \\theta = 2\\pi",
            "twist-seam** (zero, §7) is inscribed at",
            "The absorption law\n\n\\[\n\\underline{\\mathbf{0}} \\boxtimes",
        ),
        "depth7-frontier.md": (
            "the seam at `θ = 2π` where orientation flips on the doubled cover",
        ),
    }
    for path, phrases in forbidden.items():
        text = _text(path)
        for phrase in phrases:
            assert phrase not in text, f"{path} restored superseded claim: {phrase!r}"


def test_public_gonol_source_and_origin_are_machine_pinned():
    source = _text("ucns/public_gonol.py")
    assert "7af8debf6ef3905f01baff02b43d8c3bee16ccbc" in source
    assert 'PUBLIC_GONOL_SHA256 = "20d6ed51fdff5505ed9696c38d6dcc82f982eba166d9b712bee68c4521b751ac"' in source

    private = _text("ucns/public_gonol_private.py")
    assert "perm = list(range(n))" in private
    assert "for i in range(n - 1, 1, -1)" in private
    assert "if base == 0:" in private
    assert "return self.perm[0]" in private
