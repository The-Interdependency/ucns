# UCNS living surface

## Current root

- Formal carrier: directed twofold branched angular cover.
- Lifted period: 720 degrees.
- Visible projection: 360 degrees.
- Structural Null: unique and coordinate-free.
- Active package: carrier floor plus structural-cell/support floor.
- Implemented structural surface: `Cell`, non-null `Carrier`, cell-only aggregate
  support `W`, Cartesian pairing, pruning, and complete cell-support collapse.
- Full `UCNSObject`: absent by design.
- `M`, `B`, receipts, metadata, canonical structural equivalence, typed dispatch,
  arithmetic, factorization, codecs, embeddings, public-gonol bridge, and
  Theorem N: not promoted.

## Grok recovery boundary

Useful candidates from branch `ucns-Grok@7aec399` were selectively reconstructed
on current main. Do not restore that branch's current `M`, heuristic `B`, residual
`m_contrib`, package version, EDCM claims, or discharged-status language.

## Source order

1. `CANON.md`
2. `docs/chapter-1.md`
3. `docs/STRUCTURE_CONTRACT.md`
4. `STACK_MANIFEST.json`
5. module `MODULE_BUILD` and `CONTRACTS`
6. test `CHECKS`

## Required gates

```text
python tools/verify_skill_lib_contracts.py .
python -m pytest
python -m build
python -m twine check dist/*
```

hmmm: domain-specific `mu` assignment, receipts, metadata, recursion, canonical
structural equivalence, valid `M`, and faithful `B` remain the next construction
boundary.
