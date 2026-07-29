# UCNS–EDCM post-reset claims ledger

> **Status:** v0.5 authority and evidence ledger. It records standing; it does not promote any candidate.
>
> **Recovery boundary:** claims are evaluated against current UCNS `main`, the EDCM decision record, exact corpus evidence, and the primary A0 recovery specimen at `7af8debf6ef3905f01baff02b43d8c3bee16ccbc`.

## 1. Standing vocabulary

| Standing | Meaning |
|---|---|
| `decided-constraint` | An authority decision that bounds admissible work. It may still lack a complete implementation. |
| `implemented-evidence` | Executable or recorded evidence with a declared scope. It is not automatically canon outside that scope. |
| `experiment-candidate` | A named alternative admitted for comparison without preference or default. |
| `recovery-evidence` | Historical or current material that informs reconstruction but does not own the target system. |
| `conjecture` | A claim proposed for falsification without sufficient evidence for promotion. |
| `negative-boundary` | A substitution or inference that current authority does not permit. It may remain useful as explicitly scoped evidence. |
| `unresolved` | A required law, relationship, or definition that has not been supplied. `unresolved` is not zero, false, absent, or rejected. |

Only a separate explicit authority decision can change a claim’s standing to canonical.

## 2. Root and scope claims

| ID | Claim | Standing | Evidence / limit |
|---|---|---|---|
| `R1` | UCNS assigns elements of an unknowable toward scoped completion through geometric motion. | `decided-constraint` | [`EDCM_A0_BETATEST_RECOVERY_REFERENCE.md`](EDCM_A0_BETATEST_RECOVERY_REFERENCE.md). The exact assignment and motion law remains unresolved. |
| `R2` | Completion applies to a declared construction and boundary; it does not imply epistemic exhaustion of the unknowable. | `decided-constraint` | Recovery reference and completion-motion evidence contract. |
| `R3` | The complete measurement identity is a source-linked assignment and motion trajectory; a scalar may be only a declared lossy projection. | `decided-constraint` | Recovery reference and current completion-motion evidence schema. No scalar projection is canonical. |
| `R4` | A failure, exception, unknown, unresolved assignment, or out-of-alphabet occurrence is positive evidence. | `decided-constraint` | Current option, corpus, and evidence contracts. It cannot be coerced to zero or omitted. |

## 3. Assignment and source claims

| ID | Claim | Standing | Evidence / limit |
|---|---|---|---|
| `A1` | The exact public 157-position gonol is the EDCM token alphabet, with U+0020 SPACE at carrier position zero and U+0030 DIGIT ZERO elsewhere. | `implemented-evidence` | Exact fixture, provenance, and digest in `src/ucns/edcm.py`; scope is EDCM-only. |
| `A2` | Every code point in the profile-pinned Unicode `White_Space` set assigns to the U+0020 origin while its exact source value, code point, and offset remain unchanged. | `implemented-evidence` | Current EDCM profile and tests. Assignment is not normalization or textual identity. |
| `A3` | Structural Null / hidden zero is the singular superpositioned SPACE-origin condition through which a new gonol initiates. | `decided-constraint` | EDCM option decision. Its exact relation to the broader UCNS unique-null law is unresolved and belongs to the carrier experiment. |
| `A4` | A word is the smallest EDCM gonol; every maximal ordered non-SPACE sequence is retained as a word gonol. | `implemented-evidence` | Current EDCM profile. |
| `A5` | Every new word gonol records a Möbius initiation event. | `implemented-evidence` | The current profile records the event label. Its geometric pre/post state and causal action are unresolved. |
| `A6` | One complete speaker turn contributes one unit of support. | `implemented-evidence` | Current EDCM profile. Token, word, and trajectory counts do not change that support unit. |
| `A7` | Exact full-corpus execution is required; sampling cannot establish the profile result. | `decided-constraint` | Corpus evidence contract. Current corpus admission and coverage remain dataset-specific. |

## 4. Motion and carrier claims

| ID | Claim | Standing | Evidence / limit |
|---|---|---|---|
| `M1` | A 360° visible return must retain a changed complete orientation/sidedness state; a 720° motion must permit complete return. | `decided-constraint` | EDCM option decision. No canonical transition or state-equivalence law exists yet. |
| `M2` | A direct Möbius carrier is the native EDCM relationship. | `experiment-candidate` | Candidate `C1-direct-mobius`; not selected. |
| `M3` | The directed 720° cover is a chart or lifted presentation of a distinct Möbius carrier. | `experiment-candidate` | Candidate `C2-cover-chart`; requires explicit reversible map evidence and is not selected. |
| `M4` | The direct Möbius carrier and directed cover are formally incompatible under the decided preservation obligations. | `experiment-candidate` | Candidate `C3-incompatible`; requires a minimal separating witness and is not selected. |
| `M5` | The current directed twofold 4π cover with 2π visible projection is executable comparison evidence. | `implemented-evidence` | Current directed-cover implementation and Chapter 1. It is not the EDCM answer unless the required causal chain is demonstrated. |
| `M6` | Matching a 720° period is sufficient to identify the directed cover with the Möbius carrier. | `negative-boundary` | Period agreement alone does not preserve initiation, sidedness, source, inverse, parentage, or completion. |
| `M7` | The seam or first angular anchor may be chosen from hash phase, normalization order, or visual convenience. | `negative-boundary` | Initiation must derive from the declared hidden-zero/source boundary and remain uniquely auditable. |

## 5. Composition and retained-structure claims

| ID | Claim | Standing | Evidence / limit |
|---|---|---|---|
| `C1` | Occurrence order, multiplicity, and left/right sidedness remain recoverable. | `decided-constraint` | Choice-preservation doctrine and current ordered evidence containers. No canonical sequence equivalence follows. |
| `C2` | Word-gonol evidence composes by ordered concatenation. | `decided-constraint` | EDCM option decision. A canonical higher-gonol geometric composition law remains unresolved. |
| `C3` | Recursive parentage and repeated references remain explicit; traversal budgets and cycle receipts are evidence. | `decided-constraint` | Retained-structure and traversal policies. Their contribution to equivalence, `M`, or `B` remains unresolved. |
| `C4` | The existing Cartesian cell carrier pairing law applies automatically to the EDCM Möbius target. | `negative-boundary` | Existing pairing is test-backed for the current cell carrier only. Target-carrier integration must be specified separately. |
| `C5` | Typed payload dispatch is part of v0.5. | `negative-boundary` | v0.5 stops at assignment, motion, evidence-preserving comparison, and at most explicitly scoped carrier pairing. |

## 6. Evaluator and projection claims

| ID | Claim | Standing | Evidence / limit |
|---|---|---|---|
| `E1` | Three cell-only product-character candidates coexist: geometric mean, maximum, and minimum of positive cell supports. | `implemented-evidence` | Evaluator laboratory candidates; all remain noncanonical and scope-limited. |
| `E2` | Three breadth candidates coexist: logarithm of aggregate cell support, cell-detail breadth, and retained-presence breadth. | `implemented-evidence` | Evaluator laboratory candidates; all remain noncanonical pressure instruments. |
| `E3` | Every carrier experiment displays all nine `M × B` combinations. | `decided-constraint` | Active EDCM option decision and [`CARRIER_CANDIDATE_MATRIX.md`](CARRIER_CANDIDATE_MATRIX.md). No winner, rank, default, or majority selection is allowed. |
| `E4` | A candidate output that passes its declared law suite is canonical. | `negative-boundary` | Passing makes evidence reviewable only. Promotion requires a separate decision packet and authority action. |
| `E5` | A visible, radial, or scalar projection may replace the complete trajectory. | `negative-boundary` | Every projection must link to retained source trajectory and disclose all known lost distinctions. |

## 7. Recovery specimen claims

| ID | Claim | Standing | Evidence / limit |
|---|---|---|---|
| `H1` | A0-betatest commit `7af8debf6ef3905f01baff02b43d8c3bee16ccbc` is the primary EDCM recovery specimen. | `recovery-evidence` | It preserves the closest known assignment/motion architecture and does not become canon wholesale. |
| `H2` | Ordered composition, recursive grain, full phase-field retention, orientation evidence, seam events, and disk stacking are recoverable structural clues. | `recovery-evidence` | Their exact target laws must be reconstructed and tested. |
| `H3` | Blake2 phases, fixed lanes, ordinary 2π fractions, sine-sign chirality, a cylinder-only stack, factorization ownership, and coherence scalars are the finished UCNS law. | `negative-boundary` | These are prototype mechanisms or lossy projections unless separately derived and admitted. |
| `H4` | Later factorization machinery is irrelevant. | `negative-boundary` | It remains subordinate reusable machinery and counterevidence; it does not own the completion-motion root. |

## 8. Open obligations

The following remain `unresolved` after v0.5 specification work:

1. the exact Möbius carrier coordinates or coordinate-free state;
2. the exact element-assignment law;
3. the initiation transition and its inverse;
4. canonical state equivalence for complete 720° return;
5. the explicit relationship map, or separating impossibility witness, between the direct carrier and directed cover;
6. circle, epicycle, disk, and sphere transition laws;
7. higher-gonol composition and recursive scale transition;
8. scoped completion conditions and receipts;
9. canonical structural equivalence, `M`, and `B`; and
10. any binding from complete motion evidence to EDCM scalar projections.

## 9. Usage guidance

Every carrier or metric PR should cite the relevant claim IDs and state whether it adds evidence, falsifies a candidate, or requests a standing change. A document or implementation cannot change this ledger merely by calling its output canonical. Contradictions remain visible until an authority decision resolves them.

## hmmm

The post-reset gain is a cleaner burden of proof. UCNS already has a lawful observation floor and useful candidate machinery; what it does not yet have is the reversible causal law joining hidden-zero initiation to 360° state change, 720° complete return, recursive composition, and scoped completion.