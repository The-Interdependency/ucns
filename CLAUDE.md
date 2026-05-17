# CLAUDE.md — UCNS: Unit Circle Number System

This file gives AI assistants context needed to work effectively in this repository.

---

## What This Repo Is

`ucns` (pip package: **`ucns`**) is a zero-dependency pure-Python library
implementing **Unit Circle Number System** sequence theory with a focus
on recursive factorization. Given a UCNS product object P, the library
recovers factors A and B such that A ⊠ B = P.

The repo ships two installable Python packages:
- `ucns/` — **v1.0 public Python API.** Re-exports the engine plus the
  v0.6.5-lineage modules (embedding, epicycle, Möbius, similarity) and
  the A0-safe inspection facade (`ucns.a0_safe`).
- `ucns_recursive/` — **DEPRECATED for direct user imports.** The
  factorization engine implementation currently lives here and is
  re-exported by `ucns`. New user-facing code should import from `ucns`,
  not `ucns_recursive`. No runtime DeprecationWarning is emitted yet;
  the release schedule is controlled locally by the maintainer.

**Python requirement:** ≥ 3.8 (CI exercises 3.8, 3.10, 3.12)
**External dependencies:** none (fractions, math stdlib only)
**License:** Apache 2.0

---

## v1.0 Scope

UCNS v1.0 is a scoped, reproducible research release for
**catalogue-sufficient recursive factorization** (Theorem N), not a
claim of total general recursive primality. Carrier widening, tractable
sub-catalogues, and general recursive primality outside
defended-complete domains are **out of v1.0 scope**.

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
| Full frozen depth-2 domain | `IMPLEMENTED` + `TEST-BACKED` (not yet `DEFENDED`) |
| Depth-3 asymmetric (Theorem 9) | `TEST-BACKED` (6/6 empirical) |
| Catalogue-sufficient completeness (Theorem N) | `DEFENDED` — proof drafted, awaiting external formal review |
| Tractable sub-catalogues | `FRONTIER` |
| Carrier widening | `FRONTIER` / out of v1.0 scope |

Frozen depth-2 domain scope:
```
depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4
```

**A0 rule.** `SEQ-PRIME` is only absolute inside a defended-complete
domain. Consult `ucns_recursive.domain_status.VERIFIED_DOMAIN_LABELS`
and `domain_status_metadata`; treat `SEQ-PRIME` outside that set as
non-absolute.

---

## Repository Layout

```
ucns/                              # v1.0 PUBLIC API (re-exports the engine)
  __init__.py                      # Re-exports from ucns_recursive
  a0_safe.py                       # A0-safe inspection facade (v1.0 stable)
  core.py                          # UCNSObject base, multiply, is_unit (v0.6.5 lineage)
  embedding.py                     # Unit-circle embedding utilities
  epicycle.py                      # Epicycle radial modulation layers
  mobius.py                        # Möbius doubled-surface / spinor states
  similarity.py                    # UCNS object similarity metrics

ucns_recursive/                    # DEPRECATED for direct user imports;
                                   # engine implementation lives here.
  __init__.py                      # Package init — exports full deployable surface
  canonical.py                     # UCNSObject, multiply, is_unit (recursive)
  domains.py                       # Frozen D' domain + payload catalogue
  host_recovery.py                 # Recover host angle/face structure from P
  recursive_quotient.py            # find_left_factor, find_right_factor
  payload_system.py                # Coupled payload equation solver
  witness_matrix.py                # Witness, WitnessMatrix (global consistency)
  factor_search_v08.py             # Top-level factorization engine (main entry point)

  # --- v0.1 deployable surface (May 2026) ---
  recursive_codec.py               # Python ↔ UCNSObject encoder/decoder
  left_quotient.py                 # Constructive left/right quotient primitives
  store.py                         # UCNSStore — keyed corpus + algebraic retrieval

  tests/
    test_depth2_oracle.py          # Depth-2 oracle theorem (GREEN)
    test_depth2_full_domain.py     # Frozen depth-2 domain sweep
    test_failure_boundary_e109.py  # E10.9 regression tests
    test_recursive_codec.py        # Round-trip codec tests (v0.1)
    test_left_quotient.py          # Left/right quotient completeness tests (v0.1)
    test_store.py                  # UCNSStore insert/retrieval/decompose (v0.1)

ucns-code-v065.py                  # Stable v0.6.5 snapshot (read-only reference)
ucns-depth2-staged-engine.py       # Depth-2 staged engine (historical)
code/                              # Exploratory versioned artifacts (read-only)
  v080-coupled-witness-solver.py
  v080-recursive-factorization-refactor-plan.py
  v081-depth2-oracle-theorem.py
  v082-depth2-final-push.py
  v090-carrier-widening.py
  e109-depth2-failure-boundary.py
archive/                           # Archived UCN embedding library (read-only)

ucns-spec-frontier-v090.md         # Current completeness frontier spec
ucns-spec.md                       # Core UCNS specification
ucns-v06-completeness-proof.md     # Depth-6 completeness proof
ucns-v06-left-quotient-completeness.md
depth7-frontier.md                 # Depth-7 frontier notes
MANIFEST.md                        # Repository file manifest
REVIEW_PACKET.md                   # Review packet
pyproject.toml
LICENSE
README.md
```

---

## Development Workflow

```bash
# Install editable
pip install -e .

# Run all tests (unittest discover on ucns_recursive)
python -m unittest discover ucns_recursive/tests/ -v

# Run a specific test file
python -m unittest ucns_recursive.tests.test_depth2_oracle -v
python -m unittest ucns_recursive.tests.test_recursive_codec -v
python -m unittest ucns_recursive.tests.test_store -v

# Run depth-2 domain sweep
python -m unittest ucns_recursive.tests.test_depth2_full_domain -v
```

No pytest configured. Use `python -m unittest` for all testing.

---

## Deployable Surface (v0.1 — May 2026)

Three modules form the embedding-side interface between Python values and the algebraic layer.

### `recursive_codec` — Python ↔ UCNSObject

Encodes Python values as `UCNSObject`s and decodes them back.

**Encoding shape (option c — type from leading sentinel count):**

| Leading sentinels | Decoded type |
|---|---|
| 1 | `bytes` leaf |
| 2 | `list` |
| 3 | `dict` (insertion order preserved) |

A sentinel cell: `angle=Fraction(0)`, `payload=None`, `face=0`.  
Content cells: `face=1`.

**Leaf coercions** (all round-trip as `bytes`):
- `str` → UTF-8 encode
- `int` / `float` → `str().encode()` / `repr().encode()`
- `bool` → `b"1"` / `b"0"`
- `bytearray` → treated as `bytes`

```python
from ucns import recursive_encode, recursive_decode, EncodingError

obj = recursive_encode(b"hello world")
result = recursive_decode(obj)         # b"hello world"

obj2 = recursive_encode([b"a", b"b"])
result2 = recursive_decode(obj2)       # [b"a", b"b"]

obj3 = recursive_encode({b"k": b"v"})
result3 = recursive_decode(obj3)       # {b"k": b"v"}
```

Unsupported types (e.g. `set`, arbitrary objects) raise `EncodingError`.

### `left_quotient` — Constructive Quotient

Promoted from `ucns-code-v065.py`. Implements the v0.6 completeness theorem:

> If `A ⊠ B ≡_seq P`, then `left_quotient(P, A)` returns B. Returns `None` iff no such B exists.

```python
from ucns import left_quotient, right_quotient, multiply, recursive_encode

A = recursive_encode(b"hello ")
B = recursive_encode(b"world")
P = multiply(A, B)

recovered_B = left_quotient(P, A)   # equals B
recovered_A = right_quotient(P, B)  # equals A
```

**Three internal phases:** host recovery (Lemmas 2–3), payload descent (Lemmas 4–8), verification (`multiply(A, B_cand) == P`).  
`right_quotient` is the symmetric dual (asserted-by-symmetry; dual proof not yet written out).

**`None` is ambiguous:** `left_quotient` returns `None` both when no factorization exists *and* when B is the unit. Callers that need to distinguish these two cases should pre-check `A == P`.

### `store` — UCNSStore

Keyed corpus of `UCNSObject`s with proof-backed algebraic retrieval.

```python
from ucns import UCNSStore, recursive_encode

store = UCNSStore()
store.insert("doc1", b"hello world")
store.insert("doc2", b"hello there")

# Left-factor retrieval: every doc for which query is a left factor
matches = store.left_factors(b"hello ")  # [(key, remainder), ...]

# Exact-match check
store.is_left_factor(b"hello world", "doc1")  # True

# Catalogue-bounded decomposition
catalogue = [recursive_encode(b"hello ")]
decomps = store.factor_decompose("doc1", catalogue)  # [(A, B), ...]
```

**Verified domain** (completeness guaranteed): `{"depth-0", "depth-1", "depth-2-oracle"}`.  
Outside the domain, soundness holds but completeness is not proven.

```python
# Enforce at insert time
strict_store = UCNSStore(enforce_verified_domain=True)
# Raises OutOfDomainError for depth-2-non-oracle or depth-3+ inputs

# Audit per-key status
store.domain_status_of("doc1")  # "depth-1", "depth-2-oracle", etc.
```

Retrieval cost is O(corpus size) — linear scan, no index.

---

## Core Algebra (Quick Reference)

```python
from ucns import UCNSObject, multiply, is_unit, factor_search_v08
from fractions import Fraction

UNIT = None

# Depth-0 (S2)
S2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])

# Depth-1 object
A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
P = multiply(A, A)

# Factorize
result = factor_search_v08(P)
# Returns (A_recovered, B_recovered) or "SEQ-PRIME"
```

---

## Factorization Pipeline (`factor_search_v08`)

1. **Host recovery** — extract candidate A/B angle sequences from P
2. **Payload system construction** — build the p×q coupled equations
3. **Witness-matrix consistency** — verify one globally consistent payload assignment
4. **Face recovery** — enumerate valid face-bit assignments
5. **Exact recomposition** — final truth test: `multiply(A_cand, B_cand) == P`

---

## Key Conventions

- **No external dependencies** — fractions, math, itertools only. Do not add runtime deps.
- **`ucns` is the v1.0 public API.** New user-facing code should import from `ucns` (and `ucns.a0_safe` for A0-safe inspection). `ucns_recursive` is **deprecated for direct user imports** but is where the engine implementation currently lives and is still the right place to edit engine code.
- `factor_search_v08` is the authoritative solver — do not bypass it by calling internal stages directly.
- **Three invariants** in `factor_search_v08` (root-cause fixes from E10.9 analysis):
  1. **No false atomicity** — depth-1 payloads like S2 are recursed into, not treated as atomic
  2. **Global witness consistency** — one assignment must explain every payload cell simultaneously
  3. **Staged reconstruction** — host recovery → payload system → witness verification → face recovery → exact recomposition
- **`None` return from `left_quotient` is ambiguous** — it means either "no solution" or "B is the unit". Always pre-check `A == P` if you need to distinguish.
- **Insertion order is semantic** in dicts — `{b"a": b"1", b"b": b"2"}` and `{b"b": b"2", b"a": b"1"}` encode to different `UCNSObject`s by design.
- **Read-only files**: `ucns-code-v065.py`, `ucns-depth2-staged-engine.py`, everything in `code/` and `archive/`. Do not modify these.
- When adding a new solver stage: add it to `factor_search_v08.py` and add corresponding tests in `ucns_recursive/tests/`.
- When adding codec or retrieval features: add them to `recursive_codec.py`, `left_quotient.py`, or `store.py` and update `__init__.py` exports.

---

## What Does Not Exist Yet

- No linting config
- No `pytest.ini` or pyproject `[tool.pytest.ini_options]` (tests use unittest discover)
- Carrier widening and general recursive completeness — explicitly **out of v1.0 scope**
- Right-quotient completeness proof (currently asserted-by-symmetry)
- No runtime `DeprecationWarning` on `import ucns_recursive` yet (canon is docs-only for v1.0; release ships from local termux at maintainer cadence)
- No golden output fixtures or `docs/claims-ledger.md` yet (deferred from canon-only reconciliation pass)

---

## Related Repos

| Repo | Role |
|------|------|
| The-Interdependency/interdependent-lib | Meta-package bundling ucns + other libs |
| erinepshovel-code/UnitCircle | Visualization and EML experiment scripts for prime distribution |
| The-Interdependency/a0 | Agent platform that uses UCNS-derived encoding |

---

## Git Workflow

- Main branch: `main`
- Feature branches: `feat/<description>`, `fix/<description>`
- Author: Erin Patrick Spencer (wayseer@interdependentway.org)
- License: Apache 2.0
