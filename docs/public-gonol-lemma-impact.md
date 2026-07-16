# Public-gonol canon: impact on UCNS lemmas

## Load-bearing canon

The correction is foundational:

```text
public-gonol position 0 = SPACE = ZERO
position 0 = Möbius twist point = seam = system origin
origin is fixed and irreducible
one 360-degree circuit changes orientation
complete return requires 720 degrees
```

The public gonol is canon for all UCNS. It is not an application glyph table and
is not an arbitrary coordinate frame.

## What caused the scope error

The existing recursive factorization implementation normalizes an ordinary
`UCNSObject` relative to its first host angle. That object-relative operation was
flattened into a system-wide origin story. It must not be applied to the public
gonol, whose origin is already fixed by the twist.

The correction therefore separates:

```text
public gonol
    fixed global frame and twist origin

normalized UCNSObject
    internal recursive factorization representation
```

No bridge between those surfaces is assumed.

## Lemmas that remain reusable as written

These are internal combinatorial or arithmetic facts whose proof terms do not
select the system origin:

- row-major product-list lengths;
- first-row and tail-list extraction;
- generic `Nat.lcm` fold divisibility;
- generic rational denominator divisibility;
- recursive payload radius;
- top-level breadth;
- first-level payload-fork counts;
- Boolean XOR cancellation as a Boolean theorem;
- finite catalogue enumeration and exact recomposition predicates.

Their interpretation remains internal unless separately bridged to the public
gonol.

## Lemmas that remain valid only after explicit scope narrowing

### Normalized factorization identity

The existing singleton zero-angle object may remain the two-sided identity of the
normalized factorization monoid. It is not thereby the public SPACE/ZERO twist
origin.

### Idempotents and local groups

Existing zero-angle tower, idempotent, local-group, and internal-subgroup results
may remain statements about normalized factorization objects. Their local zero
must not be renamed or interpreted as the public origin.

### Carrier-LCM

The sorry-free Lean theorem proves the LCM law for the current `nMin` definition,
which is based on denominators of projected internal circle fractions. It is not
without an additional theorem the complete carrier law for the twist-bearing
public gonol.

### Theorem N family

The finite search and its `sorry`-backed completeness statements quantify over
the normalized recursive factorization model. Even after the proof holes are
closed, they do not establish completeness for the complete public-gonol system
unless a faithful origin/twist-preserving bridge is proved.

### Geometry bridge

The existing `(rho, lambda, theta, z, w)` projection is a diagnostic projection
of normalized objects. It is not the canonical public-gonol frame and must not
claim that its circular mean recovers the twist origin.

## Interpretations that are rejected

The following are not UCNS canon and must not return:

- public zero chosen from the first anchor;
- public zero located at an inferred `theta = 0` or `theta = 2π`;
- 360 degrees treated as complete system return;
- the public gonol treated as globally gauge-shiftable;
- `k/157`, `2k/157`, or another continuous formula treated as the defining
  public-gonol coordinate;
- the ordinary factorization identity identified with SPACE/ZERO;
- face XOR claimed to follow from an invented continuous seam model;
- Carrier-LCM or Theorem N described as a theorem about the full public gonol
  without a bridge proof.

## Formal repair present in this branch

`formal/Ucns/PublicGonol.lean` records and proves the immediate canon facts:

```text
position zero uniquely identifies origin
one circuit preserves local position and changes orientation
two circuits preserve local position and restore orientation
720 degrees is two 360-degree circuits
360 is not the mod-4 complete return
720 is the mod-4 complete return
admissible public-frame permutations fix origin
```

These lemmas do not invent a public-vertex-to-angle map.

## Required bridge work before system-wide theorem promotion

A later bridge, specified by Erin, must prove at least:

```text
public twist/origin is preserved
720-degree return is preserved
orientation/chirality is preserved
face information is preserved
lifted traversal and seam crossings are not erased
public composition corresponds to the internal operation used by the theorem
```

Only then can Carrier-LCM, Theorem N, geometry, or local-group results be
promoted from the internal normalized model to claims about the complete UCNS
system.

## hmmm

The internal lemmas are not discarded. They are returned to the domain they
actually proved. The missing public bridge is now an explicit obligation rather
than an invented equivalence.
