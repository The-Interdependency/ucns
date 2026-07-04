# UCNS Formal - Lean 4 scaffold for Theorem N

This directory is a Lean 4 scaffold for machine-checking the UCNS
completeness results, principally the Theorem N family described in
[`../ucns-theorem-n.md`](../ucns-theorem-n.md).

## Status: FRONTIER / awaiting external formal review

This is exploratory scaffolding. The theorem statements here are stubbed
with `sorry` and prove nothing yet. Lean will accept the file because a
`sorry` closes any goal, but each `sorry` is an unverified hole. No proof
obligation has been discharged by the presence of a stub.

The informal, prose-level argument for Theorem N and its instances lives in
[`../ucns-theorem-n.md`](../ucns-theorem-n.md). That document is the source of
truth for the claims; this directory is an attempt to restate those claims in
a form a proof assistant can eventually check.

## Mathlib / dependency discipline

Mathlib is now an explicit formal dependency in `lakefile.lean`, pinned to the
same Lean release as `formal/lean-toolchain`: Lean v4.7.0 and Mathlib v4.7.0.
The project no longer carries a separate direct `std4` requirement; Mathlib
pulls its Lean-library dependencies transitively.

Rules:

- Do not claim "Mathlib-free" as a theorem-status property.
- Do not add extra Lake dependencies until a proof actually needs them.
- Prefer specific imports inside proof files over blanket `import Mathlib` once
  a proof path stabilizes.
- If a broad import is temporarily necessary during search, reduce it later with
  `#min_imports` or an equivalent import-minimization pass.
- Document every load-bearing imported theorem or module that changes proof
  status.

## Proof-status non-transfer discipline

A `sorry`-backed statement confers no `DEFENDED` status to any consumer
repository. Concretely:

- A `theorem ... := sorry` in this directory is not a proof. It is a placeholder
  for a proof that does not yet exist.
- No downstream repository, package, or claim may cite this scaffold as evidence
  that any UCNS result is formally verified.
- A result graduates from FRONTIER only when every `sorry` in its statement and
  its transitive dependencies has been removed and replaced by a complete,
  type-checked proof term, and that has been confirmed by external formal review.

Until then, treat everything here as a specification draft, not a guarantee.

## Layout

- `lean-toolchain` - pins the Lean 4 toolchain version.
- `lakefile.lean` - Lake package definition (`Ucns`) with Mathlib pinned at
  v4.7.0.
- `Ucns/TheoremN.lean` - stub statements (all `sorry`) for:
  - depth-1 restricted completeness,
  - the depth-2 oracle result (Lemma 7),
  - catalogue-sufficient completeness (Theorem N).

## Building once Lean is installed

```sh
# from this directory, with elan/lake installed
lake exe cache get
lake build
```

`lake exe cache get` retrieves Mathlib cache artifacts where available. A
successful `lake build` here means only that the statements type-check with their
`sorry` placeholders; it does not mean the theorems are proven.

## Discharge state

`Ucns/CarrierLcm.lean` decomposes the Carrier-LCM Law
(prose: `../docs/carrier-support-pruning.md`) into a machine-checked
composition over explicit fold, denominator, slice-embedding, and upper-bound
lemmas.

Pinned-build status as of the Carrier-LCM discharge pass:

- `Ucns/CarrierLcm.lean` is `sorry`-free under `lake build Ucns.CarrierLcm`.
- The discharged surface includes `dvd_foldl_lcm_acc`, `dvd_foldl_lcm`,
  `foldl_lcm_dvd`, `nMin_dvd_of_denoms_subset`, `den_amod_dvd`,
  `den_add_dvd_lcm`, `den_circleFrac_add_dvd_lcm`,
  `slice_embedding_left/right`, `carrier_lcm_law_upper`,
  `carrier_lcm_law'`, and the public repaired-domain `Ucns.carrier_lcm_law`.
- This does not graduate the whole formal directory: imported frontier files
  such as `Ucns/Core.lean` and `Ucns/TheoremN.lean` still contain
  `sorry`-backed statements that inherit no DEFENDED status.
- The remaining Core cancellativity statement is packaged under
  `AlignedComplete` so the ratified nonempty/recursive-normalized/
  uniform-depth/canonical-carrier/common-depth/fuel hypotheses travel as one
  proof obligation; helper lemmas also derive `depth A ≤ d`, `0 < d`, and
  `∃ d0, d = d0 + 1` for unfolding the nonzero `multiplyFuel` branch. The
  remaining executable `sorry` is isolated as
  `multiply_left_cancellative_succ_obligation`. Product equality helpers now
  expose both the row-major `multiplyCells` equality and the product-carrier
  `Nat.lcm` equality from equality of successor-fuel products; the row-major
  helper surface also proves rectangular product length and right-cell-count
  equality under a nonempty left factor, then isolates equality of the first
  product row for the same left head cell.
