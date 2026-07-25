# UCNS — option-preserving definition-first restart

UCNS is a stable identifier without a canonical expansion. It is rebuilding as
an option-bearing construction system rather than patching the former
factorization kernel.

The current project exposes UCNS choices and uses EDCM experiments against real
systems to determine an EDCM-scoped ideal configuration. EDCM now fixes a
Möbius causal carrier, superpositioned Structural Null, ordered concatenation,
unit support, exact-evidence baseline, carrier pairing only, and an EDCM-specific
profile while keeping graph contribution and other information-dependent choices
open. Any eventual selection cannot become universal UCNS canon or transfer
proof or measurement validity.

The previous implementation, specifications, tests, formal work, and
experiments remain preserved under [`archive/`](archive/) with complete Git
history. They are evidence and potential machinery, not current canon.

## Option decision surface

Decisions, standing, the current exact profile, and every known unresolved
choice are recorded in
[`docs/UCNS_OPTION_DECISIONS.md`](docs/UCNS_OPTION_DECISIONS.md). The packaged
machine surface is `src/ucns/option_registry.json`, validated by
`ucns.options` and repository tests. Candidate real-system sources and their
access boundaries are recorded in
[`docs/EDCM_REAL_SYSTEM_CORPORA.md`](docs/EDCM_REAL_SYSTEM_CORPORA.md). No option
dimension has a hidden global default.

## Current implemented carrier candidate

The current reference implementation uses a **directed twofold branched angular
cover**. It remains executable comparison evidence but is not an eligible EDCM
target unless it integrates the required Möbius causal chain. For EDCM,
Structural Null is the singular superpositioned space and the twist occurs when
a new gonol initiates; the current code does not yet implement that requirement.

The comparison candidate currently provides:

- a unique coordinate-free null representation, superseded for the EDCM target;
- Non-null carrier points have a 720-degree lifted period.
- The visible projection has a 360-degree period.
- One visible lap advances to the second lifted representative on the same
  directed path.
- Two visible laps complete the lifted return.
- A 360-degree displacement does not automatically negate, reflect, reverse
  parity or chirality, invert a frame, or transform a payload.

See [`CANON.md`](CANON.md) and [`docs/chapter-1.md`](docs/chapter-1.md).

## Status firewall

UCNS distinguishes three statuses:

1. **represented evidence** — retained without being measured;
2. **candidate-measured evidence** — evaluated under a named candidate, policy,
   comparison rule, traversal rule, witness corpus, and experiment manifest;
3. **canonically measured evidence** — selected by an explicit canonization
   decision with alternatives, information loss, rollback, and independent
   evidence recorded.

The repository currently supports the first two. It does not yet contain a
canonical structural equivalence relation, canonical product character `M`, or
canonical faithful breadth `B`.

## Choice preservation

Where several interpretations, representations, policies, or constructions
remain admissible, UCNS preserves the capacity to choose among them.

Unresolved options are not silently collapsed into defaults. Policies produce
non-destructive projections that retain their source evidence and declare
information loss. Set and multiset views require caller-supplied identity keys.

See [`docs/CHOICE_PRESERVATION.md`](docs/CHOICE_PRESERVATION.md) and
[`docs/CHOICE_POLICY.md`](docs/CHOICE_POLICY.md).

## Active code

### Directed carrier floor

- unique Structural Null;
- faithful-breadth-to-radius map for an already-supplied breadth;
- 720-degree lifted points and 360-degree projection;
- deck translation and the one/two branch law.

### Structural-support floor

- fail-closed cells with finite `mu >= 0`;
- non-null canonical carriers;
- cell-only aggregate support `W`;
- Cartesian pairing with multiplicative paired-cell support;
- pruning and complete cell-support collapse.

See [`docs/STRUCTURE_CONTRACT.md`](docs/STRUCTURE_CONTRACT.md).

### Structural policies and retained evidence

- named `StructurePolicy` and `PolicyRegistry` values with no default winner;
- non-destructive projections and explicit loss records;
- repeated retained layers without overwrite;
- explicit presence even for falsey evidence;
- explicit `measured`, `unmeasured`, and `excluded` status;
- a firewall that keeps current `W` cell-only.

See [`docs/RETAINED_STRUCTURE.md`](docs/RETAINED_STRUCTURE.md).

### Explicit comparison and recursive traversal

- exact, absolute, relative, combined, ULP, interval-overlap, and custom
  `ComparisonPolicy` values;
- no hidden numerical tolerance in law suites or candidate comparisons;
- cycle handling by reject, reference receipt, bounded unfolding, or explicit
  fixed-point resolver;
- node and depth budgets with truncation receipts.

See [`docs/COMPARISON_POLICY.md`](docs/COMPARISON_POLICY.md) and
[`docs/TRAVERSAL_POLICY.md`](docs/TRAVERSAL_POLICY.md).

### Retained-layer pairing laboratory

- occurrence-addressed `EnvelopePairPlan` values;
- concatenate, Cartesian, positional zip, side-preserving, selection,
  exclusion, and custom policies;
- explicit unmatched-layer behavior;
- retained left/right source evidence and loss records;
- result layers remain unmeasured.

See [`docs/LAYER_PAIRING.md`](docs/LAYER_PAIRING.md).

### Evaluator and experiment laboratories

- multiple candidates per evaluator kind with explicit version, code reference,
  scope, and policy dependencies;
- law suites retaining pass, failure, exception, witness, and comparison-policy
  evidence;
- content-addressed subjects through explicit versioned adapters;
- development and holdout witness partitions;
- mutation and metamorphic generators;
- greedy counterexample minimization;
- complete experiment manifests and reproduction checks;
- candidate decision packets requiring holdout evidence, rollback, and separate
  candidate, witness, and decision roles.

See [`docs/EVALUATOR_LAB.md`](docs/EVALUATOR_LAB.md) and
[`docs/EXPERIMENT_MANIFESTS.md`](docs/EXPERIMENT_MANIFESTS.md).

### First competing candidate packs

The repository now supplies explicit **noncanonical** candidates:

- exact-adapter, policy-projection, and layer-scoped equivalence signatures;
- geometric-mean, maximum-support, and minimum-support cell-only `M` candidates,
  displayed together for EDCM without a selected winner;
- cell-log-support, cell-detail, and retained-presence `B` candidates, likewise
  displayed together pending more information.

Cell-only candidates fail outside scope rather than treating retained-only
evidence as zero distinction. A passing candidate remains a candidate.

See [`docs/CANDIDATE_PACKS.md`](docs/CANDIDATE_PACKS.md).

## Explicit nonclaims

The package does **not** implement or promote:

- a complete `UCNSObject`;
- canonical structural equivalence;
- canonical `M`;
- canonical `B`;
- a universal retained-layer product;
- canonical numerical equality or recursive identity;
- typed payload dispatch;
- factorization, encoding, embeddings, public-gonol integration, or Theorem N;
- any downstream-consumer dependency;
- a universally selected carrier model;
- an ideal EDCM option configuration.

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

hmmm: the EDCM floor is clearer and the current implementation is more honestly
incomplete. Seven real-system corpus candidates are documented, but ingestion,
failure-first partitions, the directed-cover/Möbius integration, external holdout
custody, and any ideal-configuration claim remain independent truth obligations.
