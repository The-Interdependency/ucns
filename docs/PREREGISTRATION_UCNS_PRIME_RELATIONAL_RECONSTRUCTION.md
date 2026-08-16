# UCNS prime-cardinality relational reconstruction adversary

Date: 2026-08-16
Status: frozen preregistration; H1/H2/H3 unrun

## Decision and standing

This program tests one bounded architectural claim: four independently encoded
prime-cardinality relational views contain complementary information that
recovers a single erased source relation, every view remains irreducible under
whole-view removal, and the four-view family outperforms the simplest
matched-information typed-block representation.

The experiment is falsification-first. `FALSIFIED`, `SURVIVED`, `UNRESOLVED`,
`BLOCKED`, and `DEPRECATED` are the only status values. A failed prerequisite
blocks dependents; a falsified dependency propagates downstream before any
repair. No criterion, representation, hint, threshold, or algorithm may change
after a result is observed.

This use of `P2`, `P3`, `P5`, and `P7` means **prime-cardinality relational
view** in this experiment. It does not assert that the new P2/P3 encoders are
the projected geometric primitives, link diagrams, or topological objects in
the existing P5/P7 program. Existing P5/P7 exact distinction remains a bounded
`SURVIVED` result and does not validate reconstruction.

## Work graph

| Participant | Exact identity | Authority and relation |
|---|---|---|
| UCNS | `The-Interdependency/ucns@123495018f50ef63697de7f8e0d15f1dc9e826b2` | owns relational encoders, reconstruction algorithms, controls, H1/H2/H3 evidence, and failure propagation |
| EDCM | `The-Interdependency/edcm@02f71b5610512108066bc91c40f6055b44ba32e4` | owns frozen normalized recovered-dissonance candidate and its controlled result; consumed only if H1–H3 survive |
| skill-lib | `The-Interdependency/skill-lib@6ef2e4c123225f9db20e5230e5894c9c86b42ee6` | build, cross-repository, action-sizing, semantic, and evidence discipline |
| UCNS PR #196 | commit `123495018f50ef63697de7f8e0d15f1dc9e826b2` | external-evaluation transport and reconciliation only; not measurement validity |

Authority, theorem/proof status, certification status, semantic authority,
measurement validity, and empirical validity do not transfer. The graph digest
is an identity check, not a signature.

## Source fixture and non-leakage boundary

The source is one hand-authored typed directed graph with anonymous nodes
`n0` through `n17` and exactly seventeen ordered edges. Edge identities expose
only group and ordinal. Relation values lie in the field `F_257` and are:

```text
G2 = [19, 241]
G3 = [7, 113, 229]
G5 = [3, 47, 89, 173, 251]
G7 = [11, 31, 67, 101, 149, 197, 239]
```

For group `Gp`, edge `Gp/rj` is `n_k -> n_(k+1)` in the displayed concatenated
order and has type `declared-relation`. Values are payload, never identity.
Public edge identity is SHA-256 of canonical JSON containing only schema,
source node, target node, relation type, group, and ordinal. Source values,
checksums, hidden values, outcome status, and reconstruction candidates are
forbidden from identity metadata. A mutation check must prove that changing a
value does not change public identity.

The fixture is development-only, authored before execution, and carries no
external or sealed outcome label.

## Frozen independent encoders

All arithmetic is exact modulo `257`. Each encoder reads the source fixture
directly and may not read another encoded view. Every view contains its own
direct block plus one checksum for the preceding view in this fixed cycle:

```text
P2: direct G2; checksum sum(G7) mod 257
P3: direct G3; checksum sum(G2) mod 257
P5: direct G5; checksum sum(G3) mod 257
P7: direct G7; checksum sum(G5) mod 257
```

The encoders are separate functions with no shared encoder helper beyond
field admission and canonical serialization. Their byte outputs and SHA-256
identities must reproduce exactly.

P2 is thereby explicit and reproducible. P3 is a direct source-native
construction, not a restriction, projection, or transformation of P5/P7.

## H1 — single-relation reconstruction

For every one of the seventeen source relations, erase its value from its
owning view while leaving all other encoded cells unchanged. The primary
algorithm obtains the complementary checksum from the next view and computes:

```text
hidden = checksum - sum(other direct values in the erased relation's group)
         mod 257
```

Admission requires exactly one field element candidate and exact equality to
the fixture value. Wrong recovery, zero candidates, more than one candidate,
identity leakage, encoder drift, or incomplete erasure coverage is
`FALSIFIED`. Infrastructure or arithmetic inability is `BLOCKED` or
`UNRESOLVED` as applicable.

Independent replay may not call the primary reconstruction function. It must
enumerate all `257` possible hidden values and retain those satisfying the
complementary checksum. Candidate sets and recovered values must match exactly.

H1 is `SURVIVED` only if all 17 erasures pass both implementations.

## H2 — whole-view irreducibility

H2 runs only after H1 survives. Remove P2, P3, P5, and P7 independently. For
each removal, enumerate source assignments consistent with every retained
direct cell and checksum. The omitted view is irreducible when at least one of
its directly owned source relations has two or more admissible values across
consistent assignments.

Every view must be irreducible. If any omitted view still admits unique
reconstruction of all seventeen source relations, that view is globally
redundant and H2 is `FALSIFIED`. Independent replay uses a symbolic degree-of-
freedom calculation over `F_257` rather than the primary constructive pair of
alternative assignments.

## H3 — simplest matched-information baseline

H3 runs only after H1 and H2 survive. The baseline is a typed-block erasure
code with four anonymous blocks `B0..B3`, direct block sizes `2,3,5,7`, the
same field, the same source partition, and the same cyclic next-block checksum
placement. It receives exactly 21 field cells, the same 17 public edge
identities, the same four block identities, and the same reconstruction
algorithm class. It carries no primality test, prime label, prime-specific
mapping, geometric primitive claim, or prime-family dispatch.

Both systems face the identical 17 H1 erasures and four H2 leave-outs.
Information matching is exact by field-cell count and public identity count.
The frozen comparison tuple is:

```text
(H1 exact recoveries, H2 irreducible leave-outs,
 encoded field cells, semantic control fields, encoder dispatch branches)
```

The prime family survives H3 only if it has strictly more H1 recoveries or H2
irreducible leave-outs than the baseline without exceeding its information
budget. Equal or worse reconstruction with a baseline having no more encoded
cells and strictly fewer semantic control fields or dispatch branches is
`FALSIFIED`. Runtime speed is reported but is not a decision criterion.

## Resource bounds and failure behavior

- Python 3.11 or newer; standard library only.
- Exact integer arithmetic; no floating point.
- At most 17 H1 erasures, 257 replay candidates per erasure, and four H2
  leave-outs.
- Wall-clock bound: 30 seconds per complete implementation on one CPU.
- Memory bound: 256 MiB.
- Deterministic canonical JSON; two complete runs must be byte-identical.
- Any out-of-field value, duplicate identity, missing cell, checksum mismatch,
  resource-limit breach, or preregistration drift fails closed.

## Frozen propagation and stopping rules

1. Prerequisites must validate before H1.
2. H1 failure records the counterexample, marks H2/H3 and every later
   reconstruction-dependent adversary `DEPRECATED`, and declares the joint
   architectural claim `FALSIFIED`.
3. H2 failure records the redundant view, marks H3 and later dependent work
   `DEPRECATED`, and declares the architecture `FALSIFIED`.
4. H3 failure records the matched baseline comparison, deprecates multi-loss,
   recursive, scale, modality, external-fixture, EDCM-external, and joint-path
   escalation as incapable of rescuing the stated prime-specific advantage,
   and declares the architecture `FALSIFIED`.
5. Only H1/H2/H3 survival permits the later adversarial and EDCM program.

No locally surviving result is erased by a downstream failure. Existing P5/P7
distinction and normalized EDCM controlled recovery remain bounded local
results.

## Usage guidance

After the implementation is committed, run it twice from a clean checkout:

```bash
PYTHONPATH=src python -m ucns.prime_relational_reconstruction \
  --repository-root . --output /tmp/prime-relations-a.json
PYTHONPATH=src python -m ucns.prime_relational_reconstruction \
  --repository-root . --output /tmp/prime-relations-b.json
cmp /tmp/prime-relations-a.json /tmp/prime-relations-b.json
```

The report is architectural experiment evidence only. It must not be imported
as UCNS canon or treated as EDCM validation.

## hmmm

These controls can falsify prime-specific reconstruction advantage, but cannot
establish that the fixture's finite-field coding resembles natural multimodal
relations. External authorship, modality semantics, temporal sampling, outcome
authority, and joint construct validity remain gated behind H1–H3.
