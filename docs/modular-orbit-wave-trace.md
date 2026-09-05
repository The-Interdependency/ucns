# Continuum wave equation → gonal boundary trace → modular action

Standing: exact geometric derivation on the **visible circle boundary**. This is not a physical-selection claim and does not yet lift the trace into the complete native Möbius state.

## 1. Continuum circle wave equation

Let a circle of radius `R` carry angular coordinate `θ ∈ R / 2πZ`. For scalar propagation speed `c`, the one-dimensional continuum wave equation on the circle is

```text
∂²u/∂t² = (c²/R²) ∂²u/∂θ².
```

Set `κ = c/R`. Separation `u(θ,t)=Θ(θ)T(t)` gives

```text
Θ'' + n² Θ = 0,
T'' + (κ n)² T = 0,
```

with integer `n` forced by periodicity `Θ(θ+2π)=Θ(θ)`. A complex traveling basis mode is

```text
u_n(θ,t) = A exp(i(nθ - |n|κt)).
```

Real sine/cosine modes are the real and imaginary combinations of the same basis. UCNS needs only the exact spatial phase relation below; it does not store floating-point complex amplitudes.

## 2. Positive-degree continuum covering

For any positive integer `a`, define the matched spacetime covering

```text
D_a(θ,t) = (aθ, at).
```

If `u` solves the circle wave equation, then `v(θ,t)=u(aθ,at)` also solves it because

```text
v_tt     = a² u_tt,
v_θθ     = a² u_θθ,
therefore v_tt = κ² v_θθ.
```

For a basis mode,

```text
u_n(D_a(θ,t)) = u_n(aθ,at) = u_(an)(θ,t)
```

for positive `a`. Thus the continuum equation admits a degree-`a` solution endomorphism that multiplies spatial harmonic number by `a` while scaling time by the same factor.

Important boundary: for `a>1`, `θ ↦ aθ` is a degree-`a` covering of the circle, not a globally invertible circle isometry. The continuum equation therefore does **not** make `a` a symmetry-group generator or select one preferred `a`.

## 3. Exact UCNS/gonal boundary trace

For an `m`-gonal visible boundary, place canonical residue `r ∈ Z/mZ` at the exact normalized turn

```text
τ_m(r) = r/m.
```

Equivalently,

```text
θ_r = 2πr/m.
```

Define the boundary trace of harmonic `n` by sampling the continuum phase at those positions:

```text
Γ_(m,n)(r) = n r / m   (mod 1).
```

The executable UCNS record stores the canonical exact phase turn

```text
phase_(m,n)(r) = (n*r mod m)/m
```

as a rational `Fraction`. No trigonometric approximation is needed.

This is the explicit mapping:

```text
continuum boundary point θ_r = 2πr/m
        ↓ sample
UCNS gonal position r at exact turn r/m
        ↓ harmonic n
exact phase turn (n*r mod m)/m.
```

The map is to the generic `m`-gonal boundary carrier. It does not automatically identify an arbitrary `m` with the 157-position Public Gonol arrangement; that identification requires its own geometric authority.

## 4. Modular multiplication appears as the finite boundary trace

Apply the continuum covering `D_a` to a gonal sample position:

```text
θ_r ↦ a θ_r = 2π (a r)/m.
```

Modulo one visible turn, this lands at canonical residue

```text
r ↦ a r (mod m).
```

Therefore the finite boundary action is exactly

```text
T_(a,m)(r) = a*r mod m.
```

For the phase trace,

```text
Γ_(m,n)(a r)
  = n a r / m           (mod 1)
  = Γ_(m,an)(r).
```

So the following square commutes exactly at the spatial boundary-trace level:

```text
continuum harmonic n  --D_a-->  continuum harmonic an
       | Γ_m                         | Γ_m
       v                             v
gonal trace n         --T_a*-->  gonal trace an
```

where `T_a*` means pullback along `r ↦ a r mod m`.

The executable witness is:

```python
from ucns import (
    build_circle_wave_mode_trace,
    build_modular_orbit_geometry,
    pullback_circle_wave_trace,
)

geometry = build_modular_orbit_geometry(9, 2, range(1, 9))
source = build_circle_wave_mode_trace(9, 1, range(1, 9))
covering = pullback_circle_wave_trace(source, geometry)

assert covering.target.harmonic == 2
assert covering.time_scale == 2
```

The existing modular-orbit primitive requires the declared finite carrier to be closed and bijective under `T_(a,m)` before calling its components disjoint cycles. That is a **finite trace boundary**, not a claim that the degree-`a` continuum covering is globally invertible.

## 5. What this derives, and what it does not

Derived exactly:

- the continuum circle wave equation and its integer harmonic basis;
- the positive-degree spacetime covering `(θ,t) ↦ (aθ,at)` preserving the equation;
- exact `m`-gonal sampling at `r/m` visible turns;
- exact phase trace `(n*r mod m)/m`;
- the induced finite action `r ↦ a*r mod m`;
- exact equivariance between modular reindexing and harmonic multiplication;
- the condition under which the finite action is a disjoint-cycle permutation.

Not derived:

- why a physical system should select one modulus `m`, one carrier subset, or one covering degree `a`;
- that modular cycles themselves are energy states, particles, primes, Fibonacci structure, or EPAC semantics;
- that the visible 360° trace already contains the complete 720° native Möbius state;
- that the generic `m`-gonal carrier is identical to the Public Gonol without a separate geometric identification.

Those nonclaims matter. The continuum derivation establishes the **representation bridge** that was missing; it does not smuggle downstream meaning into UCNS.

## hmmm

The next load-bearing step is the exact lift of this visible-circle trace into the native Möbius carrier: what state must accompany `r/m` so that one visible turn reverses local frame and two visible turns restore complete local state? Until that lift is constructed, the continuum/gonal trace is exact but only visible-boundary complete.
