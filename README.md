# ucns — Unit Circle Number System: Recursive Factorization Theory

> **Sequence-theoretic factorization on the unit circle, with a witness-matrix recursive quotient solver.**

This repository contains the UCNS (Unit Circle Number System) sequence theory and its implementation.  The focus is **recursive factorization**: given a UCNS product object *P*, recover factors *A* and *B* such that *A ⊠ B = P*.

---

## Status: Current Theorem Frontier

| Layer | Status |
|---|---|
| Flat kernel algebra | ✅ Defended |
| Depth-1 restricted completeness | ✅ Defended |
| Depth-2 oracle (smallest class) | ✅ Defended |
| Full frozen depth-2 domain | 🔄 Implemented in `factor_search_v08` |
| Carrier widening | ⏳ After depth-2 closes |

The `ucns_recursive` package implements the **witness-matrix recursive quotient solver** (`factor_search_v08`) targeting the frozen depth-2 domain:

```
depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4
```

---

## Repository Layout

```
ucns_recursive/          # Main UCNS theory package
  canonical.py           # UCNSObject, multiply, is_unit
  domains.py             # Frozen D' domain + payload catalogue
  host_recovery.py       # Recover host angle/face structure from P
  recursive_quotient.py  # find_left_factor, find_right_factor
  payload_system.py      # Coupled payload equation solver
  witness_matrix.py      # Witness, WitnessMatrix (global consistency)
  factor_search_v08.py   # Top-level factorization engine
  tests/
    test_depth2_oracle.py          # Depth-2 oracle theorem (GREEN)
    test_depth2_full_domain.py     # Frozen depth-2 domain sweep
    test_failure_boundary_e109.py  # E10.9 regression tests

ucns-code-v065.py        # Stable v0.6.5 snapshot (reference)
code/                    # Exploratory artifacts (v0.8.0–v0.9.0)
ucns-spec-frontier-v090.md  # Current completeness frontier spec

archive/ucn-embeddings/  # Archived: UCN embedding library (belongs in a separate repo)
```

---

## Core Algebra

Every UCNS object is a sequence of (angle, payload) pairs with a face-flip sequence:

```python
from ucns_recursive import UCNSObject, multiply, is_unit
from fractions import Fraction

UNIT = None

# S2: the canonical depth-0 sequence object
S2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])

# Depth-1 object: A carries S2 as payload in its first cell
A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])

# Product
P = multiply(A, B)
```

---

## Factorization: `factor_search_v08`

```python
from ucns_recursive import factor_search_v08

result = factor_search_v08(P)
# Returns (A_recovered, B_recovered)  or  "SEQ-PRIME"
```

The solver implements the full witness-matrix pipeline:

1. **Host recovery** — extract candidate A/B angle sequences from P
2. **Payload system construction** — build the p×q coupled equations  
   `multiply(S_A[k], S_B[j]) == P_payloads[k][j]`
3. **Witness-matrix consistency** — verify one globally consistent payload assignment explains every cell
4. **Face recovery** — enumerate valid face-bit assignments
5. **Exact recomposition** — final truth test: `multiply(A_cand, B_cand) == P`

---

## Running the Tests

```bash
python -m unittest discover ucns_recursive/tests/ -v
```

---

## Root Cause Fixed (E10.9)

The v0.8.0 failure analysis identified three root causes now corrected in `factor_search_v08`:

1. **No false atomicity** — depth-1 payloads such as S2 are descended into recursively, not treated as atomic
2. **Global witness consistency** — a single assignment of all payload factors must explain every cell simultaneously
3. **Staged reconstruction** — host recovery → payload system construction → witness verification

---

## Completeness Frontier

> UCNS currently has a defended flat kernel, a defended depth-1 restricted completeness theorem, and a defended depth-2 oracle theorem. The `factor_search_v08` solver extends this to the full frozen depth-2 domain via the witness-matrix architecture. Carrier widening and general recursive completeness are the next milestones.

---

**Accreditation:** GPT generated from context provided by Grok, Claude as prompted by Erin Spencer.
