# Ordinal affixiation and expanded angular carriers

Operator construction requested October 13, 2026 (America/Los_Angeles).

## Construction

The initial finite field has distance R between every pair of distinct admitted
identities. Angular placement is a declared transport from that field to a
circle, not an assertion that a large equidistant simplex fits isometrically
in a plane.

For zero-based occurrence i among n ordered participants, the radius is
R / 2**(n-i), and the angle is its exact carrier index / carrier arity, in turns.
Appending halves all earlier radii and puts the new occurrence at R/2.
Repeated identity retains its carrier angle and receives a different ordinal
radius. Initial equidistance is not asserted after this transformation.

Carrier order is explicit input. UCNS assigns no language categories, corpus
membership, operator meanings, or lexical order. English supplies its new
repertoire and versioned ordering recipe. Historical Public Gonol 157 receipts
are not rewritten to masquerade as the expanded carrier.

A closed construction participates atomically on another explicitly supplied
carrier. Its actual interior remains constitutive. This recurs without a
compulsory glyph/word/sentence ladder. A receipt indexes retained geometry;
it is not the geometry and is not producer authentication.

## Usage

```python
from ucns.ordinal_affixiation import Carrier, Participant, affixiate

public = Carrier(tuple(' TES'), 'example-v1')
word = affixiate('TEST', tuple(Participant.atom(public, c) for c in 'TEST'),
                 origin='SPACE', relation='ordered', source='example:TEST')
assert [word.placement(i).exponent for i in range(4)] == [4, 3, 2, 1]
assert ''.join(word.recover()) == 'TEST'
words = Carrier(('TEST',), 'example:word-carrier')
parent = affixiate('pair', (Participant.closed(words, word),
                          Participant.closed(words, word)),
                   origin='SPACE', relation='explicit-pair', source='example:pair')
assert parent.participants[0].interior is word
```

The parent example is a pair relation, not a text parser: real text construction
must retain its exact whitespace and punctuation participants. Duplicate carrier
identities, unadmitted participants, empty closures, surrogate-containing
identities, and inexact radius arguments fail explicitly.

`Placement.record()` stores exact exponent, turn, carrier and interior identity.
`Construction` retains interiors in memory; its record is an index, not a
standalone serialized recursive graph. Persist interiors and carrier definitions
with their references when materializing a construction. No query-time admission
expansion or implicit carrier upgrade is performed.

```bash
PYTHONPATH=src python -m pytest -q tests/test_ordinal_affixiation.py
```

Local isolated-module evidence: 28 tests passed, including an independently
iterated append oracle over 1,092 sequences, 1,500 nested levels and a
10,000-halving exponent. This is not a full repository-suite or corpus receipt.
Follow AGENTS.md for complete outcome, metadata, build and Twine gates.

## hmmm

The candidate constructs exact local-frame positions and recursive participation.
Native Mobius lift, global transport between nested frames, function semantics,
and Stack's complete corpus construction have separate evidence boundaries.
