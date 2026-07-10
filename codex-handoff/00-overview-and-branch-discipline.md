# UCNS v1.0 completion handoff for Codex

**Repository:** `The-Interdependency/ucns`  
**Prepared:** 2026-07-10  
**Published branch:** `codex-handoff`  
**Observed `main`:** `16fcdce05b24a0d90633ef106740ab85fdb0ece4`  
**Integrated prerequisite:** PR #96, `feat(base-geometry): complete O1–O7 — structure theorem, division theory, contracts`, merged into `main` at `16fcdce05b24a0d90633ef106740ab85fdb0ece4`  
**PR #96 final observed head:** `777ba653f7381280dcbb8dd204ce293384243c19`

## Mission

Take ownership of the first six v1.0 release-completion steps and execute them to completion. Do not stop after writing a plan or after making the first failing regression pass. Inspect the repository, implement the work, run focused and complete validation, diagnose every failure, repair it, and repeat until every acceptance condition below is satisfied.

The six workstreams are:

1. Exhaustive payload assignment and factor-search backtracking.
2. Machine-checkable negative-result certification.
3. Exact equivalence between oracle classification and oracle catalogue membership.
4. Migration of quotient consumers to complete solution-set APIs.
5. A nonempty, immutable, stably hashable `UCNSObject` value model.
6. Collision-safe dictionary-key coding, reconciled claims, and consistent license metadata.

A returned factorization must remain unconditionally sound: every accepted `(A, B)` must satisfy `multiply(A, B) == P`. A negative result must never be presented as certified merely because the target has a recognized domain label.

---

## Start state and branch discipline

First read, in this order:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `.agents/skills/msdmd/SKILL.md`
4. `.agents/skills/meta-module-build/SKILL.md`
5. `README.md`
6. `docs/claims-ledger.md`
7. PR #96 and its changed files

The repository-local `.agents/skills/` material is the actionable skills authority. `AGENTS.md` names the canonical upstream as `The-Interdependency/skill-lib` (singular). Do not invent a parallel local skill dialect.

This handoff is published on the implementation branch `codex-handoff`, created from `main` after PR #96 merged. Use that branch as the working branch; do not create a second implementation branch unless repository policy or an unavoidable integration conflict requires one.

Before editing, verify and synchronize the checkout:

```bash
git fetch origin main codex-handoff
git switch codex-handoff
git pull --ff-only origin codex-handoff
git merge-base --is-ancestor 16fcdce05b24a0d90633ef106740ab85fdb0ece4 HEAD
git rev-parse HEAD
```

If `main` has advanced materially, inspect the intervening commits before integrating them. Preserve the merged PR #96 implementation, especially `ucns/division_theory.py` and its contracts; do not recreate or fork that work. Keep all completion commits on `codex-handoff`, push after each coherent workstream, and leave the branch in a reviewable state after every push.

Use focused Conventional Commit subjects. A suitable sequence is:

```text
fix(factor): exhaust catalogue-bounded payload assignments
feat(result): certify negative factorization results
fix(domain): align oracle classification with catalogue membership
fix(quotient): migrate consumers to complete solution sets
refactor(canonical): enforce immutable nonempty objects
fix(codec): preserve dictionary key identity
docs: reconcile UCNS claims and license metadata
```

Do not add runtime dependencies. Preserve Python 3.8 compatibility. Do not introduce a formatter or lint gate. New public imports belong under `ucns` or `ucns.a0_safe`; `ucns_recursive` remains a supported compatibility surface, and importing `ucns` must never import `ucns_recursive`.

For every new module or schema, add the required module-local `MODULE_BUILD` declaration before implementation. Include the PR-body file plan required by `meta-module-build`:

```text
path
created_or_modified
purpose
risk
required_tests
```

Unknown external facts must be written as `hmmm`; implementation choices required by this handoff are not unknown and must not be deferred.

---
