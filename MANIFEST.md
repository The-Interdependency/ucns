# UCNS Repository Manifest

This repository currently contains:

## Top-level current artifacts
- `ucns-theorem-n.md` — **Theorem N: catalogue-sufficient completeness (unified statement)**
- `ucns-lemma8-depth3.md` — depth-3 factor search (SUPERSEDED by theorem-n; preserved as audit trail)
- `ucns-spec-frontier-v090.md` — completeness frontier through v0.9.0
- `ucns-code-v065.py` — stable defended code snapshot from the v0.6.5-based line

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
