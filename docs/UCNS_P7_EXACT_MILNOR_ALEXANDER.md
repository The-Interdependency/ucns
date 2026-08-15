# P7 exact Milnor and prime-character Alexander experiment

**Status:** nonselecting UCNS research certificate
**Research order:** P7 first, P5 second
**Preregistration SHA-256:** `f8f1a6eae5de2c8235a576266a140c93492554248c2756d838845a19240b23cc`
**Source basis:** `Möbius Strips and Quantum Geometry.txt`
**Source SHA-256:** `dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1`

## 1. Purpose

The preceding packet established three boundaries:

1. direct MPFR replay preserved the global finite-width ribbon clearance;
2. the previously selected central `T(2,7)` boundary was not uniquely forced by maximum phase gap;
3. Fourier estimates for the five pairwise-zero P7 triples converged toward zero, but did not by themselves prove exact Milnor values.

This packet performs the recommended frozen experiment:

- replace the five numerical Milnor conclusions with exact integer coefficients from preferred longitudes;
- evaluate a prime-sensitive phase selector whose criteria were hashed before evaluation;
- calculate a stronger whole-link readout from finite-field specializations of the Fox-Alexander matrix.

## 2. Source and model boundary

The source supplies the shared Möbius carrier condition:

\[
X(t+1,u)=X(t,-u),
\qquad
X(t+2,u)=X(t,u),
\]

and proposes a seven-loop form built through incremental phase shifts and three-dimensional weaving.

The generic projection, Wirtinger presentation, Magnus calculation, Fox matrices, character fields, and phase selector are new UCNS research constructions. They are not statements from the source and are not established particle physics.

## 3. Frozen preregistration

Before the phase functional or the whole-link fingerprints were evaluated, the experiment was written to

```text
docs/PREREGISTRATION_P7_PHASE_ALEXANDER.md
```

and frozen at

```text
f8f1a6eae5de2c8235a576266a140c93492554248c2756d838845a19240b23cc
```

The frozen rules include:

- the exact projection perturbation;
- the Wirtinger and Magnus conventions;
- the finite fields and prime-order characters;
- the phase-lift alignment energy;
- the selector order;
- stopping and failure rules.

No selector criterion refers to the desired boundary degree, to `T(2,7)`, or to a requirement that the output equal the prime.

## 4. Fixed generic projection

Every centerline component is translated in the projection plane by

\[
\delta_i=10^{-3}(a_i,b_i).
\]

For P7:

| Carrier | \((a_i,b_i)\) |
|---|---:|
| C | \((0,0)\) |
| R0 | \((1,2)\) |
| R1 | \((-2,1)\) |
| R2 | \((3,-1)\) |
| R3 | \((-1,-3)\) |
| R4 | \((2,-2)\) |
| R5 | \((-3,3)\) |

The maximum relative component translation is

\[
0.0072111025509279785\ldots
\]

so the straight-line simultaneous translation retains the prior ribbon clearance:

\[
0.07-0.0072111025509279785\ldots
=
0.0627888974490720214\ldots>0.
\]

Thus the generic projection is reached without intersecting the finite-width ribbons.

### P7 generic-diagram margins

| Quantity | Result |
|---|---:|
| Crossings | 38 |
| Wirtinger generators | 38 |
| Relations | 38 |
| Minimum height gap | \(0.1-4.61\times10^{-58}\) |
| Minimum transversality magnitude | 0.1601185173936971… |
| Minimum distance between distinct projected crossing points | 0.000271409310225163… |

### P5 generic-diagram margins

| Quantity | Result |
|---|---:|
| Crossings | 18 |
| Wirtinger generators | 18 |
| Relations | 18 |
| Minimum height gap | 0.1 |
| Minimum transversality magnitude | 0.0892807479681370… |
| Minimum distinct crossing-point gap | 0.00198548274226833… |

The signed crossing half-sums exactly reproduce the complete pairwise linking matrices from the prior smooth-ribbon certificate.

## 5. Exact Milnor calculation

At a crossing of sign \(\varepsilon\), with over meridian \(o\), incoming under meridian \(m_{\mathrm{in}}\), and outgoing under meridian \(m_{\mathrm{out}}\), the Wirtinger update is

\[
m_{\mathrm{out}}
=
o^{\varepsilon}
 m_{\mathrm{in}}
 o^{-\varepsilon}.
\]

Repeated conjugation makes the preferred-longitude conjugator the **reverse** product of the encountered over-arc factors. The implementation therefore prepends each factor during traversal.

For meridian \(x_i\), the Magnus expansion begins

\[
M(x_i)=1+X_i,
\qquad
M(x_i^{-1})=1-X_i+X_i^2+\cdots.
\]

All products are retained exactly through total degree two using rational coefficients. For a pairwise-zero ordered triple \((i,j,k)\), the coefficient of \(X_iX_j\) in the preferred longitude of component \(k\) is the triple Milnor coefficient under the declared orientation convention.

### Borromean gate

The closure of

\[
(\sigma_1\sigma_2^{-1})^3
\]

is evaluated before any P7 result is accepted. The implementation returns

\[
\mu_{012}=+1.
\]

Changing the global orientation convention can reverse the sign, but not its unit magnitude.

### P7 results

| Ordered triple | \(\mu_{ijk}\) | Opposite word coefficient | Longitude degree one |
|---|---:|---:|---:|
| \((R_0,R_1,R_4)\) | 0 | 0 | \((0,0,0)\) |
| \((R_0,R_1,R_5)\) | 0 | 0 | \((0,0,0)\) |
| \((R_0,R_2,R_5)\) | 0 | 0 | \((0,0,0)\) |
| \((R_0,R_4,R_5)\) | 0 | 0 | \((0,0,0)\) |
| \((R_1,R_4,R_5)\) | 0 | 0 | \((0,0,0)\) |

Therefore:

\[
\boxed{
\mu_{ijk}=0
\text{ for all five pairwise-zero P7 triples in the fixed generic diagram.}
}
\]

The prior generalized-Gauss-map Fourier convergence is retained as an independent numerical check. The exact integer result now comes from the link-group longitude calculation rather than from rounding a small floating estimate.

The remaining formal boundary is the high-precision crossing-combinatorics certificate: its margins are explicit and large relative to numerical error, but its `atan2` and smooth-field signs have not yet been replayed in a proof assistant.

## 6. Fox-Alexander whole-link fingerprint

For each Wirtinger relator \(r\), Fox derivatives produce a presentation matrix for the Alexander module after abelianization. The experiment evaluates this matrix at phase-induced finite-field characters.

For P7:

\[
\mathbb F_{29}^{\times}
\supset\langle\zeta_7\rangle,
\qquad
\zeta_7=16.
\]

For P5:

\[
\mathbb F_{11}^{\times}
\supset\langle\zeta_5\rangle,
\qquad
\zeta_5=4.
\]

For candidate \((\omega,n)\), the character is

\[
t_C=\zeta_p^{\omega},
\qquad
t_{R_i}=\zeta_p^{in}.
\]

If the evaluated Fox matrix has \(N\) columns and rank \(r\), define the excess nullity

\[
\nu=N-r-1.
\]

The subtraction removes the universal Fox-kernel direction.

### Complete P7 profile

| Quantity | Result |
|---|---:|
| Prime characters | 42 |
| Excess nullity 0 | 18 |
| Excess nullity 1 | 24 |
| Rank-vector SHA-256 | `ce6657419a659cac667bb4a377181951352346e4cc94525e1f1ef8297d66fff4` |

### Complete P5 profile

| Quantity | Result |
|---|---:|
| Prime characters | 20 |
| Excess nullity 2 | 20 |
| Rank-vector SHA-256 | `c6d2f7f443e150c2941aea4634b8de19f77f9c082dfc9f48d9efc04029971661` |

The same profiles were replayed in the common field \(\mathbb F_{71}\), which contains both fifth and seventh roots of unity. The rank vectors and hashes were unchanged.

This is a whole-link group-module readout stronger in structure than a pairwise linking matrix. It is not the full multivariable Alexander polynomial and is not a complete link invariant.

## 7. Preregistered phase selector

The frozen selector applies, in order:

1. maximum minimum phase gap;
2. maximum Fox-Alexander excess nullity;
3. minimum exact phase-lift alignment energy;
4. minimum \(|\omega\\);
5. positive before negative winding;
6. smallest outer numerator.

The alignment energy is

\[
E(\omega,n)
=
\sum_{h,c}
 d_{S^1}\left(
 \phi_{h,c},
 \frac{r_{h,c}}p
 \right)^2.
\]

### P7

The eight maximum-gap candidates have gap \(1/7\). The whole-link nullity and alignment energy leave two substantive co-winners:

| \(\omega\) | \(n\) | Fox excess nullity | Energy | Boundary degree \(1+2\omega\) |
|---:|---:|---:|---:|---:|
| 3 | 4 | 1 | \(599/196\) | 7 |
| 9 | 4 | 1 | \(599/196\) | 19 |

The frozen minimum-winding tie-break selects

\[
(\omega,n)=(3,4),
\qquad
q=7.
\]

### P5

The four maximum-gap candidates have gap \(1/5\). The substantive criteria leave:

| \(\omega\) | \(n\) | Fox excess nullity | Energy | Boundary degree \(1+2\omega\) |
|---:|---:|---:|---:|---:|
| -3 | 1 | 2 | \(39/20\) | -5 |
| 9 | 1 | 2 | \(39/20\) | 19 |

The same frozen minimum-winding rule selects

\[
(\omega,n)=(-3,1),
\qquad
q=-5.
\]

### Interpretation

Under the complete preregistered selector,

\[
|q_7|=7,
\qquad
|q_5|=5.
\]

This is a genuine outcome of a rule that did not contain a target degree. It is also not yet a theorem that prime cardinality uniquely forces the corresponding boundary knot.

The load-bearing qualification is:

> The whole-link and phase-lift criteria reduce each case to two candidates; the final choice of \(|q|=p\) still depends on the preregistered minimum-winding tie-break.

Thus the result advances the phase-selection hypothesis beyond the former arbitrary tie-break, but does not eliminate selection dependence entirely.

## 8. Consolidated conclusion

The frozen experiment supports four conclusions:

1. The five numerical P7 Milnor-zero candidates are exactly zero at degree two in the fixed generic link diagram.
2. No Borromean-type triple linking remains among those five triples.
3. P7 and P5 have sharply different prime-character Fox rank profiles under the same protocol.
4. The preregistered selector chooses boundary degree \(7\) for P7 and \(-5\) for P5, while exposing the neutral minimum-winding tie-break as the last deciding step.

The presently observed prime-sensitive structure therefore lies in the combination

\[
\text{phase gap}
+
\text{Fox-Alexander resonance}
+
\text{phase-lift alignment}
+
\text{minimum winding},
\]

not in pairwise linking or triple Milnor invariants alone.

## 9. Evidence boundary

This packet does not establish:

- proof-assistant verification of the generic crossing signs;
- a complete ambient-isotopy classification of P7 or P5;
- the full multivariable Alexander polynomial;
- uniqueness of the prime-degree phase law without a neutral tie-break;
- higher Milnor invariants beyond length three;
- an arithmetic redefinition of primality;
- an electron ontology or derivation of the Pauli exclusion principle;
- a spectral operator, prime-power law, zeta-zero correspondence, or proof of the Riemann hypothesis.

## 10. Next action

The first gate below is now complete at the computer-assisted interval level;
see
[`UCNS_P7_GENERIC_INTERVAL_CERTIFICATE.md`](UCNS_P7_GENERIC_INTERVAL_CERTIFICATE.md).
The remaining high-leverage sequence is:

1. **completed:** certify the generic crossing diagram with outward-rounded interval `atan2` and smooth-field evaluation;
2. **partially completed:** derive the symbolic multivariable Alexander presentation and certify the first-nonzero elementary-ideal boundary; complete generating sets remain open;
3. calculate length-four and higher Milnor invariants or finite nilpotent link-group quotients;
4. test whether the two substantive phase co-winners can be separated by a preregistered invariant that does not invoke minimum winding;
5. only then define a spectral or trace object.

## 11. Reproduction

```bash
PYTHONPATH=src python -m pytest -q \
  tests/test_prime_exact_milnor_alexander.py
```

```bash
PYTHONPATH=src python -c \
  'from ucns.prime_exact_milnor_alexander import write_exact_milnor_alexander_family_certificate; write_exact_milnor_alexander_family_certificate("generated/prime-exact-milnor-alexander-family-certificate.json")'
```

## 12. Method references

- J. Milnor, link invariants defined through longitudes and Magnus expansions.
- H. Kodani and T. Nosaka, *Milnor invariants via unipotent Magnus embeddings*.
- K. Okuhara and A. Sakai, *Polyak–Viro type formula for the Milnor triple linking number of link diagrams with multiple-crossings*.
- L. Traldi, *Multivariate Alexander colorings*.
