# UCNS Repository Manifest

This repository currently contains:

## v1.0 canonical surfaces
- `ucns-spec.md` — **reconciled consolidated UCNS spec (status vocabulary 2026-05-17)**
- `ucns-theorem-n.md` — **Theorem N: catalogue-sufficient completeness (unified statement)**
- `docs/ucns-spec-status-addendum-2026-05-16.md` — status vocabulary + A0 `SEQ-PRIME` rule
- `ucns/` — v1.0 public Python API (re-exports the engine and the A0-safe facade)
- `ucns_recursive/` — engine implementation; **deprecated for direct user imports**

## Historical / supporting artifacts
- `ucns-spec-frontier-v090.md` — completeness frontier through v0.9.0 (partially superseded; cross-references the reconciled canon)
- `ucns-lemma8-depth3.md` — depth-3 factor search (SUPERSEDED by theorem-n; preserved as audit trail)
- `ucns-v06-completeness-proof.md`, `ucns-v06-left-quotient-completeness.md` — defended v0.6 proof artifacts
- `depth7-frontier.md` — depth-7 Fano/octonion frontier (conjectural; out of v1.0 scope)
- `ucns-code-v065.py` — stable defended code snapshot from the v0.6.5-based line
- `docs/pure-ucns-number-system.md`, `docs/coherence-primes-scarcity.md` — pure-UCNS layer notes

## Supplementary versioned artifacts
- `code/v080-coupled-witness-solver.py`
- `code/v080-recursive-factorization-refactor-plan.py`
- `code/v081-depth2-oracle-theorem.py`
- `code/v082-depth2-final-push.py`
- `code/v090-carrier-widening.py`
- `code/e109-depth2-failure-boundary.py`

These supplementary files preserve the historical theorem / refactor frontier for the recursive and widening attempts.

## Code sweeps (empirical verification)
- `code/sweeps/depth3_sweep.py` — depth-3 factorization sweep (CI verification script)
- `code/sweeps/depth3_sweep_t9_prework.py` — instrumented 16-case sweep, three catalogue sizes (Theorem 9 pre-work)
- `code/sweeps/t9_minimal_cat.py` — Theorem 9 minimal-catalogue verification; 6/6 asymmetric depth-3 SUCCESS in milliseconds

## Notes
- The top-level files are the current recommended entry points.
- The `code/` files are versioned historical artifacts and frontier notes.
- Later depth-2 and carrier-widening artifacts remain exploratory and are not merged into the stable engine snapshot.
- `ucns-theorem-n.md` supersedes Theorem 8c (vacuous, multiplicative-D’’=∅) and the prior ∀n induction plan.
