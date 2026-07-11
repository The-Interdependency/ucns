# CLAUDE.md — UCNS: Unit Circle Number System

This file gives AI assistants context needed to work effectively in this repository.

---

## What This Repo Is

`ucns` (pip package: **`ucns`**) is a zero-dependency, pure-Python research
library implementing **Unit Circle Number System** sequence theory with a focus
on **recursive factorization**. Given a UCNS product object P, the engine
recovers factors A and B such that `A ⊠ B = P` via a witness-matrix recursive
quotient solver (`factor_search_v08`). The repo also carries mathematical
specs, a Lean 4 proof scaffold, empirical probe/sweep scripts, and an
experimental UCNS-native cache prototype.

<!-- BEGIN GENERATED:manifest -->
<!-- Generated from pyproject + repo tree by .agents/skills/manifest/generate.py — DO NOT EDIT BY HAND. Refresh with `python .agents/skills/manifest/generate.py --write`. -->

| Field | Value |
|---|---|
| Package | `ucns` |
| Version | `0.9.1` |
| Description | Unit Circle Number System recursive factorization engine |
| Status | 3 - Alpha |
| Python | >=3.8 (classifiers: 3.8, 3.10, 3.11, 3.12) |
| License | Apache-2.0 |
| Build backend | `setuptools.build_meta` |
| Author(s) | Erin Patrick Spencer <wayseer@interdependentway.org> |
| Repository | https://github.com/The-Interdependency/ucns |
| Runtime dependencies | none (stdlib only) |
| Optional extras | `dev` |
| Keywords | unit-circle, factorization, recursive-algebra, sequence-theory, witness-matrix |
| CI workflows | `carrier-lcm-target.yml`, `ci.yml`, `formal.yml`, `manifest-check.yml`, `python-package.yml` |
| Top-level directories | `audit/` · `code/` · `codex-handoff/` · `contracts/` · `docs/` · `examples/` · `formal/` · `pcea-ucns/` · `scripts/` · `tests/` · `ucns/` · `ucns_cache/` · `ucns_recursive/` |

<sub>Derived from `pyproject.toml` + the repo tree. Unknown fields surface as `hmmm` rather than a guess.</sub>
<!-- END GENERATED:manifest -->

> The block above is generated from `pyproject.toml` + the repo tree by the
> `manifest` living-spec tool (`.agents/skills/manifest/`) and gated in CI
> (`.github/workflows/manifest-check.yml`). Do not hand-edit between markers;
> run `python .agents/skills/manifest/generate.py --write` after changing
> version, dependencies, or layout.

---

## Package Surfaces

The repo ships three importable Python package surfaces:

- `ucns/` — **v1.0 public Python API.** Engine code lives here. New code imports
  from `ucns` and `ucns.a0_safe`.
- `ucns_cache/` — **EXPERIMENTAL UCNS-native cache prototype.** It derives
  canonical, payload-aware, and braider-structural cache keys for downstream
  A0 integration work. It is software-only and makes no speedup, hardware, or
  theorem-transfer claim.
- `ucns_recursive/` — **DEPRECATED for direct user imports** compatibility
  wrappers around `ucns.*`. No runtime `DeprecationWarning` is emitted; the
  deprecation is docs-only.

Packaging: `pyproject.toml` includes `ucns*` and `ucns_cache*`, so wheels carry
`ucns`, `ucns_recursive`, and `ucns_cache`. `import ucns` must not depend on the
compatibility shim.

---

## v1.0 Scope

UCNS v1.0 is a scoped, reproducible research release for
**catalogue-sufficient recursive factorization** (Theorem N), not a claim of
total general recursive primality. Carrier widening, tractable sub-catalogues,
and general recursive primality outside defended-complete domains are **out of
v1.0 scope**.

Status vocabulary: `DEFENDED`, `IMPLEMENTED`, `TEST-BACKED`,
`ORACLE-COMPLETE`, `FRONTIER`, `EXPERIMENTAL`.

| Layer | Status |
|---|---|
| Flat kernel algebra | `DEFENDED` |
| Depth-1 restricted completeness | `DEFENDED` |
| Depth-2 oracle (smallest class, Lemma 7) | `DEFENDED` + `ORACLE-COMPLETE` |
| Full frozen depth-2 domain | `IMPLEMENTED` + `TEST-BACKED` (not yet `DEFENDED` at spec level) |
| Depth-3 asymmetric (Theorem 9) | `TEST-BACKED` (6/6 empirical) |
| Catalogue-sufficient completeness — all depths (Theorem N) | `FRONTIER` — partially verified in Lean; remaining proof leaves under active discharge |
| Tractable sub-catalogues | `FRONTIER` |
| Carrier widening | `FRONTIER` / out of v1.0 scope |
| General recursive primality outside defended-complete domains | out of v1.0 scope |

Current release-status authority is `README.md` together with
`docs/claims-ledger.md`. The status snapshot at the top of `ucns-spec.md` is
dated 2026-05-17 and is historical wherever it differs from those current
release documents.

Frozen depth-2 domain scope:

```text
depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4
```

A0 rule: `SEQ-PRIME` is only absolute inside a defended-complete domain. Treat
`SEQ-PRIME` outside `VERIFIED_DOMAIN_LABELS` as non-absolute. Unit-group factors
are filtered before `SEQ-PRIME` is interpreted.

Formal proof non-transfer: `formal/` is a Lean 4 scaffold. A `sorry`-backed
statement proves nothing and confers no downstream `DEFENDED` status.

Cross-repo non-continuity: interoperability with `edcmbone`, `a0`, or
`interdependent-lib` is not theorem continuity. See
`docs/prime-quartet-discontinuity.md` and
`docs/edcm-edcmbone-bridge-checklist.md`.

---

## Repository Layout

```text
ucns/                              # v1.0 public API and engine implementation
  __init__.py                      # public exports
  a0_safe.py                       # A0-safe facade: identity, describe, canonical, factor
  canonical.py                     # UCNSObject, UNIT, multiply, is_unit
  domains.py                       # frozen D' domain + payload catalogue
  domain_status.py                 # status taxonomy + verified-domain labels
  factor_search_v08.py             # witness-matrix recursive quotient solver
  serialization.py                 # canonical JSON + stable hash
  store.py                         # UCNSStore keyed corpus + algebraic retrieval
  core.py, embedding.py, epicycle.py, mobius.py, similarity.py  # v0.6.5 lineage

ucns_cache/                        # experimental UCNS-native cache prototype
  entries.py                       # UCNSCacheKey/Entry, PrimitiveStreams, BraiderOutput
  dependencies.py                  # ucns availability / install boundary helpers
  primitive_streams.py             # angle / rotation / chirality stream derivation
  braider.py                       # deterministic event braid + lattice hash
  keys.py                          # canonical/payload/braider keys + factor reuse
  store.py                         # exact / structural / factor lookup store
  policy.py, instrumentation.py    # feature flag + lightweight metrics helpers

ucns_recursive/                    # deprecated compatibility wrappers + legacy tests
  tests/                           # engine compatibility suite

tests/                             # public API tests + cache prototype tests
formal/                            # Lean 4 scaffold; green build is type-check only
code/                              # exploratory read-only artifacts
scripts/bench_ucns_cache.py        # lightweight cache benchmark; no speedup claims
docs/ucns-native-caching.md        # cache prototype boundary, limits, phase plan
```

---

## Development Workflow

```bash
# Editable install with dev extras: build, twine, pytest
python -m pip install -e .[dev]

# Full test suite; this is what CI runs
python -m pytest ucns_recursive/tests tests -v

# Specific examples
python -m pytest ucns_recursive/tests/test_depth2_oracle.py -v
python -m pytest ucns_recursive/tests/test_depth2_full_domain.py -v
python -m pytest tests/test_ucns_cache_store.py -v

# Build + distribution validation
python -m build
python -m twine check dist/*
```

No `pytest.ini` or `[tool.pytest.ini_options]` is present; CI passes explicit
paths to pytest. No linter/formatter config is present, so there is no lint
command to run.

### CI

| Workflow | Trigger | What it does |
|---|---|---|
| `ci.yml` | push/PR touching `ucns/`, `ucns_recursive/`, `ucns_cache/`, `tests/`, `pyproject.toml` | Python 3.11; editable install with dev extras; runs `python -m pytest ucns_recursive/tests tests -v` |
| `python-package.yml` | push/PR to `main` | matrix 3.8/3.10/3.11/3.12; build; twine check; wheel import-boundary smoke test; same pytest suite |
| `manifest-check.yml` | push to `main` / all PRs | verifies generated CLAUDE manifest block has no drift |
| `formal.yml` | push/PR touching `formal/` | Lean build plus visible sorry-count; green means type-check, not proof |

---

## Deployable Surface

All public user-facing imports should come from `ucns` or `ucns.a0_safe`.

```python
from ucns import UCNSObject, UNIT, multiply, is_unit, factor_search_v08
from ucns import recursive_encode, recursive_decode, UCNSStore
from ucns import canonical_json, stable_hash, factorization_result, object_record
from ucns import a0_safe
```

`factor_search_v08` returns one valid factorization under loop ordering, or the
raw sentinel `"SEQ-PRIME"`. For A0-facing consumers, prefer the scoped envelope
from `ucns.a0_safe.factor(obj)` rather than surfacing raw sentinels.

For depth-3+ targets, extend the catalogue with the deep payloads of the
expected factors. Depth enters through catalogue selection, not through the
algorithm.

Pipeline: host recovery → payload system construction → witness-matrix global
consistency → face recovery → exact recomposition.

---

## Key Conventions & Gotchas

- Runtime stays stdlib-only. Do not add runtime dependencies.
- Dev tooling includes pytest. Because the project still advertises Python 3.8,
  keep pytest pinned below the first line that dropped 3.8 support unless the
  Python classifier and CI matrix are intentionally raised.
- `ucns_recursive` is deprecated for direct imports, but remains a supported
  compatibility path.
- `tests/test_public_import_boundary.py` protects the migration boundary and
  fails if importing `ucns` reaches for `ucns_recursive`.
- `ucns_cache` is experimental: no speedup claim, no hardware claim, no theorem
  transfer claim.
- `test_structural_hit_path` uses a stable shared-braid/distinct-identity
  fixture and should pass as part of the cache prototype suite.
- Read-only research artifacts: `ucns-code-v065.py`, `ucns_code_v065.py`,
  `code/`, and root `*_probe*.py` scripts.
- `formal/` proves nothing yet while `sorry` remains.
- Visualization/demo artifacts go under `examples/visualization/` with a README
  that states the claim illustrated and the non-proof boundary.

---

## What Does Not Exist Yet

- No linting/formatting config and no lint command.
- No runtime `DeprecationWarning` on `import ucns_recursive`.
- Right-quotient completeness proof remains asserted-by-symmetry.
- Discharged Lean proofs remain incomplete; `formal/` still has `sorry` leaves.
- Carrier widening / general recursive completeness remain out of v1.0 scope.

---

## Related Repos

| Repo | Role |
|------|------|
| The-Interdependency/interdependent-lib | Meta-package bundling ucns + other libs |
| erinepshovel-code/UnitCircle | Visualization / EML prime-distribution experiments |
| The-Interdependency/a0 | Agent platform that uses UCNS-derived encoding |

---

## Git Workflow

- Main branch: `main`
- Feature branches: `feat/<desc>`, `fix/<desc>`, `docs/<desc>`, `chore/<desc>`
- Commit style: Conventional Commits (`feat(ucns):`, `fix(factor):`, …)
- License: Apache-2.0

## Agent module-build doctrine

Before adding a new module, route, service, adapter, schema, worker, engine, UI
panel, migration, or experiment, read:

`./.agents/skills/meta-module-build/SKILL.md`.

Start new module work with a `MODULE_BUILD` block; mark unknown fields `hmmm`,
do not guess. When a module touches UCNS identity or factorization, prefer the
`ucns.a0_safe` boundary over raw sentinels.
