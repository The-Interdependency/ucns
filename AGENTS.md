# Agent instructions

Read, in order:

1. `CANON.md`
2. `docs/chapter-1.md`
3. `docs/STRUCTURE_CONTRACT.md`
4. `docs/CHOICE_PRESERVATION.md`
5. `docs/CHOICE_POLICY.md`
6. `docs/RETAINED_STRUCTURE.md`
7. `docs/COMPARISON_POLICY.md`
8. `docs/TRAVERSAL_POLICY.md`
9. `docs/LAYER_PAIRING.md`
10. `docs/EVALUATOR_LAB.md`
11. `docs/EXPERIMENT_MANIFESTS.md`
12. `docs/CANDIDATE_PACKS.md`
13. `.agents/skills/README.md`
14. the source module's `MODULE_BUILD` and `CONTRACTS` blocks
15. the corresponding test module's `CHECKS` block

Rules:

- Preserve the directed 720-degree lifted carrier and 360-degree visible
  projection.
- Do not reintroduce Möbius, seam, hidden-zero, automatic orientation reversal,
  or one-circle-completion semantics as formal carrier claims.
- Preserve the fail-closed cell zero-test: finite `mu = 0` only for a field-empty
  absent cell; finite `mu > 0` requires retained distinction.
- Treat aggregate support `W` as established only for the current cell carrier.
  Retained layers do not enter `W`, `M`, or `B` merely by existing.
- Distinguish represented evidence, candidate-measured evidence, and canonically
  measured evidence. Never report a candidate output as canonical measurement.
- Preserve every unresolved interpretation that has not been excluded by canon
  or invariant failure. Do not silently sort, deduplicate, flatten, merge,
  coerce, normalize, overwrite, or appoint defaults.
- Every lossy projection retains its source evidence and records information
  loss. Set and multiset views require caller-supplied identity keys.
- Retained layers append and may repeat names. Presence is explicit and not
  inferred from truthiness.
- Retained-layer composition requires an explicit occurrence-addressed
  `EnvelopePairPlan`. No unmatched-layer fallback is implicit. Result layers
  remain unmeasured.
- Every candidate comparison and law suite requires an explicit named
  `ComparisonPolicy`. Do not restore a hidden tolerance.
- Arbitrary research subjects require a named versioned `ContentAdapter`. Never
  hash `repr`, object identity, or arbitrary Python objects as universal
  evidence identity.
- Recursive evaluation requires caller-supplied identity, child enumeration,
  cycle policy, depth budget, and node budget. Truncation and repeated references
  produce receipts.
- Candidate identity records name, evaluator kind, version, code reference,
  scope, and policy dependencies. Do not infer stable identity from a callable.
- Witness corpora keep development and holdout partitions separate. Do not
  expose hidden holdout content merely to improve a candidate.
- Passing development fixtures is not evidence of generality. Use holdouts,
  generated mutations, metamorphic cases, adversarial cases, and minimized
  counterexamples.
- Candidate, witness, and decision authorship remain separately recorded.
- A candidate decision packet may become reviewable only with passing holdout
  evidence and rollback behavior. Reviewable does not mean canonical.
- Canonization requires a separate explicit decision recording the selected
  version, laws, witnesses, holdout custody, alternatives, information loss,
  rollback, and migration behavior.
- Do not create a complete `UCNSObject` until canonical structural equivalence,
  valid retained-layer-aware `M`, faithful `B`, typed dispatch, and their
  external evidence are explicitly constructed and ratified.
- Do not restore `ucns-Grok` wholesale or revive its rejected `M`, heuristic `B`,
  residual `m_contrib`, package version, EDCM claims, or discharged-status
  language.
- Do not restore archived arithmetic or theorem language by name similarity.
- Use `hmmm` for unresolved constraints; do not fill them with guessed certainty.
- Every behavior-bearing source module owns skill-lib `MODULE_BUILD` and
  `CONTRACTS` declarations. Every executable test owns resolving `CHECKS`.
- Run `python tools/verify_skill_lib_contracts.py .`, the complete test suite,
  build, and Twine checks before claiming `test-backed` status.
