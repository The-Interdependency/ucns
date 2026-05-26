GPT generated; context, prompt Erin Spencer

# UCNS Spec Status Addendum — 2026-05-16

## hmm

This addendum records a status reconciliation without rewriting `ucns-spec.md` directly.

Reason: the current repository contains two canon surfaces with different claims about the full frozen depth-2 domain:

1. `CLAUDE.md` states that the full frozen depth-2 domain is implemented in `factor_search_v08`.
2. `ucns-spec.md` still states that the full frozen depth-2 domain is not solved.

Both statements may be true under different meanings of "solved":

```text
implemented/test-backed != proof-defended
```

The safe reconciliation is therefore not to erase the older frontier language, but to separate statuses explicitly.

## Status Vocabulary

Use these terms going forward:

```text
DEFENDED          written proof or proof-defended theorem layer
IMPLEMENTED       code exists and is intended as authoritative implementation
TEST-BACKED       tests cover the claimed behavior in the declared domain
ORACLE-COMPLETE   complete only under oracle/catalogue assumptions
FRONTIER          plausible or partially working, not complete
EXPERIMENTAL      exploration layer, not canon
```

## Reconciled Depth-2 Status

Recommended wording:

```text
Full frozen depth-2 domain:
  implementation status: IMPLEMENTED in factor_search_v08
  test status: TEST-BACKED to the extent covered by ucns_recursive/tests
  proof status: not yet DEFENDED in the formal spec
  carrier-widening status: FRONTIER
```

## A0 Rule

A0 may consume depth-2 factorization outputs only with explicit domain-status metadata. It must not treat `SEQ-PRIME` outside a defended-complete domain as absolute primality.

## Next Canon Repair

**Status: completed 2026-05-17** on branch
`claude/ucns-v1-canon-reconciliation-ELOzV`.

`ucns-spec.md` has been patched to replace binary solved/not-solved
language with the status vocabulary in this addendum.
`ucns-spec-frontier-v090.md` has been marked partially superseded and
cross-references the reconciled canon. `README.md`, `CLAUDE.md`, and
`CHANGELOG.md` have been updated to match.

The reconciled v1.0 canon also:

- declares `ucns` the v1.0 public Python API,
- declares `ucns_recursive` deprecated for direct user imports but
  retained as a compatibility surface (no runtime warning yet — the
  release ships from a local termux build at the maintainer's cadence),
- declares carrier widening, tractable sub-catalogues, and general
  primality outside defended-complete domains **out of v1.0 scope**.

## hmmm
