# Canonical Factor Selection

**Status:** DEFENDED (proposition + proof below) + TEST-BACKED
(`ucns_recursive/tests/test_canonical_factorization.py`: validity,
permutation/duplication invariance, prune-invariance, parity with
`UCNSStore.factor_decompose`, key totality).
**Scope:** catalogue-bounded LEFT-FACTOR enumeration — the
`factor_decompose` semantics, complete for the given catalogue per the
v0.6 left-quotient completeness result
(`ucns-v06-left-quotient-completeness.md`). Canonical selection under
PAYLOAD-catalogue semantics (`factor_search_v08`) remains FRONTIER; see
§4.
**Accreditation:** Claude generated from repository context as prompted
by Erin Spencer; verified against `recursive_quotient.left_quotient`,
`serialization.canonical_bytes`, and `store.factor_decompose` at the
commit introducing this file.

---

## 1. The problem

`factor_decompose` returns *all* catalogue-bounded factorizations and
explicitly declines to order them: "The caller is responsible for
choosing among them; no canonical ordering is defined." Theorem N's
search likewise returns the *first* valid pair under loop ordering.
Non-uniqueness is real; what was missing is a deterministic choice
function.

## 2. The selection rule

For a factor pair `(A, B)` define

```
key(A, B) = (canonical_bytes(A), canonical_bytes(B))
```

with lexicographic comparison, and define

```
canonical_factorization(P, C) = min over enumerate_factorizations(P, C) of key
```

returning `SEQ-PRIME` when the enumeration is empty.

## 3. Proposition (determinism) and proof

> **Proposition.** For a fixed object `P` and a fixed catalogue *as a
> set of object values*, `canonical_factorization(P, C)` is uniquely
> determined: independent of catalogue ordering, duplication, iteration
> order, pruning (`prune=True/False`), and process state.

**Proof.**

*(i) The enumerated set is well-defined.* `enumerate_factorizations`
yields `(A, left_quotient(P, A))` for each catalogue element `A` passing
the pointwise checks (quotient exists, exact recomposition, optional
non-triviality). Each check depends only on the values of `P` and `A`,
so the set of yielded pairs (up to object equality) is a function of the
catalogue's value-set — order and multiplicity cannot add or remove a
pair. Pruning removes only candidates whose carrier support escapes
`supp(n_min(P))`; by the Carrier-LCM Law
(`docs/carrier-support-pruning.md`), no such candidate can be a left
factor of `P`, so pruning does not change the enumerated set
(test: `test_invariant_under_pruning`).

*(ii) The key order is total and equality-respecting.* Canonical
serialization mirrors `UCNSObject` equality (serialization module
contract): equal objects produce identical bytes, distinct objects
produce distinct bytes. Lexicographic order on byte-string pairs is a
total order. Hence `key` induces a total order on the enumerated set in
which equal pairs are identified — no hash-collision caveat arises
because no hashing is involved.

*(iii) A finite, nonempty, totally ordered set has a unique minimum.*
The catalogue is finite, so the enumerated set is finite. If nonempty,
its `key`-minimum is unique; if empty, the result is the `SEQ-PRIME`
sentinel. Either way the output is a function of `(P, value-set of C)`
alone. ∎

**Idempotence note.** The selected `A` need not itself be `SEQ-PRIME`
under further decomposition; canonicality here means *deterministic
choice*, not irreducibility of the chosen factors. Recursive canonical
refinement (canonically factor the factors) is a well-defined follow-on
but is not claimed here.

## 4. What this does NOT claim

- No canonical choice under `factor_search_v08`'s payload-catalogue
  semantics: that engine assembles factors rather than drawing them from
  the catalogue, returns first-found, and has no enumerating variant.
  Adding one is the open engineering item; until then, "canonical" is
  scoped to left-factor-catalogue enumeration.
- No claim that the canonical pair is minimal, balanced, or otherwise
  distinguished algebraically — the byte order is a *convention*, chosen
  for totality and stability, not for mathematical meaning.

## hmmm

- recursive canonical refinement (factor the chosen factors canonically)
  — well-defined, unclaimed, one induction away
- enumerating variant of `factor_search_v08` for payload-catalogue
  canonical selection — the declared FRONTIER remainder
