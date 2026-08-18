# Definition gonols — semantic relationships enter gonols

**Authority:** Erin Spencer  
**Recorded:** 2026-08-17  
**Corrected:** 2026-08-18  
**Status:** active first lexical deep-recursion boundary  

Read `docs/LEXICAL_RECURSION_ARCHITECTURE.md` first. It is the current construction architecture for Codex.

## Source correction

The NGSL 1.2 lexical-floor premise remains **DEPRECATED**. The later Scrabble-dictionary replacement is now **SUPERSEDED** for this work.

Current source roles are:

```text
xkcd constrained-English 1,000-word vocabulary
    -> lexical-floor candidate

Open English WordNet 2025 Core
    -> primary contemporary lexical-semantic corpus

Webster 1913
    -> deferred / not in current execution graph
```

The exact xkcd artifact identity and OEWN 2025 Core release receipt are now
pinned by `src/ucns/lexical_sources.py`. The first complete materialization is
sealed by `generated/oewn-2025-core-definition-layer-receipt.json`.

## First deep recursion

For a source lexical sense, semantic relationships expressed by its definition do not remain external metadata. They **enter the gonol**.

```text
atomic word gonols participating in one source definition
        ↓
ordered source-backed semantic relationship
        ↓
relationship becomes intrinsic to definition gonol
        ↓
closure
        ↓
definition gonol is atomic at the next scale
```

The completed definition gonol is the first lexical deep-recursion semantic object for that source sense. There is no separate vector-embedding conversion step and no authoritative sidecar semantic graph that substitutes for the gonol.

## Atomicity

A word gonol is built from character gonols, but once the word gonol exists it is atomic for morphology and definition construction.

A definition gonol is built from word gonols, but once the definition gonol exists it is atomic for further recursion.

Atomicity does not erase internal construction. Provenance and replay remain available. It means the next scale consumes the completed gonol as one object rather than re-expanding its constituents on every use.

## Preserved PR #205 machinery

`src/ucns/lexical_definition_gonols.py`, merged in PR #205, established useful implementation machinery for:

- target identity;
- sense and context identity;
- exact source identity;
- constituent order;
- multiplicity and repeated occurrences;
- provenance;
- deterministic replay; and
- immutable receipts.

Reuse and generalize that machinery.

Its NGSL-specific semantics remain historical only:

- fixed NGSL closure;
- rejection solely because a constituent is outside NGSL;
- complete coverage of exactly 2,809 targets; and
- NGSL source receipt as active lexical authority.

## Definition construction

For OEWN 2025 Core:

1. retain lexical-entry / lemma identity;
2. retain part of speech;
3. retain source sense / synset identity;
4. retain exact source gloss and source custody;
5. resolve each lexical occurrence into its gonol construction without introducing token IDs, subword IDs, opaque embeddings, or whole-string hashes;
6. preserve occurrence order and repetition;
7. incorporate the semantic relationship into the definition gonol itself;
8. close the gonol and treat it as atomic for the next recursive pass.

Where a definition uses an inscription that does not yet have a dictionary-defined lexical sense, the inscription may still be constructed from character gonols. Do not resurrect the NGSL closure rule merely to reject it. Whether that inscription receives a source-defined semantic sense depends on the selected OEWN evidence.

## Recursion

Continue across the selected OEWN Core definition corpus until every source definition in scope has been gonolized and incorporated. Completed identical gonols are reused rather than textually re-expanded.

A complete pass that yields no new source-backed gonol identity or relationship after the declared source scope is exhausted is the stopping boundary.

## Morphology boundary

Morphology precedes definition recursion, but the exact root / stem / affix / transformation law is not selected. Do not import the historical three-core morphology model or a generic stemmer as current canon.

Affixiation is scale-invariant in the broader UCNS sense: coupling enters a gonol, closes, and the result becomes atomic. Morphological affixiation is one linguistic manifestation of that operation.

## Native OEWN relation labels

OEWN's native semantic-relation labels are source evidence, but this construction is defined by:

```text
characters -> morphology -> definitions -> recursive gonol relations
```

Do not silently introduce the native OEWN relation graph as a separate semantic mechanism. Preserve it with provenance; its later participation remains `hmmm` until explicitly selected.

## Nonclaims

This document does not establish semantic efficacy, final morphology, compression ratio, lossless reconstruction, human-cognition universality, EDCM validity, or PTCNA efficacy.

## Completed declared source scope

`src/ucns/oewn_definition_recursion.py` constructs every OEWN 2025 Core
sense-definition pairing, exact source-explicit form relation, and exact
multi-inscription entry. Relationships are intrinsic ordered carriers inside
the closed gonols. A second independent complete run reproduced the 1,308-byte
receipt exactly.

This is construction evidence, not semantic efficacy. The resulting standing
is `complete-oewn-core-first-recursion-candidate`.

## hmmm

- exact xkcd 1,000-word source artifact identity;
- morphology decomposition / transformation law;
- geometry for retained carrier-unassigned Unicode source evidence;
- executable direct interscale coupling representation;
- later role of OEWN native semantic relation labels.
