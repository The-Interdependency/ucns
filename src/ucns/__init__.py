# === MODULE_BUILD ===
# id: foundations_public_surface
#   module_name: ucns public surface
#   module_kind: schema
#   summary: exports ratified foundations plus option-preserving, reproducible candidate-research infrastructure
#   owner: Erin Spencer
#   public_surface: carrier, structure, policy, envelope, comparison, traversal, laboratory, layer-pairing, experiment, candidate, and bounded downstream profile names listed in __all__
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_public_surface.py and all source-specific test modules
#   rollout: importable foundations, candidate-research infrastructure, and one explicit downstream profile only
#   rollback: remove downstream profile exports while preserving foundations and research surfaces
#   requires: directed_carrier_floor, structural_cell_support_floor, structural_choice_policy_layer, retained_structure_envelope, explicit_comparison_policy_layer, cycle_safe_traversal_policy, evaluator_candidate_laboratory, retained_layer_pairing_laboratory, reproducible_witness_experiment_pipeline, first_competing_evaluator_candidate_families
#   since: 2026-07-21
#   unresolved: canonical structural equivalence, canonical M, canonical B, complete UCNS object
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: public_surface_exposes_only_ratified_foundations
#   given: a consumer imports ucns
#   then: ratified foundations, explicit research infrastructure, and the named bounded downstream profile are exported without implying canonical M, B, factorization, theorem, or universal arithmetic
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

"""UCNS foundations and option-preserving candidate research infrastructure.

No complete ``UCNSObject``, canonical product character, canonical faithful-breadth
evaluator, theorem-bearing arithmetic, or universal downstream promise is exported.
"""

from .carrier import (
    LIFTED_PERIOD,
    STRUCTURAL_NULL,
    VISIBLE_PERIOD,
    CarrierPoint,
    LiftedCarrierPoint,
    VisibleCarrierPoint,
    VisiblePoint,
    carrier_from_breadth,
    deck_translate,
    lifted_preimages,
    project,
    radius_from_breadth,
    same_lifted_position,
    same_visible_position,
)
from .structure import (
    Carrier,
    Cell,
    Structure,
    collapse,
    make_carrier,
    pair,
    prune,
    support_weight,
)
from .policy import (
    InformationLoss,
    OccurrenceGroup,
    PolicyRegistry,
    Projection,
    SetEntry,
    StructurePolicy,
    apply_policy,
    ordered_sequence_policy,
    set_policy,
    unordered_multiset_policy,
)
from .envelope import (
    ContributionStatus,
    RetainedEnvelope,
    RetainedLayer,
    RetainedStructure,
    cell_support_weight,
    make_retained_structure,
    project_layer,
)
from .comparison import (
    ComparisonMode,
    ComparisonPolicy,
    ComparisonRegistry,
    absolute_comparison_policy,
    combined_comparison_policy,
    custom_comparison_policy,
    exact_comparison_policy,
    interval_overlap_policy,
    relative_comparison_policy,
    ulp_comparison_policy,
)
from .traversal import (
    CycleDetectedError,
    CycleMode,
    FixedPointReceipt,
    ReferenceReceipt,
    TraversalBudget,
    TraversalPolicy,
    TraversalResult,
    TruncationReceipt,
    Visit,
    traverse,
)
from .laboratory import (
    CandidateComparison,
    CandidateOutput,
    EvaluationReport,
    EvaluatorCandidate,
    EvaluatorKind,
    EvaluatorRegistry,
    Law,
    LawResult,
    LawSuite,
    Witness,
    compare_candidates,
    finite_nonnegative_law,
    invariance_law,
    null_zero_law,
    pair_multiplicative_law,
    same_candidate_different_reference_law,
    same_reference_different_candidate_law,
    sensitivity_law,
)
from .layer_pairing import (
    EnvelopePairPlan,
    EnvelopePairResult,
    LayerPairDecision,
    LayerPairMode,
    LayerPairPolicy,
    LayerPairProjection,
    LayerPairRegistry,
    LayerPairRule,
    LayerRef,
    UnmatchedLayerMode,
    cartesian_layer_policy,
    concatenate_layer_policy,
    custom_layer_pair_policy,
    exclude_layer_policy,
    keep_sides_layer_policy,
    pair_retained,
    positional_zip_layer_policy,
    select_left_layer_policy,
    select_right_layer_policy,
)
from .experiments import (
    AdapterRegistry,
    AuthorshipRecord,
    CandidateDecisionPacket,
    CandidateIdentity,
    ContentAdapter,
    CorpusPartition,
    Counterexample,
    ExperimentManifest,
    ExperimentResult,
    HoldoutReport,
    LawSuiteDigest,
    MetamorphicCase,
    MutationCase,
    NamedTransform,
    PolicyDigest,
    ReproductionCheck,
    SubjectRecord,
    WitnessCase,
    WitnessCorpus,
    WitnessOrigin,
    build_candidate_decision_packet,
    bytes_content_adapter,
    check_reproduction,
    comparison_policy_digest,
    generate_metamorphic_cases,
    generate_mutation_cases,
    greedy_minimize_counterexample,
    json_content_adapter,
    text_content_adapter,
    traversal_policy_digest,
)
from .candidates import (
    CandidateScopeError,
    cell_detail_breadth_candidate,
    cell_log_support_breadth_candidate,
    exact_evidence_equivalence_candidate,
    geometric_mean_product_candidate,
    layer_scoped_equivalence_candidate,
    maximum_support_product_candidate,
    minimum_support_product_candidate,
    policy_projection_equivalence_candidate,
    retained_presence_breadth_candidate,
)
from .bridge import (
    BRIDGE_SCHEMA_ID,
    BRIDGE_SCHEMA_VERSION,
    PRODUCER_EPOCH,
    PROFILE_ID,
    PROFILE_VERSION,
    BridgeCell,
    BridgeValidationError,
    EdcmMetapatBridgeRecord,
    InformationLossRecord,
    RetainedLayerDigest,
)
from .profiles import (
    PROFILE_OPTIONS,
    EdcmMetapatOrderedOccurrenceProfile,
    ProfileBoundStructure,
)

__all__ = [
    "LIFTED_PERIOD", "STRUCTURAL_NULL", "VISIBLE_PERIOD", "CarrierPoint",
    "LiftedCarrierPoint", "VisibleCarrierPoint", "VisiblePoint",
    "carrier_from_breadth", "deck_translate", "lifted_preimages", "project",
    "radius_from_breadth", "same_lifted_position", "same_visible_position",
    "Carrier", "Cell", "Structure", "collapse", "make_carrier", "pair",
    "prune", "support_weight", "InformationLoss", "OccurrenceGroup",
    "PolicyRegistry", "Projection", "SetEntry", "StructurePolicy",
    "apply_policy", "ordered_sequence_policy", "set_policy",
    "unordered_multiset_policy", "ContributionStatus", "RetainedEnvelope",
    "RetainedLayer", "RetainedStructure", "cell_support_weight",
    "make_retained_structure", "project_layer", "ComparisonMode",
    "ComparisonPolicy", "ComparisonRegistry", "absolute_comparison_policy",
    "combined_comparison_policy", "custom_comparison_policy",
    "exact_comparison_policy", "interval_overlap_policy",
    "relative_comparison_policy", "ulp_comparison_policy",
    "CycleDetectedError", "CycleMode", "FixedPointReceipt",
    "ReferenceReceipt", "TraversalBudget", "TraversalPolicy",
    "TraversalResult", "TruncationReceipt", "Visit", "traverse",
    "CandidateComparison", "CandidateOutput", "EvaluationReport",
    "EvaluatorCandidate", "EvaluatorKind", "EvaluatorRegistry", "Law",
    "LawResult", "LawSuite", "Witness", "compare_candidates",
    "finite_nonnegative_law", "invariance_law", "null_zero_law",
    "pair_multiplicative_law", "same_candidate_different_reference_law",
    "same_reference_different_candidate_law", "sensitivity_law",
    "EnvelopePairPlan", "EnvelopePairResult", "LayerPairDecision",
    "LayerPairMode", "LayerPairPolicy", "LayerPairProjection",
    "LayerPairRegistry", "LayerPairRule", "LayerRef", "UnmatchedLayerMode",
    "cartesian_layer_policy", "concatenate_layer_policy",
    "custom_layer_pair_policy", "exclude_layer_policy",
    "keep_sides_layer_policy", "pair_retained",
    "positional_zip_layer_policy", "select_left_layer_policy",
    "select_right_layer_policy", "AdapterRegistry", "AuthorshipRecord",
    "CandidateDecisionPacket", "CandidateIdentity", "ContentAdapter",
    "CorpusPartition", "Counterexample", "ExperimentManifest",
    "ExperimentResult", "HoldoutReport", "LawSuiteDigest",
    "MetamorphicCase", "MutationCase", "NamedTransform", "PolicyDigest",
    "ReproductionCheck", "SubjectRecord", "WitnessCase", "WitnessCorpus",
    "WitnessOrigin", "build_candidate_decision_packet",
    "bytes_content_adapter", "check_reproduction",
    "comparison_policy_digest", "generate_metamorphic_cases",
    "generate_mutation_cases", "greedy_minimize_counterexample",
    "json_content_adapter", "text_content_adapter",
    "traversal_policy_digest", "CandidateScopeError",
    "cell_detail_breadth_candidate", "cell_log_support_breadth_candidate",
    "exact_evidence_equivalence_candidate",
    "geometric_mean_product_candidate", "layer_scoped_equivalence_candidate",
    "maximum_support_product_candidate", "minimum_support_product_candidate",
    "policy_projection_equivalence_candidate",
    "retained_presence_breadth_candidate",
    "BRIDGE_SCHEMA_ID", "BRIDGE_SCHEMA_VERSION", "PRODUCER_EPOCH",
    "PROFILE_ID", "PROFILE_VERSION", "BridgeCell", "BridgeValidationError",
    "EdcmMetapatBridgeRecord", "InformationLossRecord",
    "RetainedLayerDigest", "PROFILE_OPTIONS",
    "EdcmMetapatOrderedOccurrenceProfile", "ProfileBoundStructure",
]
