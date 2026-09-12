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
- candidate exact finite modular-action orbit and circle geometry;
- candidate exact visible-circle continuum wave / gonal boundary traces;
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

## Modular orbit geometry candidate

`src/ucns/modular_orbit.py` implements a candidate finite modular multiplication representation

```text
T_{a,m}(x) = a*x mod m
```

over a caller-declared canonical residue carrier. The carrier must be nonempty, closed under the action, and bijective under that action, so the result is an exact disjoint cycle decomposition rather than a transient functional graph.

The executable arithmetic is exact within the declared model. The representation remains candidate-scoped until its own falsifier/replay/ratification path selects stronger UCNS standing. Executability alone is not ratification.

The candidate records only geometry: canonical residues, exact action edges, cycle periods, and exact normalized circle positions `r/m` turns. Display aliases and downstream meanings stay with renderers and consumers.

For the mod-9 digit carrier used in common circular diagrams:

```python
from ucns import build_modular_orbit_geometry

g = build_modular_orbit_geometry(9, 2, range(1, 9))
assert g.orbits == ((1, 2, 4, 8, 7, 5), (3, 6))
assert g.periods == (6, 2)
```

The core uses residues `0..m-1`; a renderer may choose to display residue `0` as `9` in a mod-9 digit diagram without changing the UCNS record.

## Continuum wave → gonal boundary trace candidate

`src/ucns/gonal_boundary_trace.py` supplies the candidate exact visible-boundary bridge.

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

So the candidate witnesses an exact finite boundary relation between modular multiplication and a continuum wave-equation covering. The equation does **not** select a privileged continuum lift, modulus, carrier, or physical meaning, and the representation itself is not yet ratified as selected UCNS geometry.

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
python -m pip install uv==0.11.18
uv lock --check
uv sync --locked --python python --extra test --extra build
.venv/bin/python -m pytest -q
python tools/verify_skill_lib_contracts.py .
.venv/bin/python -m build
.venv/bin/python -m twine check dist/*
.venv/bin/python tools/verify_distributions.py . dist
```

The independent interval checks also require system MPFR (for example,
`libmpfr6` on Ubuntu). Verification dependencies are locked; the isolated build
backend is pinned in `[build-system].requires`. Use a clean `dist` directory.

The wheel supplies the geometry package. Repository-context research replay and
the full tests require the source archive or checkout: run from its root, where
the archived preregistrations, generated evidence, and vendored parser live.
The distribution gate checks these inputs byte-for-byte; it does not recertify
their mathematical claims. It also binds wheel filename tags, dependencies, and flags to
`pyproject.toml`, verifies every RECORD digest, and requires the exact generated
sdist configuration. Both source PKG-INFO records and generated egg-info
dependency and file lists must agree with that same source configuration. Directory
entries are validated too; duplicate names and file/directory collisions fail.

Exact modular and trace records require immutable tuples with non-Boolean integer
residues; prefer the public builders. MPFR rational constructors accept only
integers or `Fraction`, and NaN cannot participate in interval ordering.

The no-exec graph also reconciles the exact vendored reference parser that it
executes, including a local numeric-field witness. Parser ownership remains in
skill-lib. Unused skill helper tools remain canonical dependency material.

For a source-bound, selected-check receipt:

```bash
.venv/bin/python tools/run_skill_lib_boundaries.py . \
  --check check_boundary_runner_nonactivation --receipt /tmp/ucns-receipt.json
```

Receipt schema 2.1 rejects skips, expected failures, both forms of XPASS, absent
reports, and source changes during execution (including write-and-restore
through external hardlinks).
Receipt execution requires Linux inotify; an unavailable observer is an error.
Receipt output must be outside the bound source tree and is written by atomic
replacement so an output hardlink cannot modify a bound input.
Checks import the bound checkout with ambient pytest plugins disabled and
PYTHONPATH replaced. An inherited startup hook makes ordinary Python descendants
prefer bound packages over their working directory. A separate supervisor uses Linux
child subreaping to terminate remaining descendants before observation ends;
leaked background work prevents acceptance. Timeout cleanup is outside the
pytest process, so replacing its signal handler cannot bypass descendant cleanup. Origin receipts observe the selected
pytest process. Explicit isolated/no-site interpreters and replaced child
environments do not inherit the import protocol. The observer instruments trusted
checks; it is not a sandbox for hostile test code. A `passed` receipt covers only its selected
checks; it does not select geometry, ratify candidates, or establish freshness.

`hmmm`: ratification of the modular-orbit / continuum-boundary-trace candidates, the complete higher-dimensional UCNS construction, the exact visible-circle wave-trace lift into the native Möbius carrier, any law selecting one continuum covering lift from a finite modular congruence class, and the exact geometric operation of every Public Gonol function position remain unresolved. Unresolved geometry stays unresolved; semantic machinery is not used to fill it.
