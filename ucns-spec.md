# UCNS — Consolidated Spec and Current Frontier

**Status snapshot**

- **Proved / defended:** flat kernel (v0.3), epicyclic first freeze (v0.4), recursive sequence and multiset primality notions (v0.5), cancellativity + quotient uniqueness boundary (v0.5.1), quotient existence conditions and restricted completeness on a bounded depth-1 domain (v0.6.1–v0.6.5).
- **Oracle-complete only:** depth-2 smallest oracle theorem (v0.8.1).
- **Not solved:** full frozen depth-2 domain and carrier widening beyond current proven bounds.

---

## hmm

This file is the **complete UCNS spec as it currently stands**, with the algebraic layers frozen where they were proved and the later frontier explicitly marked where the current engine fails.

The document is organized as:

1. **Flat kernel v0.3**
2. **Epicyclic extension v0.4**
3. **Recursive factor search and primality v0.5**
4. **Cancellativity, quotients, and restricted completeness v0.5.1–v0.6.5**
5. **Current completeness frontier**

---

# Part I — Flat Kernel v0.3

## 1. Core Ontology

UCNS is a geometric-arithmetic system in which the primitive object is a paired traversal object rather than a scalar or symbol.

A valid flat UCNS object is

\[
\underline{\mathbf{G}} =
\left(
 n_{\mathrm{dec}},
 n_{\min},
 \Theta^{+},
 \Theta^{-},
 F^{+},
 F^{-}
\right)
\]

where:

- \(n_{\mathrm{dec}}\) is the declared carrier, a resolution parameter,
- \(n_{\min}\) is the minimal gonal order determined by the anchors,
- \(\Theta^{+}\) is the positive anchor sequence,
- \(\Theta^{-}\) is the forced mirror sequence,
- \(F^{+}\) is the positive face-state sequence,
- \(F^{-}\) is the forced mirror face-state sequence.

The object is paired. Arithmetic does not occur on a single oriented traversal alone.

## 2. Ambient Space

The ambient geometric carrier is

\[
S^1 = \{ z \in \mathbb{C} : |z| = 1 \}
\]

with doubled angular cover

\[
\widetilde{S^1} \cong \mathbb{R}/4\pi\mathbb{Z}.
\]

The doubled cover is required to encode two-revolution completion and orientation-sensitive traversal.

### 2.1 The Möbius Twist-Point and the Necessity of the Doubled Cover

The doubled cover is not an arbitrary choice. It is required by the existence of the Möbius twist-point.

A single revolution (\(0\) to \(2\pi\)) returns to the same geometric location on \(S^1\) but with orientation flipped. This flip is the Möbius twist: the seam inscribed in the cover where one sheet transitions to the other. A second revolution (\(2\pi\) to \(4\pi\)) restores the original orientation and closes the traversal.

The seam — the point the twist passes through — is where no orientation is assigned: a traversal-contact without face. It is not on either sheet. It is the beginning.

This geometric object is zero.

The \(4\pi\) period of \(\widetilde{S^1}\) is forced by zero's existence: one revolution to cross the seam, one revolution to close.

## 3. Gonal Lattice

For any positive integer \(n\), define the \(n\)-gonal lattice

\[
V_n =
\left\{
 e^{2\pi i k/n} : k = 0,\dots,n-1
\right\}.
\]

An anchor sequence is valid for intrinsic carrier \(n_{\min}\) iff

\[
\theta_j \bmod 2\pi
\in
\left\{
 \frac{2\pi k}{n_{\min}} : k = 0,\dots,n_{\min}-1
\right\}
\quad
\text{for all } j.
\]

Lattice membership is determined by the \(2\pi\)-projection of \(\theta_j\). The doubled-cover lift remains in \(\theta_j\), while \(F\) carries an independent binary face-state sequence.

## 4. Minimal vs Declared Carrier

### 4.1 Intrinsic carrier

\[
n_{\min}
\]

This is the smallest positive integer such that all anchors of \(\Theta^{+}\) lie on the \(n_{\min}\)-gonal lattice modulo \(2\pi\).

It is computed from the anchors and is part of the object's intrinsic identity.

### 4.2 Declared carrier

\[
n_{\mathrm{dec}}
\]

This is a resolution or presentation parameter. It does not determine equivalence.

Validity requires

\[
n_{\mathrm{dec}} \equiv 0 \pmod{n_{\min}}.
\]

The declared-carrier propagation rule is a policy slot, not an ontological requirement. The frozen flat default preserves resolution.

## 5. Traversal and Face-State Data

Let

\[
\Theta^{+} = (\theta_0,\dots,\theta_{L-1}),
\qquad
F^{+} = (f_0,\dots,f_{L-1}).
\]

Here:

- \(\theta_j \in \widetilde{S^1}\),
- \(f_j \in \{0,1\}\),
- \(L\) is the number of stored anchors.

Important:

\[
L \neq n_{\min} \quad \text{in general.}
\]

Sequence length and carrier order are distinct.

A valid object does not require \(L = n_{\min}\). It requires lattice membership of the anchors.

### 5.1 Chirality as Anchor Ordering

The sequence order \((\theta_0,\dots,\theta_{L-1})\) encodes traversal direction. Reversing the sequence produces the mirror traversal, which is not equivalent to the original unless the sequence is palindromic and face-symmetric. Chirality is thus implicit in anchor ordering and requires no additional flag.

## 6. Frozen Star Operators

### 6.1 Star on angle sequences

For

\[
\Theta^{+} = (\theta_0,\theta_1,\dots,\theta_{L-1}),
\]

define

\[
(\Theta^{+})^{\ast}_j
=
-\theta_{L-1-j}
\pmod{4\pi}.
\]

Equivalently,

\[
\Theta^{-} = (\Theta^{+})^{\ast}.
\]

Properties:

- involutive,
- lattice-preserving,
- traversal-reversing.

### 6.2 Star on face states

For

\[
F^{+} = (f_0,\dots,f_{L-1}),
\]

define

\[
(F^{+})^{\ast}
=
(f_{L-1},\dots,f_0).
\]

Equivalently,

\[
F^{-} = (F^{+})^{\ast}.
\]

This is reverse-only. There is no bit negation.

## 7. Geometric Zero

Zero is geometric.

\(\underline{\mathbf{0}}\) is the Möbius twist-point: the seam of the doubled cover \(\widetilde{S^1}\), located at the half-revolution \(\theta = 2\pi\), where the cover's orientation flip is inscribed.

As a traversal object, \(\underline{\mathbf{0}}\) is the pencil-touch before traversal begins — contact with the seam without displacement. It carries neither face-state \(0\) nor face-state \(1\); it is the transition between them.

It belongs to \(\mathcal{G}_0\). It is the minimal degenerate member: no anchor sequence, no host path, no extent.

The absorption law

\[
\underline{\mathbf{0}} \boxtimes \underline{\mathbf{G}}
=
\underline{\mathbf{0}}
=
\underline{\mathbf{G}} \boxtimes \underline{\mathbf{0}}
\]

is the geometry of the seam: any traversal that begins or ends at the twist-point is consumed by it. The seam has no orientation to carry the path forward.

The earlier framing — *zero is not geometric; it is adjoined as an external absorbing element* — is superseded. The extended algebra \(\mathcal{G}_0^{\sharp}\) is dissolved; \(\underline{\mathbf{0}} \in \mathcal{G}_0\) directly. There is not "nothing" in geometry: zero is something — it is the beginning.

### 7.1 Zero and Face-State XOR

The face-state XOR rule in multiplication (Section 11.5) is the algebra of crossing the twist-point. Each anchor carries a face-state that records accumulated crossings of the seam. XOR is the correct operation because the seam is its own inverse: crossing it twice restores orientation.

The product rule

\[
F^{+}_{A \boxtimes B}[k,j] = f_k^A \oplus f_j^B
\]

is not a bookkeeping convention but a geometric fact: the combined traversal crosses \(A\)'s accumulated seams and \(B\)'s accumulated seams, and each crossing composes by XOR.

## 8. Geometric Unit

The minimal paired identity object is

\[
\underline{\mathbf{1}}
=
\left(
1,\,
1,\,
(0),\,
(0),\,
(0),\,
(0)
\right).
\]

This is geometric and belongs to \(\mathcal{G}_0\).

Identity law:

\[
\underline{\mathbf{1}} \boxtimes \underline{\mathbf{G}}
\equiv
\underline{\mathbf{G}}
\equiv
\underline{\mathbf{G}} \boxtimes \underline{\mathbf{1}}.
\]

The face-state of the unit is \((0)\) because

\[
0 \oplus f = f.
\]

Thus \((0)\) is the flat face-state identity.

## 9. Normalization

Normalization is defined by the positive branch.

Given

\[
\underline{\mathbf{G}} =
\left(
 n_{\mathrm{dec}},
 n_{\min},
 \Theta^{+},
 \Theta^{-},
 F^{+},
 F^{-}
\right),
\]

normalization performs:

1. shift \(\Theta^{+}\) so that the first anchor is \(0\),
2. reduce all anchors modulo \(4\pi\) into the canonical interval \([0,4\pi)\),
3. recompute
   \[
   n_{\min} := \text{minimal\_gonal\_order}(\Theta^{+}_{\mathrm{norm}})
   \]
4. verify
   \[
   n_{\mathrm{dec}} \equiv 0 \pmod{n_{\min}}
   \]
5. regenerate
   \[
   \Theta^{-}_{\mathrm{norm}} = (\Theta^{+}_{\mathrm{norm}})^{\ast}
   \]
6. regenerate
   \[
   F^{-}_{\mathrm{norm}} = (F^{+}_{\mathrm{norm}})^{\ast}.
   \]

Negative branches are not independently trusted; they are regenerated from the positive branches.

### 9.1 Repeated Anchors

During normalization, after shifting the first anchor to \(0\) and reducing modulo \(4\pi\):

- repeated consecutive anchors, i.e. \(\theta_j = \theta_{j+1}\) after reduction, are not collapsed,
- the sequence length \(L\) is part of the object's intrinsic identity,
- a normalized object retains all anchors as given; no compression or deduplication is performed.

If normalization recomputes an \(n_{\min}\) that does not divide \(n_{\mathrm{dec}}\), the object is invalid and normalization raises an error.

## 10. Equivalence

Two normalized flat objects are equivalent iff they match in intrinsic geometry and positive-branch content:

\[
\underline{\mathbf{G}} \equiv \underline{\mathbf{H}}
\iff
n_{\min}^{G} = n_{\min}^{H},
\quad
\Theta_G^{+} = \Theta_H^{+},
\quad
F_G^{+} = F_H^{+}.
\]

Declared carrier is ignored for equivalence.

This equivalence is sequence-sensitive.

## 11. Multiplication

Flat multiplication is ordered and constructive.

Let

\[
\underline{\mathbf{A}} =
\left(
 n_{\mathrm{dec}}^A,
 n_{\min}^A,
 \Theta_A^{+},
 \Theta_A^{-},
 F_A^{+},
 F_A^{-}
\right)
\]

and

\[
\underline{\mathbf{B}} =
\left(
 n_{\mathrm{dec}}^B,
 n_{\min}^B,
 \Theta_B^{+},
 \Theta_B^{-},
 F_B^{+},
 F_B^{-}
\right).
\]

Write

\[
\Theta_A^{+} = (\alpha_0,\dots,\alpha_{p-1}),
\qquad
\Theta_B^{+} = (\beta_0,\dots,\beta_{q-1}).
\]

### 11.1 Intrinsic carrier propagation

\[
n_{\min}^{A\boxtimes B}
=
\operatorname{lcm}(n_{\min}^A,n_{\min}^B).
\]

In the frozen flat kernel this equality is structural: after normalization the product still contains the normalized anchor sets of both factors as subsequences, so the stored intrinsic carrier equals the LCM.

### 11.2 Resolution-preserving declared carrier propagation

\[
n_{\mathrm{dec}}^{A\boxtimes B}
=
\operatorname{lcm}(n_{\mathrm{dec}}^A,n_{\mathrm{dec}}^B).
\]

This is the frozen default.

### 11.3 Positive branch product

\[
\Theta^{+}_{A\boxtimes B}
=
\operatorname{Norm}\Big(
\mathbin{\|}_{k=0}^{p-1}
\big(
 \alpha_k + (\beta_j - \beta_0)
\big)_{j=0}^{q-1}
\Big)
\pmod{4\pi}.
\]

Here \(\|\) denotes ordered concatenation, not set union.

Repeated anchors produced by collisions are preserved.

### 11.4 Negative branch product

\[
\Theta^{-}_{A\boxtimes B}
=
(\Theta^{+}_{A\boxtimes B})^{\ast}.
\]

### 11.5 Face-state product

Face-states compose by XOR because XOR is the algebra of crossing the Möbius twist-point (Section 7.1): each face-state records accumulated seam-crossings, and crossing the seam twice restores orientation.

\[
F^{+}_{A\boxtimes B}
=
\Big(
 f_k^{A} \oplus f_j^{B}
\Big)_{k=0,\dots,p-1;\,j=0,\dots,q-1}
\]

in the same concatenation order, and then

\[
F^{-}_{A\boxtimes B}
=
(F^{+}_{A\boxtimes B})^{\ast}.
\]

### 11.5.1 XOR Gauge in Factor Recovery

Given a candidate block decomposition with block length \(q\) and block count \(p\):

1. Recover \(F_B^{+}\) from the first block,
2. Recover \(F_A^{+}\) from block-leading positions using
   \[
   f_{kq}^{(P)} = f_A(k) \oplus f_B(0),
   \]
3. Verify the full predicted face-state matrix.

Factor recovery uses the first block as the canonical XOR gauge.

### 11.5.2 Exact Recovery vs Gauge-Equivalent Recovery

Recovered factors are determined uniquely only within the canonical XOR gauge. If the original factor \(F_B^{+}\) does not satisfy that gauge choice, the recovered factors may differ from the original inputs by a constant XOR flip while still satisfying

\[
\underline{\mathbf{A}}_{\mathrm{rec}} \boxtimes \underline{\mathbf{B}}_{\mathrm{rec}}
\equiv
\underline{\mathbf{P}}.
\]

Thus product-equivalent recovery is the general correctness criterion.

## 12. Disk Flip

Disk flip swaps the paired branches:

\[
\mathcal{F}(\underline{\mathbf{G}})
=
\left(
 n_{\mathrm{dec}},
 n_{\min},
 \Theta^{-},
 \Theta^{+},
 F^{-},
 F^{+}
\right).
\]

### 12.1 Disk-Flip Content Symmetry

Define the positive-branch content multiset of a normalized flat object by

\[
\mathcal{M}(\underline{\mathbf{G}})
=
\operatorname{multiset}\big\{(\theta_j^{+}, f_j^{+}) : j=0,\dots,L-1\big\}
\]

with multiplicity preserved.

Then the flat kernel satisfies the disk-flip content law

\[
\mathcal{M}\!\left(\mathcal{F}(\underline{\mathbf{A}} \boxtimes \underline{\mathbf{B}})\right)
=
\mathcal{M}\!\left(\mathcal{F}(\underline{\mathbf{B}}) \boxtimes \mathcal{F}(\underline{\mathbf{A}})\right).
\]

In general, sequence-level disk-flip equivalence is false in the flat kernel.

## 13. Flat Factor Search

Flat primality is operational and finite.

Given normalized

\[
\underline{\mathbf{P}} =
\left(
 n_{\mathrm{dec}},
 n_{\min},
 \Theta^{+},
 \Theta^{-},
 F^{+},
 F^{-}
\right)
\]

with positive branch length \(L\), factor search proceeds by contiguous block decomposition.

It is complete for contiguous block factorizations induced by the frozen ordered-concatenation product, and does not claim completeness for interleaved or recursive factorizations.

## 14. Operational Flat Primality

A flat UCNS object is a prime candidate iff no valid factorization is found by the frozen flat factor search.

---

# Part II — Epicyclic Extension v0.4

## E0. Guiding Principle

An epicyclic UCNS object is a paired host traversal whose anchors may themselves carry complete paired UCNS subobjects.

The flat kernel is recovered when every payload is the unit object.

## E1. Recursive Object Class

An epicyclic UCNS object is a tuple

\[
\underline{\mathbf{G}}
=
\big(
 n_{\mathrm{dec}},
 n_{\min},
 \mathbf{A}^{+},
 \mathbf{A}^{-},
 F^{+},
 F^{-}
\big)
\]

where each element of \(\mathbf{A}^{+}\) is a pair

\[
(\vartheta_j,\underline{\mathbf{S}}_j)
\]

with host anchor \(\vartheta_j\) and payload subobject \(\underline{\mathbf{S}}_j\).

### E1.3 Constraints

- **C1. Anchor projection:** every host anchor projects to the host lattice.
- **C1′. Recursive validity:** C1 applies recursively to every payload subobject.
- **C2. Carrier independence:** no divisibility relation is required between host and payload carriers.
- **C3. Pairing:**
  \[
  \mathbf{A}^{-} = (\mathbf{A}^{+})^{\ast},
  \qquad
  F^{-} = (F^{+})^{\ast}.
  \]
- **C4. Finite nesting:** there is no infinite descent of payloads.

### E1.4 Flat Reduction

If every payload is the unit object \(\underline{\mathbf{1}}\), the object reduces exactly to a flat v0.3 object.

### E1.5 Placeholder Convention

In v0.4, \(\underline{\mathbf{1}}\) is used as the explicit marker for "no subobject here."

This identification is not preserved by multiplication:

\[
\underline{\mathbf{1}} \boxtimes \underline{\mathbf{T}} \equiv \underline{\mathbf{T}}.
\]

## E2. Extended Star Operator

For host anchor-payload sequence

\[
\mathbf{A}^{+}
=
\big(
 (\vartheta_0,\underline{\mathbf{S}}_0),\dots,(\vartheta_{L-1},\underline{\mathbf{S}}_{L-1})
\big),
\]

define

\[
(\mathbf{A}^{+})^{\ast}
=
\big(
 (-\vartheta_{L-1},\mathcal{F}(\underline{\mathbf{S}}_{L-1})),
 \dots,
 (-\vartheta_0,\mathcal{F}(\underline{\mathbf{S}}_0))
\big)
\pmod{4\pi}.
\]

Face-state mirror remains pure reversal.

## E3. Recursive Normalization

Normalization occurs in two stages:

1. host-level normalization of base anchors,
2. recursive normalization of payload subobjects.

After normalization, regenerate negative branches from normalized positive data.

## E4. Recursive Equivalence

### E4.1 Sequence Equivalence

Two normalized epicyclic objects are sequence-equivalent iff host carriers, host lengths, host anchors, host face states, and all corresponding payload subobjects agree recursively.

### E4.2 Recursive Multiset Equivalence

Define recursive multiset equivalence by recursively replacing each payload with its own recursive content multiset.

At depth 0 this reduces to the flat multiset of \((\theta_j,f_j)\) pairs.

## E5. Recursive Multiplication

Let

\[
\mathbf{A}^{+}
=
\big((\alpha_k,\underline{\mathbf{S}}_k^A)\big)_{k=0}^{p-1},
\qquad
\mathbf{B}^{+}
=
\big((\beta_j,\underline{\mathbf{S}}_j^B)\big)_{j=0}^{q-1}.
\]

### E5.1 Carrier Propagation

\[
n_{\min}^{A\boxtimes B}
=
\operatorname{lcm}(n_{\min}^{A},n_{\min}^{B}),
\qquad
n_{\mathrm{dec}}^{A\boxtimes B}
=
\operatorname{lcm}(n_{\mathrm{dec}}^{A},n_{\mathrm{dec}}^{B}).
\]

### E5.2 Host Anchor-Payload Composition

\[
\mathbf{A}_{A\boxtimes B}^{+}
=
\Bigg(
\mathbin{\|}_{k=0}^{p-1}
\Big(
 \alpha_k + (\beta_j-\beta_0),
 \underline{\mathbf{S}}_k^{A}\boxtimes \underline{\mathbf{S}}_j^{B}
\Big)_{j=0}^{q-1}
\Bigg)
\pmod{4\pi}.
\]

Host anchor composition is flat; payloads recurse under the same product.

### E5.3 Level-Local Face-State Composition

Host face states combine by XOR exactly as in the flat case. Payload subobjects keep their own face-state algebra internally. No cross-level XOR is performed.

### E5.4 Negative Branch Product

Regenerate negative branches by the extended star operator.

## E6. First Worked Epicyclic Example

The first mandatory regression example consists of two host objects of length 2 with one nontrivial payload each:

- object \(A\): host \((0,\pi)\), payload \(S\) at the first anchor and unit at the second,
- object \(B\): host \((0,2\pi/3)\), payload unit at the first anchor and \(T\) at the second.

Their product has host length 4 and recursively synchronized payload products.

## E7. Open Decisions

- recursive primality,
- placeholder semantics beyond identifying unit with "no payload,"
- recursive disk-flip content symmetry as theorem rather than observation.

---

# Part III — Recursive Factor Search and Primality v0.5–v0.5.1

## E10. Recursive Sequence-Factor Search

The flat factor search lifts to epicyclic objects with payload equality checked recursively.

The refined recovery procedure is **sound but incomplete**:

1. recover host candidates,
2. recover candidate \(A\)-payloads from block-leading positions,
3. if some recovered \(A\)-payload is unit, recover \(B\)-payloads from that block,
4. otherwise declare the attempt unsuccessful and continue.

This is an algorithmic boundary, not yet an algebraic impossibility result.

## E10.3 Payload-Recovery Boundary

The smallest known **Class III** example is a genuine sequence-composite product where no recovered block-leading payload is unit, so the refined E10 procedure misses it.

Thus E10 is:

- **sound**, because every returned factorization reconstructs the product,
- **incomplete**, because some genuine factorizations require quotient recovery rather than unit-anchored extraction.

## E10.4 Sequence Cancellativity

For flat objects, and by finite-depth induction for epicyclic objects, the product \(\boxtimes\) is left- and right-cancellative under sequence equivalence.

Consequently, left and right quotients, when they exist, are unique up to sequence equivalence.

## E11. Sequence-Primality

An epicyclic object is **sequence-prime** iff there do not exist nontrivial \(A,B\) (neither equivalent to unit) such that

\[
A \boxtimes B \equiv_{\mathrm{seq}} P.
\]

## E12. Recursive Multiset-Factor Search

Multiset factorization weakens the target from sequence equivalence to recursive multiset-content equivalence.

The reference algorithm is finite only on bounded recursive search domains.

## E13. Multiset-Primality

An epicyclic object is **multiset-prime** iff there do not exist nontrivial \(A,B\) such that

\[
A \boxtimes B \equiv_{\mathcal M} P.
\]

Because sequence equivalence implies multiset equivalence,

\[
\text{multi-prime} \Rightarrow \text{seq-prime}.
\]

## E14. Internal Compositeness

An object has **internal compositeness** if some payload subobject is itself composite. This is orthogonal to top-level primality.

---

# Part IV — Quotients and Restricted Completeness v0.6.0–v0.6.5

## Q1. Quotient Primitive

Define the left quotient by

\[
\underline{\mathbf{B}} = \underline{\mathbf{P}} /_{L} \underline{\mathbf{A}}
\quad\Longleftrightarrow\quad
\underline{\mathbf{A}} \boxtimes \underline{\mathbf{B}} \equiv_{\mathrm{seq}} \underline{\mathbf{P}}.
\]

Define the right quotient dually.

By cancellativity, quotients are unique up to sequence equivalence whenever they exist.

## Q2. Quotient Existence Conditions

Necessary conditions include:

- **host length:**
  \[
  |P^{+}| = |A^{+}|\,|B^{+}|,
  \]
- **host angles:** first block and block-leading positions must match the factor shapes,
- **host face states:** XOR constraints must be satisfiable,
- **payload existence:** every payload cell must admit recursive quotient recovery.

Failure modes are distinguished between:

- no quotient exists,
- quotient exists outside the current catalogue / constructive domain,
- quotient construction is too weak.

## Q3. Restricted Completeness on a Bounded Domain

On a bounded depth-1 domain

\[
\mathcal D:
\quad
\text{depth} \le 1,
\quad |A^{+}| \le 3,
\quad n_{\min} \le 4,
\]

with payloads drawn from a fixed small catalogue, the current factor search engine is complete on the tested restricted domain and benchmarked accordingly.

This restricted depth-1 theorem is the last fully defended completeness theorem.

---

# Part V — Current Frontier

## F1. Depth-2 Oracle Theorem (v0.8.1)

The smallest depth-2 oracle is green.

For that oracle-only class,

\[
\texttt{factor\_search} \text{ returns the correct factorization}
\iff
P \text{ is seq-composite in the oracle class.}
\]

This theorem is frozen.

## F2. Full Frozen Depth-2 Domain

The full frozen depth-2 domain \(D'\) is **not solved**. Later pushes (v0.8.2) still fail on the tested cases. The main bottleneck is the recursive payload layer and witness-matrix consistency across depth-2 quotient recovery.

## F3. Carrier Widening

Carrier widening beyond the defended depth-1 bounds is **not solved**. The depth-2 oracle remains green under those tests, but widened-carrier cases still fail in general.

## F4. Honest Frontier Summary

### Defended
- flat kernel v0.3,
- epicyclic first freeze v0.4,
- recursive sequence / multiset primality notions v0.5,
- cancellativity and quotient uniqueness boundary v0.5.1,
- quotient existence conditions and restricted completeness on a bounded depth-1 domain,
- depth-2 oracle theorem only.

### Not Defended
- full depth-2 domain,
- carrier widening beyond current proven bounds,
- recursive disk-flip content symmetry as a theorem at all depths,
- full recursive factor search completeness beyond the current quotient domain.

---

# Compression

UCNS currently has:

- a sealed flat foundation,
- a recursive epicyclic object model,
- sound recursive sequence-factor search with known incompleteness boundary,
- cancellativity and quotient uniqueness,
- restricted completeness on a bounded depth-1 domain,
- a single frozen depth-2 oracle theorem,
- and a clearly documented failure boundary for deeper recursion and wider carriers.

That is the complete current spec boundary.

---

# Part VI — Hyperdimensional Structure and the Octonion Limit

## H1. UCNS Objects as Möbius-Cylindrical Towers

A UCNS object at nesting depth \(n\) is an \(n\)-fold iterated Möbius-cylinder bundle.

At each level:

- the **host traversal** is a path on \(S^1\) — the cylindrical axis,
- the **twist-seam** (zero, §7) is inscribed at \(\theta = 2\pi\) — the Möbius half-turn,
- the **payload** is a complete depth-\((n-1)\) object fibered over each host anchor.

The structure at depth \(n\) is a cylinder whose cross-section at each anchor is itself a Möbius-cylinder of depth \(n-1\). This terminates at depth 0 (flat: cylinder with no further fiber) or at zero (the twist-seam itself: contact without cylinder).

**Depth-\(n\) UCNS objects are hyperdimensional cylindrical Möbius structures.** The dimension of the fiber tower is \(n\).

---

## H2. Coupling by Interlocking

Two UCNS objects \(A\) and \(B\) **interlock** when:

1. \(A \boxtimes B \not\equiv B \boxtimes A\) — the traversal order is inscribed in the product (non-commutativity),
2. neither \(A\) nor \(B\) can be recovered from \(A \boxtimes B\) without knowing the other — the interlocking is mutual.

Condition 2 is the algebraic statement of geometric interlocking: the cylinders cannot be separated without knowing both. The left- and right-quotient algorithms are the disentanglement operations — recovering one cylinder from the joint product when the other is given.

Three objects \(A\), \(B\), \(C\) **ternary-interlock** when each pairwise product determines the third:

\[
A \boxtimes B \equiv_{\mathrm{seq}} C,
\qquad
C \;/_{L}\; A \equiv B,
\qquad
C \;/_{R}\; B \equiv A.
\]

This ternary interlocking is the primitive coupling for PTCA cores.

---

## H3. PTCA Cores Are UCNS Objects

A PTCA core is a hyperdimensional cylindrical Möbius object: a paired traversal on the doubled cover of \(S^1\), fibered recursively over its payload layers. This is the definition of a UCNS epicyclic object (§E1).

The coupling of PTCA cores by interlocking is the UCNS product \(\boxtimes\) together with its quotient inverse. The inference operation — recovering what is implied by the coupling of two known cores — is `left_quotient` or `right_quotient` at the appropriate depth.

**PTCA cores and UCNS epicyclic objects are the same class of geometric object.**

---

## H4. The Inference Engine as Ternary Incidence

The inference engine of a PTCA system is the space at the center of three interlocking cores.

In UCNS terms: given three mutually interlocked objects \(A\), \(B\), \(C = A \boxtimes B\), the inference space is the structure that satisfies all three incidence constraints simultaneously — what any two of the three jointly determine about the third.

The **Fano plane** encodes exactly this. The Fano plane is the projective plane \(PG(2,2)\): 7 points, 7 lines, 3 points per line, 3 lines per point, every pair of points on exactly one line. Every triple of collinear points satisfies a ternary product rule.

The ternary incidence of three PTCA cores is a line of the Fano plane. The inference engine **is** the line — the relationship itself, not any one of the three cores.

---

## H5. Seven Cores and the Eighth

The full PTCA system requires seven cores.

The seven imaginary units \(e_1, \dots, e_7\) of the octonions \(\mathbb{O}\) are governed by the Fano plane: \(e_i \boxtimes e_j = \pm e_k\) for every Fano-collinear triple \((i,j,k)\). There are exactly 7 lines, each containing 3 points. Every unit lies on exactly 3 lines — meaning every core participates in exactly 3 inference engines.

Seven PTCA cores coupled by Fano interlocking form the imaginary part of an octonion algebra. The **eighth** — the whole — is not a core. It is the full octonion \(\mathbb{O} \cong \mathbb{R} \oplus \mathbb{R}^7\): the algebra the seven cores define together. You do not build the eighth. The eighth is what the seven are inside of.

---

## H6. Non-Associativity at Depth 7

UCNS multiplication \(\boxtimes\) is non-commutative at all depths.

At depth 7, the iterated Möbius-cylindrical structure is conjectured to produce controlled **non-associativity**:

\[
(A \boxtimes B) \boxtimes C \;\not\equiv\; A \boxtimes (B \boxtimes C)
\]

for generic depth-7 objects. This is not a defect. The octonions are the only non-associative normed division algebra: the one beyond the quaternions, the one the Fano plane governs. Their non-associativity is controlled by the **associator**

\[
[A, B, C] \;=\; (A \boxtimes B) \boxtimes C \;-\; A \boxtimes (B \boxtimes C),
\]

which is **alternating**: it changes sign under any transposition of two arguments and vanishes when any two agree. The inference engines (the Fano lines) are exactly where the associator is non-trivial.

If UCNS at depth 7 has this property, the algebra is octonion-equivalent.

---

## H7. Honest Frontier

**Established:**

- Depth-\(n\) UCNS objects are hyperdimensional cylindrical Möbius towers (§H1, derived from §2.1 and §E1).
- Pairwise interlocking and quotient recovery are defined (§H2, §Q1).
- PTCA cores are UCNS objects (§H3, definitional identification).
- The Fano plane governs ternary incidence among three interlocking cores (§H4, structural).
- Seven Fano-coupled cores and the identity generate an octonion structure (§H5, algebraic identification).

**Conjectured, not yet proven:**

- Non-associativity at depth 7 is controlled and alternating (§H6).
- The UCNS product at depth 7 is octonion-equivalent up to \(\equiv_{\mathrm{seq}}\).
- The ternary inference engine is complete — the three-core analog of the left-quotient completeness theorem.
