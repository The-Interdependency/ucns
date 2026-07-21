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

## Choice preservation

Where several interpretations, representations, policies, or constructions
remain admissible, UCNS preserves the capacity to choose among them.

Unresolved options are not silently collapsed into defaults. Current cell tuples
retain order, multiplicity, and operand sidedness as evidence without declaring
that canonical structural semantics are necessarily sequence-based.

The policy layer now supports named projections, multiple coexisting policies,
caller-keyed set and multiset views, retained source evidence, and explicit
information-loss records. It has no default or canonical policy.

See [`docs/CHOICE_PRESERVATION.md`](docs/CHOICE_PRESERVATION.md) and
[`docs/CHOICE_POLICY.md`](docs/CHOICE_POLICY.md).

## Active code

The root package implements five bounded layers.

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
- collapse to Structural Null only after complete cell-support erasure;
- preservation of unresolved order, multiplicity, and operand sidedness.

See [`docs/STRUCTURE_CONTRACT.md`](docs/STRUCTURE_CONTRACT.md).

### Structural-choice policies

- `StructurePolicy` and `PolicyRegistry`;
- non-destructive `Projection` values;
- explicit `InformationLoss` records;
- ordered-sequence, caller-keyed multiset, and caller-keyed set policy
  constructors;
- support for future custom graph, tree, relation, or domain policies.

### Retained-structure envelope

- repeated, ordered retained layers without overwrite;
- explicit presence even for falsey evidence;
- optional policy bindings;
- `measured`, `unmeasured`, and `excluded` contribution status;
- receipt-only or metadata-only non-null evidence;
- a firewall that keeps current `W` cell-only.

See [`docs/RETAINED_STRUCTURE.md`](docs/RETAINED_STRUCTURE.md).

### Evaluator laboratory

- multiple equivalence, product-character, or faithful-breadth candidates;
- no default, best, majority, or automatic winner;
- law suites retaining pass, failure, exception, and witness evidence;
- side-by-side disagreement reports;
- reusable null, nonnegativity, pairing, invariance, sensitivity, and
  separation laws.

See [`docs/EVALUATOR_LAB.md`](docs/EVALUATOR_LAB.md).

The package does **not** yet implement a complete `UCNSObject`, domain-specific
support assignment, canonical structural equivalence, canonical product
character `M`, canonical faithful-breadth evaluation `B`, typed payload
dispatch, factorization, encoding, or Theorem N.

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

hmmm: UCNS now preserves competing structural choices and can compare candidate
instruments. Actual equivalence, `M`, and `B` candidates still have to be
constructed, calibrated, and explicitly selected before they become canon.
