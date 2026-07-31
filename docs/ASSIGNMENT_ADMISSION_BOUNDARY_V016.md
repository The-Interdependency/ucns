# UCNS v0.16 observed-element assignment admission boundary

**Status:** implemented, test-backed, nonselecting evidence boundary. This
package defines admission and a total tagged assignment-*outcome* relation over
explicitly adapted occurrences. It does not define a universal geometric
assignment law or a total Structural Null-to-carrier relationship.

**Depends on:**

- [`EDCM_A0_BETATEST_RECOVERY_REFERENCE.md`](EDCM_A0_BETATEST_RECOVERY_REFERENCE.md);
- [`edcm-a0-betatest-recovery-reference-v1.json`](edcm-a0-betatest-recovery-reference-v1.json);
- [`EDCM_COMPLETION_MOTION_EVIDENCE.md`](EDCM_COMPLETION_MOTION_EVIDENCE.md);
- [`EXPERIMENT_MANIFESTS.md`](EXPERIMENT_MANIFESTS.md); and
- [`FULL_CARRIER_ATTACHMENT_EVIDENCE_V015.md`](FULL_CARRIER_ATTACHMENT_EVIDENCE_V015.md).

## Question

The recovery manifest lists `define-admission-from-unknowable-source-evidence`
before the missing circle, epicycle, disk, sphere, and completion laws. v0.15
still left arbitrary observed-element assignment unresolved.

v0.16 asks the narrower prior question:

> Can arbitrary-domain observed occurrences enter exact, ordered assignment
> evidence and receive one explicit outcome without deriving geometry from a
> digest or pretending that an assignment law has been recovered?

Yes. Admission and outcome recording are executable. Geometric assignment
remains unresolved except where a caller supplies an explicitly named
unresolved or experimental candidate relation.

## Domain claims

These claims bind the meaning-bearing terms before implementation.

### Observed-element admission

```yaml
surface_form: observed-element admission
term_id: ucns.assignment_evidence.observed_element_admission
claiming_domain: UCNS assignment-evidence research
claimed_sense: entry of one exact source occurrence into assignment research through a named versioned domain adapter, isolated subject snapshot, encoded bytes, source provenance, and occurrence identity
scope: v0.16 explicitly adapted arbitrary-domain occurrences
claim_type: specialized
authority_source: pinned A0 recovery open obligation plus existing ContentAdapter and SubjectRecord contracts
status: proposed
included_uses:
  - exact evidence identity
  - source and adapter provenance
  - repeated occurrence preservation
excluded_uses:
  - geometric coordinate derivation
  - canonical structural equivalence
  - successful assignment
neighboring_terms:
  - ucns.assignment_evidence.assignment_outcome
  - ucns.completion_motion.geometric_assignment
known_collisions:
  - admission treated as successful geometric assignment
effective_version: 0.16.0
supersedes: none
unresolved:
  - adapters for domains not yet represented
```

### Assignment outcome

```yaml
surface_form: assignment outcome
term_id: ucns.assignment_evidence.assignment_outcome
claiming_domain: UCNS assignment-evidence research
claimed_sense: one exclusive tagged receipt stating that an admitted occurrence has no law, has an explicitly supplied candidate relation, or encountered an explicitly rejected proposed mechanism
scope: v0.16 admitted occurrences
claim_type: specialized
authority_source: this specification
status: proposed
included_uses:
  - unresolved-no-law
  - explicit-supplied-candidate
  - rejected-mechanism
excluded_uses:
  - inferred default assignment
  - proof that a supplied relation is correct
  - carrier selection
neighboring_terms:
  - ucns.assignment_evidence.observed_element_admission
  - ucns.completion_motion.geometric_assignment
known_collisions:
  - outcome totality confused with total geometric assignment
effective_version: 0.16.0
supersedes: none
unresolved:
  - derivation and authority of a successful universal assignment law
```

### Total tagged assignment-evidence relation

```yaml
surface_form: total assignment-evidence relation
term_id: ucns.assignment_evidence.total_tagged_outcome_relation
claiming_domain: UCNS assignment-evidence research
claimed_sense: every occurrence already admitted through an explicit adapter has exactly one validated assignment outcome tag
scope: the explicit content-adapter-admitted domain only
claim_type: specialized
authority_source: this specification and src/ucns/assignment_boundary.py
status: proposed
included_uses:
  - exclusive outcome partition
  - fail-closed malformed combinations
  - ordered repeated occurrence receipts
excluded_uses:
  - total geometric assignment
  - total Structural Null initiation
  - totality over subjects for which no domain adapter exists
neighboring_terms:
  - ucns.carrier_relation.total_structural_null_relationship
  - ucns.completion_motion.geometric_assignment
known_collisions:
  - mathematical totality of the missing assignment function
effective_version: 0.16.0
supersedes: none
unresolved:
  - arbitrary observed-element geometric assignment law
```

The collision check is clear only because the qualifiers `evidence`, `tagged`,
and `over admitted occurrences` are load-bearing. Removing them would create a
domain collision with the unresolved geometric assignment function.

## A0 recovery verdict

The exact pinned A0 files were inspected at commit
`7af8debf6ef3905f01baff02b43d8c3bee16ccbc`.

The specimen preserves useful architecture:

- ordered noncommutative composition;
- explicit chirality evidence;
- recursive grain and disk stacking;
- full-field inscription; and
- an emitted SPACE/ZERO seam event.

It does not supply the missing law. `ucns_embed.py` maps text to 53 lanes by
Blake2, reduces each lane to an ordinary `2π` fraction, and derives chirality
from the sign of sine. `gonal_inscription.py` also uses digest whitening and
hash-derived private rotation. The recovery manifest expressly rejects these
as the final assignment law.

Therefore v0.16 records the exact negative result:

```text
A0 architecture clues: retained historical evidence
A0 Blake2 phase lanes: rejected as universal assignment law
content digest: evidence identity only
arbitrary geometry: unresolved
```

## Executable evidence flow

```text
arbitrary-domain source occurrence
  -> explicit ContentAdapter(name, version, code reference)
  -> isolated SubjectRecord(snapshot, bytes, digest)
  -> ObservedElementAdmission(source, grain, occurrence, provenance)
  -> exactly one AssignmentOutcomeReceipt
       unresolved-no-law
       | explicit-supplied-candidate
       | rejected-mechanism
```

The subject digest is carried as evidence identity. It has no path to a
transverse, angular, radial, orientation, sidedness, or motion field.

Equal content may produce equal subject digests. It still produces distinct
admission and receipt identities at distinct occurrence indexes. The trace
retains input order and does not sort, deduplicate, normalize, or flatten.

## Supplied candidate boundary

A caller may attach a `GeometricAssignment` only as explicit supplied evidence.
That object must continue to name:

- relation identity;
- geometry kind;
- assignment-law identity and version;
- `unresolved` or `experiment-candidate` standing;
- orientation and sidedness;
- parameters; and
- evidence.

The v0.16 container validates linkage and evidence shape. It neither executes
the candidate law nor proves that the relation is true. No canonical standing
exists in the accepted `LawStanding` vocabulary.

## Rejected mechanisms

The fixed rejection vocabulary covers:

- A0 Blake2-derived phase lanes;
- content digest to geometry;
- runtime hash to geometry;
- `repr` to geometry; and
- object identity to geometry.

These values may appear only in a `rejected-mechanism` receipt. Such a receipt
cannot carry `GeometricAssignment`.

## AA01-AA07 falsifiers

| ID | Obligation | Falsified when |
|---|---|---|
| `AA01` | explicit adapter admission | arbitrary objects are hashed, represented, or identified without a named versioned adapter and isolated snapshot |
| `AA02` | occurrence preservation | equal content is deduplicated, sorted, reordered, or merged |
| `AA03` | total exclusive outcome | an admitted occurrence has zero or multiple outcome tags, or malformed combinations are accepted |
| `AA04` | evidence identity is not geometry | digest, runtime hash, `repr`, or object identity generates any geometric field |
| `AA05` | A0 prototype does not transfer | Blake2 lanes, fixed lane count, ordinary `2π`, or sine-sign chirality is promoted as the recovered law |
| `AA06` | supplied candidate remains bounded | supplied evidence becomes derived, canonical, selected, or silently defaulted |
| `AA07` | unresolved global boundary stays visible | outcome totality is relabeled as arbitrary geometric assignment or a total Structural Null relationship |

The report records `AA01`–`AA03` and `AA06` as exact implemented support,
`AA04`–`AA05` as supported negative results, and `AA07` as unresolved.

## Standing

```text
observed-element admission:       implemented-explicit-adapter-domain
assignment outcome relation:      total-tagged-over-admitted-occurrences
arbitrary geometric assignment:   unresolved-no-derived-law
non-null carrier evidence:        unchanged v0.15 analytic certificates
Structural Null attachment:       unchanged v0.13 partial root attachment
complete carrier relationship:    inconclusive-without-arbitrary-element-assignment
selection effect:                 none
EDCM activation:                  inactive
METAPAT activation:               inactive
```

## hmmm

- The exact law assigning an arbitrary observed element to circle, epicycle,
  disk, or sphere geometry remains unresolved.
- Adapter and subject digests are evidence identities only; they cannot supply
  transverse, angular, radial, orientation, or sidedness coordinates.
- The total topology and initiation relation from Structural Null to arbitrary
  non-null states remains unresolved.
- Explicit supplied candidate relations still require independent derivation,
  falsification, and authority before selection.
- Higher-gonol composition, scoped completion, canonical `B`, proof-assistant
  formalization, and carrier selection remain unresolved.
