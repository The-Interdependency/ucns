# UCNS Möbius Seed of Life construction candidate v0.1

**Authority:** Erin Spencer  
**Recorded:** 2026-08-10  
**Repository jurisdiction:** UCNS  
**Status:** implemented, nonselecting geometric candidate  
**Selection effect:** none  
**Machine contract:** [`mobius-seed-of-life-candidate-v1.json`](mobius-seed-of-life-candidate-v1.json)  
**Source record:** [`source/INTERSECTING_MOBIUS_STRIPS_AND_QUANTUM_GEOMETRY.md`](source/INTERSECTING_MOBIUS_STRIPS_AND_QUANTUM_GEOMETRY.md)

|∆|The seven-band Möbius Seed of Life belongs in UCNS because it is the geometric carrier and relationship object. METAPAT may later consume a commit-pinned invariant receipt to construct a spectral argument; it does not own or redefine the geometry.|∆|

## I. Scope

This candidate constructs all seven Möbius bands, the complete pair ledger, the exact projected centerline-event ledger, a two-turn phase schedule, a bounded braid-order ledger, and a deterministic sampled 3D surface export.

It does **not** assert:

- that the sampled surfaces are a certified smooth, transverse, locked embedding;
- that the four claimed single-boundary crossings of every adjacent Möbius vesica have solved exact 3D coordinates;
- that an electron is literally a Möbius strip or that the construction follows from the Pauli exclusion principle;
- that the center is already ratified as a UCNS vertex or Structural Null;
- that a spectral operator has been derived; or
- that any theorem about the Riemann zeta function has been proved.

## II. Exact seven-circle scaffold

Let every centerline circle have radius

\[
R=1.
\]

Use axial hexagonal coordinates \((q,r)\) with exact planar map

\[
C(q,r)=\left(q+\frac r2,\;\frac{\sqrt3}{2}r\right).
\]

The seven band centers are

\[
\begin{aligned}
M_0&:C(0,0),\\
M_1&:C(1,0),&M_2&:C(0,1),&M_3&:C(-1,1),\\
M_4&:C(-1,0),&M_5&:C(0,-1),&M_6&:C(1,-1).
\end{aligned}
\]

This is the complete one-center-plus-six Seed-of-Life scaffold. It does not add an eighth object at the projected center.

## III. Native Möbius band

For band center \((c_x,c_y)\), traversal turns \(u\), normalized transverse coordinate \(v\in[-1,1]\), half-width \(w=1/6\), chirality \(\chi\in\{-1,+1\}\), and lifted phase \(p\in[0,2)\), the renderer uses

\[
\theta=2\pi u,
\qquad
\tau=\pi(\chi u+p),
\]

\[
S(u,v)=
\left(
 c_x+(R+wv\cos\tau)\cos\theta,
 c_y+(R+wv\cos\tau)\sin\theta,
 wv\sin\tau
\right).
\]

It obeys the Möbius quotient endpoints

\[
S(u+1,v)=S(u,-v),
\qquad
S(u+2,v)=S(u,v).
\]

Thus one 360-degree turn reverses the retained local transverse side, while two turns return the complete sampled state.

## IV. Dyad-first phase candidate

The source requires the first dyad to be anti-aligned and later bands to phase-shift incrementally, but it does not give a numeric schedule. This candidate uses the following explicit, reversible schedule:

| Band | Role | Lifted phase in turns | Visible phase | Frame | Rendering chirality |
|---|---|---:|---:|---|---|
| M0 | central monad | 0 | 0 | positive | deosil |
| M1 | first outer dyad | 1 | 0 | reversed | widdershins |
| M2 | outer | 7/6 | 1/6 | reversed | widdershins |
| M3 | outer | 4/3 | 1/3 | reversed | widdershins |
| M4 | outer | 3/2 | 1/2 | reversed | widdershins |
| M5 | outer | 5/3 | 2/3 | reversed | widdershins |
| M6 | outer | 11/6 | 5/6 | reversed | widdershins |

The exact 1/6-turn increment and chirality pattern are |∆|candidate assumptions|∆|. They are machine-visible and replaceable; they are not silently attributed to the source.

## V. Complete pair ledger

All unordered pairs are retained:

\[
\binom72=21.
\]

Their exact center-distance classes are:

| Relationship | Squared distance | Pair count | Centerline events per pair | Total events |
|---|---:|---:|---:|---:|
| radius-distance Möbius vesica | 1 | 12 | 2 | 24 |
| secondary overlap | 3 | 6 | 2 | 12 |
| opposite tangency | 4 | 3 | 1 | 3 |
| **Total** | — | **21** | — | **39** |

The twelve radius-distance pairs are the six central-to-outer relations plus the six adjacent outer-ring relations. Every one receives two occurrence-addressed projected centerline events. The other nine pair relations remain present rather than being discarded because they are not immediate braid neighbors.

## VI. Exact projected-coordinate multiplicity

The 39 pair-addressed events occupy 13 exact projected coordinates over \(\mathbb Q(\sqrt3)\). Their multiplicity spectrum is

\[
15,\underbrace{3,3,3,3,3,3}_{6\text{ coordinates}},
\underbrace{1,1,1,1,1,1}_{6\text{ coordinates}}.
\]

The origin carries 15 distinct pairwise occurrences:

- six from adjacent outer pairs;
- six from secondary outer overlaps; and
- three from opposite outer tangencies.

These occurrences are retained separately. Current UCNS display law does not merge the origin into a character vertex or automatically promote it to Structural Null. The source hypothesis that the center is a null anchor/topological void is retained beside that standing as an unresolved interpretation boundary.

## VII. Braid and boundary-crossing obligations

Each of the twelve adjacent Möbius-vesica pairs receives:

- two alternating pair-order signs at its projected centerline events; and
- two local single-boundary slots per event, for four boundary-crossing obligations per pair.

Therefore the complete ledger contains

\[
12\times4=48
\]

single-boundary crossing obligations.

The ledger is not a transversality certificate. In v0.1 each obligation has `realized_point: null`; exact 3D intersection coordinates, tangent independence, and global compatibility across all seven bands remain open. This prevents a visually plausible mesh from being misreported as the solved locked lattice.

## VIII. Deterministic 3D export

`render_mobius_seed_obj()` samples every band independently and closes each longitudinal seam with reversed transverse indexing. Fixed sampling counts produce byte-deterministic Wavefront OBJ text linked to the exact construction digest.

The export is useful for inspection, numerical intersection search, and future deformation experiments. Its standing is:

`deterministic-sampled-rendering-not-smooth-embedding-certification`

## IX. UCNS / METAPAT authority boundary

### UCNS owns

- the seven-band construction;
- exact center identities and phase/chirality candidate declarations;
- the complete pair and occurrence ledgers;
- exact projected-coordinate invariants;
- boundary-crossing obligations;
- rendering and embedding evidence; and
- any later topological certification of the object.

### METAPAT may consume later

- an immutable UCNS commit and construction digest;
- a separately defined operator derived from UCNS invariants;
- an independently checked spectral correspondence;
- a proof that the operator has the required symmetry or self-adjointness; and
- only then, a zeta-function theorem packet.

No theorem standing transfers merely because METAPAT references the shape.

## X. Zeta proof doorway

The next mathematical bridge is not “look for zeros in the picture.” It is to derive a precise invariant-bearing operator from the seven-band object. A viable proof program must at minimum supply:

1. a Hilbert space or other exact state space generated by the construction;
2. a densely defined operator with explicit domain and boundary conditions;
3. a proof of the operator property needed to constrain its spectrum;
4. a trace, determinant, transfer, or counting identity linked exactly to \(\zeta(s)\) or its completed form;
5. a bijective, multiplicity-preserving correspondence between the relevant spectrum and nontrivial zeros; and
6. a proof that the construction forces, rather than assumes, the critical-line condition.

Until those steps exist, the Möbius Seed is a candidate proof object and invariant source—not a proof by resemblance.

## Validation

The candidate modules and nine resolving tests cover:

- seven-band phase and two-turn Möbius return;
- complete 21-pair and 39-event counts;
- the 13-coordinate multiplicity ledger;
- non-promotion of the 15-fold center bundle;
- all 48 unresolved boundary obligations;
- deterministic reversed-seam OBJ output; and
- the UCNS/METAPAT authority boundary.

Full repository tests, package build, Twine checks, and deterministic `ucns_msdmd.ts` regeneration remain required before test-backed merge standing.

## hmmm

The object is now exact where the source and current UCNS law support exactness, explicit where a candidate convention was necessary, and unresolved where a smooth locked embedding and zeta bridge still require mathematics rather than confidence.
