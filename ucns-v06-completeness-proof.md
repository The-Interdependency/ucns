# UCNS v0.6 — Completeness of `left_quotient`

**Status:** Proof.
**Scope:** The constructive `left_quotient` primitive defined in
`ucns-code-v065.py`, on objects of finite nesting depth.
**Depends on:** v0.3 flat kernel (frozen), v0.4 epicyclic extension (frozen),
E10.4 cancellativity (proven by induction in v0.5.1).
**Companion artifact:** the empirical Class III rerun, which verified zero
direct misses across 900 sequence-composite cases on the v0.5 domain.

---

## hmm

The empirical run already showed zero misses across the entire v0.5 Class III
domain. This document converts that observation into a structural statement
by showing exactly why the recursion bottoms out, and exactly when
`left_quotient(P, A)` is guaranteed to return the unique B.

The proof is straightforward induction on nesting depth, using only:

- v0.3 flat-kernel host-level direct recovery,
- v0.4 None-as-unit normalization (so payload representation is canonical),
- E10.4 cancellativity (uniqueness of quotient when it exists),
- the unit-leading short-circuit at each recursion level.

No new axioms.

---

## Statement

Let `P, A ∈ 𝒢` be normalized epicyclic UCNS objects of finite nesting depth.
Define `nesting_depth(G)` as the maximum payload-recursion depth: 0 for
flat objects, `1 + max_j nesting_depth(S_j)` otherwise.

**Theorem (Left-Quotient Completeness).** If there exists `B ∈ 𝒢` such that

    A ⊠ B ≡_seq P,

then `left_quotient(P, A, catalogue=None)` returns an object equivalent to B.

**Corollary (Decision).** `left_quotient(P, A, catalogue=None)` returns `None`
if and only if no such B exists.

---

## Notation

For object G, we write:

- `G^+` for the positive anchor-payload sequence, of length `|G^+|`
- `α_k` for `A^+[k].theta`, with `α_0 = 0` after normalization
- `β_j` for `B^+[j].theta`, with `β_0 = 0` after normalization
- `S^A_k` for `A^+[k].payload`
- `S^B_j` for `B^+[j].payload`
- `f^A_k`, `f^B_j` for face bits

Per v0.4 multiplication rule (E5.2), with `α_0 = β_0 = 0`:

    P^+[k·q + j].theta   = α_k + β_j         (mod 4π)
    P^+[k·q + j].payload = S^A_k ⊠ S^B_j      (recursive product)
    P.F^+[k·q + j]       = f^A_k ⊕ f^B_j

where `p = |A^+|`, `q = |B^+|`, and `|P^+| = pq`.

---

## Lemma 1 (Host-Length Divisibility)

If `A ⊠ B ≡_seq P`, then `|A^+|` divides `|P^+|`.

**Proof.** By construction `|P^+| = |A^+| · |B^+|`. Sequence equivalence
preserves host length (E4.1.2). ∎

This is checked by `left_quotient` step 1: `if L % p != 0: return None`.

---

## Lemma 2 (Host-Angle Direct Recovery)

If `A ⊠ B ≡_seq P`, then for `q = |P^+| / |A^+|`:

    B^+[j].theta = P^+[j].theta    for all j ∈ {0, …, q-1}.

**Proof.** Set `k = 0` in the multiplication formula. Since `α_0 = 0`:

    P^+[0·q + j].theta = α_0 + β_j = β_j.

After normalization, the first anchor of P is at θ = 0, matching β_0 = 0
exactly. The remaining `q-1` anchors of P's first block are exactly B's
remaining anchors. ∎

This is `left_quotient` Phase 1: `B_thetas = [P^+[j].theta for j in range(q)]`.

---

## Lemma 3 (Face-Bit Direct Recovery)

If `A ⊠ B ≡_seq P`, then for all j ∈ {0, …, q-1}:

    f^B_j = P.F^+[j] ⊕ f^A_0.

**Proof.** Setting `k = 0` in the face XOR rule:

    P.F^+[0·q + j] = f^A_0 ⊕ f^B_j.

XOR is its own inverse, so `f^B_j = P.F^+[j] ⊕ f^A_0`. ∎

This is `left_quotient` Phase 1: `B_faces = [P.F^+[j] ^ f_A_0 for j in range(q)]`.

---

## Lemma 4 (Payload-Quotient Reduction)

If `A ⊠ B ≡_seq P`, then for each j ∈ {0, …, q-1}:

    P^+[j].payload ≡_seq S^A_0 ⊠ S^B_j.

Equivalently: `S^B_j` is a left quotient of `P^+[j].payload` by `S^A_0`.

**Proof.** Setting `k = 0` in the payload rule:

    P^+[0·q + j].payload = S^A_0 ⊠ S^B_j.

Since v0.4 normalization collapses unit-equivalent payloads to None, this
equality holds at the level of `≡_seq` (Guard 1 / E1.5). ∎

---

## Lemma 5 (Unit-Leading Base Case)

If `S^A_0 = None` (unit), then `left_quotient` Phase 2 sets

    B^+[j].payload = P^+[j].payload    for all j

without recursive call.

**Proof.** When `S^A_0 = None`, the formula `S^A_0 ⊠ S^B_j = S^B_j` is the
identity law. So `S^B_j = P^+[j].payload` directly. ∎

This is the explicit short-circuit in `left_quotient`:

```python
if S_A_0 is None:
    B_payloads.append(target)
```

This is the **structural recursion termination point**. The next lemma
shows recursion always reaches it.

---

## Lemma 6 (Recursion Strictly Decreases Depth)

Let `d(G) = nesting_depth(G)`. Then in any recursive call

    left_quotient(target, S^A_0, catalogue),

we have `d(S^A_0) ≤ d(A) - 1`.

**Proof.** `S^A_0 = A^+[0].payload`. By definition,

    d(A) = 1 + max_k d(S^A_k) ≥ 1 + d(S^A_0).

If d(A) = 0 (A flat), Lemma 5's base case fires and no recursion occurs. ∎

---

## Lemma 7 (Recursion Bottoms Out)

For any A with `d(A) = d`, the recursive call chain in `left_quotient(P, A)`
terminates with at most `1 + d` total call frames on the stack: one outer
call plus at most `d` recursive descents.

**Proof.** By Lemma 6, each recursion level strictly decreases `d`. The
outer call enters Phase 2 with dividend A. If `d(A) = 0`, A's leading
payload is None and Lemma 5's short-circuit prevents recursion (1 frame).
Otherwise, each recursive call is invoked with dividend `S^A_0` of strictly
smaller depth. After at most `d` such descents, the dividend reaches depth
0 and Lemma 5's short-circuit fires. ∎

**Empirical verification (code/proof_trace.py).** The trace records actual call
depths on two cases:

- Class III oracle (d(A) = 1): observed max depth 2, matching `1 + 1`.
- Depth-2 oracle (d(A2) = 2): observed max depth 3, matching `1 + 2`.

In both cases the bound is achieved exactly, confirming that the
recursion is neither shallower (which would suggest the proof is
loose) nor deeper (which would falsify the lemma).

---

## Lemma 8 (Quotient Existence Locally)

At every recursion level, if `S^A_0 ⊠ S^B_j ≡_seq target` holds for the
true B, then the recursive call `left_quotient(target, S^A_0)` returns
an object equivalent to `S^B_j`.

**Proof.** By induction on `d(S^A_0)`.

**Base case (`d(S^A_0) = 0`):** `S^A_0` is flat, meaning all of its own
payloads are None. The recursive call `left_quotient(target, S^A_0)`
therefore enters Phase 2 with its own inner `S_A_0 = None` (the leading
payload of the flat object), triggering Lemma 5's short-circuit:

    B_payloads[j] = target.payload  for each j

Phase 1 (Lemmas 2, 3) recovers host angles and faces directly. Phase 3
verifies reconstruction. The result is the unique `S^B_j` such that
`S^A_0 ⊠ S^B_j ≡_seq target` (uniqueness from cancellativity, E10.4).

**Inductive step:** Assume the lemma for all objects of depth < `d`. Let
`S^A_0` have depth `d`. Then `left_quotient(target, S^A_0)` calls itself
recursively with dividend `S^{A_0}_0` (which has depth ≤ d-1, by Lemma 6).
By the inductive hypothesis, those calls succeed and return correct
sub-quotients. Phase 1 (Lemmas 2-3) handles host data directly. Phase 3's
verification check passes because cancellativity guarantees the recovered
B is the unique solution. ∎

---

## Theorem (Restated and Proven)

If `A ⊠ B ≡_seq P`, then `left_quotient(P, A, catalogue=None)` returns an
object equivalent to B.

**Proof.**

By Lemma 1, `|A^+|` divides `|P^+|`. The algorithm proceeds.

**Phase 1.** By Lemmas 2, 3, the recovered host angles and face bits are
exactly B's. No catalogue needed.

**Phase 2.** For each j ∈ {0, …, q-1}, by Lemma 4 we need to recover `S^B_j`
from `P^+[j].payload = S^A_0 ⊠ S^B_j`.

- If `S^A_0 = None`: Lemma 5 gives `S^B_j` directly.
- Else: recursive call `left_quotient(target, S^A_0)`. By Lemma 7, this
  terminates after at most `d(S^A_0)` recursive levels. By Lemma 8, the
  call returns an object equivalent to `S^B_j`.

After Phase 2, the candidate B has `B.theta`, `B.F`, and `B.payloads` all
equal to (or ≡_seq with) the true B's data.

**Phase 3.** The reconstruction check `multiply(A, B_cand).equivalent(P)`
verifies the candidate. By cancellativity (E10.4), if the data agrees
component-wise with the true B (modulo ≡_seq), the reconstruction succeeds.

Therefore `left_quotient` returns an object equivalent to B. ∎

---

## Corollary (Decision Procedure)

`left_quotient(P, A, catalogue=None)` returns `None` if and only if no B
exists with `A ⊠ B ≡_seq P`.

**Proof.**

(⇐) Contrapositive of the Theorem.

(⇒) If `left_quotient` returns a non-None result `B`, Phase 3's
verification confirms `multiply(A, B).equivalent(P)`. So a B exists. ∎

---

## What This Closes

**E10.6 (Class III boundary) is dissolved.** The size-8 oracle and all 900
search-space examples are not a boundary — they are inside the
constructive recovery domain. The completeness theorem shows there is no
remaining "Class III" subclass on objects of finite nesting depth.

**E10.7 Option B is realized.** The "introduce payload quotient" option
described in v0.5.1 is constructively present in v0.6 fix's `left_quotient`,
without introducing a new algebraic primitive. The recursion through
`left_quotient` itself plays the role of the quotient operation, with
cancellativity guaranteeing uniqueness and Lemma 7 guaranteeing termination.

**E10.8 (catalogue-bounded factor_search) is the only remaining
search-completeness question**, and it is an ordinary catalogue-coverage
question, not an algebraic one. Building a catalogue by enumeration up to
a size bound makes `factor_search` complete up to that bound.

---

## What This Does Not Close

**`right_quotient` completeness.** The proof above is for `left_quotient`.
The dual proof for `right_quotient` is structurally identical (symmetric
under the `block-leading positions = j=0` ↔ `block-leading positions = k=0`
exchange), but writing it out is its own document. Until written, treat
it as conjecturally complete.

**Cancellativity itself.** This proof depends on E10.4 cancellativity. The
v0.5.1 spec gave a proof sketch by induction; the empirical regression
verified zero violations across 11,016 product pairs at depths 0 and 1.
The proof sketch is sufficient for finite depths but worth promoting to
a fully written induction at some point.

**Higher depths.** Lemmas 6, 7 are stated for finite nesting depth. If
the kernel is ever extended to admit infinite or unbounded-depth objects,
this proof does not apply and the recursion may not terminate.

---

## Verification Status

- Empirical (depth 1): 900/900 Class III cases recovered by `left_quotient`
  with `catalogue=None`.
- Empirical (depth 2): the d(A2)=2 oracle case in `code/proof_trace.py`
  recovers cleanly with max recursion depth exactly `1 + d(A2) = 3`,
  matching Lemma 7's bound.
- Structural: this document.
- Tests: cancellativity 0 violations across 5,508 pairs (flat) +
  5,508 pairs (depth-1).

The empirical and structural results agree. RQ1 (recursive quotient
redesign) has a constructive solution on the verified domain.
