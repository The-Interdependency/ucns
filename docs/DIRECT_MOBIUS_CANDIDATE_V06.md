# UCNS–EDCM v0.6 native direct-Möbius candidate

> **Status:** implemented experiment-candidate specification for the bounded
> Structural-Null root loop. It supplies evidence for `C1-direct-mobius`; it
> does not select C1, define arbitrary element assignment, establish scoped
> completion, or change EDCM or METAPAT.
>
> **Predecessor:** the candidate-neutral v0.5 specification and executable
> F01–F16 harness.

## I. Purpose and domain

v0.6 asks one narrower question than the complete UCNS carrier problem:

> Can Structural Null initiation and the required 360°/720°/inverse behavior be
> represented by a native Möbius state law without importing the implemented
> directed cover?

The declared domain is the framed central root loop of a Möbius carrier. The
candidate does not yet assign arbitrary public-gonol positions to transverse
coordinates or higher geometry.

## II. Native state law

### 1. Formal object

Measure longitudinal motion in exact rational turns. Let

\[
\widetilde M_0 = \mathbb{Q}\times\{-1,+1\}.
\]

The native framed root loop is the quotient

\[
M_0=\widetilde M_0/\!\sim,\qquad
(t,\varepsilon)\sim(t+n,(-1)^n\varepsilon)
\quad(n\in\mathbb Z).
\]

Here:

- \(t\) is longitudinal phase in turns;
- \(\varepsilon\) is the retained local-frame sign;
- one turn is 360°;
- two turns are 720°; and
- the relation is the Möbius gluing law, not a reference to a cover state.

A canonical representative uses \(p=t-\lfloor t\rfloor\), with
\(0\le p<1\), and frame

\[
\varepsilon'=(-1)^{\lfloor t\rfloor}\varepsilon.
\]

### 2. Motion and inverse

For rational motion \(q\), `advance(q)` adds \(q\) before applying the quotient
relation. Its exact inverse is `advance(-q)`.

For the initiated state \(s=[(0,+1)]\):

\[
\operatorname{visible}(s+1)=\operatorname{visible}(s),
\qquad
\operatorname{complete}(s+1)\ne\operatorname{complete}(s),
\]

because the local frame changes sign, while

\[
\operatorname{complete}(s+2)=\operatorname{complete}(s).
\]

The visible projection retains the rational phase and source link but omits
the local-frame sign. That omission is explicit. A complete state retains the
phase, frame, initiation identity, exact source link, ordered parentage, and
declared construction scope.

### 3. Structural Null

Structural Null is a typed singular carrier-origin identity:

```text
ucns.edcm.structural-null:space-origin
```

It is distinct from numeric zero, U+0030 DIGIT ZERO, the empty speaker turn,
absence, `None`, `NA`, unresolved, unmeasured, and completion.

Every exact SPACE occurrence and every turn-boundary hidden-zero condition is
a distinct **manifestation** linked to this one carrier-origin identity.
Manifestations retain source identifier, code point, and offset when literal
source exists. Sharing the carrier origin never authorizes source
normalization, merging, or deletion.

## III. Initiation law

### 1. Cause

Every word gonol receives exactly one initiation event before its first
non-SPACE occurrence enters motion.

- A word at source offset zero is caused by the turn-boundary hidden-zero
  manifestation.
- A later word is caused by the immediately preceding exact SPACE
  manifestation.
- Leading, repeated, and trailing SPACE occurrences remain distinct evidence
  even when they do not each initiate a word.

### 2. State transition

The pre-initiation state is the typed Structural Null manifestation. The
post-initiation state is the native framed root state \([(0,+1)]\), linked to:

1. speaker-turn and word occurrence identity;
2. exact source start offset;
3. the causal boundary manifestation;
4. ordered parentage;
5. candidate ID and version; and
6. the complete v0.6 evidence packet.

Initiation creates a framed carrier state; it is not inferred from a hash,
visible anchor, normalization order, or the directed cover.

## IV. Examples and separating boundaries

### 1. Minimal example

For exact source `A`, the word begins at offset zero. Its cause is the
turn-boundary Structural Null manifestation. The post-initiation state is
\([(0,+1)]\); 360° yields \([(0,-1)]\); 720° yields \([(0,+1)]\); applying
−360° to the 360° state restores the initial complete state.

### 2. Repeated-SPACE example

For exact source `A  B`, both U+0020 occurrences survive as distinct source
manifestations of the singular origin. The second occurrence is the immediate
cause of `B`'s initiation. The first is retained boundary evidence and is not
deleted merely because it does not independently initiate another word.

### 3. Non-example

The state `(visible phase = 0)` without a retained frame sign is not a complete
native Möbius state. It identifies the 0°, 360°, and 720° states and therefore
fails F06 even though its diagram may repeat every 360°.

## V. Executable evidence and expected verdicts

The v0.6 candidate enters the unchanged v0.5 F01–F16 comparison matrix.

1. It adds bounded C1 evidence for:
   - F01 typed null/zero separation;
   - F03 initiation cardinality and causal boundary;
   - F04 singular seam with exact repeated-SPACE retention;
   - F06 360° visible coincidence with complete-frame change;
   - F07 720° complete root-state return;
   - F08 exact inverse motion; and
   - F14 independence from the directed-cover implementation.
2. It inherits exact-source, unit-support, and nine-display evidence from the
   v0.5 observation floor.
3. It leaves F09 scoped completion unresolved.
4. It does not supply the F12 C1↔C2 map or the F13 incompatibility proof.
5. It does not select, rank, or canonize a carrier.

## VI. Explicit nonclaims

v0.6 does not establish:

- the general element-to-geometry assignment law;
- transverse Möbius coordinates beyond the framed root loop;
- circle→epicycle→disk→sphere transitions;
- higher-gonol composition or recursive scale transition;
- a scoped completion receipt;
- equivalence or incompatibility between C1 and C2;
- canonical structural equivalence, `M`, or `B`;
- EDCM measurement validity or METAPAT validity; or
- runtime activation in either consumer.

## hmmm

The root loop can now twist honestly without pretending to know where every
element travels. The next burden is an explicit C1↔C2 map attempt, not a vote
between two matching 720° pictures.
