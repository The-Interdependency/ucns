# P7 independent interval replay, phase sensitivity, and Milnor triple audit

**Status:** nonselecting UCNS computer-assisted research certificate  
**Research order:** P7 first, P5 comparison second  
**Source basis:** `Möbius Strips and Quantum Geometry.txt`  
**Source SHA-256:** `dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1`

## 1. Purpose

The preceding artifact left three linked proof obligations:

1. replay the continuous separation certificate through a kernel independent of `mpmath.iv`;
2. determine whether the center boundary class `T(2,7)` follows from prime-seven structure or from a selected phase winding;
3. calculate the length-three Milnor invariant for each of the five algebraically split P7 outer triples.

This artifact closes those three obligations within declared computational boundaries.

The source supplies the one-turn opposite-side and two-turn return rule and the proposed seven-loop phase-shifted braid. It does not supply the Decimal interval kernel, phase search law, Wirtinger presentation, Magnus expansion, or Milnor values. Those are new UCNS research constructions.

## 2. Independent directed-Decimal interval kernel

The earlier interval replay used `mpmath.iv` at 80 decimal digits. The independent replay does not import `mpmath`.

It uses:

- exact `Fraction` coordinates for every dyadic subdivision box;
- Python `Decimal` with 90 declared decimal digits and 30 guard digits;
- a hard interval containing π;
- exact rational quadrant reduction for `sin(2πt)` and `cos(2πt)`;
- alternating-series enclosures for sine and cosine on `[0,π/2]`;
- guard-precision Decimal `exp` and `sqrt`, widened outward by one target-precision unit;
- the same analytic curve-speed majorants and exact branch-and-bound decisions as the preceding replay.

This is genuinely independent of the `mpmath.iv` implementation. It is not a proof-assistant-verified transcendental kernel.

### 2.1 P7 result

| Quantity | Directed Decimal | Previous `mpmath.iv` |
|---|---:|---:|
| Carrier pairs | 21 | 21 |
| Boxes evaluated | 6,173 | 6,173 |
| Maximum depth | 20 | 20 |
| Minimum outward lower endpoint | `0.090005150000754974092035106362967...` | `0.09000515000075497...` |
| Required target | `0.09` | `0.09` |
| All pairs certified | yes | yes |

The independent replay selected the same box partition, pair by pair, and all displayed pair minima agree with the earlier interval result to binary64 precision.

The accepted-leaf ledger hash is implementation-specific because the Decimal receipt records longer endpoint strings:

```text
P7 Decimal global leaf ledger:
7b5b6249ce1592632c313b12148fad59cdf46f86d817191b5d053989cebe65d8
```

### 2.2 P5 result

| Quantity | Directed Decimal | Previous `mpmath.iv` |
|---|---:|---:|
| Carrier pairs | 10 | 10 |
| Boxes evaluated | 4,340 | 4,340 |
| Maximum depth | 20 | 20 |
| Minimum outward lower endpoint | `0.090008623538792625962610625869402...` | `0.09000862353879262...` |
| Required target | `0.09` | `0.09` |
| All pairs certified | yes | yes |

```text
P5 Decimal global leaf ledger:
321077fa87c0d41bb921276aba6156978c5373ea33e741f93c6161b202b2d3c8
```

### 2.3 Finite-width consequence

The independent replay preserves

\[
d(\gamma_i,\gamma_j)>\frac9{100}.
\]

At ribbon half-width

\[
w=\frac1{100},
\]

the same triangle-inequality consequence follows:

\[
d(\mathcal R_i,\mathcal R_j)
>
\frac9{100}-2\frac1{100}
=
\frac7{100}.
\]

The small P7 margin above `0.09` remains load-bearing; the independent kernel corroborates rather than eliminates that sensitivity.

## 3. Complete phase-law sensitivity

The declared family searches

\[
\Phi_C(t)=\omega t,
\qquad
\Phi_{R_i}(t)=\frac{ik}{p}\pmod1,
\]

with

\[
-2p\le\omega\le2p,
\qquad
1\le k\le p-1.
\]

A candidate survives only when every hypernode has distinct carrier phases.

### 3.1 P7 search

| Quantity | Result |
|---|---:|
| Raw candidates | 174 |
| Admissible candidates | 144 |
| Selected winding | 3 |
| Selected outer step | `3/7` |
| Selected minimum phase gap | `1/7` |

Admissible candidates by minimum gap:

| Minimum gap | Count |
|---:|---:|
| `1/42` | 20 |
| `1/21` | 80 |
| `1/14` | 26 |
| `2/21` | 10 |
| `1/7` | 8 |

### 3.2 P5 search

| Quantity | Result |
|---|---:|
| Raw candidates | 84 |
| Admissible candidates | 72 |
| Selected winding | 3 |
| Selected outer step | `4/5` |
| Selected minimum phase gap | `1/5` |

### 3.3 Center-knot correction

For the declared framing, center winding `ω` gives boundary cable class

\[
T(2,1+2\omega).
\]

Both selected candidates use

\[
\omega=3,
\]

so both produce

\[
T(2,7).
\]

Therefore:

> `T(2,7)` is currently a consequence of the shared selected winding three. It is not a prime-seven discriminator.

This does not make the center knot irrelevant. It changes its standing from prime-emergent evidence to a framing-sensitive readout that must be varied during later operator experiments.

The prime-sensitive contrast remains in the complete hypernode and linking architecture, not in the center boundary knot alone.


Continued in `UCNS_P7_MILNOR_AUDIT.md`.
