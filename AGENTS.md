# Agent instructions

Read, in order:

1. `CANON.md`
2. `docs/chapter-1.md`
3. `docs/STRUCTURE_CONTRACT.md`
4. `docs/CHOICE_PRESERVATION.md`
5. `.agents/skills/README.md`
6. the source module's `MODULE_BUILD` and `CONTRACTS` blocks
7. the corresponding test module's `CHECKS` block

Rules:

- Preserve the directed 720-degree lifted carrier and 360-degree visible
  projection.
- Do not reintroduce Möbius, seam, hidden-zero, automatic orientation reversal,
  or one-circle-completion semantics as formal carrier claims.
- Preserve the fail-closed cell zero-test: finite `mu = 0` only for a field-empty
  absent cell; finite `mu > 0` requires retained distinction.
- Treat aggregate support `W` as established only for the current cell-only
  structure. Do not silently extend it to receipts, metadata, or recursion.
- Where multiple interpretations or representations remain admissible, preserve
  enough information to choose among them later. Do not silently sort,
  deduplicate, flatten, merge, coerce, or normalize away an unresolved option.
- Temporary choices must be explicit policies, strategies, lenses, modes, or
  projections. Defaults are conveniences, not canon.
- An option may be removed only by explicit canon, demonstrated invariant
  violation, proof of recoverability, or a scoped user choice whose information
  loss is recorded.
- Do not create a complete `UCNSObject` until receipts, metadata, recursion,
  canonical structural equivalence, a valid multiplicative `M`, and faithful `B`
  are explicitly constructed and tested.
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
