# UCNS choice-preservation doctrine

## Governing rule

Where more than one interpretation, representation, policy, or construction
remains admissible, UCNS preserves the capacity to choose among them.

An unresolved choice is retained as structure. It is not silently flattened into
a default and later described as inevitable.

## Required behavior

Until canon explicitly selects or excludes an option, implementations must:

1. retain enough information to recover every still-admissible option;
2. name any temporary computational choice as a policy, strategy, lens, mode, or
   projection rather than as the object itself;
3. preserve provenance for which option was applied and what information it
   forgot;
4. avoid irreversible sorting, deduplication, flattening, merging, coercion, or
   normalization that destroys distinctions needed by another admissible option;
5. keep defaults replaceable and distinguish convenience from canon;
6. fail closed when an operation requires a choice that has not been supplied.

## Narrowing the option set

Choice preservation does not require every proposed option to remain valid
forever. An option may be removed when one of the following occurs:

- canon explicitly rejects it;
- evidence shows it violates an established invariant;
- its information is proven recoverable from another retained representation;
- the user explicitly selects a narrower scope and the loss is recorded.

The narrowing decision must identify what was removed, why, and whether existing
objects require migration.

## Current structural application

The current cell-support floor stores cells as tuples. This preserves encounter
order and multiplicity in the evidence record, but does **not** canonize sequence
semantics.

Until structural equivalence is ratified:

- `make_carrier()` and `prune()` preserve present-cell order and duplicates;
- `pair()` preserves left/right operand sidedness and deterministic Cartesian
  encounter order;
- no operation treats the cells as a set, multiset, sequence, graph, or tree by
  default;
- future equivalence or breadth evaluators must receive an explicit structural
  policy when different interpretations produce different results.

## Examples

- Receipt order may be meaningful for a causal sequence and irrelevant for a
  multiset audit. Preserve the receipts and select the interpretation later.
- Duplicate cells may be distinct occurrences or redundant encodings. Do not
  deduplicate before canonical equivalence decides.
- Metadata-key collisions may require left-biased, right-biased, multimap, or
  conflict-object handling. Preserve both values until a policy is selected.
- Radius may be a lossy display projection while breadth remains authoritative.
  Record that projection rather than erasing the distinction.

hmmm: the policy type and provenance record for future structural choices remain
to be designed; the no-destruction boundary is canonical now.
