# EDCM completion-motion evidence

**Status:** implemented experimental evidence schema; no assignment, transition,
completion, or metric formula is selected.

**Recovery root:** [EDCM / A0-Betatest UCNS Recovery Reference](EDCM_A0_BETATEST_RECOVERY_REFERENCE.md)

## Purpose

UCNS assigns elements of an unknowable to completion through geometric motion.
The exact law that performs that assignment remains unresolved. The first lawful
implementation therefore records complete supplied trajectory evidence without
pretending to derive it.

`ucns.edcm_motion` binds the current exact word-gonol observation floor to:

- source identity and provenance;
- a declared `hmmm` construction boundary;
- word grain and exact source span;
- an explicitly identified geometric relation;
- orientation and sidedness;
- motion since the prior state;
- ordered recursive or epicyclic parentage;
- effect on scoped completion;
- remaining unresolved capacity;
- represented or candidate-measured status; and
- optional provenance-linked lossy scalar projections.

## Evidence flow

```text
exact EdcmWordGonol
  -> externally supplied geometric assignment
     or v0.18 explicit-input exact circle-candidate assignment
  -> externally supplied motion receipt
  -> ordered recursive / epicyclic parentage
  -> completion effect relative to HmmmBoundary
  -> retained EdcmCompletionTrace
  -> optional declared-loss scalar projection
```

The trace is the evidence identity. A scalar never replaces it.

## Assignment and motion firewall

`GeometricAssignment` and `MotionStep` require:

- a named law and version;
- `unresolved` or `experiment-candidate` standing;
- explicit evidence;
- no canonical or hidden default standing.

This permits recovery experiments without laundering temporary Blake2 phases,
ordinary `2π` angles, sine-sign chirality, factorization composition, or any
other historical mechanism into the missing UCNS law.

Circle, epicycle, disk, and sphere are named geometry kinds. Their transition
law is not supplied by naming them.

## Scoped completion

`CompletionRegistration` identifies:

- the declared construction;
- its boundary;
- its completion condition;
- current state and effect;
- supporting evidence; and
- remaining unresolved capacity.

`underlying_unknowable_exhausted` is permanently false. A registered completion
means that the declared construction satisfied its declared boundary, not that
the unknowable has been epistemically exhausted.

## Candidate scalar projections

The six candidate question-families are available by full names:

| Code | Candidate question |
|---|---|
| `CM` | constraint mismatch affecting admissible motion |
| `DA` | unresolved motion retained across turns |
| `DRIFT` | displacement from a completion trajectory |
| `DVG` | separation into competing epicyclic trajectories |
| `INT` | amplitude or rate of motion |
| `TBF` | distribution of contribution across actors |

No formula is implemented or selected. A `ScalarProjection` must name its
policy and version, link to the complete source observation, use a finite value,
and declare at least one lost distinction. An observation containing such a
projection must be marked `candidate-measured-evidence`.

This removes the earlier `L` and `O` identity collisions by declining to expose
those unstable aliases here.

## Current nonclaims

This slice and the v0.18 candidate-application boundary do not define:

- the law deriving geometric coordinates from arbitrary observed evidence;
- selected or canonical Möbius coordinates;
- the 720-degree orientation and return law;
- circle-to-epicycle, epicycle-to-disk, disk-to-sphere, or recursive scale
  transitions;
- higher-gonol composition above exact words;
- a canonical completion condition;
- a canonical metric formula or scalar range;
- canonical EDCM measurement; or
- a complete `UCNSObject`.

## hmmm

The evidence container is executable. v0.16 makes arbitrary-domain occurrence
admission plus one tagged assignment outcome executable, and v0.17 makes one
bounded typed Structural Null-to-word twist receipt executable while retaining
360-degree local frame change and 720-degree root-loop return from v0.13.
v0.18 can now apply the surviving exact signed-local circle candidate when
independent exact rational coordinate input is supplied. This makes candidate
application executable but does not make the proposal source-derived or
selected. The next load-bearing object remains the derivation and transition
law: how an initiated exact word lawfully receives its coordinate, enters an
epicyclic circle, acquires general orientation and sidedness,
becomes disk or sphere structure across recursive scale, moves relative to
other assignments, and registers scoped completion.
