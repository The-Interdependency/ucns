# Visible-circle displacement law — preregistration v0.5

## Standing

```text
status: INCUBATING / UNRESOLVED
canon: false
core: false
selected: false
```

This document freezes the current research boundary for the missing UCNS
geometric operation that would map declared evidence residues onto the
visible Public Gonol circle and the native Möbius frame. No law is asserted
here; the preregistration exists so a later candidate can be compared,
falsified, replayed, and ratified without redefining the problem.

## Why this boundary exists

English Gonol Construction has completed a full-corpus construct in which
every definition carries three distinct evidence channels, each reducible to
exact integer residues by the consumer:

```text
ordinal evidence          -> source order of a word's definitions
semantic evidence         -> resolved OEWN sense/synset relations
sentence-context evidence -> exact ordered word/whitespace components
```

The consumer declares the resolution rule as:

```text
preponderance relative to the rest of the sentence in which the word appears
```

UCNS owns only the geometric step that turns already-reduced residues into
displacement. UCNS does not read the English evidence, does not interpret
"preponderance," and must not invent a numeric weight to stand in for the
missing geometric operation. The consumer is responsible for reducing its
evidence channels to exact residue inputs; UCNS is responsible only for the
geometry that consumes them.

## Construct and describing graph

Two geometric objects are held separate, are never merged, and do not share
an origin:

```text
157-axis construct
    origin -> the 157 Public Gonol glyphs, each an orthogonal axis
    status -> the thing being created

3-axis describing graph
    axes   -> x, y, z
    status -> an external graph that describes the construct
    origin -> its own; it does NOT share the construct's origin
```

The evidence residue channels `x`, `y`, `z` live on the 3-axis describing
graph. They are not axes of the 157-axis construct.

## Admissible relation class between construct and describing graph

A candidate relation between the 157-axis construct and the 3-axis describing
graph is admissible only if it:

```text
maps construct positions to describing-graph positions exactly
  (157 glyph axes -> x, y, z)
keeps the two origins distinct; no shared origin is ever assigned
records the mapping as its own named candidate with falsifiers and replay
uses exact rational arithmetic only; no floating point in the core
replays byte-identically from a canonical receipt
fails closed on malformed construct axes or describing-graph axes
```

A candidate relation is not admissible if it:

```text
merges the two origins or declares a shared origin
treats the describing-graph axes as axes of the construct
derives construct geometry from graph rendering choices
invents weights, scores, or probabilities for the mapping
claims ratification from execution alone
```

## Radius semantics

For English gonols, radius does not mean character or token count and does not
mean ordinal position in the text:

```text
angular/axis position -> carries sequence/order
radius               -> carries recursive construction depth
```

Letters occupy the base shell. Affixiated letters close into a lexical gonol
on the next shell. Words affixiate into larger constructions on subsequent
shells. Repeated occurrence of the same word does not create a new radial
identity; occurrence and order belong to the relational (angular) geometry.
Spaces and boundaries trigger construction closure; they do not add
arbitrary radial distance.

The minimal rule under test is:

```text
r(x) = r0 + d(x)
```

where ``d(x)`` is the number of completed recursive affixiation/containment
levels from the 157-glyph substrate, not the ordinal position in the text.

Derived result (candidate): the open test is answered by the established
carrier primitives. UCNS scale recursion supplies the layer recursion, and
radius is the canonical radial map on breadth:

```text
radius(x) = radius_from_breadth(breadth(x))
layer(d)  = d deck translations in the lifted carrier
```

Each completed construction layer is one deck translation: the lifted
representative advances one visible lap, the visible projection is unchanged,
and two laps complete the return. Radius does not advance per layer. The
English ``r(x) = r0 + d(x)`` candidate is therefore superseded; ``d(x)``
counts deck-translation steps, not additive radial units. See the executable
``ucns.radius_recursion`` candidate and its tests.

## Existing primitives available to a candidate

A candidate displacement law may compose only established UCNS primitives:

| Primitive | What it already provides |
|---|---|
| `public_gonol` | exact 157-position Public Gonol carrier; `r -> position` |
| `modular_orbit` | finite modular action `x -> a*x mod m`, exact disjoint cycle decomposition, exact circle positions `r/m` turns |
| `gonal_boundary_trace` | visible-circle wave trace, gonal boundary samples at `r/m`, continuum covering pullback `r -> d*r mod m` with explicit degree `d` |
| `direct_mobius` | native framed Möbius quotient `(t, ε) ~ (t + n, (-1)^n ε)`; 360° visible return flips the local frame, 720° restores complete state |
| `carrier` | visible period `2π`, lifted period `4π`, unique Structural Null |

A candidate may also declare a new exact operation, but only through a named,
bounded construction with its own falsifiers and replay.

## Admissible law class

A displacement-law candidate is admissible only if it:

```text
accepts three exact integer residue channels (ordinal, semantic, context)
produces exact Fraction turns on the visible circle (r/157 positions)
returns a NativeMobiusFrame state for every output displacement
preserves the 360/720-degree native Mobius return law
uses exact rational arithmetic only; no floating point in the core
replays byte-identically from a canonical receipt
records a declared continuum covering degree d whenever a multiplier a is used
  with d ≡ a (mod 157)
fails closed when residues are malformed, the carrier is not a permutation,
  or the frame state is outside the canonical quotient
```

A candidate is not admissible if it:

```text
assigns weights, scores, or probabilities to evidence channels
derives direction or distance from Unicode names, dictionary meanings,
  or conventional punctuation grammar
silently selects one continuum lift d from the class d ≡ a (mod 157)
relabels a non-bijective functional graph as cycle geometry
claims ratification from execution alone
```

## Required controls

Any candidate must be compared against declared controls:

```text
null control          -> all three residue channels set to zero/neutral
single-channel control -> one channel nonzero, the other two neutral
pair controls         -> each pair of channels active independently
permutation control   -> the same residues under a known modular orbit action
frame control         -> one full visible turn must flip the frame; two must restore it
```

## Evidence required before stronger standing

```text
declared falsifiers that could refute the candidate;
an exact canonical receipt;
an independent complete replay agreeing byte-for-byte;
a recorded continuum covering degree d and its congruence class;
a scoped ratification receipt. None of these exist yet.
```

## Explicit hmmm

- The displacement law itself remains unconstructed.
- The exact composition rule for the three evidence residues is unresolved.
- The exact geometric relation between the 3-axis describing graph and the
  157-axis construct is unresolved beyond: the graph describes the construct
  and does not share its origin.
- The law selecting one continuum lift `d` from `d ≡ a (mod 157)` is unresolved.
- The lift from the visible 360° circle into the complete 720° native Möbius
  state (frame information included) is unresolved.
- The exact radius/scale transition is recovered as a UCNS-derived candidate:
  radius = radius_from_breadth(breadth), layers = deck translations;
  ratification of that recovery remains hmmm, and it is not an
  English-specific constant.
- Whether the Public Gonol function positions themselves participate in the
  displacement or only carry it remains unresolved.
