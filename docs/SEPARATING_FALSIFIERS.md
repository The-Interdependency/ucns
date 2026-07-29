# UCNS–EDCM v0.5 separating falsifiers

> **Status:** specification of future experiment evidence; this document adds no runtime tests and selects no carrier.
>
> **Purpose:** force the direct-Möbius, cover-chart, and incompatibility candidates to make different, inspectable claims while preserving failures and unresolved cases as evidence.

## 1. Verdict vocabulary

Every falsifier produces one of five verdicts:

| Verdict | Meaning |
|---|---|
| `supported` | The candidate supplied the required evidence for the declared witness domain. |
| `falsified` | A retained counterexample violates a candidate claim. |
| `inconclusive` | The current witness cannot distinguish the claim. |
| `unresolved` | A required law, map, equivalence, or representation has not been supplied. |
| `error` | Evaluation failed; the exception and partial evidence remain retained. |

`inconclusive`, `unresolved`, and `error` are not passing zero values. `supported` means admitted for further review, not canonical.

## 2. Minimum witness packet

A future implementation must preserve at least these exact speaker turns. Labels are descriptive; the literal source is authority.

| Witness | Exact source purpose |
|---|---|
| `W-empty` | empty speaker turn; no word initiation, one turn-level support unit |
| `W-first` | `A`; first word initiates from the declared turn-boundary hidden-zero condition |
| `W-space` | `A B`; literal U+0020 boundary and two word initiations |
| `W-nbsp` | `A B`; U+00A0 assigns to the same carrier origin while remaining textually distinct |
| `W-repeat-space` | `A  B`; both U+0020 occurrences survive even if the candidate uses a singular origin interface |
| `W-repeat-word` | `AB AB`; repeated equal word values remain distinct occurrences |
| `W-order-left` | `A B`; ordered composition witness |
| `W-order-right` | `B A`; operand-order counterwitness |
| `W-unassigned` | `A🙂B`; the emoji remains exact out-of-alphabet evidence rather than being dropped or normalized |

The packet must also contain synthetic complete-state witnesses for one declared start state `s`, its 360° advance, its 720° advance, and the inverse of each declared transition. Synthetic state evidence cannot replace the exact source witnesses; both are required.

A larger corpus may add evidence but cannot remove or rewrite these distinctions.

## 3. Foundational falsifiers

### F01 — null and zero separation

A candidate is falsified if it identifies any two of the following solely because they look empty or neutral: Structural Null / hidden zero, U+0030 DIGIT ZERO, algebraic zero, multiplicative unit, absent cell, empty turn, `NA`, unknown, unresolved, or unmeasured state.

Required evidence:

1. distinct typed identities;
2. explicit conversion rules, if any; and
3. a witness showing that a non-null retained distinction does not collapse when its payload is numerically zero.

### F02 — exact source reconstruction

For every witness, concatenating retained segments must reconstruct the exact source code points in exact order. UTF-8 input, when used, must round-trip byte-for-byte under strict decoding and encoding.

A candidate is falsified by normalization, trimming, replacement characters, whitespace collapse, deduplication, reordering, or silent deletion. `W-space` and `W-nbsp` must share a carrier-origin assignment without becoming the same source witness.

### F03 — initiation cardinality and cause

The number of initiation events must equal the number of maximal non-SPACE word gonols, including a first word with no literal preceding SPACE. Each event must point to its source offset and declared hidden-zero boundary condition.

A candidate is falsified if initiation is inferred from token value, hash phase, first visible anchor, or a post-hoc label that has no pre/post state effect.

### F04 — seam uniqueness without evidence loss

For each word initiation, the candidate must identify one causal initiation interface under its own state law. Leading, trailing, or consecutive SPACE manifestations remain exact evidence.

`W-repeat-space` separates a singular carrier-origin interface from two source occurrences. A candidate is falsified if it deletes one occurrence, invents two unrelated origins, or chooses a seam by normalization or display convenience. A candidate that cannot yet relate the two occurrences to the singular interface is `unresolved`, not silently supported.

### F05 — one support unit per speaker turn

Every complete witness turn contributes exactly one unit of support, including `W-empty` and `W-unassigned`. A candidate is falsified if token count, word count, motion distance, initiation count, or alphabet coverage changes the turn’s support unit.

## 4. Motion falsifiers

### F06 — 360° visible coincidence with complete-state change

For a declared complete state `s`:

```text
visible(advance(s, 360°)) = visible(s)
complete(advance(s, 360°)) != complete(s)
```

The changed distinction must be named and retained as orientation, sidedness, sheet, or a candidate-owned equivalent. A candidate is falsified if 360° is complete identity, if visible position changes contrary to its declared projection, or if the changed distinction exists only in prose and not in the evidence.

### F07 — 720° complete return

For the same state and declared equivalence policy:

```text
complete(advance(s, 720°)) = complete(s)
```

Equality must cover every candidate-owned carrier distinction. Source witness, occurrence identity, parentage, and provenance remain linked and cannot be discarded merely to force equality.

A candidate is falsified if a retained orientation or sidedness difference remains after 720°, or if return is claimed only because the visible projection repeats.

### F08 — exact transition inverse

For every admitted transition `t` and complete state in scope, the declared inverse must restore the prior complete state:

```text
inverse(t)(t(s)) = s
t(inverse(t)(s)) = s
```

The equality policy is explicit and versioned. A candidate is falsified if inversion restores only a scalar or visible coordinate while losing source, initiation history, sidedness, order, parentage, or completion scope.

### F09 — scoped completion

A completion receipt must identify the candidate, source span, boundary, state-equivalence policy, and completed construction. The same record must preserve remaining unresolved capacity.

A candidate is falsified if it equates carrier return with epistemic exhaustion of the unknowable, or if completion is widened or narrowed without a new scope declaration.

## 5. Structural falsifiers

### F10 — order, multiplicity, and sidedness

The experiment must distinguish `W-order-left` from `W-order-right`, retain both occurrences in `W-repeat-word`, and preserve left/right operand identity in any pairing record.

A candidate is falsified by implicit sorting, commutation, set conversion, duplicate removal, flattening, or unlabeled merging. An explicit lossy projection may ignore a distinction only if the complete source remains linked and the loss is declared.

### F11 — recursive parentage

A larger-gonol witness must retain child occurrence identities, ordered edges, repeated references, and prior-node parentage. Shared or cyclic references require explicit reference or budget receipts under a named traversal policy.

A candidate is falsified if recursive content is copied, flattened, or truncated without a receipt, or if two distinct occurrence histories become indistinguishable under a claimed lossless map.

## 6. Relationship-separating falsifiers

### F12 — cover-chart round trip

This falsifier applies to `C2-cover-chart`.

The candidate must provide explicit maps `to_mobius` and `to_cover`, declared equivalence on both sides, and round-trip evidence for every minimum witness:

```text
to_cover(to_mobius(cover_state)) = cover_state
to_mobius(to_cover(mobius_state)) = mobius_state
```

The maps must commute with initiation, 360° advance, 720° advance, and inverse motion. They must preserve exact source, order, multiplicity, sidedness, parentage, and completion scope.

One pair of complete states that the map incorrectly identifies or separates falsifies the chart claim for the declared domain. A shared period or visible coordinate alone is `inconclusive`.

### F13 — constructive incompatibility witness

This falsifier applies to `C3-incompatible`.

The candidate must retain a minimal witness for which every declared admissible map violates at least one required invariant. The report names the failed map, the violated invariant, and the two complete states incorrectly identified or separated.

A successful reversible map satisfying F01–F12 falsifies incompatibility for that witness domain. Different coordinate syntax, implementation language, or diagram style is not an incompatibility witness.

### F14 — direct-carrier independence

This falsifier applies to `C1-direct-mobius`.

The native Möbius state must define origin, initiation, 360° state change, 720° return, and inverse behavior without depending on an undeclared cover state to supply those meanings. A declared cover may be used as a visualization or comparison only after the native state is defined.

A candidate is falsified if removing the cover leaves the purported native state without a transition, orientation, or equivalence law.

## 7. Evaluator and projection falsifiers

### F15 — nine-way evaluator plurality

Every admitted carrier report must display outputs or explicit failures for all nine combinations of the three registered `M` candidates and three registered `B` candidates.

A report is falsified as a v0.5 report if it:

- hides a combination;
- appoints a winner or default;
- treats evaluator failure as zero;
- converts majority agreement into truth; or
- applies a cell-only evaluator outside scope while treating retained layers as absent.

Disagreements and counterexamples are retained results.

### F16 — projection loss disclosure

Every visible, radial, or scalar output must link to the complete trajectory and list each distinction it ignores or compresses. At minimum the declaration considers exact source, initiation cause, orientation/sidedness, occurrence order, multiplicity, recursive parentage, completion scope, and unresolved state.

A projection is falsified as faithful if two complete states that differ on a required distinction produce the same sole identity without a retained source link and loss declaration.

## 8. Candidate report shape

A v0.5 report is grouped by witness and carrier relationship. Each falsifier record contains:

1. falsifier ID and version;
2. candidate ID and version;
3. exact source or synthetic-state reference;
4. declared structural, comparison, and traversal policies;
5. verdict;
6. complete retained evidence;
7. minimized counterexample when falsified;
8. exception and partial state when errored;
9. declared information loss; and
10. rollback behavior.

The aggregate report lists all three relationship candidates. It has no `selected_candidate`, `best_candidate`, implicit default, or canonicalization field.

## 9. Admission rule

A candidate is **admitted for implementation review** only when every applicable falsifier is `supported` or accompanied by an explicitly accepted unresolved obligation. Any `falsified` result remains blocking for the exact claim it contradicts. Any exception remains visible.

Admission authorizes neither runtime deployment nor canonization. The next authority decision may retain, narrow, reject, or request more evidence from any candidate.

## 10. Usage guidance

Use these falsifiers before designing canonical coordinates, higher-gonol composition, completion conditions, metric formulas, or EDCM bindings. Future executable tests should cite the falsifier IDs and preserve their complete report packets through the evaluator laboratory and experiment-manifest infrastructure.

## hmmm

The most useful v0.5 result may be a small counterexample. If a repeated SPACE, a first-word initiation, or a 360° state pair breaks an alleged chart, that is not a failed release—it is the evidence that prevents UCNS from canonizing the wrong relationship.