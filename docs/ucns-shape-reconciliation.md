# UCNS Shape Reconciliation (UCNS-A ⟷ UCNS-G)

## Scope and method

This document resolves whether the repository's recursive algebraic UCNS object (UCNS-A) and the session-defined metric geometry UCNS object (UCNS-G) are the same construction at different layers, or parallel constructions sharing a name.

I treated source code/spec as authoritative and explicitly checked the files listed in the task brief.

---

## Corrected UCNS-A inventory (source-verified)

### 1) Core object and fields

UCNS-A is implemented as `UCNSObject(n_dec, n_min, A_plus, F_plus)` in `ucns_recursive/canonical.py`.

- `A_plus` is a list of `(angle, payload)` where `payload` is `UCNSObject | None`.
- `None` is the unit/sentinel payload (`UNIT = None`).
- `F_plus` is a parallel bit list (0/1) per stored anchor/cell.

### 2) Angle domain and representation

Angles are represented as `fractions.Fraction` values (`FractionType = Fraction`) and normalized modulo 4 via `% 4`.

Interpretation from code + docs:
- internal angle space is a doubled cover with period 4 (equivalent to `4π` in the prose spec),
- minimal-carrier computation projects through `(a % 2) / 2`, i.e., single-cover lattice membership for `n_min` while retaining doubled-cover angle storage.

### 3) `n_dec` and `n_min`

- `n_min` is intrinsic and recomputed from angles as LCM of denominators from projected circle fractions.
- `n_dec` is declared/presentation carrier, required to be a multiple of `n_min`; else object construction fails.

### 4) Star/mirror and face behavior

Normalization computes mirror data:
- `A_minus`: reverse sequence with negated angles modulo 4; payloads are recursively disk-flipped via `_disk_flip`.
- `F_minus`: reverse of `F_plus` only (no bit negation).

### 5) Multiplication semantics

`multiply(A,B)` builds full `|A|×|B|` cells.

For each `(k,j)`:
- angle: `(alpha_k + (beta_j - beta0)) % 4`,
- payload: recursive composition (`multiply`) when both payloads exist, otherwise non-`None` payload is passed through,
- face bit: XOR (`f_k_A ^ f_j_B`).

This is depth-agnostic recursion exactly as the brief states (no depth-specific branch logic).

### 6) What UCNS-A does **not** natively store in the object

`UCNSObject` itself has no explicit scalar fields for:
- radius/magnitude `r`,
- winding count/loop counter `z`,
- area-percent measure.

Those quantities are not part of the canonical recursive object structure in `ucns_recursive/canonical.py`.

### 7) Discrepancies versus the brief’s UCNS-A summary

- The brief asked whether angle might be `Fraction`; source confirms **yes**, angle is `Fraction`-typed.
- The brief asked whether face-flip is per-cell and what it does; source confirms per-cell bit in product is XOR composition, while mirror/star uses reverse-only for `F_minus`.
- The brief was uncertain on 360 vs 720-period handling; source indicates doubled-cover arithmetic (`mod 4`) and spec prose explicitly states doubled angular cover (`4π`).

---

## Candidate correspondence table (resolved)

| UCNS-G element | Candidate UCNS-A counterpart | Status | Resolution |
|---|---|---|---|
| `θ` (period 720°) | `A_plus` angle field | **MATCH** | UCNS-A angles are stored in doubled-cover coordinates (mod 4, equivalent to mod `4π` in spec prose), which matches the 720° period claim at the angular-cover level. |
| chirality / 360° sheet-flip | `F_plus` face-flip bit | **PARTIAL** | UCNS-A has explicit face bits and XOR accumulation under multiplication, plus doubled-cover orientation language in spec. But it does **not** expose a standalone “spinor closes at 2” variable; behavior is encoded via angle cover + face-bit algebra. |
| epicyclic composition / recursion-depth ladder | recursive payload nesting + `multiply` | **PARTIAL** | UCNS-A recursion depth exists and composes recursively. But UCNS-G’s named operational ladder (turn→round→session renormalization semantics) is not explicitly encoded as those labels/policies in UCNS-A core object. |
| gonal inscription / coordinate chart | (unknown) | **PARTIAL** | UCNS-A defines gonal lattice / carrier semantics and embedding helpers elsewhere (`circle_to_disk(theta, r)`), but there is no canonical UCNS-A object-level coordinate chart mapping of the form `(r, θ, z)` for recursive objects. |
| `r` (magnitude/radius) | unmatched | **NONE (in UCNS-A object)** | No `r` field exists in `UCNSObject`. Radius appears only as a parameter in auxiliary geometry/similarity helpers (`mobius.circle_to_disk`, `similarity.hyperbolic_cosine`) for embeddings, not as canonical recursive-number state. |
| `z` (winding) / DVG (loop count) | unmatched | **NONE** | No explicit winding-number/loop-count variable or derived DVG metric appears in UCNS-A canonical object or multiplication semantics. |
| area-percent / DRIFT | unmatched | **NONE** | No area-percent accounting exists in canonical UCNS-A object, normalization, or multiplication. |
| UCNS-A multiply/factorization vs UCNS-G coordinates | `multiply` / `factor_search_v08` / catalogue | **NONE (as stated)** | UCNS-A has explicit algebra + factorization theorem scope; UCNS-G statement in task defines a metric coordinate/measurement frame and does not include a source-backed multiplication/factorization structure in `(r,θ,z)` terms. |

---

## Geometry modules check (`ucns/*`) and whether they unify UCNS-G

Repository geometry/embedding modules do include disk and radius concepts, but at a different layer:

- `ucns/core.py`: unit-circle angle object `UCN` with period `2π` (`TAU`) and circle metrics.
- `ucns/mobius.py`: Poincaré-disk Möbius transforms with interior complex points and optional radial embedding helper (`circle_to_disk(theta, r)`).
- `ucns/epicycle.py`: FFT decomposition with amplitude/radius and phase per frequency component.
- `ucns/embedding.py` + `ucns/similarity.py`: embedding vectors of phases and multiple similarity metrics including hyperbolic cosine with user-chosen `radius`.

These modules establish that the repository contains **a** geometry/embedding layer with radii and disk metrics. But this is not the same as proving the canonical recursive UCNS-A number object equals a single `(r, θ, z)` state with DRIFT/DVG semantics.

No source path found that realizes all of UCNS-G’s required tuple fields and derived metrics (`r`, `θ@720`, `z`, DRIFT area-percent, DVG loop count) as canonical coordinates of `UCNSObject`.

---

## Sharpest divergence point

The first decisive divergence is object ontology:

- UCNS-A canonical object is a **recursive ordered sequence of anchors with payload trees and face bits**.
- UCNS-G is defined as a **single-point coordinate triple `(r, θ, z)`** with external metrics (DRIFT, DVG).

Without source-backed functions that map `UCNSObject` ↔ `(r, θ, z)` and recover DRIFT/DVG from canonical UCNS-A state, they are not the same object in current repo canon.

---

## Verdict

## **PARALLEL**

UCNS-A and UCNS-G currently appear to be distinct constructions sharing the name “UCNS,” with partial conceptual overlap (doubled-cover angle/orientation language and Möbius/disk vocabulary), but no full source-backed coordinate correspondence.

- UCNS-A is a recursive algebra with multiplication/factorization semantics and theorem-scoped completeness conditions.
- UCNS-G (as stated in the task) is a metric/accounting frame with `(r, θ, z)` and DRIFT/DVG, lacking demonstrated in-repo algebraic realization as UCNS-A canonical state.

Per firewall rule: Theorem N remains scoped to UCNS-A factorization/search claims and does not transfer to UCNS-G metric claims.

---

## hmmm

- I did not find a canonical source function establishing a bijection (or even total map) between `UCNSObject` and `(r, θ, z)` with DRIFT/DVG extraction.
- There is an internal split between legacy/public `ucns` geometry/embedding modules (mostly `2π` angle APIs plus optional disk radius) and recursive canonical algebra in `ucns_recursive`; naming overlap may be causing semantic bleed.
- If a unification is desired, it likely requires a new explicit spec bridge defining:
  1) coordinate projection from recursive anchor/payload trees to `(r, θ, z)`,
  2) formal definitions of DRIFT and DVG in terms of canonical UCNS-A invariants,
  3) proof/status boundary labels so theorem scope remains non-transfer by default.
