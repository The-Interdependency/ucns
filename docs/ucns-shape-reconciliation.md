# UCNS Shape Reconciliation

## Canonical public-frame correction

The previous two-surface comparison flattened the UCNS public frame into the
normalized recursive factorization object. That framing is superseded.

The exact public gonol from
`The-Interdependency/a0-betatest@7af8debf6ef3905f01baff02b43d8c3bee16ccbc`
is canon for all UCNS.

Its position `0` is SPACE/ZERO: the Möbius twist point, seam, fixed system
origin, and only always-known character. One 360-degree circuit returns to the
same local position with opposite orientation; the complete return requires 720
degrees.

The reconciliation therefore has a **three-surface ontology**:

```text
UCNS-PUBLIC
    fixed 157-position twist-bearing public gonol

UCNS-A
    normalized recursive factorization-object algebra

UCNS-G / EDCM
    downstream metric/geometry and measurement surfaces
```

There is no assumed bridge from UCNS-PUBLIC to UCNS-A, and no theorem-status
transfer from either UCNS surface into EDCM.

---

## 1. UCNS-PUBLIC: canonical frame

UCNS-PUBLIC owns:

- arity `157`;
- exact public glyph arrangement;
- SPACE/ZERO at position `0`;
- Möbius twist, seam, and fixed origin;
- public faces, chirality, adjacency, and origin-fixed mirror;
- private phase/permutation rules that fix position zero;
- lossless lifted traversal;
- full-revolution repeated-character behavior;
- spaces as emitted seam events;
- 720-degree complete return.

It does not derive its origin from a continuous coordinate, a first anchor, or a
normalized factorization object.

---

## 2. UCNS-A: normalized recursive factorization model

UCNS-A is implemented as:

```text
UCNSObject(n_dec, n_min, A_plus, F_plus)
```

with:

- ordered internal host cells;
- exact rational internal values;
- optional recursive payloads;
- internal face bits;
- object-relative normalization;
- recursive multiplication;
- quotient and factor search;
- stable serialization and evidence records.

The recursive model is an implemented UCNS subsystem. It is not the public frame.

### Internal value domain

The implementation stores internal values modulo four and computes `n_min` from
an additional internal projection. Those are facts about UCNS-A as implemented.
They do not establish a public-gonol vertex-angle map, and they do not locate the
public twist origin.

### Internal identity

The singleton internal unit may be the multiplication identity of UCNS-A. It is
not thereby public SPACE/ZERO.

### Multiplication

`multiply(A, B)` composes ordered cells, internal values, face bits, and payloads.
No current theorem proves that this operation is the complete public-gonol
composition or preserves the public twist/orientation structure.

---

## 3. UCNS-G / EDCM: downstream geometry and measurement

UCNS-G and EDCM contain metric axes, projections, geometric visualizations,
measurement records, and empirical readouts.

They may consume UCNS identities or geometry through explicit adapters, but:

- metric values are not public-gonol coordinates merely because they use UCNS;
- Theorem N does not validate EDCM measurements;
- public-gonol canon does not establish empirical semantics;
- geometry projections do not inherit injectivity or proof status without their
  own evidence.

---

## 4. Correspondence table

| Surface | Public-gonol counterpart | Status |
|---|---|---|
| Fixed system origin | public position `0`, SPACE/ZERO twist seam | **CANONICAL** |
| Complete return | two orientation-changing circuits, 720 degrees | **CANONICAL** |
| Public face/chirality | `face`, `chirality`, `n_plus`, `n_minus`, mirror | **CANONICAL** |
| Lifted text traversal | absolute path over public carrier | **CANONICAL** |
| UCNS-A first-cell normalization | none established | **NO BRIDGE** |
| UCNS-A internal modulo-four values | none established | **NO PUBLIC-VERTEX MAP** |
| UCNS-A `n_min` | none established as complete public carrier | **INTERNAL PROJECTION** |
| UCNS-A face XOR | public twist/chirality derivation absent | **BOOLEAN LAW; SYSTEM INTERPRETATION OPEN** |
| UCNS-A multiplication | public composition correspondence absent | **INTERNAL ALGEBRA** |
| UCNS-G `(rho, lambda, theta, z, w)` | fixed public-frame recovery absent | **COMPATIBILITY PROJECTION** |
| EDCM metrics | no public-gonol semantic identity | **DOWNSTREAM MEASUREMENT** |

---

## 5. Lemma impact

### Reusable internal lemmas

These remain reusable inside UCNS-A when correctly scoped:

- row-major product shape and list lengths;
- exact recomposition predicates;
- generic LCM/divisibility arithmetic;
- recursive payload radius;
- breadth and fork counts;
- Boolean XOR facts;
- finite catalogue enumeration.

### Scope-narrowed theorem families

These are not discarded, but they are internal until a bridge exists:

- factorization identity;
- idempotents and local groups;
- quotient/cancellativity results;
- Carrier-LCM;
- Theorem N search/completeness family;
- the compatibility geometry projection.

### Rejected system-wide interpretations

These must not return:

- public origin chosen by first-cell normalization;
- public zero located at inferred `θ = 0` or `θ = 2π`;
- 360 degrees treated as complete return;
- global public-frame gauge shifting;
- `k/157` or `2k/157` as defining public coordinates;
- factorization unit identified with public SPACE/ZERO;
- Carrier-LCM or Theorem N claimed for the complete public frame without a
  bridge proof.

---

## 6. Bridge obligations

A faithful UCNS-PUBLIC ↔ UCNS-A bridge must be separately specified and prove:

1. fixed origin preservation;
2. twist and seam preservation;
3. orientation change after one circuit;
4. complete 720-degree return;
5. face and chirality preservation;
6. lifted-path and seam-crossing treatment;
7. correspondence of composition;
8. correspondence, or explicit non-correspondence, of carrier invariants;
9. information loss and recoverability;
10. serialization and status boundaries.

No inferred angle convention or normalization rule may substitute for these
obligations.

---

## 7. Verdict

The old verdict “UCNS-A and UCNS-G are parallel” was incomplete because it
omitted the canonical public frame.

The corrected verdict is:

```text
UCNS-PUBLIC is the canonical system frame.
UCNS-A is an internal normalized factorization algebra.
UCNS-G/EDCM is a downstream geometry and measurement family.
Bridges among them are explicit obligations, not assumed identity.
```

Theorem N remains scoped to UCNS-A and remains `FRONTIER`. No proof status
transfers to UCNS-G or EDCM.

## Cross-repository non-transfer checklist

The mandatory downstream boundary is maintained in `docs/edcm-edcmbone-bridge-checklist.md`.

## hmmm

The public frame is no longer missing from the ontology. The bridge from that
frame into the internal algebra remains open and must be defined from Erin's
canon rather than reconstructed from historical implementation choices.
