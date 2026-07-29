import { defineMsdmdCollection } from "./.agents/skills/msdmd/collection";

export default defineMsdmdCollection({
  "declarations": [
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a consumer imports ucns",
        "since": "2026-07-21",
        "then": "ratified foundations, explicit research infrastructure, and the named bounded downstream profile are exported without implying canonical M, B, factorization, theorem, or universal arithmetic"
      },
      "file": "src/ucns/__init__.py",
      "id": "public_surface_exposes_only_ratified_foundations"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "schema",
        "module_name": "ucns public surface",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "option decisions, EDCM observation and completion-motion evidence, v0.5 carrier experiment, v0.6 native direct-Mobius candidate, carrier, structure, policy, envelope, comparison, traversal, laboratory, layer-pairing, experiment, candidate, and bounded downstream profile names listed in __all__",
        "requires": "ucns_option_decision_registry, edcm_word_gonol_profile, edcm_completion_motion_evidence, edcm_mobius_carrier_experiment, edcm_native_direct_mobius_candidate, directed_carrier_floor, structural_cell_support_floor, structural_choice_policy_layer, retained_structure_envelope, explicit_comparison_policy_layer, cycle_safe_traversal_policy, evaluator_candidate_laboratory, retained_layer_pairing_laboratory, reproducible_witness_experiment_pipeline, first_competing_evaluator_candidate_families",
        "rollback": "remove completion-motion and downstream profile exports while preserving foundations and research surfaces",
        "rollout": "importable decisions, exact EDCM word-gonol observation profile, trajectory-first completion-motion evidence, candidate-neutral v0.5 carrier experiment, nonselecting v0.6 direct-Mobius candidate, compatibility profile, and research infrastructure",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "exports the UCNS decision registry, EDCM word-gonol and completion-motion evidence profiles, current foundations, and reproducible candidate-research infrastructure",
        "tests": "tests/test_public_surface.py and all source-specific test modules",
        "unresolved": "element-assignment law, Mobius coordinates beyond the framed root loop, circle-epicycle-disk-sphere transitions, higher-gonol composition, non-SPACE out-of-alphabet treatment, canonical structural equivalence, canonical M, canonical B, complete UCNS object",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/__init__.py",
      "id": "foundations_public_surface"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "bridge cells, occurrence identities, options, retained layers, operator history, information loss, or source commit differ",
        "since": "2026-07-23",
        "then": "stable identity differs or parsing fails because identity binds the complete ordered bridge payload"
      },
      "file": "src/ucns/bridge.py",
      "id": "bridge_identity_binds_order_profile_and_content"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a downstream bridge record is constructed or parsed",
        "since": "2026-07-23",
        "then": "only the exact post-reset schema, producer epoch, profile identity, fixed false transfer fields, complete field set, and deterministic JSON values are accepted"
      },
      "file": "src/ucns/bridge.py",
      "id": "post_reset_bridge_is_exact_and_fail_closed"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "any bridge record claims theorem, EDCM measurement, or METAPAT validity transfer",
        "since": "2026-07-23",
        "then": "construction and parsing fail closed"
      },
      "file": "src/ucns/bridge.py",
      "id": "validity_transfer_is_forbidden"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_value, _canonical_bytes, _digest",
        "module_kind": "schema",
        "module_name": "bridge",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "EdcmMetapatBridgeRecord, BridgeCell, RetainedLayerDigest, InformationLossRecord, BridgeValidationError",
        "rollback": "remove bridge exports and module without changing current carrier foundations",
        "rollout": "draft bridge only; consumers remain suspended until merge and package validation",
        "since": "2026-07-23",
        "storage_boundary": "serialized bridge bytes only",
        "summary": "provides one immutable validated post-reset bridge record for the ordered-occurrence EDCM/METAPAT profile",
        "tests": "tests/test_profile_boundary.py",
        "unresolved": "downstream consumer pinning and installed-wheel validation",
        "user_data_boundary": "caller-supplied payloads must be deterministic JSON values"
      },
      "file": "src/ucns/bridge.py",
      "id": "edcm_metapat_post_reset_bridge"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an initial equivalence, M, or B candidate is constructed",
        "since": "2026-07-21",
        "then": "it remains an EvaluatorCandidate and exposes no canonical or winner status"
      },
      "file": "src/ucns/candidates.py",
      "id": "candidate_constructors_do_not_promote_canon"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a cell-only M or B candidate receives retained evidence without a cell carrier",
        "since": "2026-07-21",
        "then": "evaluation raises CandidateScopeError rather than treating unmeasured layers as zero distinction"
      },
      "file": "src/ucns/candidates.py",
      "id": "cell_only_candidates_fail_outside_scope"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "multiple equivalence, product-character, or faithful-breadth candidates are constructed",
        "since": "2026-07-21",
        "then": "each has explicit version, code reference, scope, and policy dependencies and none is selected as canonical"
      },
      "file": "src/ucns/candidates.py",
      "id": "first_candidate_families_coexist_without_selection"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "positive-support carriers are paired by the established Cartesian law",
        "since": "2026-07-21",
        "then": "geometric-mean, maximum-support, and minimum-support candidates satisfy their declared multiplicativity fixtures"
      },
      "file": "src/ucns/candidates.py",
      "id": "initial_product_candidates_multiply_under_actual_pairing"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_digest, _carrier, _cell_supports",
        "module_kind": "instrument",
        "module_name": "candidates",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "CandidateScopeError, exact_evidence_equivalence_candidate, policy_projection_equivalence_candidate, layer_scoped_equivalence_candidate, geometric_mean_product_candidate, maximum_support_product_candidate, minimum_support_product_candidate, cell_log_support_breadth_candidate, cell_detail_breadth_candidate, retained_presence_breadth_candidate",
        "requires": "evaluator_candidate_laboratory, reproducible_witness_experiment_pipeline",
        "rollback": "remove candidate constructors; laboratory and evidence remain",
        "rollout": "explicit candidate families only; no evaluator is canonical",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "supplies explicit noncanonical equivalence, product-character, and faithful-breadth candidate families for laboratory pressure",
        "tests": "tests/test_candidates.py",
        "unresolved": "canonical equivalence, canonical M, canonical B",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/candidates.py",
      "id": "first_competing_evaluator_candidate_families"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a non-null carrier retains structure while an external payload value is numerically zero",
        "since": "2026-07-21",
        "then": "carrier identity remains non-null because payload algebra is outside the carrier floor"
      },
      "file": "src/ucns/carrier.py",
      "id": "algebraic_zero_is_not_structural_null"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "any finite angular coordinate on a non-null carrier",
        "since": "2026-07-21",
        "then": "the coordinate is normalized modulo four pi and returns only after two visible laps"
      },
      "file": "src/ucns/carrier.py",
      "id": "lifted_period_is_720_degrees"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "a non-null lifted carrier point is constructed",
        "since": "2026-07-21",
        "then": "breadth is finite and strictly positive and radius lies strictly between zero and one"
      },
      "file": "src/ucns/carrier.py",
      "id": "non_null_carrier_has_positive_breadth"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a non-null lifted carrier point translated by two pi",
        "since": "2026-07-21",
        "then": "its visible projection is unchanged while its lifted representative is distinct"
      },
      "file": "src/ucns/carrier.py",
      "id": "one_visible_lap_is_deck_translation_only"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the carrier is constructed with zero faithful breadth",
        "since": "2026-07-21",
        "then": "the result is the unique Structural Null and exposes no angular coordinate"
      },
      "file": "src/ucns/carrier.py",
      "id": "structural_null_is_unique_and_coordinate_free"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a 360-degree deck translation",
        "since": "2026-07-21",
        "then": "no negation, reflection, parity, chirality, frame inversion, or payload operation is inferred by the carrier API"
      },
      "file": "src/ucns/carrier.py",
      "id": "topology_does_not_invent_orientation_algebra"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a non-null lifted carrier point translated twice by two pi",
        "since": "2026-07-21",
        "then": "the original lifted representative is restored"
      },
      "file": "src/ucns/carrier.py",
      "id": "two_visible_laps_complete_return"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a non-null lifted carrier point",
        "since": "2026-07-21",
        "then": "projection is normalized modulo two pi and has exactly two lifted representatives"
      },
      "file": "src/ucns/carrier.py",
      "id": "visible_projection_is_360_degrees"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_StructuralNull, _normalize_angle",
        "module_kind": "schema",
        "module_name": "carrier",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "STRUCTURAL_NULL, LiftedCarrierPoint, VisibleCarrierPoint, radius_from_breadth, carrier_from_breadth, project, deck_translate, lifted_preimages, same_lifted_position, same_visible_position",
        "requires": "canonical_chapter_one",
        "rollback": "remove public exports and this module",
        "rollout": "importable prototype only; no arithmetic or theorem promotion",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "represents the directed twofold branched angular carrier without defining full UCNS object semantics",
        "tests": "tests/test_carrier.py",
        "unresolved": "canonical evaluators for mu, W, M, and B; complete UCNS object schema",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/carrier.py",
      "id": "directed_carrier_floor"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a comparison policy name is already registered",
        "since": "2026-07-21",
        "then": "replacement fails unless replace is explicitly true"
      },
      "file": "src/ucns/comparison.py",
      "id": "comparison_policy_replacement_is_explicit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "exact, relative, absolute, ULP, interval, or custom policies are registered",
        "since": "2026-07-21",
        "then": "every policy remains independently addressable and no default winner is appointed"
      },
      "file": "src/ucns/comparison.py",
      "id": "comparison_registry_preserves_multiple_policies"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a custom comparison implementation is constructed or pinned in an experiment",
        "since": "2026-07-21",
        "then": "a nonempty code reference distinguishes the implementation independently of name, version, and parameters"
      },
      "file": "src/ucns/comparison.py",
      "id": "custom_comparison_identity_is_explicit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "candidate outputs or law evidence are compared",
        "since": "2026-07-21",
        "then": "an explicit named ComparisonPolicy performs the comparison and no hidden tolerance is selected"
      },
      "file": "src/ucns/comparison.py",
      "id": "evaluator_equality_requires_explicit_comparison_policy"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_numeric_pair, _ordered_float",
        "module_kind": "instrument",
        "module_name": "comparison",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "ComparisonMode, ComparisonPolicy, ComparisonRegistry, exact_comparison_policy, absolute_comparison_policy, relative_comparison_policy, combined_comparison_policy, ulp_comparison_policy, interval_overlap_policy, custom_comparison_policy",
        "requires": "structural_choice_policy_layer",
        "rollback": "remove comparison exports and restore no implicit tolerance",
        "rollout": "explicit candidate-research comparison infrastructure only",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "defines versioned comparison policies with explicit implementation identity so evaluator laws never rely on hidden tolerance or callable inference",
        "tests": "tests/test_comparison.py, tests/test_laboratory.py, tests/test_experiments.py",
        "unresolved": "canonical numerical comparison policy",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/comparison.py",
      "id": "explicit_comparison_policy_layer"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the v0.6 direct candidate enters the v0.5 carrier experiment",
        "since": "2026-07-29",
        "then": "C1 motion and independence evidence is evaluated without a directed-cover dependency, selected carrier, completion receipt, chart claim, incompatibility claim, or consumer activation"
      },
      "file": "src/ucns/direct_mobius.py",
      "id": "direct_mobius_candidate_is_independent_and_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the v0.6 initiation packet is built",
        "since": "2026-07-29",
        "then": "every word gonol has exactly one pre-state Structural Null cause and one framed root-loop post-state linked to its exact source start"
      },
      "file": "src/ucns/direct_mobius.py",
      "id": "direct_mobius_initiation_is_causal_and_cardinality_exact"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "a framed root-loop state advances under the native quotient law",
        "since": "2026-07-29",
        "then": "one turn preserves visible phase and reverses the retained local frame, two turns restore complete state, and negative motion is an exact inverse"
      },
      "file": "src/ucns/direct_mobius.py",
      "id": "direct_mobius_native_motion_has_360_change_720_return_and_inverse"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "exact source A SPACE SPACE B is adapted",
        "since": "2026-07-29",
        "then": "both SPACE occurrences remain distinct manifestations of the singular origin and the immediately preceding second occurrence causes B initiation"
      },
      "file": "src/ucns/direct_mobius.py",
      "id": "direct_mobius_repeated_space_preserves_singular_origin_and_occurrences"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the complete v0.6 report is produced",
        "since": "2026-07-29",
        "then": "arbitrary element assignment, transverse coordinates, scoped completion, higher geometry, higher-gonol composition, and the C1-C2 relationship remain explicit hmmm constraints"
      },
      "file": "src/ucns/direct_mobius.py",
      "id": "direct_mobius_report_retains_unresolved_frontier"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the v0.6 minimum witness packet is adapted to native Mobius initiation evidence",
        "since": "2026-07-29",
        "then": "every exact SPACE and turn-boundary manifestation remains distinct while sharing one typed Structural Null carrier origin that is not numeric zero, absence, or completion"
      },
      "file": "src/ucns/direct_mobius.py",
      "id": "direct_mobius_structural_null_is_typed_and_source_preserving"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "validation helpers and bounded C1 falsifier-result adapters",
        "module_kind": "experiment",
        "module_name": "direct_mobius",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "StructuralNullIdentity, StructuralNullManifestation, StructuralNullKind, NativeMobiusFrame, NativeMobiusState, MobiusInitiationEvent, NativeMobiusInitiationPacket, DirectMobiusCandidateReport, build_native_mobius_initiation_packet, native_direct_mobius_trace, run_v06_direct_mobius_experiment",
        "requires": "edcm_word_gonol_profile, edcm_mobius_carrier_experiment",
        "rollback": "remove this module, its exports, tests, and v0.6 candidate document while retaining the v0.5 comparison harness",
        "rollout": "explicit UCNS-only v0.6 experiment candidate; no carrier selection, completion, EDCM activation, or METAPAT activation",
        "since": "2026-07-29",
        "storage_boundary": "none",
        "summary": "supplies a native framed Mobius root-loop candidate with Structural Null initiation and exact rational-turn motion evidence",
        "tests": "tests/test_direct_mobius.py",
        "unresolved": "arbitrary element assignment, transverse carrier coordinates, chart map or incompatibility proof, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions",
        "user_data_boundary": "exact source witnesses and every SPACE manifestation remain linked without normalization"
      },
      "file": "src/ucns/direct_mobius.py",
      "id": "edcm_native_direct_mobius_candidate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a non-SPACE corpus code point has no assignment in the exact 157-position carrier",
        "since": "2026-07-25",
        "then": "it remains in position as out-of-alphabet evidence and is never dropped, replaced, coerced, or used to silently reject the turn"
      },
      "file": "src/ucns/edcm.py",
      "id": "edcm_alphabet_failure_is_positive_evidence"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the EDCM token alphabet is imported",
        "since": "2026-07-25",
        "then": "all 157 unique one-code-point tokens, SPACE at position zero, digit zero away from the origin, source provenance, and digest match exactly"
      },
      "file": "src/ucns/edcm.py",
      "id": "edcm_public_gonol_fixture_is_exact"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "UTF-8 corpus bytes or a Unicode speaker turn enter the profile",
        "since": "2026-07-25",
        "then": "decoding is strict, source code points remain byte-round-trippable, and the SPACE-origin carrier assignment never rewrites, normalizes, collapses, or folds source text"
      },
      "file": "src/ucns/edcm.py",
      "id": "edcm_source_text_is_not_normalized"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a source code point belongs to the profile-pinned Unicode White_Space set",
        "since": "2026-07-28",
        "then": "its exact source value, code point, and offset are preserved while its carrier token is U+0020 SPACE at public-gonol position zero"
      },
      "file": "src/ucns/edcm.py",
      "id": "edcm_space_manifestations_assign_to_origin"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "any speaker turn, including an empty or alphabet-incomplete turn",
        "since": "2026-07-25",
        "then": "the complete turn has support one while token and word counts do not alter support"
      },
      "file": "src/ucns/edcm.py",
      "id": "edcm_speaker_turn_has_unit_support"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a speaker turn contains SPACE manifestations and non-SPACE code points",
        "since": "2026-07-25",
        "then": "maximal ordered non-SPACE sequences initiate word gonols through the declared Mobius twist and every SPACE manifestation remains an explicit superpositioned nesting boundary"
      },
      "file": "src/ucns/edcm.py",
      "id": "edcm_word_is_the_smallest_gonol"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_token_observation",
        "module_kind": "schema",
        "module_name": "edcm",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "EdcmWordGonolProfile, EdcmTurnObservation, EdcmWordGonol, SuperpositionedSpaceBoundary, EdcmTokenObservation, PUBLIC_GONOL_157, EDCM_SOURCE_DOMAIN, EDCM_SPACE_CODE_POINTS, EDCM_SPACE_ASSIGNMENT_POLICY, edcm_carrier_position",
        "rollback": "remove this profile without changing the combined compatibility profile",
        "rollout": "experimental EDCM-only corpus observation profile; no universal UCNS or METAPAT selection",
        "since": "2026-07-25",
        "storage_boundary": "none",
        "summary": "exact EDCM observation profile with word gonols, source-preserving SPACE-origin nesting boundaries, and one unit of support per speaker turn",
        "tests": "tests/test_edcm_profile.py",
        "unresolved": "formal Mobius carrier coordinates, higher-gonol composition laws, and treatment of non-SPACE out-of-alphabet evidence",
        "user_data_boundary": "source text remains exact; pinned Unicode White_Space manifestations retain their raw source identity while assigning to carrier origin; non-SPACE out-of-alphabet code points are retained and reported"
      },
      "file": "src/ucns/edcm.py",
      "id": "edcm_word_gonol_profile"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "completion is registered for a declared construction boundary",
        "since": "2026-07-26",
        "then": "the receipt cannot claim that the underlying unknowable has been exhausted"
      },
      "file": "src/ucns/edcm_motion.py",
      "id": "edcm_completion_is_scoped_not_epistemic_exhaustion"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "an exact EDCM word observation is bound to explicit geometric and motion evidence",
        "since": "2026-07-26",
        "then": "source provenance, grain, relation, orientation, sidedness, motion, recursive parentage, completion effect, and unresolved capacity remain ordered and recoverable"
      },
      "file": "src/ucns/edcm_motion.py",
      "id": "edcm_motion_retains_trajectory_identity"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a scalar metric projection is attached to a motion observation",
        "since": "2026-07-26",
        "then": "it names its policy, retains a source-observation link, declares information loss, and cannot replace the trajectory"
      },
      "file": "src/ucns/edcm_motion.py",
      "id": "edcm_scalar_projection_is_declared_lossy"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "geometric assignment or motion evidence is recorded before the governing law is ratified",
        "since": "2026-07-26",
        "then": "its standing is unresolved or candidate and no default or canonical law is inferred"
      },
      "file": "src/ucns/edcm_motion.py",
      "id": "edcm_unknown_motion_laws_remain_explicit"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "validation helpers",
        "module_kind": "schema",
        "module_name": "edcm_motion",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "HmmmBoundary, GeometricAssignment, MotionStep, EpicyclicParentage, CompletionRegistration, EdcmMotionObservation, EdcmCompletionTrace, ScalarProjection, record_word_motion",
        "rollback": "remove this module and its public exports without changing the exact word-gonol observation profile",
        "rollout": "experimental EDCM-only represented and candidate-measured trajectory evidence; no assignment law, completion law, or metric selection",
        "since": "2026-07-26",
        "storage_boundary": "none",
        "summary": "trajectory-first EDCM evidence for explicit geometric assignment, recursive motion, scoped completion, and recoverable lossy scalar projections",
        "tests": "tests/test_edcm_motion.py",
        "unresolved": "element-assignment law, Mobius coordinates, circle-epicycle-disk-sphere transitions, higher-gonol composition, and canonical completion measurement",
        "user_data_boundary": "exact observed word text and source provenance remain attached to every motion observation"
      },
      "file": "src/ucns/edcm_motion.py",
      "id": "edcm_completion_motion_evidence"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a cell carrier and optional retained layers are assembled",
        "since": "2026-07-21",
        "then": "Structural Null is returned exactly when no cell carrier and no retained layer occurrence remains"
      },
      "file": "src/ucns/envelope.py",
      "id": "retained_envelope_has_unique_complete_null"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "retained evidence may be falsey or equal to None",
        "since": "2026-07-21",
        "then": "presence is determined only by the retained flag rather than truthiness"
      },
      "file": "src/ucns/envelope.py",
      "id": "retained_layer_presence_is_explicit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a selected retained layer is viewed through a structural policy",
        "since": "2026-07-21",
        "then": "the policy projection retains the untouched layer evidence and does not mutate the envelope"
      },
      "file": "src/ucns/envelope.py",
      "id": "retained_layer_projection_is_non_destructive"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "repeated or differently named structural layers are added",
        "since": "2026-07-21",
        "then": "every occurrence remains ordered and addressable and no earlier evidence is overwritten"
      },
      "file": "src/ucns/envelope.py",
      "id": "retained_layers_append_without_overwrite"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "receipts, metadata, relations, recursion, provenance, or state are retained",
        "since": "2026-07-21",
        "then": "cell_support_weight reports only the current cell carrier W and every other layer keeps explicit contribution status"
      },
      "file": "src/ucns/envelope.py",
      "id": "retained_layers_do_not_silently_enter_cell_support"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "schema",
        "module_name": "envelope",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "ContributionStatus, RetainedLayer, RetainedStructure, RetainedEnvelope, make_retained_structure, cell_support_weight, project_layer",
        "requires": "structural_cell_support_floor, structural_choice_policy_layer",
        "rollback": "remove public exports and this module",
        "rollout": "importable evidence envelope; not a complete UCNS object",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "retains optional structural layers without forcing them into cells or silently extending aggregate support",
        "tests": "tests/test_envelope.py",
        "unresolved": "layer measurement laws, canonical layer equivalence, complete UCNS object",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/envelope.py",
      "id": "retained_structure_envelope"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a witness case or candidate decision packet is content-addressed",
        "since": "2026-07-21",
        "then": "authorship role, author, provenance, and separate candidate, witness, and decision records remain identity-bearing evidence"
      },
      "file": "src/ucns/experiments.py",
      "id": "candidate_witness_and_decision_authorship_are_recorded"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "witness cases are assembled into a corpus and decision packet",
        "since": "2026-07-21",
        "then": "development and holdout partitions remain explicit and a packet cannot be reviewable without passing holdout evidence for the same candidate"
      },
      "file": "src/ucns/experiments.py",
      "id": "development_and_holdout_evidence_are_separate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a candidate experiment is declared",
        "since": "2026-07-21",
        "then": "candidate code identity, law implementation and fixtures, corpus, policies, comparison, traversal, and environment are content-addressed in one manifest"
      },
      "file": "src/ucns/experiments.py",
      "id": "experiment_manifests_pin_all_research_inputs"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "two complete ExperimentResult values claim the same manifest",
        "since": "2026-07-21",
        "then": "an explicit result adapter compares every result field or records why reproduction could not be established"
      },
      "file": "src/ucns/experiments.py",
      "id": "reproduction_checks_report_match_or_reason"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an arbitrary candidate-research subject is content-addressed",
        "since": "2026-07-21",
        "then": "a named versioned ContentAdapter supplies bytes and the stored record retains an isolated snapshot of those bytes and subject state"
      },
      "file": "src/ucns/experiments.py",
      "id": "subject_identity_requires_explicit_adapter"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_digest_bytes, _canonical_json, _validate_report_owner",
        "module_kind": "instrument",
        "module_name": "experiments",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "ContentAdapter, AdapterRegistry, json_content_adapter, text_content_adapter, bytes_content_adapter, SubjectRecord, WitnessOrigin, CorpusPartition, AuthorshipRecord, WitnessCase, WitnessCorpus, CandidateIdentity, PolicyDigest, LawSuiteDigest, ExperimentManifest, ExperimentResult, MetamorphicCase, MutationCase, Counterexample, NamedTransform, generate_metamorphic_cases, generate_mutation_cases, greedy_minimize_counterexample, HoldoutReport, CandidateDecisionPacket, ReproductionCheck, check_reproduction, build_candidate_decision_packet, comparison_policy_digest, traversal_policy_digest",
        "requires": "evaluator_candidate_laboratory, explicit_comparison_policy_layer, cycle_safe_traversal_policy",
        "rollback": "remove experiment exports; candidate laboratory remains process-local",
        "rollout": "reproducible candidate-research evidence infrastructure only",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "snapshots and content-addresses subjects, corpora, implementations, laws, manifests, holdouts, mutations, reproduction checks, and decision packets",
        "tests": "tests/test_experiments.py",
        "unresolved": "external sealed holdout storage and canonical decision authority",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/experiments.py",
      "id": "reproducible_witness_experiment_pipeline"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "competing candidates evaluate the same subjects",
        "since": "2026-07-21",
        "then": "outputs and disagreements are recorded under a named comparison policy without selecting a default, majority, best, or canonical candidate"
      },
      "file": "src/ucns/laboratory.py",
      "id": "candidate_comparison_exposes_disagreement_without_ranking"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "an evaluator candidate is constructed",
        "since": "2026-07-21",
        "then": "version, code reference, scope, and policy dependencies are recorded rather than inferred from a callable"
      },
      "file": "src/ucns/laboratory.py",
      "id": "evaluator_candidate_identity_is_explicit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "multiple candidates of one evaluator kind are registered",
        "since": "2026-07-21",
        "then": "all remain independently addressable and callers must name a candidate or request the full set"
      },
      "file": "src/ucns/laboratory.py",
      "id": "evaluator_registry_has_no_implicit_winner"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a candidate name is already registered for an evaluator kind",
        "since": "2026-07-21",
        "then": "replacement fails unless replace is explicitly true"
      },
      "file": "src/ucns/laboratory.py",
      "id": "evaluator_replacement_is_explicit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a law is admitted to a reproducible experiment manifest",
        "since": "2026-07-21",
        "then": "law name, version, code reference, and explicit fixture digest identify both implementation and retained evidence"
      },
      "file": "src/ucns/laboratory.py",
      "id": "law_identity_covers_implementation_and_fixtures"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "laws are run against an evaluator candidate",
        "since": "2026-07-21",
        "then": "pass, failure, and exception evidence are retained in one complete report"
      },
      "file": "src/ucns/laboratory.py",
      "id": "law_suites_capture_failures_and_errors"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "candidate law evidence is evaluated",
        "since": "2026-07-21",
        "then": "the LawSuite carries an explicit ComparisonPolicy and every equality decision uses it"
      },
      "file": "src/ucns/laboratory.py",
      "id": "law_suites_require_named_comparison_policy"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_evaluate_candidates",
        "module_kind": "instrument",
        "module_name": "laboratory",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "EvaluatorKind, EvaluatorCandidate, EvaluatorRegistry, Witness, LawResult, Law, LawSuite, EvaluationReport, CandidateOutput, CandidateComparison, compare_candidates, null_zero_law, finite_nonnegative_law, pair_multiplicative_law, invariance_law, sensitivity_law, same_reference_different_candidate_law, same_candidate_different_reference_law",
        "requires": "structural_cell_support_floor, retained_structure_envelope, structural_choice_policy_layer, explicit_comparison_policy_layer",
        "rollback": "remove public exports and this module",
        "rollout": "candidate research infrastructure; no canonical evaluator",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "registers versioned evaluator candidates and versioned fixture-pinned laws under explicit comparison policies without selecting a winner",
        "tests": "tests/test_laboratory.py, tests/test_candidates.py, tests/test_experiments.py",
        "unresolved": "canonical equivalence, canonical M, canonical B, candidate promotion authority",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/laboratory.py",
      "id": "evaluator_candidate_laboratory"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a retained-layer pairing policy projects two layer occurrences",
        "since": "2026-07-21",
        "then": "both untouched sources, the projected view, and every declared information loss remain in the result evidence"
      },
      "file": "src/ucns/layer_pairing.py",
      "id": "layer_pairing_preserves_sources_and_declares_loss"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "two retained envelopes contain layer occurrences",
        "since": "2026-07-21",
        "then": "every consumed occurrence is selected by an explicit LayerPairRule and policy name"
      },
      "file": "src/ucns/layer_pairing.py",
      "id": "retained_layer_pairing_requires_explicit_plan"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "retained layers are paired into a result envelope",
        "since": "2026-07-21",
        "then": "their result layers remain unmeasured and do not silently enter W, M, or B"
      },
      "file": "src/ucns/layer_pairing.py",
      "id": "retained_pairing_does_not_extend_measurements"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "retained layer occurrences remain outside the plan",
        "since": "2026-07-21",
        "then": "pairing fails closed, preserves sided occurrences, or excludes them only according to the plan's explicit unmatched mode"
      },
      "file": "src/ucns/layer_pairing.py",
      "id": "unmatched_layers_follow_explicit_mode"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_no_losses, _as_structure, _select",
        "module_kind": "instrument",
        "module_name": "layer_pairing",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "LayerPairMode, UnmatchedLayerMode, LayerRef, LayerPairProjection, LayerPairPolicy, LayerPairRegistry, LayerPairRule, EnvelopePairPlan, LayerPairDecision, EnvelopePairResult, pair_retained, concatenate_layer_policy, cartesian_layer_policy, positional_zip_layer_policy, keep_sides_layer_policy, select_left_layer_policy, select_right_layer_policy, exclude_layer_policy, custom_layer_pair_policy",
        "requires": "retained_structure_envelope, structural_cell_support_floor",
        "rollback": "remove layer-pairing exports; retained envelopes remain unpaired",
        "rollout": "candidate envelope-pairing infrastructure; no canonical retained-layer product",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "composes retained layers through explicit occurrence-level pairing plans while preserving sources and losses",
        "tests": "tests/test_layer_pairing.py",
        "unresolved": "canonical retained-layer pairing laws and measurement contributions",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/layer_pairing.py",
      "id": "retained_layer_pairing_laboratory"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a report is produced before metric laws are selected",
        "since": "2026-07-29",
        "then": "every one of the nine M-by-B combinations is displayed for every relationship with unresolved value rather than a hidden numeric default"
      },
      "file": "src/ucns/mobius_experiment.py",
      "id": "carrier_experiment_displays_all_metric_candidates_without_zero_fill"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a v0.5 carrier experiment report is produced",
        "since": "2026-07-29",
        "then": "all three relationship claims and all sixteen falsifiers remain explicit with no selected candidate or canonization effect"
      },
      "file": "src/ucns/mobius_experiment.py",
      "id": "carrier_experiment_preserves_three_relationships_without_selection"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "an explicit comparison policy raises while evaluating supplied candidate evidence",
        "since": "2026-07-29",
        "then": "the affected falsifier is recorded as error and the remaining report is still returned"
      },
      "file": "src/ucns/mobius_experiment.py",
      "id": "carrier_experiment_retains_evaluation_errors"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "chart-map or incompatibility evidence is supplied",
        "since": "2026-07-29",
        "then": "reversible preserved maps support C2 and falsify C3 for that domain, while a complete failed-map witness can support C3 without promoting it"
      },
      "file": "src/ucns/mobius_experiment.py",
      "id": "chart_and_incompatibility_evidence_remain_separating"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the implemented directed cover is evaluated as comparison candidate C2",
        "since": "2026-07-29",
        "then": "360 degrees preserves the visible key while changing the lifted representative, 720 degrees returns completely, and the inverse restores the prior state"
      },
      "file": "src/ucns/mobius_experiment.py",
      "id": "directed_cover_experiment_reports_360_change_and_720_return"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the v0.5 minimum witness packet is built",
        "since": "2026-07-29",
        "then": "every exact source turn reconstructs without normalization and retains one unit of support"
      },
      "file": "src/ucns/mobius_experiment.py",
      "id": "mobius_experiment_preserves_minimum_source_witnesses"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "validation helpers, report-matrix builders, state comparison helpers",
        "module_kind": "experiment",
        "module_name": "mobius_experiment",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "CarrierRelationship, FalsifierVerdict, CarrierExperimentState, CandidateTrace, MapCommutationWitness, CarrierMapEvidence, SeparatingWitness, FalsifierResult, MetricDisplay, CarrierExperimentReport, build_v05_witness_packet, directed_cover_trace, evaluate_candidate_trace, evaluate_chart_map, evaluate_separating_witness, run_v05_carrier_experiment",
        "requires": "edcm_word_gonol_profile, edcm_completion_motion_evidence, directed_carrier_floor, explicit_comparison_policy_layer, first_competing_evaluator_candidate_families",
        "rollback": "remove this module and its tests without changing the exact EDCM observation profile or directed carrier floor",
        "rollout": "explicit UCNS-only v0.5 experiment; no carrier, metric, completion, EDCM, or METAPAT selection",
        "since": "2026-07-29",
        "storage_boundary": "none",
        "summary": "executes the v0.5 source, motion, mapping, and incompatibility falsifier matrix without selecting a carrier",
        "tests": "tests/test_mobius_experiment.py",
        "unresolved": "direct Mobius state law, element assignment, chart map or incompatibility proof, higher-gonol composition, circle-epicycle-disk-sphere transitions, scoped completion",
        "user_data_boundary": "exact source witnesses remain attached to observations and are never normalized"
      },
      "file": "src/ucns/mobius_experiment.py",
      "id": "edcm_mobius_carrier_experiment"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the current post-reset profile is inspected",
        "since": "2026-07-25",
        "then": "its exact option values are registered as an implemented candidate with no selection effect"
      },
      "file": "src/ucns/options.py",
      "id": "current_downstream_profile_is_one_configuration"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the current option-configuration project is inspected",
        "since": "2026-07-25",
        "then": "EDCM tests real systems for an EDCM-only selection with every authority-transfer field false"
      },
      "file": "src/ucns/options.py",
      "id": "edcm_configuration_selection_is_empirical_and_scoped"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "Erin's EDCM configuration directions and the real-system research boundary are inspected",
        "since": "2026-07-25",
        "then": "every decided constraint, plural M and B display, failure-seeking principle, and corpus candidate is explicit while unresolved dimensions remain open"
      },
      "file": "src/ucns/options.py",
      "id": "edcm_constraints_are_explicit_without_early_collapse"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the UCNS option registry is loaded",
        "since": "2026-07-26",
        "then": "completion-motion is the system root, completion remains scoped, trajectory is the observation identity, and scalar projections remain optional declared-loss views"
      },
      "file": "src/ucns/options.py",
      "id": "ucns_completion_motion_root_is_authoritative"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the UCNS decision registry is loaded",
        "since": "2026-07-25",
        "then": "the identifier is exactly UCNS and canonical expansion is absent"
      },
      "file": "src/ucns/options.py",
      "id": "ucns_identifier_is_stable_without_canonical_expansion"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an option dimension is declared",
        "since": "2026-07-25",
        "then": "every choice has a recognized standing and no dimension appoints a hidden default or selected winner"
      },
      "file": "src/ucns/options.py",
      "id": "ucns_options_have_explicit_non_default_standing"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_validate_registry",
        "module_kind": "schema",
        "module_name": "options",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "OPTION_REGISTRY_SCHEMA_ID, OPTION_REGISTRY_SCHEMA_VERSION, UCNS_IDENTIFIER, OptionRegistryError, load_option_registry, option_dimension",
        "rollback": "remove the registry surface without changing existing carrier or profile behavior",
        "rollout": "authoritative completion-motion root, scoped completion, trajectory identity, decisions, and explicit unresolved choices; no mathematical option selection",
        "since": "2026-07-25",
        "storage_boundary": "packaged option_registry.json",
        "summary": "loads and validates the authoritative UCNS completion-motion root, EDCM decisions, and unresolved-option registry",
        "tests": "tests/test_option_decisions.py",
        "unresolved": "ideal EDCM-scoped configuration, non-SPACE alphabet expansion or escape, and the option dimensions marked required-evaluation or unresolved",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/options.py",
      "id": "ucns_option_decision_registry"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "multiset or set semantics are requested for arbitrary evidence",
        "since": "2026-07-21",
        "then": "the caller supplies the identity key and UCNS does not invent equality or hashing semantics"
      },
      "file": "src/ucns/policy.py",
      "id": "lossy_builtin_policies_require_explicit_keys"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "multiple named structural policies are registered",
        "since": "2026-07-21",
        "then": "every policy remains independently addressable and no default winner is appointed"
      },
      "file": "src/ucns/policy.py",
      "id": "policy_registry_preserves_multiple_choices"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a policy projects retained evidence into a view",
        "since": "2026-07-21",
        "then": "the untouched source remains attached and every ignored or discarded distinction is explicitly reported"
      },
      "file": "src/ucns/policy.py",
      "id": "projection_retains_source_and_declares_loss"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a caller requests a policy name absent from the selected registry",
        "since": "2026-07-21",
        "then": "policy application raises rather than choosing a fallback"
      },
      "file": "src/ucns/policy.py",
      "id": "unknown_policy_names_fail_closed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_no_losses, _require_hashable",
        "module_kind": "instrument",
        "module_name": "policy",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "InformationLoss, Projection, StructurePolicy, PolicyRegistry, OccurrenceGroup, SetEntry, apply_policy, ordered_sequence_policy, unordered_multiset_policy, set_policy",
        "requires": "structural_cell_support_floor",
        "rollback": "remove public exports and this module",
        "rollout": "importable candidate-policy infrastructure; no canonical structural policy",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "registers explicit structural interpretations and returns reversible projections with declared information loss",
        "tests": "tests/test_policy.py",
        "unresolved": "graph policy, tree policy, canonical structural equivalence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/policy.py",
      "id": "structural_choice_policy_layer"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a current-root Carrier is bound to the EDCM/METAPAT profile",
        "since": "2026-07-23",
        "then": "order, multiplicity, occurrence identity, sidedness, algebraic zero, and retained evidence remain explicit without projection"
      },
      "file": "src/ucns/profiles.py",
      "id": "ordered_occurrence_profile_preserves_declared_choices"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a caller supplies a structure, profile identity, option declaration, or occurrence identities",
        "since": "2026-07-23",
        "then": "only Carrier or Structural Null with the exact fixed profile declaration and matching ordered occurrence identities is accepted"
      },
      "file": "src/ucns/profiles.py",
      "id": "profile_binding_is_fail_closed"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the bounded profile is exported publicly",
        "since": "2026-07-23",
        "then": "no universal UCNSObject, multiplication, factorization, theorem, or validity-transfer authority is restored"
      },
      "file": "src/ucns/profiles.py",
      "id": "profile_does_not_restore_archived_arithmetic"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_jsonable, _cell_identity_payload, _occurrence_id",
        "module_kind": "schema",
        "module_name": "profiles",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "EdcmMetapatOrderedOccurrenceProfile, ProfileBoundStructure, PROFILE_OPTIONS",
        "rollback": "remove profile exports and module without changing current carrier foundations",
        "rollout": "merged and package-validated initial configuration; no global or EDCM option selection",
        "since": "2026-07-23",
        "storage_boundary": "none",
        "summary": "binds current UCNS structures to one explicit initial post-reset option configuration for EDCM and METAPAT",
        "tests": "tests/test_profile_boundary.py",
        "unresolved": "ideal EDCM-scoped option configuration and whether EDCM and METAPAT require separate profiles",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/profiles.py",
      "id": "edcm_metapat_ordered_occurrence_profile"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "a non-null carrier contains present cells",
        "since": "2026-07-21",
        "then": "support_weight returns the sum of their support weights and returns zero only for STRUCTURAL_NULL"
      },
      "file": "src/ucns/structure.py",
      "id": "aggregate_support_is_cell_sum"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a cell retains payload value zero with positive support",
        "since": "2026-07-21",
        "then": "the cell is present and may form a non-null carrier"
      },
      "file": "src/ucns/structure.py",
      "id": "algebraic_zero_payload_remains_structural"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an iterable of potential cells contains no positive support after pruning",
        "since": "2026-07-21",
        "then": "make_carrier returns the unique STRUCTURAL_NULL rather than an empty Carrier"
      },
      "file": "src/ucns/structure.py",
      "id": "carrier_factory_returns_unique_null"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "Carrier is constructed directly",
        "since": "2026-07-21",
        "then": "it contains at least one present cell and contains no absent cells"
      },
      "file": "src/ucns/structure.py",
      "id": "carrier_is_non_null_by_construction"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "two non-null carriers are paired",
        "since": "2026-07-21",
        "then": "every present cell meets every present cell, paired support is multiplicative, aggregate support multiplies, and STRUCTURAL_NULL absorbs"
      },
      "file": "src/ucns/structure.py",
      "id": "carrier_pairing_is_cartesian_and_support_multiplicative"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a structural cell is constructed with support mu and optional retained fields",
        "since": "2026-07-21",
        "then": "mu is finite and nonnegative; mu is zero exactly for a field-empty absent cell; positive support requires retained distinction"
      },
      "file": "src/ucns/structure.py",
      "id": "cell_support_zero_test_is_fail_closed"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "optional erasure is applied to a raw cell collection",
        "since": "2026-07-21",
        "then": "collapse returns STRUCTURAL_NULL exactly when no positive-support cells survive"
      },
      "file": "src/ucns/structure.py",
      "id": "collapse_requires_complete_structural_absence"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "potential cells contain zero-support absent cells and positive-support present cells",
        "since": "2026-07-21",
        "then": "prune removes only absent cells and preserves all present cells in order"
      },
      "file": "src/ucns/structure.py",
      "id": "pruning_removes_only_absent_cells"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "present cells retain order, multiplicity, or left/right operand distinctions while canonical structural interpretation remains unresolved",
        "since": "2026-07-21",
        "then": "make_carrier, prune, and pair preserve those distinctions without sorting, deduplicating, flattening, merging, or overwriting them"
      },
      "file": "src/ucns/structure.py",
      "id": "unresolved_structure_choices_are_preserved"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_has_distinction, _cells_from",
        "module_kind": "schema",
        "module_name": "structure",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "Cell, Carrier, Structure, make_carrier, support_weight, pair, prune, collapse",
        "requires": "directed_carrier_floor",
        "rollback": "remove exports and this module",
        "rollout": "importable foundations surface; no product character or faithful-breadth evaluator",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "defines canonical cells, non-null carriers, aggregate support, pairing, pruning, collapse, and choice-preserving structural evidence",
        "tests": "tests/test_structure.py",
        "unresolved": "domain-specific mu assignment, receipts, metadata, canonical structural equivalence, choice policy type, M, B",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/structure.py",
      "id": "structural_cell_support_floor"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "fixed-point cycle handling is selected",
        "since": "2026-07-21",
        "then": "construction fails unless both an explicit resolver and versioned resolver code reference are supplied"
      },
      "file": "src/ucns/traversal.py",
      "id": "fixed_point_traversal_requires_resolver"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "retained recursive evidence repeats an identity on the active path",
        "since": "2026-07-21",
        "then": "traversal rejects, references, depth-unfolds, or invokes a fixed-point resolver only as explicitly selected"
      },
      "file": "src/ucns/traversal.py",
      "id": "recursive_cycles_require_explicit_policy"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "reference traversal encounters an identity previously visited on another path",
        "since": "2026-07-21",
        "then": "traversal emits a ReferenceReceipt to the first path rather than double-counting or silently discarding shared structure"
      },
      "file": "src/ucns/traversal.py",
      "id": "shared_identity_references_are_retained"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "recursive traversal reaches a depth or node budget, including while iterating a large or unbounded child iterable",
        "since": "2026-07-21",
        "then": "traversal stops without materializing the remaining iterable and retains a TruncationReceipt"
      },
      "file": "src/ucns/traversal.py",
      "id": "traversal_budgets_emit_receipts"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "instrument",
        "module_name": "traversal",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "CycleMode, TraversalBudget, TraversalPolicy, Visit, ReferenceReceipt, TruncationReceipt, FixedPointReceipt, TraversalResult, CycleDetectedError, traverse",
        "requires": "retained_structure_envelope",
        "rollback": "remove traversal exports; recursive candidates fail closed",
        "rollout": "recursive-evidence research infrastructure only",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "traverses recursive evidence under explicit cycle, shared-reference, implementation-identity, depth, node, and fixed-point policies",
        "tests": "tests/test_traversal.py, tests/test_experiments.py",
        "unresolved": "canonical recursive identity, sharing, and fixed-point semantics",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/traversal.py",
      "id": "cycle_safe_traversal_policy"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_candidate_family_coexistence",
        "cleanup": "none",
        "mutates": "none",
        "proves": "first_candidate_families_coexist_without_selection",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_candidates.py",
      "id": "check_candidate_family_coexistence"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_candidate_nonpromotion",
        "cleanup": "none",
        "mutates": "none",
        "proves": "candidate_constructors_do_not_promote_canon",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_candidates.py",
      "id": "check_candidate_nonpromotion"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_cell_candidate_scope_failure",
        "cleanup": "none",
        "mutates": "none",
        "proves": "cell_only_candidates_fail_outside_scope",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_candidates.py",
      "id": "check_cell_candidate_scope_failure"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_initial_product_multiplicativity",
        "cleanup": "none",
        "mutates": "none",
        "proves": "initial_product_candidates_multiply_under_actual_pairing",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_candidates.py",
      "id": "check_initial_product_multiplicativity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_lifted_period",
        "cleanup": "none",
        "mutates": "none",
        "proves": "lifted_period_is_720_degrees, two_visible_laps_complete_return",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_carrier.py",
      "id": "check_lifted_period"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_non_null_validation_and_radius",
        "cleanup": "none",
        "mutates": "none",
        "proves": "non_null_carrier_has_positive_breadth",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_carrier.py",
      "id": "check_non_null_validation_and_radius"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_one_lap_is_deck_translation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "one_visible_lap_is_deck_translation_only, topology_does_not_invent_orientation_algebra",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_carrier.py",
      "id": "check_one_lap_is_deck_translation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_payload_zero_does_not_collapse_carrier",
        "cleanup": "none",
        "mutates": "none",
        "proves": "algebraic_zero_is_not_structural_null",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_carrier.py",
      "id": "check_payload_zero_does_not_collapse_carrier"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_structural_null_identity",
        "cleanup": "none",
        "mutates": "none",
        "proves": "structural_null_is_unique_and_coordinate_free",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_carrier.py",
      "id": "check_structural_null_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_visible_projection_and_branch_law",
        "cleanup": "none",
        "mutates": "none",
        "proves": "visible_projection_is_360_degrees",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_carrier.py",
      "id": "check_visible_projection_and_branch_law"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_comparison_registry_choices",
        "cleanup": "none",
        "mutates": "none",
        "proves": "comparison_registry_preserves_multiple_policies",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_comparison.py",
      "id": "check_comparison_registry_choices"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_comparison_replacement",
        "cleanup": "none",
        "mutates": "none",
        "proves": "comparison_policy_replacement_is_explicit",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_comparison.py",
      "id": "check_comparison_replacement"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_custom_comparison_identity",
        "cleanup": "none",
        "mutates": "none",
        "proves": "custom_comparison_identity_is_explicit",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_comparison.py",
      "id": "check_custom_comparison_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_explicit_comparison_policies",
        "cleanup": "none",
        "mutates": "none",
        "proves": "evaluator_equality_requires_explicit_comparison_policy",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_comparison.py",
      "id": "check_explicit_comparison_policies"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_native_trace_supports_motion_and_independence_without_selection",
        "cleanup": "none",
        "mutates": "none",
        "proves": "direct_mobius_candidate_is_independent_and_nonselecting",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_direct_mobius.py",
      "id": "check_direct_mobius_candidate_independence"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_v06_report_retains_complete_matrix_and_unresolved_frontier",
        "cleanup": "none",
        "mutates": "none",
        "proves": "direct_mobius_report_retains_unresolved_frontier",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_direct_mobius.py",
      "id": "check_direct_mobius_frontier_retention"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_every_word_has_one_exact_causal_initiation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "direct_mobius_initiation_is_causal_and_cardinality_exact",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_direct_mobius.py",
      "id": "check_direct_mobius_initiation_cardinality"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_native_quotient_motion_is_exact_for_360_720_and_inverse",
        "cleanup": "none",
        "mutates": "none",
        "proves": "direct_mobius_native_motion_has_360_change_720_return_and_inverse",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_direct_mobius.py",
      "id": "check_direct_mobius_native_motion"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_repeated_space_retains_two_manifestations_and_immediate_cause",
        "cleanup": "none",
        "mutates": "none",
        "proves": "direct_mobius_repeated_space_preserves_singular_origin_and_occurrences",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_direct_mobius.py",
      "id": "check_direct_mobius_repeated_space"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_structural_null_is_singular_typed_and_source_preserving",
        "cleanup": "none",
        "mutates": "none",
        "proves": "direct_mobius_structural_null_is_typed_and_source_preserving",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_direct_mobius.py",
      "id": "check_direct_mobius_structural_null_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_completion_cannot_exhaust_the_underlying_unknowable",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_completion_is_scoped_not_epistemic_exhaustion"
      },
      "file": "tests/test_edcm_motion.py",
      "id": "check_edcm_completion_scope"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_scalar_projection_requires_loss_and_source_link",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_scalar_projection_is_declared_lossy"
      },
      "file": "tests/test_edcm_motion.py",
      "id": "check_edcm_lossy_projection"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_trace_rejects_forward_parentage",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_motion_retains_trajectory_identity"
      },
      "file": "tests/test_edcm_motion.py",
      "id": "check_edcm_parentage_fail_closed"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_trace_preserves_order_parentage_and_completion",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_motion_retains_trajectory_identity"
      },
      "file": "tests/test_edcm_motion.py",
      "id": "check_edcm_recursive_trace"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_unknown_assignment_and_motion_laws_remain_visible",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_unknown_motion_laws_remain_explicit"
      },
      "file": "tests/test_edcm_motion.py",
      "id": "check_edcm_unknown_laws_visible"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_word_motion_binding_preserves_exact_evidence",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_motion_retains_trajectory_identity"
      },
      "file": "tests/test_edcm_motion.py",
      "id": "check_edcm_word_motion_binding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_carrier_assignment_terms_distinguish_fixture_membership",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_space_manifestations_assign_to_origin"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_carrier_assignment_terms"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_public_gonol_fixture_is_exact",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_public_gonol_fixture_is_exact"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_exact_public_gonol_fixture"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_observe_corpus_runs_every_turn_without_sampling",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_alphabet_failure_is_positive_evidence"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_full_corpus_iteration"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_source_text_is_exact_and_out_of_alphabet_is_retained",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_source_text_is_not_normalized"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_no_source_normalization"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_profile_options_fail_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_source_text_is_not_normalized"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_profile_options_fail_closed"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_runtime_isspace_does_not_expand_the_pinned_profile",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_space_manifestations_assign_to_origin"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_space_assignment_pin_is_runtime_independent"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pinned_unicode_white_space_manifestations_assign_to_origin",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_space_manifestations_assign_to_origin"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_space_manifestations_assign_to_origin"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_space_manifestations_split_words_without_rewriting_source",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_space_manifestations_assign_to_origin"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_space_origin_segmentation_preserves_source"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_utf8_decoding_is_strict",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_source_text_is_not_normalized"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_strict_utf8_decoding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_surrogate_code_points_are_rejected_at_text_boundaries",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_source_text_is_not_normalized"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_surrogates_fail_closed"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_one_turn_is_one_unit_regardless_of_text_extent",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_speaker_turn_has_unit_support"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_turn_unit_support"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_non_space_unicode_scalars_remain_exact_unassigned_evidence",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_alphabet_failure_is_positive_evidence"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_valid_unassigned_scalars_are_retained"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_words_are_gonols_and_each_space_is_a_nesting_boundary",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_word_is_the_smallest_gonol"
      },
      "file": "tests/test_edcm_profile.py",
      "id": "check_word_gonol_nesting"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_falsey_retained_evidence",
        "cleanup": "none",
        "mutates": "none",
        "proves": "retained_layer_presence_is_explicit",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_envelope.py",
      "id": "check_falsey_retained_evidence"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_layer_append_behavior",
        "cleanup": "none",
        "mutates": "none",
        "proves": "retained_layers_append_without_overwrite",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_envelope.py",
      "id": "check_layer_append_behavior"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_layer_measurement_firewall",
        "cleanup": "none",
        "mutates": "none",
        "proves": "retained_layers_do_not_silently_enter_cell_support",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_envelope.py",
      "id": "check_layer_measurement_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_layer_projection",
        "cleanup": "none",
        "mutates": "none",
        "proves": "retained_layer_projection_is_non_destructive",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_envelope.py",
      "id": "check_layer_projection"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_retained_null_boundary",
        "cleanup": "none",
        "mutates": "none",
        "proves": "retained_envelope_has_unique_complete_null",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_envelope.py",
      "id": "check_retained_null_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_explicit_subject_adapters",
        "cleanup": "none",
        "mutates": "none",
        "proves": "subject_identity_requires_explicit_adapter",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_experiments.py",
      "id": "check_explicit_subject_adapters"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_holdout_decision_guard",
        "cleanup": "none",
        "mutates": "none",
        "proves": "development_and_holdout_evidence_are_separate",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_experiments.py",
      "id": "check_holdout_decision_guard"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_manifest_pins_research_inputs",
        "cleanup": "none",
        "mutates": "none",
        "proves": "experiment_manifests_pin_all_research_inputs",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_experiments.py",
      "id": "check_manifest_pins_research_inputs"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_reproduction_reporting",
        "cleanup": "none",
        "mutates": "none",
        "proves": "reproduction_checks_report_match_or_reason",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_experiments.py",
      "id": "check_reproduction_reporting"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_separate_authorship_records",
        "cleanup": "none",
        "mutates": "none",
        "proves": "candidate_witness_and_decision_authorship_are_recorded",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_experiments.py",
      "id": "check_separate_authorship_records"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_candidate_comparison",
        "cleanup": "none",
        "mutates": "none",
        "proves": "candidate_comparison_exposes_disagreement_without_ranking",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_laboratory.py",
      "id": "check_candidate_comparison"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_evaluator_identity",
        "cleanup": "none",
        "mutates": "none",
        "proves": "evaluator_candidate_identity_is_explicit",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_laboratory.py",
      "id": "check_evaluator_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_evaluator_registry_choices",
        "cleanup": "none",
        "mutates": "none",
        "proves": "evaluator_registry_has_no_implicit_winner",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_laboratory.py",
      "id": "check_evaluator_registry_choices"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_evaluator_replacement",
        "cleanup": "none",
        "mutates": "none",
        "proves": "evaluator_replacement_is_explicit",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_laboratory.py",
      "id": "check_evaluator_replacement"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_explicit_law_comparison",
        "cleanup": "none",
        "mutates": "none",
        "proves": "law_suites_require_named_comparison_policy",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_laboratory.py",
      "id": "check_explicit_law_comparison"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_law_suite_evidence",
        "cleanup": "none",
        "mutates": "none",
        "proves": "law_suites_capture_failures_and_errors",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_laboratory.py",
      "id": "check_law_suite_evidence"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_separation_law_builders",
        "cleanup": "none",
        "mutates": "none",
        "proves": "law_suites_capture_failures_and_errors",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_laboratory.py",
      "id": "check_separation_law_builders"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_law_identity_covers_fixtures",
        "cleanup": "none",
        "mutates": "none",
        "proves": "law_identity_covers_implementation_and_fixtures",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_law_identity.py",
      "id": "check_law_identity_covers_fixtures"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_explicit_layer_pair_plan",
        "cleanup": "none",
        "mutates": "none",
        "proves": "retained_layer_pairing_requires_explicit_plan",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_layer_pairing.py",
      "id": "check_explicit_layer_pair_plan"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_layer_pair_source_and_loss_evidence",
        "cleanup": "none",
        "mutates": "none",
        "proves": "layer_pairing_preserves_sources_and_declares_loss",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_layer_pairing.py",
      "id": "check_layer_pair_source_and_loss_evidence"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_retained_pair_measurement_firewall",
        "cleanup": "none",
        "mutates": "none",
        "proves": "retained_pairing_does_not_extend_measurements",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_layer_pairing.py",
      "id": "check_retained_pair_measurement_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_unmatched_layer_modes",
        "cleanup": "none",
        "mutates": "none",
        "proves": "unmatched_layers_follow_explicit_mode",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_layer_pairing.py",
      "id": "check_unmatched_layer_modes"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_chart_map_success_and_round_trip_failure_separate_c2_from_c3",
        "cleanup": "none",
        "mutates": "none",
        "proves": "chart_and_incompatibility_evidence_remain_separating",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_experiment.py",
      "id": "check_v05_chart_separation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_comparison_policy_exception_is_retained_as_error",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_experiment_retains_evaluation_errors",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_experiment.py",
      "id": "check_v05_comparison_error_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_report_retains_all_relationships_and_falsifiers_without_selection",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_experiment_preserves_three_relationships_without_selection",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_experiment.py",
      "id": "check_v05_complete_relationship_matrix"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_direct_trace_is_evaluated_without_promotion",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_experiment_preserves_three_relationships_without_selection",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_experiment.py",
      "id": "check_v05_direct_candidate_stays_candidate"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_directed_cover_trace_reports_360_change_720_return_and_inverse",
        "cleanup": "none",
        "mutates": "none",
        "proves": "directed_cover_experiment_reports_360_change_and_720_return",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_experiment.py",
      "id": "check_v05_directed_cover_motion"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_complete_failed_map_witness_supports_incompatibility_only",
        "cleanup": "none",
        "mutates": "none",
        "proves": "chart_and_incompatibility_evidence_remain_separating",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_experiment.py",
      "id": "check_v05_incompatibility_witness"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_metric_grid_displays_all_nine_combinations_without_values",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_experiment_displays_all_metric_candidates_without_zero_fill",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_experiment.py",
      "id": "check_v05_metric_grid"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_minimum_witness_packet_preserves_exact_source_and_support",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_experiment_preserves_minimum_source_witnesses",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_experiment.py",
      "id": "check_v05_minimum_witness_packet"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_current_profile_is_one_exact_candidate_configuration",
        "cleanup": "none",
        "mutates": "none",
        "proves": "current_downstream_profile_is_one_configuration",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_option_decisions.py",
      "id": "check_current_profile_registration"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_edcm_constraints_plural_displays_and_corpora_remain_explicit",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_constraints_are_explicit_without_early_collapse",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_option_decisions.py",
      "id": "check_edcm_explicit_constraints_and_corpora"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_edcm_selection_project_is_scoped_and_non_transferring",
        "cleanup": "none",
        "mutates": "none",
        "proves": "edcm_configuration_selection_is_empirical_and_scoped",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_option_decisions.py",
      "id": "check_edcm_scoped_selection"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_option_dimensions_have_no_hidden_default",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ucns_options_have_explicit_non_default_standing",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_option_decisions.py",
      "id": "check_explicit_non_default_standing"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_ucns_identifier_has_no_canonical_expansion",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ucns_identifier_is_stable_without_canonical_expansion",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_option_decisions.py",
      "id": "check_stable_identifier_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_completion_motion_root_scope_and_projection_firewall",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ucns_completion_motion_root_is_authoritative",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_option_decisions.py",
      "id": "check_ucns_completion_motion_root"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_unknown_option_dimension_fails_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ucns_options_have_explicit_non_default_standing",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_option_decisions.py",
      "id": "check_unknown_dimension_fails_closed"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_explicit_policy_keys",
        "cleanup": "none",
        "mutates": "none",
        "proves": "lossy_builtin_policies_require_explicit_keys",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_policy.py",
      "id": "check_explicit_policy_keys"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_policy_registry_choices",
        "cleanup": "none",
        "mutates": "none",
        "proves": "policy_registry_preserves_multiple_choices",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_policy.py",
      "id": "check_policy_registry_choices"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_projection_loss_evidence",
        "cleanup": "none",
        "mutates": "none",
        "proves": "projection_retains_source_and_declares_loss",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_policy.py",
      "id": "check_projection_loss_evidence"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_unknown_policy_failure",
        "cleanup": "none",
        "mutates": "none",
        "proves": "unknown_policy_names_fail_closed",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_policy.py",
      "id": "check_unknown_policy_failure"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_algebraic_zero_remains_positive_retained_structure",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ordered_occurrence_profile_preserves_declared_choices"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_algebraic_zero_retained"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_profile_does_not_restore_factorization_or_universal_multiplication",
        "cleanup": "none",
        "mutates": "none",
        "proves": "profile_does_not_restore_archived_arithmetic"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_archived_arithmetic_not_restored"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_archived_schema_ids_fail_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "post_reset_bridge_is_exact_and_fail_closed"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_archived_schema_rejection"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_bridge_round_trip_preserves_complete_record",
        "cleanup": "none",
        "mutates": "none",
        "proves": "post_reset_bridge_is_exact_and_fail_closed"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_bridge_round_trip"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_serialization_is_byte_deterministic",
        "cleanup": "none",
        "mutates": "none",
        "proves": "post_reset_bridge_is_exact_and_fail_closed, bridge_identity_binds_order_profile_and_content"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_bridge_serialization_determinism"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_cartesian_pairing_produces_p_times_q_occurrences",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ordered_occurrence_profile_preserves_declared_choices"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_cartesian_pair_cardinality"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_cartesian_pairing_is_left_major",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ordered_occurrence_profile_preserves_declared_choices"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_cartesian_pair_order"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_equal_valued_duplicate_occurrences_remain_distinct",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ordered_occurrence_profile_preserves_declared_choices"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_duplicate_occurrence_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_existing_public_exports_remain_present",
        "cleanup": "none",
        "mutates": "none",
        "proves": "profile_does_not_restore_archived_arithmetic"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_existing_public_surface_retained"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_reordering_changes_stable_identity",
        "cleanup": "none",
        "mutates": "none",
        "proves": "bridge_identity_binds_order_profile_and_content"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_order_binds_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pairing_preserves_left_right_sidedness",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ordered_occurrence_profile_preserves_declared_choices"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_pair_sidedness"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_profile_identity_participates_in_stable_identity",
        "cleanup": "none",
        "mutates": "none",
        "proves": "bridge_identity_binds_order_profile_and_content, profile_binding_is_fail_closed"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_profile_identity_binding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_option_mismatch_fails_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "profile_binding_is_fail_closed"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_profile_option_rejection"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_retained_relation_layer_does_not_change_scalar_support",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ordered_occurrence_profile_preserves_declared_choices"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_retained_relation_support_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_structural_null_is_distinct_from_algebraic_zero",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ordered_occurrence_profile_preserves_declared_choices"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_structural_null_distinction"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_validity_transfer_fields_are_permanently_false",
        "cleanup": "none",
        "mutates": "none",
        "proves": "validity_transfer_is_forbidden"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_validity_transfer_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_public_surface_is_bounded",
        "cleanup": "none",
        "mutates": "none",
        "proves": "public_surface_exposes_only_ratified_foundations",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_public_surface.py",
      "id": "check_public_surface_is_bounded"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_contract_audit_detects_gaps",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "contract_audit_reports_graph_gaps",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_skill_lib_contracts.py",
      "id": "check_contract_audit_detects_gaps"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_contract_audit_no_exec",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "contract_audit_is_no_exec",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_skill_lib_contracts.py",
      "id": "check_contract_audit_no_exec"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_repository_contract_graph",
        "cleanup": "none",
        "mutates": "none",
        "proves": "contract_audit_accepts_closed_graph",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_skill_lib_contracts.py",
      "id": "check_repository_contract_graph"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_aggregate_support",
        "cleanup": "none",
        "mutates": "none",
        "proves": "aggregate_support_is_cell_sum",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_aggregate_support"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_algebraic_zero_cell",
        "cleanup": "none",
        "mutates": "none",
        "proves": "algebraic_zero_payload_remains_structural",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_algebraic_zero_cell"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_carrier_constructor",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_is_non_null_by_construction",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_carrier_constructor"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_carrier_factory_null",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_factory_returns_unique_null",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_carrier_factory_null"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_cell_support_zero_test",
        "cleanup": "none",
        "mutates": "none",
        "proves": "cell_support_zero_test_is_fail_closed",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_cell_support_zero_test"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_complete_collapse",
        "cleanup": "none",
        "mutates": "none",
        "proves": "collapse_requires_complete_structural_absence",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_complete_collapse"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pairing_support_law",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_pairing_is_cartesian_and_support_multiplicative",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_pairing_support_law"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pruning_rule",
        "cleanup": "none",
        "mutates": "none",
        "proves": "pruning_removes_only_absent_cells",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_pruning_rule"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_unresolved_choice_preservation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "unresolved_structure_choices_are_preserved",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_structure.py",
      "id": "check_unresolved_choice_preservation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_fixed_point_requires_resolver",
        "cleanup": "none",
        "mutates": "none",
        "proves": "fixed_point_traversal_requires_resolver",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_traversal.py",
      "id": "check_fixed_point_requires_resolver"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_recursive_cycle_modes",
        "cleanup": "none",
        "mutates": "none",
        "proves": "recursive_cycles_require_explicit_policy",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_traversal.py",
      "id": "check_recursive_cycle_modes"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_shared_identity_reference",
        "cleanup": "none",
        "mutates": "none",
        "proves": "shared_identity_references_are_retained",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_traversal.py",
      "id": "check_shared_identity_reference"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_traversal_budget_receipts",
        "cleanup": "none",
        "mutates": "none",
        "proves": "traversal_budgets_emit_receipts",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_traversal.py",
      "id": "check_traversal_budget_receipts"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "every declared contract has a resolving check and every check names known contracts",
        "since": "2026-07-21",
        "then": "the audit exits successfully"
      },
      "file": "tools/verify_skill_lib_contracts.py",
      "id": "contract_audit_accepts_closed_graph"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the repository contract graph is audited",
        "since": "2026-07-21",
        "then": "Python source is parsed without importing product or test modules"
      },
      "file": "tools/verify_skill_lib_contracts.py",
      "id": "contract_audit_is_no_exec"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a contract, check target, or self call is missing or unknown",
        "since": "2026-07-21",
        "then": "the audit reports the gap and exits nonzero"
      },
      "file": "tools/verify_skill_lib_contracts.py",
      "id": "contract_audit_reports_graph_gaps"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "parse_blocks, audit_repository",
        "module_kind": "instrument",
        "module_name": "verify_skill_lib_contracts",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "command-line audit",
        "rollback": "remove workflow invocation and script",
        "rollout": "required CI gate",
        "since": "2026-07-21",
        "storage_boundary": "read",
        "summary": "performs a no-exec reconciliation of skill-lib MODULE_BUILD, CONTRACTS, and CHECKS declarations",
        "tests": "tests/test_skill_lib_contracts.py",
        "unresolved": "mutation-level verification beyond planted graph gaps",
        "user_data_boundary": "none"
      },
      "file": "tools/verify_skill_lib_contracts.py",
      "id": "skill_lib_contract_audit"
    }
  ],
  "edges": [
    {
      "from": "check_aggregate_support",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_aggregate_support",
      "to": "self::test_aggregate_support"
    },
    {
      "from": "check_aggregate_support",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_aggregate_support",
      "to": "aggregate_support_is_cell_sum"
    },
    {
      "from": "check_aggregate_support",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_aggregate_support",
      "to": "python3"
    },
    {
      "from": "check_algebraic_zero_cell",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_algebraic_zero_cell",
      "to": "self::test_algebraic_zero_cell"
    },
    {
      "from": "check_algebraic_zero_cell",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_algebraic_zero_cell",
      "to": "algebraic_zero_payload_remains_structural"
    },
    {
      "from": "check_algebraic_zero_cell",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_algebraic_zero_cell",
      "to": "python3"
    },
    {
      "from": "check_algebraic_zero_retained",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_algebraic_zero_retained",
      "to": "self::test_algebraic_zero_remains_positive_retained_structure"
    },
    {
      "from": "check_algebraic_zero_retained",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_algebraic_zero_retained",
      "to": "ordered_occurrence_profile_preserves_declared_choices"
    },
    {
      "from": "check_archived_arithmetic_not_restored",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_archived_arithmetic_not_restored",
      "to": "self::test_profile_does_not_restore_factorization_or_universal_multiplication"
    },
    {
      "from": "check_archived_arithmetic_not_restored",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_archived_arithmetic_not_restored",
      "to": "profile_does_not_restore_archived_arithmetic"
    },
    {
      "from": "check_archived_schema_rejection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_archived_schema_rejection",
      "to": "self::test_archived_schema_ids_fail_closed"
    },
    {
      "from": "check_archived_schema_rejection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_archived_schema_rejection",
      "to": "post_reset_bridge_is_exact_and_fail_closed"
    },
    {
      "from": "check_bridge_round_trip",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_bridge_round_trip",
      "to": "self::test_bridge_round_trip_preserves_complete_record"
    },
    {
      "from": "check_bridge_round_trip",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_bridge_round_trip",
      "to": "post_reset_bridge_is_exact_and_fail_closed"
    },
    {
      "from": "check_bridge_serialization_determinism",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_bridge_serialization_determinism",
      "to": "self::test_serialization_is_byte_deterministic"
    },
    {
      "from": "check_bridge_serialization_determinism",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_bridge_serialization_determinism",
      "to": "bridge_identity_binds_order_profile_and_content"
    },
    {
      "from": "check_bridge_serialization_determinism",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_bridge_serialization_determinism",
      "to": "post_reset_bridge_is_exact_and_fail_closed"
    },
    {
      "from": "check_candidate_comparison",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_candidate_comparison",
      "to": "self::test_candidate_comparison"
    },
    {
      "from": "check_candidate_comparison",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_candidate_comparison",
      "to": "candidate_comparison_exposes_disagreement_without_ranking"
    },
    {
      "from": "check_candidate_comparison",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_candidate_comparison",
      "to": "python3"
    },
    {
      "from": "check_candidate_family_coexistence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_candidate_family_coexistence",
      "to": "self::test_candidate_family_coexistence"
    },
    {
      "from": "check_candidate_family_coexistence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_candidate_family_coexistence",
      "to": "first_candidate_families_coexist_without_selection"
    },
    {
      "from": "check_candidate_family_coexistence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_candidate_family_coexistence",
      "to": "python3"
    },
    {
      "from": "check_candidate_nonpromotion",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_candidate_nonpromotion",
      "to": "self::test_candidate_nonpromotion"
    },
    {
      "from": "check_candidate_nonpromotion",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_candidate_nonpromotion",
      "to": "candidate_constructors_do_not_promote_canon"
    },
    {
      "from": "check_candidate_nonpromotion",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_candidate_nonpromotion",
      "to": "python3"
    },
    {
      "from": "check_carrier_assignment_terms",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_assignment_terms",
      "to": "self::test_carrier_assignment_terms_distinguish_fixture_membership"
    },
    {
      "from": "check_carrier_assignment_terms",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_assignment_terms",
      "to": "edcm_space_manifestations_assign_to_origin"
    },
    {
      "from": "check_carrier_constructor",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_constructor",
      "to": "self::test_carrier_constructor"
    },
    {
      "from": "check_carrier_constructor",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_constructor",
      "to": "carrier_is_non_null_by_construction"
    },
    {
      "from": "check_carrier_constructor",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_carrier_constructor",
      "to": "python3"
    },
    {
      "from": "check_carrier_factory_null",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_factory_null",
      "to": "self::test_carrier_factory_null"
    },
    {
      "from": "check_carrier_factory_null",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_factory_null",
      "to": "carrier_factory_returns_unique_null"
    },
    {
      "from": "check_carrier_factory_null",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_carrier_factory_null",
      "to": "python3"
    },
    {
      "from": "check_cartesian_pair_cardinality",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_cartesian_pair_cardinality",
      "to": "self::test_cartesian_pairing_produces_p_times_q_occurrences"
    },
    {
      "from": "check_cartesian_pair_cardinality",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_cartesian_pair_cardinality",
      "to": "ordered_occurrence_profile_preserves_declared_choices"
    },
    {
      "from": "check_cartesian_pair_order",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_cartesian_pair_order",
      "to": "self::test_cartesian_pairing_is_left_major"
    },
    {
      "from": "check_cartesian_pair_order",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_cartesian_pair_order",
      "to": "ordered_occurrence_profile_preserves_declared_choices"
    },
    {
      "from": "check_cell_candidate_scope_failure",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_cell_candidate_scope_failure",
      "to": "self::test_cell_candidate_scope_failure"
    },
    {
      "from": "check_cell_candidate_scope_failure",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_cell_candidate_scope_failure",
      "to": "cell_only_candidates_fail_outside_scope"
    },
    {
      "from": "check_cell_candidate_scope_failure",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_cell_candidate_scope_failure",
      "to": "python3"
    },
    {
      "from": "check_cell_support_zero_test",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_cell_support_zero_test",
      "to": "self::test_cell_support_zero_test"
    },
    {
      "from": "check_cell_support_zero_test",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_cell_support_zero_test",
      "to": "cell_support_zero_test_is_fail_closed"
    },
    {
      "from": "check_cell_support_zero_test",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_cell_support_zero_test",
      "to": "python3"
    },
    {
      "from": "check_comparison_registry_choices",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_comparison_registry_choices",
      "to": "self::test_comparison_registry_choices"
    },
    {
      "from": "check_comparison_registry_choices",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_comparison_registry_choices",
      "to": "comparison_registry_preserves_multiple_policies"
    },
    {
      "from": "check_comparison_registry_choices",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_comparison_registry_choices",
      "to": "python3"
    },
    {
      "from": "check_comparison_replacement",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_comparison_replacement",
      "to": "self::test_comparison_replacement"
    },
    {
      "from": "check_comparison_replacement",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_comparison_replacement",
      "to": "comparison_policy_replacement_is_explicit"
    },
    {
      "from": "check_comparison_replacement",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_comparison_replacement",
      "to": "python3"
    },
    {
      "from": "check_complete_collapse",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_complete_collapse",
      "to": "self::test_complete_collapse"
    },
    {
      "from": "check_complete_collapse",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_complete_collapse",
      "to": "collapse_requires_complete_structural_absence"
    },
    {
      "from": "check_complete_collapse",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_complete_collapse",
      "to": "python3"
    },
    {
      "from": "check_contract_audit_detects_gaps",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_contract_audit_detects_gaps",
      "to": "self::test_contract_audit_detects_gaps"
    },
    {
      "from": "check_contract_audit_detects_gaps",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_contract_audit_detects_gaps",
      "to": "contract_audit_reports_graph_gaps"
    },
    {
      "from": "check_contract_audit_detects_gaps",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_contract_audit_detects_gaps",
      "to": "python3"
    },
    {
      "from": "check_contract_audit_no_exec",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_contract_audit_no_exec",
      "to": "self::test_contract_audit_no_exec"
    },
    {
      "from": "check_contract_audit_no_exec",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_contract_audit_no_exec",
      "to": "contract_audit_is_no_exec"
    },
    {
      "from": "check_contract_audit_no_exec",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_contract_audit_no_exec",
      "to": "python3"
    },
    {
      "from": "check_current_profile_registration",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_current_profile_registration",
      "to": "self::test_current_profile_is_one_exact_candidate_configuration"
    },
    {
      "from": "check_current_profile_registration",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_current_profile_registration",
      "to": "current_downstream_profile_is_one_configuration"
    },
    {
      "from": "check_current_profile_registration",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_current_profile_registration",
      "to": "python3"
    },
    {
      "from": "check_custom_comparison_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_custom_comparison_identity",
      "to": "self::test_custom_comparison_identity"
    },
    {
      "from": "check_custom_comparison_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_custom_comparison_identity",
      "to": "custom_comparison_identity_is_explicit"
    },
    {
      "from": "check_custom_comparison_identity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_custom_comparison_identity",
      "to": "python3"
    },
    {
      "from": "check_direct_mobius_candidate_independence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_candidate_independence",
      "to": "self::test_native_trace_supports_motion_and_independence_without_selection"
    },
    {
      "from": "check_direct_mobius_candidate_independence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_candidate_independence",
      "to": "direct_mobius_candidate_is_independent_and_nonselecting"
    },
    {
      "from": "check_direct_mobius_candidate_independence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_candidate_independence",
      "to": "python3"
    },
    {
      "from": "check_direct_mobius_frontier_retention",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_frontier_retention",
      "to": "self::test_v06_report_retains_complete_matrix_and_unresolved_frontier"
    },
    {
      "from": "check_direct_mobius_frontier_retention",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_frontier_retention",
      "to": "direct_mobius_report_retains_unresolved_frontier"
    },
    {
      "from": "check_direct_mobius_frontier_retention",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_frontier_retention",
      "to": "python3"
    },
    {
      "from": "check_direct_mobius_initiation_cardinality",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_initiation_cardinality",
      "to": "self::test_every_word_has_one_exact_causal_initiation"
    },
    {
      "from": "check_direct_mobius_initiation_cardinality",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_initiation_cardinality",
      "to": "direct_mobius_initiation_is_causal_and_cardinality_exact"
    },
    {
      "from": "check_direct_mobius_initiation_cardinality",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_initiation_cardinality",
      "to": "python3"
    },
    {
      "from": "check_direct_mobius_native_motion",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_native_motion",
      "to": "self::test_native_quotient_motion_is_exact_for_360_720_and_inverse"
    },
    {
      "from": "check_direct_mobius_native_motion",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_native_motion",
      "to": "direct_mobius_native_motion_has_360_change_720_return_and_inverse"
    },
    {
      "from": "check_direct_mobius_native_motion",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_native_motion",
      "to": "python3"
    },
    {
      "from": "check_direct_mobius_repeated_space",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_repeated_space",
      "to": "self::test_repeated_space_retains_two_manifestations_and_immediate_cause"
    },
    {
      "from": "check_direct_mobius_repeated_space",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_repeated_space",
      "to": "direct_mobius_repeated_space_preserves_singular_origin_and_occurrences"
    },
    {
      "from": "check_direct_mobius_repeated_space",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_repeated_space",
      "to": "python3"
    },
    {
      "from": "check_direct_mobius_structural_null_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_structural_null_identity",
      "to": "self::test_structural_null_is_singular_typed_and_source_preserving"
    },
    {
      "from": "check_direct_mobius_structural_null_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_structural_null_identity",
      "to": "direct_mobius_structural_null_is_typed_and_source_preserving"
    },
    {
      "from": "check_direct_mobius_structural_null_identity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_direct_mobius_structural_null_identity",
      "to": "python3"
    },
    {
      "from": "check_duplicate_occurrence_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_duplicate_occurrence_identity",
      "to": "self::test_equal_valued_duplicate_occurrences_remain_distinct"
    },
    {
      "from": "check_duplicate_occurrence_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_duplicate_occurrence_identity",
      "to": "ordered_occurrence_profile_preserves_declared_choices"
    },
    {
      "from": "check_edcm_completion_scope",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_completion_scope",
      "to": "self::test_completion_cannot_exhaust_the_underlying_unknowable"
    },
    {
      "from": "check_edcm_completion_scope",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_completion_scope",
      "to": "edcm_completion_is_scoped_not_epistemic_exhaustion"
    },
    {
      "from": "check_edcm_explicit_constraints_and_corpora",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_explicit_constraints_and_corpora",
      "to": "self::test_edcm_constraints_plural_displays_and_corpora_remain_explicit"
    },
    {
      "from": "check_edcm_explicit_constraints_and_corpora",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_explicit_constraints_and_corpora",
      "to": "edcm_constraints_are_explicit_without_early_collapse"
    },
    {
      "from": "check_edcm_explicit_constraints_and_corpora",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_edcm_explicit_constraints_and_corpora",
      "to": "python3"
    },
    {
      "from": "check_edcm_lossy_projection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_lossy_projection",
      "to": "self::test_scalar_projection_requires_loss_and_source_link"
    },
    {
      "from": "check_edcm_lossy_projection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_lossy_projection",
      "to": "edcm_scalar_projection_is_declared_lossy"
    },
    {
      "from": "check_edcm_parentage_fail_closed",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_parentage_fail_closed",
      "to": "self::test_trace_rejects_forward_parentage"
    },
    {
      "from": "check_edcm_parentage_fail_closed",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_parentage_fail_closed",
      "to": "edcm_motion_retains_trajectory_identity"
    },
    {
      "from": "check_edcm_recursive_trace",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_recursive_trace",
      "to": "self::test_trace_preserves_order_parentage_and_completion"
    },
    {
      "from": "check_edcm_recursive_trace",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_recursive_trace",
      "to": "edcm_motion_retains_trajectory_identity"
    },
    {
      "from": "check_edcm_scoped_selection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_scoped_selection",
      "to": "self::test_edcm_selection_project_is_scoped_and_non_transferring"
    },
    {
      "from": "check_edcm_scoped_selection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_scoped_selection",
      "to": "edcm_configuration_selection_is_empirical_and_scoped"
    },
    {
      "from": "check_edcm_scoped_selection",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_edcm_scoped_selection",
      "to": "python3"
    },
    {
      "from": "check_edcm_unknown_laws_visible",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_unknown_laws_visible",
      "to": "self::test_unknown_assignment_and_motion_laws_remain_visible"
    },
    {
      "from": "check_edcm_unknown_laws_visible",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_unknown_laws_visible",
      "to": "edcm_unknown_motion_laws_remain_explicit"
    },
    {
      "from": "check_edcm_word_motion_binding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_word_motion_binding",
      "to": "self::test_word_motion_binding_preserves_exact_evidence"
    },
    {
      "from": "check_edcm_word_motion_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_word_motion_binding",
      "to": "edcm_motion_retains_trajectory_identity"
    },
    {
      "from": "check_evaluator_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_identity",
      "to": "self::test_evaluator_identity"
    },
    {
      "from": "check_evaluator_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_identity",
      "to": "evaluator_candidate_identity_is_explicit"
    },
    {
      "from": "check_evaluator_identity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_identity",
      "to": "python3"
    },
    {
      "from": "check_evaluator_registry_choices",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_registry_choices",
      "to": "self::test_evaluator_registry_choices"
    },
    {
      "from": "check_evaluator_registry_choices",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_registry_choices",
      "to": "evaluator_registry_has_no_implicit_winner"
    },
    {
      "from": "check_evaluator_registry_choices",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_registry_choices",
      "to": "python3"
    },
    {
      "from": "check_evaluator_replacement",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_replacement",
      "to": "self::test_evaluator_replacement"
    },
    {
      "from": "check_evaluator_replacement",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_replacement",
      "to": "evaluator_replacement_is_explicit"
    },
    {
      "from": "check_evaluator_replacement",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_evaluator_replacement",
      "to": "python3"
    },
    {
      "from": "check_exact_public_gonol_fixture",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_exact_public_gonol_fixture",
      "to": "self::test_public_gonol_fixture_is_exact"
    },
    {
      "from": "check_exact_public_gonol_fixture",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_exact_public_gonol_fixture",
      "to": "edcm_public_gonol_fixture_is_exact"
    },
    {
      "from": "check_existing_public_surface_retained",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_existing_public_surface_retained",
      "to": "self::test_existing_public_exports_remain_present"
    },
    {
      "from": "check_existing_public_surface_retained",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_existing_public_surface_retained",
      "to": "profile_does_not_restore_archived_arithmetic"
    },
    {
      "from": "check_explicit_comparison_policies",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_comparison_policies",
      "to": "self::test_explicit_comparison_policies"
    },
    {
      "from": "check_explicit_comparison_policies",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_comparison_policies",
      "to": "evaluator_equality_requires_explicit_comparison_policy"
    },
    {
      "from": "check_explicit_comparison_policies",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_comparison_policies",
      "to": "python3"
    },
    {
      "from": "check_explicit_law_comparison",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_law_comparison",
      "to": "self::test_explicit_law_comparison"
    },
    {
      "from": "check_explicit_law_comparison",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_law_comparison",
      "to": "law_suites_require_named_comparison_policy"
    },
    {
      "from": "check_explicit_law_comparison",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_law_comparison",
      "to": "python3"
    },
    {
      "from": "check_explicit_layer_pair_plan",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_layer_pair_plan",
      "to": "self::test_explicit_layer_pair_plan"
    },
    {
      "from": "check_explicit_layer_pair_plan",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_layer_pair_plan",
      "to": "retained_layer_pairing_requires_explicit_plan"
    },
    {
      "from": "check_explicit_layer_pair_plan",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_layer_pair_plan",
      "to": "python3"
    },
    {
      "from": "check_explicit_non_default_standing",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_non_default_standing",
      "to": "self::test_option_dimensions_have_no_hidden_default"
    },
    {
      "from": "check_explicit_non_default_standing",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_non_default_standing",
      "to": "ucns_options_have_explicit_non_default_standing"
    },
    {
      "from": "check_explicit_non_default_standing",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_non_default_standing",
      "to": "python3"
    },
    {
      "from": "check_explicit_policy_keys",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_policy_keys",
      "to": "self::test_explicit_policy_keys"
    },
    {
      "from": "check_explicit_policy_keys",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_policy_keys",
      "to": "lossy_builtin_policies_require_explicit_keys"
    },
    {
      "from": "check_explicit_policy_keys",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_policy_keys",
      "to": "python3"
    },
    {
      "from": "check_explicit_subject_adapters",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_subject_adapters",
      "to": "self::test_explicit_subject_adapters"
    },
    {
      "from": "check_explicit_subject_adapters",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_subject_adapters",
      "to": "subject_identity_requires_explicit_adapter"
    },
    {
      "from": "check_explicit_subject_adapters",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_subject_adapters",
      "to": "python3"
    },
    {
      "from": "check_falsey_retained_evidence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_falsey_retained_evidence",
      "to": "self::test_falsey_retained_evidence"
    },
    {
      "from": "check_falsey_retained_evidence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_falsey_retained_evidence",
      "to": "retained_layer_presence_is_explicit"
    },
    {
      "from": "check_falsey_retained_evidence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_falsey_retained_evidence",
      "to": "python3"
    },
    {
      "from": "check_fixed_point_requires_resolver",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_fixed_point_requires_resolver",
      "to": "self::test_fixed_point_requires_resolver"
    },
    {
      "from": "check_fixed_point_requires_resolver",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_fixed_point_requires_resolver",
      "to": "fixed_point_traversal_requires_resolver"
    },
    {
      "from": "check_fixed_point_requires_resolver",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_fixed_point_requires_resolver",
      "to": "python3"
    },
    {
      "from": "check_full_corpus_iteration",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_iteration",
      "to": "self::test_observe_corpus_runs_every_turn_without_sampling"
    },
    {
      "from": "check_full_corpus_iteration",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_iteration",
      "to": "edcm_alphabet_failure_is_positive_evidence"
    },
    {
      "from": "check_holdout_decision_guard",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_holdout_decision_guard",
      "to": "self::test_holdout_decision_guard"
    },
    {
      "from": "check_holdout_decision_guard",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_holdout_decision_guard",
      "to": "development_and_holdout_evidence_are_separate"
    },
    {
      "from": "check_holdout_decision_guard",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_holdout_decision_guard",
      "to": "python3"
    },
    {
      "from": "check_initial_product_multiplicativity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_initial_product_multiplicativity",
      "to": "self::test_initial_product_multiplicativity"
    },
    {
      "from": "check_initial_product_multiplicativity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_initial_product_multiplicativity",
      "to": "initial_product_candidates_multiply_under_actual_pairing"
    },
    {
      "from": "check_initial_product_multiplicativity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_initial_product_multiplicativity",
      "to": "python3"
    },
    {
      "from": "check_law_identity_covers_fixtures",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_law_identity_covers_fixtures",
      "to": "self::test_law_identity_covers_fixtures"
    },
    {
      "from": "check_law_identity_covers_fixtures",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_law_identity_covers_fixtures",
      "to": "law_identity_covers_implementation_and_fixtures"
    },
    {
      "from": "check_law_identity_covers_fixtures",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_law_identity_covers_fixtures",
      "to": "python3"
    },
    {
      "from": "check_law_suite_evidence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_law_suite_evidence",
      "to": "self::test_law_suite_evidence"
    },
    {
      "from": "check_law_suite_evidence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_law_suite_evidence",
      "to": "law_suites_capture_failures_and_errors"
    },
    {
      "from": "check_law_suite_evidence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_law_suite_evidence",
      "to": "python3"
    },
    {
      "from": "check_layer_append_behavior",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_layer_append_behavior",
      "to": "self::test_layer_append_behavior"
    },
    {
      "from": "check_layer_append_behavior",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_layer_append_behavior",
      "to": "retained_layers_append_without_overwrite"
    },
    {
      "from": "check_layer_append_behavior",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_layer_append_behavior",
      "to": "python3"
    },
    {
      "from": "check_layer_measurement_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_layer_measurement_firewall",
      "to": "self::test_layer_measurement_firewall"
    },
    {
      "from": "check_layer_measurement_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_layer_measurement_firewall",
      "to": "retained_layers_do_not_silently_enter_cell_support"
    },
    {
      "from": "check_layer_measurement_firewall",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_layer_measurement_firewall",
      "to": "python3"
    },
    {
      "from": "check_layer_pair_source_and_loss_evidence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_layer_pair_source_and_loss_evidence",
      "to": "self::test_layer_pair_source_and_loss_evidence"
    },
    {
      "from": "check_layer_pair_source_and_loss_evidence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_layer_pair_source_and_loss_evidence",
      "to": "layer_pairing_preserves_sources_and_declares_loss"
    },
    {
      "from": "check_layer_pair_source_and_loss_evidence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_layer_pair_source_and_loss_evidence",
      "to": "python3"
    },
    {
      "from": "check_layer_projection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_layer_projection",
      "to": "self::test_layer_projection"
    },
    {
      "from": "check_layer_projection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_layer_projection",
      "to": "retained_layer_projection_is_non_destructive"
    },
    {
      "from": "check_layer_projection",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_layer_projection",
      "to": "python3"
    },
    {
      "from": "check_lifted_period",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_lifted_period",
      "to": "self::test_lifted_period"
    },
    {
      "from": "check_lifted_period",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_lifted_period",
      "to": "lifted_period_is_720_degrees"
    },
    {
      "from": "check_lifted_period",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_lifted_period",
      "to": "two_visible_laps_complete_return"
    },
    {
      "from": "check_lifted_period",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_lifted_period",
      "to": "python3"
    },
    {
      "from": "check_manifest_pins_research_inputs",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_manifest_pins_research_inputs",
      "to": "self::test_manifest_pins_research_inputs"
    },
    {
      "from": "check_manifest_pins_research_inputs",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_manifest_pins_research_inputs",
      "to": "experiment_manifests_pin_all_research_inputs"
    },
    {
      "from": "check_manifest_pins_research_inputs",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_manifest_pins_research_inputs",
      "to": "python3"
    },
    {
      "from": "check_no_source_normalization",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_no_source_normalization",
      "to": "self::test_source_text_is_exact_and_out_of_alphabet_is_retained"
    },
    {
      "from": "check_no_source_normalization",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_no_source_normalization",
      "to": "edcm_source_text_is_not_normalized"
    },
    {
      "from": "check_non_null_validation_and_radius",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_non_null_validation_and_radius",
      "to": "self::test_non_null_validation_and_radius"
    },
    {
      "from": "check_non_null_validation_and_radius",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_non_null_validation_and_radius",
      "to": "non_null_carrier_has_positive_breadth"
    },
    {
      "from": "check_non_null_validation_and_radius",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_non_null_validation_and_radius",
      "to": "python3"
    },
    {
      "from": "check_one_lap_is_deck_translation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_one_lap_is_deck_translation",
      "to": "self::test_one_lap_is_deck_translation"
    },
    {
      "from": "check_one_lap_is_deck_translation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_one_lap_is_deck_translation",
      "to": "one_visible_lap_is_deck_translation_only"
    },
    {
      "from": "check_one_lap_is_deck_translation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_one_lap_is_deck_translation",
      "to": "topology_does_not_invent_orientation_algebra"
    },
    {
      "from": "check_one_lap_is_deck_translation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_one_lap_is_deck_translation",
      "to": "python3"
    },
    {
      "from": "check_order_binds_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_order_binds_identity",
      "to": "self::test_reordering_changes_stable_identity"
    },
    {
      "from": "check_order_binds_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_order_binds_identity",
      "to": "bridge_identity_binds_order_profile_and_content"
    },
    {
      "from": "check_pair_sidedness",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pair_sidedness",
      "to": "self::test_pairing_preserves_left_right_sidedness"
    },
    {
      "from": "check_pair_sidedness",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pair_sidedness",
      "to": "ordered_occurrence_profile_preserves_declared_choices"
    },
    {
      "from": "check_pairing_support_law",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pairing_support_law",
      "to": "self::test_pairing_support_law"
    },
    {
      "from": "check_pairing_support_law",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pairing_support_law",
      "to": "carrier_pairing_is_cartesian_and_support_multiplicative"
    },
    {
      "from": "check_pairing_support_law",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_pairing_support_law",
      "to": "python3"
    },
    {
      "from": "check_payload_zero_does_not_collapse_carrier",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_payload_zero_does_not_collapse_carrier",
      "to": "self::test_payload_zero_does_not_collapse_carrier"
    },
    {
      "from": "check_payload_zero_does_not_collapse_carrier",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_payload_zero_does_not_collapse_carrier",
      "to": "algebraic_zero_is_not_structural_null"
    },
    {
      "from": "check_payload_zero_does_not_collapse_carrier",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_payload_zero_does_not_collapse_carrier",
      "to": "python3"
    },
    {
      "from": "check_policy_registry_choices",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_policy_registry_choices",
      "to": "self::test_policy_registry_choices"
    },
    {
      "from": "check_policy_registry_choices",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_policy_registry_choices",
      "to": "policy_registry_preserves_multiple_choices"
    },
    {
      "from": "check_policy_registry_choices",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_policy_registry_choices",
      "to": "python3"
    },
    {
      "from": "check_profile_identity_binding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_profile_identity_binding",
      "to": "self::test_profile_identity_participates_in_stable_identity"
    },
    {
      "from": "check_profile_identity_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_profile_identity_binding",
      "to": "bridge_identity_binds_order_profile_and_content"
    },
    {
      "from": "check_profile_identity_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_profile_identity_binding",
      "to": "profile_binding_is_fail_closed"
    },
    {
      "from": "check_profile_option_rejection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_profile_option_rejection",
      "to": "self::test_option_mismatch_fails_closed"
    },
    {
      "from": "check_profile_option_rejection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_profile_option_rejection",
      "to": "profile_binding_is_fail_closed"
    },
    {
      "from": "check_profile_options_fail_closed",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_profile_options_fail_closed",
      "to": "self::test_profile_options_fail_closed"
    },
    {
      "from": "check_profile_options_fail_closed",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_profile_options_fail_closed",
      "to": "edcm_source_text_is_not_normalized"
    },
    {
      "from": "check_projection_loss_evidence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_projection_loss_evidence",
      "to": "self::test_projection_loss_evidence"
    },
    {
      "from": "check_projection_loss_evidence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_projection_loss_evidence",
      "to": "projection_retains_source_and_declares_loss"
    },
    {
      "from": "check_projection_loss_evidence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_projection_loss_evidence",
      "to": "python3"
    },
    {
      "from": "check_pruning_rule",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pruning_rule",
      "to": "self::test_pruning_rule"
    },
    {
      "from": "check_pruning_rule",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pruning_rule",
      "to": "pruning_removes_only_absent_cells"
    },
    {
      "from": "check_pruning_rule",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_pruning_rule",
      "to": "python3"
    },
    {
      "from": "check_public_surface_is_bounded",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_public_surface_is_bounded",
      "to": "self::test_public_surface_is_bounded"
    },
    {
      "from": "check_public_surface_is_bounded",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_public_surface_is_bounded",
      "to": "public_surface_exposes_only_ratified_foundations"
    },
    {
      "from": "check_public_surface_is_bounded",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_public_surface_is_bounded",
      "to": "python3"
    },
    {
      "from": "check_recursive_cycle_modes",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_recursive_cycle_modes",
      "to": "self::test_recursive_cycle_modes"
    },
    {
      "from": "check_recursive_cycle_modes",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_recursive_cycle_modes",
      "to": "recursive_cycles_require_explicit_policy"
    },
    {
      "from": "check_recursive_cycle_modes",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_recursive_cycle_modes",
      "to": "python3"
    },
    {
      "from": "check_repository_contract_graph",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_repository_contract_graph",
      "to": "self::test_repository_contract_graph"
    },
    {
      "from": "check_repository_contract_graph",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_repository_contract_graph",
      "to": "contract_audit_accepts_closed_graph"
    },
    {
      "from": "check_repository_contract_graph",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_repository_contract_graph",
      "to": "python3"
    },
    {
      "from": "check_reproduction_reporting",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_reproduction_reporting",
      "to": "self::test_reproduction_reporting"
    },
    {
      "from": "check_reproduction_reporting",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_reproduction_reporting",
      "to": "reproduction_checks_report_match_or_reason"
    },
    {
      "from": "check_reproduction_reporting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_reproduction_reporting",
      "to": "python3"
    },
    {
      "from": "check_retained_null_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_retained_null_boundary",
      "to": "self::test_retained_null_boundary"
    },
    {
      "from": "check_retained_null_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_retained_null_boundary",
      "to": "retained_envelope_has_unique_complete_null"
    },
    {
      "from": "check_retained_null_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_retained_null_boundary",
      "to": "python3"
    },
    {
      "from": "check_retained_pair_measurement_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_retained_pair_measurement_firewall",
      "to": "self::test_retained_pair_measurement_firewall"
    },
    {
      "from": "check_retained_pair_measurement_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_retained_pair_measurement_firewall",
      "to": "retained_pairing_does_not_extend_measurements"
    },
    {
      "from": "check_retained_pair_measurement_firewall",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_retained_pair_measurement_firewall",
      "to": "python3"
    },
    {
      "from": "check_retained_relation_support_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_retained_relation_support_boundary",
      "to": "self::test_retained_relation_layer_does_not_change_scalar_support"
    },
    {
      "from": "check_retained_relation_support_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_retained_relation_support_boundary",
      "to": "ordered_occurrence_profile_preserves_declared_choices"
    },
    {
      "from": "check_separate_authorship_records",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_separate_authorship_records",
      "to": "self::test_separate_authorship_records"
    },
    {
      "from": "check_separate_authorship_records",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_separate_authorship_records",
      "to": "candidate_witness_and_decision_authorship_are_recorded"
    },
    {
      "from": "check_separate_authorship_records",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_separate_authorship_records",
      "to": "python3"
    },
    {
      "from": "check_separation_law_builders",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_separation_law_builders",
      "to": "self::test_separation_law_builders"
    },
    {
      "from": "check_separation_law_builders",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_separation_law_builders",
      "to": "law_suites_capture_failures_and_errors"
    },
    {
      "from": "check_separation_law_builders",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_separation_law_builders",
      "to": "python3"
    },
    {
      "from": "check_shared_identity_reference",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_shared_identity_reference",
      "to": "self::test_shared_identity_reference"
    },
    {
      "from": "check_shared_identity_reference",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_shared_identity_reference",
      "to": "shared_identity_references_are_retained"
    },
    {
      "from": "check_shared_identity_reference",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_shared_identity_reference",
      "to": "python3"
    },
    {
      "from": "check_space_assignment_pin_is_runtime_independent",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_space_assignment_pin_is_runtime_independent",
      "to": "self::test_runtime_isspace_does_not_expand_the_pinned_profile"
    },
    {
      "from": "check_space_assignment_pin_is_runtime_independent",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_space_assignment_pin_is_runtime_independent",
      "to": "edcm_space_manifestations_assign_to_origin"
    },
    {
      "from": "check_space_manifestations_assign_to_origin",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_space_manifestations_assign_to_origin",
      "to": "self::test_pinned_unicode_white_space_manifestations_assign_to_origin"
    },
    {
      "from": "check_space_manifestations_assign_to_origin",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_space_manifestations_assign_to_origin",
      "to": "edcm_space_manifestations_assign_to_origin"
    },
    {
      "from": "check_space_origin_segmentation_preserves_source",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_space_origin_segmentation_preserves_source",
      "to": "self::test_space_manifestations_split_words_without_rewriting_source"
    },
    {
      "from": "check_space_origin_segmentation_preserves_source",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_space_origin_segmentation_preserves_source",
      "to": "edcm_space_manifestations_assign_to_origin"
    },
    {
      "from": "check_stable_identifier_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_stable_identifier_boundary",
      "to": "self::test_ucns_identifier_has_no_canonical_expansion"
    },
    {
      "from": "check_stable_identifier_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_stable_identifier_boundary",
      "to": "ucns_identifier_is_stable_without_canonical_expansion"
    },
    {
      "from": "check_stable_identifier_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_stable_identifier_boundary",
      "to": "python3"
    },
    {
      "from": "check_strict_utf8_decoding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_strict_utf8_decoding",
      "to": "self::test_utf8_decoding_is_strict"
    },
    {
      "from": "check_strict_utf8_decoding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_strict_utf8_decoding",
      "to": "edcm_source_text_is_not_normalized"
    },
    {
      "from": "check_structural_null_distinction",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_structural_null_distinction",
      "to": "self::test_structural_null_is_distinct_from_algebraic_zero"
    },
    {
      "from": "check_structural_null_distinction",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_structural_null_distinction",
      "to": "ordered_occurrence_profile_preserves_declared_choices"
    },
    {
      "from": "check_structural_null_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_structural_null_identity",
      "to": "self::test_structural_null_identity"
    },
    {
      "from": "check_structural_null_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_structural_null_identity",
      "to": "structural_null_is_unique_and_coordinate_free"
    },
    {
      "from": "check_structural_null_identity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_structural_null_identity",
      "to": "python3"
    },
    {
      "from": "check_surrogates_fail_closed",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_surrogates_fail_closed",
      "to": "self::test_surrogate_code_points_are_rejected_at_text_boundaries"
    },
    {
      "from": "check_surrogates_fail_closed",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_surrogates_fail_closed",
      "to": "edcm_source_text_is_not_normalized"
    },
    {
      "from": "check_traversal_budget_receipts",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_traversal_budget_receipts",
      "to": "self::test_traversal_budget_receipts"
    },
    {
      "from": "check_traversal_budget_receipts",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_traversal_budget_receipts",
      "to": "traversal_budgets_emit_receipts"
    },
    {
      "from": "check_traversal_budget_receipts",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_traversal_budget_receipts",
      "to": "python3"
    },
    {
      "from": "check_turn_unit_support",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_turn_unit_support",
      "to": "self::test_one_turn_is_one_unit_regardless_of_text_extent"
    },
    {
      "from": "check_turn_unit_support",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_turn_unit_support",
      "to": "edcm_speaker_turn_has_unit_support"
    },
    {
      "from": "check_ucns_completion_motion_root",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_ucns_completion_motion_root",
      "to": "self::test_completion_motion_root_scope_and_projection_firewall"
    },
    {
      "from": "check_ucns_completion_motion_root",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_ucns_completion_motion_root",
      "to": "ucns_completion_motion_root_is_authoritative"
    },
    {
      "from": "check_ucns_completion_motion_root",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_ucns_completion_motion_root",
      "to": "python3"
    },
    {
      "from": "check_unknown_dimension_fails_closed",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_unknown_dimension_fails_closed",
      "to": "self::test_unknown_option_dimension_fails_closed"
    },
    {
      "from": "check_unknown_dimension_fails_closed",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_unknown_dimension_fails_closed",
      "to": "ucns_options_have_explicit_non_default_standing"
    },
    {
      "from": "check_unknown_dimension_fails_closed",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_unknown_dimension_fails_closed",
      "to": "python3"
    },
    {
      "from": "check_unknown_policy_failure",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_unknown_policy_failure",
      "to": "self::test_unknown_policy_failure"
    },
    {
      "from": "check_unknown_policy_failure",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_unknown_policy_failure",
      "to": "unknown_policy_names_fail_closed"
    },
    {
      "from": "check_unknown_policy_failure",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_unknown_policy_failure",
      "to": "python3"
    },
    {
      "from": "check_unmatched_layer_modes",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_unmatched_layer_modes",
      "to": "self::test_unmatched_layer_modes"
    },
    {
      "from": "check_unmatched_layer_modes",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_unmatched_layer_modes",
      "to": "unmatched_layers_follow_explicit_mode"
    },
    {
      "from": "check_unmatched_layer_modes",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_unmatched_layer_modes",
      "to": "python3"
    },
    {
      "from": "check_unresolved_choice_preservation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_unresolved_choice_preservation",
      "to": "self::test_unresolved_choice_preservation"
    },
    {
      "from": "check_unresolved_choice_preservation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_unresolved_choice_preservation",
      "to": "unresolved_structure_choices_are_preserved"
    },
    {
      "from": "check_unresolved_choice_preservation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_unresolved_choice_preservation",
      "to": "python3"
    },
    {
      "from": "check_v05_chart_separation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_v05_chart_separation",
      "to": "self::test_chart_map_success_and_round_trip_failure_separate_c2_from_c3"
    },
    {
      "from": "check_v05_chart_separation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_v05_chart_separation",
      "to": "chart_and_incompatibility_evidence_remain_separating"
    },
    {
      "from": "check_v05_chart_separation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_v05_chart_separation",
      "to": "python3"
    },
    {
      "from": "check_v05_comparison_error_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_v05_comparison_error_receipt",
      "to": "self::test_comparison_policy_exception_is_retained_as_error"
    },
    {
      "from": "check_v05_comparison_error_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_v05_comparison_error_receipt",
      "to": "carrier_experiment_retains_evaluation_errors"
    },
    {
      "from": "check_v05_comparison_error_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_v05_comparison_error_receipt",
      "to": "python3"
    },
    {
      "from": "check_v05_complete_relationship_matrix",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_v05_complete_relationship_matrix",
      "to": "self::test_report_retains_all_relationships_and_falsifiers_without_selection"
    },
    {
      "from": "check_v05_complete_relationship_matrix",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_v05_complete_relationship_matrix",
      "to": "carrier_experiment_preserves_three_relationships_without_selection"
    },
    {
      "from": "check_v05_complete_relationship_matrix",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_v05_complete_relationship_matrix",
      "to": "python3"
    },
    {
      "from": "check_v05_direct_candidate_stays_candidate",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_v05_direct_candidate_stays_candidate",
      "to": "self::test_direct_trace_is_evaluated_without_promotion"
    },
    {
      "from": "check_v05_direct_candidate_stays_candidate",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_v05_direct_candidate_stays_candidate",
      "to": "carrier_experiment_preserves_three_relationships_without_selection"
    },
    {
      "from": "check_v05_direct_candidate_stays_candidate",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_v05_direct_candidate_stays_candidate",
      "to": "python3"
    },
    {
      "from": "check_v05_directed_cover_motion",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_v05_directed_cover_motion",
      "to": "self::test_directed_cover_trace_reports_360_change_720_return_and_inverse"
    },
    {
      "from": "check_v05_directed_cover_motion",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_v05_directed_cover_motion",
      "to": "directed_cover_experiment_reports_360_change_and_720_return"
    },
    {
      "from": "check_v05_directed_cover_motion",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_v05_directed_cover_motion",
      "to": "python3"
    },
    {
      "from": "check_v05_incompatibility_witness",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_v05_incompatibility_witness",
      "to": "self::test_complete_failed_map_witness_supports_incompatibility_only"
    },
    {
      "from": "check_v05_incompatibility_witness",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_v05_incompatibility_witness",
      "to": "chart_and_incompatibility_evidence_remain_separating"
    },
    {
      "from": "check_v05_incompatibility_witness",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_v05_incompatibility_witness",
      "to": "python3"
    },
    {
      "from": "check_v05_metric_grid",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_v05_metric_grid",
      "to": "self::test_metric_grid_displays_all_nine_combinations_without_values"
    },
    {
      "from": "check_v05_metric_grid",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_v05_metric_grid",
      "to": "carrier_experiment_displays_all_metric_candidates_without_zero_fill"
    },
    {
      "from": "check_v05_metric_grid",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_v05_metric_grid",
      "to": "python3"
    },
    {
      "from": "check_v05_minimum_witness_packet",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_v05_minimum_witness_packet",
      "to": "self::test_minimum_witness_packet_preserves_exact_source_and_support"
    },
    {
      "from": "check_v05_minimum_witness_packet",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_v05_minimum_witness_packet",
      "to": "mobius_experiment_preserves_minimum_source_witnesses"
    },
    {
      "from": "check_v05_minimum_witness_packet",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_v05_minimum_witness_packet",
      "to": "python3"
    },
    {
      "from": "check_valid_unassigned_scalars_are_retained",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_valid_unassigned_scalars_are_retained",
      "to": "self::test_non_space_unicode_scalars_remain_exact_unassigned_evidence"
    },
    {
      "from": "check_valid_unassigned_scalars_are_retained",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_valid_unassigned_scalars_are_retained",
      "to": "edcm_alphabet_failure_is_positive_evidence"
    },
    {
      "from": "check_validity_transfer_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_validity_transfer_firewall",
      "to": "self::test_validity_transfer_fields_are_permanently_false"
    },
    {
      "from": "check_validity_transfer_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_validity_transfer_firewall",
      "to": "validity_transfer_is_forbidden"
    },
    {
      "from": "check_visible_projection_and_branch_law",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_visible_projection_and_branch_law",
      "to": "self::test_visible_projection_and_branch_law"
    },
    {
      "from": "check_visible_projection_and_branch_law",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_visible_projection_and_branch_law",
      "to": "visible_projection_is_360_degrees"
    },
    {
      "from": "check_visible_projection_and_branch_law",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_visible_projection_and_branch_law",
      "to": "python3"
    },
    {
      "from": "check_word_gonol_nesting",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_word_gonol_nesting",
      "to": "self::test_words_are_gonols_and_each_space_is_a_nesting_boundary"
    },
    {
      "from": "check_word_gonol_nesting",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_word_gonol_nesting",
      "to": "edcm_word_is_the_smallest_gonol"
    },
    {
      "from": "cycle_safe_traversal_policy",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "cycle_safe_traversal_policy",
      "to": "Erin Spencer"
    },
    {
      "from": "cycle_safe_traversal_policy",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "cycle_safe_traversal_policy",
      "to": "retained_structure_envelope"
    },
    {
      "from": "directed_carrier_floor",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "directed_carrier_floor",
      "to": "Erin Spencer"
    },
    {
      "from": "directed_carrier_floor",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "directed_carrier_floor",
      "to": "canonical_chapter_one"
    },
    {
      "from": "edcm_completion_motion_evidence",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_completion_motion_evidence",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_metapat_ordered_occurrence_profile",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_metapat_ordered_occurrence_profile",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_metapat_post_reset_bridge",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_metapat_post_reset_bridge",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_mobius_carrier_experiment",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_mobius_carrier_experiment",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_mobius_carrier_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_mobius_carrier_experiment",
      "to": "directed_carrier_floor"
    },
    {
      "from": "edcm_mobius_carrier_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_mobius_carrier_experiment",
      "to": "edcm_completion_motion_evidence"
    },
    {
      "from": "edcm_mobius_carrier_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_mobius_carrier_experiment",
      "to": "edcm_word_gonol_profile"
    },
    {
      "from": "edcm_mobius_carrier_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_mobius_carrier_experiment",
      "to": "explicit_comparison_policy_layer"
    },
    {
      "from": "edcm_mobius_carrier_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_mobius_carrier_experiment",
      "to": "first_competing_evaluator_candidate_families"
    },
    {
      "from": "edcm_native_direct_mobius_candidate",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_native_direct_mobius_candidate",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_native_direct_mobius_candidate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_native_direct_mobius_candidate",
      "to": "edcm_mobius_carrier_experiment"
    },
    {
      "from": "edcm_native_direct_mobius_candidate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_native_direct_mobius_candidate",
      "to": "edcm_word_gonol_profile"
    },
    {
      "from": "edcm_word_gonol_profile",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_word_gonol_profile",
      "to": "Erin Spencer"
    },
    {
      "from": "evaluator_candidate_laboratory",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "evaluator_candidate_laboratory",
      "to": "Erin Spencer"
    },
    {
      "from": "evaluator_candidate_laboratory",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "evaluator_candidate_laboratory",
      "to": "explicit_comparison_policy_layer"
    },
    {
      "from": "evaluator_candidate_laboratory",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "evaluator_candidate_laboratory",
      "to": "retained_structure_envelope"
    },
    {
      "from": "evaluator_candidate_laboratory",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "evaluator_candidate_laboratory",
      "to": "structural_cell_support_floor"
    },
    {
      "from": "evaluator_candidate_laboratory",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "evaluator_candidate_laboratory",
      "to": "structural_choice_policy_layer"
    },
    {
      "from": "explicit_comparison_policy_layer",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "explicit_comparison_policy_layer",
      "to": "Erin Spencer"
    },
    {
      "from": "explicit_comparison_policy_layer",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "explicit_comparison_policy_layer",
      "to": "structural_choice_policy_layer"
    },
    {
      "from": "first_competing_evaluator_candidate_families",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "first_competing_evaluator_candidate_families",
      "to": "Erin Spencer"
    },
    {
      "from": "first_competing_evaluator_candidate_families",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "first_competing_evaluator_candidate_families",
      "to": "evaluator_candidate_laboratory"
    },
    {
      "from": "first_competing_evaluator_candidate_families",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "first_competing_evaluator_candidate_families",
      "to": "reproducible_witness_experiment_pipeline"
    },
    {
      "from": "foundations_public_surface",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "Erin Spencer"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "cycle_safe_traversal_policy"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "directed_carrier_floor"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_completion_motion_evidence"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_mobius_carrier_experiment"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_native_direct_mobius_candidate"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_word_gonol_profile"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "evaluator_candidate_laboratory"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "explicit_comparison_policy_layer"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "first_competing_evaluator_candidate_families"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "reproducible_witness_experiment_pipeline"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "retained_layer_pairing_laboratory"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "retained_structure_envelope"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "structural_cell_support_floor"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "structural_choice_policy_layer"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "ucns_option_decision_registry"
    },
    {
      "from": "reproducible_witness_experiment_pipeline",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "reproducible_witness_experiment_pipeline",
      "to": "Erin Spencer"
    },
    {
      "from": "reproducible_witness_experiment_pipeline",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "reproducible_witness_experiment_pipeline",
      "to": "cycle_safe_traversal_policy"
    },
    {
      "from": "reproducible_witness_experiment_pipeline",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "reproducible_witness_experiment_pipeline",
      "to": "evaluator_candidate_laboratory"
    },
    {
      "from": "reproducible_witness_experiment_pipeline",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "reproducible_witness_experiment_pipeline",
      "to": "explicit_comparison_policy_layer"
    },
    {
      "from": "retained_layer_pairing_laboratory",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "retained_layer_pairing_laboratory",
      "to": "Erin Spencer"
    },
    {
      "from": "retained_layer_pairing_laboratory",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "retained_layer_pairing_laboratory",
      "to": "retained_structure_envelope"
    },
    {
      "from": "retained_layer_pairing_laboratory",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "retained_layer_pairing_laboratory",
      "to": "structural_cell_support_floor"
    },
    {
      "from": "retained_structure_envelope",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "retained_structure_envelope",
      "to": "Erin Spencer"
    },
    {
      "from": "retained_structure_envelope",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "retained_structure_envelope",
      "to": "structural_cell_support_floor"
    },
    {
      "from": "retained_structure_envelope",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "retained_structure_envelope",
      "to": "structural_choice_policy_layer"
    },
    {
      "from": "skill_lib_contract_audit",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "skill_lib_contract_audit",
      "to": "Erin Spencer"
    },
    {
      "from": "structural_cell_support_floor",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "structural_cell_support_floor",
      "to": "Erin Spencer"
    },
    {
      "from": "structural_cell_support_floor",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "structural_cell_support_floor",
      "to": "directed_carrier_floor"
    },
    {
      "from": "structural_choice_policy_layer",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "structural_choice_policy_layer",
      "to": "Erin Spencer"
    },
    {
      "from": "structural_choice_policy_layer",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "structural_choice_policy_layer",
      "to": "structural_cell_support_floor"
    },
    {
      "from": "ucns_option_decision_registry",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_option_decision_registry",
      "to": "Erin Spencer"
    }
  ],
  "gaps": [
    {
      "file": "archive/",
      "missing": [
        "archive tree excluded"
      ],
      "reason": "archive/ holds the pre-reset tree and its own ucns_msdmd.ts; this collection point covers the live tree only."
    }
  ],
  "repo": "The-Interdependency/ucns"
});
