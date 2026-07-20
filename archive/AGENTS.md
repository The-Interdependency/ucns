# AGENTS.md

This file applies to the entire repository.

## Start here

Read `CLAUDE.md` before editing. It describes the package surfaces, repository
layout, theorem-status vocabulary, compatibility boundaries, and current proof
frontier.

For any new module, route, service, adapter, schema, worker, engine, UI panel,
migration, or experiment, first read:

```text
.agents/skills/meta-module-build/SKILL.md
```

Start that work with the required `MODULE_BUILD` block. Record unresolved fields
as `hmmm`; do not guess.

The vendored material under `.agents/skills/` follows the canonical
`The-Interdependency/skill-lib` source. Do not create an independent local fork
of a vendored skill. Re-sync canonical files verbatim and update any integrity
hashes required by the repository checks.

## Repository invariants

- The runtime package remains pure Python and standard-library-only. Do not add a
  runtime dependency without an explicit repository decision.
- Supported Python classifiers are 3.8, 3.10, 3.11, and 3.12.
- New public imports belong under `ucns` or `ucns.a0_safe`.
- `ucns_recursive` is a supported compatibility surface but is deprecated for
  direct new user imports.
- Importing `ucns` must not import `ucns_recursive`.
- Prefer `ucns.a0_safe` for integrations that consume UCNS identity or
  factorization results rather than exposing raw sentinels.
- Do not hand-edit the generated manifest block in `CLAUDE.md`.
- Treat `README.md` together with `docs/claims-ledger.md` as the current
  release-status authority wherever historical status text in `ucns-spec.md`
  differs.
- A green Lean build means declarations type-check. It does not prove any
  statement that still contains `sorry`, and it does not confer `DEFENDED`
  status downstream.
- Do not add a lint or formatter gate unless the repository intentionally adopts
  one; none is currently configured.

## Environment setup

```bash
python -m pip install -e '.[dev]'
```

For Lean work, use the toolchain pinned by `formal/lean-toolchain`. When `elan`
is installed:

```bash
source "$HOME/.elan/env"
cd formal
lake exe cache get
```

## Required validation

Run checks that cover every changed surface. The GitHub Actions workflows are
the authoritative definitions:

```text
.github/workflows/ci.yml
.github/workflows/python-package.yml
.github/workflows/manifest-check.yml
.github/workflows/formal.yml
.github/workflows/carrier-lcm-target.yml
```

### Python tests

For changes to Python packages, tests, packaging, or shared behavior:

```bash
python -m pytest ucns_recursive/tests tests -v
```

For focused iteration, run the narrowest relevant test first, then the complete
suite above before completion.

### Distribution validation

For packaging, public-import, metadata, or release-surface changes:

```bash
rm -rf build dist
python -m build
python -m twine check dist/*
```

Also reproduce the wheel-install and public-import-boundary smoke test from
`.github/workflows/python-package.yml` when those surfaces are affected.

For compatibility-sensitive changes, verify the supported Python matrix
(3.8, 3.10, 3.11, and 3.12) or rely on the corresponding GitHub Actions matrix
before making a compatibility claim.

### Generated manifest integrity

For changes to `pyproject.toml`, package metadata, dependencies, workflow names,
or repository layout:

```bash
(
  cd .agents/skills/manifest
  sha256sum -c generate.py.sha256
)
python .agents/skills/manifest/generate.py --root . --check
```

When the generated block legitimately needs refreshing:

```bash
python .agents/skills/manifest/generate.py --root . --write
python .agents/skills/manifest/generate.py --root . --check
```

### Lean validation

For changes under `formal/` or to formal-status documentation:

```bash
source "$HOME/.elan/env"
(
  cd formal
  lake exe cache get
  lake build
  lake build Ucns.CarrierLcm
)
```

Mirror the executable `admit`/`axiom` rejection and the targeted
`CarrierLcm.lean` `sorry` rejection from
`.github/workflows/carrier-lcm-target.yml`. Other explicitly documented frontier
`sorry` leaves may be reported, but never certified as proofs.

## Change discipline

- Keep changes focused and preserve existing public behavior unless the task
  explicitly changes it.
- Do not edit read-only research artifacts as though they were production
  sources. See `CLAUDE.md` for the current list.
- Add or update tests with behavior changes.
- Use Conventional Commit subjects such as `feat(ucns):`, `fix(factor):`,
  `test(cache):`, `docs:`, or `chore:`.
- Report exactly which validation commands ran and their outcomes. Distinguish a
  check that was not run from one that passed.
- Preserve unresolved constraints explicitly with `hmmm` rather than filling
  gaps with an unsupported assumption.
