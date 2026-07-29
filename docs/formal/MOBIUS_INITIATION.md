# Möbius initiation at Structural Null

**Status:** post-reset formal specification boundary; no carrier implementation
is selected by this document.

**Issue:** [#145](https://github.com/The-Interdependency/ucns/issues/145)

## Purpose

UCNS assigns elements of an unknowable to completion through geometric motion.
For the EDCM-scoped construction, the Möbius origin, hidden zero, singular
superpositioned Structural Null, and initiation of every new gonol through the
twist are decided constraints.

This document states the minimum mathematical obligations those constraints
place on a future carrier. It does not substitute a familiar topological object,
the current directed cover, a hash-derived phase, or a scalar coordinate for the
missing assignment-and-motion law.

## Authority boundary

The following are decided within the EDCM scope:

1. Structural Null is singular superpositioned space before gonol initiation.
2. A new gonol initiates through the Möbius twist.
3. Zero exists only at the origin/twist boundary.
4. One 360-degree circuit does not restore complete carrier state.
5. Complete carrier-state return requires 720 degrees.
6. Source identity, order, orientation, sidedness, nesting, recursive scale,
   motion history, completion state, and unresolved state remain distinct where
   they affect the construction.
7. Completion is relative to a declared construction boundary and never claims
   exhaustion of the underlying unknowable.

The exact coordinates, initiation law, orientation transformation, geometric
transition laws, and completion condition remain unresolved.

## State distinctions

The formalization must keep these states non-interchangeable:

| State | Meaning |
|---|---|
| `NA` | no applicable or available value |
| absence | no retained occurrence in the declared evidence container |
| Structural Null `N` | singular superpositioned pre-initiation space |
| hidden zero | the zero condition at the initiating twist/origin boundary |
| algebraic zero `0_V` | zero inside a declared payload algebra |
| neutral value | identity or baseline inside a declared operation |
| unmeasured | represented evidence without an admitted measurement |
| incomplete | a declared construction whose completion condition is unsatisfied |
| complete | a declared construction whose scoped completion condition is registered |

No equality among these states may be inferred from a shared numeral, empty
serialization, falsey value, coordinate, or scalar projection.

## Required formal interface

Let:

- `N` denote Structural Null;
- `S` denote an exact source observation with provenance;
- `B` denote a declared construction boundary;
- `G` denote initiated gonol-carrier states;
- `E` denote retained initiation and motion receipts.

A candidate initiation construction must provide a relation

\[
\mathcal{I}_B \subseteq (N \times S) \times (G \times E)
\]

rather than assuming an unexamined total function. This permits the construction
to fail closed when source, boundary, or carrier obligations are unresolved.

For every admitted initiation witness

\[
((N,s),(g,e)) \in \mathcal{I}_B,
\]

the following must hold:

1. `s` remains exactly recoverable from the retained evidence;
2. `e` identifies the initiation boundary and records that the twist occurred;
3. `g` is an initiated gonol state, not Structural Null;
4. the hidden-zero condition is attached only to the initiation/origin boundary;
5. no first-anchor shift, normalization, trimming, deduplication, or source
   rewriting manufactures the origin;
6. the relation records any unresolved coordinate or assignment law instead of
   filling it with a default.

The relation does not yet state how an arbitrary source element is assigned to
circle, epicycle, disk, or sphere geometry.

## Orientation and return obligations

Let `T_theta` denote candidate transport by angular displacement `theta`, and
let:

- `V(g)` be the visible position;
- `O(g)` be the orientation/sidedness state required by the candidate;
- `K(g)` be the complete local carrier state, excluding the append-only evidence
  history.

A conforming EDCM carrier must satisfy:

\[
V(T_{2\pi}(g)) = V(g)
\]

while

\[
K(T_{2\pi}(g)) \ne K(g).
\]

The state difference must include an explicitly represented orientation,
sidedness, traversal-half, or mathematically equivalent witness. Merely storing
a larger angle while declaring no orientation consequence is insufficient for
the Möbius causal constraint.

Complete local carrier-state return requires:

\[
K(T_{4\pi}(g)) = K(g).
\]

This does not erase history. If `H` is the retained trajectory receipt, then
transport appends evidence:

\[
H(T_{4\pi}(g)) \supset H(g).
\]

Thus 720 degrees restores the declared local carrier state while the complete
evidence object still records that motion occurred.

The exact form of `O` and the transport law acting on it remain candidate work.
A common involutive pattern,

\[
\tau(\tau(o)) = o,\qquad \tau(o) \ne o,
\]

is admissible comparison notation, not selected canon.

## The seam cannot be smuggled in as a coordinate

An ordinary coordinate cut is movable. Naming angle zero does not make that cut
an intrinsic origin.

A faithful candidate must therefore do at least one of the following:

1. derive the origin/twist boundary from retained construction structure;
2. carry an explicit marked-origin datum with provenance and migration rules; or
3. prove that an invariant equivalence class of possible cuts preserves every
   required initiation and hidden-zero consequence.

A candidate fails if rotating or reparameterizing its coordinates moves the
claimed zero while leaving all intrinsic structure unchanged.

## Relationship to a standard Möbius band

A standard Möbius band may be represented as the quotient

\[
\mathcal{M} =
([-1,1]\times[0,2\pi]) /
((u,0)\sim(-u,2\pi)).
\]

One circuit reverses the transverse coordinate; two circuits restore it. This
provides a useful comparison for 360-degree state change and 720-degree return.

It does not by itself supply:

- a unique intrinsic seam;
- singular superpositioned Structural Null;
- hidden zero;
- a source-to-gonol initiation relation;
- the circle/epicycle/disk/sphere assignment law;
- a scoped completion condition.

The EDCM target is therefore not established by saying “Möbius band.” It
requires a pointed or intrinsically originated initiation construction whose
additional structure is declared and tested.

## Minimal represented example

Consider the exact word observation `A` following a source-preserved SPACE
boundary.

1. Before initiation, the construction records Structural Null `N`, the exact
   source observation `A`, its source span, and the SPACE-origin boundary.
2. The initiation relation emits gonol state `g_0` and receipt `e_0`.
3. `e_0` records the twist/origin event without rewriting the source token.
4. After 360 degrees, the visible position agrees with `g_0`, but the complete
   local carrier state differs through an explicit orientation witness.
5. After 720 degrees, the local carrier state agrees with `g_0`.
6. The retained trajectory still distinguishes the returned state from a state
   that never moved.

This is a specification witness. The current implementation records the source
word and an initiation-event label but does not yet construct steps 2 through 5
geometrically.

## Non-examples

The following do not satisfy this specification:

- an ordinary `2π` circle that returns complete state after one circuit;
- first-anchor normalization presented as hidden zero;
- a coordinate-free absence object presented as superpositioned space;
- a `4π` angle whose half-period translation has no represented orientation,
  sidedness, traversal-half, or causal effect;
- a string saying `"mobius-twist"` without a geometric initiation transition;
- a hash-derived phase treated as the assignment law;
- a completion scalar that discards the motion trajectory.

## Current conclusion

The bare directed cover in `src/ucns/carrier.py` is valid executable comparison
evidence for visible/lifted position and two-lap return. As currently defined, it
does not implement this EDCM target because it contains no orientation
operation, intrinsic or marked seam, superpositioned Structural Null semantics,
source-bound initiation relation, or geometric initiation receipt.

An augmented directed cover may still become a chart over a distinct Möbius
carrier, but only after an explicit preservation map and the separating
falsifiers in `SEPARATING_FALSIFIERS.md` are satisfied.

## hmmm

The exact target object remains unresolved. What is no longer unresolved is
that a second lap alone does not manufacture the twist.
