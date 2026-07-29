# UCNS–EDCM v0.9 exact-rational transverse envelope

**Status:** implemented corrective experiment; no transverse cover embedding,
carrier, or coordinate convention selected.

**Depends on:** the v0.6 native framed root loop and the v0.7 exact root-loop
cover chart.

## Result

v0.9 repairs the v0.8 evidence boundary before extending the rational stress
domain.

The executable relationship is:

```text
(native framed root state, exact local transverse value)
    ↔
(v0.7 root-loop chart, exact transverse sidecar, named convention)
```

The transverse value is explicitly marked `unmapped-sidecar`. It is not
represented in the actual directed-cover coordinate.

## Exact-rational domain

The state constructors accept exact `Fraction` values:

```text
u ∈ Q ∩ [-1, +1]
```

The mapping and motion functions are parametric over admitted exact rational
values. The report does not call finite testing a proof over all rationals. Its
reproducible stress domain contains every reduced fraction in the bound whose
denominator is at most eight:

```text
45 exact fibers
```

This is dense finite pressure, not real-valued continuity.

## Coordinate descriptions

For native state `(p, ε, u)`, v0.7 still supplies:

```text
α = p       when ε = +1
α = p + 1   when ε = -1
```

v0.9 retains two sidecar descriptions:

```text
local-frame: (α, u)
global-side: (α, εu)
```

The cover sheet recovers `ε`, making the descriptions exactly reversible. No
convention is selected.

## Explicit comparison policy

Every round trip, restriction, motion square, convention change, collision, and
report verdict retains:

```text
policy: transverse-envelope-exact@0.9.0
implementation: ucns.comparison:exact_comparison_policy
```

Comparisons operate on explicit candidate identity tuples. They do not depend
on hidden tolerance or whole-dataclass equality.

## Complete witness validation

The report reconstructs and validates the expected ordered keys for every:

- source-linked initiation;
- exact stress fiber;
- coordinate convention; and
- declared transition.

Count-preserving substitution therefore fails. Repeating one row 1,260 times
cannot impersonate complete evidence.

## Executed evidence

The default v0.9 run produces:

- 14 source-linked word initiations;
- 45 exact rational stress fibers;
- 2 coordinate conventions;
- 1,260 policy-bound two-way envelope round trips;
- 28 exact v0.7 root restrictions;
- 5,040 envelope/motion commutation witnesses;
- 630 two-way convention round trips;
- 2,520 convention/motion commutation witnesses;
- 28 explicit actual-cover collision witnesses;
- the unchanged v0.7 48-cell F01–F16 matrix;
- all 27 simultaneous `M × B` displays; and
- `selection_effect = "none"`.

## Actual-cover collision

For each initiation and convention, v0.9 compares the envelopes at `u = -1`
and `u = +1`.

Their complete envelope identities differ, but their actual cover identities
are identical:

```text
envelope(α, -1) != envelope(α, +1)
actual_cover(α, -1) == actual_cover(α, +1) == v0.7_root(α)
```

This is positive evidence that the sidecar is not an injective transverse cover
map.

## Falsifier boundary

The embedded carrier matrix is exactly the v0.7 matrix:

- `F12` remains supported only for
  `ucns.edcm.mobius-directed-cover-root-loop-chart@0.7.0`;
- `F13` remains falsified only for that same root-loop domain; and
- transverse directed-cover extension is `inconclusive`.

No v0.9 envelope identity is attributed to F12 or F13.

## Boundaries

v0.9 does not:

- map transverse displacement into carrier breadth, radius, angle, or another
  directed-cover coordinate;
- treat the sidecar as faithful breadth `B`;
- prove every rational input by finite sampling;
- establish real-valued continuity;
- assign arbitrary source elements;
- define radial, circle, epicycle, disk, sphere, or recursive-scale motion;
- define higher-gonol composition or scoped completion;
- select a carrier or coordinate convention;
- activate EDCM production; or
- activate METAPAT.

## Reproduction

```text
python -m pytest tests/test_transverse_envelope.py -q
python -c "from ucns import run_v09_transverse_envelope_experiment; r = run_v09_transverse_envelope_experiment(); print(len(r.fibers), len(r.round_trips), len(r.carrier_collisions), r.transverse_cover_verdict.value, r.selection_effect)"
```

Expected compact result:

```text
45 1260 28 inconclusive none
```

hmmm: exact sidecars now know they are sidecars. The next lawful move is an
injective cover coordinate or a separating proof that no admissible one can
preserve the required state.
