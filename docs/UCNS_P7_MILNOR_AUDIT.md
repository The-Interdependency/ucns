# P7 Milnor audit continuation

## 4. Milnor engine

For each generic projection, every ordinary double crossing records:

- the two components;
- the carrier parameters;
- which component passes under and over;
- the oriented crossing sign.

Each component is cut at a basepoint and divided into Wirtinger arcs at its undercrossings. Arc meridians are solved iteratively in the degree-two Magnus algebra:

\[
M_i=1+X_i,
\]

with products truncated after words of length two.

At a crossing of sign `ε`, the outgoing under-arc meridian is updated by

\[
x_{\mathrm{out}}
=
y^{-\varepsilon}x_{\mathrm{in}}y^{\varepsilon},
\]

where `y` is the over-arc meridian. The preferred longitude is the ordered product of the corresponding over-arc conjugators.

For an algebraically split ordered triple `(L1,L2,L3)`,

\[
\bar\mu_{123}
=
[X_1X_2]E(\lambda_3).
\]

The other cyclic longitude coefficients are calculated independently and required to agree.

### 4.1 Calibration

The closure of

\[
(\sigma_1\sigma_2^{-1})^3
\]

is used as a Borromean fixture under the declared orientation. The engine returns:

```text
pairwise linking: 0, 0, 0
cyclic coefficients: -1, -1, -1
mu-bar_123: -1
```

Thus the engine does not collapse every algebraically split triple to zero.

## 5. Frozen P7 triple set

The complete P7 core-linking matrix contains exactly five outer triples whose three pairwise linking numbers all vanish:

```text
(R0, R1, R4)
(R0, R1, R5)
(R0, R2, R5)
(R0, R4, R5)
(R1, R4, R5)
```

## 6. Projection and sampling audit

Five generic orthographic projection directions were used. The smooth centerlines were sampled at 2,048 segments per component to extract the frozen crossing tables.

| Projection | Ordinary crossings | Five Milnor values |
|---|---:|---|
| P0 | 38 | `0,0,0,0,0` |
| P1 | 42 | `0,0,0,0,0` |
| P2 | 38 | `0,0,0,0,0` |
| P3 | 42 | `0,0,0,0,0` |
| P4 | 32 | `0,0,0,0,0` |

Every projection independently reproduces the complete 21-pair P7 linking matrix.

For P0, the extraction was repeated at:

```text
512, 1024, 2048, 4096 segments per component
```

Every resolution produced:

```text
38 ordinary crossings
complete linking-matrix match
Milnor values 0,0,0,0,0
```

Ten deterministic basepoint-offset sweeps also preserved all five values.

The frozen projection-data payload is committed by:

```text
862151539ffaf328df83519cc7d69c00ad46d4ce5b422fcf90e189956fbf6c9c
```

## 7. Result

For the declared P7 smooth-centerline witness:

\[
\boxed{
\bar\mu_{123}=0
}
\]

for all five algebraically split outer triples.

Explicitly:

| Triple | `mu-bar_123` |
|---|---:|
| `(R0,R1,R4)` | 0 |
| `(R0,R1,R5)` | 0 |
| `(R0,R2,R5)` | 0 |
| `(R0,R4,R5)` | 0 |
| `(R1,R4,R5)` | 0 |

Hence:

> No Borromean three-component sublink survives the length-three Milnor test in this P7 witness.

This is a meaningful negative result. The nontrivial P7 topology detected so far is carried by pairwise links and the complete seven-component architecture, not by an algebraically split Borromean triple.

## 8. Evidence boundary

The following distinctions remain load-bearing:

- The phase enumeration is exact rational computation.
- The Magnus calculation is exact integer computation on each frozen crossing table.
- Projection crossing extraction is numerical polygonal geometry.
- Multi-projection, sampling-resolution, linking-matrix, cyclic-coefficient, and basepoint audits strongly constrain extraction error but do not replace an analytic crossing theorem.
- Vanishing length-three Milnor invariants do not imply that every higher Milnor invariant vanishes.
- Pairwise matrices plus length-three Milnor data do not classify the complete seven-component ambient-isotopy type.
- No spectral operator or zeta correspondence is claimed.

## 9. Next action

The next maximal action is no longer to search for Borromean triples. It is to calculate invariants that can detect genuinely seven-component structure:

1. higher-length Milnor invariants in the lower-central-series quotient;
2. the multivariable Alexander polynomial of the complete P7 core link and its boundary cable;
3. a phase-winding sweep that asks which whole-link invariants persist when the center knot changes;
4. only after those gates, a trace or spectral object.

## 10. Reproduction

```bash
PYTHONPATH=src python -m pytest -q \
  tests/test_prime_decimal_intervals.py \
  tests/test_prime_phase_sensitivity_milnor.py
```

```bash
PYTHONPATH=src python -c \
  'from ucns.prime_decimal_intervals import write_decimal_interval_family_certificate; write_decimal_interval_family_certificate("generated/prime-decimal-interval-family-certificate.json")'
```

```bash
PYTHONPATH=src python -c \
  'from ucns.prime_phase_sensitivity_milnor import write_phase_milnor_family_certificate; write_phase_milnor_family_certificate("generated/prime-phase-sensitivity-milnor-certificate.json")'
```
