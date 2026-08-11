# P7-native Möbius phase-and-lift engine

**Status:** nonselecting UCNS research witness  
**Research order:** P7 first, P5 second  
**Source basis:** `Möbius Strips and Quantum Geometry.txt`

## 1. Construction boundary

The source supplies the shared carrier rule: one traversal of a Möbius carrier reverses the retained side or breadth frame, while a second traversal returns to the starting position and orientation. It also supplies the seven-carrier Seed target, incremental phase shifting, weaving, and a final three-dimensional braided form.

This artifact does not reconstruct P7 from finished vesicas or triquetras. It begins with the complete P7 projected primitive—seven carriers and thirteen hypernodes—and solves phase and lift state globally. Pair and triad readouts are derived only afterward.

## 2. Exact phase-law search

The searched family is

\[
\Phi_C(t)=\omega t,\qquad \Phi_{R_i}(t)=\frac{ik}{p}\pmod1.
\]

A candidate is admissible when all carrier occurrences at every projected hypernode have distinct phases. Candidates are ranked by the smallest cyclic phase gap, followed by minimal absolute center winding, positive winding, and smallest outer numerator.

For P7 the selected law is

\[
\omega=3,\qquad k=3,\qquad \Delta\Phi_{\min}=\frac17.
\]

The search evaluates 174 candidates; 144 are admissible.

For the independently rebuilt P5 comparison, the same protocol selects

\[
\omega=3,\qquad k=4,\qquad \Delta\Phi_{\min}=\frac15,
\]

with 84 candidates and 72 admissible.

## 3. Finite-field lift

Each carrier and projected hypernode receives an exact nonzero field relation. At node \(n\), a carrier residue is multiplied by the inverse of the node generator in \(\mathbb F_p\). The result is centered and mapped to a vertical lane with spacing

\[
\lambda=\frac1{10}.
\]

The strip half-width is

\[
w=\frac1{100}.
\]

Every P7 and P5 hypernode has distinct phases and distinct lanes. The minimum centerline separation at a projected event is

\[
\frac1{10},
\]

leaving the local ribbon-clearance lower bound

\[
\frac1{10}-2\left(\frac1{100}\right)=\frac2{25}.
\]

The P7 origin remains one arity-six hypernode. Its exact lane set is

\[
\left\{-\frac3{10},-\frac2{10},-\frac1{10},\frac1{10},\frac2{10},\frac3{10}\right\}.
\]

Its fifteen pair comparisons are derived from that one six-way event. The local vertical void lower bound, after ribbon half-width, is

\[
\frac1{10}-\frac1{100}=\frac9{100}.
\]

## 4. Möbius seam

The lifted centerline height is a periodic piecewise-linear interpolation through the exact event lanes. The breadth frame is

\[
2\pi\left(\frac t2+\Phi_i(t)\right).
\]

The selected phase laws have integral winding on the center carrier and constant outer phase, so the surface satisfies

\[
X_i(t+1,u)=X_i(t,-u),
\qquad
X_i(t+2,u)=X_i(t,u).
\]

The implementation verifies binary64 residuals below \(3\times10^{-15}\). A smooth margin-preserving replacement of the piecewise-linear lift remains a separate obligation.

## 5. Typed event semantics

All projected centerline coincidences receive nonzero height separation. They are therefore typed as:

- projected centerline coincidence;
- strict braid-order event.

The artifact claims zero physical centerline contacts and zero physical boundary contacts. Physical equality and strict over-under separation are not conflated.

Because the projected primitive ledger contains every pairwise centerline coincidence and every one is separated in height, the seven lifted centerline components are pairwise disjoint.

## 6. Derived linking readouts

Only after the global lift is fixed are pairwise crossing signs and linking numbers computed.

P7 regular two-crossing pairs give:

- linking number \(+1\): 12 pairs;
- linking number \(0\): 6 pairs;
- tangent projected pairs unresolved: 3.

The nonzero-link graph has seven vertices, twelve edges, one connected component, and cycle rank six.

P5 gives:

- linking number \(+1\): 2 pairs;
- linking number \(0\): 6 pairs;
- tangent projected pairs unresolved: 2.

Its nonzero-link graph has two edges, three components, and cycle rank zero.

These are centerline-link readouts for the stated projection. They are not yet a whole-ribbon ambient-isotopy classification.

## 7. What is established

Within the declared exact candidate family:

1. P7 is solved globally before restrictions.
2. One exact phase law resolves all thirteen P7 hypernodes.
3. One finite-field lift assigns distinct lanes to every occurrence.
4. The arity-six origin remains one hypernode.
5. All lifted centerlines are pairwise disjoint.
6. The Möbius one-turn reversal and two-turn return hold.
7. Pair linking numbers are derived only after the global solution.
8. P5 is solved independently under the same protocol.

## 8. Open boundaries

This artifact does not yet establish:

- a smooth lift field with a certified global separation margin;
- absence of collisions between complete finite-width ribbons away from projected events;
- a regularized projection and link invariant for tangent pairs;
- boundary-component topology;
- ambient isotopy of the seven-ribbon complex;
- an electron ontology or Pauli-exclusion derivation;
- a spectral operator, prime-power mechanism, zeta-zero correspondence, or proof of the Riemann hypothesis.

## 9. Next action

Construct a margin-preserving smooth phase-and-lift realization and certify global finite-width ribbon disjointness. The tangent pairs should then be regularized under an explicitly declared perturbation before stronger link invariants are calculated.

## 10. Reproduction

```bash
PYTHONPATH=src python -m pytest -q \
  tests/test_prime_primitives.py \
  tests/test_prime_phase_lift.py
```

```bash
PYTHONPATH=src python -c \
  'from ucns.prime_phase_lift import write_phase_lift_family_certificate; write_phase_lift_family_certificate("generated/prime-phase-lift-family-certificate.json")'
```
