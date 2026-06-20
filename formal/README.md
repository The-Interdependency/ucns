# UCNS Formal — Lean 4 scaffold for Theorem N

This directory is a **Lean 4 scaffold** for machine-checking the UCNS
completeness results, principally the Theorem N family described in
[`../ucns-theorem-n.md`](../ucns-theorem-n.md).

## Status: FRONTIER / awaiting external formal review

This is exploratory scaffolding. **The theorem statements here are stubbed
with `sorry` and prove nothing yet.** Lean will accept the file (a `sorry`
closes any goal) but each `sorry` is an unverified hole — no proof obligation
has been discharged. The statements themselves may also be imprecise
transcriptions of the informal claims and are subject to revision during
formal review.

The informal, prose-level argument for Theorem N (and its instances Lemma 7
and the depth-3 results) lives in [`../ucns-theorem-n.md`](../ucns-theorem-n.md).
That document is the source of truth for the *claims*; this directory is an
attempt to restate those claims in a form a proof assistant could eventually
check.

## Mathlib / dependency discipline

This formalization intentionally starts small: Lean core plus the pinned `std4`
dependency in `lakefile.lean`. It does **not** currently depend on Mathlib.

That is a discipline, not a promise of permanent zero dependencies. If a
Mathlib-free proof path becomes unobtainable, the correct move is to say so
explicitly and add the minimum required dependency rather than leaving a
`sorry` in place while claiming formal discharge. Dependency-minimal is good;
proof-discharge is the controlling requirement.

Rules:

- Do not claim "Mathlib-free" as a theorem-status property.
- Do not block proof discharge merely to preserve a zero-dependency aesthetic.
- If Mathlib becomes necessary, document exactly which imported theorem or
  module is doing load-bearing work.
- A dependency-free stub with `sorry` proves less than a dependency-backed,
  sorry-free proof.

## Proof-status non-transfer discipline

**A `sorry`-backed statement confers no `DEFENDED` status to any consumer
repository.** Concretely:

- A `theorem ... := sorry` in this directory is *not* a proof. It is a
  placeholder for a proof that does not yet exist.
- No downstream repository, package, or claim may cite this scaffold as
  evidence that any UCNS result is formally verified.
- A result graduates from FRONTIER only when every `sorry` in its statement
  (and its transitive dependencies) has been removed and replaced by a
  complete, type-checked proof term, and that has been confirmed by external
  formal review.

Until then, treat everything here as a specification draft, not a guarantee.

## Layout

- `lean-toolchain` — pins the Lean 4 toolchain version.
- `lakefile.lean` — minimal Lake package definition (`Ucns`), currently with
  `std4` and no Mathlib dependency.
- `Ucns/TheoremN.lean` — stub statements (all `sorry`) for:
  - depth-1 restricted completeness,
  - the depth-2 oracle result (Lemma 7),
  - catalogue-sufficient completeness (Theorem N).

## Building (once Lean is installed)

```sh
# from this directory, with elan/lake installed
lake build
```

A successful `lake build` here means only that the *statements* type-check
with their `sorry` placeholders — it does **not** mean the theorems are proven.

## Discharge state (2026-06-10)

`Ucns/CarrierLcm.lean` decomposes the Carrier-LCM Law
(prose: `../docs/carrier-support-pruning.md`) into a machine-checked
composition over five isolated leaf obligations.

Sorry-free, audited via `#print axioms` (depend on `propext` only):

- `dvd_foldl_lcm_acc`, `dvd_foldl_lcm`, `foldl_lcm_dvd` — the lcm fold
  engine both proof directions run on
- `nMin_dvd_of_denoms_subset` — denominator-set containment implies carrier
  divisibility

Open leaves (`sorry`, inherit no status): `den_amod_dvd`,
`den_add_dvd_lcm`, `slice_embedding_left/right`,
`carrier_lcm_law_upper`. `carrier_lcm_law'` composes the bounds by
`Nat.dvd_antisymm`; its trust level equals the leaves'.
