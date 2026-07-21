# UCNS → EDCM Producer Contract (minimal)

**Status:** draft for the foundations restart (Chapter 1 sealed).  
**Purpose:** define the exact surface a UCNS object must expose so that EDCM can stop treating UCNS as typed `NA` and begin measuring it.

## Required surface

A complete, non-null UCNS object supplies:

| Field / method | Type | Meaning | Required |
|----------------|------|---------|----------|
| `W` / `support_weight()` | `float ≥ 0` | Aggregate cell support | yes |
| `M` / `product_character()` | `float ≥ 0` | Product character (combinatorial) | yes |
| `B` / `faithful_breadth()` | `float ≥ 0` | Faithful breadth (complete distinction) | yes |
| `a` / `radius()` | `float ∈ [0,1)` | Carrier radius \(1 - e^{-B}\) | yes |
| `is_null()` | `bool` | True only for Structural Null | yes |
| `cells` | sequence of cells | Each cell has definitive \(\mu \ge 0\) | yes |
| `receipts` | sequence | Ordinary retained structure | yes (may be empty) |

Structural Null is the unique object for which \(W = M = B = a = 0\).

## Invariants that must hold

1. \(B = 0 \iff\) the object is Structural Null.
2. \(W(A \boxtimes C) = W(A) \cdot W(C)\).
3. \(M(A \boxtimes C) = M(A) \cdot M(C)\).
4. \(a = 1 - e^{-B}\) exactly.
5. Algebraic zero in a payload never forces the carrier to null if \(\mu > 0\) or receipts remain.
6. Separation: there exist non-null pairs with \(W\) equal / \(M\) different, and \(M\) equal / \(W\) different.

## What EDCM may rely on

- The three valuations are independent above null.
- Pairing is the only carrier-level product; typed dispatch is a later, separate stage.
- Pruning zero-support cells commutes with pairing (Rectangular-Zero).
- Collapse to null occurs only on complete structural absence.

## What is still provisional

- Concrete evaluators for \(B\) beyond the current log-support + receipt + distinction heuristic.
- Full typed payload dispatch surface.
- Canonical equivalence relation for receipts and encoding artifacts (the first invariance tests exist; the full relation does not).

## Version

`0.1.0-foundations` — matches the sealed Chapter 1 object model on branch `ucns-Grok`.

When EDCM consumes an object that satisfies this contract, the typed-NA status for UCNS is lifted.
