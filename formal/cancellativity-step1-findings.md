# Cancellativity — Step 1 findings (statement ruling input)

**Scope:** formalization track only. The cheap, decisive counterexample search
the handoff mandates *before* any proof attempt. It neither unblocks the
morphology/ZFAE build nor ratifies a statement — the statement ruling is
Erin's (canon). Nothing here is machine-checked; `sorry`-backed ≠ proven; no
tag/release rides on it.

**Target:** `formal/Ucns/Core.lean` · `theorem multiply_left_cancellative`.
**Reproduce:** `python3 formal/cancellativity_step1_search.py` (stdlib;
faithful port of `amod`/`amod4`/`circleFrac`/`nMin`/`multiplyFuel`/`depth`/
`HostNormalized`). Python ≥ 3.9.

> **Credit.** The four conditions in §"Further counterexamples" **and** the
> cross-operand common-depth condition below were found by the Codex automated
> review on PR #66 and independently reproduced here. Each falsifies a
> successive "corrected" statement this doc proposed; the recommended domain is
> the result of folding them all in.

---

## Conclusion

The bare theorem is **FALSE**, and so are several naive fixes.
Left-cancellativity holds only on a **restricted, aligned domain**. The
empirically counterexample-free candidate is `AlignedComplete`:

> **`Complete`** := `nonempty` (recursively) ∧ **recursive** `HostNormalized`
> ∧ per-object `uniform-depth` ∧ `canonical carrier` (`nd = nMin cells`,
> recursively).
> **`AlignedComplete A B C`** := `Complete A` ∧ `Complete B` ∧ `Complete C` ∧
> **`depth A = depth B = depth C`** (cross-operand common depth), with the
> existing `depth B,C ≤ d`.

| Hypotheses (besides `depth B,C ≤ d`) | result |
|---|---|
| none (bare), d=1 | **FALSE** — β0 host-angle collapse |
| top-only `HostNormalized` (as in `Core.lean`) + payloads-present, d=2 | **FALSE** — CE 64 |
| recursive `HostNormalized` + `AllPayloadsPresent` (naive), d=2/3 | **FALSE** — 4 further CEs (below) |
| **`Complete` on A,B,C but mixed depth**, d=3 | **FALSE** — depth-mismatch CE |
| `Complete` minus canonical-carrier (vary `nd`), d=2 | **FALSE** — CE 128 |
| **`AlignedComplete` (Complete + common depth)**, d=1–3 (incl. multi-cell) | **CE 0** |

These are **finite searches over small universes** (the d=2 row includes
multi-cell operands that exercise the `csA.bind` row partition) — strong
disconfirmation where they fail, supporting evidence where they pass, **not a
proof** of sufficiency.

So the handoff's Option B (host-normalized + all-payloads-present) is
**necessary but far from sufficient**: cancellativity additionally needs
nonemptiness, per-object uniform depth, a canonical carrier, **and**
cross-operand common depth.

---

## Mechanisms

### M1 — host angle-gauge collapse (β0). Not in the handoff's obligations.
`β0 := csB.head?.angle` is subtracted, so the product encodes only
`cb.angle − β0`; a single right cell's absolute angle is erased. Witness
(flat, d=1): `A=[(0,F,·)]`, `B=[(0,F,·)]`, `C=[(1,F,·)]` →
`multiplyFuel 1 A B = multiplyFuel 1 A C`. ⇒ **Obligation 2 ("recover
`cb.angle`") is false as stated**; it holds only after host-normalization pins
`β0 = 0`.

### M1′ — `Core.lean`'s `HostNormalized` is too weak (must be recursive).
It constrains only the head cell; the `some,some` payload branch subtracts the
*payload's* β0, so payloads differing only in head angle collide. Top-only
HostNormalized + payloads-present still gives **64** CEs at d=2,3; **recursive**
HostNormalized fixes that family.

### M2 — mixed payload-branch absorption (= Obligation 4). Needs **common depth**.
`(some p, none) ⇒ some p` vs `(some p, some q)` breaks injectivity. Per-object
"all payloads present" / uniform depth is **not** enough: if one operand bottoms
out (atom) at a shallower depth than the matching cell of the other, the
`some,none` branch fires *deeper* and returns the deeper operand's payload — see
the depth-mismatch CE below. The cure is **cross-operand common depth**
(`depth A = depth B = depth C`), so every paired cell reaches an atom on the
same step and the recursion stays in `some,some` (or `none,none`).

### M3 — partially RETRACTED, partially re-scoped.
The earlier claim of a *fuel off-by-one* (`depth B ≤ d` "off by one") was a
port-bug artifact: Lean `depth` is `1 + max payload depth` (a flat object has
depth **1**), so the fuel side of `depth B,C ≤ d` is fine. **But** the earlier
companion claim that "an unconstrained deep `A` is fine" was **wrong** — the
depth-mismatch CE is exactly an unconstrained-deeper-`A` collision. `A`'s depth
*is* constrained, not by a separate fuel bound but by the **common-depth**
equality (`depth A = depth B = depth C`), which with `depth B,C ≤ d` also bounds
`depth A ≤ d`.

## Further counterexamples (Codex review — all CONFIRMED)

Each survives the *previous* corrected statement (recursive `HostNormalized` +
`AllPayloadsPresent`/`Complete` + `depth B,C ≤ d`):

1. **Depth-mismatch atom (P1).** `d=3`, `A=C=[(0,F,[(0,F,[(0,F,·)])])]` (depth 3),
   `B=[(0,F,[(0,F,·)])]` (depth 2). Each of A, B, C is individually `Complete`
   (nonempty, recursive-HN, per-object uniform depth, canonical), and
   `depth B,C ≤ 3` — yet `multiplyFuel 3 A B = multiplyFuel 3 A C` with `B≠C`:
   `B` bottoms out an atom one level above `A`'s payload, so the inner
   `some,none` branch returns `A`'s deeper payload, matching `C`'s `some,some`
   result. ⇒ needs **cross-operand common depth** (`depth A = depth B = depth C`);
   per-object uniform depth alone does **not** suffice. *(Independently checked:
   over a mixed-depth `Complete` pool, CE > 0; adding `depth A = depth B = depth C`
   → CE 0.)*
2. **Carrier `nDec`/lcm (P1).** `Nat.lcm` is not left-cancellative: `A.nd=2`,
   `B.nd=1`, `C.nd=2`, identical cells → both carriers `lcm(2,·)=2`, products
   equal, `B≠C`. ⇒ needs **canonical carrier** (`nd = nMin`), so `nd` is not a
   free distinguishing field.
3. **Empty left operand (P2).** `A.cells = []` ⇒ `csA.bind … = []`, so the
   product is `mk (Nat.lcm nd_A nd_B) []` regardless of `B`'s cells; any two
   right operands of equal carrier then collide. Vacuously satisfies the
   (pre-`Nonempty`) hypotheses. ⇒ needs **nonempty `A`**.
4. **Empty payload as atom (P2).** `IsAtom []` is vacuously true, so an empty
   payload counts as an atom and collapses like (3) one level down. ⇒ atoms /
   objects must be **nonempty recursively**.

`AlignedComplete` (Conclusion) is the conjunction that removes M1, M1′, M2, M3,
and all four of these; it is empirically CE-free at d=1–3. Dropping the
canonical-carrier conjunct alone reintroduces 128 CEs; dropping common depth
reintroduces the depth-mismatch CE.

---

## Recommended statement (Erin rules)

Condition `A`, `B`, `C` on `Complete` **and** require common depth; keep
`depth B,C ≤ d`. Lean (RATIFIED 2026-06-21 and applied to `Core.lean` as the conditioned
statement, `sorry`-backed; the recursive predicates mirror the `depth`
mutual pattern. `AlignedComplete` and its projection helpers compile in `Core.lean`; proof is Step-2):

```lean
def Nonempty (x : UCNSObject) : Prop :=
  x.cells ≠ [] ∧ ∀ c, c ∈ x.cells → ∀ p, c.payload = some p → Nonempty p

def CanonicalCarrier (x : UCNSObject) : Prop :=
  x.nDec = nMin x.cells ∧
  ∀ c, c ∈ x.cells → ∀ p, c.payload = some p → CanonicalCarrier p

/-- Per-object completeness: every root→leaf path has equal length. -/
def UniformDepth (x : UCNSObject) : Prop :=
  (∃ k, ∀ c, c ∈ x.cells → depthCell c = k) ∧
  ∀ c, c ∈ x.cells → ∀ p, c.payload = some p → UniformDepth p

/-- Recursive host-normalization (Core.lean's `HostNormalized` is head-only:
    sufficient for the carrier-LCM law, NOT for cancellativity). -/
def HostNormalizedRec (x : UCNSObject) : Prop :=
  (∀ c, x.cells.head? = some c → c.angle = 0) ∧
  ∀ c, c ∈ x.cells → ∀ p, c.payload = some p → HostNormalizedRec p

def Complete (x : UCNSObject) : Prop :=
  Nonempty x ∧ HostNormalizedRec x ∧ UniformDepth x ∧ CanonicalCarrier x

def AlignedComplete (A B C : UCNSObject) (d : Nat) : Prop :=
  Complete A ∧ Complete B ∧ Complete C ∧
    depth A = depth B ∧ depth B = depth C ∧ depth B ≤ d ∧ depth C ≤ d

theorem multiply_left_cancellative_succ_obligation
    (A B C : UCNSObject) (d0 : Nat)
    (hABC : AlignedComplete A B C (d0 + 1))
    (h : multiplyFuel (d0 + 1) A B = multiplyFuel (d0 + 1) A C) :
    B = C := by
  sorry

theorem multiply_left_cancellative
    (A B C : UCNSObject) (d : Nat)
    (hABC : AlignedComplete A B C d)
    (h : multiplyFuel d A B = multiplyFuel d A C) :
    B = C := by
  rcases exists_fuel_pred_of_alignedComplete hABC with ⟨d0, rfl⟩
  exact multiply_left_cancellative_succ_obligation A B C d0 hABC h
```

(`AlignedComplete` packages `depth A = depth B = depth C`; with `depth B,C ≤ d`
this also bounds `depth A ≤ d`. Since every Lean `UCNSObject` has positive
depth, the packaged fuel hypotheses also imply `0 < d` and expose a predecessor
`∃ d0, d = d0 + 1`, ruling out the `multiplyFuel 0` identity branch. The
row-major helper `multiplyCells_eq_of_multiplyFuel_succ_eq` now exposes the
cell-list equality that remains to be inverted.) `Complete` + common depth is the **morphology-natural
domain**: equal-depth word-trees whose cells all carry payloads to a uniform
nonempty atom layer, with canonical carriers. Remaining ruling/Step-2 work: (i)
confirm `AlignedComplete` (or a minimal weakening) is the canonical domain, and
(ii) prove it.

## Ruling options (for the record)

- **A — unconditional.** Dead (M1).
- **B — host-normalized + total payloads (handoff).** Necessary but **not
  sufficient** — fails the four further CEs *and* the depth-mismatch CE. Needs
  recursive HostNormalized *plus* nonempty + uniform-depth + canonical-carrier
  + cross-operand common depth.
- **C — condition `A` only.** Insufficient — M1/M1′/M2 and CEs 2–4 use `B`/`C`
  structure and the carrier; all of `A,B,C` must be `Complete` and equal-depth.

## Proof plan once ratified

1. Carrier-LCM Rat leaves → `amod4` additive-cancellation (Obligation 2),
   applied after recursive host-normalization; `CanonicalCarrier` gives the
   `nMin`/`Nat.lcm` leg.
2. Face XOR self-inverse (Obligation 1, trivial).
3. Row-partition lemma for `csA.bind (csB.map …)` (Obligation 3 — the
   combinatorial core); `Nonempty A` rules out the empty-bind collapse.
4. Induction on fuel under `AlignedComplete`: per-object `UniformDepth` **plus**
   `depth A = depth B = depth C` keeps every paired cell in the `some,some`
   branch (no `some,none`), so the IH applies cleanly.

## Disclosure

Cancellativity is **not** proven; the morphology decomposition is **not** shown
lossless; `formal/` remains all-`sorry`. No tag/release/version bump rides on
this. The statement ruling is Erin's; the proof, once ratified, is the
executor's.
