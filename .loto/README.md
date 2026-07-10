# RepoLOTO — base-geometry obligation locks

Protocol (base-geometry completion handoff, §1): a lock file
`.loto/<obligation_id>` is written when work on an obligation starts and is
deleted **only** when the obligation reaches its target rung
(`[mutation-verified]`, or the stated proof rung for proof-only
obligations).  All locks gone = base geometry closed.

`audit/reconcile.py` cross-checks lock state against the `loto` column of
`audit/obligation_ledger.md`: a `CLOSED` row with a surviving lock, or an
`OPEN` row without one, fails the audit.

This README is not a lock; only obligation-id files count.
