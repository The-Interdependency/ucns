# UCNS object canon — directed carrier and reproducible candidate-research floor

## Formal carrier

The formal UCNS carrier is a **directed twofold branched angular cover**.
“Möbius” is retained only as project provenance and is not part of the object
definition.

There is one unique **Structural Null** `N`. Structural Null contains no
coordinate, payload, type, shape, metadata, provenance, receipt, recursive
content, or retained relation.

Every non-null carrier point has:

- faithful breadth `B > 0`;
- radius `a = 1 - exp(-B)`, so `0 < a < 1` for every finite object;
- lifted angular coordinate `phi` modulo `4*pi` (720 degrees);
- visible projection modulo `2*pi` (360 degrees).

For every non-null visible point, the two lifted representatives are
`(a, phi)` and `(a, phi + 2*pi)`. They lie on the same directed path with the
same heading. The second is one visible lap ahead.

The half-period deck translation is `J(a, phi) = (a, phi + 2*pi)`. `J^2`
completes the lifted return.

## What 360 degrees does not imply

A one-lap displacement does not automatically create negation, reflection,
parity reversal, chirality reversal, frame inversion, destructive interference,
or payload transformation. Such effects require an explicitly declared payload
algebra or interaction driver.

## Separation of zeros

These are distinct and may not be substituted for one another:

1. Structural Null `N`: complete absence of distinction.
2. Neutral product character `M = 1`: a proposed non-null multiplicative
   baseline; canonical `M` is not implemented.
3. Algebraic zero `0_V`: zero inside a specific payload algebra.
4. Absent cell `mu(c) = 0`: no structural support at a potential cell.

Algebraic zero does not imply Structural Null. Any retained coordinate, type,
shape, state, provenance, receipt, relation, metadata, or recursive structure
keeps an object non-null.

## Structural-cell floor

The current cell-only floor fixes:

- `mu` is finite and nonnegative;
- `mu = 0` exactly for a field-empty absent cell;
- `mu > 0` requires retained distinction;
- algebraic payload zero remains a distinction;
- a canonical `Carrier` contains at least one present cell and no absent cells;
- empty or all-absent raw collections are Structural Null.

For a canonical carrier with present cells `c_i`:

```text
W(A) = sum_i mu(c_i)
```

Within this cell-only scope:

```text
W(A) = 0  iff  A = N
```

Carrier pairing is Cartesian and paired-cell support is multiplicative:

```text
mu(c pair d) = mu(c) * mu(d)
W(A pair C) = W(A) * W(C)
```

Structural Null is absorbing. Pairing determines which cells meet; it does not
determine typed payload interaction.

## Preservation of unresolved choice

Where more than one interpretation, representation, policy, comparison,
traversal, or construction remains admissible, UCNS preserves the capacity to
choose among them.

Until canon explicitly selects or excludes an option:

- enough information remains to recover every still-admissible option;
- temporary choices are explicit named policies, strategies, lenses, modes, or
  projections;
- defaults remain conveniences and do not acquire canonical standing;
- irreversible sorting, deduplication, flattening, merging, coercion,
  normalization, or overwrite is forbidden when it destroys another admissible
  option;
- operations that require an unresolved choice fail closed unless the choice is
  supplied;
- provenance records the choice and its information loss.

Choice preservation does not preserve disproven options. An option may be
removed by explicit canon, demonstrated invariant failure, proof of
recoverability, or a scoped user choice whose loss is recorded.

## Retained structural layers

A `RetainedStructure` may preserve repeated ordered occurrences of receipts,
metadata, relations, recursive content, provenance, state, and future named
layers without forcing them into cells.

Layer presence is explicit rather than inferred from truthiness. Repeated names
append rather than overwrite. Each occurrence records an optional policy binding
and an explicit contribution state: `measured`, `unmeasured`, or `excluded`.

Current `W` remains cell-only. A receipt-only or metadata-only envelope is
non-null but has zero **cell support**, not proven zero faithful breadth.

## Three evidence statuses

UCNS distinguishes:

1. **represented evidence** — retained without a measurement claim;
2. **candidate-measured evidence** — evaluated by a named candidate under a
   pinned scope, policy set, comparison policy, traversal policy, witness corpus,
   law suite, code reference, and experiment manifest;
3. **canonically measured evidence** — selected through a separate explicit
   decision recording alternatives, information loss, holdout evidence,
   authorship, rollback, and migration behavior.

The current root reaches represented evidence and candidate-measured evidence.
It does not yet reach canonically measured equivalence, `M`, or `B`.

## Explicit comparison policies

Equality and numerical closeness are not hidden implementation details.
Candidate comparisons and law suites require a named versioned
`ComparisonPolicy`.

Admitted infrastructure includes exact, absolute, relative, combined
relative/absolute, units-in-last-place, interval-overlap, and custom policies.
No comparison policy is canonical merely because it is registered or commonly
used.

## Recursive traversal policies

Recursive evidence may be a tree, shared graph, self-reference, mutual
reference, lazy structure, or cyclic system. Traversal therefore requires:

- caller-supplied hashable identity;
- caller-supplied child enumeration;
- explicit cycle mode;
- explicit depth and node budgets.

Cycles may be rejected, retained as reference receipts, unfolded to a declared
budget, or handled by an explicit fixed-point resolver. Budget exhaustion and
truncation produce evidence receipts rather than silent omission.

## Retained-layer pairing laboratory

The established cell carrier continues to pair by Cartesian product. Retained
layers pair only through an explicit occurrence-addressed `EnvelopePairPlan`.

A plan names each left and right layer occurrence, the pairing policy, the result
layer, and the treatment of unmatched occurrences. Available candidate policies
include concatenation, Cartesian pairing, positional zip, side preservation,
left/right selection, exclusion, and custom domain policy.

Every layer-pair result retains left and right sources, the projected view, and
declared losses. Result layers remain unmeasured and do not silently enter `W`,
`M`, or `B`.

## Evaluator and experiment laboratories

Canonical structural equivalence, product character `M`, and faithful breadth
`B` are developed as competing candidates before selection.

The laboratory provides:

- named versioned candidates with code reference, scope, and policy dependencies;
- multiple candidates per kind and no default, best, majority, or automatic
  promotion;
- ordered law suites with explicit comparison policy;
- pass, failure, exception, witness, and disagreement evidence;
- content-addressed subjects through explicit versioned adapters;
- witness corpora separated into development and holdout partitions;
- hand-authored, generated, adversarial, historical, mutation, and metamorphic
  witness origins;
- experiment manifests pinning all research inputs;
- reproduction checks through explicit result adapters;
- counterexample minimization;
- candidate decision packets with separate candidate, witness, and decision
  authorship.

A decision packet is reviewable only when development and holdout evidence pass,
rollback is recorded, and authorship roles remain distinct. Reviewable does not
mean canonical. No packet can make itself canonical.

## Initial candidate packs

The repository supplies explicit noncanonical candidates for pressure testing.

Equivalence candidates:

- exact evidence digest through a named adapter;
- digest after a named policy projection;
- digest over explicitly selected retained-layer names.

Cell-only product-character candidates:

- geometric mean of positive cell supports;
- maximum positive cell support;
- minimum positive cell support.

These candidates are multiplicative under the established Cartesian cell
pairing fixtures, but remain candidates subject to scope, separation, holdout,
and counterexample obligations.

Faithful-breadth candidates:

- logarithm of aggregate cell support;
- cell-detail breadth using support terms and occurrence count;
- retained-presence breadth using cell structure plus retained-layer occurrence
  presence.

Cell-only candidates fail when given retained-only evidence rather than treating
unmeasured distinction as zero.

## Current implementation boundary

Implemented and test-backed infrastructure:

1. directed 720-degree lifted carrier and 360-degree visible projection;
2. unique coordinate-free Structural Null;
3. fail-closed structural cells and cell-only aggregate support `W`;
4. Cartesian cell pairing, pruning, and complete cell-support collapse;
5. preservation of unresolved order, multiplicity, and operand sidedness;
6. structural policy registries, projections, and information-loss records;
7. retained-layer envelopes with explicit presence and contribution status;
8. evaluator registries, laws, witnesses, and disagreement reports;
9. explicit comparison policies;
10. cycle-safe traversal with budgets and receipts;
11. retained-layer pairing plans and result evidence;
12. content-addressed witness corpora and experiment manifests;
13. development/holdout separation, mutation and metamorphic generation,
    reproduction checks, and candidate decision packets;
14. initial noncanonical equivalence, `M`, and `B` candidate families.

Still unresolved and not promoted:

1. domain-specific rules assigning `mu` to real structures;
2. canonical measurement contributions for retained layers;
3. canonical structural equivalence;
4. canonical multiplicative `M` with externally reviewed separation and retained
   layer laws;
5. canonical faithful `B` reporting every retained distinction;
6. external holdout custody and independent candidate calibration;
7. canonical recursive identity, sharing, and fixed-point laws;
8. typed payload dispatch;
9. a complete `UCNSObject`, factorization, encoding, embedding, codec,
   public-gonol bridge, or theorem claim.

The useful cell, `W`, pairing, pruning, and collapse candidates were selectively
reconstructed from experimental branch `ucns-Grok`. Its former `M`, heuristic
`B`, package version, status, and downstream-consumer claims are not canon.

## Retired root doctrine

The following remain removed from formal canon:

- a Möbius strip as the carrier object;
- a localized seam or twist containing hidden zero;
- automatic orientation reversal after 360 degrees;
- first-anchor normalization as geometric zero;
- `None` or a trivial object as multiplicative identity;
- one-circle completion;
- face state inferred from a seam crossing.

hmmm: UCNS can now retain, reproduce, compose, traverse, and pressure candidate
instruments. Canonical equivalence, `M`, and `B` remain on the far side of
independent holdout evidence and an explicit canonization decision.
