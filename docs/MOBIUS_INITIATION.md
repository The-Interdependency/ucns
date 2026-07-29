# UCNS–EDCM v0.5 Möbius initiation specification

> **Status:** post-reset experiment specification; no carrier relationship, coordinate law, transition law, metric evaluator, or runtime implementation is selected here.
>
> **Scope:** EDCM word-gonol observation and the evidence required to compare a direct Möbius carrier, a directed 720° cover used as a Möbius chart, and formal incompatibility.
>
> **Authority boundary:** this document refines the decided EDCM constraints in [`UCNS_OPTION_DECISIONS.md`](UCNS_OPTION_DECISIONS.md). It does not promote a candidate to UCNS canon.

## 1. Purpose

v0.5 asks one bounded question:

> What evidence must survive so that the relationship between the EDCM Möbius carrier and the implemented directed 720° comparison carrier can be demonstrated or falsified without rewriting the source or choosing a geometry in advance?

The answer is an assignment-and-motion specification, not a metric formula. A conforming experiment must retain the complete trajectory evidence described below before it emits any scalar, radial, or visible projection.

## 2. Declared terms

### 2.1 Structural Null / hidden zero

For the EDCM experiment, **Structural Null / hidden zero** names the singular superpositioned SPACE-origin condition through which a new word gonol initiates.

The current exact profile assigns every code point in its pinned Unicode `White_Space` set to the U+0020 SPACE carrier origin while retaining the exact source value, code point, and offset. Superposition therefore means that distinct source manifestations and boundary roles share one carrier-origin assignment; it does not make those manifestations textually identical and does not authorize normalization, trimming, merging, or deletion.

Structural Null / hidden zero is not interchangeable with:

- U+0030 DIGIT ZERO;
- numeric or algebraic zero;
- a multiplicative unit or neutral product character;
- an absent cell;
- an empty string or missing field;
- `NA`, unknown, unresolved, or unmeasured status; or
- completion of the unknowable itself.

The relation between this EDCM superpositioned origin and the broader UCNS unique-null law is an object of the carrier experiment. A candidate must state that relation explicitly; it may not silently inherit either interpretation.

### 2.2 Gonol and initiation

A **word gonol** is the current profile’s smallest gonol: one maximal ordered sequence of non-SPACE source code points.

A **gonol-initiation event** occurs once at the entrance of every word gonol, before its first non-SPACE source occurrence is assigned to motion. The event is caused by crossing from the Structural Null / hidden-zero interface into that gonol. It is not inferred later from a convenient angular anchor, token value, hash phase, or normalization order.

Each initiation event must retain:

1. the speaker-turn and word-gonol identity;
2. the exact source offset at which the word begins;
3. the immediately preceding boundary occurrence when one exists;
4. the carrier candidate and candidate version;
5. the pre-initiation state;
6. the post-initiation orientation and sidedness state; and
7. a link to the complete source-preserving trajectory.

The first word in a nonempty turn still requires an initiation event. A candidate must declare how the hidden-zero condition is represented at the turn boundary; it may not omit initiation because no literal SPACE precedes the word.

### 2.3 Visible projection and complete state

A **visible projection** is a declared lossy view with 360° period. A **complete carrier state** retains every distinction required by the candidate, including orientation or sidedness that the visible projection may identify.

For a candidate state `s`, a 360° motion and a 720° motion must be distinguishable in the evidence:

```text
visible(advance(s, 360°)) = visible(s)
complete(advance(s, 360°)) != complete(s)
complete(advance(s, 720°)) = complete(s)
```

These are experiment obligations, not an implementation of `advance`. The first relation expresses visible coincidence. The second requires a retained change in orientation, sidedness, sheet, or an equivalent candidate-owned distinction. The third requires complete return under that candidate’s declared state equivalence.

A candidate that cannot define all three comparisons must report `unresolved` or `not-applicable`; it may not substitute a conventional 2π circle and claim a 720° return by repetition alone.

### 2.4 Completion

**Completion** is scoped to the declared carrier construction and boundary. A completion receipt must identify what completed, under which candidate, over which source span, and under which state-equivalence rule.

Completion does not assert that the underlying unknowable has been exhausted. Unknown, unresolved, unmeasured, and out-of-alphabet evidence remain positive evidence and are not coerced to zero.

## 3. Minimum trajectory record

Every candidate experiment must be able to reconstruct the following record for each source occurrence and each gonol-initiation event:

| Field | Required meaning |
|---|---|
| source witness | exact source value, code point, offset, speaker turn, and source identifier |
| carrier assignment | candidate-owned assignment or explicit unresolved status |
| initiation | whether this occurrence begins a word gonol and the causal boundary used |
| lifted motion | complete motion state before and after the occurrence |
| visible motion | declared 360° projection linked to the complete state |
| orientation / sidedness | state that distinguishes the 360° visible return from complete return |
| ordered parentage | word, turn, and any larger gonol parents without flattening |
| boundary evidence | exact SPACE manifestation and its simultaneous token, boundary, and interface roles |
| completion | scoped completion state and receipt, if reached |
| loss declaration | every distinction omitted by a projection |
| status | observed, candidate-derived, unresolved, not-applicable, or error |

No scalar is sufficient as the identity of this record. A scalar may appear only as a projection that links back to the complete record and declares its losses.

## 4. Composition requirements

v0.5 preserves composition evidence without supplying a canonical higher-gonol composition law.

1. Source occurrences remain ordered and multiplicity-preserving.
2. Word gonols compose by declared ordered concatenation at the evidence layer.
3. Left/right sidedness and operand order remain recoverable.
4. Recursive parentage points to prior retained nodes or explicit reference receipts; it is not flattened into an unordered collection.
5. One complete speaker turn contributes one unit of support. Token count, word count, trajectory length, and number of initiation events do not change that support unit.
6. SPACE manifestations remain explicit boundaries even when consecutive, leading, or trailing.

These rules preserve the inputs needed to test a future composition law. They do not define carrier pairing, typed dispatch, metric aggregation, or a complete `UCNSObject`.

## 5. Prohibited substitutions

The following mechanisms may be investigated as historical or comparison evidence but cannot stand in for this specification without a separate proof:

- Blake2-derived or other hash-derived phase assignment;
- fixed phase lanes treated as a derived geometric law;
- ordinary 2π angular fractions treated as complete Möbius state;
- sine-sign chirality treated as the full orientation construction;
- a cylinder-only disk stack treated as the circle/epicycle/disk/sphere law;
- factorization treated as the owner of assignment or completion motion; or
- coherence or metric scalars treated as the complete trajectory.

The primary recovery specimen remains `The-Interdependency/a0-betatest@7af8debf6ef3905f01baff02b43d8c3bee16ccbc`; its invariants are evidence, while its provisional mechanisms remain candidates.

## 6. Usage guidance

A reviewer should use this specification with [`CARRIER_CANDIDATE_MATRIX.md`](CARRIER_CANDIDATE_MATRIX.md) and [`SEPARATING_FALSIFIERS.md`](SEPARATING_FALSIFIERS.md).

A future implementation must name its carrier candidate and version in every experiment manifest. It must fail closed when assignment, state equivalence, or a required retained distinction is unavailable. Passing these obligations makes a candidate reviewable; it does not make the candidate canonical.

## hmmm

The unresolved boundary is the exact law that turns the hidden-zero initiation into a complete, source-preserving motion state. v0.5 deliberately makes that absence inspectable: 360° coincidence must not erase the retained distinction needed for a 720° return, and a plausible diagram must not outrun the causal assignment evidence.