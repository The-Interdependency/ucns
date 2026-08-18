# Lexical floor definition gonols

**Authority:** Erin Spencer  
**Recorded:** 2026-08-17  
**Status:** authority-declared construction correction and next implementation boundary  
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
definitions expressed only with members of F
        ↓
floor-definition gonols
```

## No tokenizer layer

This construction does not introduce conventional NLP tokens, token ids, subword pieces, or an external embedding lookup.

The lexical objects used to construct a definition are already-existing floor gonols. Unicode character gonols remain the primitive inscription objects from which floor words were constructed.

Source prose may be retained for custody and replay, but arbitrary definition text is not itself the semantic representation.

## Semantic role

A floor-definition gonol is the UCNS semantic-representation analogue of a conventional vector embedding: it gives a floor word a relational semantic representation built from other already-known lexical objects rather than assigning the word an opaque coordinate vector.

This is a role analogy, not an efficacy claim. No semantic benchmark, similarity metric, downstream prediction advantage, or equivalence to established vector embeddings is established by this declaration.

Multiple senses remain distinct. A word may have multiple floor-definition gonols, each separately source- and context-bound, without averaging them into one representation or rewriting the underlying word gonol.

## Current implementation discrepancy

`src/ucns/lexical_floor.py` v0.2 currently exposes `DefinitionSense.definition` as arbitrary text and can retain such text in a definition layer. That surface is insufficient to serve as the floor semantic representation described here because it does not require the definition to be constructed from floor gonols or prove lexical-floor closure.

Until the replacement construction is implemented, the existing text-bearing definition layer is historical/provenance-capable infrastructure only. It must not be reported as the completed floor-definition-gonol embedding.

## Next implementation

1. Keep the admitted lexical floor fixed.
2. Create definitions whose lexical constituents are all existing floor gonols.
3. Fail closed on every definition that references lexical material outside the floor.
4. Preserve constituent order, multiplicity, sense identity, context, source, and provenance in the definition construction.
5. Construct one immutable definition gonol per admitted sense using UCNS-owned relation/composition machinery rather than a tokenizer or opaque vector substitution.
6. Emit source-bound receipts that permit exact replay from floor identity plus definition constituents.
7. Only after this representation exists, evaluate whether definition-gonol relations perform the semantic work for which conventional systems use vector embeddings.

## Nonclaims

This document does not select a dictionary source, invent missing definitions, choose a semantic similarity metric, establish a final higher-gonol composition law, activate EDCM, or establish PTCNA efficacy.

## hmmm

The floor is fixed and definitions cannot expand it. The living boundary is the exact UCNS construction that preserves the ordered relational content of a definition while composing its constituent floor gonols into one definition gonol, plus the source/custody procedure for producing a complete closed definition set without silently importing out-of-floor lexical material.
