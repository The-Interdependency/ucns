# Repo-local skill-lib contract

Canonical source: `The-Interdependency/skill-lib`

Pinned source commit:
`fa6e6200bc274657de2334754bbbf98844ef6541`

Applied skills:

- `msdmd` — line-oriented self-declared metadata blocks and visible gaps;
- `meta-module-build` — source-owned `MODULE_BUILD` manifests before expansion;
- `test-build` — source-owned `CONTRACTS`, test-owned `CHECKS`, and no-exec graph
  reconciliation;
- `canon` and `domain-claims` — formal terms must state scope, exclusions, and
  standing before they become control surfaces;
- `interdependent-work-graph` — the UCNS and skill-lib commits and authority
  roles are pinned in `STACK_MANIFEST.json`.

The repository currently consumes the pinned doctrine through exact commit
identity and enforces its operative block contracts with
`tools/verify_skill_lib_contracts.py`.

hmmm: verbatim repo-local vendoring or a gitlink materialization of the pinned
skill directories remains a separate supply-chain step; this build does not
pretend the local bounded checker is the canonical universal parser.
