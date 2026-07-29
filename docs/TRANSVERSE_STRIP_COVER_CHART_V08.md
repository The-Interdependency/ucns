# UCNS–EDCM v0.8 bounded transverse-strip cover chart

**Status:** implemented exact witness experiment; no carrier or coordinate
convention selected.

**Depends on:** the v0.6 native framed root loop and the v0.7 exact root-loop
cover chart.

## Question

Does the reversible v0.7 C1↔C2 root-loop chart survive the first nonzero
transverse witnesses without erasing frame, side, source causality, or inverse
motion?

v0.8 answers only for the complete minimum initiation packet crossed with:

```text
u ∈ {-1, 0, +1}
```

The implementation accepts other exact rational values inside `[-1, +1]`, but
the finite experiment does not convert those representable values into a claim
of continuous-strip generality.

## Native framed transverse state

The native candidate state is:

```text
(p, ε, u)
```

where:

- `p` is the exact v0.6 phase in `[0, 1)`;
- `ε ∈ {+1, -1}` is the retained local frame;
- `u` is exact local-frame transverse displacement in `[-1, +1]`.

Native motion retains local displacement:

```text
(p, ε, u) --one visible turn--> (p, -ε, u)
```

The associated global side is `εu`, so one visible turn changes its sign. Two
visible turns restore the complete state.

## Cover chart and both coordinate conventions

The v0.7 root coordinate remains:

```text
α = p                  when ε = +1
α = p + 1              when ε = -1
```

v0.8 retains two exact descriptions of the transverse coordinate.

### Local-frame displacement

```text
Φ_local(p, ε, u) = (α, u)
```

The stored transverse coordinate remains fixed when the sheet changes.

### Global-side displacement

```text
Φ_global(p, ε, u) = (α, εu)
```

The stored transverse coordinate changes sign when the sheet changes.

The cover sheet recovers `ε`, so both maps have exact inverses. Their
sheet-aware change of coordinates is:

```text
κ(α, u) = (α, ε(α)u)
```

and `κ` is its own inverse after exchanging the declared source and target
conventions. The experiment therefore preserves both descriptions as
reversible coordinate conventions. It does not rank or select one.

## Exact v0.7 restriction

At `u = 0`, removing the transverse field recovers the unchanged v0.7 objects:

```text
(p, ε, 0) -> (p, ε)
(α, 0)    -> α
```

Every one of the fourteen initiations is checked under both conventions, giving
twenty-eight exact zero-fiber restriction witnesses.

## Executed evidence

The v0.8 run produces:

- 14 source-linked word initiations;
- 3 exact transverse fibers;
- 2 coordinate conventions;
- 84 two-way native/cover round trips;
- 28 exact v0.7 root-loop restrictions;
- 336 map/motion commutation witnesses across initiation, 360°, 720°, and
  inverse motion;
- 42 two-way coordinate-convention round trips;
- 168 coordinate-change/motion commutation witnesses;
- the retained 48-cell F01–F16 relationship matrix;
- all 27 simultaneous `M × B` displays; and
- `selection_effect = "none"`.

Every row retains the v0.6 source links, Structural Null manifestation that
caused initiation, initiation identity, order, multiplicity, parentage,
sidedness, and native completion scope.

## Falsifier result

Within this exact finite domain:

- `F12` remains **supported** for the cover-chart relationship;
- `F13` remains **falsified** for incompatibility on the same domain.

This is stronger evidence than the root loop alone. It is not proof that every
continuous transverse value, radial assignment, arbitrary element, recursive
geometry, or completion state admits the same map. A failed later extension
would narrow the supported domain; it would not retroactively erase these
exact witnesses.

## Boundaries

v0.8 does not:

- treat `u` as canonical faithful breadth `B`;
- assign carrier radius;
- assign arbitrary source elements to a transverse coordinate;
- prove continuous-strip generality;
- define radial, circle, epicycle, disk, sphere, or recursive-scale motion;
- define higher-gonol composition;
- register scoped completion;
- select the direct Möbius carrier, directed cover, or either coordinate
  convention;
- activate EDCM production; or
- activate METAPAT.

## Reproduction

```text
python -m pytest tests/test_transverse_strip_chart.py -q
python -c "from ucns import run_v08_transverse_strip_experiment; r = run_v08_transverse_strip_experiment(); print(len(r.round_trips), len(r.motion_witnesses), r.selection_effect)"
```

Expected compact run result:

```text
84 336 none
```

hmmm: the first transverse witnesses commute, and the two apparent sign laws
resolve into reversible coordinate descriptions on this domain. Continuous
transverse generality, radial placement, faithful breadth, arbitrary-element
assignment, higher geometry, recursive composition, and scoped completion
remain live constraints rather than consequences.
