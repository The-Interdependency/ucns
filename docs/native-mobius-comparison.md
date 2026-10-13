# Native Möbius comparison — derived root-loop law v1

## Domain and standing

`ucns.native-mobius-comparison@1.0.0` names an exact displacement class
between complete framed states in **one already identified native root-loop
chart**. UCNS owns this geometric sense. The implementation is an opt-in derived
geometry module; it neither selects a full UCNS carrier nor changes CANON.md.

Here **comparison** is relative complete-state displacement. **Transport** is
application of that displacement class using `NativeMobiusState.advance`.
Neither word authorizes a relation between independently rooted application
objects, communication, synchronization, a codec operation, or an inferred
traversal history. Those potentially colliding senses are explicitly excluded.
The domain claim is provisional for downstream adoption; the algebra below is
conditional only on the existing exact root-loop definition.

The native authority is `src/ucns/direct_mobius.py` at UCNS commit
`5a042416ef62abd9b674523284c2a31193918d66`, Git blob
`14a4cee36b5bbfa72cf3c03703c427abdac7f33d`. Its quotient and motion remain unchanged.
This follows METAPAT's domain restraint: geometry supplies no semantic,
empirical, cryptographic, or protocol standing merely by structural resemblance.

## Problem and frozen acceptance criteria

Multiplying canonical endpoint frame signs alone is not invariant under equal
native motion: exactly one endpoint can cross the representative seam. The
comparison must retain complete target reconstruction while removing this
coordinate artifact. Dropping the frame bit is not a repair.

Acceptance requires exact reconstruction, common-motion invariance, equivalent
representative invariance, orientation-reversal covariance, composition,
inverse, identity, the frame carry cocycle, malformed-input rejection, and
sensitivity to both the naive-product and phase-only ablations. Tests must
retain the 360-degree frame reversal and the 720-degree complete return.
No origin alignment, path winding, higher geometry, or downstream utility is
admitted by these criteria.

Implementation plan: add `src/ucns/mobius_comparison.py`, its source-owned
contracts, `tests/test_mobius_comparison.py` with accountable witnesses, and this
document plus `docs/work-graphs/native-mobius-comparison-inputs.json`. The dependency is the unchanged native motion implementation. All
state is immutable and exact; there are no network, storage, permission, or
user-data effects. Rollback removes these four files and any explicit future
consumer pins. The package root facade and native law remain unchanged.

## Derivation

Write a canonical native state as `s = (p, e)`, where `0 <= p < 1`, `p` is
rational, and `e` is either +1 or -1. The existing quotient is

    (t, e) ~ (t+n, (-1)^n e),  n in Z.

Let `b(e) = (1-e)/2`, and define the complete-state coordinate

    q([t,e]) = t + b(e)  (mod 2).

This is well-defined: replacing `(t,e)` by `(t+n,(-1)^n e)` changes
`t+b(e)` by an even integer. Conversely, equality modulo two implies an
integer difference in `t` with exactly the required frame parity. Thus `q`
is a bijection between the exact native framed state set and `Q / 2Z`.
It is a coordinate on the existing framed root loop, not an untwisted
visible-circle substitute or an assertion about all UCNS geometry.

For native motion `A_u`, set `k = floor(p+u)`. The existing implementation gives

    A_u(p,e) = (p+u-k, (-1)^k e).

Therefore

    q(A_u(s)) = q(s) + u  (mod 2).

Define the comparison from `a` to `b` by its canonical representative:

    D(a,b) = (q(b)-q(a)) mod 2,  0 <= D < 2.

This immediately proves, for every admitted exact rational input:

    A_D(a) = b,
    D(A_u(a), A_u(b)) = D(a,b),
    D(a,c) = D(a,b) + D(b,c)  (mod 2),
    D(b,a) = -D(a,b)  (mod 2),
    D(a,a) = 0.

The displacement class is unique because `q` is bijective. No new preferred
zero was chosen: simultaneous translation of the existing chart cancels in
the difference.

### The missing seam correction

Let `d = (p_b-p_a) mod 1`. Transport over this nonnegative visible arc crosses
the canonical seam exactly when `p_b < p_a`. Consequently the corrected frame
comparison is

    chi(a,b) = e_a e_b (-1)^[p_b < p_a],
    D(a,b) = d + (1-chi(a,b))/2.

The extra sign compares the target frame with the source frame **after**
transport over the specified visible arc. It is not another independent bit
invented from metadata. The implementation stores only `D`; `d` and `chi` are
projections, so they cannot drift apart.

Composition of the split representation has a carry:

    chi(a,c) = chi(a,b) chi(b,c) (-1)^floor(d(a,b)+d(b,c)).

Multiplying split signs without this carry would recreate the original defect
at composition rather than endpoint comparison.

### Coordinate scope

Common exact rational translations leave `D` invariant. Independently changing
integer representatives of either endpoint leaves their quotient states and
`D` unchanged. Reversing the native chart orientation sends `q` to `-q`, so it
sends `D` to `-D mod 2`: **covariance**, not invariance under reflection.

These statements concern the declared native affine charts and quotient
representatives. Arbitrary nonlinear reparameterizations or independently
chosen local frame gauges require their own transformation/connection rule;
this module does not silently claim that broader scope.

## Usage

```python
from fractions import Fraction
from ucns.direct_mobius import native_mobius_state
from ucns.mobius_comparison import compare_native_mobius

a = native_mobius_state(Fraction(3, 4))
b = native_mobius_state(Fraction(1, 4))
c = native_mobius_state(Fraction(2, 3))
ab = compare_native_mobius(a, b)
bc = compare_native_mobius(b, c)

assert ab.relative_turns == Fraction(3, 2)
assert ab.phase_turns == Fraction(1, 2)
assert ab.frame_sign == -1
assert ab.transport(a) == b
assert ab.inverse().transport(b) == a
assert ab.then(bc) == compare_native_mobius(a, c)
assert compare_native_mobius(a.advance(Fraction(1, 2)),
                             b.advance(Fraction(1, 2))) == ab
```

The constructor `NativeMobiusComparison` accepts only canonical `Fraction`
values in `[0,2)`. Prefer the comparison function for endpoint inputs. Negative
or multi-turn **motion** remains available through the native `advance` method;
comparison intentionally records only the resulting class modulo two.

Consumers must establish common-chart eligibility **before** calling this
module. Equal coordinate numbers, equal frame labels, or serialization ancestry
alone do not establish alignment of independent origins.

## Falsification and replay

Run the complete source, distribution, and replay gates in the repository
README. The six new accountable tests additionally provide:

- all 16 complete states on the eight-phase grid, all 256 ordered endpoint
  pairs, and all 33 motions from -2 to +2 turns in eighth-turn steps: 8,448
  checks; corrected changes 0, naive endpoint-product changes 2,688;
- exact rational non-grid and 80-digit near-seam inputs; independent endpoint
  representative changes and orientation-reversal covariance;
- all 4,096 triples on that full grid for composition and the carry cocycle;
- explicit counterexamples to the naive product and phase-only substitutes;
- rejected floats, booleans, invalid ranges/types, and immutable records;
- one-turn versus two-turn return, and the endpoint-only winding limitation.

Those finite execution counts are implementation witnesses. The general claim
rests on the exact algebra above, not on extrapolating a finite grid.

## hmmm

Complete-state comparison is implemented. Alignment between independently
rooted charts, actual path winding beyond modulo two, origin-to-origin protocol
transport, nontrivial holonomy from observed paths, higher-scale geometry,
downstream utility, and full-carrier selection remain outside this result.
In particular, endpoint comparisons around a closed complete-state chain
compose to identity; that tautology is not new evidence of path holonomy.

## Input work graph

`docs/work-graphs/native-mobius-comparison-inputs.json` is the shared exact
input-authority graph, not a claim about a future consumer deployment. Its digest
is `bd1059322ef8223d2a6531f84591e76970db67aa3982f1cbfd174d5039b5ecd5`. The output implementation is identified separately by
the delivering commit and source hashes. Consumer receipts must additionally pin
the delivered UCNS implementation; they must not mistake the native-law input
commit in this graph for that later output. Certification and empirical status
also do not transfer. This adds no participant to Stack and changes no global pin.
