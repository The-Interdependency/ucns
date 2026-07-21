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
        "StructurePolicy",
        "RetainedStructure",
        "ComparisonPolicy",
        "TraversalPolicy",
        "EvaluatorCandidate",
        "LawSuite",
        "LayerPairPolicy",
        "EnvelopePairPlan",
        "ContentAdapter",
        "ExperimentManifest",
        "CandidateDecisionPacket",
        "geometric_mean_product_candidate",
        "retained_presence_breadth_candidate",
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
        "canonical_product_character",
        "canonical_faithful_breadth",
    ):
        assert forbidden not in exported
