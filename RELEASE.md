GPT generated; context and canon by Erin Spencer.

# UCNS Release Checklist

## hmm

This checklist defines the minimum gate for a scoped UCNS v1.0.0 research release.

## Current candidate

The repository is preparing `1.0.0rc1`. The release candidate is intentionally
not the final `1.0.0` tag and must not be represented as a proof promotion.
Theorem N remains `FRONTIER`; the Lean completeness obligations remain
`sorry`-closed and external formal review remains pending.

Candidate package, metadata, wheel, import-surface, examples, formal public-frame
checks, and test gates must pass before merge. TestPyPI validation remains
required before any final public PyPI publication or `v1.0.0` release decision.

---

## v1.0.0 scope statement

UCNS v1.0.0 packages two deliberately separated surfaces:

1. the canonical public 157-gonal whose position `0` is SPACE/ZERO, the Möbius
   twist seam and fixed system origin; one 360-degree circuit changes
   orientation and complete return requires 720 degrees;
2. a scoped normalized recursive factorization research subsystem using the
   witness-matrix recursive quotient solver.

No bridge between those surfaces is assumed. Theorem N is a `FRONTIER` proof
target inside the normalized factorization subsystem.

It does not claim:

- a public-gonol ↔ normalized-factorization bridge
- proof that internal multiplication preserves the public twist, origin,
  orientation, faces, chirality, or lifted traversal
- catalogue-sufficient completeness as a discharged theorem
- total general recursive primality
- carrier widening beyond frozen internal bounds
- tractable catalogue discovery
- canonical factor choice among multiple valid decompositions
- depth-general disk-flip content symmetry
- a PTCA, Fano-plane, octonion, embedding-quality, cryptographic-security, EDCM,
  or METAPAT validity result

---

## Required before tagging v1.0.0

```text
[ ] Full pytest discovery passes on every supported Python version.
[ ] Public API smoke surface imports from ucns and ucns.a0_safe.
[ ] PUBLIC_GONOL_157 source commit and arrangement digest are pinned.
[ ] SPACE/ZERO origin, fixed-origin transforms, lifted traversal, and 720-degree return tests pass.
[ ] PrivateGonal exposes no application-level 2π inscription method.
[ ] Classical disk/embedding compatibility utilities are clearly noncanonical.
[ ] Public-frame bridge obligations PG-4 and PG-5 remain visibly OPEN.
[ ] Depth examples run without assertion failure and make no proof promotion.
[ ] Package build succeeds.
[ ] Package metadata and Twine checks succeed.
[ ] README, RELEASE.md, ucns-spec.md, ucns-theorem-n.md, docs/public-gonol.md, and docs/claims-ledger.md agree on canon and theorem status.
[ ] docs/reproducibility.md describes the current example/test surface.
[ ] CHANGELOG.md includes the public-gonol recovery.
[ ] TestPyPI validation succeeds before any public PyPI upload.
[ ] pyproject.toml version is bumped only after the above checks pass.
[ ] GitHub tag v1.0.0 is created from the passing commit.
[ ] GitHub release body includes the fixed-origin canon, honest frontier, and out-of-scope claims.
```

---

## Release body must preserve the canon and honest frontier

The release body should include this language or equivalent:

```text
UCNS is rooted in the canonical public 157-gonal. Position 0 is SPACE/ZERO,
the Möbius twist seam and fixed origin for the entire system. One 360-degree
circuit changes orientation; complete return requires 720 degrees.

This release also contains a separately scoped normalized recursive
factorization subsystem. Theorem N remains FRONTIER: the implementation-backed
proof sketch and Lean scaffold do not confer DEFENDED status, and no bridge from
the public gonol is assumed. Carrier widening, tractable sub-catalogues,
canonical factor choice, public/internal composition correspondence, and
general primality outside declared complete domains remain open.
```

## hmmm

A green candidate establishes reproducible packaging and the declared scoped
software surfaces. It does not discharge mathematical proof obligations by
version number and does not manufacture the missing bridge.
