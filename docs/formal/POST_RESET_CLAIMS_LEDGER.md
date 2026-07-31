# Post-reset UCNS claims ledger

**Status:** active issue-#145 classification surface; this ledger records
standing and provenance but does not canonize its own entries.

## Classification vocabulary

| Class | Meaning |
|---|---|
| `definition` | declared meaning within an explicitly named scope |
| `decided-constraint` | required within EDCM scope by current authority |
| `implemented-candidate` | executable comparison or research construction |
| `represented-evidence` | retained evidence without measurement or law selection |
| `empirical-result` | reproduced observation under a pinned profile and corpus |
| `historical-evidence` | source material preserved for recovery or counterevidence |
| `negative-result` | demonstrated exclusion or insufficiency within a stated scope |
| `conjecture` | falsifiable statement lacking sufficient evidence |
| `unresolved` | required choice, definition, law, or evidence remains incomplete |
| `rejected-pre-reset` | retained provenance that cannot activate current behavior |

## Authority ledger

| ID | Statement | Class | Scope | Evidence or authority |
|---|---|---|---|---|
| `ID-1` | UCNS is a stable identifier without a canonical expansion. | decided-constraint | repository-wide | `CANON.md`; option registry `stable-identifier` |
| `ROOT-1` | UCNS assigns elements of an unknowable to completion through geometric motion. | decided-constraint | repository-wide | `CANON.md`; option registry `ucns-completion-motion-root` |
| `ROOT-2` | Completion closes a declared construction relative to its boundary and does not exhaust the unknowable. | decided-constraint | repository-wide | `CANON.md`; option registry `completion-scoped-to-declared-boundary` |
| `EDCM-1` | The Möbius origin and hidden zero are required for the EDCM carrier. | decided-constraint | EDCM | option registry `edcm-mobius-causal-carrier` |
| `EDCM-2` | Structural Null is singular superpositioned space before gonol initiation. | decided-constraint | EDCM | option registry `structural-null-superposition` |
| `EDCM-3` | Every new word gonol initiates through the twist. | decided-constraint | EDCM | option registry `gonol-initiation-mobius-twist`; profile event |
| `EDCM-4` | One 360-degree circuit does not restore complete carrier state; local carrier-state return requires 720 degrees. | decided-constraint | EDCM carrier recovery | `CANON.md`; issue #145 |
| `EDCM-5` | Words are the smallest gonols, and larger gonols must preserve SPACE-origin nesting boundaries. | decided-constraint | EDCM | option registry `word-gonol-smallest-scale` |
| `EDCM-6` | The complete assignment-and-motion trajectory is the observation identity; scalars are optional declared-loss projections. | decided-constraint | EDCM | option registry `trajectory-before-scalar` |

## Implemented and represented evidence

| ID | Statement | Class | Scope | Evidence |
|---|---|---|---|---|
| `IMPL-1` | A directed twofold angular cover with `4π` lifted period and `2π` visible projection is executable. | implemented-candidate | UCNS comparison | `src/ucns/carrier.py`; `tests/test_carrier.py` |
| `IMPL-2` | The current cover returns lifted position after two visible laps. | implemented-candidate | UCNS comparison | `deck_translate`; lifted-position tests |
| `IMPL-3` | The current cover deliberately infers no orientation, chirality, sidedness, inversion, or payload operation after one lap. | implemented-candidate | UCNS comparison | `topology_does_not_invent_orientation_algebra` contract |
| `IMPL-4` | The current cover null is unique coordinate-free complete absence. | implemented-candidate | UCNS comparison | `STRUCTURAL_NULL`; carrier contract |
| `OBS-1` | The EDCM profile preserves exact source code points and SPACE-origin boundaries. | implemented-candidate | EDCM observation | `src/ucns/edcm.py` profile `0.2.0` |
| `OBS-2` | The EDCM profile records a `"mobius-twist"` initiation label for each word gonol. | represented-evidence | EDCM observation | `EdcmWordGonol.initiation_event` |
| `OBS-3` | The initiation label is not a geometric Möbius transition. | negative-result | EDCM observation | module nonclaim and absence of carrier transition |
| `MOTION-1` | Supplied assignment-and-motion trajectories can be retained with scoped completion and unresolved state. | implemented-candidate | EDCM evidence | `src/ucns/edcm_motion.py` schema `0.1.0` |
| `MOTION-2` | The evidence schema does not derive assignment, motion, or completion laws. | represented-evidence | EDCM evidence | `EDCM_COMPLETION_MOTION_EVIDENCE.md` |
| `IMPL-5` | Fourteen source-bound marked seams attach the typed Structural Null prestate to the exact root while retaining twist and motion receipts. | implemented-candidate | v0.13 minimum packet and root fiber | `src/ucns/initiation_boundary.py`; `PARTIAL_INITIATION_BOUNDARY_V013.md` |
| `IMPL-6` | The signed-local affine map and inverse are real-continuous on the complete declared intervals, and the affine product map descends through the declared non-null quotient while commuting with the sheet involution. | represented-evidence | declared real non-null candidate | exact epsilon-delta and quotient certificates in `src/ucns/full_carrier_attachment.py`; analytic, not machine-checked; no total Structural Null relation |
| `IMPL-7` | Arbitrary-domain observed occurrences can be admitted through explicit content adapters and each admitted occurrence receives exactly one ordered tagged assignment outcome. | implemented-candidate | adapter-admitted assignment evidence only | `src/ucns/assignment_boundary.py`; `ASSIGNMENT_ADMISSION_BOUNDARY_V016.md`; outcome totality is not geometric assignment totality |
| `IMPL-8` | Every v0.16 admitted occurrence receives one exclusive initiation outcome; the declared word witness crosses from typed Structural Null through one explicit Möbius-twist receipt, while unresolved and rejected occurrences stay distinct. | implemented-candidate | v0.17 admitted word-initiation evidence only | `src/ucns/gonol_initiation.py`; `GONOL_INITIATION_STRUCTURAL_NULL_V017.md`; no transverse geometry, total Structural Null topology, composition, completion, selection, or activation |
| `IMPL-9` | The surviving signed-local exact circle candidate can be applied reversibly to any explicitly initiated word occurrence for which independent exact rational coordinate input is supplied. | implemented-candidate | v0.18 explicit-input candidate application only | `src/ucns/explicit_geometric_assignment.py`; `EXPLICIT_GEOMETRIC_ASSIGNMENT_BOUNDARY_V018.md`; no source-to-coordinate derivation, total topology, higher geometry, completion, selection, or activation |

| IMPL-10 | Within one complete finite ordered trace, occurrence i of cardinality n derives exact p=(2i+1)/(2n), u=2p-1, and t=2p; initiated outcomes receive the exact circle candidate and other outcomes retain explicit blockers. | implemented-candidate | v0.19 trace-local source-coordinate derivation | src/ucns/source_coordinate.py; SOURCE_COORDINATE_DERIVATION_V019.md; exact within-scope injectivity and upstream object identity, with no selection, cross-scope composition, higher geometry, completion, or activation |

## Empirical and historical evidence

| ID | Statement | Class | Scope | Evidence |
|---|---|---|---|---|
| `EMP-1` | The repaired MultiWOZ 2.1 run processed 10,438 dialogues and 143,048 turns with zero carrier-unassigned occurrences under profile `0.2.0`. | empirical-result | one complete corpus | sealed EDCM PR #41 evidence |
| `EMP-2` | MultiWOZ completeness does not establish universal Unicode carrier coverage or the missing geometry. | negative-result | claim boundary | profile and PR explicit nonclaims |
| `EMP-3` | The corrected source-native MultiWOZ 2.1 stream reconciled all 10,438 dialogues and 143,048 turns and acquired UCNS v0.14.1 completion receipt `921ceacad026de1d884eec3e049b090246014706c937c062bd32f40bbff01f0c`. | empirical-result | one exact producer and corpus artifact | EDCM PR #44; `docs/evidence/EDCM_MULTIWOZ_V0141_HANDOFF.json` |
| `HIST-1` | The pinned a0-betatest epoch is the primary EDCM recovery specimen. | historical-evidence | recovery | commit `7af8debf6ef3905f01baff02b43d8c3bee16ccbc` |
| `HIST-2` | The specimen retains seam events, lifted traversal, ordered composition, chirality evidence, recursive grain, disk stacking, and inscription. | historical-evidence | recovery | recovery manifest and reference |
| `HIST-3` | Hash-derived lanes, fixed lane count, ordinary `2π` phase reduction, sine-sign chirality, cylinder-only geometry, coherence scalar, and factorization authority do not transfer. | rejected-pre-reset | current activation | `CANON.md`; recovery reference |

## Issue-#145 negative results

| ID | Statement | Class | Scope | Evidence |
|---|---|---|---|---|
| `NEG-1` | The bare directed cover is insufficient as the EDCM target carrier. | negative-result | current implementation | it lacks target Structural Null semantics, orientation operation, intrinsic/marked seam, initiation relation, and causal twist receipt |
| `NEG-2` | A movable angle-zero coordinate cannot by itself establish hidden zero or an intrinsic seam. | negative-result | carrier candidates | coordinate reparameterization leaves the bare cover unchanged while moving the claimed origin |
| `NEG-3` | Two-lap periodicity alone does not establish Möbius initiation. | negative-result | carrier candidates | direct comparison of implemented state with EDCM decided constraints |
| `NEG-4` | A standard Möbius band alone does not supply UCNS Structural Null, source initiation, hidden zero, or scoped completion. | negative-result | candidate terminology | missing required additional structure |
| `NEG-5` | Content digest, runtime hash, `repr`, object identity, and A0 Blake2 phase lanes cannot derive a universal geometric assignment. | negative-result | v0.16 assignment admission | exact identity-bearing evidence remains separate from geometry; the A0 prototype mechanism is explicitly rejected |
| `NEG-6` | Source SPACE manifestation, carrier position zero, directed-cover null, neutral `M`, algebraic zero, absent cell, and `NA` cannot substitute for the singular Structural Null prestate. | negative-result | v0.17 gonol initiation | typed origin-role registry and fail-closed substitution witnesses |
| `NEG-7` | Binary64 rendering, carrier position alone, scalar projection, and historical A0 lanes cannot replace independently supplied exact coordinate evidence or derive v0.18 geometry. | negative-result | v0.18 explicit candidate application | exact rational identity, rendering-collision witnesses, and named rejected-mechanism outcomes |

| NEG-8 | Content, digest, runtime identity, A0 lanes, carrier position alone, scalar projection, and binary64 rendering are not inputs to the v0.19 source-coordinate law. | negative-result | v0.19 finite ordered trace law | exact code path derives only from occurrence index and complete scope cardinality |

These results exclude only the stated shortcuts. They do not choose between a
direct pointed Möbius carrier, a faithfully augmented chart, and formal
incompatibility.

## Unresolved obligations

| ID | Statement | Class | Closure evidence required |
|---|---|---|---|
| `OPEN-1` | exact mathematical construction of singular superpositioned Structural Null | unresolved | definition, boundary cases, and separating witnesses |
| `OPEN-2` | source-to-gonol initiation relation through the twist beyond the v0.17 admitted word witness | unresolved | generalized relation or partial function with failure behavior |
| `OPEN-3` | orientation/sidedness transformation after 360 degrees beyond the bounded v0.13 root witness retained by v0.17 | unresolved | generalized state space, transport law, and two-lap return proof |
| `OPEN-4` | direct Möbius carrier versus augmented chart versus incompatibility | unresolved | preservation map or separating proof |
| `OPEN-5` | source-to-coordinate derivation and element-to-circle/epicycle/disk/sphere assignment law | unresolved | v0.18 closes explicit-input exact circle-candidate application and tagged failure behavior only; closure still requires a formal source-derived geometric law and falsifiers |
| `OPEN-6` | transition laws across geometry and recursive scale | unresolved | typed transitions and non-completion receipts |
| `OPEN-7` | higher-gonol composition above words | unresolved | SPACE-preserving composition law |
| `OPEN-8` | scoped completion condition | unresolved | construction-specific condition and registration proof |
| `OPEN-9` | canonical structural equivalence, `M`, and `B` | unresolved | independent evidence-bearing decision packets |
| `OPEN-10` | complete `UCNSObject`, factorization, codec, embedding, and Theorem N | unresolved | prohibited until their prerequisite laws are ratified |

v0.19 narrows OPEN-5 by supplying the formal finite trace-local midpoint
candidate and SC01-SC10. Comparative selection, cross-scope stability,
higher-gonol composition, and epicycle/disk/sphere assignment remain open.

## Canonization firewall

Nothing in this ledger is promoted merely because:

- it is written formally;
- code exists;
- fixtures pass;
- a corpus has complete carrier assignment;
- a candidate resembles a standard construction;
- a scalar predicts an outcome;
- a draft PR merges.

Canonization requires a separate explicit authority decision recording version,
laws, evidence, alternatives, information loss, rollback, and migration.

## hmmm

The ledger closes the false equivalence between “implemented” and “answered.”
The current cover, v0.16 assignment-admission outcomes, v0.17 bounded
Structural Null-to-word initiation receipt, v0.18 explicit-input application,
and the v0.19 exact finite ordered-source derivation candidate are implemented.
Candidate selection, cross-scope and higher-gonol composition, total Structural
Null topology, higher-scale geometry, and completion remain alive.
