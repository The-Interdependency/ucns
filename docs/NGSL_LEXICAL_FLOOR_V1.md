# NGSL 1.2 lexical floor v0.2

**Authority:** Erin Spencer  
**Recorded:** 2026-08-06  
**Corrected:** 2026-08-17  
**Status:** executable source-admitted candidate  
**Selection effect:** none

This slice admits the 2,809-word NGSL 1.2 collection as a word-only candidate
lexical floor. It applies the existing Public Gonol glyph assignments, creates
one word gonol per exact ordered glyph sequence, and exposes an occurrence-
addressed character-relationship potential. Affixiation and compounding remain
separate append-only candidate layers. The existing arbitrary-text definition
surface is retained only as historical/provenance-capable infrastructure; it is
not the completed floor semantic representation.

The lexical floor is closed by definition. Once the floor is admitted, a floor
definition cannot add another lexical word to it. The next semantic construction
is therefore a definition gonol built only from already-existing floor gonols.
The semantic relationships established by those definitions are the **first
layer of UCNS deep recursion**. They are not a precursor to a later lexical
embedding. See `docs/LEXICAL_DEFINITION_GONOLS.md`.

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

6. **The lexical floor is closed.** Floor definitions may use only word gonols
   already admitted to this floor. A definition that requires a lexical word
   outside the floor is not a floor definition and cannot enlarge the floor.

7. **No tokenizer or opaque embedding substitution.** Definition construction
   consumes already-existing floor gonols. It does not create conventional NLP
   token ids, subword units, or an external vector lookup between the floor and
   its definition gonols.

8. **Definition relations are first recursion.** The ordered semantic
   relationships among the floor gonols used in a definition constitute the
   first deep-recursion definition gonol for that sense. There is no separate
   semantic-carrier or later lexical-embedding conversion step between those
   relationships and the first recursive layer.

9. **Layers are immutable and authority-bound.** The hyperspace index and
   currently implemented definition mapping are read-only defensive copies.
   Relationship, morphology, definition, source, and snapshot standings reject
   caller promotion. The current text-bearing definition layer does not satisfy
   the new definition-gonol closure/recursion contract by itself. The separate
   `lexical_definition_gonols` module now implements that contract.

10. **Snapshots remain source-linked.** Every current v0.2 layer records the same
   source-receipt identity, exact producer, ordered parent, item count, content
   digest, fixed standing, and required `hmmm`. Altering the source, standing,
   unresolved boundary, or parent chain fails validation.

## Current implemented layer sequence

1. source-receipted word-only collection;
2. fixed-carrier glyph definitions;
3. unique exact word gonols;
4. occurrence-addressed character-relationship potential;
5. orthographic affixiation candidates;
6. orthographic compound candidates;
7. text-bearing contextual definition records.

Later metadata cannot rewrite an earlier source object or snapshot. Layer 7 is
not the completed semantic definition-gonol layer. The first-recursion
constructor is separate so arbitrary historical text cannot be silently
promoted into a closed definition gonol.

## Required first deep-recursion semantic layer

For a fixed lexical floor `F`, every floor-definition gonol must satisfy:

```text
support(definition_gonol(word, sense)) ⊆ F
```

Its lexical constituents are existing floor gonols. Definitions do not admit
new words and do not recursively expand the floor. Multiple senses remain
separate definition gonols with separate context and source provenance.

For each sense, the construction is:

```text
target floor gonol
        ↓
ordered, occurrence-preserving semantic relationships to constituent floor gonols
        ↓
definition gonol = first deep-recursion layer
```

The floor-definition gonol is intended to perform the semantic-representation
role for which conventional systems commonly use vector embeddings, while
remaining decomposable into source-bound UCNS lexical objects. That role analogy
does not establish semantic quality, similarity behavior, or downstream utility.

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

## Existing definition surface

`DefinitionSense` currently attaches context identity, arbitrary definition text,
source identity, and fixed standing to an existing word-gonol identity. That
surface may retain source prose and provenance, but arbitrary text is not itself
a floor-definition gonol.

The replacement semantic construction must resolve every lexical constituent to
an already-existing floor gonol, preserve order, multiplicity, occurrence,
context and source, fail closed on out-of-floor lexical material, and materialize
the ordered semantic relations as the first-recursion definition gonol.

Historical broad wording in the v0.2 implementation that leaves a
"deep-recursion hyperdimensional embedding law" unresolved must be read narrowly:
the first lexical deep-recursion layer is now fixed by authority as the closed
semantic definition relationships. What remains unresolved is implementing that
layer and the deeper recursion above it, not whether those relationships are
already recursion.

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

The current v0.2 test slice exercises:

- exact source receipt and tamper rejection;
- direct and indirect SPACE-boundary bypasses;
- unassigned-glyph rejection;
- unique exact word-gonol identities;
- occurrence multiplicity and address retention;
- explicit loss in the glyph-type set projection;
- immutable indexes and current definition records;
- candidate-identity and standing substitution attacks; and
- source, parent, standing, and unresolved-boundary snapshot attacks.

The first-recursion test slice rejects any floor definition whose lexical
support is not a subset of the admitted floor, preserves repeated ordered
occurrences, rejects incomplete floor coverage, and replays definition-gonol
identities from exact floor, source, sense, context, relation, and occurrence
evidence.

## Nonclaims

This slice does not provide:

- an independently custodied official NGSL checksum;
- a canonical linguistic affix inventory;
- adjudicated compound-word status;
- a completed closed definition-gonol corpus;
- a semantic metric or demonstrated vector-embedding replacement advantage;
- an authorized source corpus that supplies closed definitions for all 2,809
  floor words;
- the recursion law above the definition-gonol layer;
- geometric coordinates for every lexical relationship;
- the seven-gonol construction or pairing plan; or
- EDCM measurement activation.

## hmmm

The 2,809 spellings now form one source-bound, occurrence-preserving lexical
floor. That floor is not permitted to expand through its definitions. The
first-recursion mechanism is executable, but no authorized source has yet
supplied a closed definition for every floor word. That complete-corpus custody
boundary, official-source checksum custody, attested morphology, selector-role
interrogation, and recursion above the definition-gonol layer remain open.
