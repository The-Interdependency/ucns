# Dictionary definition gonols — first lexical deep recursion

**Authority:** Erin Spencer  
**Recorded:** 2026-08-17  
**Corrected:** 2026-08-17  
**Status:** active replacement boundary; prior lexical-floor closure DEPRECATED  

## Replacement boundary

The earlier fixed lexical-floor model is deprecated. NGSL 1.2 is a word list, not a dictionary, and no longer defines the active lexical universe or a closure requirement for semantic definitions.

A **Scrabble dictionary** is authorized as the replacement lexical source class. The exact edition/source identity and custody boundary must be pinned before corpus ingestion.

The active construction is:

```text
Unicode character gonols
        ↓
dictionary lexical entries / words
        ↓
word gonols
        ↓
source-bound dictionary definitions and senses
        ↓
ordered semantic relationships among word gonols
        ↓
definition gonols = first lexical deep-recursion layer
        ↓
further recursion
```

## First deep recursion

The semantic relationships expressed by a dictionary definition are themselves the first lexical deep-recursion layer. They are not metadata awaiting a later embedding step.

For a dictionary entry `w` and one source sense:

```text
target word gonol G(w)
        ↓
ordered semantic relations to the word gonols occurring in the definition
        ↓
definition gonol for (w, sense)
```

The definition gonol is the depth-plus-one UCNS object constituted by those source-bound semantic relationships.

## No fixed-floor closure

The former rule

```text
support(definition_gonol) ⊆ fixed NGSL floor
```

is DEPRECATED and has no forward authority.

A definition is not rejected merely because it uses a word absent from NGSL or another preselected word list. Lexical support is derived from the selected dictionary evidence under explicit provenance rather than forced to close over an artificial subset.

The exact treatment of a definition word that is not separately present as a headword in the selected dictionary remains a source-ingestion boundary to freeze after the exact dictionary is pinned. It is not permission to resurrect the NGSL closure rule.

## Preserved invariants

The replacement does not introduce a conventional NLP token layer. Preserve:

- Unicode-character gonols as primitive inscription objects;
- exact word spelling and ordered character composition;
- target word identity;
- constituent order, multiplicity, and occurrence position;
- sense identity;
- source identity and source-text custody;
- deterministic replay and immutable receipts;
- multiple senses as distinct definition gonols;
- semantic relations themselves as the first recursion.

Token IDs, subword IDs, opaque vector embeddings, and whole-string hashes are not substitutes for these objects.

## PR #205 status

`src/ucns/lexical_definition_gonols.py`, merged in PR #205, established useful fail-closed machinery for preserving target, sense, context, source, order, repeated occurrences, provenance, replay, and receipts.

Its **NGSL-specific closed-floor semantics are deprecated**:

- requiring every constituent to be inside the fixed NGSL word set;
- requiring complete coverage of exactly 2,809 NGSL targets;
- treating the NGSL source receipt as the current lexical authority.

Those requirements remain valid only for historical reproduction of the PR #205 experiment. The reusable provenance/order/receipt mechanism should be generalized to the dictionary corpus rather than discarded.

## Semantic role

Dictionary-derived definition gonols are intended to occupy the semantic-representation role commonly served by vector embeddings while remaining decomposable into source-bound UCNS relations. That is a role statement, not an efficacy claim.

No semantic metric, similarity quality, benchmark advantage, or downstream utility is established until the dictionary corpus is instantiated and separately evaluated.

## Next implementation

1. Pin the exact authorized Scrabble dictionary edition/source and custody/redistribution boundary.
2. Freeze the machine-readable acquisition and normalization procedure before inspecting derived semantic structure.
3. Construct dictionary word gonols from Unicode-character gonols.
4. Preserve every definition sense and ordered/repeated lexical occurrence.
5. Generalize the PR #205 producer to dictionary-source receipts and remove NGSL closure/2,809-coverage gates.
6. Emit exact replayable first-recursion definition-gonol receipts.
7. Preserve the old NGSL path as historical only.
8. Evaluate semantic behavior only after construction is complete.

## hmmm

The exact Scrabble dictionary edition/source, its machine-readable acquisition and legal custody boundary, and the treatment of definition lexical material not separately listed as headwords remain unresolved until source selection is pinned. Recursion above the dictionary definition-gonol layer remains separately open.
