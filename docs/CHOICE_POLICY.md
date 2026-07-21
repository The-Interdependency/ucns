# UCNS structural-choice policy layer

**Status:** bounded infrastructure; no policy is canonical by default.  
**Consumers:** internal UCNS construction only.

## Governing rule

Where multiple interpretations, representations, policies, or constructions remain admissible, UCNS preserves the capacity to choose among them.

A policy is therefore a named, explicit interpretation applied to retained evidence. It is not a rewrite of the evidence and does not silently become canon by being registered first or used most often.

## Required objects

- `StructurePolicy`: a named projector plus an explicit information-loss declaration.
- `PolicyRegistry`: holds multiple policies without appointing a default winner.
- `Projection`: records the policy, untouched source evidence, projected view, and all declared losses.
- `InformationLoss`: names a discarded or ignored distinction and whether it remains recoverable from the retained source.
- `apply_policy()`: applies a policy by object or registry name and fails closed on unknown policy names.

## Built-in policy constructors

The initial implementation supplies constructors rather than universal singleton choices:

- ordered sequence: retains order and multiplicity;
- unordered multiset: retains multiplicity but declares order ignored;
- set view: declares both order and multiplicity ignored;
- custom policy: permits graph, tree, relation, domain, or future policy implementations without changing the registry contract.

Multiset and set policies require an explicit key function. UCNS does not invent a universal equality or hashing rule for arbitrary structural evidence.

## Preservation boundary

Every projection retains its source evidence. A lossy view may therefore be inspected or compared without destroying the option to apply another policy later.

No implementation may:

- sort evidence without a selected policy;
- deduplicate evidence without a selected policy;
- collapse left/right sidedness implicitly;
- overwrite a registered policy unless replacement is explicit;
- present a registered policy as canonical merely because it exists.

## Nonclaims

This layer does not define canonical structural equivalence. It provides the mechanism through which candidate equivalence policies can coexist, be tested, and later be selected or rejected explicitly.

hmmm: graph and tree semantics remain domain policies because their node, edge, root, and parent laws have not yet been canonized.
