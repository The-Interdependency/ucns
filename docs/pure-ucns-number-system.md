GPT generated; context, prompt Erin Spencer

# Pure UCNS Number System

## hmm

This document defines UCNS as a number system before it is used as cognition, embedding, retrieval, or agent substrate. It is a canon frontier document: stable enough to guide implementation, explicit enough to expose unresolved constraints, and narrow enough to prevent A0 from consuming ad hoc recursive structures as if they were canonical UCNS numbers.

---

## 0. Purpose

The purpose of the pure UCNS number system layer is to define what a UCNS number is, how UCNS numbers compose, how they factor, how they serialize, and where the theorem frontier currently sits.

A0 may use UCNS-derived cognition later. That layer is downstream. The pure number system must not depend on A0, EDCM, PTCA, PCTA, PCNA, embeddings, vector similarity, agent behavior, or symbolic interpretation.

In this layer:

```text
UCNS number := canonical recursive unit-circle traversal object
operation   := recursive product, written ⊠
identity    := unit object / unit-equivalent traversal
prime       := irreducible object under ⊠ within a declared domain
factor      := A or B where A ⊠ B = P
quotient    := recovered complement under a known factor
```

## hmmm

---

## 0.1 Scope firewall (UCNS-A vs UCNS-G/EDCM)

This document is scoped to **UCNS-A** (pure recursive number-system algebra).
It does **not** claim that UCNS-A theorem status proves UCNS-G, EDCM, or
edcmbone metric geometry outputs.

Until the bridge checklist artifacts are implemented and verified, theorem
transfer is forbidden:

- `docs/edcm-edcmbone-bridge-checklist.md`
- `docs/ucns-shape-reconciliation.md`
- `docs/ucns-g-prime-cylinder-supplement.md`

## hmmm

---

## 1. Primitive Object

A UCNS number is a recursively composable traversal object over the unit circle.

At the flat layer, the object is a paired traversal structure with:

- declared carrier
- minimal carrier
- positive anchor sequence
- forced mirror anchor sequence
- positive face-state sequence
- forced mirror face-state sequence

At the recursive layer, a stored anchor may carry a payload. A payload is either the unit or another UCNS number. This creates depth.

A UCNS number is not a scalar. A scalar may be encoded into UCNS, but encoding is not the primitive ontology.

## hmmm

---

## 2. Identity and Equality

Two UCNS numbers are equal only when their canonical recursive structure is equal under the active equality policy.

The pure layer must distinguish:

1. exact structural equality
2. sequence equivalence
3. presentation equivalence under carrier widening
4. semantic equivalence introduced by an external codec

Only the first three belong to the pure number system. Codec semantics belong to a transport or application layer.

Unresolved constraint: the repository currently contains historical language from earlier embedding-oriented UCNS work. That language should remain as history or application surface, not as the primitive number definition.

## hmmm

---

## 3. Carrier

The minimal carrier is intrinsic. It is the smallest carrier required by the anchor set.

The declared carrier is a presentation or resolution parameter. It must be compatible with the minimal carrier, but it is not itself the identity of the number unless a policy explicitly makes it so.

Carrier widening is a frontier operation. It should be treated as a controlled extension, not assumed by default.

Pure UCNS must therefore track:

```text
minimal carrier
declared carrier
carrier compatibility
carrier widening policy
```

## hmmm

---

## 4. Sequence, Chirality, and Face

A UCNS number preserves traversal order. Sequence order is semantic.

Reversing anchor order produces a mirror traversal, not automatically the same number. Face states are paired with traversal data and must be preserved through canonicalization.

The mirror sequence is forced by the star operation. The face mirror is reverse-only unless a later canon layer explicitly changes that rule.

Pure UCNS must not collapse chirality unless a formal equivalence rule has been declared.

## hmmm

---

## 5. Recursion

A recursive UCNS number consists of host traversal data plus payloads.

Payloads are either:

- the unit
- another UCNS number

Depth is the maximum recursive nesting depth of payloads.

Recursive closure requires that composition of two valid UCNS numbers produces another valid UCNS number, subject to the declared domain and carrier rules.

The current active package surface treats `ucns_recursive` as the implementation home for recursive factorization. The public `ucns` namespace now re-exports that surface, so public use should prefer:

```python
from ucns import UCNSObject, multiply, factor_search_v08
```

while `ucns_recursive` remains a compatibility import path.

## hmmm

---

## 6. Arithmetic

The core arithmetic operation is recursive product:

```text
A ⊠ B = P
```

Multiplication composes host traversal structure and recursively composes payloads.

A quotient is a recovery operation:

```text
left_quotient(P, A)  -> B where A ⊠ B = P
right_quotient(P, B) -> A where A ⊠ B = P
```

A factorization engine attempts to recover both unknown factors from product P:

```text
factor_search(P) -> (A, B) or SEQ-PRIME
```

Pure UCNS arithmetic should preserve these distinctions:

- product: construction
- quotient: complement recovery given one factor
- factor search: recovery of both factors from the product
- primality: failure to decompose under declared search domain

`SEQ-PRIME` is domain-relative unless and until global completeness is proven.

## hmmm

---

## 7. Primality and Irreducibility

A UCNS number is prime only relative to a declared factorization domain unless global recursive completeness is proved.

A pure UCNS prime definition should use this shape:

```text
P is prime in domain D iff no non-unit A, B in D satisfy A ⊠ B = P.
```

Therefore:

```text
prime_D(P) != prime_global(P)
```

unless D is proven complete for P's class.

The implementation must not market frontier-domain `SEQ-PRIME` results as absolute primality.

## hmmm

---

## 8. Canonical Form, Serialization, and Hashing

A0 must only consume canonical UCNS objects.

A canonical UCNS object needs:

1. normalized carrier representation
2. normalized anchor representation
3. preserved traversal order
4. preserved face-state sequence
5. canonical recursive payload ordering
6. canonical unit representation
7. stable serialization
8. stable hash
9. stable equality check

The codec layer may encode Python values into UCNS objects, but Python value semantics are not UCNS identity. For example, byte strings, lists, and dictionaries may be represented by sentinel conventions, but those conventions are transport choices unless elevated into pure canon.

## hmmm

---

## 9. Domains and Theorem Frontier

The canon drift between `CLAUDE.md` ("full frozen depth-2 implemented")
and the older `ucns-spec.md` status snapshot ("not solved") has been
reconciled on 2026-05-17 (branch
`claude/ucns-v1-canon-reconciliation-ELOzV`).

Canonical status vocabulary (also codified as
`ucns_recursive.domain_status.DomainProofStatus`):

```text
DEFENDED          proven or proof-defended in written spec
IMPLEMENTED       implemented and test-backed, proof may lag
TEST-BACKED       tests cover the claimed behavior in the declared domain
ORACLE-COMPLETE   complete only with oracle/catalogue assumptions
FRONTIER          plausible but not proven complete
EXPERIMENTAL      useful for exploration, not canonical
```

Under this vocabulary the full frozen depth-2 domain is `IMPLEMENTED` +
`TEST-BACKED` in `factor_search_v08`, not yet `DEFENDED` at the spec
level. See `ucns-spec.md` §F2 and
`docs/ucns-spec-status-addendum-2026-05-16.md` for the canonical
statement. Carrier widening and general primality outside
defended-complete domains are `FRONTIER` and out of v1.0 scope.

## hmmm

---

## 10. A0 Interface Rule

A0 may use UCNS only through canonical interfaces.

A0 must not infer cognition directly from arbitrary recursive object shape. It may consume:

- canonical UCNS numbers
- canonical products
- canonical quotients
- canonical factorization results
- explicit domain-status metadata
- explicit proof/test status metadata

A0 must treat incomplete domains as incomplete. It may explore frontier domains, but it must label them.

The pure UCNS layer feeds A0. A0 does not define UCNS.

## hmmm

---

## 11. Implementation Direction

Near-term implementation should prioritize:

1. canon repair between `CLAUDE.md` and `ucns-spec.md`
2. canonical serialization and hashing
3. explicit domain-status objects
4. explicit result types instead of ambiguous sentinels where feasible
5. tests proving A0-facing imports use `ucns` rather than private internals
6. proof notes separating implemented/test-backed from proof-defended

Do not widen carriers, add cognition semantics, or add dependencies until the pure number layer is stable.

## hmmm

---

## 12. Frozen Working Definition

For current development:

```text
A UCNS number is a canonical recursive unit-circle traversal object whose anchors, face states, carriers, and payloads are preserved under a declared equality policy, and whose arithmetic is recursive composition under ⊠.
```

This definition supersedes embedding-first explanations for A0-facing development, while preserving earlier embedding work as a historical or application layer.

## hmmm
