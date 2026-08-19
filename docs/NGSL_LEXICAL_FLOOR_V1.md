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

A later plan authorized a Scrabble dictionary as the replacement source
class. That authorization is now **SUPERSEDED**. Current source roles are
the xkcd Simple Writer 0.2.1 floor candidate and OEWN 2025 Core as the
primary dictionary corpus. See
[`XKCD_LEXICAL_FLOOR_V1.md`](XKCD_LEXICAL_FLOOR_V1.md) and
[`LEXICAL_RECURSION_ARCHITECTURE.md`](LEXICAL_RECURSION_ARCHITECTURE.md).

```text
Unicode character gonols
        ↓
xkcd closed surfaces / OEWN lemmas and forms
        ↓
word gonols
        ↓
OEWN definitions and senses represented as relations among closed word gonols
        ↓
definition gonols = first lexical deep-recursion layer
```

No additional closed-floor requirement is authorized. Do not revive NGSL
coverage rules or treat the historical Scrabble instruction as current
ingestion work.

## Preserved historical evidence

The following remain reproducible historical evidence and are not erased by this deprecation:

- packaged NGSL 1.2 source and attribution artifacts;
- `src/ucns/lexical_floor.py` and its source receipts;
- exact word-gonol construction and occurrence-preserving character relations;
- affixiation and compounding candidates within their original declared scope;
- the PR #205 first-recursion producer's order, multiplicity, sense, provenance, replay, and receipt mechanisms;
- tests and receipts proving behavior under the then-declared NGSL closed-floor contract.

Those artifacts may be used for historical reproduction or mined for reusable implementation machinery. They must not be cited as the current lexical basis or as authority for NGSL-specific coverage/closure in the current xkcd/OEWN construction.

## Preserved forward invariants

The replacement does not introduce conventional NLP token IDs, subword IDs, opaque embedding vectors, or whole-string hashes as lexical primitives. Unicode-character gonols remain the primitive inscription objects; word spelling, order, multiplicity, senses, source provenance, deterministic replay, and recursive semantic relations remain load-bearing.

## Next

This document is historical. Current next work is the punctuation-aware
xkcd floor reconstruction and OEWN definition recursion documented in
[`LEXICAL_RECURSION_ARCHITECTURE.md`](LEXICAL_RECURSION_ARCHITECTURE.md).
Do not pin or ingest a Scrabble dictionary for this program.

## hmmm

The historical Scrabble edition/source question is retired for this
program. Remaining open questions belong to the current xkcd/OEWN path:
the 3,634 → 1,000 family mapping, morphology decomposition, and
full-corpus replay of the punctuation-aware OEWN producer.
