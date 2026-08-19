# NGSL 1.2 lexical-floor experiment — DEPRECATED

**Authority:** Erin Spencer  
**Recorded:** 2026-08-06  
**Deprecated:** 2026-08-17  
**Status:** DEPRECATED; historical evidence only  

## Why this is deprecated

NGSL 1.2 is a 2,809-word word list, not a dictionary. The earlier UCNS construction treated that list as a closed lexical floor and required semantic definitions to use only members of the fixed list. That premise is withdrawn.

The label **NGSL lexical floor** has no forward authority in UCNS. The current
floor candidate is the xkcd Simple Writer 0.2.1 binder in
[`XKCD_LEXICAL_FLOOR_V1.md`](XKCD_LEXICAL_FLOOR_V1.md). A word list without its
own definition corpus is not the semantic base this work requires.

The closed-floor rule is therefore also deprecated:

```text
support(definition) ⊆ fixed NGSL list
```

Definitions no longer need to close over NGSL or any other artificially preselected word list before participating in UCNS deep recursion.

## Replacement

A Scrabble dictionary is authorized as the replacement lexical source class. The current target is a source-bound **dictionary corpus** containing lexical entries and definitions, not a lexical floor.

```text
Unicode character gonols
        ↓
dictionary words / lexical entries
        ↓
word gonols
        ↓
dictionary definitions and senses represented as relations among word gonols
        ↓
definition gonols = first lexical deep-recursion layer
```

The exact Scrabble dictionary edition, source identity, acquisition path, and license/custody boundary must be pinned before ingestion. No additional closed-floor requirement is authorized.

## Preserved historical evidence

The following remain reproducible historical evidence and are not erased by this deprecation:

- packaged NGSL 1.2 source and attribution artifacts;
- `src/ucns/lexical_floor.py` and its source receipts;
- exact word-gonol construction and occurrence-preserving character relations;
- affixiation and compounding candidates within their original declared scope;
- the PR #205 first-recursion producer's order, multiplicity, sense, provenance, replay, and receipt mechanisms;
- tests and receipts proving behavior under the then-declared NGSL closed-floor contract.

Those artifacts may be used for historical reproduction or mined for reusable implementation machinery. They must not be cited as the current lexical basis or as authority for NGSL-specific coverage/closure in the replacement dictionary construction.

## Preserved forward invariants

The replacement does not introduce conventional NLP token IDs, subword IDs, opaque embedding vectors, or whole-string hashes as lexical primitives. Unicode-character gonols remain the primitive inscription objects; word spelling, order, multiplicity, senses, source provenance, deterministic replay, and recursive semantic relations remain load-bearing.

## Next

Pin and ingest the authorized Scrabble dictionary source; construct word gonols and first-recursion definition gonols from its source-bound lexical entries and definitions; generalize useful PR #205 machinery while removing the NGSL 2,809-word coverage and closed-floor assumptions.

## hmmm

Exact Scrabble dictionary edition/source, machine-readable acquisition, redistribution/custody boundary, and the handling of definition words not separately listed as dictionary headwords remain source-ingestion questions to freeze before corpus construction.
