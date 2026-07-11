# UCNS Base Geometry — the operation algebra of ⊠

**Status:** structure theorem landed (O6); statements below are proved at the
spec level from the implementation of `multiply` in `ucns/canonical.py` and
are machine-witnessed by the `contracts/` suite (one contract per obligation,
each with a mutation-catch check).  This document is the proof surface for
the base-geometry completion handoff (2026-07-10); the obligation ↔ witness
reconciliation lives in `audit/obligation_ledger.md` + `audit/reconcile.py`.

Formal non-transfer: nothing here confers Lean-checked status; `formal/`
remains `sorry`-backed.  Cross-repo non-continuity: the θ=0 origin's role in
any external glyph codebook is out of this repo's scope.

---

## 0. The carrier

Let **N** be the set of *nonempty, recursively host-normalized* `UCNSObject`
values, taken modulo the implementation's equality (`__eq__` compares
`n_min`, the `(angle, payload)` sequence, and `F_plus`; it deliberately
ignores `n_dec`, so the algebra's carrier is objects modulo carrier
declaration).  Every constructed `UCNSObject` is normalized (the constructor
calls `normalize()`, which gauge-shifts the first angle to 0 and recurses
into payloads), so N is exactly "the objects that exist," minus the empty
one.

**Why nonempty (boundary O1.b).**  At the time this theorem set landed, the
empty object was constructible and asymmetric under ⊠: as a *left* operand it
absorbed, while as a *right* operand `multiply(A, ∅)` raised `IndexError` —
so totality held on N × N and failed off it; the Lean findings independently
flag empty operands (P2/P3 in `formal/cancellativity-step1-findings.md`).
Since the v1.0 completion (codex-handoff/05) the boundary is enforced at
construction: `UCNSObject` rejects empty `A_plus`/`F_plus`, so the runtime
carrier IS the nonempty normalized object set and ⊠ is total on everything
constructible.  The base geometry is the algebra on N.

Notation: for `A ∈ N` write `p = len(A.A_plus)`, angles `α_0..α_{p-1}`
(with `α_0 = 0` after normalization), payloads `S^A_k ∈ N ∪ {None}`, faces
`f^A_k ∈ {0,1}`.  Write `⊗` for the payload-merge branch of `multiply`:
`None ⊗ y = y`, `x ⊗ None = x`, `x ⊗ y = multiply(x, y)` otherwise.

The definition of the product (from the code): `A ⊠ B` has `p·q` cells in
row-major order `(k, j)`, with

```text
angle_(k,j)   = (α_k + (β_j − β_0)) mod 4        (β_0 = 0 on N)
payload_(k,j) = S^A_k ⊗ S^B_j
face_(k,j)    = f^A_k XOR f^B_j
n_dec         = lcm(n_dec_A, n_dec_B);   n_min recomputed from the angles
```

followed by `normalize()`, which is a no-op on the angles because the first
cell's angle is `α_0 + 0 = 0`.

---

## 1. O1 — ⊠ is total and representation-independent  (`multiply_well_defined`)

**Theorem 1.1 (totality).**  For all `A, B ∈ N`, `A ⊠ B ∈ N`.

*Proof.*  The double loop always produces `p·q ≥ 1` cells, so the product is
nonempty.  Angles are exact `Fraction`s reduced mod 4.  The constructor's
divisibility check succeeds: every product angle is `α_k + β_j`, whose
circle-fraction denominator divides `lcm(n_min_A, n_min_B)`, which divides
`lcm(n_dec_A, n_dec_B) = n_dec_{A⊠B}` (each `n_min` divides its `n_dec` by
the operands' own validity).  Payloads are products of payloads (induction on
depth) or inherited.  ∎

**Theorem 1.2 (representation independence).**  The product depends only on
the equality classes of the operands: (i) a global gauge shift `δ` applied to
a raw angle list yields the same canonical object, hence the same product;
(ii) `n_dec` enters the product only through the product's own `n_dec`,
which equality ignores.

*Proof.*  (i) `normalize()` subtracts the first angle; `(α_k + δ) − (α_0 + δ)
= α_k − α_0`.  (ii) By inspection `n_dec` appears in `multiply` only in
`lcm(A.n_dec, B.n_dec)`; validity is preserved by the divisibility argument
of 1.1 for any admissible `n_dec` choices.  ∎

**Theorem 1.3 (grading).**  `len(A ⊠ B) = len(A) · len(B)`; equivalently the
degree valuation `r = log(len)` is additive.  *Proof:* the loop emits exactly
`p·q` cells; `normalize` never deletes cells.  ∎

Evidence: `contracts/test_multiply_canonical.py` (600 mixed-depth pairs, 300
representation pairs, boundary check).  Mutation: a canonicalizer that skips
the mod-4 reduction separates gauge-equivalent representations and is caught.
Rung: **[mutation-verified]**.

---

## 2. O2 — the θ=0 origin is a two-sided identity  (`multiply_identity`)

Let `e = UCNSObject(1, 1, [(0, None)], [0])`.

**Theorem 2.1.**  For all `A ∈ N`: `e ⊠ A = A` **and** `A ⊠ e = A`
(both sides proved separately; non-commutativity means neither implies the
other).

*Proof.*  Left: `p = 1`, `α_0 = 0`, `S^e_0 = None`, `f^e_0 = 0`.  Cell
`(0, j)` is `(0 + β_j, None ⊗ S^B_j, 0 XOR f^B_j) = (β_j, S^B_j, f^B_j)`;
row-major order preserves `j`; `n_min` recomputed identically.  Right:
`q = 1`, `β_0 = 0`; cell `(k, 0)` is `(α_k + 0, S^A_k ⊗ None, f^A_k XOR 0)`.
∎

The `None` sentinel is a definitional identity (`multiply` returns the other
operand), consistent with `e`.  The face-flipped unit `u₁ = [(0, None)],[1]`
is **not** an identity (it flips every face bit on either side) but is
self-inverse: `u₁ ⊠ u₁ = e`.

Evidence + mutation (a face-law mutant breaks two-sidedness and is caught):
`contracts/test_identity_two_sided.py`.  Rung: **proven two-sided** +
[mutation-verified].

---

## 3. O3 — ⊠ is associative  (`multiply_associativity`)

This was the handoff's "sleeper hard problem," conditioned on whether the θ
payload carries the resultant vector or only the collapsed angle.
**Resolution: the question dissolves at the algebra level.**  A UCNS object
carries its *entire* angle sequence — all `p·q` product cells — so no
circular mean is ever taken inside ⊠.  The payload-weighted circular mean
exists only in the `geometry_bridge` *projection* `(r, θ, z, w)`.  The
feared failure mode is real for a mean-collapsing operation (the mutation
check exhibits its non-associativity) — but ⊠ is not that operation.

**Theorem 3.1 (associativity).**  For all `A, B, C ∈ N`:
`(A ⊠ B) ⊠ C = A ⊠ (B ⊠ C)`.

*Proof.*  By strong induction on the maximum payload depth.

*Cells and order.*  `(A ⊠ B) ⊠ C` has cells indexed `((k, j), l)`; since
`A ⊠ B` is row-major in `(k, j)` and the outer product is row-major again,
the total order is lexicographic `(k, j, l)`.  `A ⊠ (B ⊠ C)` has cells
`(k, (j, l))` — also lexicographic `(k, j, l)`.  The two sides enumerate the
same index set in the same order.

*Angles.*  All operands and intermediate products are normalized (first
angle 0), so the gauge terms vanish and both sides carry
`(α_k + β_j + γ_l) mod 4` at `(k, j, l)`: exact rational addition is
associative.

*Faces.*  `f^A_k XOR f^B_j XOR f^C_l` both ways: XOR is associative.

*Payloads.*  Both sides carry `(S^A_k ⊗ S^B_j) ⊗ S^C_l` vs
`S^A_k ⊗ (S^B_j ⊗ S^C_l)`.  `⊗` is `multiply` extended by `None` as a
two-sided identity; if any argument is `None` both sides collapse to the
same expression by the identity laws, and if all three are objects their
depth is strictly smaller than the ambient product's, so the induction
hypothesis applies.

*Carrier.*  `lcm` is associative; `n_min` is recomputed from identical angle
lists; equality ignores `n_dec` regardless.  ∎

**Corollary 3.2.**  `(N, ⊠)` is a semigroup; with Theorem 2.1, a monoid.
The geometric composition `θ_A + θ_B mod 4π` is associative trivially, and
the homomorphism `ucns_a_to_g` transports 3.1 to the non-degenerate part of
the geometry.

Evidence: `contracts/test_associativity_triples.py` — 400 mixed-depth random
**triples** (the prior 500+-pair evidence was binary only and never tested
this) plus an exhaustive adversarial 6³ grid (identities, units, towers,
degenerate-θ).  Mutation: the mean-angle mutant is non-associative on a
concrete triple and is caught.  Rung: **proven** + [mutation-verified].

---

## 4. O4 — commutativity ruling  (`multiply_commutativity_ruling`)

**Theorem 4.1 (non-commutativity).**  ⊠ is not commutative.  Witness:
`B₁ = [(0,·,0), (1,·,0)]`, `B₂ = [(0,·,0), (2,·,0)]`:
`B₁ ⊠ B₂` has angle sequence `(0, 2, 1, 3)` while `B₂ ⊠ B₁` has
`(0, 1, 2, 3)`.  ∎

**Theorem 4.2 (the geometry is blind to the commutator).**  For all
`A, B ∈ N`: `ucns_a_to_g(A ⊠ B) = ucns_a_to_g(B ⊠ A)`.

*Proof.*  `r`: `log(pq)` both ways.  `θ`: the circular mean depends on the
*multiset* of top-level angles, and `{α_k + β_j} = {β_j + α_k}` as
multisets (degenerate cases coincide for the same reason).  `z`:
`Σ (f^A_k XOR f^B_j) mod 2` is multiset-invariant; equivalently the composed
rule `z_A·w_B + w_A·z_B mod 2` is symmetric in the operands.  `w`:
`pq mod 2` is symmetric.  ∎

**This corrects the handoff's expected shape.**  The guess was "commutes in
angle and size, not in chirality; the commutator lives in (z, w)."  In fact
the chirality composition is *symmetric* — the commutator lives in the
**sequence ordering**: row-major interleaving `(k, j)` vs `(j, k)`, and
payload order at depth.  ⊠ commutes *as geometry*, never in general *as
sequence*.

**Theorem 4.3 (center).**  `Z(N) = the unit towers`: the nested length-1
objects `[(0, S, f)]` with `S = None` or `S` itself a unit tower, any face
bits.  (The unit group `{e, u₁}` is the depth-1 layer; deeper towers are
central but not invertible.)

*Proof.*  (⊇)  Let `t = [(0, S, f)]` with `S` central-or-None.  For any `B`:
both `t ⊠ B` and `B ⊠ t` have cells `(β_j, S ⊗ S^B_j, f XOR f^B_j)` and
`(β_j, S^B_j ⊗ S, f^B_j XOR f)` in the same order `j`; the payloads agree
because `S` commutes with every object and `⊗`'s `None` cases are two-sided.
Induction on tower depth grounds at `S = None`.

(⊆)  Let `A` be central with `p ≥ 2`.  Test against `B_c = [(0,·,0),(c,·,0)]`
for `c ∈ {1, 2}`.  Cell 1 of `A ⊠ B_c` is `(α_0 + c) = c`; cell 1 of
`B_c ⊠ A` is `α_1`.  Centrality forces `α_1 = 1` and `α_1 = 2`
simultaneously — contradiction.  So `p = 1`, `A = [(0, S, f)]`.  For any
object `T`, testing against `[(0, T, 0)]` forces `S ⊗ T = T ⊗ S`; ranging
`T` over N (plus the `None` cases, which hold identically) makes `S` central
or `None`, and induction rebuilds the tower.  ∎

Evidence + mutation (a cell-sorting mutant erases the commutator and is
caught): `contracts/test_commutator.py`.  Rung: **proven ruling** +
[mutation-verified].

---

## 5. O5 — division theory  (`division_theory`)

Under non-commutativity division splits into left (`A ⊠ X = P`) and right
(`X ⊠ B = P`) problems.  Everything below is stated for the left problem;
the right statements are exact duals with "first block / columns" replaced
by "block-leading positions / rows" (and are implemented and tested as
such).

**Lemma 5.1 (forced host).**  If `A ⊠ X = P` then `q = len(P)/len(A)` and
the top level of `X` is forced: `ξ_j = angle_P(j)` and
`f^X_j = f_P(j) XOR f^A_0` for `j < q`.  Consequently `len(A) | len(P)` and
`r(X) = r(P) − r(A)` (division is **partial**: no quotient exists when the
degree valuation says so).

*Proof.*  Row `k = 0` of the product is `(0 + ξ_j, S^A_0 ⊗ S^X_j,
f^A_0 XOR f^X_j)`.  ∎

**Theorem 5.2 (solvability + multiplicity).**  `A ⊠ X = P` is solvable iff
(i) the length gate and host consistency of Lemma 5.1 hold across *all*
rows, and (ii) for every column `j` the payload system
`{S^A_k ⊗ y = payload_P(k·q + j) : k < p}` has a solution.  The solution
set is exactly `{host + (y_j)_{j<q} : y_j ∈ C_j}` where `C_j` is the
solution set of column `j`'s system; the sets `C_j` are finite, computed by
recursion on the target's payload depth, and the number of solutions is
`∏_j |C_j|`.

*Proof.*  Columns are independent because cell `(k, j)` constrains only
`S^X_j`.  Per-cell equations `S ⊗ y = t` resolve as: `S = None ⇒ y = t`
forced; `S ≠ None ⇒ y = None` iff `t = S`, plus every object solution of
`multiply(S, y) = t`, which by Lemma 5.1 (applied recursively) has forced
host and strictly shallower payload targets — the recursion terminates and
enumerates everything.  Finiteness follows by induction.  ∎

Implementation: `ucns/division_theory.py` (`left_quotients` /
`right_quotients`) — sound and complete; exhaustively cross-checked on a
closed 78-object universe (6,084 ordered pairs, zero misses, zero unsound
returns; full sweep re-runnable via `UCNS_EXHAUSTIVE=1`, CI runs a
deterministic stride sample of the same universe).  Solutions are monoid
elements: the identity appears once, as the canonical identity object,
never additionally as the `None` sentinel alias.

**Theorem 5.3 (flat-divisor cancellativity).**  If `A` is flat (depth 1,
all payloads `None`) then `A ⊠ X = A ⊠ Y ⇒ X = Y`, and dually
`X ⊠ B = Y ⊠ B ⇒ X = Y` for flat `B`.  *Proof:* with `S^A_k = None` every
payload cell is `S^X_j` itself, and angles/faces are recovered by exact
subtraction/XOR from any single row (column).  ∎
This explains why the v0.5.1 empirical cancellativity regression (11,016
pairs at depths 0–1) saw zero violations: depth ≤ 1 divisors are
cancellative.

**Theorem 5.5 (cancellativity dichotomy).**  A divisor `A` is
left-cancellative **iff at least one top-level payload of `A` is the unit**
(`S^A_{k₀} = None` for some `k₀`); dually for right divisors (some
`S^B_{j₀} = None`).  Flat divisors (5.3) are the all-unit special case.

*Proof.*  (⇐)  Row `k₀` of `A ⊠ X` carries the payload cells
`None ⊗ S^X_j = S^X_j` verbatim, so all of `X`'s payloads are forced;
angles and faces are forced from any row by exact subtraction/XOR.
(⇒)  If every `S^A_k ≠ None`, take `X = [(0, e, 0)]` and `Y = e`: for
every `k`, `S^A_k ⊗ e = S^A_k = S^A_k ⊗ None`, so `A ⊠ X = A = A ⊠ Y`
with `X ≠ Y` — the unit-payload/`None`-payload ambiguity.  ∎

The dichotomy does not contradict the `AlignedComplete` conjecture: the
witness pair `([(0, e, 0)], e)` has unequal depths, which the
cross-operand common-depth conjunct excludes.  `AlignedComplete`
conjectures cancellation on the depth-aligned all-payloads-present
subdomain; the dichotomy characterizes it over the whole monoid.

**Theorem 5.4 (non-uniqueness is structural).**  Cancellativity fails from
depth ≥ 2 divisors on: with towers `T₂ = [(0, e, 0)]`, `T₃ = [(0, T₂, 0)]`:
`T₃ ⊠ T₂ = T₃ ⊠ T₃ = T₃` yet `T₂ ≠ T₃` — and the same witness kills the
right side.  More precisely, `T_d ⊠ X = T_d` has exactly `d` solutions
`{e, T₂, …, T_d}` (multiplicity theorem verified by the enumerator).
`ALT-FACTOR` multiplicity in sweeps and `store.left_factors` non-uniqueness
are therefore **properties of the problem** — the correct posture is to
canonize the multivalued answer (return the solution set), not to "fix" it.
A canonical-choice procedure among solutions remains open (as in
`ucns-theorem-n.md` hmmm 3).

**Scope correction (2026-07-10) to the v0.6 Left-Quotient Completeness
theorem.**  The claim "`left_quotient(P, A, catalogue=None)` returns an
object equivalent to B whenever `A ⊠ B ≡ P`" is **false as stated**.
Counterexample (permanent regression in
`contracts/test_quotient_solvability.py::test_v06_scope_correction`):

```python
T = UCNSObject(1, 1, [(0, None)], [0])
A = UCNSObject(4, 1, [(0, T), (2, None)], [0, 0])
B = UCNSObject(1, 1, [(0, T)], [0])
left_quotient(multiply(A, B), A)  # None — misses B
```

Mechanism: the proof depends on E10.4 cancellativity, which fails at depth
(Theorem 5.4); the greedy row-0 payload recovery resolves the ambiguous
per-cell equation `T ⊗ y = T` to the unit and then global verification
fails.  The greedy primitive remains **sound** (phase-3 verification) and
complete on flat divisors (Theorem 5.3); completeness in general is
recovered by the `division_theory` enumerators.  The dual `right_quotient`
is additionally incomplete for a second reason: it recovers payloads with
the *left*-quotient helper where the dual equation needs a right quotient —
observed as misses on random solvable instances even where the left
primitive succeeds.  Both corrections are recorded in
`docs/claims-ledger.md` and banners on the two v0.6 proof documents.

Rung: **solvability theorem landed** + [mutation-verified] (a
verification-skipping mutant returns an unsound candidate and is caught).

---

## 6. O6 — structure theorem  (`structure_naming`)

**Theorem 6.1.**  `(N, ⊠, e)` is a **non-commutative, non-cancellative
monoid, graded by length over (ℕ≥1, ×)** — equivalently, the degree
valuation `r = log(len)` is an additive grading — with:

- unit group `U(N) = {e, u₁} ≅ ℤ/2` (length multiplicativity forces
  length 1; a payload can never `⊗`-cancel, forcing payload `None`; face
  self-inverse under XOR);
- center `Z(N)` = the unit towers (Theorem 4.3), a commutative submonoid
  strictly containing `U(N)`, rich in non-identity idempotents
  (`T_d ⊠ T_d = T_d` for all-zero-face towers);
- partial, multivalued division with forced hosts and finite fibers
  (Theorems 5.1–5.4); a divisor cancels iff one of its top-level payloads
  is the unit (Theorem 5.5 dichotomy — flat divisors are the special
  case), with the depth-aligned `AlignedComplete` conditional statement
  remaining a `formal/` frontier obligation.

**What it is not.**  Not a group and not embeddable in one (non-cancellative);
not a groupoid/category-with-inverses (the multivalued quotients are fibers
of monoid multiplication, not inverse morphisms); not a ring or semiring
(no primitive addition — O7; the derived ⊕ distributes on one side only).

**Earned name.**  *A length-graded monoid* — specifically: a noncommutative
monoid with ℤ/2 unit group, tower center, additive degree valuation, and
absorption-driven failure of cancellation.  Per the handoff's own rule, the
structure is called this and nothing more; "number system" remains
aspirational until an addition with two-sided distributivity is exhibited
or the payload ontology is enriched.

Evidence + mutation (a deduplicating product breaks the grading and is
caught): `contracts/test_structure_axioms.py`.  Rung: **structure theorem**
(O1–O5 as lemmas) + [mutation-verified].

---

## 7. O7 — the addition boundary  (`addition_boundary`)

**Ruling: ⊠ is the sole primitive; there is no primitive addition.**

1. *Radial growth is emergent, confirmed:* `r(A ⊠ B) = r(A) + r(B)`
   (Theorem 1.3).  The degree already behaves additively under the one
   primitive; no second operation is required to generate growth.
2. *The natural derived candidate does not qualify.*  Top-level
   concatenation `A ⊕ B` (the only sequence-level addition available
   without enriching the ontology) is associative, non-commutative, and
   **right-distributive** over ⊠ — `(B ⊕ C) ⊠ A = (B ⊠ A) ⊕ (C ⊠ A)`,
   because right multiplication preserves block order — but **left
   distributivity fails**: `A ⊠ (B ⊕ C)` interleaves the rows of `A ⊠ B`
   and `A ⊠ C` instead of concatenating them (witness in
   `contracts/test_addition_boundary.py`).  One-sided distributivity earns
   at most a right-near-semiring reading and no primitive status.
3. *Scope consequence:* the base-geometry operation set closes as
   `{⊠, left/right division (partial, multivalued), e, U(N) ≅ ℤ/2}`.
   Enriching the payload to make a two-sided addition exist is future
   ontology work, not v1.0 base geometry.

Evidence + mutation (a gauge-drifting concatenation breaks right
distributivity and is caught): `contracts/test_addition_boundary.py`.
Rung: **ruled**.

---

## 8. Rung summary and open items

| id | law | arrival | landed at |
|---|---|---|---|
| O1 `multiply_well_defined` | total + representation-independent | `[test-backed]` | `[mutation-verified]`, carrier boundary pinned (nonempty) |
| O2 `multiply_identity` | θ=0 origin two-sided | `hmmm` | proven two-sided + `[mutation-verified]` |
| O3 `multiply_associativity` | (a⊠b)⊠c = a⊠(b⊠c) | `hmmm` (never tested) | **proven** + `[mutation-verified]` |
| O4 `multiply_commutativity_ruling` | non-commutative; subclass | partial | proven ruling (commutator = ordering, geometry commutes, center = towers) + `[mutation-verified]` |
| O5 `division_theory` | quotient existence + multiplicity | `hmmm` | solvability + multiplicity theorems, complete enumerators, v0.6 scope correction + `[mutation-verified]` |
| O6 `structure_naming` | name the object | pending | **length-graded non-cancellative monoid** (theorem, O1–O5 as lemmas) |
| O7 `addition_boundary` | primitive addition? | `hmmm` | ruled: none; ⊕ derived, right-distributive only |

Open (`hmmm`, preserved):

- `AlignedComplete`-domain cancellativity: empirical CE-free at d ≤ 3,
  Lean statement ratified, proof undischarged (`formal/`).
- Canonical-choice procedure among multiple quotients (structural
  multiplicity now canonized; choosing a representative remains open).
- The exact canonical counting rule for `# ratios:` bookends is not
  vendored in this repo; new files carry best-effort counts (rule
  documented in `audit/obligation_ledger.md`).
- Retrofitting `ratios` bookends onto pre-existing engine files is left to
  a dedicated pass.
- θ=0 origin ↔ external 157-glyph codebook linkage: cross-repo, out of
  scope here.
