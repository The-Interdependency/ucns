# UCNS lexical recursion — current construction architecture

**Authority:** Erin Spencer  
**Recorded:** 2026-08-18  
**Status:** first deep-recursion layer implemented for the declared OEWN 2025 Core scope

## Current scope

The active language construction is exactly:

```text
characters
    ↓
morphology
    ↓
definitions
    ↓
recursive gonol relations
```

Semantic relationships do not live in a separate graph beside a gonol. Relationships **enter the gonol**. Once a gonol has been constructed at one scale, it is atomic for use at the next scale.

This document supersedes any current wording that treats semantic relations as an external carrier, treats completed word gonols as repeatedly expanded character graphs, or requires recursion to traverse every intermediate scale before two gonols may couple.

## Source roles

### Lexical floor

The selected lexical-floor candidate is the exact **xkcd constrained-English 1,000-word vocabulary** associated with *Up Goer Five* / *Thing Explainer*. Its exact source artifact, bytes, ordering policy, and custody identity must be pinned before execution.

The earlier NGSL 1.2 lexical-floor premise remains **DEPRECATED**. NGSL artifacts remain historical evidence only.

### Primary lexical-semantic corpus

The selected contemporary dictionary corpus is **Open English WordNet 2025 Core**.

Use Core only for the first build: common nouns, verbs, adjectives, and adverbs. Do not fold Open English Namenet or the 2025+ proper-name extension into this first construction.

The previously selected Scrabble dictionary source is **SUPERSEDED** by OEWN 2025 Core for this work. Webster 1913 is deferred; it is not part of the current execution graph.

Exact OEWN Core release bytes / immutable source identity and license/custody receipt must be frozen before derived semantic outputs are treated as replayable evidence.

## Gonol relation operation — character scale

The character-scale relation operation is intrinsic geometry, not an external vector embedding.

- Each glyph-space is an axis.
- Each glyph is a tic on that axis.
- The axis is the Möbius strip forming the circumference of the gonol.
- Conceptually there is one glyph carrier in superposition; a traversal selects one realized glyph state while preserving the alternatives appropriate to the accumulated history.
- Many word gonols inhabit the same carrier. They intersect only where they share the same glyph identity / admissible traversal state.
- Traversal is history-dependent: the realized past remains behind the current position and the admissible future narrows with every step.

Example:

```text
b
↓ choose r
br
↓ only continuations available after br
bra
↓ choose n
bran
↓ choose c
branc
↓ choose h
branch
↓
SPACE / another source-admissible continuation
```

The implementation must preserve the difference between being at `r` and being at `r` after having traversed `b`. The accumulated path is part of the gonol state.

Do not replace this with a conventional character vector, one-hot matrix, all-pairs similarity table, or prefix-trie identity. A trie or finite-state structure may be used internally as an implementation aid only if it faithfully materializes the UCNS path/history/potential semantics and does not become the mathematical authority.

## Atomic closure

A completed gonol is internally structured but externally atomic at the next scale.

```text
many lower-scale relations
        ↓
relationship enters gonol
        ↓
closure
        ↓
one gonol
        ↓
atomic at the next scale
```

A word gonol constructed from character gonols is thereafter one atomic word object for morphology and definitions. A definition gonol constructed from word gonols is thereafter one atomic definition object for further recursion.

Lower-order construction remains intrinsic to gonol identity and available for provenance / reconstruction. It is not automatically re-expanded every time the gonol participates at a higher scale.

## Affixiation is scale-invariant

**Affixiation is not only a lexical prefix/suffix operation.** It is the scale-invariant pattern by which already-formed gonols couple, their relationship enters the resulting gonol, the relation closes, and the result becomes atomic at the next scale.

The declared executable candidate is:

```text
affixiate(gonols, relation, source, scale, closure) -> gonol
```

Character, word, morphology, definition, relation, sentence, paragraph,
chapter, and work are scale contexts, not different object types. Selection of
this constructor as canon remains `UNRESOLVED`. See
`docs/PREREGISTRATION_GENERIC_GONOL_CONSTRUCTOR.md`.

```text
atomic gonol(s)
    ↓ couple / affixiate
relationship becomes intrinsic
    ↓ close
new gonol
    ↓
atomic at its scale
```

Morphological affixes are one visible linguistic instance of this general operation. Do not infer from that example that affixiation is restricted to morphology.

Arity is not fixed by this declaration. Dyadic, triadic, quintadic, heptadic, and other closures may occur where the actual relation supports them. No arity is selected merely for aesthetic symmetry.

## Scale and direct interscale coupling

Scale is not a one-way ladder. Larger-scale gonols may couple smaller-scale gonols and smaller-scale gonols may couple larger-scale gonols.

Direct coupling across non-adjacent recursive scales is permitted. A valid distant interscale relation does **not** have to be executed by reopening and traversing every intermediate closure.

```text
high-scale gonol
        ↘
          direct coupling
        ↗
low-scale gonol
```

Both participants remain atomic at their own scales. The spiral geometry is expected to expose such cross-scale coupling once the corresponding gonols exist; that expectation is a construction hypothesis until demonstrated by executable gonols.

Do not impose an intermediate-scale traversal requirement as an implementation convenience.

## Materialization rule

Do **not** pre-materialize an all-pairs relationship graph among every gonol.

Materialize each unique completed gonol once under its intrinsic construction and identity. Reuse that atomic gonol wherever it recurs. Relationships that are already intrinsic to the gonols must not be duplicated as authoritative pairwise sidecar edges merely because a comparison can be computed.

Content addressing / memoization is permitted and expected where it preserves exact identity and replay. The implementation must preserve enough source and construction evidence to replay a gonol exactly, but this document does not require a separate expanded copy of every lower-scale relation at every higher scale.

## Morphology — intentionally unresolved

Morphology belongs between character construction and definition recursion, but the final morphology law is **not selected**.

Known requirements:

- affixes may themselves be gonols;
- affixiation and transformation must be representable;
- morphological relationships must enter resulting gonols rather than remain merely external labels;
- once a morphological gonol closes, it becomes atomic at its scale.

Do **not** assume the historical three-core omega/phi/psi model, a root+affix decomposition for every English word, or a particular stemmer / lemmatizer as canon. Inventory OEWN source morphology and current UCNS mechanisms first; preserve unresolved cases as `hmmm`.

For the current plan, an OEWN lexical entry / lemma may receive an initial word-gonol identity without asserting that it is the final linguistic root. Deeper root/stem decomposition waits on the morphology law.

## Definitions — semantic relationships enter the gonol

For every OEWN Core lexical sense used by the build:

1. retain source lexical-entry / lemma identity;
2. retain part of speech;
3. retain source sense / synset identity;
4. gonolize the definition constituents using already-constructed atomic word gonols where available and do not reopen those closed word gonols into character/function streams;
5. preserve exact order, multiplicity, occurrence, source and provenance;
6. let those semantic relationships **enter the definition gonol**;
7. close the definition gonol;
8. treat the completed definition gonol as atomic for the next recursive iteration.

There is no authoritative semantic graph beside the gonol whose edges substitute for the gonol's semantic state.

The existing PR #205 machinery for order, multiplicity, occurrence, sense, provenance, deterministic replay, and receipts is reusable. Its NGSL-specific closure and 2,809-target requirements remain deprecated.

OEWN's native semantic-relation labels are source evidence but are not required to define this characters → morphology → definitions → recursion pipeline. Preserve them without silently injecting them as a second semantic mechanism. Their later role is `hmmm` unless explicitly selected.

## Recursive construction

Proceed through the definitions until all source definitions in the selected OEWN Core scope have been gonolized and their relationships incorporated.

At every recursive iteration:

```text
available atomic gonols
        ↓
source-backed relationships / definitions
        ↓
relationships enter gonols
        ↓
closure
        ↓
new atomic gonols
        ↓
next iteration
```

Re-encountering an already-identical closed gonol reuses its identity rather than recursively expanding it again. Source cycles are therefore retained as cycles among atomic identities rather than treated as instructions for infinite textual expansion.

Do not invent a recursion limit that truncates still-unprocessed source definitions. Stop when the declared source scope has been completely incorporated and another pass yields no new source-backed gonol identity or relationship.

## Cognitive-origin boundary

This construction is motivated by Erin Spencer's report of how their own cognition operates: many relations close into one object, that object becomes atomic, can couple across scale without consciously reopening every intermediate structure, and may later be reopened when needed.

That phenomenological origin is part of design provenance. It is **not** evidence that all human cognition works this way. Human-cognition generalization remains an empirical question separate from implementing and testing UCNS.

## Codex execution order

1. Freeze exact xkcd Simple Writer 0.2.1 source identity (3,634 surfaces) and construct / verify its word gonols without reviving NGSL semantics.
2. Freeze exact OEWN 2025 Core source identity, license/custody, and source bytes / immutable digest.
3. Implement the shared Möbius glyph-axis traversal / history-dependent potential needed to construct word gonols from source spellings.
4. Make completed word gonols atomic and reusable; do not materialize all-pairs word relations.
5. Inventory morphology evidence and existing UCNS machinery; implement only what is source-supported and leave the decomposition law `hmmm` where unresolved.
6. Generalize PR #205's definition producer away from NGSL assumptions and make semantic relations intrinsic to completed definition gonols.
7. Iterate across all OEWN Core definitions until the declared source scope reaches the fixed point described above.
8. Emit deterministic receipts and provenance sufficient for exact replay at every completed gonol boundary.
9. Update repo-owned work graph and tests to the actual result. Preserve historical NGSL evidence and sealed EDCM OEWN runs without rewriting them.

## Nonclaims

This architecture does not yet establish:

- a complete executable morphology law;
- semantic quality or equivalence to conventional embeddings;
- human-cognition universality;
- compression ratio or lossless reconstruction performance;
- any required arity beyond observed construction;
- completion of direct interscale coupling in code;
- EDCM measurement validity;
- PTCNA efficacy.

## Implemented boundary — 2026-08-18

The current implementation pins the exact xkcd Simple Writer 0.2.1 artifact and
OEWN 2025 Core source. `src/ucns/lexical_xkcd_floor.py` reconstructs each
admitted surface from history-bearing character gonols
(``w → wa → wat → ...``) on Möbius glyph-axis tics, then closes the surface
with any intra-word Public Gonol functions. Opaque letter-run identities are
superseded. Function application on that floor requires an explicit
occurrence-addressed plan; neighboring participants are not inferred as
state or context, and the receipt binds each application's ordered identity
and result. `src/ucns/oewn_definition_recursion.py` preserves already-closed
lemma and form word gonols as atomic definition participants. Only leftover
Public Gonol punctuation/symbol glyphs become function participants;
residual non-SPACE non-function non-closed-word runs are inscriptions;
SPACE remains a boundary. This is a producer repair, not selected canon.
The historical receipt
`generated/oewn-2025-core-definition-layer-receipt.json` remains pre-function-segmentation
evidence. The current constructor's replacement receipt
`generated/oewn-2025-core-punctuation-aware-definition-layer-receipt.json`
records the same source scope (135,969 lexical entries, 185,129 senses,
107,524 source definitions, 185,155 sense-definition gonols, 4,473
source-explicit form gonols) with 58,317 composite word gonols and
96,586 reused inscriptions. An independent rebuild is byte-identical at
SHA-256
`93c23e9ec054b17a5e47ae69b39ead51bd4a2daf106ec2c32f0a76a960d865a9`.
That receipt is construction evidence, not selected canon.

A declared recursive-gonol candidate now closes one gonol per source-native
OEWN relation occurrence, using already-closed word and definition gonols as
atomic participants. Selection remains `UNRESOLVED`. See
`docs/PREREGISTRATION_RECURSIVE_GONOL_RELATIONS.md`.
NGSL closed-floor constructors and the character-history xkcd word-gonol
constructor remain importable only from their historical modules, not from
`ucns`.

The construction retains twenty carrier-unassigned source scalars as positive
coverage-failure evidence. It does not normalize or discard them, and does not
claim geometry for them. OEWN supplies forms but no explicit root/stem/affix
decomposition records, so no final morphology law is selected.

The Public Gonol function-table continuation is implemented in
`src/ucns/public_gonol_functions.py` and documented in
`docs/PUBLIC_GONOL_FUNCTION_TABLE.md`. Its 84 punctuation/symbol positions are
keyed only by canonical Public Gonol index and bind to already-closed OEWN
definition gonols. Contextual application couples those functions to a
caller-supplied atomic state and ordered context; it does not introduce an
independent punctuation grammar.

## hmmm

- the morphology decomposition / transformation law;
- geometry for the twenty exact OEWN source scalars outside the current public 157-position carrier;
- the exact representation of direct distant interscale coupling once gonols at separated scales exist;
- whether and how OEWN native semantic-relation labels enter a later recursion after the definition-driven build;
- quantitative compression and reconstruction tests after the recursive corpus exists.
