# Separating falsifiers for the Möbius carrier boundary

**Status:** specification-level falsifier suite for issue
[#145](https://github.com/The-Interdependency/ucns/issues/145). These tests
classify candidates; they do not select universal UCNS canon.

## Purpose

The current directed cover, a direct pointed Möbius carrier, and an augmented
cover can all display two visible laps. A useful test must therefore distinguish
their load-bearing structure rather than reward visual resemblance.

Each falsifier below states:

- the competing claims;
- the exact witness;
- what must be retained;
- the exclusion result.

## Evidence sources

Tests may use:

1. current `src/ucns/carrier.py` and its contracts;
2. current exact EDCM word-gonol observations;
3. current completion-motion evidence containers;
4. the pinned a0-betatest recovery manifest and exact blobs;
5. hand-constructed minimal mathematical witnesses.

Historical mechanisms remain evidence, not defaults.

## F1 — one-lap orientation witness

**Question:** Does one 360-degree circuit change an explicitly represented
orientation/sidedness state?

**Witness:** initiate one non-null gonol state `g`, transport it by `2π`, and
compare visible position, lifted state, and orientation witness.

**Required result:**

\[
V(T_{2\pi}(g))=V(g),\qquad K(T_{2\pi}(g))\ne K(g).
\]

The inequality must be evidenced by orientation, sidedness, traversal-half, or
an equivalent causal state—not only by storing `angle + 2π`.

**Excludes:** an ordinary `2π` circle and the bare current cover as a complete
EDCM carrier. The bare cover retains a distinct lifted representative but has no
orientation operation.

## F2 — two-lap local return

**Question:** Does 720-degree transport restore the complete declared local
carrier state?

**Witness:** apply the same declared transport twice.

**Required result:**

\[
K(T_{4\pi}(g))=K(g).
\]

**Excludes:** candidates that require more or fewer than two visible laps or
leave orientation unresolved after the second lap.

**Current evidence:** the directed cover passes lifted-position return. It does
not thereby pass initiation or orientation tests.

## F3 — retained-history non-erasure

**Question:** Does local return incorrectly erase the fact that motion occurred?

**Witness:** compare the complete evidence object before transport with the
evidence object after 720-degree local return.

**Required result:** local carrier state returns; the trajectory receipt gains
ordered motion evidence.

**Excludes:** identity rules that equate “returned after motion” with “never
moved” by discarding causal history.

## F4 — seam invariance

**Question:** Is hidden zero intrinsic or provenance-bearing, rather than a
movable coordinate cut?

**Witness:** reparameterize every angular coordinate by a nonzero constant
offset.

**Required result:** the construction can still identify the same
origin/initiation boundary through intrinsic structure, a marked datum with
provenance, or an invariant equivalence class.

**Excludes:** any candidate whose hidden zero moves merely because numeric angle
zero moved.

**Current evidence:** the bare cover has no intrinsic or marked seam and
therefore fails this test as an EDCM target.

## F5 — Structural Null semantics

**Question:** Does the candidate distinguish singular superpositioned
pre-initiation space from complete absence?

**Witness:** compare:

1. `NA`;
2. no retained occurrence;
3. current coordinate-free absence null;
4. EDCM Structural Null before initiation;
5. an initiated gonol at the origin.

**Required result:** all five states remain distinguishable and migration among
them requires an explicit relation.

**Excludes:** treating the current cover's complete-absence singleton as the
EDCM Structural Null without additional structure and evidence.

## F6 — causal initiation

**Question:** Does a new gonol geometrically initiate through the twist, or does
the implementation merely attach a label?

**Witness:** one exact word gonol and its preceding source-preserved SPACE
boundary.

**Required retained evidence:**

- exact source and span;
- boundary identity;
- pre-initiation Structural Null state;
- initiated carrier state;
- twist/origin event;
- orientation/sidedness initial state;
- declared unresolved assignment law where still unknown.

**Excludes:** a string field alone, a hash-derived position alone, or a carrier
constructor with no source-bound transition.

**Current evidence:** `EdcmWordGonol.initiation_event` is represented evidence,
not a geometric transition.

## F7 — exact source inverse

**Question:** Can the candidate recover the exact source observation after
assignment and motion evidence are attached?

**Witness set:** repeated SPACE manifestations, leading and trailing SPACE,
U+0009, U+000A, U+00A0, repeated tokens, and non-SPACE carrier-unassigned Unicode
scalars.

**Required result:** exact source code points, offsets, order, multiplicity, and
speaker-turn identity reconstruct without normalization.

**Excludes:** first-anchor shifting, whitespace collapse, replacement
characters, deduplication, sorting, or hash-only identity.

**Current evidence:** the EDCM profile passes exact turn reconstruction. This
does not establish the geometric assignment law.

## F8 — `2π` leakage

**Question:** Does any supposedly complete state path normalize modulo `2π`
before orientation and traversal-half evidence are retained?

**Witness:** two states with equal visible position separated by one visible lap.

**Required result:** they remain distinguishable until the declared 720-degree
return condition is met.

**Excludes:** ordinary-circle reduction, Fourier-phase substitution, and any
serialization that stores visible angle as complete identity.

## F9 — Möbius monodromy comparison

**Question:** Does the proposed relationship preserve the characteristic
one-lap state transformation rather than merely two-lap periodicity?

**Witness:** in the standard comparison quotient,

\[
(u,0)\sim(-u,2\pi),
\]

choose `u != 0` and transport one circuit.

**Required result for a claimed faithful chart:** the chart carries an explicit
state corresponding to `u -> -u`, or proves a mathematically equivalent
orientation transformation.

**Excludes:** a preservation claim whose target has only breadth and angle and
therefore forgets the transverse/orientation witness.

This test does not make the standard Möbius quotient the UCNS target. It only
separates monodromy from bare double-period bookkeeping.

## F10 — scoped completion firewall

**Question:** Can a carrier return be mistaken for completion of a larger
construction or exhaustion of the unknowable?

**Witness:** a locally returned word-gonol state inside an incomplete
higher-gonol construction.

**Required result:** local carrier return, higher construction completion, and
underlying unknowable exhaustion remain three distinct claims. The last is
always false in a UCNS completion receipt.

**Excludes:** coherence scalars or local angle return used as universal
completion.

## Candidate result table

| Falsifier | Direct pointed Möbius | Bare directed cover | Augmented chart | Separate/incompatible |
|---|---|---|---|---|
| F1 one-lap orientation | must demonstrate | fails as target | must demonstrate | target-only |
| F2 two-lap return | must demonstrate | passes lifted position | must demonstrate | independently test |
| F3 history retention | must demonstrate | outside carrier state | must demonstrate | target-only |
| F4 seam invariance | must demonstrate | fails as target | must demonstrate | target-only |
| F5 Structural Null | must define | fails as target | must preserve separately | target-only |
| F6 causal initiation | must define | fails | must preserve | target-only |
| F7 source inverse | must bind profile | profile supplies separately | must bind profile | profile remains separate |
| F8 `2π` leakage | must pass | passes lifted distinction | must pass | independently test |
| F9 monodromy | natural comparison, exact law open | fails as target | must preserve | establishes separation |
| F10 completion firewall | must pass | no completion law | must pass | target-only |

## Reproducibility against the current tree

The current evidence boundary can be reproduced without adding behavior:

```text
python -m pytest tests/test_carrier.py tests/test_edcm_profile.py tests/test_edcm_motion.py -q
```

The relevant public-state inspection is deterministic:

- `LiftedCarrierPoint` contains `breadth` and `angle`;
- `deck_translate()` adds one visible period;
- the carrier contract forbids inferred orientation operations;
- `EdcmWordGonol` retains an initiation-event label;
- the completion-motion schema requires externally supplied assignment and
  motion evidence.

Passing those tests confirms the current boundary. It does not make the missing
Möbius initiation executable.

## Closure rule

Issue #145 may close when:

1. the authority and state distinctions in `MOBIUS_INITIATION.md` are accepted;
2. the bare-cover insufficiency result is accepted or disproved with explicit
   retained state;
3. at least one A/C/D relationship survives every applicable falsifier, or the
   remaining incompletion is explicitly recorded;
4. any selected relationship records migration and rollback;
5. no runtime activation occurs merely because the specification merged.

## hmmm

A falsifier earns its keep when two beautiful diagrams stop looking equivalent.
