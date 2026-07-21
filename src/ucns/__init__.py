# === MODULE_BUILD ===
# id: foundations_public_surface
#   module_name: ucns public surface
#   module_kind: schema
#   summary: exports ratified carrier/support foundations plus option-preserving policy, envelope, and evaluator-lab infrastructure
#   owner: Erin Spencer
#   public_surface: carrier, structure, policy, envelope, and laboratory names listed in __all__
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_public_surface.py, tests/test_structure.py, tests/test_policy.py, tests/test_envelope.py, tests/test_laboratory.py
#   rollout: importable foundations and candidate-research infrastructure only
#   rollback: remove policy, envelope, and laboratory exports while preserving carrier/support floors
#   requires: directed_carrier_floor, structural_cell_support_floor, structural_choice_policy_layer, retained_structure_envelope, evaluator_candidate_laboratory
#   since: 2026-07-21
#   unresolved: canonical structural equivalence, canonical M, canonical B, complete UCNS object
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: public_surface_exposes_only_ratified_foundations
#   given: a consumer imports ucns
#   then: ratified foundations and explicit candidate infrastructure are exported without implying canonical M, B, factorization, theorem, or downstream status
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

"""UCNS foundations and option-preserving candidate infrastructure.

No complete ``UCNSObject``, canonical product character, canonical faithful-breadth
evaluator, theorem-bearing arithmetic, or downstream-consumer promise is exported.
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

__all__ = [
    "LIFTED_PERIOD",
    "STRUCTURAL_NULL",
    "VISIBLE_PERIOD",
    "CarrierPoint",
    "LiftedCarrierPoint",
    "VisibleCarrierPoint",
    "VisiblePoint",
    "carrier_from_breadth",
    "deck_translate",
    "lifted_preimages",
    "project",
    "radius_from_breadth",
    "same_lifted_position",
    "same_visible_position",
    "Carrier",
    "Cell",
    "Structure",
    "collapse",
    "make_carrier",
    "pair",
    "prune",
    "support_weight",
    "InformationLoss",
    "OccurrenceGroup",
    "PolicyRegistry",
    "Projection",
    "SetEntry",
    "StructurePolicy",
    "apply_policy",
    "ordered_sequence_policy",
    "set_policy",
    "unordered_multiset_policy",
    "ContributionStatus",
    "RetainedEnvelope",
    "RetainedLayer",
    "RetainedStructure",
    "cell_support_weight",
    "make_retained_structure",
    "project_layer",
    "CandidateComparison",
    "CandidateOutput",
    "EvaluationReport",
    "EvaluatorCandidate",
    "EvaluatorKind",
    "EvaluatorRegistry",
    "Law",
    "LawResult",
    "LawSuite",
    "Witness",
    "compare_candidates",
    "finite_nonnegative_law",
    "invariance_law",
    "null_zero_law",
    "pair_multiplicative_law",
    "same_candidate_different_reference_law",
    "same_reference_different_candidate_law",
    "sensitivity_law",
]
