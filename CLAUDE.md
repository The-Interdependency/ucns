# UCNS living surface

## Current root

- Formal carrier: directed twofold branched angular cover.
- Lifted period: 720 degrees.
- Visible projection: 360 degrees.
- Structural Null: unique and coordinate-free.
- Active package: carrier floor, structural-cell/support floor, structural-choice
  policies, retained-structure envelope, and evaluator laboratory.
- Implemented structural surface: `Cell`, non-null `Carrier`, cell-only aggregate
  support `W`, Cartesian pairing, pruning, and complete cell-support collapse.
- Implemented policy surface: named policies, independent registry entries,
  non-destructive projections, explicit loss records, and caller-keyed set and
  multiset views.
- Implemented retained-evidence surface: repeated ordered layers, explicit
  presence, optional policy binding, and explicit measured/unmeasured/excluded
  status without silently entering `W`.
- Implemented evaluator surface: multiple candidates per kind, law suites,
  witnesses, failure/error evidence, separation-law builders, and disagreement
  reports without a default winner.
- Full `UCNSObject`: absent by design.
- Canonical `M`, canonical `B`, canonical structural equivalence, typed dispatch,
  arithmetic, factorization, codecs, embeddings, public-gonol bridge, and
  Theorem N: not promoted.

## Candidate boundary

The policy registry, retained envelope, and evaluator laboratory are
infrastructure. They do not establish a canonical policy or mathematical
instrument.

- Do not appoint a default policy or evaluator.
- Do not count retained layers in cell support `W`.
- Do not overwrite repeated layers.
- Do not infer absence from falsey evidence.
- Do not treat a passing candidate as canon without a separate recorded
  selection decision.

## Grok recovery boundary

Useful candidates from branch `ucns-Grok@7aec399` were selectively reconstructed
on current main. Do not restore that branch's current `M`, heuristic `B`, residual
`m_contrib`, package version, EDCM claims, or discharged-status language.

## Source order

1. `CANON.md`
2. `docs/chapter-1.md`
3. `docs/STRUCTURE_CONTRACT.md`
4. `docs/CHOICE_PRESERVATION.md`
5. `docs/CHOICE_POLICY.md`
6. `docs/RETAINED_STRUCTURE.md`
7. `docs/EVALUATOR_LAB.md`
8. `STACK_MANIFEST.json`
9. module `MODULE_BUILD` and `CONTRACTS`
10. test `CHECKS`

## Required gates

```text
python tools/verify_skill_lib_contracts.py .
python -m pytest
python -m build
python -m twine check dist/*
```

hmmm: infrastructure now preserves and tests competing options. The next
construction boundary is actual equivalence, `M`, and `B` candidates over
retained layers, followed by explicit calibration and canonization decisions.
