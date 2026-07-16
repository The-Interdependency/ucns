/-
  Ucns/PublicGonol.lean — load-bearing public-gonol origin and return canon.

  CANON SOURCE:
    The-Interdependency/a0-betatest
    commit 7af8debf6ef3905f01baff02b43d8c3bee16ccbc
    memory/ARCHITECTURE_FOUNDATION.md F3/F4

  ERIN CANON:
    * public-gonol position 0 is SPACE/ZERO;
    * that point is the Möbius twist, seam, and origin for the entire system;
    * the origin is fixed, not selected by first-anchor normalization;
    * one 360-degree circuit changes orientation;
    * complete return requires 720 degrees.

  This file does not invent a map from the 157 public vertices into the
  normalized recursive factorization angles of Ucns.Core. That bridge remains
  hmmm. It formalizes only the canon stated above and the lifted-carrier facts
  already present in A0.
-/

-- === MODULE_BUILD ===
-- id: ucns_formal_public_gonol
--   module_name: Ucns.PublicGonol
--   module_kind: schema
--   summary: formalizes the fixed SPACE/ZERO Möbius-twist origin, 157-position lifted carrier, orientation flip after one circuit, and 720-degree complete return
--   owner: Erin Spencer
--   public_surface: arity, Vertex, origin, Orientation, flip, oneCircuitDegrees, completeReturnDegrees, FramedPosition, advanceOneCircuit, advanceCompleteReturn, OriginPreservingPermutation
--   internal_surface: oneCircuitHalfTurns, completeReturnHalfTurns
--   auth_boundary: none
--   storage_boundary: none
--   network_boundary: none
--   user_data_boundary: none
--   admin_only: false
--   tests: lake build; tests/test_public_gonol_claim_guard.py
--   rollout: formal_definition_surface
--   rollback: remove only with a canon migration explicitly approved by Erin Spencer
--   requires: ucns_formal_core_definitions
--   since: 2026-07-16
--   unresolved: bridge from the fixed public-gonol frame into normalized recursive factorization objects remains hmmm
-- === END MODULE_BUILD ===

import Ucns.Core

namespace Ucns
namespace PublicGonol

/-- The exact public-gonol arity. -/
def arity : Nat := 157

 theorem arity_pos : 0 < arity := by
  norm_num [arity]

/-- A public-gonol carrier position. -/
abbrev Vertex := Fin arity

/-- SPACE/ZERO: the Möbius twist point, seam, and origin for the system. -/
def origin : Vertex := ⟨0, arity_pos⟩

@[simp] theorem origin_val : origin.val = 0 := rfl

/-- Position zero uniquely identifies the public origin. -/
theorem eq_origin_of_val_eq_zero (v : Vertex) (h : v.val = 0) : v = origin := by
  apply Fin.ext
  simpa [origin] using h

/-- The two orientations of the Möbius return state. -/
inductive Orientation where
  | positive
  | negative
  deriving DecidableEq, Repr

/-- Crossing one complete carrier circuit flips orientation. -/
def flip : Orientation → Orientation
  | .positive => .negative
  | .negative => .positive

@[simp] theorem flip_flip (o : Orientation) : flip (flip o) = o := by
  cases o <;> rfl

theorem flip_ne_self (o : Orientation) : flip o ≠ o := by
  cases o <;> simp [flip]

/-- One circuit of the carrier. It is not a complete system return. -/
def oneCircuitDegrees : Nat := 360

/-- The complete system return required by the Möbius twist. -/
def completeReturnDegrees : Nat := 720

@[simp] theorem completeReturnDegrees_eq_720 : completeReturnDegrees = 720 := rfl

@[simp] theorem completeReturn_is_two_circuits :
    completeReturnDegrees = 2 * oneCircuitDegrees := by
  norm_num [completeReturnDegrees, oneCircuitDegrees]

/-- Existing normalized factorization angles use half-turn units. These names
    record the 360/720 period only; they do not map public vertices to angles. -/
def oneCircuitHalfTurns : Rat := 2
def completeReturnHalfTurns : Rat := 4

/-- In the existing mod-4 internal angle representation, 360 degrees is the
    opposite orientation state, not the normalized return. -/
theorem oneCircuit_amod4 :
    UCNSObject.amod4 oneCircuitHalfTurns = 2 := by
  norm_num [oneCircuitHalfTurns, UCNSObject.amod4, UCNSObject.amod]

/-- In the existing mod-4 internal angle representation, 720 degrees returns
    to the period origin. This is a period fact, not a vertex-angle bridge. -/
theorem completeReturn_amod4 :
    UCNSObject.amod4 completeReturnHalfTurns = 0 := by
  norm_num [completeReturnHalfTurns, UCNSObject.amod4, UCNSObject.amod]

theorem oneCircuit_is_not_complete_return :
    UCNSObject.amod4 oneCircuitHalfTurns ≠ 0 := by
  rw [oneCircuit_amod4]
  norm_num

/-- Recover the local public-gonol position from an absolute lifted position. -/
def localVertex (position : Nat) : Vertex :=
  ⟨position % arity, Nat.mod_lt _ arity_pos⟩

@[simp] theorem localVertex_val (position : Nat) :
    (localVertex position).val = position % arity := rfl

@[simp] theorem localVertex_zero : localVertex 0 = origin := by
  rfl

/-- One 157-step circuit returns to the same local carrier position. -/
theorem add_arity_same_local_vertex (position : Nat) :
    localVertex (position + arity) = localVertex position := by
  apply Fin.ext
  simp [localVertex, Nat.add_mod]

/-- A circuit advances on the lifted path; it is never a zero-length repeat. -/
theorem add_arity_strict (position : Nat) : position < position + arity := by
  omega

/-- A lifted position together with the orientation carried across the twist. -/
structure FramedPosition where
  position : Nat
  orientation : Orientation
  deriving Repr

/-- Advance one carrier circuit: same local vertex, opposite orientation. -/
def advanceOneCircuit (state : FramedPosition) : FramedPosition :=
  { position := state.position + arity
    orientation := flip state.orientation }

/-- Advance the complete 720-degree return: two carrier circuits. -/
def advanceCompleteReturn (state : FramedPosition) : FramedPosition :=
  advanceOneCircuit (advanceOneCircuit state)

@[simp] theorem oneCircuit_same_local_vertex (state : FramedPosition) :
    localVertex (advanceOneCircuit state).position = localVertex state.position := by
  exact add_arity_same_local_vertex state.position

theorem oneCircuit_changes_orientation (state : FramedPosition) :
    (advanceOneCircuit state).orientation ≠ state.orientation := by
  exact flip_ne_self state.orientation

@[simp] theorem completeReturn_same_local_vertex (state : FramedPosition) :
    localVertex (advanceCompleteReturn state).position = localVertex state.position := by
  simp [advanceCompleteReturn, advanceOneCircuit, add_arity_same_local_vertex]

@[simp] theorem completeReturn_restores_orientation (state : FramedPosition) :
    (advanceCompleteReturn state).orientation = state.orientation := by
  simp [advanceCompleteReturn, advanceOneCircuit]

/-- An admissible public-frame permutation must fix SPACE/ZERO exactly. -/
structure OriginPreservingPermutation where
  toEquiv : Equiv.Perm Vertex
  fixesOrigin : toEquiv origin = origin

@[simp] theorem origin_fixed (transform : OriginPreservingPermutation) :
    transform.toEquiv origin = origin :=
  transform.fixesOrigin

end PublicGonol
end Ucns
