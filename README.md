# UCNS — reset at zero

This repository has been reset in public.

The previous seven months of implementation, experiments, specifications,
tests, and formal work are preserved without deletion under
[`archive/`](archive/), with the complete Git history still intact.

That work produced a normalized recursive factorization kernel, but the
type called `UCNSObject` omitted a load-bearing invariant specified at the
beginning of the project: **every UCNS object is a Möbius-twisted carrier,
and zero exists only at its hidden twist/seam**.

This is a foundational object-definition failure, not a cosmetic refactor.
Continuing to patch the old type would preserve the error. The root of the
repository therefore begins again from zero. Archived code may later be
recovered only as an explicitly defined projection of complete UCNS; it is
not to be represented as complete UCNS merely because it compiled, passed
tests, or accumulated proofs.

## Canonical starting constraint

- Every UCNS object is a recursive Möbius carrier.
- Every object has exactly one intrinsic hidden twist/seam.
- The seam is zero.
- Zero is not an anchor, coordinate, ordinary glyph, face bit, empty list,
  first-angle normalization point, or multiplicative identity.
- One circuit returns to the same visible position with reversed orientation.
- Two circuits restore orientation and complete the return.
- Normalization and admissible transformations cannot select, move, erase,
  or expose the seam.
- Every recursive payload is itself a complete twist-bearing UCNS object.

## Current status

There is no current implementation and no system-wide theorem claim at the
repository root. The archive is evidence, history, and potentially reusable
machinery—not the definition of UCNS.

hmmm: the restart is public because the error and the work are public.
