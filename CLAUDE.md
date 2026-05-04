# CLAUDE.md — UCNS: Unit Circle Number System

This file gives AI assistants context needed to work effectively in this repository.

---

## What This Repo Is

`ucns` (pip package: **`ucns`**, v0.8.0) is a zero-dependency pure-Python library implementing **Unit Circle Number System** sequence theory with a focus on recursive factorization. Given a UCNS product object P, the library recovers factors A and B such that A ⊠ B = P.

The repo ships two installable Python packages:
- `ucns/` — stable v0.6.5-lineage modules: embedding, epicycle, Möbius, similarity
- `ucns_recursive/` — active depth-2 witness-matrix factorization engine (`factor_search_v08`)

**Python requirement:** ≥ 3.8  
**External dependencies:** none (fractions, math stdlib only)  
**License:** Apache 2.0

---

## Current Theorem Frontier

| Layer | Status |
|---|---|
| Flat kernel algebra | Defended |
| Depth-1 restricted completeness | Defended |
| Depth-2 oracle (smallest class) | Defended |
| Full frozen depth-2 domain | Implemented in `factor_search_v08` |
| Carrier widening | After depth-2 closes |

Frozen depth-2 domain scope:
```
depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4
```

---

## Repository Layout

```
ucns/                              # Stable v0.6.5-lineage package
  __init__.py                      # Public API
  core.py                          # UCNSObject base, multiply, is_unit
  embedding.py                     # Unit-circle embedding utilities
  epicycle.py                      # Epicycle radial modulation layers
  mobius.py                        # Möbius doubled-surface / spinor states
  similarity.py                    # UCNS object similarity metrics

ucns_recursive/                    # Active factorization engine
  canonical.py                     # UCNSObject, multiply, is_unit (recursive)
  domains.py                       # Frozen D' domain + payload catalogue
  host_recovery.py                 # Recover host angle/face structure from P
  recursive_quotient.py            # find_left_factor, find_right_factor
  payload_system.py                # Coupled payload equation solver
  witness_matrix.py                # Witness, WitnessMatrix (global consistency)
  factor_search_v08.py             # Top-level factorization engine (main entry point)
  tests/
    test_depth2_oracle.py          # Depth-2 oracle theorem (GREEN)
    test_depth2_full_domain.py     # Frozen depth-2 domain sweep
    test_failure_boundary_e109.py  # E10.9 regression tests

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

# Run depth-2 domain sweep
python -m unittest ucns_recursive.tests.test_depth2_full_domain -v
```

No pytest configured. Use `python -m unittest` for all testing.

---

## Core Algebra (Quick Reference)

```python
from ucns_recursive import UCNSObject, multiply, is_unit, factor_search_v08
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
- `ucns_recursive` is the active package for factorization work. `ucns/` is a stable reference baseline.
- `factor_search_v08` is the authoritative solver — do not bypass it by calling internal stages directly.
- **Three invariants** in `factor_search_v08` (root-cause fixes from E10.9 analysis):
  1. **No false atomicity** — depth-1 payloads like S2 are recursed into, not treated as atomic
  2. **Global witness consistency** — one assignment must explain every payload cell simultaneously
  3. **Staged reconstruction** — host recovery → payload system → witness verification → face recovery → exact recomposition
- **Read-only files**: `ucns-code-v065.py`, `ucns-depth2-staged-engine.py`, everything in `code/` and `archive/`. Do not modify these.
- When adding a new solver stage: add it to `factor_search_v08.py` and add corresponding tests in `ucns_recursive/tests/`.

---

## What Does Not Exist Yet

- No CI/CD pipeline
- No linting config
- No `pytest.ini` or pyproject `[tool.pytest.ini_options]` (tests use unittest discover)
- Carrier widening and general recursive completeness are future milestones

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
