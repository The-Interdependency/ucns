# EDCM/edcmbone Bridge Checklist (UCNS-A ↔ UCNS-G)

**Status:** Planning checklist only. No theorem transfer.
**Date pinned:** 2026-05-22

## 0) Linked firewall and scope anchors

This checklist inherits the existing UCNS-A/UCNS-G firewall from:

- `docs/ucns-shape-reconciliation.md` (PARALLEL verdict + firewall rule)
- `docs/ucns-g-prime-cylinder-supplement.md` (UCNS-G side refinement only;
  no theorem transfer)

## 1) What UCNS-A currently proves / implements

UCNS-A in this repository is the recursive factorization algebra implemented by
`UCNSObject`/`multiply` with `factor_search_v08` as the v1.0 factorization
engine.

Current theorem scope and status are documented in:

- `ucns-theorem-n.md` (catalogue-sufficient completeness claim scope)
- `ucns-spec.md` and `docs/ucns-spec-status-addendum-2026-05-16.md`
- `docs/ucns-shape-reconciliation.md` and
  `docs/ucns-g-prime-cylinder-supplement.md`

This checklist does not alter engine code, theorem text, or defended-domain
status labels.

## 2) What UCNS-G / EDCM / edcmbone currently measures

UCNS-G (as currently pinned in the cross-repo handoffs referenced by
`docs/ucns-g-prime-cylinder-supplement.md`) is the EDCM-side metric geometry
framing. It is described as a prime-indexed tensor of metric disks with
session-grain structure and typed state conventions.

`edcmbone` is the structural measurement package on that side. Its emitted
metrics/telemetry are measurement outputs, not UCNS-A theorem objects.

## 3) Required bridge artifacts before any theorem transfer

Before any claim that UCNS-A theorem status supports UCNS-G/EDCM outputs, all
of the following artifacts must exist with source-backed tests:

1. **Projection function (source-backed):**
   A concrete, versioned mapping from explicit UCNS-A source objects to UCNS-G
   metric-disk tensor outputs.
2. **Reverse/recoverability limits:**
   Written limits describing what can and cannot be recovered from UCNS-G
   outputs back to UCNS-A objects.
3. **Per-output status labels:**
   Bridge outputs must carry explicit labels (for example, `EXPERIMENTAL`,
   `IMPLEMENTED`, `DEFENDED`) with the same discipline used in UCNS docs.
4. **Comparative test suite:**
   Tests that compare known UCNS-A objects against produced UCNS-G metric-disk
   outputs and pin expected behavior.

Until these artifacts are implemented and verified, theorem transfer is not
allowed.

## 4) Explicit non-transfer rule

**Theorem N does not validate edcmbone/EDCM metric claims.**

UCNS-A theorem/proof status remains scoped to UCNS-A algebra/factorization
claims unless a future bridge satisfies the checklist above.

## 5) Allowed now

`edcmbone` may emit UCNS-style telemetry as **EXPERIMENTAL audit output**.

## 6) Forbidden now

Public docs and release messaging must not claim that UCNS theorem results
already prove EDCM/edcmbone metric correctness or UCNS-G geometry correctness.

## hmmm

hmmm is the mandatory boundary object that records unresolved constraint,
preserves honest incompletion, and marks the transition between delivered
output and living continuation.
