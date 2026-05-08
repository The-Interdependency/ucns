# UCNS — Depth-3 Empirical Sweep Report

**Date:** 2026-05-07  
**Target:** `factor_search_v08` past the v0.8 frozen domain D'.  
**Scope:** 16 hand-built cases, depths 2–4, host lengths 2–9, three catalogue levels.  
**Status:** maps the failure boundary; does not establish a theorem.

---

## TL;DR

- **Algorithm boundary not yet exposed.** Every depth-3 (and depth-4) case in the sweep *succeeded* when the catalogue contained the necessary atoms. The witness-matrix architecture appears to extend to depth ≥ 3 without modification.
- **The boundary is catalogue coverage.** Default catalogue (depth-1 oracle atoms only) cannot reach depth ≥ 3 — it has nothing for `solve_payload_system` to enumerate as a depth-2 leading payload. This is predictable, not architectural.
- **One sharper finding (case 16):** "leading payloads + visible-in-P payloads" is *not* a sufficient catalogue for depth-3. A factor's non-leading payloads can be invisible in P (composed away into products), but the solver still needs them as catalogue entries to recover via `find_left_factor`. **The covering catalogue must include every payload appearing anywhere in A and B, not just the visible ones.**
- **One non-uniqueness sighting (case 06):** D2_c × S2 admits multiple valid (A, B) factorizations. Algorithm returns *a* valid factorization (Phase 5 verified), not necessarily the originating one. This is consistent with the v0.6/v0.8 theorems, which claim existence, not uniqueness.

---

## What this means for the frontier

The depth-3 frontier reformulates from:

> 🔴 *factor_search_v08 may be incomplete past D'*

to:

> 🟡 *factor_search_v08 is empirically complete past D' when given a covering catalogue. The open work is defining a frozen depth-3 domain D'' and constructing a bounded catalogue that covers it.*

This is a **theoretical / catalogue-construction problem**, not an algorithm problem. The architecture continues to function correctly through at least depth-4 (per package convention). The witness-matrix global-consistency check accepts no false positives; failures manifest as `SEQ-PRIME` returns when the catalogue is insufficient (all-soundness, no-completeness).

---

## Sweep table

Convention: `depth_of` per `ucns_recursive.domains` (None=0, flat=1, d-leading=1+d). Frozen domain D' caps `depth ≤ 2`. Each result is paired with elapsed wallclock seconds. SUCCESS = recovered the original A,B. ALT-FACTOR = recovered some (A',B') with `multiply(A',B')==P` but `(A',B') != (A,B)` — non-uniqueness on the input. FALSE-NEGATIVE = `SEQ-PRIME` returned when a non-trivial factorization exists.

```
#   name                       P_d  |P+|  default              narrow-tailored      broad-tailored
01  trivial-unit-right          3    2    FALSE-NEGATIVE 0.0s  FALSE-NEGATIVE 0.0s  FALSE-NEGATIVE 0.0s
02  symmetric-d2xd2             2    4    SUCCESS        0.1s  SUCCESS        0.1s  SUCCESS        0.1s
03  d2-times-d1                 2    4    SUCCESS        0.1s  SUCCESS        0.1s  SUCCESS        0.1s
04  d3-times-d1                 3    4    FALSE-NEGATIVE 0.3s  SUCCESS        0.5s  SUCCESS        0.5s
05  d3-times-d3                 3    4    FALSE-NEGATIVE 0.3s  SUCCESS        0.8s  SUCCESS        0.8s
06  d2c-times-s2                2    4    ALT-FACTOR     0.0s  ALT-FACTOR     0.0s  ALT-FACTOR     0.0s
07  len3-host-d2-times-d1       2    6    SUCCESS        0.5s  SUCCESS        0.4s  SUCCESS        0.4s
08  d2-times-len3-flat          2    6    SUCCESS        0.1s  SUCCESS        0.1s  SUCCESS        0.1s
09  d3-distinct-leadings        3    4    FALSE-NEGATIVE 0.3s  SUCCESS        0.9s  SUCCESS        0.9s
10  d3-times-d2                 3    4    FALSE-NEGATIVE 0.3s  SUCCESS        0.6s  SUCCESS        0.6s
11  d3-both-cells-d2            3    4    FALSE-NEGATIVE 0.3s  SUCCESS        0.5s  SUCCESS        0.5s
12  len3-d3-times-d1            3    6    FALSE-NEGATIVE 0.7s  SUCCESS        1.0s  SUCCESS        1.0s
13  d3xlen3-times-d3xlen3       3    9    FALSE-NEGATIVE 0.3s  SUCCESS        0.7s  SUCCESS        0.6s
14  d3-with-d2c-leading         3    4    FALSE-NEGATIVE 0.3s  SUCCESS        0.6s  SUCCESS        0.6s
15  d4-times-d1                 4    4    FALSE-NEGATIVE 0.3s  SUCCESS        0.9s  SUCCESS        1.0s
16  adversarial-non-leading     3    4    FALSE-NEGATIVE 0.3s  FALSE-NEGATIVE 1.3s  SUCCESS        0.9s
```

**Default:** 11 false-negative, 4 success, 1 alt-factor.  
**Narrow-tailored:** 2 false-negative, 13 success, 1 alt-factor.  
**Broad-tailored:** 1 false-negative, 14 success, 1 alt-factor.

---

## Catalogue levels — what each contains

- **default** = `generate_payload_catalogue()`: 51 entries, all depth-1 oracle atoms in D'. This is what `factor_search_v08` uses when called with `catalogue=None`.
- **narrow-tailored** = default + `A.A_plus[0][1]` + `B.A_plus[0][1]` + every payload appearing in `P.A_plus`. Roughly: “things visible in the inputs/output.”
- **broad-tailored** = narrow + every payload appearing anywhere recursively in A or B. Strictly: “all atoms used in the construction.”

---

## Per-finding analysis

### Finding 1 — algorithm functions through depth 4

Case 15 (depth-4 A, S2 B) succeeded with the broad-tailored catalogue. The witness-matrix mechanism does not break at depth 4. Within the test set, no architectural ceiling was found — every failure had a catalogue explanation.

### Finding 2 — narrow-tailored is not enough (case 16)

Case 16 was constructed deliberately:
- `A = [(0, D2_a), (1, D2_b)]`, `B = [(0, S2), (1, S2b)]`.
- `A`'s second-cell payload is `D2_b`. `D2_b` *never appears in P alone* — `P_payloads` are all of the form `(D2_b ⊠ S2)`, `(D2_b ⊠ S2b)`, `(D2_a ⊠ S2)`, `(D2_a ⊠ S2b)`.
- Narrow catalogue has `D2_a` (leading) and the four product payloads, but **not** `D2_b`.
- `solve_payload_system` enumerates `S0_A` candidates, picks `D2_a` correctly, derives `S_B[j]` from row 0, then needs `find_left_factor(P_payloads[1][0], S_B[0], catalogue)` to recover `S_A[1] = D2_b`. With `D2_b` absent from catalogue, the `find_left_factor` scan falls through to None.

Broad catalogue includes `D2_b` (gathered recursively) → succeeds.

**This refines the depth-3 completeness condition.** A “covering” catalogue is one containing every payload appearing anywhere in the unknown factors, including non-leading and non-visible-in-P atoms. That's a stronger requirement than the depth-2 case suggested.

### Finding 3 — non-uniqueness at depth-2 (case 06)

Case 06: `D2_c = [(0, S2), (1, S2)]` (both cells point to the same `S2`), `B = S2`. P = D2_c ⊠ S2 has all four outermost payloads equal to `S2`. The product is “structurally degenerate” and admits multiple valid factorizations. The algorithm finds one of them; verifies via `multiply(A_rec, B_rec) == P`; returns it. The recovered (A_rec, B_rec) is not equal to the original (D2_c, S2) but is genuinely a valid factorization.

This is **not unsoundness.** The v0.6 and v0.8 completeness theorems claim *existence* of a factorization when P is seq-composite, not *uniqueness*. Cancellativity gives uniqueness *given* one of the factors, but with neither factor known, multiple solutions are admissible.

Worth noting: this means `factor_search_v08(P)` should be understood as returning *a* witness of seq-compositeness, not *the* canonical factorization.

### Finding 4 — performance scales well

All cases completed in under 1.3s, including case 16’s narrow-tailored attempt (which exhausted the catalogue without finding a solution, in 1.25s). The witness-matrix architecture is fast on inputs of this size; the bottleneck for production-scale depth-3 work will be **catalogue construction**, not search.

For reference: `build_catalogue_d2_oracle(payload_basis=[None, S2, D1a])` produced 274 depth-2 atoms in 0.87s. A full depth-2 catalogue with the default depth-1 basis (51 atoms) would be much larger; the existing `build_catalogue_d2_oracle` docstring warns about `|basis|^length` enumeration cost.

### Finding 5 — case 01 is correctly SEQ-PRIME

Case 01: `A` = depth-3 length-2, `B` = unit. `P = A ⊠ B = A` (since unit is the multiplicative identity). `factor_search_v08`'s loop is `for p in range(2, n)` where `n = |P+| = 2` — empty range, immediately returns `SEQ_PRIME`. This is the algorithm's correct behavior: there are no non-trivial host factorizations of a length-2 object (only 1×2 and 2×1, both involving a unit factor, which the search excludes by `is_unit(A_cand) or is_unit(B_cand): continue`). Not a false negative — labelled as one in the table only because the test harness can’t distinguish “correctly SEQ-PRIME” from “missed factorization” without a uniqueness oracle.

---

## What the sweep does *not* settle

1. **Algorithm completeness past D' is not proven** — only empirically witnessed on 14 hand-built cases. A real completeness claim at depth-3 needs a frozen domain D'' definition + a proof analogous to `ucns-v06-completeness-proof.md` Theorem.
2. **Catalogue size scaling** is unmeasured. The 274-atom catalogue from a 3-element basis is small, but extrapolating to D'' with the full depth-1 basis (51 atoms) requires actually building it. The combinatorial bound suggests this could be in the hundreds of thousands at length-3.
3. **Adversarial cases past 16** were not constructed. The sweep used 16 cases; a stress sweep at 50–100 cases (especially with widened carriers, mixed face-state structures, and longer hosts) might surface failures the current set misses.
4. **No depth-3 case where broad-tailored catalogue itself fails** was found. If one exists, it would be the *first* algorithm-level depth-3 boundary. Worth searching for adversarially.

---

## Recommendations

In priority order:

### Define the frozen depth-3 domain D''

A proposed shape, mirroring D':

```
D'' :  depth_of(P) ≤ 3
       |A+| ≤ A_PLUS_MAX_3        (likely 2 or 3 to keep catalogue bounded)
       n_min ≤ N_MIN_MAX_3        (likely 4)
       Payload alphabet ⊆ depth-2 oracle catalogue
                          (= ORACLE_ATOM_PAYLOADS ∪ build_catalogue_d2_oracle output)
```

The narrowness of D'' is the design lever: tighter D'' = smaller catalogue = faster but less coverage. The depth-2 frozen domain set `A_PLUS_MAX = 3, N_MIN_MAX = 4`; D'' should probably start tighter (e.g. `A_PLUS_MAX_3 = 2`) and widen empirically.

### Implement `build_catalogue_d3_oracle`

Mirror `build_catalogue_d2_oracle` one level up: take a depth-2 basis, generate all depth-3 objects within D''. Time-and-space-budget the build before consuming it in production.

### Write the depth-3 completeness theorem

Structure mirrors the v0.6 left-quotient proof:
- Lemmas 1–4 (host recovery): identical, no depth dependency
- Lemma 5 (unit-leading base case): identical
- Lemma 6 (recursion strictly decreases depth): identical
- Lemma 7 (recursion bottoms out): bound becomes `1 + d(A)`, identical
- **Lemma 8 (quotient existence locally):** the hinge. Now needs catalogue-coverage as a hypothesis: *given a catalogue covering all payloads of A and B, the local quotient exists.* This is the formal statement of what the sweep observed empirically.

### Promote the sweep into a regression test

Convert the 16 cases into a `test_depth3_sweep.py` that runs against the broad-tailored catalogue. All-pass-on-broad would freeze the architecture's depth-3 reach as a contract. Any future change that breaks this set is automatically flagged.

---

## hmmm — preserved

- The non-uniqueness in case 06 (ALT-FACTOR) is a property of the problem, not the algorithm. But it raises a question about `store.left_factors` / `right_factors`: those return *one* match per stored object. If multiple valid factorizations exist for a stored P, the store reports only one. Whether that’s the right semantics for retrieval depends on the use case. Worth a separate audit pass on `store.py`’s contract once D'' work begins.
- The package’s `depth_of` and the spec’s `d` differ by 1 on non-unit objects. This sweep used the package’s convention. If a depth-3 theorem is written, the convention used must be stated explicitly to avoid the kind of off-by-one I almost made when first sizing test cases.
- `factor_search_v08` documents itself as “Witness-matrix recursive quotient solver for the frozen depth-2 domain.” That docstring should be updated either way after this sweep — either to acknowledge the depth-3 reach (with catalogue-coverage caveat), or to remain conservative until the formal D'' proof lands. Lean conservative; flag as a doc-update blocker on the D'' theorem.

---

## Provenance

- Sweep performed: 2026-05-07 against commit `d0307d3` plus the right-quotient fix from the prior session.
- Test harness: `depth3_sweep.py`, 16 cases, three catalogue levels per case, 20-second timeout per attempt.
- All cases completed; no timeouts, no exceptions.
- Total wallclock: ~30 seconds for 48 factor_search_v08 invocations.
