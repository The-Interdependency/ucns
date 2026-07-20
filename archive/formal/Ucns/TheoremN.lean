/-
  Ucns.TheoremN
  =============

  Lean 4 model of the UCNS Theorem N family and of the finite search it
  quantifies over.

  SOURCE OF TRUTH FOR THE CLAIMS: ../../ucns-theorem-n.md
  SOURCE OF TRUTH FOR THE SEARCH SEMANTICS: ../../ucns/factor_search_v08.py,
  ../../ucns/payload_system.py, ../../ucns/host_recovery.py

  STATUS: FRONTIER / awaiting external formal review.

  The three completeness theorems below are still closed with `sorry`.
  A `sorry` is an UNVERIFIED HOLE: Lean accepts the file, but nothing it
  closes is proven, and no DEFENDED status transfers downstream (see
  README.md).

  What changed relative to the earlier scaffold: `FindsFactorization` is
  no longer an opaque proposition standing in for the whole solver, and
  `ContainsPayloads` is no longer opaque. Both are now DEFINED over the
  faithful object model of `Ucns/Core.lean`:

  * `normalizedCandidates` — finite catalogue normalization with exactly
    one unit sentinel, first (mirrors `normalize_payload_catalogue`;
    structural dedup is omitted because it does not change membership,
    only enumeration order/size);
  * `splitCandidates` — host split enumeration `p = 2..n` then `p = 1`,
    divisors only (mirrors `_search_exhaustive`);
  * `recoverHostAngles` — structural host-angle extraction
    `A_angles[k] = P.cells[k*q].angle`, `B_angles[j] = P.cells[j].angle`
    (mirrors `recover_host_angles`);
  * `assignments` — all candidate payload assignments of a given length
    over the normalized candidates (superset ordering of the Python
    enumeration; membership agrees);
  * `faceAssignments` — all candidate face-bit assignments of a given
    length. DECLARED MODELING BOUNDARY: this is the full 2^k space,
    whereas `recover_face_structures` derives the at-most-two XOR-
    consistent options. The accepted witness spaces coincide because the
    final gate is exact recomposition, and any recomposing face
    assignment satisfies the XOR system that `recover_face_structures`
    solves completely. This equivalence is itself a proof obligation,
    recorded in ../../audit/obligation_ledger.md.
  * `assemble` — candidate factor construction from angles, payloads,
    and faces. DECLARED MODELING BOUNDARY: no re-normalization is
    applied (the Python constructor normalizes; for host-normalized
    products of normalized factors the recovered angles are already
    gauge-fixed). Recorded in the obligation ledger.
  * `isMultiplicativeUnit` — executable unit-group rejection (mirrors
    `is_multiplicative_unit`);
  * `searchCandidates` / `AcceptedWitness` / `FindsFactorization` — the
    success relation is a defined existential whose witness carries the
    ACTUAL candidate factors and the ACTUAL product equality
    `multiply A' B' = P`. No opaque success predicate remains.

  The Python side of the shared conformance fixture lives in
  ../../tests/test_formal_conformance.py: it re-enumerates this model's
  witness space literally and compares it against the executable
  solver's witness space on the declared fixture domain.
-/

-- === MODULE_BUILD ===
-- id: ucns_formal_theorem_n_search_model
--   module_name: Ucns.TheoremN
--   module_kind: schema
--   summary: Defined (non-opaque) finite-search model for factor_search_v08 - catalogue normalization, split/host/payload/face enumeration, unit rejection, exact-recomposition success relation - plus the Theorem N statement family over it.
--   owner: Erin Spencer
--   public_surface: multiply, width, Catalogue, normalizedCandidates, splitCandidates, recoverHostAngles, assignments, faceAssignments, assemble, isMultiplicativeUnit, searchCandidates, AcceptedWitness, FindsFactorization, ContainsPayloads, depth1_restricted_completeness, lemma7_depth2_oracle_completeness, theoremN_catalogue_sufficient_completeness
--   internal_surface: PayloadsSubset, PayloadsSubsetCells, PayloadsSubsetCell
--   auth_boundary: none
--   storage_boundary: none
--   network_boundary: none
--   user_data_boundary: none
--   admin_only: false
--   tests: lake build (type-check only); tests/test_formal_conformance.py (Python-side witness-space conformance)
--   rollout: built by the formal CI job
--   rollback: restore the opaque-predicate scaffold from git history
--   requires: ucns_formal_core_definitions
--   since: 2026-07-12
--   unresolved: face-superset equivalence and no-renormalization boundary are undischarged obligations; the three completeness theorems remain sorry; not machine-checked in the authoring environment (no Lean toolchain) - CI formal.yml is the checking authority
-- === END MODULE_BUILD ===

import Ucns.Core

namespace Ucns

open UCNSObject

/-- The depth-agnostic product, at fuel sufficient for both operands. -/
def multiply (A B : UCNSObject) : UCNSObject :=
  multiplyFuel (Nat.max (depth A) (depth B)) A B

/-- Number of top-level `A_plus` cells of an object (`|A.A_plus|`). -/
def width (x : UCNSObject) : Nat := x.cells.length

/-- A catalogue `C`: a candidate set of payloads (`UCNSObject | None`),
    modelled as a list of objects (the unit payload is made explicit by
    `normalizedCandidates`). -/
abbrev Catalogue : Type := List UCNSObject

/-! ## Finite search model -/

/-- Finite catalogue normalization with exactly one unit sentinel, first.
    Mirrors `normalize_payload_catalogue`: the unit payload `none` appears
    exactly once and first; remaining candidates preserve caller order.
    Structural deduplication is intentionally not modelled — it changes
    the enumeration's size, never its membership. -/
def normalizedCandidates (C : Catalogue) : List (Option UCNSObject) :=
  none :: C.map some

/-- Host split candidates for a product of width `n`: divisor pairs
    `(p, n / p)` with `p = 2..n` first and the `p = 1` fallback last,
    exactly as `_search_exhaustive` orders them. -/
def splitCandidates (n : Nat) : List (Nat × Nat) :=
  (((List.range (n + 1)).drop 2) ++ [1]).filterMap
    (fun p => if 0 < p ∧ n % p = 0 then some (p, n / p) else none)

/-- Structural host-angle recovery from the product, mirroring
    `recover_host_angles`: `A_angles[k] = P.cells[k*q].angle` and
    `B_angles[j] = P.cells[j].angle`. Out-of-range indices (impossible
    for genuine splits of `width P`) default to the zero-angle cell. -/
def recoverHostAngles (P : UCNSObject) (p q : Nat) : List Rat × List Rat :=
  ((List.range p).map
      (fun k => (P.cells.getD (k * q) ⟨0, false, none⟩).angle),
   (List.range q).map
      (fun j => (P.cells.getD j ⟨0, false, none⟩).angle))

/-- All candidate payload assignments of length `k` over a candidate
    list. Enumeration order differs from the Python solver's; membership
    is what the model quantifies over. -/
def assignments (cands : List (Option UCNSObject)) :
    Nat → List (List (Option UCNSObject))
  | 0 => [[]]
  | k + 1 =>
    (assignments cands k).bind (fun rest => cands.map (fun c => c :: rest))

/-- All candidate face-bit assignments of length `k`. See the module
    header: this is a declared superset of the at-most-two XOR-consistent
    options that `recover_face_structures` derives; the accepted witness
    spaces coincide under the exact-recomposition gate (undischarged
    obligation). -/
def faceAssignments : Nat → List (List Bool)
  | 0 => [[]]
  | k + 1 =>
    (faceAssignments k).bind
      (fun rest => [false, true].map (fun b => b :: rest))

/-- Candidate factor assembly from recovered angles, a payload
    assignment, and a face assignment (declared carrier inherited from
    the product, as in `_search_exhaustive`). No re-normalization is
    applied — a declared modeling boundary recorded in the obligation
    ledger. -/
def assemble (nd : Nat) (angles : List Rat)
    (payloads : List (Option UCNSObject)) (faces : List Bool) : UCNSObject :=
  UCNSObject.mk nd
    (((angles.zip payloads).zip faces).map
      (fun az => { angle := az.1.1, face := az.2, payload := az.1.2 }))

/-- Executable multiplicative-unit-group membership, mirroring
    `is_multiplicative_unit`: width one and unit payload, any face bit. -/
def isMultiplicativeUnit (x : UCNSObject) : Bool :=
  match x.cells with
  | [c] => c.payload.isNone
  | _ => false

/-- The finite candidate enumeration of the modelled search: every
    split, payload assignment, and face assignment, assembled into a
    candidate factor pair. This is the space the solver walks; acceptance
    is separate (`AcceptedWitness`). -/
def searchCandidates (P : UCNSObject) (C : Catalogue) :
    List (UCNSObject × UCNSObject) :=
  (splitCandidates (width P)).bind (fun pq =>
    let hosts := recoverHostAngles P pq.1 pq.2
    (assignments (normalizedCandidates C) pq.1).bind (fun sa =>
      (assignments (normalizedCandidates C) pq.2).bind (fun sb =>
        (faceAssignments pq.1).bind (fun fa =>
          (faceAssignments pq.2).map (fun fb =>
            (assemble P.nDec hosts.1 sa fa,
             assemble P.nDec hosts.2 sb fb))))))

/-- Acceptance of a candidate pair: both candidates survive unit-group
    rejection and the pair EXACTLY recomposes to the product. The witness
    carries the actual factors and the actual product equality. -/
def AcceptedWitness (P : UCNSObject) (pair : UCNSObject × UCNSObject) : Prop :=
  isMultiplicativeUnit pair.1 = false ∧
  isMultiplicativeUnit pair.2 = false ∧
  multiply pair.1 pair.2 = P

/-- `FindsFactorization P C`: the modelled finite search over `C` accepts
    at least one candidate pair for `P`. This is a DEFINED existential
    finite-search outcome — the success witness contains actual factors
    and the exact recomposition equality — not an opaque proposition. -/
def FindsFactorization (P : UCNSObject) (C : Catalogue) : Prop :=
  ∃ pair ∈ searchCandidates P C, AcceptedWitness P pair

/-! ## Catalogue sufficiency -/

/-! Recursive payload containment: every payload appearing recursively in
    the object is a member of the catalogue (the unit payload is implicit
    — `normalizedCandidates` always supplies it). Mirrors the Theorem N
    catalogue hypothesis and `catalogue_from_objects`. -/
mutual
  def PayloadsSubset : UCNSObject → Catalogue → Prop
    | UCNSObject.mk _ cs, C => PayloadsSubsetCells cs C
  def PayloadsSubsetCells : List (Cell UCNSObject) → Catalogue → Prop
    | [], _ => True
    | c :: rest, C => PayloadsSubsetCell c C ∧ PayloadsSubsetCells rest C
  def PayloadsSubsetCell : Cell UCNSObject → Catalogue → Prop
    | ⟨_, _, none⟩, _ => True
    | ⟨_, _, some p⟩, C => p ∈ C ∧ PayloadsSubset p C
end

/-- `ContainsPayloads C X` holds when the catalogue `C` contains every
    payload appearing recursively in `X` (the identity is implicit).
    Single catalogue hypothesis of Theorem N — now a defined predicate
    over the real object type, independently testable cell by cell. -/
def ContainsPayloads (C : Catalogue) (X : UCNSObject) : Prop :=
  PayloadsSubset X C

/-! ## Theorem statement family

    All three statements below remain closed by `sorry`: they are
    UNVERIFIED HOLES awaiting proof and external formal review, and they
    confer no DEFENDED status. What is no longer a hole is their
    MEANING — the conclusion now unfolds to "some enumerated candidate
    pair survives unit rejection and exactly recomposes". -/

/--
  **Depth-1 restricted completeness (statement; unproven).**

  Informal claim: for depth-1 factors `A`, `B` whose (atomic) payloads are
  all present in the catalogue `C`, the modelled search accepts a
  factorization of `P = multiply A B` (cf. `ucns-theorem-n.md` §4).

  UNVERIFIED: closed by `sorry`.
-/
theorem depth1_restricted_completeness
    (A B : UCNSObject) (C : Catalogue)
    (hA : depth A ≤ 1) (hB : depth B ≤ 1)
    (hwA : 1 ≤ width A) (hwB : 1 ≤ width B)
    (huA : isMultiplicativeUnit A = false)
    (huB : isMultiplicativeUnit B = false)
    (hCA : ContainsPayloads C A) (hCB : ContainsPayloads C B) :
    FindsFactorization (multiply A B) C := by
  sorry

/--
  **Lemma 7 — depth-2 oracle completeness (statement; unproven).**

  Informal claim (`ucns-theorem-n.md` §4.1): for `A, B` in the depth-2
  oracle class (depth ≤ 2), every payload of `A` and `B` is a depth-1
  oracle atom and so lies in the generated payload catalogue `C`; the
  modelled search then accepts a factorization. Presented as an instance
  of Theorem N.

  UNVERIFIED: closed by `sorry`.
-/
theorem lemma7_depth2_oracle_completeness
    (A B : UCNSObject) (C : Catalogue)
    (hA : depth A ≤ 2) (hB : depth B ≤ 2)
    (hwA : 1 ≤ width A) (hwB : 1 ≤ width B)
    (huA : isMultiplicativeUnit A = false)
    (huB : isMultiplicativeUnit B = false)
    (hCA : ContainsPayloads C A) (hCB : ContainsPayloads C B) :
    FindsFactorization (multiply A B) C := by
  sorry

/--
  **Theorem N — catalogue-sufficient factorization (statement; unproven).**

  Informal claim (`ucns-theorem-n.md` §2): let `A`, `B` be UCNS objects
  with `|A.A_plus|, |B.A_plus| ≥ 1`, neither in the multiplicative unit
  group, and let `C` contain every payload appearing recursively in `A`
  or `B`. Then the modelled exhaustive search over `C` accepts SOME pair
  `(A', B')` with `multiply A' B' = P` for `P = multiply A B`. This is an
  exhaustive-inclusion completeness target: NO cancellativity, NO
  quotient uniqueness, and NO recovery of the original pair is claimed.

  UNVERIFIED: closed by `sorry`.
-/
theorem theoremN_catalogue_sufficient_completeness
    (A B : UCNSObject) (C : Catalogue)
    (hwA : 1 ≤ width A) (hwB : 1 ≤ width B)
    (huA : isMultiplicativeUnit A = false)
    (huB : isMultiplicativeUnit B = false)
    (hCA : ContainsPayloads C A) (hCB : ContainsPayloads C B) :
    FindsFactorization (multiply A B) C := by
  sorry

end Ucns
