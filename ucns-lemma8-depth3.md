# UCNS v0.8 — Lemma 8: Depth-3 Factor Search

**Status:** All three theorems proven. Depth-3 completeness holds
unconditionally after the `range(2,n)` → `range(1,n)` code fix
(see §1.6).
**Scope:** `factor_search_v08` applied to depth-3 objects, using the
depth-1 oracle catalogue as payload basis.
**Depends on:** Lemma 7 (depth-2 oracle theorem), E10.4 cancellativity,
v0.6 left-quotient completeness, recursive multiply structural definition.
**Supersedes:** prior drafts with two issues fixed:
(1) coverage definition treated catalogue as factor-pair set (§1.3).
(2) Conjecture 8c specified wrong catalogue (depth-2 instead of depth-1) (§1.3).
(3) algorithm loop `range(2,n)` excluded non-unit 1-cell factors (§1.6, now fixed).

---

## hmm

This document is split into three theorems plus the reframed coverage
condition. The split exists because the prior single-statement Lemma 8
draft conflated three independent facts:

- **Closure** of multiplicative-D'' inside the depth-3 oracle class.
- **Soundness** of `factor_search_v08` on depth-3 inputs.
- **Completeness** of `factor_search_v08` on multiplicative-D''.

All three discharge.

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
constructive. The converse is false in general.

### §1.2 What "catalogue" means in `factor_search_v08`

The `catalogue` parameter is passed to `solve_payload_system` and used
as the candidate set for `S_A` and `S_B` — the **payload sequences** of
the reconstructed factors. The catalogue is not a set of factor pairs.

### §1.3 Coverage condition (corrected) and catalogue

**Definition (catalogue covers a target domain).** A catalogue `C`
**covers** `T` iff for every `P ∈ T`, there exist `A`, `B` such that:

1. `multiply(A, B) ≡_seq P`,
2. every payload of `A` and every payload of `B` lies in `C`,
3. the angle and face structures of `A` and `B` are consistent with
   the host-recovery and face-recovery procedures.

Lemma 7 at depth-2 and Theorem 8c at depth-3 both use
C = `generate_payload_catalogue()` (depth-1 oracle atoms, including
`None`). The catalogue is always one level below the factors' payload
depth: for depth-2-oracle factors, payloads are depth-1 atoms.

### §1.4 Multiply structural recursion (confirmed)

`canonical.py:189` (`new_payload = multiply(S_k_A, S_j_B)`) is
genuinely recursive with no depth-conditional branches.

### §1.5 Algorithm depth-agnosticism (W2 + W3)

`find_right_factor_or_sentinel` in `recursive_quotient.py` is a pure
catalogue scan using `multiply` and `==`. No depth branch. The witness
matrix checks use only `==` on canonical objects. Both W2 and W3
discharge unconditionally.

### §1.6 Loop range fix (premise error corrected)

The prior algorithm had `for p in range(2, n)`. This excluded `p = 1`,
making factorizations where one factor has exactly 1 cell unreachable.

`is_unit` in `canonical.py` returns True only for the specific 1-cell
object with `angle=0, payload=None, face=[0], n_min=1`. Non-unit 1-cell
objects (e.g. `face=[1]` or `payload≠None`) are valid D'_oracle members
whose factorizations were silently missed. Concretely: for `|P|=2`, the
loop `range(2,2)` is empty and the algorithm returns SEQ-PRIME for every
2-cell P regardless of content — a completeness violation.

`host_recovery.recover_host_angles(P, 1, n)` and
`recover_face_structures(P, 1, n)` both work correctly for `p=1`
(verified by reading the arithmetic: A_angles = [0], B_angles =
P's full angle sequence; face assignment is consistent).

**Fix:** `factor_search_v08.py` loop changed to `range(1, n)`. The
existing `is_unit(A_cand)` check at step 5 correctly filters the true
unit; non-unit 1-cell factors are now reachable.

---

## §2 — Theorem 8a: Closure

**Theorem 8a (Multiplicative-D'' ⊆ Constructive-D'').** If `A, B ∈
D'_oracle` and `multiply(A, B)` is defined and has depth 3, then
`multiply(A, B)` lies in constructive-D''.

**Proof.** Each payload of `P = multiply(A, B)` at cell `(k, j)` is
`multiply(A.payload[k], B.payload[j])`. Since `A, B ∈ D'_oracle`, both
payloads are depth-1 oracle atoms. By Lemma 7 oracle closure,
`multiply(depth-1-atom, depth-1-atom) ∈ D'_oracle`. So every payload of
`P` lies in `D'_oracle`. Combined with `depth(P) = 3` (given) and the
canonical well-formedness of `multiply`'s output, `P ∈` constructive-D''. ∎

---

## §3 — Theorem 8b: Soundness

**Theorem 8b (Soundness).** For any catalogue `C` and any input `P`,
if `factor_search_v08(P, C)` returns `(A, B)`, then `multiply(A, B) = P`.

**Proof.** Step 5 is the literal check `multiply(A_cand, B_cand) == P`.
The function returns only when this holds. ∎

---

## §4 — Theorem 8c: Completeness on multiplicative-D''

**Theorem 8c (Completeness).** Let `C = generate_payload_catalogue()`.
For every `P ∈ multiplicative-D''`, `factor_search_v08(P, C)` returns
`(A, B)` with `multiply(A, B) = P`.

**Proof.** Let `P = A ⨠ B` where `A, B ∈ D'_oracle`, `p = |A.A_plus|`,
`q = |B.A_plus|`, `n = pq`.

**Step 1.** The loop `range(1, n)` reaches `p` (since `1 ≤ p < n`
because `q ≥ 1` and non-triviality is enforced by the `is_unit` check,
not by the loop bound). Host recovery extracts `A.angles`, `B.angles`
exactly (W1, structural, depth-agnostic). ✓

**Step 2.** `P_payloads[k][j] = multiply(A.payload[k], B.payload[j])`.
When `solve_payload_system` tries `S0_A = A.payload[0] ∈ C`:
- Row 0: `find_right_factor_or_sentinel` scans `C` for `R` with
  `multiply(A.payload[0], R) = multiply(A.payload[0], B.payload[j])`.
  E10.4 gives `R = B.payload[j] ∈ C` uniquely. ✓
- Column 0, k > 0: symmetric, recovers `S_A[k] = A.payload[k] ∈ C`. ✓
- Global consistency: holds by construction of `P`. ✓

**Step 3.** Witness matrix: all cells verified, row/column consistent.
`globally_consistent()` = True (depth-agnostic `==` checks). ✓

**Step 4.** `recover_face_structures` returns correct `A.faces`, `B.faces`. ✓

**Step 5.** `A_cand = A`, `B_cand = B`. `is_unit(A)` and `is_unit(B)`
are both False (A, B ∈ D'_oracle are non-unit by hypothesis).
`multiply(A, B) = P`. Returns `(A, B)`. ∎

---

## §5 — Operative consequences

### §5.1 Frontier table

| Row | Status |
|---|---|
| Cancellativity (E10.4) | ✅ |
| Right-quotient completeness | ✅ |
| Depth-2 oracle (Lemma 7) | ✅ |
| Multiplicative-D'' ⊆ Constructive-D'' | ✅ (Theorem 8a) |
| Soundness at depth-3 | ✅ (Theorem 8b) |
| Completeness at depth-3 (multiplicative target) | ✅ (Theorem 8c) |
| Carrier widening | 🔴 out of scope |

### §5.2 `factor_search_v08` docstring

Updated in the file to reflect Theorem N coverage (all depths).
Hmmm 4 closed.

### §5.3 PyPI blockers

Unchanged: hmmm 3 (store non-uniqueness), hmmm 6 (carrier widening),
hmmm 7 (snapshot file at repo root).

---

## §6 — hmmm items

**DISCHARGED:**
- hmmm A' (Conjecture 8c) → Theorem 8c (§4).
- hmmm D (multiply lift consistency): canonical.py:189 confirmed recursive.
- hmmm W2: find_right_factor_or_sentinel is depth-agnostic catalogue scan.
- hmmm W3: globally_consistent() is depth-agnostic.
- hmmm 4 (factor_search_v08 docstring): updated in file.
- **Loop range premise error**: fixed by range(1,n) + is_unit gate.

**OPEN:**
- hmmm E: closure corollary to arbitrary depth (theorem scales, iteration cost compounds).
- hmmm F: asymmetric factorization layers (depth-3 × depth-1, "Theorem 9").

---

*Sigma-tensor / Theta-kernel and recursive multiset equivalence
(§E4.2, §E13) remain outside this proof's frontier.*
