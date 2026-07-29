# Möbius carrier candidate matrix

**Status:** option-preserving comparison for issue
[#145](https://github.com/The-Interdependency/ucns/issues/145); no universal
carrier selection.

## Question

How may the EDCM-critical Möbius carrier relate to the implemented directed
twofold `4π` cover without erasing the singular origin, hidden zero, initiating
twist, orientation state, or retained source evidence?

## Compared constructions

### A. Direct pointed Möbius initiation carrier

A new carrier is defined from the Möbius construction itself, augmented with
the origin and initiation structure required by EDCM. The current directed cover
remains historical comparison evidence.

This is the cleanest option if no faithful map from the current cover can retain
the causal and superposition semantics.

### B. Bare directed twofold cover

This is the current executable candidate:

\[
\widetilde D =
\{N_c\}\cup((0,1)\times\mathbb{R}/4\pi\mathbb{Z}),
\]

with visible projection modulo `2π` and half-period deck translation.

Its `N_c` is coordinate-free absence. Its public state contains breadth and
angle. Half-period translation changes the lifted representative but
deliberately infers no orientation, chirality, sidedness, seam, or payload
operation.

### C. Directed cover as an augmented Möbius chart

The current `4π` cover is retained as a coordinate or observation chart over a
formally distinct Möbius initiation carrier. Additional state supplies:

- orientation or sidedness monodromy;
- an intrinsic or provenance-bearing origin;
- singular superpositioned Structural Null;
- the source-bound initiation relation;
- causal twist receipts.

This option is admissible only if an explicit map proves those additions are
preserved rather than reconstructed by guesswork after projection.

### D. Formal incompatibility

The direct Möbius carrier and directed cover remain separate constructions. The
cover continues to support comparison, visualization, and negative witnesses,
but cannot activate the EDCM carrier role.

This is a useful result if every proposed preservation map either loses the
origin semantics or changes the current cover into a materially different
object.

## Requirement matrix

| Requirement | A. Direct pointed Möbius | B. Bare directed cover | C. Augmented chart | D. Separate/incompatible |
|---|---|---|---|---|
| 720-degree local return | structurally available | implemented | required | available only in cover evidence |
| visible equality after 360 degrees | structurally available | implemented | required | available only in cover evidence |
| explicit state change after 360 degrees | available through monodromy, exact law open | lifted representative changes; orientation consequence absent | required and must be mapped | target and cover retain different meanings |
| singular superpositioned Structural Null | must be added and defined | absent; current null means complete absence | required in target, mapped separately | belongs only to target |
| hidden zero at origin/twist | must be intrinsic, marked, or invariantly derived | angle zero is a movable coordinate | required and provenance-bearing | belongs only to target |
| new-gonol initiation through twist | must be defined | absent | required | belongs only to target |
| exact source preservation | must bind to observation profile | supplied by a separate profile, not carrier | required through source link | remains external to cover |
| causal initiation receipt | must be defined | absent | required | target-only evidence |
| circle/epicycle/disk/sphere transitions | unresolved | absent | unresolved | unresolved |
| scoped completion condition | unresolved | absent | unresolved | unresolved |
| current implementation standing | not implemented | implemented comparison candidate | not implemented | admissible relationship verdict |

## Evidence already available

### Current directed cover

`src/ucns/carrier.py` establishes:

- lifted period `4π`;
- visible period `2π`;
- two lifted representatives away from the candidate null;
- one-lap deck translation;
- two-lap lifted-position return;
- no inferred orientation, chirality, inversion, or payload operation.

The candidate's dataclass state is `breadth` plus `angle`. It has no seam,
orientation value, initiation boundary, source identity, or twist receipt.

### Exact EDCM observation profile

`src/ucns/edcm.py` establishes:

- exact source preservation;
- the exact public 157-position carrier;
- Unicode White_Space assignment to the U+0020 origin;
- words as the smallest gonols;
- an initiation-event label;
- explicit SPACE nesting boundaries.

It explicitly does not provide Möbius coordinates or a higher-gonol composition
law.

### A0-betatest recovery specimen

The pinned historical specimen contributes candidate invariants:

- fixed SPACE/ZERO seam;
- lifted forward traversal;
- seam events;
- ordered noncommutative composition;
- chirality evidence;
- recursive grain and disk-stack structure;
- full-field inscription.

It does not authorize hash-derived lanes, fixed lane count, ordinary `2π`
reductions, sine-sign chirality, cylinder-only geometry, scalar coherence, or
factorization-centered authority.

## Negative result: the bare cover is insufficient

The bare directed cover cannot be a faithful realization of the EDCM target as
currently implemented.

The reason is structural, not terminological:

1. its null is complete coordinate-free absence rather than superpositioned
   pre-initiation space;
2. its half-period translation has no orientation or sidedness operation;
3. its angle-zero cut is not an intrinsic seam;
4. it has no source-bound initiation relation;
5. it emits no causal twist receipt.

Any map that discards these distinctions is not faithful. Any augmentation that
adds them produces candidate C, not evidence that candidate B already contained
them.

This negative result narrows the option set without selecting between A, C, and
D.

## Decision rule

Candidate C may be preferred over A or D only if a preservation map

\[
F:\mathcal{M}_{\mathrm{init}}\longrightarrow\widetilde D_{\mathrm{aug}}
\]

is explicitly defined and demonstrates:

1. source and initiation-boundary preservation;
2. one-to-one treatment of the hidden-zero condition;
3. orientation/sidedness state change after 360 degrees;
4. local carrier-state return after 720 degrees;
5. retained causal receipts;
6. no dependence on a movable coordinate cut;
7. declared information loss, if any.

If `F` is injective only after adding target state absent from the bare cover,
that addition must remain explicit. If `F` forgets any load-bearing distinction,
candidate C fails. If no faithful `F` exists, the lawful result is D.

## Migration consequences

| Result | Consequence |
|---|---|
| A selected for EDCM | add a new carrier implementation; keep `carrier.py` comparison-only |
| C survives falsification | version an augmented chart; do not mutate the bare cover's meaning in place |
| D established | prohibit the directed cover from EDCM target activation while retaining its tests and provenance |
| evidence remains incomplete | keep all A/C/D options open and fail closed on target activation |

No outcome transfers EDCM selection into universal UCNS canon.

## hmmm

The bare cover has now answered one question honestly: it is a map of two laps,
not yet a map of the twist.
