# Möbius Seed global phase-and-lift compatibility certificate

**Status:** exact UCNS obstruction certificate within a declared assembly family  
**Selection effect:** none  
**Stack:** PR #174 → PR #175 → this artifact  
**Source basis:** `Möbius Strips and Quantum Geometry.txt`  
**Source SHA-256:** `dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1`

## 1. Question

The local Möbius-vesica artifact supplies one exact two-band realization with:

- opposite twist chirality;
- a quarter-turn relative phase in the normalized horizontal placement;
- two physical centerline contacts;
- four physical contacts between the two single continuous boundary curves.

The seven-band Seed-of-Life projection has twelve structural vesica pairs:

- six center-to-ring pairs;
- six adjacent-ring pairs.

This artifact asks the next exact question:

> Can all twelve structural pairs simultaneously be orientation-preserving rigid copies of the certified local dyad when each of the seven global bands has one constant chirality and one constant surface phase?

It also checks whether the same pair event may simultaneously be a physical three-dimensional contact and a strictly separated over-under braid crossing.

## 2. Assumptions and limits

The result applies only under all of the following assumptions:

1. The structural relation graph is the wheel \(W_7\): one center vertex, six rim vertices, six spokes, and six rim edges.
2. Each global Möbius band carries one constant chirality \(\chi\in\{-1,+1\}\).
3. Each global band carries one constant surface phase \(\phi\).
4. Every inheriting structural pair is a rigid copy of the normalized quarter-turn, opposite-chirality dyad certified in PR #175.
5. Contact and braid separation are compared only when they refer to the same two occurrences at the same event.

The result is **not** an obstruction to nonconstant phase fields, recursive carriers, multiple phase channels, other local dyad families, or event splitting.

## 3. Surface phase is modulo one half turn

For the standard Möbius ribbon parameterization,

\[
X(t,u;\phi+\tfrac12)=X(t,-u;\phi).
\]

Because \(u\in[-w,w]\), replacing \(\phi\) by \(\phi+\tfrac12\) gives the same unlabelled surface. Its single continuous boundary is also the same curve, shifted by one carrier turn.

Therefore the global assembly problem uses

\[
\phi\in\mathbb{Q}/\tfrac12\mathbb{Z}
\]

for the exact rational phases appearing here. This is the more permissive unlabelled-surface quotient. If a seam label or signed breadth orientation is retained, phase lives modulo one turn and compatibility can only become stricter; the obstruction below therefore does not depend on discarding a seam label.

## 4. Rigid-rotation phase transport

The normalized certified dyad has:

\[
(\chi_L,\phi_L)=(+1,0),
\qquad
(\chi_R,\phi_R)=(-1,\tfrac14).
\]

Rotate the complete dyad in its plane by \(\rho\) turns. A local carrier parameter \(t\) becomes the global parameter

\[
q=t+\rho.
\]

The frame angle transforms as

\[
\chi\pi t+2\pi\phi
=
\chi\pi q+2\pi\left(\phi-\frac{\chi\rho}{2}\right).
\]

Thus, if the positive-chirality band occupies the left endpoint of an edge whose axis is \(\rho\), the two required global states are

\[
L:\left(+1,-\frac{\rho}{2}\right),
\qquad
R:\left(-1,\frac14+\frac{\rho}{2}\right)
\pmod{\tfrac12}.
\]

If the positive-chirality band occupies the right endpoint, the required states are

\[
L:\left(-1,\frac{\rho}{2}\right),
\qquad
R:\left(+1,\frac14-\frac{\rho}{2}\right)
\pmod{\tfrac12}.
\]

These are not fitted phases. They follow from rigidly rotating the already certified local surface.

## 5. Chirality-only obstruction

Before phase is considered, every exact local copy requires opposite chirality on its two endpoints.

The wheel \(W_7\) contains six triangles. It is not bipartite, so all twelve edges cannot be opposite-chirality edges under one binary chirality assignment.

Exact enumeration with the center chirality fixed positive to quotient the global sign reversal gives:

\[
\max \#\{\text{opposite-chirality structural edges}\}=9.
\]

There are two canonical maximizing assignments: alternating outer chirality, beginning with either sign. Thus at least three of the twelve structural pairs must already depart from the opposite-chirality local relation if every band has one chirality.

This is only the coarse obstruction. The exact phase law is stronger.

## 6. Exact incidence-state obstruction

Two structural pairs are incident when they share one global band. For each of the 33 incident edge pairs, the engine compares all four combinations of local dyad orientation:

\[
33\times 2\times 2=132
\]

exact state comparisons.

The result is:

\[
\boxed{0\text{ compatible oriented incidences out of }132.}
\]

In other words:

> No two distinct structural pairs sharing a band can both be rigid copies of the certified quarter-turn dyad while that shared band retains one constant chirality and one constant surface phase.

This conclusion includes both chirality and phase. It is stronger than the odd-cycle obstruction.

## 7. Global capacity theorem

Because no two inheriting edges may share a vertex, every simultaneously inheriting edge set is a matching in \(W_7\).

A matching on seven vertices has at most

\[
\left\lfloor\frac72\right\rfloor=3
\]

edges. The engine enumerates all \(2^{12}\) structural edge subsets and finds:

- maximum matching size: \(3\);
- number of maximum matchings: \(20\);
- all maximum witnesses are pairwise vertex-disjoint.

Therefore:

\[
\boxed{\text{at most }3\text{ of }12\text{ structural pairs can inherit the exact rigid local certificate}.}
\]

Equivalently:

\[
\boxed{\text{at least }9\text{ structural pairs require a relaxed or different relation}.}
\]

The maximum exact-inheritance fraction is

\[
\frac3{12}=\frac14.
\]

## 8. Six-channel lower bound at the center

The six spoke axes are

\[
\rho_i=\frac{i}{6},
\qquad i=0,\ldots,5.
\]

For either fixed center chirality, the six rigid-copy requirements demand the six distinct surface phases

\[
\left\{
0,
\frac1{12},
\frac16,
\frac14,
\frac13,
\frac5{12}
\right\}
\pmod{\tfrac12}.
\]

Hence a single constant-phase center band can inherit at most one spoke certificate.

If all six spokes are to remain exact rigid copies, the center requires at least six phase channels, six recursively distinguishable carrier states, or a nonconstant phase field capable of realizing six incidence conditions without violating the Möbius seam.

This lower bound does not select among those relaxations.

## 9. Comparison with PR #174

PR #174 pins the following schedule:

- center: positive chirality, phase \(0\);
- outer band \(i\): negative chirality, phase \(\tfrac12+\tfrac{i}{12}\).

Modulo the half-turn surface quotient, the outer phases are

\[
0,
\frac1{12},
\frac16,
\frac14,
\frac13,
\frac5{12}.
\]

Exact comparison with both allowed rigid-copy orientations on every structural edge finds:

\[
\boxed{0\text{ of }12\text{ complete local certificates inherited by PR #174}.}
\]

This does not invalidate PR #174 as a nonselecting braid-lift candidate. It means its half-turn/incremental schedule and the quarter-turn physical-contact certificate are different constructions and cannot be treated as one already-reconciled geometry.

## 10. Lift-event compatibility boundary

A physical three-dimensional centerline contact requires equality of all coordinates. In particular,

\[
\Delta z=0.
\]

A strict over-under braid crossing at the same projected coincidence requires

\[
\Delta z\ne0.
\]

Therefore:

\[
(\Delta z=0)\land(\Delta z\ne0)
\]

is impossible for the same pair of occurrences at the same event.

PR #174 requires nonzero lift-height differences of opposite signs at its two structural projected centerline events. Those events are therefore projected braid crossings, not physical centerline intersections.

The local vesica certificate requires two physical centerline contacts. It cannot be inherited at those same lifted occurrences unless one of the following changes:

1. the lift separation is removed at the physical-contact events;
2. physical contacts and projected braid crossings are assigned to different parameter events;
3. the word “intersection” is explicitly changed from physical equality to projected crossing;
4. a new singular junction semantics is introduced and certified.

The same distinction applies to the four boundary events: physical equality and strict over-under separation cannot describe the same event.

## 11. Result

Under the declared single-state rigid-copy assumptions:

- all twelve certified dyads are obstructed;
- opposite chirality alone can cover at most nine pairs;
- the full rigid chirality-plus-phase law can cover at most three pairs;
- PR #174 currently inherits zero full local rigid-copy certificates;
- same-event physical contact and strict braid separation are logically incompatible.

The strongest supported conclusion is:

> Constant global band state is insufficient as the assembly variable for the full Möbius Seed of Life.

This is a design result, not a declaration that the Möbius Seed is impossible.

## 12. Highest-leverage continuation

The next constructive target is a **Möbius phase-field and event-splitting engine**.

It should define a continuous phase field \(\Phi_i(t)\) on each band, then solve:

\[
\Phi_i(t+1)=\Phi_i(t)+\frac12\pmod 1
\]

or the equivalent seam-compatible frame condition appropriate to the selected parameterization, while imposing the required local states only at the certified contact neighborhoods.

The engine must separately label:

- physical centerline contacts;
- physical boundary contacts;
- projected braid crossings;
- noncontact lift-order events.

Acceptance must allow either:

- a certified phase-field realization;
- a certified obstruction under the declared function class;
- or a precise statement that a recursive or multichannel carrier is required.

## 13. Explicit nonclaims

This artifact is not:

- an obstruction to every possible seven-band Möbius embedding;
- a proof that the source geometry is impossible;
- a classification of nonconstant phase fields;
- a complete lift-equation, linking, or ambient-isotopy theorem;
- an electron ontology or Pauli-exclusion derivation;
- a spectral correspondence, zeta-function theorem, or proof of the Riemann hypothesis;
- EDCM or METAPAT validity.

## 14. Reproduction

From a checkout containing PR #175:

```bash
PYTHONPATH=src python -m pytest -q tests/test_mobius_global_compatibility.py
```

Regenerate the certificate:

```bash
PYTHONPATH=src python -c \
  'from ucns.mobius_global_compatibility import write_global_compatibility_certificate; write_global_compatibility_certificate("generated/mobius-seed-global-compatibility-certificate.json")'
```
