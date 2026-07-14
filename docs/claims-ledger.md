GPT generated; context, prompt Erin Spencer.

# UCNS Claims Ledger

## hmm

This ledger separates UCNS definitions, implemented behavior, test-backed
results, proof-defended claims, conjectures, known limitations, and deprecated
claims. The goal is not to inflate certainty, but to make the current frontier
reviewable by mathematics and computational collaborators.

Status vocabulary follows `docs/ucns-spec-status-addendum-2026-05-16.md`:

```text
DEFENDED          written proof or proof-defended theorem layer
IMPLEMENTED       code exists and is intended as authoritative implementation
TEST-BACKED       tests cover the claimed behavior in the declared domain
ORACLE-COMPLETE   complete only under oracle/catalogue assumptions
FRONTIER          plausible or partially working, not complete
EXPERIMENTAL      exploration layer, not canon
```

**Release-status precedence.** This ledger together with `README.md` supersedes
every status classification anywhere in `ucns-spec.md`. Until the remaining
Lean proof leaves are discharged and external formal review is complete, the
current release status of Theorem N is `FRONTIER`.

## Artifact-grounded enumeration rule

Every numerical statement about executed tests, trials, epochs, products,
mutations, proof obligations, examples, passes, failures, benchmarks, or
coverage must identify the immutable artifact that recorded the execution.

Source code may establish a configured count, intended loop bound, or finite
domain size. Source code alone does not establish that the configured cases
executed successfully in a particular run. Acceptable execution evidence
includes immutable CI runs, committed reports, audit manifests, release
artifacts, or formal-checker output tied to an exact source revision.

README prose, module comments, test names, inherited summaries, and uncited
copied counts are `UNVERIFIED-PROVENANCE`. When no execution artifact is
available, use nonnumerical wording such as "tested over randomized cases in
the cited suite."

---

## 1. Definitions / ontology claims

| Claim | Status | Primary surface | Notes |
|---|---|---|---|
| A UCNS object is represented as `UCNSObject(n_dec, n_min, A_plus, F_plus)`. | `IMPLEMENTED` | `ucns.canonical` | `A_plus` is a sequence of `(angle, payload)` pairs; payloads are `UCNSObject | None`. |
| `None` is the unit payload. | `IMPLEMENTED` | `ucns.canonical`, `ucns.domains` | Exported as `UNIT`. |
| Recursive radius is payload nesting: `rho(None)=0`; `rho(U)=1+max(payload radius)`. | `IMPLEMENTED` | `ucns.relational_geometry.recursive_radius`, `ucns.domains.depth_of` | Formerly called recursive depth; now explicitly the radial coordinate. |
| Breadth is `lambda(U)=log(len(U.A_plus))`. | `IMPLEMENTED` | `ucns.relational_geometry.breadth`, `ucns.geometry_bridge` | The bridge field `r` remains a compatibility storage name; new prose uses breadth/lambda. |
| First-level fork count is the number of top-level cells carrying non-unit payloads. | `IMPLEMENTED` | `ucns.relational_geometry.first_level_fork_count` | Structural observable only; no semantic claim that every payload fork is constitutive. |
| Frozen domain D' is bounded by `depth <= 2`, `|A_plus| <= 3`, `n_min <= 4`. | `IMPLEMENTED` | `ucns.domains` | Used as the standing depth-2 implementation/test envelope. |
| Oracle atoms are `None` plus depth-1 objects inside the frozen bounds. | `IMPLEMENTED` | `ucns.domains.generate_payload_catalogue` | Used as the default payload catalogue for the solver. |
| `SEQ-PRIME` is a solver sentinel, not an unscoped mathematical absolute. | `DEFENDED` policy rule | `ucns-spec.md`, `domain_status.py`, `factorization_result.py` | Absolute only inside declared complete domains. |

---

## 2. Implemented algorithms

| Algorithm / API | Status | Surface | v1.0 interpretation |
|---|---|---|---|
| `multiply(A, B)` | `IMPLEMENTED` | `ucns.canonical`, re-exported from `ucns` | Builds a recursive product object cellwise. |
| Relational geometry and local-group helpers | `IMPLEMENTED` + `TEST-BACKED` | `ucns.relational_geometry`, `contracts/test_local_groups_and_geometry.py` | Radius, breadth, fork count, tower constructors, idempotent recognition, and home-relative local-group predicates. |
| `factor_search_v08(P, catalogue=None)` | `IMPLEMENTED` | `ucns.factor_search_v08`, re-exported from `ucns` | v1.0 factorization engine: witness-matrix recursive quotient solver. |
| Host recovery | `IMPLEMENTED` | `ucns.host_recovery` | Structural recovery of candidate factor angle/face hosts. |
| Payload equation solving | `IMPLEMENTED` | `ucns.payload_system` | Catalogue-bounded solving of coupled payload equations. |
| Witness matrix consistency | `IMPLEMENTED` | `ucns.witness_matrix` | Global row/column consistency gate before recomposition. |
| Exact recomposition guard | `IMPLEMENTED` | `factor_search_v08` | Accepted factors must satisfy `multiply(A, B) == P`. |
| A0-facing result envelope | `IMPLEMENTED` | `ucns.factorization_result` | Wraps raw factorization output with scoped domain certainty metadata. |
| Stable identity serialization/hash | `IMPLEMENTED` | `ucns.serialization` | Canonical data and hash surface for audit logs and object identity. |
| Constructor invariants | `IMPLEMENTED` + `TEST-BACKED` | `ucns.canonical.UCNSObject` | Nonempty sequences, positive carriers, typed payloads, exact angles, parallel faces. |
| Official cross-repository bridge record + adapter | `IMPLEMENTED` + `TEST-BACKED` | `ucns.bridge` | Versioned neutral bridge; provenance carries no theorem status. |
| Downstream proof-status evidence envelope | `IMPLEMENTED` + `TEST-BACKED` | `ucns.evidence` | Distinguishes construction, finite-search, coverage, certified negatives, theorem statuses, and absence of proof status. |
| `ucns` public namespace | `IMPLEMENTED` | `ucns/__init__.py` | `ucns_recursive` remains a compatibility shim. |

---

## 3. Proof-defended / theorem claims

| Claim | Status | Scope | Notes |
|---|---|---|---|
| Flat kernel algebra | `DEFENDED` | v0.3 layer | Preserved in `ucns-spec.md`. |
| Epicyclic first freeze | `DEFENDED` | v0.4 layer | Preserved in `ucns-spec.md`. |
| Recursive sequence / multiset primality notions | `DEFENDED` | v0.5 layer | Preserved with later scoping warnings. |
| Cancellativity and quotient uniqueness boundary | **REFUTED in general; `DEFENDED` dichotomy** | current monoid | A divisor cancels iff some top-level payload is the unit; see `docs/base-geometry.md`. |
| v0.6 Left-Quotient Completeness (`catalogue=None`) | **scope-corrected**: sound always; complete for flat divisors; incomplete in general | `ucns.left_quotient` | Complete solution-set enumeration lives in `ucns.division_theory`. |
| Base geometry structure theorem | `DEFENDED` at spec level + `TEST-BACKED` (`[mutation-verified]`) | current finite-depth normalized carrier | Length-graded noncommutative noncancellative monoid; unit group `Z/2`; center is unit towers. Not Lean-checked. |
| Idempotent census: `E box E=E` iff `E=T_d` | `DEFENDED` at spec level + `TEST-BACKED` (`[mutation-verified]`) | current finite-depth normalized carrier | Proof and reopening conditions: `docs/local-groups-and-relational-geometry.md`; bounded conformance is not the proof. |
| Local group at `T_d` is `(Z/2)^d` | `DEFENDED` at spec level + `TEST-BACKED` (`[mutation-verified]`) | current finite-depth normalized carrier | Uses all cancellation and identity-absorption equations; depth-two ghost rejects inverse-only membership. |
| Every internal UCNS subgroup is abelian | `DEFENDED` at spec level + `TEST-BACKED` (`[mutation-verified]`) | current finite-depth normalized carrier | Internal invertibility forces recursively singleton towers. |
| Every semigroup homomorphism `2I -> UCNS` is constant at an idempotent | `DEFENDED` at spec level + `TEST-BACKED` regression | current carrier plus standard premise that `2I` is perfect | No internal binary-icosahedral subgroup; sphere symmetry must use an external action. Not Lean-checked. |
| Recursive radius max law | `DEFENDED` at spec level + `TEST-BACKED` (`[mutation-verified]`) | finite-depth carrier | `rho(A box B)=max(rho(A),rho(B))`; target is the commutative idempotent max monoid. |
| Breadth plus law | `DEFENDED` at spec level + `TEST-BACKED` | nonempty carrier | `lambda(A box B)=lambda(A)+lambda(B)`; historical `r=log(len)` invariant under corrected name. |
| Zero-breadth spindle theorem | `DEFENDED` at spec level + `TEST-BACKED` | internal local groups/subgroups | Every internal group lies on `lambda=0`; noncommutative witnesses require positive breadth, converse refused. |
| First-level fork inclusion-exclusion law | `DEFENDED` at spec level + `TEST-BACKED` (`[mutation-verified]`) | top-level payload-bearing count | Full fork profile remains unpinned. |
| Restricted completeness on bounded depth-1 domain | `DEFENDED` + `TEST-BACKED` | v0.6.1-v0.6.5 | Older defended completeness layer. |
| Depth-2 smallest oracle theorem / Lemma 7 | `DEFENDED` + `ORACLE-COMPLETE` | Depth-2 under oracle assumptions | Complete only under declared oracle surface. |
| Theorem N: catalogue-sufficient factorization | `FRONTIER` | all depths under catalogue sufficiency | Completeness statements remain `sorry`-closed and await external formal review. |
| Formal search model / Python witness-space conformance | `TEST-BACKED` on declared fixture only | Lean/Python fixture | Lean-side fixture evaluation remains open. |

---

## 4. Empirically verified / test-backed results

| Result | Status | Test / artifact | Notes |
|---|---|---|---|
| Local-group and relational-geometry implementation conformance | `TEST-BACKED` after green implementing PR CI | `contracts/test_local_groups_and_geometry.py`, `tests/test_base_geometry_contracts.py` | The CI run is the execution artifact; source fixture counts are configuration only. |
| Full frozen depth-2 domain behavior | `IMPLEMENTED` + `TEST-BACKED`; not spec-defended | `ucns_recursive/tests/test_depth2_full_domain.py` | Compact closure sweep plus hand-constructed cases; not literal exhaustive enumeration. |
| Depth-3 asymmetric examples | historical `TEST-BACKED` claim; execution count requires artifact citation | `code/sweeps/t9_minimal_cat.py` | Do not repeat inherited numeric success counts without the exact run artifact. |
| Soundness guard for returned factors | `TEST-BACKED` | test suite and recomposition checks | Any returned factors must recompose. |
| A0 domain-status metadata | `TEST-BACKED` | domain-status and factorization-envelope tests | Prevents unscoped `SEQ-PRIME` claims. |
| Public namespace import surface | `TEST-BACKED` by release artifacts | package workflow | Import path is `ucns`. |

---

## 5. Known limitations / open frontier

| Item | Status | Decision |
|---|---|---|
| Full recursive fork profile `B(U)` | `FRONTIER` / `EXPERIMENTAL` | Counting convention and target composition law must be pinned before it is a bridge coordinate. |
| Semantic fork admissibility | downstream encoding constraint, not a UCNS algebra theorem | METAPAT authority plus integration lint must enforce constitutive simultaneity. |
| Quaternionic lift / `SU(2)` axis data | `FRONTIER` | Corrected `(rho,lambda,theta,z,w)` bridge remains commutative and does not recover the commutator. |
| Carrier widening beyond frozen bounds | `FRONTIER` | Out of v1.0 scope. |
| Tractable sub-catalogues | `FRONTIER`, narrowed | Support pruning is defended; catalogue design remains open. |
| General recursive primality outside defended-complete domains | out of scope | `SEQ-PRIME` remains scoped. |
| Recursive disk-flip content symmetry as depth-n theorem | `FRONTIER` | Not required for v1.0. |
| Canonical factor choice under v0.8 catalogue semantics | `FRONTIER` | Deterministic selection under older complete enumerator is separate. |
| Performance scaling for large catalogues | `FRONTIER` | Efficient search within pruned lattice remains open. |
| External formal review | Open | Theorem N needs mathematical pressure before stronger language. |

---

## 6. Deprecated or superseded claims

| Claim | Status | Replacement |
|---|---|---|
| `r=log(len)` described as recursive depth/radius | Superseded | `rho` is recursive radius; `lambda=log(len)` is breadth. Compatibility field `GeometricPoint.r` stores breadth. |
| Binary “solved / not solved” depth-2 language | Superseded | Typed status vocabulary. |
| Theorem 8c as practically meaningful depth-3 symmetric completeness | Superseded / vacuous | Catalogue-sufficient frontier and asymmetric examples. |
| Prior depth-indexed induction plan for Theorem N | Superseded | Depth-agnostic catalogue-sufficient target. |
| Direct user import from `ucns_recursive` | Deprecated | Use `ucns`; compatibility shim remains. |

---

## 7. v1.0 release claim

The recommended v1.0 wording remains:

```text
UCNS v1.0.0 is a scoped, reproducible research release for
catalogue-sufficient recursive factorization using the witness-matrix recursive
quotient solver. It does not claim total general recursive primality, carrier
widening, tractable catalogue discovery, a universal canonical factor-choice
procedure, a quaternionic lift, improved embedding performance, or a fully
discharged Lean proof of Theorem N.
```

## hmmm
