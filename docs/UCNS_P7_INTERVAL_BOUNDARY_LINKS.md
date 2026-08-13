# P7 outward-interval and Möbius ribbon-boundary link certificate

**Status:** nonselecting, computer-assisted UCNS research certificate  
**Research order:** P7 first, P5 second  
**Selection effect:** none  
**Recorded:** 2026-08-11  
**Source basis:** `Möbius Strips and Quantum Geometry.txt`  
**Source SHA-256:** `dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1`

## 1. Purpose and standing

The preceding P7 artifact constructed seven smooth finite-width Möbius ribbons and covered every pair-parameter torus with a deterministic binary64 Lipschitz subdivision. It established a centerline target of

\[
\frac{9}{100}
\]

and therefore a finite-width ribbon clearance of

\[
\frac{7}{100}
\]

at half-width \(w=1/100\). Its explicit next boundary was:

1. replay separation with directed interval endpoints;
2. extract each Möbius ribbon's one continuous boundary curve;
3. calculate boundary-component and first higher-order link invariants;
4. do this before defining any spectral object.

This artifact carries out those steps for P7 first and then applies the same protocol independently to P5.

The source supplies the shared carrier requirement that one traversal reaches the opposite side and a second traversal returns to the original position and orientation, together with the proposed seven-loop phase-shifted braided target. The interval method, boundary-cable analysis, Smith normal forms, generic projection, and Milnor calculations are new UCNS research constructions. They are not claims made by the source.

## 2. Outward-directed interval replay

### 2.1 Pair domain

For every unordered carrier pair \((i,j)\), replay the complete parameter torus

\[
(t,s)\in[0,1]^2.
\]

Every subdivision endpoint is an exact dyadic rational. Carrier centers are entered as exact rational or quadratic expressions. At a box center, elementary functions are evaluated with `mpmath.iv` directed interval endpoints at 70 decimal digits.

For a box

\[
B=[a,b]\times[c,d],
\]

let \(t_0=(a+b)/2\) and \(s_0=(c+d)/2\). Interval evaluation gives a lower endpoint

\[
d_0^-\le
\left\|\gamma_i(t_0)-\gamma_j(s_0)\right\|.
\]

The already derived exact lift-derivative majorants give interval upper endpoints \(L_i^+\) and \(L_j^+\) for the curve speeds. Every point in the box then satisfies

\[
\left\|\gamma_i(t)-\gamma_j(s)\right\|
\ge
 d_0^-
 -L_i^+\frac{b-a}{2}
 -L_j^+\frac{d-c}{2}.
\]

A leaf is accepted only when this directed lower endpoint is strictly greater than

\[
\boxed{\frac9{100}}.
\]

No separately chosen floating-point subtraction is used in this replay. If a box does not close, the parameter direction with the larger Lipschitz contribution is bisected.

### 2.2 P7 result

| Quantity | P7 result |
|---|---:|
| Carriers | 7 |
| Unordered carrier pairs | 21 |
| Parameter boxes evaluated | 6,173 |
| Maximum subdivision depth | 20 |
| Smallest accepted directed lower endpoint | 0.0900051500007549715176580207299 |
| Required centerline target | \(9/100\) |
| Every pair certified | yes |

The limiting P7 pair is `C::R5` in this deterministic subdivision ledger.

### 2.3 P5 same-protocol result

| Quantity | P5 result |
|---|---:|
| Carriers | 5 |
| Unordered carrier pairs | 10 |
| Parameter boxes evaluated | 4,340 |
| Maximum subdivision depth | 20 |
| Smallest accepted directed lower endpoint | 0.0900086235387926259626106258406 |
| Required centerline target | \(9/100\) |
| Every pair certified | yes |

The limiting P5 pair is `R2::R3`.

### 2.4 Finite-width consequence

Every ribbon point lies no farther than \(w=1/100\) from its centerline. Therefore, for distinct ribbons,

\[
\begin{aligned}
d(\mathcal R_i,\mathcal R_j)
&\ge d(\gamma_i,\gamma_j)-2w\\
&>\frac9{100}-\frac2{100}\\
&=\boxed{\frac7{100}}.
\end{aligned}
\]

Thus the complete declared P7 and P5 finite-width ribbons remain pairwise disjoint under the interval replay.

### 2.5 Interval proof boundary

This is an outward-directed replay at the `mpmath` library level. It is stronger than the earlier binary64-plus-guard computation because transcendental values and derived bounds are carried as directed endpoint intervals. It is not yet:

- an independently implemented MPFI replay;
- a proof-assistant theorem;
- a formally checked certificate of every library rounding primitive.

The complete pair ledger and every accepted lower endpoint are retained in the expanded machine receipt.

## 3. Extracting the one continuous Möbius boundary

For one ribbon, retain positive breadth and traverse two carrier turns:

\[
B_i(t)=X_i(t,w),
\qquad 0\le t<2.
\]

Because

\[
X_i(t+1,w)=X_i(t,-w),
\]

the positive and negative local strip edges are successive portions of one continuous boundary component. Closure occurs after two turns:

\[
B_i(t+2)=B_i(t).
\]

Let the selected phase field have integer winding \(\omega_i\). During two carrier turns:

- the boundary travels twice longitudinally around the carrier core;
- the Möbius half-turn contributes one normal-frame revolution;
- the phase field contributes \(2\omega_i\) further normal-frame revolutions.

The boundary slope in the carrier's tubular torus is therefore

\[
[B_i]=2\lambda_i+(1+2\omega_i)\mu_i.
\]

The meridional coefficient is odd, so

\[
\gcd(2,1+2\omega_i)=1.
\]

The slope is primitive and describes one boundary component, not two.

## 4. Boundary-component knot types

Each carrier centerline is a vertical graph over an embedded planar circle. Scaling its height function continuously to zero supplies an explicit isotopy to the circle, so every core component is an unknot.

A primitive slope

\[
2\lambda+q\mu
\]

on the boundary of its embedded tubular neighborhood is consequently the torus knot \(T(2,q)\), with orientation-sensitive sign carried by \(q\).

### 4.1 Selected P7 and P5 phase law

Both selected candidates use:

\[
\omega_C=3,
\qquad
\omega_{R_i}=0.
\]

Therefore:

| Carrier type | Boundary slope | Knot type | Core-boundary linking |
|---|---:|---|---:|
| Center `C` | \((2,7)\) | \(T(2,7)\) | 7 |
| Every outer `Ri` | \((2,1)\) | unknot \(T(2,1)\) | 1 |

For the center-boundary knot \(T(2,7)\):

\[
g=3,
\qquad
\det=7,
\qquad
c=7,
\]

and the symmetrically normalized Alexander polynomial is

\[
\Delta_C(t)=
 t^3-t^2+t-1+t^{-1}-t^{-2}+t^{-3}.
\]

Every outer boundary has

\[
\Delta_{R_i}(t)=1.
\]

### 4.2 Important comparison warning

P7 and P5 currently have the same selected center phase winding \(\omega_C=3\). Both therefore have a \(T(2,7)\) center-boundary component.

> The center-boundary knot type alone does not encode the prime label.

Any prime-specific distinction must come from the complete interaction system, not from this one component invariant.

## 5. Boundary and mixed pairwise linking

Let

\[
L=(\ell_{ij})
\]

be the oriented core linking matrix and put

\[
q_i=1+2\omega_i,
\qquad
D=\operatorname{diag}(q_i).
\]

For distinct tubular neighborhoods, the boundary's longitudinal multiplicity controls external linking. Hence

\[
\operatorname{lk}(B_i,B_j)=4\ell_{ij}
\qquad(i\ne j),
\]

and

\[
\operatorname{lk}(C_i,B_j)=2\ell_{ij}
\qquad(i\ne j).
\]

On the diagonal,

\[
\operatorname{lk}(C_i,B_i)=q_i.
\]

Thus the boundary matrix and mixed core-boundary block are

\[
L_{\partial}=4L,
\qquad
M=2L+D.
\]

The complete core-plus-boundary pairwise matrix is

\[
\Lambda=
\begin{pmatrix}
L&M\\
M^T&4L
\end{pmatrix}.
\]

These are invariants of the oriented components. Reorienting components conjugates the matrices by diagonal sign matrices and leaves rank, nullity, absolute determinant, and Smith factors unchanged.

### 5.1 P7 exact integer readouts

For the seven boundary components:

| Invariant | P7 boundary matrix |
|---|---:|
| Rank over \(\mathbb Q\) | 6 |
| Nullity | 1 |
| Nonzero Smith factors | \(4,4,4,4,4,4\) |

For all seven cores plus all seven boundaries:

| Invariant | P7 full \(14\times14\) matrix |
|---|---:|
| Rank over \(\mathbb Q\) | 14 |
| Nullity | 0 |
| Determinant | 73,423 |
| Factorization | \(7\cdot17\cdot617\) |
| Smith factors | thirteen \(1\)'s, then \(73{,}423\) |

### 5.2 P5 exact integer readouts

For the five boundary components:

| Invariant | P5 boundary matrix |
|---|---:|
| Rank over \(\mathbb Q\) | 2 |
| Nullity | 3 |
| Nonzero Smith factors | \(4,4\) |

For all five cores plus all five boundaries:

| Invariant | P5 full \(10\times10\) matrix |
|---|---:|
| Rank over \(\mathbb Q\) | 10 |
| Nullity | 0 |
| Determinant | 1,519 |
| Factorization | \(7^2\cdot31\) |
| Smith factors | eight \(1\)'s, then \(7,217\) |

These exact integer readouts distinguish the current P7 and P5 candidates. They do not classify the complete links.

### 5.3 Terminology boundary

The object analyzed here is the **link of ribbon-boundary components**. It should not be called a “boundary link” in the specialized knot-theoretic sense merely because each component bounds its own Möbius ribbon: those spanning surfaces are nonorientable and are not asserted to be disjoint orientable Seifert surfaces.

## 6. Simultaneous generic projection of the core link

Milnor readouts require a generic link diagram with distinct crossing parameters. The exact projected primitive contains multi-carrier hypernodes, so the implementation applies one deterministic simultaneous in-plane translation to all carrier centers.

The maximum translation per component is bounded by

\[
\frac7{5000}=0.0014.
\]

Because two components may move toward one another, the residual complete-ribbon clearance is bounded below by

\[
\frac7{100}-2\frac7{5000}
=
\boxed{\frac{42}{625}}
=0.0672.
\]

The translated projection therefore remains within a disjoint ambient isotopy of the certified ribbons.

| Generic-diagram quantity | P7 | P5 |
|---|---:|---:|
| Double crossings | 36 | 16 |
| Minimum distinct crossing-turn gap | 0.000171017593726416... | 0.000340771090498766... |
| Minimum crossing-height gap | 0.1 | 0.1 |
| Pairwise linking matrix preserved | yes | yes |

The crossing locations are solved at 80 decimal digits. The retained positive turn gaps make the subsequent deterministic ordering stable at the represented precision. This ordering has not yet been interval-replayed.

## 7. Length-three Milnor profile

For an ordered triple of distinct components, the implementation builds Wirtinger longitudes and computes the degree-two coefficient in the truncated noncommutative Magnus expansion. The convention is regression-tested on the closure of

\[
(\sigma_1\sigma_2^{-1})^3,
\]

where the Borromean triple invariant has magnitude one. Antisymmetry and cyclic behavior are checked in that regression.

For a triple \((i,j,k)\), the Milnor invariant \(\bar\mu_{ijk}\) is defined modulo

\[
\delta=\gcd\bigl(
\operatorname{lk}(L_i,L_j),
\operatorname{lk}(L_i,L_k),
\operatorname{lk}(L_j,L_k)
\bigr).
\]

When all three pairwise linking numbers vanish, \(\delta=0\) and the length-three invariant is integer-valued. When \(\delta=1\), the residue class contains no information.

### 7.1 P7 result

P7 has

\[
\binom73=35
\]

core-component triples. Five are algebraically split and therefore have integer-valued length-three invariants:

| P7 triple | \(\bar\mu\) |
|---|---:|
| \((R_0,R_1,R_4)\) | 0 |
| \((R_0,R_1,R_5)\) | 0 |
| \((R_0,R_2,R_5)\) | 0 |
| \((R_0,R_4,R_5)\) | 0 |
| \((R_1,R_4,R_5)\) | 0 |

The values are unchanged across five basepoint choices and satisfy the checked antisymmetry relations.

The remaining 30 triples have indeterminacy modulus one and therefore yield only the trivial residue class.

### 7.2 P5 result

P5 has

\[
\binom53=10
\]

core-component triples. Five are algebraically split:

| P5 triple | \(\bar\mu\) |
|---|---:|
| \((C,R_0,R_1)\) | 0 |
| \((C,R_0,R_2)\) | 0 |
| \((C,R_0,R_3)\) | 0 |
| \((C,R_1,R_3)\) | 0 |
| \((R_0,R_1,R_3)\) | 0 |

The remaining five have indeterminacy modulus one.

### 7.3 Meaning of the zero result

The supported conclusion is negative but useful:

> No informative nonzero length-three Milnor invariant is detected in the current P7 or P5 core-link witness.

In particular, the current algebraically split triples do not exhibit a Borromean-type length-three obstruction. This does **not** imply that the whole link is reducible to pairwise linking. Length-four and higher Milnor invariants, Massey-product structure, multivariable Alexander invariants, and the complement group remain open.

## 8. Consolidated result

Within the declared witness and computational boundary:

1. every P7 and P5 centerline pair clears \(9/100\) under directed interval replay;
2. every distinct finite-width ribbon pair clears \(7/100\);
3. every Möbius ribbon has one explicitly extracted two-turn boundary component;
4. the center boundary is \(T(2,7)\), while every outer boundary is \(T(2,1)\);
5. exact boundary and mixed linking matrices, determinants, factorizations, and Smith forms are issued;
6. a clearance-preserving simultaneous generic projection preserves the core linking matrix;
7. every informative length-three Milnor invariant computed for P7 and P5 is zero.

## 9. Explicit nonclaims

This artifact does not establish:

- proof-assistant verification of the interval library or every leaf;
- one canonical generic projection for all possible diagram invariants;
- the complete ambient-isotopy class of the P7 or P5 ribbon links;
- length-four or higher Milnor invariants;
- the multivariable Alexander polynomial, HOMFLY-PT polynomial, or full link group;
- an arithmetic redefinition of primality;
- an electron ontology or derivation of the Pauli exclusion principle;
- a spectral operator, prime-power law, zeta-zero correspondence, zeta theorem, or proof of the Riemann hypothesis;
- EDCM or METAPAT validity.

## 10. Next proof boundary

The next maximal action is:

1. export the complete dyadic interval leaf ledger in a proof-checkable format;
2. replay it with an independent outward-rounded backend or proof assistant;
3. compute length-four Milnor invariants for the zero-pairwise-linking sublinks;
4. compute a multivariable Alexander-type invariant of the complete core and core-boundary links;
5. compare the resulting higher-order signatures of P7 and P5;
6. only then define a spectral or trace object.

## 11. Reproduction

Install the research dependencies:

```bash
python -m pip install -e '.[test,research]'
```

Run the stacked tests:

```bash
PYTHONPATH=src python -m pytest -q \
  tests/test_prime_primitives.py \
  tests/test_prime_phase_lift.py \
  tests/test_prime_smooth_ribbons.py \
  tests/test_prime_interval_boundary_links.py
```

Regenerate the expanded and compact receipts:

```bash
PYTHONPATH=src python -c \
  'from ucns.prime_interval_boundary_links import write_interval_boundary_family_certificate, write_interval_boundary_family_summary; write_interval_boundary_family_certificate("generated/prime-interval-boundary-family-certificate-expanded.json"); write_interval_boundary_family_summary("generated/prime-interval-boundary-family-certificate.json")'
```

## 12. Mathematical references for the Milnor calculation

- Blake Mellor and Paul Melvin, “A geometric interpretation of Milnor's triple linking numbers,” *Algebraic & Geometric Topology* 3 (2003), 557–568, arXiv:math/0110001.
- Dennis DeTurck, Herman Gluck, Rafael Komendarczyk, Paul Melvin, Haggai Nuchi, Clayton Shonkwiler, and David Shea Vela-Vick, “Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links,” arXiv:0901.1612.
