# === MODULE_BUILD ===
# id: product_character_candidates
#   module_name: product_character_candidates
#   module_kind: instrument
#   summary: registers a concrete product-of-support candidate for M together with the two structural separation witnesses against W
#   owner: Erin Spencer
#   public_surface: product_of_supports, PRODUCT_OF_SUPPORTS_CANDIDATE, same_W_different_M_witness, same_M_different_W_witness, separation_suite_for_product_of_supports
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_product_character_candidates.py
#   rollout: candidate only; does not promote a canonical M
#   rollback: remove this module and its test
#   requires: structural_cell_support_floor, evaluator_candidate_laboratory
#   since: 2026-07-21
#   unresolved: whether product-of-supports is the eventual canonical M; richer combinatorial grades; receipt contribution policy
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: product_of_supports_is_multiplicative
#   given: two non-null carriers
#   then: the product-of-supports candidate on their Cartesian pair equals the product of the candidate values
#   class: correctness
#   since: 2026-07-21
#
# id: product_of_supports_separates_from_W
#   given: the two structural partition witnesses
#   then: same total support can yield different product-of-supports values, and identical product-of-supports values can arise from different total support
#   class: doctrine
#   since: 2026-07-21
#
# id: product_of_supports_null_is_zero
#   given: Structural Null
#   then: the candidate returns exactly 0
#   class: doctrine
#   since: 2026-07-21
# === END CONTRACTS ===

"""Concrete product-character candidate derived from cell supports.

This is a laboratory candidate, not a promoted canonical evaluator.
It demonstrates that a multiplicative M independent of the sum W exists
and can be witnessed with pure structural partitions of support mass.
"""

from __future__ import annotations

from .carrier import STRUCTURAL_NULL
from .laboratory import (
    EvaluatorCandidate,
    EvaluatorKind,
    LawSuite,
    Witness,
    finite_nonnegative_law,
    null_zero_law,
    pair_multiplicative_law,
    same_candidate_different_reference_law,
    same_reference_different_candidate_law,
)
from .structure import Carrier, Cell, Structure, pair, support_weight


def product_of_supports(obj: Structure) -> float:
    """Primary combinatorial product character: product of present-cell µ values.

    - Structural Null maps to 0.
    - Any collection of pure unit-support cells yields 1.
    - Different partitions of the same total support yield different values
      (the required separation from W).
    """
    if obj is STRUCTURAL_NULL:
        return 0.0
    if not isinstance(obj, Carrier):
        raise TypeError("product_of_supports expects STRUCTURAL_NULL or Carrier")
    prod = 1.0
    for cell in obj.cells:
        s = cell.support
        if s > 0.0:
            prod *= s
    return prod


PRODUCT_OF_SUPPORTS_CANDIDATE = EvaluatorCandidate(
    name="product-of-supports",
    kind=EvaluatorKind.PRODUCT_CHARACTER,
    evaluator=product_of_supports,
    notes=(
        "Derived solely from the multiset of cell supports. "
        "No free scalar grade. Neutral value 1 on any pure unit-support collection."
    ),
    version="0.1.0-foundations",
)


def same_W_different_M_witness() -> Witness:
    """Two unit cells (W=2, M=1) versus one cell µ=2 (W=2, M=2)."""
    left = Carrier((Cell(coordinate="u1", mu=1.0), Cell(coordinate="u2", mu=1.0)))
    right = Carrier((Cell(coordinate="double", mu=2.0),))
    return Witness(
        name="same-W-different-product",
        subjects=(left, right),
        expectation="W equal while product-of-supports differs",
    )


def same_M_different_W_witness() -> Witness:
    """One unit cell versus three unit cells (both M=1, different W)."""
    left = Carrier((Cell(coordinate="single", mu=1.0),))
    right = Carrier(
        (
            Cell(coordinate="a", mu=1.0),
            Cell(coordinate="b", mu=1.0),
            Cell(coordinate="c", mu=1.0),
        )
    )
    return Witness(
        name="same-product-different-W",
        subjects=(left, right),
        expectation="product-of-supports equal while W differs",
    )


def separation_suite_for_product_of_supports() -> LawSuite:
    """Law suite that the product-of-supports candidate must pass against W."""
    left, right = same_W_different_M_witness().subjects
    return LawSuite(
        name="product-of-supports-separation",
        laws=(
            null_zero_law(),
            finite_nonnegative_law(
                (STRUCTURAL_NULL, left, right, pair(left, right))
            ),
            pair_multiplicative_law(((left, right),)),
            same_reference_different_candidate_law(
                support_weight,
                (same_W_different_M_witness(),),
            ),
            same_candidate_different_reference_law(
                support_weight,
                (same_M_different_W_witness(),),
            ),
        ),
    )
