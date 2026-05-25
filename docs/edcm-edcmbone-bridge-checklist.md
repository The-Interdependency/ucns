# EDCM / edcmbone ↔ UCNS Bridge Checklist

**Status:** Checklist for future UCNS-A ↔ UCNS-G (EDCM / edcmbone) bridge
work. Not a bridge construction. Not a claim that one exists.
**Date pinned:** 2026-05-22
**Companion docs:**
- `docs/ucns-shape-reconciliation.md` — PARALLEL verdict (PR #21).
- `docs/ucns-g-prime-cylinder-supplement.md` — UCNS-G v3 supplement (PR #22).
- `The-Interdependency/edcmbone:docs/ucns-boundary.md` — non-transfer rule.
- `The-Interdependency/edcmbone:docs/handoffs/2026-05-22-ucns-g-prime-cylinder-v3.md` — UCNS-G v3 pin.

## 0. Why this exists

The `ucns` repo's theorem frontier is fenced. UCNS-A is the recursive
factorization algebra defined and implemented in this repo.
**UCNS-G** is the EDCM metric geometry pinned by `edcmbone` (a
prime-indexed tensor of non-closing Möbius-cylinder metric disks).

The PARALLEL verdict from `docs/ucns-shape-reconciliation.md` says: no
source-backed bijection exists between UCNS-A and UCNS-G. This document
exists so that any future attempt to construct one has to pass a fixed
checklist before any theorem status is transferred.

This document does **not** change any UCNS-A code, theorem, or status
label. It only records the gate.

## 1. What UCNS-A currently proves / implements

(From `docs/claims-ledger.md` and `CLAUDE.md`. Status vocabulary per
`docs/ucns-spec-status-addendum-2026-05-16.md`.)

| Claim / surface | Status |
|---|---|
| Flat kernel algebra | `DEFENDED` |
| Depth-1 restricted completeness | `DEFENDED` |
| Depth-2 oracle (smallest class, Lemma 7) | `DEFENDED` + `ORACLE-COMPLETE` |
| Full frozen depth-2 domain | `IMPLEMENTED` + `TEST-BACKED` (not yet `DEFENDED`) |
| Depth-3 asymmetric (Theorem 9) | `TEST-BACKED` (6/6 empirical) |
| Catalogue-sufficient completeness (Theorem N) | `DEFENDED` — proof drafted, awaiting external formal review |
| Tractable sub-catalogues | `FRONTIER` |
| Carrier widening | `FRONTIER` / out of v1.0 scope |
| `SEQ-PRIME` as solver sentinel inside defended-complete domains | `DEFENDED` policy rule |

Core implemented surface:

- `UCNSObject(n_dec, n_min, A_plus, F_plus)` with `(angle, payload)` anchors,
  modulo-4 doubled-cover angle arithmetic, payload recursion, face bits,
  XOR face composition.
- `multiply`, `factor_search_v08`, `left_quotient`, `right_quotient`,
  `UCNSStore`, `recursive_encode`/`recursive_decode`.

**None of these speak about transcripts, behavioral metrics, scalar
EDCM vectors, or signed ternary axis states.**

## 2. What UCNS-G / EDCM / edcmbone currently measures

(From `edcmbone:docs/handoffs/2026-05-22-ucns-g-prime-cylinder-v3.md`
and `edcmbone:docs/ucns-boundary.md`.)

UCNS-G v3 pins:

- `UCNS-G = prime-indexed tensor of non-closing Möbius-cylinder metric disks.`
- One disk per metric axis. Primitive axes anchored on primes:
  `P→2, K→3, Q→5, T→7, S→11, C→13, R→17, D→19, N→23, L→29, O→31,
  F→37, E→41, I→43`.
- Signed ternary axis state `s ∈ {-1, 0, +1}` plus magnitude
  `m ∈ [0, 1]`. `0` is neutral, not absent.
- Twist is an **ordinal seam**, not an angle value.
- Canonical state is `(twist_ordinal, phase, face/orientation)`, not
  `θ mod 360°` or `θ mod 720°`.
- Möbius face rule: `face_{n+1} = -face_n`.
- Grain hierarchy: `token → turn → round → session → archive`.

`edcmbone` currently implements:

- Scalar EDCM metric vector M_t (C, R, F, E, D, N, I, O, L, P, κ) in
  `backend/src/edcmbone/metrics/compute.py`.
- Behavioral metrics pipeline in `core/behavioral/behavioral_metrics.py`,
  optionally emitting `raw_counts.ucns_hits_by_metric` audit telemetry.
- UCNS-G v3 schema in `edcmbone/ucns_g/` (Python) and
  `frontend/src/ucns_g/types.ts` (TypeScript). **Schema only**; no
  scoring runtime consumes it yet.
- Local closed-token UCNS encoder in `closed_tokens.py`. This is a
  **measurement / encoding layer**, not a re-implementation of UCNS-A.

**None of these inherit proof status from UCNS-A's Theorem N or any
other `ucns` theorem layer.**

## 3. Required bridge artifacts (before any theorem transfer)

Any PR that attempts to transfer status from UCNS-A into UCNS-G / EDCM /
edcmbone must include **all** of the following:

### 3.1 Source-backed projection function

A documented function `π: UCNS-A → UCNS-G`, with:

- explicit input domain (cited against `ucns_recursive.canonical.UCNSObject`),
- explicit output codomain (cited against `edcmbone.ucns_g.MetricDiskState`
  and `GrainTensor`),
- worked examples for at least every `DEFENDED` / `ORACLE-COMPLETE`
  domain listed in §1 (depth-0, depth-1 restricted, depth-2 oracle),
- worked examples for at least one `TEST-BACKED` boundary (depth-2 full
  frozen domain) showing the projection's behavior on cases that are not
  yet `DEFENDED`.

A pseudocode sketch or English description is **not** sufficient. The
projection must be implemented and importable.

### 3.2 Reverse / recoverability limits

A documented statement of:

- whether `π` is injective on the cited input domain,
- whether `π` admits any partial inverse `π^{-1}: UCNS-G → UCNS-A` and
  on what domain,
- the **information loss** at each step (twist collapse, phase rounding,
  gauge ambiguity, sign quantization),
- whether known UCNS-A invariants (`n_dec`, `n_min`, face bits, payload
  recursion depth) are preserved, partially preserved, or destroyed by
  `π`.

If `π` is lossy, the PR must state: "Theorem N status is **not**
transferred across this projection because `π` is lossy on [list]."

### 3.3 Status labels per output

Every UCNS-G / EDCM / edcmbone output produced through `π` must carry an
explicit status label drawn from the existing vocabulary:

```text
DEFENDED          (only allowed if π is provably status-preserving)
IMPLEMENTED       code exists and is intended as authoritative implementation
TEST-BACKED       tests cover the projected behavior in a declared domain
ORACLE-COMPLETE   complete only under oracle/catalogue assumptions
FRONTIER          plausible or partially working, not complete
EXPERIMENTAL      exploration layer, not canon
```

Default label for a first bridge attempt is `EXPERIMENTAL`. Promotion
to any higher label requires its own PR with the artifacts in §3.1–3.4.

### 3.4 Tests comparing known UCNS-A objects to UCNS-G outputs

A new test file (suggested name:
`ucns_recursive/tests/test_ucns_g_bridge.py`) that:

- constructs known `UCNSObject`s from the existing depth-0 / depth-1 /
  depth-2-oracle catalogues,
- runs `π` on them,
- asserts the resulting `MetricDiskState` / `GrainTensor` shapes,
- pins the status label per output,
- includes at least one **negative** test: an `UCNSObject` from a
  `FRONTIER` domain that intentionally produces an `EXPERIMENTAL`
  UCNS-G output, demonstrating that the bridge does **not**
  silently upgrade status.

The tests must run under the existing `python -m unittest discover
ucns_recursive/tests/ -v` workflow.

## 4. Non-transfer rule (explicit)

Until **all** of §3.1–§3.4 are merged into `the-interdependency/ucns`
or `the-interdependency/edcmbone` and cited in a follow-up update to
`docs/ucns-shape-reconciliation.md`:

```text
Theorem N does NOT validate edcmbone, EDCM, or UCNS-G metric claims.
```

This rule applies to:

- the scalar EDCM metric vector in
  `edcmbone:backend/src/edcmbone/metrics/compute.py`,
- the behavioral metrics in
  `edcmbone:core/behavioral/behavioral_metrics.py`,
- the v3 schema in `edcmbone:edcmbone/ucns_g/`,
- the local closed-token encoder in `edcmbone:closed_tokens.py`,
- any `raw_counts.ucns_hits_by_metric` audit telemetry,
- any `a0` EDCM runtime that delegates to `edcmbone`,
- any `interdependent-lib` aggregate that exposes `edcmbone`.

PR descriptions touching any of those surfaces should state:

> No UCNS-A theorem/proof status is transferred to EDCM, edcmbone, or
> UCNS-G by this change.

## 5. Allowed now (without §3 artifacts)

Without any bridge in place, the following are explicitly allowed and
do not require any change to UCNS-A theorem status:

- `edcmbone` may emit UCNS-shaped audit telemetry (e.g.
  `raw_counts.ucns_hits_by_metric`) labeled `EXPERIMENTAL`.
- `edcmbone` may carry the UCNS-G v3 schema as a typed data structure
  with no scoring runtime attached.
- `a0` may delegate EDCM measurement primitives to `edcmbone` as long
  as it does not claim UCNS-A theorem support.
- `interdependent-lib` may list `edcmbone` as an optional dependency.
- Visualizations (e.g. `erinepshovel-code/UnitCircle`) may render UCNS-G
  metric disks on the unit circle and on Möbius-doubled outer surfaces.

None of the above is a bridge.

## 6. Forbidden now (without §3 artifacts)

The following are explicitly **not** allowed without the §3 artifacts
in place. Public docs (READMEs, CLAUDE.md, spec docs, release notes,
issue templates, PR descriptions, web copy) must not contain phrasings
equivalent to:

- "UCNS proves EDCM."
- "Theorem N proves EDCM metrics."
- "UCNS-G is proven."
- "EDCM is a UCNS-A factorization output."
- "SEQ-PRIME applies to EDCM transcripts."
- "edcmbone implements UCNS-A."

If such phrasing already exists in any repo, it should be patched in a
**claim-audit PR** (separate from any bridge construction PR) that
cites this checklist.

## 7. What this checklist does NOT do

- It does not construct the bridge.
- It does not modify `factor_search_v08`, `multiply`, or any other
  engine code.
- It does not change `docs/claims-ledger.md` status labels.
- It does not modify the PARALLEL verdict in
  `docs/ucns-shape-reconciliation.md`. That verdict remains the
  default until §3 artifacts exist and an explicit reconciliation PR
  updates it.
- It does not pre-authorize any specific projection design. Section 3
  is a gate, not a blueprint.

## 8. Hint for the bridge branch (if attempted)

A future bridge attempt would naturally live on its own branch in
`edcmbone` (suggested: `feat/ucns-g-edcmbone-bridge-experimental`), not
in `ucns`, since the construction depends on `edcmbone.ucns_g`. The
matching `ucns` work would be the tests in §3.4 and a follow-up update
to this checklist + `docs/ucns-shape-reconciliation.md`.

Default initial status for the bridge is `EXPERIMENTAL`. Promotion to
any other label requires its own PR.
