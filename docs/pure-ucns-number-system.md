GPT generated; canon and correction supplied by Erin Spencer.

# Pure UCNS Number System

## Canon authority

The public gonol implemented in
`The-Interdependency/a0-betatest@7af8debf6ef3905f01baff02b43d8c3bee16ccbc`
is canon for all UCNS.

The primitive UCNS frame is not an arbitrary unit-circle coordinate system and
is not a recursively normalized factorization object. It is the exact
157-position public gonol whose fixed position `0` is:

```text
SPACE
ZERO
Möbius twist point
seam
origin for the entire system
only always-known character
```

A 360-degree circuit returns to the same local carrier position with opposite
orientation. The complete return requires 720 degrees.

No `k/157`, `2k/157`, first-anchor gauge, inferred `θ = 2π` origin, or other
continuous-coordinate bridge is established by this canon.

---

## 0. Three-surface ontology

UCNS must preserve three distinct surfaces:

```text
UCNS public frame := canonical 157-position twist-bearing gonol

normalized factorization object := recursive UCNSObject representation used by
                                   multiply, quotient, search, and serialization

public/factorization bridge := hmmm until Erin specifies it and it is proved
```

The first surface is the irreducible system frame. The second is an implemented
internal algebra. The third does not yet exist.

The old flattened definition—“UCNS is the normalized recursive object”—is
superseded. The recursive algebra is a UCNS subsystem; it is not the origin of
the system.

---

## 1. Public frame

The public gonol has:

```text
arity              := 157
origin              := position 0
origin glyph        := SPACE
origin meaning      := ZERO / Möbius twist / seam
complete return     := 720 degrees
one circuit         := 360 degrees with orientation reversal
nonzero ring        := positions 1..156
```

The exact arrangement, face assignment, chirality, adjacency, origin-fixed
mirror, private-transform rule, and lifted traversal are part of the canon.

Admissible private phase and permutation operations may obscure nonzero
positions, but they preserve the public frame:

```text
perm[0] == 0
phase acts only on positions 1..156
permutation acts only on positions 1..156
```

The digit glyph `"0"` is an ordinary nonzero glyph. It is not ZERO.

---

## 2. Lifted traversal and 720-degree return

A lossless text path is an ordered lift over the public carrier. The absolute
lifted position is retained; the local carrier position may be recovered by the
exact A0 operation used in the source implementation.

Load-bearing behavior:

- path positions are strictly increasing;
- repeated characters require a full 157-step carrier revolution;
- SPACE is emitted as a seam event, never deleted;
- decoding is the exact inverse over the public carrier alphabet;
- local recurrence after one circuit does not imply complete oriented return;
- complete oriented return requires two circuits, or 720 degrees.

The modulo operation used to recover a local vertex does not create the origin,
remove the twist, or turn the frame into an unpointed cyclic quotient.

---

## 3. Faces, chirality, and twist

Faces and chirality belong to the public frame. They are not decorative labels
added after a coordinate has been chosen.

The public implementation fixes:

```text
origin / upper public face := +1
lower public face          := -1
clockwise neighbor         := n_plus
counterclockwise neighbor  := n_minus
mirror                     := reflection through fixed origin 0
```

The twist is load-bearing in composition and orientation. Any later theorem
connecting public chirality to the internal factorization face-XOR operation
must be proved from this canon. Boolean XOR identities remain valid Boolean
lemmas, but their public-gonol interpretation is not inferred.

---

## 4. Normalized recursive factorization objects

`ucns.canonical.UCNSObject` implements a separate internal representation:

```text
UCNSObject(n_dec, n_min, A_plus, F_plus)
```

It provides:

- ordered host cells;
- recursive optional payloads;
- internal rational values;
- object-relative normalization;
- face-bit data;
- recursive multiplication;
- quotients, factor search, stable serialization, and evidence records.

This representation remains useful and substantially implemented. It is not the
public gonol and may not move, redefine, or substitute for the public origin.

The internal singleton object used as multiplication identity is a
**factorization-unit object, not public SPACE/ZERO**.

Object-relative first-cell normalization is therefore scoped as:

```text
normalization applies to normalized factorization objects
normalization does not apply to the public gonol
normalization does not establish the system origin
```

---

## 5. Internal multiplication and factorization

The existing recursive product is:

```text
A ⊠ B = P
```

within the normalized factorization model. The implementation composes ordered
host cells, internal values, face bits, and recursive payloads.

Related operations are:

```text
left_quotient(P, A)  -> B where A ⊠ B = P
right_quotient(P, B) -> A where A ⊠ B = P
factor_search(P)     -> factors or a scoped negative result
```

These are not yet proved to be the public-gonol composition law. In particular,
no current theorem proves that internal multiplication preserves:

```text
fixed SPACE/ZERO origin
Möbius twist
orientation after one circuit
720-degree complete return
public faces and chirality
lifted seam crossings
```

That bridge remains `hmmm`.

---

## 6. Carrier terminology

Two carrier notions must not be flattened:

### Public carrier

The public carrier is the exact 157-position twist-bearing gonol.

### Internal projected `n_min`

The factorization model computes `n_min` from denominators of an internal
projected value. Carrier-LCM is currently proved for that exact definition on
its declared normalized-object domain.

Therefore:

```text
Carrier-LCM theorem
    = theorem about internal projected n_min
    != theorem about the complete public carrier
```

A public-carrier theorem requires a bridge that preserves the origin, twist,
orientation, faces, chirality, and 720-degree return.

---

## 7. Equality and identity

Public-frame identity and internal-object equality are separate questions.

### Public-frame identity

The public frame is identified by the exact canon:

- source commit;
- 157-position arrangement;
- fixed position-zero twist/origin;
- faces, chirality, adjacency, mirror;
- origin-preserving private transforms;
- lossless lifted traversal.

### Internal factorization equality

The internal model distinguishes exact structure, normalized sequence equality,
presentation/carrier compatibility, and codec semantics according to its
implemented policies.

An internal equality or normalization theorem cannot silently imply equality of
public frames.

---

## 8. Serialization and stable identity

UCNS needs separate canonical records for separate surfaces.

### Public gonol

The public-gonol identity is pinned by its source provenance, exact arrangement,
fixed origin, and behavior contracts.

### Normalized factorization object

`ucns.serialization` canonically serializes normalized recursive objects for
hashing, retrieval, evidence, and cross-repository records.

A future bridge record must state what information is preserved or lost. It may
not encode the public frame by inventing an angle formula.

---

## 9. Primality and Theorem N

Primality and Theorem N currently belong to the normalized recursive
factorization model.

```text
P is prime in domain D iff no non-unit internal A, B in D satisfy A ⊠ B = P
```

`SEQ-PRIME` remains domain-relative unless completeness is proved for the exact
declared factorization class.

Theorem N remains `FRONTIER`. Its Lean completeness statements remain
`sorry`-backed. Even after those holes are discharged, the result does not become
a theorem about the complete public gonol unless the public/factorization bridge
is also proved.

---

## 10. Geometry and measurement firewall

The public gonol is the UCNS frame. This does not make every geometry,
visualization, embedding, or EDCM metric a theorem of that frame.

The current `(rho, lambda, theta, z, w)` geometry bridge is a compatibility
projection of normalized factorization objects. It is not the public frame and
does not recover the twist origin.

EDCM and edcmbone remain downstream measurement systems. No UCNS theorem status
transfers to their empirical outputs without a separately implemented and proved
status-preserving bridge.

---

## 11. Canonical status summary

| Surface | Current status |
|---|---|
| Exact public gonol arrangement and fixed origin | `IMPLEMENTED` + `TEST-BACKED` after green promotion CI |
| Public lifted traversal | `IMPLEMENTED` + `TEST-BACKED` after green promotion CI |
| Public origin and 720-degree return formal definitions | intended sorry-free; `lake build` is authority |
| Normalized recursive factorization engine | `IMPLEMENTED` + domain-scoped test/proof statuses |
| Carrier-LCM | sorry-free for internal projected `n_min`; not public-carrier theorem |
| Theorem N completeness | `FRONTIER`; `sorry`-backed |
| Public-gonol ↔ normalized-factorization bridge | `hmmm` |
| UCNS theorem ↔ EDCM measurement transfer | forbidden absent a proved bridge |

---

## Reopening rule

No document, test, or implementation may reintroduce any of these as canon:

- an arbitrary or movable system origin;
- public zero chosen from the first normalized cell;
- 360 degrees as complete return;
- public zero placed at an inferred continuous angle;
- `k/157` or `2k/157` as the defining public coordinate;
- factorization unit identified with public SPACE/ZERO;
- Carrier-LCM or Theorem N claimed for the complete public gonol without a
  bridge proof.

## hmmm

The public frame is fixed. The internal algebra is retained. The missing bridge
is now an explicit scientific obligation rather than an assumed equivalence.
