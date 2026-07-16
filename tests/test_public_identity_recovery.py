"""Keep package, release, and planning identities rooted in the public gonol."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_package_and_zenodo_identity_name_the_public_frame_first():
    pyproject = _text("pyproject.toml")
    assert "Fixed-origin public gonol canon" in pyproject
    assert "scoped recursive factorization research subsystem" in pyproject

    zenodo = json.loads(_text(".zenodo.json"))
    assert "Fixed-Origin Public Gonol" in zenodo["title"]
    assert "complete return requires 720 degrees" in zenodo["description"]
    assert "internal projected n_min" in zenodo["description"]
    assert "public gonol" in zenodo["keywords"]


def test_agent_instructions_cannot_flatten_the_repository_again():
    agents = _text("AGENTS.md")
    assert "Public-gonol canon is load-bearing" in agents
    assert "one 360-degree circuit changes orientation" in agents
    assert "complete return requires 720 degrees" in agents
    assert "Do not infer a bridge" in agents

    claude = _text("CLAUDE.md")
    assert "fixed-origin public gonol" in claude
    assert "separately scoped normalized recursive factorization subsystem" in claude
    assert "No bridge between them is assumed" in claude
    assert "6/6 empirical" not in claude
    assert "public_gonol.py" in claude
    assert "public-gonol ↔ normalized-factorization bridge" in claude


def test_readme_is_not_flattened_into_factorization_only():
    readme = _text("README.md")
    assert readme.startswith(
        "# ucns — Fixed-Origin Public Gonol and Scoped Recursive Factorization"
    )
    assert "Canonical 157-position twist-bearing UCNS frame" in readme
    assert "No bridge between those surfaces is assumed" in readme
    assert "Theorem N remains a `FRONTIER` proof target" in readme
    assert "not yet discharged as a complete Lean proof" in readme
    assert "6/6 empirical" not in readme
    assert "compatibility-only local coordinate/disk/embedding utilities" in readme


def test_repository_manifest_changelog_and_release_record_the_recovery():
    manifest = _text("MANIFEST.md")
    assert "canonical public 157-gonal and fixed SPACE/ZERO Möbius twist origin" in manifest
    assert "The public-gonol ↔ normalized-factorization bridge remains `hmmm`" in manifest
    assert "6/6 asymmetric depth-3 SUCCESS" not in manifest

    changelog = _text("CHANGELOG.md")
    assert "## Unreleased — public-gonol recovery" in changelog
    assert "complete return requires 720 degrees" in changelog
    assert "removed PTCA/Fano/octonion status overclaims" in changelog

    release = _text("RELEASE.md")
    assert "UCNS v1.0.0 packages two deliberately separated surfaces" in release
    assert "complete return requires 720 degrees" in release
    assert "public-gonol ↔ normalized-factorization bridge" in release
    assert "PrivateGonal exposes no application-level 2π inscription method" in release


def test_crypto_planning_document_cannot_redefine_the_public_carrier():
    crypto = _text("pcea-ucns/ucns-crypto-domain-v0.md")
    assert "## Public-frame correction" in crypto
    assert "normalized recursive factorization subsystem only" in crypto
    assert "internal projected-`n_min` identity" in crypto
    assert "not a theorem about the complete public gonol" in crypto
    assert "Carrier-LCM Law is a leak" not in crypto
    assert "52/60" not in crypto
    assert "~71%" not in crypto


def test_current_spec_does_not_promote_uncited_depth3_counts():
    spec = _text("ucns-spec.md")
    assert "6/6 empirical" not in spec
    assert "depth-3 asymmetric experiments are evidence only where tied to immutable execution artifacts" in spec
    assert "not a proved Theorem N instance" in spec
