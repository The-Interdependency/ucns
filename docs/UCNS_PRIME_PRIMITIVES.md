# UCNS prime primitives: P7 first, P5 second

**Status:** nonselecting exact projected research artifact  
**Source:** `Möbius Strips and Quantum Geometry.txt`  
**Source SHA-256:** `dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1`

## Standing

The working hypothesis is

\[
p\longmapsto\mathcal P_p,
\]

where every prime label may have its own geometric primitive. A higher form is constructed directly; dyadic and triadic forms found inside it are restrictions or projections, not parts from which it was assembled.

Arithmetic primality and UCNS primitive standing are separate predicates. Under the ordinary divisor definition, 2 remains prime. The exact conditional finding is narrower:

\[
K_2:\quad \beta_1=E-V+1=1-2+1=0.
\]

Thus 2 fails any **declared closed-primitive criterion** requiring a nontrivial relational cycle. That does not prove that 2 is nonprime in arithmetic, because the internal 720-degree Möbius return might itself count as primitive closure. The ontology remains open until the closure axiom is chosen.

## Direct P7 construction

P7 contains one central radius-one carrier and six radius-one outer carriers whose centers form a regular hexagon on the unit circle. The object is primary before any pair or triad is extracted.

Its exact complete-pair signature is:

| Relation | Count | Squared center distance |
|---|---:|---:|
| Unit vesica | 12 | 1 |
| Other secant | 6 | 3 |
| Tangent | 3 | 4 |

The 21 pairs produce 39 projected pair events. Those events occupy 13 exact hypernodes with arity spectrum

\[
\{2^6,3^6,6^1\}.
\]

At the origin, all six outer centerlines coincide. This is one arity-six projected hypernode. Its 15 pairwise coincidences are a derived flattening:

\[
\binom62=15.
\]

The six spokes and six adjacent-rim edges all have center separation one. More generally, for an outer ring of order \(q\), adjacent-rim separation is

\[
2\sin\frac\pi q.
\]

Equality with the unit spoke requires

\[
2\sin\frac\pi q=1,
\]

whose unique integer solution for \(q\ge3\) is \(q=6\). Therefore total carrier cardinality is

\[
p=q+1=7.
\]

Seven is the unique equal-radius central-ring member with one uniform unit-vesica relation on every wheel edge.

After P7 exists, it yields 12 dyadic unit-vesica restrictions and 6 all-unit-vesica triadic restrictions. These do not construct or exhaust the arity-six primitive.

## Direct P5 construction

P5 contains one central radius-one carrier and four radius-one outer carriers centered at the cardinal directions. It is rebuilt directly from cardinality five; it is not obtained by deleting two bands from P7.

Its exact complete-pair signature is:

| Relation | Count | Squared center distance |
|---|---:|---:|
| Unit vesica | 4 | 1 |
| Other secant | 4 | 2 |
| Tangent | 2 | 4 |

The 10 pairs produce 18 projected pair events occupying 13 exact hypernodes with arity spectrum

\[
\{2^{12},4^1\}.
\]

The origin is one arity-four projected hypernode, whose pairwise flattening is

\[
\binom42=6.
\]

P5 has four unit-vesica spoke restrictions but no all-unit-vesica triadic restriction. Its adjacent-rim distance is \(\sqrt2\), so its closure uses a mixed relation spectrum. This is part of its own primitive signature rather than a failed copy of P7.

## Möbius boundary

The source supplies the shared carrier rule: one traversal reverses the retained side or breadth frame and a second traversal returns it. The current P7 and P5 artifacts certify projected carrier and hypernode complexes only.

They do not yet assign:

- a seam-compatible phase field;
- chirality or any higher carrier state;
- physical contact versus projected coincidence;
- over-under braid order;
- boundary-curve events;
- a three-dimensional null void;
- link topology or ambient isotopy.

## Next action

The next prime-family goal is no longer another P7 invariant. Test whether independently constructed P2, P3, P5, and P7 views can reconstruct deliberately removed relational information exactly and uniquely.

Proceed in dependency order:

1. resolve P2 enough to emit one explicit candidate representation without changing arithmetic primality;
2. construct P3 directly as its own artifact rather than as a restriction of P5/P7;
3. freeze the source fixture, view mappings, erasures, baselines, resource bounds, and outcome criteria in [`PRIME_LOSS_RECONSTRUCTION_PLAN.md`](PRIME_LOSS_RECONSTRUCTION_PLAN.md);
4. run only the smallest single-relation erasure test first;
5. record `FALSIFIED`, `SURVIVED`, or `UNRESOLVED` before repair or escalation;
6. only after survival, test structural erasure, leave-one-view-out contribution, and simpler matched baselines.

P5/P7 distinguishability is prerequisite evidence, not evidence of reconstruction. No claim that all four views are necessary, sufficient, or prime-specific is active until the frozen tests survive.

No spectral operator, prime-power law, zeta-zero correspondence, or proof of the Riemann hypothesis is claimed.

## Usage guidance

Use this document for the current standing of the direct P5/P7 artifacts. Use `docs/PRIME_LOSS_RECONSTRUCTION_PLAN.md` for the reconstruction experiment and its stop rules. Do not infer P2/P3 construction standing from dyadic or triadic restrictions inside P5/P7.

## Reproduction

```bash
PYTHONPATH=src python -m pytest -q tests/test_prime_primitives.py
```
