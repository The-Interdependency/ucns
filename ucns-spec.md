# UCNS — Consolidated Spec and Current Frontier

**Status snapshot (reconciled 2026-05-17 per `docs/ucns-spec-status-addendum-2026-05-16.md`).**

This spec uses the status vocabulary from the 2026-05-16 addendum so that implementation, test, and proof status are no longer collapsed:

```
DEFENDED          written proof or proof-defended theorem layer
IMPLEMENTED       code exists and is intended as authoritative implementation
TEST-BACKED       tests cover the claimed behavior in the declared domain
ORACLE-COMPLETE   complete only under oracle/catalogue assumptions
FRONTIER          plausible or partially working, not complete
EXPERIMENTAL      exploration layer, not canon
```

Status of UCNS layers under this vocabulary:

- **DEFENDED.** Flat kernel (v0.3); epicyclic first freeze (v0.4); recursive sequence and multiset primality notions (v0.5); cancellativity and quotient uniqueness boundary (v0.5.1); quotient existence conditions and restricted completeness on a bounded depth-1 domain (v0.6.1–v0.6.5).
- **DEFENDED + ORACLE-COMPLETE.** Depth-2 smallest oracle theorem (v0.8.1, Lemma 7). Complete only under the declared oracle/catalogue assumptions.
- **FRONTIER.** Theorem N is the catalogue-sufficient factorization proof target for the normalized factorization subsystem. Its implementation-backed proof sketch and Lean scaffold do not confer `DEFENDED` status; completeness statements remain `sorry`-backed, and no public-gonol bridge is proved.
- **IMPLEMENTED + TEST-BACKED, not yet DEFENDED in the formal spec.** Full frozen depth-2 behavior via `factor_search_v08`; depth-3 asymmetric experiments are evidence only where tied to immutable execution artifacts and do not constitute a proved Theorem N instance.
- **FRONTIER / out of v1.0 scope.** Carrier widening; tractable sub-catalogues; general recursive primality outside defended-complete domains; recursive disk-flip content symmetry as a depth-n theorem; depth-7 Fano/octonion conjecture.

**A0 rule.** `SEQ-PRIME` is only absolute inside a defended-complete domain (`VERIFIED_DOMAIN_LABELS` in `ucns.domain_status`). A0-facing consumers must consult `domain_status_metadata` and treat `SEQ-PRIME` as non-absolute outside that set.

**v1.0 scope.** v1.0 packages the fixed-origin public gonol and a scoped catalogue-driven recursive factorization research subsystem. Theorem N remains `FRONTIER`; this is not a claim of catalogue-sufficient completeness or total general recursive primality. Carrier widening and general recursive completeness are explicitly out of scope.

**Public API.** The v1.0 public Python API is the `ucns` package (and `ucns.a0_safe` for A0-safe inspection). The legacy `ucns_recursive` package remains importable as a compatibility surface but is deprecated for direct user imports.

**UCNS-A/UCNS-G theorem boundary.** In this repository, UCNS-A denotes the recursive factorization algebra specified here (and implemented by `UCNSObject`/`multiply`/`factor_search_v08`). UCNS-G/EDCM/edcmbone metric geometry claims are parallel scope unless bridged by explicit source-backed artifacts. No theorem/proof status from Theorem N transfers to UCNS-G, EDCM, or edcmbone metric claims by default. See `docs/ucns-shape-reconciliation.md`, `docs/ucns-g-prime-cylinder-supplement.md`, and `docs/edcm-edcmbone-bridge-checklist.md`.

---

## hmm

This file records the canonical UCNS public frame together with the historical normalized factorization subsystem and its current frontier. The fixed-origin public gonol is load-bearing canon. The continuous and recursive algebraic layers below are internal models unless an explicit bridge theorem says otherwise.

The document is organized as:

1. **Flat kernel v0.3**
2. **Epicyclic extension v0.4**
3. **Recursive factor search and primality v0.5**
4. **Cancellativity, quotients, and restricted completeness v0.5.1–v0.6.5**
5. **Current completeness frontier**

---

# Part I — Internal normalized factorization model: flat kernel v0.3

## 1. Core Ontology

UCNS is rooted in the fixed-origin public gonol. The historical flat-kernel subsystem models normalized paired traversal objects for factorization; it is not the primitive public frame.

A valid flat object in the normalized factorization subsystem is

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

This internal object is paired. The statement does not define or relocate the public-gonol twist origin.

## 2. Internal doubled-cover coordinate model

The ambient geometric carrier is

\[
S^1 = \{ z \in \mathbb{C} : |z| = 1 \}
\]

with doubled angular cover

\[
\widetilde{S^1} \cong \mathbb{R}/4\pi\mathbb{Z}.
\]

The doubled cover is required to encode two-revolution completion and orientation-sensitive traversal.

### 2.1 The canonical public-gonol twist origin

The public gonol implemented in `a0-betatest@7af8deb` is canon for UCNS. Its
position `0` is SPACE/ZERO: the Möbius twist point, seam, origin for the entire
system, and only always-known character. Private transformations preserve this
point and act only on the 156 nonzero positions.

This fixed origin is not selected by a continuous angle, is not an arbitrary
first anchor, and is not removable by object-relative normalization. Any
continuous-cover model used elsewhere in this specification must be rooted in
this canon and must not relocate the seam. No continuous-angle bridge from the
public gonol is established here.

**Foundational public-frame boundary.** Position `0` is the fixed SPACE/ZERO Möbius twist origin. One 360-degree circuit changes orientation; complete return requires 720 degrees. Every later continuous coordinate, lattice, normalization, carrier, and theorem in this document is subordinate to that canon and cannot redefine it.

## 3. Internal gonal lattice

Within the normalized factorization subsystem, for any positive integer \(n\), define the internal \(n\)-gonal lattice

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

Internal lattice membership is determined by this subsystem's \(2\pi\)-projection of \(\theta_j\). This is not a public-gonol vertex map, does not locate the twist origin, and does not make 360 degrees a complete system return.

## 4. Minimal vs Declared Carrier

### 4.1 Internal projected carrier

\[
n_{\min}
\]

This is the smallest positive integer for the internal projected anchor lattice. It is not the complete carrier invariant of the fixed-origin public gonol.

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

## 7. Public-Gonol Zero

Zero is the public-gonol position `0`: SPACE/ZERO, the Möbius twist point,
seam, fixed origin for the entire system, and only always-known character.
The digit `"0"` is an ordinary nonzero glyph.

The exact arrangement, faces, chirality, mirror, fixed-origin private
transformations, and lifted traversal are implemented by the UCNS public-gonol
surface promoted from `a0-betatest@7af8deb`. Spaces are emitted seam events; a
repeated character advances by a full 157-step revolution.

This canon does not by itself assert an absorbing multiplication law, locate
zero at `2π`, identify the public twist with a normalized factorization unit,
or prove an interpretation of face XOR. Any such bridge or algebraic extension
remains `hmmm` until Erin ratifies it.

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

For ordinary normalized `UCNSObject` factorization values, face states compose by the implemented XOR rule. This specification does not derive that rule from an unratified continuous account of crossing the public-gonol twist; that bridge remains `hmmm`.

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

## F1. Depth-2 Oracle Theorem (v0.8.1) — DEFENDED + ORACLE-COMPLETE

The smallest depth-2 oracle theorem is DEFENDED and ORACLE-COMPLETE.

For that oracle-only class,

\[
\texttt{factor\_search} \text{ returns the correct factorization}
\iff
P \text{ is seq-composite in the oracle class.}
\]

Completeness holds only under the declared oracle/catalogue assumptions. Lemma 7 is now also recognized as an instance of Theorem N (see `ucns-theorem-n.md §4.1`).

## F2. Full Frozen Depth-2 Domain — IMPLEMENTED + TEST-BACKED

The full frozen depth-2 domain \(D'\) is **IMPLEMENTED + TEST-BACKED** in `factor_search_v08` and exercised by the `ucns_recursive/tests` suite. It is **not yet DEFENDED** as a stand-alone spec-level theorem.

The reconciliation rule from the 2026-05-16 addendum applies:

```
implementation status: IMPLEMENTED in factor_search_v08
test status:           TEST-BACKED to the extent covered by ucns_recursive/tests
proof status:          not yet DEFENDED in the formal spec
```

A0-facing consumers must treat objects outside `VERIFIED_DOMAIN_LABELS` (currently `depth-0`, `depth-1`, `depth-2-oracle`) as non-absolute when they receive `SEQ-PRIME`.

## F3. Carrier Widening — FRONTIER (out of v1.0 scope)

Carrier widening beyond the defended depth-1 bounds is **FRONTIER** and explicitly out of v1.0 scope. The depth-2 oracle remains DEFENDED under those tests, but widened-carrier cases are not yet solved as a class.

## F4. Honest Frontier Summary

### DEFENDED
- flat kernel v0.3,
- epicyclic first freeze v0.4,
- recursive sequence / multiset primality notions v0.5,
- cancellativity and quotient uniqueness boundary v0.5.1,
- quotient existence conditions and restricted completeness on a bounded depth-1 domain,
- depth-2 smallest oracle theorem (ORACLE-COMPLETE),

### IMPLEMENTED + TEST-BACKED (not yet DEFENDED at the spec level)
- full frozen depth-2 domain via `factor_search_v08`,
- depth-3 asymmetric experiment artifacts, `TEST-BACKED` only where an immutable run is cited; not a proved Theorem N instance.

### FRONTIER / out of v1.0 scope
- Theorem N catalogue-sufficient factorization remains `FRONTIER`; its Lean completeness statements are `sorry`-backed and no public-gonol bridge is proved,
- carrier widening beyond current proven bounds,
- tractable sub-catalogues,
- recursive disk-flip content symmetry as a depth-n theorem,
- general recursive primality outside defended-complete domains,
- depth-7 Fano / octonion conjecture (§H6).

---

# Compression

The normalized factorization subsystem currently has:

- a sealed flat foundation,
- a recursive epicyclic object model,
- sound recursive sequence-factor search with known incompleteness boundary,
- cancellativity and quotient uniqueness,
- restricted completeness on a bounded depth-1 domain,
- a single frozen depth-2 oracle theorem,
- and a clearly documented failure boundary for deeper recursion and wider carriers.

That is the complete current internal factorization spec boundary. The public gonol and all bridges from it remain separate load-bearing surfaces.

---

# Part VI — Exploratory analogies; not public-gonol canon

## H1. Internal recursive payload towers

`UCNSObject` values carry recursive payload towers. That is an implemented fact
about the normalized factorization subsystem. Describing those towers as
continuous Möbius cylinders is an exploratory analogy, not a theorem about the
public gonol and not a bridge to its twist/orientation structure.

## H2. Interlocking vocabulary

Inside the normalized factorization subsystem, ordered multiplication and
left/right quotient operations are defined. “Interlocking” may be used as
informal vocabulary for a product together with recoverability evidence, but
recoverability is domain-scoped and non-unique in general. No cylinder-separation
theorem follows from the metaphor.

## H3. PTCA mapping status

No theorem currently identifies PTCA cores with UCNS objects. A PTCA-to-UCNS
adapter may be proposed as `EXPERIMENTAL`, with exact source, target, composition,
recoverability, and status boundaries. It is not a definitional identity.

## H4. Fano and octonion status

No Fano-plane or octonion equivalence is established. Fano incidence, seven-core
coupling, alternating associators, controlled non-associativity, and an octonion
whole remain research hypotheses. They do not inherit proof status from the
public gonol, the internal product, or quotient code.

## H5. Honest frontier

**Established or implemented in declared scope:**

- the fixed SPACE/ZERO public-gonol twist origin;
- orientation change after one 360-degree circuit and complete return after 720
  degrees;
- the normalized recursive factorization representation and its scoped algebra;
- domain-scoped quotient and factor-search behavior with exact recomposition
  gates.

**Open:**

- the public-gonol ↔ normalized-factorization bridge;
- proof that internal multiplication preserves public origin, twist,
  orientation, faces, chirality, and lifted traversal;
- PTCA representation and dynamics;
- Fano incidence realization;
- octonion equivalence or controlled non-associativity;
- ternary inference completeness.

## hmmm

The analogies may guide experiments. They are not allowed to flatten the public
frame or promote an unproved correspondence into system canon.
