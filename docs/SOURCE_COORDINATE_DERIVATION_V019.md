# UCNS v0.19 ordered-source coordinate derivation boundary

**Status:** implemented, test-backed candidate law; nonselecting and
trace-local. The package derives exact signed-local circle-candidate
coordinates from authority-bound complete finite ordered source-occurrence
addresses. It does
not select this law, compose coordinates across scopes or higher gonols,
complete the Structural Null topology, or activate EDCM or METAPAT.

**Depends on:**

- EXPLICIT_GEOMETRIC_ASSIGNMENT_BOUNDARY_V018.md;
- GONOL_INITIATION_STRUCTURAL_NULL_V017.md;
- ASSIGNMENT_ADMISSION_BOUNDARY_V016.md;
- EXACT_COORDINATE_BOUNDARY_V011.md; and
- EDCM_A0_BETATEST_RECOVERY_REFERENCE.md.

## Question

v0.18 proved that an independently supplied exact rational proposal can enter
the surviving signed-local circle candidate without being confused with
source derivation. v0.19 asks the next bounded question:

> Can one transparent rule derive exact coordinate input from retained source
> structure while preserving complete scope, order, multiplicity, exact
> initiation identity, blockers, rendering loss, and nonselection?

Yes, within one complete finite ordered v0.17 trace whose exhaustion,
cardinality, and ordered outcome identities are carried by a producer-issued
receipt derived from the exact validated v0.17 authority report. Callers cannot
mint those authority fields inline. The candidate is the ordered-cell midpoint
law. The current trace-level issuer is intentionally limited to the fixed full
three-outcome v0.17 producer demonstration. Another source scope requires a new
versioned producer-owned declaration rather than a caller-constructed report.

## Domain claims

### Ordered-source cell midpoint

    surface_form: ordered-source cell midpoint coordinate
    term_id: ucns.edcm_assignment.ordered_source_cell_midpoint
    claiming_domain: UCNS EDCM source-coordinate research
    claimed_sense: exact coordinate input derived from one occurrence index and
      the authority-bound cardinality of its complete finite ordered initiation
      trace
    scope: indices 0 <= i < n for producer-receipted complete finite n > 0
    claim_type: specialized
    authority_source: this specification and src/ucns/source_coordinate.py
    status: provisional
    included_uses:
      - exact p=(2*i+1)/(2*n)
      - exact u=2*p-1
      - exact lifted turns t=2*p
      - order and multiplicity preservation
      - explicit upstream blockers
    excluded_uses:
      - source content or digest as geometry
      - cross-scope or higher-gonol composition
      - semantic coordinate adequacy
      - canonical selection
      - higher geometry or completion
    neighboring_terms:
      - ucns.edcm_assignment.source_to_coordinate_candidate
      - ucns.edcm_assignment.canonical_source_coordinate_law
    known_collisions:
      - midpoint coordinates inferred from an unbound or sampled tuple length
    effective_version: 0.19.0
    supersedes: none
    unresolved:
      - comparative selection
      - cross-scope and higher-gonol composition

### Source-to-coordinate candidate law

    surface_form: source-to-coordinate candidate law
    term_id: ucns.edcm_assignment.source_to_coordinate_candidate
    claiming_domain: UCNS EDCM assignment and motion
    claimed_sense: a named falsifiable rule that maps retained source structure
      to exact coordinate input and records explicit failure when prerequisites
      are absent
    scope: producer-receipted complete finite v0.17 initiation traces
    claim_type: native
    authority_source: source_coordinate.py and SC01-SC10
    status: provisional
    included_uses:
      - exact source-address derivation
      - exact v0.17 trace and outcome object linkage
      - exact v0.11 circle-candidate application
      - unresolved and rejected upstream blockers
    excluded_uses:
      - selected or canonical law
      - arbitrary infinite scope
      - trace-prefix execution
      - transfer of EDCM measurement validity
    neighboring_terms:
      - ucns.edcm_assignment.explicit_coordinate_candidate_application
      - ucns.edcm_assignment.canonical_source_coordinate_law
    known_collisions:
      - one implemented candidate described as the universal selected law
    effective_version: 0.19.0
    supersedes: none
    unresolved:
      - comparative selection
      - cross-scope stability and higher-gonol composition

### Canonical source-coordinate law

    surface_form: canonical source-coordinate law
    term_id: ucns.edcm_assignment.canonical_source_coordinate_law
    claiming_domain: UCNS canonization
    claimed_sense: a separately selected law with evidence for its scope,
      alternatives, information loss, rollback, migration, and composition
    scope: future UCNS EDCM source-coordinate selection decisions
    claim_type: provisional
    authority_source: hmmm; no selection authority decision exists
    status: proposed
    included_uses:
      - future explicit selection decision
    excluded_uses:
      - automatic promotion from implementation or passing tests
    neighboring_terms:
      - ucns.edcm_assignment.ordered_source_cell_midpoint
      - ucns.edcm_assignment.source_to_coordinate_candidate
    known_collisions:
      - provisional midpoint candidate described as selected canon
    effective_version: hmmm
    supersedes: none
    unresolved:
      - cross-scope stability
      - higher-gonol composition
      - external evidence
      - migration and rollback

The phrase source-to-coordinate law is therefore qualified as candidate in
v0.19. The source derivation gap has an executable proposal; the selection and
composition gaps remain open.

## Exact law

For an authority-bound complete finite ordered scope containing n occurrences,
occurrence i with 0 <= i < n receives:

    p_i = (2*i + 1) / (2*n)
    u_i = 2*p_i - 1 = (2*i + 1 - n) / n
    t_i = 2*p_i = (2*i + 1) / n
    B_i = 1 + u_i/2

All arithmetic is Fraction-valued.

The source midpoint p lies strictly in (0,1), local transverse u lies strictly
in (-1,1), and lifted turns t lie strictly in (0,2). Native frame is positive
for t < 1 and reversed for t >= 1. Local side is the sign of u.

Within a fixed n, distinct indices have distinct p, u, and t. Therefore the
exact coordinate identity is injective over the declared ordered scope.

## Why this source evidence is admissible

The inputs are structural:

- exact occurrence index already retained by v0.16 and v0.17;
- a v0.17 producer-issued exhaustion receipt derived from the exact validated
  authority report, including source identity, receipt identity, exhaustion,
  scope identity, cardinality, and ordered outcome identities;
- the producer-owned fixed declaration of all three v0.17 demonstration
  admission ids and outcome ids;
- the exact full v0.16 admission trace and complete ordered v0.17 outcome
  evidence identities, including dispositions, evidence tuples, initiation
  receipts, and rejected substitutions;
- exact complete scope cardinality from that binding rather than tuple length;
- exact upstream trace and outcome objects;
- explicit initiated-word standing.

The following are not inputs:

- raw source content;
- content or subject digest;
- runtime hash, repr, or object identity;
- A0 Blake2 phase lanes;
- public-gonol carrier position alone;
- scalar metric projection;
- binary64 rendering; and
- caller-supplied authority strings, cardinality, or ordered outcome ids; and
- the supplied trace tuple length without a matching completion binding.

Equal-content occurrences therefore remain distinct because their occurrence
addresses differ, not because their content is hashed into geometry.

## Work graph

    exact validated v0.17 authority report
      -> producer-issued trace-exhaustion receipt
      -> complete-scope binding
      -> exact complete finite ordered v0.17 trace
      -> exact upstream outcome at occurrence i
         -> initiated word
            -> p=(2*i+1)/(2*n)
            -> u=2*p-1 and t=2*p
            -> v0.11 exact signed-local circle candidate
            -> candidate GeometricAssignment
            -> linked declared-loss binary64 rendering
         -> unresolved initiation
            -> blocked-unresolved
         -> rejected initiation
            -> blocked-rejected
      -> one complete ordered v0.19 outcome trace

No rewrapped prefix can reuse the complete-scope binding: the binding retains
the exact trace object and a receipt that the v0.17 producer derives from its
exact validated report, including the report-backed cardinality and ordered
outcome identities. A rewrapped prefix cannot be made into that authority
report, and the binding API accepts no caller-authored authority strings,
cardinality, or outcome ids. Consistently truncating both the v0.16 and v0.17
report layers also fails because the v0.17 authority report validates the fixed
full producer-owned admission trace and exact complete outcomes, not their ids
alone. Moving initiation to a different occurrence, altering evidence, or
changing a blocker therefore changes or invalidates the receipt. A distinct scope
requires a new versioned producer declaration and receipt; tuple length alone
never supplies completion.
Every result retains the binding and the exact upstream outcome object at its
original index.

## SC01-SC10 falsifiers

| ID | Obligation | Falsified when |
|---|---|---|
| SC01 | authority-bound complete ordered source address | the completion binding is absent or mismatched, or index/cardinality is invalid or taken from an unbound prefix |
| SC02 | exact fixed law | midpoint, transverse, lifted-turn formula, version, or code reference changes |
| SC03 | within-scope injectivity | two distinct indices in one scope receive the same exact coordinate |
| SC04 | reversible exact application | B(u), inverse, frame, side, or assignment law identity diverges |
| SC05 | total exclusive outcomes | an upstream outcome is omitted, duplicated, reordered, or given multiple tags |
| SC06 | identity shortcuts remain negative | content, digest, runtime identity, A0 lanes, carrier position, or projection creates geometry |
| SC07 | exact upstream identity | a copied, substituted, prefixed, or reordered upstream graph is accepted |
| SC08 | rendering firewall | binary64 replaces exact rational identity |
| SC09 | nonselection | implementation is described as canonical or selected, or cross-scope composition is assumed |
| SC10 | broader incompletion | derivation is relabeled as total topology, higher geometry, completion, or consumer activation |

SC01-SC03, SC05, and SC07 have exact implemented support. SC04 retains the
bounded upstream exact circle candidate. SC06 and SC08 are supported negative
results. SC09 and SC10 remain unresolved.

## Demonstration

The fixed v0.17 trace has cardinality three. Its initiated first occurrence has
i=0 and therefore:

    producer scope receipt id =
      dae7f32a36dc0203854e4d95dc649557b3a335f4c01201ee31fa7510683f728b
    complete ordered trace evidence SHA-256 =
      f28fadda197c8d3492b2fe0f0999198aeca7a62bb7836b8cbdfad348a8428cbf

    p = 1/6
    u = -2/3
    t = 1/3
    B = 2/3
    frame = positive-local-frame
    side = local-negative

The second upstream outcome remains blocked-unresolved. The third remains
blocked-rejected. The v0.18 hand-authored value u=1/3 remains a separate
nonselected application witness and is not silently rewritten as source
derivation.

## Claims and nonclaims

v0.19 claims:

- a concrete source-to-coordinate candidate is executable;
- its finite ordered-scope formula is exact and injective;
- completion authority, complete source scope, order, multiplicity, initiation
  identity, and blockers remain recoverable;
- the concrete receipt is issued and verified against the exact in-process
  v0.17 producer report and complete ordered outcome evidence rather than
  self-reported binding fields or ids alone;
- the exact signed-local circle candidate is applied reversibly; and
- rendering and selection firewalls remain active.

v0.19 does not claim:

- that the midpoint law is selected, canonical, or semantically ideal;
- cross-turn, cross-corpus, or higher-gonol coordinate stability;
- total Structural Null topology;
- epicycle, disk, sphere, or recursive scale transitions;
- scoped completion;
- canonical faithful breadth;
- EDCM or METAPAT activation; or
- universal UCNS authority transfer.

## hmmm

The candidate supplies an exact trace-local answer, but a change in scope
cardinality changes every midpoint. That is visible evidence, not something to
hide. Cross-scope stability and higher-gonol composition therefore remain the
next geometric obligations. Candidate selection also requires separate
evidence, alternatives, rollback, and migration.
The in-process receipt verifies the exact v0.17 producer report and prevents
callers from self-reporting scope fields. Trust in external producers and
cryptographic authentication across storage or transport remain separate
obligations. The current issuer supports only the fixed v0.17 demonstration;
general producer enrollment is not silently inferred from constructible report
objects.
