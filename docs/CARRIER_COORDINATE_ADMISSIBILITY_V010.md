# UCNS v0.10 bounded carrier-coordinate admissibility

**Status:** implemented bounded candidate experiment; one candidate is
admissible on the declared exact-rational materialization domain. No carrier,
faithful-breadth law, coordinate convention, EDCM profile, or METAPAT profile is
selected.

## Question

v0.9 retained an exact transverse value but proved that the value remained a
sidecar: distinct transverse states shared one actual directed-cover
coordinate.

v0.10 asks a narrower constructive question:

> Can a declared transverse-to-radial law place every stress fiber into the
> actual `LiftedCarrierPoint.breadth` and `LiftedCarrierPoint.angle` fields while
> preserving the v0.7 root, coordinate-description invariance, and declared
> root motion?

Only actual stored cover fields count. A new wrapper field or identity tuple
cannot establish coordinate injectivity.

## Declared domain

The experiment retains the v0.9 finite stress domain:

```text
u in Q intersect [-1,+1]
every reduced rational with denominator <= 8
45 fibers
14 minimum-packet initiations
2 transverse coordinate conventions
4 declared root transitions
```

The root coordinate is the v0.7 exact lifted turn `t` in `[0,2)`. Candidate
materialization is:

```text
LiftedCarrierPoint(
    breadth = float(B(u)),
    angle = float(t) * 2*pi,
)
```

Every materialized comparison uses the exact stored binary64 identities
`breadth.hex()` and `angle.hex()` under
`carrier-coordinate-admissibility-exact@0.10.0`. No hidden tolerance is used.

This is finite implementation evidence. It is not a theorem over all rational
values or evidence of real-valued continuity.

## Admissibility criteria

Every candidate must satisfy all four criteria on the declared domain:

1. **actual-cover fiber injectivity** — distinct `u` values at one root have
   distinct stored `LiftedCarrierPoint` coordinates;
2. **zero-fiber root restriction** — `u=0` materializes to the unchanged v0.7
   root point with breadth one;
3. **coordinate-convention invariance** — local-frame and global-side
   descriptions of the same native state materialize identically; and
4. **root-motion commutation** — mapping after initiation, 360-degree,
   720-degree, or inverse root motion matches actual carrier rotation.

Candidate failure remains evidence. The report retains every collision-class
link and every failed motion row.

## Candidate family and result

| Candidate | Exact breadth law | Fiber injective | Zero root | Convention invariant | Motion commutes | Bounded status |
|---|---|---:|---:|---:|---:|---|
| constant root breadth | `B(u)=1` | no | yes | yes | yes | rejected |
| unsigned local radial | `B(u)=1+abs(u)/2` | no | yes | yes | yes | rejected |
| signed local affine radial | `B(u)=1+u/2` | yes | yes | yes | yes | admissible |
| signed global affine radial | `B(u)=1+(frame_sign*u)/2` | yes | yes | yes | no | rejected |

The signed local law stays positive on the declared interval:

```text
1/2 <= B(u) <= 3/2
```

It preserves the root because `B(0)=1`. Its exact declared formula has the
inverse:

```text
u = 2 * (B - 1)
```

The experiment also verifies that all 45 declared values remain distinct after
materialization into the actual binary64 cover fields. That finite
materialization check is the implemented claim.

The unsigned law loses sign. The constant law loses the entire transverse
coordinate. The global signed law is injective at a fixed state, but after one
visible lap the native global side reverses while actual directed-cover
rotation preserves breadth; its odd-motion failures therefore remain explicit.

## Evidence totals

```text
candidate images:              5,040
zero-fiber root restrictions:    112
convention witnesses:          2,520
motion witnesses:             20,160
actual-cover collision links:  1,848
retained motion failures:      2,464
admissible candidate ids:      signed-local-affine-radial
selection effect:              none
```

The collision links represent every non-singleton actual-coordinate class by
connecting its first image to each remaining image. The report re-derives those
classes from the complete image set during validation.

## Authority boundary

`admissible-on-declared-domain` means only that the candidate passed the four
published criteria over this bounded experiment. It does not establish:

- a selected carrier or selected coordinate law;
- canonical faithful breadth `B`;
- injectivity for arbitrary exact rationals after binary64 materialization;
- real-valued continuity;
- arbitrary public-gonol element assignment;
- global Möbius-to-cover equivalence;
- circle, epicycle, disk, or sphere transition laws;
- scoped completion;
- EDCM activation; or
- METAPAT activation.

The v0.7 F12/F13 verdicts remain bounded to the root-loop map. v0.10 does not
rewrite their map identity or promote a global relationship verdict.

## Reproduction

```bash
python -m pytest tests/test_carrier_coordinate.py -q
python -c "from ucns import run_v010_carrier_coordinate_experiment; r = run_v010_carrier_coordinate_experiment(); print(len(r.fibers), len(r.results), sum(len(x.images) for x in r.results), sum(len(x.motion_witnesses) for x in r.results), r.admissible_candidate_ids, r.selection_effect)"
```

Expected experiment line:

```text
45 4 5040 20160 ('signed-local-affine-radial',) none
```

## hmmm

The sidecar now has one bounded route into the actual cover, but the route is
still wearing an experiment badge. Arbitrary assignment, exact-to-real
continuity, faithful-breadth authority, higher geometry, and completion remain
the living boundary.
