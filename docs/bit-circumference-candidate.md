# Bits at circumference locations

**Standing: executable geometric candidate; unselected.**

UCNS scope: `ucns.bit-circle.v1` means a complete binary state on an explicitly
identified finite, ordered visible-circle carrier. Every admitted bit position
exists; each carries an integer 0 or 1. Position and value are distinct.
This is a specialization of finite-circle geometry. It neither replaces the
157-position Public Gonol nor supplies program semantics, a physical storage
mechanism, or a native Möbius lift. No overlapping meaning is selected by name.

Erin Spencer proposed circumference markings and cumulative glyph angles, then
asked for the construction to belong in UCNS and proposed: “if each bit is a
circumference location...” (2026-11-04, America/Los_Angeles). Equal spacing and
binary-weighted spacing are two explicit candidate interpretations implemented
here; the conversation did not select between them. GPT generated; context,
prompt Erin Spencer.

## Construction and recovery

For width \(N>0\), local ordinal \(k\), binary state \(b_k\), SPACE direction
\(s\), and orientation \(\epsilon\in\{-1,+1\}\):

\[
\theta_k=(s+\epsilon q_k)\bmod 1,\qquad
b_k\in\{0,1\}.
\]

| Placement | Local bit position \(q_k\) | Native finite-circle grid |
|---|---|---|
| `equal-v1` | \(k/N\) | \(N\) positions |
| `binary-v1` | \(2^{-(k+1)}\) | \(2^N\) positions; the \(N\) power-of-two positions carry bits |

Angles use exact rational **turns**; one turn is 360 degrees. The native
`AxisCirclePosition` binds each local address to the caller's origin receipt,
grid size, and ordinal. Frame changes move the displayed marks without changing
those local addresses. A state change alters the bit without replacing its
address. The caller supplies the meaning of the origin receipt.

Readback first inverts the frame. For `equal-v1`:

\[
k=N\bigl(\epsilon(\theta_k-s)\bmod 1\bigr).
\]

For `binary-v1`, each recovered local position must be exactly \(1/2^{k+1}\)
for one admitted \(k\). Every recovered ordinal must appear exactly once and carry a
binary value. Missing zero marks are errors. Reading geometry requires width,
SPACE and orientation; identifying which object's state was read additionally
requires its origin identity. The numeric coordinate 0 is not Structural Null.

For a byte under `equal-v1`, local bit locations are:

| Ordinal | Local turn | Angle |
|---:|---:|---:|
| 0 | 0 | 0° |
| 1 | 1/8 | 45° |
| 2 | 1/4 | 90° |
| 3 | 3/8 | 135° |
| 4 | 1/2 | 180° |
| 5 | 5/8 | 225° |
| 6 | 3/4 | 270° |
| 7 | 7/8 | 315° |

There are eight bit addresses and 256 possible binary states. `binary-v1`
instead places those eight bit addresses at 1/2, 1/4, ..., 1/256 turn, with
descending binary significance. Byte ordering, Unicode encoding, and parsing
remain caller decisions; the constructor accepts an already ordered bit tuple.

## What the sum retains

Both candidates expose the sum of the **local positions occupied by 1 states**.
For `equal-v1`:

\[
S=\sum_{k=0}^{N-1}b_k k/N.
\]

For eight bits, all 256 states produce only **29 distinct exact sums** and
**8 distinct remainders modulo one turn**. For example:

| Ordered bits | Positions with value 1 | Exact sum |
|---|---|---:|
| `10000001` | 0, 7 | 7/8 |
| `01000010` | 1, 6 | 7/8 |

The full marked circumference distinguishes them. The equal-spaced sum, remainder, bit count,
and completed-turn count do not distinguish this pair. Thus a circumference
summary's retained information depends on the placement law. Neither static
sum is automatically a winding number or an exit bearing: those require a
declared motion/attachment construction.

### Binary-weighted boundary

For `binary-v1`,

\[
S=\sum_{k=0}^{N-1}b_k2^{-(k+1)}=B/2^N,\qquad 0\le S<1.
\]

Here \(B\) is the ordinary integer value of the ordered bits, most significant
first. **The exact sum and width recover every bit.** All 256 bytes have distinct
sums; `10000001` gives 129/256 turn and `01000010` gives 66/256 turn.
The resulting sum selects one of 256 boundary bearings, while the constituent
bit locations remain individually accessible.

Concatenating a sequence \(A\) of width \(n\) and a sequence \(B\) of width \(m\)
has the geometric rule

\[
(n,S_A)\mathbin{\star}(m,S_B)
=\left(n+m,\;S_A+2^{-n}S_B\right).
\]

The first group's positions stay fixed; the second group's local angles shrink
by \(2^{-n}\). Thus `10` followed by `01` gives 9/16 turn, while the reverse order
gives 6/16. Grouping preserves the result because both associations give
\(S_A+2^{-n}S_B+2^{-(n+m)}S_C\). Simple unscaled angle addition has different
behavior and is not concatenation.

The census checks all **65,536 ordered byte pairs** under this rule. The boundary
pair recovers their bit sequence, not child origin identities, grouping history,
source provenance, or code relationships. Those require retained construction
records. Width is essential: `(1,)` and `(1, 0)` both have sum 1/2. Exact rational
angles are authoritative; a rounded display need not distinguish long sequences.
Native axis-circle receipt size limits also apply to the binary placement grid.

## Relation to the continuous glyph line

The existing `attachment_stack.join` already joins closed constructions at the
previous terminal endpoint without another contraction. `attached_view` gives
the uninterrupted line; the exact construction retains its constituent objects.
For primitive turns composed through the explicitly chosen `exit-heading-v1`
policy, the terminal direction is their angle sum modulo one turn. Grouping
preserves that direction. Reordering can preserve it too.

That is separate from the bit-circle state above. A bit-circle mark locates one
state; it does not itself command a turn or select either existing closed-bearing
policy. A full-turn lift must also be declared rather than recovered from a
direction that has already been reduced modulo one turn.

For complex coding relationships, the plausible use is **addressable boundaries
with retained interiors**: a consumer can name a precise location on a precise
object and can carry its ordered bit sequence in a binary-weighted boundary
pair. This module supplies those locations and states. A later construction must
declare how rings attach, which locations are linked, edge direction, occurrence
identity, and how recursive interiors remain recoverable. A consumer must then
test whether those relations represent its intended data flow or dependencies.
Geometric coincidence alone establishes none of those code relationships.

## Usage

From the repository root after `uv sync --locked --extra test --extra build`:

```python
from fractions import Fraction
from hashlib import sha256
from ucns.bit_circle import BitCircle, read_bit_circle, read_binary_angle

# A caller-owned carrier fixture, not a hash inferred to mean a program object.
origin = sha256(b"example:ordered-eight-bit-carrier:v1").hexdigest()
circle = BitCircle(origin, (1, 0, 0, 0, 0, 0, 0, 1),
                   space=Fraction(1, 7), orientation=-1)

# The readback receives only unordered marks and the declared frame.
bits = read_bit_circle(tuple(reversed(circle.marks)), width=8,
                       space=circle.space, orientation=circle.orientation)
assert bits == (1, 0, 0, 0, 0, 0, 0, 1)
assert circle.occupied_turn_sum == Fraction(7, 8)
address_of_first_bit = circle.positions[0].identity_sha256

weighted = BitCircle(origin, bits, placement="binary-v1")
assert weighted.occupied_turn_sum == Fraction(129, 256)
assert read_binary_angle(weighted.occupied_turn_sum, width=8) == bits
```

Replay the byte census and rejection controls:

```bash
.venv/bin/python -m pytest tests/test_bit_circle.py
```

The census reads every byte in both orientations at three exact frame offsets,
including an offset outside the equal-spaced byte grid. Binary placement also
checks both orientations, sum recovery, and every ordered byte pair. Controls
cover shuffled marks, address persistence, width/origin changes, frame loss,
equal-spaced sum collisions, and rejection of malformed geometry. The complete
repository gate remains the command under **Build** in `README.md`.

## Scope and completion

FROM: a conversational proposal to locate bits on a circumference.
TO: two named placements with exact readback and a reproducible byte census.
DONE WHEN: all 256 byte states recover, geometric errors fail closed, the
equal-spaced sum's loss is exhibited, and the binary-weighted sum recovers state
and composes by the declared ordered concatenation law.
FAILS IF: positions or zeros disappear, float rounding determines identity,
the frame is inferred silently, or equal summaries become equal objects.

Implementation files: `src/ucns/bit_circle.py`, `tests/test_bit_circle.py`, this
document, and its README link. Existing carriers and attachment policies remain
authoritative. Rollback removes the optional module and its consumer imports.

Placement authority: UCNS `CANON.md`, `AGENTS.md`, `axis_circle.py`, and
`attachment_stack.py` at `3f97f5292b0bd2dab911540062ccf79dea2be1bf`.
Domain restraint was checked against METAPAT `DOMAIN_RESTRAINT.md`, `AXIOMS.md`,
and `POSTULATES.md` at `7480d6d6d42cded74a9d69aeac975e590368c097`.
This change imports no METAPAT implementation and changes no domain authority.

**hmmm:** both spacing rules and these state placements remain candidate choices;
composition with the continuous attachment line, recursive bit-circle closure,
native Möbius transport, and usefulness for real code relationships require
their own explicit constructions and falsifiers.
