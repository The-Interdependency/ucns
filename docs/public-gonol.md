# UCNS public gonol canon

**Status:** `IMPLEMENTED` in the Python package; source parity and behavior are
covered by `tests/test_public_gonol.py`. This promotion adds no factorization,
linguistic, embedding-performance, EDCM-measurement, or METAPAT-validity claim.
The origin/orientation surface is also represented in
`formal/Ucns/PublicGonol.lean`; `lake build` is the execution authority for that
formal file.

## Authority

The public gonol is promoted from:

```text
repository: The-Interdependency/a0-betatest
commit:     7af8debf6ef3905f01baff02b43d8c3bee16ccbc
```

Load-bearing source surfaces:

```text
memory/ARCHITECTURE_FOUNDATION.md                    F3 / F4
backend/interdependent_lib/gonal/gonal.py             public arrangement
backend/interdependent_lib/gonal/faces.py             faces / chirality / adjacency
backend/interdependent_lib/gonal/mirror.py            origin-fixed mirror
backend/interdependent_lib/gonal/lifted_path.py        lossless text traversal
backend/interdependent_lib/zfae/gonal_inscription.py   fixed-origin private transform
```

UCNS is now the canonical package home. A0 and EDCM remain downstream consumers;
they must not maintain competing copies as authority.

## Canon

The public gonol has `ARITY = 157`.

Position zero is:

```text
SPACE
ZERO
Möbius twist point
the seam
the origin for the entire system
the only always-known character
```

The glyph `"0"` is not zero. It is an ordinary digit glyph at its own nonzero
carrier position.

The fixed origin is not an arbitrary first anchor and is not removed by
normalization. Private phase and permutation may obscure every nonzero position,
but they do not move or hide position zero:

```text
perm[0] == 0
phase acts on positions 1..156
permutation acts on positions 1..156
```

The exact arrangement is exported as `PUBLIC_GONOL_157` and `EXAMPLE_157`. Its
one-glyph-per-line SHA-256 is:

```text
20d6ed51fdff5505ed9696c38d6dcc82f982eba166d9b712bee68c4521b751ac
```

## Orientation and complete return

The Möbius twist makes orientation part of the public frame.

```text
one carrier circuit = 360 degrees
result after one circuit = same local position, opposite orientation
complete system return = two circuits = 720 degrees
```

Therefore a local recurrence after 360 degrees is not the complete UCNS return.
The full return requires restoration of orientation after 720 degrees. This is a
load-bearing property of the public gonol, not a convention imported from the
normalized factorization model.

## Faces, chirality, mirror, and adjacency

The promoted API preserves the A0 definitions:

```python
from ucns import (
    ARITY,
    ORIGIN,
    face,
    chirality,
    n_plus,
    n_minus,
    mirror_of,
)
```

The upper public face occupies positions `1..78`, the lower public face occupies
positions `79..156`, and position zero remains the origin. The mirror is the
position reflection across the diameter through position zero and therefore
keeps the origin fixed.

No replacement algebra, angle conversion, quotient interpretation, or gauge
model is introduced by this promotion.

## Lossless lifted traversal

```python
from ucns import encode_text_path, decode_text_path

path = encode_text_path("a a")
assert decode_text_path(path) == "a a"
```

The path is an ordered, strictly increasing traversal. A repeated character
advances by a full 157-step revolution. SPACE is emitted as a seam event rather
than deleted. Characters outside the public carrier raise `CarrierCharError`.

The expression `position % 157` is preserved exactly where the A0 source uses it
to recover the local carrier position from a lifted path. This document does not
extend that operation into an unratified mathematical interpretation.

## Relationship to ordinary `UCNSObject`

`UCNSObject.normalize()` remains unchanged in this promotion. It normalizes the
recursive factorization object representation by shifting an object's first
internal value. That local representation rule is not applied to the public
gonol.

The public gonol and ordinary `UCNSObject` are therefore distinct public
surfaces in this patch:

```text
public gonol:
    fixed system origin, twist-bearing carrier, and 720-degree return canon

UCNSObject:
    existing normalized recursive factorization object
```

A future bridge between them must be explicitly specified and ratified. This
promotion does not invent one.

## Usage

```python
from ucns import (
    PUBLIC_GONOL_157,
    ORIGIN,
    vertex_of_char,
    char_of_vertex,
    encode_text_path,
    decode_text_path,
    PrivateGonal,
)

assert PUBLIC_GONOL_157[ORIGIN] == " "
assert char_of_vertex(vertex_of_char("0")) == "0"
assert decode_text_path(encode_text_path("aa")) == "aa"
assert PrivateGonal.from_seed(b"agent").perm[ORIGIN] == ORIGIN
```

## Migration order

1. UCNS owns and exports the exact canon.
2. `a0-betatest` replaces its local authority with UCNS imports or strict parity
   wrappers.
3. EDCM removes its copied public-gonol authority and consumes UCNS.
4. Corpus or word-list tools remain downstream applications.

## hmmm

The public gonol is promoted exactly. Any bridge from this twist-bearing global
frame into another UCNS representation remains unresolved until Erin specifies
it; no guessed mathematics fills that gap.
