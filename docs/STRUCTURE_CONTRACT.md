# UCNS structural-support contract

**Status:** test-backed foundations surface.  
**Consumers:** none currently. This is an internal UCNS contract, not a downstream compatibility promise.

## Purpose

This contract records the useful structural floor selectively recovered from the
experimental `ucns-Grok` branch without promoting that branch's provisional
product character, faithful-breadth heuristic, package version, or EDCM claims.

## Public surface

| Surface | Meaning | Standing |
|---|---|---|
| `Cell` | potential structural cell with definitive finite support `mu >= 0` | implemented and test-backed |
| `Carrier` | canonical non-null collection of present cells | implemented and test-backed |
| `make_carrier()` | prune raw potential cells and return `Carrier` or unique Structural Null | implemented and test-backed |
| `support_weight()` | aggregate support `W`, the sum of present-cell supports | implemented and test-backed |
| `pair()` | Cartesian carrier pairing with paired support multiplication | implemented and test-backed |
| `prune()` | remove only zero-support absent cells | implemented and test-backed |
| `collapse()` | collapse to Structural Null only after complete cell-support erasure | implemented and test-backed |

## Cell zero-test

A cell is absent exactly when:

```text
mu == 0
and
no coordinate, payload, type tag, shape, state, provenance, or relation remains
```

A present cell has finite `mu > 0` and retains at least one structural
distinction. Algebraic payload zero is still a retained value and therefore does
not imply absence.

Invalid states fail closed:

- negative or non-finite `mu`;
- `mu == 0` with retained fields;
- `mu > 0` with no retained field.

## Carrier and null law

A directly constructed `Carrier` is always non-null and contains only present
cells. Empty and all-absent raw collections are represented only by the unique
`STRUCTURAL_NULL`, through `make_carrier()` or `collapse()`.

Therefore the structural-support floor has a unique aggregate-support zero:

```text
support_weight(A) == 0  iff  A is STRUCTURAL_NULL
```

This claim is scoped to the current cell-only structure. Receipts, metadata, and
recursive structure have not yet been admitted into the object model.

## Pairing law

For present cells `c` and `d`:

```text
mu(c pair d) = mu(c) * mu(d)
```

For canonical carriers:

```text
W(A pair C) = W(A) * W(C)
```

Structural Null is absorbing. Pairing defines where cells meet; it does not
define typed payload interaction.

## Explicit exclusions

This contract does not define or authorize:

- a product character `M`;
- faithful breadth `B`;
- canonical structural equivalence;
- receipt or metadata semantics;
- typed payload dispatch;
- a complete `UCNSObject`;
- factorization, encoding, embedding, or theorem claims;
- any EDCM or other downstream-consumer dependency.

## Provenance

Candidate field inventory, support aggregation, Cartesian pairing, pruning, and
collapse fixtures were recovered from branch `ucns-Grok` at commit
`7aec3997879b5b7f748445f92f9faab92a0ed0dc`. The recovered material was
reconstructed on current `main`; it was not merged wholesale because the branch
also contained an invalid multiplicativity claim for `M`, a provisional `B`
heuristic, representable non-null objects with zero breadth, and premature status
language.

hmmm: the next boundary is deciding whether receipts, metadata, recursion, and
ordering are cells, relations among cells, or distinct structural layers before
canonical equivalence and faithful breadth can be defined.
