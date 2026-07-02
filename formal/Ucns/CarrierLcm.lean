/-
  Ucns/CarrierLcm.lean — discharge skeleton for the Carrier-LCM Law.

  Mirrors the prose proof in docs/carrier-support-pruning.md §2:

    upper bound:  every product-angle denominator divides L = lcm(nMin A, nMin B)
    lower bound:  each factor's angles embed verbatim in the product (j=0 / k=0
                  slices), so nMin A ∣ nMin P and nMin B ∣ nMin P
    conclusion:   Nat.dvd_antisymm.

  DISCHARGE STATE — read before citing:
  - The lcm fold engine (`dvd_foldl_lcm_acc`, `dvd_foldl_lcm`, `foldl_lcm_dvd`)
    and the composition layer (`carrier_lcm_law'` from the two bound
    lemmas) are targeted SORRY-FREE.
  - The Rat denominator leaves (`den_add_dvd_lcm`, `den_amod_dvd`) are
    discharged against the installed `Std` Rat API.
  - The slice-embedding proofs compile under the pinned Lean/Lake build.
  - The upper-bound bind/map threading proof and the circle-fraction addition
    denominator bridge compile under the pinned Lean/Lake build.
  - This module is intended to be `sorry`-free; imported frontier files may
    still contain `sorry` leaves with NO DEFENDED status (formal/README.md).
  - Remaining `sorry` leaves include the upper-bound threading proof. A
    `sorry`-backed lemma confers NO DEFENDED status (formal/README.md).
-/

-- === MODULE_BUILD ===
-- id: ucns_formal_carrier_lcm_discharge
--   module_name: Ucns.CarrierLcm
--   module_kind: schema
--   summary: Decomposition of the Carrier-LCM Law into machine-checked composition plus isolated leaf obligations, with the Nat.lcm fold engine fully discharged.
--   owner: Erin Spencer
--   public_surface: dvd_foldl_lcm, foldl_lcm_dvd, nMin_dvd_of_denoms_subset, carrier_lcm_law_upper, carrier_lcm_law_lower, carrier_lcm_law'
--   internal_surface: none
--   auth_boundary: none
--   storage_boundary: none
--   network_boundary: none
--   user_data_boundary: none
--   admin_only: false
--   tests: lake build; sorry-count visible in CI per-run report
--   rollout: built by the formal CI job
--   rollback: remove file and its import from Ucns.lean
--   requires: ucns_formal_core_definitions
--   since: 2026-06-10
--   unresolved: none in this module; imported frontier files still contain sorry-backed statements
-- === END MODULE_BUILD ===

import Ucns.Core
import Std.Data.Nat.Gcd
import Std.Data.Rat.Lemmas
import Std.Data.List.Lemmas
import Mathlib.Data.Rat.Floor
import Mathlib.Tactic.Ring

namespace Ucns
namespace UCNSObject

/-! ## The lcm fold engine (target: sorry-free) -/

/-- Divisibility of the accumulator persists through the lcm-fold. -/
theorem dvd_foldl_lcm_acc (l : List Nat) (d : Nat) :
    ∀ a : Nat, d ∣ a → d ∣ l.foldl Nat.lcm a := by
  induction l with
  | nil => intro a h; simpa using h
  | cons y _ ih =>
    intro a h
    exact ih (Nat.lcm a y) (Nat.dvd_trans h (Nat.dvd_lcm_left a y))

/-- Every element of the list divides the lcm-fold. -/
theorem dvd_foldl_lcm (x : Nat) :
    ∀ (l : List Nat), x ∈ l → ∀ a : Nat, x ∣ l.foldl Nat.lcm a
  | [], hx, _ => absurd hx (List.not_mem_nil x)
  | y :: ys, hx, a => by
    rcases List.mem_cons.mp hx with h | h
    · subst h
      exact dvd_foldl_lcm_acc ys x (Nat.lcm a x) (Nat.dvd_lcm_right a x)
    · exact dvd_foldl_lcm x ys h (Nat.lcm a y)

/-- If every element divides n, the lcm-fold (from a dividing seed)
    divides n. -/
theorem foldl_lcm_dvd (l : List Nat) (n : Nat)
    (h : ∀ x ∈ l, x ∣ n) (a : Nat) (ha : a ∣ n) :
    l.foldl Nat.lcm a ∣ n := by
  induction l generalizing a with
  | nil => simpa using ha
  | cons y ys ih =>
    have hy : y ∣ n := h y (List.mem_cons_self y ys)
    exact ih (fun x hx => h x (List.mem_cons_of_mem y hx))
      (Nat.lcm a y) (Nat.lcm_dvd ha hy)

/-! ## Denominator-set divisibility bridge -/

/-- If the denominator list of `cs` is a sub-multiset (membership-wise)
    of that of `ds`, then `nMin`-of-`cs` divides `nMin`-of-`ds`. -/
theorem nMin_dvd_of_denoms_subset
    (cs ds : List (Cell UCNSObject))
    (h : ∀ x ∈ angleDenoms cs, x ∈ angleDenoms ds) :
    (angleDenoms cs).foldl Nat.lcm 1 ∣ (angleDenoms ds).foldl Nat.lcm 1 := by
  exact foldl_lcm_dvd _ _
    (fun x hx => dvd_foldl_lcm x _ (h x hx) 1)
    1 (Nat.one_dvd _)


/-- A `Complete` object is host-normalized at the top level. -/
theorem hostNormalized_of_complete (A : UCNSObject) (hA : Complete A) :
    HostNormalized A := by
  cases A with
  | mk nd cs =>
    simp [Complete, HostNormalized, HostNormalizedRec] at hA ⊢
    exact hA.2.1.1

/-- A `Complete` object has a nonempty top-level cell list. -/
theorem cells_ne_nil_of_complete (A : UCNSObject) (hA : Complete A) :
    A.cells ≠ [] := by
  cases A with
  | mk nd cs =>
    simp [Complete, NonemptyRec] at hA ⊢
    exact hA.1.1

/-- A `Complete` object has a top-level head cell. -/
theorem exists_head?_of_complete (A : UCNSObject) (hA : Complete A) :
    ∃ c, A.cells.head? = some c := by
  cases A with
  | mk nd cs =>
    rcases List.exists_cons_of_ne_nil (cells_ne_nil_of_complete (UCNSObject.mk nd cs) hA) with
      ⟨c, rest, hcs⟩
    subst hcs
    exact ⟨c, rfl⟩

/-- The head cell of a `Complete` object has zero angle. -/
theorem head_angle_zero_of_complete (A : UCNSObject) (hA : Complete A)
    {c : Cell UCNSObject} (hc : A.cells.head? = some c) :
    c.angle = 0 :=
  hostNormalized_of_complete A hA c hc

/-- A cell returned by `head?` is a member of the same list.

    Local replacement for newer `List.mem_of_mem_head?` API names that are not
    present in the pinned Lean 4.7.0/Std version. -/
theorem mem_of_head?_eq_some {α : Type} {xs : List α} {x : α}
    (h : xs.head? = some x) : x ∈ xs := by
  cases xs with
  | nil =>
    simp at h
  | cons y ys =>
    simp at h
    simp [h]

/-- `Rat.floor` shifts predictably by an integer.

    Local bridge from the protected `Rat.floor` used by `amod` to Mathlib's
    floor-ring notation/API. -/
theorem rat_floor_sub_int (a : Rat) (z : Int) :
    Rat.floor (a - (z : Rat)) = Rat.floor a - z := by
  change ⌊a - (z : Rat)⌋ = ⌊a⌋ - z
  exact Int.floor_sub_int a z

/-- Taking the circle fraction after reducing modulo 4 is the same as taking
    the circle fraction directly: the extra reduction only subtracts an even
    integer before the final modulo-2 quotient. -/
theorem circleFrac_amod4 (a : Rat) : circleFrac (amod4 a) = circleFrac a := by
  unfold circleFrac amod4 amod
  let z4 : Int := Rat.floor (a / (4 : Rat))
  let z2 : Int := Rat.floor (a / (2 : Rat))
  have hdiv :
      (a - (4 : Rat) * (z4 : Rat)) / (2 : Rat) =
        a / (2 : Rat) - ((z4 * 2 : Int) : Rat) := by
    rw [Int.cast_mul]
    ring
  have hfloor :
      Rat.floor ((a - (4 : Rat) * (z4 : Rat)) / (2 : Rat)) = z2 - z4 * 2 := by
    rw [hdiv]
    dsimp [z2]
    exact rat_floor_sub_int (a / (2 : Rat)) (z4 * 2)
  change
    (a - (4 : Rat) * (z4 : Rat) -
        (2 : Rat) * (Rat.floor ((a - (4 : Rat) * (z4 : Rat)) / (2 : Rat)) : Int)) /
      (2 : Rat) =
    (a - (2 : Rat) * (z2 : Rat)) / (2 : Rat)
  rw [hfloor]
  rw [Int.cast_sub, Int.cast_mul]
  ring

/-- Membership in `angleDenoms` is exactly a cell whose nonzero circle fraction
    has the requested denominator. This packages the `map`/`filterMap` shape so
    slice proofs can focus on constructing product cells. -/
theorem mem_angleDenoms_iff (x : Nat) (cs : List (Cell UCNSObject)) :
    x ∈ angleDenoms cs ↔
      ∃ c, c ∈ cs ∧ circleFrac c.angle ≠ 0 ∧ (circleFrac c.angle).den = x := by
  unfold angleDenoms
  simp only [List.mem_filterMap, List.mem_map]
  constructor
  · rintro ⟨q, ⟨c, hc, rfl⟩, hq⟩
    by_cases hz : circleFrac c.angle = 0
    · simp [hz] at hq
    · simp [hz] at hq
      exact ⟨c, hc, hz, hq⟩
  · rintro ⟨c, hc, hz, hden⟩
    refine ⟨circleFrac c.angle, ⟨c, hc, rfl⟩, ?_⟩
    simp [hz, hden]

/-! ## Analytic leaves (precise hypotheses) -/

/-- The denominator emitted by `Rat.normalize` divides its input denominator. -/
theorem den_normalize_dvd (num : Int) (den : Nat) (h : den ≠ 0) :
    (Rat.normalize num den h).den ∣ den := by
  rcases Rat.normalize_num_den' num den h with ⟨d, _, _, hden⟩
  exact ⟨d, hden⟩

/-- The product of a natural-number rational and an integer rational is integral,
    hence has denominator one. -/
theorem den_mul_nat_int_cast_eq_one (n : Nat) (z : Int) :
    ((n : Rat) * (z : Rat)).den = 1 := by
  have hdiv : ((n : Rat) * (z : Rat)).den ∣ 1 := by
    rw [Rat.mul_def]
    have hraw :
        (Rat.normalize ((n : Rat).num * (z : Rat).num)
          ((n : Rat).den * (z : Rat).den)
          (Nat.mul_ne_zero (n : Rat).den_nz (z : Rat).den_nz)).den ∣
          (n : Rat).den * (z : Rat).den :=
      den_normalize_dvd _ _ _
    simpa only [Rat.ofNat_den, Rat.intCast_den, Nat.mul_one] using hraw
  exact Nat.eq_one_of_dvd_one hdiv

/-- The denominator emitted by `Rat.normalize` divides its input denominator. -/
theorem den_normalize_dvd (num : Int) (den : Nat) (h : den ≠ 0) :
    (Rat.normalize num den h).den ∣ den := by
  rcases Rat.normalize_num_den' num den h with ⟨d, _, _, hden⟩
  exact ⟨d, hden⟩

/-- The product of a natural-number rational and an integer rational is integral,
    hence has denominator one. -/
theorem den_mul_nat_int_cast_eq_one (n : Nat) (z : Int) :
    ((n : Rat) * (z : Rat)).den = 1 := by
  have hdiv : ((n : Rat) * (z : Rat)).den ∣ 1 := by
    rw [Rat.mul_def]
    have hraw :
        (Rat.normalize ((n : Rat).num * (z : Rat).num)
          ((n : Rat).den * (z : Rat).den)
          (Nat.mul_ne_zero (n : Rat).den_nz (z : Rat).den_nz)).den ∣
          (n : Rat).den * (z : Rat).den :=
      den_normalize_dvd _ _ _
    simpa only [Rat.ofNat_den, Rat.intCast_den, Nat.mul_one] using hraw
  exact Nat.eq_one_of_dvd_one hdiv

/-- amod never enlarges a denominator. LEAF: Rat arithmetic. -/
theorem den_amod_dvd (a : Rat) (n : Nat) (_hn : 0 < n) :
    (amod a n).den ∣ a.den := by
  unfold amod
  let z : Int := (a / (n : Rat)).floor
  have hmul : ((n : Rat) * (z : Rat)).den = 1 :=
    den_mul_nat_int_cast_eq_one n z
  rw [Rat.sub_def]
  have hnorm :
      (Rat.normalize
        (a.num * ((n : Rat) * (z : Rat)).den -
          ((n : Rat) * (z : Rat)).num * a.den)
        (a.den * ((n : Rat) * (z : Rat)).den)
        (Nat.mul_ne_zero a.den_nz ((n : Rat) * (z : Rat)).den_nz)).den ∣
        a.den * ((n : Rat) * (z : Rat)).den :=
    den_normalize_dvd _ _ _
  have hprod : a.den * ((n : Rat) * (z : Rat)).den ∣ a.den := by
    rw [hmul, Nat.mul_one]
  exact Nat.dvd_trans hnorm hprod

/-- The denominator emitted by `Rat.maybeNormalize` divides its input
    denominator whenever the normalizing gcd divides that denominator. -/
theorem den_maybeNormalize_dvd_of_dvd (num : Int) (den g : Nat)
    (den_nz : den / g ≠ 0) (reduced : (num.div g).natAbs.Coprime (den / g))
    (hg : g ∣ den) :
    (Rat.maybeNormalize num den g den_nz reduced).den ∣ den := by
  unfold Rat.maybeNormalize
  by_cases h : g = 1
  · simp [h]
  · simp [h]
    exact ⟨g, (Nat.div_mul_cancel hg).symm⟩

/-- The denominator of a sum divides the lcm of the denominators.
    LEAF: Rat arithmetic. -/
theorem den_add_dvd_lcm (a b : Rat) :
    (a + b).den ∣ Nat.lcm a.den b.den := by
  change (Rat.add a b).den ∣ Nat.lcm a.den b.den
  unfold Rat.add
  dsimp only
  by_cases hg : Nat.gcd a.den b.den = 1
  · simp [hg, Nat.lcm]
  · simp [hg]
    let g := Nat.gcd a.den b.den
    let den := (a.den / g) * b.den
    let num := a.num * ↑(b.den / g) + b.num * ↑(a.den / g)
    let g1 := num.natAbs.gcd g
    have hden_dvd_lcm : den ∣ Nat.lcm a.den b.den := by
      have hden_eq : den = Nat.lcm a.den b.den := by
        simp [den, g, Nat.lcm]
        rw [Nat.mul_comm (a.den / Nat.gcd a.den b.den) b.den,
          ← Nat.mul_div_assoc b.den (Nat.gcd_dvd_left a.den b.den),
          Nat.mul_comm b.den a.den]
      rw [hden_eq]
    have hg1den : g1 ∣ den := by
      have e : g1 = num.natAbs.gcd den := Rat.add.aux a b rfl rfl rfl
      rw [e]
      exact Nat.gcd_dvd_right _ _
    have hnormden : den / g1 ∣ den := ⟨g1, (Nat.div_mul_cancel hg1den).symm⟩
    exact Nat.dvd_trans hnormden hden_dvd_lcm

/-- Adding angles and then taking the circle fraction is the same as adding
    circle fractions and reducing modulo one full circle-fraction turn. -/
theorem circleFrac_add_eq_amod_one (a b : Rat) :
    circleFrac (a + b) = amod (circleFrac a + circleFrac b) 1 := by
  unfold circleFrac amod
  let fa : Int := Rat.floor (a / (2 : Rat))
  let fb : Int := Rat.floor (b / (2 : Rat))
  let fab : Int := Rat.floor ((a + b) / (2 : Rat))
  have hsum :
      (a - (2 : Rat) * (fa : Rat)) / (2 : Rat) +
        (b - (2 : Rat) * (fb : Rat)) / (2 : Rat) =
        (a + b) / (2 : Rat) - ((fa + fb : Int) : Rat) := by
    rw [Int.cast_add]
    ring
  have hfloor :
      Rat.floor
        (((a - (2 : Rat) * (fa : Rat)) / (2 : Rat) +
          (b - (2 : Rat) * (fb : Rat)) / (2 : Rat)) / (1 : Rat)) =
        fab - (fa + fb) := by
    have hone :
        ((a - (2 : Rat) * (fa : Rat)) / (2 : Rat) +
          (b - (2 : Rat) * (fb : Rat)) / (2 : Rat)) / (1 : Rat) =
        (a - (2 : Rat) * (fa : Rat)) / (2 : Rat) +
          (b - (2 : Rat) * (fb : Rat)) / (2 : Rat) := by
      ring
    rw [hone, hsum]
    dsimp [fab]
    exact rat_floor_sub_int ((a + b) / (2 : Rat)) (fa + fb)
  change
    (a + b - (2 : Rat) * (Rat.floor ((a + b) / (2 : Rat)) : Int)) /
      (2 : Rat) =
    (a - (2 : Rat) * (fa : Rat)) / (2 : Rat) +
        (b - (2 : Rat) * (fb : Rat)) / (2 : Rat) -
      (1 : Rat) *
        (Rat.floor
          (((a - (2 : Rat) * (fa : Rat)) / (2 : Rat) +
            (b - (2 : Rat) * (fb : Rat)) / (2 : Rat)) / (1 : Rat)) : Int)
  rw [hfloor]
  rw [Int.cast_sub, Int.cast_add]
  ring

/-- Circle-fraction denominators are submultiplicative under addition.

    This is the remaining arithmetic bridge needed by the Carrier-LCM upper
    bound: after quotienting angles by full turns, product-angle denominators
    cannot introduce primes outside the lcm of the operand circle-fraction
    denominators. -/
theorem den_circleFrac_add_dvd_lcm (a b : Rat) :
    (circleFrac (a + b)).den ∣
      Nat.lcm (circleFrac a).den (circleFrac b).den := by
  rw [circleFrac_add_eq_amod_one]
  exact Nat.dvd_trans (den_amod_dvd (circleFrac a + circleFrac b) 1 (by decide))
    (den_add_dvd_lcm (circleFrac a) (circleFrac b))

/-- The circle-fraction denominator of any listed cell divides that list's
    host carrier, with the zero circle-fraction case contributing denominator
    one. -/
theorem den_circleFrac_dvd_nMin_of_mem
    (c : Cell UCNSObject) (cs : List (Cell UCNSObject)) (hc : c ∈ cs) :
    (circleFrac c.angle).den ∣ (angleDenoms cs).foldl Nat.lcm 1 := by
  by_cases hz : circleFrac c.angle = 0
  · simp [hz]
  · exact dvd_foldl_lcm _ _ ((mem_angleDenoms_iff _ cs).mpr
      ⟨c, hc, hz, rfl⟩) 1

/-- If a product cell has a nonzero emitted denominator, that denominator
    divides the lcm of the two operand carriers. This theorem contains the
    bind/map threading for the Carrier-LCM upper bound, after the isolated
    circle-fraction addition arithmetic lemma above has handled denominators. -/
theorem product_angleDenom_dvd_lcm
    (A B : UCNSObject) (d x : Nat)
    (hB : Complete B)
    (hx : x ∈ angleDenoms (multiplyFuel (d + 1) A B).cells) :
    x ∣ Nat.lcm (nMin A) (nMin B) := by
  rcases (mem_angleDenoms_iff x (multiplyFuel (d + 1) A B).cells).mp hx with
    ⟨cp, hcp, _hcp_ne, hcp_den⟩
  rcases exists_head?_of_complete B hB with ⟨b0, hb0_head⟩
  have hβ0 :
      (match B.cells.head? with
        | some c => c.angle
        | none => 0) = 0 := by
    simp [hb0_head, head_angle_zero_of_complete B hB hb0_head]
  cases A with
  | mk nda csA =>
    cases B with
    | mk ndb csB =>
      have hβ0cs :
          (match List.head? csB with
            | some c => c.angle
            | none => 0) = 0 := by
        simpa [cells] using hβ0
      simp only [cells, multiplyFuel] at hcp
      rcases List.mem_bind.mp hcp with ⟨ca, hca, hca_map⟩
      rcases List.mem_map.mp hca_map with ⟨cb, hcb, hcp_eq⟩
      subst hcp_eq
      simp only [nMin, cells]
      have hca_den_dvd :
          (circleFrac ca.angle).den ∣ (angleDenoms csA).foldl Nat.lcm 1 :=
        den_circleFrac_dvd_nMin_of_mem ca csA hca
      have hcb_den_dvd :
          (circleFrac cb.angle).den ∣ (angleDenoms csB).foldl Nat.lcm 1 :=
        den_circleFrac_dvd_nMin_of_mem cb csB hcb
      have hsum_den_dvd :
          (circleFrac (ca.angle + cb.angle)).den ∣
            Nat.lcm (circleFrac ca.angle).den (circleFrac cb.angle).den :=
        den_circleFrac_add_dvd_lcm ca.angle cb.angle
      have hlcm_dvd :
          Nat.lcm (circleFrac ca.angle).den (circleFrac cb.angle).den ∣
            Nat.lcm ((angleDenoms csA).foldl Nat.lcm 1)
              ((angleDenoms csB).foldl Nat.lcm 1) := by
        exact Nat.lcm_dvd
          (Nat.dvd_trans hca_den_dvd
            (Nat.dvd_lcm_left _ _))
          (Nat.dvd_trans hcb_den_dvd
            (Nat.dvd_lcm_right _ _))
      rw [← hcp_den]
      change
        (circleFrac
          (amod4 (ca.angle + (cb.angle -
            (match List.head? csB with
              | some c => c.angle
              | none => 0))))).den ∣
          Nat.lcm ((angleDenoms csA).foldl Nat.lcm 1)
            ((angleDenoms csB).foldl Nat.lcm 1)
      simpa [hβ0cs, circleFrac_amod4] using
        Nat.dvd_trans hsum_den_dvd hlcm_dvd

/-- Host-normalized objects keep their angle list pointwise inside the
    product's angle list (the j = 0 slice for A).

    Repaired domain: use `Complete` operands so the empty-factor counterexample is
    excluded and host-normalization is supplied by `hostNormalized_of_complete`.

    Discharged by list membership through bind/map + amod4 fixpoint under
    range normalization. -/
theorem slice_embedding_left
    (A B : UCNSObject) (d : Nat)
    (hA : Complete A) (hB : Complete B) :
    ∀ x ∈ angleDenoms A.cells,
      x ∈ angleDenoms (multiplyFuel (d + 1) A B).cells := by
  intro x hx
  rcases mem_angleDenoms_iff x A.cells |>.mp hx with ⟨ca, hca, hca_ne, hca_den⟩
  rcases exists_head?_of_complete B hB with ⟨cb, hcb_head⟩
  have hcb_mem : cb ∈ B.cells := by
    exact mem_of_head?_eq_some hcb_head
  have hcb_zero : cb.angle = 0 := head_angle_zero_of_complete B hB hcb_head
  refine (mem_angleDenoms_iff x (multiplyFuel (d + 1) A B).cells).mpr ?_
  refine ⟨
    { angle := amod4 (ca.angle + (cb.angle - (match B.cells.head? with
        | some c => c.angle
        | none => 0)))
      face := xor ca.face cb.face
      payload :=
        match ca.payload, cb.payload with
        | some p, some q => some (multiplyFuel d p q)
        | some p, none   => some p
        | none,   some q => some q
        | none,   none   => none },
    ?_, ?_, ?_⟩
  · cases A with
    | mk nda csA =>
      cases B with
      | mk ndb csB =>
        simp only [cells, multiplyFuel]
        exact List.mem_bind.mpr ⟨ca, hca, List.mem_map.mpr ⟨cb, hcb_mem, rfl⟩⟩
  · simp [hcb_head, hcb_zero, circleFrac_amod4, hca_ne]
  · simp [hcb_head, hcb_zero, circleFrac_amod4, hca_den]

/-- Symmetric embedding for B (the k = 0 slice).

    Repaired domain: use `Complete` operands so the empty-factor counterexample is
    excluded and host-normalization is supplied by `hostNormalized_of_complete`.
    Discharged by the symmetric list-membership witness construction. -/
theorem slice_embedding_right
    (A B : UCNSObject) (d : Nat)
    (hA : Complete A) (hB : Complete B) :
    ∀ x ∈ angleDenoms B.cells,
      x ∈ angleDenoms (multiplyFuel (d + 1) A B).cells := by
  intro x hx
  rcases mem_angleDenoms_iff x B.cells |>.mp hx with ⟨cb, hcb, hcb_ne, hcb_den⟩
  rcases exists_head?_of_complete A hA with ⟨ca, hca_head⟩
  rcases exists_head?_of_complete B hB with ⟨b0, hb0_head⟩
  have hca_mem : ca ∈ A.cells := by
    exact mem_of_head?_eq_some hca_head
  have hca_zero : ca.angle = 0 := head_angle_zero_of_complete A hA hca_head
  have hb0_zero : b0.angle = 0 := head_angle_zero_of_complete B hB hb0_head
  refine (mem_angleDenoms_iff x (multiplyFuel (d + 1) A B).cells).mpr ?_
  refine ⟨
    { angle := amod4 (ca.angle + (cb.angle - (match B.cells.head? with
        | some c => c.angle
        | none => 0)))
      face := xor ca.face cb.face
      payload :=
        match ca.payload, cb.payload with
        | some p, some q => some (multiplyFuel d p q)
        | some p, none   => some p
        | none,   some q => some q
        | none,   none   => none },
    ?_, ?_, ?_⟩
  · cases A with
    | mk nda csA =>
      cases B with
      | mk ndb csB =>
        simp only [cells, multiplyFuel]
        exact List.mem_bind.mpr ⟨ca, hca_mem, List.mem_map.mpr ⟨cb, hcb, rfl⟩⟩
  · simp [hb0_head, hca_zero, hb0_zero, circleFrac_amod4, hcb_ne]
  · simp [hb0_head, hca_zero, hb0_zero, circleFrac_amod4, hcb_den]

/-! ## Bound lemmas and composition -/

theorem carrier_lcm_law_lower_left
    (A B : UCNSObject) (d : Nat)
    (hA : Complete A) (hB : Complete B) :
    nMin A ∣ nMin (multiplyFuel (d + 1) A B) := by
  unfold nMin
  exact nMin_dvd_of_denoms_subset _ _ (slice_embedding_left A B d hA hB)

theorem carrier_lcm_law_lower_right
    (A B : UCNSObject) (d : Nat)
    (hA : Complete A) (hB : Complete B) :
    nMin B ∣ nMin (multiplyFuel (d + 1) A B) := by
  unfold nMin
  exact nMin_dvd_of_denoms_subset _ _ (slice_embedding_right A B d hA hB)

/-- Upper bound: every product-angle denominator divides
    L = lcm(nMin A, nMin B). -/
theorem carrier_lcm_law_upper
    (A B : UCNSObject) (d : Nat)
    (_hA : Complete A) (hB : Complete B) :
    nMin (multiplyFuel (d + 1) A B) ∣ Nat.lcm (nMin A) (nMin B) := by
  unfold nMin
  exact foldl_lcm_dvd _ _ (fun x hx =>
    product_angleDenom_dvd_lcm A B d x hB hx) 1 (Nat.one_dvd _)

/-- The Law, composed from the bounds by antisymmetry. The Carrier-LCM
    decomposition in this module is machine-checked and sorry-free. -/
theorem carrier_lcm_law'
    (A B : UCNSObject) (d : Nat)
    (hA : Complete A) (hB : Complete B) :
    nMin (multiplyFuel (d + 1) A B) = Nat.lcm (nMin A) (nMin B) := by
  apply Nat.dvd_antisymm
  · exact carrier_lcm_law_upper A B d hA hB
  · exact Nat.lcm_dvd
      (carrier_lcm_law_lower_left A B d hA hB)
      (carrier_lcm_law_lower_right A B d hA hB)

end UCNSObject
end Ucns
