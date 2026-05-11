# ucns — Unit Circle Number System: Recursive Factorization Theory

> **Sequence-theoretic factorization on the unit circle, with a witness-matrix recursive quotient solver.**

This repository contains the UCNS (Unit Circle Number System) sequence theory and its implementation.  The focus is **recursive factorization**: given a UCNS product object *P*, recover factors *A* and *B* such that *A ⊠ B = P*.

---

## Collaboration wanted

We are currently looking for mathematics collaborators to help formalize UCNS.

Start here:

- Collaboration issue: https://github.com/The-Interdependency/ucns/issues/7
- Starter task: define one UCNS term in standard mathematical language, with notation, example, non-example, and relationship to existing concepts.

The ask is bounded: help separate definitions, implemented algorithms, empirical results, proof sketches, conjectures, limitations, and counterexamples.

GPT generated; context, prompt Erin Spencer.

---

## Status: Current Theorem Frontier

| Layer | Status |
|---|---|
| Flat kernel algebra | ✅ Defended |
| Depth-1 restricted completeness | ✅ Defended |
| Depth-2 oracle (Lemma 7) | ✅ Defended |
| Depth-3 asymmetric (Theorem 9) | ✅ Empirically verified (6/6) |
| **Catalogue-sufficient completeness — all depths (Theorem N)** | **✅ Proven** |
| Tractable sub-catalogues | 🟡 Open |
| Carrier widening | ⏳ Out of scope |

The `ucns_recursive` package implements the **witness-matrix recursive quotient solver** (`factor_search_v08`).

See `ucns-theorem-n.md` for the unified completeness theorem. The key insight: `factor_search_v08` is depth-agnostic — every step operates on `==` and plain catalogue scans. One theorem covers all depths; the catalogue is the only depth-sensitive input.

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

ucns-theorem-n.md        # Theorem N: catalogue-sufficient completeness (unified)
ucns-lemma8-depth3.md    # Depth-3 factor search (SUPERSEDED — see theorem-n)
ucns-code-v065.py        # Stable v0.6.5 snapshot (reference)
code/                    # Exploratory artifacts (v0.8.0–v0.9.0)
code/sweeps/             # Empirical verification scripts
ucns-spec-frontier-v090.md  # Completeness frontier spec
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

Returns **a** valid factorisation — the first one found under the loop ordering (balanced p ≥ 2 splits first, p = 1 last). Factorisation is not generally unique; other valid pairs may exist. Use `store.factor_decompose` with an explicit catalogue to enumerate all catalogue-bounded factorisations.

The solver implements the full witness-matrix pipeline:

1. **Host recovery** — extract candidate A/B angle sequences from P
2. **Payload system construction** — build the p×q coupled equations  
   `multiply(S_A[k], S_B[j]) == P_payloads[k][j]`
3. **Witness-matrix consistency** — verify one globally consistent payload assignment explains every cell
4. **Face recovery** — enumerate valid face-bit assignments
5. **Exact recomposition** — final truth test: `multiply(A_cand, B_cand) == P`

For depth-3+ targets, extend the catalogue with the deep payloads of the expected factors
(see `ucns-theorem-n.md §4.2–4.3`):

```python
# Theorem 9 example: depth-3 A × depth-2 B
from ucns_recursive.domains import depth_of

def catalogue_from(*objs):
    """Minimal catalogue: recursive payload closure of given objects."""
    cat = [None]
    def collect(o):
        if o is None: return
        for _, p in o.A_plus:
            if p is not None and p not in cat:
                cat.append(p); collect(p)
    for o in objs: collect(o)
    return cat

result = factor_search_v08(P, catalogue_from(A, B))
```

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

UCNS has a defended flat kernel, a defended depth-1 restricted completeness theorem, and a defended depth-2 oracle theorem (Lemma 7). These are all instances of **Theorem N** (catalogue-sufficient factorization, `ucns-theorem-n.md`): if the catalogue contains every payload of the true factors, `factor_search_v08` finds a factorization. Depth enters only through catalogue selection, not through the algorithm. Theorem 9 (asymmetric depth-3) is verified empirically; see `code/sweeps/t9_minimal_cat.py`.

---

**Accreditation:** GPT generated from context provided by Grok, Claude as prompted by Erin Spencer.
