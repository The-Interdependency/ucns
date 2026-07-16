# UCNS Formal — public-gonol foundation and Theorem N scaffold

This directory contains two formally distinct surfaces that must not be
flattened into one another:

1. **`Ucns/PublicGonol.lean`** — the load-bearing public frame: the exact
   157-position carrier, fixed SPACE/ZERO Möbius-twist origin, orientation flip
   after one 360-degree circuit, and complete return after 720 degrees.
2. **`Ucns/Core.lean`, `Ucns/CarrierLcm.lean`, and `Ucns/TheoremN.lean`** — the
   existing normalized recursive factorization-object model and its finite
   search/proof surfaces.

The public gonol is canon for all UCNS. The normalized recursive object model is
an internal representation within UCNS. A bridge from the fixed public frame to
that representation is **`hmmm`** until Erin Spencer specifies it. No theorem in
this directory may infer that bridge from angle normalization, a first anchor,
a quotient, or a continuous-coordinate convention.

## Public-gonol canon

The formal source records the canon supplied by Erin and implemented in
`The-Interdependency/a0-betatest@7af8debf6ef3905f01baff02b43d8c3bee16ccbc`:

```text
arity = 157
position 0 = SPACE = ZERO
position 0 = Möbius twist point = seam = system origin
origin is fixed, not a gauge choice
one 360-degree circuit flips orientation
complete return requires 720 degrees
private/admissible transformations preserve origin
```

`Ucns/PublicGonol.lean` proves the elementary consequences of those declarations:

```text
origin is uniquely position zero
one circuit returns to the same local carrier position but changes orientation
two circuits return to the same local position and restore orientation
720 degrees = two 360-degree circuits
existing mod-4 half-turn representation distinguishes 360 from the 720 return
origin-preserving permutations fix SPACE/ZERO
```

The mod-4 lemmas establish the already-declared 720-degree period of the
internal angle representation. They do **not** define a map from public-gonol
vertices to internal angles.

## Theorem N status: FRONTIER / awaiting external formal review

The completeness theorem statements in `Ucns/TheoremN.lean` are still closed
with `sorry` and prove nothing yet. Lean accepts the files because `sorry` closes
any goal, but each `sorry` is an unverified hole. No proof obligation is
discharged by the presence of a stub, and a successful build is never a proof
while any transitive theorem hole remains.

The search model is no longer opaque: `Ucns/TheoremN.lean` defines catalogue
normalization, split candidates, structural host-angle recovery, payload and
face assignments, assembly, unit rejection, exact recomposition, witness
records, and recursive catalogue membership. The Python-side conformance fixture
lives in `../tests/test_formal_conformance.py`.

All Theorem N statements are presently scoped to the normalized recursive
factorization algebra defined by `Ucns/Core.lean`. They do not establish
completeness for the public gonol or for a public-gonol-to-factorization bridge.

## Carrier-LCM scope

`Ucns/CarrierLcm.lean` is sorry-free under the pinned build. It proves the LCM
law for `nMin` as currently defined on `Complete` normalized factorization
objects:

```text
nMin(multiplyFuel A B) = lcm(nMin A, nMin B)
```

`nMin` uses denominators of the internal projected circle fractions
`(angle mod 2) / 2`. The theorem is machine-checked for that definition. It is
not, without an additional bridge theorem, a theorem about the complete
fixed-origin, twist-bearing public carrier.

## Modeling boundaries

`Ucns/Core.lean` retains the existing Python-faithful internal model:

- rational angles reduced modulo four half-turn units;
- 720-degree period;
- object-relative first-angle normalization;
- face XOR;
- recursive payload multiplication;
- `nMin` from projected circle-fraction denominators.

Object-relative normalization is not applied to the public gonol and does not
move or redefine SPACE/ZERO.

The following remain explicitly unresolved:

```text
public-gonol vertex/path → normalized recursive object bridge
proof that the internal multiplication preserves the public twist/origin
proof that nMin is the complete twist-bearing carrier invariant
proof that face XOR is the public-gonol seam/chirality law
public-gonol scope for Theorem N completeness
```

## Proof-status non-transfer discipline

A `sorry`-backed statement confers no `DEFENDED` status to any consumer.
Specifically:

- A theorem closed by `sorry` is not a proof.
- A green `lake build` proves only that definitions and proof terms type-check.
- No downstream package may cite this directory as validation of EDCM
  measurements, METAPAT semantics, linguistic meaning, embedding quality,
  diagnosis, intent, consciousness, or external truth.
- A result graduates from `FRONTIER` only after every transitive hole is removed
  and external formal review confirms the proof.

## Mathlib / dependency discipline

Mathlib is pinned in `lakefile.lean` to Lean/Mathlib v4.7.0.

Rules:

- Do not claim “Mathlib-free” as theorem status.
- Do not add dependencies until a proof requires them.
- Prefer specific imports once proof search stabilizes.
- Record every load-bearing imported theorem that changes proof status.

## Layout

```text
lean-toolchain              pinned Lean toolchain
lakefile.lean               pinned Mathlib package definition
Ucns.lean                   library imports
Ucns/PublicGonol.lean       fixed twist origin and 720-degree return canon
Ucns/Core.lean              normalized recursive factorization definitions
Ucns/CarrierLcm.lean        sorry-free internal nMin LCM theorem
Ucns/TheoremN.lean          defined search model + sorry-backed completeness family
```

## Building

```sh
cd formal
lake exe cache get
lake build
```

A successful build means only that the current formal surface type-checks under
the pinned toolchain.

## Discharge state

- `Ucns/PublicGonol.lean` is intended to be sorry-free.
- `Ucns/CarrierLcm.lean` is intended to remain sorry-free for the scoped internal
  `nMin` theorem.
- `Ucns/TheoremN.lean` retains its declared `sorry` holes.
- The former broad cancellativity claim remains refuted on the existing weak
  domain by the concrete mod-4 tail-angle counterexample.

## hmmm

The irreducible public frame is now formalized instead of assumed away. The
missing bridge is visible, and no local normalization rule is allowed to stand
in for it.
