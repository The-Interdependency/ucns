# Recursive carrier successor candidate

This candidate closes one narrow gap in the UCNS construction: how an already
validated epicyclic connection becomes a generator of a successor carrier layer.

## Law

For an admitted epicyclic connection `e` with placement layer `l`, canonical
radius `r`, Structural Null attachment `O`, and complete native Möbius state
`M`, the `k`-step successor is

```text
S_k(e) = (O, r, l + k, advance(M, k))
```

for positive integer `k`.

A successor step is exactly one visible-lap deck translation. Therefore:

- Structural Null attachment is unchanged.
- Radius is unchanged; depth is not added to radius.
- Visible Möbius phase is unchanged after each whole-lap successor.
- One successor reverses the local frame.
- Two successors restore the complete Möbius state.

The source epicyclic edge must replay exactly from its declared inputs. The zero
identity connection cannot seed recursion because it contains no spatial
expansion.

## Standing

Candidate only. This establishes a successor-carrier binding from the existing
epicyclic, radius-recursion, and native Möbius primitives. It does **not**
identify a successor as a disk or sphere, prove direct coupling across distant
scales, or ratify the full circle → epicycle → disk → sphere → recursive-scale
construction.

## Failure conditions

Construction fails if the source edge is malformed or tampered, if its schema
or version is wrong, if the source is the zero identity connection, or if the
requested successor depth is not a positive integer. Replay additionally fails
unless the complete record is byte-identical to deterministic reconstruction.

## hmmm

The next unresolved boundary is no longer “how does a connection advance one
carrier scale?” It is “what geometric closure operation makes a completed
successor carrier specifically a disk, then a sphere, without importing that
identity by declaration?”
