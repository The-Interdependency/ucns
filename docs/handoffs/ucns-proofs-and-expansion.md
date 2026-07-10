# Handoff — UCNS proof frontier and mathematical expansion

**Prepared by:** Claude (review + roadmap), on behalf of Erin Patrick Spencer / The Interdependency
**Date:** 2026-07-10
**Target repo:** `The-Interdependency/ucns` — Claude's repo under one-AI-one-repo. Executor is the ucns maintainer (Claude by custody) or a delegated prover; either way the claim-status discipline below is binding.
**Sources:** the v0.6 Left-Quotient Completeness proof (`ucns_v06_completeness_proof.md`, canon); the live algebra/geometry grades in `a0-betatest/HMMM.md`; Lean specifics from prior working memory, flagged for confirmation against the live `formal/` tree.
**Claim-status legend:** proven · defended · oracle-complete · test-backed · conjectural · frontier. No status transfers across a shared name.

---

## Current state — what is and isn't proven

**UCNS-A — the factorization algebra.** *[proven]* The Left-Quotient Completeness Theorem holds: induction on nesting depth, no new axioms, dissolving the old "Class III boundary" — there is no unfactorable subclass on finite-depth objects. *[oracle-complete]* Live grade in HMMM.md: DEFENDED + ORACLE-COMPLETE at the depths the catalogue covers. The load-bearing dependency is cancellativity (E10.4), currently *sketch induction + empirics only* — a proof sketch plus zero violations across 11,016 product pairs, not a fully written induction.

**UCNS-G — the metric geometry.** *[frontier]* Unproven. The algebra's completeness lends it nothing; the "Theorem N proof status is not transferred by shared name" rule exists to keep that boundary honest.

**Formal (Lean) layer.** *[test-backed, not formally verified]* The algebra is exhaustively tested and structurally argued, but the Lean verification carries open `sorry`s on the arithmetic substrate. Until they close, the honest status is *test-backed*.

---

## Proof track — harden the floor, in order

### P1 — Formalize cancellativity in Lean (not prose)
Cancellativity is the lemma the whole algebra stands on and is its least-proven part. A machine-checked induction promotes the sketch **and** advances formal verification in one motion — do not write the induction twice. Begin with the arithmetic leaves it rests on: the Rat-denominator obligations (`den_add_dvd_lcm`, `den_amod_dvd` — confirm names against live `formal/`), using Mathlib as a **proof-time** dependency only; the runtime zero-dependency guarantee is unchanged.
- *Contract:* cancellativity discharged with zero `sorry` on finite depth.

### P2 — Write right_quotient completeness
The cheapest real win. It is the exact dual of the proven left-quotient theorem, symmetric under the block-leading-position exchange, and currently only *conjectural*. Writing it closes division in both directions.
- *Contract:* a standalone proof document mirroring the left case; `right_quotient` regraded *proven* on the verified domain.

### P3 — Reach zero sorries
Discharge order (memory; confirm against live): Rat-denominator leaves → `carrier_lcm_law_upper` → the two `slice_embedding` List-membership leaves. Reaching zero `sorry` is the status jump — *test-backed* becomes *formally verified*, the single most consequential upgrade the project's external narrative can earn.
- *Contract:* `lake build` green, zero `sorry`, Mathlib confined to proof-time.

---

## Expansion track — new territory, gated on the floor being machine-checked

### E1 — UCNS-G metric geometry
The flagship. The correct first move is not to prove geometry claims but to **prove the bridge**: the exact relationship between the algebra and the coordinates (r, θ, z, w), so "route through the bridge, don't claim by name" graduates from a discipline into a theorem. Sequenced after Lean-green on the algebra, because opening geometry on an unverified floor is the precise status-leakage the no-transfer rule guards.

### E2 — Unbounded depth
The completeness proof's termination (Lemmas 6, 7) is stated for **finite** nesting and explicitly fails for infinite / unbounded-depth objects. Extending it needs a well-founded or coinductive treatment. See the pre-flight — this may already be a gap rather than a frontier.

### E3 — Carrier widening (the v080–v090 FRONTIER work)
Widens the **domain** the completeness theorem covers rather than proving new structure. Currently parked FRONTIER; unpark once the finite-depth floor is fully verified.

---

## Pre-flight — do this before any sprint

Reconcile **what the theorem covers** against **what the current kernel admits.** The completeness proof of record is v0.6; the live kernel is ~v0.8/0.9 and the depth-2 / carrier-widening experiments (v080–v090) suggest the frontier already moved past depth-1. If the current kernel admits depth-2 objects that the completeness theorem does not yet reach, then E2 (unbounded depth) is not expansion — it is a gap beneath a claim already in use, and it moves to the top of the proof track, ahead of P2.

---

## Compliance and bar

- Every assertion typed by claim status; memory-derived figures (the Lean leaf names, the `sorry` count) reconfirmed against the live repository before use in any external document.
- Lean runtime stays zero-dependency; Mathlib is a **proof-time** dependency in `formal/lakefile.lean` only.
- Any new or changed Python / Lean module follows meta-module-build (manifest-first) per skill-lib.
- No theorem, proof, or empirical status transfers by shared name — UCNS-A's completeness says nothing about UCNS-G.
- A0-facing surfaces consume `ucns.a0_safe`, not raw factorization sentinels, and treat `SEQ-PRIME` outside `VERIFIED_DOMAIN_LABELS` as non-absolute.

---

## hmmm

- Currency: the proof state read here is v0.6; the live kernel has moved. The pre-flight is not optional — it decides whether E2 is a frontier or a hole, and that reorders the whole track.
- Memory-flagged: the Lean leaf names (`den_add_dvd_lcm`, `den_amod_dvd`, `carrier_lcm_law_upper`, `slice_embedding`) and the exact `sorry` count come from prior working memory and must be confirmed against the live `formal/` before being quoted anywhere external.
- Executor: ucns is Claude's under one-AI-one-repo. If this is delegated to another prover, custody of the ucns pen still returns to Claude — the delegate produces proofs for review, not commits by shared name.
