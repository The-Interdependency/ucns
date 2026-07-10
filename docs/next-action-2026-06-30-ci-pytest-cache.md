# Next action record — pytest CI + UCNS cache guardrail

Date: 2026-06-30

## Delivered

- Added pytest to dev tooling with a Python 3.8-compatible pin.
- Switched CI commands from unittest-only discovery to the full pytest-discovered suite:
  `python -m pytest ucns_recursive/tests tests -v`.
- Added `ucns_cache/**` to the path-gated CI workflow so cache-only changes trigger CI.
- Updated README and CLAUDE.md so repository instructions no longer point maintainers at a weaker test gate.

## Why pytest is pinned below 8.4

The repository still advertises and tests Python 3.8. Pytest 8.4 dropped Python 3.8 support, so dev tooling must stay on `pytest>=8.3,<8.4` until the project intentionally raises its Python floor.

## Completed follow-up — structural cache witness

`tests/test_ucns_cache_store.py::test_structural_hit_path` now uses an executable stable UCNS fixture with:

```text
shared braider identity
and
distinct canonical identity
```

The witness pair is depth-1, face-zero, length-3 structure over carriers `n_min=1` and `n_min=3`. Under the current primitive-stream derivation, both objects braid to the same structural lattice hash while retaining distinct canonical identities. This closes the prior xfail handoff and keeps the structural cache claim executable rather than aspirational.

## Next atomic action

The structural-hit path is now exercised against the frozen-domain catalogue smoke workload in `scripts/bench_ucns_cache.py`; next, wire A0 read-through/write-through behind `A0_UCNS_CACHE=1` when the downstream checkout is available, still without assigning a performance or reuse-quality claim.

hmmm: the braid got a small catalogue job; the big spoon remains in the sibling kitchen.
