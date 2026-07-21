# Repo-local skill-lib materialization

Canonical source: `The-Interdependency/skill-lib`

Pinned source commit:
`fa6e6200bc274657de2334754bbbf98844ef6541`

Vendored verbatim:

- `msdmd/`
- `meta-module-build/`
- `test-build/`
- `canon/`
- `domain-claims/`
- `interdependent-work-graph/`
- shared `doctrine/` required by those skills

Repo-local additions are allowed beside the canonical assets. UCNS adds
`tools/verify_skill_lib_contracts.py` as its bounded executable evidence
reconciler; it does not replace or modify the canonical skill files.

Drift gate:

```text
python <skill-lib>/tools/check_consumer_drift.py . \
  --canon-root <skill-lib> \
  --sha fa6e6200bc274657de2334754bbbf98844ef6541 \
  --strict-sha --require-vendored
```

hmmm: future skill-lib updates require an explicit new pinned commit and
a fresh drift-clean materialization; no floating update is authorized.
