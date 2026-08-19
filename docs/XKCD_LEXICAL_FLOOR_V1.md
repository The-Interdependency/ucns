# xkcd lexical-floor reconstruction v1.1

**Authority:** Erin Spencer
**Recorded:** 2026-08-19
**Status:** punctuation-aware reconstruction candidate; not selected canon

This is the reconstruction of the xkcd Simple Writer 0.2.1 source in which
Public Gonol punctuation and symbol functions participate intrinsically.
It is not a completed selected floor and it does not close OEWN definitions.

The earlier named binder over character-history word gonols is only scaffolding.
It is not the reconstruction required by the current construction frontier.

## Construction

```text
official quoted payload: word|word|...
    ↓
letter-runs (ASCII a-z)
+ Public Gonol function participants
    (intra-word ' and ’, every source VERTICAL LINE, any other functional glyph)
    ↓
ordered occurrences, exact spans, reused identities
    ↓
relation enters an intrinsic carrier
    ↓
closed surface gonols and one closed source-stream floor
```

Letter-runs are lexical. A glyph at a Public Gonol punctuation or symbol
index is a function participant keyed by that canonical index. The
implementation does not attach an independent punctuation grammar.

xkcd describes the Thing Explainer set as “ten hundred words.” The official
artifact contains 3,634 surfaces and no authoritative family map. The floor
records `family_count = 1000` and `family_mapping_available = false`.

## Usage

```python
from ucns import (
    load_xkcd_lexical_floor,
    reconstruct_xkcd_lexical_floor,
    replay_xkcd_lexical_floor,
)

floor = load_xkcd_lexical_floor()
assert floor.punctuation_functions_intrinsic
assert floor.closed_surface("don't").occurrences[1].kind == "public-gonol-function"
assert sum(
    item.public_gonol_index == 47 for item in floor.function_occurrences()
) == 3633
replay_xkcd_lexical_floor(floor)
```

To bind already-constructed Public Gonol function identities:

```python
floor = reconstruct_xkcd_lexical_floor(source, table)
```

`table` is optional. Without it, function participants still use canonical
Public Gonol indices. With it, `apply_public_gonol_function` records
construction applications over the exact stream.

Unknown, casefolded, or padded spellings fail closed.

## Module

```text
src/ucns/lexical_xkcd_floor.py
tests/test_lexical_xkcd_floor.py
```

Depends on `lexical_sources`, `public_gonol_functions`, and
`relational_carrier`. It does not wrap `lexical_word_gonols`.

## hmmm

- authoritative 3,634 → 1,000 family mapping
- artifact-specific license applicability of the packaged `words.js`
- whether any later definition corpus should be constrained by this floor
- geometry of contextual function application
