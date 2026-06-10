/-
  Ucns.TheoremN
  =============

  Lean 4 scaffold for the UCNS Theorem N family.

  SOURCE OF TRUTH FOR THE CLAIMS: ../../ucns-theorem-n.md

  STATUS: FRONTIER / awaiting external formal review.

  Every statement in this file is closed with `sorry`. A `sorry` is an
  UNVERIFIED HOLE: Lean accepts the file, but nothing here is proven. These
  are statement stubs, not proofs. Per the proof-status non-transfer
  discipline (see README.md), a `sorry`-backed statement confers NO DEFENDED
  status to any consumer repository.

  The abstract objects below (UCNSObject, multiply, catalogues, the search
  procedure factor_search_v08) are modelled as opaque placeholders so the
  statements can be written down. Faithful definitions are future work and
  are themselves part of what external formal review must check.
-/

import Ucns.Core

namespace Ucns

open UCNSObject

/-! The placeholder `opaque UCNSObject` of the original scaffold is replaced
    by the faithful definitions in `Ucns/Core.lean`. `multiply` and `depth`
    below are the real (fuel-indexed) operations; `width`,
    `ContainsPayloads`, and `FindsFactorization` remain modelling
    predicates pending the formalization of the search procedure itself —
    they are now definitions/opaques over the REAL object type. -/

/-- The depth-agnostic product, at fuel sufficient for both operands. -/
def multiply (A B : UCNSObject) : UCNSObject :=
  multiplyFuel (Nat.max (depth A) (depth B)) A B

/-- Number of top-level `A_plus` cells of an object (`|A.A_plus|`). -/
def width (x : UCNSObject) : Nat := x.cells.length

/-- A catalogue `C`: a candidate set of payloads (`UCNSObject | None`),
    modelled as a list of objects (the unit payload is implicit). -/
abbrev Catalogue : Type := List UCNSObject

/-- `ContainsPayloads C X` holds when the catalogue `C` contains every payload
    appearing recursively in `X` (including the identity). Single hypothesis
    of Theorem N. Still a modelling predicate over the real type. -/
opaque ContainsPayloads : Catalogue → UCNSObject → Prop

/-- `FindsFactorization P C` holds when `factor_search_v08(P, C)` returns a
    pair `(A', B')` with `multiply A' B' = P`. Models the success of the
    depth-agnostic search procedure; the procedure itself is not yet
    formalized. -/
opaque FindsFactorization : UCNSObject → Catalogue → Prop

/--
  **Depth-1 restricted completeness (stub).**

  Informal claim: for depth-1 factors `A`, `B` whose (atomic) payloads are all
  present in the catalogue `C`, the search procedure recovers a factorization of
  `P = multiply A B`. This is the base/restricted case underneath the depth-2
  oracle result and Theorem N (cf. `ucns-theorem-n.md` §4).

  STUB: proves nothing — closed by `sorry`.
-/
theorem depth1_restricted_completeness
    (A B : UCNSObject) (C : Catalogue)
    (hA : depth A ≤ 1) (hB : depth B ≤ 1)
    (hwA : 1 ≤ width A) (hwB : 1 ≤ width B)
    (hCA : ContainsPayloads C A) (hCB : ContainsPayloads C B) :
    FindsFactorization (multiply A B) C := by
  sorry

/--
  **Lemma 7 — depth-2 oracle completeness (stub).**

  Informal claim (`ucns-theorem-n.md` §4.1): for `A, B` in the depth-2 oracle
  class `D'_oracle` (depth ≤ 2), every payload of `A` and `B` is a depth-1
  oracle atom and so lies in the generated payload catalogue `C`; the search
  procedure is therefore complete. Presented in §2/§4 as an instance of
  Theorem N rather than an independent result.

  STUB: proves nothing — closed by `sorry`.
-/
theorem lemma7_depth2_oracle_completeness
    (A B : UCNSObject) (C : Catalogue)
    (hA : depth A ≤ 2) (hB : depth B ≤ 2)
    (hwA : 1 ≤ width A) (hwB : 1 ≤ width B)
    (hCA : ContainsPayloads C A) (hCB : ContainsPayloads C B) :
    FindsFactorization (multiply A B) C := by
  sorry

/--
  **Theorem N — catalogue-sufficient factorization (stub).**

  Informal claim (`ucns-theorem-n.md` §2): let `A`, `B` be UCNS objects with
  `|A.A_plus|, |B.A_plus| ≥ 1`, and let `C` be a catalogue containing every
  payload appearing recursively in `A` or `B` (including the identity). Define
  `P = multiply A B`. Then `factor_search_v08(P, C)` returns `(A', B')` with
  `multiply A' B' = P`. There is NO depth parameter and NO oracle-class
  predicate; the only hypothesis is that the catalogue contains the necessary
  payloads. Lemma 7 and the depth-1 case above are instances.

  STUB: proves nothing — closed by `sorry`.
-/
theorem theoremN_catalogue_sufficient_completeness
    (A B : UCNSObject) (C : Catalogue)
    (hwA : 1 ≤ width A) (hwB : 1 ≤ width B)
    (hCA : ContainsPayloads C A) (hCB : ContainsPayloads C B) :
    FindsFactorization (multiply A B) C := by
  sorry

end Ucns
