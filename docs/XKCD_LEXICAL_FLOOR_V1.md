# xkcd lexical-floor candidate v1

**Authority:** Erin Spencer
**Recorded:** 2026-08-18
**Status:** implemented candidate; no selection, OEWN closure, or family-map invention

This is the current UCNS lexical-floor candidate. It is not the deprecated
NGSL 1.2 closed floor and it does not constrain OEWN definition recursion.

## What the floor is

The floor binds two already-pinned surfaces into one named object:

```text
xkcd Simple Writer 0.2.1 exact bytes
    ↓
3,634 unique accepted surfaces in source order
    ↓
atomic history-bearing word gonols
    ↓
ucns.lexical-floor.xkcd-simplewriter-0.2.1
```

Each completed word gonol is atomic at the next scale. The floor does not
materialize an authoritative all-pairs relation table.

xkcd describes the underlying Thing Explainer set as “ten hundred words.”
The official artifact contains 3,634 surfaces and no authoritative
surface-to-family map. The floor records `family_count = 1000` and
`family_mapping_available = false`. It does not invent the map.

## What the floor is not

- not a closed definition-support set
- not a 1,000-lemma morphology inventory
- not a replacement for OEWN 2025 Core
- not a revival of NGSL closure
- not selected UCNS canon
- not a METAPAT Theory 10 mapping

Historical NGSL machinery remains in `src/ucns/lexical_floor.py` as
deprecated evidence.

## Usage

```python
from ucns import load_xkcd_lexical_floor, replay_xkcd_lexical_floor

floor = load_xkcd_lexical_floor()
assert floor.contains("branch")
word = floor.word_gonol("branch")
assert word.atomic_at_next_scale
replay_xkcd_lexical_floor(floor)
```

Unknown, casefolded, or whitespace-padded spellings fail closed.

## Module

```text
src/ucns/lexical_xkcd_floor.py
tests/test_lexical_xkcd_floor.py
```

Depends only on `lexical_sources` and `lexical_word_gonols`.

## hmmm

- authoritative 3,634 → 1,000 family mapping
- artifact-specific license applicability of the packaged `words.js`
- whether any later definition corpus should be constrained by this floor
