# UCNS skill-lib boundary runner

**Status:** test-backed executable evidence boundary; no UCNS selection, EDCM activation, or canon effect.

`tools/run_skill_lib_boundaries.py` extends the existing no-exec contract graph audit into a bounded executor for declarations governed by the vendored `msdmd` and `test-build` skills.

The runner:

1. requires the complete `MODULE_BUILD` / `CONTRACTS` / `CHECKS` audit to close before execution;
2. resolves only audited `self::test_*` calls;
3. starts one isolated pytest process group per declared check;
4. consumes declared host capabilities and positive per-check timeouts;
5. records `PASS`, assertion `FAIL`, harness `ERROR`, and `TIMEOUT` separately while continuing after individual failures;
6. binds contract ids, command, requirements, mutation and cleanup declarations, outcome, bounded output excerpts, complete output digests, and a receipt digest;
7. refuses to promote a passing run into UCNS selection, EDCM activation, or canon status.

Run all declared boundaries:

```text
uv run --extra test python tools/run_skill_lib_boundaries.py . \
  --receipt generated/skill-lib-boundary-run-receipt.json
```

Run selected check ids by repeating `--check`:

```text
uv run --extra test python tools/run_skill_lib_boundaries.py . \
  --check check_explicit_comparison_policies \
  --check check_comparison_registry_choices
```

Selected-id mode still audits the complete repository first. Missing capabilities are evidence-bearing `ERROR` outcomes, not skips. A timeout kills the spawned process group. Output excerpts are capped while full output byte counts and SHA-256 digests remain in the receipt.

The boundary is intentionally limited to the repository's current Python/pytest `self::` call scheme. Mutation verification and additional executable call schemes remain `hmmm`; neither may be inferred from a passing receipt.
