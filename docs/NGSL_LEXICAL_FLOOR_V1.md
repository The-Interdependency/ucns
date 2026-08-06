# NGSL 1.2 lexical floor v0.2

**Authority:** Erin Spencer  
**Recorded:** 2026-08-06  
**Status:** executable source-admitted candidate  
**Selection effect:** none

This slice admits the 2,809-word NGSL 1.2 collection as a word-only candidate
lexical floor. It applies the existing Public Gonol glyph assignments, creates
one word gonol per exact ordered glyph sequence, and exposes an occurrence-
addressed character-relationship potential. Affixiation, compounding, and
context-derived definitions remain separate append-only layers.

## Fixed boundaries

1. **One fixed carrier.** The lexical floor activates addresses on the existing
   157-position Public Gonol carrier. It does not introduce a 26-, 27-, or
   2,809-based replacement radix and does not renumber existing addresses.

2. **One exact spelling, one word gonol.** Case, glyph order, and multiplicity
   remain authoritative. Exact duplicate spellings fail admission. Source rank,
   frequency, and serialization position do not enter identity.

3. **SPACE remains the nesting boundary.** Every public word-construction path
   rejects the profile-pinned Unicode SPACE manifestations. A caller cannot use
   the direct word identifier or dataclass constructor to smuggle a boundary
   into one word gonol. A glyph without a Public Gonol carrier assignment also
   fails admission rather than being silently coerced.

4. **Source custody is executable.** The JSON source record, attribution notice,
   exact word bytes, terminal-newline policy, Git blob, byte SHA-256, ordered
   word-sequence digest, source standing, and unresolved official-checksum
   boundary produce one immutable `LexicalSourceReceipt`.

5. **Relationships retain occurrences.** A character relationship stores every
   matching left/right occurrence pair with both offsets. The optional glyph-
   type set view is explicitly identified by Unicode scalar value and records
   that occurrence order, multiplicity, and pairing were lost.

6. **Layers are immutable and authority-bound.** The hyperspace index and
   definition mapping are read-only defensive copies. Relationship, morphology,
   definition, source, and snapshot standings reject caller promotion.

7. **Snapshots remain source-linked.** Every current layer records the same
   source-receipt identity, exact producer, ordered parent, item count, content
   digest, fixed standing, and required `hmmm`. Altering the source, standing,
   unresolved boundary, or parent chain fails validation.

## Current layer sequence

1. source-receipted word-only collection;
2. fixed-carrier glyph definitions;
3. unique exact word gonols;
4. occurrence-addressed character-relationship potential;
5. orthographic affixiation candidates;
6. orthographic compound candidates;
7. plural context-sourced definitions.

Later metadata cannot rewrite an earlier source object or snapshot.

## Affixiation

An affixiation candidate exists when one retained word can be produced by adding
one nonempty prefix or suffix to another retained word. The candidate binds the
exact base and derived word-gonol identities. Its standing remains
`orthographic-candidate`; it does not establish morpheme authority, allomorphy,
historical derivation, or meaning.

## Compounding

A compound candidate exists when one retained word divides at an exact glyph
boundary into two other retained words. The candidate binds all three exact word-
gonol identities and remains `orthographic-candidate` until independently
attested.

## Definitions

Definitions attach to an existing word-gonol identity. Every sense retains a
context identity, exact definition text, source identity, and fixed
`context-sourced-definition` standing. Multiple senses may coexist; the source
word gonol remains singular.

## Source and attribution files

- `src/ucns/data/ngsl_1_2_words.txt` — exact word strings only.
- `src/ucns/data/ngsl_1_2_source.json` — acquisition, identity, serialization,
  attribution digest, standing, and custody boundary.
- `src/ucns/data/NGSL_1_2_ATTRIBUTION.txt` — packaged creator, source, license,
  transformation, non-endorsement, and unresolved-custody notice.

The data record declares CC BY-SA 4.0 for NGSL 1.2. This notice addresses the
packaged lexical artifact; it does not manufacture a repository-wide software
license or resolve the repository's broader licensing policy.

## Verification surface

The test slice exercises:

- exact source receipt and tamper rejection;
- direct and indirect SPACE-boundary bypasses;
- unassigned-glyph rejection;
- unique exact word-gonol identities;
- occurrence multiplicity and address retention;
- explicit loss in the glyph-type set projection;
- immutable indexes and definition layers;
- candidate-identity and standing substitution attacks; and
- source, parent, standing, and unresolved-boundary snapshot attacks.

## Nonclaims

This slice does not provide:

- an independently custodied official NGSL checksum;
- a canonical linguistic affix inventory;
- adjudicated compound-word status;
- a definitions corpus;
- a semantic metric;
- geometric coordinates for lexical relationships;
- the seven-gonol construction or pairing plan;
- deep-recursion hyperdimensional embedding; or
- EDCM measurement activation.

## hmmm

The 2,809 spellings can now enter one source-bound, occurrence-preserving lexical
producer without crossing SPACE or laundering a lossy set view into exact
evidence. Official-source checksum custody, attested morphology, context-corpus
custody, selector-role interrogation, and the law that embeds retained relations
into UCNS deep recursion remain living boundaries.
