# UCNS

<p align="center">
  <img src="docs/ucns-geometry-repository.svg" alt="UCNS — Geometry Repository" width="100%">
</p>

UCNS is a geometry repository.

Its active scope is limited to constructions that directly represent or test geometry:

- the exact 157-position Public Gonol carrier;
- the directed lifted carrier and its 360° visible / 720° complete return;
- exact framed Möbius motion;
- Möbius vesica and Seed-of-Life constructions and certificates;
- exact finite modular-action orbit and circle geometry;
- exact visible-circle continuum wave / gonal boundary traces;
- prime-indexed ribbon, link, interval, Milnor, Alexander, and related topological geometry;
- numerical machinery used to certify those constructions.

Everything semantic is outside this repository's active domain: lexical corpora, definitions, morphology, NLP parsing, function-name semantics, EDCM measurement profiles, PTCNA state, evaluator laboratories, and cross-stack adapters.

The poster above is a display certificate of those constructions. It is not an interpretation layer.

## Public Gonol

The Public Gonol is the exact ordered 157-position carrier in `src/ucns/public_gonol.py`. Every glyph is a Public Gonol function position. UCNS does not divide glyphs into letters, punctuation, digits, or symbols for construction.

A function's geometric operation is not inferred from Unicode names or dictionary definitions. Where an operation is not geometrically established, it remains `hmmm`.

## Möbius root loop

`src/ucns/direct_mobius.py` implements the exact framed quotient

```text
(t, ε) ~ (t + n, (-1)^n ε)
```

One visible turn preserves phase and reverses the local frame. Two visible turns restore the complete state.

## Modular orbit geometry

`src/ucns/modular_orbit.py` represents a finite modular multiplication action

```text
T_{a,m}(x) = a*x mod m
```

over a caller-declared canonical residue carrier. The carrier must be nonempty, closed under the action, and bijective under that action, so the result is an exact disjoint cycle decomposition rather than a transient functional graph.

UCNS records only the geometry: canonical residues, exact action edges, cycle periods, and exact normalized circle positions `r/m` turns. Display aliases and downstream meanings stay with renderers and consumers.

For the mod-9 digit carrier used in common circular diagrams:

```python
from ucns import build_modular_orbit_geometry

g = build_modular_orbit_geometry(9, 2, range(1, 9))
assert g.orbits == ((1, 2, 4, 8, 7, 5), (3, 6))
assert g.periods == (6, 2)
```

The core uses residues `0..m-1`; a renderer may choose to display residue `0` as `9` in a mod-9 digit diagram without changing the UCNS record.

## Continuum wave → gonal boundary trace

`src/ucns/gonal_boundary_trace.py` supplies the exact visible-boundary bridge.

On a circle of radius `R`, the continuum scalar wave equation is

```text
u_tt = (c^2/R^2) u_θθ.
```

Periodic spatial modes have integer harmonic number `n`. On an `m`-gonal visible boundary, residue `r` sits at exactly `r/m` turns and harmonic `n` has exact phase

```text
(n*r mod m)/m.
```

For positive integer continuum covering degree `d`, the matched spacetime covering

```text
(θ, t) -> (dθ, dt)
```

preserves the wave equation. Its finite gonal trace is

```text
r -> d*r mod m.
```

If `a = d mod m`, this is exactly the finite modular action `r -> a*r mod m`.

The finite trace forgets the continuum degree: `d`, `d+m`, `d+2m`, ... all produce the same residue action while multiplying the continuum harmonic and time scale differently. Therefore the continuum covering degree is an explicit input; UCNS does not infer it from the modular multiplier.

```python
from ucns import (
    build_circle_wave_mode_trace,
    build_modular_orbit_geometry,
    pullback_circle_wave_trace,
)

geometry = build_modular_orbit_geometry(9, 2, range(1, 9))
source = build_circle_wave_mode_trace(9, 1, range(1, 9))

covering_2 = pullback_circle_wave_trace(source, geometry, 2)
covering_11 = pullback_circle_wave_trace(source, geometry, 11)

assert covering_2.action == covering_11.action == geometry.action
assert covering_2.target.harmonic == 2
assert covering_11.target.harmonic == 11
assert covering_2.time_scale == 2
assert covering_11.time_scale == 11
```

So modular multiplication is not merely drawn on a circle: it is the exact finite boundary trace of a continuum wave-equation covering. The equation does **not** select a privileged continuum lift, modulus, carrier, or physical meaning.

The full derivation and nonclaims are in `docs/modular-orbit-wave-trace.md`.

This trace is exact on the visible 360° boundary. It is **not yet** the complete native Möbius state; the frame-bearing lift required for 720° local return remains `hmmm`.

## Geometry modules

The active package also retains the Möbius vesica/seed family and the `prime_*` topological geometry family. Generated geometry certificates remain evidence; semantic receipts do not.

## Usage

```python
from fractions import Fraction
from ucns import public_gonol_function, native_mobius_state

w = public_gonol_function("w")
s0 = native_mobius_state(Fraction(0))
s360 = s0.advance(1)
s720 = s0.advance(2)

assert s360.visible_key == s0.visible_key
assert s360.complete_key != s0.complete_key
assert s720 == s0
```

## Build

```bash
python -m pip install -e ".[test,build]"
python -m pytest -q
python tools/verify_skill_lib_contracts.py .
python -m build
python -m twine check dist/*
```

`hmmm`: the complete higher-dimensional UCNS construction, the exact visible-circle wave-trace lift into the native Möbius carrier, any law selecting one continuum covering lift from a finite modular congruence class, and the exact geometric operation of every Public Gonol function position remain unresolved. Unresolved geometry stays unresolved; semantic machinery is not used to fill it.
