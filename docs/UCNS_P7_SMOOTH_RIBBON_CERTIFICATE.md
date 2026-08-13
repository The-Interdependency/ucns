# P7 smooth finite-width Möbius-ribbon certificate

**Status:** nonselecting computer-assisted UCNS research certificate  
**Research order:** P7 first, P5 second  
**Selection effect:** none  
**Source basis:** `Möbius Strips and Quantum Geometry.txt`  
**Source SHA-256:** `dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1`

## 1. Purpose and standing

The preceding P7-native phase-and-lift artifact solved phase and event-height state on the complete seven-carrier, thirteen-hypernode primitive before deriving pairwise readouts. Its lift interpolation was periodic and piecewise linear. It separated centerlines at every projected event but did not certify the complete finite-width ribbons away from those events.

This artifact:

1. replaces every piecewise-linear lift by an event-preserving periodic \(C^\infty\) field;
2. covers every pair-parameter torus \([0,1]^2\) with a deterministic Lipschitz subdivision certificate;
3. derives a global finite-width ribbon-separation bound;
4. regularizes tangent projected pairs and issues complete pairwise linking matrices.

The source supplies the one-turn opposite-side and two-turn return boundary, together with the seven-carrier braided target. It does not supply the smoothing law, subdivision certificate, tangent isotopy, or linking matrix. Those are new UCNS research constructions.

## 2. Event-preserving smooth lift

For adjacent event knots \((t_i,h_i)\) and \((t_{i+1},h_{i+1})\), put

\[
s=\frac{t-t_i}{t_{i+1}-t_i}
\]

and use the flat step

\[
S(s)=\frac{e^{-1/s}}{e^{-1/s}+e^{-1/(1-s)}}
\]

for \(0<s<1\), extended by \(S=0\) to the left and \(S=1\) to the right. Define

\[
z_i(t)=h_i+(h_{i+1}-h_i)S(s).
\]

All derivatives of \(S\) vanish at zero and one. The periodic segments therefore join in class \(C^\infty\), reproduce every event height exactly, and introduce no overshoot.

Writing \(q=2s-1\),

\[
S'(s)=
\frac{2(1+q^2)}{(1-q^2)^2}
\frac{1}{\cosh^2\!\left(\frac{2q}{1-q^2}\right)}.
\]

Since \(\cosh^2 x\ge1+x^2\),

\[
0\le S'(s)\le2.
\]

Each lift interval has the exact derivative majorant

\[
\left|\frac{dz}{dt}\right|
\le2\frac{|h_{i+1}-h_i|}{t_{i+1}-t_i}.
\]

For a unit-circle carrier centerline, a valid speed majorant is

\[
L=\sqrt{(2\pi)^2+M_z^2}.
\]

## 3. Möbius return

The surface law remains

\[
X_i(t,u)=C_i(t)+z_i(t)e_z+u[\cos(2\pi(t/2+\Phi_i(t)))r_i(t)+\sin(2\pi(t/2+\Phi_i(t)))e_z].
\]

The smooth lift is periodic and the selected phase fields have integer winding. Hence

\[
X_i(t+1,u)=X_i(t,-u),
\qquad
X_i(t+2,u)=X_i(t,u).
\]

| Candidate | One-turn residual | Two-turn residual |
|---|---:|---:|
| P7 | \(8.01\times10^{-16}\) | \(2.40\times10^{-15}\) |
| P5 | \(7.56\times10^{-16}\) | \(2.35\times10^{-15}\) |

Every stored event-height residual is zero.

## 4. Continuous-domain separation certificate

For each unordered carrier pair, cover

\[
(t,s)\in[0,1]^2.
\]

For a box \(B=[a,b]\times[c,d]\), sample its center \((t_0,s_0)\). If

\[
d_0=\|\gamma_i(t_0)-\gamma_j(s_0)\|,
\]

then every point in the box satisfies

\[
\|\gamma_i(t)-\gamma_j(s)\|
\ge d_0-L_i\frac{b-a}{2}-L_j\frac{d-c}{2}.
\]

The implementation subtracts a binary64 guard of \(10^{-12}\). A box is accepted only when the guarded lower bound exceeds

\[
\boxed{9/100}.
\]

Otherwise, the dimension with the larger Lipschitz contribution is bisected. Termination means accepted boxes cover the complete parameter torus for every pair.

| Quantity | P7 | P5 |
|---|---:|---:|
| Carrier pairs | 21 | 10 |
| Boxes evaluated | 6,173 | 4,340 |
| Maximum depth | 20 | 20 |
| Smallest accepted leaf lower bound | 0.09000514999975501 | 0.09000862353779256 |
| Centerline target | \(9/100\) | \(9/100\) |

This is a deterministic computer-assisted Lipschitz certificate with a declared binary64 buffer. It is stronger than mesh inspection because it covers the continuous parameter domains, but it is not formal interval arithmetic or a proof-assistant replay.

## 5. Global finite-width disjointness

Every ribbon point lies within

\[
w=1/100
\]

of its centerline. Thus

\[
d(\mathcal R_i,\mathcal R_j)
\ge d(\gamma_i,\gamma_j)-2w
>\frac9{100}-\frac2{100}
=\boxed{7/100}.
\]

The complete declared finite-width ribbon components are therefore pairwise disjoint under the numerical certificate—not merely their centerlines and not merely at projected events. No physical centerline or boundary contacts are claimed in this strict braid realization.

## 6. Tangent regularization

The tangent projected pairs are:

- P7: \((R_0,R_3),(R_1,R_4),(R_2,R_5)\);
- P5: \((R_0,R_2),(R_1,R_3)\).

For one tangent pair, translate one whole ribbon outward along its center axis by

\[
\varepsilon=1/100.
\]

Projected center separation becomes

\[
2+\varepsilon=201/100>2,
\]

so the projected unit circles are disjoint and have no crossings. During this pair-specific isotopy, complete ribbon clearance remains greater than

\[
7/100-1/100=3/50.
\]

The pair stays disjoint, linking number is invariant, and each tangent pair receives

\[
\boxed{\operatorname{lk}=0}.
\]

## 7. Complete P7 linking matrix

In order \((C,R_0,R_1,R_2,R_3,R_4,R_5)\),

\[
L_7=
\begin{pmatrix}
0&1&1&1&1&1&1\\
1&0&0&0&0&0&0\\
1&0&0&1&1&0&0\\
1&0&1&0&1&1&0\\
1&0&1&1&0&1&1\\
1&0&0&1&1&0&0\\
1&0&0&0&1&0&0
\end{pmatrix}.
\]

| Invariant | P7 |
|---|---:|
| Linking \(+1\) pairs | 12 |
| Linking \(0\) pairs | 9 |
| Rank over \(\mathbb Q\) | 6 |
| Nullity | 1 |
| Determinant | 0 |
| Nonzero-link components | 1 |
| Nonzero-link cycle rank | 6 |

## 8. P5 comparison matrix

In order \((C,R_0,R_1,R_2,R_3)\),

\[
L_5=
\begin{pmatrix}
0&0&0&0&0\\
0&0&0&0&0\\
0&0&0&1&0\\
0&0&1&0&1\\
0&0&0&1&0
\end{pmatrix}.
\]

| Invariant | P5 |
|---|---:|
| Linking \(+1\) pairs | 2 |
| Linking \(0\) pairs | 8 |
| Rank over \(\mathbb Q\) | 2 |
| Nullity | 3 |
| Determinant | 0 |
| Nonzero-link components | 3 |
| Nonzero-link cycle rank | 0 |

Reorienting a component conjugates a linking matrix by a diagonal sign matrix. Rank, nullity, determinant, and the zero pattern remain invariant.

The pairwise matrix does not classify the complete multi-component link or detect every higher-order linking invariant.

## 9. Result and boundary

Within the declared witness family:

- every event lane survives a periodic \(C^\infty\) smoothing;
- one-turn reversal and two-turn return survive;
- every P7 and P5 centerline pair is globally separated by more than \(9/100\) under the declared numerical certificate;
- every finite-width ribbon pair is separated by more than \(7/100\);
- every tangent projected pair is regularized without consuming the margin;
- every pair receives an integer linking number;
- complete pairwise linking matrices are issued.

This does not yet establish formal interval replay, the full ambient-isotopy class, higher-order link invariants, boundary-component link invariants, a spectral operator, a prime-power law, a zeta-zero correspondence, a proof of the Riemann hypothesis, an arithmetic redefinition of primality, or an electron ontology.

## 10. Next action

1. Replay the subdivision proof with outward-rounded interval arithmetic.
2. Extract the seven continuous ribbon-boundary curves.
3. Calculate boundary linking and higher-order invariants.
4. Distinguish the whole P7 link from links sharing its pairwise matrix.
5. Only then define a spectral or trace object.

## 11. Reproduction

```bash
PYTHONPATH=src python -m pytest -q \
  tests/test_prime_primitives.py \
  tests/test_prime_phase_lift.py \
  tests/test_prime_smooth_ribbons.py
```

```bash
PYTHONPATH=src python -c \
  'from ucns.prime_smooth_ribbons import write_smooth_ribbon_family_certificate; write_smooth_ribbon_family_certificate("generated/prime-smooth-ribbon-family-certificate.json")'
```
