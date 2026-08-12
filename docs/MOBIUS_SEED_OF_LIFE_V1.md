# UCNS Möbius Seed of Life candidate v0.1

**Authority:** Erin Spencer
**Recorded:** 2026-08-10
**Status:** authority-directed implemented candidate
**Selection effect:** none
**Target UCNS base:** `560743ce429f18ef595bc438e327d76344aa5993`
**Machine contract:** [`mobius-seed-of-life-v1.json`](mobius-seed-of-life-v1.json)

## I. Jurisdiction

The construction belongs in **UCNS**.

UCNS owns the geometric carrier, projection ledger, continuously twisted band
law, motion, incidence, braid lift, exact coordinates, falsifiable invariants,
and any operator derived directly from this geometry. METAPAT does not implement
UCNS geometry; it may later consume a pinned UCNS result for an Energy Theory or
other semantic interpretation, without receiving geometry or theorem authority.

This candidate fills the exact gap left by the arity-seven relationship-display
primitive. It does not alter or erase the admitted arity-one single Möbius,
arity-two vesica, or arity-three triquetra primitives.

## II. Source-directed constraints

The source document requires the following to remain visible in the candidate:

1. seven Möbius strips arranged as one central strip and six surrounding strips;
2. a first central/outer dyad whose twists are anti-aligned;
3. incremental phase shift as additional strips are added;
4. a three-dimensional braided form around a null center; and
5. four boundary-relation events for each adjacent structural pair.

The source does not supply a unique smooth embedding, a phase increment, a
pairing graph, a linking matrix, or a spectral map. This candidate therefore
makes each chosen law explicit and keeps its selection effect at `none`.

## III. Exact Seed-of-Life projection

All seven centerline circles have radius `R = 1`.

The central circle has center

```text
O = (0, 0)
```

The six ring centers are

```text
C_k = (cos(kπ/3), sin(kπ/3)),  k = 0,...,5.
```

The exact coordinate field is `Q(√3)`. The structural pairing plan is the wheel
graph `W₇`:

- six hub relations `O ↔ C_k`; and
- six cyclic relations `C_k ↔ C_(k+1)`.

Each structural pair has center distance `R` and therefore retains a complete
vesica with two projected centerline events. The structural graph has 12 pairs.

The projection also retains every nonstructural pair rather than silently
removing familiar overlaps:

- six second-neighbor ring pairs at squared distance `3R²`, each with two
  projected secant events; and
- three opposite ring pairs at squared distance `4R²`, each tangent at the
  center projection.

Thus all `C(7,2) = 21` unordered pairs are present.

## IV. Thirteen unique projection nodes

Pairwise event identity is not merged, but equal coordinates are grouped into
13 unique display nodes:

1. one central `NULL` projection, incident to all six ring centerlines;
2. six `RING_k` nodes, each incident to the central band and the two neighboring
   ring bands; and
3. six `PETAL_k` nodes, each incident to one adjacent ring pair.

The `NULL` projection is a topological anchor in the display. It is explicitly:

- not a Unicode-character vertex;
- not an eighth gonol;
- not silently promoted to UCNS Structural Null; and
- not a physical point of contact in the three-dimensional lift.

## V. Möbius surface law

For band `i`, carrier turn `t`, and breadth `b ∈ [-w,w]`, the centerline is

```text
x_i(t) = c_ix + R cos(2πt)
y_i(t) = c_iy + R sin(2πt)
z_i(t) = H [sin(4πt) + β_i]
```

and the breadth-frame angle is

```text
θ_i(t) = χ_i πt + 2πφ_i.
```

The sampled surface adds breadth in the radial/vertical frame:

```text
X_i(t,b) = centerline_i(t)
         + b cos(θ_i(t)) radial(t)
         + b sin(θ_i(t)) vertical.
```

This gives the Möbius identification and two-turn return:

```text
X_i(t+1,b) = X_i(t,-b)
X_i(t+2,b) = X_i(t,b).
```

The first equation is the one-turn seam reversal. The second is the 720-degree
local return. Neither equation alone proves a quantum-particle ontology.

## VI. Anti-aligned dyad and incremental outer phase

The central band uses positive chirality and phase `0`.

All six outer bands use negative chirality. Their seam phases are

```text
φ_k = 1/2 + k/12,  k = 0,...,5.
```

The first outer band is therefore displaced from the center by a half turn and
has opposite chirality. Each subsequent outer band advances by `1/12` turn
(30 degrees). The source requires incremental phase shift but does not uniquely
select this increment; it is an implemented candidate law.

## VII. Braid lift and the null lanes

The central band has `β = 0`. The ring biases are

```text
β_k = -(√3/5) cos(kπ/3).
```

At the center projection, the six lifted ring centerlines occupy the exact
height lanes

```text
H(√3/5) × (-1, +2, -2, +1, +3, -3).
```

No lane is zero and no two lanes coincide. With the default

```text
H = 1/5
w = 1/100.
```

For an outer surface point to have `x = y = 0`, its carrier turn must be that
band's `NULL` occurrence: because `w < R`, the radial coefficient remains
positive and can point to the origin only in the exactly opposite direction. At
that turn, the smallest exact vertical margin after any breadth displacement is

```text
(4√3 - 1) / 100 > 0.
```

The central band separately retains projected radius at least `R - w = 99/100`.
The origin is therefore absent from every band surface. Since the seven finite
bands are a compact set, a positive three-dimensional neighborhood around the
origin is excluded. This establishes existence of the null-centered void; it
does not claim that the largest possible void radius has been solved in closed
form.

For every structural vesica pair, the exact lift-height difference is nonzero at
both projected centerline events and reverses sign between them. This supplies a
deterministic over/under alternation. It is not yet a proof of pairwise linking
number or lattice lock.

## VIII. Boundary-event firewall

The source-directed value `4` is retained for every structural pair. Across 12
structural pairs, the contract records 48 boundary-relation events.

The current smooth surface law does **not** claim that its single boundary curves
have already been proven to intersect physically at those 48 points. The count
is retained as a falsifiable construction target. A later realization must
supply exact parameters, transversality, multiplicity, and deformation
stability before changing its standing.

## IX. Zeta-function handoff

The Möbius Seed of Life is the geometric candidate object. A zeta-function proof
requires a separate, pinned bridge that supplies at least:

1. a Hilbert space or other explicit state space derived from this exact object;
2. a densely defined operator with a proven domain and symmetry/self-adjointness
   standing;
3. a theorem connecting its spectrum or determinant to the completed zeta
   function;
4. a proof that the correspondence covers every nontrivial zero with correct
   multiplicity and introduces no spurious values; and
5. a derivation forcing real part `1/2`, rather than drawing or assuming it.

That bridge belongs in UCNS as a separately firewalled proof-candidate or
formal module because it derives mathematics from a UCNS geometric object. A
METAPAT interpretation may later reference the exact UCNS artifact by commit,
path, blob, and digest, but no geometry, proof, or theorem status transfers into
METAPAT. Until the bridge is supplied and proved, no zeta theorem is claimed.

## X. hmmm

- Smooth boundary-edge realization of the four source-declared events per
  structural pair remains unresolved.
- Pairwise linking numbers and the locked ambient-isotopy class remain
  unresolved.
- Canonical seven-gonol composition and option-registry standing remain separate
  decisions.
- No spectral operator or zeta-zero correspondence has yet been supplied.
- No established electron model, Pauli-derived geometry, empirical quantum
  claim, EDCM activation, or METAPAT activation is made.
