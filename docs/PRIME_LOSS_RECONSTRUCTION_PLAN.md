# P2/P3/P5/P7 relational loss reconstruction plan

**Status:** HYPOTHESIS / experiment plan  
**Result:** not run  
**Authority:** UCNS representation evidence only; no EDCM measurement or universal prime claim

## Question

Can independently constructed P2, P3, P5, and P7 relational views preserve enough complementary information that deliberately removed relational information can be reconstructed exactly and uniquely?

Distinguishability is not reconstruction. P5 and P7 are already distinguishable under exact invariants, but that does not establish that the family can recover loss.

## Hypotheses

### H1 — joint sufficiency

For a frozen relational object `X`, the complete P2/P3/P5/P7 view family uniquely reconstructs each preregistered single-relation erasure.

**SURVIVED** only if every frozen erasure has exactly one admissible reconstruction and it equals the hidden source relation.

**FALSIFIED** if any frozen erasure yields the wrong relation, no relation, or more than one admissible relation.

**UNRESOLVED** if a prerequisite, identity map, implementation, or resource boundary prevents the frozen test from completing.

### H2 — complementary contribution

Each of P2, P3, P5, and P7 contributes information unavailable from the other three on at least one frozen witness.

**SURVIVED** only if leave-one-view-out testing finds at least one witness for every view where removing that view changes a uniquely recoverable case into ambiguity or failure.

**FALSIFIED** for any view that is redundant across the complete frozen witness set.

Run H2 only if H1 survives.

### H3 — prime-family advantage

The P2/P3/P5/P7 family reconstructs relational loss better than a simpler representation with matched source information and comparable resource bounds.

**SURVIVED** only if the frozen prime-family criterion exceeds the frozen simple baseline on a preregistered adversarial set.

**FALSIFIED** if the simpler baseline matches or exceeds it.

Run H3 only if H1 and H2 survive.

## Prerequisites

1. Resolve P2 enough to emit one explicit candidate representation without changing ordinary arithmetic primality.
2. Construct P3 directly as its own artifact. Do not derive it by deleting or flattening P5/P7.
3. Keep P5 and P7 as direct constructions rather than construction lineage from lower views.
4. Define one source relational object with exact occurrence identities and a complete relation ledger.
5. Define explicit mappings between source relation identities and each view. Mapping metadata may align endpoints; it may not reveal the hidden relation value during recovery.
6. Freeze encoders, fixture identity, reconstruction policy, resource limits, baselines, and outcome criteria before erasure results are inspected.

Until P2 and P3 exist independently, the reconstruction claim remains `UNRESOLVED` and no downstream result may be promoted.

## Cheapest decisive experiment

### Stage A — single-view erasure

1. Encode the same complete source object independently as P2, P3, P5, and P7.
2. Verify all four complete views against the frozen source ledger.
3. For each preregistered target relation and target view, remove that relation from the target view only.
4. Give the reconstruction procedure the corrupted family, endpoint identity, frozen policies, and no source-ledger access.
5. Enumerate every relation consistent with the surviving evidence.
6. Record the candidate-set cardinality and reconstructed value.

The decisive invariant is:

```text
candidate_set == {hidden_source_relation}
```

A score, nearest match, or preferred candidate does not count as reconstruction.

### Stage B — structural erasure

Only if Stage A survives: remove the target relation value everywhere it is directly repeated while retaining its structural consequences. Test whether cross-view constraints still force one exact value.

This separates simple redundancy from structural reconstruction.

### Stage C — leave-one-view-out

Only if Stage B survives: repeat recovery after removing each complete view in turn. Record which losses become ambiguous. This tests whether 2, 3, 5, and 7 are complementary rather than merely different.

## Controls

Use at least:

- the source relation graph under a simpler typed representation;
- duplicated-view control with the same representation repeated four times;
- relation-label permutation negative control;
- endpoint-preserving but relation-destroying counterexamples;
- equal-content distinct-occurrence cases;
- reordered and partially missing structures;
- a resource-matched simple reconstruction policy.

If a simpler typed graph reconstructs the same frozen losses under the same information boundary, do not attribute reconstruction to prime geometry.

## Evidence receipt

Every run records:

```text
source identity
encoder identities and commits
P2/P3/P5/P7 view digests
erasure identity
allowed evidence
reconstruction policy
candidate set
expected hidden relation
result: FALSIFIED | SURVIVED | UNRESOLVED | BLOCKED | DEPRECATED
negative-control results
resource use
information loss
hmmm
```

No repair, retargeting, weakened criterion, or added hint is allowed before the frozen result is recorded.

## Stop rules

- H1 failure stops H2 and H3.
- P2/P3 prerequisite failure stops the experiment.
- Ambiguity counts as failure, not partial success.
- A simple baseline matching the prime family stops prime-specific reconstruction claims.
- Success establishes only survival on the declared fixture family, not general error correction, universal prime necessity, physical significance, consciousness claims, spectral claims, or zeta claims.

## If it survives

Extend in this order:

1. multiple simultaneous relation erasures;
2. larger and recursive relational objects;
3. multimodal typed relations from the UCNS multimodal-object work;
4. scale transitions and cross-scope composition;
5. externally authored adversarial fixtures.

## Usage guidance

Use this document to freeze the experiment before implementation. Implement prerequisites and the smallest Stage A fixture first. Do not begin Stage B, Stage C, or multimodal scaling until the prerequisite result survives.

## hmmm

- P2 closed-primitive standing remains unresolved.
- P3 does not yet have an independent direct artifact.
- The minimum source fixture that is nontrivial without smuggling the answer into cross-view identity metadata remains to be frozen.
- Whether any proper subset of P2/P3/P5/P7 is already sufficient is deliberately unknown and belongs to leave-one-view-out evidence.
- Whether prime-native views offer any reconstruction advantage over a simpler typed relation graph is deliberately unknown.