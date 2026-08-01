# UCNS v0.18 explicit geometric-assignment boundary

**Status:** implemented, test-backed, nonselecting candidate-application
boundary. This package can apply the surviving exact signed-local circle
candidate to any explicitly initiated word occurrence when a caller supplies
independent exact rational coordinate evidence. It does not derive those
coordinates from arbitrary source evidence and therefore does not establish a
universal arbitrary-element assignment law.

**Depends on:**

- [`GONOL_INITIATION_STRUCTURAL_NULL_V017.md`](GONOL_INITIATION_STRUCTURAL_NULL_V017.md);
- [`ASSIGNMENT_ADMISSION_BOUNDARY_V016.md`](ASSIGNMENT_ADMISSION_BOUNDARY_V016.md);
- [`FULL_CARRIER_ATTACHMENT_EVIDENCE_V015.md`](FULL_CARRIER_ATTACHMENT_EVIDENCE_V015.md);
- [`EXACT_COORDINATE_BOUNDARY_V011.md`](EXACT_COORDINATE_BOUNDARY_V011.md); and
- [`EDCM_A0_BETATEST_RECOVERY_REFERENCE.md`](EDCM_A0_BETATEST_RECOVERY_REFERENCE.md).

## Question

v0.17 made the causal Structural Null-to-word doorway executable while keeping
geometry absent. v0.11 had already retained one exact, reversible signed-local
circle-coordinate candidate. v0.18 asks the narrow next question:

> Can the exact candidate be applied to every explicitly initiated word for
> which independent exact coordinate input is supplied, while source identity,
> lossy rendering, total topology, completion, and selection remain separate?

Yes. Candidate application is now executable and falsifiable. The missing law
that chooses or derives coordinate input from arbitrary source evidence remains
unresolved.

## Domain claims

These claims bind the meaning-bearing terms before provenance or implementation
is used as evidence.

### Explicit coordinate candidate application

```yaml
surface_form: explicit coordinate candidate application
term_id: ucns.edcm_assignment.explicit_coordinate_candidate_application
claiming_domain: UCNS EDCM geometric-assignment research
claimed_sense: application of the surviving signed-local exact circle-coordinate candidate to one explicitly initiated word occurrence using independently supplied exact rational transverse and lifted-turn input
scope: v0.18 GonolInitiationReceipt values and Fraction-valued proposals
claim_type: specialized
authority_source: v0.11 exact candidate evidence joined to v0.17 initiation evidence by src/ucns/explicit_geometric_assignment.py
status: implemented
included_uses:
  - exact B(u)=1+u/2 candidate mapping
  - exact inverse u=2*(B-1)
  - normalized lifted turns in [0,2)
  - native two-turn frame parity
  - local side from the sign of exact u
  - one candidate GeometricAssignment
excluded_uses:
  - derivation from source content or identity
  - canonical faithful breadth
  - carrier or coordinate selection
  - higher geometry or completion
neighboring_terms:
  - ucns.edcm_assignment.source_to_coordinate_law
  - ucns.assignment_evidence.observed_element_admission
  - ucns.edcm_origin.gonol_initiation
known_collisions:
  - explicit candidate application described as universal arbitrary-element assignment
effective_version: 0.18.0
supersedes: none
unresolved:
  - why a particular source occurrence should receive a particular exact coordinate
```

### Exact candidate coordinate identity

```yaml
surface_form: exact candidate coordinate identity
term_id: ucns.edcm_assignment.exact_candidate_coordinate_identity
claiming_domain: UCNS signed-local circle-candidate evidence
claimed_sense: the Fraction-valued local transverse, breadth, and normalized lifted-turn tuple retained as authoritative candidate evidence for one explicit proposal
scope: v0.18 application of the v0.11 signed-local candidate
claim_type: specialized
authority_source: src/ucns/exact_coordinate.py and src/ucns/explicit_geometric_assignment.py
status: implemented-candidate
included_uses:
  - reversible rational evidence
  - frame and local-side validation
  - linked lossy binary64 rendering
excluded_uses:
  - binary64 point as exact identity
  - proof of canonical B
  - source-derived geometry
neighboring_terms:
  - ucns.rendering.binary64_carrier_point
known_collisions:
  - rendered coordinate treated as exact coordinate identity
effective_version: 0.18.0
supersedes: none
unresolved:
  - selection standing of the signed-local candidate
```

### Source-to-coordinate law

```yaml
surface_form: source-to-coordinate law
term_id: ucns.edcm_assignment.source_to_coordinate_law
claiming_domain: UCNS EDCM assignment and motion
claimed_sense: an evidence-supported rule deriving exact geometric coordinate input from an arbitrary admitted source occurrence while retaining provenance, orientation, sidedness, scale, and failure behavior
scope: arbitrary source evidence after explicit admission and gonol initiation
claim_type: native
authority_source: UCNS completion-motion root and open v0.18 obligation
status: unresolved
included_uses:
  - future lawful coordinate derivation or explicit partial failure
excluded_uses:
  - digest angles
  - A0 Blake2 phase lanes as transferred authority
  - object identity or repr
  - carrier position alone
  - scalar projection
  - externally supplied value relabeled as derived
neighboring_terms:
  - ucns.edcm_assignment.explicit_coordinate_candidate_application
known_collisions:
  - assignment input confused with assignment derivation
effective_version: 0.18.0
supersedes: none
unresolved:
  - complete law
  - transition to higher geometry
  - failure and non-completion semantics
```

The collision check is clear only when the phrase **explicit-input candidate
application** is retained. Bare **arbitrary-element assignment** collides with
the unresolved universal source-to-coordinate derivation and must not describe
the implemented v0.18 scope.

## Exact work graph

```text
v0.16 explicit adapter admission
  -> v0.17 explicit word-gonol initiation
       -> independent exact coordinate proposal
            local transverse u in [-1,1]
            lifted turns t normalized to [0,2)
            derived_from_evidence_identity = false
       -> v0.11 signed-local candidate application
            B(u) = 1 + u/2
            inverse u = 2*(B-1)
            frame = positive for t in [0,1), reversed for t in [1,2)
            side = sign(u)
       -> candidate GeometricAssignment(CIRCLE)
       -> linked lossy binary64 rendering
       -> exactly one v0.18 outcome
            assigned | unresolved | rejected
```

The graph has no edge from source digest, runtime identity, A0 lane, carrier
position, scalar projection, or binary64 rendering to coordinate input.

## Candidate relation

The implemented relation has fixed evidence identity:

```text
geometry:             CIRCLE
law id:               ucns.edcm.explicit-signed-local-circle-assignment
law version:          0.18.0
law standing:         candidate
orientation:          native Möbius frame
sidedness:            sign of exact local transverse u
parameters:           candidate id, u, B(u), lifted turns, input role
completion:           not registered
parent gonols:         none
selection effect:     none
```

Two equal-content occurrences remain two occurrences. They may receive distinct
independent exact proposals without changing their equal content digests. This
demonstrates that evidence identity is retained but does not determine geometry.

## GA01-GA09 falsifiers

| ID | Obligation | Falsified when |
|---|---|---|
| `GA01` | exact initiation linkage | an assignment loses or substitutes its v0.17 admission, word-gonol, boundary, or twist receipt |
| `GA02` | independent exact input | coordinate input is non-rational, hidden, or marked as derived from evidence identity |
| `GA03` | exact reversible candidate | `B(u)=1+u/2`, normalized turns, exact inverse, candidate id, or candidate standing is altered |
| `GA04` | frame and side preservation | native two-turn frame parity or the sign-derived local side is changed |
| `GA05` | total exclusive ordered outcomes | a v0.17 occurrence has no tag, multiple tags, reordered identity, deduplication, or a malformed combination |
| `GA06` | rendering firewall | binary64 rendering replaces exact rational identity or loses its source/policy link |
| `GA07` | rejected shortcuts remain negative | digest, A0 lanes, runtime identity, carrier position, scalar projection, or invalid upstream state creates an applied assignment |
| `GA08` | unresolved derivation stays visible | explicit input is relabeled as a universal source-to-coordinate derivation |
| `GA09` | broader incompletion stays visible | circle entry is relabeled as total Structural Null topology, higher geometry, composition, completion, selection, or consumer activation |

`GA01`, `GA02`, `GA05` are exact implemented support. `GA03` and `GA04`
retain bounded upstream candidate support. `GA06` and `GA07` are supported
negative results. `GA08` and `GA09` remain unresolved.

## Demonstration report

The fixed experiment preserves the three v0.17 outcomes in order:

1. the initiated word receives an independent proposal `u=1/3`, `t=0` and one
   exact circle-candidate assignment;
2. the unresolved upstream occurrence remains unresolved without a proposal;
3. the invalid origin substitution remains a named rejected mechanism.

The demonstration shows outcome plumbing and boundary enforcement. It is not
empirical support for the proposal value and does not select a law.

## Claims and nonclaims

v0.18 claims:

- explicit exact coordinate proposals can be validated and applied to any
  explicitly initiated word occurrence;
- the signed-local candidate and inverse remain exact within their declared
  domain;
- native frame, local side, occurrence order, exact identity, and rendering
  loss remain inspectable;
- all v0.17 outcomes receive one exclusive ordered v0.18 outcome.

v0.18 does not claim:

- a law deriving coordinate input from arbitrary source evidence;
- that the signed-local candidate is canonical or selected;
- a total topology from Structural Null to arbitrary non-null states;
- epicycle, disk, sphere, or recursive-scale transition laws;
- higher-gonol composition;
- scoped completion or honest non-completion receipts;
- EDCM or METAPAT activation;
- authority, theorem, measurement, or semantic transfer.

## Standing

```text
explicit-input candidate application: implemented and test-backed
signed-local exact law:               surviving nonselected candidate
source-to-coordinate derivation:      unresolved
binary64 coordinate identity:         rejected; rendering only
outcome relation:                     total tagged over v0.17 outcomes
total Structural Null topology:       unresolved
higher geometry and composition:      unresolved
scoped completion:                    not registered
selection effect:                     none
EDCM activation:                      inactive
METAPAT activation:                   inactive
```

## hmmm

- The law deriving exact transverse and lifted-turn coordinates from arbitrary
  source evidence remains unresolved.
- An explicit proposal makes application executable but does not prove that its
  value is the lawful source assignment.
- The total topology from singular Structural Null to arbitrary non-null
  carrier states remains unresolved.
- Circle-to-epicycle, epicycle-to-disk, disk-to-sphere, recursive scale, and
  higher-gonol composition laws remain unresolved.
- Scoped completion, canonical `B`, proof-assistant formalization, carrier
  selection, EDCM activation, and METAPAT activation remain unresolved.
