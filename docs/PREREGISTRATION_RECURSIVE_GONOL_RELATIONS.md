# Recursive gonol relations — source-native candidate

**Authority:** Erin Spencer
**Recorded:** 2026-08-19
**Status:** declared candidate constructor; selection `UNRESOLVED`
**Selection effect:** none

This preregisters evaluation criteria before a completion receipt is minted.
It does not select a recursive mechanism or promote native OEWN labels to
canon.

## Decision

Begin recursive gonol construction as an explicitly identified candidate
after the punctuation-aware definition layer. Closed word and definition
gonols remain atomic. Every source-native OEWN relation occurrence becomes
one recursive gonol whose relation enters the construction. Selection stays
unresolved until later evidence and ratification authorize promotion.

## Frozen constructor identity

```text
constructor_id: ucns.recursive-gonol.source-native-oewn-relations
version:        0.1.0
standing:       source-native-recursive-gonol-candidate
selection:      false
```

## Frozen inputs

| Input | Identity |
|---|---|
| OEWN 2025 Core | `ucns.oewn-core-receipt:sha256:3ea1f9f0d60bb0c440d7bcb6375050673c0cd03b774f87fed9e4be223bc3c973` |
| Punctuation-aware definition layer | `ucns.oewn-definition-layer:sha256:c53c9941b9286193c677e8057238f380f00e90b06bf488b78a2c7caece5738b7` |
| Historical definition receipt | `generated/oewn-2025-core-definition-layer-receipt.json` remains historical |

## Frozen choices

These choices are bound, not selected as canon:

1. **Source of relations.** Only already-inventoried OEWN Core sense-level and
   synset-level native relation occurrences. No inferred adjacency, no
   all-pairs graph, no family map, no morphology decomposition.
2. **Occurrence identity.** One recursive gonol per source relation
   occurrence, in source order: lexical entries × senses × relation labels ×
   targets, then synsets × relation labels × targets.
3. **Participant assembly.** No cartesian pairing of definitions.
   - Sense occurrence: source word gonol, then that sense's definition
     gonols in layer order, then target word gonol, then the target sense's
     definition gonols in layer order.
   - Synset occurrence: source member word gonols in source member order,
     then definition gonols of that synset in layer order, then the same
     for the target synset.
4. **Atomicity.** Participants are only already-closed word or definition
   gonol identities from the supplied definition layer. Construction fails
   closed if a member or target cannot be resolved without reopening.
5. **Carrier code.** One integer code `7` meaning "source-native OEWN
   relation occurrence." Exact labels live in the gonol payload, not as an
   invented per-label geometry.
6. **Standing.** `source-native-recursive-gonol-candidate`. Promotion of
   standing or `selected=true` fails closed.

## Frozen evaluation criteria

A completion receipt is issued only if every condition holds:

1. Recursive gonol count equals the snapshot's source-native relation
   occurrence count.
2. Every recursive gonol reconstructs from its bound source addresses and
   the same definition layer.
3. No participant reopens a closed word or definition into a character or
   function stream.
4. Exact source relation labels are preserved without remapping.
5. An independent rebuild from the same snapshot and definition layer is
   byte-identical.
6. `selected` remains false and standing is not promoted.
7. Missing targets, unresolved members, or incomplete scope fail closed.

Outcome vocabulary: the receipt may say the candidate `SURVIVED` replay. That
does not mean proved, useful, grammatical, or selected.

## Sealed candidate receipt

`generated/oewn-2025-core-source-native-recursive-gonol-receipt.json`

- layer `ucns.recursive-gonol-layer:sha256:561c8cee9cfc0befdcef9620cfc044033cf034ac4ca9cb1eadaf8b7527bb8af3`
- SHA-256 `33fc59ab40a7a6a1c68cbe2caecbd4eaa4d30544af3afd99ee9a5ffe701ee111`
- 244727 recursive gonols, matching source relation occurrences
- `selected: false`
- independent rebuild byte-identical

## Nonclaims

This candidate does not establish a morphology law, family map, native-OEWN
canon, semantic efficacy, EDCM measurement validity, compression, or
recursive-gonol selection.

## Usage

```python
from ucns.oewn_definition_recursion import build_oewn_definition_layer
from ucns.recursive_gonol_relations import (
    build_source_native_recursive_gonols,
    recursive_gonol_layer_bytes,
    replay_source_native_recursive_gonols,
)

layer = build_oewn_definition_layer(snapshot)
recursive = build_source_native_recursive_gonols(snapshot, layer)
replay_source_native_recursive_gonols(recursive, snapshot, layer)
```

## hmmm

- whether this candidate later becomes selected canon
- whether a different source-backed relation set should be the next candidate
- executable geometry for direct distant interscale coupling
