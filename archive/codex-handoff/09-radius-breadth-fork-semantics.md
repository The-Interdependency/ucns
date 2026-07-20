# UCNS radius, breadth, fork observables, and semantic enforcement

## Assignment

Complete this work as the geometry-and-semantics sibling of [`08-idempotents-local-groups-2i-no-go.md`](./08-idempotents-local-groups-2i-no-go.md).

This package has four purposes:

1. correct the geometry vocabulary so recursive depth is radius and log-length is breadth;
2. prove the max/plus composition laws for those two coordinates;
3. state the zero-breadth spindle consequence of the local-group package;
4. keep fork structure as a derived observable while placing fork admissibility in the METAPAT-to-UCNS encoding policy and integration lint, where the semantic rule can actually be enforced.

Do not implement the quaternionic lift, METAPAT encoding selection, fiq metering, 600-cell coordinates, EDCM measurements, or full-field experiments in this patch.

---

# I. Coordinate correction

## Radius

Use recursive payload depth as radius:

```text
rho(None) = 0
rho(U) = 1 + max(rho(P_i))
```

where the maximum ranges over the payloads of the cells of `U`, with `None` contributing depth zero.

This is the existing `ucns.domains.depth_of` law. Cite the owning implementation and specification surfaces directly.

## Breadth

Rename the existing geometry-bridge coordinate:

```text
lambda(U) = log(len(U.A_plus)).
```

The old bridge name `r` or `log-depth` is incorrect. It measures top-level sequence breadth, not recursive depth.

The implementation and documentation may retain a compatibility alias temporarily, but all public mathematical prose must distinguish:

```text
rho     recursive radius / payload depth
lambda  breadth valuation / log top-level length
```

Do not silently change serialized schemas or public field names without an explicit compatibility plan.

## Corrected commutative projection

The corrected projection is at least:

```text
(rho, lambda, theta, z, w).
```

This correction removes a false geometric claim. It does not add quaternionic axis information and does not advance H5C by itself.

Add an explicit bridge note:

> The enriched `(rho, lambda, theta, z, w)` target remains commutative and remains a projection of any future nonabelian quaternionic lift. Separating radius from breadth repairs the coordinate semantics; it does not recover the commutator or supply `SU(2)` axis data.

---

# II. The radius max law

## Theorem R

For all finite-depth UCNS carrier objects `A` and `B`:

```text
rho(A box B) = max(rho(A), rho(B)).
```

Use `None` as depth zero where the public multiplication surface admits the unit sentinel.

## Required proof

Proceed by induction on:

```text
max(rho(A), rho(B)).
```

A product cell carries payload:

```text
P_i tensor Q_j.
```

Use the complete payload table:

```text
None tensor None = None
None tensor Q    = Q
P tensor None    = P
P tensor Q       = P box Q      when P,Q are non-None objects.
```

Then establish cellwise:

```text
rho(P_i tensor Q_j) = max(rho(P_i), rho(Q_j)).
```

The nontrivial fourth case follows by the induction hypothesis.

Taking the maximum over all product cells gives:

```text
max_(i,j) max(rho(P_i), rho(Q_j))
  = max(max_i rho(P_i), max_j rho(Q_j)).
```

Adding the outer object layer yields:

```text
rho(A box B) = max(rho(A), rho(B)).
```

Normalization changes angles and recursively normalizes payload representations; it does not add or remove payload levels. Cite this depth-blindness directly rather than assuming it.

## Target algebra

Record the homomorphism:

```text
rho : (N, box) -> (Z_ge_0, max, 0).
```

The target is a commutative idempotent monoid.

Required identities:

```text
max(a,b) = max(b,a)
max(max(a,b),c) = max(a,max(b,c))
max(a,a) = a
max(a,0) = a.
```

Do not conflate idempotence of the target operation with idempotence of arbitrary UCNS objects.

---

# III. The breadth plus law

## Theorem L

For all nonempty carrier objects `A` and `B`:

```text
lambda(A box B) = lambda(A) + lambda(B).
```

## Required proof

The ordered product emits exactly:

```text
len(A) * len(B)
```

cells, and normalization deletes no cells. Therefore:

```text
lambda(A box B)
  = log(len(A box B))
  = log(len(A) * len(B))
  = log(len(A)) + log(len(B))
  = lambda(A) + lambda(B).
```

Record the target as:

```text
lambda : (N, box) -> (R_ge_0, +, 0).
```

This is the existing valid bridge invariant under its corrected name.

---

# IV. Zero-breadth spindle theorem

## Definition

Define the zero-breadth spindle:

```text
S_0 = { U in N : lambda(U) = 0 }.
```

Because carrier objects are nonempty:

```text
lambda(U) = 0  iff  len(U.A_plus) = 1.
```

## Theorem S

Every internal UCNS subgroup lies entirely in the zero-breadth spindle:

```text
H <= (N, box)  implies  H subset S_0.
```

## Required proof

Let `E` be the internal identity of `H`, and let `X` have local inverse `Y` in `H`.

From:

```text
X box Y = E
```

and the idempotent/local-group package, `E` has length one. Length grading gives:

```text
len(X) * len(Y) = 1.
```

Hence:

```text
len(X) = len(Y) = 1
```

and therefore:

```text
lambda(X) = lambda(Y) = 0.
```

Conclude that every local group and every internal subgroup is confined to `S_0`.

## Noncommutativity boundary

State the geometric consequence carefully:

> Internal group structure is confined to zero breadth. UCNS noncommutativity requires ordered multi-cell sequence structure and therefore requires positive breadth.

Use:

```text
lambda(U) > 0  iff  len(U.A_plus) >= 2.
```

Do not claim that every positive-breadth pair fails to commute. The correct statement is that the carrier's noncommutative witnesses require positive breadth; zero-breadth products are recursively singleton and commute within their local groups.

## Relation to the binary-icosahedral no-go

Add the picture to the `2I` theorem package:

```text
all internal groups live on lambda = 0
2I is nonabelian and perfect
therefore 2I cannot live internally in UCNS
```

The positive sphere program remains an external action:

```text
rho_action : 2I -> Aut(D).
```

Use a name such as `rho_action` in prose or code contexts where the symbol `rho` would collide with recursive radius.

---

# V. Fork profile as a derived observable

## First-level payload count

Define:

```text
b_1(U) = number of top-level cells of U whose payload is non-None.
```

Let:

```text
m_A = len(A)
m_B = len(B)
b_A = b_1(A)
b_B = b_1(B).
```

A product cell lacks a payload only when both source cells lack payloads. Therefore:

```text
b_1(A box B)
  = m_A*m_B - (m_A-b_A)*(m_B-b_B)
  = b_A*m_B + b_B*m_A - b_A*b_B.
```

This is an inclusion-exclusion law.

## Fork profile

A deeper fork profile may be defined as a derived observable:

```text
B(U) = (b_1(U), b_2(U), ..., b_rho(U))
```

where each `b_d` is defined by a pinned traversal/counting convention over payload-bearing branches at recursive radius `d`.

Before implementing `B`, the patch must specify:

- whether repeated structurally equal payloads count separately;
- whether counts are per cell, per distinct payload identity, or per path;
- how shared/cyclic payloads would be handled if later admitted;
- whether the profile records total nodes, payload-bearing nodes, or branching excess;
- how the profile treats `None` leaves.

## Status rule

Ship `B` as a derived observable, not as a primitive geometry-bridge coordinate.

Reason:

- its composition is nonlinear;
- the full profile law has not yet been proved and pinned;
- appending it to a tuple does not automatically produce a homomorphism into a product of simple monoids.

The bridge documentation may mention `B` as an optional diagnostic surface, but must not claim that:

```text
(rho, lambda, theta, z, w, B)
```

is a homomorphic product-coordinate system without a proved target operation for `B`.

---

# VI. Hyper-tensor layer definition

This handoff resolves research question R3 provisionally at the semantic boundary:

> A true hyper-tensor layer is a UCNS payload fork representing simultaneous constitutive components of one parent simplex or tensor state.

This definition has two parts:

## Structural part owned by UCNS

UCNS can represent:

- one parent object;
- multiple payload-bearing cells;
- recursive radii;
- ordered branches;
- exact face and carrier state.

UCNS can calculate depth, breadth, and fork observables.

## Semantic part not owned by UCNS

UCNS cannot determine from algebra alone whether children are:

- simultaneous constitutive components;
- temporal successors;
- adjacent independent objects;
- alternatives;
- provenance references;
- symmetry images;
- merely associated records.

Therefore the rule:

> Fork only for simultaneous constitutive components.

is not a `UCNSObject` constructor invariant.

It belongs to the METAPAT-to-UCNS encoding policy `Phi` and to an integration-repository validator.

---

# VII. Phi encoding-policy enforcement

Add the following required Stage 3 exit criterion to the future integration research plan.

## Fork admissibility criterion

A candidate encoding fails if it represents any of the following as UCNS payload containment without an explicit METAPAT rule declaring constitutive simultaneity:

- sequence or temporal succession;
- sphere adjacency;
- fiq gate connectivity;
- provenance or citation;
- alternatives or dissenting interpretations;
- external symmetry action;
- arbitrary graph association;
- references between independently existing modules.

A candidate may use payload forks only when the METAPAT module envelope or encoding declaration states that all children are simultaneous constitutive components of the parent.

## Required encoding declaration

Every encoded fork must carry or reference a deterministic declaration containing at least:

```text
parent module identity
child module identities in order
relation kind = constitutive-simultaneous
source METAPAT statement references
encoding-policy version
canon digest
unresolved hmmm fields
```

The declaration is semantic provenance. It must not be inferred from the existence of a UCNS payload.

## Negative fixtures

Stage 3 must include encodings that incorrectly route:

- a temporal sequence;
- an adjacency edge;
- a provenance link;
- an external `2I` action;

into payload forks.

The Phi policy validator must reject all of them.

---

# VIII. Integration-repository lint contract

The future integration repository must implement a lint or schema-validation surface before full-field experiments.

For every payload fork, validate:

1. a `constitutive-simultaneous` declaration exists;
2. the declaration is bound to the exact METAPAT canon and encoding-policy version;
3. all child identities match the actual UCNS payload children and order;
4. no external edge identifier is being retyped as containment;
5. adjacency, provenance, time, fiq motion, and group actions remain on their external relation surfaces;
6. unresolved semantics remain marked rather than defaulted to containment.

A failed fork lint invalidates the encoded fixture. It is not a warning.

The lint belongs downstream because only the integration layer can inspect both:

- METAPAT semantic authority;
- UCNS structural representation.

Do not add a misleading semantic boolean to the core UCNS constructor.

---

# IX. Executable contracts

Add or extend focused contracts for the following.

## Contract R1 — Depth max law

Across bounded mixed-depth fixtures, assert:

```text
rho(A box B) == max(rho(A), rho(B)).
```

Include all payload-table branches.

Mutation witness:

- a payload merge that wraps `P box Q` in an additional object and increments depth;
- a merge that drops the deeper payload;
- normalization that accidentally adds or removes a payload layer.

## Contract L1 — Breadth plus law

Assert:

```text
lambda(A box B) == lambda(A) + lambda(B)
```

for bounded nonempty fixtures.

Retain existing length-grading contracts and update terminology rather than duplicating unsupported execution counts.

## Contract S1 — Zero-breadth spindle

For bounded generated local-group elements:

```text
lambda(X) == 0.
```

Also include:

- a known positive-breadth noncommuting witness;
- the depth-two ghost, which has zero breadth but belongs to different local homes depending on the idempotent tested.

## Contract B1 — First-level fork law

For bounded fixtures, assert the exact inclusion-exclusion formula:

```text
b_1(A box B)
  = len(A)*len(B)
    - (len(A)-b_1(A))*(len(B)-b_1(B)).
```

Include edge cases:

- no payloads in either operand;
- payloads in only one operand;
- all cells payload-bearing;
- mixed payload-bearing cells.

Do not present this bounded contract as proof of an unpinned full-profile law.

## Contract B2 — Derived-observable boundary

Add a documentation or schema guard that prevents `B` from being advertised as a primitive homomorphic bridge coordinate unless a target composition law and proof status are supplied.

---

# X. Documentation and claims-ledger changes

## Geometry bridge

Correct `r = log(len)` naming to breadth valuation `lambda` in mathematical prose.

Add recursive radius `rho` from `depth_of`.

Preserve compatibility deliberately if public code fields cannot be renamed immediately.

State explicitly that the corrected commutative tuple does not solve the quaternionic lift.

## Base geometry

Add the max/plus pair:

```text
rho(A box B)    = max(rho(A), rho(B))
lambda(A box B) = lambda(A) + lambda(B).
```

Add the zero-breadth spindle theorem and its scope.

## Claims ledger

Add separate claim rows for:

- recursive radius max law;
- breadth plus law under corrected terminology;
- every internal subgroup lies on `lambda = 0`;
- first-level fork-count inclusion-exclusion law;
- full fork profile as `EXPERIMENTAL` or `FRONTIER` until its definition and composition are pinned.

Do not promote the semantic fork-admissibility rule as a UCNS algebra theorem. Record it as a downstream encoding constraint owned by METAPAT authority plus integration validation.

## Evidence provenance

Apply the artifact-grounded enumeration rule from handoff 08. Configured fixture counts are not completed execution counts.

---

# XI. Explicit exclusions

Do not include in this patch:

- selection of a METAPAT-to-UCNS encoding;
- implementation of the integration lint outside a schema/contract stub;
- 600-cell geometry;
- quaternionic axis construction;
- `2I` orbit execution;
- fiq runtime integration;
- epoch machinery;
- sphere-to-cylinder projection;
- prime-stratum analysis;
- EDCM scoring;
- claims that UCNS embeddings outperform current methods.

This package establishes the coordinates and enforcement boundary needed to test such claims later.

---

# XII. Completion standard

The handoff is complete only when:

1. recursive depth is named radius `rho` in mathematical prose;
2. `log(len)` is named breadth `lambda`;
3. the radius max law is written and mutation-backed;
4. the breadth plus law remains pinned under its corrected name;
5. the zero-breadth spindle theorem is added;
6. no claim says every positive-breadth pair is noncommuting;
7. the bridge states that the corrected tuple remains commutative and is not the quaternionic lift;
8. `b_1` and its inclusion-exclusion law are defined and tested;
9. the full fork profile remains derived and non-primitive pending a proved composition law;
10. a true hyper-tensor layer is defined as constitutive simultaneity, with semantic ownership outside UCNS;
11. fork admissibility is added to Phi Stage 3 exit criteria;
12. the future integration lint is specified as fail-closed;
13. temporal, adjacency, provenance, fiq, and symmetry relations are prohibited from silent payload nesting;
14. claims-ledger rows keep algebraic results separate from semantic encoding constraints;
15. no execution count appears without an immutable execution artifact;
16. no downstream integration or performance claim is implemented or promoted in this patch.

## hmmm

Radius says how far inward the recursive object reaches.

Breadth says how much ordered multiplicative extent exists at one level.

Forks say how many constitutive components coexist there—but only METAPAT can authorize that meaning, and only the integration layer can verify that the authorization survived encoding.

The subgroups live on the zero-breadth spindle. The tensors begin where breadth and constitutive forks appear.