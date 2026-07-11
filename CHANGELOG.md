# Changelog

## Unreleased — v1.0 completion (codex-handoff workstreams 1–6)

### Solver
- `payload_system` now enumerates **every** catalogue-bounded payload
  assignment (`iter_payload_system_solutions`; deterministic, unit-first,
  structurally deduplicated, brute-force-equal on bounded oracles);
  `solve_payload_system` remains as a first-solution compatibility wrapper.
- `factor_search_v08` iterates every payload-system solution and every face
  option per host split and continues past every rejected candidate;
  `SEQ-PRIME` is reached only through demonstrable exhaustion. Permanent
  tower regression pins the greedy-era false negative.
### Certification
- New `ucns.catalogue_certificate`: machine-checked catalogue coverage
  (canonical-exact / canonical-superset / uncertified) bound to the exact
  catalogue fingerprint and `ORACLE_CATALOGUE_RULE_VERSION`.
- `factor_search_report` exposes exhaustion + pruning provenance;
  `factorization_result` certifies a negative only when domain, exhaustion,
  coverage, and coverage-preserving pruning all check out —
  `seq_prime_is_absolute` is now an exact alias of
  `negative_result_certified` and is never set from a domain label alone.
### Oracle class
- `is_oracle_atom` is now structural membership in the canonical generated
  catalogue (conservative v1.0 boundary); the geometric bounds are no longer
  an oracle certificate. Catalogue is immutable/copy-on-return with a stable
  rule version.
### Quotients
- `left_quotients` / `right_quotients` / `SolutionLimitExceeded` are public
  (`ucns` + `ucns_recursive`); singular `left_quotient` / `right_quotient`
  are reimplemented as deterministic selectors over the complete solution
  sets (retiring the greedy path and the right-quotient direction defect).
  `UCNSStore.left_factors`/`right_factors` surface every remainder
  (repeated keys documented), `is_left_factor` decides on the complete set,
  and `factor_decompose`/`enumerate_factorizations` consume all solutions.
### Object model
- `UCNSObject` is a recursively immutable canonical value: nonempty
  (empty construction rejected — the runtime carrier is the nonempty
  normalized object set), tuple storage, frozen attributes, strict
  constructor validation (booleans rejected as faces/carriers/angles,
  floats rejected as angles), constructor normalization with `normalize()`
  an idempotent no-op, copy/deepcopy returning `self`, and hash consistent
  with equality.
### Codec
- Versioned typed dictionary-key capsules: keys round-trip with exact type
  identity (bytes, str, int, bool, finite float, tuples thereof);
  `{1: …, "1": …, b"1": …}` coexist; unsupported/non-finite keys raise at
  encode; malformed/unknown capsules raise at decode; duplicate decoded keys
  raise instead of silently overwriting; legacy dictionaries still decode.
### Claims / licensing
- README, claims ledger, and module docstrings reconciled to the exact
  executable/catalogue/oracle/formal boundaries (exhaustion is evidence,
  not Lean proof; a green Lean build is type-checking only).
- All root-package/release metadata now states Apache-2.0 (`.zenodo.json`,
  `CLAUDE.md`); imported-artifact attribution notes corrected to name this
  repo's actual license.

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
