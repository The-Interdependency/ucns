# UCNS local groups and relational geometry

**Status.** Specification-level proof surface for the structure package in
`codex-handoff/08-idempotents-local-groups-2i-no-go.md` and
`codex-handoff/09-radius-breadth-fork-semantics.md`.

The claims below become `DEFENDED at specification level + TEST-BACKED` only
when the implementing pull request has a green immutable CI run covering
`contracts/test_local_groups_and_geometry.py`. They are not Lean-checked.

Nothing here transfers UCNS proof status into METAPAT ontology validity, fiq
motion validity, EDCM measurement validity, or any future embedding claim.

---

## 1. Owning carrier laws

Let `N` be the current carrier of nonempty, finite-depth, recursively normalized
`UCNSObject` values modulo implementation equality.

Stored angles are exact coordinates `a in [0,4)` in half-turn units, representing
mathematical angles `theta = pi*a` on `R / 4*pi*Z`. Construction calls
`normalize()`, which replaces every angle by `(a_i-a_0) mod 4` and recursively
normalizes payloads. Consequently every singleton object has canonical angle
zero: its absolute singleton angle is gauge, not an independent group
coordinate.

For normalized nonempty objects `A` and `B`, `multiply(A,B)` emits exactly
`len(A)*len(B)` cells and constructs/normalizes a new `UCNSObject`, so the
product is again in `N`.

The payload merge law is complete in all four cases:

```text
None tensor None = None
None tensor Q    = Q
P tensor None    = P
P tensor Q       = P box Q     when P,Q are objects
```

Faces compose by XOR.

---

## 2. Radius, breadth, and fork count

Define recursive radius:

```text
rho(None) = 0
rho(U) = 1 + max_i rho(payload_i).
```

Define breadth:

```text
lambda(U) = log(len(U.A_plus))
```

for nonempty objects, with the external `None` unit assigned breadth zero where
that public surface is used.

Define the first-level fork count:

```text
b1(U) = number of top-level cells whose payload is not None.
```

### Theorem 2.1 — radius max law

For all finite-depth carrier objects:

```text
rho(A box B) = max(rho(A), rho(B)).
```

**Proof.** Product-cell payloads are `P_i tensor Q_j`. The first three payload
cases give the max identity immediately. In the fourth case, induction on
`max(rho(P_i),rho(Q_j))` gives
`rho(P_i box Q_j)=max(rho(P_i),rho(Q_j))`. Taking the maximum over all product
cells gives

```text
max_(i,j) max(rho(P_i),rho(Q_j))
  = max(max_i rho(P_i), max_j rho(Q_j)).
```

Adding the outer object layer yields the claim. Normalization changes angle
gauge and recursively canonicalizes payload representations; it neither adds
nor deletes payload levels. Therefore `rho` maps UCNS multiplication to the
commutative idempotent monoid `(Z_ge_0,max,0)`. ∎

### Theorem 2.2 — breadth plus law

```text
lambda(A box B) = lambda(A) + lambda(B).
```

**Proof.** The ordered product emits exactly `len(A)*len(B)` cells and
normalization deletes none. Apply `log(xy)=log(x)+log(y)`. ∎

This is the invariant historically called `r=log(len)`. Its mathematics was
valid; its geometric name was not. New prose uses breadth `lambda`; the bridge
retains field `r` only for compatibility.

### Theorem 2.3 — first-level fork inclusion-exclusion

Let `m_A=len(A)`, `m_B=len(B)`, `b_A=b1(A)`, and `b_B=b1(B)`. A product cell has
no payload exactly when both source cells have no payload. Hence

```text
b1(A box B)
  = m_A*m_B - (m_A-b_A)*(m_B-b_B)
  = b_A*m_B + b_B*m_A - b_A*b_B.
```

The full recursive fork profile is a derived observable, not a primitive
homomorphic bridge coordinate, until its counting convention and target
composition law are separately pinned.

---

## 3. Idempotent census

Define zero-faced towers recursively:

```text
T_1 = [(0,None)],[0]
T_(d+1) = [(0,T_d)],[0].
```

### Theorem 3.1

For every finite-depth carrier object `E`:

```text
E box E = E    iff    E = T_d for exactly one d >= 1.
```

**Proof.** Length grading gives `len(E)^2=len(E)`. Carrier lengths are positive
integers, so `len(E)=1`. Gauge normalization forces the sole angle to zero. If
the face is `f`, idempotence requires `f XOR f=f`; the left side is zero, so
`f=0`. The payload is either `None`, giving `T_1`, or an object `P` satisfying
`P box P=P`. Induction on finite recursive depth gives `T_d`. Conversely, the
complete payload law and XOR show directly that every zero-faced tower squares
to itself. ∎

The theorem must be reopened if the carrier later admits cyclic payload graphs,
infinite recursive values, unnormalized singleton angles, a changed equality
relation, or different face/payload laws.

---

## 4. Home-relative local groups

For idempotent `T_d`, a pair `X,Y` belongs to the local group at `T_d` only when
all six equations hold:

```text
X box Y = T_d = Y box X
T_d box X = X = X box T_d
T_d box Y = Y = Y box T_d.
```

Cancellation alone does not determine local home.

### The depth-two ghost

Let

```text
X = [(0,None)],[1]
Y = [(0,T_1)],[1].
```

Then `X box Y=T_2=Y box X`, but `T_2 box X=Y!=X` and
`X box T_2=Y!=X`. Thus `X` cancels with `Y` to `T_2` but is not in the local
group at `T_2`. Structurally, `X` is the nontrivial element of `G_1`, while
`Y=X box T_2` is its depth-two translate. Units act across depths; identity
absorption, not cancellation, identifies the home.

### Theorem 4.1 — local-group census

For every `d>=1`:

```text
G_d is isomorphic to (Z/2)^d.
```

**Proof.** If `X,Y` are local inverses at `T_d`, length grading applied to
`X box Y=T_d` forces both top-level lengths to one. Normalization forces their
singleton angles to zero. Write `X=[(0,P_X)],[f_X]` and similarly for `Y`.
The inverse equations give top-level XOR cancellation and payload cancellation
to `T_(d-1)`. Those equations alone are insufficient. The two-sided identity
equations with `T_d` additionally give

```text
T_(d-1) tensor P_X = P_X = P_X tensor T_(d-1),
```

and likewise for `P_Y`; therefore the payloads belong to `G_(d-1)`. At depth
one, the two face values form `Z/2` with `None tensor None=None`. Each further
level contributes one independent XOR bit, so
`G_d = Z/2 x G_(d-1)`, hence `(Z/2)^d`. Every element is self-inverse and every
local group is abelian. ∎

### Corollary 4.2 — every internal subgroup is abelian

Every internal subgroup has an idempotent identity `T_d` and lies inside its
local group `G_d`; therefore every internal subgroup is abelian.

The carrier-level explanation is sharper: UCNS noncommutativity lives in the
ordered interleaving of multi-cell sequences. Group invertibility forces
recursively singleton objects, where angle gauge is zero and face/payload
composition is commutative.

---

## 5. Zero-breadth spindle

Define

```text
S_0 = { U in N : lambda(U)=0 }.
```

Because carrier objects are nonempty, `lambda(U)=0` iff `len(U)=1`.

### Theorem 5.1

Every internal UCNS subgroup lies in `S_0`.

**Proof.** If `X` has local inverse `Y` at idempotent `T_d`, then
`len(X)*len(Y)=len(T_d)=1`; therefore both lengths are one and both breadths are
zero. ∎

Thus internal group structure is confined to the zero-breadth spindle.
Noncommutative witnesses require positive breadth, but positive breadth is not
sufficient for noncommutativity; the converse is expressly refused.

---

## 6. Binary-icosahedral no-go

The binary icosahedral group `2I` is nonabelian and perfect
(`2I` is isomorphic to `SL(2,5)`).

### Theorem 6.1

Every semigroup homomorphism

```text
phi : 2I -> (N, box)
```

is constant at an idempotent.

**Proof.** `phi(e)` is an idempotent, hence some `T_d`. For every `g`,
`phi(g)` and `phi(g^-1)` are local inverses at `T_d`, so the image lies in the
abelian local group `G_d`. Any homomorphism from a perfect group to an abelian
group is trivial. Therefore `phi(g)=T_d` for all `g`. ∎

Consequently there is no global-identity or off-identity internal copy of
`2I`, and no nonabelian internal subgroup. Future sphere integration must model
binary-icosahedral symmetry through an external action

```text
rho_action : 2I -> Aut(D),
```

not through an embedded-group field.

---

## 7. Bridge and semantic boundary

The corrected commutative bridge coordinate is at least

```text
(rho, lambda, theta, z, w).
```

Separating radius from breadth repairs coordinate semantics. It does not supply
quaternionic axis data, recover the commutator, or advance the future `SU(2)`
lift by itself.

A true hyper-tensor layer is provisionally a payload fork whose children are
simultaneous constitutive components of one parent METAPAT simplex/tensor
state. UCNS can represent the fork but cannot infer that semantic relation.
Fork admissibility therefore belongs to the METAPAT-to-UCNS encoding policy and
a fail-closed integration validator. Time, adjacency, provenance, fiq motion,
alternatives, and external symmetry actions must remain external relations
unless METAPAT explicitly declares constitutive simultaneity.

---

## 8. Evidence boundary

The executable contract uses bounded fixtures and explicit mutants. Those
fixtures witness implementation conformance; they do not prove the unbounded
statements by enumeration.

Every numerical execution claim must cite the immutable CI run or committed
artifact that recorded it. Source loop bounds establish configured counts, not
completed passing counts. No count from module prose, README prose, an assistant
summary, or an uncited historical report is execution evidence.
