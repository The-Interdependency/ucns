# Repo-local skill-lib materialization

Canonical source: `The-Interdependency/skill-lib`

Pinned source commit:
`289d4959f7920efc214f180cca3443d8090f4095`

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
  --sha 289d4959f7920efc214f180cca3443d8090f4095 \
  --strict-sha --require-vendored
```

hmmm: future skill-lib updates require an explicit new pinned commit and
a fresh drift-clean materialization; no floating update is authorized.
