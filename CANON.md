# UCNS object canon — directed carrier and structural-support floor

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

## Current implementation boundary

Implemented and test-backed:

1. directed 720-degree lifted carrier and 360-degree visible projection;
2. unique coordinate-free Structural Null;
3. structural-cell support representation and fail-closed zero-test;
4. aggregate cell support `W`;
5. Cartesian carrier pairing and the aggregate-support multiplication law;
6. cell pruning and complete cell-support collapse.

Still unresolved and not promoted:

1. domain-specific rules assigning `mu` to real structures;
2. receipts, metadata, recursion, and their relation to cells;
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

hmmm: cell support and aggregate support now have executable boundaries; the
meaning of retained ordering, receipts, metadata, recursion, equivalence, `M`,
and `B` remains deliberately open.
