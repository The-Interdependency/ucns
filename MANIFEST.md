# UCNS Repository Manifest

This repository currently contains:

## v1.0 canonical surfaces
- `ucns/public_gonol.py` — **canonical public 157-gonal and fixed SPACE/ZERO Möbius twist origin**
- `formal/Ucns/PublicGonol.lean` — origin/orientation model: one 360-degree circuit flips orientation; complete return requires 720 degrees
- `docs/public-gonol.md` — ownership, behavior, migration, and non-flattening boundary
- `docs/pure-ucns-number-system.md` — three-surface ontology: public frame, normalized factorization subsystem, absent bridge
- `ucns-spec.md` — reconciled specification with public-frame canon and internally scoped factorization layers
- `ucns-theorem-n.md` — **FRONTIER** catalogue-sufficient factorization proof target for the normalized subsystem
- `docs/ucns-spec-status-addendum-2026-05-16.md` — status vocabulary + A0 `SEQ-PRIME` rule
- `ucns/` — v1.0 public Python API
- `ucns_recursive/` — compatibility wrappers; **deprecated for direct user imports**

## Historical / supporting artifacts
- `ucns-spec-frontier-v090.md` — normalized-factorization frontier through v0.9.0, partially superseded and explicitly separated from the public frame
- `ucns-lemma8-depth3.md` — depth-3 factor-search artifact (SUPERSEDED by the current Theorem N frontier statement; preserved as audit trail)
- `ucns-v06-completeness-proof.md`, `ucns-v06-left-quotient-completeness.md` — historical v0.6 proof artifacts with current scope corrections
- `depth7-frontier.md` — depth-7 Fano/octonion analogy boundary; conjectural and out of v1.0 scope
- `ucns-code-v065.py` — stable historical code snapshot from the v0.6.5-based line
- `docs/coherence-primes-scarcity.md` — exploratory layer note

## Supplementary versioned artifacts
- `code/v080-coupled-witness-solver.py`
- `code/v080-recursive-factorization-refactor-plan.py`
- `code/v081-depth2-oracle-theorem.py`
- `code/v082-depth2-final-push.py`
- `code/v090-carrier-widening.py`
- `code/e109-depth2-failure-boundary.py`

These supplementary files preserve historical theorem, refactor, and widening attempts. They are not public-gonol canon and do not widen the current theorem status.

## Code sweeps
- `code/sweeps/depth3_sweep.py` — depth-3 factorization experiment script
- `code/sweeps/depth3_sweep_t9_prework.py` — instrumented historical sweep configuration
- `code/sweeps/t9_minimal_cat.py` — minimal-catalogue asymmetric depth-3 experiment

Execution counts or success rates from sweep source are not current evidence unless tied to an immutable run artifact. These scripts are `TEST-BACKED` only to the extent established by cited CI or committed reports.

## Notes
- The public gonol is the system frame; the normalized recursive algebra is an internal subsystem.
- The public-gonol ↔ normalized-factorization bridge remains `hmmm`.
- Theorem N remains `FRONTIER`; its Lean completeness statements are `sorry`-backed.
- Carrier-LCM is proved for the internal projected `n_min`, not for the complete twist-bearing public carrier.
- No downstream measurement, embedding, cryptographic, PTCA, Fano, or octonion claim inherits proof status from the public frame or internal factorization subsystem.
