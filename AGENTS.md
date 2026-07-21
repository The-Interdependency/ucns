# Agent instructions

Read, in order:

1. `CANON.md`
2. `docs/chapter-1.md`
3. `docs/STRUCTURE_CONTRACT.md`
4. `docs/CHOICE_PRESERVATION.md`
5. `docs/CHOICE_POLICY.md`
6. `docs/RETAINED_STRUCTURE.md`
7. `docs/EVALUATOR_LAB.md`
8. `.agents/skills/README.md`
9. the source module's `MODULE_BUILD` and `CONTRACTS` blocks
10. the corresponding test module's `CHECKS` block

Rules:

- Preserve the directed 720-degree lifted carrier and 360-degree visible
  projection.
- Do not reintroduce Möbius, seam, hidden-zero, automatic orientation reversal,
  or one-circle-completion semantics as formal carrier claims.
- Preserve the fail-closed cell zero-test: finite `mu = 0` only for a field-empty
  absent cell; finite `mu > 0` requires retained distinction.
- Treat aggregate support `W` as established only for the current cell carrier.
  Retained receipts, metadata, relations, recursion, provenance, and state do not
  enter `W` merely by existing.
- Where multiple interpretations or representations remain admissible, preserve
  enough information to choose among them later. Do not silently sort,
  deduplicate, flatten, merge, coerce, normalize, or overwrite an unresolved
  option.
- Temporary choices must be explicit `StructurePolicy` values or equivalent
  named projections. Policies remain independently addressable; no default
  policy gains canonical standing.
- Every lossy projection must retain its source evidence and record information
  loss. Set and multiset views require caller-supplied identity keys.
- Retained layers append and may repeat names. Never overwrite an earlier layer
  occurrence by convenience. Presence is explicit and not inferred from
  truthiness.
- Layer contribution status must remain explicit: `measured`, `unmeasured`, or
  `excluded` with a scoped note. The envelope does not calculate canonical `M`
  or `B`.
- Equivalence, product-character, and faithful-breadth proposals belong in the
  evaluator laboratory as named `EvaluatorCandidate` values. Register multiple
  candidates, run declared law suites, retain witnesses and disagreements, and
  do not add a default, best, majority, or automatic promotion path.
- Candidate canonization requires a separate explicit decision recording the
  selected version, laws, witnesses, alternatives, information loss, and
  rollback behavior.
- An option may be removed only by explicit canon, demonstrated invariant
  violation, proof of recoverability, or a scoped user choice whose information
  loss is recorded.
- Do not create a complete `UCNSObject` until canonical structural equivalence,
  a valid multiplicative `M`, faithful `B`, retained-layer measurement laws, and
  typed dispatch are explicitly constructed and tested.
- Do not restore `ucns-Grok` wholesale. Its cell/`W`/pair/prune/collapse material
  has been selectively reconstructed; its current `M`, heuristic `B`, residual
  `m_contrib`, package version, EDCM claims, and discharged-status language are
  rejected.
- Do not restore archived arithmetic or theorem language by name similarity.
- Use `hmmm` for unresolved constraints; do not fill them with guessed certainty.
- Every behavior-bearing source module must own skill-lib `MODULE_BUILD` and
  `CONTRACTS` declarations. Every executable test must own a resolving `CHECKS`
  declaration.
- Run `python tools/verify_skill_lib_contracts.py .` and the complete test suite
  before claiming `test-backed` status.
