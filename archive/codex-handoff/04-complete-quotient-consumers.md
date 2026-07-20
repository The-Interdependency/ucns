# Workstream 4 — complete quotient consumers

## Required API migration

Build on PR #96’s:

```python
left_quotients(P, A)
right_quotients(P, B)
```

These solution-set APIs are the authoritative complete quotient surface. Re-export them from `ucns` and mirror them through the supported `ucns_recursive` compatibility surface. Export `SolutionLimitExceeded` if it remains part of the behavior contract.

Keep singular `left_quotient` and `right_quotient` for compatibility, but reimplement them on top of the complete solution sets. Their deterministic behavior should be:

- return the first non-unit solution under the documented solution ordering;
- return `None` when no non-unit solution exists, preserving the legacy ambiguity between “no solution” and “only the unit solution”;
- document that callers needing multiplicity or that distinction must use the plural API.

Do not retain the old recursive-direction bug in `right_quotient`. Do not leave public documentation claiming the singular implementation is complete while it still follows a greedy path.

## Store migration

Migrate every quotient consumer found by repository-wide search, including at least:

- `UCNSStore.left_factors`
- `UCNSStore.right_factors`
- `UCNSStore.is_left_factor`
- `UCNSStore.factor_decompose`
- canonical factorization or catalogue helpers that call singular quotients
- tests, examples, and compatibility wrappers that make completeness claims

Required store behavior:

- `left_factors` and `right_factors` consume all quotient solutions. If a stored key has multiple valid remainders, return each `(key, remainder)` deterministically; repeated keys are permitted and must be documented.
- Represent the unit remainder consistently at the compatibility boundary, preferably as `None` where the existing method promises `None`.
- `is_left_factor` is true when the complete solution set is nonempty, including the unit case.
- `factor_decompose` returns every catalogue-bounded nontrivial pair it claims to return; it must not take only the first quotient for each candidate left factor.
- Deduplicate structurally identical pairs.
- If `SolutionLimitExceeded` can occur, propagate it visibly. Never convert it to “no match.” Add an optional limit parameter only if the public behavior is fully documented and tested.

## Required tests

- Preserve every PR #96 quotient-solvability contract.
- Add a recursive, explicitly noncommutative right-quotient regression that fails when left/right payload direction is swapped.
- Singular quotient wrappers recover a non-unit solution even when the first algebraic solution is the unit or an absorbing alternative.
- Plural APIs return all solutions in deterministic order with no duplicates.
- Store methods surface multiple valid remainders for the same key.
- `factor_decompose` matches a brute-force catalogue oracle.
- Limit exceptions propagate and never become false negatives.
- Public import-boundary tests cover the new exports and confirm `import ucns` does not import `ucns_recursive`.

## Workstream 4 acceptance

No public or proof-claimed retrieval path relies on a greedy single quotient to justify “all,” “complete,” or “no false negatives.”

---
