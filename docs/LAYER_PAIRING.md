# UCNS retained-layer pairing laboratory

**Status:** explicit candidate-composition infrastructure; no retained-layer product is canonical.  
**Consumers:** internal UCNS research only.

## Purpose

The established cell carrier pairs by Cartesian product. Receipts, metadata, relations, recursive content, provenance, state, and future retained layers do not yet have one universal composition law.

`pair_retained()` therefore requires an `EnvelopePairPlan`. The plan selects exact layer occurrences, names a registered policy for each pair, names each result layer, and declares how unmatched occurrences are treated.

## Pairing policies

Initial policy constructors include:

- concatenate;
- Cartesian product;
- positional zip;
- preserve left and right separately;
- select left;
- select right;
- exclude;
- custom domain policy.

Every `LayerPairProjection` keeps:

- untouched left evidence;
- untouched right evidence;
- projected view;
- declared information losses;
- whether a result layer is retained.

## Occurrence addressing

Layer names may repeat. A `LayerRef` identifies a name plus occurrence ordinal. One occurrence may appear in at most one rule in a plan.

## Unmatched occurrences

The plan must choose one mode:

- fail closed;
- preserve unmatched occurrences with explicit left/right names;
- exclude them while recording losses.

There is no implicit fallback.

## Measurement firewall

The cell carriers continue using the established Cartesian cell law. Result layers are `unmeasured`; pairing them does not make them contribute to `W`, `M`, or `B`.

## Nonclaims

This laboratory does not establish canonical receipt, metadata, relation, recursion, provenance, or state composition. It provides the option-preserving mechanism needed to test whole-envelope evaluator candidates.

hmmm: a whole-envelope multiplicative `M` cannot be claimed until its retained-layer pairing plan is explicit and law-tested.