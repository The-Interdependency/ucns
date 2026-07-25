# UCNS option decisions and open choices

**Authority:** Erin Spencer  
**Recorded:** 2026-07-25  
**Machine surface:** `src/ucns/option_registry.json`  
**EDCM profile:** `src/ucns/edcm.py`  
**Corpus research:** [`EDCM_REAL_SYSTEM_CORPORA.md`](EDCM_REAL_SYSTEM_CORPORA.md)  
**Status:** active EDCM-scoped authority; an exact observation profile is
implemented, while the carrier and higher-composition mathematics remain
incomplete.

## Authority boundary

UCNS is a stable identifier without a canonical expansion. UCNS exposes named,
versioned, provenance-bearing choices without appointing hidden global defaults.

The active project is narrower: determine an EDCM-specific UCNS configuration
against real systems. An EDCM decision does not become universal UCNS canon and
transfers no theorem, measurement, or METAPAT validity.

## EDCM floor now decided

1. **Scale and nesting.** The word is the smallest gonol. The 157 character
   tokens compose word gonols; every larger gonol must compose from word gonols
   without flattening the exact SPACE occurrences that act simultaneously as
   token, word boundary, and superpositioned nesting interface.
2. **Möbius initiation.** Structural Null is singular superpositioned space. A
   new gonol initiates through the Möbius twist, supplying the causal chain
   needed by the later hyper-dimensional lattice relating letters and words.
3. **Token alphabet.** The alphabet is the exact source-provenance public
   157-position fixture. Each entry is one Unicode code point, SPACE occupies
   position zero, and the digit `0` is an ordinary token at zero-based position
   139.
4. **Source normalization.** Authoritative evidence is not normalized. UTF-8 is
   decoded strictly, exact code points are preserved, and out-of-alphabet code
   points stay in order as coverage failures.
5. **Occurrence operation.** EDCM requires ordered concatenation. Multiset and
   set views may exist only as named information-losing projections.
6. **Support.** One complete speaker turn has support one. Token count, word
   count, and text extent do not alter that unit.
7. **Graph contribution.** More information is required. Graphs, edges, nodes,
   relation labels, and graph-dependent state remain retained outside scalar
   `W`.
8. **Equivalence progression.** Exact evidence is the baseline. Projection may
   increase only along an explicit sliding scale justified by accumulated
   experimental evidence and recorded information loss.
9. **Product character `M`.** Display geometric mean, maximum support, and
   minimum support together. None is selected.
10. **Faithful breadth `B`.** Display cell-log support, cell detail, and
    retained presence together. None is selected.
11. **Operators.** Use carrier pairing only for EDCM pending more information.
    Typed payload dispatch remains outside the active configuration.
12. **Profile scope.** The target profile is EDCM-specific. The combined
    EDCM-METAPAT profile remains a compatibility artifact, not an eligible target
    configuration.
13. **Corpus execution.** Run every turn of each admitted corpus. Failure-seeking
    is post-run comparison and surfacing, not sampled execution.

These are scoped constraints, not proof that the ideal configuration has been
found.

## Implemented EDCM observation profile

```text
profile:         ucns.profile.edcm-word-gonol/0.1.0
scope:           EDCM only
smallest gonol:  word
boundary:        exact SPACE / superpositioned nesting interface
initiation:      Möbius twist event
alphabet:        exact public-gonol-157
normalization:   none; preserve source
out of alphabet: retain and report
support:         one unit per speaker turn
execution:       full corpus
selection:       none
```

The profile reconstructs every turn exactly, preserves every SPACE occurrence,
initiates each maximal non-SPACE word sequence as a word gonol, and reports every
code point outside the 157-token alphabet. It records the required initiating
event but does not pretend that the unresolved Möbius coordinate construction or
higher-gonol composition law has been supplied.

## Unicode and glyph normalization

No normalization is required for the 157-token fixture: it is exact,
one-code-point-per-position, and protected by its source commit plus SHA-256
digest. Corpus evidence receives strict UTF-8 decoding and exact code-point
matching; no replacement characters are introduced.

NFC may be tested later only as a separately named comparison projection. It
must preserve the raw source and record every changed sequence. NFKC/NFKD, case
folding, diacritic stripping, whitespace trimming or collapse, quote/dash
folding, confusable mapping, and variation-selector removal are not authoritative
EDCM transformations because they can destroy token or nesting distinctions.

A Unicode code point is not a font-rendered glyph identifier. The current
fixture fixes character identity; if visual glyph shape becomes evidential, the
font, font file digest, shaping engine, renderer, and Unicode version must be
pinned separately.

See [Unicode Normalization Forms](https://unicode.org/reports/tr15/) and
[Unicode Text Segmentation](https://unicode.org/reports/tr29/) for the external
technical distinction. Those standards inform the adapter boundary; they do not
override the exact EDCM fixture.

## Compatibility profile

The earlier post-reset producer profile remains:

```text
producer commit: 19f1afddb993f7d933ac8727627e7d5e1c3b88fc
epoch:           ucns.post-reset.v1
profile:         ucns.profile.edcm-metapat-ordered-occurrence/1.0.0
bridge:          ucns.bridge.edcm-metapat-ordered-occurrence/1.0.0
standing:        implemented compatibility candidate
selection:       none
```

It still preserves useful occurrence evidence but does not implement the
EDCM-specific nesting contract. The directed twofold branched angular cover also
remains executable comparison evidence; its formal relation to the required
Möbius construction is open.

## Choices still genuinely open

### Möbius carrier and directed cover

**Direct Möbius carrier.** Implement the twist as the primary carrier and treat
the directed cover only as historical comparison evidence. This is cleanest if
the cover cannot preserve the singular-space initiation semantics.

**Directed cover as a Möbius chart.** Retain the 720-degree cover as a coordinate
or observation chart over a formally distinct Möbius carrier. This is admissible
only if the mapping preserves the twist's causal meaning rather than merely
sharing a two-lap visual pattern.

**Formal incompatibility.** Prove that the cover and Möbius construction encode
different structures and keep both as explicitly incompatible options. A
negative result here is useful because it prevents a convenient but false
identification.

### Higher-gonol composition above words

**Recursive SPACE composition.** Treat exact SPACE occurrences as the interfaces
that recursively compose adjacent word gonols into larger gonols. This needs a
law for nesting depth and for repeated, leading, and trailing spaces.

**Turn- and dialogue-scoped composition.** Use speaker-turn and dialogue
structure to determine higher groupings while retaining SPACE as the internal
boundary witness. This must not confuse the support unit with the smallest
gonol.

**Additional relation-bearing composition.** Allow syntax, reference, or graph
relations to create higher gonols over word gonols. The relation must remain
explicit, and no parser may silently replace the source nesting evidence.

### Code points outside the 157-token alphabet

**Coverage failure only.** Preserve and report every unmapped code point while
declining to construct a fully covered word gonol. This is the strictest reading
of the fixed alphabet and will show its real-system boundary quickly.

**Named escape or secondary carrier.** Preserve the 157 positions and represent
other code points through an explicit escape or another carrier. The encoding
must be injective, ordered, provenance-bearing, and unable to collide with the
157 native tokens.

**Revised alphabet.** Change the token inventory only through a separately
versioned EDCM experiment. This would be a major configuration change, not
normalization and not an in-place edit of the source fixture.

### Visual glyph identity

**Code-point identity is sufficient.** Treat the source fixture's Unicode
strings as the complete token identity and regard font rendering as
presentation. This keeps corpus runs renderer-independent.

**Pinned rendering identity.** Add a font and shaping receipt when visual form is
part of the evidence. This is necessary if two renderings of one code point or
one ligature are intended to behave differently.

### Graph contribution

**Retained-only graphs.** Keep nodes, edges, labels, and graph state outside
scalar `W`; this is the current safe floor. It preserves disagreement that a
scalar would otherwise hide.

**Named graph support policy.** Permit particular edges or graph states to
contribute support under an explicit policy. The experiment must show what
distinctions are preserved and why the scalar is useful.

**Graph-bearing paired carrier.** Carry graph evidence through carrier pairing
without reducing it to support. This is structurally richer but needs explicit
pairing laws and failure behavior.

### Projection scale

**Exact-only readout.** Remain at the zero-loss baseline for a readout when no
projection has earned admissibility. This is always available.

**Evidence-threshold projection.** Permit a named projection after declared
full-corpus evidence meets a threshold. The threshold, lost distinctions,
reversibility, and affected readout must be recorded.

**Readout-specific projection.** Allow different projection positions for
different questions instead of choosing one global equivalence. This may match
the experimental facts better, but complicates comparison and receipts.

### Simultaneous `M` and `B` displays

**Remain permanently plural.** Treat disagreement among all three `M` and all
three `B` candidates as the result rather than a temporary inconvenience. This
best resists premature scalar collapse.

**Conditionally interpret a candidate.** Give one candidate a named
readout-specific interpretation after full-corpus evidence justifies it, while
continuing to display the other two. This would not authorize a universal
canonical `M` or `B`.

### Corpus adapters and evidence

**Source-native adapters.** Build one deterministic full-corpus adapter per
source, preserving native turns, speakers, annotations, redactions, and
provenance layers. This maximizes fidelity but requires more adapter work.

**Shared minimal envelope.** Map every corpus into a small common turn envelope
while retaining source-native evidence beside it. The common fields must not
flatten multiparty, graph, task-state, or multimodal differences.

Outcome labels are not required to measure EDCM. They become relevant only if a
separate study asks whether an EDCM readout predicts an external outcome.

### Typed payload operations

**Carrier pairing only.** Keep the current boundary and make no domain meaning
implicit. This remains active until another option earns evidence.

**Typed dispatch.** Introduce explicit modality types and interaction laws for
text, graph, audio, image, or task-state payloads. It requires a registry,
failure modes, and cross-type tests before activation.

### Final EDCM selection

**Research profile remains experimental.** Continue full-corpus comparisons
without declaring an ideal configuration while foundational laws remain open.
This is the current state.

**Explicit EDCM-scoped promotion.** Promote a configuration only through a named
authority decision that states evidence, known failures, loss, migration, and
rollback. Promotion still transfers no authority to universal UCNS or METAPAT.

## Full-corpus selection rule

```text
exact source corpus
  -> every speaker turn, in source order
  -> exact code points + explicit SPACE nesting + word gonols
  -> all candidate configurations and all M/B displays
  -> post-run failure, disagreement, and coverage analysis
  -> explicit EDCM-scoped decision, or an honest unresolved result
```

Passing current fixtures or a corpus average is not a selection event.

## hmmm

The flattening failure is now an explicit negative constraint: characters are
tokens, words are the smallest gonols, SPACE is a superpositioned nesting
interface, and a speaker turn is the support unit. Any adapter or evaluator that
turns those four different roles into one flat sequence has changed the EDCM
question before the experiment begins.
