# Changelog

## Unreleased — v1.0 canon reconciliation

### Canon
- Reconciled `ucns-spec.md` to use the status vocabulary
  (`DEFENDED`, `IMPLEMENTED`, `TEST-BACKED`, `ORACLE-COMPLETE`,
  `FRONTIER`, `EXPERIMENTAL`) from the 2026-05-16 addendum.
- Replaced binary solved / not-solved language in §F1–F4 with explicit
  per-layer status; full frozen depth-2 domain is now stated as
  `IMPLEMENTED` + `TEST-BACKED`, not yet `DEFENDED` at the spec level.
- Marked Theorem N as `DEFENDED` (proof drafted, awaiting external
  formal review); marked depth-3 asymmetric as `TEST-BACKED`.
- `ucns-spec-frontier-v090.md` cross-references the reconciled canon
  and is marked partially superseded for depth-2 implementation status.
- 2026-05-16 addendum's "Next Canon Repair" section marked completed.

### v1.0 scope
- Declared `ucns` the v1.0 public Python API; `ucns_recursive` is
  retained as a compatibility import path but **deprecated for direct
  user imports**. No runtime `DeprecationWarning` is emitted yet.
- Declared carrier widening, tractable sub-catalogues, and general
  recursive primality outside defended-complete domains **out of v1.0
  scope**.

### Docs
- README, `CLAUDE.md`, and example snippets switched to `from ucns
  import …`; status table aligned with the vocabulary.
- A0 rule on `SEQ-PRIME` outside `VERIFIED_DOMAIN_LABELS` documented
  at the README, spec, and `CLAUDE.md` level.

### Tests / metadata
- Tightened `test_depth2_full_domain.py` docstring; no longer claims
  exhaustive enumeration over the frozen domain, accurately describes
  the hand-constructed cases plus compact closure sweep already in use.
- Aligned `pyproject.toml` Python classifiers with the CI matrix
  (3.8, 3.10, 3.12); removed unsupported 3.9, 3.11, 3.13 claims.

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
- catalogue-sufficient completeness (Theorem N)

### Compatibility
Test target:
- Python 3.8+

### Notes
This release is intended first for TestPyPI validation before public PyPI publication.

GPT generated; context, prompt Erin Spencer.
