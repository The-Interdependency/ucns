# UCNS object canon — directed carrier and option-preserving structural floor

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

A one-lap displacement does not automatically create:

- negation;
- reflection;
- parity reversal;
- chirality reversal;
- frame inversion;
- destructive interference;
- payload transformation.

Any such effect belongs to an explicitly declared payload algebra or
interaction driver, not to carrier topology.

## Separation of zeros

These are distinct and may not be substituted for one another:

1. Structural Null `N`: complete absence of distinction.
2. Neutral product character `M = 1`: a proposed non-null multiplicative
   baseline; `M` is not yet implemented.
3. Algebraic zero `0_V`: zero inside a specific payload algebra.
4. Absent cell `mu(c) = 0`: no structural support at a potential cell.

Algebraic zero does not imply Structural Null. Any retained coordinate, type,
shape, state, provenance, receipt, relation, metadata, or recursive structure
keeps an object non-null.

## Structural-cell zero-test

The current cell-only structural floor fixes the following representation law:

- `mu` is finite and nonnegative;
- `mu = 0` exactly for a potential cell retaining no coordinate, payload, type
  tag, shape, state, provenance, or relation;
- `mu > 0` requires at least one such retained distinction;
- algebraic payload zero remains a distinction and may have positive support.

A canonical `Carrier` contains at least one present cell and contains no absent
cells. Empty or all-absent raw collections are represented only by Structural
Null. This makes an object with aggregate cell support zero but not Structural
Null unrepresentable within the current cell-only scope.

## Aggregate support and pairing

For a canonical carrier with present cells `c_i`, aggregate support is

```text
W(A) = sum_i mu(c_i)
```

Within the current cell-only scope:

```text
W(A) = 0  iff  A = N
```

Carrier pairing is the Cartesian cross-pairing of present cells. Paired-cell
support is multiplicative:

```text
mu(c pair d) = mu(c) * mu(d)
```

Therefore aggregate support is multiplicative under carrier pairing:

```text
W(A pair C) = W(A) * W(C)
```

Structural Null is absorbing. Pairing determines which structural cells meet;
it does not determine typed payload interaction.

Pruning removes only zero-support absent cells. Collapse returns Structural Null
only when no positive-support cells survive after an explicitly supplied
structural erasure.

## Preservation of unresolved choice

Where more than one interpretation, representation, policy, or construction
remains admissible, UCNS preserves the capacity to choose among them.

Until canon explicitly selects or excludes an option:

- enough information must remain to recover every still-admissible option;
- temporary computational choices must be explicit policies, strategies,
  lenses, modes, or projections rather than being conflated with the object;
- defaults remain replaceable and do not acquire canonical standing merely by
  being convenient;
- irreversible sorting, deduplication, flattening, merging, coercion, or
  normalization is forbidden when it destroys distinctions required by another
  admissible option;
- operations that require an unresolved choice fail closed unless the choice is
  supplied;
- provenance records which choice was applied and what information it forgot.

Choice preservation does not keep disproven options alive. An option may be
removed by explicit canon, invariant violation, proof of recoverability, or an
explicitly scoped user decision whose information loss is recorded.

The current cell tuple preserves order, multiplicity, and left/right sidedness
as evidence. It does **not** declare that cells are canonically a sequence rather
than a set, multiset, graph, tree, or another structure.

The structural-choice policy layer now makes those choices explicit:

- multiple policies coexist in a registry with no default winner;
- every projection retains its untouched source evidence;
- ignored or discarded distinctions are reported as information loss;
- set and multiset views require caller-supplied identity keys;
- graph, tree, and future domain interpretations remain registerable policies
  rather than changes to the retained object.

See [`docs/CHOICE_PRESERVATION.md`](docs/CHOICE_PRESERVATION.md) and
[`docs/CHOICE_POLICY.md`](docs/CHOICE_POLICY.md).

## Retained structural layers

Cells are not required to absorb every kind of evidence. A
`RetainedStructure` may preserve repeated, ordered layer occurrences for:

- receipts;
- metadata;
- relations;
- recursive content;
- provenance;
- state;
- future named layers.

Layer presence is explicit rather than inferred from truthiness. Values such as
`0`, `False`, `None`, empty mappings, and empty sequences may remain retained
evidence.

Repeated layer names append and do not overwrite one another. Each layer records
an optional policy binding and one of three contribution states: `measured`,
`unmeasured`, or `excluded` with a scoped explanation.

This representation does not extend cell support. Current `W` still measures
only the cell carrier. A receipt-only or metadata-only envelope is non-null but
has zero **cell support**, not proven zero faithful breadth.

See [`docs/RETAINED_STRUCTURE.md`](docs/RETAINED_STRUCTURE.md).

## Evaluator laboratory

Canonical structural equivalence, product character `M`, and faithful breadth
`B` must be developed as competing candidates before selection.

The evaluator laboratory provides:

- named candidate registries separated by evaluator kind;
- explicit replacement rather than silent overwrite;
- no `default`, `best`, majority, or automatic promotion operation;
- ordered law suites retaining pass, failure, exception, and witness evidence;
- side-by-side candidate comparison that reports disagreement without ranking;
- reusable null, nonnegativity, pairing, invariance, sensitivity, and separation
  laws.

Candidate infrastructure is not an evaluator. Registering or passing a candidate
does not make it canonical. Canonization requires a separate recorded decision
that identifies the selected version, passed laws, witnesses, alternatives,
information loss, and rollback behavior.

See [`docs/EVALUATOR_LAB.md`](docs/EVALUATOR_LAB.md).

## Current implementation boundary

Implemented and test-backed:

1. directed 720-degree lifted carrier and 360-degree visible projection;
2. unique coordinate-free Structural Null;
3. structural-cell support representation and fail-closed zero-test;
4. aggregate cell support `W`;
5. Cartesian carrier pairing and the aggregate-support multiplication law;
6. cell pruning and complete cell-support collapse;
7. preservation of unresolved cell order, multiplicity, and operand sidedness;
8. explicit structural policy registry, projections, and information-loss records;
9. retained-layer envelopes with explicit presence, policy binding, and
   contribution status;
10. evaluator candidate registries, law suites, witness retention, separation
    law builders, and disagreement reports.

Still unresolved and not promoted:

1. domain-specific rules assigning `mu` to real structures;
2. lawful measurement contributions for receipts, metadata, relations,
   recursion, provenance, and state;
3. canonical structural equivalence;
4. a nontrivial multiplicative product character `M`, witnessed distinct from
   `W` under the actual pairing law;
5. a faithful-breadth evaluator `B` that reports every retained distinction;
6. typed payload dispatch;
7. a complete `UCNSObject`, factorization, encoding, embedding, codec, public
   gonol bridge, or theorem claim.

The useful cell, `W`, pairing, pruning, and collapse candidates were selectively
reconstructed from experimental branch `ucns-Grok`. Its current `M`, `B`,
package version, status, and downstream-consumer claims are not canon.

## Retired root doctrine

The following are removed from formal canon:

- a Möbius strip as the carrier object;
- a localized seam or twist that contains hidden zero;
- automatic orientation reversal after 360 degrees;
- first-anchor normalization as geometric zero;
- `None` or a trivial object as multiplicative identity;
- one-circle completion;
- face state inferred from a seam crossing.

hmmm: UCNS can now retain the unresolved structure, apply explicit competing
policies, and compare candidate instruments. The next truth boundary is the
construction and calibration of actual equivalence, `M`, and `B` candidates over
retained layers without mistaking infrastructure for mathematical validity.
