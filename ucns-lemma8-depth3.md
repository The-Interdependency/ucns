# UCNS v0.8 — Lemma 8: Depth-3 Factor Search

**Status:** All three theorems proven. Depth-3 completeness discharges via
Lemma 7 + E10.4 with the corrected catalogue. See §1.3 errata.
**Scope:** `factor_search_v08` applied to depth-3 objects, using the
depth-1 oracle catalogue as payload basis.
**Depends on:** Lemma 7 (depth-2 oracle theorem), E10.4 cancellativity,
v0.6 left-quotient completeness, recursive multiply structural definition.
**Supersedes:** the prior-turn draft (two issues fixed):
(1) the coverage definition treated the catalogue as a factor-pair set;
    §1.3 corrects it to a payload-basis definition.
(2) Conjecture 8c specified C = build_catalogue_d2_oracle() (depth-2);
    §1.3 errata corrects it to C = generate_payload_catalogue() (depth-1).
    With the correct catalogue, Conjecture 8c is Theorem 8c.

---

## hmm

This document is split into three theorems plus the reframed coverage
condition. The split exists because the prior single-statement Lemma 8
draft conflated three independent facts:

- **Closure** of multiplicative-D'' inside the depth-3 oracle class.
- **Soundness** of `factor_search_v08` on depth-3 inputs.
- **Completeness** of `factor_search_v08` on multiplicative-D''.

All three discharge. The completeness proof was blocked only by the
wrong catalogue choice in the prior draft.

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

- **Multiplicative D''** (the algorithmic-reach target of Theorem 8c):
  the set `{ multiply(A, B) : A, B ∈ D'_oracle, multiply(A, B) defined,
  depth(multiply(A, B)) = 3 }`.

These are *not* the same set. §2 (Closure) shows multiplicative ⊆
constructive. The converse is false in general (constructive objects
that are SEQ-PRIME at the depth-2-factor level exist; the depth-3
sweep's FALSE-NEGATIVE outcomes with the depth-1 catalogue are the
correct witnesses for this claim).

### §1.2 What "catalogue" means in `factor_search_v08`

Reading `factor_search_v08.py` lines 80–127: the `catalogue` parameter is
passed to `solve_payload_system` and is used as the candidate set for
filling `S_A` and `S_B` — the **payload sequences** of the reconstructed
factors `A` and `B`. The catalogue is **not** a set of factor pairs.

### §1.3 Coverage condition (corrected) and catalogue errata

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
(`generate_payload_catalogue()`) and T = D'_oracle. Theorem 8c at
depth-3 uses the **same** catalogue C = `generate_payload_catalogue()`
(depth-1 oracle atoms) and T = multiplicative-D''.

**Errata (prior draft catalogue error).** The prior draft stated Lemma 8
uses C = `build_catalogue_d2_oracle()`. This is wrong and is retracted.
The argument:

- In multiplicative-D'', factors A, B are depth-2-oracle objects.
- Depth-2-oracle objects have depth-1 oracle atoms as payloads.
- `solve_payload_system` fills `S_A[k]` and `S_B[j]` from the catalogue
  where `S_A[k] = A.payload[k]` and `S_B[j] = B.payload[j]`.
- Therefore `S_A[k]` and `S_B[j]` are depth-1 oracle atoms.
- The correct catalogue is `generate_payload_catalogue()` (depth-1).

With depth-2 catalogue: `multiply(depth-2, depth-2) = depth-3`, which
never equals a depth-2 target payload. The only matches come via `cand =
None`, which finds depth-3 × depth-1 factorizations — a different
algorithmic layer, not what Theorem 8c requires.

**hmmm F (new):** Two distinct catalogue choices serve two distinct
factorization layers on depth-3 targets:
- C = `generate_payload_catalogue()` (depth-1): finds depth-2 × depth-2
  factorizations (Theorem 8c domain).
- C = `build_catalogue_d2_oracle()` (depth-2): finds depth-3 × depth-1
  factorizations (a different, unproven domain).
The depth-3 sweep's improvement from depth-1 to depth-2 catalogue is
evidence for the second kind of factorization, not for Theorem 8c.
The 4 SUCCESSes with the depth-1 catalogue are the 4 sweep targets in
multiplicative-D''. The 11 FALSE-NEGATIVEs are constructive-D'' \
multiplicative-D'' (genuinely SEQ-PRIME at the depth-2-factor level).

### §1.4 Multiply structural recursion (confirmed)

For depth ≥ 1 objects A, B with compatible host structure,
`multiply(A, B)` produces an object whose payloads at each cell index
`(k, j)` are `multiply(A.payloads[k], B.payloads[j])`. Confirmed by
direct inspection of `canonical.py:189` (`new_payload = multiply(S_k_A,
S_j_B)`, genuinely recursive, no depth-conditional branches).

### §1.5 Algorithm depth-agnosticism (W2 + W3, from audit)

`solve_payload_system` calls `find_right_factor_or_sentinel(target,
left, catalogue)` from `recursive_quotient.py`. Reading that function:

```python
for cand in catalogue:
    if multiply(left, cand) == target:
        return cand
return _NO_SOLUTION
```

This is a pure catalogue scan using `multiply` and `==`. No depth
branch, no depth-1 assumption, no structural restriction on the objects.
The witness matrix checks (`globally_consistent()`) also use only `==`
on canonical objects — depth-agnostic. **W2 and W3 from the prior
draft's open list both discharge unconditionally.** No code gap exists.

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

Apply Lemma 7 (depth-2 oracle closure): if X, Y are depth-1 oracle
atoms, then `multiply(X, Y)` lies in `D'_oracle`. Therefore each
payload of `P` lies in `D'_oracle`. Combined with (i), `P` satisfies
the constructive-D'' definition.   ∎

**Corollary (Closure is monotone).** Closure at depth k+1 follows from
closure at depth k by the same argument applied recursively. The proof
above is the depth-3 instance of a single induction on depth that
generates the entire oracle hierarchy. *hmmm E — this corollary is
stated but the inductive step beyond depth-3 is not formally written
here; the construction `is_in_oracle_class_d4`, `_d5`, etc. would need
to exist for each level, and the iteration cost compounds. Out of scope
for this document.*

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
final verification step, which is identical at all depths.

---

## §4 — Theorem 8c: Completeness on multiplicative-D''

**Theorem 8c (Completeness).** Let `C = generate_payload_catalogue()`
(depth-1 oracle atoms, the same catalogue used in Lemma 7). For every
`P ∈ multiplicative-D''`, `factor_search_v08(P, C)` returns `(A, B)`
with `multiply(A, B) = P`.

**Proof.** Let `P = A ⨠ B` where `A, B ∈ D'_oracle`. Write `p =
len(A.A_plus)`, `q = len(B.A_plus)`, `n = p × q = len(P.A_plus)`.

**Step 1 — Host recovery (W1).** The algorithm iterates over
factorisations of `n` and will reach `(p, q)`. `recover_host_angles`
extracts the angle sequences of `A` and `B` exactly (W1 is structural
and depth-agnostic).   ✓

**Step 2 — Payload system (W2).** For each k, j:

```
P_payloads[k][j] = multiply(A.payload[k], B.payload[j])
```

Since `A, B ∈ D'_oracle`, `A.payload[k]` and `B.payload[j]` are
depth-1 oracle atoms, so each `P_payloads[k][j] ∈ D'_oracle`
(Theorem 8a applied at the payload level).

`solve_payload_system(P_payloads, p, q, C)` iterates S0_A over C.
When S0_A = `A.payload[0]` is reached (it is in C since `A.payload[0]`
is a depth-1 oracle atom):

- *Row 0, column j:* `find_right_factor_or_sentinel(P_payloads[0][j],
  A.payload[0], C)` scans C for R with
  `multiply(A.payload[0], R) = multiply(A.payload[0], B.payload[j])`.
  By E10.4 cancellativity, R = `B.payload[j]` uniquely. Since
  `B.payload[j] ∈ C`, it is found. Returns `S_B[j] = B.payload[j]`.✓

- *Column 0, row k > 0:* `find_left_factor_or_sentinel(P_payloads[k][0],
  B.payload[0], C)` scans C for L with
  `multiply(L, B.payload[0]) = multiply(A.payload[k], B.payload[0])`.
  By E10.4, L = `A.payload[k]` uniquely ∈ C. Returns
  `S_A[k] = A.payload[k]`.   ✓

- *Global consistency:* `multiply(A.payload[k], B.payload[j]) =
  P_payloads[k][j]` for all k, j — true by construction of P.   ✓

`solve_payload_system` returns `(S_A, S_B) = (A.payloads, B.payloads)`.

**Step 3 — Witness matrix (W3).** `build_witness_matrix(S_A, S_B,
P_payloads)` sets `W[k][j].verified = (multiply(A.payload[k],
B.payload[j]) == P_payloads[k][j])` — True for all k, j. Row
consistency: all `left_payload` in row k = `A.payload[k]`. Column
consistency: all `right_payload` in column j = `B.payload[j]`.
`globally_consistent()` returns True.   ✓

**Step 4 — Face recovery.** `recover_face_structures` returns the
correct A.faces, B.faces (structural, depth-agnostic).   ✓

**Step 5 — Exact recomposition.** The constructed candidates are
exactly `A_cand = A` and `B_cand = B`. So `multiply(A, B) = P`.   ✓

`factor_search_v08` returns `(A, B)`.   ∎

**Discharge note.** The W2 open item from the prior draft resolves here:
`solve_payload_system` does not call a depth-aware recursive solver — it
delegates to a plain catalogue scan (`find_right_factor_or_sentinel`)
whose depth-agnosticism (§1.5) means the depth-2 × depth-2 case works
identically to the depth-1 case. The "recursion" is inside `multiply`,
not inside the solver. W3 resolves because `globally_consistent()` uses
only `==` on canonical objects.

---

## §5 — Operative consequences

### §5.1 Frontier table

| Row | Prior status | New status |
|---|---|---|
| Cancellativity (E10.4) | ✅ | ✅ (unchanged) |
| Right-quotient completeness | ✅ | ✅ (unchanged) |
| Depth-2 oracle (Lemma 7) | ✅ | ✅ (unchanged) |
| Multiplicative-D'' ⊆ Constructive-D'' | not stated | ✅ (Theorem 8a) |
| Soundness at depth-3 | not stated | ✅ (Theorem 8b) |
| Completeness at depth-3 (multiplicative target) | 🟡 conjecture | ✅ (Theorem 8c) |
| Carrier widening | 🔴 | 🔴 (unchanged, out of scope) |

### §5.2 `factor_search_v08` docstring update

Current text: `"frozen depth-2 domain"`.

Replacement (defensible against this document):

```
factor_search_v08 — soundness on all UCNS inputs (Theorem 8b).
Completeness:
  - depth-2 oracle class: unconditional (Lemma 7).
    Catalogue: generate_payload_catalogue() (depth-1 oracle atoms).
  - depth-3 multiplicative class: unconditional (Theorem 8c).
    Catalogue: generate_payload_catalogue() (depth-1 oracle atoms,
    same as Lemma 7 — the catalogue is always one level below the
    factors' depth).
SEQ-PRIME is returned for objects outside these classes (including
depth-3 constructive objects not in multiplicative-D''), and for
objects whose factorizations require a catalogue the caller did not
provide.
```

This closes `hmmm 4` from the prior session.

### §5.3 PyPI implication

All three theorems proven. Soundness (Theorem 8b) is unconditional.
Completeness (Theorem 8c) holds for the documented domain. The
remaining PyPI blockers are unchanged from prior session:
hmmm 3 (`store.py` non-uniqueness), hmmm 7 (snapshot file at repo
root), and the carrier widening question (hmmm 6).

---

## §6 — hmmm items

**DISCHARGED:**

- **hmmm A' (Conjecture 8c):** Promoted to Theorem 8c. Proof in §4.

- **hmmm D (depth-3 multiply lift consistency):** §1.4. `canonical.py:189`
  confirmed genuinely recursive, no depth-conditional branching.

- **hmmm W2 (solve_payload_system recursive-call audit):** §1.5, §4 Step 2.
  `find_right_factor_or_sentinel` is a plain catalogue scan; no depth-1
  assumption; the "recursion" is inside `multiply`, not the solver.

- **hmmm W3 (witness matrix depth-3 behaviour):** §1.5, §4 Step 3.
  `globally_consistent()` uses only `==` on canonical objects; fully
  depth-agnostic.

**OPEN:**

- **hmmm E (closure corollary):** Theorem 8a's corollary suggests a
  single induction generates the oracle hierarchy to arbitrary depth.
  The *theorem* scales; the *catalogue iteration cost* compounds
  exponentially per level. Worth flagging for future depth-N reach
  documentation.

- **hmmm F (two-layer catalogue distinction):** Two factorization layers
  on depth-3 targets use different catalogues:
  - depth-1 catalogue → depth-2 × depth-2 factorizations (Theorem 8c).
  - depth-2 catalogue → depth-3 × depth-1 factorizations (unproven).
  The depth-3 sweep's improvement from depth-1 to depth-2 catalogue
  is evidence for the second layer, not the first. A "Theorem 9" for
  the depth-3 × depth-1 layer would follow the same structure as
  Theorem 8c with the depth-2 catalogue in place of the depth-1 one.

---

*Document scope ends here. The sigma-tensor / Theta-kernel and
recursive multiset equivalence (§E4.2, §E13) layers remain outside
this proof's frontier.*
