# Recursive Unicode object completion

GPT generated; context, prompt Erin Spencer.

Research area: UCNS, priority 1. Stack owns language admission; UCNS owns these
objects and their geometry. The default operation is exact recursive addition.

## Contract

`close_unicode` and `add_unicode` consume ordered native glyphs, complete scalar
frames, and completed objects. They retain every actual operand and return a
`UnicodeSum`. Its exact native `Point` resultant enters the same addition again.
There is no separate parent-bearing input to choose.

For a glyph at scalar turn `t`, the native vector is `exp(2πit)`. A scalar frame
adds those vectors at its retained geometric radius. If operand `i` has complete
result `v_i`, addition returns `sum(v_i)`. Optional exact rotations `a_i` and one
positive common scale `R` give `R * sum(exp(2πia_i) * v_i)`; defaults are zero
rotations and `R=1`. These transforms preserve the retained child objects.

Both radius and direction remain in the vector expression. Normalizing the
result to unit length would lose information and is not part of this operation.
Exact antipodal terms cancel. A zero result remains a closed object with its
whole source construction; it has no forced direction and is not Structural Null.
The resultant is a projection: equal sums do not identify distinct object graphs.

For a Unicode scalar `DiskStack`, use `word.rays` for the ordered local
placements, `word.endpoint` for their placed endpoint and
`word.additive_resultant` for the recursive sum. Each frame radius multiplies
the sum of the unit scalar vectors and complete additive results of its
children. At unit frame radii, `AB | C` and `A | BC` agree in this sum while
their glyph-scale radius sequences distinguish the word boundaries. The
native attachment graph replays all three quantities from one set of operands.

```python
from ucns.unicode_gonol import build_unicode_scalar_frame
from ucns.unicode_recursive import (
    close_unicode, unicode_resultant, export_unicode_graph, replay_unicode_graph,
)

word = build_unicode_scalar_frame("Aë e\u0308!\n")
pair = close_unicode((word, word), relation="addition", source="example:pair")
parent = close_unicode((pair, pair), relation="addition", source="example:parent")
assert parent.recover() == word.text * 4
assert parent.participants[0] is pair
assert unicode_resultant(parent) == unicode_resultant(word).scaled(4)
assert replay_unicode_graph(export_unicode_graph(parent)).receipt == parent.receipt
```

The graph includes every retained object, source, relation, occurrence, exact
result and receipt. Shared storage never deduplicates occurrences. Graph
replay refuses missing/extra nodes, cycles, changed scalar anatomy, changed
placement, noncanonical rationals and altered provenance, even if the outer
digest is recomputed. Receipts establish integrity, not authentication.

Run `python -m pytest tests/test_unicode_recursive.py tests/test_unicode_addition.py`;
the complete geometry outcome gate remains required. Falsifiers include exact
cardinal-direction sums, cancellation and reuse of zero, changed order/grouping,
1,100 nested levels, replay followed by another addition, retained child radii,
Unicode/UTF-8/UTF-32BE recovery, shared occurrences and forged-result rejection.

## Declared-placement replay

Explicit `bearings=(...)` selects the previous `UnicodeClosedFrame` operation.
At bearing `t`, parent radius `R`, and local rotation `a`, its reversible map is
`T(z) = R exp(2πit) + exp(2πia) z`. Old v2 glyph/frame records and v1 explicit-frame
receipts remain unchanged. This optional placement operation is distinct from
the default sum; its parameters do not become prerequisites for addition.

## Source and rollback

Erin Spencer requested addition whose completed result enters the same operation
again on 2026-11-15. This implementation uses UCNS's existing exact planar vector
algebra and supersedes the mandatory external-bearing barrier for that operation.
It makes no claim that a scalar sum recovers a whole construction or that every
UCNS scale transition has been solved. Rollback selects the prior pinned producer
and consumer together; it does not reinterpret an existing receipt.

## hmmm

Physical sheet lifting, domain semantics and the complete UCNS scale-transition
law remain separate. Recursive addition requires no independent bearing selector.
