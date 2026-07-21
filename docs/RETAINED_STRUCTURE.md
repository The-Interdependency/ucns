# UCNS retained-structure envelope

**Status:** bounded evidence container with explicit candidate composition; not a complete `UCNSObject`.  
**Consumers:** none currently.

## Purpose

The current `Carrier` and aggregate support `W` are intentionally cell-only.
UCNS also retains receipts, metadata, relations, recursive content, provenance,
state, and future named layers without forcing them into cells or silently
extending `W`.

## Layer rules

Layers are stored as ordered occurrences. Repeated names are permitted. Adding a
layer appends and never overwrites earlier evidence.

A `RetainedLayer` records:

- name;
- raw evidence;
- explicit retained/absent status;
- optional structural-policy binding;
- `measured`, `unmeasured`, or `excluded` contribution status;
- scoped contribution or exclusion note.

Truthiness is not absence. Values such as `0`, `False`, `None`, empty mappings,
and empty sequences may remain retained evidence.

## Measurement firewall

Only the current cell carrier contributes to `cell_support_weight()`.

A retained layer does not enter `W`, `M`, or `B` merely because it exists. The
envelope itself does not calculate `M` or `B`.

A receipt-only, metadata-only, provenance-only, or recursive-only envelope remains
non-null evidence even though its cell support is zero and its broader
measurement remains unresolved.

## Structural policy projections

`project_layer()` applies a named structural policy to one selected layer without
rewriting the envelope. The projection retains the untouched source and records
information loss.

## Retained-layer pairing

Retained layers compose only through an explicit `EnvelopePairPlan`.

A `LayerRef` identifies a name and occurrence ordinal. Every `LayerPairRule`
selects one left occurrence, one right occurrence, a registered pairing policy,
and a result-layer name.

Initial candidate pairing policies include:

- concatenate;
- Cartesian product;
- positional zip;
- preserve left and right separately;
- select left;
- select right;
- exclude;
- custom domain policy.

Unmatched occurrences follow an explicit plan mode: fail closed, preserve sides,
or exclude with loss records. There is no implicit fallback.

Every paired-layer projection retains the untouched left and right sources,
projected view, retained/excluded state, and losses. Result layers remain
`unmeasured` and do not silently enter `W`, `M`, or `B`.

The cell carriers continue using the already established Cartesian cell law.
See [`LAYER_PAIRING.md`](LAYER_PAIRING.md).

## Recursive evidence

Recursive layers may contain shared graphs or cycles. Any traversal requires a
caller-supplied identity function, child enumerator, cycle mode, depth budget,
and node budget. Repeated references and truncation produce receipts. See
[`TRAVERSAL_POLICY.md`](TRAVERSAL_POLICY.md).

## Structural Null

`make_retained_structure()` returns Structural Null only when:

- the carrier is Structural Null; and
- no layer occurrence has `retained = true`.

## Nonclaims

The envelope and pairing laboratory do not settle whether retained layers are
cells, relations among cells, graphs, trees, receipts, or distinct structural
strata. They do not establish canonical pairing, canonical equivalence,
canonical `M`, or canonical `B`.

hmmm: retained-layer measurement laws remain evaluator and canonization work,
not container or pairing-plan behavior.
