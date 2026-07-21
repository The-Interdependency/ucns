# UCNS — definition-first restart

UCNS is rebuilding from its carrier definition rather than patching the former
factorization kernel.

The previous implementation, specifications, tests, formal work, and
experiments remain preserved under [`archive/`](archive/) with complete Git
history. They are evidence and potential machinery, not current canon.

## Current formal foundation

The carrier is a **directed twofold branched angular cover**:

- Structural Null is the unique coordinate-free absence of distinction.
- Non-null carrier points have a 720-degree lifted period.
- The visible projection has a 360-degree period.
- One visible lap advances to the second lifted representative on the same
  directed path.
- Two visible laps complete the lifted return.
- A 360-degree displacement does not automatically negate, reflect, reverse
  parity or chirality, invert a frame, or transform a payload.

The earlier Möbius/seam account remains provenance only. It is not the formal
object definition. See [`CANON.md`](CANON.md) and
[`docs/chapter-1.md`](docs/chapter-1.md).

## Active code

The root package implements two bounded layers.

### Directed carrier floor

- Structural Null;
- the faithful-breadth-to-radius map supplied with an already-known breadth;
- 720-degree lifted points;
- 360-degree visible projection;
- deck translation and the one/two branch law.

### Structural-support floor

- fail-closed structural cells with finite support `mu >= 0`;
- non-null canonical carriers;
- aggregate support `W` as the sum of present-cell supports;
- Cartesian pairing with multiplicative paired-cell support;
- pruning of zero-support absent cells;
- collapse to Structural Null only after complete cell-support erasure.

See [`docs/STRUCTURE_CONTRACT.md`](docs/STRUCTURE_CONTRACT.md).

It does **not** yet implement a complete `UCNSObject`, domain-specific support
assignment, receipts, metadata, canonical structural equivalence, product
character `M`, faithful-breadth evaluation `B`, typed payload dispatch,
factorization, encoding, or Theorem N.

The structural-support implementation was selectively reconstructed from the
useful parts of experimental branch `ucns-Grok`; the branch was not merged
wholesale because its `M`, `B`, status, and consumer claims remain provisional
or invalid.

## Verification

```text
python tools/verify_skill_lib_contracts.py .
python -m pytest
python -m build
python -m twine check dist/*
```

The source owns skill-lib `MODULE_BUILD` and `CONTRACTS` declarations; tests own
`CHECKS` declarations. The no-exec audit fails closed on undeclared source
modules, missing contracts, unknown witnesses, non-executable check targets, or
unresolved `self::` calls.

## Build doctrine

This build is pinned to
`The-Interdependency/skill-lib@fa6e6200bc274657de2334754bbbf98844ef6541`.
See [`.agents/skills/README.md`](.agents/skills/README.md) and
[`STACK_MANIFEST.json`](STACK_MANIFEST.json).

hmmm: cells and aggregate support now have executable boundaries; receipts,
metadata, recursive structure, equivalence, `M`, and `B` still have to earn
their semantics before they become public structure.
