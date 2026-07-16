#!/usr/bin/env python3
"""Reconcile public identity and planning docs with the public-gonol canon."""

from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(
            f"{relative}: expected one occurrence, found {count}: {old[:140]!r}"
        )
    path.write_text(text.replace(old, new), encoding="utf-8")


def insert_before_once(relative: str, marker: str, addition: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if addition.strip() in text:
        return
    count = text.count(marker)
    if count != 1:
        raise SystemExit(
            f"{relative}: expected one marker, found {count}: {marker!r}"
        )
    path.write_text(text.replace(marker, addition + marker), encoding="utf-8")


def repair_readme() -> None:
    replace_once(
        "README.md",
        "# ucns — Unit Circle Number System: Recursive Factorization Theory",
        "# ucns — Fixed-Origin Public Gonol and Scoped Recursive Factorization",
    )
    replace_once(
        "README.md",
        "> **Experimental sequence-theoretic factorization on the unit circle, with a witness-matrix recursive quotient solver.**",
        "> **Canonical 157-position twist-bearing UCNS frame, with a separately scoped experimental recursive factorization subsystem.**",
    )
    replace_once(
        "README.md",
        "This repository contains the UCNS (Unit Circle Number System) sequence theory and its implementation. The focus is **recursive factorization**: given a UCNS product object *P*, recover factors *A* and *B* such that *A ⊠ B = P*.",
        "This repository owns the UCNS public gonol: the exact 157-position frame whose fixed position `0` is SPACE/ZERO, the Möbius twist seam and system origin. It also contains a separately scoped normalized recursive factorization subsystem that studies products *P = A ⊠ B*. No bridge between those surfaces is assumed.",
    )
    replace_once(
        "README.md",
        "> **v1.0 scope.** UCNS v1.0 is a scoped, reproducible research release for\n> catalogue-sufficient recursive factorization (Theorem N), not a claim of\n> total general recursive primality.",
        "> **v1.0 scope.** UCNS v1.0 packages the fixed-origin public gonol and a\n> scoped catalogue-driven recursive factorization research subsystem. Theorem N\n> remains a `FRONTIER` proof target, not a claim of complete factorization or\n> total general recursive primality.",
    )
    replace_once(
        "README.md",
        "The ask is bounded: help separate definitions, implemented algorithms, empirical results, proof sketches, conjectures, limitations, and counterexamples. The Lean finite-search model now type-checks, while the completeness theorems remain `sorry`-closed and require external formal review. Cancellativity is refuted in general and fully characterized by the divisor dichotomy (`docs/base-geometry.md` §5); it is **not** a premise of the current completeness target. Theorem N is an exhaustive-inclusion completeness target — the finite search provably enumerates a space containing the true candidate at every stage — not a cancellation or uniqueness theorem.",
        "The ask is bounded: help separate definitions, implemented algorithms, empirical results, proof sketches, conjectures, limitations, and counterexamples. The Lean finite-search model now type-checks, while the completeness theorems remain `sorry`-closed and require external formal review. Cancellativity is refuted in general and fully characterized by the divisor dichotomy (`docs/base-geometry.md` §5); it is **not** a premise of the current completeness target. Theorem N is an exhaustive-inclusion proof target: its sketch argues that the finite search should include a valid witness, but that inclusion is not yet discharged as a complete Lean proof and has no public-gonol scope without the missing bridge.",
    )
    replace_once(
        "README.md",
        "| Depth-3 asymmetric (Theorem 9) | `TEST-BACKED` (6/6 empirical) |",
        "| Depth-3 asymmetric experiment | `TEST-BACKED` only by cited execution artifacts; not proof-defended and not a status promotion for Theorem N |",
    )
    replace_once(
        "README.md",
        "See `ucns-theorem-n.md` for the unified catalogue-sufficient theorem statement and its current formal frontier.",
        "See `ucns-theorem-n.md` for the catalogue-sufficient proof target and its current formal frontier.",
    )
    replace_once(
        "README.md",
        "  core.py, embedding.py, epicycle.py, mobius.py, similarity.py\n                         # v0.6.5-lineage modules (stable reference)",
        "  core.py, embedding.py, epicycle.py, mobius.py, similarity.py\n                         # compatibility-only local coordinate/disk/embedding utilities; not the public frame",
    )


def repair_spec_counts() -> None:
    replace_once(
        "ucns-spec.md",
        "- **IMPLEMENTED + TEST-BACKED, not yet DEFENDED in the formal spec.** Full frozen depth-2 domain via `factor_search_v08`; depth-3 asymmetric (Theorem 9 instance of Theorem N, 6/6 empirical in `code/sweeps/t9_minimal_cat.py`).",
        "- **IMPLEMENTED + TEST-BACKED, not yet DEFENDED in the formal spec.** Full frozen depth-2 behavior via `factor_search_v08`; depth-3 asymmetric experiments are evidence only where tied to immutable execution artifacts and do not constitute a proved Theorem N instance.",
    )
    replace_once(
        "ucns-spec.md",
        "**v1.0 scope.** v1.0 is a scoped, reproducible research release for catalogue-sufficient recursive factorization. It is not a claim of total general recursive primality.",
        "**v1.0 scope.** v1.0 packages the fixed-origin public gonol and a scoped catalogue-driven recursive factorization research subsystem. Theorem N remains `FRONTIER`; this is not a claim of catalogue-sufficient completeness or total general recursive primality.",
    )
    replace_once(
        "ucns-spec.md",
        "- depth-3 asymmetric (Theorem 9 instance of Theorem N, 6/6 empirical).",
        "- depth-3 asymmetric experiment artifacts, `TEST-BACKED` only where an immutable run is cited; not a proved Theorem N instance.",
    )


def repair_changelog() -> None:
    insert_before_once(
        "CHANGELOG.md",
        "## 1.0.0rc1 — 2026-07-12\n",
        "## Unreleased — public-gonol recovery\n\n"
        "- Restored the exact A0 public gonol as UCNS canon: position `0` is SPACE/ZERO, the Möbius twist seam and fixed system origin; one 360-degree circuit reverses orientation and complete return requires 720 degrees.\n"
        "- Separated the public frame from the normalized recursive factorization subsystem; the public/factorization bridge remains `hmmm`.\n"
        "- Removed the application-level `2π` inscription method from the canonical `PrivateGonal` class and quarantined classical Poincaré-disk transforms as compatibility utilities.\n"
        "- Re-scoped Carrier-LCM to internal projected `n_min`, retained Theorem N as `FRONTIER`, and removed PTCA/Fano/octonion status overclaims.\n"
        "- Added permanent origin, 720-degree return, theorem-status, bridge-obligation, metadata, and non-flattening regressions.\n\n",
    )


def repair_crypto_note() -> None:
    insert_before_once(
        "pcea-ucns/ucns-crypto-domain-v0.md",
        "---\n\n## What today's UCNS results force\n",
        "## Public-frame correction\n\n"
        "This planning artifact concerns the normalized recursive factorization subsystem only. The canonical public gonol is the fixed 157-position twist-bearing frame and is not a cryptographic carrier chosen by `n_min`. The Carrier-LCM result cited below is an internal projected-`n_min` identity, not a theorem about the complete public gonol. No cryptographic construction or hardness claim follows from the public frame. Historical attack counts require the immutable run artifact that produced them; source code and prose alone are not execution evidence.\n\n"
        "---\n\n",
    )
    replace_once(
        "pcea-ucns/ucns-crypto-domain-v0.md",
        "1. **The Carrier-LCM Law is a leak.** `n_min(A ⊠ B) = lcm(n_min(A),\n   n_min(B))` (DEFENDED + TEST-BACKED in ucns). Measured: private\n   carrier supports {2} and {2,5} produce public carrier 80 with support\n   exactly {2,5}. **A secret encoded in carrier choice is public by\n   construction.** The private key must live where the Law does not\n   project: not in the carrier.",
        "1. **The internal projected-`n_min` LCM identity leaks projected factorization support.** Within the normalized factorization subsystem, `n_min(A ⊠ B) = lcm(n_min(A), n_min(B))` on its declared domain. This is not a public-gonol carrier theorem. A cryptographic design must therefore not hide secrets in that projected support; this statement does not establish security elsewhere.",
    )
    replace_once(
        "pcea-ucns/ucns-crypto-domain-v0.md",
        "2. **The oracle domain is exhaustively breakable.** Measured: 52/60\n   (~87%) of random products on the frozen depth-2 oracle domain are\n   recovered by `factor_search_v08`. This domain is ORACLE-COMPLETE in\n   the ucns ledger. **Categorically forbidden for key material.**",
        "2. **The oracle domain is unsuitable for key material.** Its declared `ORACLE-COMPLETE` factor-search status means catalogue-bounded negatives and recoveries are not a hardness foundation. Historical recovery rates are not repeated here without their immutable execution artifact.",
    )
    replace_once(
        "pcea-ucns/ucns-crypto-domain-v0.md",
        "3. **Pruning is an attacker's accelerator.** Measured: Carrier-LCM-Law\n   payload pruning removes ~71% of the candidate catalogue for free on\n   the {2,5} product. Any domain whose key space is enumerable as a\n   payload catalogue inherits this speedup against it.",
        "3. **Internal support pruning can accelerate catalogue search.** Any key space enumerable as a normalized-subsystem payload catalogue may inherit that reduction. Exact historical percentages require a cited immutable run artifact and are not a public-gonol claim.",
    )
    replace_once(
        "pcea-ucns/ucns-crypto-domain-v0.md",
        "A UCNS object whose carrier and gross shape are publishable, derived from",
        "A normalized factorization object whose projected `n_min` and gross shape are publishable, derived from",
    )
    replace_once(
        "pcea-ucns/ucns-crypto-domain-v0.md",
        "A carrier in the analytic-frontier regime — minimally the **carrier-40,",
        "An internal projected-`n_min` instance in the analytic-frontier regime — historically the **carrier-40,",
    )
    replace_once(
        "pcea-ucns/ucns-crypto-domain-v0.md",
        "Carrier (leaked anyway, fact 1), object depth, gross cell count, the KEM",
        "Internal projected `n_min`, object depth, gross cell count, the KEM",
    )
    replace_once(
        "pcea-ucns/ucns-crypto-domain-v0.md",
        "Carrier magnitude trades directly against",
        "Internal projected-`n_min` magnitude trades directly against",
    )


def main() -> int:
    repair_readme()
    repair_spec_counts()
    repair_changelog()
    repair_crypto_note()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
