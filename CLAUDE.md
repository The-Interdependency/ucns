# UCNS living surface

## Current root

- Formal carrier: directed twofold branched angular cover.
- Lifted period: 720 degrees.
- Visible projection: 360 degrees.
- Structural Null: unique and coordinate-free.
- Active package: carrier floor only.
- Full `UCNSObject`: absent by design.
- Arithmetic, factorization, codecs, embeddings, public-gonol bridge, and
  Theorem N: not promoted.

## Source order

1. `CANON.md`
2. `docs/chapter-1.md`
3. `STACK_MANIFEST.json`
4. module `MODULE_BUILD` and `CONTRACTS`
5. test `CHECKS`

## Required gates

```text
python tools/verify_skill_lib_contracts.py .
python -m pytest
python -m build
python -m twine check dist/*
```

hmmm: `mu`, `W`, `M`, `B`, and canonical structural equivalence remain the
next construction boundary.
