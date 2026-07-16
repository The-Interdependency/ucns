#!/usr/bin/env python3
"""Apply the public-gonol theorem/status recovery to a UCNS checkout.

This maintenance script is intentionally stored on a temporary branch. It edits
``agent/remove-2pi-inscription-from-canon`` through an out-of-band workflow and
is not part of the target runtime package.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()


def _path(relative: str) -> Path:
    return ROOT / relative


def replace_once(relative: str, old: str, new: str) -> None:
    path = _path(relative)
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(
            f"{relative}: expected one occurrence, found {count}: {old[:120]!r}"
        )
    path.write_text(text.replace(old, new), encoding="utf-8")


def insert_before_once(relative: str, marker: str, addition: str) -> None:
    path = _path(relative)
    text = path.read_text(encoding="utf-8")
    if addition.strip() in text:
        return
    count = text.count(marker)
    if count != 1:
        raise SystemExit(
            f"{relative}: expected one marker, found {count}: {marker!r}"
        )
    path.write_text(text.replace(marker, addition + marker), encoding="utf-8")


def repair_links() -> None:
    insert_before_once(
        "docs/ucns-shape-reconciliation.md",
        "## hmmm\n",
        "## Cross-repository non-transfer checklist\n\n"
        "The mandatory downstream boundary is maintained in "
        "`docs/edcm-edcmbone-bridge-checklist.md`.\n\n",
    )
    insert_before_once(
        "docs/pure-ucns-number-system.md",
        "## hmmm\n",
        "## Cross-repository non-transfer checklist\n\n"
        "The mandatory downstream boundary is maintained in "
        "`docs/edcm-edcmbone-bridge-checklist.md`.\n\n",
    )
    insert_before_once(
        "docs/edcm-edcmbone-bridge-checklist.md",
        "## hmmm\n",
        "## Prime-quartet discontinuity boundary\n\n"
        "The separate discontinuity and non-transfer rule is recorded in "
        "`docs/prime-quartet-discontinuity.md`.\n\n",
    )


def repair_main_spec() -> None:
    replace_once(
        "ucns-spec.md",
        "This file is the **complete UCNS spec as it currently stands**, with the algebraic layers frozen where they were proved and the later frontier explicitly marked where the current engine fails.",
        "This file records the canonical UCNS public frame together with the historical normalized factorization subsystem and its current frontier. The fixed-origin public gonol is load-bearing canon. The continuous and recursive algebraic layers below are internal models unless an explicit bridge theorem says otherwise.",
    )
    replace_once(
        "ucns-spec.md",
        "# Part I — Flat Kernel v0.3",
        "# Part I — Internal normalized factorization model: flat kernel v0.3",
    )
    replace_once(
        "ucns-spec.md",
        "UCNS is a geometric-arithmetic system in which the primitive object is a paired traversal object rather than a scalar or symbol.",
        "UCNS is rooted in the fixed-origin public gonol. The historical flat-kernel subsystem models normalized paired traversal objects for factorization; it is not the primitive public frame.",
    )
    replace_once(
        "ucns-spec.md",
        "A valid flat UCNS object is",
        "A valid flat object in the normalized factorization subsystem is",
    )
    replace_once(
        "ucns-spec.md",
        "The object is paired. Arithmetic does not occur on a single oriented traversal alone.",
        "This internal object is paired. The statement does not define or relocate the public-gonol twist origin.",
    )
    replace_once(
        "ucns-spec.md",
        "## 2. Ambient Space",
        "## 2. Internal doubled-cover coordinate model",
    )
    replace_once(
        "ucns-spec.md",
        "public gonol is established here.\n",
        "public gonol is established here.\n\n"
        "**Foundational public-frame boundary.** Position `0` is the fixed "
        "SPACE/ZERO Möbius twist origin. One 360-degree circuit changes "
        "orientation; complete return requires 720 degrees. Every later "
        "continuous coordinate, lattice, normalization, carrier, and theorem "
        "in this document is subordinate to that canon and cannot redefine it.\n",
    )
    replace_once(
        "ucns-spec.md",
        "## 3. Gonal Lattice",
        "## 3. Internal gonal lattice",
    )
    replace_once(
        "ucns-spec.md",
        "For any positive integer \\(n\\), define the \\(n\\)-gonal lattice",
        "Within the normalized factorization subsystem, for any positive integer \\(n\\), define the internal \\(n\\)-gonal lattice",
    )
    replace_once(
        "ucns-spec.md",
        "Lattice membership is determined by the \\(2\\pi\\)-projection of \\(\\theta_j\\). The doubled-cover lift remains in \\(\\theta_j\\), while \\(F\\) carries an independent binary face-state sequence.",
        "Internal lattice membership is determined by this subsystem's \\(2\\pi\\)-projection of \\(\\theta_j\\). This is not a public-gonol vertex map, does not locate the twist origin, and does not make 360 degrees a complete system return.",
    )
    replace_once(
        "ucns-spec.md",
        "### 4.1 Intrinsic carrier",
        "### 4.1 Internal projected carrier",
    )
    replace_once(
        "ucns-spec.md",
        "This is the smallest positive integer such that all anchors of \\(\\Theta^{+}\\) lie on the \\(n_{\\min}\\)-gonal lattice modulo \\(2\\pi\\).",
        "This is the smallest positive integer for the internal projected anchor lattice. It is not the complete carrier invariant of the fixed-origin public gonol.",
    )
    replace_once(
        "ucns-spec.md",
        "- Theorem N catalogue-sufficient factorization (proof drafted, awaiting external formal review).\n",
        "",
    )
    replace_once(
        "ucns-spec.md",
        "### FRONTIER / out of v1.0 scope\n- carrier widening beyond current proven bounds,",
        "### FRONTIER / out of v1.0 scope\n"
        "- Theorem N catalogue-sufficient factorization remains `FRONTIER`; "
        "its Lean completeness statements are `sorry`-backed and no public-gonol bridge is proved,\n"
        "- carrier widening beyond current proven bounds,",
    )
    replace_once(
        "ucns-spec.md",
        "UCNS currently has:",
        "The normalized factorization subsystem currently has:",
    )
    replace_once(
        "ucns-spec.md",
        "That is the complete current spec boundary.",
        "That is the complete current internal factorization spec boundary. The public gonol and all bridges from it remain separate load-bearing surfaces.",
    )

    path = _path("ucns-spec.md")
    text = path.read_text(encoding="utf-8")
    marker = "# Part VI — Hyperdimensional Structure and the Octonion Limit\n"
    if text.count(marker) != 1:
        raise SystemExit("ucns-spec.md: Part VI marker drifted")
    prefix = text.split(marker, 1)[0]
    corrected_tail = """# Part VI — Exploratory analogies; not public-gonol canon

## H1. Internal recursive payload towers

`UCNSObject` values carry recursive payload towers. That is an implemented fact
about the normalized factorization subsystem. Describing those towers as
continuous Möbius cylinders is an exploratory analogy, not a theorem about the
public gonol and not a bridge to its twist/orientation structure.

## H2. Interlocking vocabulary

Inside the normalized factorization subsystem, ordered multiplication and
left/right quotient operations are defined. “Interlocking” may be used as
informal vocabulary for a product together with recoverability evidence, but
recoverability is domain-scoped and non-unique in general. No cylinder-separation
theorem follows from the metaphor.

## H3. PTCA mapping status

No theorem currently identifies PTCA cores with UCNS objects. A PTCA-to-UCNS
adapter may be proposed as `EXPERIMENTAL`, with exact source, target, composition,
recoverability, and status boundaries. It is not a definitional identity.

## H4. Fano and octonion status

No Fano-plane or octonion equivalence is established. Fano incidence, seven-core
coupling, alternating associators, controlled non-associativity, and an octonion
whole remain research hypotheses. They do not inherit proof status from the
public gonol, the internal product, or quotient code.

## H5. Honest frontier

**Established or implemented in declared scope:**

- the fixed SPACE/ZERO public-gonol twist origin;
- orientation change after one 360-degree circuit and complete return after 720
  degrees;
- the normalized recursive factorization representation and its scoped algebra;
- domain-scoped quotient and factor-search behavior with exact recomposition
  gates.

**Open:**

- the public-gonol ↔ normalized-factorization bridge;
- proof that internal multiplication preserves public origin, twist,
  orientation, faces, chirality, and lifted traversal;
- PTCA representation and dynamics;
- Fano incidence realization;
- octonion equivalence or controlled non-associativity;
- ternary inference completeness.

## hmmm

The analogies may guide experiments. They are not allowed to flatten the public
frame or promote an unproved correspondence into system canon.
"""
    path.write_text(prefix + corrected_tail, encoding="utf-8")


def repair_frontier_docs() -> None:
    replace_once(
        "depth7-frontier.md",
        "The current repository now contains two connected layers:\n\n1. an implemented and partially defended UCNS recursive algebra line, and\n2. a newly framed depth-7 geometric hypothesis that points toward Fano-plane / octonion behavior.\n\nThe first layer is the engine.  \nThe second layer is the frontier.",
        "The current repository contains three deliberately separated surfaces:\n\n1. the fixed-origin public gonol;\n2. an implemented and partially defended normalized factorization subsystem; and\n3. a depth-7 geometric hypothesis pointing toward Fano-plane / octonion behavior.\n\nThe public frame is canon. The normalized factorization subsystem is the current engine. The depth-seven material is frontier analogy. None may be collapsed into another without a proved bridge.",
    )
    replace_once(
        "depth7-frontier.md",
        "## 1.1 UCNS objects are recursive paired traversal objects\n\nA UCNS object is a positive host sequence whose cells may carry payloads that are themselves UCNS objects.",
        "## 1.1 Normalized factorization objects are recursive payload structures\n\nA normalized factorization object is a positive host sequence whose cells may carry payloads that are themselves normalized factorization objects.",
    )
    replace_once(
        "depth7-frontier.md",
        "This is the structural basis for calling depth-`n` UCNS objects recursive Möbius-cylindrical towers.",
        "This supports recursive-tower language inside the normalized factorization subsystem. Calling those towers Möbius cylinders is exploratory and does not identify them with the public gonol.",
    )
    replace_once(
        "depth7-frontier.md",
        "- Theorem N (catalogue-sufficient factorization, `ucns-theorem-n.md`):\n  `DEFENDED` (proof drafted, awaiting external formal review),",
        "- Theorem N remains `FRONTIER`: the implementation-backed proof sketch and Lean scaffold do not confer `DEFENDED` status, and no public-gonol bridge is proved,",
    )
    replace_once(
        "depth7-frontier.md",
        "A depth-`n` UCNS object may be interpreted as an `n`-level recursive Möbius-cylindrical tower.",
        "A depth-`n` normalized factorization object may be explored through an `n`-level tower analogy. This is not public-gonol canon or a proved continuous geometry.",
    )

    replace_once(
        "ucns-spec-frontier-v090.md",
        "> file as historical context; current canon lives in `ucns-spec.md` and\n> `ucns-theorem-n.md`.",
        "> file as historical context; current canon lives in `ucns-spec.md`,\n> `docs/pure-ucns-number-system.md`, and `ucns-theorem-n.md`. The public gonol\n> is the fixed UCNS frame; this document concerns only the normalized\n> factorization frontier, and the public-gonol bridge is absent.",
    )
    replace_once(
        "ucns-spec-frontier-v090.md",
        "- external zero,",
        "- an internal factorization-unit object, not public SPACE/ZERO,",
    )
    replace_once(
        "ucns-spec-frontier-v090.md",
        "Theorem N (`ucns-theorem-n.md`) addresses the **catalogue-sufficient**\nform of these claims and is `DEFENDED` (proof drafted, awaiting external\nformal review): if the catalogue contains every recursive payload of the\ntrue factors, `factor_search_v08` finds a factorization.",
        "Theorem N (`ucns-theorem-n.md`) addresses the **catalogue-sufficient**\nform of these claims as a `FRONTIER` proof target. The proof sketch and\nimplementation do not confer `DEFENDED` status; Lean completeness statements\nremain `sorry`-backed. If proved in the normalized factorization subsystem, it\nstill would not become a theorem about the public gonol without the absent bridge.",
    )
    replace_once(
        "ucns-spec-frontier-v090.md",
        "> UCNS has a `DEFENDED` flat kernel, a `DEFENDED` depth-1 restricted\n> completeness theorem, and a `DEFENDED` + `ORACLE-COMPLETE` depth-2\n> oracle theorem. **Theorem N (`ucns-theorem-n.md`,\n> catalogue-sufficient factorization at all depths) is `DEFENDED`\n> (proof drafted, awaiting external formal review).** The full frozen\n> depth-2 domain is `IMPLEMENTED` + `TEST-BACKED` in `factor_search_v08`,\n> not yet `DEFENDED` at the spec level. Carrier widening and general\n> primality outside defended-complete domains are `FRONTIER` and out\n> of v1.0 scope.",
        "> Within the normalized factorization subsystem, UCNS has a `DEFENDED`\n> flat kernel, a `DEFENDED` depth-1 restricted completeness theorem, and a\n> `DEFENDED` + `ORACLE-COMPLETE` depth-2 oracle theorem. **Theorem N\n> (`ucns-theorem-n.md`) remains `FRONTIER`; its proof sketch, implementation,\n> and Lean scaffold do not confer `DEFENDED` status.** The full frozen depth-2\n> domain is `IMPLEMENTED` + `TEST-BACKED`, not spec-level `DEFENDED`. The\n> public-gonol bridge is absent, and carrier widening/general primality remain\n> `FRONTIER` and out of v1.0 scope.",
    )
    replace_once(
        "ucns-spec-frontier-v090.md",
        "- DEFENDED (proof drafted, awaiting external review): Theorem N — catalogue-sufficient factorization at all depths,",
        "- FRONTIER: Theorem N — catalogue-sufficient factorization proof target in the normalized subsystem; Lean completeness remains `sorry`-backed and the public bridge is absent,",
    )


def repair_ledger() -> None:
    insert_before_once(
        "audit/obligation_ledger.md",
        "## Findings of record (this run)\n",
        "## Public-gonol and bridge obligations\n\n"
        "This table is informational and is not parsed by `audit/reconcile.py`. "
        "It prevents the normalized factorization ledger from being mistaken "
        "for the complete public-frame proof surface.\n\n"
        "| id | obligation | status | evidence / next proof |\n"
        "|---|---|---|---|\n"
        "| `PG-1` | public position `0` is SPACE/ZERO, the fixed Möbius twist origin | CLOSED | `ucns/public_gonol.py`, `formal/Ucns/PublicGonol.lean`, public-gonol tests |\n"
        "| `PG-2` | one 360-degree circuit changes orientation; complete return requires 720 degrees | CLOSED | `formal/Ucns/PublicGonol.lean`, claim guards |\n"
        "| `PG-3` | admissible private phase/permutation preserves origin and acts only on positions `1..156` | CLOSED | `ucns/public_gonol_private.py`, public-gonol tests |\n"
        "| `PG-4` | define a faithful public-gonol ↔ normalized-factorization bridge | OPEN | must preserve origin, twist, orientation, faces, chirality, lifted traversal, serialization, and information-loss boundary |\n"
        "| `PG-5` | prove correspondence between public composition and internal `multiply` | OPEN | no correspondence theorem exists; Carrier-LCM and Theorem N remain internal |\n"
        "| `PG-6` | prevent theorem/status transfer across absent bridges | CLOSED as policy guard; mathematical bridge remains open | claims ledger, bridge checklist, permanent regression tests |\n\n",
    )


def main() -> int:
    repair_links()
    repair_main_spec()
    repair_frontier_docs()
    repair_ledger()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
