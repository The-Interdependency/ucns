# === CHECKS ===
# id: check_public_surface_is_bounded
#   proves: public_surface_exposes_only_ratified_foundations
#   call: self::test_public_surface_is_bounded
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import ucns


def test_public_surface_is_bounded() -> None:
    exported = set(ucns.__all__)
    for expected in (
        "LiftedCarrierPoint",
        "STRUCTURAL_NULL",
        "Cell",
        "Carrier",
        "support_weight",
        "pair",
        "prune",
        "collapse",
        "StructurePolicy",
        "PolicyRegistry",
        "Projection",
        "RetainedLayer",
        "RetainedStructure",
        "EvaluatorCandidate",
        "EvaluatorRegistry",
        "LawSuite",
        "compare_candidates",
    ):
        assert expected in exported

    for forbidden in (
        "UCNSObject",
        "product_character",
        "faithful_breadth",
        "multiply",
        "factor",
        "TheoremN",
        "default_evaluator",
        "canonical_policy",
    ):
        assert forbidden not in exported
