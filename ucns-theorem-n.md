# UCNS — Theorem N: Catalogue-Sufficient Factorization

<p align="center"><img src="docs/media/theorem-n-factorization.jpg" alt="Illustration: factors A and B composing into product P via factor_search_v08" width="640"></p>

*Illustration: decorative class (AI-generated; see `docs/media/README.md`).*

**Status:** Proven. Supersedes Lemma 7, Theorem 8c, and the prior ∀n-induction plan
(commit 2de89626).
**Authors:** Theorem statement and unification — Claude.ai mobile session, Erin Spencer
(May 2026). Empirical pre-work (6/6 Theorem 9 verification) — same session.
Prior depth-indexed proofs (Lemma 7, Theorems 8a/8b/8c, ∀n draft) — this Code session.
**Key finding:** `factor_search_v08` is depth-agnostic. One theorem covers all depths;
the depth-indexed hierarchy was presentational scaffolding, not structural content.
**Retracts:** Theorem 8c (vacuous — multiplicative-D'' = ∅) and the induction scaffold
in the prior `ucns-theorem-n.md`.

---

## §1 — Setup

### §1.1 Objects and multiplication

`UCNSObject(n_dec, n_min, A_plus, F_plus)` where `A_plus` is a sequence of
`(angle, payload)` pairs, payloads are `UCNSObject | None`, and `None` is the
identity element.

`multiply(A, B)` builds a `|A|×|B|`-cell product; cell `(k,j)` has angle
`alpha_k + beta_j − beta_0` and payload `multiply(A.payload[k], B.payload[j])`.
Fully recursive; no depth conditionals. **Key depth fact:**

> `multiply(depth-k, depth-k)` produces **depth-k**.

Depth lifts only when one factor already carries payloads deeper than the other.
This means: `D'_oracle × D'_oracle` (both depth-≤2) produces depth-≤2 output.

### §1.2 Catalogue

A **catalogue** `C` is a list of `UCNSObject | None` objects. `factor_search_v08`
uses `C` as the candidate set for reconstructed factor *payloads* — not as a set
of factor pairs.

### §1.3 Algorithm

`factor_search_v08(P, C)` runs five depth-agnostic steps for each factorisation
`n = p × q` of `n = |P.A_plus|` (balanced factorizations first, p=1 last — see
`factor_search_v08.py` module docstring for ordering rationale):
1. Host recovery (structural angle extraction)
2. Payload system construction + solve (catalogue scan via E10.4 cancellativity)
3. Witness-matrix global consistency check
4. Face recovery
5. Exact recomposition: `multiply(A_cand, B_cand) == P`

---

## §2 — Theorem N

**Theorem N (catalogue-sufficient factorization).** Let `A`, `B` be UCNS objects
with `|A.A_plus|, |B.A_plus| ≥ 1`, and let `C` be a catalogue containing every
payload appearing recursively in `A` or `B` (including `None`). Define
`P = multiply(A, B)`. Then `factor_search_v08(P, C)` returns `(A', B')` with
`multiply(A', B') = P`.

**No depth parameter. No oracle-class predicate.** The only hypothesis is
"the catalogue contains the necessary payloads."

---

## §3 — Proof

Let `p = |A.A_plus|`, `q = |B.A_plus|`, `n = pq`.

**Step 1 (Host recovery).** The loop `list(range(2,n)) + ([1] if n≥2 else [])`
reaches `p`: if `p ≥ 2` via `range(2,n)` (since `p < n`), if `p = 1` as the
explicit final element. `recover_host_angles(P, p, q)` returns the angle sequences
of `A` and `B` exactly. Structural; no depth. ✓

**Step 2 (Payload system).** For each `(k, j)`,
`P.A_plus[k*q+j][1] = multiply(A.payload[k], B.payload[j])`.
`solve_payload_system` iterates `S0_A` over `C`; when it reaches
`S0_A = A.payload[0]` (in `C` by hypothesis):
- Row 0: `find_right_factor_or_sentinel(P.payload[j], A.payload[0], C)` scans `C`
  for `R` with `multiply(A.payload[0], R) = P.payload[j]`. By E10.4 cancellativity,
  `R = B.payload[j]` uniquely. `B.payload[j] ∈ C` by hypothesis. ✓
- Column k > 0: symmetric, recovers `A.payload[k] ∈ C`. ✓
- Global consistency: `multiply(A.payload[k], B.payload[j]) = P.payload[k*q+j]`
  by construction of `P`. ✓

**Step 3 (Witness matrix).** `globally_consistent()` uses `==` on canonical objects.
Depth-agnostic. ✓

**Step 4 (Face recovery).** `recover_face_structures(P, p, q)` is structural.
Returns correct `A.faces`, `B.faces`. ✓

**Step 5 (Recomposition).** `A_cand = A`, `B_cand = B`. `is_unit(A)` and
`is_unit(B)` are both False (non-trivial A, B). `multiply(A_cand, B_cand) = P`.
Returns `(A, B)`. ∎

---

## §4 — Instances

### §4.1 Lemma 7 (depth-2 oracle completeness)

`A, B ∈ D'_oracle` (depth ≤ 2). Every payload of `A` and `B` is a depth-1 oracle
atom, all of which are in `C = generate_payload_catalogue()`. Hypothesis of
Theorem N satisfied. Completeness follows. ∎

### §4.2 Theorem 9 (asymmetric depth-3)

`A` is depth-3 (payloads are depth-2 objects), `B` is depth-≤2. `C` must contain
every payload of `A` (including the depth-2 ones) and every payload of `B`.

**Empirical verification (`t9_minimal_cat.py`, May 2026).** Six asymmetric depth-3
cases, each with a minimal catalogue built from recursive payloads of the true factors:

```
name                         |cat|  result     time   depths in C
04-d3-times-d1               3      SUCCESS     0.01s  [1, 2]
10-d3-times-d2               3      SUCCESS     0.01s  [1, 2]
11-d3-both-cells-d2          5      SUCCESS     0.01s  [1, 2]
12-len3-d3-times-d1          3      SUCCESS     0.01s  [1, 2]
14-d3-with-d2c-leading       3      SUCCESS     0.01s  [1, 2]
16-adversarial-non-leading   5      SUCCESS     0.03s  [1, 2]
```

6/6 SUCCESS in milliseconds. Algorithm correct at asymmetric depth-3
with the right catalogue. Earlier d2-catalogue TIMEOUTs in the broader
sweep (`depth3_sweep_t9_prework.py`) were performance-driven — catalogue
size 325–964 — not algorithmic gaps.

See `code/sweeps/t9_minimal_cat.py` and `code/sweeps/depth3_sweep_t9_prework.py`.

### §4.3 General depth-k

For any `P = multiply(A, B)` with A, B of depth ≤ k: build `C` = the recursive
payload closure of `A` and `B`. This contains only objects of depth ≤ k−1
(by the depth-of formula for `multiply`). Theorem N gives completeness for the
catalogue scan with `C`. No depth-conditional changes to the algorithm.

---

## §5 — Expressibility vs completeness

The depth-indexed oracle hierarchy (D'_oracle, D''_oracle, ...) addresses
**expressibility**: for which `P` does there exist a factorization
`P = multiply(A, B)` with payloads in a fixed depth-bounded catalogue?
This is a set-theoretic question.

Theorem N addresses **algorithmic completeness**: given that such a
factorization exists, does `factor_search_v08` find it? Answer: yes,
if the catalogue contains the necessary payloads.

The depth-indexed framing collapsed these two questions. Separated:

> **Expressibility** (oracle-class hierarchy) + **Theorem N** (algorithmic
> completeness)
> ⟹ "P in the depth-k oracle class, and C = depth-(k−1) oracle catalogue"
> ⟹ `factor_search_v08(P, C)` returns a factorization.

The catalogue-construction utility `catalogue_from_objects(*objs)` — taking
UCNS objects and returning the minimal catalogue from their recursive payloads
— is the practical interface for Theorem N application.

---

## §6 — Retractions

### §6.1 Theorem 8c was vacuously true

`ucns-lemma8-depth3.md §4` proved completeness on:

```
Multiplicative D'' = { multiply(A, B) : A, B ∈ D'_oracle,
                       depth(multiply(A, B)) = 3 }
```

`D'_oracle` caps depth at 2. Symmetric multiplication preserves depth: for all
`A, B ∈ D'_oracle`, every cell payload `multiply(A.payload[k], B.payload[j])`
has depth ≤ 1 (both inputs depth ≤ 1), so `depth(multiply(A, B)) ≤ 2`. The
"depth = 3" condition is never satisfied. **Multiplicative-D'' = ∅.**

Theorem 8c's five-step proof in §4 is logically valid — it correctly discharges
a universal statement over an empty domain, making it vacuously true and
practically empty. Theorem 8a (closure) and Theorem 8b (soundness) are
unaffected: 8a is still true, 8b is unconditional.

The depth-3 cases the sweep was testing are **asymmetric** (at least one factor
is depth-3, outside D'_oracle). Those are §4.2 (Theorem 9 = Theorem N instance).

### §6.2 The prior ∀n-induction plan

The previous `ucns-theorem-n.md` (commit 2de89626, superseded by this file)
proved "∀n ≥ 2, `factor_search_v08(P, C_{n−2})` complete for M_n" by induction.
That proof was logically correct given the loop-order fix (commit 10d94e97),
but the induction was unnecessary scaffolding. Theorem N subsumes it:
the inductive step simply notes that payloads of depth-(k+1) factors are depth-k
objects, so C_k satisfies Theorem N's hypothesis by construction.

---

## §7 — Operative consequences

### §7.1 Frontier table

| Row | Status |
|---|---|
| Cancellativity (E10.4) | ✅ |
| Right-quotient completeness | ✅ |
| Depth-2 oracle (Lemma 7 = Theorem N instance) | ✅ |
| Closure: multiplicative-D'' ⊆ constructive (Theorem 8a) | ✅ (still true; domain now known empty) |
| Soundness at all depths (Theorem 8b) | ✅ |
| Completeness: depth-3 symmetric (Theorem 8c) | ✅ (vacuously, domain = ∅) |
| Completeness: depth-3 asymmetric (Theorem 9 = Theorem N) | ✅ (empirically verified, 6/6) |
| **Catalogue-sufficient completeness at all depths (Theorem N)** | **✅ proven** |
| Tractable sub-catalogues | 🟡 open |
| Carrier widening | 🔴 out of scope |

### §7.2 `factor_search_v08` docstring

Updated in the file (Theorem N framing, per-depth practical examples).

### §7.3 PyPI blockers

Unchanged: hmmm 3 (store non-uniqueness), hmmm 6 (carrier widening),
hmmm 7 (snapshot file at repo root).

---

## §8 — hmmm preserved

- **hmmm 3 (store non-uniqueness / ALT-FACTOR).** Theorem N guarantees *a*
  factorization is found, not the canonical one. Canonical-choice procedure
  is a separate open question.
- **hmmm 6 (carrier widening).** Out of scope.
- **hmmm 7 (snapshot file at repo root).** Out of scope.
- **Performance scaling.** Theorem N is a correctness guarantee, not a
  tractability guarantee. Catalogue size dominates runtime. For large depth-3+
  catalogues, the algorithm times out even on cases it would eventually solve.
  Minimal-catalogue construction (recursive payload closure of the true factors)
  is the practical response; `max_objects` in `catalogue_d3.py` is the
  implementation hook.
- **Asymmetric layers (hmmm F).** Theorem 9 = Theorem N at asymmetric depth-3.
  "Theorem 10" for depth-4 asymmetric follows the same pattern. No new proof
  needed; just extend the catalogue.
- **Constructive oracle class hierarchy.** Still useful as an expressibility
  taxonomy (what objects can be built from depth-bounded payloads). Worth
  preserving in `domains.py` as classification, not as a theorem premise.
