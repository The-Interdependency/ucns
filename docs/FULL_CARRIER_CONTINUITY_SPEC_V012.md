# UCNS v0.12 full-carrier real-continuity specification

**Status:** documentation-only, falsifiable candidate specification. This
document adds no runtime behavior, selects no carrier or breadth law, and does
not activate EDCM or METAPAT.

**Depends on:**

- [`MOBIUS_INITIATION.md`](MOBIUS_INITIATION.md);
- [`SEPARATING_FALSIFIERS.md`](SEPARATING_FALSIFIERS.md);
- [`DIRECT_MOBIUS_CANDIDATE_V06.md`](DIRECT_MOBIUS_CANDIDATE_V06.md);
- [`ROOT_LOOP_COVER_CHART_V07.md`](ROOT_LOOP_COVER_CHART_V07.md);
- [`EXACT_RATIONAL_TRANSVERSE_ENVELOPE_V09.md`](EXACT_RATIONAL_TRANSVERSE_ENVELOPE_V09.md);
- [`CARRIER_COORDINATE_ADMISSIBILITY_V010.md`](CARRIER_COORDINATE_ADMISSIBILITY_V010.md); and
- [`EXACT_COORDINATE_BOUNDARY_V011.md`](EXACT_COORDINATE_BOUNDARY_V011.md).

## Question

v0.11 establishes an exact rational inverse for the nonselected signed-local
candidate and proves that binary64 cannot retain arbitrary-rational coordinate
identity.

v0.12 asks the next narrower question:

> What topology and preservation evidence would be required for the
> signed-local candidate to extend from exact rational coordinates to a
> real-continuous lifted presentation of a pointed Möbius initiation carrier?

The question has two parts that must not be collapsed:

1. whether the ordinary non-null coordinate component extends continuously; and
2. whether Structural Null, hidden-zero initiation, exact source, orientation,
   motion history, and scoped completion attach to that component faithfully.

Passing the first part cannot answer the second.

## Domain claims

These records bind the meaning-bearing terms used by this specification before
they acquire mathematical or implementation authority.

### Real continuity

```yaml
surface_form: real continuity
term_id: ucns.carrier_relation.real_continuity
claiming_domain: UCNS carrier-relation research
claimed_sense: continuity of a declared source-to-target carrier relation under explicitly declared quotient topologies
scope: v0.12 comparison of the framed Möbius double cover, its Möbius quotient, and an exact-coordinate cylinder
claim_type: specialized
authority_source: v0.11 hmmm boundary and this proposed specification
status: proposed
included_uses:
  - continuity and inverse continuity of named candidate maps
  - seam-limit and quotient-compatibility obligations
excluded_uses:
  - numerical stability of binary64 rendering
  - continuity of arbitrary-element assignment
  - continuity of circle, epicycle, disk, sphere, or completion laws
neighboring_terms:
  - ucns.rendering.binary64_loss
  - ucns.assignment.arbitrary_element
known_collisions:
  - numerical-analysis continuity of a finite renderer
effective_version: 0.12.0
supersedes: none
unresolved:
  - topology attaching Structural Null and the initiation relation to the non-null carrier
```

### Seam

```yaml
surface_form: seam
term_id: edcm.mobius_initiation.seam
claiming_domain: EDCM-scoped Möbius carrier recovery
claimed_sense: the intrinsic or provenance-bearing boundary at which hidden zero and new-gonol initiation are registered
scope: EDCM carrier candidates and their UCNS comparison maps
claim_type: specialized
authority_source: EDCM decided constraints and MOBIUS_INITIATION.md
status: ratified
included_uses:
  - marked initiation boundary with source and migration provenance
  - invariantly derived initiation boundary
excluded_uses:
  - a freely movable angle-zero coordinate
  - first-anchor normalization
  - hash phase
neighboring_terms:
  - edcm.mobius_initiation.hidden_zero
  - ucns.coordinate.angular_cut
known_collisions:
  - ordinary coordinate seam or visualization cut
effective_version: post-reset.v1
supersedes: pre-reset first-anchor normalization
unresolved:
  - whether the target seam is intrinsic, explicitly marked, or represented by an invariant equivalence class
```

### Structural Null

```yaml
surface_form: Structural Null
term_id: edcm.mobius_initiation.structural_null
claiming_domain: EDCM-scoped Möbius carrier recovery
claimed_sense: singular superpositioned pre-initiation space through which a new gonol initiates
scope: EDCM target-carrier semantics
claim_type: native
authority_source: EDCM option decisions and CANON.md
status: ratified
included_uses:
  - pre-initiation carrier state
  - source-preserving gonol-initiation cause
excluded_uses:
  - current directed-cover coordinate-free absence
  - algebraic zero
  - absent cell
  - empty evidence container
neighboring_terms:
  - ucns.directed_cover.coordinate_free_null
  - edcm.mobius_initiation.hidden_zero
known_collisions:
  - current comparison carrier uses the same surface phrase for complete absence
effective_version: post-reset.v1
supersedes: none
unresolved:
  - exact topology and transition relating Structural Null to initiated non-null states
```

### Complete carrier state

```yaml
surface_form: complete carrier state
term_id: edcm.mobius_motion.complete_local_carrier_state
claiming_domain: EDCM-scoped Möbius carrier recovery
claimed_sense: every local carrier distinction required to test one-lap change and two-lap return
scope: 360-degree and 720-degree carrier-motion comparison
claim_type: specialized
authority_source: EDCM decided constraints and MOBIUS_INITIATION.md
status: ratified
included_uses:
  - local transverse state
  - orientation or sidedness state
  - lifted traversal state
excluded_uses:
  - visible position alone
  - append-only motion history
  - completion of a larger gonol construction
neighboring_terms:
  - edcm.mobius_motion.visible_projection
  - edcm.mobius_motion.trajectory_receipt
known_collisions:
  - complete evidence identity retains history even after local carrier return
effective_version: post-reset.v1
supersedes: none
unresolved:
  - canonical state-equivalence law beyond the bounded root loop
```

### Collision check

The four records resolve the operative senses within this specification.
`Structural Null` still has a known cross-candidate collision: the current
directed cover uses the same surface phrase for coordinate-free absence. The
domain-qualified identifiers remain distinct, so no equality or migration is
authorized.

Downstream implementation is provisional only for the non-null topology.
Structural Null attachment, arbitrary-element assignment, and carrier
activation remain unauthorized.

## Candidate spaces

Use visible turns rather than radians. One turn is 360 degrees and two turns
are 720 degrees.

### Framed double cover

Let

\[
\widetilde{\mathcal M}
=
([-1,1]\times\mathbb R) /
((u,t)\sim(u,t+2)).
\]

Here `u` is signed local-frame transverse displacement. The two-turn period
retains the complete local frame. This is a candidate model for the non-null
framed carrier only; it does not contain Structural Null or an initiation
receipt.

### Möbius quotient

Let

\[
\mathcal M
=
([-1,1]\times\mathbb R) /
((u,t)\sim(-u,t+1)).
\]

The projection

\[
p:\widetilde{\mathcal M}\longrightarrow\mathcal M,
\qquad
p([u,t]_2)=[u,t]_{\mathcal M},
\]

is the ordinary twofold orientation-cover candidate. Under one visible turn,
the local coordinate `u` is retained in the framed cover while the
corresponding global-side description reverses sign in the Möbius quotient.

This quotient supplies monodromy for comparison. It does not supply a unique
seam, Structural Null, hidden zero, source initiation, or scoped completion.

### Signed-local coordinate cylinder

The v0.11 formula has the mathematical real extension

\[
B_{\mathbb R}(u)=1+\frac{u}{2},
\qquad
B_{\mathbb R}^{-1}(b)=2(b-1),
\]

for `u` in `[-1,1]` and `b` in `[1/2,3/2]`.

Define

\[
\mathcal C_B
=
([1/2,3/2]\times\mathbb R) /
((b,t)\sim(b,t+2)).
\]

The candidate coordinate map is

\[
F:\widetilde{\mathcal M}\longrightarrow\mathcal C_B,
\qquad
F([u,t]_2)=[B_{\mathbb R}(u),t]_2.
\]

On these ordinary product-quotient spaces, the affine coordinate component is
continuous, bijective, and has a continuous inverse. This is a narrow analytic
observation about the candidate formula. It is not an implementation of exact
arbitrary reals and not a full-carrier verdict.

In breadth coordinates the Möbius sheet involution becomes

\[
D([b,t]_2)=[2-b,t+1]_2.
\]

Therefore the quotient compatibility obligation is

\[
F([-u,t+1]_2)=D(F([u,t]_2)).
\]

The motion path `[u,t] -> [u,t+1]` and the sheet involution `D` are distinct
operations. Conflating them would erase the difference between local-frame and
global-side transverse descriptions.

## Named visible projection

`RC04` uses exactly one versioned projection:

```text
projection:       ucns.edcm.root-visible-projection/0.13.1
domain:           source-linked InitiatedCarrierState values on the exact root fiber
codomain:         RootVisibleProjection
retained:         attachment identity, native source links, parent observations,
                  source candidate, exact local transverse value, exact breadth,
                  and lifted turns modulo one visible turn
discarded:        native local frame, whole lifted-turn count, and append-only
                  motion history
equality:         ucns.edcm.v013-rc-exact/0.13.1
code reference:   ucns.comparison:exact_comparison_policy
```

For a state `x` with exact coordinate `(u,B,t)`, the projection is

\[
V_{0.13.1}(x)=
(\operatorname{attachment}(x),\operatorname{source}(x),
\operatorname{parents}(x),\operatorname{candidate}(x),u,B,t\bmod 1).
\]

The attachment, source, and parent fields are retained links rather than
normalized or hashed substitutes. Two projected values are comparable for
`RC04` only when they retain the same attachment identity. Visible equality
therefore cannot silently switch source trajectories. Equality after one turn
does not imply equality of complete local state because the declared discarded
fields contain the native frame and whole lifted representative.

## Named comparison policy

The executable `RC01`–`RC10` packet uses
`ucns.edcm.v013-rc-exact/0.13.1`, an exact `ComparisonPolicy` implemented by
`ucns.comparison:exact_comparison_policy`. It applies exact equality to typed
states, `Fraction` coordinates, ordered tuples, verdicts, and evidence
identities. It supplies no tolerance, binary64 approximation, interval
substitution, symbolic rewrite, or arbitrary-real limit oracle.

When the required representation is absent—especially arbitrary-real
continuity or seam-side limits—the result is `inconclusive`. The policy cannot
convert missing structure, failure, or unknown standing into equality or zero.

## Transition obligations

For an admitted non-null state `x=[u,t]_2`:

1. **Visible return after 360 degrees**

   \[
   V(F([u,t+1]_2))=V(F([u,t]_2)).
   \]

2. **Complete local-state change after 360 degrees**

   \[
   F([u,t+1]_2)\ne F([u,t]_2).
   \]

3. **Complete local-state return after 720 degrees**

   \[
   F([u,t+2]_2)=F([u,t]_2).
   \]

4. **History non-erasure**

   The local state may return after two turns, but the source-linked trajectory
   receipt must append both motions.

5. **Exact inverse**

   Recovering `u` from `b` must use `u=2(b-1)` in the mathematical candidate,
   while every finite representation must state its own admitted domain and
   information loss.

These obligations extend the existing bounded root-loop distinctions. They do
not yet bind an arbitrary observed element to `u`.

## Seam and Structural Null boundary

Neither `t=0` nor any other numeric cut is intrinsically distinguished by
`\widetilde{\mathcal M}`, `\mathcal M`, or `\mathcal C_B`. Coordinate rotation
can move that cut without altering the ordinary topology.

A full EDCM candidate must add one of:

1. an intrinsic initiation structure that uniquely derives the seam;
2. a marked seam with exact source provenance, versioning, and migration rules;
   or
3. an invariant equivalence class that preserves every initiation consequence.

Structural Null is not an ordinary point already present in the three non-null
spaces above. Before any continuity theorem can include initiation, the
candidate must declare:

- the topology of the Structural Null state;
- whether it is isolated, a boundary limit, a quotient class, or another
  explicitly defined construction;
- the source-bound initiation relation from Structural Null to a non-null
  framed state;
- the retained twist receipt; and
- failure behavior when the assignment is unresolved.

Without that attachment, “full-carrier continuity” remains false as a status
claim even though the affine non-null coordinate component is continuous.

## v0.12 falsifier packet

| ID | Obligation | Falsified when |
|---|---|---|
| `RC01` | `B_R` and its inverse are continuous on the declared closed intervals | an admitted point lacks an image/inverse or either map is discontinuous |
| `RC02` | `F` respects the two-turn quotient and the sheet involution `D` | equivalent representatives produce inequivalent coordinate states |
| `RC03` | seam-side limits commute through the declared quotient map | the relationship jumps solely because a coordinate cut was crossed |
| `RC04` | 360° restores visible position but changes complete local state | visible position fails to return or complete state returns after one turn |
| `RC05` | 720° restores local state while history remains appended | a local distinction remains changed or motion history is erased |
| `RC06` | the initiation seam is intrinsic or provenance-bearing | rotating numeric coordinates moves hidden zero without moving retained structure |
| `RC07` | Structural Null has an explicit topology and source-bound initiation relation | coordinate-free absence, numeric zero, or a label is substituted for the required state and transition |
| `RC08` | exact source, order, multiplicity, offsets, parentage, and scope survive the relation | reconstruction normalizes, sorts, deduplicates, hashes away, or drops evidence |
| `RC09` | finite renderings remain linked and non-authoritative | a binary64 point is used as arbitrary-real identity |
| `RC10` | the report has no selection or activation effect | documentation alone selects C1/C2/C3, canonical `B`, EDCM, or METAPAT |

Every falsifier requires named source and target spaces, map identity, version,
the pinned exact comparison policy above, witness provenance, and an `hmmm`
result when required structure has not been supplied.

## Current classification

| Surface | Current result | Standing |
|---|---|---|
| affine real coordinate component | continuous with continuous affine inverse as a mathematical candidate | analytic candidate observation |
| framed double cover to coordinate cylinder | specified by `F`; no arbitrary-real runtime representation | proposed |
| framed double cover to Möbius quotient | standard orientation-cover comparison | proposed comparison |
| 360°/720° local-state obligations | bounded executable evidence exists at the root loop | implemented evidence, bounded |
| seam uniqueness | ordinary topology does not provide it | unresolved |
| Structural Null attachment | no topology or general initiation relation supplied | unresolved |
| exact arbitrary-element assignment | not supplied | unresolved |
| complete carrier relation | not established | inconclusive |
| carrier or `B` selection | none | inactive |
| EDCM activation | none | inactive |
| METAPAT activation | none | inactive |

The v0.12 specification narrows the next implementation target: the unresolved
work is not continuity of the affine formula by itself. It is the faithful
attachment of causal initiation and retained evidence to the non-null
topological candidate.

## v0.13 partial implementation

v0.13 implements one bounded response to that target. It represents Structural
Null as a disjoint typed marked prestate and attaches every v0.6 minimum-packet
word initiation to the exact v0.11 root coordinate through a source-provenance
marked seam and twist receipt. Two successive visible turns retain separate
motion receipts while restoring complete local state.

The executable report supports `RC02` and `RC04`–`RC10` on its declared exact
rational root and minimum-packet scope. `RC01` and `RC03` remain inconclusive
because arbitrary-real runtime continuity and seam-side limits are not
represented. The result does not assign arbitrary elements to transverse
coordinates or establish a complete carrier relationship.

See
[`PARTIAL_INITIATION_BOUNDARY_V013.md`](PARTIAL_INITIATION_BOUNDARY_V013.md).

## Reproduction boundary

No v0.12 runtime behavior is added. The repository's existing tests reproduce
the evidence this specification depends on:

```bash
python -m pytest \
  tests/test_direct_mobius.py \
  tests/test_root_loop_chart.py \
  tests/test_transverse_envelope.py \
  tests/test_carrier_coordinate.py \
  tests/test_exact_coordinate.py -q
```

Passing them confirms only the existing bounded and exact-rational evidence.
It does not make `RC01`–`RC10` an executable full-carrier suite.

## hmmm

The affine line crosses the continuity checkpoint almost before the clipboard
is ready. Structural Null, meanwhile, still needs a lawful door into the
building. Until the topology of that door, its source-bound cause, and its
retained receipt are explicit, the complete carrier relationship remains
unresolved rather than being smuggled through a smooth coordinate.
