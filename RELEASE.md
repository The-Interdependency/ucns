GPT generated; context, prompt Erin Spencer.

# UCNS Release Checklist

## hmm

This checklist defines the minimum gate for a scoped UCNS v1.0.0 research release.

---

## v1.0.0 scope statement

UCNS v1.0.0 is a scoped, reproducible research release for catalogue-sufficient recursive factorization using the witness-matrix recursive quotient solver.

It does not claim:

- total general recursive primality
- carrier widening beyond frozen bounds
- tractable catalogue discovery
- canonical factor choice among multiple valid decompositions
- depth-general disk-flip content symmetry

---

## Required before tagging v1.0.0

```text
[ ] Full unittest discovery passes.
[ ] Public API smoke surface imports from ucns and ucns.a0_safe.
[ ] Depth examples run without assertion failure.
[ ] Package build succeeds.
[ ] Package metadata check succeeds.
[ ] README, ucns-spec.md, ucns-theorem-n.md, and docs/claims-ledger.md agree on theorem status.
[ ] docs/reproducibility.md describes the current example/test surface.
[ ] CHANGELOG.md includes the release-prep changes.
[ ] pyproject.toml version is bumped only after the above checks pass.
[ ] GitHub tag v1.0.0 is created from the passing commit.
[ ] GitHub release body includes the honest frontier and out-of-scope claims.
[ ] TestPyPI validation succeeds before any public PyPI upload.
```

---

## Release body must preserve the honest frontier

The release body should include this language or equivalent:

```text
This release is not a claim of total general recursive primality. It is a scoped research release for catalogue-sufficient recursive factorization under the status vocabulary documented in the repository. Carrier widening, tractable sub-catalogues, canonical factor choice, and general primality outside declared complete domains remain open frontier work.
```

## hmmm
