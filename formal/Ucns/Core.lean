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
--   public_surface: UCNSObject, Cell, amod4, circleFrac, nMin, depth, normalizeFuel, multiplyFuel, HostNormalized, Complete (with NonemptyRec/HostNormalizedRec/UniformDepth/CanonicalCarrier), carrier_lcm_law + multiply_left_cancellative (statements)
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
--   unresolved: AlignedComplete cancellativity statement ratified 2026-06-21 + applied (sorry; not machine-checked here — proof + Mathlib pin pending). Discharge order — cancellativity, then carrier_lcm_law, then depth1 completeness
-- === END MODULE_BUILD ===

import Std.Data.Rat.Basic
import Std.Data.Nat.Gcd

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

/-- Recursive nonemptiness: no empty cell-list at any level
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

/-- Recursive host-normalization: head angle 0 for the object AND every payload
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

/-- Canonical carrier: `nDec = nMin cells` at every level
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

/-- Per-object uniform depth: all cells share one `depthCell`, recursively
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

end UCNSObject

open UCNSObject

/--
  CARRIER-LCM LAW (statement; prose proof in
  docs/carrier-support-pruning.md; TEST-BACKED at 2000 trials in
  ucns_recursive/tests/test_catalogue_pruning.py).

  For host-normalized A, B and sufficient fuel, the carrier of the
  product is exactly the lcm of the operand carriers.

  STUB: proves nothing — closed by `sorry`. A `sorry`-backed statement
  confers no DEFENDED status (see README.md).
-/
theorem carrier_lcm_law
    (A B : UCNSObject) (d : Nat)
    (hA : HostNormalized A) (hB : HostNormalized B)
    (hd : 1 ≤ d) :
    nMin (multiplyFuel d A B) = Nat.lcm (nMin A) (nMin B) := by
  sorry

/--
  CANCELLATIVITY on the ratified `AlignedComplete` domain (Step-1 result;
  Erin ratified 2026-06-21). The bare statement is FALSE; left-cancellativity
  requires `Complete A,B,C` (nonempty + recursive host-normalized + uniform
  depth + canonical carrier) AND cross-operand common depth
  (`depth A = depth B = depth C`), with `depth B,C ≤ d`. See
  `formal/cancellativity-step1-findings.md` for the counterexample search.

  STUB: proves nothing — closed by `sorry`. A `sorry`-backed statement confers
  NO DEFENDED status (see README.md). Not machine-checked in the authoring
  environment; the proof discharge + Mathlib pin are Step-2 work.
-/
theorem multiply_left_cancellative
    (A B C : UCNSObject) (d : Nat)
    (hA : Complete A) (hB : Complete B) (hC : Complete C)
    (hAB : depth A = depth B) (hBC : depth B = depth C)   -- common depth
    (h : multiplyFuel d A B = multiplyFuel d A C)
    (hdB : depth B ≤ d) (hdC : depth C ≤ d) :
    B = C := by
  sorry

end Ucns
