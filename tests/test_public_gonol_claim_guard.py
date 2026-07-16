"""Permanent guardrails for the fixed public-gonol twist/origin canon."""

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
            "No continuous-angle bridge from the",
            "public gonol is established here.",
            "**Foundational public-frame boundary.**",
            "**FRONTIER.** Theorem N",
        ),
        "docs/claims-ledger.md": (
            "The public gonol is the canonical 157-position UCNS carrier",
            "Position `0` is SPACE/ZERO",
            "Unratified formulas such as `k/157` or `2k/157`",
        ),
        "docs/pure-ucns-number-system.md": (
            "UCNS public frame := canonical 157-position twist-bearing gonol",
            "complete return     := 720 degrees",
            "one circuit         := 360 degrees with orientation reversal",
            "factorization-unit object, not public SPACE/ZERO",
        ),
        "docs/ucns-shape-reconciliation.md": (
            "Canonical public-frame correction",
            "fixed system origin",
            "three-surface ontology",
        ),
        "docs/edcm-edcmbone-bridge-checklist.md": (
            "UCNS is rooted in the fixed-origin public gonol",
            "Catalogue-sufficient completeness (Theorem N)",
            "There is no assumed bridge",
        ),
        "docs/carrier-support-pruning.md": (
            "not the complete carrier theorem for the fixed-origin",
            "internal projected-`n_min` identity",
            "720-degree return",
        ),
        "docs/eng_ucns_spec.md": (
            "The public gonol",
            "is canon for all UCNS",
            "A 16-gonal grammatical class table",
            "not the public gonol",
            "not “proven at full depth”",
        ),
        "docs/ucns_operational_widening.md": (
            "internal projected carrier `n_min`",
            "not a theorem about widening of the canonical public gonol",
            "not called “per-sublattice finiteness of UCNS”",
        ),
        "formal/README.md": (
            "fixed SPACE/ZERO Möbius-twist origin",
            "complete return after 720 degrees",
            "one 360-degree circuit flips orientation",
            "Object-relative normalization is not applied to the public gonol",
        ),
        "formal/Ucns/PublicGonol.lean": (
            "position 0 is SPACE/ZERO",
            "complete return requires 720 degrees",
            "independent of the normalized factorization core",
            "def completeReturnDegrees : Nat := 720",
            "theorem oneCircuit_changes_orientation",
            "theorem completeReturn_restores_orientation",
            "structure OriginPreservingPermutation",
        ),
        "formal/Ucns/Core.lean": (
            "normalized recursive factorization-object algebra",
            "object-relative",
            "does not select, move, or quotient the public-gonol twist origin",
        ),
        "formal/Ucns/CarrierLcm.lean": (
            "internal projected nMin",
            "not the complete public-carrier theorem",
        ),
        "formal/Ucns/TheoremN.lean": (
            "not completeness for the fixed-origin public gonol",
            "no public-gonol bridge is assumed",
        ),
        "ucns/geometry_bridge.py": (
            "not the public-gonol frame",
            'PUBLIC_GONOL_BRIDGE_STATUS = "hmmm"',
        ),
        "ucns/core.py": (
            "not the canonical UCNS public gonol",
            "does not model the 720-degree complete return",
            "compatibility_only",
        ),
        "ucns/embedding.py": (
            "not the canonical public gonol",
            "distinct from ``ucns.encode_text_path``",
            "compatibility_only",
        ),
        "ucns/epicycle.py": (
            "does not define the UCNS public gonol",
            "do not preserve the public Möbius orientation state",
            "compatibility_only",
        ),
        "ucns/similarity.py": (
            "not metrics on the canonical public gonol",
            "compatibility_only",
        ),
    }
    for path, phrases in required.items():
        value = _text(path)
        for phrase in phrases:
            assert phrase in value, f"{path} lost public-gonol canon phrase: {phrase!r}"


def test_superseded_origin_angle_and_system_scope_claims_cannot_reappear():
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
            "**DEFENDED — proof drafted, awaiting external formal review.** Theorem N",
        ),
        "depth7-frontier.md": (
            "the seam at `θ = 2π` where orientation flips on the doubled cover",
        ),
        "formal/README.md": (
            "360-degree complete return",
            "public gonol is gauge-normalized",
            "mod-4 lemmas establish",
        ),
        "formal/Ucns/PublicGonol.lean": (
            "oneCircuitHalfTurns",
            "completeReturnHalfTurns",
            "UCNSObject.amod4",
        ),
        "docs/pure-ucns-number-system.md": (
            "UCNS number := canonical recursive unit-circle traversal object",
            "identity    := unit object / unit-equivalent traversal",
        ),
        "docs/edcm-edcmbone-bridge-checklist.md": (
            "Catalogue-sufficient completeness (Theorem N) | `DEFENDED`",
        ),
        "docs/ucns-shape-reconciliation.md": (
            "UCNS-A canonical object is a **recursive ordered sequence",
        ),
        "docs/eng_ucns_spec.md": (
            "UCNS-G geometry axis, not a linguistic or statistical choice",
            "This law is proven at full depth",
            "The carrier of a sentence is the LCM",
        ),
        "docs/ucns_operational_widening.md": (
            "Carrier monotonicity is proven at full recursive depth",
            "per-sublattice finiteness of UCNS",
        ),
        "formal/Ucns/Core.lean": (
            "faithful definitions for the UCNS recursive algebra",
        ),
        "formal/Ucns/CarrierLcm.lean": (
            "Public Carrier-LCM law on the repaired `Complete` domain",
        ),
        "formal/Ucns/TheoremN.lean": (
            "Lean 4 model of the UCNS Theorem N family",
        ),
        "ucns/core.py": (
            "The fundamental numeric primitive",
            "The additive identity (theta = 0)",
        ),
        "ucns/embedding.py": (
            "the canonical UCNS inner product",
            "High-level embedding API built on the Unit Circle Number System",
        ),
        "ucns/epicycle.py": (
            "Why epicycles for UCNS?",
        ),
        "ucns/similarity.py": (
            "Similarity and distance metrics for Unit Circle Number embeddings",
        ),
        "ucns/public_gonol_private.py": (
            "def inscribe(",
            "2.0 * math.pi",
            "value / (2.0 * math.pi)",
        ),
    }
    for path, phrases in forbidden.items():
        value = _text(path)
        for phrase in phrases:
            assert phrase not in value, f"{path} restored superseded claim: {phrase!r}"

    formal_imports = {
        line.strip()
        for line in _text("formal/Ucns/PublicGonol.lean").splitlines()
        if line.strip().startswith("import ")
    }
    assert "import Ucns.Core" not in formal_imports


def test_public_gonol_source_origin_and_return_are_machine_pinned():
    source = _text("ucns/public_gonol.py")
    assert "7af8debf6ef3905f01baff02b43d8c3bee16ccbc" in source
    assert 'PUBLIC_GONOL_SHA256 = "20d6ed51fdff5505ed9696c38d6dcc82f982eba166d9b712bee68c4521b751ac"' in source

    private = _text("ucns/public_gonol_private.py")
    assert "perm = list(range(ARITY))" in private
    assert "for i in range(ARITY - 1, 1, -1)" in private
    assert "def inscribe(" not in private
    assert "2.0 * math.pi" not in private
    assert "continuous angles" in private
    assert "360 degrees is a complete UCNS return" in private

    formal = _text("formal/Ucns/PublicGonol.lean")
    assert "def origin : Vertex := ⟨0, arity_pos⟩" in formal
    assert "def oneCircuitDegrees : Nat := 360" in formal
    assert "def completeReturnDegrees : Nat := 720" in formal
    assert "oneCircuitHalfTurns" not in formal
    assert "completeReturnHalfTurns" not in formal
    assert "UCNSObject.amod4" not in formal


def test_formal_theorem_families_are_scoped_away_from_unproved_public_bridge():
    formal_readme = _text("formal/README.md")
    required = (
        "All Theorem N statements are presently scoped to the normalized recursive",
        "not, without an additional bridge theorem, a theorem about the complete",
        "proof that the internal multiplication preserves the public twist/origin",
        "public-gonol scope for Theorem N completeness",
    )
    for phrase in required:
        assert phrase in formal_readme

    imports = _text("formal/Ucns.lean")
    assert "import Ucns.PublicGonol" in imports

    ledger = _text("audit/obligation_ledger.md")
    for obligation in ("PG-1", "PG-2", "PG-3", "PG-4", "PG-5", "PG-6"):
        assert obligation in ledger
