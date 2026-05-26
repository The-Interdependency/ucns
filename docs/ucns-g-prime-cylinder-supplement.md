# UCNS-G Prime-Cylinder Supplement to Shape Reconciliation

**Status:** Supplements `docs/ucns-shape-reconciliation.md` (PR #21). Does not modify
the PARALLEL verdict between UCNS-A and UCNS-G. Updates the UCNS-G side only.
**Date pinned:** 2026-05-22
**Companion handoff:** `edcmbone:docs/handoffs/2026-05-22-ucns-g-prime-cylinder-v3.md`
and the mirrored copy in `erinepshovel-code` (EDCM / UnitCircle).

## 0. Firewall preserved

This supplement does **not** assert a bijection between UCNS-A and UCNS-G.

The PARALLEL verdict from `ucns-shape-reconciliation.md` stands:

* UCNS-A is the recursive factorization algebra implemented as
  `UCNSObject(n_dec, n_min, A_plus, F_plus)` in this repository, with
  `(angle, payload)` anchors, face bits, modulo-4 doubled-cover angle
  arithmetic, payload recursion, and XOR face composition.
* UCNS-G is the EDCM session-defined metric geometry described in the
  companion v3 handoff in `edcmbone` and `erinepshovel-code`.

No proof status flows across this boundary. UCNS-A theorem claims do not
validate UCNS-G metric claims, and vice versa.

## 1. What this supplement updates

The shape reconciliation document, and earlier UCNS-G metric handoff v2,
described UCNS-G informally as a single metric point of the form:

```text
(r, θ, z)
```

with twist treated as a θ half-period / doubled-cover behavior.

That description was too narrow. It captured one projected metric-disk
state, not the full UCNS-G structure.

The corrected UCNS-G side, pinned in the companion v3 handoff, is:

```text
UCNS-G = prime-indexed tensor of non-closing Möbius-cylinder metric disks.
```

In summary:

* One disk per metric axis (one disk for each EDCM and Operator axis).
* A turn is a tensor sample across metric disks.
* A round is an ordered tensor of turn tensors.
* A session is an ordered tensor of round tensors.
* Each metric disk is a non-closing Möbius-cylinder lift of a circular
  projection; closure is a local-perspective artifact, not canonical
  identity.
* Each primitive metric axis sits on a prime anchor; composite positions
  may represent interactions/couplings.
* Each axis state is signed ternary `s ∈ {-1, 0, 1}` with magnitude
  `m ∈ [0, 1]`; `0` is neutral / uncommitted, not scalar absence.
* Twist is an ordinal seam/zero-boundary, not an angle value:
  `360°` returns to phase zero but advances `twist_n → twist_{n+1}`.
* Canonical state requires `(twist_ordinal, phase, face/orientation)`,
  not only `θ mod 360°` or `θ mod 720°`.
* Unit gauge is typed: `1_R`, `1_C`, `1_A`, `1_Z` may all display as `1`
  but are distinct unit bases (radius / circumferential traversal /
  area coverage / ordinal recurrence depth).

The full pin set is in
`edcmbone:docs/handoffs/2026-05-22-ucns-g-prime-cylinder-v3.md`.

## 2. Effect on the shape reconciliation verdict

The PARALLEL verdict is unchanged. The supplement only refines the
UCNS-G side of the comparison so future bridge attempts compare against
the correct UCNS-G structure.

Specifically, any future attempt to bridge UCNS-A and UCNS-G must
target:

* not `(r, θ, z)` alone, but a prime-indexed tensor of metric disks;
* not θ-as-angle, but twist-as-ordinal-seam plus phase plus face;
* not scalar magnitude alone, but signed ternary axis state plus
  magnitude plus typed unit gauge;
* not a single grain, but the token/turn/round/session/archive grain
  tensor.

Until such a bridge is constructed and verified against UCNS-A source,
the two constructions remain parallel.

## 3. Pointers

* `docs/ucns-shape-reconciliation.md` — the existing PARALLEL verdict
  and source-verified UCNS-A inventory (this supplement does not
  modify it).
* `docs/edcm-edcmbone-bridge-checklist.md` — checklist of required
  artifacts before any UCNS-A theorem/proof transfer to UCNS-G/EDCM claims.
* `edcmbone:docs/handoffs/2026-05-22-ucns-g-prime-cylinder-v3.md` —
  the canonical UCNS-G v3 pin.
* `erinepshovel-code` (EDCM / UnitCircle):
  `docs/handoffs/2026-05-22-ucns-g-prime-cylinder-v3.md` —
  mirrored UCNS-G v3 pin for the prime-on-circle / Möbius visualization
  side.
