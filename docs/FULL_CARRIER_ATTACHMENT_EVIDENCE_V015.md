# UCNS v0.15 full-carrier attachment evidence

**Status:** specification-defended analytic and executable evidence. This
package selects no carrier or breadth law, supplies no arbitrary-element
assignment, and activates neither EDCM nor METAPAT.

**Depends on:**

- [`FULL_CARRIER_CONTINUITY_SPEC_V012.md`](FULL_CARRIER_CONTINUITY_SPEC_V012.md);
- [`PARTIAL_INITIATION_BOUNDARY_V013.md`](PARTIAL_INITIATION_BOUNDARY_V013.md);
- [`EXACT_COORDINATE_BOUNDARY_V011.md`](EXACT_COORDINATE_BOUNDARY_V011.md); and
- the exact v0.14.1 downstream execution receipt recorded in
  [`evidence/EDCM_MULTIWOZ_V0141_HANDOFF.json`](evidence/EDCM_MULTIWOZ_V0141_HANDOFF.json).

## Question

v0.13 implemented source-bound initiation only at the exact rational root and
left `RC01` and `RC03` inconclusive because its executable comparator had no
arbitrary-real object or limit oracle.

v0.15 asks a narrower proof question:

> Can the already-declared affine map and non-null quotient relationship be
> certified for their complete real intervals without sampling, while keeping
> Structural Null attachment and arbitrary observed-element assignment at
> their actual bounded standing?

The answer is yes for the analytic non-null relationship and no for the
complete initiation relationship. Those two results are retained separately.

## Domain claims

These records bind the meaning-bearing terms before implementation.

### Analytic continuity certificate

```yaml
surface_form: analytic continuity certificate
term_id: ucns.carrier_relation.affine_real_continuity_certificate
claiming_domain: UCNS carrier-relation research
claimed_sense: a finite exact record of an affine map, its inverse, and universal epsilon-delta moduli whose written derivation covers every real point in the declared closed intervals
scope: B_R from [-1,1] to [1/2,3/2] and B_R inverse
claim_type: specialized
authority_source: FULL_CARRIER_CONTINUITY_SPEC_V012.md and this proof package
status: proposed
included_uses:
  - exact affine coefficients and endpoint images
  - exact inverse-composition identities
  - positive epsilon to positive delta proof schemes
excluded_uses:
  - enumeration or sampling of real values
  - a runtime arbitrary-real representation
  - a machine-checked theorem
  - canonical faithful breadth
neighboring_terms:
  - ucns.carrier_relation.real_continuity
  - ucns.exact_coordinate.signed_local_affine
known_collisions:
  - finite numerical continuity tests
effective_version: 0.15.0
supersedes: none
unresolved:
  - formalization in a proof assistant
```

### Quotient seam commutation certificate

```yaml
surface_form: quotient seam commutation certificate
term_id: ucns.carrier_relation.non_null_quotient_seam_commutation
claiming_domain: UCNS carrier-relation research
claimed_sense: an exact proof record that the continuous affine product map is deck-equivariant, descends through the declared two-turn quotient, and commutes with the declared sheet involution
scope: the non-null framed double cover, coordinate cylinder, and their declared quotient maps
claim_type: specialized
authority_source: FULL_CARRIER_CONTINUITY_SPEC_V012.md and this proof package
status: proposed
included_uses:
  - two-turn deck equivalence
  - B_R(-u) = 2 - B_R(u)
  - coordinate-cut side paths converging to one quotient class
excluded_uses:
  - the provenance-bearing initiation seam
  - Structural Null as a numeric seam point or boundary limit
  - proof of seam uniqueness
neighboring_terms:
  - edcm.mobius_initiation.marked_seam
  - ucns.coordinate.angular_cut
known_collisions:
  - source-provenance seam and freely movable chart cut
effective_version: 0.15.0
supersedes: none
unresolved:
  - intrinsic-versus-marked target seam choice
```

### Full-carrier attachment evidence

```yaml
surface_form: full-carrier attachment evidence
term_id: ucns.carrier_relation.full_carrier_attachment_evidence
claiming_domain: UCNS carrier-relation research
claimed_sense: one nonselecting evidence graph joining full non-null analytic certificates to the bounded source-bound Structural Null initiation attachments without broadening either scope
scope: v0.15 report over the declared real non-null candidate and v0.13 minimum-packet root attachments
claim_type: specialized
authority_source: this specification
status: proposed
included_uses:
  - analytic RC01 and non-null RC03 evidence
  - exact v0.13 RC02 and RC04-RC10 evidence
  - explicit unresolved complete-relationship status
excluded_uses:
  - arbitrary observed-element transverse assignment
  - a total Structural Null-to-carrier relation
  - carrier selection or downstream activation
neighboring_terms:
  - ucns.carrier_relation.partial_structural_null_attachment
  - ucns.carrier_relation.real_continuity
known_collisions:
  - a completed global carrier implementation
effective_version: 0.15.0
supersedes: none
unresolved:
  - arbitrary-element assignment and total initiation relationship
```

## Exact affine proof

Let

\[
B_{\mathbb R}(u)=1+\frac{u}{2},\qquad
G_{\mathbb R}(b)=2(b-1).
\]

The endpoint identities are

\[
B_{\mathbb R}(-1)=\frac12,\quad
B_{\mathbb R}(1)=\frac32,\quad
G_{\mathbb R}\!\left(\frac12\right)=-1,\quad
G_{\mathbb R}\!\left(\frac32\right)=1.
\]

Both compositions are the identity by exact coefficient algebra. For every
real `epsilon > 0`, choose `delta_B = 2 epsilon`. Then

\[
|u-v|<\delta_B
\Longrightarrow
|B_{\mathbb R}(u)-B_{\mathbb R}(v)|
=\frac12|u-v|<\epsilon.
\]

For the inverse choose `delta_G = epsilon / 2`; then

\[
|b-c|<\delta_G
\Longrightarrow
|G_{\mathbb R}(b)-G_{\mathbb R}(c)|
=2|b-c|<\epsilon.
\]

This is a universal derivation over the declared real intervals, not a finite
grid test. The implementation records and validates its exact coefficients,
endpoints, compositions, and modulus multipliers. Python is not treated as a
proof assistant; the standing is `analytic-certificate-not-machine-checked`.

## Non-null quotient proof

Use the v0.12 spaces

\[
\widetilde{\mathcal M}=([-1,1]\times\mathbb R)/(t\sim t+2)
\]

and

\[
\mathcal C_B=([1/2,3/2]\times\mathbb R)/(t\sim t+2).
\]

The product map `f(u,t) = (B_R(u),t)` is continuous by the affine proof and
the identity map on turns. It is equivariant under the two-turn deck action:

\[
f(u,t+2)=(B_{\mathbb R}(u),t+2)\sim(B_{\mathbb R}(u),t)=f(u,t).
\]

It therefore descends to the declared continuous quotient map `F`. At any
chosen two-turn coordinate cut, the representative paths `(u,2-s)` and
`(u,s)` for `s -> 0+` converge to the same quotient class, and their images
do likewise. A moved coordinate cut changes only the representatives.

The one-turn sheet identity is exact:

\[
B_{\mathbb R}(-u)=1-\frac{u}{2}
=2-\left(1+\frac{u}{2}\right)
=2-B_{\mathbb R}(u).
\]

Hence

\[
F([-u,t+1]_2)=D(F([u,t]_2)).
\]

This supports `RC03` only for the declared non-null quotient map. The
provenance-bearing marked initiation seam is not a coordinate cut, and
Structural Null is not inserted into either real interval or treated as a
limit point.

## Combined evidence standing

| Obligation | v0.15 standing | Scope |
|---|---|---|
| `RC01` | analytic-supported | complete declared real affine intervals |
| `RC02` | exact-implemented-supported | v0.13 rational coordinate domain |
| `RC03` | analytic-supported | non-null quotient only |
| `RC04`–`RC10` | exact-implemented-supported | v0.13 minimum-packet root attachments |

The mixed scopes are intentional. The report may not relabel them as one
uniform runtime domain.

## Complete-relationship boundary

The v0.13 marked seam and twist receipt remain the only Structural Null
attachment. They are source-bound partial edges to the exact root. v0.15 adds
no law assigning an arbitrary observed element to `u`, no total initiation
relation, and no topology that makes Structural Null a point or limit of the
non-null carrier.

Therefore:

```text
non-null real continuity:       analytic-certificate-not-machine-checked
non-null quotient commutation:  analytic-certificate-not-machine-checked
Structural Null attachment:     source-bound-partial-root-attachment
complete carrier relationship:  inconclusive-without-arbitrary-element-assignment
carrier selection:              none
EDCM activation:                inactive
METAPAT activation:             inactive
```

## Falsification and tamper boundary

The implementation fails closed if any coefficient, endpoint, inverse,
epsilon-delta multiplier, deck period, sheet identity, upstream v0.13 report,
standing, scope, or activation field is substituted. Tests also construct
forged certificates to prove those substitutions are rejected.

## hmmm

- No arbitrary observed-element transverse assignment is supplied.
- No runtime arbitrary-real object model or machine-checked theorem is
  supplied.
- The total topology and relation from Structural Null to arbitrary non-null
  states remains unresolved.
- The marked-versus-intrinsic target seam choice remains unresolved.
- No full-carrier result selects canonical `B`, activates EDCM, activates
  METAPAT, or establishes higher-gonol composition.
