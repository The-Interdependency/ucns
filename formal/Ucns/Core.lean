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
--   summary: Faithful Lean 4 model of UCNSObject, carrier (nMin), depth, fuel-indexed normalize and multiply, and the statement surface for the Carrier-LCM Law and cancellativity.
--   owner: Erin Spencer
--   public_surface: UCNSObject, Cell, amod4, circleFrac, nMin, depth, normalizeFuel, multiplyFuel, HostNormalized, Complete/AlignedComplete (with NonemptyRec/HostNormalizedRec/UniformDepth/CanonicalCarrier), multiply_left_cancellative (statement)
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
--   unresolved: AlignedComplete cancellativity statement ratified 2026-06-21 + applied (sorry; proof pending). Carrier-LCM is discharged in Ucns/CarrierLcm.lean; remaining order — cancellativity, then depth1 completeness
-- === END MODULE_BUILD ===

import Std.Data.Rat.Basic
import Std.Data.Nat.Gcd
import Std.Data.List.Lemmas

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

/-- Ratified cancellativity domain: each operand is `Complete`, all three
    operands share one depth, and the right-hand operands fit inside the
    available multiplication fuel. -/
def AlignedComplete (A B C : UCNSObject) (d : Nat) : Prop :=
  Complete A ∧ Complete B ∧ Complete C ∧
    depth A = depth B ∧ depth B = depth C ∧ depth B ≤ d ∧ depth C ≤ d

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

/-- Every UCNS object has positive Lean depth. This is the basic fuel fact
    used to rule out the `multiplyFuel 0` identity branch under
    `AlignedComplete`. -/
theorem depth_pos (A : UCNSObject) : 0 < depth A := by
  cases A with
  | mk nd cs =>
    unfold depth
    simpa [Nat.succ_eq_add_one, Nat.add_comm] using Nat.succ_pos (depthCells cs)

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
  CANCELLATIVITY on the ratified `AlignedComplete` domain (Step-1 result;
  Erin ratified 2026-06-21). The bare statement is FALSE; left-cancellativity
  requires `Complete A,B,C` (nonempty + recursive host-normalized + uniform
  depth + canonical carrier) AND cross-operand common depth
  (`depth A = depth B = depth C`), with `depth B,C ≤ d`. See
  `formal/cancellativity-step1-findings.md` for the counterexample search.

  STUB: proves nothing — closed by `sorry`. A `sorry`-backed statement confers
  NO DEFENDED status (see README.md). The statement now takes the domain as a
  single `AlignedComplete` hypothesis so the remaining proof target cannot
  accidentally omit one of the counterexample-blocking conjuncts.
-/
/-- The remaining cancellativity proof obligation after `AlignedComplete` has
    ruled out zero fuel. This is the real recursive-product case: the proof may
    unfold `multiplyFuel (d0 + 1)` and reason about the row-major product cells.

    Still `sorry`-backed: this theorem marks the exact argument frontier. -/
theorem multiply_left_cancellative_succ_obligation
    (A B C : UCNSObject) (d0 : Nat)
    (hABC : AlignedComplete A B C (d0 + 1))
    (h : multiplyFuel (d0 + 1) A B = multiplyFuel (d0 + 1) A C) :
    B = C := by
  sorry

theorem multiply_left_cancellative
    (A B C : UCNSObject) (d : Nat)
    (hABC : AlignedComplete A B C d)
    (h : multiplyFuel d A B = multiplyFuel d A C) :
    B = C := by
  rcases exists_fuel_pred_of_alignedComplete hABC with ⟨d0, rfl⟩
  exact multiply_left_cancellative_succ_obligation A B C d0 hABC h

end Ucns
