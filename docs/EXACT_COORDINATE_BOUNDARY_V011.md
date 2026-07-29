# UCNS v0.11 exact-coordinate representation boundary

**Status:** implemented exact-rational candidate evidence with explicit
binary64 collision witnesses. No carrier, coordinate law, faithful-breadth
evaluator, EDCM profile, or METAPAT profile is selected.

## Question

v0.10 found `signed-local-affine-radial` admissible after materializing the
complete 45-fiber stress domain into actual `LiftedCarrierPoint` breadth and
angle fields.

v0.11 separates the exact mathematical law from that finite machine
representation:

> Does the signed-local affine law remain injective over the declared arbitrary
> exact-rational transverse interval, and can binary64 `LiftedCarrierPoint`
> fields preserve that exact identity?

## Exact coordinate

For every exact rational transverse value

```text
u in Q intersect [-1,+1]
```

the candidate records:

```text
B(u) = 1 + u/2
t    = exact lifted turns modulo 2
```

The breadth remains exact and positive:

```text
1/2 <= B(u) <= 3/2
```

The inverse is exact:

```text
u = 2 * (B - 1)
```

Therefore distinct exact `u` values have distinct exact breadths. This is an
algebraic result over the declared rational interval, not an inference from a
finite enumeration. The implementation uses `fractions.Fraction` throughout
the exact record and rejects floating-point inputs.

Every `ExactCarrierCoordinate` retains:

- the exact local transverse value;
- the exact breadth;
- exact normalized lifted turns;
- the v0.10 source schema and candidate identity;
- the v0.11 law identity, version, formula, and code reference;
- scope and nonselection status.

## Binary64 is a rendering

`render_exact_coordinate_binary64()` produces the current actual
`LiftedCarrierPoint` type while retaining its exact source record and declaring
the information loss:

```text
exact rational breadth -> binary64 breadth
exact rational lifted turns -> binary64 turns -> binary64 2*pi angle
```

The float point has status `lossy-nonauthoritative-rendering`. It is not the
exact evidence identity.

## Separating witnesses

### Breadth collision

At lifted turn zero:

```text
u0 = 0
B0 = 1

u1 = 1 / 2^53
B1 = 1 + 1 / 2^54
```

The exact coordinates differ, but both breadths round to binary64 `1.0`. Their
complete actual `LiftedCarrierPoint` identities therefore collide.

### Lifted-turn collision

At transverse value zero:

```text
t0 = 1
t1 = 1 + 1 / 2^54
```

The exact lifted turns differ, but both round to binary64 `1.0` before the
binary64 angle multiplication. Their complete actual `LiftedCarrierPoint`
identities also collide.

Either witness is sufficient to falsify arbitrary-rational injectivity for the
binary64 representation. Together they identify both stored-coordinate loss
surfaces.

## Result

| Surface | Result | Standing |
|---|---|---|
| exact signed-local rational coordinate | exact inverse; injective on the declared rational interval | experiment candidate |
| binary64 `LiftedCarrierPoint` | explicit breadth and lifted-turn collisions | lossy rendering |
| carrier selection | none | inactive |
| canonical faithful breadth | not established | unresolved |
| full real-continuous Möbius-to-cover relation | not established | unresolved |
| arbitrary observed-element assignment | not established | unresolved |
| EDCM activation | none | inactive |
| METAPAT activation | none | inactive |

v0.11 does not rewrite the v0.10 result. The earlier 45-fiber materialization
remains valid bounded evidence: none of those 45 values collided. v0.11 shows
why that finite pass cannot generalize to every exact rational after binary64
materialization.

## Reproduction

```bash
python -m pytest tests/test_exact_coordinate.py -q
python -c "from ucns import run_v011_exact_coordinate_boundary_experiment as run; r = run(); print(r.exact_law_status, r.binary64_status, len(r.collision_witnesses), r.rendering_role, r.selection_effect, r.edcm_activation, r.metapat_activation)"
```

Expected experiment line:

```text
exact-rational-bijection-on-declared-transverse-interval not-injective-on-arbitrary-exact-rational-domain 2 lossy-nonauthoritative-rendering none inactive inactive
```

## hmmm

The rational coordinate survives by refusing to become a float. The complete
real-continuous carrier relationship, arbitrary observed-element assignment,
canonical faithful breadth, epicyclic higher geometry, recursive composition,
and scoped completion remain alive rather than being rounded into agreement.
