# UCNS cycle-safe recursive traversal

**Status:** recursive-evidence research infrastructure; no recursive semantics are canonical.

## Purpose

Retained recursive content may be a tree, shared directed graph, self-reference, mutual reference, lazy structure, or cyclic system. A serializer or evaluator must not assume acyclicity or recurse without a budget.

## Explicit traversal inputs

`traverse()` requires:

- a child-enumeration function;
- a caller-defined hashable identity function;
- a named `TraversalPolicy`;
- a depth and node budget.

UCNS does not infer object identity from representation or equality.

## Cycle modes

- reject the cycle;
- retain a reference receipt to the first path;
- unfold until the declared depth budget;
- invoke an explicit fixed-point resolver.

Fixed-point mode cannot be constructed without a resolver.

## Evidence receipts

Traversal records:

- visits and paths;
- repeated-reference receipts;
- depth, node, and cycle truncation receipts;
- fixed-point receipts.

Budget exhaustion is evidence, not silent omission.

## Nonclaims

Traversal does not decide whether recursive content contributes to equivalence, `M`, or `B`. It supplies bounded evidence for candidate evaluators.

hmmm: canonical recursive identity, shared-substructure accounting, and fixed-point laws remain candidate work.