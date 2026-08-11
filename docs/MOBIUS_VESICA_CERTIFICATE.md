# Construct the certified Möbius-vesica embedding and continuation engine

**Status:** UCNS exact research candidate  
**Selection effect:** none  
**Source basis:** `Möbius Strips and Quantum Geometry.txt`  
**Source SHA-256:** `dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1`

## 1. Research question retained from the source

The source specifies a two-strip Möbius Vesica Piscis with:

- one turn reversing the retained side/orientation and two turns restoring it;
- exactly two centerline contacts;
- exactly four contacts between the strips' single continuous boundary curves;
- opposite twist alignment for the first dyad.

This artifact treats those statements as geometric claims to prove or falsify. It does not substitute projected crossings or abstract relation events for physical equality in three-dimensional space.

## 2. Certified standard-circular embedding

Let the two carrier centerlines be equal unit circles in the plane:

\[
C_L(t)=\left(-\frac12+\cos 2\pi t,\;\sin 2\pi t,\;0\right),
\]

\[
C_R(s)=\left(+\frac12+\cos 2\pi s,\;\sin 2\pi s,\;0\right).
\]

Their centers are one radius apart, the classical Vesica Piscis relation. For signed breadth \(u\in[-w,w]\), set

\[
X_i(t,u)=C_i(t)+u\left(\cos\alpha_i(t)\,\mathbf r_i(t)+
\sin\alpha_i(t)\,\mathbf z\right),
\]

where \(\mathbf r_i\) is the outward radial direction and

\[
\alpha_L(t)=\pi t,
\qquad
\alpha_R(s)=-\pi s+\frac{\pi}{2}.
\]

Thus the left and right strips have opposite chirality. The right strip has a quarter-turn phase offset. The default half-width is

\[
w=\frac1{100}.
\]

Because each frame angle changes by an odd multiple of \(\pi\) after one carrier turn,

\[
X_i(t+1,u)=X_i(t,-u),
\qquad
X_i(t+2,u)=X_i(t,u).
\]

The implementation tests sampled binary64 realizations of these analytic identities to below \(10^{-12}\); the identities themselves follow algebraically from the parameterization.

## 3. Exact two-centerline result

Two equal unit circles whose centers are one unit apart have exactly two intersections:

\[
P_+=\left(0,\frac{\sqrt3}{2},0\right),
\qquad
P_-=\left(0,-\frac{\sqrt3}{2},0\right).
\]

The corresponding turns are:

| Event | Left turn | Right turn |
|---|---:|---:|
| upper | \(1/6\) | \(1/3\) |
| lower | \(5/6\) | \(2/3\) |

Therefore the source's two-centerline count is realized exactly in this family.

## 4. Exact four-boundary-contact result

Each Möbius strip has one continuous boundary, parameterized over two carrier turns by \(B_i(t)=X_i(t,w)\). For the selected chirality and phase pair,

\[
B_L(t)=\left(
-\frac12+(1+w\cos\pi t)\cos2\pi t,
(1+w\cos\pi t)\sin2\pi t,
w\sin\pi t
\right),
\]

\[
B_R(s)=\left(
+\frac12+(1+w\sin\pi s)\cos2\pi s,
(1+w\sin\pi s)\sin2\pi s,
w\cos\pi s
\right).
\]

Equality of their heights gives two branches.

### 4.1 Viable branch

The branch

\[
t+s=\frac12\pmod 2
\]

makes the radial factors equal. Writing

\[
x=\cos\pi t,
\]

planar equality reduces to

\[
(1+wx)(2x^2-1)=\frac12,
\]

or

\[
P_w(x)=4wx^3+4x^2-2wx-3=0.
\]

For \(w=1/100\), the integer-scaled polynomial is

\[
2x^3+200x^2-x-150=0.
\]

An exact rational Sturm chain proves that this cubic has exactly two distinct roots in \((-1,1)\):

\[
x_1\approx-0.867287257684167,
\qquad
x_2\approx 0.864787007648224.
\]

Each root of \(x=\cos\pi t\) has two distinct preimages in the boundary domain \(t\in[0,2)\). Hence the two roots induce exactly four physical boundary contacts.

Approximate witnesses are:

| Contact | Left turn | Right turn | Approximate point \((x,y,z)\) |
|---|---:|---:|---|
| upper 1 | 0.1674533711 | 0.3325466289 | \((0,\;0.8759968755,\;0.0050213886)\) |
| upper 2 | 1.1658615812 | 1.3341384188 | \((0,\;0.8559961878,\;-0.0049780801)\) |
| lower 1 | 0.8341384188 | 1.6658615812 | \((0,\;-0.8559961878,\;0.0049780801)\) |
| lower 2 | 1.8325466289 | 0.6674533711 | \((0,\;-0.8759968755,\;-0.0050213886)\) |

This realizes the source's description of two boundary contacts near the upper node and two near the lower node.

### 4.2 Obstructed branch

The alternate height branch is

\[
t-s=\frac12\pmod 2.
\]

Under that substitution, planar equality would require

\[
2e^{2\pi i t}=1,
\]

which is impossible because the left side has modulus two and the right side has modulus one. The alternate branch therefore contributes no additional contacts.

Together, the Sturm count and branch obstruction prove exactly four physical contacts between the two continuous boundary curves in this parameter family.

## 5. Null-center clearance

The origin is not a vertex and is not promoted to UCNS Structural Null. The minimum distance from the origin to either unit centerline is \(1/2\). Every surface point lies at most \(w\) from its centerline, so

\[
\operatorname{dist}(0,X_i)\ge\frac12-w=\frac{49}{100}>0.
\]

This is an exact geometric clearance certificate. It does not establish a quantum probability node.

## 6. Continuation engine

The continuation engine independently reruns the Sturm certificate for exact rational widths

\[
\frac1{200},\frac1{100},\frac1{80},\frac1{50},
\frac1{20},\frac1{10},\frac15,\frac14.
\]

Every listed quarter-turn stage retains two cubic roots and four physical boundary contacts. The result is not inherited from a mesh or neighboring sample; every stage is recertified with rational arithmetic.

The engine also emits twelve rigid local placements corresponding to the Seed-of-Life structural relation graph:

- six center-to-ring vesicas;
- six adjacent-ring vesicas.

Rigid motion preserves the local two-plus-four certificate. The artifact does **not** claim that all twelve copies can yet be realized simultaneously by seven global bands with one compatible phase and lift assignment.

## 7. Phase-law finding against the current seven-band candidate

The current PR-174 candidate records:

- positive/negative first-dyad chirality;
- half-width \(1/100\);
- a right-band phase of \(1/2\) turn.

The exact physical-contact witness here uses a right-band phase of \(1/4\) turn. In the same standard-circular family, the half-turn phase has an exact zero-contact obstruction for \(0<w<1/2\):

1. One height branch would require \(|2w\cos\pi t|=1\), impossible because \(2w<1\).
2. The other branch forces \(\sin2\pi t=0\), after which the two x coordinates still differ by one.

Therefore the PR-174 half-turn dyad does not inherit this four-contact certificate. This is a parameter-family result, not a proof that every possible half-turn Möbius embedding lacks four contacts.

The next load-bearing problem is a global phase-and-lift compatibility theorem: determine whether seven bands can satisfy all twelve structural dyads while preserving the locally certified physical contacts, or whether the source's local contact rule must be weakened in the full Seed.

## 8. Explicit boundaries

This artifact proves a specific existence result for two standard circular Möbius ribbons. It does not yet prove:

- the complete intersection locus of the two two-dimensional surfaces;
- stability of the four curve contacts under arbitrary three-dimensional perturbations;
- a disjoint-link, linking-number, Hopf-link, or ambient-isotopy class;
- simultaneous realization of all twelve Seed-of-Life dyads;
- an electron ontology or derivation from the Pauli exclusion principle;
- a spectral operator, prime-orbit law, zeta-zero correspondence, or Riemann-hypothesis proof;
- EDCM or METAPAT validity.

Physical contacts between curves in three dimensions are symmetry-supported and nongeneric. They must not be silently re-described as a stable link of disjoint curves.

## 9. Reproduction

From the repository root:

```bash
PYTHONPATH=src python -m pytest -q tests/test_mobius_vesica_exact.py
```

Regenerate the machine receipt:

```bash
PYTHONPATH=src python -c \
  'from ucns.mobius_continuation import write_default_artifact; write_default_artifact("generated/mobius-vesica-certificate.json")'
```
