"""Guard the theorem and bridge scope corrected by the public-gonol recovery."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_current_specs_keep_theorem_n_at_frontier():
    required = {
        "ucns-spec.md": (
            "**Foundational public-frame boundary.**",
            "**FRONTIER.** Theorem N is the catalogue-sufficient factorization proof target",
            "Theorem N catalogue-sufficient factorization remains `FRONTIER`",
            "internal factorization spec boundary",
        ),
        "depth7-frontier.md": (
            "Theorem N remains `FRONTIER`",
            "normalized factorization subsystem",
        ),
        "ucns-spec-frontier-v090.md": (
            "Theorem N remains `FRONTIER`",
            "public-gonol bridge is absent",
            "does not promote Theorem N itself beyond",
        ),
        "ucns-theorem-n.md": (
            "**Status:** FRONTIER",
            "does not confer DEFENDED status",
        ),
    }
    for path, phrases in required.items():
        value = _text(path)
        for phrase in phrases:
            assert phrase in value, f"{path} lost status boundary: {phrase!r}"

    forbidden = (
        "proof drafted, awaiting external formal review",
        "DEFENDED (proof drafted",
        "Theorem N catalogue-sufficient factorization (proof drafted",
    )
    for path in ("ucns-spec.md", "depth7-frontier.md", "ucns-spec-frontier-v090.md"):
        value = _text(path)
        for phrase in forbidden:
            assert phrase not in value, f"{path} restored theorem overclaim: {phrase!r}"


def test_internal_tower_language_cannot_claim_public_seams_or_automatic_recovery():
    frontier = _text("depth7-frontier.md")
    assert "internal host traversal record" in frontier
    assert "does not assert a public-gonol seam" in frontier
    assert "explicitly scoped quotient evidence" in frontier
    assert "one doubled-cover seam structure" not in frontier
    assert "> Pairwise interlocking is UCNS product plus quotient recovery." not in frontier


def test_hyperdimensional_and_ptca_language_is_frontier_not_established():
    spec = _text("ucns-spec.md")
    assert "# Part VI — Exploratory analogies; not public-gonol canon" in spec
    assert "No theorem currently identifies PTCA cores with UCNS objects" in spec
    assert "No Fano-plane or octonion equivalence is established" in spec
    assert "PTCA cores and UCNS epicyclic objects are the same class" not in spec
    assert "Seven Fano-coupled cores and the identity generate an octonion structure" not in spec


def test_public_bridge_obligations_are_visible_and_open_where_unproved():
    ledger = _text("audit/obligation_ledger.md")
    for obligation in ("PG-1", "PG-2", "PG-3", "PG-4", "PG-5", "PG-6"):
        assert obligation in ledger
    assert "PG-4" in ledger and "OPEN" in ledger
    assert "PG-5" in ledger and "OPEN" in ledger


def test_core_docs_link_the_cross_repository_boundary():
    needle = "docs/edcm-edcmbone-bridge-checklist.md"
    assert needle in _text("docs/ucns-shape-reconciliation.md")
    assert needle in _text("docs/pure-ucns-number-system.md")
    assert "docs/prime-quartet-discontinuity.md" in _text(
        "docs/edcm-edcmbone-bridge-checklist.md"
    )
