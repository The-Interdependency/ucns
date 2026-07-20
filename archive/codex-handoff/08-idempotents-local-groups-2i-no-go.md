# UCNS idempotents, local groups, and binary-icosahedral no-go

## Assignment

Complete this work entirely inside `The-Interdependency/ucns` before any sphere-integration repository or integration implementation is created.

This is a structure-only theorem package:

1. pin the owning carrier laws;
2. prove the idempotent census;
3. prove the local-group census;
4. prove every internal UCNS subgroup is abelian;
5. derive the total binary-icosahedral no-go;
6. add mutation-backed executable contracts;
7. update the claims ledger with artifact-grounded evidence rules.

Do **not** implement METAPAT integration, fiq metering, 600-cell coordinates, quaternionic lifts, or full-field experiments in this patch.

---

## Source pin and re-read rule

At publication of this handoff:

- repository `main`: `f8a40ee5177606b92742e18e8cab311da2f46534`;
- `ucns/canonical.py` blob: `c78bc72b2eef94d0b20a82adfd5f2bc329bdcb3f`.

Before editing, re-read the live files and record the actual source commit used by the implementation PR. If `main` moved, inspect the intervening changes rather than copying these claims forward by inheritance.

The owning artifacts are:

- `ucns/canonical.py` — object construction, normalization, equality, multiplication, face law, and recursive payload law;
- `ucns-spec.md` — mathematical doubled-cover convention and normalization specification;
- `docs/base-geometry.md` — existing length grading, associativity, unit group, center, and structure theorem;
- `docs/claims-ledger.md` — controlling public claim-status surface.

---

# I. Carrier laws that must be cited in the proof surface

## Law 0 — Stored-angle unit convention

UCNS distinguishes the stored exact coordinate `a` from the mathematical doubled-cover angle `theta`.

The convention is:

```text
theta = pi * a
```

Thus:

```text
a in [0, 4)
```

represents:

```text
theta in [0, 4*pi)
```

and implementation reduction:

```text
a mod 4
```

is the same law as mathematical reduction:

```text
theta mod 4*pi.
```

Pin this to both owning surfaces:

- `ucns-spec.md`, which defines the doubled cover as `R / 4*pi*Z`;
- `ucns/canonical.py`, whose constructor documentation stores exact `Fraction` values in `[0, 4)` and treats plain integers as whole half-turn coordinates.

Do not write that the implementation uses radians modulo `4`. Use:

> stored coordinate `a` modulo `4`, representing mathematical angle `theta = pi*a` modulo `4*pi`.

## Law 1 — Mandatory construction normalization

`UCNSObject.__init__` calls `self.normalize()`.

`normalize()` applies:

```python
theta0 = self.A_plus[0][0]
new_theta = (theta - theta0) % 4
```

and recursively normalizes every non-unit payload.

Required consequence:

> Every constructed length-one UCNS object has canonical top-level stored angle zero, regardless of the supplied absolute angle.

The singleton angle is gauge-removed before local invertibility is considered. It is neither an invertible nor a non-invertible independent singleton coordinate in the current carrier.

## Law 2 — Product closure on the normalized carrier

`multiply(A, B)` constructs a new `UCNSObject` and normalizes it before returning.

Required consequence:

> The product of normalized carrier objects is again a normalized carrier object.

Use this law explicitly whenever equations such as `X box Y = T_d` compare products with canonical tower objects.

## Law 3 — Length grading

For nonempty carrier objects:

```text
len(A box B) = len(A) * len(B).
```

Reuse the existing proof and executable witnesses in `docs/base-geometry.md` and `contracts/`; do not silently restate the law as new.

## Law 4 — Face composition

At each product cell:

```text
f_new = f_A XOR f_B.
```

## Law 5 — Complete recursive payload composition

State all four cases explicitly:

```text
None tensor None = None
None tensor Q    = Q
P tensor None    = P
P tensor Q       = multiply(P, Q), when P and Q are both objects
```

The `None tensor None` base case is load-bearing for `T_1 box T_1 = T_1`; do not leave it implicit.

---

# II. Definitions

Define the zero-faced towers recursively.

```text
T_1 = UCNSObject(..., A_plus=[(0, None)], F_plus=[0])
```

and:

```text
T_(d+1) = UCNSObject(..., A_plus=[(0, T_d)], F_plus=[0]).
```

Use equality classes under the current implementation equality. Differing admissible `n_dec` declarations are not distinct algebraic objects where equality deliberately ignores `n_dec`.

For an idempotent `T_d`, define the local group `G_d` by the full four-equation condition. An object `X` belongs to `G_d` only when there exists `Y` such that:

```text
X box Y   = T_d
Y box X   = T_d
T_d box X = X
X box T_d = X.
```

The first pair establishes mutual cancellation to the candidate idempotent. The second pair establishes that the candidate idempotent is actually the local identity — the element's home.

---

# III. Theorem A — Idempotent census

## Statement

For every finite-depth, nonempty, normalized UCNS object `E`:

```text
E box E = E
```

if and only if:

```text
E = T_d
```

for exactly one finite depth `d >= 1`.

## Required proof

1. Let `n = len(E)`.
2. Length grading gives `n^2 = n`.
3. Since carrier objects are nonempty, `n = 1`.
4. Mandatory normalization gives sole top-level angle zero.
5. If the sole face bit is `f`, idempotence requires `f XOR f = f`. Since `f XOR f = 0`, conclude `f = 0`.
6. If the payload is `None`, the object is `T_1`.
7. If the payload is an object `P`, idempotence reduces to `P box P = P`.
8. Apply induction on finite recursive depth.
9. Prove the converse directly for every `T_d`, including the explicit `None tensor None = None` base case.

## Scope boundary

The theorem is scoped to the current:

- finite-depth carrier;
- acyclic recursive object model;
- mandatory gauge normalization;
- current equality relation;
- XOR face law;
- current recursive payload product.

Reopen it if UCNS later admits cyclic payload graphs, infinite recursive objects, unnormalized absolute singleton angles, an altered equality relation, or a changed face/payload law.

---

# IV. Theorem B — Local-group census

## Statement

For each finite depth `d >= 1`:

```text
G_d is isomorphic to (Z/2)^d.
```

Its elements are exactly recursively length-one towers of depth `d`, with canonical angle zero at every level, one freely chosen face bit at each level, and termination in `None`.

## Required proof

Let `X, Y in G_d`, with `Y` the local inverse of `X`.

### Step 1 — Top-level length

From:

```text
X box Y = T_d
```

and length grading:

```text
len(X) * len(Y) = 1.
```

Positive integral lengths force:

```text
len(X) = len(Y) = 1.
```

### Step 2 — Top-level angle

Mandatory normalization forces each singleton's stored angle to zero. Cite gauge normalization directly; do not justify this using an inverse/non-inverse dichotomy for modular angles.

### Step 3 — Top-level inverse equations

Write:

```text
X = [(0, P_X)], [f_X]
Y = [(0, P_Y)], [f_Y].
```

The inverse equations give:

```text
f_X XOR f_Y = 0
P_X tensor P_Y = T_(d-1)
P_Y tensor P_X = T_(d-1)
```

for `d > 1`.

These equations establish cancellation relative to the target payload. They do **not** establish local-group membership of the payloads.

### Step 4 — Identity absorption pins the recursive home

Use both local-identity equations:

```text
T_d box X = X
X box T_d = X
```

which imply:

```text
T_(d-1) tensor P_X = P_X
P_X tensor T_(d-1) = P_X.
```

Likewise for `P_Y`.

Together with the payload inverse equations, this proves:

```text
P_X, P_Y in G_(d-1).
```

This step pins the recursive depth to exactly `d`. Inverse equations alone admit depth-mismatched ghosts.

### Step 5 — Base case

At `d = 1`, the payload is `None`. The two possible top-level face bits form `Z/2`, with `None tensor None = None`.

### Step 6 — Induction

Each new depth contributes one independent XOR face bit while the payload belongs to `G_(d-1)`:

```text
G_d is isomorphic to Z/2 x G_(d-1).
```

Therefore:

```text
G_d is isomorphic to (Z/2)^d.
```

Every element is self-inverse and every local group is abelian.

---

# V. The depth-two ghost and home-relative membership

Use the following permanent witness.

```text
T_1 = [(0, None)], [0]
T_2 = [(0, T_1)], [0]
X   = [(0, None)], [1]
Y   = [(0, T_1)], [1].
```

Then:

```text
X box Y = T_2
Y box X = T_2
```

but:

```text
T_2 box X = Y != X
X box T_2 = Y != X.
```

Therefore `X` does not belong to `G_2` even though it has a two-sided cancellation partner to `T_2`.

The witness is structural, not stray:

- `X` is precisely the nontrivial element of `G_1`, the face-one member of the global unit group;
- `Y = X box T_2` is its depth-two translate;
- global units act across idempotent depths;
- cancellation is blind to depth, while identity absorption determines local home.

State this in the proof surface:

> The depth-two ghost is not an anomalous inverse pair: `X` is the nontrivial element of `G_1`, while `Y = X box T_2` is its depth-two translate. Global units can act across idempotent depths, so cancellation alone does not determine local-group membership; the four identity-absorption equations determine the element's local home.

---

# VI. Theorem C — Every internal UCNS subgroup is abelian

## Statement

Every subgroup contained in the current finite-depth UCNS monoid is abelian.

## Proof through the census

1. Let `H` be an internal subgroup, possibly with identity distinct from the global identity.
2. Its internal identity `E` is idempotent.
3. Theorem A gives `E = T_d` for some `d`.
4. Therefore `H` is contained in `G_d`.
5. Theorem B gives `G_d isomorphic to (Z/2)^d`.
6. Hence `H` is abelian.

## Carrier-law-minimal proof shape

Also record the more robust structural explanation:

- subgroup invertibility forces top-level length one by the length grading;
- local identity absorption recurses this singleton condition through participating payload levels;
- normalized singleton angles are gauge-zero;
- face composition is XOR;
- recursively singleton products commute.

Therefore:

> UCNS noncommutativity lives in ordered multi-cell sequences of length at least two. Internal group structure is confined to recursively singleton objects.

This structural statement is the true obstruction to internal nonabelian groups.

---

# VII. Theorem D — Total binary-icosahedral no-go

## Statement

Every semigroup homomorphism:

```text
phi : 2I -> (N, box)
```

is constant at a UCNS idempotent. Preservation of the global UCNS identity is not assumed.

## Required proof

1. Let `e_2I` be the identity of `2I` and set `E = phi(e_2I)`.
2. Then `E box E = E`, so Theorem A gives `E = T_d`.
3. For every `g in 2I`:

   ```text
   phi(g) box phi(g^-1) = T_d
   phi(g^-1) box phi(g) = T_d.
   ```

4. The image lies in the local group `G_d`.
5. `G_d` is abelian.
6. The binary icosahedral group `2I` is perfect.
7. Every homomorphism from a perfect group to an abelian group is trivial.
8. Therefore `phi(g) = T_d` for every `g`.

## Exact conclusion

There is:

- no global-identity copy of `2I`;
- no off-identity copy of `2I`;
- no nonconstant semigroup homomorphism from `2I` into UCNS;
- no nonabelian internal subgroup of any kind.

There is one constant homomorphism for each UCNS idempotent `T_d`.

## Integration consequence

Future sphere-integration schemas must reserve an external action surface:

```text
rho : 2I -> Aut(D)
```

and must not reserve or imply an internal embedded-group field:

```text
2I subset (UCNSObject, multiply).
```

The latter is ruled out under the current carrier.

---

# VIII. Documentation changes

## `docs/base-geometry.md`

Add a numbered section:

```text
Idempotents, local groups, and internal symmetry obstruction
```

It must contain:

- Laws 0–5 with owning citations;
- Theorems A–D;
- the depth-two ghost and its structural address;
- scope and reopening conditions;
- the distinction between internal subgroup and external automorphism action;
- explicit non-transfer language: this is a UCNS algebra result, not a METAPAT, EDCM, fiq, consciousness, or physical-ontology proof.

Do not call any theorem Lean-checked unless an actual discharged Lean proof is added.

## `docs/claims-ledger.md`

Add separate rows for:

1. idempotent census;
2. local group at `T_d` is `(Z/2)^d`;
3. every internal UCNS subgroup is abelian;
4. every semigroup homomorphism `2I -> UCNS` is constant at an idempotent.

Proposed status after written proof review and passing contracts:

```text
DEFENDED at specification level + TEST-BACKED
```

The `2I` row must distinguish the UCNS structural premises from the external group-theory premise that `2I` is perfect. None of these claims are Lean-checked unless a discharged formal proof is supplied.

---

# IX. Repository-wide evidence-provenance rule

Add this rule to `docs/claims-ledger.md`.

## Artifact-grounded enumeration

Every numerical claim about executed evidence must cite the exact immutable artifact that recorded the execution.

This includes:

- test counts;
- randomized cases;
- exhaustive cases;
- mutation cases;
- epochs;
- examples;
- failures;
- passes;
- proof obligations;
- products;
- benchmarks;
- coverage values.

Distinguish:

```text
configured count
```

from:

```text
executed and passing count.
```

Source code may establish that a test is configured to attempt a given number of cases. Source code alone does not establish that all cases executed successfully in a particular run.

Acceptable execution artifacts include immutable CI runs, committed reports, audit manifests, release artifacts, formal checker output, and versioned generated evidence.

README prose, module comments, function names, inherited assistant summaries, and copied uncited counts are `UNVERIFIED-PROVENANCE`.

Never replace a missing execution artifact with a plausible number.

---

# X. Executable contracts

Add a focused contract module, preferably:

```text
contracts/test_local_groups.py
```

or another name consistent with current repository conventions.

The contracts witness implementation consequences. They do not convert bounded finite tests into unbounded theorem proof.

## Contract 1 — Singleton gauge collapse

Construct singleton objects from several exact rational stored angles. Assert every constructed object has canonical angle zero.

Mutation: preserve an absolute singleton angle or bypass normalization; the contract must fail.

## Contract 2 — Product closure

For representative normalized objects at mixed depths:

- multiply them;
- assert the result is normalized;
- assert its first angle is zero;
- recursively assert every payload object is normalized.

Mutation: return a raw unnormalized product; the contract must fail.

## Contract 3 — Positive idempotent towers

Generate `T_d` at several bounded depths and assert:

```text
T_d box T_d == T_d.
```

Do not describe the bounded depth range as theorem coverage.

## Contract 4 — Bounded idempotent census

Within a declared finite generated domain:

- enumerate objects;
- select those satisfying `X box X == X`;
- assert every selected object is a generated zero-faced tower;
- assert every in-domain tower is selected.

Describe this only as bounded executable conformance to Theorem A.

## Contract 5 — Bounded local-group enumeration

For several bounded depths:

1. generate the `2^d` face-bit tower states;
2. verify closure;
3. verify identity `T_d`;
4. verify every state is self-inverse;
5. verify commutativity;
6. verify the configured state count from construction, while citing successful execution counts only through the exact CI artifact.

Mutations must include non-XOR face composition, a lost recursive face level, an incorrect local identity, and non-normalized singleton angles.

## Contract 5A — Home-relative membership and the depth-two ghost

Using the permanent witness, verify:

1. `X box Y == T_2`;
2. `Y box X == T_2`;
3. `T_2 box X != X`;
4. `X box T_2 != X`;
5. a full four-equation predicate rejects `X` at `T_2`;
6. the same predicate **accepts `X` at `T_1`**;
7. a bounded `G_2` census excludes `X`.

Mutation: certify local membership from inverse equations alone; the witness must catch it.

## Contract 6 — Noncommutativity boundary

Demonstrate both:

- a known multi-cell pair that does not commute;
- every generated bounded local-group tower commutes.

This directly witnesses:

```text
noncommutativity requires ordered multi-cell sequence structure.
```

## Contract 7 — Constant-map sanity fixture

For a bounded binary-icosahedral multiplication-table fixture, verify that constant maps to generated idempotents satisfy the semigroup-homomorphism equation.

Do not claim this finite fixture proves the no-go. The no-go is proof-defended; this is regression evidence only.

Do not add a 14,400-product sphere/integration sweep in this patch.

---

# XI. Mutation requirements

At minimum, contracts must catch implementations that:

1. preserve absolute singleton angle instead of gauge-normalizing it;
2. stop recursively normalizing payloads;
3. return an unnormalized product;
4. replace XOR with another face operation;
5. drop one recursive face level from local-group multiplication;
6. admit a multi-cell object as a local inverse of a singleton tower;
7. misidentify a face-one tower as idempotent;
8. certify local-group membership from inverse equations alone without identity absorption.

Mutation evidence must be tied to the exact immutable execution artifact that ran it.

---

# XII. Formalization boundary

Lean formalization is optional unless the existing carrier model supports this cleanly.

Do not introduce opaque predicates merely to label the result formal.

A useful formal model must include:

- finite recursive tower structure;
- length grading;
- singleton gauge normalization;
- XOR face vectors;
- full four-equation local membership;
- local-group multiplication;
- abelian-subgroup conclusion.

Any remaining `sorry` leaves the result specification-defended, not Lean-proved.

---

# XIII. Required gates

Run the repository's actual release and contract gates from the final revision.

At minimum:

1. manifest/generated-document drift checks;
2. targeted new contracts;
3. complete contract suite;
4. complete public and compatibility test suites;
5. package build;
6. metadata check;
7. built-wheel installation smoke test;
8. documentation claim guardrail;
9. mutation suite required by the base-geometry proof layer.

Record:

- exact source commit;
- exact final commit;
- exact commands;
- exact CI run identifiers;
- exact artifacts supporting every numerical execution claim.

Do not write “all tests passed” without identifying the run that records the result.

---

# XIV. Explicit exclusions

Do not include in this patch:

- METAPAT-to-UCNS encoding selection;
- `.loto/PHI_ENCODING_OPEN`;
- integration repository creation;
- 600-cell coordinates;
- quaternion address tables;
- `SU(2)` lift construction;
- 120-state injectivity checks;
- 14,400-pair image-correspondence experiments;
- fiq gates or epoch events;
- sphere-to-cylinder projection;
- coherence-prime experiments;
- EDCM measurements.

Those depend on this structure result but do not belong to it.

---

# XV. Completion standard

The handoff is complete only when:

1. both normalization and product-closure pins appear in the proof surface;
2. the stored-coordinate convention `theta = pi*a` is cited from owning artifacts;
3. mathematical modulo `4*pi` and implementation modulo `4` are explicitly reconciled;
4. the payload law includes `None tensor None = None`;
5. Theorems A–D are written with exact scope;
6. Theorem B invokes both inverse equations and both local-identity equations;
7. the local-group proof cites gauge normalization directly;
8. the depth-two ghost appears in proof and contract surfaces;
9. the ghost is accepted at `T_1` and rejected at `T_2` by the same home-relative predicate;
10. the abelian-subgroup theorem is separated from the stronger complete local-group classification;
11. mutation-backed contracts cover all load-bearing laws;
12. inverse-only local-membership certification is mutation-caught;
13. the claims ledger adds artifact-grounded enumeration;
14. no execution count appears without an immutable execution artifact;
15. claims remain specification-defended unless stronger proof evidence exists;
16. all required gates are green;
17. the PR states the integration consequence: model `2I` as an external action, not an internal UCNS subgroup.

---

## Dependency chain

```text
Law 0: stored-angle unit convention
  -> Laws 1–5: normalized carrier and product
  -> Theorem A: idempotent census
  -> Theorem B: four-equation local-group census
  -> Theorem C: every internal subgroup is abelian
  -> Theorem D: every 2I homomorphism is constant
  -> integration constraint: rho-action slots, no embedded-group fields
```

## hmmm

The ghost has a home one floor down.

Cancellation says which objects can meet and erase one another to an idempotent. Identity absorption says where an object lives. Once UCNS group structure is forced into recursively singleton towers, only finite sequences of face reversals remain. The sphere's 120-fold nonabelian symmetry must therefore act from outside UCNS multiplication.