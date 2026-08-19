# xkcd lexical-floor reconstruction v1.2

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
    FunctionApplicationPlan,
    load_xkcd_lexical_floor,
    reconstruct_xkcd_lexical_floor,
    replay_xkcd_lexical_floor,
)
from ucns.public_gonol_functions import AtomicFunctionState

floor = load_xkcd_lexical_floor()
assert floor.punctuation_functions_intrinsic
assert floor.closed_surface("don't").occurrences[1].kind == "public-gonol-function"
assert sum(
    item.public_gonol_index == 47 for item in floor.function_occurrences()
) == 3633
replay_xkcd_lexical_floor(floor)
```

A surface such as ``don't`` closes at word scale as letter-runs plus the
intra-word apostrophe function. That closed surface is later consumed
atomically by definition construction. The floor does not reopen it.

To bind already-constructed Public Gonol function identities, supply the
table and every application as an explicit occurrence-addressed plan:

```python
floor = reconstruct_xkcd_lexical_floor(
    source,
    table,
    (FunctionApplicationPlan(ordinal, AtomicFunctionState(state_id), (context_ordinal,)),),
)
replay_xkcd_lexical_floor(floor, table)
```

`table` is optional. Without it, function participants still use canonical
Public Gonol indices and no applications are recorded. Neighboring stream
participants are never inferred as current state or context. The receipt
binds each application's ordered identity, result, function, and occurrence
addresses. Replay requires the same table and plans. Packaged official
bytes are validated before a floor receipt is minted.

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
