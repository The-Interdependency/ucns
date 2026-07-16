#!/usr/bin/env python3
"""Apply final status/scope corrections after the primary public-frame repair."""

from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(
            f"{relative}: expected one occurrence, found {count}: {old[:120]!r}"
        )
    path.write_text(text.replace(old, new), encoding="utf-8")


def main() -> int:
    replace_once(
        "ucns-spec.md",
        "- **DEFENDED — proof drafted, awaiting external formal review.** Theorem N (catalogue-sufficient factorization at all depths). See `ucns-theorem-n.md`. The only hypothesis is that the catalogue contains every recursive payload of the true factors; no depth condition is imposed on the algorithm.",
        "- **FRONTIER.** Theorem N is the catalogue-sufficient factorization proof target for the normalized factorization subsystem. Its implementation-backed proof sketch and Lean scaffold do not confer `DEFENDED` status; completeness statements remain `sorry`-backed, and no public-gonol bridge is proved.",
    )
    replace_once(
        "depth7-frontier.md",
        "Each level contributes:\n\n- one host traversal,\n- one doubled-cover seam structure,\n- one layer of payload fiber geometry.\n\nThis is a structural interpretation of the recursive object model.",
        "Each level contributes an internal host traversal record, internal face data, and one layer of recursive payload structure. This is a structural description of the normalized factorization model; it does not assert a public-gonol seam or orientation frame at every payload level.",
    )
    replace_once(
        "depth7-frontier.md",
        "> Pairwise interlocking is UCNS product plus quotient recovery.",
        "> Pairwise interlocking is an exploratory label for an internal ordered product accompanied by explicitly scoped quotient evidence.",
    )
    replace_once(
        "ucns-spec-frontier-v090.md",
        "`DEFENDED`** at the spec level. The depth-2 oracle theorem (Lemma 7)\nremains `DEFENDED` + `ORACLE-COMPLETE` and is now recognized as an\ninstance of Theorem N (`ucns-theorem-n.md §4.1`).",
        "`DEFENDED`** at the spec level. The depth-2 oracle theorem (Lemma 7)\nremains `DEFENDED` + `ORACLE-COMPLETE`. It fits the intended catalogue-sufficient\nshape of the Theorem N proof target, but does not promote Theorem N itself beyond\n`FRONTIER` (`ucns-theorem-n.md §4.1`).",
    )
    replace_once(
        "ucns-spec-frontier-v090.md",
        "- DEFENDED + ORACLE-COMPLETE: depth-2 smallest oracle (Lemma 7 = Theorem N instance),",
        "- DEFENDED + ORACLE-COMPLETE: depth-2 smallest oracle; its catalogue-sufficient shape is evidence for the FRONTIER Theorem N target, not a status promotion,",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
