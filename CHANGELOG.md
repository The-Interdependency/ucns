# Changelog

## Unreleased — stack repair (Theorem N alignment, bridge, evidence)

### Theorem and formal alignment
- Rewrote the Theorem N documentation (`ucns-theorem-n.md`, README, claims
  ledger) around **exhaustive inclusion**: the target is finding **a** valid
  nontrivial factorization via a finite enumeration that provably includes
  the true candidate at every stage. Removed wording implying general
  cancellativity, quotient uniqueness, or recovery of the original factor
  pair. Theorem N remains `FRONTIER`.
- Replaced the opaque `FindsFactorization` / `ContainsPayloads` predicates
  in `formal/Ucns/TheoremN.lean` with a defined finite-search model:
  catalogue normalization with one unit sentinel, split candidates
  (`p = 2..n` then `1`), structural host-angle recovery, exhaustive payload
  and face assignments, executable unit-group rejection, and an
  exact-recomposition success relation whose witness carries actual factors.
  The completeness theorems remain `sorry`-closed; every remaining hole and
  declared modeling boundary is enumerated in `audit/obligation_ledger.md`.
- Added a shared Python/Lean conformance fixture
  (`tests/test_formal_conformance.py`): the literal Python transcription of
  the Lean model enumerates exactly the executable solver's accepted
  witness space on the declared small-domain fixture.

### Constructor invariants
- `UCNSObject` construction now rejects empty `A_plus`/`F_plus` sequences,
  non-positive or non-integral `n_dec`, non-positive supplied `n_min`, and
  non-UCNS payload types (`TypeError`), in addition to the existing
  parallel-length and face-bit validation. Adversarial constructor tests
  added to both the public and compatibility suites; the empty-carrier
  contract now pins construction-time rejection.

### Cross-repository bridge and downstream evidence
- Added `ucns.bridge`: the official versioned neutral record
  (`ucns-bridge-record` v1) with fail-closed `import_bridge_record` /
  `export_bridge_record`. Imports produce actual `UCNSObject`s; round trips
  preserve UCNS equality and stable hash; external provenance/canon tags
  survive round trips without entering UCNS equality.
- Added `ucns.evidence`: a non-boolean `UCNSEvidence` envelope
  distinguishing construction success, finite-search exhaustion, validated
  catalogue coverage, certified domain-relative negatives, theorem-layer
  status vocabulary, and explicit absence of proof status.
- Added the shared UCNS/METAPAT/EDCM contract suite
  (`tests/test_stack_contract_suite.py`) with canonical fixtures owned by
  this repo (`tests/fixtures/ucns_stack_contract_fixtures.json`), covering
  bridge representation, round-trip identity, provenance preservation,
  EDCM geometry construction from actual objects, `NA != 0` at the EDCM
  boundary, no theorem-status transfer into measurement output, fail-closed
  rejection, and canon-digest visibility.
- Added regressions proving bridge metadata cannot forge or promote
  negative certification (`tests/test_bridge_certification_boundary.py`);
  the raw solver stays catalogue-relative and the evidence-bearing envelope
  remains the only negative-certification surface.

## Unreleased — base geometry completion

### Base geometry (operation algebra of ⊠)
- Landed the structure theorem: `(nonempty normalized objects, multiply, e)`
  is a **length-graded, non-commutative, non-cancellative monoid** with unit
  group ≅ ℤ/2 and center exactly the unit towers (`docs/base-geometry.md`).
- **Associativity proven** (O3): the object carries its full angle sequence;
  the circular-mean collapse exists only in the `geometry_bridge`
  projection. First triples-level test coverage (prior evidence was
  pairs-only).
- Identity proven two-sided (O2); commutativity ruling landed (O4): the
  geometric projection always commutes, the commutator lives in sequence
  ordering — not chirality — and the center is the unit towers.
- **Division theory** (O5): forced-host lemma, solvability criterion,
  finite-fiber multiplicity theorem (`T_d ⊠ x = T_d` has exactly `d`
  solutions), the cancellativity dichotomy (a divisor cancels iff some
  top-level payload is the unit; flat divisors are the special case), and
  complete left/right quotient solution-set enumerators in
  `ucns/division_theory.py` (exhaustively cross-checked on a closed
  78-object universe).
- **Scope correction:** the v0.6 Left-Quotient Completeness theorem is false
  as written (its E10.4 cancellativity premise fails at depth ≥ 2);
  `left_quotient` is sound always and complete for flat divisors;
  `right_quotient` additionally used the left payload helper and misses
  more. Banners added to both v0.6 proof documents; claims ledger updated;
  permanent counterexample regression added.
- Addition boundary ruled (O7): ⊠ is the sole primitive; derived top-level
  concatenation is associative and right-distributive over ⊠ but fails left
  distributivity, so it earns no primitive status.
- New `contracts/` suite: one CONTRACTS witness per obligation (declared in
  `ucns/canonical.py` / `ucns/division_theory.py`), each with a
  mutation-catch check; `audit/obligation_ledger.md` + `audit/reconcile.py`
  reconcile obligations ↔ witnesses ↔ RepoLOTO state without imports;
  CI runs the aggregates via `tests/test_base_geometry_contracts.py`.

## Unreleased — v1.0 canon reconciliation

### Canon
- Reconciled `ucns-spec.md` to use the status vocabulary (`DEFENDED`, `IMPLEMENTED`, `TEST-BACKED`, `ORACLE-COMPLETE`, `FRONTIER`, `EXPERIMENTAL`) from the 2026-05-16 addendum.
- Replaced binary solved / not-solved language in §F1–F4 with explicit per-layer status.
- Reconciled Theorem N public language to `FRONTIER`: implementation-backed proof sketch, Lean proof pending, awaiting external formal review. Depth-3 asymmetric remains `TEST-BACKED`.
- `ucns-spec-frontier-v090.md` cross-references the reconciled canon and is marked partially superseded for depth-2 implementation status.
- 2026-05-16 addendum's "Next Canon Repair" section marked completed.

### v1.0 scope
- Declared `ucns` the v1.0 public Python API; `ucns_recursive` is retained as a compatibility import path but **deprecated for direct user imports**.
- Declared carrier widening, tractable sub-catalogues, and general recursive primality outside defended-complete domains **out of v1.0 scope**.
- Kept Theorem N out of `DEFENDED` release language until Lean `sorry` leaves and external formal review are discharged.

### Docs
- README, `CLAUDE.md`, and example snippets switched to `from ucns import ...`; status table aligned with the vocabulary.
- A0 rule on `SEQ-PRIME` outside `VERIFIED_DOMAIN_LABELS` documented at the README, spec, and `CLAUDE.md` level.
- Added `docs/claims-ledger.md`, `docs/mathematical-glossary.md`, `docs/reproducibility.md`, and `RELEASE.md` for reviewer-facing v1.0 preparation.
- Glossary now records the multiplicative-unit boundary: unit-group factors are filtered before `SEQ-PRIME` is interpreted.
- Current release-prep branch reconciles README, `ucns-theorem-n.md`, `docs/claims-ledger.md`, and this changelog to conservative Theorem N language.

### Examples
- Added minimal reviewer examples under `examples/depth_examples/` covering depth-1, depth-2 oracle, depth-3 catalogue-sufficient, and catalogue-boundary behavior.

### Tests / metadata
- Tightened `test_depth2_full_domain.py` docstring; no longer claims exhaustive enumeration over the frozen domain.
- Added constructor invariant tests for `A_plus` / `F_plus` length and binary face-bit validation on both `ucns_recursive` and public `ucns` import surfaces.
- Aligned `pyproject.toml` Python classifiers with the CI matrix.
- Retained the factorization envelope test canon from the multiplicative-unit fix: the flat length-2 object is a defended-domain `SEQ-PRIME` example after unit-group factors are filtered.
- Began replacing stale `MODULE_BUILD tests:` paths with real test files used by the current pytest surface.

## v0.8.1 — PyPI Release Candidate

### Packaging
- Added enriched PyPI metadata and classifiers.
- Added project URLs and author metadata.
- Added build + twine validation workflow.
- Added wheel build dependency.

### CI
- GitHub Actions workflow now:
  - builds the package
  - validates metadata via twine
  - installs built wheel artifact
  - runs the UCNS test suite

### Status
UCNS remains an experimental/research-stage algebraic system.
The repository currently defends:
- flat kernel algebra
- depth-1 restricted completeness
- depth-2 oracle completeness

Catalogue-sufficient completeness (Theorem N) is the current implementation-backed frontier proof target, not a fully discharged formal theorem.

### Compatibility
Test target:
- Python 3.8+

### Notes
This release is intended first for TestPyPI validation before public PyPI publication.

GPT generated; context, prompt Erin Spencer.
