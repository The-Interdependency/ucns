# Generic gonol constructor — affixiate candidate

**Authority:** Erin Spencer
**Recorded:** 2026-08-19
**Status:** declared candidate constructor; selection `UNRESOLVED`
**Selection effect:** none

This preregisters evaluation criteria before a completion receipt is minted.
It does not select `affixiate` as canon.

## Decision

```text
affixiate(gonols, relation, source, scale, closure) -> gonol
```

One constructor is used at every scale. Character, word, morphology,
definition, relation, sentence, paragraph, chapter, and work are scale
contexts, not different object types. Sentence, paragraph, chapter, and
work have no source construction in this change.

## Frozen constructor identity

```text
constructor_id: ucns.gonol.affixiate
version:        0.1.0
standing:       generic-affixiation-candidate
selection:      false
```

## Frozen application order

1. Close OEWN 2025 Core lemmas and forms from corpus-wide character history.
2. Resolve xkcd Simple Writer 0.2.1 surfaces against those closed words.
   Shared surfaces reuse OEWN word identities. Surfaces absent from the OEWN
   inventory are closed against OEWN-wide admissible paths and recorded as
   absent; they are not a 3,634→1,000 family map.
3. Build definition and recursive gonols with the same primitive, keeping
   source-specific receipt wrappers.

## Full-scope receipts (2026-08-19)

Independent reconstruct and replay of the declared OEWN 2025 Core scope,
followed by xkcd subset resolution:

| Artifact | Identity |
|---|---|
| Character-word corpus | `ucns.character-word-corpus:sha256:4f26c5c614434268e396450a2626bec576cde654fbff2deb95b6acbdca81268d` |
| xkcd floor v1.4 | `ucns.xkcd-lexical-floor-receipt:sha256:31a1b3bdf6ba56ccd2ce28def049bfe7802d556b5d1794f166fc017088ad57aa` |
| Affixiate definition layer | `ucns.oewn-definition-layer:sha256:00845896f42528bb5389064f5714a4774794425138e4bc9ef7cac00f0839bffa` |
| Affixiate recursive layer | `ucns.recursive-gonol-layer:sha256:822d983ec6e3cc68484c88e793f53c05da8c77e50cf8f9c8d8eb16ff40a06793` |

Counts: 131798 closed OEWN lemma/form surfaces, 92021 tokens, 3634 xkcd
surfaces of which 1618 are absent from the OEWN inventory, 185155 definition
gonols, 244727 recursive gonols, `selected=false`. Replay `SURVIVED`. That
does not select the constructor as canon.

## Frozen nonclaims

- `selected` remains false
- no invented xkcd family mapping
- no morphology decomposition law
- historical receipts are not rewritten:
  `generated/oewn-2025-core-definition-layer-receipt.json`,
  `generated/oewn-2025-core-punctuation-aware-definition-layer-receipt.json`,
  `generated/oewn-2025-core-source-native-recursive-gonol-receipt.json`

## Frozen evaluation criteria

1. `affixiate` returns `Gonol` at every declared scale context used.
2. Scale is a bound field, not a Python type.
3. Relation enters the carrier; the result is atomic at the next scale.
4. OEWN character admissible futures come from the complete lemma/form token
   inventory of the supplied snapshot.
5. Independent rebuild of the declared scope is byte-identical.
6. Historical generated receipts remain byte-identical on disk.

## Usage

```python
from ucns import affixiate, AffixiationRelation, AffixiationSource, AffixiationClosure
from ucns import build_oewn_character_word_corpus, reconstruct_xkcd_lexical_floor

corpus = build_oewn_character_word_corpus(snapshot)
floor = reconstruct_xkcd_lexical_floor(xkcd_source, corpus)
```

hmmm: selection of this constructor as canon remains separate from
implementing and testing it.
