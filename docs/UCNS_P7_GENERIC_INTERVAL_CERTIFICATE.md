# P7/P5 generic crossing interval certificate

**Status:** nonselecting computer-assisted UCNS research certificate  
**Research order:** P7 first, P5 second  
**Backend:** direct system MPFR with explicit directed rounding  
**Source:** `Möbius Strips and Quantum Geometry.txt`  
**Source SHA-256:** `dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1`

## 1. Result

The first next-action gate from
[`UCNS_P7_EXACT_MILNOR_ALEXANDER.md`](UCNS_P7_EXACT_MILNOR_ALEXANDER.md)
is complete for the frozen generic P7/P5 diagrams.

An independent direct-MPFR replay reconstructs every shifted equal-circle
intersection and evaluates:

1. both incident turns through outward-rounded `atan2`;
2. the complete smooth-field interval on the uniquely containing segment;
3. the over/under height difference;
4. the tangent determinant without a trigonometric sign shortcut; and
5. the resulting oriented crossing sign.

All intervals fail closed on origin containment, `atan2` branch-cut crossing,
segment-boundary ambiguity, zero-containing height difference, or
zero-containing transversality.

| Candidate | Frozen crossings | Interval-reconstructed crossings | Turn display cells matched | Height orders matched | Signs matched |
|---|---:|---:|---|---|---|
| P7 | 38 | 38 | yes | yes | yes |
| P5 | 18 | 18 | yes | yes | yes |

Thus all 56 frozen crossing decisions are independently supported by
outward-rounded interval evidence.

## 2. Independence and comparison boundary

The replay does not use stored turn, height, over/under, or sign fields as
numerical inputs. It rebuilds the translated centers, intersection points,
turns, smooth values, and tangent determinants from the declared construction.
The frozen crossings enter only after evaluation as comparison targets.

The frozen diagram serializes turns with `mp.nstr`. Those strings are rounded
displays, not exact coordinates. The comparison therefore asks whether each
independent interval intersects the display string's half-unit-in-last-place
rounding cell. Treating the display string as exact would counterfeit a stronger
claim and can reject a correct enclosure narrower than the display precision.

## 3. Mathematical construction

For translated unit-circle centers `c_L` and `c_R`, the replay encloses

```text
d = ||c_R - c_L||
h = sqrt(1 - d²/4)
m = (c_L + c_R)/2
p± = m ± h * perpendicular(c_R - c_L)/d
```

Each turn is enclosed by

```text
t = atan2(p_y - c_y, p_x - c_x) / (2π) mod 1.
```

The smooth lift is evaluated over the whole turn interval with the declared
flat step

```text
S(x) = exp(-1/x) / (exp(-1/x) + exp(-1/(1-x))).
```

The tangent determinant is evaluated algebraically from the two radius
intervals. The crossing sign is the sign of

```text
(height_left - height_right) * det(tangent_left, tangent_right).
```

Both factors must exclude zero independently.

## 4. Evidence standing

This closes the prior pointwise generic-crossing sign-margin obligation at the
computer-assisted interval level. It strengthens the evidence supporting the
exact Magnus and Fox calculations on the frozen Wirtinger diagram.

It does **not** establish:

- proof-assistant verification of the MPFR binding or interval formulas;
- a complete ambient-isotopy classification;
- the full multivariable Alexander polynomial;
- higher Milnor invariants;
- uniqueness of the prime-degree phase law;
- an arithmetic, physical, spectral, zeta, or prime-emergence claim.

Selection effect remains `none`.

## 5. Usage guidance

Run the focused checks:

```bash
uv run --extra test python -m pytest -q \
  tests/test_prime_generic_interval_certificate.py
```

Regenerate the deterministic receipt:

```bash
uv run --extra test python -m ucns.prime_generic_interval_certificate \
  generated/prime-generic-interval-family-certificate.json
```

The runtime requires system `libmpfr`. A missing library or ambiguous interval
is a failed certificate, not permission to fall back to point arithmetic.

## 6. Next action

The exact symbolic presentation and first-nonzero elementary-ideal boundary are
now recorded in
[`UCNS_P7_SYMBOLIC_ALEXANDER.md`](UCNS_P7_SYMBOLIC_ALEXANDER.md). The remaining
Alexander obligation is a separately pinned reduced generating-set/Gröbner
protocol. Length-four and higher Milnor or finite nilpotent quotient work remains
an independent next route without erasing the current exact length-three zero
result.

## hmmm

- Proof-assistant replay of the MPFR FFI and interval identities remains open.
- A separately preregistered whole-link invariant capable of separating the two
  substantive phase co-winners remains open.
