/-
  Ucns/CarrierLcm.lean — discharge skeleton for the Carrier-LCM Law.

  Mirrors the prose proof in docs/carrier-support-pruning.md §2:

    upper bound:  every product-angle denominator divides L = lcm(nMin A, nMin B)
    lower bound:  each factor's angles embed verbatim in the product (j=0 / k=0
                  slices), so nMin A ∣ nMin P and nMin B ∣ nMin P
    conclusion:   Nat.dvd_antisymm.

  DISCHARGE STATE — read before citing:
  - The lcm fold engine (`dvd_foldl_lcm`, `foldl_lcm_dvd`, `foldl_lcm_pos`)
    and the composition layer (`carrier_lcm_law'` from the two bound
    lemmas) are targeted SORRY-FREE.
  - The analytic leaves (`denEngine` group: amod/denominator behavior over
    Rat; `embedding` group: slice membership under host normalization)
    remain `sorry`-stubbed with precise hypotheses. A `sorry`-backed
    lemma confers NO DEFENDED status (formal/README.md).
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
--   unresolved: denominator-of-sum leaf, amod-denominator leaf, slice-embedding leaf
-- === END MODULE_BUILD ===

import Ucns.Core
import Std.Data.Nat.Gcd
import Std.Data.List.Lemmas

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

/-! ## Analytic leaves (sorry-stubbed, precise hypotheses) -/

/-- amod never enlarges a denominator. LEAF: Rat arithmetic. -/
theorem den_amod_dvd (a : Rat) (n : Nat) (hn : 0 < n) :
    (amod a n).den ∣ a.den := by
  sorry

/-- The denominator of a sum divides the lcm of the denominators.
    LEAF: Rat arithmetic. -/
theorem den_add_dvd_lcm (a b : Rat) :
    (a + b).den ∣ Nat.lcm a.den b.den := by
  sorry

/-- Host-normalized objects keep their angle list pointwise inside the
    product's angle list (the j = 0 slice for A).
    LEAF: list membership through bind/map + amod4 fixpoint under
    range normalization. -/
theorem slice_embedding_left
    (A B : UCNSObject) (d : Nat)
    (hA : HostNormalized A) (hB : HostNormalized B) :
    ∀ x ∈ angleDenoms A.cells,
      x ∈ angleDenoms (multiplyFuel (d + 1) A B).cells := by
  sorry

/-- Symmetric embedding for B (the k = 0 slice). LEAF. -/
theorem slice_embedding_right
    (A B : UCNSObject) (d : Nat)
    (hA : HostNormalized A) (hB : HostNormalized B) :
    ∀ x ∈ angleDenoms B.cells,
      x ∈ angleDenoms (multiplyFuel (d + 1) A B).cells := by
  sorry

/-! ## Bound lemmas and composition (sorry-free modulo leaves) -/

theorem carrier_lcm_law_lower_left
    (A B : UCNSObject) (d : Nat)
    (hA : HostNormalized A) (hB : HostNormalized B) :
    nMin A ∣ nMin (multiplyFuel (d + 1) A B) := by
  unfold nMin
  exact nMin_dvd_of_denoms_subset _ _ (slice_embedding_left A B d hA hB)

theorem carrier_lcm_law_lower_right
    (A B : UCNSObject) (d : Nat)
    (hA : HostNormalized A) (hB : HostNormalized B) :
    nMin B ∣ nMin (multiplyFuel (d + 1) A B) := by
  unfold nMin
  exact nMin_dvd_of_denoms_subset _ _ (slice_embedding_right A B d hA hB)

/-- Upper bound: every product-angle denominator divides
    L = lcm(nMin A, nMin B). LEAF GROUP: den_add_dvd_lcm + den_amod_dvd
    threaded through the bind/map structure. -/
theorem carrier_lcm_law_upper
    (A B : UCNSObject) (d : Nat)
    (hA : HostNormalized A) (hB : HostNormalized B) :
    nMin (multiplyFuel (d + 1) A B) ∣ Nat.lcm (nMin A) (nMin B) := by
  sorry

/-- The Law, composed from the bounds by antisymmetry. The composition
    is machine-checked; status is inherited from the leaves above. -/
theorem carrier_lcm_law'
    (A B : UCNSObject) (d : Nat)
    (hA : HostNormalized A) (hB : HostNormalized B) :
    nMin (multiplyFuel (d + 1) A B) = Nat.lcm (nMin A) (nMin B) := by
  apply Nat.dvd_antisymm
  · exact carrier_lcm_law_upper A B d hA hB
  · exact Nat.lcm_dvd
      (carrier_lcm_law_lower_left A B d hA hB)
      (carrier_lcm_law_lower_right A B d hA hB)

end UCNSObject
end Ucns
