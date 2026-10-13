# Recursive carrier successor candidate

This candidate derives successor layer and native Möbius state from an already
validated epicyclic connection. It does not yet establish an origin-attached
recursive carrier: the source schema supplies no Structural Null attachment
witness.

## Law

For an admitted epicyclic connection `e` with placement layer `l`, canonical
radius `r` and complete native Möbius state `M`, the implemented `k`-step
candidate relation is

```text
S_k(e) = (r, l + k, advance(M, k))
```

for positive integer `k`.

A successor step is exactly one visible-lap deck translation. Therefore:

- Structural Null attachment is unresolved. The receipt records
  `origin_attachment: null`; it does not synthesize inheritance from a global
  origin identifier. Establishing and preserving this relation remains a
  requirement for the intended recursive construction.
- Radius is unchanged; depth is not added to radius.
- Visible Möbius phase is unchanged after each whole-lap successor.
- One successor reverses the local frame.
- Two successors restore the complete Möbius state.

The source epicyclic edge must replay exactly from its declared inputs. A
geometric identity cannot seed recursion: coincident nodes, zero radius and
layer, and the complete native identity state are checked after reconstruction.
This also rejects nonzero input aliases such as `(314, 0, 0)`. A one-turn frame
reversal is not mistaken for the two-turn complete return.

## Standing

Candidate only. Version `0.2.0` removes the unsupported inherited-origin claim;
version `0.1.0` receipts are not accepted as evidence for this corrected schema.
The implemented relation uses existing epicyclic, radius-recursion, and native
Möbius primitives. It does **not** establish source origin attachment, identify
a successor as a disk or sphere, prove direct coupling across distant scales,
or ratify the full circle → epicycle → disk → sphere → recursive-scale construction.

## Failure conditions

Construction fails if the source edge is malformed or tampered, if its schema
or version is wrong, if the reconstructed source is a geometric identity, or if the
requested successor depth is not a positive integer. Replay additionally fails
unless the complete record is byte-identical to deterministic reconstruction.

## hmmm

The source construction must supply a Structural Null attachment witness before
an origin-preserving recursive-carrier transition can be claimed. Copying the
singular origin identifier does not supply that geometric relation.

The geometric closure operation that makes a completed successor carrier
specifically a disk, then a sphere also remains unresolved. Neither relation is
imported by declaration.
