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

## Remaining visible frontier

`tests/test_ucns_cache_store.py::test_structural_hit_path` remains an intentional xfail until there is a stable UCNS fixture with:

```text
shared braider identity
and
distinct canonical identity
```

That fixture determines whether the structural cache path has an executable witness, or whether the store semantics need to be narrowed.

## Next atomic action

Create or find the smallest valid UCNS object pair that shares `braider_hash` while differing in `canonical_hash`; if impossible under current primitive-stream derivation, document that impossibility and change the structural-hit claim accordingly.

hmmm: the gate is awake now; the remaining unknown is whether the braid has a lawful twin or only a poetic cousin.
