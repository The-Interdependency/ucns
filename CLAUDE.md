# CLAUDE.md — UCNS: Unit Circle Number System

This file gives AI assistants context needed to work effectively in this repository.

---

## What This Repo Is

`ucns` (pip package: **`ucns`**) is a zero-dependency, pure-Python research
library implementing **Unit Circle Number System** sequence theory with a
focus on **recursive factorization**. Given a UCNS product object P, the
engine recovers factors A and B such that `A ⊠ B = P` via a witness-matrix
recursive quotient solver (`factor_search_v08`). The repo also carries the
mathematical specs, completeness proofs, a Lean 4 proof scaffold, and a set
of empirical probe/sweep scripts.

<!-- BEGIN GENERATED:manifest -->
<!-- Generated from pyproject + repo tree by .agents/skills/manifest/generate.py — DO NOT EDIT BY HAND. Refresh with `python .agents/skills/manifest/generate.py --write`. -->

| Field | Value |
|---|---|
| Package | `ucns` |
| Version | `0.9.1` |
| Description | Unit Circle Number System recursive factorization engine |
| Status | 3 - Alpha |
| Python | >=3.8 (classifiers: 3.8, 3.10, 3.11, 3.12) |
| License | MPL-2.0 |
| Build backend | `setuptools.build_meta` |
| Author(s) | Erin Patrick Spencer <wayseer@interdependentway.org> |
| Repository | https://github.com/The-Interdependency/ucns |
| Runtime dependencies | none (stdlib only) |
| Optional extras | `dev` |
| Keywords | unit-circle, factorization, recursive-algebra, sequence-theory, witness-matrix |
| CI workflows | `ci.yml`, `formal.yml`, `manifest-check.yml`, `python-package.yml` |
| Top-level directories | `code/` · `docs/` · `examples/` · `formal/` · `pcea-ucns/` · `tests/` · `ucns/` · `ucns_recursive/` |

<sub>Derived from `pyproject.toml` + the repo tree. Unknown fields surface as `hmmm` rather than a guess.</sub>
<!-- END GENERATED:manifest -->

> The block above is generated from `pyproject.toml` + the repo tree by the
> `manifest` living-spec tool (`.agents/skills/manifest/`) and gated in CI
> (`.github/workflows/manifest-check.yml`) — do not hand-edit between the
> markers; run `python .agents/skills/manifest/generate.py --write` after
> changing version/deps/layout. The table below is the hand-authored
> supplement: judgement plus facts the generator does not derive.

| Fact | Value |
|---|---|
| Stdlib modules used | `fractions`, `math`, `cmath`, `itertools`, `struct`, … |
| License | MPL-2.0 (weak copyleft — embed anywhere, but changes to these files must be published; relicensed from MIT) |

The repo ships **two** importable Python packages plus a separate set of
single-file lineage modules:

- `ucns/` — **v1.0 public Python API.**
  - `ucns/__init__.py` exports the engine surface from modules that now live
    directly under `ucns`.
  - `ucns.a0_safe` is the A0-safe inspection facade (stable).
  - `ucns/core.py`, `embedding.py`, `epicycle.py`, `mobius.py`,
    `similarity.py` are the **v0.6.5-lineage embedding modules**. They live
    inside the `ucns/` package but are **not** imported by
    `ucns/__init__.py`; import them by submodule path
    (`from ucns import core` / `from ucns.core import UCN`).
- `ucns_recursive/` — **DEPRECATED for direct user imports** compatibility
  wrappers around `ucns.*`. Engine code should be edited under `ucns/`. No
  runtime `DeprecationWarning` is emitted; the deprecation is docs-only and
  release timing is controlled locally by the maintainer.

**Packaging note.** `pyproject.toml` `[tool.setuptools.packages.find]` sets
`include = ["ucns*"]` (no `exclude`), so the **wheel** bundles **both** the
`ucns/` package and the `ucns_recursive/` compatibility shim (verified:
`top_level.txt` is `ucns` and `ucns_recursive`). The wheel keeps
`ucns_recursive` for legacy callers, but `import ucns` no longer depends on it.
The **sdist** likewise bundles the shim via `MANIFEST.in`
(`recursive-include ucns_recursive *.py`), so editable, sdist, and wheel
installs all preserve compatibility consistently.

> History: earlier releases set `exclude = ["ucns_recursive*"]`, which dropped
> the then-engine package from the wheel and made wheel-only `import ucns` fail
> with `ModuleNotFoundError: No module named 'ucns_recursive'` (masked only by
> editable/sdist installs). The engine now lives under `ucns`; the
> `ucns_recursive` package remains only as a compatibility shim.

---

## v1.0 Scope

UCNS v1.0 is a scoped, reproducible research release for
**catalogue-sufficient recursive factorization** (Theorem N), not a claim
of total general recursive primality. Carrier widening, tractable
sub-catalogues, and general recursive primality outside defended-complete
domains are **out of v1.0 scope**.

See `docs/ucns-spec-status-addendum-2026-05-16.md` for the status
vocabulary and `ucns-spec.md` §F1–F4 for the reconciled spec.

---

## Current Theorem Frontier

Status vocabulary: `DEFENDED`, `IMPLEMENTED`, `TEST-BACKED`,
`ORACLE-COMPLETE`, `FRONTIER`, `EXPERIMENTAL`.

| Layer | Status |
|---|---|
| Flat kernel algebra | `DEFENDED` |
| Depth-1 restricted completeness | `DEFENDED` |
| Depth-2 oracle (smallest class, Lemma 7) | `DEFENDED` + `ORACLE-COMPLETE` |
| Full frozen depth-2 domain | `IMPLEMENTED` + `TEST-BACKED` (not yet `DEFENDED` at spec level) |
| Depth-3 asymmetric (Theorem 9) | `TEST-BACKED` (6/6 empirical) |
| Catalogue-sufficient completeness — all depths (Theorem N) | `DEFENDED` — proof drafted, awaiting external formal review |
| Tractable sub-catalogues | `FRONTIER` |
| Carrier widening | `FRONTIER` / out of v1.0 scope |
| General recursive primality outside defended-complete domains | out of v1.0 scope |

Frozen depth-2 domain scope:
```
depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4
```

`factor_search_v08` is depth-agnostic: every step operates on `==` and plain
catalogue scans. Depth enters only through catalogue selection. See
`ucns-theorem-n.md` for the unified completeness theorem.

**A0 rule.** `SEQ-PRIME` is only absolute inside a defended-complete domain.
Consult `ucns_recursive.domain_status.VERIFIED_DOMAIN_LABELS` and
`domain_status_metadata`; treat `SEQ-PRIME` outside that set as
non-absolute. Unit-group factors are filtered before `SEQ-PRIME` is
interpreted (multiplicative-unit boundary; see `docs/mathematical-glossary.md`).

**Formal proof non-transfer.** `formal/` is a Lean 4 scaffold whose theorem
statements are all `sorry`-stubbed and prove nothing yet. A `sorry`-backed
statement confers **no** `DEFENDED` status to any consumer; results graduate
from FRONTIER only when every `sorry` is discharged and externally reviewed.

**Cross-repo non-continuity.** Interoperability with `edcmbone`, `a0`,
`interdependent-lib` is not theorem continuity. See
`docs/prime-quartet-discontinuity.md` and
`docs/edcm-edcmbone-bridge-checklist.md`.

---

## Repository Layout

```
ucns/                              # v1.0 PUBLIC API
  __init__.py                      # exports engine surface from ucns modules
  a0_safe.py                       # A0-safe facade: identity, describe, canonical, factor
  core.py                          # UCN angular primitive (v0.6.5 lineage; not re-exported)
  embedding.py                     # Unit-circle embedding utilities (lineage)
  epicycle.py                      # Epicycle radial modulation (lineage)
  mobius.py                        # Möbius doubled-surface / spinor states (lineage)
  similarity.py                    # UCNS object similarity metrics (lineage)
  py.typed

ucns_recursive/                    # DEPRECATED compatibility wrappers
  __init__.py                      # Re-exports the full deployable surface from ucns
  canonical.py                     # UCNSObject, UNIT, multiply, is_unit, is_multiplicative_unit
  domains.py                       # Frozen D' domain params, oracle predicates, S2
  domain_status.py                 # Typed status taxonomy + VERIFIED_DOMAIN_LABELS
  host_recovery.py                 # Recover host angle/face structure from P
  recursive_quotient.py            # Catalogue-bounded payload factor finders
  payload_system.py                # Coupled payload equation solver
  witness_matrix.py                # Witness, WitnessMatrix (global consistency)
  factor_search_v08.py             # Top-level factorization engine (main entry point)
  recursive_codec.py               # Python ↔ UCNSObject encoder/decoder
  left_quotient.py                 # Constructive left/right quotient primitives
  store.py                         # UCNSStore — keyed corpus + algebraic retrieval
  catalogue.py / catalogue_d3.py   # Catalogue builders for factor_decompose
  serialization.py                 # Canonical JSON + stable hashing
  factorization_result.py          # A0-facing scoped factorization envelope
  object_record.py                 # A0-facing object inspection record
  geometry_bridge.py               # UCNS-A ↔ UCNS-G homomorphism check
  tests/                           # ENGINE test suite (run by CI)
    test_depth2_oracle.py          # Depth-2 oracle theorem (DEFENDED + ORACLE-COMPLETE)
    test_depth2_full_domain.py     # Frozen depth-2 domain compact sweep
    test_failure_boundary_e109.py  # E10.9 regression tests
    test_recursive_codec.py        # Round-trip codec tests
    test_left_quotient.py          # Left/right quotient completeness tests
    test_store.py                  # UCNSStore insert/retrieval/decompose
    test_catalogue_d3.py, test_domain_status.py, test_serialization.py,
    test_factorization_result.py, test_object_record.py, test_a0_safe.py,
    test_geometry_bridge.py, test_visualization_boundary.py

tests/                             # v1.0 API-package test suite (run by CI)
  test_core.py, test_embedding.py, test_epicycle.py,
  test_mobius.py, test_similarity.py   # lineage-module tests
  test_docs_claim_guardrail.py     # doc overclaim guardrail
  test_public_import_boundary.py   # verifies ucns does not import compatibility shim

formal/                            # Lean 4 proof scaffold (FRONTIER, all `sorry`)
  lean-toolchain                   # leanprover/lean4:v4.7.0
  lakefile.lean                    # Lake package `Ucns`
  Ucns/TheoremN.lean               # stubbed statements (depth-1, Lemma 7, Theorem N)

code/                              # Exploratory versioned artifacts (read-only reference)
  v080-*.py, v081-*.py, v082-*.py, v090-*.py, e109-*.py, proof_trace.py
  sweeps/                          # Empirical verification scripts (e.g. t9_minimal_cat.py)

examples/
  depth_examples/                  # Minimal reviewer examples (depth1/2/3, catalogue boundary)
  visualization/                   # Human-facing demos (e.g. seed53.html) + claim-linkage README

docs/                              # Specs, status, glossary, reproducibility, claims ledger
  ucns-spec-status-addendum-2026-05-16.md   # status vocabulary + A0 rule
  claims-ledger.md, mathematical-glossary.md, reproducibility.md
  prime-quartet-discontinuity.md, edcm-edcmbone-bridge-checklist.md
  (and other supplements)

# Root-level docs / specs
ucns-spec.md                       # Reconciled core UCNS spec (canonical)
ucns-theorem-n.md                  # Theorem N: catalogue-sufficient completeness (unified)
ucns-spec-frontier-v090.md         # v0.9.0 frontier (partially superseded)
ucns-lemma8-depth3.md              # Depth-3 factor search (SUPERSEDED by theorem-n)
ucns-v06-completeness-proof.md, ucns-v06-left-quotient-completeness.md
depth7-frontier.md, MANIFEST.md, REVIEW_PACKET.md, RELEASE.md, CHANGELOG.md
README.md, DOCTRINE.md, CONTRIBUTING.md, accreditation.md
LICENSE, MANIFEST.in

# Root-level reference snapshot + probe scripts (read-only research artifacts)
ucns-code-v065.py                  # Stable v0.6.5 snapshot (dashed name; not importable)
ucns_code_v065.py                  # Import shim so proof scripts can load the snapshot
operational_widening_probe.py, ternary_widening_probe.py,
prime5_widening_probe.py, prime_carpet_probe.py,
phi_compose_probe.py, phi_compose_probe_v2.py, phi_compose_probe_v3.py
                                   # Carrier-widening / Phi-composition empirical probes (FRONTIER)
```

---

## Development Workflow (verified commands)

```bash
# Editable install (with dev extras: build, twine)
python -m pip install -e .[dev]

# Run the ENGINE test suite (this is what CI runs)
python -m unittest discover ucns_recursive/tests/ -v

# Run a specific engine test module
python -m unittest ucns_recursive.tests.test_depth2_oracle -v
python -m unittest ucns_recursive.tests.test_recursive_codec -v
python -m unittest ucns_recursive.tests.test_store -v
python -m unittest ucns_recursive.tests.test_depth2_full_domain -v

# Build + validate distribution (matches python-package.yml)
python -m build
python -m twine check dist/*
```

No pytest is configured (no `pytest.ini`, no `[tool.pytest.ini_options]`).
Use `python -m unittest` for all testing. No linter/formatter config is
present (`.ruff_cache`/`.mypy_cache` are gitignored but no config files
exist), so there is no lint command to run.

### CI

Two GitHub Actions workflows under `.github/workflows/`:

| Workflow | Trigger | What it does |
|---|---|---|
| `ci.yml` | push/PR touching `ucns/`, `ucns_recursive/`, `tests/`, `pyproject.toml` | Python 3.11; `pip install -e .[dev]`; runs **both** `ucns_recursive/tests/` and the top-level `tests/` suite |
| `python-package.yml` | push/PR to `main` | matrix 3.8/3.10/3.11/3.12; `python -m build`; `twine check`; wheel import-boundary smoke test; runs `ucns_recursive/tests/` and top-level `tests/` |

**Both CI workflows exercise the top-level `tests/`** suite as well as
`ucns_recursive/tests/`; `python-package.yml` also validates that wheel-only
`import ucns` does not import the compatibility shim.

---

## Deployable Surface (engine API)

All of the following import cleanly from `ucns` (re-exported from
`ucns_recursive`). See `ucns_recursive/__init__.py` `__all__` for the full list.

### `recursive_codec` — Python ↔ UCNSObject

Encodes Python values as `UCNSObject`s and decodes them back. Type is
inferred from the leading-sentinel count:

| Leading sentinels | Decoded type |
|---|---|
| 1 | `bytes` leaf |
| 2 | `list` |
| 3 | `dict` (insertion order preserved) |

A sentinel cell: `angle=Fraction(0)`, `payload=None`, `face=0`. Content
cells use `face=1`. Leaf coercions (all round-trip as `bytes`): `str`→UTF-8,
`int`/`float`→`str()`/`repr()` encoded, `bool`→`b"1"`/`b"0"`,
`bytearray`→`bytes`. Unsupported types raise `EncodingError`.

```python
from ucns import recursive_encode, recursive_decode, EncodingError
recursive_decode(recursive_encode(b"hi"))      # b"hi"
recursive_decode(recursive_encode([b"a"]))     # [b"a"]
recursive_decode(recursive_encode({b"k": b"v"}))  # {b"k": b"v"}
```

### `left_quotient` / `right_quotient` — Constructive Quotient

> If `A ⊠ B ≡_seq P`, then `left_quotient(P, A)` returns B; returns `None`
> iff no such B exists.

```python
from ucns import left_quotient, right_quotient, multiply, recursive_encode
A, B = recursive_encode(b"hello "), recursive_encode(b"world")
P = multiply(A, B)
left_quotient(P, A)   # == B
right_quotient(P, B)  # == A
```

`right_quotient` is the symmetric dual (asserted-by-symmetry; dual proof not
yet written out). **`None` is ambiguous:** it means either "no factorization"
or "B is the unit". Pre-check `A == P` to distinguish.

### `store` — UCNSStore

Keyed corpus of `UCNSObject`s with proof-backed algebraic retrieval (linear
O(corpus) scan, no index).

```python
from ucns import UCNSStore, recursive_encode
store = UCNSStore()
store.insert("doc1", b"hello world")
store.left_factors(b"hello ")          # [(key, remainder), ...]
store.is_left_factor(b"hello world", "doc1")  # True
store.factor_decompose("doc1", [recursive_encode(b"hello ")])  # [(A, B), ...]

# Verified domain (completeness guaranteed): {"depth-0","depth-1","depth-2-oracle"}
strict = UCNSStore(enforce_verified_domain=True)  # raises OutOfDomainError out-of-domain
store.domain_status_of("doc1")
```

### `a0_safe` — A0-safe inspection facade (preferred for A0-facing claims)

```python
from ucns import a0_safe
a0_safe.describe(obj)    # UCNSObjectRecord, no factorization run
a0_safe.identity(obj)    # stable canonical hash
a0_safe.canonical(obj)   # canonical JSON (or as_bytes=True for bytes)
a0_safe.factor(obj)      # scoped FactorizationResult envelope
```

Do not surface raw factorization sentinels (`SEQ-PRIME`) for A0-facing
claims when a scoped envelope exists.

---

## Core Algebra & Factorization

```python
from ucns import UCNSObject, multiply, is_unit, factor_search_v08
from fractions import Fraction
UNIT = None

S2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])   # depth-0
A  = UCNSObject(2, 2, [(Fraction(0), S2),   (Fraction(1), UNIT)], [0, 0])   # depth-1
P  = multiply(A, A)

result = factor_search_v08(P)   # -> (A_recovered, B_recovered) or "SEQ-PRIME"
```

`factor_search_v08` returns **one** valid factorization (first under the loop
ordering: balanced `p ≥ 2` splits first, `p = 1` last); factorization is not
generally unique. Use `store.factor_decompose` with an explicit catalogue to
enumerate all catalogue-bounded factorizations. For depth-3+ targets, extend
the catalogue with the deep payloads of the expected factors
(`ucns-theorem-n.md §4.2–4.3`).

**Pipeline:** host recovery → payload system construction (p×q coupled
equations) → witness-matrix global consistency → face recovery → exact
recomposition (`multiply(A_cand, B_cand) == P`).

---

## Key Conventions & Gotchas

- **No external dependencies.** stdlib only. Do not add runtime deps.
- **`ucns` is the v1.0 public API.** New user-facing code imports from `ucns`
  (and `ucns.a0_safe`). `ucns_recursive` is deprecated for direct user
  imports; edit engine code under `ucns/`.
- **Lineage modules are not auto-exported.** `core`, `embedding`, `epicycle`,
  `mobius`, `similarity` live in `ucns/` but are not in `ucns/__init__.py`;
  import them by submodule path.
- **CI runs both test suites.** `tests/` covers the v1.0 API package;
  `ucns_recursive/tests/` covers legacy compatibility. `python-package.yml`
  also runs a wheel import-boundary check.
- **`tests/test_public_import_boundary.py` protects the migration boundary.**
  It fails if importing `ucns` reaches for `ucns_recursive`.
- `factor_search_v08` is the authoritative solver — do not bypass it by
  calling internal stages directly.
- **Three E10.9 invariants** in `factor_search_v08`: (1) no false atomicity
  (descend into depth-1 payloads like S2); (2) global witness consistency
  (one assignment explains every cell); (3) staged reconstruction.
- **`left_quotient` `None` is ambiguous** — pre-check `A == P`.
- **Insertion order is semantic** in encoded dicts.
- **Read-only research artifacts** — do not modify: `ucns-code-v065.py`,
  `ucns_code_v065.py`, everything in `code/`, and the root probe scripts
  (`*_probe*.py`, `prime_carpet_probe.py`).
- **`formal/` proves nothing yet** — all `sorry`; never cite it as
  formal verification.
- When adding a solver stage: edit `ucns/factor_search_v08.py` and add tests in
  the relevant public or compatibility suite. When adding codec/retrieval
  features: edit `ucns/recursive_codec.py` / `ucns/left_quotient.py` /
  `ucns/store.py` and update `ucns/__init__.py` `__all__`.
- **Visualization/demo artifacts** go under `examples/visualization/` with a
  README stating the exact claim illustrated and the non-proof boundary
  (see README "What belongs in this repo").

---

## What Does Not Exist Yet

- No linting/formatting config and no lint command.
- No `pytest.ini` / pyproject pytest config (unittest only).
- No runtime `DeprecationWarning` on `import ucns_recursive` (docs-only).
- Right-quotient completeness proof (asserted-by-symmetry).
- Discharged Lean proofs — `formal/` is all `sorry`.
- Carrier widening / general recursive completeness — out of v1.0 scope.

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
- License: MPL-2.0 (weak copyleft — embed anywhere, but changes to these files must be published; relicensed from MIT)

## Agent module-build doctrine

Before adding a new module, route, service, adapter, schema, worker, engine,
UI panel, migration, or experiment, read:

`./.agents/skills/meta-module-build/SKILL.md` (built on `msdmd`; see also
`test-build`). Start new module work with a `MODULE_BUILD` block; mark
unknown fields `hmmm`, do not guess. When a module touches UCNS identity or
factorization, prefer the `ucns.a0_safe` boundary over raw sentinels.
