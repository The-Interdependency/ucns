# Lexical floor definition gonols

**Authority:** Erin Spencer  
**Recorded:** 2026-08-17  
**Corrected:** 2026-08-17  
**Status:** authority-declared first deep-recursion construction boundary  
**Selection effect:** none

## Fixed lexical-floor closure

Let `F` be the already-admitted lexical floor: the fixed set of floor word gonols.
A floor definition cannot enlarge `F`.

For any floor word `w ∈ F`, every lexical constituent used to construct a floor-definition gonol for `w` must itself already be a member of `F`.

```text
support(definition_gonol(w, sense)) ⊆ F
```

A proposed definition that requires a lexical word outside `F` is not a floor definition. It does not admit that word, extend the floor, or trigger recursive vocabulary growth.

The construction order is therefore fixed:

```text
Unicode character gonols
        ↓
fixed floor word gonols
        ↓
complete lexical floor F
        ↓
semantic relationships among floor gonols expressed by floor definitions
        ↓
floor-definition gonols = first deep-recursion layer
        ↓
further recursion over those gonols
```

## First deep recursion

The semantic relationships among the floor word gonols are **the first layer of deep recursion**.

They are not metadata collected in preparation for a later deep-recursion embedding, and they are not a temporary semantic carrier waiting to be transformed into one.

For a floor word `w` and one admitted sense, the definition establishes an ordered, occurrence-preserving relation among already-existing floor gonols:

```text
target floor gonol G(w)
        ↓
ordered semantic relations to G(w1), G(w2), ... G(wn), with every wi ∈ F
        ↓
definition gonol for (w, sense)
```

That definition gonol is the depth-plus-one UCNS object constituted by those semantic relationships. Constructing those relationships is therefore constructing the first deep-recursion layer itself.

No additional lexical "embedding step" sits between the semantic relationships and this first recursive layer.

## No tokenizer layer

This construction does not introduce conventional NLP tokens, token ids, subword pieces, or an external embedding lookup.

The lexical objects participating in a definition are already-existing floor gonols. Unicode character gonols remain the primitive inscription objects from which floor words were constructed.

Source prose may be retained for custody and replay, but arbitrary definition text is not itself the semantic representation.

## Semantic role

A floor-definition gonol is the UCNS semantic-representation analogue of a conventional vector embedding: it gives a floor word a relational semantic representation built from other already-known lexical objects rather than assigning the word an opaque coordinate vector.

This is a role analogy, not an efficacy claim. No semantic benchmark, similarity metric, downstream prediction advantage, or equivalence to established vector embeddings is established by this declaration.

Multiple senses remain distinct. A word may have multiple floor-definition gonols, each separately source- and context-bound, without averaging them into one representation or rewriting the underlying word gonol.

Because the definition gonols are themselves gonols, they are available as objects for subsequent recursive layers. The existence of those later layers does not demote the definition relationships to a pre-recursive representation.

## Executable construction

`src/ucns/lexical_definition_gonols.py` implements the declared construction.
It accepts source-receipted definition evidence only after every ordered
constituent has been resolved to an exact existing floor-gonol identity. It
constructs one occurrence node per constituent, preserves order and repetition,
binds target, sense, context, source record, source-text digest, floor receipt,
and definition-source receipt into the definition-gonol identity, and rejects
the entire proposal when any endpoint is outside the floor.

The complete-layer constructor admits no partial result: every submitted record
must construct, the source receipt count must match, and at least one separate
sense must target every word gonol in the exact floor. Its canonical receipt
replays all definition-gonol identities and the complete covered-target
inventory. Intrinsic carriers contain only dense integer occurrences and the
fixed definition-constituent relation code. They attach no geometry or
measurement.

`src/ucns/lexical_floor.py` v0.2 still exposes `DefinitionSense.definition` as
arbitrary historical text. That older surface remains
historical/provenance-capable infrastructure and is not the new definition
gonol.

Historical wording in `src/ucns/lexical_floor.py` that broadly leaves a "deep-recursion hyperdimensional embedding law" unresolved is superseded for this boundary: the first deep-recursion lexical layer is fixed as the semantic relationships created by closed floor definitions. What remains unresolved is a complete authorized source corpus and whatever recursion lies above this executable layer, not whether these relationships count as deep recursion.

## Construction protocol

1. Keep the admitted lexical floor fixed.
2. Create definitions whose lexical constituents are all existing floor gonols.
3. Fail closed on every proposed floor definition that requires lexical material outside the floor.
4. Preserve constituent order, multiplicity, occurrence position, target-word identity, sense identity, context, source, and provenance.
5. Materialize the semantic relationships from the target word gonol to the floor gonols participating in each definition.
6. Treat that ordered semantic relationship object as the first deep-recursion definition gonol for the sense; do not insert a separate pre-embedding or later conversion step.
7. Emit source-bound receipts that permit exact replay from the fixed floor identity plus the semantic relationship evidence.
8. Preserve multiple senses as separate definition gonols.
9. Only after this representation exists, evaluate whether the resulting first-recursion semantic structure performs the work for which conventional systems use vector embeddings.

## Nonclaims

This document does not select a dictionary source, invent missing definitions, choose a semantic similarity metric, establish the recursion law above the definition-gonol layer, activate EDCM, or establish PTCNA efficacy.

## hmmm

The floor is fixed, definitions cannot expand it, their semantic relationships
are the first deep-recursion layer, and the executable representation now fails
closed on that boundary. The living boundaries are an authorized source/custody
procedure that actually supplies at least one closed definition for every floor
word, and the deeper recursion that consumes completed definition gonols.
