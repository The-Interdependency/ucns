# Recursive Unicode object completion

GPT generated; context, prompt Erin Spencer.

Research area: UCNS, priority 1. Stack owns language admission; UCNS owns these
objects and the declared local-frame geometry. This repairs object completion
without selecting an automatic next-scale bearing.

## Contract

`close_unicode` consumes ordered native glyphs, complete scalar frames, or its
own completed frames. Every occurrence retains its actual interior. One positive
exact parent radius applies to every sibling origin. Primitive glyph bearings
come from the existing Unicode scalar rule. For completed frames, the caller
must supply one exact parent bearing per occurrence. No label, hash, terminal
glyph, ordinal halving or historical candidate supplies that bearing.

At bearing `t`, parent radius `R`, and declared local rotation `a`, the native
point map is `T(z) = R exp(2πit) + exp(2πia) z`. Its inverse is
`T⁻¹(w) = exp(-2πia) (w - R exp(2πit))`. Existing native `Point` and `Direction`
expressions implement both operations exactly. Child-local radii stay unchanged.
Rotation defaults to zero, preserving the child's SPACE orientation; it does not
infer an affixiation transform. Nested placement composes these same maps.

```python
from fractions import Fraction
from ucns.unicode_gonol import build_unicode_scalar_frame
from ucns.unicode_recursive import close_unicode, export_unicode_graph, replay_unicode_graph

word = build_unicode_scalar_frame("Aë e\u0308!\n")
pair = close_unicode((word, word), bearings=(0, Fraction(1, 2)),
                     relation="ordered", source="example:pair")
parent = close_unicode((pair, pair), bearings=(0, Fraction(1, 2)),
                       relation="ordered", source="example:parent", radius=3)
assert parent.recover() == word.text * 4
assert parent.participants[0] is pair
assert replay_unicode_graph(export_unicode_graph(parent)).receipt == parent.receipt
```

The graph includes every retained object, source, relation, occurrence, exact
placement and receipt. Shared storage never deduplicates occurrences. Graph
replay refuses missing/extra nodes, cycles, changed scalar anatomy, changed
placement, noncanonical rationals and altered provenance, even if the outer
digest is recomputed. Receipts establish integrity, not authentication.

Run `python -m pytest tests/test_unicode_recursive.py`; the complete geometry
outcome gate remains required. Tests include 1,100 nested levels, exact composed
placement/inversion, Unicode/UTF-8/UTF-32BE recovery, sharing, and negative inputs.
Existing v2 glyph/frame receipts and historical attachment producers remain
unchanged. Rollback selects the prior pinned producer and consumer together.

## hmmm

Automatic next-scale bearing selection, affixiation beyond declared rigid
placement, physical sheet lifting and domain semantics remain outside this
constructor. This result establishes recursive completion for declared frames;
it does not establish the complete UCNS scale-transition law.
