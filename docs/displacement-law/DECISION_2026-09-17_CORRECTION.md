# UCNS displacement-law corrective decision — 2026-09-17

This receipt supersedes the selection standing recorded in
`DECISION_2026-09-16.md`. The original bytes remain recoverable in Git history
and remain historical evidence of the ratification attempt; its selected
standings are no longer active.

```text
decision_id: ucns-displacement-selection-correction-2026-09-17
scope: displacement-law candidate behavior under the preregistered control set
authority: Erin Spencer
prior_decision: ucns-displacement-survivors-2026-09-16
prior_source_head: fc1166697d49c132a0812197100282d08cd8d132
prior_falsification_receipt_sha256: d2a750f60e68375b0141b5e9eb4630e35d5c617b726fdbdd8b996ae5bdcc1aa9
comparison_policy: hard gates are noncompensable; required evidence must be complete before selection
candidate_set:
  - ordered-concatenation
  - placement-frame
  - composite-displacement
selected_set: none
terminal_standings:
  ordered-concatenation: BLOCKED
  placement-frame: REJECTED
  composite-displacement: REJECTED
```

## Why the prior selection is withdrawn

Post-merge exact review found two load-bearing defects in the evidence used by
the 2026-09-16 decision.

1. The preregistration requires a permutation control using the same residues
   under a **known modular-orbit action**. The harness instead rotated the three
   channel positions. That diagnostic does not satisfy the frozen control, so
   required selection evidence is incomplete.
2. `placement-frame` fails the frame hard gate. The composite carries that
   failed sub-candidate, but the old harness marked the composite frame control
   successful using only `ordered-concatenation`. A hard-gate failure cannot be
   compensated by another component's survival.

The earlier decision also renamed the registered `placement-frame` candidate as
`placement-frame ordinal-only angle`. The registered identity is restored here;
the failed ordinal-angle behavior is evidence about that candidate, not a new
candidate identity.

## Current standing

- `ordered-concatenation` retains useful implemented evidence but is `BLOCKED`
  from selection until the preregistered modular-orbit control has a frozen
  comparison criterion, executes, and replays completely.
- `placement-frame` is `REJECTED` for this decision boundary because it fails
  the frame hard gate.
- `composite-displacement` is `REJECTED` for this decision boundary because it
  carries the same failed frame component and may not bypass the hard gate.

The public candidate registry therefore correctly remains at candidate standing;
no machine-readable selection should be projected from the superseded receipt.

## Claims not authorized

This correction selects no universal or scoped displacement law. It establishes
no prime-arity successor or ladder, PCEA security property, EDCM measurement
validity, physical interpretation, theorem, or cross-repository status transfer.

## Required next evidence

Before any new displacement selection:

1. define the exact modular-orbit action and the expected comparison criterion
   without inspecting its outcome;
2. execute that frozen control against every admissible candidate;
3. propagate every hard-gate failure through composite constructions;
4. independently replay the complete declared scope; and
5. issue a new scoped decision receipt only after those evidence gates close.

## hmmm

The preregistration says what action class the missing control must use, but it
does not yet state enough to invent the expected candidate relation safely.
That criterion remains `hmmm` until it is frozen before execution. A missing
ruler does not become a passing measurement because the tape measure was handy.
