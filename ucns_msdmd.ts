import { defineMsdmdCollection } from "./.agents/skills/msdmd/collection";

export default defineMsdmdCollection({
  "declarations": [
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "contract_addition_boundary, test_r_additive_under_multiply, test_concat_is_associative, test_concat_right_distributive, test_concat_left_distributivity_fails, test_concat_noncommutative, test_mutation_caught",
        "module_kind": "experiment",
        "module_name": "addition_boundary",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "none",
        "rollback": "n/a",
        "rollout": "sets the full operation set for the base geometry",
        "since": "2026-07-10",
        "storage_boundary": "none",
        "summary": "rule whether a primitive addition exists or radial growth stays derived",
        "tests": "contracts.test_addition_boundary",
        "unresolved": "none - ruled: no second primitive; concatenation stays derived",
        "user_data_boundary": "none"
      },
      "file": "archive/contracts/test_addition_boundary.py",
      "id": "addition_boundary"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "contract_multiply_associativity, test_random_triples, test_adversarial_triples, test_full_sequence_carried, test_mutation_caught",
        "module_kind": "experiment",
        "module_name": "multiply_associativity",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "none",
        "rollback": "keep as open",
        "rollout": "gates every structure name in O6 (monoid requires it)",
        "since": "2026-07-10",
        "storage_boundary": "none",
        "summary": "prove or bound (a x b) x c = a x (b x c)",
        "tests": "contracts.test_associativity_triples",
        "unresolved": "none - resolved: the payload carries the full angle sequence; mean-collapse exists only in the projection",
        "user_data_boundary": "none"
      },
      "file": "archive/contracts/test_associativity_triples.py",
      "id": "multiply_associativity"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "contract_multiply_commutativity_ruling, test_noncommutative_witness, test_projection_always_commutes, test_towers_are_central, test_long_objects_not_central, test_nontower_payload_not_central, test_mutation_caught",
        "module_kind": "experiment",
        "module_name": "commutativity_ruling",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "none",
        "rollback": "n/a",
        "rollout": "fixes whether O5 needs left AND right division (it does)",
        "since": "2026-07-10",
        "storage_boundary": "none",
        "summary": "prove non-commutative in general; characterize the commuting subclass",
        "tests": "contracts.test_commutator",
        "unresolved": "none - ruling landed: commutator lives in sequence ordering, not chirality",
        "user_data_boundary": "none"
      },
      "file": "archive/contracts/test_commutator.py",
      "id": "multiply_commutativity_ruling"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "contract_multiply_identity, test_left_identity, test_right_identity, test_none_sentinel, test_unit_group_not_identity, test_mutation_caught",
        "module_kind": "engine",
        "module_name": "multiply_identity",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "none",
        "rollback": "n/a",
        "rollout": "required for any monoid/group claim in O6",
        "since": "2026-07-10",
        "storage_boundary": "none",
        "summary": "prove the normalized factorization identity is two-sided; do not conflate it with the public-gonol SPACE/ZERO twist origin",
        "tests": "contracts.test_identity_two_sided",
        "unresolved": "bridge between the fixed-origin public gonol and ordinary normalized factorization objects remains hmmm",
        "user_data_boundary": "none"
      },
      "file": "archive/contracts/test_identity_two_sided.py",
      "id": "multiply_identity"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "test_singleton_gauge_collapse, test_product_closure, test_idempotent_census_bounded, test_local_groups_bounded, test_depth_two_ghost_home_relative, test_radius_max_law, test_breadth_plus_law, test_zero_breadth_spindle, test_first_level_fork_law, test_mutations_caught",
        "module_kind": "test",
        "module_name": "local_groups_and_relational_geometry",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "contract_local_groups_and_relational_geometry",
        "requires": "ucns_relational_geometry, ucns_canonical",
        "rollback": "remove contract and shim entry",
        "rollout": "default_enabled",
        "since": "2026-07-14",
        "storage_boundary": "none",
        "summary": "mutation-backed witnesses for idempotent towers, home-relative local groups, radius, breadth, spindle, and fork laws",
        "tests": "contracts.test_local_groups_and_geometry, tests.test_base_geometry_contracts",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/contracts/test_local_groups_and_geometry.py",
      "id": "local_groups_relational_geometry_contracts"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "contract_multiply_well_defined, test_totality_and_grading, test_representation_independence, test_empty_carrier_boundary, test_mutation_caught",
        "module_kind": "engine",
        "module_name": "multiply_totality",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "none",
        "rollback": "revert to empirical closure",
        "rollout": "backbone; everything downstream assumes it",
        "since": "2026-07-10",
        "storage_boundary": "none",
        "summary": "prove multiply is total and canonical (representation-independent) at all depths",
        "tests": "contracts.test_multiply_canonical",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/contracts/test_multiply_canonical.py",
      "id": "multiply_well_defined"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "contract_division_theory, test_enumerator_exhaustive_universe, test_soundness_random, test_length_gate, test_multiplicity_towers, test_flat_divisor_cancellativity, test_cancellativity_dichotomy, test_v06_scope_correction, test_greedy_left_quotient_still_sound, test_mutation_caught",
        "module_kind": "engine",
        "module_name": "division_theory",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "none",
        "rollback": "keep left_factors as standing hmmm",
        "rollout": "this IS \"division and the like\"",
        "since": "2026-07-10",
        "storage_boundary": "read",
        "summary": "left/right quotient solvability and multiplicity for multiply",
        "tests": "contracts.test_quotient_solvability",
        "unresolved": "AlignedComplete-domain cancellativity proof remains a formal/ obligation; canonical-choice procedure among multiple quotients remains open (structural, per O6)",
        "user_data_boundary": "none"
      },
      "file": "archive/contracts/test_quotient_solvability.py",
      "id": "division_theory"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "contract_structure_naming, test_monoid_axioms, test_grading, test_unit_group_is_z2, test_not_cancellative, test_center_sample, test_idempotents_exist, test_mutation_caught",
        "module_kind": "engine",
        "module_name": "structure_theorem",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "none",
        "requires": "multiply_well_defined, multiply_identity, multiply_associativity, multiply_commutativity_ruling, division_theory",
        "rollback": "n/a",
        "rollout": "base geometry complete == this theorem lands",
        "since": "2026-07-10",
        "storage_boundary": "none",
        "summary": "name the algebraic object (UCNS, multiply) given O1-O5 and the r-grading",
        "tests": "contracts.test_structure_axioms",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/contracts/test_structure_axioms.py",
      "id": "structure_naming"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "adapter",
        "module_name": "a0_safe",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "identity, describe, canonical, factor, UCNSObjectRecord, FactorizationResult",
        "requires": "ucns_object_record, ucns_factorization_result, ucns_serialization, ucns_canonical",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "A0-safe public facade for inspecting, identifying, canonicalizing, and factoring UCNS objects via evidence-bearing scoped envelopes.",
        "tests": "ucns_recursive/tests/test_a0_safe.py, tests/test_certified_negative_results.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/a0_safe.py",
      "id": "ucns_a0_safe"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_object_to_data, _object_from_data, _require",
        "module_kind": "adapter",
        "module_name": "bridge",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "BRIDGE_SCHEMA, BRIDGE_SCHEMA_VERSION, BridgeValidationError, BridgeImport, export_bridge_record, import_bridge_record",
        "requires": "ucns_canonical, ucns_serialization",
        "rollback": "remove module and its re-exports; sibling adapters fall back to repo-local encodings",
        "rollout": "default_enabled additive public API; sibling repos consume the record shape, not UCNS internals",
        "since": "2026-07-12",
        "storage_boundary": "none",
        "summary": "Versioned neutral bridge record plus fail-closed import/export adapter between actual UCNSObjects and sibling repositories, preserving equality and stable hash and carrying provenance without theorem status.",
        "tests": "tests/test_bridge_round_trip.py, tests/test_stack_contract_suite.py, tests/test_bridge_certification_boundary.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/bridge.py",
      "id": "ucns_bridge"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "call": "contracts.test_addition_boundary.contract_addition_boundary",
        "class": "correctness",
        "given": "the derived candidate addition (top-level sequence concatenation)",
        "then": "no second primitive operation exists in the base geometry; r is"
      },
      "file": "archive/ucns/canonical.py",
      "id": "addition_boundary"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "call": "contracts.test_associativity_triples.contract_multiply_associativity",
        "class": "correctness",
        "given": "TRIPLES of normalized objects at mixed depths, including",
        "then": "multiply(multiply(a, b), c) == multiply(a, multiply(b, c));"
      },
      "file": "archive/ucns/canonical.py",
      "id": "multiply_associativity"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "call": "contracts.test_commutator.contract_multiply_commutativity_ruling",
        "class": "correctness",
        "given": "normalized objects; the separating witnesses B1 = [0,1] and",
        "then": "multiply is non-commutative in general; the (r, theta, z, w)"
      },
      "file": "archive/ucns/canonical.py",
      "id": "multiply_commutativity_ruling"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "call": "contracts.test_identity_two_sided.contract_multiply_identity",
        "class": "correctness",
        "given": "the normalized factorization identity e =",
        "then": "multiply(e, a) == a and multiply(a, e) == a (two-sided, checked"
      },
      "file": "archive/ucns/canonical.py",
      "id": "multiply_identity"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "call": "contracts.test_multiply_canonical.contract_multiply_well_defined",
        "class": "correctness",
        "given": "ordinary normalized nonempty factorization UCNSObjects at mixed",
        "then": "multiply is total, its output is normalized with n_dec a multiple of"
      },
      "file": "archive/ucns/canonical.py",
      "id": "multiply_well_defined"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "call": "contracts.test_structure_axioms.contract_structure_naming",
        "class": "correctness",
        "given": "obligations O1-O5 discharged (well-definedness, identity,",
        "then": "(nonempty normalized objects, multiply, e) is a non-commutative,"
      },
      "file": "archive/ucns/canonical.py",
      "id": "structure_naming"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "normalize, _compute_n_min, _star, _disk_flip",
        "module_kind": "engine",
        "module_name": "canonical",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "UCNSObject, multiply, is_unit, is_multiplicative_unit, lcm, UNIT",
        "requires": "none",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Core UCNS algebraic objects and operations - UCNSObject, the ordered-concatenation product, and unit predicates.",
        "tests": "ucns_recursive/tests/test_depth2_full_domain.py, ucns_recursive/tests/test_canonical_constructor_validation.py, tests/test_canonical_constructor_validation.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/canonical.py",
      "id": "ucns_canonical"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "service",
        "module_name": "canonical_factorization",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "enumerate_factorizations, canonical_factorization, canonical_key, SEQ_PRIME",
        "requires": "ucns_carrier_support_pruning",
        "rollback": "remove module and its re-exports",
        "rollout": "additive module; no existing surface modified",
        "since": "2026-06-10",
        "storage_boundary": "none",
        "summary": "Deterministic canonical choice among all catalogue-bounded left-factor factorizations of P, selected by lexicographic canonical-bytes order over a v0.6-complete enumeration.",
        "tests": "ucns.tests.test_canonical_factorization",
        "unresolved": "canonical selection under payload-catalogue (factor_search_v08) semantics",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/canonical_factorization.py",
      "id": "ucns_canonical_factor_selection"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_obj_key",
        "module_kind": "engine",
        "module_name": "catalogue",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "build_catalogue_d1, build_catalogue_d2_oracle",
        "requires": "ucns_canonical, ucns_domains",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Catalogue builders enumerating canonical depth-1 oracle atoms and depth-2 oracle-class UCNSObjects for factor decomposition.",
        "tests": "tests.test_catalogue, tests.test_oracle_catalogue_equivalence",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/catalogue.py",
      "id": "ucns_catalogue"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_required_catalogue_for_domain, _structural_tokens",
        "module_kind": "engine",
        "module_name": "catalogue_coverage",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "CatalogueCoverage, CATALOGUE_COVERAGE_RULE_VERSION, COVERAGE_CANONICAL_EXACT, COVERAGE_CANONICAL_SUPERSET, COVERAGE_UNCERTIFIED, check_catalogue_coverage, validate_catalogue_coverage, coverage_matches_search_report",
        "requires": "ucns_domains, ucns_factor_search_v08, ucns_serialization",
        "rollback": "remove module and public re-exports",
        "rollout": "additive evidence surface; no FactorizationResult integration",
        "since": "2026-07-11",
        "storage_boundary": "none",
        "summary": "Recomputable catalogue-coverage records bound to an exact supplied catalogue fingerprint, domain label, and required catalogue rule version; makes no primality-certification claim.",
        "tests": "tests/test_catalogue_coverage.py",
        "unresolved": "negative-result certification deliberately remains separate",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/catalogue_coverage.py",
      "id": "ucns_catalogue_coverage"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_recursive_obj_key",
        "module_kind": "engine",
        "module_name": "catalogue_d3",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "is_in_oracle_class_d3, D3CatalogueResult, build_catalogue_d3_oracle",
        "requires": "ucns_canonical, ucns_domains, ucns_catalogue",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "DRAFT depth-3 oracle-class predicate and bounded catalogue enumerator (build_catalogue_d3_oracle) carrying a coverage attestation against Lemma 8.",
        "tests": "ucns.tests.test_catalogue_d3",
        "unresolved": "DRAFT - depth-3 constructive-vs-multiplicative D'' coverage equivalence, payload_basis/chirality interaction, and size-budget exhaustion gating are all unproven (hmmm A/B/C in module docstring)",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/catalogue_d3.py",
      "id": "ucns_catalogue_d3"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "service",
        "module_name": "catalogue_pruning",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "PAYLOAD_PRUNING_RULE_NAME, PAYLOAD_PRUNING_RULE_VERSION, PAYLOAD_PRUNING_PRESERVES_COVERAGE, prime_support, carrier_lcm, prune_catalogue, payload_support, prune_payload_catalogue",
        "requires": "none",
        "rollback": "pass prune=False to factor_search_v08, or remove the module and the prune kwarg",
        "rollout": "prune_catalogue opt-in for left-factor catalogues; prune_payload_catalogue default-on inside factor_search_v08 (prune=False escape hatch)",
        "since": "2026-06-09",
        "storage_boundary": "none",
        "summary": "Sound named and versioned catalogue pre-filter removing factor candidates whose carrier prime support escapes the product carrier's prime support, justified by the Carrier-LCM Law.",
        "tests": "ucns.tests.test_catalogue_pruning, tests/test_factor_search_provenance.py, tests/test_certified_negative_results.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/catalogue_pruning.py",
      "id": "ucns_carrier_support_pruning"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "adapter",
        "module_name": "core",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "UCN, TAU",
        "requires": "none",
        "rollback": "remove after all legacy circular-embedding consumers migrate",
        "rollout": "compatibility_only",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "legacy local 2pi circular coordinate for periodic embeddings; explicitly not the fixed-origin public gonol or complete UCNS number-system primitive",
        "tests": "tests.test_core",
        "unresolved": "no public-gonol bridge is defined; this surface must remain scoped as a local 2pi coordinate",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/core.py",
      "id": "ucns_core"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "call": "contracts.test_quotient_solvability.contract_division_theory",
        "class": "correctness",
        "given": "normalized nonempty A, P (left) or B, P (right) of finite depth",
        "then": "left_quotients/right_quotients return exactly the set of X over"
      },
      "file": "archive/ucns/division_theory.py",
      "id": "division_theory"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "left_quotients, right_quotients, _left_payload_solutions, _right_payload_solutions, _dedup",
        "module_kind": "engine",
        "module_name": "division_theory",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "none",
        "requires": "ucns_canonical",
        "rollback": "keep ucns.left_quotient greedy primitives as the standing surface",
        "rollout": "this IS \"division and the like\"; importable, not re-exported from ucns/__init__",
        "since": "2026-07-10",
        "storage_boundary": "none",
        "summary": "left/right quotient solvability and multiplicity for multiply - complete finite solution-set enumeration",
        "tests": "contracts.test_quotient_solvability",
        "unresolved": "none for enumeration; AlignedComplete cancellativity proof remains a formal/ obligation",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/division_theory.py",
      "id": "division_theory"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "domain_status",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "DomainProofStatus, DomainStatusMetadata, VERIFIED_DOMAIN_LABELS, domain_status_metadata, status_for_object, is_verified_domain_label, seq_prime_requires_scope",
        "requires": "ucns_canonical",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Typed domain-level prerequisite metadata; bare labels never certify SEQ-PRIME, and result-level certainty is delegated to ucns.factorization_result.",
        "tests": "ucns_recursive/tests/test_domain_status.py, tests/test_certified_negative_results.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/domain_status.py",
      "id": "ucns_domain_status"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_generate_canonical_catalogue, _oracle_atom_key, _CANONICAL_ORACLE_KEYS",
        "module_kind": "engine",
        "module_name": "domains",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "DEPTH_MAX, A_PLUS_MAX, N_MIN_MAX, S2, ORACLE_ATOM_PAYLOADS, ORACLE_CATALOGUE_RULE_VERSION, generate_payload_catalogue, in_domain, depth_of, is_oracle_atom, is_in_oracle_class, verified_domain_status",
        "requires": "ucns_canonical",
        "rollback": "restore geometric-bounds oracle classification (reintroduces catalogue mismatch)",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Defines the frozen depth-2 geometry, canonical oracle catalogue, and exact catalogue-membership predicates used to scope oracle claims.",
        "tests": "tests/test_oracle_catalogue_equivalence.py, ucns_recursive/tests/test_depth2_full_domain.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/domains.py",
      "id": "ucns_domains"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_to_signal",
        "module_kind": "adapter",
        "module_name": "embedding",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "UCNEmbedding",
        "requires": "ucns_epicycle",
        "rollback": "remove after legacy consumers migrate to explicitly named embedding surfaces",
        "rollout": "compatibility_only",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "legacy FFT phase-vector embedding over local 2pi coordinates; explicitly not the public-gonol encoder or a semantic/theorem surface",
        "tests": "tests.test_embedding",
        "unresolved": "no public-gonol or semantic bridge is defined",
        "user_data_boundary": "read"
      },
      "file": "archive/ucns/embedding.py",
      "id": "ucns_embedding"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_next_pow2, _fft_inplace",
        "module_kind": "adapter",
        "module_name": "epicycle",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "fft, ifft, EpicycleDecomposition",
        "requires": "none",
        "rollback": "remove after legacy FFT embedding consumers migrate",
        "rollout": "compatibility_only",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "legacy radix-2 FFT and epicycle signal decomposition over local 2pi phases; not the public-gonol frame",
        "tests": "tests.test_epicycle",
        "unresolved": "no public-gonol bridge is defined",
        "user_data_boundary": "read"
      },
      "file": "archive/ucns/epicycle.py",
      "id": "ucns_epicycle"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "adapter",
        "module_name": "evidence",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "UCNSEvidence, no_proof_status, evidence_from_construction, evidence_from_bridge_import, evidence_from_factorization_result",
        "requires": "ucns_canonical, ucns_factorization_result, ucns_domain_status, ucns_bridge",
        "rollback": "remove module and its re-exports; consumers fall back to reading FactorizationResult directly",
        "rollout": "default_enabled additive public API",
        "since": "2026-07-12",
        "storage_boundary": "none",
        "summary": "Non-boolean downstream evidence envelope distinguishing construction success, search exhaustion, validated coverage, certified domain-relative negatives, theorem-layer status vocabulary, and absence of proof status.",
        "tests": "tests/test_stack_contract_suite.py, tests/test_bridge_certification_boundary.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/evidence.py",
      "id": "ucns_evidence"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_bytes, _digest, _exact_fields, _strict_bool, _strict_int, _strict_str, _strict_string_tuple, _strict_hex_digest, _status_values",
        "module_kind": "schema",
        "module_name": "evidence_envelope",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "BRIDGE_RECORD_SCHEMA_ID, BRIDGE_RECORD_SCHEMA_VERSION, FACTORIZATION_EVIDENCE_SCHEMA_ID, FACTORIZATION_EVIDENCE_SCHEMA_VERSION, UCNSBridgeRecord, UCNSFactorizationEvidence, bridge_record, factorization_evidence",
        "requires": "ucns_object_record, ucns_factorization_result, ucns_serialization, ucns_domain_status",
        "rollback": "remove envelope exports while preserving object_record and factorization_result",
        "rollout": "default_enabled",
        "since": "2026-07-12",
        "storage_boundary": "deterministic serialization only; no persistence",
        "summary": "versioned deterministic bridge records and factorization evidence envelopes binding UCNS stable identity, canonical serialization, typed domain status, exhaustive-search provenance, catalogue coverage, pruning policy, and negative-certification scope.",
        "tests": "tests.test_evidence_envelope",
        "unresolved": "cryptographic producer authentication is not provided; evidence digests are tamper-evident content identities only",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/evidence_envelope.py",
      "id": "ucns_evidence_envelope"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_prepare_search_catalogues, _search_exhaustive",
        "module_kind": "engine",
        "module_name": "factor_search_v08",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "factor_search_v08, factor_search_report, FactorSearchReport, payload_catalogue_fingerprint",
        "requires": "ucns_canonical, ucns_domains, ucns_host_recovery, ucns_payload_system, ucns_witness_matrix, ucns_serialization, ucns_carrier_support_pruning",
        "rollback": "remove report API while retaining factor_search_v08 and _search_exhaustive",
        "rollout": "factor_search_v08 unchanged; factor_search_report additive",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Exhaustive catalogue-bounded factorization with a compatibility sentinel API and a provenance-bearing search report that makes no certification claim.",
        "tests": "tests/test_exhaustive_factor_search.py, tests/test_factor_search_provenance.py, tests/test_certified_negative_results.py, ucns_recursive/tests/test_depth2_oracle.py",
        "unresolved": "negative-result certification lives only in ucns.factorization_result",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/factor_search_v08.py",
      "id": "ucns_factor_search_v08"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_pruning_is_recognized, _negative_certification_reasons, _claim_scope",
        "module_kind": "engine",
        "module_name": "factorization_result",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "FactorizationResultKind, FactorizationResult, NEGATIVE_CERTIFICATION_POLICY_VERSION, factorization_result",
        "requires": "ucns_canonical, ucns_domain_status, ucns_domains, ucns_factor_search_v08, ucns_catalogue_coverage, ucns_carrier_support_pruning, ucns_serialization",
        "rollback": "retain provenance and coverage evidence but set negative_result_certified and seq_prime_is_absolute false",
        "rollout": "default_enabled for A0-facing envelopes; raw factor_search_v08 remains catalogue-relative",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "A0-facing factorization envelope that certifies negative results only from frozen-domain membership, validated catalogue coverage, exact search-report binding, exhaustive untruncated search, recognized sound pruning, a complete declared domain, and a non-unit target.",
        "tests": "tests/test_certified_negative_results.py, tests/test_one_shot_catalogue.py, ucns_recursive/tests/test_factorization_result.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/factorization_result.py",
      "id": "ucns_factorization_result"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_r, _rho, _theta, _zw, ThetaDegenerate",
        "module_kind": "engine",
        "module_name": "geometry_bridge",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "GeometricPoint, ucns_a_to_g, compose, homomorphism_check, HomomorphismResult, check_injectivity",
        "requires": "ucns.canonical, ucns.relational_geometry",
        "rollback": "remove export from ucns/__init__.py",
        "rollout": "default_enabled",
        "storage_boundary": "none",
        "summary": "commutative audit projection via recursive radius, breadth, spinor angle, and chirality coordinates",
        "tests": "ucns_recursive.tests.test_geometry_bridge, contracts.test_local_groups_and_geometry",
        "unresolved": "injectivity-proof-analytical, degenerate-theta-canonical-form, quaternionic-axis-lift",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/geometry_bridge.py",
      "id": "ucns_geometry_bridge"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "host_recovery",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "recover_host_angles, recover_face_structures",
        "requires": "ucns_canonical",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Recovers the candidate A/B host angle sequences and enumerates consistent face-bit assignments from a normalised product object P.",
        "tests": "ucns_recursive/tests/test_depth2_full_domain.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/host_recovery.py",
      "id": "ucns_host_recovery"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_left_quotient_payload",
        "module_kind": "engine",
        "module_name": "left_quotient",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "left_quotient, right_quotient",
        "requires": "ucns_canonical",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Constructive left/right quotient primitives implementing the v0.6 left-quotient completeness theorem; recovers B (or A) from a product, else None.",
        "tests": "ucns.tests.test_left_quotient",
        "unresolved": "v0.6 completeness scope-corrected 2026-07-10 (counterexample; complete on flat divisors only; full enumeration in ucns.division_theory); right_quotient dual additionally uses the left payload helper and misses more",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/left_quotient.py",
      "id": "ucns_left_quotient"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "mobius",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "MobiusTransform, poincare_distance, disk_to_circle, circle_to_disk",
        "requires": "none",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Mobius (bilinear) transformations of the Poincare unit disk plus hyperbolic-distance and disk/circle projection helpers.",
        "tests": "tests.test_mobius",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/mobius.py",
      "id": "ucns_mobius"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "object_record",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "UCNSObjectRecord, object_record",
        "requires": "ucns_canonical, ucns_domain_status, ucns_domains, ucns_serialization",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Builds a self-describing inspection record (canonical identity, domain-status metadata, structural facts) for any UCNS object without invoking factorization.",
        "tests": "ucns.tests.test_object_record",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/object_record.py",
      "id": "ucns_object_record"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_globally_consistent",
        "module_kind": "engine",
        "module_name": "payload_system",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "normalize_payload_catalogue, iter_payload_system_solutions, solve_payload_system",
        "requires": "ucns_canonical",
        "rollback": "restore the greedy first-quotient solver",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Normalizes payload catalogues and exhaustively enumerates every assignment satisfying the coupled product equations, with a first-solution compatibility wrapper.",
        "tests": "tests/test_exhaustive_factor_search.py, tests/test_factor_search_provenance.py, ucns_recursive/tests/test_depth2_full_domain.py",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/payload_system.py",
      "id": "ucns_payload_system"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "UPPERCASE, LOWERCASE, DIGITS_ODD, DIGITS_EVEN, PAIRED_OPEN, PAIRED_CLOSE, UNPAIRED_ASCII, UNPAIRED_OPS, UNPAIRED_ALL",
        "module_kind": "engine",
        "module_name": "public_gonol",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "GonalSpec, build_gonal, validate_gonal, print_gonal, EXAMPLE_157, PUBLIC_GONOL_157, make_example_157, get_default, public_gonol_sha256, PUBLIC_GONOL_SHA256",
        "requires": "none",
        "rollback": "remove public exports after downstream consumers return to the pinned a0-betatest source",
        "rollout": "default_enabled",
        "since": "2026-07-16",
        "storage_boundary": "none",
        "summary": "owns the exact public 157-gonal arrangement and fixed SPACE/ZERO twist origin promoted from a0-betatest",
        "tests": "tests.test_public_gonol",
        "unresolved": "hmmm \u2014 no continuous-angle projection is ratified by this promotion",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/public_gonol.py",
      "id": "ucns_public_gonol"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "schema",
        "module_name": "public_gonol_faces",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "face, chirality, n_plus, n_minus, ARITY, ORIGIN, UPPER_ARC_RANGE, LOWER_ARC_RANGE",
        "requires": "ucns_public_gonol",
        "rollback": "remove exports after reverting consumers to the pinned a0-betatest source",
        "rollout": "default_enabled",
        "since": "2026-07-16",
        "storage_boundary": "none",
        "summary": "preserves the exact public face, chirality, adjacency, arity, and fixed origin formulas from a0-betatest",
        "tests": "tests.test_public_gonol",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/public_gonol_faces.py",
      "id": "ucns_public_gonol_faces"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_ARRANGEMENT, _VERTEX_OF_CHAR",
        "module_kind": "engine",
        "module_name": "public_gonol_lifted_path",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "encode_text_path, decode_text_path, vertex_of_char, char_of_vertex, is_seam_event, path_vertices, CarrierCharError, ARITY, ORIGIN",
        "requires": "ucns_public_gonol, ucns_public_gonol_faces",
        "rollback": "remove exports after reverting consumers to the pinned a0-betatest source",
        "rollout": "default_enabled",
        "since": "2026-07-16",
        "storage_boundary": "none",
        "summary": "losslessly encodes and decodes text as the exact lifted traversal over the fixed-origin public gonol",
        "tests": "tests.test_public_gonol",
        "unresolved": "none",
        "user_data_boundary": "read"
      },
      "file": "archive/ucns/public_gonol_lifted_path.py",
      "id": "ucns_public_gonol_lifted_path"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "public_gonol_mirror",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "mirror_of",
        "requires": "ucns_public_gonol",
        "rollback": "remove export after reverting consumers to the pinned a0-betatest source",
        "rollout": "default_enabled",
        "since": "2026-07-16",
        "storage_boundary": "none",
        "summary": "preserves the exact origin-fixed public-gonol mirror involution from a0-betatest",
        "tests": "tests.test_public_gonol",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/public_gonol_mirror.py",
      "id": "ucns_public_gonol_mirror"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "public_gonol_private",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "PrivateGonal",
        "requires": "ucns_public_gonol, ucns_public_gonol_faces",
        "rollback": "remove export after reverting consumers to the pinned a0-betatest source",
        "rollout": "default_enabled",
        "since": "2026-07-16",
        "storage_boundary": "none",
        "summary": "preserves the exact A0 private phase and permutation law that fixes the public SPACE/ZERO twist origin",
        "tests": "tests.test_public_gonol",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/public_gonol_private.py",
      "id": "ucns_public_gonol_private"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_byte_to_angle, _angle_to_byte, _safe_n_dec, _make_sentinel_cells, _encode_bytes, _encode_list, _encode_dict, _count_leading_sentinels",
        "module_kind": "engine",
        "module_name": "recursive_codec",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "recursive_encode, recursive_decode, EncodingError",
        "requires": "ucns_canonical",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Recursive encoder/decoder between Python values (bytes/list/tuple/dict and coercible leaves) and UCNSObject, with type recovered from leading-sentinel count.",
        "tests": "ucns.tests.test_recursive_codec",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/recursive_codec.py",
      "id": "ucns_codec"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "find_right_factor_or_sentinel, find_left_factor_or_sentinel",
        "module_kind": "engine",
        "module_name": "recursive_quotient",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "find_left_factor, find_right_factor, left_quotient, right_quotient",
        "requires": "ucns_canonical, ucns_left_quotient",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Payload-level single-equation factor finders (find_left_factor / find_right_factor) that enumerate a candidate catalogue, plus re-exports of the left/right quotient primitives.",
        "tests": "ucns.tests.test_left_quotient",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/recursive_quotient.py",
      "id": "ucns_quotient"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_face_tower_bits",
        "module_kind": "engine",
        "module_name": "relational_geometry",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "recursive_radius, breadth, first_level_fork_count, is_normalized, zero_faced_tower, face_tower, idempotent_tower_depth, is_local_group_pair, is_local_group_member, local_group_elements",
        "requires": "ucns_canonical",
        "rollback": "remove module and dependent contracts",
        "rollout": "default_enabled",
        "since": "2026-07-14",
        "storage_boundary": "none",
        "summary": "recursive radius, breadth, fork observables, idempotent towers, and home-relative local-group predicates",
        "tests": "contracts.test_local_groups_and_geometry, tests.test_base_geometry_contracts",
        "unresolved": "full fork-profile counting convention; METAPAT fork admissibility remains downstream",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/relational_geometry.py",
      "id": "ucns_relational_geometry"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_fraction_to_data",
        "module_kind": "engine",
        "module_name": "serialization",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "CANONICAL_SERIALIZATION_VERSION, DEFAULT_HASH_ALGORITHM, canonical_data, canonical_json, canonical_bytes, stable_hash, stable_hash_bytes",
        "requires": "ucns_canonical",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Canonical deterministic JSON serialization and stable SHA-256 hashing for UCNS recursive objects, mirroring UCNSObject equality policy for content addressing and identity.",
        "tests": "ucns.tests.test_serialization",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/serialization.py",
      "id": "ucns_serialization"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_check_same_length",
        "module_kind": "adapter",
        "module_name": "similarity",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "phase_cosine, arc_distance, hyperbolic_cosine, top_k_overlap",
        "requires": "none",
        "rollback": "remove after legacy embedding consumers migrate",
        "rollout": "compatibility_only",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "similarity and distance helpers for legacy local 2pi phase-vector embeddings; not public-gonol geometry",
        "tests": "tests.test_similarity",
        "unresolved": "no public-gonol or semantic metric bridge is defined",
        "user_data_boundary": "read"
      },
      "file": "archive/ucns/similarity.py",
      "id": "ucns_similarity"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "store",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "UCNSStore, Match, OutOfDomainError",
        "requires": "ucns_canonical, ucns_domains, ucns_left_quotient, ucns_codec",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "UCNSStore - an in-memory keyed corpus of UCNSObjects with proof-backed algebraic retrieval (left_factors, is_left_factor, factor_decompose) and optional verified-domain enforcement.",
        "tests": "ucns.tests.test_store",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/store.py",
      "id": "ucns_store"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "witness_matrix",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "Witness, WitnessMatrix, build_witness_matrix",
        "requires": "ucns_canonical",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Witness and WitnessMatrix types plus build_witness_matrix; verifies per-cell factor products and row/column global consistency for a host factorisation candidate.",
        "tests": "ucns.tests.test_failure_boundary_e109",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns/witness_matrix.py",
      "id": "ucns_witness_matrix"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "feature_flag": "A0_UCNS_CACHE for downstream a0-betatest integration",
        "internal_surface": "dependencies, keys, entries, primitive_streams, braider, store, policy, instrumentation",
        "module_kind": "experiment",
        "module_name": "ucns_cache",
        "network_boundary": "none",
        "owner": "Erin Spencer / Codex",
        "public_surface": "UCNSCacheKey, UCNSCacheEntry, PrimitiveStreams, BraiderOutput, CacheLookupResult, UCNSCacheStore, make_ucns_cache_key, derive_primitive_streams, braid_streams, factor_reuse_candidates",
        "rollback": "remove ucns_cache package, docs/ucns-native-caching.md, scripts/bench_ucns_cache.py, and tests/test_ucns_cache_*.py",
        "rollout": "opt-in prototype / downstream A0_UCNS_CACHE integration",
        "since": "2026-06-28",
        "storage_boundary": "none",
        "summary": "Software-only UCNS-native cache prototype for canonical keying, primitive streams, braider identity, and conservative structural reuse.",
        "tests": "tests/test_ucns_cache_keys.py, tests/test_ucns_cache_streams.py, tests/test_ucns_cache_store.py, tests/test_ucns_cache_factor_reuse.py",
        "unresolved": "a0-betatest checkout unavailable in this workspace, downstream inference hook not installed, stable shared-braid fixture pending",
        "user_data_boundary": "none"
      },
      "file": "archive/ucns_cache/entries.py",
      "id": "ucns_native_cache"
    },
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
        "public_surface": "option decisions, EDCM observation, completion-motion, v0.14 full-corpus execution evidence, v0.15 full-carrier attachment evidence, v0.16 assignment-admission evidence, v0.17 gonol-initiation and Structural Null evidence, v0.18 explicit geometric-assignment evidence, v0.19 authority-bound ordered source-coordinate derivation evidence, v0.5 carrier experiment, v0.6 native direct-Mobius candidate, v0.7 bounded root-loop cover chart, v0.9 exact-rational transverse-envelope repair, v0.10 bounded carrier-coordinate admissibility experiment, v0.11 exact-coordinate representation boundary, v0.13 partial initiation boundary, carrier, structure, policy, envelope, comparison, traversal, laboratory, layer-pairing, experiment, candidate, and bounded downstream profile names listed in __all__",
        "requires": "ucns_option_decision_registry, edcm_word_gonol_profile, edcm_completion_motion_evidence, edcm_full_corpus_execution_gate, edcm_full_carrier_attachment_evidence, edcm_assignment_admission_boundary, edcm_gonol_initiation_structural_null_boundary, edcm_explicit_geometric_assignment_boundary, edcm_source_coordinate_derivation_boundary, edcm_mobius_carrier_experiment, edcm_native_direct_mobius_candidate, edcm_root_loop_cover_chart_candidate, edcm_exact_rational_transverse_envelope_experiment, edcm_carrier_coordinate_admissibility_experiment, edcm_exact_coordinate_representation_boundary, edcm_partial_initiation_boundary, directed_carrier_floor, structural_cell_support_floor, structural_choice_policy_layer, retained_structure_envelope, explicit_comparison_policy_layer, cycle_safe_traversal_policy, evaluator_candidate_laboratory, retained_layer_pairing_laboratory, reproducible_witness_experiment_pipeline, first_competing_evaluator_candidate_families",
        "rollback": "remove completion-motion and downstream profile exports while preserving foundations and research surfaces",
        "rollout": "importable decisions, exact EDCM word-gonol observation profile, trajectory-first completion-motion evidence, fail-closed v0.14 full-corpus execution receipts, nonselecting v0.15 analytic and bounded attachment evidence, nonselecting v0.16 assignment-admission evidence, nonselecting v0.17 origin separation and gonol-initiation evidence, nonselecting v0.18 explicit-input exact circle-candidate application, nonselecting v0.19 authority-bound ordered source-coordinate derivation, candidate-neutral v0.5 carrier experiment, nonselecting v0.6 direct-Mobius candidate, nonselecting v0.7 bounded root-loop chart, nonselecting v0.9 exact-rational transverse-envelope repair, nonselecting v0.10 bounded carrier-coordinate admissibility experiment, nonselecting v0.11 exact-coordinate representation boundary, nonselecting v0.13 partial initiation boundary, compatibility profile, and research infrastructure",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "exports the UCNS decision registry, EDCM word-gonol, completion-motion, full-corpus execution, bounded full-carrier evidence, v0.16 assignment admission, v0.17 gonol initiation, v0.18 explicit exact-coordinate application, and v0.19 ordered-source coordinate derivation with current foundations and reproducible candidate-research infrastructure",
        "tests": "tests/test_public_surface.py and all source-specific test modules",
        "unresolved": "selection and cross-scope composition of the v0.19 source-coordinate candidate, total Structural Null topology, proof-assistant formalization, circle-epicycle-disk-sphere transitions, higher-gonol composition, non-SPACE out-of-alphabet treatment, canonical structural equivalence, canonical M, canonical B, complete UCNS object",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/__init__.py",
      "id": "foundations_public_surface"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "equal-content occurrences enter one admission trace",
        "since": "2026-07-31",
        "then": "each occurrence retains its own admission and receipt identity in exact input order even when subject digests are equal"
      },
      "file": "src/ucns/assignment_boundary.py",
      "id": "assignment_admission_preserves_occurrence_order_and_multiplicity"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an arbitrary-domain observed element is admitted for assignment research",
        "since": "2026-07-31",
        "then": "a named versioned ContentAdapter creates an isolated SubjectRecord and its digest is labeled evidence identity only, never a geometric coordinate"
      },
      "file": "src/ucns/assignment_boundary.py",
      "id": "assignment_admission_requires_explicit_domain_adapter"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the v0.16 report joins admission evidence to the v0.15 carrier report",
        "since": "2026-07-31",
        "then": "arbitrary-element geometry, the total Structural Null relationship, carrier selection, EDCM activation, and METAPAT activation remain absent"
      },
      "file": "src/ucns/assignment_boundary.py",
      "id": "assignment_boundary_does_not_complete_initiation_or_activate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "content digest, runtime hash, repr, object identity, or the historical A0 Blake2 phase lanes are proposed as a universal assignment law",
        "since": "2026-07-31",
        "then": "the mechanism can be retained only as an explicit rejected outcome and supplies no GeometricAssignment"
      },
      "file": "src/ucns/assignment_boundary.py",
      "id": "assignment_identity_mechanisms_cannot_derive_geometry"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "an explicitly admitted occurrence reaches the v0.16 assignment boundary",
        "since": "2026-07-31",
        "then": "exactly one tagged outcome is recorded as unresolved, explicit supplied candidate, or rejected mechanism and invalid combinations fail closed"
      },
      "file": "src/ucns/assignment_boundary.py",
      "id": "assignment_outcome_is_total_and_exclusive_over_admitted_evidence"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a caller supplies an explicit GeometricAssignment for one admitted occurrence",
        "since": "2026-07-31",
        "then": "the exact relation, law identity, standing, orientation, sidedness, parameters, and evidence remain linked without derivation, selection, or canonical promotion"
      },
      "file": "src/ucns/assignment_boundary.py",
      "id": "supplied_assignment_remains_candidate_evidence"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "fixed AA01-AA07 evidence construction and exact validation helpers",
        "module_kind": "experiment",
        "module_name": "assignment_boundary",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "ObservedElementAdmission, AssignmentOutcomeReceipt, AssignmentAdmissionTrace, AssignmentAdmissionBoundaryReport, AssignmentDisposition, RejectedAssignmentMechanism, AssignmentFalsifierResult, AssignmentEvidenceStanding, admit_observed_element, record_assignment_outcome, run_v016_assignment_admission_boundary_experiment",
        "requires": "reproducible_witness_experiment_pipeline, edcm_completion_motion_evidence, edcm_full_carrier_attachment_evidence",
        "rollback": "remove this module, exports, tests, and v0.16 document while retaining v0.15 carrier evidence and the reusable ContentAdapter/SubjectRecord infrastructure",
        "rollout": "nonselecting v0.16 admission and assignment-outcome evidence over explicitly adapted occurrences; no universal assignment law, total Structural Null relationship, EDCM activation, or METAPAT activation",
        "since": "2026-07-31",
        "storage_boundary": "none",
        "summary": "admits arbitrary-domain observed-element occurrences through explicit content adapters and records one total tagged assignment outcome without deriving geometry from evidence identity",
        "tests": "tests/test_assignment_boundary.py",
        "unresolved": "arbitrary observed-element geometric assignment, total Structural Null initiation relationship, circle-epicycle-disk-sphere transitions, higher-gonol composition, scoped completion, canonical faithful breadth, and carrier selection",
        "user_data_boundary": "adapter-produced bytes and an isolated subject snapshot remain exact evidence; their digest never becomes a geometric coordinate"
      },
      "file": "src/ucns/assignment_boundary.py",
      "id": "edcm_assignment_admission_boundary"
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
        "class": "evidence",
        "given": "a candidate loses transverse sign, collapses fibers, or fails to commute with root motion",
        "since": "2026-07-29",
        "then": "the exact collision or motion witness remains in its result and the candidate is rejected only on the declared finite domain"
      },
      "file": "src/ucns/carrier_coordinate.py",
      "id": "carrier_coordinate_admissibility_retains_failures"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a candidate is injective and passes every declared criterion on the bounded exact-rational domain",
        "since": "2026-07-29",
        "then": "its status is admissible-on-declared-domain while carrier selection, faithful-breadth canon, arbitrary-element assignment, EDCM activation, and METAPAT activation remain absent"
      },
      "file": "src/ucns/carrier_coordinate.py",
      "id": "carrier_coordinate_constructive_result_does_not_select"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the v0.10 experiment is constructed",
        "since": "2026-07-29",
        "then": "every candidate has a fixed name, version, formula, coordinate basis, code reference, and scope; all results remain visible and selection_effect remains none"
      },
      "file": "src/ucns/carrier_coordinate.py",
      "id": "carrier_coordinate_family_is_explicit_and_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a v0.10 report is constructed or replaced through the public dataclass API",
        "since": "2026-07-29",
        "then": "every expected candidate, event, fiber, convention, and transition key appears exactly once in declared order and collision witnesses are re-derived from the actual cover identities"
      },
      "file": "src/ucns/carrier_coordinate.py",
      "id": "carrier_coordinate_report_validates_complete_witness_identities"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "a candidate maps one transverse envelope",
        "since": "2026-07-29",
        "then": "the declared exact breadth and unchanged lifted turn materialize as the breadth and angle of an actual LiftedCarrierPoint; wrapper-only identity does not count as coordinate injectivity"
      },
      "file": "src/ucns/carrier_coordinate.py",
      "id": "carrier_coordinate_uses_actual_cover_fields"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "any declared v0.10 candidate receives exact transverse zero",
        "since": "2026-07-29",
        "then": "its actual directed-cover point equals the unchanged v0.7 root materialization under the pinned exact comparison policy"
      },
      "file": "src/ucns/carrier_coordinate.py",
      "id": "carrier_coordinate_zero_fiber_restricts_to_v07"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact coordinate adapters, binary64 materialization identities, exhaustive witness-key validation, collision classes, root restrictions, convention witnesses, and motion witnesses",
        "module_kind": "experiment",
        "module_name": "carrier_coordinate",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "CarrierCoordinateCandidate, CarrierCoordinateImage, CarrierCoordinateCandidateResult, CarrierCoordinateAdmissibilityReport, carrier_coordinate_candidates, map_transverse_to_actual_cover, run_v010_carrier_coordinate_experiment",
        "requires": "edcm_exact_rational_transverse_envelope_experiment, directed_carrier_floor, explicit_comparison_policy_layer",
        "rollback": "remove this module, its exports, tests, and v0.10 document while retaining the v0.5 through v0.9 evidence",
        "rollout": "explicit UCNS-only v0.10 bounded candidate experiment; no carrier selection, faithful-breadth canon, arbitrary-element assignment, global equivalence, completion, EDCM activation, or METAPAT activation",
        "since": "2026-07-29",
        "storage_boundary": "none",
        "summary": "evaluates a declared family of exact-rational transverse-to-cover coordinate laws against actual directed-cover materialization, injectivity, root restriction, convention invariance, and motion commutation",
        "tests": "tests/test_carrier_coordinate.py",
        "unresolved": "real-valued continuity, arbitrary-element assignment, canonical faithful breadth, global Mobius-to-cover equivalence, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions",
        "user_data_boundary": "exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and native completion scope remain linked through every candidate coordinate image"
      },
      "file": "src/ucns/carrier_coordinate.py",
      "id": "edcm_carrier_coordinate_admissibility_experiment"
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
        "given": "exact transverse values zero and two to the minus fifty-third are rendered at the same lifted turn",
        "since": "2026-07-29",
        "then": "their exact breadths remain distinct while their actual binary64 LiftedCarrierPoint identities collide"
      },
      "file": "src/ucns/exact_coordinate.py",
      "id": "exact_coordinate_binary64_breadth_collision_is_retained"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an exact coordinate is materialized as a LiftedCarrierPoint",
        "since": "2026-07-29",
        "then": "the actual binary64 fields, exact source record, rendering policy, and known information losses remain linked while the float point is classified only as a rendering"
      },
      "file": "src/ucns/exact_coordinate.py",
      "id": "exact_coordinate_binary64_is_declared_rendering"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "exact lifted turns one and one plus two to the minus fifty-four are rendered at the same transverse value",
        "since": "2026-07-29",
        "then": "their exact lifted turns remain distinct while their actual binary64 LiftedCarrierPoint identities collide"
      },
      "file": "src/ucns/exact_coordinate.py",
      "id": "exact_coordinate_binary64_turn_collision_is_retained"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the v0.11 boundary report is constructed",
        "since": "2026-07-29",
        "then": "exact rational injectivity and binary64 noninjectivity are reported together while carrier selection, faithful-breadth canon, arbitrary-element assignment, real-continuity theorem, EDCM activation, and METAPAT activation remain absent"
      },
      "file": "src/ucns/exact_coordinate.py",
      "id": "exact_coordinate_boundary_does_not_select_or_activate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "an exact coordinate record is constructed",
        "since": "2026-07-29",
        "then": "the v0.10 source candidate, v0.11 law identity, code reference, scope, and nonselection effect remain attached and fail closed on substitution"
      },
      "file": "src/ucns/exact_coordinate.py",
      "id": "exact_coordinate_provenance_is_fixed_and_retained"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "any exact rational local transverse value in the declared interval is mapped by the signed-local affine law",
        "since": "2026-07-29",
        "then": "breadth remains an exact positive Fraction and the exact inverse recovers the original transverse value without enumeration or binary64 conversion"
      },
      "file": "src/ucns/exact_coordinate.py",
      "id": "exact_coordinate_signed_local_law_round_trips"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact Fraction validation, exact coordinate identities, binary64 rendering identities, and fixed witness construction",
        "module_kind": "experiment",
        "module_name": "exact_coordinate",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "ExactCoordinateProvenance, ExactCarrierCoordinate, Binary64CarrierRendering, Binary64CollisionKind, Binary64CollisionWitness, ExactCoordinateBoundaryReport, signed_local_exact_coordinate, recover_signed_local_transverse, render_exact_coordinate_binary64, binary64_collision_witnesses, run_v011_exact_coordinate_boundary_experiment",
        "requires": "edcm_carrier_coordinate_admissibility_experiment, directed_carrier_floor",
        "rollback": "remove this module, its exports, tests, and v0.11 document while retaining the complete v0.10 candidate-family evidence",
        "rollout": "explicit UCNS-only v0.11 representation-boundary experiment; no carrier selection, canonical faithful breadth, arbitrary-element assignment, real-continuity theorem, EDCM activation, or METAPAT activation",
        "since": "2026-07-29",
        "storage_boundary": "none",
        "summary": "preserves the signed-local carrier-coordinate candidate as exact rational evidence and exhibits explicit binary64 rendering collisions",
        "tests": "tests/test_exact_coordinate.py",
        "unresolved": "real-continuous full-carrier map, arbitrary-element assignment, canonical faithful breadth, global Mobius-to-cover equivalence, higher geometry, and scoped completion",
        "user_data_boundary": "exact local transverse value, lifted turn, upstream candidate identity, law identity, and rendering loss remain linked"
      },
      "file": "src/ucns/exact_coordinate.py",
      "id": "edcm_exact_coordinate_representation_boundary"
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
        "class": "correctness",
        "given": "a valid explicit coordinate proposal is applied",
        "since": "2026-07-31",
        "then": "the exact v0.11 signed-local candidate maps u to B(u)=1+u/2, recovers u exactly, retains normalized lifted turns, and records one candidate GeometricAssignment with fixed initiation, proposal, implementation, and inverse evidence"
      },
      "file": "src/ucns/explicit_geometric_assignment.py",
      "id": "explicit_geometry_applies_exact_signed_local_candidate_reversibly"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the v0.18 report joins explicit candidate application to v0.17 initiation evidence",
        "since": "2026-07-31",
        "then": "the source-to-coordinate derivation law, total Structural Null topology, higher geometry, composition, completion, carrier selection, EDCM activation, and METAPAT activation remain absent"
      },
      "file": "src/ucns/explicit_geometric_assignment.py",
      "id": "explicit_geometry_does_not_claim_total_law_complete_select_or_activate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "v0.17 initiation outcomes enter one v0.18 trace",
        "since": "2026-07-31",
        "then": "every occurrence in one retained exact upstream trace keeps order and receives exactly one assigned, unresolved, or rejected outcome without prefixes, deduplication, or malformed combinations"
      },
      "file": "src/ucns/explicit_geometric_assignment.py",
      "id": "explicit_geometry_outcomes_are_total_exclusive_and_ordered"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "an exact lifted-turn and local-transverse proposal enters the candidate relation",
        "since": "2026-07-31",
        "then": "frame parity follows the two-turn native root law, local side follows the sign of u, exact identity survives, and binary64 remains a declared-loss rendering only"
      },
      "file": "src/ucns/explicit_geometric_assignment.py",
      "id": "explicit_geometry_preserves_mobius_frame_and_local_side"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "digest, runtime hash, repr, object identity, A0 Blake2 lanes, binary64 rendering identity, carrier position alone, scalar projection, or an invalid upstream prestate is proposed as geometry",
        "since": "2026-07-31",
        "then": "the mechanism remains named negative evidence and cannot create an AppliedGeometricAssignment"
      },
      "file": "src/ucns/explicit_geometric_assignment.py",
      "id": "explicit_geometry_rejects_identity_projection_and_upstream_substitution"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "one admitted word occurrence is proposed for v0.18 geometric assignment",
        "since": "2026-07-31",
        "then": "the proposal retains the exact v0.17 initiation receipt and independent Fraction-valued coordinate input while evidence identity, digest, and carrier position derive no geometric field"
      },
      "file": "src/ucns/explicit_geometric_assignment.py",
      "id": "explicit_geometry_requires_initiated_word_and_independent_exact_input"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "fixed GA01-GA09 evidence construction and exact validation helpers",
        "module_kind": "experiment",
        "module_name": "explicit_geometric_assignment",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "ExplicitCoordinateProposal, AppliedGeometricAssignment, GeometricAssignmentOutcome, GeometricAssignmentTrace, ExplicitGeometricAssignmentBoundaryReport, GeometricAssignmentDisposition, RejectedGeometricAssignmentMechanism, GeometricAssignmentEvidenceStanding, GeometricAssignmentFalsifierResult, propose_explicit_coordinate, apply_explicit_geometric_assignment, record_geometric_assignment_outcome, run_v018_explicit_geometric_assignment_experiment",
        "requires": "edcm_gonol_initiation_structural_null_boundary, edcm_exact_coordinate_representation_boundary",
        "rollback": "remove this module, exports, tests, and v0.18 document while retaining v0.17 initiation evidence and v0.11 exact-coordinate candidate evidence",
        "rollout": "nonselecting v0.18 exact-coordinate candidate application over explicitly initiated word occurrences; no universal source-to-coordinate derivation, total Structural Null topology, higher geometry, completion, EDCM activation, or METAPAT activation",
        "since": "2026-07-31",
        "storage_boundary": "none",
        "summary": "applies the surviving exact signed-local circle-coordinate candidate to explicitly initiated word occurrences while keeping coordinate input separate from evidence identity and the source-to-coordinate law unresolved",
        "tests": "tests/test_explicit_geometric_assignment.py",
        "unresolved": "source-to-coordinate derivation law, total Structural Null topology, intrinsic seam derivation, epicycle-disk-sphere transitions, higher-gonol composition, scoped completion, canonical faithful breadth, and carrier selection",
        "user_data_boundary": "v0.17 initiation and v0.16 adapter evidence remain exact; independently supplied exact coordinate input never becomes evidence identity and evidence identity never derives geometry"
      },
      "file": "src/ucns/explicit_geometric_assignment.py",
      "id": "edcm_explicit_geometric_assignment_boundary"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an external evaluator is executed",
        "since": "2026-08-16",
        "then": "input size, output file size, wall timeout, and process group termination are enforced rather than merely reported"
      },
      "file": "src/ucns/external_evaluation.py",
      "id": "external_evaluation_is_resource_bounded"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "an external evaluation completes successfully",
        "since": "2026-08-16",
        "then": "evaluator outputs remain candidate evidence and cannot select a benchmark or evaluator, validate UCNS measurement, activate EDCM, or confer canon status"
      },
      "file": "src/ucns/external_evaluation.py",
      "id": "external_evaluation_receipt_is_nonpromoting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an external EDCM evaluation plan is constructed or executed",
        "since": "2026-08-16",
        "then": "it binds an execution-generated FullCorpusCompletionReceipt and cannot run from a declaration, incomplete report, or corpus prefix"
      },
      "file": "src/ucns/external_evaluation.py",
      "id": "external_evaluation_requires_completed_corpus_gate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "cases cross the external process boundary",
        "since": "2026-08-16",
        "then": "evaluator identity, executable digest, exact argv, declared environment keys, network policy, case order, subject digests, custody references, and disclosure authorities enter the request and receipt identity"
      },
      "file": "src/ucns/external_evaluation.py",
      "id": "external_evaluator_identity_and_disclosure_are_bound"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "an evaluator returns candidate results",
        "since": "2026-08-16",
        "then": "protocol, plan, evaluator echo, exact ordered case coverage, result status, and JSON shape must reconcile or the receipt remains incomplete with the failure visible"
      },
      "file": "src/ucns/external_evaluation.py",
      "id": "external_response_reconciliation_is_fail_closed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "external corpus admission and per-case disclosure authority remain caller supplied and receipt bound",
        "internal_surface": "canonical request encoding, executable validation, process-group timeout, output-bound enforcement, response reconciliation",
        "module_kind": "instrument",
        "module_name": "external_evaluation",
        "network_boundary": "evaluator network access is declared but must be enforced by the caller-provided wrapper or execution environment",
        "owner": "Erin Spencer",
        "public_surface": "ExternalEvaluatorIdentity, ExternalEvaluatorCommand, ExternalEvaluationCase, ExternalEvaluationPlan, ExternalEvaluationStatus, ExternalEvaluationReceipt, execute_external_evaluation",
        "requires": "edcm_full_corpus_execution_gate, skill_lib_boundary_runner",
        "rollback": "remove module, exports, tests, and documentation while retaining the full-corpus gate and skill-lib boundary runner",
        "rollout": "candidate external evaluation transport only; no benchmark, evaluator selection, measurement validity, EDCM activation, or canon effect",
        "since": "2026-08-16",
        "storage_boundary": "request and response bytes are process-local; receipts retain digests, bounded excerpts, and parsed result evidence",
        "summary": "executes one explicitly identified external evaluator behind the completed EDCM corpus gate and emits bounded reconciled nonpromoting receipts",
        "tests": "tests/test_external_evaluation.py",
        "unresolved": "authenticated remote transport, network sandbox enforcement, external secret delivery, and evaluator-specific semantic validity",
        "user_data_boundary": "only explicitly supplied case payloads cross the process boundary; raw corpus custody is neither inferred nor fetched"
      },
      "file": "src/ucns/external_evaluation.py",
      "id": "edcm_external_evaluation_harness"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the corrected downstream EDCM MultiWOZ result is recorded in UCNS",
        "since": "2026-07-31",
        "then": "the corpus, report, receipt, producer, and publication identities remain exact while geometry, proof, canon, EDCM activation, and METAPAT activation do not transfer"
      },
      "file": "src/ucns/full_carrier_attachment.py",
      "id": "external_multiwoz_v0141_handoff_is_exact_and_nonpromoting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the v0.15 affine continuity certificate is constructed",
        "since": "2026-07-31",
        "then": "exact coefficients, endpoints, inverse compositions, and epsilon-delta multipliers encode the written proof over both complete real intervals without numerical sampling"
      },
      "file": "src/ucns/full_carrier_attachment.py",
      "id": "full_carrier_affine_certificate_is_universal_and_exact"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "analytic non-null evidence and bounded initiation evidence are joined",
        "since": "2026-07-31",
        "then": "arbitrary-element assignment, a total Structural Null relation, machine-checked proof, carrier selection, EDCM activation, and METAPAT activation remain absent and fail closed on substitution"
      },
      "file": "src/ucns/full_carrier_attachment.py",
      "id": "full_carrier_attachment_does_not_complete_select_or_activate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the v0.15 combined report is constructed",
        "since": "2026-07-31",
        "then": "RC01 and non-null RC03 retain analytic standing, RC02 and RC04-RC10 retain their bounded v0.13 executable standing, and no result is relabeled as one uniform arbitrary-real runtime scope"
      },
      "file": "src/ucns/full_carrier_attachment.py",
      "id": "full_carrier_attachment_retains_mixed_evidence_scopes"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the v0.15 quotient seam certificate is constructed",
        "since": "2026-07-31",
        "then": "two-turn deck equivariance and the one-turn sheet identity hold by exact coefficient algebra while coordinate cuts remain nonauthoritative and Structural Null remains outside the non-null quotient"
      },
      "file": "src/ucns/full_carrier_attachment.py",
      "id": "full_carrier_quotient_certificate_commutes_without_moving_the_marked_seam"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact coefficient validation and fixed mixed-scope RC01-RC10 evidence construction",
        "module_kind": "experiment",
        "module_name": "full_carrier_attachment",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "AffineContinuityCertificate, QuotientSeamCommutationCertificate, CarrierAttachmentEvidenceResult, FullCarrierAttachmentReport, ContinuityEvidenceStanding, run_v015_full_carrier_attachment_experiment",
        "requires": "edcm_exact_coordinate_representation_boundary, edcm_partial_initiation_boundary",
        "rollback": "remove this module, exports, tests, and v0.15 document while retaining v0.12 specification and v0.13 executable evidence",
        "rollout": "nonselecting v0.15 analytic certificates for the complete declared real affine intervals and non-null quotient, joined to the unchanged v0.13 partial root attachment",
        "since": "2026-07-31",
        "storage_boundary": "none",
        "summary": "records exact analytic certificates for the declared full non-null affine carrier and quotient seam while retaining the bounded source-bound Structural Null attachment",
        "tests": "tests/test_full_carrier_attachment.py",
        "unresolved": "arbitrary observed-element transverse assignment, total Structural Null initiation relationship, intrinsic-versus-marked seam choice, proof-assistant formalization, higher geometry, higher-gonol composition, scoped completion, canonical faithful breadth, and carrier selection",
        "user_data_boundary": "v0.13 source provenance remains attached and no arbitrary observed-element assignment is introduced"
      },
      "file": "src/ucns/full_carrier_attachment.py",
      "id": "edcm_full_carrier_attachment_evidence"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "every successfully processed speaker turn is observed",
        "since": "2026-07-31",
        "then": "the exact fixed profile implementation with canonical authority fields observes exact built-in turn tuples, speaker ids, and text values and length-prefixed source and reconstructed-observation stream digests agree before the report can complete"
      },
      "file": "src/ucns/full_corpus.py",
      "id": "full_corpus_gate_requires_exact_stream_reconstruction"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "an admitted corpus iterable is executed through the exact EDCM profile",
        "since": "2026-07-31",
        "then": "a complete report requires iterator exhaustion and exact agreement with the manifest's expected turn count"
      },
      "file": "src/ucns/full_corpus.py",
      "id": "full_corpus_gate_requires_exhaustion_and_turn_count"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a corpus is declared for EDCM execution",
        "since": "2026-07-31",
        "then": "source version and digest, expected turn count, license, privacy and redaction treatment, adapter identity, and external admission decision remain explicit"
      },
      "file": "src/ucns/full_corpus.py",
      "id": "full_corpus_manifest_pins_admission_identity"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a full-corpus completion receipt is issued",
        "since": "2026-07-31",
        "then": "it requires module-executed evidence, binds every authority-bearing manifest field, opens only failure-seeking post-run analysis, and cannot select a carrier, validate EDCM measurement, activate EDCM, or activate METAPAT"
      },
      "file": "src/ucns/full_corpus.py",
      "id": "full_corpus_receipt_has_no_selection_or_activation_effect"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "iteration, observation, reconstruction, or expected-count agreement fails",
        "since": "2026-07-31",
        "then": "the exact stopping index and failure class remain visible and no post-run completion receipt can be issued"
      },
      "file": "src/ucns/full_corpus.py",
      "id": "incomplete_corpus_run_fails_closed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "admission authority remains external and is retained by admission_decision_id",
        "internal_surface": "exact profile-implementation validation, length-prefixed turn-stream hashing, executed-run capability binding, incomplete-report construction, and complete manifest-bound receipt identity helpers",
        "module_kind": "experiment",
        "module_name": "full_corpus",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "CorpusAdapterIdentity, AdmittedCorpusManifest, CorpusRunStatus, CorpusRunFailureKind, CorpusRunFailure, FullCorpusExecutionReport, FullCorpusCompletionReceipt, execute_admitted_corpus, issue_full_corpus_completion_receipt",
        "requires": "edcm_word_gonol_profile",
        "rollback": "remove this module, its exports, tests, and v0.14 document while retaining the full-corpus authority decision and v0.13 carrier evidence",
        "rollout": "explicit UCNS-only v0.14 execution gate; no corpus is admitted by this module, no real-system run is claimed, and no carrier, EDCM, or METAPAT activation follows",
        "since": "2026-07-31",
        "storage_boundary": "raw corpus and per-turn observations remain in source or downstream custody; this bounded report retains counts and linked digests only",
        "summary": "fail-closed EDCM corpus execution reports and completion receipts that require iterator exhaustion, declared turn-count agreement, and exact source reconstruction before post-run analysis",
        "tests": "tests/test_full_corpus.py",
        "unresolved": "source-native corpus adapters, authenticated source custody, actual corrected MultiWOZ and later corpus runs, post-run falsifier implementations, completion-motion trajectories, and EDCM-scoped selection",
        "user_data_boundary": "exact source text enters the fixed EDCM profile without normalization; the report retains no raw text and cannot replace source or trajectory custody"
      },
      "file": "src/ucns/full_corpus.py",
      "id": "edcm_full_corpus_execution_gate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the v0.17 report joins origin separation, initiation outcomes, and root-return evidence",
        "since": "2026-07-31",
        "then": "arbitrary geometry, total Structural Null topology, scoped completion, carrier selection, EDCM activation, and METAPAT activation remain absent"
      },
      "file": "src/ucns/gonol_initiation.py",
      "id": "gonol_initiation_does_not_assign_complete_select_or_activate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the v0.17 origin registry is constructed",
        "since": "2026-07-31",
        "then": "Structural Null, source SPACE manifestation, carrier position zero, directed-cover null, neutral M, algebraic zero, absent cell, and NA retain distinct domain-qualified roles and only Structural Null may be an initiation prestate"
      },
      "file": "src/ucns/gonol_initiation.py",
      "id": "gonol_initiation_origin_roles_are_domain_separated"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "v0.16 admitted occurrences enter one v0.17 trace",
        "since": "2026-07-31",
        "then": "every occurrence retains exact order and receives exactly one initiated, unresolved, or rejected-substitution outcome with malformed combinations rejected"
      },
      "file": "src/ucns/gonol_initiation.py",
      "id": "gonol_initiation_outcome_is_total_and_exclusive"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "SPACE text, carrier zero, directed-cover null, neutral M, algebraic zero, absent cell, or NA is proposed as the Structural Null prestate",
        "since": "2026-07-31",
        "then": "the proposal can be retained only as an explicit rejected substitution and cannot create an initiation receipt"
      },
      "file": "src/ucns/gonol_initiation.py",
      "id": "gonol_initiation_rejects_zero_and_absence_substitutions"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "one v0.16 admitted word occurrence is initiated as a gonol",
        "since": "2026-07-31",
        "then": "exactly one source-bound boundary manifestation links the singular typed Structural Null prestate to an initiated non-null evidence state while geometric assignment remains absent"
      },
      "file": "src/ucns/gonol_initiation.py",
      "id": "gonol_initiation_requires_explicit_structural_null_transition"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the unchanged v0.13 source-bound root trajectory is retained",
        "since": "2026-07-31",
        "then": "360 degrees preserve the visible projection while changing complete local state, 720 degrees restore complete local state, both receipts survive, and no construction completion is registered"
      },
      "file": "src/ucns/gonol_initiation.py",
      "id": "gonol_initiation_root_return_is_bounded_and_noncompleting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the exact validated v0.17 authority report matching the fixed full producer-owned demonstration scope is supplied to the scope-exhaustion issuer",
        "since": "2026-07-31",
        "then": "receipt scope, cardinality, full ordered outcome evidence digest, and identity derive from that report while consistent multi-layer prefixes, id-preserving outcome changes, sampling, construction completion, and selection remain absent"
      },
      "file": "src/ucns/gonol_initiation.py",
      "id": "gonol_initiation_scope_receipt_is_producer_issued"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "the in-process scope-exhaustion issuer accepts only an exact validated v0.17 authority report whose full v0.16 admission trace and every ordered v0.17 disposition, admission evidence identity, initiation receipt, rejection, evidence tuple, and trace field match the fixed producer-owned demonstration; receipt identity binds that complete evidence while external transport authentication remains outside this module",
        "internal_surface": "fixed GI01-GI08 evidence construction and exact validation helpers",
        "module_kind": "experiment",
        "module_name": "gonol_initiation",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "OriginRole, OriginTermRecord, GonolInitiationReceipt, GonolInitiationOutcome, GonolInitiationTrace, GonolInitiationScopeCompletionReceipt, RootLoopReturnWitness, GonolInitiationBoundaryReport, GonolInitiationDisposition, RejectedOriginSubstitution, GonolInitiationEvidenceStanding, GonolInitiationFalsifierResult, origin_term_registry, initiate_word_gonol, record_gonol_initiation_outcome, issue_gonol_initiation_scope_completion_receipt, build_root_loop_return_witness, run_v017_gonol_initiation_boundary_experiment",
        "requires": "edcm_assignment_admission_boundary, edcm_partial_initiation_boundary",
        "rollback": "remove this module, exports, tests, and v0.17 document while retaining v0.16 admission evidence and v0.13 bounded initiation evidence",
        "rollout": "nonselecting v0.17 initiation-evidence boundary over admitted occurrences with bounded native-root return semantics; no arbitrary geometry, total Structural Null topology, scoped completion, EDCM activation, or METAPAT activation",
        "since": "2026-07-31",
        "storage_boundary": "none",
        "summary": "separates Structural Null from neighboring zero and absence roles, records one total tagged initiation outcome per admitted occurrence, and retains bounded 360-degree/720-degree root-return evidence",
        "tests": "tests/test_gonol_initiation.py",
        "unresolved": "arbitrary observed-element geometric assignment, total Structural Null topology, intrinsic seam derivation, higher geometry, higher-gonol composition, scoped completion, canonical faithful breadth, and carrier selection",
        "user_data_boundary": "v0.16 adapter evidence and exact source-bound Structural Null manifestations remain linked; neither evidence identity nor carrier position zero becomes geometry"
      },
      "file": "src/ucns/gonol_initiation.py",
      "id": "edcm_gonol_initiation_structural_null_boundary"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "an exact rational signed-local coordinate enters the declared sheet involution",
        "since": "2026-07-30",
        "then": "D maps B(u),t to B(-u),t+1 exactly and applying D twice restores the original coordinate"
      },
      "file": "src/ucns/initiation_boundary.py",
      "id": "partial_initiation_exact_quotient_compatibility"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "an attached root state advances by two successive visible turns",
        "since": "2026-07-30",
        "then": "the versioned source-linked visible projection returns after one exact turn while complete local state changes, a second exact turn restores local state, and both endpoint-validated motion receipts remain appended"
      },
      "file": "src/ucns/initiation_boundary.py",
      "id": "partial_initiation_motion_preserves_360_720_and_history"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the v0.13 report is produced",
        "since": "2026-07-30",
        "then": "RC01 through RC10 use canonical built-in payload, container, receipt-link, witness, and report-authority types and the constructor-bound exact ComparisonPolicy over fixed complete result payloads and partial scope, while canonical attachment identities bind the trajectory to one retained report attachment and consumer activation remains absent"
      },
      "file": "src/ucns/initiation_boundary.py",
      "id": "partial_initiation_report_executes_rc_packet_without_selection"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "one source-linked initiation is represented under different numeric coordinate cuts",
        "since": "2026-07-30",
        "then": "the marked seam and attachment identity retain the event, boundary manifestation, native source links, and parent observations while each numeric cut remains a nonauthoritative view"
      },
      "file": "src/ucns/initiation_boundary.py",
      "id": "partial_initiation_seam_is_provenance_bearing"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a v0.13 initiation attachment is constructed",
        "since": "2026-07-30",
        "then": "typed Structural Null remains a disjoint marked prestate connected to a non-null exact root only by the declared partial initiation relation"
      },
      "file": "src/ucns/initiation_boundary.py",
      "id": "partial_initiation_structural_null_topology_is_explicit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "each minimum-packet word gonol initiates",
        "since": "2026-07-30",
        "then": "exactly one twist receipt links its typed prestate, marked seam, exact source occurrence, native post-state, and exact root coordinate"
      },
      "file": "src/ucns/initiation_boundary.py",
      "id": "partial_initiation_twist_receipt_is_source_bound"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact validation helpers and fixed RC01-RC10 result construction",
        "module_kind": "experiment",
        "module_name": "initiation_boundary",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "StructuralNullTopologyKind, MarkedInitiationSeam, SeamCoordinateView, TwistReceipt, PartialInitiationAttachment, CarrierMotionReceipt, RootVisibleProjection, InitiatedCarrierState, ContinuityFalsifierResult, PartialInitiationBoundaryReport, partial_initiation_exact_comparison_policy, build_partial_initiation_attachments, view_marked_seam_at_cut, project_root_visible_state, initiate_carrier_state, advance_attached_state, exact_sheet_involution, run_v013_partial_initiation_boundary_experiment",
        "requires": "edcm_native_direct_mobius_candidate, edcm_exact_coordinate_representation_boundary",
        "rollback": "remove this module, its exports, tests, and v0.13 document while retaining the v0.12 specification and all earlier evidence",
        "rollout": "explicit UCNS-only v0.13 partial-attachment experiment; no carrier selection, canonical faithful breadth, arbitrary-element assignment, full real-continuity theorem, EDCM activation, or METAPAT activation",
        "since": "2026-07-30",
        "storage_boundary": "none",
        "summary": "attaches the typed Structural Null prestate to exact root coordinates through source-provenance marked seams and retained twist receipts",
        "tests": "tests/test_initiation_boundary.py",
        "unresolved": "arbitrary-real seam-side limits, intrinsic seam derivation, arbitrary-element transverse assignment, higher geometry, higher-gonol composition, scoped completion, and global carrier relationship",
        "user_data_boundary": "exact source witness, boundary manifestation, word occurrence, offsets, parentage, and initiation provenance remain linked without normalization"
      },
      "file": "src/ucns/initiation_boundary.py",
      "id": "edcm_partial_initiation_boundary"
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
        "class": "doctrine",
        "given": "character decomposition finds a retained base or two retained component words",
        "since": "2026-08-04",
        "then": "the result is constructor-bound to exact word identities and labeled orthographic-candidate until independently attested; it never rewrites the word gonol"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "affixiation_and_compounding_are_candidate_layers"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "definitions are added to retained word gonols",
        "since": "2026-08-06",
        "then": "multiple senses may coexist with distinct context and source identity, authority standing is fixed, and the returned layer cannot be mutated in place"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "definitions_are_context_plural_and_immutable"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "words, glyphs, gonols, hyperspace potential, affixiation, compounding, or definitions are materialized",
        "since": "2026-08-06",
        "then": "the exact ordered snapshot chain records the source receipt, producer, parent, count, digest, fixed standing, and unresolved boundary; a changed source or parent fails validation"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "every_added_layer_has_a_source_bound_snapshot"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the source collection is serialized",
        "since": "2026-08-04",
        "then": "deterministic casefold-plus-exact-codepoint order supports reproducible builds but contributes no rank, frequency, meaning, or gonol identity"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "lexical_floor_order_is_serialization_only"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a source spelling is converted to a word gonol",
        "since": "2026-08-04",
        "then": "each exact Unicode scalar occurrence uses the existing EDCM carrier assignment and retains its value, position, multiplicity, and order"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "lexical_floor_reuses_canonical_glyph_assignment"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the packaged NGSL source metadata and word file are loaded",
        "since": "2026-08-06",
        "then": "exact schema, collection, attribution notice, serialization, count, Git blob, byte digests, word-sequence digest, and unresolved custody boundary are retained in one immutable source receipt"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "lexical_floor_source_receipt_binds_packaged_bytes"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "any public word-gonol construction path is used",
        "since": "2026-08-04",
        "then": "the word is nonempty, contains only assigned Unicode scalars, contains no profile-pinned SPACE manifestation, preserves exact case and order, and cannot duplicate another exact spelling in one floor"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "lexical_floor_words_are_unique_exact_glyph_sets"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "two word gonols are compared",
        "since": "2026-08-06",
        "then": "exact cross-word glyph occurrence addresses, prefix, suffix, containment, and edit distance are retained; any glyph-type set view names its identity policy and information loss; no semantic, morphological, geometric, or embedding standing follows"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "lexical_hyperspace_is_occurrence_preserving_projection_not_embedding"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_digest, _word_sort_key, _edit_distance, _load_source_bundle, _git_blob_sha1",
        "module_kind": "domain",
        "module_name": "lexical_floor",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "GlyphDefinition, LexicalSourceReceipt, LexicalWordGonol, SharedGlyphOccurrence, GlyphTypeSetProjection, CharacterRelationship, LexicalHyperspacePotential, AffixiationCandidate, CompoundCandidate, DefinitionSense, LexicalLayerSnapshot, load_ngsl_source_receipt, load_ngsl_words, define_glyphs, create_word_gonols, create_hyperspace_potential, derive_affixiation_candidates, derive_compound_candidates, create_definition_layer, snapshot_layers, validate_snapshot_chain, word_gonol_id",
        "rollback": "remove this module and packaged NGSL artifacts without altering the existing EDCM word-gonol profile",
        "rollout": "experimental lexical-floor producer; no hyperdimensional embedding or linguistic canon selection",
        "since": "2026-08-04",
        "storage_boundary": "packaged immutable text and JSON source evidence; caller-selected snapshot output",
        "summary": "source-bound NGSL word gonols, occurrence-addressed character relationships, layered affixiation, compounding, contextual definitions, and immutable snapshots",
        "tests": "tests/test_lexical_floor.py",
        "unresolved": "independent official-source checksum custody, attested affix authority, compound adjudication, contextual definition custody, and the deep-recursion hyperdimensional embedding law",
        "user_data_boundary": "no user data; exact source spellings remain unchanged and definitions require explicit context and source identity"
      },
      "file": "src/ucns/lexical_floor.py",
      "id": "ngsl_lexical_floor"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the exact quarter-turn height equation is split into its two trigonometric branches",
        "since": "2026-08-10",
        "then": "the difference branch is rejected by the exact modulus contradiction two times radius not equal center separation"
      },
      "file": "src/ucns/mobius_certificates.py",
      "id": "mobius_vesica_alternate_height_branch_is_obstructed"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a machine receipt is serialized",
        "since": "2026-08-10",
        "then": "it records selection effect none and denies electron ontology, Pauli derivation, whole-surface classification, link proof, spectral correspondence, and Riemann-hypothesis proof"
      },
      "file": "src/ucns/mobius_certificates.py",
      "id": "mobius_vesica_certificate_is_nonselecting_and_zeta_firewalled"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a certificate is emitted",
        "since": "2026-08-10",
        "then": "physical boundary contacts, centerline contacts, projected crossings, and the unresolved full surface-intersection locus remain distinct fields"
      },
      "file": "src/ucns/mobius_certificates.py",
      "id": "mobius_vesica_contact_semantics_are_not_flattened"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the normalized radius-one, separation-one, half-width-one-hundredth, opposite-chirality, quarter-turn dyad is constructed",
        "since": "2026-08-10",
        "then": "exact Sturm arithmetic proves two roots of the boundary-contact cubic in minus one to one and each root induces two distinct physical contacts, for exactly four"
      },
      "file": "src/ucns/mobius_certificates.py",
      "id": "mobius_vesica_sturm_proves_four_physical_boundary_contacts"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "rational polynomial arithmetic, branch obstruction, deterministic witness realization, payload hashing",
        "module_kind": "experiment",
        "module_name": "mobius_certificates",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "RationalInterval, SturmCertificate, BoundaryContactWitness, MobiusVesicaCertificate, sturm_sequence, count_real_roots, isolate_real_roots, certify_mobius_vesica, write_default_certificate",
        "requires": "ucns_mobius_vesica_exact_embedding",
        "rollback": "remove with mobius_vesica and mobius_continuation without changing the seven-band candidate",
        "rollout": "exact certificate for the normalized circular-ribbon quarter-turn family only; selection effect none",
        "since": "2026-08-10",
        "storage_boundary": "caller-supplied local paths only through write_default_certificate",
        "summary": "certifies the canonical Mobius Vesica centerline count, physical boundary-contact count, quotient return, null clearance, and proof firewall using exact rational Sturm arithmetic plus residual witnesses",
        "tests": "tests/test_mobius_vesica_exact.py",
        "unresolved": "full surface-pair intersection locus, general-phase classification, arbitrary-perturbation stability, linking, ambient isotopy, zeta operator",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/mobius_certificates.py",
      "id": "ucns_mobius_vesica_certificates"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the standard circular family has opposite chirality, phase pair zero and one half, and width below one half",
        "since": "2026-08-10",
        "then": "exact branch equations admit zero physical boundary contacts"
      },
      "file": "src/ucns/mobius_continuation.py",
      "id": "mobius_vesica_half_turn_phase_has_exact_contact_obstruction"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the Seed-of-Life wheel relation graph is requested",
        "since": "2026-08-10",
        "then": "six center-to-ring and six adjacent-ring rigid placements are emitted, each preserving the local two-plus-four certificate in isolation"
      },
      "file": "src/ucns/mobius_continuation.py",
      "id": "mobius_vesica_rigid_placements_cover_seed_structural_pairs"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the exact quarter-turn dyad is compared with the current PR-174 half-turn first dyad",
        "since": "2026-08-10",
        "then": "chirality and width matches are retained, phase mismatch is explicit, and the four-contact certificate is not transferred"
      },
      "file": "src/ucns/mobius_continuation.py",
      "id": "mobius_vesica_seed_phase_mismatch_blocks_certificate_inheritance"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "a sequence of rational widths strictly between zero and one half is requested at quarter-turn phase",
        "since": "2026-08-10",
        "then": "every stage is independently Sturm-certified rather than inheriting a sampled contact count"
      },
      "file": "src/ucns/mobius_continuation.py",
      "id": "mobius_vesica_width_continuation_recertifies_each_stage"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact width stages, half-turn obstruction, rigid pair placement, deterministic combined receipt",
        "module_kind": "experiment",
        "module_name": "mobius_continuation",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "ContinuationStage, PhaseStage, SeedDyadComparison, VesicaPlacement, MobiusVesicaContinuationEngine, build_default_continuation_report, build_artifact_payload, write_default_artifact",
        "requires": "ucns_mobius_vesica_certificates, ucns_mobius_seed_of_life_candidate",
        "rollback": "remove with mobius_vesica and mobius_certificates",
        "rollout": "research continuation only; does not rewrite PR 174 phase law or select the seven-band candidate",
        "since": "2026-08-10",
        "storage_boundary": "caller-supplied local paths only through write_default_artifact",
        "summary": "continues the exact Mobius Vesica across rational widths, replicates it into the twelve rigid Seed-of-Life pair placements, and firewalls the quarter-turn certificate from the current half-turn seed phase",
        "tests": "tests/test_mobius_vesica_exact.py",
        "unresolved": "general phase classification, compatible seven-band global phase assignment, simultaneous twelve-pair realization, link invariants, spectral bridge",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/mobius_continuation.py",
      "id": "ucns_mobius_vesica_continuation"
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
        "class": "evidence",
        "given": "all six spokes are rigid copies while the center retains one chirality",
        "since": "2026-08-10",
        "then": "they demand six distinct center phases modulo one half turn"
      },
      "file": "src/ucns/mobius_global_compatibility.py",
      "id": "mobius_seed_center_needs_six_phase_channels_for_six_spokes"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the certificate is serialized",
        "since": "2026-08-10",
        "then": "selection effect is none and the obstruction remains bounded to its declared assumptions"
      },
      "file": "src/ucns/mobius_global_compatibility.py",
      "id": "mobius_seed_global_compatibility_certificate_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "two wheel-W7 structural pairs share a band and each is a rigid copy of the certified quarter-turn anti-chiral vesica",
        "since": "2026-08-10",
        "then": "all four orientation combinations demand different chirality-phase states at the shared band"
      },
      "file": "src/ucns/mobius_global_compatibility.py",
      "id": "mobius_seed_incident_certified_dyads_are_state_incompatible"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the same occurrences at one event are declared both physically equal and strictly height-separated",
        "since": "2026-08-10",
        "then": "delta-z equals zero contradicts delta-z nonzero"
      },
      "file": "src/ucns/mobius_global_compatibility.py",
      "id": "mobius_seed_physical_contact_and_strict_braid_are_event_exclusive"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the pinned PR-174 phase/chirality schedule is compared with both exact rigid-copy orientations",
        "since": "2026-08-10",
        "then": "zero of twelve structural pairs inherit the complete local certificate"
      },
      "file": "src/ucns/mobius_global_compatibility.py",
      "id": "mobius_seed_pr174_inherits_no_exact_rigid_vesica_pairs"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "each band has one chirality and one constant surface phase modulo one half turn",
        "since": "2026-08-10",
        "then": "compatible certified pairs form a matching and W7 has maximum matching size three"
      },
      "file": "src/ucns/mobius_global_compatibility.py",
      "id": "mobius_seed_single_state_certified_capacity_is_three"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact half-turn phase quotient, rigid-rotation transport, W7 cut and matching enumeration, pinned PR-174 comparison",
        "module_kind": "experiment",
        "module_name": "mobius_global_compatibility",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "EdgeOrientation, SurfacePhaseState, StructuralEdge, CertifiedEdgeCopy, CompatibilityBoundary, surface_phase, build_structural_edges, certified_edge_copies, pinned_pr174_assignment, edge_inherits_certificate, contact_and_strict_braid_compatible, prove_global_compatibility_boundary, write_global_compatibility_certificate",
        "requires": "ucns_mobius_vesica_continuation, ucns_mobius_seed_of_life_candidate",
        "rollback": "remove this module, its test, documentation, and generated certificate",
        "rollout": "stacked nonselecting UCNS obstruction certificate; does not alter PR 174 or PR 175",
        "since": "2026-08-10",
        "storage_boundary": "caller-supplied local path only",
        "summary": "proves the single-state phase/chirality capacity and contact-versus-braid boundary for assembling the certified Mobius Vesica across the twelve structural Seed-of-Life pairs",
        "tests": "tests/test_mobius_global_compatibility.py",
        "unresolved": "nonconstant phase fields, recursive or multichannel carriers, other local dyad families, simultaneous surface embedding, complete lift equations, spectral operator, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/mobius_global_compatibility.py",
      "id": "ucns_mobius_seed_global_compatibility"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a receipt or OBJ realization is emitted",
        "since": "2026-08-10",
        "then": "the artifact records selection effect none and explicitly denies zeta proof, electron ontology, Pauli-derived geometry, verified linking, and canonical UCNS completion"
      },
      "file": "src/ucns/mobius_seed.py",
      "id": "mobius_seed_candidate_is_nonselecting_and_proof_firewalled"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the default seven-band schedule is inspected",
        "since": "2026-08-10",
        "then": "the central band and first outer band have opposite chirality and half-turn seam displacement while the six outer seam phases advance by one twelfth turn"
      },
      "file": "src/ucns/mobius_seed.py",
      "id": "mobius_seed_dyad_is_anti_aligned_and_outer_phase_is_incremental"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "coincident projected occurrences are lifted into three dimensions",
        "since": "2026-08-10",
        "then": "every incident band has a distinct exact lift height, the six outer strands occupy nonzero one-two-three lane pairs at the center, and exact origin exclusion plus compactness preserves a positive three-dimensional void"
      },
      "file": "src/ucns/mobius_seed.py",
      "id": "mobius_seed_lift_preserves_null_as_nonvertex_void"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the default Mobius Seed of Life candidate is constructed",
        "since": "2026-08-10",
        "then": "seven equal-radius operands, all twenty-one unordered pairs, thirteen unique projection nodes, twelve structural vesicas, six incidental secants, and three incidental tangencies are retained without hidden pair deletion"
      },
      "file": "src/ucns/mobius_seed.py",
      "id": "mobius_seed_projection_is_exact_and_pair_complete"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "either projected crossing of each structural vesica is inspected",
        "since": "2026-08-10",
        "then": "the exact lift-height difference is nonzero at both events and changes sign between them without claiming physical contact or a verified boundary-edge intersection"
      },
      "file": "src/ucns/mobius_seed.py",
      "id": "mobius_seed_structural_pairs_have_alternating_braid_order"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "any default band surface point is advanced one or two carrier turns",
        "since": "2026-08-10",
        "then": "one turn equals the seam-identified point at reversed breadth and two turns restore the complete sampled point"
      },
      "file": "src/ucns/mobius_seed.py",
      "id": "mobius_seed_surface_obeys_360_seam_and_720_return"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact sextant trigonometry, incidence construction, candidate validation, deterministic OBJ serialization",
        "module_kind": "experiment",
        "module_name": "mobius_seed",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "Qsqrt3, ExactPoint2, Point3, BandSlot, TwistChirality, PairStanding, NodeStanding, ProjectionNode, PairProjectionEvent, PairRelation, MobiusBandSpec, MobiusSeedOfLife, build_mobius_seed_of_life",
        "requires": "ucns_gonol_relationship_display_v1, edcm_native_direct_mobius_candidate",
        "rollback": "remove this module, its tests, and MOBIUS_SEED_OF_LIFE_V1 documents without altering arity-one, arity-two, or arity-three relationship-display primitives",
        "rollout": "explicit UCNS-only implemented candidate; selection effect none; no canonical seven-gonol composition, zeta proof, physical-model validation, EDCM activation, or METAPAT activation",
        "since": "2026-08-10",
        "storage_boundary": "caller-supplied local paths only through write_obj and write_receipt",
        "summary": "constructs the seven-band Mobius Seed of Life as an exact projection ledger plus a deterministic nonselecting three-dimensional braid-lift candidate",
        "tests": "tests/test_mobius_seed.py",
        "unresolved": "smooth boundary-edge intersection realization, pairwise linking matrix, ambient-isotopy lock proof, canonical seven-gonol composition, spectral operator, zeta-zero correspondence, proof-assistant formalization",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/mobius_seed.py",
      "id": "ucns_mobius_seed_of_life_candidate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the canonical equal-radius vesica embedding is constructed",
        "since": "2026-08-10",
        "then": "the two circular centerlines meet at exactly two exact points, zero plus or minus sqrt(3)/2 in the projection plane"
      },
      "file": "src/ucns/mobius_vesica.py",
      "id": "mobius_vesica_has_exact_two_centerline_contacts"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "radius one, center separation one, and half width one hundredth",
        "since": "2026-08-10",
        "then": "the origin is excluded from both individual bands by an exact lower clearance bound of forty-nine hundredths"
      },
      "file": "src/ucns/mobius_vesica.py",
      "id": "mobius_vesica_null_origin_has_positive_clearance"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "either band is evaluated at any admissible breadth",
        "since": "2026-08-10",
        "then": "one carrier turn reverses breadth under the quotient and two turns restore the full point"
      },
      "file": "src/ucns/mobius_vesica.py",
      "id": "mobius_vesica_obeys_one_turn_seam_and_two_turn_return"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the source note is used to define the dyad research target",
        "since": "2026-08-10",
        "then": "two centerline contacts and four physical continuous-boundary contacts remain explicit hypotheses to prove or falsify without being replaced by projected or abstract events"
      },
      "file": "src/ucns/mobius_vesica.py",
      "id": "mobius_vesica_preserves_source_claims_as_testable_geometry"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact vesica parameters, circular ribbon frame, quotient validation, boundary-contact polynomial",
        "module_kind": "experiment",
        "module_name": "mobius_vesica",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "VesicaBand, TwistChirality, Point3, CenterlineContact, MobiusBandEmbedding, MobiusVesicaParameters, MobiusVesica, build_mobius_vesica",
        "requires": "ucns_mobius_seed_of_life_candidate",
        "rollback": "remove this module, mobius_certificates, mobius_continuation, their tests, documentation, and generated receipt",
        "rollout": "UCNS-only exact candidate; selection effect none; does not alter the seven-band candidate or select a canonical zeta operator",
        "since": "2026-08-10",
        "storage_boundary": "none",
        "summary": "defines the canonical two-band Mobius Vesica Piscis embedding whose centerlines meet twice and whose single continuous boundaries admit an exact four-contact certificate",
        "tests": "tests/test_mobius_vesica_exact.py",
        "unresolved": "full pair-surface intersection set, arbitrary-perturbation stability, linking data, ambient-isotopy class, seven-band phase reconciliation, spectral operator, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/mobius_vesica.py",
      "id": "ucns_mobius_vesica_exact_embedding"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the frozen P7/P5 partition is replayed",
        "since": "2026-08-11",
        "then": "direct system MPFR is used instead of the primary mpmath interval backend and the pinned partition identities match"
      },
      "file": "src/ucns/mpfr_interval.py",
      "id": "prime_mpfr_replay_is_backend_independent"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "every frozen pair box is replayed with directed MPFR endpoints",
        "since": "2026-08-11",
        "then": "both prime candidates retain lower endpoints above the declared centerline margin"
      },
      "file": "src/ucns/mpfr_interval.py",
      "id": "prime_mpfr_replay_recertifies_ribbon_margin"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "ctypes MPFR bindings with explicit directed rounding modes",
        "module_kind": "experiment",
        "module_name": "mpfr_interval",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "MPNumber, MPInterval, mpfr_version, atan2_interval, flat_step_interval",
        "requires": "system libmpfr",
        "rollback": "remove with prime_independent_phase_milnor and its tests",
        "rollout": "independent interval backend only; certificate status does not transfer",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "provides direct system-MPFR outward-rounded interval primitives for an independent P7/P5 separation replay",
        "tests": "tests/test_prime_independent_phase_milnor.py",
        "unresolved": "proof-assistant verification of the MPFR binding",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/mpfr_interval.py",
      "id": "ucns_mpfr_interval"
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
        "rollout": "authoritative completion-motion root, scoped completion, trajectory identity, exact MultiWOZ receipt standing, v0.15 mixed carrier-evidence scopes, v0.16 assignment admission, v0.17 gonol initiation, v0.18 explicit-input application, v0.19 ordered-source derivation candidate, Structural Null standing, decisions, and explicit unresolved choices; no mathematical option selection",
        "since": "2026-07-25",
        "storage_boundary": "packaged option_registry.json",
        "summary": "loads and validates the authoritative UCNS completion-motion root, EDCM decisions, external receipt standing, analytic carrier evidence, assignment-admission, gonol-initiation, explicit geometric-assignment, ordered-source coordinate derivation, Structural Null, and unresolved-option boundaries",
        "tests": "tests/test_option_decisions.py",
        "unresolved": "selection and cross-scope composition of the v0.19 derivation candidate, total Structural Null topology, higher geometry and composition, later corpus runs, ideal EDCM-scoped configuration, non-SPACE alphabet expansion or escape, and the option dimensions marked required-evaluation or unresolved",
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
        "class": "evidence",
        "given": "the owning facade invokes this readable helper",
        "since": "2026-08-11",
        "then": "the helper behavior is exercised through the named facade test without becoming a separate certificate"
      },
      "file": "src/ucns/prime_boundary_link_invariants.py",
      "id": "prime_boundary_helper_is_facade_witnessed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "module implementation",
        "module_kind": "experiment",
        "module_name": "prime_boundary_link_invariants",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "internal readable implementation used through the declared facade",
        "requires": "ucns_prime_interval_boundary_links_p7_p5",
        "rollback": "remove only with the owning consolidated research layer",
        "rollout": "readable implementation; authority remains with the facade contracts",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "readable exact boundary-component and integer linking invariant implementation",
        "tests": "tests/test_prime_interval_boundary_links.py",
        "unresolved": "see owning facade contracts and research document",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_boundary_link_invariants.py",
      "id": "ucns_prime_boundary_link_invariants"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the complete rational-Laurent determinantal generator family is accepted",
        "then": "component-variable saturation and exact lex reduction return a monic reduced basis for the complete ideal"
      },
      "file": "src/ucns/prime_determinantal_grobner.py",
      "id": "prime_grobner_basis_is_complete_reduced_and_saturated"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "P7 E1 or P5 E3 generators are constructed",
        "then": "every rank-size row/column subset pair is accounted for through the exact compound identity with no non-monomial denominator, and the frozen anchor, pivot-neighbor, and SHA-selected full minors agree under both direct determinant paths"
      },
      "file": "src/ucns/prime_determinantal_grobner.py",
      "id": "prime_grobner_generators_cover_every_maximal_minor"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "regression",
        "given": "primary and independent computations finish within frozen bounds",
        "then": "generator digests, mutual reductions, and canonical reduced basis maps agree exactly"
      },
      "file": "src/ucns/prime_determinantal_grobner.py",
      "id": "prime_grobner_independent_replay_agrees"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a determinantal basis computation begins",
        "then": "the committed preregistration bytes have the frozen SHA-256 identity and the parent presentation digest matches"
      },
      "file": "src/ucns/prime_determinantal_grobner.py",
      "id": "prime_grobner_protocol_identity_is_frozen"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family receipt is serialized",
        "then": "rational ideal evidence does not escalate phase, isotopy, prime-forcing, spectral, zeta, or theorem standing"
      },
      "file": "src/ucns/prime_determinantal_grobner.py",
      "id": "prime_grobner_receipt_preserves_nonclaims"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "compound maximal-minor coordinates, frozen direct full-minor audit, Laurent normalization, saturation, exact reduced lex bases, independent Buchberger replay",
        "module_kind": "experiment",
        "module_name": "prime_determinantal_grobner",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "determinantal_grobner_certificate, determinantal_grobner_family_certificate, write_determinantal_grobner_family_certificate",
        "requires": "ucns_prime_symbolic_alexander_p7_p5, sympy==1.14.0",
        "rollback": "remove this module, its tests, result document, and generated receipt while retaining preregistration and prior rank/onset evidence",
        "rollout": "protocol 7841af16; P7 first and P5 second; selection effect none",
        "since": "2026-08-15",
        "storage_boundary": "caller-supplied local paths only through writer functions",
        "summary": "executes the preregistered complete rational-Laurent determinantal-ideal Groebner protocol for the frozen P7 and P5 Fox matrices",
        "tests": "tests/test_prime_determinantal_grobner.py",
        "unresolved": "integral-Laurent strong bases, length-four Milnor invariants, finite nilpotent quotients, preregistered phase-co-winner separator",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_determinantal_grobner.py",
      "id": "ucns_prime_determinantal_grobner_p7_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family certificate is serialized",
        "since": "2026-08-11",
        "then": "it claims no arithmetic redefinition, electron ontology, zeta theorem, or Riemann-hypothesis proof"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "prime_exact_milnor_alexander_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a P7 or P5 whole-link fingerprint is issued",
        "since": "2026-08-11",
        "then": "every distinct phase-induced prime character has a rank and excess-nullity value committed by SHA-256"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "prime_fox_fingerprint_covers_all_prime_characters"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the P7 or P5 diagram is constructed",
        "since": "2026-08-11",
        "then": "every component uses the preregistered rational planar translation and the straight-line isotopy remains inside the prior seven-hundredths ribbon clearance"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "prime_generic_diagram_is_fixed_before_invariants"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "all generic double crossings are signed",
        "since": "2026-08-11",
        "then": "their half-sums reproduce the previously certified complete P7 and P5 pairwise linking matrices"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "prime_generic_diagram_preserves_pairwise_linking"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the closure of the braid sigma-one sigma-two-inverse cubed is evaluated",
        "since": "2026-08-11",
        "then": "the degree-two preferred-longitude Magnus coefficient has absolute value one"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "prime_magnus_benchmark_recovers_borromean_integer"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the five pairwise-zero P7 triples are evaluated in the fixed generic diagram",
        "since": "2026-08-11",
        "then": "every degree-two Magnus coefficient is exactly the integer zero"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "prime_p7_five_milnor_candidates_are_exact_zero_in_diagram"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the phase selector is evaluated",
        "since": "2026-08-11",
        "then": "its document hash equals the preregistered hash and no post-evaluation criterion is added"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "prime_phase_selector_matches_frozen_preregistration"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "an admissible phase law is scored",
        "since": "2026-08-11",
        "then": "the score uses maximum phase gap, finite-field Fox-Alexander excess nullity, and exact phase-lift alignment energy before neutral tie breakers"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "prime_phase_selector_uses_whole_link_character"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "fixed planar translations, high-precision circle intersections, Wirtinger arcs, degree-two Magnus algebra, finite-field Fox derivatives, exact rational phase-lift energy",
        "module_kind": "experiment",
        "module_name": "prime_exact_milnor_alexander",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "DiagramCrossing, GenericLinkDiagram, MilnorIntegerCertificate, FoxRankFingerprint, PhaseSelectorResult, build_generic_prime_seven_diagram, build_generic_prime_five_diagram, exact_p7_milnor_certificates, fox_rank_fingerprint, common_field_fox_rank_fingerprint, evaluate_preregistered_phase_selector, exact_milnor_alexander_family_certificate, write_exact_milnor_alexander_family_certificate",
        "requires": "ucns_prime_independent_phase_milnor_p7_p5, mpmath>=1.3",
        "rollback": "remove this module, its tests, documentation, preregistration, and generated certificate",
        "rollout": "P7 first, P5 same-protocol comparison second; preregistration SHA-256 frozen before evaluation; selection effect none",
        "since": "2026-08-11",
        "storage_boundary": "caller-supplied local paths only through writer functions",
        "summary": "generically resolves the P7/P5 centerline diagrams, replaces the five numerical Milnor-zero candidates with exact degree-two Magnus coefficients, freezes and evaluates a prime-character Fox-Alexander phase selector, and issues whole-link rank fingerprints",
        "tests": "tests/test_prime_exact_milnor_alexander.py",
        "unresolved": "proof-assistant replay of diagram signs, full multivariable Alexander polynomial, ambient-isotopy classification, higher Milnor invariants, spectral operator, prime-power law, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_exact_milnor_alexander.py",
      "id": "ucns_prime_exact_milnor_alexander_p7_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the owning facade invokes this readable helper",
        "since": "2026-08-11",
        "then": "the helper behavior is exercised through the named facade test without becoming a separate certificate"
      },
      "file": "src/ucns/prime_generic_diagram.py",
      "id": "prime_generic_helper_is_facade_witnessed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "module implementation",
        "module_kind": "experiment",
        "module_name": "prime_generic_diagram",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "internal readable implementation used through the declared facade",
        "requires": "ucns_prime_interval_boundary_links_p7_p5",
        "rollback": "remove only with the owning consolidated research layer",
        "rollout": "readable implementation; authority remains with the facade contracts",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "readable clearance-preserving generic diagram implementation",
        "tests": "tests/test_prime_interval_boundary_links.py",
        "unresolved": "see owning facade contracts and research document",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_generic_diagram.py",
      "id": "ucns_prime_generic_diagram"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "every reconstructed crossing has interval-certified height ordering and tangent determinant",
        "since": "2026-08-15",
        "then": "all P7-first and P5-second crossing signs agree with the frozen generic diagrams"
      },
      "file": "src/ucns/prime_generic_interval_certificate.py",
      "id": "prime_generic_crossing_signs_are_interval_certified"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family certificate is serialized",
        "since": "2026-08-15",
        "then": "it retains method, backend, complete crossing coverage, source identities, information boundary, and selection effect none"
      },
      "file": "src/ucns/prime_generic_interval_certificate.py",
      "id": "prime_generic_interval_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "each incident turn interval lies within one declared smooth-field segment",
        "since": "2026-08-15",
        "then": "the complete smooth-field interval difference excludes zero and agrees with the frozen over-under ordering"
      },
      "file": "src/ucns/prime_generic_interval_certificate.py",
      "id": "prime_generic_smooth_signs_are_interval_certified"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "every frozen P7/P5 generic equal-circle crossing is reconstructed",
        "since": "2026-08-15",
        "then": "direct system MPFR encloses both incident turns through directed-rounded atan2 without a branch-cut ambiguity"
      },
      "file": "src/ucns/prime_generic_interval_certificate.py",
      "id": "prime_generic_turns_are_outward_atan2_enclosed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "shifted-center, equal-circle intersection, turn, smooth-field, and transversality interval construction",
        "module_kind": "experiment",
        "module_name": "prime_generic_interval_certificate",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "GenericIntervalCrossingCertificate, GenericIntervalDiagramCertificate, certify_generic_prime_diagram, generic_interval_family_certificate, write_generic_interval_family_certificate",
        "requires": "ucns_mpfr_interval, ucns_prime_exact_milnor_alexander_p7_p5",
        "rollback": "remove this module, its tests, document, and generated certificate",
        "rollout": "nonselecting certificate over the already frozen P7/P5 generic diagrams",
        "since": "2026-08-15",
        "storage_boundary": "caller-supplied local paths only through the writer function",
        "summary": "independently replays the frozen P7/P5 generic crossing diagram with outward-rounded MPFR atan2 and smooth-field intervals",
        "tests": "tests/test_prime_generic_interval_certificate.py",
        "unresolved": "proof-assistant replay and symbolic validation of every interval primitive",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_generic_interval_certificate.py",
      "id": "ucns_prime_generic_interval_certificate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "independent replay findings are summarized",
        "since": "2026-08-11",
        "then": "negative and numerical results retain explicit nonclaims"
      },
      "file": "src/ucns/prime_independent_phase_milnor.py",
      "id": "prime_independent_phase_milnor_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "numerical estimates resolve near integers",
        "since": "2026-08-11",
        "then": "numerical resolution is not represented as an exact theorem"
      },
      "file": "src/ucns/prime_independent_phase_milnor.py",
      "id": "prime_milnor_exactness_boundary_is_preserved"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the numerical Fourier extractor is benchmarked",
        "since": "2026-08-11",
        "then": "it converges to the declared Borromean value under the recorded convention"
      },
      "file": "src/ucns/prime_independent_phase_milnor.py",
      "id": "prime_milnor_fourier_benchmark_recovers_borromean"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the five split P7 triples are evaluated across increasing resolutions",
        "since": "2026-08-11",
        "then": "every estimate converges numerically toward zero"
      },
      "file": "src/ucns/prime_independent_phase_milnor.py",
      "id": "prime_milnor_p7_split_triples_resolve_numerically_to_zero"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "every equal-gap phase alternative is enumerated",
        "since": "2026-08-11",
        "then": "the selected winding is identified without treating it as prime-specific emergence"
      },
      "file": "src/ucns/prime_independent_phase_milnor.py",
      "id": "prime_phase_sensitivity_separates_selection_from_emergence"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "falsifier",
        "given": "P7 and P5 maximum-gap candidates are compared",
        "since": "2026-08-11",
        "then": "their shared knot-degree alternatives preserve the negative result that T two-seven is not forced by prime alone"
      },
      "file": "src/ucns/prime_independent_phase_milnor.py",
      "id": "prime_phase_sensitivity_torus_seven_is_not_forced"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "zlib-compressed byte-exact validated readable implementation",
        "module_kind": "experiment",
        "module_name": "prime_independent_phase_milnor",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "independent MPFR replay, phase sensitivity report, Fourier Milnor estimate, P7 triple resolution",
        "requires": "ucns_mpfr_interval, ucns_prime_smooth_ribbons_p7_p5",
        "rollback": "remove with its tests and independent research documents",
        "rollout": "independent replay and negative-result evidence; numerical extraction is not promoted to exact computation",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "compact executable representation of the independent interval replay, phase sensitivity, and numerical Milnor extraction",
        "tests": "tests/test_prime_independent_phase_milnor.py",
        "unresolved": "analytic proof of all numerical zero resolutions",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_independent_phase_milnor.py",
      "id": "ucns_prime_independent_phase_milnor"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the selected phase law is evaluated over the two-turn boundary traversal",
        "since": "2026-08-11",
        "then": "the center boundary has cable class two-seven and each outer boundary has cable class two-one in the declared framing"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "prime_boundary_cable_winding_is_derived_from_phase"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "one finite-width M\u00f6bius ribbon is restricted to positive half-width",
        "since": "2026-08-11",
        "then": "its boundary closes only after two carrier turns and retracts with longitudinal degree two"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "prime_boundary_curve_is_single_two_turn_component"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "boundary components retract to degree-two traversals of their cores inside pairwise-disjoint ribbons",
        "since": "2026-08-11",
        "then": "every inter-ribbon boundary linking number is four times the corresponding core linking number"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "prime_boundary_linking_scales_by_four"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "triples of boundary components are classified by pairwise support",
        "since": "2026-08-11",
        "then": "algebraically split triples are enumerated while Milnor and complete-link invariants remain explicitly unresolved"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "prime_higher_order_boundary_is_explicit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family certificate is built",
        "since": "2026-08-11",
        "then": "P7 interval and boundary invariants are completed before the same protocol is applied independently to P5"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "prime_interval_boundaries_p7_precedes_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family receipt is serialized",
        "since": "2026-08-11",
        "then": "it records the interval-kernel boundary and claims no arithmetic redefinition, electron ontology, zeta theorem, or Riemann-hypothesis proof"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "prime_interval_boundary_compact_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "every complete pair-parameter torus is recursively covered",
        "since": "2026-08-11",
        "then": "high-precision interval point values and interval speed majorants certify the same nine-hundredths centerline target without a binary64 subtraction heuristic"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "prime_interval_replay_uses_outward_endpoints"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "core-core, core-boundary, and boundary-boundary linking laws are combined",
        "since": "2026-08-11",
        "then": "a complete two-p by two-p integer matrix and exact rank and determinant are issued"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "prime_mixed_core_boundary_matrix_is_complete"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "recovered legacy types and payloads over readable PR 181 interval and boundary certificates",
        "module_kind": "experiment",
        "module_name": "prime_interval_boundaries",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "IntervalPairReplay, IntervalReplayCertificate, BoundaryComponentCertificate, BoundaryInvariantCertificate, replay_prime_seven_intervals, replay_prime_five_intervals, certify_prime_seven_boundaries, certify_prime_five_boundaries, interval_boundary_family_certificate, write_interval_boundary_family_certificate, render_boundary_obj, render_core_boundary_obj",
        "requires": "ucns_prime_smooth_ribbons_p7_p5, mpmath>=1.3",
        "rollback": "remove this module, its test, documentation, generated certificate, and boundary exports",
        "rollout": "P7 first, P5 same-protocol comparison second; selection effect none; does not alter prior smooth-ribbon receipts",
        "since": "2026-08-11",
        "storage_boundary": "caller-supplied local paths only through writer functions",
        "summary": "replays the P7-first smooth-ribbon separation certificate with outward interval endpoints, extracts each M\u00f6bius strip's single two-turn boundary curve, and derives exact boundary-cable and mixed core-boundary invariants before P5 comparison",
        "tests": "tests/test_prime_interval_boundaries.py",
        "unresolved": "independently verified interval kernel, proof-assistant replay, Milnor invariants of algebraically split triples, multivariable Alexander polynomial of the complete boundary link, ambient isotopy, spectral operator, prime-power law, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_interval_boundaries.py",
      "id": "ucns_prime_interval_boundaries_p7_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "each centerline is a vertical graph over a circle and hence an unknot",
        "since": "2026-08-11",
        "then": "each boundary component is assigned its exact two-by-odd torus-cable type and Alexander, genus, determinant, and crossing-number readouts"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_boundary_component_knot_types_are_derived"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "one M\u00f6bius ribbon is evaluated at positive boundary breadth over two carrier turns",
        "since": "2026-08-11",
        "then": "it yields one closed boundary component with longitudinal winding two and odd meridional winding one plus twice the phase winding"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_boundary_curve_is_single_and_closed"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "distinct boundary components each carry longitudinal coefficient two",
        "since": "2026-08-11",
        "then": "their pairwise linking matrix equals four times the core linking matrix and the mixed core-boundary off-diagonal block equals twice the core matrix"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_boundary_linking_matrix_follows_cable_homology"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family certificate is built",
        "since": "2026-08-11",
        "then": "P7 is interval-certified and analyzed first and P5 is independently processed second"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_interval_boundary_p7_precedes_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family receipt is serialized",
        "since": "2026-08-11",
        "then": "it records dependency, precision, generic-projection, and invariant boundaries and claims no arithmetic redefinition, electron ontology, zeta theorem, or Riemann-hypothesis proof"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_interval_boundary_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "every complete P7 or P5 pair-parameter torus is replayed",
        "since": "2026-08-11",
        "then": "elementary evaluations use directed interval endpoints and every accepted leaf has a rigorous lower endpoint strictly above nine hundredths at the declared precision"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_interval_replay_is_outward_rounded"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "interval centerline clearance exceeds nine hundredths and half width is one hundredth",
        "since": "2026-08-11",
        "then": "all distinct complete ribbons remain separated by more than seven hundredths"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_interval_replay_preserves_finite_width_disjointness"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a clearance-preserving simultaneous generic projection is constructed",
        "since": "2026-08-11",
        "then": "pairwise linking is unchanged and every integer-valued length-three Milnor invariant is computed by a truncated Magnus expansion validated on the Borromean braid"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_length_three_milnor_profile_is_computed_after_global_lift"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "core, boundary, and own-core boundary linkings are combined",
        "since": "2026-08-11",
        "then": "rank, nullity, determinant, factorization, and Smith invariant factors are computed over the integers"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "prime_mixed_linking_matrix_has_exact_integer_invariants"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "prime_interval_common, prime_interval_replay, prime_boundary_link_invariants, prime_generic_diagram, prime_milnor_invariants",
        "module_kind": "experiment",
        "module_name": "prime_interval_boundary_links",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "IntervalPairCertificate, IntervalSeparationCertificate, BoundaryComponentInvariant, IntegerMatrixInvariant, BoundaryLinkCertificate, DiagramCrossing, GenericCoreDiagram, MilnorTripleInvariant, MilnorProfile, IntervalBoundaryCertificate, replay_interval_separation, extract_boundary_components, build_boundary_link_certificate, build_generic_core_diagram, compute_milnor_profile, certify_interval_boundary_prime_seven, certify_interval_boundary_prime_five, interval_boundary_family_certificate, interval_boundary_family_summary, write_interval_boundary_family_certificate, write_interval_boundary_family_summary, render_boundary_curve_obj",
        "requires": "ucns_prime_smooth_ribbons_p7_p5",
        "rollback": "remove this facade and its five helper modules, test, documentation, generated certificate, and boundary models; revert the research/test optional dependencies",
        "rollout": "P7 first, P5 same-protocol comparison second; selection effect none; does not alter prior smooth-ribbon receipts",
        "since": "2026-08-11",
        "storage_boundary": "caller-supplied local paths only through writer and renderer functions",
        "summary": "replays P7-first smooth-ribbon separation with outward-rounded interval arithmetic, extracts each M\u00f6bius ribbon's single continuous boundary, and computes boundary, mixed, component-knot, and length-three Milnor readouts before any spectral construction",
        "tests": "tests/test_prime_interval_boundary_links.py",
        "unresolved": "proof-assistant replay, simultaneous global projection regularization, length-four-and-higher Milnor invariants, whole-link ambient isotopy, multivariable Alexander or HOMFLYPT invariants, spectral operator, prime-power law, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_interval_boundary_links.py",
      "id": "ucns_prime_interval_boundary_links_p7_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the owning facade invokes this readable helper",
        "since": "2026-08-11",
        "then": "the helper behavior is exercised through the named facade test without becoming a separate certificate"
      },
      "file": "src/ucns/prime_interval_common.py",
      "id": "prime_interval_common_is_facade_witnessed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "module implementation",
        "module_kind": "experiment",
        "module_name": "prime_interval_common",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "internal readable implementation used through the declared facade",
        "requires": "ucns_prime_smooth_ribbons_p7_p5",
        "rollback": "remove only with the owning consolidated research layer",
        "rollout": "readable implementation; authority remains with the facade contracts",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "shared constants and dependency guards for readable interval and boundary research",
        "tests": "tests/test_prime_interval_boundary_links.py",
        "unresolved": "see owning facade contracts and research document",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_interval_common.py",
      "id": "ucns_prime_interval_common"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the owning facade invokes this readable helper",
        "since": "2026-08-11",
        "then": "the helper behavior is exercised through the named facade test without becoming a separate certificate"
      },
      "file": "src/ucns/prime_interval_replay.py",
      "id": "prime_interval_replay_helper_is_facade_witnessed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "module implementation",
        "module_kind": "experiment",
        "module_name": "prime_interval_replay",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "internal readable implementation used through the declared facade",
        "requires": "ucns_prime_interval_common",
        "rollback": "remove only with the owning consolidated research layer",
        "rollout": "readable implementation; authority remains with the facade contracts",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "readable outward-directed interval replay implementation",
        "tests": "tests/test_prime_interval_boundary_links.py",
        "unresolved": "see owning facade contracts and research document",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_interval_replay.py",
      "id": "ucns_prime_interval_replay"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the degree-three Magnus engine evaluates [[x1,x2],x3]",
        "since": "2026-08-15",
        "then": "the four frozen degree-three coefficients and every lower degree coefficient match the preregistration"
      },
      "file": "src/ucns/prime_length4_milnor.py",
      "id": "prime_length4_magnus_gate_matches_frozen_commutator"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the result is serialized",
        "since": "2026-08-15",
        "then": "it preserves computer-assisted diagram standing and makes no isotopy-classification, phase, spectral, zeta, or theorem-status claim"
      },
      "file": "src/ucns/prime_length4_milnor.py",
      "id": "prime_p7_length4_receipt_is_bounded"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the frozen target passes its lower-order gates",
        "since": "2026-08-15",
        "then": "the canonical, reverse-word, and four cyclic-rotation coefficients are retained without changing the primary target"
      },
      "file": "src/ucns/prime_length4_milnor.py",
      "id": "prime_p7_length4_result_records_cyclic_conventions"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the minimal P7 length-four experiment is evaluated",
        "since": "2026-08-15",
        "then": "only R0,R1,R4,R5 is targeted and all six linking, four triple-Milnor, and required longitude lower-degree gates are exact zero"
      },
      "file": "src/ucns/prime_length4_milnor.py",
      "id": "prime_p7_length4_target_is_frozen_and_lower_gated"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "degree-three noncommutative series, fixed-diagram Wirtinger longitude replay",
        "module_kind": "experiment",
        "module_name": "prime_length4_milnor",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "LengthFourMilnorCertificate, length_four_commutator_gate, evaluate_p7_length_four_milnor, write_p7_length_four_milnor_certificate",
        "requires": "ucns_prime_exact_milnor_alexander_p7_p5",
        "rollback": "remove this module, its tests, result document, and generated certificate",
        "rollout": "frozen ordered target R0,R1,R4,R5 only; accept nonzero, zero, or unresolved without retargeting",
        "since": "2026-08-15",
        "storage_boundary": "caller-supplied local paths only through writer function",
        "summary": "evaluates the frozen minimal P7 length-four Milnor experiment with exact degree-three Magnus arithmetic",
        "tests": "tests/test_prime_length4_milnor.py",
        "unresolved": "repeated-index Milnor invariants, higher nilpotent quotients, whole-link length-four program",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_length4_milnor.py",
      "id": "ucns_prime_length4_milnor_p7"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the owning facade invokes this readable helper",
        "since": "2026-08-11",
        "then": "the helper behavior is exercised through the named facade test without becoming a separate certificate"
      },
      "file": "src/ucns/prime_milnor_invariants.py",
      "id": "prime_milnor_helper_is_facade_witnessed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "module implementation",
        "module_kind": "experiment",
        "module_name": "prime_milnor_invariants",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "internal readable implementation used through the declared facade",
        "requires": "ucns_prime_generic_diagram",
        "rollback": "remove only with the owning consolidated research layer",
        "rollout": "readable implementation; authority remains with the facade contracts",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "readable length-three Milnor extraction and benchmark implementation",
        "tests": "tests/test_prime_interval_boundary_links.py",
        "unresolved": "see owning facade contracts and research document",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_milnor_invariants.py",
      "id": "ucns_prime_milnor_invariants"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "P7 and P5 higher signatures are compared",
        "since": "2026-08-15",
        "then": "component count and weight-one rank alone cannot produce distinguish"
      },
      "file": "src/ucns/prime_nilpotent_discriminator.py",
      "id": "prime_nilpotent_comparison_excludes_known_rank"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "substantive phase co-winners bind identical group and peripheral inputs",
        "since": "2026-08-15",
        "then": "their nilpotent comparison is no-distinguish"
      },
      "file": "src/ucns/prime_nilpotent_discriminator.py",
      "id": "prime_nilpotent_phase_binding_is_topological"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "GAP/NQ emits a class-four marked quotient",
        "since": "2026-08-15",
        "then": "exact degree-four Magnus replay reconstructs every marked meridian and longitude from NQ pc-generator preimages"
      },
      "file": "src/ucns/prime_nilpotent_discriminator.py",
      "id": "prime_nilpotent_primary_and_replay_agree"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a quotient computation starts",
        "since": "2026-08-15",
        "then": "the preregistration SHA-256, class four, backend versions, component orders, and resource bounds match PR 191"
      },
      "file": "src/ucns/prime_nilpotent_discriminator.py",
      "id": "prime_nilpotent_protocol_identity_is_frozen"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "deterministic GAP/NQ script, exact degree-four Magnus replay, frozen higher-signature comparison",
        "module_kind": "experiment",
        "module_name": "prime_nilpotent_discriminator",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "compute_nilpotent_discriminator, write_nilpotent_discriminator_receipt",
        "requires": "ucns_prime_exact_milnor_alexander_p7_p5, GAP 4.12.1, NQ 2.5.11",
        "rollback": "remove this module, tests, result document, and generated receipt",
        "rollout": "protocol ffaecb935e8086200fa9a27c5d55ba6e759721107d8c4979049eed760eae8aee; P7 then P5 then phase bindings",
        "since": "2026-08-15",
        "storage_boundary": "caller-supplied local output path and private temporary GAP script",
        "summary": "computes the frozen class-four marked peripheral nilpotent quotients for the complete P7 and P5 core links",
        "tests": "tests/test_prime_nilpotent_discriminator.py",
        "unresolved": "classes above four, repeated-index classification, ambient isotopy",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_nilpotent_discriminator.py",
      "id": "ucns_prime_nilpotent_discriminator_p7_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the complete projected pair-event ledger",
        "since": "2026-08-11",
        "then": "every projected coincidence has nonzero height separation"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "prime_phase_lift_centerlines_are_disjoint"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the phase-lift family is built",
        "since": "2026-08-11",
        "then": "P7 is solved globally on seven carriers and thirteen hypernodes before pair or triad readouts"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "prime_phase_lift_constructs_p7_before_restrictions"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "a carrier surface is evaluated",
        "since": "2026-08-11",
        "then": "one turn reverses breadth and two turns return the same point"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "prime_phase_lift_is_seam_compatible"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a pair has a regular two-crossing projection",
        "since": "2026-08-11",
        "then": "linking number is computed only after the global lift is fixed"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "prime_phase_lift_link_numbers_are_derived"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "P7 is complete",
        "since": "2026-08-11",
        "then": "P5 is solved independently by the same protocol"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "prime_phase_lift_p5_follows_same_protocol"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the P7 origin is evaluated",
        "since": "2026-08-11",
        "then": "it remains one arity-six hypernode with six nonzero lanes and fifteen derived pair comparisons"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "prime_phase_lift_preserves_nary_origin"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family receipt is serialized",
        "since": "2026-08-11",
        "then": "it claims no arithmetic redefinition, electron ontology, zeta theorem, or proof of the Riemann hypothesis"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "prime_phase_lift_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "any P7 or P5 hypernode",
        "since": "2026-08-11",
        "then": "every occurrence has a distinct exact phase and lift lane"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "prime_phase_lift_resolves_every_hypernode"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact phase-law search, finite-field lane assignment, deterministic certificate serialization",
        "module_kind": "experiment",
        "module_name": "prime_phase_lift",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "EventSemantic, PhaseLaw, LiftOccurrence, LiftHypernode, PairLinkReadout, PrimePhaseLiftCandidate, select_phase_law, build_prime_seven_phase_lift, build_prime_five_phase_lift, phase_lift_family_certificate, write_phase_lift_family_certificate",
        "requires": "ucns_prime_primitives_p7_p5",
        "rollback": "remove this module with prime_phase_lift_data, prime_phase_lift_model, their test, document, and generated certificate",
        "rollout": "nonselecting P7-first witness; pair and triad readouts follow the global solution",
        "since": "2026-08-11",
        "storage_boundary": "caller-supplied local path only through write_phase_lift_family_certificate",
        "summary": "solves P7 globally with an exact seam-compatible phase law and finite-field lift over all thirteen hypernodes, then applies the same protocol independently to P5",
        "tests": "tests/test_prime_phase_lift.py",
        "unresolved": "smooth lift replacement, whole-ribbon disjointness, tangent regularization, boundary topology, ambient isotopy, spectral operator, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_phase_lift.py",
      "id": "ucns_prime_phase_lift_p7_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the P7 and P5 phase-and-lift candidates consume their frozen ledgers",
        "since": "2026-08-11",
        "then": "every primitive hypernode occurrence resolves to an exact carrier turn, residue lane, generator, and projected center"
      },
      "file": "src/ucns/prime_phase_lift_data.py",
      "id": "prime_phase_lift_data_covers_every_p7_p5_hypernode"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "experiment",
        "module_name": "prime_phase_lift_data",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "P7_TURNS, P5_TURNS, P7_CARRIER_RESIDUES, P5_CARRIER_RESIDUES, P7_NODE_GENERATORS, P5_NODE_GENERATORS, P7_CENTERS, P5_CENTERS",
        "requires": "ucns_prime_primitives_p7_p5",
        "rollback": "remove with the complete prime phase-and-lift witness",
        "rollout": "exact static research ledger; selection effect none",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "stores the exact P7 and P5 occurrence-turn, carrier-residue, node-generator, and projected-center ledgers consumed by the phase-and-lift witness",
        "tests": "tests/test_prime_phase_lift.py",
        "unresolved": "independently derived ledgers beyond the frozen P7/P5 construction",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_phase_lift_data.py",
      "id": "ucns_prime_phase_lift_data"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "pair readouts are requested from a complete phase-and-lift candidate",
        "since": "2026-08-11",
        "then": "link readouts are derived from the globally fixed occurrence heights rather than used as construction inputs"
      },
      "file": "src/ucns/prime_phase_lift_model.py",
      "id": "prime_phase_lift_model_derives_links_after_global_lift"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "a lifted projected event is represented",
        "since": "2026-08-11",
        "then": "projected coincidence and strict braid order remain typed separately and no physical contact is inferred"
      },
      "file": "src/ucns/prime_phase_lift_model.py",
      "id": "prime_phase_lift_model_preserves_event_semantics"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact modular phase helpers, height-gap calculation, component and cycle-rank readouts",
        "module_kind": "experiment",
        "module_name": "prime_phase_lift_model",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "EventSemantic, PhaseLaw, LiftOccurrence, LiftHypernode, PairLinkReadout, PrimePhaseLiftCandidate, PhaseLiftError",
        "requires": "ucns_prime_phase_lift_data, ucns_prime_primitives_p7_p5",
        "rollback": "remove with the complete prime phase-and-lift witness",
        "rollout": "typed research model; projected coincidence remains distinct from physical contact",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "defines the typed exact phase, lift, event-semantic, geometric, and derived pair-link readouts for the P7-first witness",
        "tests": "tests/test_prime_phase_lift.py",
        "unresolved": "smooth lift replacement, whole-ribbon disjointness, tangent regularization, ambient isotopy",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_phase_lift_model.py",
      "id": "ucns_prime_phase_lift_model"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "arithmetic primality and UCNS primitive standing are evaluated",
        "since": "2026-08-11",
        "then": "the predicates remain separate and two remains arithmetic-prime"
      },
      "file": "src/ucns/prime_primitives.py",
      "id": "prime_arithmetic_geometry_firewall"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "P5 is constructed directly from one center plus four outer carriers",
        "since": "2026-08-11",
        "then": "ten pairs, eighteen projected pair events, and arity spectrum two-twelve four-one reconcile exactly"
      },
      "file": "src/ucns/prime_primitives.py",
      "id": "prime_p5_direct_exact_signature"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "P7 is constructed directly from one center plus six outer carriers",
        "since": "2026-08-11",
        "then": "twenty-one pairs, thirty-nine projected pair events, and arity spectrum two-six three-six six-one reconcile exactly"
      },
      "file": "src/ucns/prime_primitives.py",
      "id": "prime_p7_direct_exact_signature"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "P7 spoke and adjacent-rim separations are measured",
        "since": "2026-08-11",
        "then": "all twelve structural edges are unit-vesica relations and q equals six is the unique equal-spoke-rim ring order"
      },
      "file": "src/ucns/prime_primitives.py",
      "id": "prime_p7_uniform_structural_relation"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "dyadic and triadic readouts are reported",
        "since": "2026-08-11",
        "then": "they are derived restrictions and never treated as construction lineage"
      },
      "file": "src/ucns/prime_primitives.py",
      "id": "prime_restrictions_follow_construction"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "K2 is tested under a closure axiom requiring a nontrivial relational cycle",
        "since": "2026-08-11",
        "then": "its cycle rank is zero and it conditionally fails closed-primitive standing without changing arithmetic primality"
      },
      "file": "src/ucns/prime_primitives.py",
      "id": "prime_two_cycle_boundary"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact pair-distance ledgers, hypernode reconciliation, restriction counts, deterministic hashing",
        "module_kind": "experiment",
        "module_name": "prime_primitives",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "RelationKind, Hypernode, PrimePrimitive, is_arithmetic_prime, cycle_rank, dyadic_boundary, build_prime_seven, build_prime_five, family_certificate",
        "requires": "none",
        "rollback": "remove this module, its test, and documentation",
        "rollout": "nonselecting P7-first research artifact; lower-prime forms are restrictions, not construction parts",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "constructs P7 first and P5 second as direct exact projected carrier complexes, preserves n-ary hypernodes, and separates arithmetic primality from UCNS closed-primitive standing",
        "tests": "tests/test_prime_primitives.py",
        "unresolved": "P2 ontology, P3 artifact, smooth M\u00f6bius lift, phase field, physical event semantics, braid topology, spectral operator, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_primitives.py",
      "id": "ucns_prime_primitives_p7_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the registered anonymous baseline preserves the 2/3/5/7 partition, F_257 arithmetic, checksum operator, and 21-cell budget",
        "since": "2026-08-17",
        "then": "the report identifies structural isomorphism and leaves prime-cardinality architectural standing UNRESOLVED"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "prime_relational_baseline_isomorphism_blocks_architecture_transfer"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the complete producer CLI is executed by the resource-bound test harness",
        "since": "2026-08-17",
        "then": "one-CPU affinity, 256 MiB address-space limit, and 30-second timeout are applied and the report completes"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "prime_relational_complete_run_obeys_registered_resources"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the frozen P2/P3/P5/P7 encoders are inspected as source",
        "since": "2026-08-17",
        "then": "four distinct entry points exist and none delegates to another encoder or a shared encoding helper"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "prime_relational_encoders_remain_source_independent"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "registered H3 is FALSIFIED but its baseline changes only semantic labels, dispatch specialization, and checksum placement",
        "since": "2026-08-17",
        "then": "no prime-cardinality dependent claim is deprecated; every unexecuted dependent claim remains UNRESOLVED and local bounded survivors remain recorded"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "prime_relational_failure_propagation_is_scope_bounded"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "public identity is computed for a source relation",
        "since": "2026-08-16",
        "then": "changing its value cannot change identity and forbidden payload fields are absent"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "prime_relational_fixture_identity_excludes_values"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "each frozen source relation is erased once from its owning prime-cardinality view",
        "since": "2026-08-16",
        "then": "primary and brute-force replay use the complementary view checksum and agree on exactly one hidden field value"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "prime_relational_h1_requires_complementary_unique_reconstruction"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "H1 survives and each complete prime-cardinality view is omitted independently",
        "since": "2026-08-16",
        "then": "constructive ambiguity and an independent field-degree replay agree whether every view uniquely matters"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "prime_relational_h2_tests_every_whole_view"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "H1 and H2 survive and an exactly information-matched typed-block baseline is evaluated",
        "since": "2026-08-16",
        "then": "equal or better reconstruction with strictly lower semantic or dispatch complexity falsifies only the registered semantic-label and dispatch advantage"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "prime_relational_h3_applies_frozen_software_complexity_criterion"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "preregistration validation, exact field reconstruction, brute-force replay, whole-view ambiguity witnesses, typed-block baseline, structural-isomorphism audit, canonical report serialization",
        "module_kind": "experiment",
        "module_name": "prime_relational_reconstruction",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "Status, public_relation_identity, encode_p2, encode_p3, encode_p5, encode_p7, audit_baseline_architecture, run_architecture_gates, main",
        "requires": "edcm_external_evaluation_harness",
        "rollback": "revert the interpretation correction while retaining immutable preregistration, original execution commits, and prior bounded results",
        "rollout": "registered experiment plus interpretation correction only; no canon or runtime activation",
        "since": "2026-08-16",
        "storage_boundary": "writes one caller-selected aggregate report",
        "summary": "executes frozen P2/P3/P5/P7 gates and audits whether the registered baseline changes the prime-cardinality architecture before propagating failure",
        "tests": "tests/test_prime_relational_reconstruction.py",
        "unresolved": "genuinely non-prime-cardinality matched baseline, natural multimodal semantics, external authorship, measurement validity, independent external replication",
        "user_data_boundary": "hand-authored development fixture only; no external or sealed labels"
      },
      "file": "src/ucns/prime_relational_reconstruction.py",
      "id": "ucns_prime_relational_reconstruction_adversary"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the owning facade invokes this readable helper",
        "since": "2026-08-11",
        "then": "the helper behavior is exercised through the named facade test without becoming a separate certificate"
      },
      "file": "src/ucns/prime_replay_phase_milnor_data.py",
      "id": "prime_replay_data_is_receipt_witnessed"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "module implementation",
        "module_kind": "experiment",
        "module_name": "prime_replay_phase_milnor_data",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "internal readable implementation used through the declared facade",
        "requires": "ucns_prime_smooth_ribbons_p7_p5",
        "rollback": "remove only with the owning consolidated research layer",
        "rollout": "readable implementation; authority remains with the facade contracts",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "immutable independent replay, phase-sensitivity, and numerical Milnor receipt data",
        "tests": "tests/test_prime_replay_phase_milnor_receipt.py",
        "unresolved": "see owning facade contracts and research document",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_replay_phase_milnor_data.py",
      "id": "ucns_prime_replay_phase_milnor_data"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "P7 and P5 selected phase laws are compared",
        "since": "2026-08-11",
        "then": "both use center winding three and therefore both produce T two-seven"
      },
      "file": "src/ucns/prime_replay_phase_milnor_receipt.py",
      "id": "prime_replay_receipt_exposes_phase_imposition"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the five algebraically split outer triples are audited",
        "since": "2026-08-11",
        "then": "each length-three mu-bar value is zero across the frozen projection, resolution, and basepoint sweeps"
      },
      "file": "src/ucns/prime_replay_phase_milnor_receipt.py",
      "id": "prime_replay_receipt_freezes_p7_milnor_values"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the compact receipt is serialized",
        "since": "2026-08-11",
        "then": "no phase law, arithmetic redefinition, electron ontology, zeta theorem, or Riemann-hypothesis proof is selected"
      },
      "file": "src/ucns/prime_replay_phase_milnor_receipt.py",
      "id": "prime_replay_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the compact receipt is loaded",
        "since": "2026-08-11",
        "then": "P7 and P5 pair counts, box counts, margins, and independent Decimal ledger hashes remain pinned"
      },
      "file": "src/ucns/prime_replay_phase_milnor_receipt.py",
      "id": "prime_replay_receipt_preserves_independent_interval_result"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "immutable base receipt validation and deterministic payload hashing",
        "module_kind": "experiment",
        "module_name": "prime_replay_phase_milnor_receipt",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "boundary_knot, validate_receipt, build_receipt",
        "requires": "ucns_prime_smooth_ribbons_p7_p5",
        "rollback": "remove this module, its test, documents, and generated summary",
        "rollout": "compact GitHub publication surface; selection effect none",
        "since": "2026-08-11",
        "storage_boundary": "none",
        "summary": "freezes the independent P7/P5 interval replay, phase-winding sensitivity, and length-three P7 Milnor audit while preserving the executable reference packet as the producing evidence",
        "tests": "tests/test_prime_replay_phase_milnor_receipt.py",
        "unresolved": "proof-assistant interval replay, analytic crossing extraction, length-four and higher Milnor invariants, multivariable Alexander polynomial, spectral operator, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_replay_phase_milnor_receipt.py",
      "id": "ucns_prime_replay_phase_milnor_receipt"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "centerline separation exceeds nine hundredths and ribbon half-width is one hundredth",
        "since": "2026-08-11",
        "then": "the complete finite-width ribbons have pairwise separation greater than seven hundredths by the triangle inequality"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "prime_smooth_ribbons_are_globally_disjoint_at_declared_width"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "every unordered pair of P7 or P5 carriers is subdivided over the complete parameter torus",
        "since": "2026-08-11",
        "then": "a deterministic Lipschitz certificate establishes centerline separation greater than nine hundredths under the declared binary64 roundoff boundary"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "prime_smooth_ribbons_have_global_centerline_margin"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "regular secant readouts and tangent regularizations are combined",
        "since": "2026-08-11",
        "then": "every pair receives an integer linking number and matrix rank, nullity, determinant, and nonzero-link graph readouts are derived"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "prime_smooth_ribbons_issue_complete_linking_matrix"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "any carrier and admissible breadth",
        "since": "2026-08-11",
        "then": "the smoothed surface obeys one-turn breadth reversal and two-turn return"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "prime_smooth_ribbons_obey_mobius_return"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family certificate is built",
        "since": "2026-08-11",
        "then": "P7 is certified first and P5 is independently processed second under the same smoothing and separation protocol"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "prime_smooth_ribbons_p7_precedes_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the piecewise-linear P7 or P5 lift knots are replaced",
        "since": "2026-08-11",
        "then": "one periodic C-infinity field per carrier reproduces every exact event height without overshoot"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "prime_smooth_ribbons_preserve_all_event_lanes"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family receipt is serialized",
        "since": "2026-08-11",
        "then": "it records the numerical proof boundary and claims no arithmetic redefinition, electron ontology, zeta theorem, or Riemann-hypothesis proof"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "prime_smooth_ribbons_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a projected pair is externally tangent",
        "since": "2026-08-11",
        "then": "a one-hundredth outward pair-specific isotopy remains inside the global clearance, makes the projected circles disjoint, and certifies linking number zero"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "prime_smooth_ribbons_regularize_tangent_pairs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "flat C-infinity interpolation, exact derivative majorant, binary64 Lipschitz subdivision, pair-specific tangent isotopy, rational matrix rank",
        "module_kind": "experiment",
        "module_name": "prime_smooth_ribbons",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "SmoothPeriodicField, SmoothPrimeRibbon, PairSeparationCertificate, TangentRegularization, LinkingMatrixCertificate, SmoothRibbonCertificate, flat_step, flat_step_derivative, build_smooth_prime_seven, build_smooth_prime_five, certify_smooth_prime_seven, certify_smooth_prime_five, smooth_ribbon_family_certificate, write_smooth_ribbon_family_certificate, render_smooth_centerline_obj, render_smooth_ribbon_obj",
        "requires": "ucns_prime_phase_lift_p7_p5",
        "rollback": "remove this module, its test, documentation, generated certificate, and generated meshes",
        "rollout": "P7 first, P5 same-protocol comparison second; selection effect none; does not alter prior phase or lift receipts",
        "since": "2026-08-11",
        "storage_boundary": "caller-supplied local paths only through writer functions",
        "summary": "replaces the P7-first piecewise-linear lift by a C-infinity event-preserving field, certifies global finite-width ribbon separation by deterministic Lipschitz subdivision, regularizes tangent projections, and applies the same protocol to P5 second",
        "tests": "tests/test_prime_smooth_ribbons.py",
        "unresolved": "formal interval or proof-assistant replay, whole-link ambient isotopy, higher-order link invariants, boundary-link invariants, spectral operator, prime-power law, zeta correspondence",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_smooth_ribbons.py",
      "id": "ucns_prime_smooth_ribbons_p7_p5"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the family certificate is serialized",
        "since": "2026-08-15",
        "then": "it distinguishes presentation and ideal-boundary evidence from a complete ideal basis, link classification, phase selection, or spectral claim"
      },
      "file": "src/ucns/prime_symbolic_alexander.py",
      "id": "prime_symbolic_alexander_receipt_is_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "regression",
        "given": "the symbolic matrix is specialized at every previously frozen prime-order character",
        "since": "2026-08-15",
        "then": "every modular rank equals the independently retained Fox-character fingerprint"
      },
      "file": "src/ucns/prime_symbolic_alexander.py",
      "id": "prime_symbolic_certificate_replays_finite_characters"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the exact symbolic presentation is evaluated over its Laurent-polynomial fraction field",
        "since": "2026-08-15",
        "then": "exact rank and a nonzero pivot minor certify every earlier elementary ideal as zero and the declared first nonzero ideal as nonzero"
      },
      "file": "src/ucns/prime_symbolic_alexander.py",
      "id": "prime_symbolic_elementary_boundary_is_exact"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the frozen P7 or P5 Wirtinger diagram is abelianized over one Laurent variable per component",
        "since": "2026-08-15",
        "then": "every sparse Fox entry has exact integer Laurent coefficients and every row satisfies the Fox fundamental identity"
      },
      "file": "src/ucns/prime_symbolic_alexander.py",
      "id": "prime_symbolic_fox_presentation_is_exact"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact Laurent Fox derivatives, rational-function rank, pivot minor, Fox fundamental identity",
        "module_kind": "experiment",
        "module_name": "prime_symbolic_alexander",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "SymbolicAlexanderCertificate, symbolic_alexander_certificate, symbolic_alexander_family_certificate, write_symbolic_alexander_family_certificate",
        "requires": "ucns_prime_exact_milnor_alexander_p7_p5, sympy>=1.12,<2",
        "rollback": "remove this module, its tests, documentation, and generated certificate",
        "rollout": "P7 first and P5 same-construction comparison second; selection effect none",
        "since": "2026-08-15",
        "storage_boundary": "caller-supplied local paths only through writer functions",
        "summary": "derives the exact multivariable Fox-Alexander presentations and certifies their first nonzero elementary-ideal boundaries for the frozen P7 and P5 diagrams",
        "tests": "tests/test_prime_symbolic_alexander.py",
        "unresolved": "complete generating sets and Groebner bases for the first nonzero ideals, higher elementary ideals, phase-co-winner separation, higher Milnor invariants",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/prime_symbolic_alexander.py",
      "id": "ucns_prime_symbolic_alexander_p7_p5"
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
        "class": "doctrine",
        "given": "a valid receipt is produced or consumed",
        "then": "candidate integration does not select geometry, prove usefulness, or establish privacy"
      },
      "file": "src/ucns/ptcna_state.py",
      "id": "ucns_ptcna_candidate_transfers_no_status"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the same exact UCNS producer commit and module bytes",
        "then": "canonical receipt bytes and state digest are byte-identical and bind the exact public-gonol provenance"
      },
      "file": "src/ucns/ptcna_state.py",
      "id": "ucns_ptcna_receipt_is_deterministic_and_provenance_bound"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "any authority-bearing receipt field is changed",
        "then": "validation fails before downstream state construction"
      },
      "file": "src/ucns/ptcna_state.py",
      "id": "ucns_ptcna_receipt_rejects_tampering"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the PTCNA candidate receipt is built",
        "then": "it describes exactly 157x7x7x53 C-order little-endian float64 state with every element present and initialized to positive zero"
      },
      "file": "src/ucns/ptcna_state.py",
      "id": "ucns_ptcna_state_has_exact_requested_shape"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "canonical serialization, streaming zero-state digest, producer checkout verification",
        "module_kind": "schema",
        "module_name": "ptcna_state",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "PTCNA_STATE_SHAPE, PTCNAStateReceiptError, build_ptcna_state_receipt, validate_ptcna_state_receipt, write_ptcna_state_receipt",
        "requires": "edcm_word_gonol_profile",
        "rollback": "remove this module and export without changing the 157-position EDCM carrier or any prior candidate",
        "rollout": "explicit candidate receipt generation only; no universal UCNS or PTCNA selection",
        "since": "2026-08-17",
        "storage_boundary": "write",
        "summary": "emits and validates the candidate-scoped dense 157x7x7x53 PTCNA initialization state with deterministic provenance receipts",
        "tests": "tests/test_ptcna_state.py",
        "unresolved": "continuous seven-fold geometry, representative efficacy, and any canonical higher-gonol composition law",
        "user_data_boundary": "none"
      },
      "file": "src/ucns/ptcna_state.py",
      "id": "ucns_ptcna_candidate_state"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a relational carrier is constructed or parsed",
        "since": "2026-08-16",
        "then": "its complete intrinsic payload contains only schema identity, dense integer node addresses, ordered typed integer relations, and permanently false transfer fields"
      },
      "file": "src/ucns/relational_carrier.py",
      "id": "relational_carrier_is_intrinsic_and_metadata_free"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "node order, edge order, multiplicity, relation code, endpoint, or sidedness differs",
        "since": "2026-08-16",
        "then": "the canonical bytes and stable identity differ without sorting or deduplication"
      },
      "file": "src/ucns/relational_carrier.py",
      "id": "relational_carrier_preserves_order_multiplicity_and_sidedness"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "canonical carrier bytes are parsed and serialized again",
        "since": "2026-08-16",
        "then": "the resulting bytes are exactly identical and malformed or noncanonical input fails closed"
      },
      "file": "src/ucns/relational_carrier.py",
      "id": "relational_carrier_roundtrip_is_canonical"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_bytes",
        "module_kind": "schema",
        "module_name": "relational_carrier",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "RelationalNode, RelationalEdge, RelationalCarrier, build_relational_carrier, relational_carrier_bytes, parse_relational_carrier",
        "requires": "none",
        "rollback": "remove module and exports without changing carrier, geometry, measurement, or option decisions",
        "rollout": "explicit non-geometric representation bridge; no consumer activation or canonical UCNS object",
        "since": "2026-08-16",
        "storage_boundary": "serialized intrinsic representation bytes only",
        "summary": "constructs deterministic metadata-free ordered relational carriers from dense occurrence addresses and caller-declared relation codes",
        "tests": "tests.test_relational_carrier",
        "unresolved": "geometric assignment, higher-gonol composition, canonical structural equivalence, M, B, and domain interpretation of relation codes",
        "user_data_boundary": "accepts integers only; domain evidence and provenance remain external"
      },
      "file": "src/ucns/relational_carrier.py",
      "id": "ucns_relational_carrier"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "initiation, positive 360-degree motion, positive 720-degree motion, and inverse 360-degree motion are evaluated",
        "since": "2026-07-29",
        "then": "mapping after native motion exactly equals chart motion after mapping for every declared transition"
      },
      "file": "src/ucns/root_loop_chart.py",
      "id": "root_loop_chart_commutes_with_bounded_motion"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "any exact rational state in the bounded framed Mobius root-loop domain or its exact directed-cover chart image",
        "since": "2026-07-29",
        "then": "both Mobius-to-cover-to-Mobius and cover-to-Mobius-to-cover round trips restore every retained state distinction"
      },
      "file": "src/ucns/root_loop_chart.py",
      "id": "root_loop_chart_maps_are_exact_two_way_inverses"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the complete v0.6 minimum witness packet enters the v0.7 chart adapter",
        "since": "2026-07-29",
        "then": "all fourteen word initiations retain exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and completion scope"
      },
      "file": "src/ucns/root_loop_chart.py",
      "id": "root_loop_chart_preserves_every_source_linked_initiation"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the complete v0.7 report is produced",
        "since": "2026-07-29",
        "then": "F12 is supported and F13 falsified only for the declared root-loop witness domain while selection remains none and global equivalence, completion, higher geometry, EDCM, and METAPAT remain unresolved"
      },
      "file": "src/ucns/root_loop_chart.py",
      "id": "root_loop_chart_support_is_bounded_and_nonselecting"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a native frame is mapped to a directed-cover representative",
        "since": "2026-07-29",
        "then": "first-versus-second lifted representative carries the candidate chart correspondence while the directed carrier API remains unchanged and no topology-owned orientation field is invented"
      },
      "file": "src/ucns/root_loop_chart.py",
      "id": "root_loop_chart_uses_cover_sheet_as_hypothesis_not_native_orientation"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact-turn normalization and report-matrix adapters",
        "module_kind": "experiment",
        "module_name": "root_loop_chart",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "RootLoopCoverChartState, RootLoopChartRoundTrip, RootLoopChartReport, mobius_to_root_loop_cover, root_loop_cover_to_mobius, build_root_loop_chart_round_trips, build_root_loop_chart_evidence, run_v07_root_loop_chart_experiment",
        "requires": "directed_carrier_floor, edcm_mobius_carrier_experiment, edcm_native_direct_mobius_candidate",
        "rollback": "remove this module, its exports, tests, and v0.7 candidate document while retaining the v0.5 and v0.6 experiments",
        "rollout": "explicit UCNS-only v0.7 bounded chart experiment; no global carrier equivalence, carrier selection, completion, EDCM activation, or METAPAT activation",
        "since": "2026-07-29",
        "storage_boundary": "none",
        "summary": "tests an exact reversible chart between the native framed Mobius root loop and the directed twofold cover over the bounded v0.7 witness domain",
        "tests": "tests/test_root_loop_chart.py",
        "unresolved": "extension beyond the framed root loop, transverse and radial assignment, arbitrary element assignment, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions",
        "user_data_boundary": "exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and completion scope remain linked through both maps"
      },
      "file": "src/ucns/root_loop_chart.py",
      "id": "edcm_root_loop_cover_chart_candidate"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "one valid source-coordinate derivation is applied",
        "since": "2026-07-31",
        "then": "exact candidate and inverse, native frame, local side, GeometricAssignment, and declared-loss rendering remain mutually consistent"
      },
      "file": "src/ucns/source_coordinate.py",
      "id": "source_coordinate_assignment_applies_exact_candidate_reversibly"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "one initiated v0.17 outcome receives a derived coordinate",
        "since": "2026-07-31",
        "then": "the exact upstream trace and outcome objects, admission, initiation, boundary, source address, law identity, formula, and code reference remain linked"
      },
      "file": "src/ucns/source_coordinate.py",
      "id": "source_coordinate_derivation_retains_exact_initiation_identity"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "distinct occurrence indices in the same declared finite scope",
        "since": "2026-07-31",
        "then": "their exact source positions, transverse values, lifted turns, and coordinate identities remain distinct without binary64 conversion"
      },
      "file": "src/ucns/source_coordinate.py",
      "id": "source_coordinate_law_is_exact_and_scope_injective"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "v0.19 evidence is reported",
        "since": "2026-07-31",
        "then": "digests, runtime identity, A0 lanes, carrier position, projections, and renderings derive no coordinate while selection, higher geometry, completion, and activation remain absent"
      },
      "file": "src/ucns/source_coordinate.py",
      "id": "source_coordinate_law_rejects_identity_shortcuts_and_nonselection"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "an occurrence index i and an authority-bearing completion binding for a complete finite ordered scope of cardinality n",
        "since": "2026-07-31",
        "then": "exact p=(2i+1)/(2n), u=2p-1, and t=2p derive only from the bound source address and invalid, sampled, prefixed, or unbound addresses fail closed"
      },
      "file": "src/ucns/source_coordinate.py",
      "id": "source_coordinate_law_uses_complete_ordered_source_address"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "an authority-bound complete v0.17 initiation trace enters v0.19",
        "since": "2026-07-31",
        "then": "every exact outcome appears once in order as derived-assigned, blocked-unresolved, or blocked-rejected with no prefix, reordering, deduplication, or fallback"
      },
      "file": "src/ucns/source_coordinate.py",
      "id": "source_coordinate_outcomes_are_total_exclusive_and_ordered"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "complete-scope binding requires a producer-issued v0.17 exhaustion receipt over the exact fixed full authority-report trace and its complete ordered outcome evidence digest; callers cannot supply authority fields, cardinality, outcome ids, outcome contents, or consistently truncated report layers inline",
        "internal_surface": "fixed SC01-SC10 evidence construction and exact validation helpers",
        "module_kind": "experiment",
        "module_name": "source_coordinate",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "CompleteOrderedSourceScopeBinding, OrderedSourceCoordinate, SourceCoordinateDerivation, AppliedSourceCoordinateAssignment, SourceCoordinateOutcome, SourceCoordinateTrace, SourceCoordinateBoundaryReport, SourceCoordinateDisposition, SourceCoordinateEvidenceStanding, SourceCoordinateFalsifierResult, bind_complete_ordered_source_scope, derive_ordered_source_coordinate, derive_source_coordinate, apply_source_coordinate_assignment, derive_source_coordinate_trace, run_v019_source_coordinate_derivation_experiment",
        "requires": "edcm_explicit_geometric_assignment_boundary, edcm_gonol_initiation_structural_null_boundary, edcm_exact_coordinate_representation_boundary",
        "rollback": "remove this module, exports, tests, and v0.19 document while retaining v0.18 explicit-input candidate application",
        "rollout": "nonselecting v0.19 ordered-source-address derivation candidate over authority-bound complete scopes and explicitly initiated words with explicit blocked outcomes and no construction completion or activation",
        "since": "2026-07-31",
        "storage_boundary": "none",
        "summary": "derives exact signed-local circle-candidate coordinates from authority-bound complete finite ordered source-occurrence addresses while retaining exact upstream initiation identity and explicit blocked outcomes",
        "tests": "tests/test_source_coordinate.py",
        "unresolved": "canonical law selection, cross-scope and higher-gonol composition, total Structural Null topology, higher geometry, completion, faithful breadth, and consumer activation",
        "user_data_boundary": "a producer-issued completion receipt, exact v0.17 authority report and trace identity, source occurrence index, and report-derived complete finite scope cardinality derive coordinates; content, caller-supplied authority fields, digests, runtime identity, carrier position, and projections do not"
      },
      "file": "src/ucns/source_coordinate.py",
      "id": "edcm_source_coordinate_derivation_boundary"
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
        "class": "doctrine",
        "given": "a v0.9 round trip, restriction, motion, convention, collision, or report verdict is constructed",
        "since": "2026-07-29",
        "then": "the named versioned exact comparison policy and implementation reference are retained and no hidden equality tolerance is used"
      },
      "file": "src/ucns/transverse_envelope.py",
      "id": "transverse_envelope_comparison_policy_is_explicit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "the complete v0.9 report is produced",
        "since": "2026-07-29",
        "then": "F12 support and F13 falsification retain only the v0.7 root-loop map identity while transverse cover extension remains inconclusive and selection remains none"
      },
      "file": "src/ucns/transverse_envelope.py",
      "id": "transverse_envelope_does_not_extend_cover_verdicts"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "two distinct transverse values share the same v0.7 root state",
        "since": "2026-07-29",
        "then": "their envelope identities remain distinct while their actual directed-cover coordinates coincide, proving that the envelope is not an injective transverse cover map"
      },
      "file": "src/ucns/transverse_envelope.py",
      "id": "transverse_envelope_exposes_cover_nonembedding"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "a framed native state with any admitted exact rational transverse coordinate and either coordinate convention",
        "since": "2026-07-29",
        "then": "native-to-envelope-to-native and envelope-to-native-to-envelope restore every declared identity field under the pinned exact comparison policy"
      },
      "file": "src/ucns/transverse_envelope.py",
      "id": "transverse_envelope_maps_preserve_exact_rational_state"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a v0.9 report is constructed or replaced through the public dataclass API",
        "since": "2026-07-29",
        "then": "every expected event, fiber, convention, and transition key appears exactly once in declared order and remains cross-checked against the v0.7 root report"
      },
      "file": "src/ucns/transverse_envelope.py",
      "id": "transverse_envelope_report_validates_complete_witness_identities"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "correctness",
        "given": "the transverse coordinate is exact zero",
        "since": "2026-07-29",
        "then": "removing the envelope field recovers the unchanged v0.7 native and cover root-loop states for every initiation and both conventions"
      },
      "file": "src/ucns/transverse_envelope.py",
      "id": "transverse_envelope_restricts_exactly_to_v07_root_loop"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "exact identity adapters, exhaustive witness-key validation, root restriction witnesses, motion witnesses, and cover-collision evidence",
        "module_kind": "experiment",
        "module_name": "transverse_envelope",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "FramedMobiusStripState, TransverseCoordinateConvention, TransverseEnvelopeState, TransverseEnvelopeReport, TransverseCarrierCollisionWitness, exact_rational_stress_fibers, mobius_to_transverse_envelope, transverse_envelope_to_mobius, convert_transverse_convention, run_v09_transverse_envelope_experiment",
        "requires": "edcm_root_loop_cover_chart_candidate, edcm_native_direct_mobius_candidate, explicit_comparison_policy_layer",
        "rollback": "remove this module, its exports, tests, and v0.9 document while retaining the v0.5 through v0.7 experiments and the v0.8 historical erratum",
        "rollout": "explicit UCNS-only v0.9 repair and bounded exact-rational stress experiment; no transverse cover embedding, radial assignment, arbitrary-element assignment, global carrier equivalence, carrier selection, completion, EDCM activation, or METAPAT activation",
        "since": "2026-07-29",
        "storage_boundary": "none",
        "summary": "repairs the v0.8 sidecar overclaim and evaluates a source-preserving exact-rational transverse envelope without claiming a directed-cover embedding",
        "tests": "tests/test_transverse_envelope.py",
        "unresolved": "an injective transverse or radial directed-cover coordinate, faithful-breadth assignment, arbitrary element assignment, real-valued continuity, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions",
        "user_data_boundary": "exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and native completion scope remain linked through every envelope map"
      },
      "file": "src/ucns/transverse_envelope.py",
      "id": "edcm_exact_rational_transverse_envelope_experiment"
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
        "call": "self::test_admission_requires_adapter_and_keeps_digest_out_of_geometry",
        "cleanup": "none",
        "mutates": "none",
        "proves": "assignment_admission_requires_explicit_domain_adapter",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_assignment_boundary.py",
      "id": "check_assignment_admission_explicit_adapter"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_trace_preserves_equal_content_as_distinct_ordered_occurrences",
        "cleanup": "none",
        "mutates": "none",
        "proves": "assignment_admission_preserves_occurrence_order_and_multiplicity",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_assignment_boundary.py",
      "id": "check_assignment_admission_occurrence_preservation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_v016_report_retains_upstream_and_unresolved_geometry",
        "cleanup": "none",
        "mutates": "none",
        "proves": "assignment_boundary_does_not_complete_initiation_or_activate",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_assignment_boundary.py",
      "id": "check_assignment_boundary_nonactivation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_identity_derived_mechanisms_are_rejected_without_geometry",
        "cleanup": "none",
        "mutates": "none",
        "proves": "assignment_identity_mechanisms_cannot_derive_geometry",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_assignment_boundary.py",
      "id": "check_assignment_identity_mechanism_rejection"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_outcome_partition_is_total_exclusive_and_fail_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "assignment_outcome_is_total_and_exclusive_over_admitted_evidence",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_assignment_boundary.py",
      "id": "check_assignment_outcome_partition"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_supplied_candidate_is_retained_without_derivation_or_selection",
        "cleanup": "none",
        "mutates": "none",
        "proves": "supplied_assignment_remains_candidate_evidence",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_assignment_boundary.py",
      "id": "check_assignment_supplied_candidate_evidence"
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
        "call": "self::test_candidate_image_materializes_declared_breadth_and_root_angle",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_coordinate_uses_actual_cover_fields",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_carrier_coordinate.py",
      "id": "check_carrier_coordinate_actual_cover_fields"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_signed_local_candidate_is_bounded_admissible_without_selection",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_coordinate_constructive_result_does_not_select",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_carrier_coordinate.py",
      "id": "check_carrier_coordinate_constructive_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_rejected_candidates_retain_exact_collision_and_motion_witnesses",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_coordinate_admissibility_retains_failures",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_carrier_coordinate.py",
      "id": "check_carrier_coordinate_failure_retention"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_candidate_family_is_explicit_ordered_and_nonselecting",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_coordinate_family_is_explicit_and_nonselecting",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_carrier_coordinate.py",
      "id": "check_carrier_coordinate_family_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_every_candidate_zero_fiber_is_the_v07_actual_root",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_coordinate_zero_fiber_restricts_to_v07",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_carrier_coordinate.py",
      "id": "check_carrier_coordinate_root_restriction"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_report_rejects_count_preserving_identity_substitution",
        "cleanup": "none",
        "mutates": "none",
        "proves": "carrier_coordinate_report_validates_complete_witness_identities",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_carrier_coordinate.py",
      "id": "check_carrier_coordinate_witness_identities"
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
        "proves": "edcm_completion_is_scoped_not_epistemic_exhaustion",
        "timeout": "10"
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
        "proves": "edcm_scalar_projection_is_declared_lossy",
        "timeout": "10"
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
        "proves": "edcm_motion_retains_trajectory_identity",
        "timeout": "10"
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
        "proves": "edcm_motion_retains_trajectory_identity",
        "timeout": "10"
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
        "proves": "edcm_unknown_motion_laws_remain_explicit",
        "timeout": "10"
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
        "proves": "edcm_motion_retains_trajectory_identity",
        "timeout": "10"
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
        "proves": "edcm_space_manifestations_assign_to_origin",
        "timeout": "10"
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
        "proves": "edcm_public_gonol_fixture_is_exact",
        "timeout": "10"
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
        "proves": "edcm_alphabet_failure_is_positive_evidence",
        "timeout": "10"
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
        "proves": "edcm_source_text_is_not_normalized",
        "timeout": "10"
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
        "proves": "edcm_source_text_is_not_normalized",
        "timeout": "10"
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
        "proves": "edcm_space_manifestations_assign_to_origin",
        "timeout": "10"
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
        "proves": "edcm_space_manifestations_assign_to_origin",
        "timeout": "10"
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
        "proves": "edcm_space_manifestations_assign_to_origin",
        "timeout": "10"
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
        "proves": "edcm_source_text_is_not_normalized",
        "timeout": "10"
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
        "proves": "edcm_source_text_is_not_normalized",
        "timeout": "10"
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
        "proves": "edcm_speaker_turn_has_unit_support",
        "timeout": "10"
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
        "proves": "edcm_alphabet_failure_is_positive_evidence",
        "timeout": "10"
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
        "proves": "edcm_word_is_the_smallest_gonol",
        "timeout": "10"
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
        "call": "self::test_binary64_breadth_collision_retains_exact_distinction",
        "cleanup": "none",
        "mutates": "none",
        "proves": "exact_coordinate_binary64_breadth_collision_is_retained",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_exact_coordinate.py",
      "id": "check_exact_coordinate_binary64_breadth_collision"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_binary64_point_is_linked_lossy_rendering_only",
        "cleanup": "none",
        "mutates": "none",
        "proves": "exact_coordinate_binary64_is_declared_rendering",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_exact_coordinate.py",
      "id": "check_exact_coordinate_binary64_rendering_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_binary64_turn_collision_retains_exact_distinction",
        "cleanup": "none",
        "mutates": "none",
        "proves": "exact_coordinate_binary64_turn_collision_is_retained",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_exact_coordinate.py",
      "id": "check_exact_coordinate_binary64_turn_collision"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_exact_coordinate_retains_fixed_provenance_and_fails_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "exact_coordinate_provenance_is_fixed_and_retained",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_exact_coordinate.py",
      "id": "check_exact_coordinate_fixed_provenance"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_v011_report_keeps_selection_and_activation_absent",
        "cleanup": "none",
        "mutates": "none",
        "proves": "exact_coordinate_boundary_does_not_select_or_activate",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_exact_coordinate.py",
      "id": "check_exact_coordinate_nonselection_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_signed_local_exact_law_round_trips_rational_domain",
        "cleanup": "none",
        "mutates": "none",
        "proves": "exact_coordinate_signed_local_law_round_trips",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_exact_coordinate.py",
      "id": "check_exact_coordinate_signed_local_round_trip"
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
        "call": "self::test_assignment_applies_exact_signed_local_candidate_reversibly",
        "cleanup": "none",
        "mutates": "none",
        "proves": "explicit_geometry_applies_exact_signed_local_candidate_reversibly",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_explicit_geometric_assignment.py",
      "id": "check_explicit_geometry_exact_candidate_application"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_assignment_preserves_frame_side_and_rendering_boundary",
        "cleanup": "none",
        "mutates": "none",
        "proves": "explicit_geometry_preserves_mobius_frame_and_local_side",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_explicit_geometric_assignment.py",
      "id": "check_explicit_geometry_frame_side_and_rendering"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_proposal_requires_initiated_word_and_independent_exact_input",
        "cleanup": "none",
        "mutates": "none",
        "proves": "explicit_geometry_requires_initiated_word_and_independent_exact_input",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_explicit_geometric_assignment.py",
      "id": "check_explicit_geometry_independent_exact_input"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_v018_report_retains_unresolved_law_and_nonactivation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "explicit_geometry_does_not_claim_total_law_complete_select_or_activate",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_explicit_geometric_assignment.py",
      "id": "check_explicit_geometry_nonactivation_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_rejected_mechanisms_never_create_an_applied_assignment",
        "cleanup": "none",
        "mutates": "none",
        "proves": "explicit_geometry_rejects_identity_projection_and_upstream_substitution",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_explicit_geometric_assignment.py",
      "id": "check_explicit_geometry_rejected_mechanisms"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_trace_is_total_exclusive_ordered_and_occurrence_preserving",
        "cleanup": "none",
        "mutates": "none",
        "proves": "explicit_geometry_outcomes_are_total_exclusive_and_ordered",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_explicit_geometric_assignment.py",
      "id": "check_explicit_geometry_total_outcomes"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_plan_requires_execution_generated_completion_receipt",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "external_evaluation_requires_completed_corpus_gate",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_external_evaluation.py",
      "id": "check_external_evaluation_corpus_gate"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_complete_external_receipt_is_candidate_evidence_only",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "external_evaluation_receipt_is_nonpromoting",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_external_evaluation.py",
      "id": "check_external_evaluation_nonpromotion"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_timeout_input_output_and_executable_bounds_fail_closed",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "external_evaluation_is_resource_bounded",
        "requires": "python3",
        "timeout": "20"
      },
      "file": "tests/test_external_evaluation.py",
      "id": "check_external_evaluation_resource_bounds"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_request_binds_identity_command_cases_and_disclosure",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "external_evaluator_identity_and_disclosure_are_bound",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_external_evaluation.py",
      "id": "check_external_evaluator_identity_disclosure_binding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_response_requires_exact_protocol_and_ordered_case_coverage",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "external_response_reconciliation_is_fail_closed",
        "requires": "python3",
        "timeout": "15"
      },
      "file": "tests/test_external_evaluation.py",
      "id": "check_external_response_reconciliation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_external_edcm_receipt_handoff_is_exact_and_nonpromoting",
        "cleanup": "none",
        "mutates": "none",
        "proves": "external_multiwoz_v0141_handoff_is_exact_and_nonpromoting",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_carrier_attachment.py",
      "id": "check_edcm_multiwoz_v0141_handoff"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_affine_certificate_retains_exact_universal_proof_data",
        "cleanup": "none",
        "mutates": "none",
        "proves": "full_carrier_affine_certificate_is_universal_and_exact",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_carrier_attachment.py",
      "id": "check_full_carrier_affine_certificate"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_report_retains_analytic_and_bounded_executable_scopes",
        "cleanup": "none",
        "mutates": "none",
        "proves": "full_carrier_attachment_retains_mixed_evidence_scopes",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_carrier_attachment.py",
      "id": "check_full_carrier_mixed_scope_report"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_report_rejects_scope_completion_selection_and_activation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "full_carrier_attachment_does_not_complete_select_or_activate",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_carrier_attachment.py",
      "id": "check_full_carrier_nonactivation_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_quotient_certificate_commutes_and_excludes_structural_null",
        "cleanup": "none",
        "mutates": "none",
        "proves": "full_carrier_quotient_certificate_commutes_without_moving_the_marked_seam",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_carrier_attachment.py",
      "id": "check_full_carrier_quotient_certificate"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_exact_stream_digest_is_stable_across_equivalent_iterables",
        "cleanup": "none",
        "mutates": "none",
        "proves": "full_corpus_gate_requires_exact_stream_reconstruction",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_corpus.py",
      "id": "check_full_corpus_exact_reconstruction"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_complete_run_exhausts_every_turn_and_matches_expected_count",
        "cleanup": "none",
        "mutates": "none",
        "proves": "full_corpus_gate_requires_exhaustion_and_turn_count",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_corpus.py",
      "id": "check_full_corpus_exhaustion_and_count_gate"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_manifest_pins_source_adapter_and_admission_boundary",
        "cleanup": "none",
        "mutates": "none",
        "proves": "full_corpus_manifest_pins_admission_identity",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_corpus.py",
      "id": "check_full_corpus_manifest_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_completion_receipt_opens_analysis_only",
        "cleanup": "none",
        "mutates": "none",
        "proves": "full_corpus_receipt_has_no_selection_or_activation_effect",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_corpus.py",
      "id": "check_full_corpus_receipt_nonactivation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_partial_iteration_and_count_mismatch_cannot_issue_receipts",
        "cleanup": "none",
        "mutates": "none",
        "proves": "incomplete_corpus_run_fails_closed",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_corpus.py",
      "id": "check_incomplete_corpus_fail_closed"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_invalid_turn_records_exact_stopping_boundary",
        "cleanup": "none",
        "mutates": "none",
        "proves": "incomplete_corpus_run_fails_closed",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_full_corpus.py",
      "id": "check_invalid_corpus_turn_fail_closed"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_word_gonol_requires_one_source_bound_structural_null_twist",
        "cleanup": "none",
        "mutates": "none",
        "proves": "gonol_initiation_requires_explicit_structural_null_transition",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_gonol_initiation.py",
      "id": "check_gonol_initiation_explicit_transition"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_v017_report_retains_unresolved_geometry_and_nonactivation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "gonol_initiation_does_not_assign_complete_select_or_activate",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_gonol_initiation.py",
      "id": "check_gonol_initiation_nonactivation_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_origin_registry_separates_structural_null_from_neighboring_roles",
        "cleanup": "none",
        "mutates": "none",
        "proves": "gonol_initiation_origin_roles_are_domain_separated",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_gonol_initiation.py",
      "id": "check_gonol_initiation_origin_role_separation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_neighboring_zero_and_absence_roles_cannot_become_prestate",
        "cleanup": "none",
        "mutates": "none",
        "proves": "gonol_initiation_rejects_zero_and_absence_substitutions",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_gonol_initiation.py",
      "id": "check_gonol_initiation_rejected_substitutions"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_root_return_preserves_360_change_720_return_and_noncompletion",
        "cleanup": "none",
        "mutates": "none",
        "proves": "gonol_initiation_root_return_is_bounded_and_noncompleting",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_gonol_initiation.py",
      "id": "check_gonol_initiation_root_return_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_scope_completion_receipt_derives_only_from_exact_authority_report",
        "cleanup": "none",
        "mutates": "none",
        "proves": "gonol_initiation_scope_receipt_is_producer_issued",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_gonol_initiation.py",
      "id": "check_gonol_initiation_scope_receipt_authority"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_initiation_trace_is_total_exclusive_ordered_and_occurrence_preserving",
        "cleanup": "none",
        "mutates": "none",
        "proves": "gonol_initiation_outcome_is_total_and_exclusive",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_gonol_initiation.py",
      "id": "check_gonol_initiation_total_outcome_relation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_marked_seam_survives_numeric_coordinate_cut_movement",
        "cleanup": "none",
        "mutates": "none",
        "proves": "partial_initiation_seam_is_provenance_bearing",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_initiation_boundary.py",
      "id": "check_partial_initiation_marked_seam_provenance"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_360_changes_720_returns_and_two_motion_receipts_survive",
        "cleanup": "none",
        "mutates": "none",
        "proves": "partial_initiation_motion_preserves_360_720_and_history",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_initiation_boundary.py",
      "id": "check_partial_initiation_motion_history"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_v013_report_is_complete_bounded_and_nonselecting",
        "cleanup": "none",
        "mutates": "none",
        "proves": "partial_initiation_report_executes_rc_packet_without_selection",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_initiation_boundary.py",
      "id": "check_partial_initiation_rc_packet"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_exact_sheet_involution_matches_signed_local_quotient",
        "cleanup": "none",
        "mutates": "none",
        "proves": "partial_initiation_exact_quotient_compatibility",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_initiation_boundary.py",
      "id": "check_partial_initiation_sheet_involution"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_structural_null_is_disjoint_typed_prestate_with_partial_edges",
        "cleanup": "none",
        "mutates": "none",
        "proves": "partial_initiation_structural_null_topology_is_explicit",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_initiation_boundary.py",
      "id": "check_partial_initiation_structural_null_topology"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_every_word_attachment_has_one_source_bound_twist_receipt",
        "cleanup": "none",
        "mutates": "none",
        "proves": "partial_initiation_twist_receipt_is_source_bound",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_initiation_boundary.py",
      "id": "check_partial_initiation_twist_receipts"
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
        "call": "self::test_source_word_and_glyph_boundaries",
        "cleanup": "none",
        "mutates": "none",
        "proves": "lexical_floor_source_receipt_binds_packaged_bytes, lexical_floor_words_are_unique_exact_glyph_sets, lexical_floor_order_is_serialization_only, lexical_floor_reuses_canonical_glyph_assignment",
        "timeout": "30"
      },
      "file": "tests/test_lexical_floor.py",
      "id": "lexical_floor_source_and_word_check"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_projection_candidate_and_definition_boundaries",
        "cleanup": "none",
        "mutates": "none",
        "proves": "lexical_hyperspace_is_occurrence_preserving_projection_not_embedding, affixiation_and_compounding_are_candidate_layers, definitions_are_context_plural_and_immutable",
        "timeout": "30"
      },
      "file": "tests/test_lexical_floor_layers.py",
      "id": "lexical_floor_layer_check"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_snapshot_chain_is_source_bound_and_fail_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "every_added_layer_has_a_source_bound_snapshot",
        "timeout": "30"
      },
      "file": "tests/test_lexical_floor_snapshots.py",
      "id": "lexical_floor_snapshot_check"
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
        "call": "self::test_center_spokes_require_six_distinct_surface_phases",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_center_needs_six_phase_channels_for_six_spokes",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_center_six_phase_channels"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_physical_contact_and_strict_braid_are_same_event_exclusive",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_physical_contact_and_strict_braid_are_event_exclusive",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_contact_braid_exclusivity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_rigid_rotation_phase_transport_matches_direct_surface_rotation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_incident_certified_dyads_are_state_incompatible",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_direct_rotation_agreement"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_generated_certificate_is_deterministic_nonselecting_and_bounded",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "mobius_seed_global_compatibility_certificate_is_nonselecting",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_global_certificate_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_all_oriented_incident_edge_states_are_incompatible",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_incident_certified_dyads_are_state_incompatible",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_incident_dyad_state_incompatibility"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pinned_pr174_schedule_inherits_zero_complete_local_certificates",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_pr174_inherits_no_exact_rigid_vesica_pairs",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_pr174_zero_inheritance"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_rigid_rotation_transport_is_exact_on_representative_spokes",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_incident_certified_dyads_are_state_incompatible",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_rigid_rotation_transport"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_compatible_certified_pairs_have_exact_maximum_capacity_three",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_single_state_certified_capacity_is_three",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_single_state_capacity_three"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_surface_phase_uses_the_unlabelled_half_turn_quotient",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_incident_certified_dyads_are_state_incompatible",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_global_compatibility.py",
      "id": "check_mobius_seed_surface_phase_quotient"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_every_structural_pair_reverses_over_under_order",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_structural_pairs_have_alternating_braid_order",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_seed.py",
      "id": "check_mobius_seed_braid_order"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_dyad_is_anti_aligned_and_outer_phases_increment",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_dyad_is_anti_aligned_and_outer_phase_is_incremental",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_seed.py",
      "id": "check_mobius_seed_dyad_phase_schedule"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_null_lift_has_six_distinct_nonzero_lanes_and_origin_margin",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_lift_preserves_null_as_nonvertex_void",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_seed.py",
      "id": "check_mobius_seed_null_void"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_projection_retains_exact_seed_nodes_and_all_pairs",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_projection_is_exact_and_pair_complete",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_seed.py",
      "id": "check_mobius_seed_projection_pair_completion"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_and_obj_are_deterministic_nonselecting_candidates",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_candidate_is_nonselecting_and_proof_firewalled",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_seed.py",
      "id": "check_mobius_seed_proof_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_each_surface_obeys_mobius_seam_and_two_turn_return",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_seed_surface_obeys_360_seam_and_720_return",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_seed.py",
      "id": "check_mobius_seed_surface_quotient"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_sturm_certificate_proves_exactly_four_physical_boundary_contacts",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_alternate_height_branch_is_obstructed",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_alternate_branch_obstruction"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_centerlines_have_exactly_two_contacts_and_positive_null_clearance",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_has_exact_two_centerline_contacts",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_centerline_contacts"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_contact_semantics_and_global_surface_boundary_remain_distinct",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_contact_semantics_are_not_flattened",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_contact_semantics"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_sturm_certificate_proves_exactly_four_physical_boundary_contacts",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_sturm_proves_four_physical_boundary_contacts",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_four_boundary_contacts"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_seed_half_turn_phase_is_obstructed_and_cannot_inherit_certificate",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_half_turn_phase_has_exact_contact_obstruction",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_half_turn_obstruction"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_centerlines_have_exactly_two_contacts_and_positive_null_clearance",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_null_origin_has_positive_clearance",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_null_clearance"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_each_band_obeys_one_turn_seam_and_two_turn_return",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_obeys_one_turn_seam_and_two_turn_return",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_quotient_return"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_combined_receipt_is_deterministic_nonselecting_and_firewalled",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "mobius_vesica_certificate_is_nonselecting_and_zeta_firewalled",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_receipt_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_seed_half_turn_phase_is_obstructed_and_cannot_inherit_certificate",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_seed_phase_mismatch_blocks_certificate_inheritance",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_seed_phase_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_sturm_certificate_proves_exactly_four_physical_boundary_contacts",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_preserves_source_claims_as_testable_geometry",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_source_claims"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_rigid_placement_plan_covers_all_twelve_structural_pairs",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_rigid_placements_cover_seed_structural_pairs",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_structural_placements"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_width_continuation_recertifies_four_contacts_at_every_stage",
        "cleanup": "none",
        "mutates": "none",
        "proves": "mobius_vesica_width_continuation_recertifies_each_stage",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_mobius_vesica_exact.py",
      "id": "check_mobius_vesica_width_continuation"
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
        "call": "self::test_complete_minor_accounting_is_sealed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_grobner_generators_cover_every_maximal_minor",
        "requires": "python3, sympy",
        "timeout": "5"
      },
      "file": "tests/test_prime_determinantal_grobner.py",
      "id": "check_prime_grobner_complete_accounting"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_result_document_preserves_research_boundary",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_grobner_receipt_preserves_nonclaims",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_determinantal_grobner.py",
      "id": "check_prime_grobner_nonclaims"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_protocol_and_parent_presentations_are_frozen",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_grobner_protocol_identity_is_frozen",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_determinantal_grobner.py",
      "id": "check_prime_grobner_protocol_frozen"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_sealed_reduced_bases_have_expected_digests",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_grobner_basis_is_complete_reduced_and_saturated",
        "requires": "python3, sympy",
        "timeout": "5"
      },
      "file": "tests/test_prime_determinantal_grobner.py",
      "id": "check_prime_grobner_reduced_bases"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_independent_replay_is_exact",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_grobner_independent_replay_agrees",
        "requires": "python3, sympy",
        "timeout": "5"
      },
      "file": "tests/test_prime_determinantal_grobner.py",
      "id": "check_prime_grobner_replay"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_borromean_magnus_benchmark_is_unit",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_magnus_benchmark_recovers_borromean_integer",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_exact_milnor_alexander.py",
      "id": "check_prime_borromean_magnus"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_family_receipt_is_deterministic_bounded_and_nonselecting",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "prime_exact_milnor_alexander_receipt_is_nonselecting",
        "requires": "python3, mpmath",
        "timeout": "180"
      },
      "file": "tests/test_prime_exact_milnor_alexander.py",
      "id": "check_prime_exact_receipt_nonselecting"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_fox_rank_fingerprints_cover_every_prime_character",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_fox_fingerprint_covers_all_prime_characters",
        "requires": "python3, mpmath",
        "timeout": "120"
      },
      "file": "tests/test_prime_exact_milnor_alexander.py",
      "id": "check_prime_fox_complete_fingerprint"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_generic_projection_preserves_positive_isotopy_clearance",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_generic_diagram_is_fixed_before_invariants",
        "requires": "python3, mpmath",
        "timeout": "30"
      },
      "file": "tests/test_prime_exact_milnor_alexander.py",
      "id": "check_prime_generic_diagram_fixed"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_generic_diagrams_reproduce_complete_linking_matrices",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_generic_diagram_preserves_pairwise_linking",
        "requires": "python3, mpmath",
        "timeout": "60"
      },
      "file": "tests/test_prime_exact_milnor_alexander.py",
      "id": "check_prime_generic_pairwise_linking"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_all_five_p7_milnor_coefficients_are_exact_zero",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_p7_five_milnor_candidates_are_exact_zero_in_diagram",
        "requires": "python3, mpmath",
        "timeout": "60"
      },
      "file": "tests/test_prime_exact_milnor_alexander.py",
      "id": "check_prime_p7_exact_milnor_zero"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_preregistration_hash_and_selector_order_are_frozen",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_selector_matches_frozen_preregistration",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_exact_milnor_alexander.py",
      "id": "check_prime_phase_preregistration_hash"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_preregistered_selector_outputs_are_not_target_fitted",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_selector_uses_whole_link_character",
        "requires": "python3, mpmath",
        "timeout": "120"
      },
      "file": "tests/test_prime_exact_milnor_alexander.py",
      "id": "check_prime_phase_whole_link_selector"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_all_frozen_turns_are_inside_outward_atan2_intervals",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_generic_turns_are_outward_atan2_enclosed",
        "requires": "python3, system-libmpfr, mpmath",
        "timeout": "60"
      },
      "file": "tests/test_prime_generic_interval_certificate.py",
      "id": "check_prime_generic_interval_atan2"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_all_p7_first_p5_second_crossing_signs_are_certified",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_generic_crossing_signs_are_interval_certified",
        "requires": "python3, system-libmpfr, mpmath",
        "timeout": "60"
      },
      "file": "tests/test_prime_generic_interval_certificate.py",
      "id": "check_prime_generic_interval_crossing_signs"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_family_receipt_is_deterministic_complete_and_nonselecting",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "prime_generic_interval_receipt_is_nonselecting",
        "requires": "python3, system-libmpfr, mpmath",
        "timeout": "120"
      },
      "file": "tests/test_prime_generic_interval_certificate.py",
      "id": "check_prime_generic_interval_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_all_smooth_height_intervals_exclude_zero_and_preserve_order",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_generic_smooth_signs_are_interval_certified",
        "requires": "python3, system-libmpfr, mpmath",
        "timeout": "60"
      },
      "file": "tests/test_prime_generic_interval_certificate.py",
      "id": "check_prime_generic_interval_smooth_signs"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_research_boundaries_remain_explicit",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_independent_phase_milnor_receipt_is_nonselecting",
        "requires": "python3",
        "timeout": "60"
      },
      "file": "tests/test_prime_independent_phase_milnor.py",
      "id": "check_prime_independent_receipt_nonselecting"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_fourier_milnor_benchmark_converges_to_minus_one",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_milnor_fourier_benchmark_recovers_borromean",
        "requires": "python3, numpy",
        "timeout": "20"
      },
      "file": "tests/test_prime_independent_phase_milnor.py",
      "id": "check_prime_milnor_borromean_benchmark"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_numerical_resolution_is_not_promoted_to_exact_theorem",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_milnor_exactness_boundary_is_preserved",
        "requires": "python3",
        "timeout": "60"
      },
      "file": "tests/test_prime_independent_phase_milnor.py",
      "id": "check_prime_milnor_exactness_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_all_five_p7_triples_converge_numerically_to_zero",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_milnor_p7_split_triples_resolve_numerically_to_zero",
        "requires": "python3, numpy",
        "timeout": "30"
      },
      "file": "tests/test_prime_independent_phase_milnor.py",
      "id": "check_prime_milnor_p7_zero_resolution"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_direct_mpfr_replay_matches_frozen_partition",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_mpfr_replay_is_backend_independent",
        "requires": "python3, libmpfr",
        "timeout": "120"
      },
      "file": "tests/test_prime_independent_phase_milnor.py",
      "id": "check_prime_mpfr_backend_independence"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_direct_mpfr_replay_recertifies_both_primes",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_mpfr_replay_recertifies_ribbon_margin",
        "requires": "python3, libmpfr",
        "timeout": "120"
      },
      "file": "tests/test_prime_independent_phase_milnor.py",
      "id": "check_prime_mpfr_ribbon_margin"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_phase_sensitivity_enumerates_all_equal_gap_alternatives",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_sensitivity_separates_selection_from_emergence",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_independent_phase_milnor.py",
      "id": "check_prime_phase_sensitivity_selection"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_p7_and_p5_share_the_same_maximum_gap_knot_degrees",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_sensitivity_torus_seven_is_not_forced",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_independent_phase_milnor.py",
      "id": "check_prime_phase_torus_seven_not_forced"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_boundary_cable_classes_and_component_knot_invariants",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_boundary_cable_winding_is_derived_from_phase",
        "requires": "python3",
        "timeout": "60"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_boundary_cable_winding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_boundary_linking_matrices_are_four_times_core_matrices",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_boundary_linking_scales_by_four",
        "requires": "python3",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_boundary_linking_fourfold"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_each_mobius_boundary_is_one_two_turn_component",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_boundary_curve_is_single_two_turn_component",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_boundary_single_two_turn_component"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_algebraically_split_triples_are_enumerated_without_fake_milnor_values",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_higher_order_boundary_is_explicit",
        "requires": "python3",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_higher_order_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_family_receipt_preserves_p7_first_order",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_interval_boundaries_p7_precedes_p5",
        "requires": "python3, mpmath",
        "timeout": "30"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_interval_boundaries_p7_first"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_and_boundary_exports_are_deterministic_and_firewalled",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "prime_interval_boundary_compact_receipt_is_nonselecting",
        "requires": "python3, mpmath",
        "timeout": "40"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_interval_boundary_compact_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_interval_replay_closes_every_complete_parameter_torus",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_interval_replay_uses_outward_endpoints",
        "requires": "python3, mpmath",
        "timeout": "30"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_interval_replay_outward_endpoints"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_legacy_surface_is_an_explicit_adapter_over_readable_evidence",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_interval_replay_uses_outward_endpoints",
        "requires": "python3, mpmath, sympy",
        "timeout": "40"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_legacy_readable_adapter"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_mixed_core_boundary_matrices_are_full_rank_with_exact_determinants",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_mixed_core_boundary_matrix_is_complete",
        "requires": "python3",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundaries.py",
      "id": "check_prime_mixed_core_boundary_matrix"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_boundary_component_cable_and_knot_invariants",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_boundary_component_knot_types_are_derived",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_boundary_component_knot_types"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_boundary_and_mixed_linking_blocks_follow_cable_homology",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_boundary_helper_is_facade_witnessed",
        "requires": "python3, sympy",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_boundary_helper_facade"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_boundary_and_mixed_linking_blocks_follow_cable_homology",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_boundary_linking_matrix_follows_cable_homology",
        "requires": "python3, sympy",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_boundary_linking_matrix"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_each_mobius_ribbon_has_one_closed_two_turn_boundary",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_boundary_curve_is_single_and_closed",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_boundary_single_closed_component"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_generic_diagram_and_length_three_milnor_profile",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_generic_helper_is_facade_witnessed",
        "requires": "python3, mpmath",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_generic_helper_facade"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_and_boundary_models_are_deterministic_and_bounded",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "prime_interval_boundary_receipt_is_nonselecting",
        "requires": "python3, mpmath, sympy",
        "timeout": "60"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_interval_boundary_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_family_certificate_preserves_p7_first_order",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_interval_boundary_p7_precedes_p5",
        "requires": "python3, mpmath, sympy",
        "timeout": "60"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_interval_boundary_research_order"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_outward_interval_replay_covers_every_pair",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_interval_common_is_facade_witnessed",
        "requires": "python3, mpmath",
        "timeout": "30"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_interval_common_facade"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_interval_margin_implies_complete_ribbon_disjointness",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_interval_replay_preserves_finite_width_disjointness",
        "requires": "python3, mpmath",
        "timeout": "30"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_interval_finite_width_disjointness"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_outward_interval_replay_covers_every_pair",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_interval_replay_is_outward_rounded",
        "requires": "python3, mpmath",
        "timeout": "30"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_interval_outward_replay"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_outward_interval_replay_covers_every_pair",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_interval_replay_helper_is_facade_witnessed",
        "requires": "python3, mpmath",
        "timeout": "30"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_interval_replay_helper_facade"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_generic_diagram_and_length_three_milnor_profile",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_length_three_milnor_profile_is_computed_after_global_lift",
        "requires": "python3, mpmath",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_length_three_milnor_profile"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_generic_diagram_and_length_three_milnor_profile",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_milnor_helper_is_facade_witnessed",
        "requires": "python3, mpmath",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_milnor_helper_facade"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_full_core_boundary_integer_invariants_distinguish_p7_and_p5",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_mixed_linking_matrix_has_exact_integer_invariants",
        "requires": "python3, sympy",
        "timeout": "20"
      },
      "file": "tests/test_prime_interval_boundary_links.py",
      "id": "check_prime_mixed_integer_invariants"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_is_deterministic_and_bounded",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "prime_p7_length4_receipt_is_bounded",
        "requires": "python3, mpmath",
        "timeout": "60"
      },
      "file": "tests/test_prime_length4_milnor.py",
      "id": "check_prime_length4_bounded_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_frozen_degree_three_commutator_gate",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_length4_magnus_gate_matches_frozen_commutator",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_length4_milnor.py",
      "id": "check_prime_length4_commutator_gate"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_result_records_primary_reverse_and_cyclic_coefficients",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_p7_length4_result_records_cyclic_conventions",
        "requires": "python3, mpmath",
        "timeout": "60"
      },
      "file": "tests/test_prime_length4_milnor.py",
      "id": "check_prime_length4_cyclic_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_frozen_target_and_lower_order_gates",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_p7_length4_target_is_frozen_and_lower_gated",
        "requires": "python3, mpmath",
        "timeout": "60"
      },
      "file": "tests/test_prime_length4_milnor.py",
      "id": "check_prime_length4_lower_gates"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_phase_co_winners_bind_identical_inputs",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_nilpotent_phase_binding_is_topological",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_nilpotent_discriminator.py",
      "id": "check_nilpotent_phase_binding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_checked_in_receipt_records_exact_replay",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_nilpotent_primary_and_replay_agree",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_nilpotent_discriminator.py",
      "id": "check_nilpotent_primary_replay"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_protocol_identity_and_frozen_receipt",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_nilpotent_protocol_identity_is_frozen",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_nilpotent_discriminator.py",
      "id": "check_nilpotent_protocol_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_comparison_excludes_weight_one_rank",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_nilpotent_comparison_excludes_known_rank",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_nilpotent_discriminator.py",
      "id": "check_nilpotent_rank_exclusion"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_every_hypernode_has_distinct_phase_and_height",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_data_covers_every_p7_p5_hypernode",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_data_coverage"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_projected_pair_events_are_strictly_height_separated",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_centerlines_are_disjoint",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_disjoint_centerlines"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_every_hypernode_has_distinct_phase_and_height",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_resolves_every_hypernode",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_hypernodes"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_link_readouts_follow_global_lift",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_link_numbers_are_derived",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_links"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_link_readouts_follow_global_lift",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_model_derives_links_after_global_lift",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_model_derived_links"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_projected_pair_events_are_strictly_height_separated",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_model_preserves_event_semantics",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_model_event_semantics"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_p7_origin_remains_one_arity_six_hypernode",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_preserves_nary_origin",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_origin"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_p5_is_independent_same_protocol_comparison",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_p5_follows_same_protocol",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_p5_second"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_p7_global_candidate_precedes_readouts",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_constructs_p7_before_restrictions",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_p7_first"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_is_deterministic_and_bounded",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "prime_phase_lift_receipt_is_nonselecting",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_mobius_one_turn_reversal_and_two_turn_return",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_phase_lift_is_seam_compatible",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_phase_lift.py",
      "id": "check_prime_phase_lift_seam"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_arithmetic_and_geometry_are_separate",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_arithmetic_geometry_firewall",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_primitives.py",
      "id": "check_prime_arithmetic_geometry_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_p5_exact_signature",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_p5_direct_exact_signature",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_primitives.py",
      "id": "check_prime_p5_direct_signature"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_p7_exact_signature",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_p7_direct_exact_signature",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_primitives.py",
      "id": "check_prime_p7_direct_signature"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_p7_uniform_relation_and_uniqueness",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_p7_uniform_structural_relation",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_primitives.py",
      "id": "check_prime_p7_uniform_relation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_restrictions_are_readouts_not_parts",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_restrictions_follow_construction",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_primitives.py",
      "id": "check_prime_restrictions_after_construction"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_two_cycle_boundary_is_conditional",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_two_cycle_boundary",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_primitives.py",
      "id": "check_prime_two_cycle_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_frozen_encoders_do_not_delegate_to_shared_or_peer_helpers",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_relational_encoders_remain_source_independent",
        "timeout": "10"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_encoder_source_independence"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_h3_failure_does_not_deprecate_architecture_dependents",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_relational_failure_propagation_is_scope_bounded",
        "timeout": "10"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_failure_propagation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_h1_all_erased_relations_reconstruct_exactly_in_both_implementations",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_relational_h1_requires_complementary_unique_reconstruction",
        "timeout": "10"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_h1_reconstruction"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_h2_every_whole_view_is_irreducible",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_relational_h2_tests_every_whole_view",
        "timeout": "10"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_h2_irreducibility"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_h3_baseline_preserves_prime_cardinality_architecture",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_relational_baseline_isomorphism_blocks_architecture_transfer",
        "timeout": "10"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_h3_architecture_isomorphism"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_h3_registered_criterion_falsifies_only_software_advantage",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_relational_h3_applies_frozen_software_complexity_criterion",
        "timeout": "10"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_h3_matched_baseline"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_public_identity_does_not_leak_value",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_relational_fixture_identity_excludes_values",
        "timeout": "10"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_identity_nonleakage"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_independent_replay_agrees_with_committed_report",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_relational_replay_avoids_product_import, prime_relational_replay_scopes_registered_falsification",
        "timeout": "10"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_independent_replay"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_complete_cli_run_obeys_registered_resource_bounds",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "prime_relational_complete_run_obeys_registered_resources",
        "requires": "python3, posix_resource, sched_affinity",
        "timeout": "30"
      },
      "file": "tests/test_prime_relational_reconstruction.py",
      "id": "check_prime_relational_registered_resource_bounds"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_is_deterministic_and_nonselecting",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_replay_data_is_receipt_witnessed",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_replay_phase_milnor_receipt.py",
      "id": "check_prime_replay_data_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_independent_decimal_replay_is_pinned",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_replay_receipt_preserves_independent_interval_result",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_replay_phase_milnor_receipt.py",
      "id": "check_prime_replay_receipt_interval"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_all_five_length_three_values_are_zero",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_replay_receipt_freezes_p7_milnor_values",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_replay_phase_milnor_receipt.py",
      "id": "check_prime_replay_receipt_milnor"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_is_deterministic_and_nonselecting",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_replay_receipt_is_nonselecting",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_replay_phase_milnor_receipt.py",
      "id": "check_prime_replay_receipt_nonselecting"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_phase_winding_is_shared_not_prime_specific",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_replay_receipt_exposes_phase_imposition",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_prime_replay_phase_milnor_receipt.py",
      "id": "check_prime_replay_receipt_phase"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_complete_parameter_tori_certify_nine_hundredths_centerline_margin",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_smooth_ribbons_have_global_centerline_margin",
        "requires": "python3",
        "timeout": "20"
      },
      "file": "tests/test_prime_smooth_ribbons.py",
      "id": "check_prime_smooth_ribbons_centerline_margin"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_flat_step_fields_are_c_infinity_bounded_and_event_preserving",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_smooth_ribbons_preserve_all_event_lanes",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_smooth_ribbons.py",
      "id": "check_prime_smooth_ribbons_event_lanes"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_triangle_inequality_certifies_seven_hundredths_ribbon_margin",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_smooth_ribbons_are_globally_disjoint_at_declared_width",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_smooth_ribbons.py",
      "id": "check_prime_smooth_ribbons_finite_width_disjointness"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_complete_pairwise_linking_matrices_have_expected_invariants",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_smooth_ribbons_issue_complete_linking_matrix",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_smooth_ribbons.py",
      "id": "check_prime_smooth_ribbons_linking_matrix"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_smoothed_surfaces_obey_one_turn_reversal_and_two_turn_return",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_smooth_ribbons_obey_mobius_return",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_smooth_ribbons.py",
      "id": "check_prime_smooth_ribbons_mobius_return"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_family_receipt_preserves_p7_first_p5_second_order",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_smooth_ribbons_p7_precedes_p5",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_smooth_ribbons.py",
      "id": "check_prime_smooth_ribbons_p7_first"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_and_smooth_meshes_are_deterministic_and_firewalled",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "prime_smooth_ribbons_receipt_is_nonselecting",
        "requires": "python3",
        "timeout": "30"
      },
      "file": "tests/test_prime_smooth_ribbons.py",
      "id": "check_prime_smooth_ribbons_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_tangent_pairs_receive_clearance_preserving_zero_link_regularizations",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_smooth_ribbons_regularize_tangent_pairs",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_prime_smooth_ribbons.py",
      "id": "check_prime_smooth_ribbons_tangent_regularization"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_symbolic_specializations_replay_frozen_character_ranks",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_symbolic_certificate_replays_finite_characters",
        "requires": "python3, sympy",
        "timeout": "180"
      },
      "file": "tests/test_prime_symbolic_alexander.py",
      "id": "check_prime_symbolic_character_replay"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_exact_ranks_and_first_nonzero_elementary_ideals_differ",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_symbolic_elementary_boundary_is_exact",
        "requires": "python3, sympy",
        "timeout": "180"
      },
      "file": "tests/test_prime_symbolic_alexander.py",
      "id": "check_prime_symbolic_elementary_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_symbolic_presentations_are_sparse_exact_and_deterministic",
        "cleanup": "none",
        "mutates": "none",
        "proves": "prime_symbolic_fox_presentation_is_exact",
        "requires": "python3, sympy",
        "timeout": "180"
      },
      "file": "tests/test_prime_symbolic_alexander.py",
      "id": "check_prime_symbolic_fox_exact"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_family_receipt_is_deterministic_and_bounded",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "prime_symbolic_alexander_receipt_is_nonselecting",
        "requires": "python3, sympy",
        "timeout": "360"
      },
      "file": "tests/test_prime_symbolic_alexander.py",
      "id": "check_prime_symbolic_receipt_nonselecting"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_algebraic_zero_remains_positive_retained_structure",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ordered_occurrence_profile_preserves_declared_choices",
        "timeout": "10"
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
        "proves": "profile_does_not_restore_archived_arithmetic",
        "timeout": "10"
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
        "proves": "post_reset_bridge_is_exact_and_fail_closed",
        "timeout": "10"
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
        "proves": "post_reset_bridge_is_exact_and_fail_closed",
        "timeout": "10"
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
        "proves": "post_reset_bridge_is_exact_and_fail_closed, bridge_identity_binds_order_profile_and_content",
        "timeout": "10"
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
        "proves": "ordered_occurrence_profile_preserves_declared_choices",
        "timeout": "10"
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
        "proves": "ordered_occurrence_profile_preserves_declared_choices",
        "timeout": "10"
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
        "proves": "ordered_occurrence_profile_preserves_declared_choices",
        "timeout": "10"
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
        "proves": "profile_does_not_restore_archived_arithmetic",
        "timeout": "10"
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
        "proves": "bridge_identity_binds_order_profile_and_content",
        "timeout": "10"
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
        "proves": "ordered_occurrence_profile_preserves_declared_choices",
        "timeout": "10"
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
        "proves": "bridge_identity_binds_order_profile_and_content, profile_binding_is_fail_closed",
        "timeout": "10"
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
        "proves": "profile_binding_is_fail_closed",
        "timeout": "10"
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
        "proves": "ordered_occurrence_profile_preserves_declared_choices",
        "timeout": "10"
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
        "proves": "ordered_occurrence_profile_preserves_declared_choices",
        "timeout": "10"
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
        "proves": "validity_transfer_is_forbidden",
        "timeout": "10"
      },
      "file": "tests/test_profile_boundary.py",
      "id": "check_validity_transfer_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_is_byte_deterministic_and_provenance_bound",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ucns_ptcna_receipt_is_deterministic_and_provenance_bound",
        "timeout": "10"
      },
      "file": "tests/test_ptcna_state.py",
      "id": "check_ucns_ptcna_deterministic_receipt"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_has_exact_dense_shape_and_state_digest",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ucns_ptcna_state_has_exact_requested_shape",
        "timeout": "10"
      },
      "file": "tests/test_ptcna_state.py",
      "id": "check_ucns_ptcna_exact_shape"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_preserves_candidate_and_nonclaim_boundaries",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ucns_ptcna_candidate_transfers_no_status",
        "timeout": "10"
      },
      "file": "tests/test_ptcna_state.py",
      "id": "check_ucns_ptcna_status_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_every_tested_authority_tamper_is_rejected",
        "cleanup": "none",
        "mutates": "none",
        "proves": "ucns_ptcna_receipt_rejects_tampering",
        "timeout": "10"
      },
      "file": "tests/test_ptcna_state.py",
      "id": "check_ucns_ptcna_tamper_rejection"
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
        "call": "self::test_relational_carrier_exact_boundary",
        "cleanup": "none",
        "mutates": "none",
        "proves": "relational_carrier_is_intrinsic_and_metadata_free, relational_carrier_preserves_order_multiplicity_and_sidedness, relational_carrier_roundtrip_is_canonical",
        "timeout": "30"
      },
      "file": "tests/test_relational_carrier.py",
      "id": "relational_carrier_exact_boundary_check"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_all_fourteen_initiations_round_trip_without_evidence_loss",
        "cleanup": "none",
        "mutates": "none",
        "proves": "root_loop_chart_preserves_every_source_linked_initiation",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_root_loop_chart.py",
      "id": "check_root_loop_chart_all_initiations"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_v07_report_supports_f12_only_on_bounded_domain_without_selection",
        "cleanup": "none",
        "mutates": "none",
        "proves": "root_loop_chart_support_is_bounded_and_nonselecting",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_root_loop_chart.py",
      "id": "check_root_loop_chart_bounded_verdict"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_chart_commutes_with_initiation_360_720_and_inverse",
        "cleanup": "none",
        "mutates": "none",
        "proves": "root_loop_chart_commutes_with_bounded_motion",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_root_loop_chart.py",
      "id": "check_root_loop_chart_commutation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_sheet_correspondence_materializes_on_existing_cover_without_mutation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "root_loop_chart_uses_cover_sheet_as_hypothesis_not_native_orientation",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_root_loop_chart.py",
      "id": "check_root_loop_chart_sheet_hypothesis"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_chart_maps_are_exact_inverses_for_rational_root_loop_states",
        "cleanup": "none",
        "mutates": "none",
        "proves": "root_loop_chart_maps_are_exact_two_way_inverses",
        "requires": "python3",
        "timeout": "5"
      },
      "file": "tests/test_root_loop_chart.py",
      "id": "check_root_loop_chart_two_way_inverse"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_audit_gap_prevents_execution",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "boundary_runner_audits_before_execution",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_skill_lib_boundary_runner.py",
      "id": "check_boundary_runner_audit_gate"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_missing_capability_and_timeout_are_enforced",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "boundary_runner_consumes_capabilities_and_timeouts",
        "requires": "python3",
        "timeout": "15"
      },
      "file": "tests/test_skill_lib_boundary_runner.py",
      "id": "check_boundary_runner_capability_timeout_consumption"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_passing_receipt_has_no_activation_or_selection_effect",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "boundary_runner_has_no_activation_effect",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_skill_lib_boundary_runner.py",
      "id": "check_boundary_runner_nonactivation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_receipt_binds_declarations_outputs_and_identity",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "boundary_runner_receipt_is_bounded_and_bound",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_skill_lib_boundary_runner.py",
      "id": "check_boundary_runner_receipt_binding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_runner_classifies_all_outcomes_and_continues",
        "cleanup": "pytest temporary_path",
        "mutates": "temporary_path",
        "proves": "boundary_runner_classifies_and_continues",
        "requires": "python3",
        "timeout": "20"
      },
      "file": "tests/test_skill_lib_boundary_runner.py",
      "id": "check_boundary_runner_status_continuation"
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
        "call": "self::test_ordered_source_coordinate_uses_exact_complete_address",
        "cleanup": "none",
        "mutates": "none",
        "proves": "source_coordinate_law_uses_complete_ordered_source_address",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_source_coordinate.py",
      "id": "check_source_coordinate_complete_ordered_address"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_source_coordinate_assignment_is_exact_and_reversible",
        "cleanup": "none",
        "mutates": "none",
        "proves": "source_coordinate_assignment_applies_exact_candidate_reversibly",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_source_coordinate.py",
      "id": "check_source_coordinate_exact_assignment"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_equal_content_is_separate_and_report_remains_nonselecting",
        "cleanup": "none",
        "mutates": "none",
        "proves": "source_coordinate_law_rejects_identity_shortcuts_and_nonselection",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_source_coordinate.py",
      "id": "check_source_coordinate_negative_and_nonselection"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_prefix_cannot_reuse_or_impersonate_complete_scope_binding",
        "cleanup": "none",
        "mutates": "none",
        "proves": "source_coordinate_law_uses_complete_ordered_source_address",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_source_coordinate.py",
      "id": "check_source_coordinate_prefix_requires_completion_binding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_ordered_source_coordinate_is_exact_and_scope_injective",
        "cleanup": "none",
        "mutates": "none",
        "proves": "source_coordinate_law_is_exact_and_scope_injective",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_source_coordinate.py",
      "id": "check_source_coordinate_scope_injectivity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_trace_retains_total_ordered_outcomes_and_blockers",
        "cleanup": "none",
        "mutates": "none",
        "proves": "source_coordinate_outcomes_are_total_exclusive_and_ordered",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_source_coordinate.py",
      "id": "check_source_coordinate_total_outcomes"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_derivation_retains_exact_upstream_identity",
        "cleanup": "none",
        "mutates": "none",
        "proves": "source_coordinate_derivation_retains_exact_initiation_identity",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_source_coordinate.py",
      "id": "check_source_coordinate_upstream_identity"
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
        "call": "self::test_local_and_global_descriptions_remain_reversible",
        "cleanup": "none",
        "mutates": "none",
        "proves": "transverse_envelope_maps_preserve_exact_rational_state",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_transverse_envelope.py",
      "id": "check_transverse_envelope_convention_round_trip"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_distinct_transverse_values_collide_in_the_actual_cover",
        "cleanup": "none",
        "mutates": "none",
        "proves": "transverse_envelope_exposes_cover_nonembedding",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_transverse_envelope.py",
      "id": "check_transverse_envelope_cover_collision"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_parametric_exact_rational_maps_and_motion",
        "cleanup": "none",
        "mutates": "none",
        "proves": "transverse_envelope_maps_preserve_exact_rational_state",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_transverse_envelope.py",
      "id": "check_transverse_envelope_exact_round_trip"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_every_witness_retains_the_pinned_exact_policy",
        "cleanup": "none",
        "mutates": "none",
        "proves": "transverse_envelope_comparison_policy_is_explicit",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_transverse_envelope.py",
      "id": "check_transverse_envelope_explicit_policy"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_zero_sidecar_restricts_exactly_to_v07",
        "cleanup": "none",
        "mutates": "none",
        "proves": "transverse_envelope_restricts_exactly_to_v07_root_loop",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_transverse_envelope.py",
      "id": "check_transverse_envelope_root_restriction"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_v09_report_keeps_transverse_cover_extension_inconclusive",
        "cleanup": "none",
        "mutates": "none",
        "proves": "transverse_envelope_does_not_extend_cover_verdicts",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_transverse_envelope.py",
      "id": "check_transverse_envelope_verdict_boundary"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_report_rejects_count_preserving_identity_substitution",
        "cleanup": "none",
        "mutates": "none",
        "proves": "transverse_envelope_report_validates_complete_witness_identities",
        "requires": "python3",
        "timeout": "10"
      },
      "file": "tests/test_transverse_envelope.py",
      "id": "check_transverse_envelope_witness_identities"
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
        "given": "the independent architecture replay runs",
        "since": "2026-08-16",
        "then": "it derives H1 candidate sets, H2 dimensions, and H3 comparison from frozen JSON using only the Python standard library"
      },
      "file": "tools/replay_prime_relational_reconstruction.py",
      "id": "prime_relational_replay_avoids_product_import"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the committed aggregate report is replayed",
        "since": "2026-08-17",
        "then": "H1/H2 counts, registered H3 falsification, baseline structural isomorphism, unresolved architectural status, and blocked propagation must all agree or replay fails closed"
      },
      "file": "tools/replay_prime_relational_reconstruction.py",
      "id": "prime_relational_replay_scopes_registered_falsification"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "canonical JSON loading, checksum enumeration, dimension audit, matched-baseline tuple comparison, structural-isomorphism audit",
        "module_kind": "instrument",
        "module_name": "replay_prime_relational_reconstruction",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "replay, command-line interface",
        "requires": "ucns_prime_relational_reconstruction_adversary",
        "rollback": "revert the interpretation audit without changing frozen preregistration or historical execution commits",
        "rollout": "evidence replay and interpretation audit only; no candidate execution, canon, or activation effect",
        "since": "2026-08-16",
        "storage_boundary": "read",
        "summary": "independently replays frozen H1/H2/H3 arithmetic and verifies that the registered baseline is structurally isomorphic before accepting propagation status",
        "tests": "tests/test_prime_relational_reconstruction.py",
        "unresolved": "genuinely non-prime-cardinality matched control, independent external implementation, and producer authentication",
        "user_data_boundary": "hand-authored development fixture and aggregate evidence only"
      },
      "file": "tools/replay_prime_relational_reconstruction.py",
      "id": "prime_relational_reconstruction_independent_replay"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "declared skill-lib checks are requested for execution",
        "since": "2026-08-15",
        "then": "the no-exec contract graph audit must close before any check process starts"
      },
      "file": "tools/run_skill_lib_boundaries.py",
      "id": "boundary_runner_audits_before_execution"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "one declared check passes, fails an assertion, raises unexpectedly, or times out",
        "since": "2026-08-15",
        "then": "the runner records PASS, FAIL, ERROR, or TIMEOUT respectively and continues with remaining selected checks"
      },
      "file": "tools/run_skill_lib_boundaries.py",
      "id": "boundary_runner_classifies_and_continues"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a CHECKS declaration names requires and timeout fields",
        "since": "2026-08-15",
        "then": "execution refuses missing capabilities and applies the positive timeout to the spawned pytest process group"
      },
      "file": "tools/run_skill_lib_boundaries.py",
      "id": "boundary_runner_consumes_capabilities_and_timeouts"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "every selected check passes",
        "since": "2026-08-15",
        "then": "the receipt closes only the declared executable evidence boundary and cannot select UCNS options, activate EDCM, or confer canon status"
      },
      "file": "tools/run_skill_lib_boundaries.py",
      "id": "boundary_runner_has_no_activation_effect"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a boundary run completes",
        "since": "2026-08-15",
        "then": "its receipt binds declarations, commands, capabilities, outcomes, output digests, declared mutation and cleanup, bounded output excerpts, and an identity digest"
      },
      "file": "tools/run_skill_lib_boundaries.py",
      "id": "boundary_runner_receipt_is_bounded_and_bound"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "capability resolution, subprocess classification, receipt hashing",
        "module_kind": "instrument",
        "module_name": "run_skill_lib_boundaries",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "command-line boundary runner, run_boundaries, write_receipt",
        "requires": "skill_lib_contract_audit",
        "rollback": "remove this tool, its tests, and documentation",
        "rollout": "explicit local and CI evidence runner; no product, EDCM, or canon activation",
        "since": "2026-08-15",
        "storage_boundary": "optional caller-selected JSON receipt path",
        "summary": "audits and executes declared skill-lib CHECKS as isolated pytest boundaries with capability, timeout, and receipt enforcement",
        "tests": "tests/test_skill_lib_boundary_runner.py",
        "unresolved": "mutation verification and non-pytest CHECKS call schemes",
        "user_data_boundary": "captured test output is bounded and retained only in the caller-selected receipt"
      },
      "file": "tools/run_skill_lib_boundaries.py",
      "id": "skill_lib_boundary_runner"
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
      "from": "check_assignment_admission_explicit_adapter",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_assignment_admission_explicit_adapter",
      "to": "self::test_admission_requires_adapter_and_keeps_digest_out_of_geometry"
    },
    {
      "from": "check_assignment_admission_explicit_adapter",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_assignment_admission_explicit_adapter",
      "to": "assignment_admission_requires_explicit_domain_adapter"
    },
    {
      "from": "check_assignment_admission_explicit_adapter",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_assignment_admission_explicit_adapter",
      "to": "python3"
    },
    {
      "from": "check_assignment_admission_occurrence_preservation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_assignment_admission_occurrence_preservation",
      "to": "self::test_trace_preserves_equal_content_as_distinct_ordered_occurrences"
    },
    {
      "from": "check_assignment_admission_occurrence_preservation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_assignment_admission_occurrence_preservation",
      "to": "assignment_admission_preserves_occurrence_order_and_multiplicity"
    },
    {
      "from": "check_assignment_admission_occurrence_preservation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_assignment_admission_occurrence_preservation",
      "to": "python3"
    },
    {
      "from": "check_assignment_boundary_nonactivation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_assignment_boundary_nonactivation",
      "to": "self::test_v016_report_retains_upstream_and_unresolved_geometry"
    },
    {
      "from": "check_assignment_boundary_nonactivation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_assignment_boundary_nonactivation",
      "to": "assignment_boundary_does_not_complete_initiation_or_activate"
    },
    {
      "from": "check_assignment_boundary_nonactivation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_assignment_boundary_nonactivation",
      "to": "python3"
    },
    {
      "from": "check_assignment_identity_mechanism_rejection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_assignment_identity_mechanism_rejection",
      "to": "self::test_identity_derived_mechanisms_are_rejected_without_geometry"
    },
    {
      "from": "check_assignment_identity_mechanism_rejection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_assignment_identity_mechanism_rejection",
      "to": "assignment_identity_mechanisms_cannot_derive_geometry"
    },
    {
      "from": "check_assignment_identity_mechanism_rejection",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_assignment_identity_mechanism_rejection",
      "to": "python3"
    },
    {
      "from": "check_assignment_outcome_partition",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_assignment_outcome_partition",
      "to": "self::test_outcome_partition_is_total_exclusive_and_fail_closed"
    },
    {
      "from": "check_assignment_outcome_partition",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_assignment_outcome_partition",
      "to": "assignment_outcome_is_total_and_exclusive_over_admitted_evidence"
    },
    {
      "from": "check_assignment_outcome_partition",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_assignment_outcome_partition",
      "to": "python3"
    },
    {
      "from": "check_assignment_supplied_candidate_evidence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_assignment_supplied_candidate_evidence",
      "to": "self::test_supplied_candidate_is_retained_without_derivation_or_selection"
    },
    {
      "from": "check_assignment_supplied_candidate_evidence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_assignment_supplied_candidate_evidence",
      "to": "supplied_assignment_remains_candidate_evidence"
    },
    {
      "from": "check_assignment_supplied_candidate_evidence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_assignment_supplied_candidate_evidence",
      "to": "python3"
    },
    {
      "from": "check_boundary_runner_audit_gate",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_audit_gate",
      "to": "self::test_audit_gap_prevents_execution"
    },
    {
      "from": "check_boundary_runner_audit_gate",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_audit_gate",
      "to": "boundary_runner_audits_before_execution"
    },
    {
      "from": "check_boundary_runner_audit_gate",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_audit_gate",
      "to": "python3"
    },
    {
      "from": "check_boundary_runner_capability_timeout_consumption",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_capability_timeout_consumption",
      "to": "self::test_missing_capability_and_timeout_are_enforced"
    },
    {
      "from": "check_boundary_runner_capability_timeout_consumption",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_capability_timeout_consumption",
      "to": "boundary_runner_consumes_capabilities_and_timeouts"
    },
    {
      "from": "check_boundary_runner_capability_timeout_consumption",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_capability_timeout_consumption",
      "to": "python3"
    },
    {
      "from": "check_boundary_runner_nonactivation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_nonactivation",
      "to": "self::test_passing_receipt_has_no_activation_or_selection_effect"
    },
    {
      "from": "check_boundary_runner_nonactivation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_nonactivation",
      "to": "boundary_runner_has_no_activation_effect"
    },
    {
      "from": "check_boundary_runner_nonactivation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_nonactivation",
      "to": "python3"
    },
    {
      "from": "check_boundary_runner_receipt_binding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_receipt_binding",
      "to": "self::test_receipt_binds_declarations_outputs_and_identity"
    },
    {
      "from": "check_boundary_runner_receipt_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_receipt_binding",
      "to": "boundary_runner_receipt_is_bounded_and_bound"
    },
    {
      "from": "check_boundary_runner_receipt_binding",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_receipt_binding",
      "to": "python3"
    },
    {
      "from": "check_boundary_runner_status_continuation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_status_continuation",
      "to": "self::test_runner_classifies_all_outcomes_and_continues"
    },
    {
      "from": "check_boundary_runner_status_continuation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_status_continuation",
      "to": "boundary_runner_classifies_and_continues"
    },
    {
      "from": "check_boundary_runner_status_continuation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_boundary_runner_status_continuation",
      "to": "python3"
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
      "from": "check_carrier_coordinate_actual_cover_fields",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_actual_cover_fields",
      "to": "self::test_candidate_image_materializes_declared_breadth_and_root_angle"
    },
    {
      "from": "check_carrier_coordinate_actual_cover_fields",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_actual_cover_fields",
      "to": "carrier_coordinate_uses_actual_cover_fields"
    },
    {
      "from": "check_carrier_coordinate_actual_cover_fields",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_actual_cover_fields",
      "to": "python3"
    },
    {
      "from": "check_carrier_coordinate_constructive_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_constructive_boundary",
      "to": "self::test_signed_local_candidate_is_bounded_admissible_without_selection"
    },
    {
      "from": "check_carrier_coordinate_constructive_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_constructive_boundary",
      "to": "carrier_coordinate_constructive_result_does_not_select"
    },
    {
      "from": "check_carrier_coordinate_constructive_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_constructive_boundary",
      "to": "python3"
    },
    {
      "from": "check_carrier_coordinate_failure_retention",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_failure_retention",
      "to": "self::test_rejected_candidates_retain_exact_collision_and_motion_witnesses"
    },
    {
      "from": "check_carrier_coordinate_failure_retention",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_failure_retention",
      "to": "carrier_coordinate_admissibility_retains_failures"
    },
    {
      "from": "check_carrier_coordinate_failure_retention",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_failure_retention",
      "to": "python3"
    },
    {
      "from": "check_carrier_coordinate_family_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_family_identity",
      "to": "self::test_candidate_family_is_explicit_ordered_and_nonselecting"
    },
    {
      "from": "check_carrier_coordinate_family_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_family_identity",
      "to": "carrier_coordinate_family_is_explicit_and_nonselecting"
    },
    {
      "from": "check_carrier_coordinate_family_identity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_family_identity",
      "to": "python3"
    },
    {
      "from": "check_carrier_coordinate_root_restriction",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_root_restriction",
      "to": "self::test_every_candidate_zero_fiber_is_the_v07_actual_root"
    },
    {
      "from": "check_carrier_coordinate_root_restriction",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_root_restriction",
      "to": "carrier_coordinate_zero_fiber_restricts_to_v07"
    },
    {
      "from": "check_carrier_coordinate_root_restriction",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_root_restriction",
      "to": "python3"
    },
    {
      "from": "check_carrier_coordinate_witness_identities",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_witness_identities",
      "to": "self::test_report_rejects_count_preserving_identity_substitution"
    },
    {
      "from": "check_carrier_coordinate_witness_identities",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_witness_identities",
      "to": "carrier_coordinate_report_validates_complete_witness_identities"
    },
    {
      "from": "check_carrier_coordinate_witness_identities",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_carrier_coordinate_witness_identities",
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
      "from": "check_edcm_multiwoz_v0141_handoff",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_edcm_multiwoz_v0141_handoff",
      "to": "self::test_external_edcm_receipt_handoff_is_exact_and_nonpromoting"
    },
    {
      "from": "check_edcm_multiwoz_v0141_handoff",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_edcm_multiwoz_v0141_handoff",
      "to": "external_multiwoz_v0141_handoff_is_exact_and_nonpromoting"
    },
    {
      "from": "check_edcm_multiwoz_v0141_handoff",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_edcm_multiwoz_v0141_handoff",
      "to": "python3"
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
      "from": "check_exact_coordinate_binary64_breadth_collision",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_breadth_collision",
      "to": "self::test_binary64_breadth_collision_retains_exact_distinction"
    },
    {
      "from": "check_exact_coordinate_binary64_breadth_collision",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_breadth_collision",
      "to": "exact_coordinate_binary64_breadth_collision_is_retained"
    },
    {
      "from": "check_exact_coordinate_binary64_breadth_collision",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_breadth_collision",
      "to": "python3"
    },
    {
      "from": "check_exact_coordinate_binary64_rendering_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_rendering_boundary",
      "to": "self::test_binary64_point_is_linked_lossy_rendering_only"
    },
    {
      "from": "check_exact_coordinate_binary64_rendering_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_rendering_boundary",
      "to": "exact_coordinate_binary64_is_declared_rendering"
    },
    {
      "from": "check_exact_coordinate_binary64_rendering_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_rendering_boundary",
      "to": "python3"
    },
    {
      "from": "check_exact_coordinate_binary64_turn_collision",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_turn_collision",
      "to": "self::test_binary64_turn_collision_retains_exact_distinction"
    },
    {
      "from": "check_exact_coordinate_binary64_turn_collision",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_turn_collision",
      "to": "exact_coordinate_binary64_turn_collision_is_retained"
    },
    {
      "from": "check_exact_coordinate_binary64_turn_collision",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_binary64_turn_collision",
      "to": "python3"
    },
    {
      "from": "check_exact_coordinate_fixed_provenance",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_fixed_provenance",
      "to": "self::test_exact_coordinate_retains_fixed_provenance_and_fails_closed"
    },
    {
      "from": "check_exact_coordinate_fixed_provenance",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_fixed_provenance",
      "to": "exact_coordinate_provenance_is_fixed_and_retained"
    },
    {
      "from": "check_exact_coordinate_fixed_provenance",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_fixed_provenance",
      "to": "python3"
    },
    {
      "from": "check_exact_coordinate_nonselection_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_nonselection_boundary",
      "to": "self::test_v011_report_keeps_selection_and_activation_absent"
    },
    {
      "from": "check_exact_coordinate_nonselection_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_nonselection_boundary",
      "to": "exact_coordinate_boundary_does_not_select_or_activate"
    },
    {
      "from": "check_exact_coordinate_nonselection_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_nonselection_boundary",
      "to": "python3"
    },
    {
      "from": "check_exact_coordinate_signed_local_round_trip",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_signed_local_round_trip",
      "to": "self::test_signed_local_exact_law_round_trips_rational_domain"
    },
    {
      "from": "check_exact_coordinate_signed_local_round_trip",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_signed_local_round_trip",
      "to": "exact_coordinate_signed_local_law_round_trips"
    },
    {
      "from": "check_exact_coordinate_signed_local_round_trip",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_exact_coordinate_signed_local_round_trip",
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
      "from": "check_explicit_geometry_exact_candidate_application",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_exact_candidate_application",
      "to": "self::test_assignment_applies_exact_signed_local_candidate_reversibly"
    },
    {
      "from": "check_explicit_geometry_exact_candidate_application",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_exact_candidate_application",
      "to": "explicit_geometry_applies_exact_signed_local_candidate_reversibly"
    },
    {
      "from": "check_explicit_geometry_exact_candidate_application",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_exact_candidate_application",
      "to": "python3"
    },
    {
      "from": "check_explicit_geometry_frame_side_and_rendering",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_frame_side_and_rendering",
      "to": "self::test_assignment_preserves_frame_side_and_rendering_boundary"
    },
    {
      "from": "check_explicit_geometry_frame_side_and_rendering",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_frame_side_and_rendering",
      "to": "explicit_geometry_preserves_mobius_frame_and_local_side"
    },
    {
      "from": "check_explicit_geometry_frame_side_and_rendering",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_frame_side_and_rendering",
      "to": "python3"
    },
    {
      "from": "check_explicit_geometry_independent_exact_input",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_independent_exact_input",
      "to": "self::test_proposal_requires_initiated_word_and_independent_exact_input"
    },
    {
      "from": "check_explicit_geometry_independent_exact_input",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_independent_exact_input",
      "to": "explicit_geometry_requires_initiated_word_and_independent_exact_input"
    },
    {
      "from": "check_explicit_geometry_independent_exact_input",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_independent_exact_input",
      "to": "python3"
    },
    {
      "from": "check_explicit_geometry_nonactivation_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_nonactivation_boundary",
      "to": "self::test_v018_report_retains_unresolved_law_and_nonactivation"
    },
    {
      "from": "check_explicit_geometry_nonactivation_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_nonactivation_boundary",
      "to": "explicit_geometry_does_not_claim_total_law_complete_select_or_activate"
    },
    {
      "from": "check_explicit_geometry_nonactivation_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_nonactivation_boundary",
      "to": "python3"
    },
    {
      "from": "check_explicit_geometry_rejected_mechanisms",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_rejected_mechanisms",
      "to": "self::test_rejected_mechanisms_never_create_an_applied_assignment"
    },
    {
      "from": "check_explicit_geometry_rejected_mechanisms",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_rejected_mechanisms",
      "to": "explicit_geometry_rejects_identity_projection_and_upstream_substitution"
    },
    {
      "from": "check_explicit_geometry_rejected_mechanisms",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_rejected_mechanisms",
      "to": "python3"
    },
    {
      "from": "check_explicit_geometry_total_outcomes",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_total_outcomes",
      "to": "self::test_trace_is_total_exclusive_ordered_and_occurrence_preserving"
    },
    {
      "from": "check_explicit_geometry_total_outcomes",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_total_outcomes",
      "to": "explicit_geometry_outcomes_are_total_exclusive_and_ordered"
    },
    {
      "from": "check_explicit_geometry_total_outcomes",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_explicit_geometry_total_outcomes",
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
      "from": "check_external_evaluation_corpus_gate",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_corpus_gate",
      "to": "self::test_plan_requires_execution_generated_completion_receipt"
    },
    {
      "from": "check_external_evaluation_corpus_gate",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_corpus_gate",
      "to": "external_evaluation_requires_completed_corpus_gate"
    },
    {
      "from": "check_external_evaluation_corpus_gate",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_corpus_gate",
      "to": "python3"
    },
    {
      "from": "check_external_evaluation_nonpromotion",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_nonpromotion",
      "to": "self::test_complete_external_receipt_is_candidate_evidence_only"
    },
    {
      "from": "check_external_evaluation_nonpromotion",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_nonpromotion",
      "to": "external_evaluation_receipt_is_nonpromoting"
    },
    {
      "from": "check_external_evaluation_nonpromotion",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_nonpromotion",
      "to": "python3"
    },
    {
      "from": "check_external_evaluation_resource_bounds",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_resource_bounds",
      "to": "self::test_timeout_input_output_and_executable_bounds_fail_closed"
    },
    {
      "from": "check_external_evaluation_resource_bounds",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_resource_bounds",
      "to": "external_evaluation_is_resource_bounded"
    },
    {
      "from": "check_external_evaluation_resource_bounds",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluation_resource_bounds",
      "to": "python3"
    },
    {
      "from": "check_external_evaluator_identity_disclosure_binding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluator_identity_disclosure_binding",
      "to": "self::test_request_binds_identity_command_cases_and_disclosure"
    },
    {
      "from": "check_external_evaluator_identity_disclosure_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluator_identity_disclosure_binding",
      "to": "external_evaluator_identity_and_disclosure_are_bound"
    },
    {
      "from": "check_external_evaluator_identity_disclosure_binding",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_external_evaluator_identity_disclosure_binding",
      "to": "python3"
    },
    {
      "from": "check_external_response_reconciliation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_external_response_reconciliation",
      "to": "self::test_response_requires_exact_protocol_and_ordered_case_coverage"
    },
    {
      "from": "check_external_response_reconciliation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_external_response_reconciliation",
      "to": "external_response_reconciliation_is_fail_closed"
    },
    {
      "from": "check_external_response_reconciliation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_external_response_reconciliation",
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
      "from": "check_full_carrier_affine_certificate",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_affine_certificate",
      "to": "self::test_affine_certificate_retains_exact_universal_proof_data"
    },
    {
      "from": "check_full_carrier_affine_certificate",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_affine_certificate",
      "to": "full_carrier_affine_certificate_is_universal_and_exact"
    },
    {
      "from": "check_full_carrier_affine_certificate",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_affine_certificate",
      "to": "python3"
    },
    {
      "from": "check_full_carrier_mixed_scope_report",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_mixed_scope_report",
      "to": "self::test_report_retains_analytic_and_bounded_executable_scopes"
    },
    {
      "from": "check_full_carrier_mixed_scope_report",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_mixed_scope_report",
      "to": "full_carrier_attachment_retains_mixed_evidence_scopes"
    },
    {
      "from": "check_full_carrier_mixed_scope_report",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_mixed_scope_report",
      "to": "python3"
    },
    {
      "from": "check_full_carrier_nonactivation_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_nonactivation_boundary",
      "to": "self::test_report_rejects_scope_completion_selection_and_activation"
    },
    {
      "from": "check_full_carrier_nonactivation_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_nonactivation_boundary",
      "to": "full_carrier_attachment_does_not_complete_select_or_activate"
    },
    {
      "from": "check_full_carrier_nonactivation_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_nonactivation_boundary",
      "to": "python3"
    },
    {
      "from": "check_full_carrier_quotient_certificate",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_quotient_certificate",
      "to": "self::test_quotient_certificate_commutes_and_excludes_structural_null"
    },
    {
      "from": "check_full_carrier_quotient_certificate",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_quotient_certificate",
      "to": "full_carrier_quotient_certificate_commutes_without_moving_the_marked_seam"
    },
    {
      "from": "check_full_carrier_quotient_certificate",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_full_carrier_quotient_certificate",
      "to": "python3"
    },
    {
      "from": "check_full_corpus_exact_reconstruction",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_exact_reconstruction",
      "to": "self::test_exact_stream_digest_is_stable_across_equivalent_iterables"
    },
    {
      "from": "check_full_corpus_exact_reconstruction",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_exact_reconstruction",
      "to": "full_corpus_gate_requires_exact_stream_reconstruction"
    },
    {
      "from": "check_full_corpus_exact_reconstruction",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_exact_reconstruction",
      "to": "python3"
    },
    {
      "from": "check_full_corpus_exhaustion_and_count_gate",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_exhaustion_and_count_gate",
      "to": "self::test_complete_run_exhausts_every_turn_and_matches_expected_count"
    },
    {
      "from": "check_full_corpus_exhaustion_and_count_gate",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_exhaustion_and_count_gate",
      "to": "full_corpus_gate_requires_exhaustion_and_turn_count"
    },
    {
      "from": "check_full_corpus_exhaustion_and_count_gate",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_exhaustion_and_count_gate",
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
      "from": "check_full_corpus_manifest_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_manifest_identity",
      "to": "self::test_manifest_pins_source_adapter_and_admission_boundary"
    },
    {
      "from": "check_full_corpus_manifest_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_manifest_identity",
      "to": "full_corpus_manifest_pins_admission_identity"
    },
    {
      "from": "check_full_corpus_manifest_identity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_manifest_identity",
      "to": "python3"
    },
    {
      "from": "check_full_corpus_receipt_nonactivation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_receipt_nonactivation",
      "to": "self::test_completion_receipt_opens_analysis_only"
    },
    {
      "from": "check_full_corpus_receipt_nonactivation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_receipt_nonactivation",
      "to": "full_corpus_receipt_has_no_selection_or_activation_effect"
    },
    {
      "from": "check_full_corpus_receipt_nonactivation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_full_corpus_receipt_nonactivation",
      "to": "python3"
    },
    {
      "from": "check_gonol_initiation_explicit_transition",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_explicit_transition",
      "to": "self::test_word_gonol_requires_one_source_bound_structural_null_twist"
    },
    {
      "from": "check_gonol_initiation_explicit_transition",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_explicit_transition",
      "to": "gonol_initiation_requires_explicit_structural_null_transition"
    },
    {
      "from": "check_gonol_initiation_explicit_transition",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_explicit_transition",
      "to": "python3"
    },
    {
      "from": "check_gonol_initiation_nonactivation_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_nonactivation_boundary",
      "to": "self::test_v017_report_retains_unresolved_geometry_and_nonactivation"
    },
    {
      "from": "check_gonol_initiation_nonactivation_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_nonactivation_boundary",
      "to": "gonol_initiation_does_not_assign_complete_select_or_activate"
    },
    {
      "from": "check_gonol_initiation_nonactivation_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_nonactivation_boundary",
      "to": "python3"
    },
    {
      "from": "check_gonol_initiation_origin_role_separation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_origin_role_separation",
      "to": "self::test_origin_registry_separates_structural_null_from_neighboring_roles"
    },
    {
      "from": "check_gonol_initiation_origin_role_separation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_origin_role_separation",
      "to": "gonol_initiation_origin_roles_are_domain_separated"
    },
    {
      "from": "check_gonol_initiation_origin_role_separation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_origin_role_separation",
      "to": "python3"
    },
    {
      "from": "check_gonol_initiation_rejected_substitutions",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_rejected_substitutions",
      "to": "self::test_neighboring_zero_and_absence_roles_cannot_become_prestate"
    },
    {
      "from": "check_gonol_initiation_rejected_substitutions",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_rejected_substitutions",
      "to": "gonol_initiation_rejects_zero_and_absence_substitutions"
    },
    {
      "from": "check_gonol_initiation_rejected_substitutions",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_rejected_substitutions",
      "to": "python3"
    },
    {
      "from": "check_gonol_initiation_root_return_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_root_return_boundary",
      "to": "self::test_root_return_preserves_360_change_720_return_and_noncompletion"
    },
    {
      "from": "check_gonol_initiation_root_return_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_root_return_boundary",
      "to": "gonol_initiation_root_return_is_bounded_and_noncompleting"
    },
    {
      "from": "check_gonol_initiation_root_return_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_root_return_boundary",
      "to": "python3"
    },
    {
      "from": "check_gonol_initiation_scope_receipt_authority",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_scope_receipt_authority",
      "to": "self::test_scope_completion_receipt_derives_only_from_exact_authority_report"
    },
    {
      "from": "check_gonol_initiation_scope_receipt_authority",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_scope_receipt_authority",
      "to": "gonol_initiation_scope_receipt_is_producer_issued"
    },
    {
      "from": "check_gonol_initiation_scope_receipt_authority",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_scope_receipt_authority",
      "to": "python3"
    },
    {
      "from": "check_gonol_initiation_total_outcome_relation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_total_outcome_relation",
      "to": "self::test_initiation_trace_is_total_exclusive_ordered_and_occurrence_preserving"
    },
    {
      "from": "check_gonol_initiation_total_outcome_relation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_total_outcome_relation",
      "to": "gonol_initiation_outcome_is_total_and_exclusive"
    },
    {
      "from": "check_gonol_initiation_total_outcome_relation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_gonol_initiation_total_outcome_relation",
      "to": "python3"
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
      "from": "check_incomplete_corpus_fail_closed",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_incomplete_corpus_fail_closed",
      "to": "self::test_partial_iteration_and_count_mismatch_cannot_issue_receipts"
    },
    {
      "from": "check_incomplete_corpus_fail_closed",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_incomplete_corpus_fail_closed",
      "to": "incomplete_corpus_run_fails_closed"
    },
    {
      "from": "check_incomplete_corpus_fail_closed",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_incomplete_corpus_fail_closed",
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
      "from": "check_invalid_corpus_turn_fail_closed",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_invalid_corpus_turn_fail_closed",
      "to": "self::test_invalid_turn_records_exact_stopping_boundary"
    },
    {
      "from": "check_invalid_corpus_turn_fail_closed",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_invalid_corpus_turn_fail_closed",
      "to": "incomplete_corpus_run_fails_closed"
    },
    {
      "from": "check_invalid_corpus_turn_fail_closed",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_invalid_corpus_turn_fail_closed",
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
      "from": "check_mobius_seed_braid_order",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_braid_order",
      "to": "self::test_every_structural_pair_reverses_over_under_order"
    },
    {
      "from": "check_mobius_seed_braid_order",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_braid_order",
      "to": "mobius_seed_structural_pairs_have_alternating_braid_order"
    },
    {
      "from": "check_mobius_seed_braid_order",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_braid_order",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_center_six_phase_channels",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_center_six_phase_channels",
      "to": "self::test_center_spokes_require_six_distinct_surface_phases"
    },
    {
      "from": "check_mobius_seed_center_six_phase_channels",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_center_six_phase_channels",
      "to": "mobius_seed_center_needs_six_phase_channels_for_six_spokes"
    },
    {
      "from": "check_mobius_seed_center_six_phase_channels",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_center_six_phase_channels",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_contact_braid_exclusivity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_contact_braid_exclusivity",
      "to": "self::test_physical_contact_and_strict_braid_are_same_event_exclusive"
    },
    {
      "from": "check_mobius_seed_contact_braid_exclusivity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_contact_braid_exclusivity",
      "to": "mobius_seed_physical_contact_and_strict_braid_are_event_exclusive"
    },
    {
      "from": "check_mobius_seed_contact_braid_exclusivity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_contact_braid_exclusivity",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_direct_rotation_agreement",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_direct_rotation_agreement",
      "to": "self::test_rigid_rotation_phase_transport_matches_direct_surface_rotation"
    },
    {
      "from": "check_mobius_seed_direct_rotation_agreement",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_direct_rotation_agreement",
      "to": "mobius_seed_incident_certified_dyads_are_state_incompatible"
    },
    {
      "from": "check_mobius_seed_direct_rotation_agreement",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_direct_rotation_agreement",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_dyad_phase_schedule",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_dyad_phase_schedule",
      "to": "self::test_dyad_is_anti_aligned_and_outer_phases_increment"
    },
    {
      "from": "check_mobius_seed_dyad_phase_schedule",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_dyad_phase_schedule",
      "to": "mobius_seed_dyad_is_anti_aligned_and_outer_phase_is_incremental"
    },
    {
      "from": "check_mobius_seed_dyad_phase_schedule",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_dyad_phase_schedule",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_global_certificate_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_global_certificate_firewall",
      "to": "self::test_generated_certificate_is_deterministic_nonselecting_and_bounded"
    },
    {
      "from": "check_mobius_seed_global_certificate_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_global_certificate_firewall",
      "to": "mobius_seed_global_compatibility_certificate_is_nonselecting"
    },
    {
      "from": "check_mobius_seed_global_certificate_firewall",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_global_certificate_firewall",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_incident_dyad_state_incompatibility",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_incident_dyad_state_incompatibility",
      "to": "self::test_all_oriented_incident_edge_states_are_incompatible"
    },
    {
      "from": "check_mobius_seed_incident_dyad_state_incompatibility",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_incident_dyad_state_incompatibility",
      "to": "mobius_seed_incident_certified_dyads_are_state_incompatible"
    },
    {
      "from": "check_mobius_seed_incident_dyad_state_incompatibility",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_incident_dyad_state_incompatibility",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_null_void",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_null_void",
      "to": "self::test_null_lift_has_six_distinct_nonzero_lanes_and_origin_margin"
    },
    {
      "from": "check_mobius_seed_null_void",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_null_void",
      "to": "mobius_seed_lift_preserves_null_as_nonvertex_void"
    },
    {
      "from": "check_mobius_seed_null_void",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_null_void",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_pr174_zero_inheritance",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_pr174_zero_inheritance",
      "to": "self::test_pinned_pr174_schedule_inherits_zero_complete_local_certificates"
    },
    {
      "from": "check_mobius_seed_pr174_zero_inheritance",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_pr174_zero_inheritance",
      "to": "mobius_seed_pr174_inherits_no_exact_rigid_vesica_pairs"
    },
    {
      "from": "check_mobius_seed_pr174_zero_inheritance",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_pr174_zero_inheritance",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_projection_pair_completion",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_projection_pair_completion",
      "to": "self::test_projection_retains_exact_seed_nodes_and_all_pairs"
    },
    {
      "from": "check_mobius_seed_projection_pair_completion",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_projection_pair_completion",
      "to": "mobius_seed_projection_is_exact_and_pair_complete"
    },
    {
      "from": "check_mobius_seed_projection_pair_completion",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_projection_pair_completion",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_proof_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_proof_firewall",
      "to": "self::test_receipt_and_obj_are_deterministic_nonselecting_candidates"
    },
    {
      "from": "check_mobius_seed_proof_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_proof_firewall",
      "to": "mobius_seed_candidate_is_nonselecting_and_proof_firewalled"
    },
    {
      "from": "check_mobius_seed_proof_firewall",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_proof_firewall",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_rigid_rotation_transport",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_rigid_rotation_transport",
      "to": "self::test_rigid_rotation_transport_is_exact_on_representative_spokes"
    },
    {
      "from": "check_mobius_seed_rigid_rotation_transport",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_rigid_rotation_transport",
      "to": "mobius_seed_incident_certified_dyads_are_state_incompatible"
    },
    {
      "from": "check_mobius_seed_rigid_rotation_transport",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_rigid_rotation_transport",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_single_state_capacity_three",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_single_state_capacity_three",
      "to": "self::test_compatible_certified_pairs_have_exact_maximum_capacity_three"
    },
    {
      "from": "check_mobius_seed_single_state_capacity_three",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_single_state_capacity_three",
      "to": "mobius_seed_single_state_certified_capacity_is_three"
    },
    {
      "from": "check_mobius_seed_single_state_capacity_three",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_single_state_capacity_three",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_surface_phase_quotient",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_surface_phase_quotient",
      "to": "self::test_surface_phase_uses_the_unlabelled_half_turn_quotient"
    },
    {
      "from": "check_mobius_seed_surface_phase_quotient",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_surface_phase_quotient",
      "to": "mobius_seed_incident_certified_dyads_are_state_incompatible"
    },
    {
      "from": "check_mobius_seed_surface_phase_quotient",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_surface_phase_quotient",
      "to": "python3"
    },
    {
      "from": "check_mobius_seed_surface_quotient",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_surface_quotient",
      "to": "self::test_each_surface_obeys_mobius_seam_and_two_turn_return"
    },
    {
      "from": "check_mobius_seed_surface_quotient",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_surface_quotient",
      "to": "mobius_seed_surface_obeys_360_seam_and_720_return"
    },
    {
      "from": "check_mobius_seed_surface_quotient",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_seed_surface_quotient",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_alternate_branch_obstruction",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_alternate_branch_obstruction",
      "to": "self::test_sturm_certificate_proves_exactly_four_physical_boundary_contacts"
    },
    {
      "from": "check_mobius_vesica_alternate_branch_obstruction",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_alternate_branch_obstruction",
      "to": "mobius_vesica_alternate_height_branch_is_obstructed"
    },
    {
      "from": "check_mobius_vesica_alternate_branch_obstruction",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_alternate_branch_obstruction",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_centerline_contacts",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_centerline_contacts",
      "to": "self::test_centerlines_have_exactly_two_contacts_and_positive_null_clearance"
    },
    {
      "from": "check_mobius_vesica_centerline_contacts",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_centerline_contacts",
      "to": "mobius_vesica_has_exact_two_centerline_contacts"
    },
    {
      "from": "check_mobius_vesica_centerline_contacts",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_centerline_contacts",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_contact_semantics",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_contact_semantics",
      "to": "self::test_contact_semantics_and_global_surface_boundary_remain_distinct"
    },
    {
      "from": "check_mobius_vesica_contact_semantics",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_contact_semantics",
      "to": "mobius_vesica_contact_semantics_are_not_flattened"
    },
    {
      "from": "check_mobius_vesica_contact_semantics",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_contact_semantics",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_four_boundary_contacts",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_four_boundary_contacts",
      "to": "self::test_sturm_certificate_proves_exactly_four_physical_boundary_contacts"
    },
    {
      "from": "check_mobius_vesica_four_boundary_contacts",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_four_boundary_contacts",
      "to": "mobius_vesica_sturm_proves_four_physical_boundary_contacts"
    },
    {
      "from": "check_mobius_vesica_four_boundary_contacts",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_four_boundary_contacts",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_half_turn_obstruction",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_half_turn_obstruction",
      "to": "self::test_seed_half_turn_phase_is_obstructed_and_cannot_inherit_certificate"
    },
    {
      "from": "check_mobius_vesica_half_turn_obstruction",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_half_turn_obstruction",
      "to": "mobius_vesica_half_turn_phase_has_exact_contact_obstruction"
    },
    {
      "from": "check_mobius_vesica_half_turn_obstruction",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_half_turn_obstruction",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_null_clearance",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_null_clearance",
      "to": "self::test_centerlines_have_exactly_two_contacts_and_positive_null_clearance"
    },
    {
      "from": "check_mobius_vesica_null_clearance",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_null_clearance",
      "to": "mobius_vesica_null_origin_has_positive_clearance"
    },
    {
      "from": "check_mobius_vesica_null_clearance",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_null_clearance",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_quotient_return",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_quotient_return",
      "to": "self::test_each_band_obeys_one_turn_seam_and_two_turn_return"
    },
    {
      "from": "check_mobius_vesica_quotient_return",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_quotient_return",
      "to": "mobius_vesica_obeys_one_turn_seam_and_two_turn_return"
    },
    {
      "from": "check_mobius_vesica_quotient_return",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_quotient_return",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_receipt_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_receipt_firewall",
      "to": "self::test_combined_receipt_is_deterministic_nonselecting_and_firewalled"
    },
    {
      "from": "check_mobius_vesica_receipt_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_receipt_firewall",
      "to": "mobius_vesica_certificate_is_nonselecting_and_zeta_firewalled"
    },
    {
      "from": "check_mobius_vesica_receipt_firewall",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_receipt_firewall",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_seed_phase_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_seed_phase_firewall",
      "to": "self::test_seed_half_turn_phase_is_obstructed_and_cannot_inherit_certificate"
    },
    {
      "from": "check_mobius_vesica_seed_phase_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_seed_phase_firewall",
      "to": "mobius_vesica_seed_phase_mismatch_blocks_certificate_inheritance"
    },
    {
      "from": "check_mobius_vesica_seed_phase_firewall",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_seed_phase_firewall",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_source_claims",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_source_claims",
      "to": "self::test_sturm_certificate_proves_exactly_four_physical_boundary_contacts"
    },
    {
      "from": "check_mobius_vesica_source_claims",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_source_claims",
      "to": "mobius_vesica_preserves_source_claims_as_testable_geometry"
    },
    {
      "from": "check_mobius_vesica_source_claims",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_source_claims",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_structural_placements",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_structural_placements",
      "to": "self::test_rigid_placement_plan_covers_all_twelve_structural_pairs"
    },
    {
      "from": "check_mobius_vesica_structural_placements",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_structural_placements",
      "to": "mobius_vesica_rigid_placements_cover_seed_structural_pairs"
    },
    {
      "from": "check_mobius_vesica_structural_placements",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_structural_placements",
      "to": "python3"
    },
    {
      "from": "check_mobius_vesica_width_continuation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_width_continuation",
      "to": "self::test_width_continuation_recertifies_four_contacts_at_every_stage"
    },
    {
      "from": "check_mobius_vesica_width_continuation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_width_continuation",
      "to": "mobius_vesica_width_continuation_recertifies_each_stage"
    },
    {
      "from": "check_mobius_vesica_width_continuation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_mobius_vesica_width_continuation",
      "to": "python3"
    },
    {
      "from": "check_nilpotent_phase_binding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_phase_binding",
      "to": "self::test_phase_co_winners_bind_identical_inputs"
    },
    {
      "from": "check_nilpotent_phase_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_phase_binding",
      "to": "prime_nilpotent_phase_binding_is_topological"
    },
    {
      "from": "check_nilpotent_phase_binding",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_phase_binding",
      "to": "python3"
    },
    {
      "from": "check_nilpotent_primary_replay",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_primary_replay",
      "to": "self::test_checked_in_receipt_records_exact_replay"
    },
    {
      "from": "check_nilpotent_primary_replay",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_primary_replay",
      "to": "prime_nilpotent_primary_and_replay_agree"
    },
    {
      "from": "check_nilpotent_primary_replay",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_primary_replay",
      "to": "python3"
    },
    {
      "from": "check_nilpotent_protocol_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_protocol_identity",
      "to": "self::test_protocol_identity_and_frozen_receipt"
    },
    {
      "from": "check_nilpotent_protocol_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_protocol_identity",
      "to": "prime_nilpotent_protocol_identity_is_frozen"
    },
    {
      "from": "check_nilpotent_protocol_identity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_protocol_identity",
      "to": "python3"
    },
    {
      "from": "check_nilpotent_rank_exclusion",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_rank_exclusion",
      "to": "self::test_comparison_excludes_weight_one_rank"
    },
    {
      "from": "check_nilpotent_rank_exclusion",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_rank_exclusion",
      "to": "prime_nilpotent_comparison_excludes_known_rank"
    },
    {
      "from": "check_nilpotent_rank_exclusion",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_nilpotent_rank_exclusion",
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
      "from": "check_partial_initiation_marked_seam_provenance",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_marked_seam_provenance",
      "to": "self::test_marked_seam_survives_numeric_coordinate_cut_movement"
    },
    {
      "from": "check_partial_initiation_marked_seam_provenance",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_marked_seam_provenance",
      "to": "partial_initiation_seam_is_provenance_bearing"
    },
    {
      "from": "check_partial_initiation_marked_seam_provenance",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_marked_seam_provenance",
      "to": "python3"
    },
    {
      "from": "check_partial_initiation_motion_history",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_motion_history",
      "to": "self::test_360_changes_720_returns_and_two_motion_receipts_survive"
    },
    {
      "from": "check_partial_initiation_motion_history",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_motion_history",
      "to": "partial_initiation_motion_preserves_360_720_and_history"
    },
    {
      "from": "check_partial_initiation_motion_history",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_motion_history",
      "to": "python3"
    },
    {
      "from": "check_partial_initiation_rc_packet",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_rc_packet",
      "to": "self::test_v013_report_is_complete_bounded_and_nonselecting"
    },
    {
      "from": "check_partial_initiation_rc_packet",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_rc_packet",
      "to": "partial_initiation_report_executes_rc_packet_without_selection"
    },
    {
      "from": "check_partial_initiation_rc_packet",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_rc_packet",
      "to": "python3"
    },
    {
      "from": "check_partial_initiation_sheet_involution",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_sheet_involution",
      "to": "self::test_exact_sheet_involution_matches_signed_local_quotient"
    },
    {
      "from": "check_partial_initiation_sheet_involution",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_sheet_involution",
      "to": "partial_initiation_exact_quotient_compatibility"
    },
    {
      "from": "check_partial_initiation_sheet_involution",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_sheet_involution",
      "to": "python3"
    },
    {
      "from": "check_partial_initiation_structural_null_topology",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_structural_null_topology",
      "to": "self::test_structural_null_is_disjoint_typed_prestate_with_partial_edges"
    },
    {
      "from": "check_partial_initiation_structural_null_topology",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_structural_null_topology",
      "to": "partial_initiation_structural_null_topology_is_explicit"
    },
    {
      "from": "check_partial_initiation_structural_null_topology",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_structural_null_topology",
      "to": "python3"
    },
    {
      "from": "check_partial_initiation_twist_receipts",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_twist_receipts",
      "to": "self::test_every_word_attachment_has_one_source_bound_twist_receipt"
    },
    {
      "from": "check_partial_initiation_twist_receipts",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_twist_receipts",
      "to": "partial_initiation_twist_receipt_is_source_bound"
    },
    {
      "from": "check_partial_initiation_twist_receipts",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_partial_initiation_twist_receipts",
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
      "from": "check_prime_arithmetic_geometry_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_arithmetic_geometry_firewall",
      "to": "self::test_arithmetic_and_geometry_are_separate"
    },
    {
      "from": "check_prime_arithmetic_geometry_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_arithmetic_geometry_firewall",
      "to": "prime_arithmetic_geometry_firewall"
    },
    {
      "from": "check_prime_arithmetic_geometry_firewall",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_arithmetic_geometry_firewall",
      "to": "python3"
    },
    {
      "from": "check_prime_borromean_magnus",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_borromean_magnus",
      "to": "self::test_borromean_magnus_benchmark_is_unit"
    },
    {
      "from": "check_prime_borromean_magnus",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_borromean_magnus",
      "to": "prime_magnus_benchmark_recovers_borromean_integer"
    },
    {
      "from": "check_prime_borromean_magnus",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_borromean_magnus",
      "to": "python3"
    },
    {
      "from": "check_prime_boundary_cable_winding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_cable_winding",
      "to": "self::test_boundary_cable_classes_and_component_knot_invariants"
    },
    {
      "from": "check_prime_boundary_cable_winding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_cable_winding",
      "to": "prime_boundary_cable_winding_is_derived_from_phase"
    },
    {
      "from": "check_prime_boundary_cable_winding",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_cable_winding",
      "to": "python3"
    },
    {
      "from": "check_prime_boundary_component_knot_types",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_component_knot_types",
      "to": "self::test_boundary_component_cable_and_knot_invariants"
    },
    {
      "from": "check_prime_boundary_component_knot_types",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_component_knot_types",
      "to": "prime_boundary_component_knot_types_are_derived"
    },
    {
      "from": "check_prime_boundary_component_knot_types",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_component_knot_types",
      "to": "python3"
    },
    {
      "from": "check_prime_boundary_helper_facade",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_helper_facade",
      "to": "self::test_boundary_and_mixed_linking_blocks_follow_cable_homology"
    },
    {
      "from": "check_prime_boundary_helper_facade",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_helper_facade",
      "to": "prime_boundary_helper_is_facade_witnessed"
    },
    {
      "from": "check_prime_boundary_helper_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_helper_facade",
      "to": "python3"
    },
    {
      "from": "check_prime_boundary_helper_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_helper_facade",
      "to": "sympy"
    },
    {
      "from": "check_prime_boundary_linking_fourfold",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_linking_fourfold",
      "to": "self::test_boundary_linking_matrices_are_four_times_core_matrices"
    },
    {
      "from": "check_prime_boundary_linking_fourfold",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_linking_fourfold",
      "to": "prime_boundary_linking_scales_by_four"
    },
    {
      "from": "check_prime_boundary_linking_fourfold",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_linking_fourfold",
      "to": "python3"
    },
    {
      "from": "check_prime_boundary_linking_matrix",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_linking_matrix",
      "to": "self::test_boundary_and_mixed_linking_blocks_follow_cable_homology"
    },
    {
      "from": "check_prime_boundary_linking_matrix",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_linking_matrix",
      "to": "prime_boundary_linking_matrix_follows_cable_homology"
    },
    {
      "from": "check_prime_boundary_linking_matrix",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_linking_matrix",
      "to": "python3"
    },
    {
      "from": "check_prime_boundary_linking_matrix",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_linking_matrix",
      "to": "sympy"
    },
    {
      "from": "check_prime_boundary_single_closed_component",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_single_closed_component",
      "to": "self::test_each_mobius_ribbon_has_one_closed_two_turn_boundary"
    },
    {
      "from": "check_prime_boundary_single_closed_component",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_single_closed_component",
      "to": "prime_boundary_curve_is_single_and_closed"
    },
    {
      "from": "check_prime_boundary_single_closed_component",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_single_closed_component",
      "to": "python3"
    },
    {
      "from": "check_prime_boundary_single_two_turn_component",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_single_two_turn_component",
      "to": "self::test_each_mobius_boundary_is_one_two_turn_component"
    },
    {
      "from": "check_prime_boundary_single_two_turn_component",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_single_two_turn_component",
      "to": "prime_boundary_curve_is_single_two_turn_component"
    },
    {
      "from": "check_prime_boundary_single_two_turn_component",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_boundary_single_two_turn_component",
      "to": "python3"
    },
    {
      "from": "check_prime_exact_receipt_nonselecting",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_exact_receipt_nonselecting",
      "to": "self::test_family_receipt_is_deterministic_bounded_and_nonselecting"
    },
    {
      "from": "check_prime_exact_receipt_nonselecting",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_exact_receipt_nonselecting",
      "to": "prime_exact_milnor_alexander_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_exact_receipt_nonselecting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_exact_receipt_nonselecting",
      "to": "mpmath"
    },
    {
      "from": "check_prime_exact_receipt_nonselecting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_exact_receipt_nonselecting",
      "to": "python3"
    },
    {
      "from": "check_prime_fox_complete_fingerprint",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_fox_complete_fingerprint",
      "to": "self::test_fox_rank_fingerprints_cover_every_prime_character"
    },
    {
      "from": "check_prime_fox_complete_fingerprint",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_fox_complete_fingerprint",
      "to": "prime_fox_fingerprint_covers_all_prime_characters"
    },
    {
      "from": "check_prime_fox_complete_fingerprint",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_fox_complete_fingerprint",
      "to": "mpmath"
    },
    {
      "from": "check_prime_fox_complete_fingerprint",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_fox_complete_fingerprint",
      "to": "python3"
    },
    {
      "from": "check_prime_generic_diagram_fixed",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_diagram_fixed",
      "to": "self::test_generic_projection_preserves_positive_isotopy_clearance"
    },
    {
      "from": "check_prime_generic_diagram_fixed",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_diagram_fixed",
      "to": "prime_generic_diagram_is_fixed_before_invariants"
    },
    {
      "from": "check_prime_generic_diagram_fixed",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_diagram_fixed",
      "to": "mpmath"
    },
    {
      "from": "check_prime_generic_diagram_fixed",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_diagram_fixed",
      "to": "python3"
    },
    {
      "from": "check_prime_generic_helper_facade",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_helper_facade",
      "to": "self::test_generic_diagram_and_length_three_milnor_profile"
    },
    {
      "from": "check_prime_generic_helper_facade",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_helper_facade",
      "to": "prime_generic_helper_is_facade_witnessed"
    },
    {
      "from": "check_prime_generic_helper_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_helper_facade",
      "to": "mpmath"
    },
    {
      "from": "check_prime_generic_helper_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_helper_facade",
      "to": "python3"
    },
    {
      "from": "check_prime_generic_interval_atan2",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_atan2",
      "to": "self::test_all_frozen_turns_are_inside_outward_atan2_intervals"
    },
    {
      "from": "check_prime_generic_interval_atan2",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_atan2",
      "to": "prime_generic_turns_are_outward_atan2_enclosed"
    },
    {
      "from": "check_prime_generic_interval_atan2",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_atan2",
      "to": "mpmath"
    },
    {
      "from": "check_prime_generic_interval_atan2",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_atan2",
      "to": "python3"
    },
    {
      "from": "check_prime_generic_interval_atan2",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_atan2",
      "to": "system-libmpfr"
    },
    {
      "from": "check_prime_generic_interval_crossing_signs",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_crossing_signs",
      "to": "self::test_all_p7_first_p5_second_crossing_signs_are_certified"
    },
    {
      "from": "check_prime_generic_interval_crossing_signs",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_crossing_signs",
      "to": "prime_generic_crossing_signs_are_interval_certified"
    },
    {
      "from": "check_prime_generic_interval_crossing_signs",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_crossing_signs",
      "to": "mpmath"
    },
    {
      "from": "check_prime_generic_interval_crossing_signs",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_crossing_signs",
      "to": "python3"
    },
    {
      "from": "check_prime_generic_interval_crossing_signs",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_crossing_signs",
      "to": "system-libmpfr"
    },
    {
      "from": "check_prime_generic_interval_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_receipt",
      "to": "self::test_family_receipt_is_deterministic_complete_and_nonselecting"
    },
    {
      "from": "check_prime_generic_interval_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_receipt",
      "to": "prime_generic_interval_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_generic_interval_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_receipt",
      "to": "mpmath"
    },
    {
      "from": "check_prime_generic_interval_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_receipt",
      "to": "python3"
    },
    {
      "from": "check_prime_generic_interval_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_receipt",
      "to": "system-libmpfr"
    },
    {
      "from": "check_prime_generic_interval_smooth_signs",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_smooth_signs",
      "to": "self::test_all_smooth_height_intervals_exclude_zero_and_preserve_order"
    },
    {
      "from": "check_prime_generic_interval_smooth_signs",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_smooth_signs",
      "to": "prime_generic_smooth_signs_are_interval_certified"
    },
    {
      "from": "check_prime_generic_interval_smooth_signs",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_smooth_signs",
      "to": "mpmath"
    },
    {
      "from": "check_prime_generic_interval_smooth_signs",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_smooth_signs",
      "to": "python3"
    },
    {
      "from": "check_prime_generic_interval_smooth_signs",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_interval_smooth_signs",
      "to": "system-libmpfr"
    },
    {
      "from": "check_prime_generic_pairwise_linking",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_pairwise_linking",
      "to": "self::test_generic_diagrams_reproduce_complete_linking_matrices"
    },
    {
      "from": "check_prime_generic_pairwise_linking",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_pairwise_linking",
      "to": "prime_generic_diagram_preserves_pairwise_linking"
    },
    {
      "from": "check_prime_generic_pairwise_linking",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_pairwise_linking",
      "to": "mpmath"
    },
    {
      "from": "check_prime_generic_pairwise_linking",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_generic_pairwise_linking",
      "to": "python3"
    },
    {
      "from": "check_prime_grobner_complete_accounting",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_complete_accounting",
      "to": "self::test_complete_minor_accounting_is_sealed"
    },
    {
      "from": "check_prime_grobner_complete_accounting",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_complete_accounting",
      "to": "prime_grobner_generators_cover_every_maximal_minor"
    },
    {
      "from": "check_prime_grobner_complete_accounting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_complete_accounting",
      "to": "python3"
    },
    {
      "from": "check_prime_grobner_complete_accounting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_complete_accounting",
      "to": "sympy"
    },
    {
      "from": "check_prime_grobner_nonclaims",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_nonclaims",
      "to": "self::test_result_document_preserves_research_boundary"
    },
    {
      "from": "check_prime_grobner_nonclaims",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_nonclaims",
      "to": "prime_grobner_receipt_preserves_nonclaims"
    },
    {
      "from": "check_prime_grobner_nonclaims",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_nonclaims",
      "to": "python3"
    },
    {
      "from": "check_prime_grobner_protocol_frozen",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_protocol_frozen",
      "to": "self::test_protocol_and_parent_presentations_are_frozen"
    },
    {
      "from": "check_prime_grobner_protocol_frozen",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_protocol_frozen",
      "to": "prime_grobner_protocol_identity_is_frozen"
    },
    {
      "from": "check_prime_grobner_protocol_frozen",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_protocol_frozen",
      "to": "python3"
    },
    {
      "from": "check_prime_grobner_reduced_bases",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_reduced_bases",
      "to": "self::test_sealed_reduced_bases_have_expected_digests"
    },
    {
      "from": "check_prime_grobner_reduced_bases",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_reduced_bases",
      "to": "prime_grobner_basis_is_complete_reduced_and_saturated"
    },
    {
      "from": "check_prime_grobner_reduced_bases",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_reduced_bases",
      "to": "python3"
    },
    {
      "from": "check_prime_grobner_reduced_bases",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_reduced_bases",
      "to": "sympy"
    },
    {
      "from": "check_prime_grobner_replay",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_replay",
      "to": "self::test_independent_replay_is_exact"
    },
    {
      "from": "check_prime_grobner_replay",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_replay",
      "to": "prime_grobner_independent_replay_agrees"
    },
    {
      "from": "check_prime_grobner_replay",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_replay",
      "to": "python3"
    },
    {
      "from": "check_prime_grobner_replay",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_grobner_replay",
      "to": "sympy"
    },
    {
      "from": "check_prime_higher_order_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_higher_order_boundary",
      "to": "self::test_algebraically_split_triples_are_enumerated_without_fake_milnor_values"
    },
    {
      "from": "check_prime_higher_order_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_higher_order_boundary",
      "to": "prime_higher_order_boundary_is_explicit"
    },
    {
      "from": "check_prime_higher_order_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_higher_order_boundary",
      "to": "python3"
    },
    {
      "from": "check_prime_independent_receipt_nonselecting",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_independent_receipt_nonselecting",
      "to": "self::test_research_boundaries_remain_explicit"
    },
    {
      "from": "check_prime_independent_receipt_nonselecting",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_independent_receipt_nonselecting",
      "to": "prime_independent_phase_milnor_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_independent_receipt_nonselecting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_independent_receipt_nonselecting",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_boundaries_p7_first",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundaries_p7_first",
      "to": "self::test_family_receipt_preserves_p7_first_order"
    },
    {
      "from": "check_prime_interval_boundaries_p7_first",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundaries_p7_first",
      "to": "prime_interval_boundaries_p7_precedes_p5"
    },
    {
      "from": "check_prime_interval_boundaries_p7_first",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundaries_p7_first",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_boundaries_p7_first",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundaries_p7_first",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_boundary_compact_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_compact_receipt",
      "to": "self::test_receipt_and_boundary_exports_are_deterministic_and_firewalled"
    },
    {
      "from": "check_prime_interval_boundary_compact_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_compact_receipt",
      "to": "prime_interval_boundary_compact_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_interval_boundary_compact_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_compact_receipt",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_boundary_compact_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_compact_receipt",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_boundary_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_receipt",
      "to": "self::test_receipt_and_boundary_models_are_deterministic_and_bounded"
    },
    {
      "from": "check_prime_interval_boundary_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_receipt",
      "to": "prime_interval_boundary_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_interval_boundary_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_receipt",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_boundary_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_receipt",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_boundary_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_receipt",
      "to": "sympy"
    },
    {
      "from": "check_prime_interval_boundary_research_order",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_research_order",
      "to": "self::test_family_certificate_preserves_p7_first_order"
    },
    {
      "from": "check_prime_interval_boundary_research_order",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_research_order",
      "to": "prime_interval_boundary_p7_precedes_p5"
    },
    {
      "from": "check_prime_interval_boundary_research_order",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_research_order",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_boundary_research_order",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_research_order",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_boundary_research_order",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_boundary_research_order",
      "to": "sympy"
    },
    {
      "from": "check_prime_interval_common_facade",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_common_facade",
      "to": "self::test_outward_interval_replay_covers_every_pair"
    },
    {
      "from": "check_prime_interval_common_facade",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_common_facade",
      "to": "prime_interval_common_is_facade_witnessed"
    },
    {
      "from": "check_prime_interval_common_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_common_facade",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_common_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_common_facade",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_finite_width_disjointness",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_finite_width_disjointness",
      "to": "self::test_interval_margin_implies_complete_ribbon_disjointness"
    },
    {
      "from": "check_prime_interval_finite_width_disjointness",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_finite_width_disjointness",
      "to": "prime_interval_replay_preserves_finite_width_disjointness"
    },
    {
      "from": "check_prime_interval_finite_width_disjointness",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_finite_width_disjointness",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_finite_width_disjointness",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_finite_width_disjointness",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_outward_replay",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_outward_replay",
      "to": "self::test_outward_interval_replay_covers_every_pair"
    },
    {
      "from": "check_prime_interval_outward_replay",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_outward_replay",
      "to": "prime_interval_replay_is_outward_rounded"
    },
    {
      "from": "check_prime_interval_outward_replay",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_outward_replay",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_outward_replay",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_outward_replay",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_replay_helper_facade",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_replay_helper_facade",
      "to": "self::test_outward_interval_replay_covers_every_pair"
    },
    {
      "from": "check_prime_interval_replay_helper_facade",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_replay_helper_facade",
      "to": "prime_interval_replay_helper_is_facade_witnessed"
    },
    {
      "from": "check_prime_interval_replay_helper_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_replay_helper_facade",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_replay_helper_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_replay_helper_facade",
      "to": "python3"
    },
    {
      "from": "check_prime_interval_replay_outward_endpoints",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_replay_outward_endpoints",
      "to": "self::test_interval_replay_closes_every_complete_parameter_torus"
    },
    {
      "from": "check_prime_interval_replay_outward_endpoints",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_replay_outward_endpoints",
      "to": "prime_interval_replay_uses_outward_endpoints"
    },
    {
      "from": "check_prime_interval_replay_outward_endpoints",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_replay_outward_endpoints",
      "to": "mpmath"
    },
    {
      "from": "check_prime_interval_replay_outward_endpoints",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_interval_replay_outward_endpoints",
      "to": "python3"
    },
    {
      "from": "check_prime_legacy_readable_adapter",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_legacy_readable_adapter",
      "to": "self::test_legacy_surface_is_an_explicit_adapter_over_readable_evidence"
    },
    {
      "from": "check_prime_legacy_readable_adapter",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_legacy_readable_adapter",
      "to": "prime_interval_replay_uses_outward_endpoints"
    },
    {
      "from": "check_prime_legacy_readable_adapter",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_legacy_readable_adapter",
      "to": "mpmath"
    },
    {
      "from": "check_prime_legacy_readable_adapter",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_legacy_readable_adapter",
      "to": "python3"
    },
    {
      "from": "check_prime_legacy_readable_adapter",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_legacy_readable_adapter",
      "to": "sympy"
    },
    {
      "from": "check_prime_length4_bounded_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_bounded_receipt",
      "to": "self::test_receipt_is_deterministic_and_bounded"
    },
    {
      "from": "check_prime_length4_bounded_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_bounded_receipt",
      "to": "prime_p7_length4_receipt_is_bounded"
    },
    {
      "from": "check_prime_length4_bounded_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_bounded_receipt",
      "to": "mpmath"
    },
    {
      "from": "check_prime_length4_bounded_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_bounded_receipt",
      "to": "python3"
    },
    {
      "from": "check_prime_length4_commutator_gate",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_commutator_gate",
      "to": "self::test_frozen_degree_three_commutator_gate"
    },
    {
      "from": "check_prime_length4_commutator_gate",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_commutator_gate",
      "to": "prime_length4_magnus_gate_matches_frozen_commutator"
    },
    {
      "from": "check_prime_length4_commutator_gate",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_commutator_gate",
      "to": "python3"
    },
    {
      "from": "check_prime_length4_cyclic_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_cyclic_receipt",
      "to": "self::test_result_records_primary_reverse_and_cyclic_coefficients"
    },
    {
      "from": "check_prime_length4_cyclic_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_cyclic_receipt",
      "to": "prime_p7_length4_result_records_cyclic_conventions"
    },
    {
      "from": "check_prime_length4_cyclic_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_cyclic_receipt",
      "to": "mpmath"
    },
    {
      "from": "check_prime_length4_cyclic_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_cyclic_receipt",
      "to": "python3"
    },
    {
      "from": "check_prime_length4_lower_gates",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_lower_gates",
      "to": "self::test_frozen_target_and_lower_order_gates"
    },
    {
      "from": "check_prime_length4_lower_gates",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_lower_gates",
      "to": "prime_p7_length4_target_is_frozen_and_lower_gated"
    },
    {
      "from": "check_prime_length4_lower_gates",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_lower_gates",
      "to": "mpmath"
    },
    {
      "from": "check_prime_length4_lower_gates",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length4_lower_gates",
      "to": "python3"
    },
    {
      "from": "check_prime_length_three_milnor_profile",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_length_three_milnor_profile",
      "to": "self::test_generic_diagram_and_length_three_milnor_profile"
    },
    {
      "from": "check_prime_length_three_milnor_profile",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_length_three_milnor_profile",
      "to": "prime_length_three_milnor_profile_is_computed_after_global_lift"
    },
    {
      "from": "check_prime_length_three_milnor_profile",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length_three_milnor_profile",
      "to": "mpmath"
    },
    {
      "from": "check_prime_length_three_milnor_profile",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_length_three_milnor_profile",
      "to": "python3"
    },
    {
      "from": "check_prime_milnor_borromean_benchmark",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_borromean_benchmark",
      "to": "self::test_fourier_milnor_benchmark_converges_to_minus_one"
    },
    {
      "from": "check_prime_milnor_borromean_benchmark",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_borromean_benchmark",
      "to": "prime_milnor_fourier_benchmark_recovers_borromean"
    },
    {
      "from": "check_prime_milnor_borromean_benchmark",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_borromean_benchmark",
      "to": "numpy"
    },
    {
      "from": "check_prime_milnor_borromean_benchmark",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_borromean_benchmark",
      "to": "python3"
    },
    {
      "from": "check_prime_milnor_exactness_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_exactness_boundary",
      "to": "self::test_numerical_resolution_is_not_promoted_to_exact_theorem"
    },
    {
      "from": "check_prime_milnor_exactness_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_exactness_boundary",
      "to": "prime_milnor_exactness_boundary_is_preserved"
    },
    {
      "from": "check_prime_milnor_exactness_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_exactness_boundary",
      "to": "python3"
    },
    {
      "from": "check_prime_milnor_helper_facade",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_helper_facade",
      "to": "self::test_generic_diagram_and_length_three_milnor_profile"
    },
    {
      "from": "check_prime_milnor_helper_facade",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_helper_facade",
      "to": "prime_milnor_helper_is_facade_witnessed"
    },
    {
      "from": "check_prime_milnor_helper_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_helper_facade",
      "to": "mpmath"
    },
    {
      "from": "check_prime_milnor_helper_facade",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_helper_facade",
      "to": "python3"
    },
    {
      "from": "check_prime_milnor_p7_zero_resolution",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_p7_zero_resolution",
      "to": "self::test_all_five_p7_triples_converge_numerically_to_zero"
    },
    {
      "from": "check_prime_milnor_p7_zero_resolution",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_p7_zero_resolution",
      "to": "prime_milnor_p7_split_triples_resolve_numerically_to_zero"
    },
    {
      "from": "check_prime_milnor_p7_zero_resolution",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_p7_zero_resolution",
      "to": "numpy"
    },
    {
      "from": "check_prime_milnor_p7_zero_resolution",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_milnor_p7_zero_resolution",
      "to": "python3"
    },
    {
      "from": "check_prime_mixed_core_boundary_matrix",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_mixed_core_boundary_matrix",
      "to": "self::test_mixed_core_boundary_matrices_are_full_rank_with_exact_determinants"
    },
    {
      "from": "check_prime_mixed_core_boundary_matrix",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_mixed_core_boundary_matrix",
      "to": "prime_mixed_core_boundary_matrix_is_complete"
    },
    {
      "from": "check_prime_mixed_core_boundary_matrix",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_mixed_core_boundary_matrix",
      "to": "python3"
    },
    {
      "from": "check_prime_mixed_integer_invariants",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_mixed_integer_invariants",
      "to": "self::test_full_core_boundary_integer_invariants_distinguish_p7_and_p5"
    },
    {
      "from": "check_prime_mixed_integer_invariants",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_mixed_integer_invariants",
      "to": "prime_mixed_linking_matrix_has_exact_integer_invariants"
    },
    {
      "from": "check_prime_mixed_integer_invariants",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_mixed_integer_invariants",
      "to": "python3"
    },
    {
      "from": "check_prime_mixed_integer_invariants",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_mixed_integer_invariants",
      "to": "sympy"
    },
    {
      "from": "check_prime_mpfr_backend_independence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_mpfr_backend_independence",
      "to": "self::test_direct_mpfr_replay_matches_frozen_partition"
    },
    {
      "from": "check_prime_mpfr_backend_independence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_mpfr_backend_independence",
      "to": "prime_mpfr_replay_is_backend_independent"
    },
    {
      "from": "check_prime_mpfr_backend_independence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_mpfr_backend_independence",
      "to": "libmpfr"
    },
    {
      "from": "check_prime_mpfr_backend_independence",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_mpfr_backend_independence",
      "to": "python3"
    },
    {
      "from": "check_prime_mpfr_ribbon_margin",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_mpfr_ribbon_margin",
      "to": "self::test_direct_mpfr_replay_recertifies_both_primes"
    },
    {
      "from": "check_prime_mpfr_ribbon_margin",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_mpfr_ribbon_margin",
      "to": "prime_mpfr_replay_recertifies_ribbon_margin"
    },
    {
      "from": "check_prime_mpfr_ribbon_margin",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_mpfr_ribbon_margin",
      "to": "libmpfr"
    },
    {
      "from": "check_prime_mpfr_ribbon_margin",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_mpfr_ribbon_margin",
      "to": "python3"
    },
    {
      "from": "check_prime_p5_direct_signature",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_p5_direct_signature",
      "to": "self::test_p5_exact_signature"
    },
    {
      "from": "check_prime_p5_direct_signature",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_p5_direct_signature",
      "to": "prime_p5_direct_exact_signature"
    },
    {
      "from": "check_prime_p5_direct_signature",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_p5_direct_signature",
      "to": "python3"
    },
    {
      "from": "check_prime_p7_direct_signature",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_direct_signature",
      "to": "self::test_p7_exact_signature"
    },
    {
      "from": "check_prime_p7_direct_signature",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_direct_signature",
      "to": "prime_p7_direct_exact_signature"
    },
    {
      "from": "check_prime_p7_direct_signature",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_direct_signature",
      "to": "python3"
    },
    {
      "from": "check_prime_p7_exact_milnor_zero",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_exact_milnor_zero",
      "to": "self::test_all_five_p7_milnor_coefficients_are_exact_zero"
    },
    {
      "from": "check_prime_p7_exact_milnor_zero",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_exact_milnor_zero",
      "to": "prime_p7_five_milnor_candidates_are_exact_zero_in_diagram"
    },
    {
      "from": "check_prime_p7_exact_milnor_zero",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_exact_milnor_zero",
      "to": "mpmath"
    },
    {
      "from": "check_prime_p7_exact_milnor_zero",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_exact_milnor_zero",
      "to": "python3"
    },
    {
      "from": "check_prime_p7_uniform_relation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_uniform_relation",
      "to": "self::test_p7_uniform_relation_and_uniqueness"
    },
    {
      "from": "check_prime_p7_uniform_relation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_uniform_relation",
      "to": "prime_p7_uniform_structural_relation"
    },
    {
      "from": "check_prime_p7_uniform_relation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_p7_uniform_relation",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_data_coverage",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_data_coverage",
      "to": "self::test_every_hypernode_has_distinct_phase_and_height"
    },
    {
      "from": "check_prime_phase_lift_data_coverage",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_data_coverage",
      "to": "prime_phase_lift_data_covers_every_p7_p5_hypernode"
    },
    {
      "from": "check_prime_phase_lift_data_coverage",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_data_coverage",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_disjoint_centerlines",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_disjoint_centerlines",
      "to": "self::test_projected_pair_events_are_strictly_height_separated"
    },
    {
      "from": "check_prime_phase_lift_disjoint_centerlines",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_disjoint_centerlines",
      "to": "prime_phase_lift_centerlines_are_disjoint"
    },
    {
      "from": "check_prime_phase_lift_disjoint_centerlines",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_disjoint_centerlines",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_hypernodes",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_hypernodes",
      "to": "self::test_every_hypernode_has_distinct_phase_and_height"
    },
    {
      "from": "check_prime_phase_lift_hypernodes",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_hypernodes",
      "to": "prime_phase_lift_resolves_every_hypernode"
    },
    {
      "from": "check_prime_phase_lift_hypernodes",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_hypernodes",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_links",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_links",
      "to": "self::test_link_readouts_follow_global_lift"
    },
    {
      "from": "check_prime_phase_lift_links",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_links",
      "to": "prime_phase_lift_link_numbers_are_derived"
    },
    {
      "from": "check_prime_phase_lift_links",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_links",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_model_derived_links",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_model_derived_links",
      "to": "self::test_link_readouts_follow_global_lift"
    },
    {
      "from": "check_prime_phase_lift_model_derived_links",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_model_derived_links",
      "to": "prime_phase_lift_model_derives_links_after_global_lift"
    },
    {
      "from": "check_prime_phase_lift_model_derived_links",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_model_derived_links",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_model_event_semantics",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_model_event_semantics",
      "to": "self::test_projected_pair_events_are_strictly_height_separated"
    },
    {
      "from": "check_prime_phase_lift_model_event_semantics",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_model_event_semantics",
      "to": "prime_phase_lift_model_preserves_event_semantics"
    },
    {
      "from": "check_prime_phase_lift_model_event_semantics",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_model_event_semantics",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_origin",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_origin",
      "to": "self::test_p7_origin_remains_one_arity_six_hypernode"
    },
    {
      "from": "check_prime_phase_lift_origin",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_origin",
      "to": "prime_phase_lift_preserves_nary_origin"
    },
    {
      "from": "check_prime_phase_lift_origin",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_origin",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_p5_second",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_p5_second",
      "to": "self::test_p5_is_independent_same_protocol_comparison"
    },
    {
      "from": "check_prime_phase_lift_p5_second",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_p5_second",
      "to": "prime_phase_lift_p5_follows_same_protocol"
    },
    {
      "from": "check_prime_phase_lift_p5_second",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_p5_second",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_p7_first",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_p7_first",
      "to": "self::test_p7_global_candidate_precedes_readouts"
    },
    {
      "from": "check_prime_phase_lift_p7_first",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_p7_first",
      "to": "prime_phase_lift_constructs_p7_before_restrictions"
    },
    {
      "from": "check_prime_phase_lift_p7_first",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_p7_first",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_receipt",
      "to": "self::test_receipt_is_deterministic_and_bounded"
    },
    {
      "from": "check_prime_phase_lift_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_receipt",
      "to": "prime_phase_lift_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_phase_lift_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_receipt",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_lift_seam",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_seam",
      "to": "self::test_mobius_one_turn_reversal_and_two_turn_return"
    },
    {
      "from": "check_prime_phase_lift_seam",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_seam",
      "to": "prime_phase_lift_is_seam_compatible"
    },
    {
      "from": "check_prime_phase_lift_seam",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_lift_seam",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_preregistration_hash",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_preregistration_hash",
      "to": "self::test_preregistration_hash_and_selector_order_are_frozen"
    },
    {
      "from": "check_prime_phase_preregistration_hash",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_preregistration_hash",
      "to": "prime_phase_selector_matches_frozen_preregistration"
    },
    {
      "from": "check_prime_phase_preregistration_hash",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_preregistration_hash",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_sensitivity_selection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_sensitivity_selection",
      "to": "self::test_phase_sensitivity_enumerates_all_equal_gap_alternatives"
    },
    {
      "from": "check_prime_phase_sensitivity_selection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_sensitivity_selection",
      "to": "prime_phase_sensitivity_separates_selection_from_emergence"
    },
    {
      "from": "check_prime_phase_sensitivity_selection",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_sensitivity_selection",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_torus_seven_not_forced",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_torus_seven_not_forced",
      "to": "self::test_p7_and_p5_share_the_same_maximum_gap_knot_degrees"
    },
    {
      "from": "check_prime_phase_torus_seven_not_forced",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_torus_seven_not_forced",
      "to": "prime_phase_sensitivity_torus_seven_is_not_forced"
    },
    {
      "from": "check_prime_phase_torus_seven_not_forced",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_torus_seven_not_forced",
      "to": "python3"
    },
    {
      "from": "check_prime_phase_whole_link_selector",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_whole_link_selector",
      "to": "self::test_preregistered_selector_outputs_are_not_target_fitted"
    },
    {
      "from": "check_prime_phase_whole_link_selector",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_whole_link_selector",
      "to": "prime_phase_selector_uses_whole_link_character"
    },
    {
      "from": "check_prime_phase_whole_link_selector",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_whole_link_selector",
      "to": "mpmath"
    },
    {
      "from": "check_prime_phase_whole_link_selector",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_phase_whole_link_selector",
      "to": "python3"
    },
    {
      "from": "check_prime_relational_encoder_source_independence",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_encoder_source_independence",
      "to": "self::test_frozen_encoders_do_not_delegate_to_shared_or_peer_helpers"
    },
    {
      "from": "check_prime_relational_encoder_source_independence",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_encoder_source_independence",
      "to": "prime_relational_encoders_remain_source_independent"
    },
    {
      "from": "check_prime_relational_failure_propagation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_failure_propagation",
      "to": "self::test_h3_failure_does_not_deprecate_architecture_dependents"
    },
    {
      "from": "check_prime_relational_failure_propagation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_failure_propagation",
      "to": "prime_relational_failure_propagation_is_scope_bounded"
    },
    {
      "from": "check_prime_relational_h1_reconstruction",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_h1_reconstruction",
      "to": "self::test_h1_all_erased_relations_reconstruct_exactly_in_both_implementations"
    },
    {
      "from": "check_prime_relational_h1_reconstruction",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_h1_reconstruction",
      "to": "prime_relational_h1_requires_complementary_unique_reconstruction"
    },
    {
      "from": "check_prime_relational_h2_irreducibility",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_h2_irreducibility",
      "to": "self::test_h2_every_whole_view_is_irreducible"
    },
    {
      "from": "check_prime_relational_h2_irreducibility",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_h2_irreducibility",
      "to": "prime_relational_h2_tests_every_whole_view"
    },
    {
      "from": "check_prime_relational_h3_architecture_isomorphism",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_h3_architecture_isomorphism",
      "to": "self::test_h3_baseline_preserves_prime_cardinality_architecture"
    },
    {
      "from": "check_prime_relational_h3_architecture_isomorphism",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_h3_architecture_isomorphism",
      "to": "prime_relational_baseline_isomorphism_blocks_architecture_transfer"
    },
    {
      "from": "check_prime_relational_h3_matched_baseline",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_h3_matched_baseline",
      "to": "self::test_h3_registered_criterion_falsifies_only_software_advantage"
    },
    {
      "from": "check_prime_relational_h3_matched_baseline",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_h3_matched_baseline",
      "to": "prime_relational_h3_applies_frozen_software_complexity_criterion"
    },
    {
      "from": "check_prime_relational_identity_nonleakage",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_identity_nonleakage",
      "to": "self::test_public_identity_does_not_leak_value"
    },
    {
      "from": "check_prime_relational_identity_nonleakage",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_identity_nonleakage",
      "to": "prime_relational_fixture_identity_excludes_values"
    },
    {
      "from": "check_prime_relational_independent_replay",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_independent_replay",
      "to": "self::test_independent_replay_agrees_with_committed_report"
    },
    {
      "from": "check_prime_relational_independent_replay",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_independent_replay",
      "to": "prime_relational_replay_avoids_product_import"
    },
    {
      "from": "check_prime_relational_independent_replay",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_independent_replay",
      "to": "prime_relational_replay_scopes_registered_falsification"
    },
    {
      "from": "check_prime_relational_registered_resource_bounds",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_registered_resource_bounds",
      "to": "self::test_complete_cli_run_obeys_registered_resource_bounds"
    },
    {
      "from": "check_prime_relational_registered_resource_bounds",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_registered_resource_bounds",
      "to": "prime_relational_complete_run_obeys_registered_resources"
    },
    {
      "from": "check_prime_relational_registered_resource_bounds",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_registered_resource_bounds",
      "to": "posix_resource"
    },
    {
      "from": "check_prime_relational_registered_resource_bounds",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_registered_resource_bounds",
      "to": "python3"
    },
    {
      "from": "check_prime_relational_registered_resource_bounds",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_relational_registered_resource_bounds",
      "to": "sched_affinity"
    },
    {
      "from": "check_prime_replay_data_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_data_receipt",
      "to": "self::test_receipt_is_deterministic_and_nonselecting"
    },
    {
      "from": "check_prime_replay_data_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_data_receipt",
      "to": "prime_replay_data_is_receipt_witnessed"
    },
    {
      "from": "check_prime_replay_data_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_data_receipt",
      "to": "python3"
    },
    {
      "from": "check_prime_replay_receipt_interval",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_interval",
      "to": "self::test_independent_decimal_replay_is_pinned"
    },
    {
      "from": "check_prime_replay_receipt_interval",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_interval",
      "to": "prime_replay_receipt_preserves_independent_interval_result"
    },
    {
      "from": "check_prime_replay_receipt_interval",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_interval",
      "to": "python3"
    },
    {
      "from": "check_prime_replay_receipt_milnor",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_milnor",
      "to": "self::test_all_five_length_three_values_are_zero"
    },
    {
      "from": "check_prime_replay_receipt_milnor",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_milnor",
      "to": "prime_replay_receipt_freezes_p7_milnor_values"
    },
    {
      "from": "check_prime_replay_receipt_milnor",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_milnor",
      "to": "python3"
    },
    {
      "from": "check_prime_replay_receipt_nonselecting",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_nonselecting",
      "to": "self::test_receipt_is_deterministic_and_nonselecting"
    },
    {
      "from": "check_prime_replay_receipt_nonselecting",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_nonselecting",
      "to": "prime_replay_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_replay_receipt_nonselecting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_nonselecting",
      "to": "python3"
    },
    {
      "from": "check_prime_replay_receipt_phase",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_phase",
      "to": "self::test_phase_winding_is_shared_not_prime_specific"
    },
    {
      "from": "check_prime_replay_receipt_phase",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_phase",
      "to": "prime_replay_receipt_exposes_phase_imposition"
    },
    {
      "from": "check_prime_replay_receipt_phase",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_replay_receipt_phase",
      "to": "python3"
    },
    {
      "from": "check_prime_restrictions_after_construction",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_restrictions_after_construction",
      "to": "self::test_restrictions_are_readouts_not_parts"
    },
    {
      "from": "check_prime_restrictions_after_construction",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_restrictions_after_construction",
      "to": "prime_restrictions_follow_construction"
    },
    {
      "from": "check_prime_restrictions_after_construction",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_restrictions_after_construction",
      "to": "python3"
    },
    {
      "from": "check_prime_smooth_ribbons_centerline_margin",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_centerline_margin",
      "to": "self::test_complete_parameter_tori_certify_nine_hundredths_centerline_margin"
    },
    {
      "from": "check_prime_smooth_ribbons_centerline_margin",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_centerline_margin",
      "to": "prime_smooth_ribbons_have_global_centerline_margin"
    },
    {
      "from": "check_prime_smooth_ribbons_centerline_margin",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_centerline_margin",
      "to": "python3"
    },
    {
      "from": "check_prime_smooth_ribbons_event_lanes",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_event_lanes",
      "to": "self::test_flat_step_fields_are_c_infinity_bounded_and_event_preserving"
    },
    {
      "from": "check_prime_smooth_ribbons_event_lanes",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_event_lanes",
      "to": "prime_smooth_ribbons_preserve_all_event_lanes"
    },
    {
      "from": "check_prime_smooth_ribbons_event_lanes",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_event_lanes",
      "to": "python3"
    },
    {
      "from": "check_prime_smooth_ribbons_finite_width_disjointness",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_finite_width_disjointness",
      "to": "self::test_triangle_inequality_certifies_seven_hundredths_ribbon_margin"
    },
    {
      "from": "check_prime_smooth_ribbons_finite_width_disjointness",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_finite_width_disjointness",
      "to": "prime_smooth_ribbons_are_globally_disjoint_at_declared_width"
    },
    {
      "from": "check_prime_smooth_ribbons_finite_width_disjointness",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_finite_width_disjointness",
      "to": "python3"
    },
    {
      "from": "check_prime_smooth_ribbons_linking_matrix",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_linking_matrix",
      "to": "self::test_complete_pairwise_linking_matrices_have_expected_invariants"
    },
    {
      "from": "check_prime_smooth_ribbons_linking_matrix",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_linking_matrix",
      "to": "prime_smooth_ribbons_issue_complete_linking_matrix"
    },
    {
      "from": "check_prime_smooth_ribbons_linking_matrix",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_linking_matrix",
      "to": "python3"
    },
    {
      "from": "check_prime_smooth_ribbons_mobius_return",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_mobius_return",
      "to": "self::test_smoothed_surfaces_obey_one_turn_reversal_and_two_turn_return"
    },
    {
      "from": "check_prime_smooth_ribbons_mobius_return",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_mobius_return",
      "to": "prime_smooth_ribbons_obey_mobius_return"
    },
    {
      "from": "check_prime_smooth_ribbons_mobius_return",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_mobius_return",
      "to": "python3"
    },
    {
      "from": "check_prime_smooth_ribbons_p7_first",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_p7_first",
      "to": "self::test_family_receipt_preserves_p7_first_p5_second_order"
    },
    {
      "from": "check_prime_smooth_ribbons_p7_first",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_p7_first",
      "to": "prime_smooth_ribbons_p7_precedes_p5"
    },
    {
      "from": "check_prime_smooth_ribbons_p7_first",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_p7_first",
      "to": "python3"
    },
    {
      "from": "check_prime_smooth_ribbons_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_receipt",
      "to": "self::test_receipt_and_smooth_meshes_are_deterministic_and_firewalled"
    },
    {
      "from": "check_prime_smooth_ribbons_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_receipt",
      "to": "prime_smooth_ribbons_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_smooth_ribbons_receipt",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_receipt",
      "to": "python3"
    },
    {
      "from": "check_prime_smooth_ribbons_tangent_regularization",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_tangent_regularization",
      "to": "self::test_tangent_pairs_receive_clearance_preserving_zero_link_regularizations"
    },
    {
      "from": "check_prime_smooth_ribbons_tangent_regularization",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_tangent_regularization",
      "to": "prime_smooth_ribbons_regularize_tangent_pairs"
    },
    {
      "from": "check_prime_smooth_ribbons_tangent_regularization",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_smooth_ribbons_tangent_regularization",
      "to": "python3"
    },
    {
      "from": "check_prime_symbolic_character_replay",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_character_replay",
      "to": "self::test_symbolic_specializations_replay_frozen_character_ranks"
    },
    {
      "from": "check_prime_symbolic_character_replay",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_character_replay",
      "to": "prime_symbolic_certificate_replays_finite_characters"
    },
    {
      "from": "check_prime_symbolic_character_replay",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_character_replay",
      "to": "python3"
    },
    {
      "from": "check_prime_symbolic_character_replay",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_character_replay",
      "to": "sympy"
    },
    {
      "from": "check_prime_symbolic_elementary_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_elementary_boundary",
      "to": "self::test_exact_ranks_and_first_nonzero_elementary_ideals_differ"
    },
    {
      "from": "check_prime_symbolic_elementary_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_elementary_boundary",
      "to": "prime_symbolic_elementary_boundary_is_exact"
    },
    {
      "from": "check_prime_symbolic_elementary_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_elementary_boundary",
      "to": "python3"
    },
    {
      "from": "check_prime_symbolic_elementary_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_elementary_boundary",
      "to": "sympy"
    },
    {
      "from": "check_prime_symbolic_fox_exact",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_fox_exact",
      "to": "self::test_symbolic_presentations_are_sparse_exact_and_deterministic"
    },
    {
      "from": "check_prime_symbolic_fox_exact",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_fox_exact",
      "to": "prime_symbolic_fox_presentation_is_exact"
    },
    {
      "from": "check_prime_symbolic_fox_exact",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_fox_exact",
      "to": "python3"
    },
    {
      "from": "check_prime_symbolic_fox_exact",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_fox_exact",
      "to": "sympy"
    },
    {
      "from": "check_prime_symbolic_receipt_nonselecting",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_receipt_nonselecting",
      "to": "self::test_family_receipt_is_deterministic_and_bounded"
    },
    {
      "from": "check_prime_symbolic_receipt_nonselecting",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_receipt_nonselecting",
      "to": "prime_symbolic_alexander_receipt_is_nonselecting"
    },
    {
      "from": "check_prime_symbolic_receipt_nonselecting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_receipt_nonselecting",
      "to": "python3"
    },
    {
      "from": "check_prime_symbolic_receipt_nonselecting",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_symbolic_receipt_nonselecting",
      "to": "sympy"
    },
    {
      "from": "check_prime_two_cycle_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_prime_two_cycle_boundary",
      "to": "self::test_two_cycle_boundary_is_conditional"
    },
    {
      "from": "check_prime_two_cycle_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_prime_two_cycle_boundary",
      "to": "prime_two_cycle_boundary"
    },
    {
      "from": "check_prime_two_cycle_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_prime_two_cycle_boundary",
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
      "from": "check_root_loop_chart_all_initiations",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_all_initiations",
      "to": "self::test_all_fourteen_initiations_round_trip_without_evidence_loss"
    },
    {
      "from": "check_root_loop_chart_all_initiations",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_all_initiations",
      "to": "root_loop_chart_preserves_every_source_linked_initiation"
    },
    {
      "from": "check_root_loop_chart_all_initiations",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_all_initiations",
      "to": "python3"
    },
    {
      "from": "check_root_loop_chart_bounded_verdict",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_bounded_verdict",
      "to": "self::test_v07_report_supports_f12_only_on_bounded_domain_without_selection"
    },
    {
      "from": "check_root_loop_chart_bounded_verdict",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_bounded_verdict",
      "to": "root_loop_chart_support_is_bounded_and_nonselecting"
    },
    {
      "from": "check_root_loop_chart_bounded_verdict",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_bounded_verdict",
      "to": "python3"
    },
    {
      "from": "check_root_loop_chart_commutation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_commutation",
      "to": "self::test_chart_commutes_with_initiation_360_720_and_inverse"
    },
    {
      "from": "check_root_loop_chart_commutation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_commutation",
      "to": "root_loop_chart_commutes_with_bounded_motion"
    },
    {
      "from": "check_root_loop_chart_commutation",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_commutation",
      "to": "python3"
    },
    {
      "from": "check_root_loop_chart_sheet_hypothesis",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_sheet_hypothesis",
      "to": "self::test_sheet_correspondence_materializes_on_existing_cover_without_mutation"
    },
    {
      "from": "check_root_loop_chart_sheet_hypothesis",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_sheet_hypothesis",
      "to": "root_loop_chart_uses_cover_sheet_as_hypothesis_not_native_orientation"
    },
    {
      "from": "check_root_loop_chart_sheet_hypothesis",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_sheet_hypothesis",
      "to": "python3"
    },
    {
      "from": "check_root_loop_chart_two_way_inverse",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_two_way_inverse",
      "to": "self::test_chart_maps_are_exact_inverses_for_rational_root_loop_states"
    },
    {
      "from": "check_root_loop_chart_two_way_inverse",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_two_way_inverse",
      "to": "root_loop_chart_maps_are_exact_two_way_inverses"
    },
    {
      "from": "check_root_loop_chart_two_way_inverse",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_root_loop_chart_two_way_inverse",
      "to": "python3"
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
      "from": "check_source_coordinate_complete_ordered_address",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_complete_ordered_address",
      "to": "self::test_ordered_source_coordinate_uses_exact_complete_address"
    },
    {
      "from": "check_source_coordinate_complete_ordered_address",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_complete_ordered_address",
      "to": "source_coordinate_law_uses_complete_ordered_source_address"
    },
    {
      "from": "check_source_coordinate_complete_ordered_address",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_complete_ordered_address",
      "to": "python3"
    },
    {
      "from": "check_source_coordinate_exact_assignment",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_exact_assignment",
      "to": "self::test_source_coordinate_assignment_is_exact_and_reversible"
    },
    {
      "from": "check_source_coordinate_exact_assignment",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_exact_assignment",
      "to": "source_coordinate_assignment_applies_exact_candidate_reversibly"
    },
    {
      "from": "check_source_coordinate_exact_assignment",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_exact_assignment",
      "to": "python3"
    },
    {
      "from": "check_source_coordinate_negative_and_nonselection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_negative_and_nonselection",
      "to": "self::test_equal_content_is_separate_and_report_remains_nonselecting"
    },
    {
      "from": "check_source_coordinate_negative_and_nonselection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_negative_and_nonselection",
      "to": "source_coordinate_law_rejects_identity_shortcuts_and_nonselection"
    },
    {
      "from": "check_source_coordinate_negative_and_nonselection",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_negative_and_nonselection",
      "to": "python3"
    },
    {
      "from": "check_source_coordinate_prefix_requires_completion_binding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_prefix_requires_completion_binding",
      "to": "self::test_prefix_cannot_reuse_or_impersonate_complete_scope_binding"
    },
    {
      "from": "check_source_coordinate_prefix_requires_completion_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_prefix_requires_completion_binding",
      "to": "source_coordinate_law_uses_complete_ordered_source_address"
    },
    {
      "from": "check_source_coordinate_prefix_requires_completion_binding",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_prefix_requires_completion_binding",
      "to": "python3"
    },
    {
      "from": "check_source_coordinate_scope_injectivity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_scope_injectivity",
      "to": "self::test_ordered_source_coordinate_is_exact_and_scope_injective"
    },
    {
      "from": "check_source_coordinate_scope_injectivity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_scope_injectivity",
      "to": "source_coordinate_law_is_exact_and_scope_injective"
    },
    {
      "from": "check_source_coordinate_scope_injectivity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_scope_injectivity",
      "to": "python3"
    },
    {
      "from": "check_source_coordinate_total_outcomes",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_total_outcomes",
      "to": "self::test_trace_retains_total_ordered_outcomes_and_blockers"
    },
    {
      "from": "check_source_coordinate_total_outcomes",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_total_outcomes",
      "to": "source_coordinate_outcomes_are_total_exclusive_and_ordered"
    },
    {
      "from": "check_source_coordinate_total_outcomes",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_total_outcomes",
      "to": "python3"
    },
    {
      "from": "check_source_coordinate_upstream_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_upstream_identity",
      "to": "self::test_derivation_retains_exact_upstream_identity"
    },
    {
      "from": "check_source_coordinate_upstream_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_upstream_identity",
      "to": "source_coordinate_derivation_retains_exact_initiation_identity"
    },
    {
      "from": "check_source_coordinate_upstream_identity",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_source_coordinate_upstream_identity",
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
      "from": "check_transverse_envelope_convention_round_trip",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_convention_round_trip",
      "to": "self::test_local_and_global_descriptions_remain_reversible"
    },
    {
      "from": "check_transverse_envelope_convention_round_trip",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_convention_round_trip",
      "to": "transverse_envelope_maps_preserve_exact_rational_state"
    },
    {
      "from": "check_transverse_envelope_convention_round_trip",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_convention_round_trip",
      "to": "python3"
    },
    {
      "from": "check_transverse_envelope_cover_collision",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_cover_collision",
      "to": "self::test_distinct_transverse_values_collide_in_the_actual_cover"
    },
    {
      "from": "check_transverse_envelope_cover_collision",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_cover_collision",
      "to": "transverse_envelope_exposes_cover_nonembedding"
    },
    {
      "from": "check_transverse_envelope_cover_collision",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_cover_collision",
      "to": "python3"
    },
    {
      "from": "check_transverse_envelope_exact_round_trip",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_exact_round_trip",
      "to": "self::test_parametric_exact_rational_maps_and_motion"
    },
    {
      "from": "check_transverse_envelope_exact_round_trip",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_exact_round_trip",
      "to": "transverse_envelope_maps_preserve_exact_rational_state"
    },
    {
      "from": "check_transverse_envelope_exact_round_trip",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_exact_round_trip",
      "to": "python3"
    },
    {
      "from": "check_transverse_envelope_explicit_policy",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_explicit_policy",
      "to": "self::test_every_witness_retains_the_pinned_exact_policy"
    },
    {
      "from": "check_transverse_envelope_explicit_policy",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_explicit_policy",
      "to": "transverse_envelope_comparison_policy_is_explicit"
    },
    {
      "from": "check_transverse_envelope_explicit_policy",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_explicit_policy",
      "to": "python3"
    },
    {
      "from": "check_transverse_envelope_root_restriction",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_root_restriction",
      "to": "self::test_zero_sidecar_restricts_exactly_to_v07"
    },
    {
      "from": "check_transverse_envelope_root_restriction",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_root_restriction",
      "to": "transverse_envelope_restricts_exactly_to_v07_root_loop"
    },
    {
      "from": "check_transverse_envelope_root_restriction",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_root_restriction",
      "to": "python3"
    },
    {
      "from": "check_transverse_envelope_verdict_boundary",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_verdict_boundary",
      "to": "self::test_v09_report_keeps_transverse_cover_extension_inconclusive"
    },
    {
      "from": "check_transverse_envelope_verdict_boundary",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_verdict_boundary",
      "to": "transverse_envelope_does_not_extend_cover_verdicts"
    },
    {
      "from": "check_transverse_envelope_verdict_boundary",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_verdict_boundary",
      "to": "python3"
    },
    {
      "from": "check_transverse_envelope_witness_identities",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_witness_identities",
      "to": "self::test_report_rejects_count_preserving_identity_substitution"
    },
    {
      "from": "check_transverse_envelope_witness_identities",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_witness_identities",
      "to": "transverse_envelope_report_validates_complete_witness_identities"
    },
    {
      "from": "check_transverse_envelope_witness_identities",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_transverse_envelope_witness_identities",
      "to": "python3"
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
      "from": "check_ucns_ptcna_deterministic_receipt",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_ucns_ptcna_deterministic_receipt",
      "to": "self::test_receipt_is_byte_deterministic_and_provenance_bound"
    },
    {
      "from": "check_ucns_ptcna_deterministic_receipt",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_ucns_ptcna_deterministic_receipt",
      "to": "ucns_ptcna_receipt_is_deterministic_and_provenance_bound"
    },
    {
      "from": "check_ucns_ptcna_exact_shape",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_ucns_ptcna_exact_shape",
      "to": "self::test_receipt_has_exact_dense_shape_and_state_digest"
    },
    {
      "from": "check_ucns_ptcna_exact_shape",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_ucns_ptcna_exact_shape",
      "to": "ucns_ptcna_state_has_exact_requested_shape"
    },
    {
      "from": "check_ucns_ptcna_status_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_ucns_ptcna_status_firewall",
      "to": "self::test_receipt_preserves_candidate_and_nonclaim_boundaries"
    },
    {
      "from": "check_ucns_ptcna_status_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_ucns_ptcna_status_firewall",
      "to": "ucns_ptcna_candidate_transfers_no_status"
    },
    {
      "from": "check_ucns_ptcna_tamper_rejection",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_ucns_ptcna_tamper_rejection",
      "to": "self::test_every_tested_authority_tamper_is_rejected"
    },
    {
      "from": "check_ucns_ptcna_tamper_rejection",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_ucns_ptcna_tamper_rejection",
      "to": "ucns_ptcna_receipt_rejects_tampering"
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
      "from": "lexical_floor_layer_check",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_layer_check",
      "to": "self::test_projection_candidate_and_definition_boundaries"
    },
    {
      "from": "lexical_floor_layer_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_layer_check",
      "to": "affixiation_and_compounding_are_candidate_layers"
    },
    {
      "from": "lexical_floor_layer_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_layer_check",
      "to": "definitions_are_context_plural_and_immutable"
    },
    {
      "from": "lexical_floor_layer_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_layer_check",
      "to": "lexical_hyperspace_is_occurrence_preserving_projection_not_embedding"
    },
    {
      "from": "lexical_floor_snapshot_check",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_snapshot_check",
      "to": "self::test_snapshot_chain_is_source_bound_and_fail_closed"
    },
    {
      "from": "lexical_floor_snapshot_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_snapshot_check",
      "to": "every_added_layer_has_a_source_bound_snapshot"
    },
    {
      "from": "lexical_floor_source_and_word_check",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_source_and_word_check",
      "to": "self::test_source_word_and_glyph_boundaries"
    },
    {
      "from": "lexical_floor_source_and_word_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_source_and_word_check",
      "to": "lexical_floor_order_is_serialization_only"
    },
    {
      "from": "lexical_floor_source_and_word_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_source_and_word_check",
      "to": "lexical_floor_reuses_canonical_glyph_assignment"
    },
    {
      "from": "lexical_floor_source_and_word_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_source_and_word_check",
      "to": "lexical_floor_source_receipt_binds_packaged_bytes"
    },
    {
      "from": "lexical_floor_source_and_word_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "lexical_floor_source_and_word_check",
      "to": "lexical_floor_words_are_unique_exact_glyph_sets"
    },
    {
      "from": "relational_carrier_exact_boundary_check",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "relational_carrier_exact_boundary_check",
      "to": "self::test_relational_carrier_exact_boundary"
    },
    {
      "from": "relational_carrier_exact_boundary_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "relational_carrier_exact_boundary_check",
      "to": "relational_carrier_is_intrinsic_and_metadata_free"
    },
    {
      "from": "relational_carrier_exact_boundary_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "relational_carrier_exact_boundary_check",
      "to": "relational_carrier_preserves_order_multiplicity_and_sidedness"
    },
    {
      "from": "relational_carrier_exact_boundary_check",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "relational_carrier_exact_boundary_check",
      "to": "relational_carrier_roundtrip_is_canonical"
    },
    {
      "from": "addition_boundary",
      "kind": "calls",
      "source_block": "CONTRACTS",
      "source_id": "addition_boundary",
      "to": "contracts.test_addition_boundary.contract_addition_boundary"
    },
    {
      "from": "division_theory",
      "kind": "calls",
      "source_block": "CONTRACTS",
      "source_id": "division_theory",
      "to": "contracts.test_quotient_solvability.contract_division_theory"
    },
    {
      "from": "multiply_associativity",
      "kind": "calls",
      "source_block": "CONTRACTS",
      "source_id": "multiply_associativity",
      "to": "contracts.test_associativity_triples.contract_multiply_associativity"
    },
    {
      "from": "multiply_commutativity_ruling",
      "kind": "calls",
      "source_block": "CONTRACTS",
      "source_id": "multiply_commutativity_ruling",
      "to": "contracts.test_commutator.contract_multiply_commutativity_ruling"
    },
    {
      "from": "multiply_identity",
      "kind": "calls",
      "source_block": "CONTRACTS",
      "source_id": "multiply_identity",
      "to": "contracts.test_identity_two_sided.contract_multiply_identity"
    },
    {
      "from": "multiply_well_defined",
      "kind": "calls",
      "source_block": "CONTRACTS",
      "source_id": "multiply_well_defined",
      "to": "contracts.test_multiply_canonical.contract_multiply_well_defined"
    },
    {
      "from": "structure_naming",
      "kind": "calls",
      "source_block": "CONTRACTS",
      "source_id": "structure_naming",
      "to": "contracts.test_structure_axioms.contract_structure_naming"
    },
    {
      "from": "addition_boundary",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "addition_boundary",
      "to": "Erin Spencer"
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
      "from": "division_theory",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "division_theory",
      "to": "Erin Spencer"
    },
    {
      "from": "division_theory",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "division_theory",
      "to": "Erin Spencer"
    },
    {
      "from": "division_theory",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "division_theory",
      "to": "ucns_canonical"
    },
    {
      "from": "edcm_assignment_admission_boundary",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_assignment_admission_boundary",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_assignment_admission_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_assignment_admission_boundary",
      "to": "edcm_completion_motion_evidence"
    },
    {
      "from": "edcm_assignment_admission_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_assignment_admission_boundary",
      "to": "edcm_full_carrier_attachment_evidence"
    },
    {
      "from": "edcm_assignment_admission_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_assignment_admission_boundary",
      "to": "reproducible_witness_experiment_pipeline"
    },
    {
      "from": "edcm_carrier_coordinate_admissibility_experiment",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_carrier_coordinate_admissibility_experiment",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_carrier_coordinate_admissibility_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_carrier_coordinate_admissibility_experiment",
      "to": "directed_carrier_floor"
    },
    {
      "from": "edcm_carrier_coordinate_admissibility_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_carrier_coordinate_admissibility_experiment",
      "to": "edcm_exact_rational_transverse_envelope_experiment"
    },
    {
      "from": "edcm_carrier_coordinate_admissibility_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_carrier_coordinate_admissibility_experiment",
      "to": "explicit_comparison_policy_layer"
    },
    {
      "from": "edcm_completion_motion_evidence",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_completion_motion_evidence",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_exact_coordinate_representation_boundary",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_exact_coordinate_representation_boundary",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_exact_coordinate_representation_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_exact_coordinate_representation_boundary",
      "to": "directed_carrier_floor"
    },
    {
      "from": "edcm_exact_coordinate_representation_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_exact_coordinate_representation_boundary",
      "to": "edcm_carrier_coordinate_admissibility_experiment"
    },
    {
      "from": "edcm_exact_rational_transverse_envelope_experiment",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_exact_rational_transverse_envelope_experiment",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_exact_rational_transverse_envelope_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_exact_rational_transverse_envelope_experiment",
      "to": "edcm_native_direct_mobius_candidate"
    },
    {
      "from": "edcm_exact_rational_transverse_envelope_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_exact_rational_transverse_envelope_experiment",
      "to": "edcm_root_loop_cover_chart_candidate"
    },
    {
      "from": "edcm_exact_rational_transverse_envelope_experiment",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_exact_rational_transverse_envelope_experiment",
      "to": "explicit_comparison_policy_layer"
    },
    {
      "from": "edcm_explicit_geometric_assignment_boundary",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_explicit_geometric_assignment_boundary",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_explicit_geometric_assignment_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_explicit_geometric_assignment_boundary",
      "to": "edcm_exact_coordinate_representation_boundary"
    },
    {
      "from": "edcm_explicit_geometric_assignment_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_explicit_geometric_assignment_boundary",
      "to": "edcm_gonol_initiation_structural_null_boundary"
    },
    {
      "from": "edcm_external_evaluation_harness",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_external_evaluation_harness",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_external_evaluation_harness",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_external_evaluation_harness",
      "to": "edcm_full_corpus_execution_gate"
    },
    {
      "from": "edcm_external_evaluation_harness",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_external_evaluation_harness",
      "to": "skill_lib_boundary_runner"
    },
    {
      "from": "edcm_full_carrier_attachment_evidence",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_full_carrier_attachment_evidence",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_full_carrier_attachment_evidence",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_full_carrier_attachment_evidence",
      "to": "edcm_exact_coordinate_representation_boundary"
    },
    {
      "from": "edcm_full_carrier_attachment_evidence",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_full_carrier_attachment_evidence",
      "to": "edcm_partial_initiation_boundary"
    },
    {
      "from": "edcm_full_corpus_execution_gate",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_full_corpus_execution_gate",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_full_corpus_execution_gate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_full_corpus_execution_gate",
      "to": "edcm_word_gonol_profile"
    },
    {
      "from": "edcm_gonol_initiation_structural_null_boundary",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_gonol_initiation_structural_null_boundary",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_gonol_initiation_structural_null_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_gonol_initiation_structural_null_boundary",
      "to": "edcm_assignment_admission_boundary"
    },
    {
      "from": "edcm_gonol_initiation_structural_null_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_gonol_initiation_structural_null_boundary",
      "to": "edcm_partial_initiation_boundary"
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
      "from": "edcm_partial_initiation_boundary",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_partial_initiation_boundary",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_partial_initiation_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_partial_initiation_boundary",
      "to": "edcm_exact_coordinate_representation_boundary"
    },
    {
      "from": "edcm_partial_initiation_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_partial_initiation_boundary",
      "to": "edcm_native_direct_mobius_candidate"
    },
    {
      "from": "edcm_root_loop_cover_chart_candidate",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_root_loop_cover_chart_candidate",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_root_loop_cover_chart_candidate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_root_loop_cover_chart_candidate",
      "to": "directed_carrier_floor"
    },
    {
      "from": "edcm_root_loop_cover_chart_candidate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_root_loop_cover_chart_candidate",
      "to": "edcm_mobius_carrier_experiment"
    },
    {
      "from": "edcm_root_loop_cover_chart_candidate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_root_loop_cover_chart_candidate",
      "to": "edcm_native_direct_mobius_candidate"
    },
    {
      "from": "edcm_source_coordinate_derivation_boundary",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_source_coordinate_derivation_boundary",
      "to": "Erin Spencer"
    },
    {
      "from": "edcm_source_coordinate_derivation_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_source_coordinate_derivation_boundary",
      "to": "edcm_exact_coordinate_representation_boundary"
    },
    {
      "from": "edcm_source_coordinate_derivation_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_source_coordinate_derivation_boundary",
      "to": "edcm_explicit_geometric_assignment_boundary"
    },
    {
      "from": "edcm_source_coordinate_derivation_boundary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "edcm_source_coordinate_derivation_boundary",
      "to": "edcm_gonol_initiation_structural_null_boundary"
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
      "to": "edcm_assignment_admission_boundary"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_carrier_coordinate_admissibility_experiment"
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
      "to": "edcm_exact_coordinate_representation_boundary"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_exact_rational_transverse_envelope_experiment"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_explicit_geometric_assignment_boundary"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_full_carrier_attachment_evidence"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_full_corpus_execution_gate"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_gonol_initiation_structural_null_boundary"
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
      "to": "edcm_partial_initiation_boundary"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_root_loop_cover_chart_candidate"
    },
    {
      "from": "foundations_public_surface",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "foundations_public_surface",
      "to": "edcm_source_coordinate_derivation_boundary"
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
      "from": "local_groups_relational_geometry_contracts",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "local_groups_relational_geometry_contracts",
      "to": "Erin Spencer"
    },
    {
      "from": "local_groups_relational_geometry_contracts",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "local_groups_relational_geometry_contracts",
      "to": "ucns_canonical"
    },
    {
      "from": "local_groups_relational_geometry_contracts",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "local_groups_relational_geometry_contracts",
      "to": "ucns_relational_geometry"
    },
    {
      "from": "multiply_associativity",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "multiply_associativity",
      "to": "Erin Spencer"
    },
    {
      "from": "multiply_commutativity_ruling",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "multiply_commutativity_ruling",
      "to": "Erin Spencer"
    },
    {
      "from": "multiply_identity",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "multiply_identity",
      "to": "Erin Spencer"
    },
    {
      "from": "multiply_well_defined",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "multiply_well_defined",
      "to": "Erin Spencer"
    },
    {
      "from": "ngsl_lexical_floor",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ngsl_lexical_floor",
      "to": "Erin Spencer"
    },
    {
      "from": "prime_relational_reconstruction_independent_replay",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "prime_relational_reconstruction_independent_replay",
      "to": "Erin Spencer"
    },
    {
      "from": "prime_relational_reconstruction_independent_replay",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "prime_relational_reconstruction_independent_replay",
      "to": "ucns_prime_relational_reconstruction_adversary"
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
      "from": "skill_lib_boundary_runner",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "skill_lib_boundary_runner",
      "to": "Erin Spencer"
    },
    {
      "from": "skill_lib_boundary_runner",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "skill_lib_boundary_runner",
      "to": "skill_lib_contract_audit"
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
      "from": "structure_naming",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "structure_naming",
      "to": "Erin Spencer"
    },
    {
      "from": "structure_naming",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "structure_naming",
      "to": "division_theory"
    },
    {
      "from": "structure_naming",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "structure_naming",
      "to": "multiply_associativity"
    },
    {
      "from": "structure_naming",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "structure_naming",
      "to": "multiply_commutativity_ruling"
    },
    {
      "from": "structure_naming",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "structure_naming",
      "to": "multiply_identity"
    },
    {
      "from": "structure_naming",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "structure_naming",
      "to": "multiply_well_defined"
    },
    {
      "from": "ucns_a0_safe",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_a0_safe",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_a0_safe",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_a0_safe",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_a0_safe",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_a0_safe",
      "to": "ucns_factorization_result"
    },
    {
      "from": "ucns_a0_safe",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_a0_safe",
      "to": "ucns_object_record"
    },
    {
      "from": "ucns_a0_safe",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_a0_safe",
      "to": "ucns_serialization"
    },
    {
      "from": "ucns_bridge",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_bridge",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_bridge",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_bridge",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_bridge",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_bridge",
      "to": "ucns_serialization"
    },
    {
      "from": "ucns_canonical",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_canonical",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_canonical",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_canonical",
      "to": "none"
    },
    {
      "from": "ucns_canonical_factor_selection",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_canonical_factor_selection",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_canonical_factor_selection",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_canonical_factor_selection",
      "to": "ucns_carrier_support_pruning"
    },
    {
      "from": "ucns_carrier_support_pruning",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_carrier_support_pruning",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_carrier_support_pruning",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_carrier_support_pruning",
      "to": "none"
    },
    {
      "from": "ucns_catalogue",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_catalogue",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_catalogue",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue",
      "to": "ucns_domains"
    },
    {
      "from": "ucns_catalogue_coverage",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue_coverage",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_catalogue_coverage",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue_coverage",
      "to": "ucns_domains"
    },
    {
      "from": "ucns_catalogue_coverage",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue_coverage",
      "to": "ucns_factor_search_v08"
    },
    {
      "from": "ucns_catalogue_coverage",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue_coverage",
      "to": "ucns_serialization"
    },
    {
      "from": "ucns_catalogue_d3",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue_d3",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_catalogue_d3",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue_d3",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_catalogue_d3",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue_d3",
      "to": "ucns_catalogue"
    },
    {
      "from": "ucns_catalogue_d3",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_catalogue_d3",
      "to": "ucns_domains"
    },
    {
      "from": "ucns_codec",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_codec",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_codec",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_codec",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_core",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_core",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_core",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_core",
      "to": "none"
    },
    {
      "from": "ucns_domain_status",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_domain_status",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_domain_status",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_domain_status",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_domains",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_domains",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_domains",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_domains",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_embedding",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_embedding",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_embedding",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_embedding",
      "to": "ucns_epicycle"
    },
    {
      "from": "ucns_epicycle",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_epicycle",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_epicycle",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_epicycle",
      "to": "none"
    },
    {
      "from": "ucns_evidence",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_evidence",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence",
      "to": "ucns_bridge"
    },
    {
      "from": "ucns_evidence",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_evidence",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence",
      "to": "ucns_domain_status"
    },
    {
      "from": "ucns_evidence",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence",
      "to": "ucns_factorization_result"
    },
    {
      "from": "ucns_evidence_envelope",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence_envelope",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_evidence_envelope",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence_envelope",
      "to": "ucns_domain_status"
    },
    {
      "from": "ucns_evidence_envelope",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence_envelope",
      "to": "ucns_factorization_result"
    },
    {
      "from": "ucns_evidence_envelope",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence_envelope",
      "to": "ucns_object_record"
    },
    {
      "from": "ucns_evidence_envelope",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_evidence_envelope",
      "to": "ucns_serialization"
    },
    {
      "from": "ucns_factor_search_v08",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factor_search_v08",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_factor_search_v08",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factor_search_v08",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_factor_search_v08",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factor_search_v08",
      "to": "ucns_carrier_support_pruning"
    },
    {
      "from": "ucns_factor_search_v08",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factor_search_v08",
      "to": "ucns_domains"
    },
    {
      "from": "ucns_factor_search_v08",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factor_search_v08",
      "to": "ucns_host_recovery"
    },
    {
      "from": "ucns_factor_search_v08",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factor_search_v08",
      "to": "ucns_payload_system"
    },
    {
      "from": "ucns_factor_search_v08",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factor_search_v08",
      "to": "ucns_serialization"
    },
    {
      "from": "ucns_factor_search_v08",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factor_search_v08",
      "to": "ucns_witness_matrix"
    },
    {
      "from": "ucns_factorization_result",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factorization_result",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_factorization_result",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factorization_result",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_factorization_result",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factorization_result",
      "to": "ucns_carrier_support_pruning"
    },
    {
      "from": "ucns_factorization_result",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factorization_result",
      "to": "ucns_catalogue_coverage"
    },
    {
      "from": "ucns_factorization_result",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factorization_result",
      "to": "ucns_domain_status"
    },
    {
      "from": "ucns_factorization_result",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factorization_result",
      "to": "ucns_domains"
    },
    {
      "from": "ucns_factorization_result",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factorization_result",
      "to": "ucns_factor_search_v08"
    },
    {
      "from": "ucns_factorization_result",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_factorization_result",
      "to": "ucns_serialization"
    },
    {
      "from": "ucns_geometry_bridge",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_geometry_bridge",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_geometry_bridge",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_geometry_bridge",
      "to": "ucns.canonical"
    },
    {
      "from": "ucns_geometry_bridge",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_geometry_bridge",
      "to": "ucns.relational_geometry"
    },
    {
      "from": "ucns_host_recovery",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_host_recovery",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_host_recovery",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_host_recovery",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_left_quotient",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_left_quotient",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_left_quotient",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_left_quotient",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_mobius",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_mobius",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius",
      "to": "none"
    },
    {
      "from": "ucns_mobius_seed_global_compatibility",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_seed_global_compatibility",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_mobius_seed_global_compatibility",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_seed_global_compatibility",
      "to": "ucns_mobius_seed_of_life_candidate"
    },
    {
      "from": "ucns_mobius_seed_global_compatibility",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_seed_global_compatibility",
      "to": "ucns_mobius_vesica_continuation"
    },
    {
      "from": "ucns_mobius_seed_of_life_candidate",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_seed_of_life_candidate",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_mobius_seed_of_life_candidate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_seed_of_life_candidate",
      "to": "edcm_native_direct_mobius_candidate"
    },
    {
      "from": "ucns_mobius_seed_of_life_candidate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_seed_of_life_candidate",
      "to": "ucns_gonol_relationship_display_v1"
    },
    {
      "from": "ucns_mobius_vesica_certificates",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_vesica_certificates",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_mobius_vesica_certificates",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_vesica_certificates",
      "to": "ucns_mobius_vesica_exact_embedding"
    },
    {
      "from": "ucns_mobius_vesica_continuation",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_vesica_continuation",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_mobius_vesica_continuation",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_vesica_continuation",
      "to": "ucns_mobius_seed_of_life_candidate"
    },
    {
      "from": "ucns_mobius_vesica_continuation",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_vesica_continuation",
      "to": "ucns_mobius_vesica_certificates"
    },
    {
      "from": "ucns_mobius_vesica_exact_embedding",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_vesica_exact_embedding",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_mobius_vesica_exact_embedding",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mobius_vesica_exact_embedding",
      "to": "ucns_mobius_seed_of_life_candidate"
    },
    {
      "from": "ucns_mpfr_interval",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mpfr_interval",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_mpfr_interval",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_mpfr_interval",
      "to": "system libmpfr"
    },
    {
      "from": "ucns_native_cache",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_native_cache",
      "to": "Erin Spencer / Codex"
    },
    {
      "from": "ucns_object_record",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_object_record",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_object_record",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_object_record",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_object_record",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_object_record",
      "to": "ucns_domain_status"
    },
    {
      "from": "ucns_object_record",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_object_record",
      "to": "ucns_domains"
    },
    {
      "from": "ucns_object_record",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_object_record",
      "to": "ucns_serialization"
    },
    {
      "from": "ucns_option_decision_registry",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_option_decision_registry",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_payload_system",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_payload_system",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_payload_system",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_payload_system",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_prime_boundary_link_invariants",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_boundary_link_invariants",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_boundary_link_invariants",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_boundary_link_invariants",
      "to": "ucns_prime_interval_boundary_links_p7_p5"
    },
    {
      "from": "ucns_prime_determinantal_grobner_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_determinantal_grobner_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_determinantal_grobner_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_determinantal_grobner_p7_p5",
      "to": "sympy==1.14.0"
    },
    {
      "from": "ucns_prime_determinantal_grobner_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_determinantal_grobner_p7_p5",
      "to": "ucns_prime_symbolic_alexander_p7_p5"
    },
    {
      "from": "ucns_prime_exact_milnor_alexander_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_exact_milnor_alexander_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_exact_milnor_alexander_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_exact_milnor_alexander_p7_p5",
      "to": "mpmath>=1.3"
    },
    {
      "from": "ucns_prime_exact_milnor_alexander_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_exact_milnor_alexander_p7_p5",
      "to": "ucns_prime_independent_phase_milnor_p7_p5"
    },
    {
      "from": "ucns_prime_generic_diagram",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_generic_diagram",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_generic_diagram",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_generic_diagram",
      "to": "ucns_prime_interval_boundary_links_p7_p5"
    },
    {
      "from": "ucns_prime_generic_interval_certificate",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_generic_interval_certificate",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_generic_interval_certificate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_generic_interval_certificate",
      "to": "ucns_mpfr_interval"
    },
    {
      "from": "ucns_prime_generic_interval_certificate",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_generic_interval_certificate",
      "to": "ucns_prime_exact_milnor_alexander_p7_p5"
    },
    {
      "from": "ucns_prime_independent_phase_milnor",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_independent_phase_milnor",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_independent_phase_milnor",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_independent_phase_milnor",
      "to": "ucns_mpfr_interval"
    },
    {
      "from": "ucns_prime_independent_phase_milnor",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_independent_phase_milnor",
      "to": "ucns_prime_smooth_ribbons_p7_p5"
    },
    {
      "from": "ucns_prime_interval_boundaries_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_boundaries_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_interval_boundaries_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_boundaries_p7_p5",
      "to": "mpmath>=1.3"
    },
    {
      "from": "ucns_prime_interval_boundaries_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_boundaries_p7_p5",
      "to": "ucns_prime_smooth_ribbons_p7_p5"
    },
    {
      "from": "ucns_prime_interval_boundary_links_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_boundary_links_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_interval_boundary_links_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_boundary_links_p7_p5",
      "to": "ucns_prime_smooth_ribbons_p7_p5"
    },
    {
      "from": "ucns_prime_interval_common",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_common",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_interval_common",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_common",
      "to": "ucns_prime_smooth_ribbons_p7_p5"
    },
    {
      "from": "ucns_prime_interval_replay",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_replay",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_interval_replay",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_interval_replay",
      "to": "ucns_prime_interval_common"
    },
    {
      "from": "ucns_prime_length4_milnor_p7",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_length4_milnor_p7",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_length4_milnor_p7",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_length4_milnor_p7",
      "to": "ucns_prime_exact_milnor_alexander_p7_p5"
    },
    {
      "from": "ucns_prime_milnor_invariants",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_milnor_invariants",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_milnor_invariants",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_milnor_invariants",
      "to": "ucns_prime_generic_diagram"
    },
    {
      "from": "ucns_prime_nilpotent_discriminator_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_nilpotent_discriminator_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_nilpotent_discriminator_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_nilpotent_discriminator_p7_p5",
      "to": "GAP 4.12.1"
    },
    {
      "from": "ucns_prime_nilpotent_discriminator_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_nilpotent_discriminator_p7_p5",
      "to": "NQ 2.5.11"
    },
    {
      "from": "ucns_prime_nilpotent_discriminator_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_nilpotent_discriminator_p7_p5",
      "to": "ucns_prime_exact_milnor_alexander_p7_p5"
    },
    {
      "from": "ucns_prime_phase_lift_data",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_phase_lift_data",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_phase_lift_data",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_phase_lift_data",
      "to": "ucns_prime_primitives_p7_p5"
    },
    {
      "from": "ucns_prime_phase_lift_model",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_phase_lift_model",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_phase_lift_model",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_phase_lift_model",
      "to": "ucns_prime_phase_lift_data"
    },
    {
      "from": "ucns_prime_phase_lift_model",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_phase_lift_model",
      "to": "ucns_prime_primitives_p7_p5"
    },
    {
      "from": "ucns_prime_phase_lift_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_phase_lift_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_phase_lift_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_phase_lift_p7_p5",
      "to": "ucns_prime_primitives_p7_p5"
    },
    {
      "from": "ucns_prime_primitives_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_primitives_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_primitives_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_primitives_p7_p5",
      "to": "none"
    },
    {
      "from": "ucns_prime_relational_reconstruction_adversary",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_relational_reconstruction_adversary",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_relational_reconstruction_adversary",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_relational_reconstruction_adversary",
      "to": "edcm_external_evaluation_harness"
    },
    {
      "from": "ucns_prime_replay_phase_milnor_data",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_replay_phase_milnor_data",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_replay_phase_milnor_data",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_replay_phase_milnor_data",
      "to": "ucns_prime_smooth_ribbons_p7_p5"
    },
    {
      "from": "ucns_prime_replay_phase_milnor_receipt",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_replay_phase_milnor_receipt",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_replay_phase_milnor_receipt",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_replay_phase_milnor_receipt",
      "to": "ucns_prime_smooth_ribbons_p7_p5"
    },
    {
      "from": "ucns_prime_smooth_ribbons_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_smooth_ribbons_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_smooth_ribbons_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_smooth_ribbons_p7_p5",
      "to": "ucns_prime_phase_lift_p7_p5"
    },
    {
      "from": "ucns_prime_symbolic_alexander_p7_p5",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_symbolic_alexander_p7_p5",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_prime_symbolic_alexander_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_symbolic_alexander_p7_p5",
      "to": "<2"
    },
    {
      "from": "ucns_prime_symbolic_alexander_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_symbolic_alexander_p7_p5",
      "to": "sympy>=1.12"
    },
    {
      "from": "ucns_prime_symbolic_alexander_p7_p5",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_prime_symbolic_alexander_p7_p5",
      "to": "ucns_prime_exact_milnor_alexander_p7_p5"
    },
    {
      "from": "ucns_ptcna_candidate_state",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_ptcna_candidate_state",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_ptcna_candidate_state",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_ptcna_candidate_state",
      "to": "edcm_word_gonol_profile"
    },
    {
      "from": "ucns_public_gonol",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_public_gonol",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol",
      "to": "none"
    },
    {
      "from": "ucns_public_gonol_faces",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_faces",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_public_gonol_faces",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_faces",
      "to": "ucns_public_gonol"
    },
    {
      "from": "ucns_public_gonol_lifted_path",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_lifted_path",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_public_gonol_lifted_path",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_lifted_path",
      "to": "ucns_public_gonol"
    },
    {
      "from": "ucns_public_gonol_lifted_path",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_lifted_path",
      "to": "ucns_public_gonol_faces"
    },
    {
      "from": "ucns_public_gonol_mirror",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_mirror",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_public_gonol_mirror",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_mirror",
      "to": "ucns_public_gonol"
    },
    {
      "from": "ucns_public_gonol_private",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_private",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_public_gonol_private",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_private",
      "to": "ucns_public_gonol"
    },
    {
      "from": "ucns_public_gonol_private",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_public_gonol_private",
      "to": "ucns_public_gonol_faces"
    },
    {
      "from": "ucns_quotient",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_quotient",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_quotient",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_quotient",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_quotient",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_quotient",
      "to": "ucns_left_quotient"
    },
    {
      "from": "ucns_relational_carrier",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_relational_carrier",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_relational_carrier",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_relational_carrier",
      "to": "none"
    },
    {
      "from": "ucns_relational_geometry",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_relational_geometry",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_relational_geometry",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_relational_geometry",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_serialization",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_serialization",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_serialization",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_serialization",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_similarity",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_similarity",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_similarity",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_similarity",
      "to": "none"
    },
    {
      "from": "ucns_store",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_store",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_store",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_store",
      "to": "ucns_canonical"
    },
    {
      "from": "ucns_store",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_store",
      "to": "ucns_codec"
    },
    {
      "from": "ucns_store",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_store",
      "to": "ucns_domains"
    },
    {
      "from": "ucns_store",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_store",
      "to": "ucns_left_quotient"
    },
    {
      "from": "ucns_witness_matrix",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_witness_matrix",
      "to": "Erin Spencer"
    },
    {
      "from": "ucns_witness_matrix",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "ucns_witness_matrix",
      "to": "ucns_canonical"
    }
  ],
  "gaps": [],
  "repo": "The-Interdependency/ucns"
});
