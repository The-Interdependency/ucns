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

> **Credit.** The four conditions in §"Further counterexamples" were found by
> the Codex automated review on PR #66 and independently reproduced here. They
> falsify the first "corrected" statement this doc proposed; the recommended
> domain below is the result of folding them in.

---

## Conclusion

The bare theorem is **FALSE**, and so is the naive fix. Left-cancellativity
holds only on a **restricted domain**. The empirically counterexample-free
candidate is:

> **`Complete`** := `nonempty` (recursively) ∧ **recursive** `HostNormalized`
> ∧ `uniform-depth` (complete tree) ∧ `canonical carrier` (`nd = nMin cells`,
> recursively), required on `A`, `B`, `C`, with the existing `depth B,C ≤ d`.

| Hypotheses (besides `depth B,C ≤ d`) | result |
|---|---|
| none (bare), d=1 | **FALSE** — β0 host-angle collapse |
| top-only `HostNormalized` (as in `Core.lean`) + payloads-present, d=2 | **FALSE** — CE 64 |
| recursive `HostNormalized` + `AllPayloadsPresent` (naive), d=2/3 | **FALSE** — 4 further CEs (below) |
| **`Complete` on A,B,C**, d=1/2 (incl. multi-cell depth-2) | **CE 0** |
| `Complete` minus canonical-carrier (vary `nd`), d=2 | **FALSE** — CE 128 |

These are **finite searches over small universes** (the d=2 row now includes
multi-cell operands that exercise the `csA.bind` row partition) — strong
disconfirmation where they fail, supporting evidence where they pass, **not a
proof** of sufficiency.

So the handoff's Option B (host-normalized + all-payloads-present) is
**necessary but not sufficient**; cancellativity additionally needs
nonemptiness, uniform depth, and a canonical-carrier condition.

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

### M2 — mixed payload-branch absorption (= Obligation 4). Stronger than thought.
`(some p, none) ⇒ some p` vs `(some p, some q)` breaks injectivity. Naively this
looked killed by "all payloads present", but the **depth-mismatch** case below
shows the `some,none` branch still fires deeper when one operand bottoms out
earlier — so the cure is *uniform depth*, not merely "present".

### M3 — RETRACTED. No fuel off-by-one. (Port-bug artifact.)
Lean `depth` is `1 + max payload depth` (a flat object has depth **1**); an
earlier note used 0 and wrongly inferred a strict-fuel / `depth A ≤ d` need.
With the correct metric, `depth B,C ≤ d` suffices on the fuel side and an
unconstrained deep `A` is fine *within `Complete`*.

## Further counterexamples (Codex review — all CONFIRMED)

Each survives recursive `HostNormalized` + naive `AllPayloadsPresent` +
`depth B,C ≤ d`, i.e. falsifies the first corrected statement:

1. **Depth-mismatch atom (P1).** `d=3`, `A=C=[(0,F,[(0,F,[(0,F,·)])])]`,
   `B=[(0,F,[(0,F,·)])]`. `B` bottoms out an atom one level above `A`'s
   payload, so the inner `some,none` branch returns `A`'s deeper payload,
   matching `C`'s `some,some` result. ⇒ needs **uniform depth** (no early atom
   against a deeper operand).
2. **Carrier `nDec`/lcm (P1).** `Nat.lcm` is not left-cancellative: `A.nd=2`,
   `B.nd=1`, `C.nd=2`, identical cells → both carriers `lcm(2,·)=2`, products
   equal, `B≠C`. ⇒ needs **canonical carrier** (`nd = nMin`), so `nd` is not a
   free distinguishing field.
3. **Empty left operand (P2).** `A.cells = []` ⇒ `csA.bind … = []` erases every
   right cell; all `B` collide. Vacuously satisfies the predicates. ⇒ needs
   **nonempty `A`**.
4. **Empty payload as atom (P2).** `IsAtom []` is vacuously true, so an empty
   payload counts as an atom and collapses like (3) one level down. ⇒ atoms /
   objects must be **nonempty recursively**.

The `Complete` domain (Conclusion) is exactly the conjunction that removes M1,
M1′, M2, and all four of these, and is empirically CE-free at d=1,2; dropping
the canonical-carrier conjunct alone reintroduces 128 CEs.

---

## Recommended statement (Erin rules)

Condition `A`, `B`, `C` on `Complete`; keep `depth B,C ≤ d`. Proposed Lean
(PROPOSED — **not** merged into `Core.lean`; the recursive predicates need the
same mutual / well-founded treatment as `depth`/`depthCells`/`depthCell`):

```lean
def Nonempty (x : UCNSObject) : Prop :=
  x.cells ≠ [] ∧ ∀ c, c ∈ x.cells → ∀ p, c.payload = some p → Nonempty p

def CanonicalCarrier (x : UCNSObject) : Prop :=
  x.nDec = nMin x.cells ∧
  ∀ c, c ∈ x.cells → ∀ p, c.payload = some p → CanonicalCarrier p

/-- Complete tree: every root→leaf path has equal length (no early atom). -/
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

theorem multiply_left_cancellative
    (A B C : UCNSObject) (d : Nat)
    (hA : Complete A) (hB : Complete B) (hC : Complete C)
    (h  : multiplyFuel d A B = multiplyFuel d A C)
    (hdB : depth B ≤ d) (hdC : depth C ≤ d) :
    B = C := by
  sorry
```

`Complete` is the **morphology-natural domain**: uniform-depth word-trees whose
cells all carry payloads down to a nonempty atom layer, with canonical
carriers. The remaining ruling/Step-2 work is to (i) confirm `Complete` (or a
minimal weakening) is the canonical domain, and (ii) prove it — `uniform-depth`
+ `nonempty` are what make the `some,some` induction clean and stop the
`some,none` branch firing, and `CanonicalCarrier` discharges the `Nat.lcm` leg.

## Ruling options (for the record)

- **A — unconditional.** Dead (M1).
- **B — host-normalized + total payloads (handoff).** Necessary but **not
  sufficient** — fails the four further CEs. Needs recursive HostNormalized
  *plus* nonempty + uniform-depth + canonical-carrier.
- **C — condition `A` only.** Insufficient — M1/M1′/M2 and CEs 2–4 use `B`/`C`
  structure and the carrier; all of `A,B,C` must be `Complete`.

## Proof plan once ratified

1. Carrier-LCM Rat leaves → `amod4` additive-cancellation (Obligation 2),
   applied after recursive host-normalization; `CanonicalCarrier` gives the
   `nMin`/`Nat.lcm` leg.
2. Face XOR self-inverse (Obligation 1, trivial).
3. Row-partition lemma for `csA.bind (csB.map …)` (Obligation 3 — the
   combinatorial core); `Nonempty A` rules out the empty-bind collapse.
4. Induction on fuel under `Complete`: `UniformDepth` keeps every pair in the
   `some,some` branch (no `some,none`), so the IH applies cleanly.

## Disclosure

Cancellativity is **not** proven; the morphology decomposition is **not** shown
lossless; `formal/` remains all-`sorry`. No tag/release/version bump rides on
this. The statement ruling is Erin's; the proof, once ratified, is the
executor's.
