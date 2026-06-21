# Cancellativity — Step 1 findings (statement ruling input)

**Scope:** formalization track only. This is the cheap, decisive
counterexample search the handoff mandates *before* any proof attempt. It
neither unblocks the morphology/ZFAE build nor ratifies a statement — the
statement ruling is Erin's (canon). Nothing here is machine-checked;
`sorry`-backed ≠ proven; no tag/release rides on it.

**Target:** `formal/Ucns/Core.lean` · `theorem multiply_left_cancellative`.
**Reproduce:** `python3 formal/cancellativity_step1_search.py` (stdlib only;
a faithful port of `amod4`, `multiplyFuel`, `depth`, `HostNormalized`).

---

## Conclusion

The bare theorem is **FALSE as stated**. It becomes counterexample-free under
two added hypotheses — **recursive HostNormalized** and **AllPayloadsPresent**
— with the *existing* `depth B,C ≤ d` bounds and **no** extra fuel or depth-`A`
condition. This is essentially the handoff's **Option B**, with two
corrections (HostNormalized must be recursive; no strict-fuel bound is needed).

| Hypotheses (besides `depth B,C ≤ d`) | result |
|---|---|
| none (bare theorem), `d=1` | **FALSE** — counterexample found |
| top-only `HostNormalized` (as in `Core.lean`) + `AllPayloadsPresent`, `d=2,3` | **still FALSE** — CE = 64 |
| **recursive** `HostNormalized` + `AllPayloadsPresent`, `d=2,3` | **CE = 0** |
| …same, with unconstrained deep `A` (depth 3 > d) | **CE = 0** |

---

## The failure mechanisms

### M1 — host angle-gauge collapse (β0). NOT in the handoff's obligations.
`multiplyFuel` sets `β0 := csB.head?.angle` and emits angles
`amod4(ca.angle + (cb.angle − β0))`. The right operand's **own** first-cell
angle is subtracted, so absolute angles of `B` are not encoded — the product
is invariant under shifting all of `B`'s angles by a constant, and a
single-cell `B`'s angle is erased entirely. Witness (flat, depth 1, `d=1`):

```
A = [(0,F,·)]   B = [(0,F,·)]   C = [(1,F,·)]
multiplyFuel 1 A B = multiplyFuel 1 A C = [(0,F,·)]      B ≠ C ,  depth B,C = 1 ≤ 1
```

Consequence: **handoff Obligation 2 ("recover `cb.angle` by `amod4`
cancellation") is false for the head cell as stated.** It only holds once
host-normalization pins `β0 = 0`. `HostNormalized` is load-bearing, not
cosmetic.

### M1′ — the in-file `HostNormalized` is too weak (must be recursive).
`Core.lean`'s `HostNormalized` constrains only the **head** cell's angle. But
the `some,some` payload branch calls `multiplyFuel d p q`, which subtracts the
*payload's* own β0 — so payloads differing only in head angle collide. Under
top-only HostNormalized + AllPayloadsPresent the search still finds **64**
counterexamples at `d=2,3`:

```
A = [(0,F,[(0,F,·)])]   B = [(0,F,[(0,F,·)])]   C = [(0,F,[(1,F,·)])]
```

(`B`,`C` head-normalized, but their payload heads are `0` vs `1`.) Making
`HostNormalized` **recursive** (object and all payloads) drops this to **0**.

### M2 — mixed payload-branch absorption. (= handoff Obligation 4, confirmed.)
`(some p, none) ⇒ some p` versus `(some p, some q) ⇒ some (mul d p q)` breaks
injectivity: a present `A`-payload absorbs the difference between a `none`
`B`-cell and a `some` `C`-cell. Eliminated by **AllPayloadsPresent** (no
`none` payload at any multiplied cell; recursion bottoms at atom leaves).

### M3 — RETRACTED. There is no fuel off-by-one.
An earlier note claimed `depth B ≤ d` was off by one and a strict fuel /
`depth A ≤ d` bound was needed. That was an artifact of a port bug: Lean's
`depth` is `1 + max payload depth` (**a flat object has depth 1**), which my
first port set to 0. With the correct metric, `depth B,C ≤ d` already gives
the inner recursion enough fuel, and an **unconstrained deep `A`** yields no
counterexample (row 4 above). No fuel bound and **no `depth A ≤ d`** needed.

---

## Recommended statement (Option B, corrected) — Erin rules

Add to the existing theorem: `HostNormalized` (recursive) and
`AllPayloadsPresent` on `A`, `B`, `C`; keep `depth B ≤ d`, `depth C ≤ d`; add
no depth-`A` or fuel hypothesis.

Proposed Lean (PROPOSED — **not** merged into `Core.lean`; predicates need the
same mutual/well-founded treatment as `depth`/`depthCells`/`depthCell`):

```lean
/-- A "letter": a leaf whose every cell payload is `none`. -/
def IsAtom (x : UCNSObject) : Prop :=
  ∀ c, c ∈ x.cells → c.payload = none

/-- No `none` payload at any *multiplied* cell; recursion bottoms at atoms.
    (Matches the morphology: every word-cell carries a payload.) -/
def AllPayloadsPresent (x : UCNSObject) : Prop :=
  ∀ c, c ∈ x.cells → ∃ p, c.payload = some p ∧ (IsAtom p ∨ AllPayloadsPresent p)

/-- Recursive host-normalization: head angle 0 for the object AND every payload.
    (Core.lean's current `HostNormalized` is the non-recursive head-only version
    — sufficient for the carrier-LCM law, NOT for cancellativity.) -/
def HostNormalizedRec (x : UCNSObject) : Prop :=
  (∀ c, x.cells.head? = some c → c.angle = 0) ∧
  (∀ c, c ∈ x.cells → ∀ p, c.payload = some p → HostNormalizedRec p)

theorem multiply_left_cancellative
    (A B C : UCNSObject) (d : Nat)
    (hAn : HostNormalizedRec A) (hBn : HostNormalizedRec B) (hCn : HostNormalizedRec C)
    (hAp : AllPayloadsPresent A) (hBp : AllPayloadsPresent B) (hCp : AllPayloadsPresent C)
    (h   : multiplyFuel d A B = multiplyFuel d A C)
    (hdB : depth B ≤ d) (hdC : depth C ≤ d) :
    B = C := by
  sorry
```

The one genuine **definitional ruling**: where `AllPayloadsPresent` bottoms
out. It is satisfiable only with an atom convention (a pure "no `none`
anywhere" predicate is uninhabited for finite objects). `IsAtom` above is one
choice (leaf = all-`none` letter); ratify it or supply the canonical atom
definition.

---

## The three ruling options (for the record)

- **Option A — unconditional.** Dead. The bare theorem is refuted (M1); do not
  attempt to prove it.
- **Option B — host-normalized + total payloads.** Recommended, with the two
  corrections above: HostNormalized must be **recursive**, and **no** extra
  fuel/`depth A` hypothesis is needed (contra the earlier draft). Search-clean
  at `d=2,3` incl. deep `A`.
- **Option C — condition `A` only.** Insufficient. M1/M1′ (β0) and M2 are
  driven by `B`/`C` structure; HostNormalized and AllPayloadsPresent are
  required on `B` and `C` (and on `A` so the `some,some` recursion stays in
  the inductive domain).

## Proof plan once ratified (unchanged in spirit, re-anchored)

1. Carrier-LCM Rat leaves first → gives the `amod4` additive-cancellation
   lemma (Obligation 2), now applied **after** recursive host-normalization.
2. Face XOR self-inverse (Obligation 1, trivial).
3. Row-partition lemma for `csA.bind (csB.map …)` (Obligation 3 — the real
   combinatorial work; `List.bind`/`List.length_bind`).
4. Induction on fuel `d` under the conditioned hypotheses; the `some,some`
   branch is clean (no mixed branches under AllPayloadsPresent; payload heads
   normalized under recursive HostNormalized).

## Disclosure

Cancellativity is **not** proven; the morphology decomposition is **not**
shown lossless. `formal/` remains all-`sorry`. No tag, release, or version
bump on the strength of this. The statement ruling is Erin's; the proof, once
ratified, is the executor's.
