# ratios: loc_comments=89:24 imports_exports=3:2 calls_definitions=67:2
"""Obligation ↔ witness reconciler for the base-geometry ledger.

Doctrine (handoff §1): the audit reconciles the witness list against the
obligation list *without importing either*.  This script only reads text:

  1. obligation rows from ``audit/obligation_ledger.md`` (id + loto state);
  2. ``# === CONTRACTS ===`` entries from ``ucns/*.py`` (msdmd block
     syntax, parsed with a self-contained regex — no skill_lib import);
  3. the contract files and callables named by each ``call:`` field
     (existence checked textually, never imported);
  4. RepoLOTO state in ``.loto/``.

Exit 0 iff every obligation has exactly one witness, every witness maps to
an obligation, every call target exists textually, and lock state matches
the ledger.  Modules under ``ucns/`` without a CONTRACTS block are listed
as visible coverage gaps (msdmd rule: gaps are informational, never
silently dropped).

Usage:  python audit/reconcile.py   (from the repo root)
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LEDGER = ROOT / "audit" / "obligation_ledger.md"
LOTO_DIR = ROOT / ".loto"
SOURCE_DIR = ROOT / "ucns"

BLOCK_RE = re.compile(
    r"^# === CONTRACTS ===\n(.*?)^# === END CONTRACTS ===",
    re.MULTILINE | re.DOTALL,
)
ENTRY_ID_RE = re.compile(r"^# id: (\S+)", re.MULTILINE)
CALL_RE = re.compile(r"^#   call:\s+(\S+)", re.MULTILINE)
LEDGER_ROW_RE = re.compile(
    r"^\| `([a-z0-9_]+)` \|.*\| (OPEN|CLOSED) \|$", re.MULTILINE
)


def parse_contracts():
    """(id, call, source_file) triples + list of gap modules."""
    entries = []
    gaps = []
    for path in sorted(SOURCE_DIR.glob("*.py")):
        text = path.read_text(encoding="utf-8")
        blocks = BLOCK_RE.findall(text)
        if not blocks:
            gaps.append(path.relative_to(ROOT))
            continue
        for block in blocks:
            ids = ENTRY_ID_RE.findall(block)
            calls = CALL_RE.findall(block)
            if len(ids) != len(calls):
                print(f"MALFORMED: {path}: {len(ids)} ids vs {len(calls)} calls")
                return None, gaps
            entries.extend(
                (i, c, path.relative_to(ROOT)) for i, c in zip(ids, calls)
            )
    return entries, gaps


def main() -> int:
    failures = []

    ledger_rows = LEDGER_ROW_RE.findall(LEDGER.read_text(encoding="utf-8"))
    obligations = {row[0]: row[1] for row in ledger_rows}
    if len(obligations) != 7:
        failures.append(
            f"ledger declares {len(obligations)} obligations, expected 7"
        )

    entries, gaps = parse_contracts()
    if entries is None:
        return 1
    witness_ids = [e[0] for e in entries]

    # bijection: obligations <-> witnesses
    for ob in obligations:
        hits = [e for e in entries if e[0] == ob]
        if len(hits) != 1:
            failures.append(f"obligation {ob}: {len(hits)} witnesses (need 1)")
    for wid in witness_ids:
        if wid not in obligations:
            failures.append(f"witness {wid}: no obligation row in ledger")
    if len(set(witness_ids)) != len(witness_ids):
        failures.append("duplicate witness ids in CONTRACTS blocks")

    # call targets exist textually
    for wid, call, src in entries:
        module_path, _, fn = call.rpartition(".")
        target = ROOT / (module_path.replace(".", "/") + ".py")
        if not target.exists():
            failures.append(f"{wid}: call module missing: {target}")
            continue
        if f"def {fn}(" not in target.read_text(encoding="utf-8"):
            failures.append(f"{wid}: callable {fn} not found in {target}")

    # RepoLOTO state matches ledger
    locks = (
        {p.name for p in LOTO_DIR.iterdir() if p.is_file() and p.name != "README.md"}
        if LOTO_DIR.exists()
        else set()
    )
    for ob, state in obligations.items():
        if state == "CLOSED" and ob in locks:
            failures.append(f"{ob}: ledger CLOSED but .loto/{ob} still present")
        if state == "OPEN" and ob not in locks:
            failures.append(f"{ob}: ledger OPEN but .loto/{ob} missing")
    for lock in locks:
        if lock not in obligations:
            failures.append(f".loto/{lock}: lock without ledger row")

    print(f"obligations: {len(obligations)}  witnesses: {len(entries)}  "
          f"locks: {len(locks)}")
    print(f"coverage gaps (ucns modules without CONTRACTS): {len(gaps)}")
    for gap in gaps[:20]:
        print(f"  . {gap}")
    if len(gaps) > 20:
        print(f"  ... and {len(gaps) - 20} more")

    if failures:
        print(f"\n{len(failures)} RECONCILIATION FAILURES")
        for f in failures:
            print(f"  ! {f}")
        return 1
    print("\nreconciled: zero unmatched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
# ratios: loc_comments=89:24 imports_exports=3:2 calls_definitions=67:2
