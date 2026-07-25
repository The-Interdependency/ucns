# Agent instructions

Read, in order:

1. `CANON.md`
2. `docs/UCNS_OPTION_DECISIONS.md`
3. `src/ucns/option_registry.json`
4. `docs/chapter-1.md`
5. `docs/STRUCTURE_CONTRACT.md`
6. `docs/CHOICE_PRESERVATION.md`
7. `docs/CHOICE_POLICY.md`
8. `docs/RETAINED_STRUCTURE.md`
9. `docs/COMPARISON_POLICY.md`
10. `docs/TRAVERSAL_POLICY.md`
11. `docs/LAYER_PAIRING.md`
12. `docs/EVALUATOR_LAB.md`
13. `docs/EXPERIMENT_MANIFESTS.md`
14. `docs/CANDIDATE_PACKS.md`
15. `.agents/skills/README.md`
16. the source module's `MODULE_BUILD` and `CONTRACTS` blocks
17. the corresponding test module's `CHECKS` block

Rules:

- Treat `UCNS` as a stable identifier without a canonical expansion.
- Treat every option-registry standing as authoritative. Do not appoint a global
  default or selected winner where the registry does not.
- Preserve the directed 720-degree lifted carrier and 360-degree visible
  projection as the current implemented candidate, not universal option canon.
- Do not promote Möbius, seam, hidden-zero, automatic orientation reversal, or
  one-circle-completion semantics as settled formal claims. Preserve the
  Möbius-origin/hidden-zero construction as `required-evaluation` until its
  exact relation to the directed-cover candidate is decided.
- Use EDCM experiments against real systems to support an EDCM-scoped option
  selection. Never transfer that selection into universal UCNS canon.
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
