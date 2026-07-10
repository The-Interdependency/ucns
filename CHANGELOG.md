# Changelog

## Unreleased — v1.0 canon reconciliation

### Canon
- Reconciled `ucns-spec.md` to use the status vocabulary (`DEFENDED`, `IMPLEMENTED`, `TEST-BACKED`, `ORACLE-COMPLETE`, `FRONTIER`, `EXPERIMENTAL`) from the 2026-05-16 addendum.
- Replaced binary solved / not-solved language in §F1–F4 with explicit per-layer status.
- Reconciled Theorem N public language to `FRONTIER`: implementation-backed proof sketch, Lean proof pending, awaiting external formal review. Depth-3 asymmetric remains `TEST-BACKED`.
- `ucns-spec-frontier-v090.md` cross-references the reconciled canon and is marked partially superseded for depth-2 implementation status.
- 2026-05-16 addendum's "Next Canon Repair" section marked completed.

### v1.0 scope
- Declared `ucns` the v1.0 public Python API; `ucns_recursive` is retained as a compatibility import path but **deprecated for direct user imports**.
- Declared carrier widening, tractable sub-catalogues, and general recursive primality outside defended-complete domains **out of v1.0 scope**.
- Kept Theorem N out of `DEFENDED` release language until Lean `sorry` leaves and external formal review are discharged.

### Docs
- README, `CLAUDE.md`, and example snippets switched to `from ucns import ...`; status table aligned with the vocabulary.
- A0 rule on `SEQ-PRIME` outside `VERIFIED_DOMAIN_LABELS` documented at the README, spec, and `CLAUDE.md` level.
- Added `docs/claims-ledger.md`, `docs/mathematical-glossary.md`, `docs/reproducibility.md`, and `RELEASE.md` for reviewer-facing v1.0 preparation.
- Glossary now records the multiplicative-unit boundary: unit-group factors are filtered before `SEQ-PRIME` is interpreted.
- Current release-prep branch reconciles README, `ucns-theorem-n.md`, `docs/claims-ledger.md`, and this changelog to conservative Theorem N language.

### Examples
- Added minimal reviewer examples under `examples/depth_examples/` covering depth-1, depth-2 oracle, depth-3 catalogue-sufficient, and catalogue-boundary behavior.

### Tests / metadata
- Tightened `test_depth2_full_domain.py` docstring; no longer claims exhaustive enumeration over the frozen domain.
- Added constructor invariant tests for `A_plus` / `F_plus` length and binary face-bit validation on both `ucns_recursive` and public `ucns` import surfaces.
- Aligned `pyproject.toml` Python classifiers with the CI matrix.
- Retained the factorization envelope test canon from the multiplicative-unit fix: the flat length-2 object is a defended-domain `SEQ-PRIME` example after unit-group factors are filtered.
- Began replacing stale `MODULE_BUILD tests:` paths with real test files used by the current pytest surface.

## v0.8.1 — PyPI Release Candidate

### Packaging
- Added enriched PyPI metadata and classifiers.
- Added project URLs and author metadata.
- Added build + twine validation workflow.
- Added wheel build dependency.

### CI
- GitHub Actions workflow now:
  - builds the package
  - validates metadata via twine
  - installs built wheel artifact
  - runs the UCNS test suite

### Status
UCNS remains an experimental/research-stage algebraic system.
The repository currently defends:
- flat kernel algebra
- depth-1 restricted completeness
- depth-2 oracle completeness

Catalogue-sufficient completeness (Theorem N) is the current implementation-backed frontier proof target, not a fully discharged formal theorem.

### Compatibility
Test target:
- Python 3.8+

### Notes
This release is intended first for TestPyPI validation before public PyPI publication.

GPT generated; context, prompt Erin Spencer.
