# EDCM / edcmbone ↔ UCNS Bridge Checklist

**Status:** mandatory gate for future public-gonol, factorization, geometry, or
measurement bridges. This document is not a bridge and transfers no theorem or
measurement status.

## 0. Foundational boundary

UCNS is rooted in the fixed-origin public gonol promoted from
`a0-betatest@7af8deb`:

```text
position 0 = SPACE = ZERO
position 0 = Möbius twist point = seam = system origin
one 360-degree circuit flips orientation
complete return requires 720 degrees
```

UCNS also contains a normalized recursive factorization algebra
(`UCNSObject`, `multiply`, quotient, factor search) and compatibility geometry
projections. Those surfaces do not become identical to the public frame by
naming, normalization, or historical usage.

EDCM and edcmbone are downstream measurement systems. Their scalar readouts,
metric disks, transcript analysis, and empirical claims are not UCNS theorems.

---

## 1. Current surface/status inventory

| Claim / surface | Current status |
|---|---|
| Exact public gonol and fixed SPACE/ZERO origin | `IMPLEMENTED` + `TEST-BACKED` after green promotion CI |
| Public lifted traversal | `IMPLEMENTED` + `TEST-BACKED` after green promotion CI |
| Public origin and 720-degree formal definition | intended sorry-free; `lake build` is authority |
| Normalized recursive factorization implementation | `IMPLEMENTED` with domain-specific evidence |
| Flat kernel algebra | `DEFENDED` in its declared internal scope |
| Depth-1 restricted completeness | `DEFENDED` in its declared internal scope |
| Depth-2 oracle class | `DEFENDED` + `ORACLE-COMPLETE` in its declared scope |
| Full frozen depth-2 domain | `IMPLEMENTED` + `TEST-BACKED`; not generally `DEFENDED` |
| Catalogue-sufficient completeness (Theorem N) | `FRONTIER`; Lean statements remain `sorry`-backed |
| Public-gonol ↔ normalized-factorization bridge | `hmmm`; absent |
| Normalized-factorization ↔ UCNS-G/EDCM bridge | partial adapters; no theorem-status transfer |
| Public-gonol ↔ EDCM semantic/measurement identity | absent and not implied |

No numerical historical test count is an execution claim unless tied to an
immutable artifact.

---

## 2. Existing systems

### 2.1 UCNS public frame

The public frame owns the origin, twist, faces, chirality, adjacency, mirror,
origin-preserving transformations, lifted traversal, and 720-degree complete
return.

### 2.2 Normalized recursive factorization algebra

The internal algebra implements ordered recursive objects, multiplication,
quotients, catalogue search, stable serialization, and proof-status evidence.

Its internal multiplication identity is a factorization-unit object, not public
SPACE/ZERO. Its first-cell normalization is object-relative, not a system-origin
operation.

### 2.3 UCNS compatibility geometry

The current geometry projection emits compatibility coordinates such as radius,
breadth, a circular-mean internal value, and chirality-derived fields. It is not
the public frame and has no assumed public-gonol bridge.

### 2.4 EDCM / edcmbone

EDCM and edcmbone implement source processing, metric readouts, axis states,
provenance, and empirical result contracts. They may attach UCNS identity or
status evidence, but they do not inherit UCNS theorem status.

---

## 3. Required bridge layers

A complete cross-stack bridge cannot be one flattened function. It must identify
which transition it implements.

### 3.1 Public frame → normalized factorization object

A bridge `β` must declare and test:

- exact input: public arrangement, lifted path, or other public-gonol value;
- exact output: normalized `UCNSObject` value;
- fixed origin preservation;
- twist and seam preservation;
- orientation after one and two circuits;
- 720-degree complete return;
- face and chirality treatment;
- lifted order and seam-crossing treatment;
- composition correspondence;
- carrier correspondence;
- recoverability and information loss;
- stable serialization and versioning.

No angle formula, first-anchor shift, quotient, hash placement, or object-relative
normalization may stand in for these declarations.

### 3.2 Normalized factorization object → compatibility geometry

A projection `π` must declare:

- input domain;
- output codomain;
- whether it is total;
- whether it is injective;
- degeneracy policy;
- information loss;
- whether internal multiplication is preserved;
- explicit statement that it is not the public frame unless composed with a
  proved `β`.

### 3.3 UCNS evidence → EDCM / edcmbone

A consumer adapter must declare:

- exact UCNS record schema/version;
- source object identity;
- domain and theorem-status evidence;
- whether negative certification is authoritative;
- EDCM policy/measurement epoch identity;
- proof-status and measurement-validity non-transfer.

### 3.4 Public gonol → EDCM language/corpus use

Any word-list, dictionary, morphology, or corpus adapter must consume the UCNS
public gonol rather than reproduce it. It must not:

- derive glyph positions from hashes or dictionary evidence;
- turn carrier indices into invented fractions;
- move or normalize away the origin;
- erase repeated-character revolutions or SPACE seam events;
- infer linguistic semantics from carrier coordinates alone.

---

## 4. Status and evidence requirements

Every bridge output must carry a status from the existing vocabulary:

```text
DEFENDED
IMPLEMENTED
TEST-BACKED
ORACLE-COMPLETE
FRONTIER
EXPERIMENTAL
```

A first implementation defaults to `EXPERIMENTAL` unless stronger evidence is
provided.

The bridge PR must include:

1. exact source and target identities;
2. versioned records;
3. positive fixtures;
4. negative/tamper fixtures;
5. round-trip or explicit non-recoverability tests;
6. composition tests where composition is claimed;
7. origin/twist/720-degree tests where the public frame is involved;
8. proof-status non-transfer tests;
9. generated metadata and package checks;
10. immutable CI artifacts for execution claims.

---

## 5. Mandatory negative tests

At minimum, fail closed when:

- public origin is moved from position zero;
- SPACE is duplicated or absent;
- a custom/private carrier is substituted for the public gonol;
- 360 degrees is treated as complete return;
- lifted order or revolution count is discarded;
- digit `"0"` is treated as ZERO;
- object-relative first-cell normalization is applied to the public frame;
- a public-gonol bridge is inferred from `k/157`, `2k/157`, or another unratified
  continuous convention;
- a geometry projection is labeled injective without evidence;
- Theorem N is used to validate EDCM metrics;
- an uncertified factor-search negative is reported as certified;
- package availability is reported as evidence attachment.

---

## 6. Non-transfer rule

Until every relevant bridge layer is implemented and proved/tested at its
claimed status:

```text
The public gonol does not automatically equal a normalized UCNSObject.
The normalized factorization algebra does not automatically equal UCNS-G.
Theorem N does not validate EDCM, edcmbone, or UCNS-G metric claims.
EDCM outputs do not validate UCNS theorem claims.
```

All cross-repository result contracts must preserve:

```text
authority_transfer = false
proof_status_transfer = false
measurement_status_transfer = false
```

---

## 7. Allowed now

Without a completed bridge, the following remain allowed:

- UCNS may expose and test the exact public gonol.
- A0 may consume UCNS public-gonol surfaces for its applications.
- EDCM may attach canonical UCNS bridge/evidence records under explicit
  non-transfer rules.
- EDCM may preserve morphology and dictionary evidence independently of gonol
  placement.
- Visualizers may render declared projections as `EXPERIMENTAL` so long as they
  do not redefine the public origin.
- Historical objects may be inspected for migration without generating new
  canon claims.

---

## 8. Forbidden now

Without the required artifacts, do not claim:

- normalized `UCNSObject` is the public gonol;
- internal unit is public SPACE/ZERO;
- internal first-cell normalization establishes the system origin;
- Carrier-LCM is the complete public-carrier theorem;
- Theorem N is completeness for the public gonol;
- geometry projection recovers the public twist;
- UCNS proves EDCM metrics;
- EDCM outputs are factorization theorems;
- dictionary semantics determine public-gonol coordinates.

---

## 9. Implementation order

1. Promote and validate the exact public gonol in UCNS.
2. Make A0 consume UCNS rather than maintain a duplicate authority.
3. Keep EDCM's noncanonical placement retired.
4. Specify `β`, the public-frame-to-factorization bridge, only from Erin's canon.
5. Prove/test `β` before widening Carrier-LCM or Theorem N scope.
6. Build downstream word-list or corpus adapters as consumers, not authorities.

---

## 10. Boundary object

This checklist records the living boundary between:

```text
fixed public frame
defined internal algebra
compatibility geometry
downstream measurement
```

It preserves honest incompletion until the missing bridges are real.

## hmmm

The system now has its origin back. What remains is not permission to guess the
bridge; it is the obligation to construct it without flattening the twist.
