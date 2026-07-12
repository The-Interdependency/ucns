GPT generated; context, prompt Erin Spencer.

# UCNS Claims Ledger

## hmm

This ledger separates UCNS definitions, implemented behavior, test-backed results, proof-defended claims, conjectures, known limitations, and deprecated claims. It is a v1.0 release-prep artifact: the goal is not to inflate certainty, but to make the current frontier reviewable by mathematics and computational collaborators.

Status vocabulary follows `docs/ucns-spec-status-addendum-2026-05-16.md`:

```text
DEFENDED          written proof or proof-defended theorem layer
IMPLEMENTED       code exists and is intended as authoritative implementation
TEST-BACKED       tests cover the claimed behavior in the declared domain
ORACLE-COMPLETE   complete only under oracle/catalogue assumptions
FRONTIER          plausible or partially working, not complete
EXPERIMENTAL      exploration layer, not canon
```

**Release-status precedence.** This ledger together with `README.md` supersedes every status classification anywhere in `ucns-spec.md`, not only the dated status snapshot at its beginning. That scope explicitly includes §F4 and any historical statement that labels Theorem N `DEFENDED`. Until the remaining Lean proof leaves are discharged and external formal review is complete, the current release status of Theorem N is `FRONTIER`.

---

## 1. Definitions / ontology claims

| Claim | Status | Primary surface | Notes |
|---|---|---|---|
| A UCNS object is represented as `UCNSObject(n_dec, n_min, A_plus, F_plus)`. | `IMPLEMENTED` | `ucns.canonical` | `A_plus` is a sequence of `(angle, payload)` pairs; payloads are `UCNSObject | None`. |
| `None` is the unit payload. | `IMPLEMENTED` | `ucns.canonical`, `ucns.domains` | Exported as `UNIT`. |
| Recursive depth is defined by payload nesting: `None -> 0`; object depth is `1 + max(payload depth)`. | `IMPLEMENTED` | `ucns.domains.depth_of` | Used by domain-status metadata and tests. |
| Frozen domain D' is bounded by `depth <= 2`, `|A_plus| <= 3`, `n_min <= 4`. | `IMPLEMENTED` | `ucns.domains` | Used as the standing depth-2 implementation/test envelope. |
| Oracle atoms are `None` plus depth-1 objects inside the frozen bounds. | `IMPLEMENTED` | `ucns.domains.generate_payload_catalogue` | Used as the default payload catalogue for the solver. |
| `SEQ-PRIME` is a solver sentinel, not an unscoped mathematical absolute. | `DEFENDED` policy rule | `ucns-spec.md`, `domain_status.py`, `factorization_result.py` | Absolute only inside declared complete domains. |

---

## 2. Implemented algorithms

| Algorithm / API | Status | Surface | v1.0 interpretation |
|---|---|---|---|
| `multiply(A, B)` | `IMPLEMENTED` | `ucns.canonical`, re-exported from `ucns` | Builds a recursive product object cellwise. |
| `factor_search_v08(P, catalogue=None)` | `IMPLEMENTED` | `ucns.factor_search_v08`, re-exported from `ucns` | v1.0 factorization engine: witness-matrix recursive quotient solver. |
| Host recovery | `IMPLEMENTED` | `ucns.host_recovery` | Structural recovery of candidate factor angle/face hosts. |
| Payload equation solving | `IMPLEMENTED` | `ucns.payload_system` | Catalogue-bounded solving of coupled payload equations. |
| Witness matrix consistency | `IMPLEMENTED` | `ucns.witness_matrix` | Global row/column consistency gate before recomposition. |
| Exact recomposition guard | `IMPLEMENTED` | `factor_search_v08` | Soundness guard: accepted factors must satisfy `multiply(A, B) == P`. |
| A0-facing result envelope | `IMPLEMENTED` | `ucns.factorization_result` | Wraps raw factorization output with scoped domain certainty metadata. |
| Stable identity serialization/hash | `IMPLEMENTED` | `ucns.serialization` | Canonical data and hash surface for audit logs and object identity. |
| Constructor invariants (nonempty `A_plus`, positive carriers, typed payloads, parallel faces) | `IMPLEMENTED` + `TEST-BACKED` | `ucns.canonical.UCNSObject` | Empty object sequences, non-positive `n_dec`/`n_min`, and non-UCNS payload types are rejected at construction; adversarial tests in both the public and compatibility suites. |
| Official cross-repository bridge record + adapter | `IMPLEMENTED` + `TEST-BACKED` | `ucns.bridge` | Versioned neutral record (`ucns-bridge-record` v1); fail-closed import into actual `UCNSObject`; round trip preserves equality and stable hash; provenance carries no theorem status. |
| Downstream proof-status evidence envelope | `IMPLEMENTED` + `TEST-BACKED` | `ucns.evidence` | Non-boolean vocabulary distinguishing construction, search exhaustion, validated coverage, certified domain-relative negatives, theorem-layer statuses, and absence of proof status. |
| `ucns` public namespace | `IMPLEMENTED` | `ucns/__init__.py` | v1.0 public import surface; `ucns_recursive` remains a compatibility shim. |

---

## 3. Proof-defended / theorem claims

| Claim | Status | Scope | Notes |
|---|---|---|---|
| Flat kernel algebra | `DEFENDED` | v0.3 layer | Preserved in `ucns-spec.md`. |
| Epicyclic first freeze | `DEFENDED` | v0.4 layer | Preserved in `ucns-spec.md`. |
| Recursive sequence / multiset primality notions | `DEFENDED` | v0.5 layer | Preserved with later scoping warnings. |
| Cancellativity and quotient uniqueness boundary | **REFUTED in general; `DEFENDED` dichotomy: a divisor cancels iff some top-level payload is the unit** | v0.5.1 layer; corrected in `docs/base-geometry.md` §5 (Theorems 5.3–5.5) | Counterexamples: tower absorption (`T3 ⊠ T2 = T3 ⊠ T3`, both sides) and `formal/cancellativity-step1-findings.md`; flat divisors are the all-unit special case (why the v0.5.1 depth-0/1 regression saw zero violations). The depth-aligned `AlignedComplete` conditional statement remains a Lean frontier obligation. |
| v0.6 Left-Quotient Completeness (`catalogue=None`) | **scope-corrected 2026-07-10**: sound always; complete for flat divisors; incomplete in general | `ucns.left_quotient`, `docs/base-geometry.md` §5 | Counterexample is a permanent regression in `contracts/test_quotient_solvability.py`. Complete solution-set enumeration: `ucns.division_theory`. `right_quotient` additionally used the left payload helper (extra misses; still sound). |
| Base geometry structure theorem: `(N, ⊠, e)` is a length-graded, non-commutative, non-cancellative monoid; unit group ≅ ℤ/2; center = unit towers | `DEFENDED` at spec level + `TEST-BACKED` (`[mutation-verified]` contracts) | `docs/base-geometry.md`, `contracts/` | O1–O7 of the base-geometry handoff: associativity proven (θ collapse exists only in the geometric projection); division partial and multivalued with forced hosts and finite fibers; no primitive addition (derived ⊕ is right-distributive only). Not Lean-checked. |
| Restricted completeness on bounded depth-1 domain | `DEFENDED` + `TEST-BACKED` | v0.6.1-v0.6.5 | The older defended completeness layer. |
| Depth-2 smallest oracle theorem / Lemma 7 | `DEFENDED` + `ORACLE-COMPLETE` | Depth-2 under oracle/catalogue assumptions | Complete only under the declared oracle surface. |
| Theorem N: catalogue-sufficient factorization | `FRONTIER`; implementation-backed proof sketch, Lean proof pending, awaiting external formal review | All depths, assuming catalogue contains every recursive payload of true non-multiplicative-unit factors | Central v1.0 proof target. It is an **exhaustive-inclusion** completeness target for finding **a** valid factorization: no general cancellativity, no quotient uniqueness, and no recovery of the original factor pair is claimed or needed. The Lean model (`formal/Ucns/TheoremN.lean`) now defines the finite search and its exact-recomposition success relation (no opaque predicates); the completeness statements themselves remain `sorry`-closed. Not a tractability theorem and not yet a DEFENDED theorem. |
| Formal search model / Python witness-space conformance | `TEST-BACKED` on the declared small-domain fixture only | `formal/Ucns/TheoremN.lean`, `tests/test_formal_conformance.py` | The Python transcription of the Lean search model enumerates exactly the executable solver's accepted witness space on the declared fixture domain. Lean-side evaluation of the fixture and the declared modeling boundaries remain open (`audit/obligation_ledger.md`). |

---

## 4. Empirically verified / test-backed results

| Result | Status | Test / artifact | Notes |
|---|---|---|---|
| Full frozen depth-2 domain behavior | `IMPLEMENTED` + `TEST-BACKED`; not yet `DEFENDED` at spec level | `ucns_recursive/tests/test_depth2_full_domain.py` | Compact closure sweep plus hand-constructed edge cases; not literal exhaustive enumeration. |
| Depth-3 asymmetric examples | `TEST-BACKED` | `code/sweeps/t9_minimal_cat.py` | 6/6 empirical success with minimal catalogues. |
| Soundness guard for returned factors | `TEST-BACKED` | test suite and recomposition checks | Any returned factors must recompose to the product. |
| A0 domain-status metadata | `TEST-BACKED` | `ucns_recursive/tests/test_domain_status.py` and factorization envelope tests | Prevents unscoped `SEQ-PRIME` claims outside verified domains. |
| Public namespace import surface | `TEST-BACKED` by release-prep smoke commands | README / PR test plan | `from ucns import ...` is the documented v1.0 path. |

---

## 5. Known limitations / open frontier

| Item | Status | v1.0 decision |
|---|---|---|
| Carrier widening beyond frozen bounds | `FRONTIER` (analytic side only) | Explicitly out of v1.0 scope. The Carrier-LCM Law (`docs/carrier-support-pruning.md`, `DEFENDED` + `TEST-BACKED` on this substrate) closes the operational side exactly; cross-prime *factoring* remains open. |
| Tractable sub-catalogues | `FRONTIER`, narrowed | Carrier-support pruning (`ucns.catalogue_pruning`, `DEFENDED` + `TEST-BACKED`) gives a sound opt-in pre-filter; catalogue *design* beyond support-pruning remains open. |
| General recursive primality outside defended-complete domains | Out of v1.0 scope | `SEQ-PRIME` remains scoped by `domain_status_metadata`. |
| Recursive disk-flip content symmetry as a depth-n theorem | `FRONTIER` | Not required for v1.0. |
| Canonical factor choice among multiple valid decompositions | `FRONTIER`, narrowed | Deterministic selector over the v0.6-complete left-factor enumeration is `DEFENDED` + `TEST-BACKED` (`ucns.canonical_factorization`, `docs/canonical-factor-selection.md`). Canonical choice under `factor_search_v08` payload-catalogue semantics remains open. |
| Performance scaling for large catalogues | `FRONTIER`, narrowed | Sound support-pruning is `DEFENDED`; efficient search *within* the pruned lattice remains open. |
| External formal review | Open | Theorem N should receive mathematical pressure before stronger publication language. |

---

## 6. Deprecated or superseded claims

| Claim | Status | Replacement |
|---|---|---|
| Binary “solved / not solved” depth-2 language | Superseded | Status vocabulary distinguishing implementation, tests, proof, oracle, and frontier. |
| Theorem 8c as practically meaningful depth-3 symmetric completeness | Superseded / vacuous | Theorem N-style catalogue-sufficient frontier and asymmetric depth-3 examples. |
| The prior depth-indexed induction plan for Theorem N | Superseded | Depth-agnostic catalogue-sufficient theorem statement as a proof target. |
| Direct user import from `ucns_recursive` as preferred API | Deprecated for direct user imports | Use `ucns` and `ucns.a0_safe`; `ucns_recursive` remains a compatibility shim. |

---

## 7. v1.0 release claim

The recommended v1.0 wording is:

```text
UCNS v1.0.0 is a scoped, reproducible research release for catalogue-sufficient recursive factorization using the witness-matrix recursive quotient solver. It does not claim total general recursive primality, carrier widening, tractable catalogue discovery, a canonical factor-choice procedure, or a fully discharged Lean proof of Theorem N.
```

## hmmm
