# UCNS v0.8 — Lemma 8: Depth-3 Factor Search

**Status:** Closure theorem proven. Soundness discharges by reduction.
Completeness on multiplicative-D'' open, with the gap precisely characterized.
**Scope:** `factor_search_v08` applied to depth-3 objects, using a depth-2
oracle catalogue as payload basis.
**Depends on:** Lemma 7 (depth-2 oracle theorem), E10.4 cancellativity,
v0.6 left-quotient completeness, recursive multiply structural definition.
**Supersedes:** the prior-turn draft that defined "catalogue covers D''" in
terms of factor pairs (A, B ∈ C). That definition was structurally wrong —
the catalogue is a payload basis, not a factor-pair set. See §1.2.

---

## hmm

This document is split into three theorems plus the reframed coverage
condition. The split exists because the prior single-statement Lemma 8
draft conflated three independent facts:

- **Closure** of multiplicative-D'' inside the depth-3 oracle class.
- **Soundness** of `factor_search_v08` on depth-3 inputs.
- **Completeness** of `factor_search_v08` on multiplicative-D''.

The first two discharge cleanly. The third is the genuinely open content.
Splitting them out lets the docstring (`hmmm 4` from prior session) update
honestly: soundness holds unconditionally, closure holds, completeness is
empirically witnessed but not theorem'd.

---

## §1 — Reframed setup

### §1.1 Domains

Let `D'` denote the frozen depth-2 domain (depth ≤ 2, |A⁺| ≤ 3, n_min ≤ 4),
with the oracle-class predicate `is_in_oracle_class` from `domains.py`.

Let `D'_oracle ⊆ D'` denote the depth-2 oracle class (objects that
`is_in_oracle_class` accepts: depth ≤ 2 with all payloads being depth ≤ 1
oracle atoms, plus the unit).

Define two depth-3 domains:

- **Constructive D''** (the output of `build_catalogue_d3_oracle`):
  the set of objects of depth exactly 3, every payload in `D'_oracle`,
  every angle/face combination accepted by the canonical constructor.

- **Multiplicative D''** (the algorithmic-reach target of Lemma 8):
  the set `{ multiply(A, B) : A, B ∈ D'_oracle, multiply(A, B) defined,
  depth(multiply(A, B)) = 3 }`.

These are *not* the same set. §2 (Closure) shows multiplicative ⊆
constructive. The converse is false in general (constructive objects
that are SEQ-PRIME at depth-3 exist; the depth-3 sweep's
`FALSE-NEGATIVE` outcomes are candidates).

### §1.2 What "catalogue" means in `factor_search_v08`

Reading `factor_search_v08.py` lines 80–127: the `catalogue` parameter is
passed to `solve_payload_system` and is used as the candidate set for
filling `S_A` and `S_B` — the **payload sequences** of the reconstructed
factors `A` and `B`. The catalogue is **not** a set of factor pairs.

The prior-turn draft defined "C covers D'' iff for every P ∈ D'', ∃ A, B ∈
C with multiply(A, B) ≡_seq P." This treats C as a factor-pair source.
Wrong. The correct definition is below.

### §1.3 Coverage condition (corrected)

**Definition (catalogue covers a target domain).** Let `T` be a target
domain (subset of UCNS objects). A catalogue `C` (list of UCNS objects
including possibly `None`) **covers** `T` iff for every `P ∈ T`,
there exist UCNS objects `A`, `B` such that:

1. `multiply(A, B) ≡_seq P`,
2. every payload of `A` and every payload of `B` lies in `C`,
3. the angle and face structures of `A` and `B` are consistent with
   the host-recovery and face-recovery procedures of `factor_search_v08`.

**Operative content.** This is the condition the algorithm actually
needs. Lemma 7 at depth-2 uses C = depth-1 oracle catalogue
(`generate_payload_catalogue()`) and the target T = D'_oracle. Lemma 8
at depth-3 uses C = depth-2 oracle catalogue
(`build_catalogue_d2_oracle()`) and the target T = multiplicative-D''.

### §1.4 Multiply structural recursion (assumed, used below)

For depth ≥ 1 objects A, B with compatible host structure,
`multiply(A, B)` produces an object whose payloads at each cell index
`(k, j)` are `multiply(A.payloads[k], B.payloads[j])`. This recursion
is the operative definition of `multiply` at all depths — verified for
depth-2 in v0.5/v0.6, and confirmed at depth-3 by direct inspection of
`canonical.py:189` (`new_payload = multiply(S_k_A, S_j_B)`, genuinely
recursive, no depth-conditional branches).

---

## §2 — Theorem 8a: Closure

**Theorem 8a (Multiplicative-D'' ⊆ Constructive-D'').** If `A, B ∈
D'_oracle` and `multiply(A, B)` is defined and has depth 3, then
`multiply(A, B)` lies in constructive-D''.

**Proof.** Let `P = multiply(A, B)`. We must show:

(i) `depth(P) = 3` — given.
(ii) every payload of `P` is in `D'_oracle`.
(iii) `P` satisfies the canonical-constructor well-formedness conditions.

For (iii): the codomain of `multiply` is by construction a canonical
UCNS object. Discharges by definition of `multiply`'s output type.

For (ii): by §1.4, each payload of `P` at cell `(k, j)` is
`multiply(A.payloads[k], B.payloads[j])`. Since `A, B ∈ D'_oracle`,
both `A.payloads[k]` and `B.payloads[j]` lie in the depth-1 oracle
class (by definition of `is_in_oracle_class` at depth 2: all payloads
are oracle atoms, i.e. depth ≤ 1).

Apply Lemma 7 (depth-2 oracle closure, which is the contrapositive
specialization): if X, Y are depth-1 oracle atoms, then
`multiply(X, Y)` lies in `D'_oracle`. (Lemma 7's content is exactly
that the oracle class is closed under multiply at depth-2.)

Therefore each payload of `P` lies in `D'_oracle`. Combined with (i),
`P` satisfies the constructive-D'' definition.   ∎

**Corollary (Closure is monotone).** Closure at depth k+1 follows from
closure at depth k by the same argument applied recursively. The proof
above is the depth-3 instance of a single induction on depth that
generates the entire oracle hierarchy. *hmmm — this corollary is stated
but the inductive step beyond depth-3 is not formally written here;
the construction `is_in_oracle_class_d4`, `_d5`, etc. would need to
exist for each level, and the iteration cost (§3.3) compounds. Out of
scope for this document.*

---

## §3 — Theorem 8b: Soundness

**Theorem 8b (Soundness).** For any catalogue `C` and any input `P`,
if `factor_search_v08(P, C)` returns `(A, B)`, then
`multiply(A, B) ≡_seq P`.

**Proof.** Step 5 of the algorithm (`factor_search_v08.py` line 124) is
the literal check `multiply(A_cand, B_cand) == P`. The function returns
`(A, B)` only when this equality holds. Equality of canonical UCNS
objects implies sequence-equivalence (`≡_seq` is implied by `==` in the
canonical layer; v0.5 normalization). Discharges directly.   ∎

**Note.** Soundness is depth-agnostic — the proof inspects only the
final verification step, which is identical at all depths. This is why
the docstring update (`hmmm 4`) can claim soundness unconditionally.

---

## §4 — Theorem 8c: Completeness on multiplicative-D'' (OPEN)

**Conjecture 8c (Completeness).** Let `C = build_catalogue_d2_oracle()`.
For every `P ∈ multiplicative-D''`, `factor_search_v08(P, C)` returns
`(A, B)` with `multiply(A, B) ≡_seq P` (i.e. does not return SEQ-PRIME).

### §4.1 Status

Empirically witnessed but not proven.

The depth-3 sweep (Item 2 of prior session) reported, with the
narrow-tailored catalogue:

    {'FALSE-NEGATIVE': 2, 'SUCCESS': 13, 'ALT-FACTOR': 1}

This sweep enumerated targets in *constructive-D''*, not multiplicative-D''.
The 2 FALSE-NEGATIVE outcomes are consistent with two distinct
explanations:

(a) The targets lie in multiplicative-D'' and the algorithm fails to
    find a factorization — completeness violation.
(b) The targets lie in constructive-D'' \ multiplicative-D'' (depth-3
    oracle objects that genuinely don't factor through D'_oracle) —
    correct SEQ-PRIME behavior, not a completeness violation.

The sweep methodology cannot distinguish (a) from (b) without an
independent oracle for multiplicative-D'' membership.

### §4.2 What discharging Conjecture 8c requires

Lemma 7's completeness proof at depth-2 was carried by the witness
matrix machinery (`witness_matrix.py`): the global consistency check
on the p×q witness grid is what guarantees that if a factorization
exists, the algorithm finds one. The proof relied on:

- (W1) host recovery is exact when n factors as p × q,
- (W2) the payload system has a solution iff the target has a
  factorization with payloads in C,
- (W3) the witness matrix is globally consistent iff the candidate
  payload sequences extend to a real factorization.

The depth-3 case inherits W1 (host recovery is structural, not
depth-dependent). W2 and W3 are the open content:

- **W2 at depth-3:** does `solve_payload_system` produce all valid
  `(S_A, S_B)` candidates when payloads are themselves depth-2 objects?
  The depth-2 case only had to solve for depth-1 payloads in C.
  At depth-3, each payload-system equation
  `multiply(S_A[k], S_B[j]) == P_payloads[k][j]` is *itself* a
  depth-2 factorization problem. The depth-3 solver must call the
  depth-2 solver as a subroutine.

  *Open question:* if the depth-2 subroutine is complete on its
  domain (Lemma 7), and every payload in the depth-3 problem lies
  in that domain (which Theorem 8a guarantees for multiplicative-D''
  targets), does the depth-3 outer solve succeed? This is the
  conjecture's reduction to the depth-2 case — needs the recursive
  call structure of `solve_payload_system` audited explicitly.

- **W3 at depth-3:** is the witness matrix's `globally_consistent()`
  check still sound and complete when the witnesses are themselves
  factorizations of depth-2 objects? The check operates on the
  *equality* of witness payload pairs, which is depth-agnostic at
  the canonical-object level — but row/column consistency may
  acquire new degrees of freedom at depth 3 that the depth-2
  formulation didn't anticipate.

### §4.3 Discharge plan (recommended next steps, not part of this proof)

1. Read `payload_system.solve_payload_system` end-to-end and
   characterize its recursive call structure when payloads have
   depth > 1. Determine whether it currently calls a depth-2-aware
   solver or implicitly assumes depth-1 payloads.

2. If implicit depth-1 assumption is found, that's a code-level
   bug-or-gap, not a proof gap — the algorithm doesn't currently
   solve the depth-3 case correctly, and the empirical SUCCESSes
   are coincidence (small/symmetric cases).

3. If it does call recursively, write the formal statement
   "`solve_payload_system` is complete at depth k assuming
   completeness at depth k-1" and discharge by induction.

4. Re-run the depth-3 sweep with the full
   `build_catalogue_d2_oracle()` catalogue (not the narrow-tailored
   one) and classify the FALSE-NEGATIVE cases against multiplicative
   reachability — this is the empirical separation of (a) vs (b)
   from §4.1.

---

## §5 — Operative consequences

### §5.1 Frontier table promotion

| Row | Prior status | New status |
|---|---|---|
| Cancellativity (E10.4) | ✅ | ✅ (unchanged) |
| Right-quotient completeness | ✅ | ✅ (unchanged) |
| Depth-2 oracle (Lemma 7) | ✅ | ✅ (unchanged) |
| Multiplicative-D'' ⊆ Constructive-D'' | not stated | ✅ (Theorem 8a) |
| Soundness at depth-3 | not stated | ✅ (Theorem 8b) |
| Completeness at depth-3 (multiplicative target) | 🟡 empirically GREEN | 🟡 conjecture, gap characterized |
| Carrier widening | 🔴 | 🔴 (unchanged, out of scope) |

Net: depth-3 row stays 🟡, but the gap is now precisely a single open
question (W2 + W3 at depth-3, reducible to a `solve_payload_system`
audit) rather than a vague "no theorem yet."

### §5.2 `factor_search_v08` docstring update

Current text: `"frozen depth-2 domain"`.

Replacement (defensible against this document):

```
factor_search_v08 — soundness on all UCNS inputs (Theorem 8b).
Completeness:
  - depth-2 oracle class: unconditional (Lemma 7).
  - depth-3 multiplicative class: conjectured under
    catalogue = build_catalogue_d2_oracle() (Conjecture 8c, open).
Outside these classes, SEQ-PRIME may be returned for objects
that admit factorizations not expressible in the catalogue.
```

This is the docstring change that closes `hmmm 4` from the prior
session — it states what's true honestly without overclaiming.

### §5.3 PyPI implication

Conjecture 8c being open does **not** block PyPI. The library's
correctness contract is soundness (Theorem 8b), which is
unconditional. Completeness is a quality-of-search guarantee, and
the docstring update above accurately conveys the partial state.

The remaining PyPI blockers are unchanged from prior session:
hmmm 3 (`store.py` non-uniqueness), hmmm 7 (snapshot file at repo
root), and the carrier widening question (hmmm 6).

---

## §6 — New hmmm items surfaced

- **hmmm A' (replaces hmmm A from prior turn):** Conjecture 8c — depth-3
  completeness on multiplicative-D''. The gap is now §4.2's W2 + W3
  reduction to a `solve_payload_system` recursive-call audit. Scoped,
  not vague.

- **hmmm D (DISCHARGED — recorded for audit trail):** §1.4's depth-3
  multiply lift was initially flagged as *assumed* consistent. Spot-check
  on `canonical.py:189` confirmed: `new_payload = multiply(S_k_A, S_j_B)`
  is genuinely recursive over payloads with no depth-conditional
  branching. Theorem 8a's proof of (ii) stands.

- **hmmm E (new):** Theorem 8a's corollary (closure at depth k+1 from
  depth k) suggests a single induction generates the oracle hierarchy
  to arbitrary depth. The catalogue-builder iteration cost compounds
  exponentially per level, so the *theorem* scales but the *practical
  algorithm* does not. Worth flagging in any future "depth-N reach"
  documentation.

---

*Document scope ends here. The sigma-tensor / Theta-kernel and
recursive multiset equivalence (§E4.2, §E13) layers remain outside
this proof's frontier.*
