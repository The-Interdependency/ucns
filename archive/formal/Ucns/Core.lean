/-
  Ucns/Core.lean — faithful definitions for the UCNS recursive algebra.

  SOURCE OF TRUTH FOR SEMANTICS: ../../ucns/canonical.py
  and ../../ucns-spec.md. This file replaces the `Unit` placeholder
  carrier of the original scaffold with the real recursive
  (angle, face, payload) sequence object.

  MODELING DECISIONS (declared, not hidden):

  1. Angles are `Rat` (Lean core rationals), taken mod 4 via `amod4`,
     mirroring `Fraction` angles in `[0, 4)`.
  2. `normalize` and `multiply` recurse into payloads. Rather than fight
     the nested-inductive termination checker, they are FUEL-INDEXED:
     `normalizeFuel d x` / `multiplyFuel d a b` recurse structurally on
     the fuel `d : Nat`. This matches the repository's own domain
     discipline — every DEFENDED claim is depth-bounded (frozen domain:
     depth ≤ 2) — so fuel is the depth bound made explicit. For any
     object of depth ≤ d, fuel d computes the intended total function.
  3. Faces are `Bool`; face combination is `xor`, mirroring `F_plus` XOR.
  4. `nMin` is computed exactly as `_compute_n_min`: lcm of denominators
     of nonzero circle-fractions `(a mod 2) / 2`.

  PROOF-STATUS NON-TRANSFER DISCIPLINE (see README.md): definitions in
  this file are definitions, not theorems. Any theorem stated here or in
  TheoremN.lean that is closed by `sorry` confers NO DEFENDED status.
-/

-- === MODULE_BUILD ===
-- id: ucns_formal_core_definitions
--   module_name: Ucns.Core
--   module_kind: schema
--   summary: Faithful Lean 4 model of UCNSObject, carrier (nMin), depth, fuel-indexed normalize and multiply, and the statement surface for the Carrier-LCM Law and cancellativity counterexample/status.
--   owner: Erin Spencer
--   public_surface: UCNSObject, Cell, amod4, circleFrac, nMin, depth, normalizeFuel, multiplyFuel, HostNormalized, Complete/AlignedComplete (with NonemptyRec/HostNormalizedRec/UniformDepth/CanonicalCarrier), not_multiply_left_cancellative_on_alignedComplete (guardrail counterexample)
--   internal_surface: angleDenoms
--   auth_boundary: none
--   storage_boundary: none
--   network_boundary: none
--   user_data_boundary: none
--   admin_only: false
--   tests: lake build (type-checking); no sorry-free theorems yet — see formal/README.md
--   rollout: built by the formal CI job; imports nothing outside Lean core
--   rollback: remove file and its import from TheoremN.lean
--   requires: none
--   since: 2026-06-09
--   unresolved: AlignedComplete cancellativity as previously stated is refuted by a concrete mod-4 tail-angle counterexample; next true theorem needs canonical angle-range/floor-zero evidence. Carrier-LCM is discharged in Ucns/CarrierLcm.lean; remaining order — repair cancellativity domain, then depth1 completeness
-- === END MODULE_BUILD ===

import Std.Data.Rat.Basic
import Std.Data.Nat.Gcd
import Std.Data.List.Lemmas
import Mathlib.Tactic

namespace Ucns

/-- A cell: host angle, face bit, optional recursive payload. -/
structure Cell (α : Type) where
  angle : Rat
  face  : Bool
  payload : Option α
  deriving Repr

/-- A UCNS object: a nonempty-in-practice list of cells whose payloads
    are themselves UCNS objects. `n_dec` (declared carrier) is carried
    separately, as in the Python implementation. -/
inductive UCNSObject where
  | mk (nDec : Nat) (cells : List (Cell UCNSObject)) : UCNSObject
  deriving Repr

namespace UCNSObject

def nDec : UCNSObject → Nat
  | mk d _ => d

def cells : UCNSObject → List (Cell UCNSObject)
  | mk _ cs => cs

/-- Reduce a rational into `[0, n)` (n > 0), mirroring Python `% n`
    on `Fraction`s. -/
def amod (a : Rat) (n : Nat) : Rat :=
  a - (n : Rat) * (((a / (n : Rat)).floor : Int) : Rat)

def amod4 (a : Rat) : Rat := amod a 4

/-- If a rational already has quotient floor zero when divided by four, then
    reducing it modulo four leaves it unchanged. This is the small arithmetic
    bridge needed to turn canonical `[0,4)` range facts into `amod4`
    fixed-point facts. -/
theorem amod4_eq_self_of_floor_div_four_eq_zero
    (a : Rat) (h : (a / (4 : Rat)).floor = 0) :
    amod4 a = a := by
  unfold amod4 amod
  have h' : Rat.floor (a / ↑(4 : Nat)) = 0 := by
    simpa using h
  rw [h']
  norm_num

/-- Circle fraction `(a mod 2) / 2`, as in `_compute_n_min`. -/
def circleFrac (a : Rat) : Rat := amod a 2 / 2

/-- Denominators of nonzero circle fractions of a cell list. -/
def angleDenoms (cs : List (Cell UCNSObject)) : List Nat :=
  (cs.map (fun c => circleFrac c.angle)).filterMap
    (fun q => if q = 0 then none else some q.den)

/-- The minimal carrier: lcm of nonzero circle-fraction denominators
    (empty lcm = 1). Host-level only — payloads do not enter, exactly
    as in `_compute_n_min`. -/
def nMin (x : UCNSObject) : Nat :=
  (angleDenoms x.cells).foldl Nat.lcm 1

/-! Payload-nesting depth: `none → 0`; object depth is
    `1 + max payload depth` (0 for a flat object), matching
    `ucns.domains.depth_of` up to the flat-object base case. -/
mutual
  def depth : UCNSObject → Nat
    | mk _ cs => 1 + depthCells cs
  def depthCells : List (Cell UCNSObject) → Nat
    | [] => 0
    | c :: rest => Nat.max (depthCell c) (depthCells rest)
  def depthCell : Cell UCNSObject → Nat
    | ⟨_, _, none⟩ => 0
    | ⟨_, _, some p⟩ => depth p
end

/-- Fuel-indexed normalization. Fuel 0 is the identity (out of budget);
    fuel (d+1) shifts host angles by the first angle and normalizes
    payloads with fuel d. For `x` with `depth x ≤ d`, `normalizeFuel d x`
    is the intended total normalization. -/
def normalizeFuel : Nat → UCNSObject → UCNSObject
  | 0, x => x
  | d + 1, mk nd cs =>
    let θ0 : Rat := match cs.head? with
      | some c => c.angle
      | none => 0
    mk nd (cs.map (fun c =>
      { angle := amod4 (c.angle - θ0)
        face := c.face
        payload := c.payload.map (normalizeFuel d) }))

/-- Fuel-indexed ordered-concatenation product `A ⊠ B`, mirroring
    `multiply` in `canonical.py`: row-major cross product of cells,
    angles `αₖ + (βⱼ - β₀)` mod 4, faces XOR, payloads multiplied
    recursively (unit `none` is the payload identity). -/
def multiplyFuel : Nat → UCNSObject → UCNSObject → UCNSObject
  | 0, a, _ => a
  | d + 1, mk nda csA, mk ndb csB =>
    let β0 : Rat := match csB.head? with
      | some c => c.angle
      | none => 0
    let newCells :=
      csA.bind (fun ca =>
        csB.map (fun cb =>
          { angle := amod4 (ca.angle + (cb.angle - β0))
            face := xor ca.face cb.face
            payload :=
              match ca.payload, cb.payload with
              | some p, some q => some (multiplyFuel d p q)
              | some p, none   => some p
              | none,   some q => some q
              | none,   none   => none }))
    mk (Nat.lcm nda ndb) newCells

/-- One row of the row-major successor-fuel product cell list, for a fixed
    left cell. This is factored out only as a proof aid for cancellativity. -/
def multiplyRow (d : Nat) (csB : List (Cell UCNSObject)) (ca : Cell UCNSObject) :
    List (Cell UCNSObject) :=
  let β0 : Rat := match csB.head? with
    | some c => c.angle
    | none => 0
  csB.map (fun cb =>
    { angle := amod4 (ca.angle + (cb.angle - β0))
      face := xor ca.face cb.face
      payload :=
        match ca.payload, cb.payload with
        | some p, some q => some (multiplyFuel d p q)
        | some p, none   => some p
        | none,   some q => some q
        | none,   none   => none })

/-- One successor-fuel product row with the right-head baseline supplied
    explicitly. This is the "tail row" shape after the selected right head has
    been peeled: non-head right cells are still measured against the original
    right-head angle, not against the tail's own head. -/
def multiplyRowWithBase (d : Nat) (β0 : Rat)
    (csB : List (Cell UCNSObject)) (ca : Cell UCNSObject) :
    List (Cell UCNSObject) :=
  csB.map (fun cb =>
    { angle := amod4 (ca.angle + (cb.angle - β0))
      face := xor ca.face cb.face
      payload :=
        match ca.payload, cb.payload with
        | some p, some q => some (multiplyFuel d p q)
        | some p, none   => some p
        | none,   some q => some q
        | none,   none   => none })

/-- Peeling the selected right head from a product row leaves the tail mapped
    with the original selected right-head angle as baseline. -/
theorem multiplyRow_cons_tail_eq_multiplyRowWithBase
    (d : Nat) (ca b : Cell UCNSObject) (bs : List (Cell UCNSObject)) :
    (multiplyRow d (b :: bs) ca).tail =
      multiplyRowWithBase d b.angle bs ca := by
  simp [multiplyRow, multiplyRowWithBase]

/-- The row-major cell list generated by the successor-fuel product branch.
    This is definitionally the `newCells` expression inside `multiplyFuel`; it
    is factored out only as a proof aid for cancellativity. -/
def multiplyCells (d : Nat)
    (csA csB : List (Cell UCNSObject)) : List (Cell UCNSObject) :=
  csA.bind (multiplyRow d csB)

theorem multiplyRow_length
    (d : Nat) (csB : List (Cell UCNSObject)) (ca : Cell UCNSObject) :
    (multiplyRow d csB ca).length = csB.length := by
  simp [multiplyRow]

/-- The successor product cell list has rectangular row-major length. This is
    an intentionally small "opinion-making" invariant: before proving full
    cancellativity, product equality already forces observable shape data. -/
theorem multiplyCells_length
    (d : Nat) (csA csB : List (Cell UCNSObject)) :
    (multiplyCells d csA csB).length = csA.length * csB.length := by
  induction csA with
  | nil =>
      simp [multiplyCells]
  | cons ca rest ih =>
      simp [multiplyCells] at ih ⊢
      rw [multiplyRow_length, ih]
      simp [Nat.succ_mul, Nat.add_comm]

/-- If a nonempty left factor gives equal successor-product cell lists, then
    the right factors already have equal top-level cell counts. This is weaker
    than cancellativity, but it is a useful observable invariant extracted from
    the row-major product shape. -/
theorem right_cells_length_eq_of_multiplyCells_eq
    (d : Nat) (csA csB csC : List (Cell UCNSObject))
    (hA : csA ≠ [])
    (h : multiplyCells d csA csB = multiplyCells d csA csC) :
    csB.length = csC.length := by
  have hlen : (multiplyCells d csA csB).length =
      (multiplyCells d csA csC).length := congrArg List.length h
  rw [multiplyCells_length, multiplyCells_length] at hlen
  have hpos : 0 < csA.length := by
    cases csA with
    | nil => exact False.elim (hA rfl)
    | cons _ _ => simp
  exact Nat.mul_left_cancel hpos hlen

theorem first_row_eq_of_multiplyCells_eq
    (d : Nat) (ca : Cell UCNSObject)
    (rest csB csC : List (Cell UCNSObject))
    (hlen : csB.length = csC.length)
    (h : multiplyCells d (ca :: rest) csB =
      multiplyCells d (ca :: rest) csC) :
    multiplyRow d csB ca = multiplyRow d csC ca := by
  simp [multiplyCells] at h
  have ht := congrArg (fun xs => xs.take (multiplyRow d csB ca).length) h
  have hrowLen : (multiplyRow d csC ca).length = (multiplyRow d csB ca).length := by
    simp [multiplyRow_length, hlen.symm]
  simpa [List.take_left, List.take_left' hrowLen] using ht

theorem multiplyFuel_succ_eq_mk
    (d nda ndb : Nat) (csA csB : List (Cell UCNSObject)) :
    multiplyFuel (d + 1) (UCNSObject.mk nda csA) (UCNSObject.mk ndb csB) =
      UCNSObject.mk (Nat.lcm nda ndb) (multiplyCells d csA csB) := by
  rfl

/-- Equality of successor-fuel products exposes equality of their row-major
    product cell lists. This is the first concrete list-level obligation behind
    cancellativity once `AlignedComplete` has ruled out zero fuel. -/
theorem multiplyCells_eq_of_multiplyFuel_succ_eq
    (d nda ndb ndc : Nat) (csA csB csC : List (Cell UCNSObject))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda csA) (UCNSObject.mk ndb csB) =
        multiplyFuel (d + 1) (UCNSObject.mk nda csA) (UCNSObject.mk ndc csC)) :
  multiplyCells d csA csB = multiplyCells d csA csC := by
  rw [multiplyFuel_succ_eq_mk, multiplyFuel_succ_eq_mk] at h
  injection h with _ hcells

/-- Equality of successor-fuel products also exposes equality of the product
    carriers. This is intentionally separate from the cell-list equality:
    cancellativity cannot rely on `Nat.lcm` cancellation alone, but the carrier
    equality is still one of the product equality's observable components. -/
theorem productCarrier_eq_of_multiplyFuel_succ_eq
    (d nda ndb ndc : Nat) (csA csB csC : List (Cell UCNSObject))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda csA) (UCNSObject.mk ndb csB) =
        multiplyFuel (d + 1) (UCNSObject.mk nda csA) (UCNSObject.mk ndc csC)) :
  Nat.lcm nda ndb = Nat.lcm nda ndc := by
  rw [multiplyFuel_succ_eq_mk, multiplyFuel_succ_eq_mk] at h
  injection h with hcarrier _

/-- Successor-product equality with a nonempty left cell list forces equal
    top-level cell counts on the two right operands. This is another small,
    executable piece of the cancellativity argument: row-major rectangular shape
    is cancellative even before cell contents are inverted. -/
theorem right_cells_length_eq_of_multiplyFuel_succ_eq
    (d nda ndb ndc : Nat) (csA csB csC : List (Cell UCNSObject))
    (hA : csA ≠ [])
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda csA) (UCNSObject.mk ndb csB) =
        multiplyFuel (d + 1) (UCNSObject.mk nda csA) (UCNSObject.mk ndc csC)) :
    csB.length = csC.length := by
  exact right_cells_length_eq_of_multiplyCells_eq d csA csB csC hA
    (multiplyCells_eq_of_multiplyFuel_succ_eq d nda ndb ndc csA csB csC h)

theorem first_row_eq_of_multiplyFuel_succ_eq
    (d nda ndb ndc : Nat) (ca : Cell UCNSObject)
    (rest csB csC : List (Cell UCNSObject))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb csB) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc csC)) :
    multiplyRow d csB ca = multiplyRow d csC ca := by
  have hcells :
      multiplyCells d (ca :: rest) csB = multiplyCells d (ca :: rest) csC :=
    multiplyCells_eq_of_multiplyFuel_succ_eq d nda ndb ndc (ca :: rest) csB csC h
  have hlen : csB.length = csC.length :=
    right_cells_length_eq_of_multiplyCells_eq d (ca :: rest) csB csC
      (by simp) hcells
  exact first_row_eq_of_multiplyCells_eq d ca rest csB csC hlen hcells

/-- First-row equality also preserves the unselected tail of the transformed
    right-row cells. This is the list-induction handhold after the selected
    right head has been inverted: it peels the head product cell and leaves the
    mapped tail products as an equality to be consumed by the next tail step. -/
theorem tail_product_cells_eq_of_first_row_eq
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    multiplyRowWithBase d b.angle bs ca =
      multiplyRowWithBase d c.angle cs ca := by
  rw [← multiplyRow_cons_tail_eq_multiplyRowWithBase d ca b bs,
    ← multiplyRow_cons_tail_eq_multiplyRowWithBase d ca c cs]
  exact congrArg List.tail hrow

/-- Raw successor-product version of `tail_product_cells_eq_of_first_row_eq`:
    equality of full products exposes first-row equality, then peeling the
    selected right-head product cell yields equality of the first-row tails. -/
theorem tail_product_cells_eq_of_multiplyFuel_succ_eq
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    multiplyRowWithBase d b.angle bs ca =
      multiplyRowWithBase d c.angle cs ca := by
  exact tail_product_cells_eq_of_first_row_eq d ca b c bs cs
    (first_row_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca rest (b :: bs) (c :: cs) h)

/-- If the selected right-head angles have already been identified, the mapped
    first-row tail equality can be placed over one common baseline. This is the
    exact shape needed before trying to invert individual non-head tail cells:
    both tails are transformed by the same angle offset. -/
theorem tail_product_cells_eq_of_multiplyFuel_succ_eq_commonBase
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hangle : b.angle = c.angle)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    multiplyRowWithBase d b.angle bs ca =
      multiplyRowWithBase d b.angle cs ca := by
  simpa [hangle] using
    tail_product_cells_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca b c rest bs cs h





/-- Boolean xor is cancellative in its right argument. This is the tiny face-bit
    algebra needed when a product row exposes `xor left.face right.face` on both
    sides. -/
theorem bool_xor_left_cancel {a b c : Bool} (h : xor a b = xor a c) : b = c := by
  cases a <;> cases b <;> cases c <;> simp at h ⊢

/-- Equality of first product rows exposes equality of the product head cells
    when both right operands have selected head cells. -/
theorem head_product_cell_eq_of_first_row_eq
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    ({ angle := amod4 (ca.angle + (b.angle - b.angle))
       face := xor ca.face b.face
       payload :=
         match ca.payload, b.payload with
         | some p, some q => some (multiplyFuel d p q)
         | some p, none   => some p
         | none,   some q => some q
         | none,   none   => none } : Cell UCNSObject) =
    ({ angle := amod4 (ca.angle + (c.angle - c.angle))
       face := xor ca.face c.face
       payload :=
         match ca.payload, c.payload with
         | some p, some q => some (multiplyFuel d p q)
         | some p, none   => some p
         | none,   some q => some q
         | none,   none   => none } : Cell UCNSObject) := by
  have hhead := congrArg List.head? hrow
  simpa [multiplyRow] using hhead

/-- Equality of first product rows also exposes equality of the remaining
    product-row tails. This deliberately keeps the original right-head base
    angles visible: tail angle inversion is exactly where later proof work must
    use normalized/canonical angle facts rather than pretending `amod4` is
    globally injective. -/
theorem tail_product_cells_map_eq_of_first_row_eq
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    List.map (fun (cb : Cell UCNSObject) =>
      Cell.mk
        (amod4 (ca.angle + (cb.angle - b.angle)))
        (xor ca.face cb.face)
        (match ca.payload, cb.payload with
          | some p, some q => some (multiplyFuel d p q)
          | some p, none   => some p
          | none,   some q => some q
          | none,   none   => none)) bs =
    List.map (fun (cc : Cell UCNSObject) =>
      Cell.mk
        (amod4 (ca.angle + (cc.angle - c.angle)))
        (xor ca.face cc.face)
        (match ca.payload, cc.payload with
          | some p, some r => some (multiplyFuel d p r)
          | some p, none   => some p
          | none,   some r => some r
          | none,   none   => none)) cs := by
  have htail := congrArg List.tail hrow
  simpa [multiplyRow] using htail

/-- Once the selected right-head angles have been identified, the first-row tail
    equality can be rewritten so both tails use the same base angle. This is the
    row-list induction handoff before the still-missing non-head angle inversion. -/
theorem tail_product_cells_eq_of_first_row_eq_head_angle_eq
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hangle : b.angle = c.angle)
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    List.map (fun (cb : Cell UCNSObject) =>
      Cell.mk
        (amod4 (ca.angle + (cb.angle - b.angle)))
        (xor ca.face cb.face)
        (match ca.payload, cb.payload with
          | some p, some q => some (multiplyFuel d p q)
          | some p, none   => some p
          | none,   some q => some q
          | none,   none   => none)) bs =
    List.map (fun (cc : Cell UCNSObject) =>
      Cell.mk
        (amod4 (ca.angle + (cc.angle - b.angle)))
        (xor ca.face cc.face)
        (match ca.payload, cc.payload with
          | some p, some r => some (multiplyFuel d p r)
          | some p, none   => some p
          | none,   some r => some r
          | none,   none   => none)) cs := by
  have htail := tail_product_cells_map_eq_of_first_row_eq d ca b c bs cs hrow
  rw [← hangle] at htail
  exact htail

/-- Successor-product equality exposes equality of the first product row tails,
    after the selected right-head product cell is removed. This is the
    product-level wrapper around `tail_product_cells_eq_of_first_row_eq`. -/
theorem tail_product_cells_map_eq_of_multiplyFuel_succ_eq
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    List.map (fun (cb : Cell UCNSObject) =>
      Cell.mk
        (amod4 (ca.angle + (cb.angle - b.angle)))
        (xor ca.face cb.face)
        (match ca.payload, cb.payload with
          | some p, some q => some (multiplyFuel d p q)
          | some p, none   => some p
          | none,   some q => some q
          | none,   none   => none)) bs =
    List.map (fun (cc : Cell UCNSObject) =>
      Cell.mk
        (amod4 (ca.angle + (cc.angle - c.angle)))
        (xor ca.face cc.face)
        (match ca.payload, cc.payload with
          | some p, some r => some (multiplyFuel d p r)
          | some p, none   => some p
          | none,   some r => some r
          | none,   none   => none)) cs := by
  have hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca :=
    first_row_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca rest (b :: bs) (c :: cs) h
  exact tail_product_cells_map_eq_of_first_row_eq d ca b c bs cs hrow

/-- Face-bit head inversion for the first row: once row equality has selected
    the head product cell, xor cancellation recovers equality of the right-head
    face bits. -/
theorem right_head_face_eq_of_first_row_eq
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    b.face = c.face := by
  have hcell := head_product_cell_eq_of_first_row_eq d ca b c bs cs hrow
  have hface : xor ca.face b.face = xor ca.face c.face := by
    exact congrArg Cell.face hcell
  exact bool_xor_left_cancel hface


/-- The payload relation exposed by a selected product-row head. If the selected
    left head is the payload unit, this is direct right-payload equality; if the
    selected left head carries payload `p`, this is equality of the transformed
    recursive payload expressions. -/
def rightHeadPayloadRelation (d : Nat)
    (ca b c : Cell UCNSObject) : Prop :=
  match ca.payload with
  | none => b.payload = c.payload
  | some p =>
      (match b.payload with
        | some q => some (multiplyFuel d p q)
        | none => some p) =
      (match c.payload with
        | some r => some (multiplyFuel d p r)
        | none => some p)

/-- Payload head inversion for the unit-left-payload row case: when the selected
    left head has no payload, the product head payload is exactly the selected
    right-head payload, so first-row equality recovers right-head payload
    equality. -/
theorem right_head_payload_eq_of_first_row_eq_left_payload_none
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hca : ca.payload = none)
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    b.payload = c.payload := by
  have hcell := head_product_cell_eq_of_first_row_eq d ca b c bs cs hrow
  have hpayload := congrArg Cell.payload hcell
  cases ca with
  | mk caAngle caFace caPayload =>
      cases caPayload with
      | none =>
          cases b with
          | mk bAngle bFace bPayload =>
              cases c with
              | mk cAngle cFace cPayload =>
                  cases bPayload <;> cases cPayload <;>
                    simp at hpayload ⊢ <;> assumption
      | some p =>
          simp at hca

/-- Payload-head bridge for the recursive-left-payload row case: when the
    selected left head has payload `some p`, first-row equality exposes equality
    of the transformed right-head payload expressions. Full right-payload
    cancellation is deliberately not claimed here; the `some/some` branch still
    needs the recursive cancellativity induction. -/
theorem right_head_product_payload_eq_of_first_row_eq_left_payload_some
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject)) (p : UCNSObject)
    (hca : ca.payload = some p)
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    (match b.payload with
      | some q => some (multiplyFuel d p q)
      | none => some p) =
    (match c.payload with
      | some r => some (multiplyFuel d p r)
      | none => some p) := by
  have hcell := head_product_cell_eq_of_first_row_eq d ca b c bs cs hrow
  have hpayload := congrArg Cell.payload hcell
  cases ca with
  | mk caAngle caFace caPayload =>
      cases caPayload with
      | none =>
          simp at hca
      | some p' =>
          cases hca
          cases b with
          | mk bAngle bFace bPayload =>
              cases c with
              | mk cAngle cFace cPayload =>
                  cases bPayload <;> cases cPayload <;>
                    simp at hpayload ⊢ <;> assumption


/-- Single-door payload inversion for first-row equality. This packages the
    `none` and `some p` left-head payload cases into the exact relation exposed
    by the product head, avoiding callers having to split immediately. -/
theorem right_head_payload_relation_of_first_row_eq
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    rightHeadPayloadRelation d ca b c := by
  cases hca : ca.payload with
  | none =>
      simpa [rightHeadPayloadRelation, hca] using
        right_head_payload_eq_of_first_row_eq_left_payload_none d ca b c bs cs hca hrow
  | some p =>
      simpa [rightHeadPayloadRelation, hca] using
        right_head_product_payload_eq_of_first_row_eq_left_payload_some d ca b c bs cs p hca hrow


/-- Equality of common-baseline mapped tail rows exposes equality of the
    selected non-head product cells. This is the non-head analogue of
    `head_product_cell_eq_of_first_row_eq`: the baseline is now supplied
    explicitly instead of read from the right-row head. -/
theorem head_product_cell_eq_of_commonBase_tail_eq
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    ({ angle := amod4 (ca.angle + (b.angle - β0))
       face := xor ca.face b.face
       payload :=
         match ca.payload, b.payload with
         | some p, some q => some (multiplyFuel d p q)
         | some p, none   => some p
         | none,   some q => some q
         | none,   none   => none } : Cell UCNSObject) =
    ({ angle := amod4 (ca.angle + (c.angle - β0))
       face := xor ca.face c.face
       payload :=
         match ca.payload, c.payload with
         | some p, some q => some (multiplyFuel d p q)
         | some p, none   => some p
         | none,   some q => some q
         | none,   none   => none } : Cell UCNSObject) := by
  have hhead := congrArg List.head? hrow
  simpa [multiplyRowWithBase] using hhead

/-- Non-head common-baseline angle inversion, in the strongest form available
    without an `amod4` injectivity/range lemma: the transformed angles are
    equal under the shared baseline. -/
theorem right_tail_head_transformed_angle_eq_of_commonBase_tail_eq
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    amod4 (ca.angle + (b.angle - β0)) =
      amod4 (ca.angle + (c.angle - β0)) := by
  exact congrArg Cell.angle
    (head_product_cell_eq_of_commonBase_tail_eq d β0 ca b c bs cs hrow)

/-- Raw non-head angle inversion from a common-baseline tail equality, provided
    the two transformed angles are already known to be fixed by `amod4`.

    This theorem isolates the exact remaining canonical-domain obligation:
    prove the two fixed-point hypotheses from the normalized/canonical angle
    range, and ordinary rational cancellation recovers the right-cell angle. -/
theorem right_tail_head_angle_eq_of_commonBase_tail_eq_of_amod4_fixed
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hb :
      amod4 (ca.angle + (b.angle - β0)) =
        ca.angle + (b.angle - β0))
    (hc :
      amod4 (ca.angle + (c.angle - β0)) =
        ca.angle + (c.angle - β0))
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    b.angle = c.angle := by
  have hraw :
      ca.angle + (b.angle - β0) =
        ca.angle + (c.angle - β0) := by
    simpa [hb, hc] using
      right_tail_head_transformed_angle_eq_of_commonBase_tail_eq d β0 ca b c bs cs hrow
  linarith

/-- Raw non-head angle inversion from a common-baseline tail equality, with the
    `amod4` fixed-point facts supplied as concrete floor-zero obligations. -/
theorem right_tail_head_angle_eq_of_commonBase_tail_eq_of_floor_div_four_eq_zero
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hb :
      ((ca.angle + (b.angle - β0)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c.angle - β0)) / (4 : Rat)).floor = 0)
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    b.angle = c.angle := by
  exact right_tail_head_angle_eq_of_commonBase_tail_eq_of_amod4_fixed
    d β0 ca b c bs cs
    (amod4_eq_self_of_floor_div_four_eq_zero (ca.angle + (b.angle - β0)) hb)
    (amod4_eq_self_of_floor_div_four_eq_zero (ca.angle + (c.angle - β0)) hc)
    hrow

/-- Non-head common-baseline face inversion: once both tail heads are measured
    against the same baseline, product-cell equality exposes the xor equation
    and xor cancellation recovers the right-cell face bit. -/
theorem right_tail_head_face_eq_of_commonBase_tail_eq
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    b.face = c.face := by
  have hcell := head_product_cell_eq_of_commonBase_tail_eq d β0 ca b c bs cs hrow
  have hface : xor ca.face b.face = xor ca.face c.face := by
    exact congrArg Cell.face hcell
  exact bool_xor_left_cancel hface

/-- Non-head common-baseline payload inversion. This is intentionally the same
    payload relation used for selected heads: a unit left payload gives direct
    right-payload equality, while a recursive left payload gives equality of
    the transformed recursive products to be consumed by induction. -/
theorem right_tail_head_payload_relation_of_commonBase_tail_eq
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    rightHeadPayloadRelation d ca b c := by
  have hcell := head_product_cell_eq_of_commonBase_tail_eq d β0 ca b c bs cs hrow
  have hpayload := congrArg Cell.payload hcell
  cases hca : ca.payload with
  | none =>
      cases ca with
      | mk caAngle caFace caPayload =>
          cases caPayload with
          | none =>
              cases b with
              | mk bAngle bFace bPayload =>
                  cases c with
                  | mk cAngle cFace cPayload =>
                      cases bPayload <;> cases cPayload <;>
                        simp [rightHeadPayloadRelation] at hpayload ⊢ <;> assumption
          | some p =>
              simp at hca
  | some p =>
      cases ca with
      | mk caAngle caFace caPayload =>
          cases caPayload with
          | none =>
              simp at hca
          | some p' =>
              cases hca
              cases b with
              | mk bAngle bFace bPayload =>
                  cases c with
                  | mk cAngle cFace cPayload =>
                      cases bPayload <;> cases cPayload <;>
                        simp [rightHeadPayloadRelation] at hpayload ⊢ <;> assumption




/-- Successor-product head-face inversion: product equality exposes first-row
    equality, and first-row equality recovers equality of selected right-head
    face bits. -/
theorem right_head_face_eq_of_multiplyFuel_succ_eq
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    b.face = c.face := by
  have hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca :=
    first_row_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca rest (b :: bs) (c :: cs) h
  exact right_head_face_eq_of_first_row_eq d ca b c bs cs hrow

/-- Successor-product head-payload inversion in the unit-left-payload case:
    when the selected left head has no payload, product equality recovers
    equality of selected right-head payloads. -/
theorem right_head_payload_eq_of_multiplyFuel_succ_eq_left_payload_none
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hca : ca.payload = none)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    b.payload = c.payload := by
  have hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca :=
    first_row_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca rest (b :: bs) (c :: cs) h
  exact right_head_payload_eq_of_first_row_eq_left_payload_none d ca b c bs cs hca hrow

/-- Successor-product payload bridge in the recursive-left-payload case. This
    lifts the row-level transformed-payload equality to the unfolded
    `multiplyFuel (d + 1)` product. -/
theorem right_head_product_payload_eq_of_multiplyFuel_succ_eq_left_payload_some
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p : UCNSObject)
    (hca : ca.payload = some p)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    (match b.payload with
      | some q => some (multiplyFuel d p q)
      | none => some p) =
    (match c.payload with
      | some r => some (multiplyFuel d p r)
      | none => some p) := by
  have hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca :=
    first_row_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca rest (b :: bs) (c :: cs) h
  exact right_head_product_payload_eq_of_first_row_eq_left_payload_some d ca b c bs cs p hca hrow


/-- Single-door payload inversion for successor-product equality. This exposes
    the payload relation determined by the selected left head without requiring
    callers to choose the `none` or `some p` branch up front. -/
theorem right_head_payload_relation_of_multiplyFuel_succ_eq
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    rightHeadPayloadRelation d ca b c := by
  have hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca :=
    first_row_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca rest (b :: bs) (c :: cs) h
  exact right_head_payload_relation_of_first_row_eq d ca b c bs cs hrow


/-- In the recursive-left/recursive-right payload branch, the single-door payload
    relation opens to exactly the recursive product equality needed by the
    cancellativity induction. -/
theorem recursive_payload_eq_of_rightHeadPayloadRelation_some_some
    (d : Nat) (ca b c : Cell UCNSObject) (p q r : UCNSObject)
    (hca : ca.payload = some p)
    (hb : b.payload = some q)
    (hc : c.payload = some r)
    (hrel : rightHeadPayloadRelation d ca b c) :
    multiplyFuel d p q = multiplyFuel d p r := by
  simpa [rightHeadPayloadRelation, hca, hb, hc] using hrel

/-- First-row equality, with selected recursive payloads on all three head
    cells, exposes the recursive product equality for those payloads. -/
theorem recursive_payload_eq_of_first_row_eq_some_some
    (d : Nat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (hca : ca.payload = some p)
    (hb : b.payload = some q)
    (hc : c.payload = some r)
    (hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca) :
    multiplyFuel d p q = multiplyFuel d p r := by
  exact recursive_payload_eq_of_rightHeadPayloadRelation_some_some d ca b c p q r
    hca hb hc (right_head_payload_relation_of_first_row_eq d ca b c bs cs hrow)

/-- Successor-product equality, with selected recursive payloads on all three
    head cells, exposes the recursive product equality for those payloads. This
    is the direct induction handoff for the `some/some` payload branch. -/
theorem recursive_payload_eq_of_multiplyFuel_succ_eq_some_some
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (hca : ca.payload = some p)
    (hb : b.payload = some q)
    (hc : c.payload = some r)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    multiplyFuel d p q = multiplyFuel d p r := by
  exact recursive_payload_eq_of_rightHeadPayloadRelation_some_some d ca b c p q r
    hca hb hc
    (right_head_payload_relation_of_multiplyFuel_succ_eq d nda ndb ndc ca b c rest bs cs h)

/-- Common-baseline tail equality, with recursive payloads on the selected left
    cell and both selected tail-head cells, exposes the recursive product
    equality needed by the cancellativity induction. -/
theorem recursive_tail_payload_eq_of_commonBase_tail_eq_some_some
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (hca : ca.payload = some p)
    (hb : b.payload = some q)
    (hc : c.payload = some r)
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    multiplyFuel d p q = multiplyFuel d p r := by
  exact recursive_payload_eq_of_rightHeadPayloadRelation_some_some d ca b c p q r
    hca hb hc
    (right_tail_head_payload_relation_of_commonBase_tail_eq d β0 ca b c bs cs hrow)

/-- A small bundling lemma for later row-content inversion steps: cell equality
    follows from equality of the three observable fields. -/
theorem cell_eq_of_fields_eq
    {b c : Cell UCNSObject}
    (hangle : b.angle = c.angle)
    (hface : b.face = c.face)
    (hpayload : b.payload = c.payload) :
    b = c := by
  cases b
  cases c
  cases hangle
  cases hface
  cases hpayload
  rfl

/-- An object is normalized (at the host level) when its first angle
    is zero — the property (N1) used by the Carrier-LCM Law proof. -/
def HostNormalized (x : UCNSObject) : Prop :=
  ∀ c, x.cells.head? = some c → c.angle = 0

/-! Ratified Step-1 cancellativity domain (`AlignedComplete`).
    Erin ratified the domain on 2026-06-21; see
    `formal/cancellativity-step1-findings.md` for the counterexample search
    that motivates each conjunct. The recursive predicates mirror the `depth`
    mutual-recursion pattern above.
    NOTE: not machine-checked in the authoring environment (no Lean toolchain);
    compile + the proof discharge remain Step-2 work. `sorry` ⇒ no DEFENDED status. -/

/- Recursive nonemptiness: no empty cell-list at any level
    (rules out the empty-left-operand and empty-atom counterexamples). -/
mutual
  def NonemptyRec : UCNSObject → Prop
    | mk _ cs => cs ≠ [] ∧ NonemptyRecCells cs
  def NonemptyRecCells : List (Cell UCNSObject) → Prop
    | [] => True
    | c :: rest => NonemptyRecCell c ∧ NonemptyRecCells rest
  def NonemptyRecCell : Cell UCNSObject → Prop
    | ⟨_, _, none⟩ => True
    | ⟨_, _, some p⟩ => NonemptyRec p
end

/- Recursive host-normalization: head angle 0 for the object AND every payload
    (the head-only `HostNormalized` above is too weak — payload β0 collapses). -/
mutual
  def HostNormalizedRec : UCNSObject → Prop
    | mk _ cs => (∀ c, cs.head? = some c → c.angle = 0) ∧ HostNormalizedRecCells cs
  def HostNormalizedRecCells : List (Cell UCNSObject) → Prop
    | [] => True
    | c :: rest => HostNormalizedRecCell c ∧ HostNormalizedRecCells rest
  def HostNormalizedRecCell : Cell UCNSObject → Prop
    | ⟨_, _, none⟩ => True
    | ⟨_, _, some p⟩ => HostNormalizedRec p
end

/- Canonical carrier: `nDec = nMin cells` at every level
    (`Nat.lcm` is not left-cancellative, so a free `nDec` breaks it). -/
mutual
  def CanonicalCarrier : UCNSObject → Prop
    | mk d cs => d = (angleDenoms cs).foldl Nat.lcm 1 ∧ CanonicalCarrierCells cs
  def CanonicalCarrierCells : List (Cell UCNSObject) → Prop
    | [] => True
    | c :: rest => CanonicalCarrierCell c ∧ CanonicalCarrierCells rest
  def CanonicalCarrierCell : Cell UCNSObject → Prop
    | ⟨_, _, none⟩ => True
    | ⟨_, _, some p⟩ => CanonicalCarrier p
end

/- Per-object uniform depth: all cells share one `depthCell`, recursively
    (a complete tree with no early atom). -/
mutual
  def UniformDepth : UCNSObject → Prop
    | mk _ cs => (∀ c ∈ cs, ∀ c' ∈ cs, depthCell c = depthCell c') ∧ UniformDepthCells cs
  def UniformDepthCells : List (Cell UCNSObject) → Prop
    | [] => True
    | c :: rest => UniformDepthCell c ∧ UniformDepthCells rest
  def UniformDepthCell : Cell UCNSObject → Prop
    | ⟨_, _, none⟩ => True
    | ⟨_, _, some p⟩ => UniformDepth p
end

/-- Per-object completeness (nonempty + recursive host-normalized + uniform
    depth + canonical carrier). Cross-operand common depth is added at the
    theorem (`AlignedComplete` = `Complete A,B,C` + `depth A = depth B = depth C`). -/
def Complete (x : UCNSObject) : Prop :=
  NonemptyRec x ∧ HostNormalizedRec x ∧ UniformDepth x ∧ CanonicalCarrier x


/-- If every cell in a list has zero payload depth, then the list-level maximum
    payload depth is zero. -/
theorem depthCells_eq_zero_of_forall_depthCell_zero
    (cs : List (Cell UCNSObject))
    (h : ∀ c ∈ cs, depthCell c = 0) :
    depthCells cs = 0 := by
  induction cs with
  | nil =>
      rfl
  | cons c rest ih =>
      simp [depthCells, h c (by simp), ih (by
        intro c' hc'
        exact h c' (by simp [hc']))]

/-- In a uniform-depth object whose selected head has no payload, every top-level
    cell has payload depth zero, so the object itself has depth one. -/
theorem depth_eq_one_of_uniformDepth_mk_cons_head_payload_none
    (nd : Nat) (c : Cell UCNSObject) (cs : List (Cell UCNSObject))
    (hu : UniformDepth (UCNSObject.mk nd (c :: cs)))
    (hc : c.payload = none) :
    depth (UCNSObject.mk nd (c :: cs)) = 1 := by
  have huObj :
      (∀ c' ∈ c :: cs, ∀ c'' ∈ c :: cs, depthCell c' = depthCell c'') ∧
        UniformDepthCells (c :: cs) := by
    simpa [UniformDepth] using hu
  have hzero : ∀ c' ∈ c :: cs, depthCell c' = 0 := by
    intro c' hc'
    have hsame := huObj.1 c' hc' c (by simp)
    rw [hsame]
    cases c with
    | mk angle face payload =>
        cases payload <;> simp [depthCell] at hc ⊢
  simp [depth, depthCells_eq_zero_of_forall_depthCell_zero (c :: cs) hzero]

/-- A complete non-flat object cannot have a payload-unit selected head: under
    uniform depth, a head payload of `none` would force object depth one. -/
theorem exists_head_payload_of_complete_mk_cons_depth_gt_one
    (nd : Nat) (c : Cell UCNSObject) (cs : List (Cell UCNSObject))
    (h : Complete (UCNSObject.mk nd (c :: cs)))
    (hd : 1 < depth (UCNSObject.mk nd (c :: cs))) :
    ∃ p, c.payload = some p := by
  cases hc : c.payload with
  | none =>
      have hdepth := depth_eq_one_of_uniformDepth_mk_cons_head_payload_none nd c cs h.2.2.1 hc
      rw [hdepth] at hd
      exact False.elim (by exact Nat.lt_irrefl 1 hd)
  | some p =>
      exact ⟨p, rfl⟩


/-- If every cell in a nonempty list has the same payload depth `n`, the
    list-level maximum is exactly `n`. -/
theorem depthCells_eq_of_forall_depthCell_eq
    (xs : List (Cell UCNSObject)) (n : Nat)
    (hne : xs ≠ [])
    (h : ∀ c ∈ xs, depthCell c = n) :
    depthCells xs = n := by
  induction xs with
  | nil =>
      exact False.elim (hne rfl)
  | cons c rest ih =>
      cases rest with
      | nil =>
          simp [depthCells, h c (by simp)]
      | cons c' rest' =>
          have hrest_ne : c' :: rest' ≠ [] := by simp
          have hrest : ∀ x ∈ c' :: rest', depthCell x = n := by
            intro x hx
            exact h x (by simp [hx])
          have ihrest := ih hrest_ne hrest
          simp [depthCells, h c (by simp), ihrest]

/-- If every top-level cell in a nonempty list has the same payload depth as the
    selected head, the list-level maximum is that selected depth. -/
theorem depthCells_eq_head_of_forall_depthCell_eq_head
    (c : Cell UCNSObject) (cs : List (Cell UCNSObject))
    (h : ∀ c' ∈ c :: cs, depthCell c' = depthCell c) :
    depthCells (c :: cs) = depthCell c :=
  depthCells_eq_of_forall_depthCell_eq (c :: cs) (depthCell c) (by simp) h

/-- In a uniform-depth object, a selected recursive head payload determines the
    enclosing object depth exactly: object depth is one plus that payload depth. -/
theorem depth_eq_succ_depth_payload_of_uniformDepth_mk_cons_head_payload_some
    (nd : Nat) (c : Cell UCNSObject) (cs : List (Cell UCNSObject))
    (p : UCNSObject)
    (hu : UniformDepth (UCNSObject.mk nd (c :: cs)))
    (hc : c.payload = some p) :
    depth (UCNSObject.mk nd (c :: cs)) = depth p + 1 := by
  have huObj :
      (∀ c' ∈ c :: cs, ∀ c'' ∈ c :: cs, depthCell c' = depthCell c'') ∧
        UniformDepthCells (c :: cs) := by
    simpa [UniformDepth] using hu
  have hall : ∀ c' ∈ c :: cs, depthCell c' = depthCell c := by
    intro c' hc'
    exact huObj.1 c' hc' c (by simp)
  have hcells := depthCells_eq_head_of_forall_depthCell_eq_head c cs hall
  cases c with
  | mk angle face payload =>
      cases payload with
      | none =>
          simp at hc
      | some p' =>
          cases hc
          simp [depth, depthCell, hcells, Nat.add_comm]

/-- Completeness descends through a selected recursive head payload. -/
theorem complete_payload_of_complete_mk_cons_head_payload_some
    (nd : Nat) (c : Cell UCNSObject) (cs : List (Cell UCNSObject))
    (p : UCNSObject)
    (h : Complete (UCNSObject.mk nd (c :: cs)))
    (hc : c.payload = some p) :
    Complete p := by
  have hnObj : (c :: cs) ≠ [] ∧ NonemptyRecCells (c :: cs) := by
    simpa [NonemptyRec] using h.1
  have hhObj :
      (∀ c', (c :: cs).head? = some c' → c'.angle = 0) ∧
        HostNormalizedRecCells (c :: cs) := by
    simpa [HostNormalizedRec] using h.2.1
  have huObj :
      (∀ c' ∈ c :: cs, ∀ c'' ∈ c :: cs, depthCell c' = depthCell c'') ∧
        UniformDepthCells (c :: cs) := by
    simpa [UniformDepth] using h.2.2.1
  have hcObj :
      nd = (angleDenoms (c :: cs)).foldl Nat.lcm 1 ∧
        CanonicalCarrierCells (c :: cs) := by
    simpa [CanonicalCarrier] using h.2.2.2
  have hnCellsCons : NonemptyRecCell c ∧ NonemptyRecCells cs := by
    simpa [NonemptyRecCells] using hnObj.2
  have hhCellsCons : HostNormalizedRecCell c ∧ HostNormalizedRecCells cs := by
    simpa [HostNormalizedRecCells] using hhObj.2
  have huCellsCons : UniformDepthCell c ∧ UniformDepthCells cs := by
    simpa [UniformDepthCells] using huObj.2
  have hcCellsCons : CanonicalCarrierCell c ∧ CanonicalCarrierCells cs := by
    simpa [CanonicalCarrierCells] using hcObj.2
  have hncell : NonemptyRecCell c := hnCellsCons.1
  have hhcell : HostNormalizedRecCell c := hhCellsCons.1
  have hucell : UniformDepthCell c := huCellsCons.1
  have hccell : CanonicalCarrierCell c := hcCellsCons.1
  cases c with
  | mk angle face payload =>
      cases payload with
      | none =>
          simp at hc
      | some p' =>
          cases hc
          exact
            ⟨by simpa [NonemptyRecCell] using hncell,
              by simpa [HostNormalizedRecCell] using hhcell,
              by simpa [UniformDepthCell] using hucell,
              by simpa [CanonicalCarrierCell] using hccell⟩

/-- Ratified cancellativity domain: each operand is `Complete`, all three
    operands share one depth, and the right-hand operands fit inside the
    available multiplication fuel. -/
def AlignedComplete (A B C : UCNSObject) (d : Nat) : Prop :=
  Complete A ∧ Complete B ∧ Complete C ∧
    depth A = depth B ∧ depth B = depth C ∧ depth B ≤ d ∧ depth C ≤ d

/-! A concrete guardrail for the current cancellativity frontier.

    `AlignedComplete` does not currently constrain non-head host angles to a
    chosen representative interval. Consequently, tail angles that differ by a
    multiple of four collapse under `amod4`, while the right operands remain
    syntactically different. This is the exact missing domain piton behind the
    later floor-zero witness obligations. -/

abbrev cancellativityCounterLeft : UCNSObject :=
  UCNSObject.mk 1 [{ angle := 0, face := false, payload := none }]

abbrev cancellativityCounterRightB : UCNSObject :=
  UCNSObject.mk 1
    [{ angle := 0, face := false, payload := none },
      { angle := 4, face := false, payload := none }]

abbrev cancellativityCounterRightC : UCNSObject :=
  UCNSObject.mk 1
    [{ angle := 0, face := false, payload := none },
      { angle := 0, face := false, payload := none }]

theorem alignedComplete_cancellativityCounter :
    AlignedComplete cancellativityCounterLeft cancellativityCounterRightB
      cancellativityCounterRightC 1 := by
  have hAden :
      angleDenoms [{ angle := (0 : Rat), face := false, payload := none }] = [] := by
    native_decide
  have hBden :
      angleDenoms
        [{ angle := (0 : Rat), face := false, payload := none },
          { angle := 4, face := false, payload := none }] = [] := by
    native_decide
  have hCden :
      angleDenoms
        [{ angle := (0 : Rat), face := false, payload := none },
          { angle := 0, face := false, payload := none }] = [] := by
    native_decide
  simp [AlignedComplete, Complete, cancellativityCounterLeft,
    cancellativityCounterRightB, cancellativityCounterRightC, NonemptyRec,
    NonemptyRecCells, NonemptyRecCell, HostNormalizedRec,
    HostNormalizedRecCells, HostNormalizedRecCell, UniformDepth,
    UniformDepthCells, UniformDepthCell, CanonicalCarrier,
    CanonicalCarrierCells, CanonicalCarrierCell, depth, depthCells,
    depthCell, hAden, hBden, hCden]

theorem multiplyFuel_cancellativityCounter_eq :
    multiplyFuel 1 cancellativityCounterLeft cancellativityCounterRightB =
      multiplyFuel 1 cancellativityCounterLeft cancellativityCounterRightC := by
  rfl

theorem cancellativityCounter_right_ne :
    cancellativityCounterRightB ≠ cancellativityCounterRightC := by
  intro h
  injection h with _ hc
  simp [cancellativityCounterRightB, cancellativityCounterRightC] at hc

theorem not_multiply_left_cancellative_on_alignedComplete :
    ¬ (∀ A B C d,
      AlignedComplete A B C d →
      multiplyFuel d A B = multiplyFuel d A C →
      B = C) := by
  intro hcancel
  exact cancellativityCounter_right_ne
    (hcancel cancellativityCounterLeft cancellativityCounterRightB
      cancellativityCounterRightC 1 alignedComplete_cancellativityCounter
      multiplyFuel_cancellativityCounter_eq)

theorem complete_left_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    Complete A := h.1

theorem complete_right_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    Complete B := h.2.1

theorem complete_cancel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    Complete C := h.2.2.1

/-- `AlignedComplete` wrapper for the first-row tail equality. The domain
    hypothesis is not needed for the raw list fact, but carrying it here keeps
    later cancellativity code on the same canonical/normalized proof path as
    the head-inversion lemmas. -/
theorem tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (_hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    multiplyRowWithBase d b.angle bs ca =
      multiplyRowWithBase d c.angle cs ca := by
  exact tail_product_cells_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca b c rest bs cs h


/-- A complete object with a selected head cell has normalized head angle. -/
theorem head_angle_eq_zero_of_complete_mk_cons
    (nd : Nat) (c : Cell UCNSObject) (cs : List (Cell UCNSObject))
    (h : Complete (UCNSObject.mk nd (c :: cs))) :
    c.angle = 0 := by
  have hnorm : HostNormalizedRec (UCNSObject.mk nd (c :: cs)) := h.2.1
  unfold HostNormalizedRec at hnorm
  exact hnorm.1 c rfl

/-- Head-angle equality for selected right heads follows from completeness alone:
    both right operands are recursively host-normalized, so both selected head
    angles are zero. -/
theorem right_head_angle_eq_of_complete_heads
    (ndb ndc : Nat) (b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hB : Complete (UCNSObject.mk ndb (b :: bs)))
    (hC : Complete (UCNSObject.mk ndc (c :: cs))) :
    b.angle = c.angle := by
  exact (head_angle_eq_zero_of_complete_mk_cons ndb b bs hB).trans
    (head_angle_eq_zero_of_complete_mk_cons ndc c cs hC).symm

/-- Under `AlignedComplete`, selected right-head angles are equal. This is the
    angle component needed by the row-content inversion bundle; unlike face and
    payload, it comes from the normalized-domain hypothesis rather than from xor
    or recursive payload cancellation. -/
theorem right_head_angle_eq_of_alignedComplete_heads
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) d) :
    b.angle = c.angle := by
  exact right_head_angle_eq_of_complete_heads ndb ndc b c bs cs
    (complete_right_of_alignedComplete hABC)
    (complete_cancel_of_alignedComplete hABC)

/-- Under `AlignedComplete`, the first-row tail equality can be normalized to a
    common selected-right-head baseline. This combines successor product
    equality with the unified normalized-domain head-angle inversion path. -/
theorem tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    multiplyRowWithBase d b.angle bs ca =
      multiplyRowWithBase d b.angle cs ca := by
  exact tail_product_cells_eq_of_multiplyFuel_succ_eq_commonBase
    d nda ndb ndc ca b c rest bs cs
    (right_head_angle_eq_of_alignedComplete_heads (d + 1) nda ndb ndc ca b c rest bs cs hABC)
    h

/-- `AlignedComplete` successor-product inversion for the first non-head
    tail cell's transformed angle. This is deliberately the modulo-normalized
    equality exposed by the current model; recovering raw `b₁.angle = c₁.angle`
    still requires the separate `amod4` injectivity/range fact. -/
theorem right_tail_head_transformed_angle_eq_of_multiplyFuel_succ_eq_alignedComplete
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    amod4 (ca.angle + (b₁.angle - b.angle)) =
      amod4 (ca.angle + (c₁.angle - b.angle)) := by
  exact right_tail_head_transformed_angle_eq_of_commonBase_tail_eq d b.angle ca b₁ c₁ bs cs
    (tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
      d nda ndb ndc ca b c rest (b₁ :: bs) (c₁ :: cs) hABC h)

/-- `AlignedComplete` successor-product raw angle inversion for the first
    non-head tail cell, parameterized by the canonical-domain facts that the two
    transformed angles are already fixed by `amod4`. -/
theorem right_tail_head_angle_eq_of_multiplyFuel_succ_eq_alignedComplete_of_amod4_fixed
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (hb :
      amod4 (ca.angle + (b₁.angle - b.angle)) =
        ca.angle + (b₁.angle - b.angle))
    (hc :
      amod4 (ca.angle + (c₁.angle - b.angle)) =
        ca.angle + (c₁.angle - b.angle))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    b₁.angle = c₁.angle := by
  exact right_tail_head_angle_eq_of_commonBase_tail_eq_of_amod4_fixed
    d b.angle ca b₁ c₁ bs cs hb hc
    (tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
      d nda ndb ndc ca b c rest (b₁ :: bs) (c₁ :: cs) hABC h)

/-- `AlignedComplete` successor-product raw angle inversion for the first
    non-head tail cell, with canonical-domain fixed-point obligations supplied
    as concrete floor-zero facts. -/
theorem right_tail_head_angle_eq_of_multiplyFuel_succ_eq_alignedComplete_of_floor_div_four_eq_zero
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (hb :
      ((ca.angle + (b₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    b₁.angle = c₁.angle := by
  exact right_tail_head_angle_eq_of_multiplyFuel_succ_eq_alignedComplete_of_amod4_fixed
    d nda ndb ndc ca b c b₁ c₁ rest bs cs hABC
    (amod4_eq_self_of_floor_div_four_eq_zero (ca.angle + (b₁.angle - b.angle)) hb)
    (amod4_eq_self_of_floor_div_four_eq_zero (ca.angle + (c₁.angle - b.angle)) hc)
    h

/-- `AlignedComplete` successor-product inversion for the first non-head tail
    cell's face bit. -/
theorem right_tail_head_face_eq_of_multiplyFuel_succ_eq_alignedComplete
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    b₁.face = c₁.face := by
  exact right_tail_head_face_eq_of_commonBase_tail_eq d b.angle ca b₁ c₁ bs cs
    (tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
      d nda ndb ndc ca b c rest (b₁ :: bs) (c₁ :: cs) hABC h)

/-- `AlignedComplete` successor-product inversion for the first non-head tail
    cell's payload relation. -/
theorem right_tail_head_payload_relation_of_multiplyFuel_succ_eq_alignedComplete
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    rightHeadPayloadRelation d ca b₁ c₁ := by
  exact right_tail_head_payload_relation_of_commonBase_tail_eq d b.angle ca b₁ c₁ bs cs
    (tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
      d nda ndb ndc ca b c rest (b₁ :: bs) (c₁ :: cs) hABC h)

/-- `AlignedComplete` successor-product recursive-payload handoff for the
    first non-head tail cell. This is the tail analogue of
    `recursive_payload_eq_of_multiplyFuel_succ_eq_some_some`. -/
theorem recursive_tail_payload_eq_of_multiplyFuel_succ_eq_alignedComplete_some_some
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (hca : ca.payload = some p)
    (hb : b₁.payload = some q)
    (hc : c₁.payload = some r)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    multiplyFuel d p q = multiplyFuel d p r := by
  exact recursive_payload_eq_of_rightHeadPayloadRelation_some_some d ca b₁ c₁ p q r
    hca hb hc
    (right_tail_head_payload_relation_of_multiplyFuel_succ_eq_alignedComplete
      d nda ndb ndc ca b c b₁ c₁ rest bs cs hABC h)

/-- First non-head tail-cell equality in the recursive-left-payload case, once
    the recursive induction has identified the two right payload witnesses. -/
theorem right_tail_head_cell_eq_of_multiplyFuel_succ_eq_alignedComplete_left_payload_some_of_floor_div_four_eq_zero_of_payload_eq
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (_hca : ca.payload = some p)
    (hbPayload : b₁.payload = some q)
    (hcPayload : c₁.payload = some r)
    (hqr : q = r)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (hb :
      ((ca.angle + (b₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    b₁ = c₁ := by
  have hangle :=
    right_tail_head_angle_eq_of_multiplyFuel_succ_eq_alignedComplete_of_floor_div_four_eq_zero
      d nda ndb ndc ca b c b₁ c₁ rest bs cs hABC hb hc h
  have hface :=
    right_tail_head_face_eq_of_multiplyFuel_succ_eq_alignedComplete
      d nda ndb ndc ca b c b₁ c₁ rest bs cs hABC h
  have hpayload : b₁.payload = c₁.payload := by
    rw [hbPayload, hcPayload, hqr]
  exact cell_eq_of_fields_eq hangle hface hpayload


/-- The shared payload relation collapses to direct right-payload equality when
    the selected left cell is the payload unit. -/
theorem right_payload_eq_of_rightHeadPayloadRelation_left_payload_none
    (d : Nat) (ca b c : Cell UCNSObject)
    (hca : ca.payload = none)
    (hrel : rightHeadPayloadRelation d ca b c) :
    b.payload = c.payload := by
  simpa [rightHeadPayloadRelation, hca] using hrel


/-- Common-baseline first-tail-cell equality in the unit-left-payload branch. -/
theorem right_tail_head_cell_eq_of_commonBase_tail_eq_left_payload_none_of_floor_div_four_eq_zero
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hca : ca.payload = none)
    (hb :
      ((ca.angle + (b.angle - β0)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c.angle - β0)) / (4 : Rat)).floor = 0)
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    b = c := by
  have hangle :=
    right_tail_head_angle_eq_of_commonBase_tail_eq_of_floor_div_four_eq_zero
      d β0 ca b c bs cs hb hc hrow
  have hface :=
    right_tail_head_face_eq_of_commonBase_tail_eq d β0 ca b c bs cs hrow
  have hpayload :=
    right_payload_eq_of_rightHeadPayloadRelation_left_payload_none d ca b c hca
      (right_tail_head_payload_relation_of_commonBase_tail_eq d β0 ca b c bs cs hrow)
  exact cell_eq_of_fields_eq hangle hface hpayload

/-- One common-baseline list-induction step for the unit-left-payload branch:
    invert the current tail head and preserve equality of the remaining mapped
    tails. This is the reusable cons-step for proving equality of full right
    tails. -/
theorem right_tail_head_cell_eq_and_tail_product_cells_eq_of_commonBase_tail_eq_left_payload_none_of_floor_div_four_eq_zero
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hca : ca.payload = none)
    (hb :
      ((ca.angle + (b.angle - β0)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c.angle - β0)) / (4 : Rat)).floor = 0)
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    b = c ∧ multiplyRowWithBase d β0 bs ca =
      multiplyRowWithBase d β0 cs ca := by
  have hcell :=
    right_tail_head_cell_eq_of_commonBase_tail_eq_left_payload_none_of_floor_div_four_eq_zero
      d β0 ca b c bs cs hca hb hc hrow
  have htail : multiplyRowWithBase d β0 bs ca =
      multiplyRowWithBase d β0 cs ca := by
    have htailRaw := congrArg List.tail hrow
    simpa [multiplyRowWithBase] using htailRaw
  exact ⟨hcell, htail⟩

/-- Common-baseline first-tail-cell equality in the recursive-left-payload
    branch, once recursive induction has identified the two right payload
    witnesses. -/
theorem right_tail_head_cell_eq_of_commonBase_tail_eq_left_payload_some_of_floor_div_four_eq_zero_of_payload_eq
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (_hca : ca.payload = some p)
    (hbPayload : b.payload = some q)
    (hcPayload : c.payload = some r)
    (hqr : q = r)
    (hb :
      ((ca.angle + (b.angle - β0)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c.angle - β0)) / (4 : Rat)).floor = 0)
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    b = c := by
  have hangle :=
    right_tail_head_angle_eq_of_commonBase_tail_eq_of_floor_div_four_eq_zero
      d β0 ca b c bs cs hb hc hrow
  have hface :=
    right_tail_head_face_eq_of_commonBase_tail_eq d β0 ca b c bs cs hrow
  have hpayload : b.payload = c.payload := by
    rw [hbPayload, hcPayload, hqr]
  exact cell_eq_of_fields_eq hangle hface hpayload

/-- One common-baseline list-induction step for the recursive-left-payload
    branch: consume one tail cell after recursive induction has identified the
    payload witnesses, and keep equality of the remaining mapped tails. -/
theorem right_tail_head_cell_eq_and_tail_product_cells_eq_of_commonBase_tail_eq_left_payload_some_of_floor_div_four_eq_zero_of_payload_eq
    (d : Nat) (β0 : Rat) (ca b c : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (hca : ca.payload = some p)
    (hbPayload : b.payload = some q)
    (hcPayload : c.payload = some r)
    (hqr : q = r)
    (hb :
      ((ca.angle + (b.angle - β0)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c.angle - β0)) / (4 : Rat)).floor = 0)
    (hrow : multiplyRowWithBase d β0 (b :: bs) ca =
      multiplyRowWithBase d β0 (c :: cs) ca) :
    b = c ∧ multiplyRowWithBase d β0 bs ca =
      multiplyRowWithBase d β0 cs ca := by
  have hcell :=
    right_tail_head_cell_eq_of_commonBase_tail_eq_left_payload_some_of_floor_div_four_eq_zero_of_payload_eq
      d β0 ca b c bs cs p q r hca hbPayload hcPayload hqr hb hc hrow
  have htail : multiplyRowWithBase d β0 bs ca =
      multiplyRowWithBase d β0 cs ca := by
    have htailRaw := congrArg List.tail hrow
    simpa [multiplyRowWithBase] using htailRaw
  exact ⟨hcell, htail⟩

/-- One `AlignedComplete` successor-product list-induction step for the
    unit-left-payload branch: invert the first non-head right-tail cell and
    preserve common-baseline equality of the remaining mapped tails. -/
theorem right_tail_head_cell_eq_and_tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_left_payload_none_of_floor_div_four_eq_zero
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (hca : ca.payload = none)
    (hb :
      ((ca.angle + (b₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    b₁ = c₁ ∧ multiplyRowWithBase d b.angle bs ca =
      multiplyRowWithBase d b.angle cs ca := by
  exact
    right_tail_head_cell_eq_and_tail_product_cells_eq_of_commonBase_tail_eq_left_payload_none_of_floor_div_four_eq_zero
      d b.angle ca b₁ c₁ bs cs hca hb hc
      (tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
        d nda ndb ndc ca b c rest (b₁ :: bs) (c₁ :: cs) hABC h)

/-- Paired floor-zero evidence for a common-baseline right-tail walk. The
    proposition is intentionally list-shaped rather than membership-shaped:
    cancellativity consumes the two right tails in lockstep. -/
def commonBaseTailFloorZeros (ca : Cell UCNSObject) (β0 : Rat) :
    List (Cell UCNSObject) → List (Cell UCNSObject) → Prop
  | [], [] => True
  | b :: bs, c :: cs =>
      ((ca.angle + (b.angle - β0)) / (4 : Rat)).floor = 0 ∧
      ((ca.angle + (c.angle - β0)) / (4 : Rat)).floor = 0 ∧
      commonBaseTailFloorZeros ca β0 bs cs
  | _, _ => False

/-- Full common-baseline right-tail list equality in the unit-left-payload
    branch. This is the iterated form of the unit-left cons-step: each paired
    tail cell supplies its floor-zero evidence, the current cells are inverted,
    and the mapped-tail equality is threaded to the recursive call. -/
theorem right_tail_cells_eq_of_commonBase_tail_eq_left_payload_none_of_floorZeros
    (d : Nat) (β0 : Rat) (ca : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject))
    (hca : ca.payload = none)
    (hfloors : commonBaseTailFloorZeros ca β0 bs cs)
    (hrow : multiplyRowWithBase d β0 bs ca =
      multiplyRowWithBase d β0 cs ca) :
    bs = cs := by
  induction bs generalizing cs with
  | nil =>
      cases cs with
      | nil => rfl
      | cons c cs =>
          simp [commonBaseTailFloorZeros] at hfloors
  | cons b bs ih =>
      cases cs with
      | nil =>
          simp [commonBaseTailFloorZeros] at hfloors
      | cons c cs =>
          rcases hfloors with ⟨hb, hc, hrest⟩
          have hstep :=
            right_tail_head_cell_eq_and_tail_product_cells_eq_of_commonBase_tail_eq_left_payload_none_of_floor_div_four_eq_zero
              d β0 ca b c bs cs hca hb hc hrow
          have htailEq := ih cs hrest hstep.2
          rw [hstep.1, htailEq]

/-- Full `AlignedComplete` successor-product right-tail list equality in the
    unit-left-payload branch, after peeling the selected right head. -/
theorem right_tail_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_left_payload_none_of_floorZeros
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hca : ca.payload = none)
    (hfloors : commonBaseTailFloorZeros ca b.angle bs cs)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    bs = cs := by
  exact right_tail_cells_eq_of_commonBase_tail_eq_left_payload_none_of_floorZeros
    d b.angle ca bs cs hca hfloors
    (tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
      d nda ndb ndc ca b c rest bs cs hABC h)

/-- Paired evidence for a recursive-left common-baseline right-tail walk. Each
    paired tail cell supplies floor-zero facts plus concrete payload witnesses
    already identified by the recursive cancellativity induction. -/
def commonBaseTailRecursivePayloadEqWitnesses
    (ca : Cell UCNSObject) (β0 : Rat) :
    List (Cell UCNSObject) → List (Cell UCNSObject) → Prop
  | [], [] => True
  | b :: bs, c :: cs =>
      (∃ q r,
        b.payload = some q ∧
        c.payload = some r ∧
        q = r ∧
        ((ca.angle + (b.angle - β0)) / (4 : Rat)).floor = 0 ∧
        ((ca.angle + (c.angle - β0)) / (4 : Rat)).floor = 0 ∧
        commonBaseTailRecursivePayloadEqWitnesses ca β0 bs cs)
  | _, _ => False

/-- Full common-baseline right-tail list equality in the recursive-left-payload
    branch, after recursive induction has supplied payload equality witnesses
    for every paired tail cell. -/
theorem right_tail_cells_eq_of_commonBase_tail_eq_left_payload_some_of_payloadEqWitnesses
    (d : Nat) (β0 : Rat) (ca : Cell UCNSObject)
    (bs cs : List (Cell UCNSObject)) (p : UCNSObject)
    (hca : ca.payload = some p)
    (hwitnesses : commonBaseTailRecursivePayloadEqWitnesses ca β0 bs cs)
    (hrow : multiplyRowWithBase d β0 bs ca =
      multiplyRowWithBase d β0 cs ca) :
    bs = cs := by
  induction bs generalizing cs with
  | nil =>
      cases cs with
      | nil => rfl
      | cons c cs =>
          simp [commonBaseTailRecursivePayloadEqWitnesses] at hwitnesses
  | cons b bs ih =>
      cases cs with
      | nil =>
          simp [commonBaseTailRecursivePayloadEqWitnesses] at hwitnesses
      | cons c cs =>
          rcases hwitnesses with ⟨q, r, hbPayload, hcPayload, hqr, hbFloor, hcFloor, hrest⟩
          have hstep :=
            right_tail_head_cell_eq_and_tail_product_cells_eq_of_commonBase_tail_eq_left_payload_some_of_floor_div_four_eq_zero_of_payload_eq
              d β0 ca b c bs cs p q r hca hbPayload hcPayload hqr hbFloor hcFloor hrow
          have htailEq := ih cs hrest hstep.2
          rw [hstep.1, htailEq]

/-- Full `AlignedComplete` successor-product right-tail list equality in the
    recursive-left-payload branch, after peeling the selected right head and
    supplying recursive payload equality witnesses for every paired tail cell. -/
theorem right_tail_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_left_payload_some_of_payloadEqWitnesses
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p : UCNSObject)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hca : ca.payload = some p)
    (hwitnesses : commonBaseTailRecursivePayloadEqWitnesses ca b.angle bs cs)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    bs = cs := by
  exact right_tail_cells_eq_of_commonBase_tail_eq_left_payload_some_of_payloadEqWitnesses
    d b.angle ca bs cs p hca hwitnesses
    (tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
      d nda ndb ndc ca b c rest bs cs hABC h)

/-- One `AlignedComplete` successor-product list-induction step for the
    recursive-left-payload branch: consume the first non-head tail cell after
    recursive induction identifies the payload witnesses, and preserve
    common-baseline equality of the remaining mapped tails. -/
theorem right_tail_head_cell_eq_and_tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_left_payload_some_of_floor_div_four_eq_zero_of_payload_eq
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (hca : ca.payload = some p)
    (hbPayload : b₁.payload = some q)
    (hcPayload : c₁.payload = some r)
    (hqr : q = r)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (hb :
      ((ca.angle + (b₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    b₁ = c₁ ∧ multiplyRowWithBase d b.angle bs ca =
      multiplyRowWithBase d b.angle cs ca := by
  exact
    right_tail_head_cell_eq_and_tail_product_cells_eq_of_commonBase_tail_eq_left_payload_some_of_floor_div_four_eq_zero_of_payload_eq
      d b.angle ca b₁ c₁ bs cs p q r hca hbPayload hcPayload hqr hb hc
      (tail_product_cells_eq_of_multiplyFuel_succ_eq_alignedComplete_commonBase
        d nda ndb ndc ca b c rest (b₁ :: bs) (c₁ :: cs) hABC h)

/-- First non-head tail-cell equality in the unit-left-payload case. Angle
    equality is supplied by the floor-zero canonical-domain bridge, face
    equality by xor inversion, and payload equality by collapsing the shared
    payload relation under `ca.payload = none`. -/
theorem right_tail_head_cell_eq_of_multiplyFuel_succ_eq_alignedComplete_left_payload_none_of_floor_div_four_eq_zero
    (d nda ndb ndc : Nat) (ca b c b₁ c₁ : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: b₁ :: bs))
      (UCNSObject.mk ndc (c :: c₁ :: cs)) (d + 1))
    (hca : ca.payload = none)
    (hb :
      ((ca.angle + (b₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (hc :
      ((ca.angle + (c₁.angle - b.angle)) / (4 : Rat)).floor = 0)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: b₁ :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: c₁ :: cs))) :
    b₁ = c₁ := by
  have hangle :=
    right_tail_head_angle_eq_of_multiplyFuel_succ_eq_alignedComplete_of_floor_div_four_eq_zero
      d nda ndb ndc ca b c b₁ c₁ rest bs cs hABC hb hc h
  have hface :=
    right_tail_head_face_eq_of_multiplyFuel_succ_eq_alignedComplete
      d nda ndb ndc ca b c b₁ c₁ rest bs cs hABC h
  have hpayload :=
    right_payload_eq_of_rightHeadPayloadRelation_left_payload_none d ca b₁ c₁ hca
      (right_tail_head_payload_relation_of_multiplyFuel_succ_eq_alignedComplete
        d nda ndb ndc ca b c b₁ c₁ rest bs cs hABC h)
  exact cell_eq_of_fields_eq hangle hface hpayload


/-- Under `AlignedComplete`, successor-product equality exposes equality of the
    first product row tails with a shared right-head base angle. Head-angle
    equality comes from recursive host-normalization; the remaining tail cells
    still require non-head field inversion. -/
theorem tail_product_cells_map_eq_of_multiplyFuel_succ_eq_alignedComplete
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    List.map (fun (cb : Cell UCNSObject) =>
      Cell.mk
        (amod4 (ca.angle + (cb.angle - b.angle)))
        (xor ca.face cb.face)
        (match ca.payload, cb.payload with
          | some p, some q => some (multiplyFuel d p q)
          | some p, none   => some p
          | none,   some q => some q
          | none,   none   => none)) bs =
    List.map (fun (cc : Cell UCNSObject) =>
      Cell.mk
        (amod4 (ca.angle + (cc.angle - b.angle)))
        (xor ca.face cc.face)
        (match ca.payload, cc.payload with
          | some p, some r => some (multiplyFuel d p r)
          | some p, none   => some p
          | none,   some r => some r
          | none,   none   => none)) cs := by
  have hrow : multiplyRow d (b :: bs) ca = multiplyRow d (c :: cs) ca :=
    first_row_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca rest (b :: bs) (c :: cs) h
  exact tail_product_cells_eq_of_first_row_eq_head_angle_eq d ca b c bs cs
    (right_head_angle_eq_of_alignedComplete_heads (d + 1) nda ndb ndc ca b c rest bs cs hABC)
    hrow

/-- In the unit-left-payload case, successor-product equality plus
    `AlignedComplete` already identifies the selected right-head cells: angles
    come from recursive host-normalization, faces from xor inversion, and
    payloads from the unit-left-payload row inversion. -/
theorem right_head_cell_eq_of_multiplyFuel_succ_eq_left_payload_none
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hca : ca.payload = none)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    b = c := by
  have hangle := right_head_angle_eq_of_alignedComplete_heads (d + 1) nda ndb ndc ca b c rest bs cs hABC
  have hface := right_head_face_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca b c rest bs cs h
  have hpayload :=
    right_head_payload_eq_of_multiplyFuel_succ_eq_left_payload_none d nda ndb ndc ca b c rest bs cs hca h
  exact cell_eq_of_fields_eq hangle hface hpayload


theorem common_depth_left_right_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth A = depth B := h.2.2.2.1

theorem common_depth_right_cancel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth B = depth C := h.2.2.2.2.1

theorem depth_right_le_fuel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth B ≤ d := h.2.2.2.2.2.1

theorem depth_cancel_le_fuel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth C ≤ d := h.2.2.2.2.2.2

/-- Every UCNS object has positive Lean depth. This is the basic fuel fact
    used to rule out the `multiplyFuel 0` identity branch under
    `AlignedComplete`. -/
theorem depth_pos (A : UCNSObject) : 0 < depth A := by
  cases A with
  | mk nd cs =>
    unfold depth
    simpa [Nat.succ_eq_add_one, Nat.add_comm] using Nat.succ_pos (depthCells cs)

/-- Selected recursive payloads inherit the full `AlignedComplete` domain with
    one less fuel. This is the induction-domain handoff for the `some/some`
    head branch. -/
theorem alignedComplete_payloads_of_alignedComplete_heads_some
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p q r : UCNSObject)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hca : ca.payload = some p)
    (hb : b.payload = some q)
    (hc : c.payload = some r) :
    AlignedComplete p q r d := by
  have hCp : Complete p :=
    complete_payload_of_complete_mk_cons_head_payload_some nda ca rest p
      (complete_left_of_alignedComplete hABC) hca
  have hCq : Complete q :=
    complete_payload_of_complete_mk_cons_head_payload_some ndb b bs q
      (complete_right_of_alignedComplete hABC) hb
  have hCr : Complete r :=
    complete_payload_of_complete_mk_cons_head_payload_some ndc c cs r
      (complete_cancel_of_alignedComplete hABC) hc
  have hpa :=
    depth_eq_succ_depth_payload_of_uniformDepth_mk_cons_head_payload_some nda ca rest p
      (complete_left_of_alignedComplete hABC).2.2.1 hca
  have hqb :=
    depth_eq_succ_depth_payload_of_uniformDepth_mk_cons_head_payload_some ndb b bs q
      (complete_right_of_alignedComplete hABC).2.2.1 hb
  have hrc :=
    depth_eq_succ_depth_payload_of_uniformDepth_mk_cons_head_payload_some ndc c cs r
      (complete_cancel_of_alignedComplete hABC).2.2.1 hc
  have hpq : depth p = depth q := by
    have hparent := common_depth_left_right_of_alignedComplete hABC
    rw [hpa, hqb] at hparent
    exact Nat.succ.inj (by simpa [Nat.succ_eq_add_one] using hparent)
  have hqr : depth q = depth r := by
    have hparent := common_depth_right_cancel_of_alignedComplete hABC
    rw [hqb, hrc] at hparent
    exact Nat.succ.inj (by simpa [Nat.succ_eq_add_one] using hparent)
  have hqle : depth q ≤ d := by
    have hle := depth_right_le_fuel_of_alignedComplete hABC
    rw [hqb] at hle
    exact Nat.succ_le_succ_iff.mp (by simpa [Nat.succ_eq_add_one] using hle)
  have hrle : depth r ≤ d := by
    have hle := depth_cancel_le_fuel_of_alignedComplete hABC
    rw [hrc] at hle
    exact Nat.succ_le_succ_iff.mp (by simpa [Nat.succ_eq_add_one] using hle)
  exact ⟨hCp, hCq, hCr, hpq, hqr, hqle, hrle⟩

/-- A selected recursive head payload makes the enclosing object non-flat. -/
theorem depth_gt_one_of_mk_cons_head_payload_some
    (nd : Nat) (c : Cell UCNSObject) (cs : List (Cell UCNSObject))
    (p : UCNSObject)
    (hc : c.payload = some p) :
    1 < depth (UCNSObject.mk nd (c :: cs)) := by
  cases c with
  | mk angle face payload =>
      cases payload with
      | none =>
          simp at hc
      | some p' =>
          simp only [depth, depthCells, depthCell]
          have hmax : 0 < Nat.max (depth p') (depthCells cs) :=
            Nat.lt_of_lt_of_le (depth_pos p') (Nat.le_max_left _ _)
          simpa using Nat.add_lt_add_left hmax 1

/-- Under common depth, a recursive payload at a selected left head forces a
    selected right head to carry a recursive payload as well. This rules out the
    recursive-left/unit-right mismatch before invoking recursive cancellation. -/
theorem exists_right_head_payload_of_alignedComplete_left_head_payload_some
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p : UCNSObject)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) d)
    (hca : ca.payload = some p) :
    (∃ q, b.payload = some q) ∧ (∃ r, c.payload = some r) := by
  have hAgt : 1 < depth (UCNSObject.mk nda (ca :: rest)) :=
    depth_gt_one_of_mk_cons_head_payload_some nda ca rest p hca
  have hBgt : 1 < depth (UCNSObject.mk ndb (b :: bs)) := by
    rwa [common_depth_left_right_of_alignedComplete hABC] at hAgt
  have hCgt : 1 < depth (UCNSObject.mk ndc (c :: cs)) := by
    rwa [common_depth_right_cancel_of_alignedComplete hABC] at hBgt
  exact
    ⟨exists_head_payload_of_complete_mk_cons_depth_gt_one ndb b bs
        (complete_right_of_alignedComplete hABC) hBgt,
      exists_head_payload_of_complete_mk_cons_depth_gt_one ndc c cs
        (complete_cancel_of_alignedComplete hABC) hCgt⟩

/-- Successor-product equality in the recursive-head case supplies the exact
    recursive equality needed by induction, with the matching right-head payload
    witnesses obtained from `AlignedComplete` rather than passed by the caller. -/
theorem recursive_payload_eq_of_multiplyFuel_succ_eq_left_payload_some
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p : UCNSObject)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hca : ca.payload = some p)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    ∃ q r, b.payload = some q ∧ c.payload = some r ∧
      multiplyFuel d p q = multiplyFuel d p r := by
  rcases exists_right_head_payload_of_alignedComplete_left_head_payload_some
      (d + 1) nda ndb ndc ca b c rest bs cs p hABC hca with
    ⟨⟨q, hb⟩, ⟨r, hc⟩⟩
  exact ⟨q, r, hb, hc,
    recursive_payload_eq_of_multiplyFuel_succ_eq_some_some
      d nda ndb ndc ca b c rest bs cs p q r hca hb hc h⟩


/-- If the recursive induction hypothesis can cancel the smaller payload product,
    the recursive-head successor case recovers equality of the selected
    right-head payload fields. -/
theorem right_head_payload_eq_of_multiplyFuel_succ_eq_left_payload_some_of_recursive_cancel
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p : UCNSObject)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hca : ca.payload = some p)
    (hcancel : ∀ q r : UCNSObject,
      multiplyFuel d p q = multiplyFuel d p r → q = r)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    b.payload = c.payload := by
  rcases recursive_payload_eq_of_multiplyFuel_succ_eq_left_payload_some
      d nda ndb ndc ca b c rest bs cs p hABC hca h with
    ⟨q, r, hb, hc, hp⟩
  have hqr : q = r := hcancel q r hp
  rw [hb, hc, hqr]

/-- In the recursive-left-payload case, successor-product equality identifies
    the selected right-head cells once the caller supplies the recursive
    cancellativity step for the selected left payload. -/
theorem right_head_cell_eq_of_multiplyFuel_succ_eq_left_payload_some_of_recursive_cancel
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject)) (p : UCNSObject)
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hca : ca.payload = some p)
    (hcancel : ∀ q r : UCNSObject,
      multiplyFuel d p q = multiplyFuel d p r → q = r)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    b = c := by
  have hangle :=
    right_head_angle_eq_of_alignedComplete_heads (d + 1) nda ndb ndc ca b c rest bs cs hABC
  have hface := right_head_face_eq_of_multiplyFuel_succ_eq d nda ndb ndc ca b c rest bs cs h
  have hpayload :=
    right_head_payload_eq_of_multiplyFuel_succ_eq_left_payload_some_of_recursive_cancel
      d nda ndb ndc ca b c rest bs cs p hABC hca hcancel h
  exact cell_eq_of_fields_eq hangle hface hpayload


/-- Unified selected-head cell inversion for successor products. The unit-left
    payload case uses direct payload inversion; the recursive-left payload case
    uses the caller-provided smaller-fuel cancellation hypothesis for that
    selected payload. -/
theorem right_head_cell_eq_of_multiplyFuel_succ_eq_of_payload_recursive_cancel
    (d nda ndb ndc : Nat) (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hcancel : ∀ p q r : UCNSObject,
      ca.payload = some p →
      multiplyFuel d p q = multiplyFuel d p r → q = r)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    b = c := by
  cases hca : ca.payload with
  | none =>
      exact right_head_cell_eq_of_multiplyFuel_succ_eq_left_payload_none
        d nda ndb ndc ca b c rest bs cs hABC hca h
  | some p =>
      exact right_head_cell_eq_of_multiplyFuel_succ_eq_left_payload_some_of_recursive_cancel
        d nda ndb ndc ca b c rest bs cs p hABC hca
        (fun q r hp => hcancel p q r hca hp) h


/-- Object-level selected-head inversion for nonempty successor products. This
    is the same one-door head-cell inversion as above, packaged at the
    `UCNSObject.mk` boundary so the main cancellativity proof can expose the
    first cells of all three operands and immediately recover equality of the
    two right heads. -/
theorem right_head_cell_eq_of_multiplyFuel_succ_eq_mk_cons_of_payload_recursive_cancel
    (d nda ndb ndc : Nat)
    (ca b c : Cell UCNSObject)
    (rest bs cs : List (Cell UCNSObject))
    (hABC : AlignedComplete
      (UCNSObject.mk nda (ca :: rest))
      (UCNSObject.mk ndb (b :: bs))
      (UCNSObject.mk ndc (c :: cs)) (d + 1))
    (hcancel : ∀ p q r : UCNSObject,
      ca.payload = some p →
      multiplyFuel d p q = multiplyFuel d p r → q = r)
    (h :
      multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndb (b :: bs)) =
        multiplyFuel (d + 1) (UCNSObject.mk nda (ca :: rest)) (UCNSObject.mk ndc (c :: cs))) :
    b = c := by
  exact right_head_cell_eq_of_multiplyFuel_succ_eq_of_payload_recursive_cancel
    d nda ndb ndc ca b c rest bs cs hABC hcancel h

theorem depth_left_le_fuel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth A ≤ d := by
  rw [common_depth_left_right_of_alignedComplete h]
  exact depth_right_le_fuel_of_alignedComplete h

/-- `AlignedComplete` plus the fuel bound excludes the zero-fuel branch of
    `multiplyFuel`: the common positive depth must fit inside the fuel. -/
theorem fuel_pos_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    0 < d :=
  Nat.lt_of_lt_of_le (depth_pos B) (depth_right_le_fuel_of_alignedComplete h)

/-- A convenience destructor for cancellativity proofs: under
    `AlignedComplete`, the fuel can always be exposed as `d0 + 1`, so proofs may
    unfold the product branch rather than the fuel-zero identity branch. -/
theorem exists_fuel_pred_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    ∃ d0, d = d0 + 1 := by
  cases d with
  | zero =>
    exact absurd (fuel_pos_of_alignedComplete h) (Nat.not_lt_zero 0)
  | succ d0 =>
    exact ⟨d0, rfl⟩

end UCNSObject

open UCNSObject

theorem complete_left_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    Complete A := h.1

theorem complete_right_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    Complete B := h.2.1

theorem complete_cancel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    Complete C := h.2.2.1

theorem common_depth_left_right_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth A = depth B := h.2.2.2.1

theorem common_depth_right_cancel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth B = depth C := h.2.2.2.2.1

theorem depth_right_le_fuel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth B ≤ d := h.2.2.2.2.2.1

theorem depth_cancel_le_fuel_of_alignedComplete
    {A B C : UCNSObject} {d : Nat} (h : AlignedComplete A B C d) :
    depth C ≤ d := h.2.2.2.2.2.2


/-
  CANCELLATIVITY STATUS (2026-07-10)

  The formerly stated `multiply_left_cancellative` theorem over
  `AlignedComplete` is not merely unfinished: the concrete guardrail
  `not_multiply_left_cancellative_on_alignedComplete` above proves that the
  current domain is too weak. Non-head host angles may differ by multiples of
  four, collapse under `amod4` during multiplication, and still satisfy the
  current `Complete`/`AlignedComplete` predicates.

  Therefore the old `sorry`-backed theorem has been removed rather than
  discharged dishonestly. The next true theorem must strengthen the domain with
  canonical angle-range/floor-zero evidence (or normalize operands before the
  equality claim) and then rebuild the cancellativity proof against that sharper
  statement.
-/

end Ucns
