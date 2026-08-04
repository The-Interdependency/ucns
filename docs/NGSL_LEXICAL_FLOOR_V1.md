# NGSL 1.2 lexical floor v0.1

**Authority:** Erin Spencer  
**Recorded:** 2026-08-04  
**Status:** executable first assignment; source-admitted candidate  
**Selection effect:** none

This slice admits one word-only collection of 2,809 general-English spellings,
applies the existing UCNS glyph canon, creates one word gonol per exact glyph
sequence, and opens a character-derived projection potential. Affixiation and
compounding begin as orthographic candidate layers. Definitions attach later as
plural context-sourced senses.

## Decisions

1. **Source order has no semantic purpose.** Frequency rank and source row order
   are excluded from word-gonol identity. The text file uses deterministic
   Unicode casefold ordering with an exact code-point tie-break only so builds
   and snapshots reproduce byte-for-byte.

2. **One spelling, one word gonol.** Exact duplicate spellings fail admission.
   Each retained spelling has one exact ordered glyph tuple and one deterministic
   gonol identity. Definitions never create another copy of the word.

3. **Glyph law is inherited, not rebuilt.** Each Unicode scalar occurrence uses
   the carrier assignment already implemented by `src/ucns/edcm.py`. No
   normalization, case folding, glyph replacement, or source-order rank enters
   identity.

4. **The hyperspace is initially potential.** It can project exact character
   relationships between any two retained word gonols: shared glyphs, common
   prefix and suffix lengths, containment, and edit distance. This is not yet
   the deep-recursion hyperdimensional embedding and does not imply semantic or
   morphological relation.

5. **Metadata is append-only and snapshotted.** The layer sequence is:

   1. word-only source;
   2. glyph definitions;
   3. unique word gonols;
   4. character-relationship hyperspace potential;
   5. affixiation candidates;
   6. compound candidates;
   7. context-derived definitions.

   `snapshot_layers()` emits a parent-linked digest boundary after every layer.
   Later metadata cannot rewrite an earlier snapshot.

## Affixiation

An affixiation candidate exists when one retained word can be produced by adding
a nonempty prefix or suffix to another retained word. The result is
`orthographic-candidate`, not attested morphology. It does not establish
allomorphy, historical derivation, morpheme identity, or meaning.

## Compounding

A compound candidate exists when one retained word can be divided at an exact
glyph boundary into two other retained words. It is likewise
`orthographic-candidate` until separately attested.

## Definitions

Definitions are keyed to the existing word-gonol identity. Each sense must retain
a context identity and source identity. Many senses may attach to one word gonol;
the source word itself remains singular.

## Files

- `src/ucns/data/ngsl_1_2_words.txt` — word strings only.
- `src/ucns/data/ngsl_1_2_source.json` — separate provenance and admission policy.
- `src/ucns/lexical_floor.py` — gonols, projection potential, layers, and snapshots.
- `tests/test_lexical_floor.py` — collection, identity, candidate, definition, and
  snapshot boundaries.

## Nonclaims

This slice does not provide:

- a canonical linguistic affix inventory;
- adjudicated compound-word status;
- a definitions corpus;
- a semantic metric;
- geometric coordinates for lexical relations;
- deep-recursion hyperdimensional embedding; or
- EDCM measurement activation.

## hmmm

The 2,809 spellings are now an executable candidate lexical floor. Independent
reconciliation against an official NGSL 1.2 download, attested morphology,
context-corpus custody, and the law that embeds these retained relationships into
UCNS deep recursion remain living boundaries.
