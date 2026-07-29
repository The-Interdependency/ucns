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
        "EdcmMotionObservation",
        "EdcmCompletionTrace",
        "HmmmBoundary",
        "ScalarProjection",
        "CarrierExperimentReport",
        "CarrierRelationship",
        "FalsifierVerdict",
        "run_v05_carrier_experiment",
        "DirectMobiusCandidateReport",
        "NativeMobiusState",
        "StructuralNullIdentity",
        "run_v06_direct_mobius_experiment",
        "RootLoopChartReport",
        "RootLoopCoverChartState",
        "run_v07_root_loop_chart_experiment",
        "FramedMobiusStripState",
        "TransverseEnvelopeState",
        "TransverseEnvelopeReport",
        "TransverseCarrierCollisionWitness",
        "run_v09_transverse_envelope_experiment",
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
        "TransverseCoverChartState",
        "TransverseStripReport",
        "run_v08_transverse_strip_experiment",
    ):
        assert forbidden not in exported
