# Recursive attachment stack

GPT generated; context, prompt Erin Spencer.

> **Standing:** historical/replay geometry for text after the Unicode scalar gonol replacement. Existing receipts remain valid evidence of this profile; new Unicode text construction must use `ucns.unicode_gonol` and must not treat ordinal radius-halving or the closed-bearing candidates below as active canon.

This version implements the operator-specified planar attachment and halving
construction. Each halving is one disk depth. The same operation accepts a
primitive or an already closed construction. It does not require a physical
camera model, a separately allocated SPACE object, or a linguistic scale ladder.

## Operation and exact representation

For ordered occurrences numbered from zero, depth is `n-i` and local radius is
`R/2**(n-i)`. The local direction composes with the previous placement heading;
the previous endpoint supplies the next local origin. Appending halves earlier
parent placements and adds a newest radius `R/2`. Closed interiors retain their
own local coordinates. Parent depiction and child-local coordinates are distinct.

`Direction` represents an exact unit complex expression: a rational turn and
zero or more normalized endpoints of retained closed constructions. `Point`
represents an exact rational linear combination of these directed rays. This
is constructive geometry, not a floating-point coordinate array or a hash used
in place of geometry. A hash indexes a complete retained construction graph.

Expression equality combines identical terms and cancels inverse factors. It
is **not** a complete test for geometric equality between different expressions.
For example, it does not decide every cyclotomic identity. `display` is secondary
and refuses detected floating range/collapse failures; small numeric differences
or coincidence in a display are not evidence of exact equality or inequality.

Common-origin views retain the ordered local displacement rays. Attached-origin
views are their ordered prefix sums. Subtraction recovers the rays without glyph
labels. The root origin and SPACE direction travel with each exported view.
These are recoverably related views, not generally congruent point sets.

## Closed bearings: explicit candidate boundary

Recursive stacking is specified. The exact direction extracted from a whole
closed construction has no selected numerical functional in the source record.
`Closed(interior, bearing)` therefore requires one explicit candidate:

| Binding | Exact direction | Standing |
|---|---|---|
| `root-endpoint-v1` | Normalize the vector from the construction root to its endpoint | Unselected candidate |
| `exit-heading-v1` | Reuse its accumulated final placement heading | Unselected candidate |

A finite dyadic stack's endpoint is nonzero: its final radius `R/2` exceeds
the sum of all earlier radii `R/2 - R/2**n`. Endpoint normalization is therefore
well-defined at every recursive stack level, regardless of the participant
directions. This does not prove a particular candidate is the intended bearing.
The exit-heading candidate can coincide for permuted interiors; interiors are
never replaced by that heading. No hash, centroid, separate word carrier or
terminal glyph identity is substituted for the whole closed construction.

## Usage

```python
from ucns.ordinal_affixiation import Carrier, Participant
from ucns.attachment_stack import Closed, stack, common_view, attached_view, recover_common, attach
from ucns.attachment_codec import export_graph, replay_graph, export_view, replay_view
from ucns.public_gonol import PUBLIC_GONOL_157, PUBLIC_GONOL_SHA256

carrier = Carrier(PUBLIC_GONOL_157, PUBLIC_GONOL_SHA256)
def build(text):
    return stack(text, tuple(Participant.atom(carrier, g) for g in text),
                 relation='declared-order', source='example')

left, right = build('bull'), build('shit')
assert recover_common(attached_view(common_view(left))) == left.rays
# Explicit compound transport: second l, zero-based occurrence 3.
incoming = attach(left, 3, right)
# Explicit candidate evaluation; no selection is implied.
sentence = stack('example', (Closed(left, 'root-endpoint-v1'),
                             Closed(right, 'root-endpoint-v1')),
                 relation='declared-sequence', source='example')
assert replay_graph(export_graph(sentence)).recover() == tuple('bullshit')
assert replay_view(export_view(sentence))[0].receipt == sentence.receipt
```

`attach` rigidly transports an incoming stack without recontracting its radii.
`join` closes an explicit terminal attachment as an `AttachmentJoin`, retaining
both components, their boundary and relation. A joined construction can itself
participate atomically in a later stack. Unlike a dyadic stack, a join can have
a zero endpoint. Endpoint-bearing promotion therefore requires an exact nonzero
proof: strict ray-length dominance or a pure prime-order cyclotomic coefficient
check. Zero or unsupported cases refuse that candidate; the exit-frame candidate
remains defined. UCNS does not infer compound spelling,
sentences, punctuation functions or definition ownership.

`export_graph` includes all carriers and interiors. Replay requires the complete
canonical graph and rejects cycles, missing references, extra nodes, changed
bindings and substituted receipts. It accepts data, never executable expressions.
The historical `ordinal_affixiation` schema remains explicitly replayable; its
old shared-origin geometry is not relabeled as this new attachment construction.

## Verification and boundary

Run the complete outcome gate, contract audit, build and Twine checks in README.
Focused checks: `.venv/bin/python -m pytest tests/test_attachment_stack.py`.
The native suite includes all 24,336 non-SPACE Public Gonol pairs against an
independent exact cyclotomic coefficient oracle; iterative append examples;
both-view recovery and root-frame controls; closed recursion; compound transport;
deep graph replay; malformed/tampered records; and display underflow controls.

The new CHECKS entries leave the selected-boundary executor's required timeout
as `hmmm`: no claim-relevant or externally imposed per-check deadline has been
specified. The complete suite outcome gate executes without an invented time
cutoff. Running these new checks through the separate timeout-boundary executor
requires resolving that operational field first; its refusal is not waived.

**hmmm:** Selection of the closed-construction bearing functional; complete
geometric equivalence of different exact expressions; native Möbius lift and
sheet-state transport; domain-specific admission and closure outside this API.
