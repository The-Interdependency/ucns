# Workstream 1 — exhaustive payload assignments and factor search

## Defect to eliminate

`ucns.payload_system.solve_payload_system` currently chooses one right quotient per row-zero cell and one left quotient per column-zero cell. When multiplication is non-cancellative, a local equation may have multiple solutions. A first local choice can fail global consistency even though a later choice yields a valid factorization. `factor_search_v08` then returns `SEQ-PRIME` without exhausting the catalogue-bounded assignments.

## Required architecture

Implement a lazy, deterministic, catalogue-bounded solution iterator. The exact internal name may vary; the preferred public/internal split is:

```python
iter_payload_system_solutions(...) -> Iterator[(S_A, S_B)]
solve_payload_system(...) -> first solution or None  # compatibility wrapper
```

Non-negotiable behavior:

- Normalize the input catalogue into deterministic unit-first order.
- Include the `None` payload unit exactly once.
- Deduplicate structurally equal candidates without relying on mutable-object identity.
- Enumerate **every** assignment in the supplied catalogue satisfying
  `multiply(S_A[k], S_B[j]) == P_payloads[k][j]` for all cells.
- Use backtracking and early domain intersection/pruning; do not use a first-match quotient as a completeness step.
- Never silently stop because an arbitrary internal solution count was reached. If an explicit operational limit is retained anywhere, exceeding it must raise a typed exception and must never become `SEQ-PRIME`.
- Preserve deterministic ordering so the legacy “first returned factorization” remains reproducible.

A straightforward complete strategy is sufficient:

1. Iterate each possible `S_A[0]` from the normalized catalogue.
2. For each column `j`, compute the full catalogue subset satisfying row-zero.
3. Backtrack through all combinations of the `S_B[j]` domains, preferably choosing the smallest remaining domain first while preserving deterministic tie order.
4. For each remaining row `k`, intersect all catalogue candidates satisfying every equation against the chosen `S_B` values.
5. Backtrack through all nonempty `S_A[k]` domains.
6. Run a final full-grid consistency check before yielding.

The complete whole-object APIs from PR #96, `division_theory.left_quotients` and `right_quotients`, are not a substitute for catalogue-bounded payload enumeration. They may support the implementation, but the factor-search catalogue remains the explicit candidate boundary.

Update `factor_search_v08` so that, for every host split, it iterates every payload-system solution and every face option. It must continue after:

- witness inconsistency;
- a missing or invalid face assignment;
- a multiplicative-unit factor;
- a failed final recomposition;
- any other rejected candidate.

Only return `SEQ-PRIME` after all host splits, all payload assignments, and all face assignments are exhausted.

Retain exact recomposition as the final acceptance gate.

## Mandatory regression

Add the following as a permanent regression, adjusted only for final API names:

```python
from fractions import Fraction

from ucns import UCNSObject, UNIT, factor_search_v08, multiply


e = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
t2 = UCNSObject(1, 1, [(Fraction(0), e)], [0])
t3 = UCNSObject(1, 1, [(Fraction(0), t2)], [0])

A = UCNSObject(
    2,
    2,
    [(Fraction(0), t3), (Fraction(1), UNIT)],
    [0, 0],
)
B = UCNSObject(
    2,
    2,
    [(Fraction(0), t2), (Fraction(1), UNIT)],
    [0, 0],
)
P = multiply(A, B)

result = factor_search_v08(P, [UNIT, e, t2, t3], prune=False)

assert isinstance(result, tuple)
rec_A, rec_B = result
assert multiply(rec_A, rec_B) == P
```

This test must fail on the old greedy solver and pass only because alternative quotient assignments are explored.

## Additional required tests

- Compare the payload iterator with a brute-force Cartesian-product oracle over several tiny catalogues and all small `p × q` grids generated from known `S_A` and `S_B` values. The yielded solution set must equal the brute-force set exactly.
- Duplicate catalogue entries must not duplicate assignments.
- Assignment and first-factor ordering must be deterministic across runs.
- A valid later assignment must still be reached after an earlier assignment reconstructs a multiplicative-unit factor.
- Every yielded payload assignment satisfies the full grid.
- Every factor pair returned by `factor_search_v08` recomposes exactly.
- `prune=True` and `prune=False` must agree on factor existence for a bounded regression corpus; pruning may change work performed, not truth.

## Workstream 1 acceptance

- The tower regression returns factors.
- The iterator equals brute force on the bounded test universe.
- No first-match helper remains on a path used to justify negative-result completeness.
- `SEQ-PRIME` is reached only through demonstrable exhaustion.

---
