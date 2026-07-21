# UCNS retained-structure envelope

**Status:** bounded evidence container; not a complete `UCNSObject`.  
**Consumers:** none currently.

## Purpose

The current `Carrier` and aggregate support `W` are intentionally cell-only. UCNS also needs to retain receipts, metadata, relations, recursive content, provenance, state, and future structural layers without forcing them into cells or silently extending `W`.

The retained-structure envelope preserves those layers as evidence while leaving their semantics and measurement status explicit.

## Required objects

- `ContributionStatus`: `measured`, `unmeasured`, or `excluded`.
- `RetainedLayer`: a named occurrence of evidence with optional policy binding and explicit contribution status.
- `RetainedStructure`: a non-null envelope containing a cell carrier, one or more retained layers, or both.
- `make_retained_structure()`: returns Structural Null only when neither a carrier nor any retained layer remains.
- `project_layer()`: applies a named structural policy to one selected layer without rewriting the envelope.

## Layer rules

Layers are stored as an ordered tuple of occurrences. Repeated layer names are permitted. Adding a layer appends; it never overwrites an earlier layer.

A layer records:

- its name;
- its raw evidence;
- whether evidence is actually retained;
- an optional policy name;
- contribution status;
- a scoped note explaining measurement or exclusion.

Truthiness is not an absence test. Values such as `0`, `False`, `None`, an empty mapping, or an empty sequence may be retained evidence when the layer explicitly says they are retained.

An absent placeholder has `retained = false` and no evidence. It is ignored by the non-null test but may remain in an envelope as a declared option slot.

## Measurement firewall

Only the current cell carrier contributes to `support_weight()`.

A retained layer does not enter `W`, `M`, or `B` merely because it exists. Its contribution status must remain one of:

- `measured`: a named evaluator and scope have established a contribution;
- `unmeasured`: retained but not yet assigned a lawful contribution;
- `excluded`: deliberately omitted under an explicit scope, with the reason recorded.

The envelope itself does not calculate `M` or `B`.

## Structural Null

`make_retained_structure()` returns the unique Structural Null only when:

- the carrier is Structural Null; and
- no layer occurrence has `retained = true`.

Therefore a receipt-only, metadata-only, provenance-only, or recursive-only envelope remains non-null evidence even though its cell support is currently zero and unmeasured.

## Nonclaims

This envelope does not settle whether layers are cells, relations among cells, graphs, trees, receipts, or distinct structural strata. It preserves each admissible representation until a policy or canon decision is made.

hmmm: how retained layers contribute to canonical equivalence, product character, and faithful breadth remains evaluator work rather than container behavior.
