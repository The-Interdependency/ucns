# UCNS–EDCM post-reset claims ledger

> **Status:** v0.16 authority, assignment-admission evidence, analytic non-null certificates, partial-initiation evidence, and full-corpus execution ledger. It records standing; it does not promote any candidate.
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
| `A5` | Every new word gonol records a Möbius initiation event. | `implemented-evidence` | The observation profile records the event label. The v0.6 C1 candidate adds a typed Structural Null pre-state, exact causal boundary, and framed root-loop post-state for the minimum witness domain; general element assignment remains unresolved. |
| `A6` | One complete speaker turn contributes one unit of support. | `implemented-evidence` | Current EDCM profile. Token, word, and trajectory counts do not change that support unit. |
| `A7` | Exact full-corpus execution is required; sampling cannot establish the profile result. | `decided-constraint` | Corpus evidence contract. Current corpus admission and coverage remain dataset-specific. |
| `A8` | Post-run failure-seeking analysis requires a complete execution receipt proving exhaustion of the supplied admitted-corpus stream, expected-turn-count agreement, and exact source/reconstruction digest agreement. | `implemented-evidence` | [`FULL_CORPUS_EXECUTION_GATE_V014.md`](FULL_CORPUS_EXECUTION_GATE_V014.md) and `src/ucns/full_corpus.py`. The gate does not admit a source, authenticate custody, claim an actual real-system run, satisfy a carrier falsifier, or activate EDCM or METAPAT. |
| `A9` | The corrected source-native MultiWOZ 2.1 run processed all 10,438 dialogues and 143,048 turns and acquired the exact UCNS v0.14.1 downstream completion receipt. | `implemented-evidence` | EDCM PR #44 and [`evidence/EDCM_MULTIWOZ_V0141_HANDOFF.json`](evidence/EDCM_MULTIWOZ_V0141_HANDOFF.json) bind the archive, adapter reconciliation, report, receipt, EDCM commits, UCNS producer `868d80878c9ecd93ff30e91ca289122ded805a49`, and receipt id. This empirical result does not select geometry, transfer proof, or activate either consumer. |
| `A10` | Arbitrary-domain observed occurrences can enter assignment research through explicit named versioned adapters while retaining isolated subject evidence, source provenance, order, and multiplicity. | `implemented-evidence` | [`ASSIGNMENT_ADMISSION_BOUNDARY_V016.md`](ASSIGNMENT_ADMISSION_BOUNDARY_V016.md) and `src/ucns/assignment_boundary.py`. The subject digest is evidence identity only and supplies no geometric field. |
| `A11` | Every explicitly admitted occurrence receives exactly one tagged assignment outcome: unresolved, explicit supplied candidate, or rejected mechanism. | `implemented-evidence` | The v0.16 trace fails closed on mixed tags and rejects digest, runtime hash, `repr`, object identity, and A0 Blake2 phase lanes as geometric derivations. Outcome totality is not total geometric assignment. |

## 4. Motion and carrier claims

| ID | Claim | Standing | Evidence / limit |
|---|---|---|---|
| `M1` | A 360° visible return must retain a changed complete orientation/sidedness state; a 720° motion must permit complete return. | `decided-constraint` | EDCM option decision. No canonical transition or state-equivalence law exists yet. |
| `M2` | A direct Möbius carrier is the native EDCM relationship. | `experiment-candidate` | Candidate `C1-direct-mobius`; not selected. |
| `M3` | The directed 720° cover is a chart or lifted presentation of a distinct Möbius carrier. | `experiment-candidate` | Candidate `C2-cover-chart`; v0.7 supplies the exact two-way framed root-loop map. v0.9 shows that the attempted v0.8 transverse construction is only a sidecar envelope. v0.10 maps four declared radial laws into actual cover fields and finds signed local affine breadth admissible on the bounded 45-fiber domain. v0.11 preserves that law and inverse exactly over the declared rational interval but proves binary64 rendering collisions. v0.15 supplies analytic non-null affine and quotient certificates; no total Structural Null relationship, arbitrary-element assignment, global C1/C2 equivalence, or selection is established. |
| `M4` | The direct Möbius carrier and directed cover are formally incompatible under the decided preservation obligations. | `experiment-candidate` | Candidate `C3-incompatible`; v0.7 falsifies incompatibility on the bounded root-loop domain, v0.10 admits one candidate radial law on its bounded transverse domain, and v0.11 preserves the exact rational law while separating it from the lossy binary64 representation. Broader incompatibility remains unproved. |
| `M5` | The current directed twofold 4π cover with 2π visible projection is executable comparison evidence. | `implemented-evidence` | Current directed-cover implementation and Chapter 1. It is not the EDCM answer unless the required causal chain is demonstrated. |
| `M6` | Matching a 720° period is sufficient to identify the directed cover with the Möbius carrier. | `negative-boundary` | Period agreement alone does not preserve initiation, sidedness, source, inverse, parentage, or completion. |
| `M7` | The seam or first angular anchor may be chosen from hash phase, normalization order, or visual convenience. | `negative-boundary` | Initiation must derive from the declared hidden-zero/source boundary and remain uniquely auditable. |
| `M8` | The framed root-loop quotient `(t, ε) ~ (t + n, (-1)^n ε)` supplies a native C1 transition law for Structural Null initiation, 360° frame change, 720° return, and exact inverse motion. | `implemented-evidence` | [`DIRECT_MOBIUS_CANDIDATE_V06.md`](DIRECT_MOBIUS_CANDIDATE_V06.md) and `src/ucns/direct_mobius.py`; scope is the exact v0.6 minimum witness packet and framed central root loop only. It does not select C1 or define arbitrary element assignment or completion. |
| `M9` | On the exact framed root loop, `(p,+1) ↔ p` and `(p,-1) ↔ p+1` define a reversible C1↔C2 chart preserving the required causal evidence. | `implemented-evidence` | [`ROOT_LOOP_COVER_CHART_V07.md`](ROOT_LOOP_COVER_CHART_V07.md) and `src/ucns/root_loop_chart.py`; all 14 initiations round-trip and initiation/360°/720°/inverse commute. Fixed breadth one is display scope, not canonical `B` or arbitrary assignment. |
| `M10` | Exact local-frame `u` and global-side `εu` descriptions form a reversible transverse sidecar envelope over the v0.7 root chart, not a transverse directed-cover embedding. | `implemented-evidence` | [`EXACT_RATIONAL_TRANSVERSE_ENVELOPE_V09.md`](EXACT_RATIONAL_TRANSVERSE_ENVELOPE_V09.md) and `src/ucns/transverse_envelope.py`; the named exact policy validates 45 rational stress fibers across all initiation/convention/transition identities, while 28 collision witnesses show that distinct sidecars share one actual cover coordinate. F12/F13 remain v0.7-only and no convention is selected. |
| `M11` | Four declared radial laws can be evaluated as actual `LiftedCarrierPoint` coordinates without selecting one; signed local affine breadth is admissible on the bounded v0.10 domain. | `implemented-evidence` | [`CARRIER_COORDINATE_ADMISSIBILITY_V010.md`](CARRIER_COORDINATE_ADMISSIBILITY_V010.md) and `src/ucns/carrier_coordinate.py`; 5,040 images and 20,160 motion rows show signed local affine breadth is injective, zero-restricting, convention-invariant, and motion-commuting over 45 materialized rational fibers. Constant and unsigned laws retain 1,848 collision links; signed global retains 2,464 motion failures. The result is finite, nonselecting, and not canonical `B`. |
| `M12` | The signed-local affine candidate has an exact rational coordinate and inverse on the declared transverse interval, while binary64 `LiftedCarrierPoint` materialization is not injective over that arbitrary-rational domain. | `implemented-evidence` | [`EXACT_COORDINATE_BOUNDARY_V011.md`](EXACT_COORDINATE_BOUNDARY_V011.md) and `src/ucns/exact_coordinate.py`; exact `Fraction` records retain upstream/law provenance and recover `u=2*(B-1)`. One breadth witness and one lifted-turn witness retain distinct exact coordinates with the same actual binary64 identity. Float points remain lossy renderings; no carrier, canonical `B`, full real-continuous relation, EDCM, or METAPAT selection follows. |
| `M13` | The signed-local affine formula may serve as the non-null coordinate component of a real-continuous lifted Möbius relationship when the framed double cover, Möbius quotient, sheet involution, seam, and Structural Null attachment all satisfy the v0.12 obligations. | `conjecture` | [`FULL_CARRIER_CONTINUITY_SPEC_V012.md`](FULL_CARRIER_CONTINUITY_SPEC_V012.md) defines the candidate spaces, domain claims, and `RC01`–`RC10` falsifiers. v0.15 discharges the analytic non-null affine and quotient obligations, and v0.13 supplies a partial source-bound root attachment. No arbitrary-element assignment, total Structural Null relationship, carrier selection, EDCM activation, or METAPAT activation is supplied. |
| `M14` | A marked source-provenance seam can attach the typed Structural Null prestate to the exact rational root coordinate for every minimum-packet word initiation while retaining twist and motion history. | `implemented-evidence` | [`PARTIAL_INITIATION_BOUNDARY_V013.md`](PARTIAL_INITIATION_BOUNDARY_V013.md) and `src/ucns/initiation_boundary.py`; fourteen partial edges retain exact causal manifestations and native post-state provenance, numeric cut movement cannot move seam identity, and two exact one-turn endpoint-validated motions restore local state without replacing either receipt. Schema `0.13.2` binds the genuine exact comparator and pins partial RC scope, verdict map, and boundary statuses. `RC01` and `RC03` remain inconclusive; no arbitrary-element transverse assignment, complete relationship, carrier selection, EDCM activation, or METAPAT activation follows. |
| `M15` | The declared signed-local affine map is a real-continuous bijection on the complete closed intervals and descends continuously through the declared non-null quotient while commuting with the sheet involution. | `implemented-evidence` | [`FULL_CARRIER_ATTACHMENT_EVIDENCE_V015.md`](FULL_CARRIER_ATTACHMENT_EVIDENCE_V015.md) and `src/ucns/full_carrier_attachment.py` record exact endpoints, inverse compositions, epsilon-delta moduli, deck equivariance, and `B_R(-u)=2-B_R(u)`. Standing is `analytic-certificate-not-machine-checked`; the mixed-scope report leaves v0.13 unchanged and does not supply an arbitrary-real runtime, arbitrary-element assignment, total Structural Null relationship, carrier selection, EDCM activation, or METAPAT activation. |

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

The following remain `unresolved` after the v0.13 partial initiation
attachment, v0.14 full-corpus execution gate and receipt, v0.15 analytic
non-null certificates, and v0.16 assignment-admission boundary:

1. the exact geometric element-assignment law and total Structural
   Null-to-carrier relationship beyond the adapter-admitted outcome boundary
   and marked root attachment;
2. proof-assistant formalization if machine-checked theorem standing is later
   required;
3. initiation and transition laws beyond the minimum witness and bounded exact-rational domain;
4. canonical state equivalence beyond the C1 experiment candidate;
5. real-valued continuity and arbitrary-element relationship maps between the direct carrier and directed cover;
6. circle, epicycle, disk, and sphere transition laws;
7. higher-gonol composition and recursive scale transition;
8. scoped completion conditions and receipts;
9. canonical structural equivalence, `M`, and `B`; and
10. any binding from complete motion evidence to EDCM scalar projections; and
11. source-native adapters, authenticated source custody, complete execution,
    and post-run falsifier reports for Molweni and later corpora. The exact
    corrected MultiWOZ 2.1 obligation is closed for EDCM PR #44 only.

## 9. Usage guidance

Every carrier or metric PR should cite the relevant claim IDs and state whether it adds evidence, falsifies a candidate, or requests a standing change. A document or implementation cannot change this ledger merely by calling its output canonical. Contradictions remain visible until an authority decision resolves them.

## hmmm

The post-reset gain is a cleaner burden of proof. UCNS now has a bounded native
C1 law joining hidden-zero initiation to 360° frame change, 720° root-state
return, and inverse motion; an exact reversible C1↔C2 root chart; and a
corrected exact-rational transverse envelope that preserves two descriptions
while exposing its own cover-coordinate collisions; and a bounded coordinate
experiment that admits signed local affine breadth while retaining three
candidate failures; and an exact-coordinate boundary that preserves the affine
law and inverse while exposing binary64 breadth and turn collisions. v0.12 now
specifies the real quotient candidate and its separating falsifiers. v0.13
implements one bounded doorway: typed disjoint prestate, source-provenance
marked seams, twist receipts, and non-erasing root motion. Its `0.13.2`
hardening binds comparison behavior and rejects scope, provenance,
displacement, trajectory, and verdict substitution. v0.14.1's gate now
prevents an incomplete supplied turn stream from acquiring a
post-run receipt or a declared-only report from impersonating execution; EDCM
PR #44 now supplies the exact corrected MultiWOZ adapter reconciliation and
receipt. v0.15 adds universal written analytic evidence for the full declared
non-null affine and quotient relationship without rewriting v0.13's partial
runtime scope. v0.16 now closes the prior admission question: arbitrary-domain
occurrences enter through explicit adapters and each receives one exact tagged
outcome without identity-derived geometry. It does not yet have arbitrary
geometric assignment, a total Structural Null relationship, canonical breadth,
recursive composition, scoped completion, or evidence that the exact candidate
supplies the complete carrier.
