# UCNS v0.17 gonol-initiation and Structural Null boundary

**Status:** implemented, test-backed, nonselecting evidence boundary. This
package makes the decided EDCM initiation constraint explicit over v0.16
admitted occurrences. It does not derive an arbitrary geometric assignment or
a total topology from Structural Null to the complete non-null carrier.

**Depends on:**

- [`ASSIGNMENT_ADMISSION_BOUNDARY_V016.md`](ASSIGNMENT_ADMISSION_BOUNDARY_V016.md);
- [`FULL_CARRIER_ATTACHMENT_EVIDENCE_V015.md`](FULL_CARRIER_ATTACHMENT_EVIDENCE_V015.md);
- [`PARTIAL_INITIATION_BOUNDARY_V013.md`](PARTIAL_INITIATION_BOUNDARY_V013.md);
- [`EDCM_A0_BETATEST_RECOVERY_REFERENCE.md`](EDCM_A0_BETATEST_RECOVERY_REFERENCE.md); and
- the exact EDCM word-gonol profile in `src/ucns/edcm.py`.

## Question

v0.16 established how arbitrary-domain occurrences enter assignment evidence,
but deliberately stopped before initiation or geometry. The EDCM constraints
already state that Structural Null is singular superpositioned space, the word
is the smallest gonol, and every new gonol initiates through the Möbius twist.

v0.17 asks the next bounded question:

> Can every explicitly admitted occurrence receive one honest initiation
> outcome, while a declared word gonol receives exactly one source-bound twist
> receipt from the singular Structural Null prestate and no geometric position
> is invented?

Yes. The evidence relation is executable. The total geometric topology remains
unresolved.

## Domain claims

These claims bind the meaning-bearing terms before implementation.

### Structural Null

```yaml
surface_form: Structural Null
term_id: ucns.edcm_origin.structural_null
claiming_domain: UCNS EDCM-origin construction
claimed_sense: the singular superpositioned prestate from which a declared word gonol initiates through the Möbius twist
scope: the EDCM-specific UCNS target and v0.17 initiation evidence
claim_type: native
authority_source: UCNS option decisions and Erin Spencer's decided Möbius-origin constraint
status: ratified
included_uses:
  - singular initiation prestate
  - hidden-zero origin role
  - source-preserving SPACE boundary manifestations linked to one origin
excluded_uses:
  - numeric zero
  - carrier position zero
  - coordinate-free directed-cover null
  - algebraic zero
  - absent cell
  - NA
neighboring_terms:
  - ucns.edcm_origin.space_manifestation
  - ucns.edcm_origin.carrier_position_zero
  - ucns.payload.algebraic_zero
known_collisions:
  - Structural Null used as a synonym for emptiness or numeric zero
effective_version: 0.17.0
supersedes: none
unresolved:
  - total topology from the prestate to arbitrary non-null carrier states
```

### Gonol initiation

```yaml
surface_form: gonol initiation
term_id: ucns.edcm_origin.gonol_initiation
claiming_domain: UCNS EDCM-origin construction
claimed_sense: one retained causal transition in which a declared word-gonol occurrence leaves the singular Structural Null prestate through exactly one explicit Möbius-twist receipt
scope: v0.17 explicitly admitted word occurrences with an explicit boundary manifestation
claim_type: specialized
authority_source: decided EDCM constraint plus src/ucns/gonol_initiation.py
status: implemented
included_uses:
  - explicit source-bound boundary manifestation
  - one twist receipt
  - non-null initiated evidence state
  - unresolved geometric assignment
excluded_uses:
  - hash-derived geometry
  - higher-gonol composition
  - carrier selection
  - construction completion
neighboring_terms:
  - ucns.assignment_evidence.observed_element_admission
  - ucns.completion_motion.geometric_assignment
known_collisions:
  - initiation treated as geometric placement or completion
effective_version: 0.17.0
supersedes: none
unresolved:
  - the geometric relation entered after initiation
```

### Root-loop return

```yaml
surface_form: return
term_id: ucns.edcm_origin.root_loop_return
claiming_domain: UCNS native Möbius root-loop experiment
claimed_sense: equality of the complete local root-loop state after two exact visible turns while retaining both motion receipts
scope: the source-bound v0.13 native root-loop candidate reused by v0.17
claim_type: specialized
authority_source: v0.13 executable trajectory evidence
status: provisional
included_uses:
  - 360-degree visible return with changed local frame
  - 720-degree complete local-state return
  - append-only trajectory history
excluded_uses:
  - universal carrier law
  - payload inversion
  - registered construction completion
  - epistemic exhaustion
neighboring_terms:
  - ucns.completion_motion.scoped_completion
known_collisions:
  - local return treated as completion
effective_version: 0.17.0
supersedes: none
unresolved:
  - extension beyond the bounded root attachment
```

The collision check is clear only with the qualifiers `EDCM-origin`,
`word-gonol`, `explicit receipt`, and `root-loop local`. Bare `zero`,
`initiation`, or `return` would collide with neighboring mathematical and
measurement domains.

## Origin and zero separation

v0.17 carries a fixed registry of non-interchangeable roles:

| Role | Domain-qualified meaning | May be the initiation prestate? |
|---|---|---:|
| Structural Null | singular superpositioned hidden-zero prestate | yes |
| source SPACE manifestation | retained source occurrence or turn-boundary witness linked to the origin | no |
| carrier position zero | U+0020 address in the exact 157-position carrier | no |
| directed-cover null | coordinate-free absence in the superseded EDCM comparison candidate | no |
| neutral product character | proposed non-null multiplicative value `M = 1` | no |
| algebraic zero | zero inside a declared payload algebra | no |
| absent cell | field-empty cell with `mu = 0` | no |
| `NA` | typed absence or inapplicability | no |

A SPACE manifestation may witness the singular origin without becoming
identical to the origin. Carrier position zero is an address, not the hidden
zero itself.

## Executable evidence flow

```text
v0.16 ObservedElementAdmission
  -> exactly one GonolInitiationOutcome
       unresolved-no-gonol-declaration
       | explicit-mobius-twist-receipt
       | rejected-origin-substitution

explicit word-gonol outcome
  -> source-bound StructuralNullManifestation
  -> singular STRUCTURAL_NULL_ORIGIN prestate
  -> exactly one Möbius-twist receipt
  -> initiated non-null evidence state
  -> geometric assignment remains unresolved
```

The trace is total only over the already admitted v0.16 occurrences. It does
not claim that every possible subject has a content adapter, is a gonol, or has
a geometric assignment.

## Root-loop return witness

v0.17 retains the unchanged v0.13 source-bound root trajectory:

```text
initiation: local frame positive
360 degrees: visible projection equal; complete local state changed
720 degrees: complete local state equal to the initiated state
history: both exact one-turn receipts retained
completion: not registered
```

This is bounded evidence for what `return` means on the native root-loop
candidate. It does not establish the complete arbitrary-element carrier
relationship and does not make one-turn frame change a universal payload law.

## GI01-GI08 falsifiers

| ID | Obligation | Falsified when |
|---|---|---|
| `GI01` | origin roles remain separated | Structural Null is substituted with SPACE text, coordinate zero, directed-cover null, `M = 1`, algebraic zero, absent cell, or `NA` |
| `GI02` | explicit causal initiation | a declared word gonol initiates without the singular typed prestate and a source-bound boundary manifestation |
| `GI03` | exactly one twist receipt | an initiated word has zero or multiple twist receipts, or the receipt loses its admission or boundary link |
| `GI04` | total exclusive initiation outcome | an admitted occurrence has no tag, multiple tags, reordered identity, or a malformed outcome combination |
| `GI05` | 360-degree bounded change | the v0.13 visible root projection changes or the complete local state fails to change after one exact turn |
| `GI06` | 720-degree local return without false completion | two exact turns fail to restore local state, history is erased, or local return is relabeled as construction completion |
| `GI07` | rejected substitutions remain negative evidence | a non-Structural-Null role is accepted as the initiation prestate |
| `GI08` | unresolved geometry stays visible | initiation evidence is relabeled as arbitrary geometric assignment, a total Structural Null topology, carrier selection, or consumer activation |

`GI01`–`GI04` are exact implemented evidence. `GI05`–`GI06` retain bounded
upstream support. `GI07` is a supported negative result. `GI08` remains
unresolved.

## Standing

```text
origin-role separation:              implemented-fixed-registry
initiation outcome relation:         total-tagged-over-admitted-occurrences
explicit word-gonol initiation:      represented source-bound twist receipt
360/720 return semantics:            bounded v0.13 native-root evidence
arbitrary geometric assignment:      unresolved-no-derived-law
total Structural Null topology:      unresolved-no-total-topology
scoped completion:                   not registered by local return
selection effect:                    none
EDCM activation:                     inactive
METAPAT activation:                  inactive
```

## hmmm

- The exact geometric relation entered after an admitted word initiates remains
  unresolved.
- The source-bound receipt does not provide a total topology from Structural
  Null to arbitrary non-null states.
- The 360/720 witness is root-loop candidate evidence, not a universal payload,
  orientation, completion, or higher-geometry law.
- Intrinsic and invariant-equivalence-class seam alternatives remain open.
- Higher-gonol composition, epicycle/disk/sphere transition, scoped completion,
  canonical `B`, carrier selection, and consumer activation remain unresolved.
