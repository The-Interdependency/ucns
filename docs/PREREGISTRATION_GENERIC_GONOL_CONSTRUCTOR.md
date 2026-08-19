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

One constructor is used at every scale. Characters are gonols. Character,
word, morphology, definition, relation, sentence, paragraph, chapter, and
work are scale contexts, not different object types. An atomic character
glyph gonol has no smaller gonol participant; history-bearing character
gonols affixiate that glyph gonol. Sentence, paragraph, chapter, and work
have no source construction in this change.

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
| Character-word corpus | `ucns.character-word-corpus:sha256:dd033fe1b533b9d65a0755b1391c15ccf0d864f06ffe8d4b5a72f23b52444d57` |
| xkcd floor v1.4 | `ucns.xkcd-lexical-floor-receipt:sha256:ea27e4de3e2ab9cdd7cb9e865727b57f5d8ae08700fb19844a2ec0354439d4e7` |
| Affixiate definition layer | `ucns.oewn-definition-layer:sha256:0242af7a53d0e6a9b1095136e1dd139a4822700c8b6700ee104e229dcb646b2b` |
| Affixiate recursive layer | `ucns.recursive-gonol-layer:sha256:78ee88fa67c2a39973b27cede9d2dbf4e7a09d572a22cadcddbbd5d30a85dc8a` |

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
