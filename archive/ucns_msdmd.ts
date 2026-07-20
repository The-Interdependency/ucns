import { defineMsdmdCollection } from "./.agents/skills/msdmd/collection";

export default defineMsdmdCollection({
  "declarations": [
    {
      "block": "LLMS",
      "fields": {
        "content": "- Skills live as root directories with SKILL.md files and optional helpers."
      },
      "file": ".tmp-skill-lib/llms/metadata.py",
      "id": "architecture_summary"
    },
    {
      "block": "LLMS",
      "fields": {
        "msdmd": "Module Self-Declared Metadata in Markdown \u2014 the foundational convention where each source module declares its own structured metadata in a fenced comment block."
      },
      "file": ".tmp-skill-lib/llms/metadata.py",
      "id": "key_definitions"
    },
    {
      "block": "LLMS",
      "fields": {
        "content": "skill-lib is the canonical organization-wide source for reusable agent skills in The Interdependency."
      },
      "file": ".tmp-skill-lib/llms/metadata.py",
      "id": "project_overview"
    },
    {
      "block": "LLMS",
      "fields": {
        "content": "- Read AGENTS.md, skills.json, and the relevant skill file before changing a skill."
      },
      "file": ".tmp-skill-lib/llms/metadata.py",
      "id": "usage_rules"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "`loto clear` on a scar",
        "then": "refused on dirty tree; on clean tree produces a commit touching zero files, carrying scar trailers, and deletes the scar"
      },
      "file": ".tmp-skill-lib/skill_lib/safety/repo_loto.py",
      "id": "loto_clear_is_empty_commit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "one in-scope mutation commit and passing test evidence; `loto close`",
        "then": ".loto/ is empty and HEAD carries Loto-* trailers; git is the only archive"
      },
      "file": ".tmp-skill-lib/skill_lib/safety/repo_loto.py",
      "id": "loto_close_deletes_tag"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "a failing run of a test command followed by a passing run of the identical command",
        "then": "close proceeds; a distinct command whose latest run failed still blocks close"
      },
      "file": ".tmp-skill-lib/skill_lib/safety/repo_loto.py",
      "id": "loto_latest_test_wins"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "more than one commit between base and HEAD at close",
        "then": "close refuses (v0.1 invariant: one session, one mutation commit)"
      },
      "file": ".tmp-skill-lib/skill_lib/safety/repo_loto.py",
      "id": "loto_one_commit_per_session"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "doctrine",
        "given": "clean working tree; `loto open` succeeds",
        "then": "working tree is still clean; exclusion went to .git/info/exclude, never .gitignore"
      },
      "file": ".tmp-skill-lib/skill_lib/safety/repo_loto.py",
      "id": "loto_open_never_dirties"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an unacknowledged SCAR-*.json in .loto/",
        "then": "`loto open` refuses and `loto guard` exits nonzero"
      },
      "file": ".tmp-skill-lib/skill_lib/safety/repo_loto.py",
      "id": "loto_scar_blocks_work"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "files touched outside the declared --files globs",
        "then": "close refuses with the violating paths named"
      },
      "file": ".tmp-skill-lib/skill_lib/safety/repo_loto.py",
      "id": "loto_scope_enforced"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_load, _save, _touched_files, _scope_violations, _trailers, _digest, _commit, _git, _ensure_gitignored",
        "module_kind": "instrument",
        "module_name": "repo_loto",
        "network_boundary": "none",
        "owner": "Way Seer Erin",
        "public_surface": "loto open, loto run, loto test, loto close, loto fail, loto clear, loto status, loto guard, loto install-hook",
        "rollback": "rm -rf .loto/ and remove hook line",
        "rollout": "manual invocation; pre-push hook calls `loto guard`",
        "storage_boundary": "write",
        "summary": "delete-on-completion session gate for repo mutation; presence of state means open work, absence means clean",
        "tests": "tests/test_repo_loto.py (CHECKS-declared, reconciled via --audit)",
        "unresolved": "credential-gate integration, ratios bookends",
        "user_data_boundary": "none"
      },
      "file": ".tmp-skill-lib/skill_lib/safety/repo_loto.py",
      "id": "repo_mutation_gate"
    },
    {
      "block": "DOCS",
      "fields": {
        "source": "docs/module.md",
        "status": "current",
        "summary": "module docs"
      },
      "file": ".tmp-skill-lib/tests/test_collect.py",
      "id": "module_docs"
    },
    {
      "block": "LLMS",
      "fields": {
        "content": "example only"
      },
      "file": ".tmp-skill-lib/tests/test_llms_build.py",
      "id": "project_overview"
    },
    {
      "block": "LLMS",
      "fields": {
        "content": "real declaration"
      },
      "file": ".tmp-skill-lib/tests/test_llms_build.py",
      "id": "project_overview"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_clear_is_empty_commit",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "loto_clear_is_empty_commit",
        "requires": "git, python3, posix_shell",
        "timeout": "20"
      },
      "file": ".tmp-skill-lib/tests/test_repo_loto.py",
      "id": "check_clear_is_empty_commit"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_close_deletes_tag",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "loto_close_deletes_tag",
        "requires": "git, python3, posix_shell",
        "timeout": "20"
      },
      "file": ".tmp-skill-lib/tests/test_repo_loto.py",
      "id": "check_close_deletes_tag"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_latest_test_wins",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "loto_latest_test_wins",
        "requires": "git, python3, posix_shell",
        "timeout": "20"
      },
      "file": ".tmp-skill-lib/tests/test_repo_loto.py",
      "id": "check_latest_test_wins"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_one_commit_per_session",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "loto_one_commit_per_session",
        "requires": "git, python3, posix_shell",
        "timeout": "20"
      },
      "file": ".tmp-skill-lib/tests/test_repo_loto.py",
      "id": "check_one_commit_per_session"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_open_never_dirties",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "loto_open_never_dirties",
        "requires": "git, python3, posix_shell",
        "timeout": "20"
      },
      "file": ".tmp-skill-lib/tests/test_repo_loto.py",
      "id": "check_open_never_dirties"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_scar_blocks_work",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "loto_scar_blocks_work",
        "requires": "git, python3, posix_shell",
        "timeout": "20"
      },
      "file": ".tmp-skill-lib/tests/test_repo_loto.py",
      "id": "check_scar_blocks_work"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_scope_enforced",
        "cleanup": "tempdir_teardown",
        "mutates": "filesystem",
        "proves": "loto_scope_enforced",
        "requires": "git, python3, posix_shell",
        "timeout": "20"
      },
      "file": ".tmp-skill-lib/tests/test_repo_loto.py",
      "id": "check_scope_enforced"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "internal_surface": "_mk_repo, _run, _loto, _parse_block, _resolve_call, _requires_met",
        "module_kind": "checks",
        "module_name": "test_repo_loto",
        "owner": "Way Seer Erin",
        "public_surface": "test_* functions, main, --audit",
        "summary": "evidentiary procedures for repo_loto CONTRACTS; standalone or pytest; --audit reconciles the declared graph without execution",
        "tests": "self",
        "unresolved": "mutation-level verification that checks actually exercise their contracts"
      },
      "file": ".tmp-skill-lib/tests/test_repo_loto.py",
      "id": "repo_loto_evidence"
    },
    {
      "block": "DOCS",
      "fields": {
        "summary": "second"
      },
      "file": ".tmp-skill-lib/tests/test_universal_parser.py",
      "id": "second_docs"
    },
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
      "file": "contracts/test_addition_boundary.py",
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
      "file": "contracts/test_associativity_triples.py",
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
      "file": "contracts/test_commutator.py",
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
      "file": "contracts/test_identity_two_sided.py",
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
      "file": "contracts/test_local_groups_and_geometry.py",
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
      "file": "contracts/test_multiply_canonical.py",
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
      "file": "contracts/test_quotient_solvability.py",
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
      "file": "contracts/test_structure_axioms.py",
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
      "file": "ucns/a0_safe.py",
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
      "file": "ucns/bridge.py",
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
      "file": "ucns/canonical.py",
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
      "file": "ucns/canonical.py",
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
      "file": "ucns/canonical.py",
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
      "file": "ucns/canonical.py",
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
      "file": "ucns/canonical.py",
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
      "file": "ucns/canonical.py",
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
      "file": "ucns/canonical.py",
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
      "file": "ucns/canonical_factorization.py",
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
      "file": "ucns/catalogue.py",
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
      "file": "ucns/catalogue_coverage.py",
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
      "file": "ucns/catalogue_d3.py",
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
      "file": "ucns/catalogue_pruning.py",
      "id": "ucns_carrier_support_pruning"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "engine",
        "module_name": "core",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "UCN, TAU",
        "requires": "none",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Defines UCN, the fundamental angle-on-unit-circle numeric primitive with group arithmetic, similarity, and compact serialization.",
        "tests": "tests.test_core",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "ucns/core.py",
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
      "file": "ucns/division_theory.py",
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
      "file": "ucns/division_theory.py",
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
      "file": "ucns/domain_status.py",
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
      "file": "ucns/domains.py",
      "id": "ucns_domains"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_to_signal",
        "module_kind": "engine",
        "module_name": "embedding",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "UCNEmbedding",
        "requires": "ucns_epicycle",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "High-level UCNS embedding API that encodes data to unit-circle phase vectors via epicycle/FFT decomposition and compares them.",
        "tests": "tests.test_embedding",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "ucns/embedding.py",
      "id": "ucns_embedding"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_next_pow2, _fft_inplace",
        "module_kind": "engine",
        "module_name": "epicycle",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "fft, ifft, EpicycleDecomposition",
        "requires": "none",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Pure-Python radix-2 FFT plus EpicycleDecomposition, representing signals as weighted unit-circle rotations for phase fingerprints.",
        "tests": "tests.test_epicycle",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "ucns/epicycle.py",
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
      "file": "ucns/evidence.py",
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
      "file": "ucns/evidence_envelope.py",
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
      "file": "ucns/factor_search_v08.py",
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
      "file": "ucns/factorization_result.py",
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
      "file": "ucns/geometry_bridge.py",
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
      "file": "ucns/host_recovery.py",
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
      "file": "ucns/left_quotient.py",
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
      "file": "ucns/mobius.py",
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
      "file": "ucns/object_record.py",
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
      "file": "ucns/payload_system.py",
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
      "file": "ucns/public_gonol.py",
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
      "file": "ucns/public_gonol_faces.py",
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
      "file": "ucns/public_gonol_lifted_path.py",
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
      "file": "ucns/public_gonol_mirror.py",
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
      "file": "ucns/public_gonol_private.py",
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
      "file": "ucns/recursive_codec.py",
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
      "file": "ucns/recursive_quotient.py",
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
      "file": "ucns/relational_geometry.py",
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
      "file": "ucns/serialization.py",
      "id": "ucns_serialization"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_check_same_length",
        "module_kind": "engine",
        "module_name": "similarity",
        "network_boundary": "none",
        "owner": "Erin Spencer",
        "public_surface": "phase_cosine, arc_distance, hyperbolic_cosine, top_k_overlap",
        "requires": "none",
        "rollback": "remove module and its re-exports",
        "rollout": "default_enabled",
        "since": "2026-06-02",
        "storage_boundary": "none",
        "summary": "Similarity and distance metrics (phase-cosine, arc, hyperbolic, top-k overlap) over UCNS angle-list embeddings.",
        "tests": "tests.test_similarity",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "ucns/similarity.py",
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
      "file": "ucns/store.py",
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
      "file": "ucns/witness_matrix.py",
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
      "file": "ucns_cache/entries.py",
      "id": "ucns_native_cache"
    }
  ],
  "edges": [
    {
      "from": "check_clear_is_empty_commit",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_clear_is_empty_commit",
      "to": "self::test_clear_is_empty_commit"
    },
    {
      "from": "check_clear_is_empty_commit",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_clear_is_empty_commit",
      "to": "loto_clear_is_empty_commit"
    },
    {
      "from": "check_clear_is_empty_commit",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_clear_is_empty_commit",
      "to": "git"
    },
    {
      "from": "check_clear_is_empty_commit",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_clear_is_empty_commit",
      "to": "posix_shell"
    },
    {
      "from": "check_clear_is_empty_commit",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_clear_is_empty_commit",
      "to": "python3"
    },
    {
      "from": "check_close_deletes_tag",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_close_deletes_tag",
      "to": "self::test_close_deletes_tag"
    },
    {
      "from": "check_close_deletes_tag",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_close_deletes_tag",
      "to": "loto_close_deletes_tag"
    },
    {
      "from": "check_close_deletes_tag",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_close_deletes_tag",
      "to": "git"
    },
    {
      "from": "check_close_deletes_tag",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_close_deletes_tag",
      "to": "posix_shell"
    },
    {
      "from": "check_close_deletes_tag",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_close_deletes_tag",
      "to": "python3"
    },
    {
      "from": "check_latest_test_wins",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_latest_test_wins",
      "to": "self::test_latest_test_wins"
    },
    {
      "from": "check_latest_test_wins",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_latest_test_wins",
      "to": "loto_latest_test_wins"
    },
    {
      "from": "check_latest_test_wins",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_latest_test_wins",
      "to": "git"
    },
    {
      "from": "check_latest_test_wins",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_latest_test_wins",
      "to": "posix_shell"
    },
    {
      "from": "check_latest_test_wins",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_latest_test_wins",
      "to": "python3"
    },
    {
      "from": "check_one_commit_per_session",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_one_commit_per_session",
      "to": "self::test_one_commit_per_session"
    },
    {
      "from": "check_one_commit_per_session",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_one_commit_per_session",
      "to": "loto_one_commit_per_session"
    },
    {
      "from": "check_one_commit_per_session",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_one_commit_per_session",
      "to": "git"
    },
    {
      "from": "check_one_commit_per_session",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_one_commit_per_session",
      "to": "posix_shell"
    },
    {
      "from": "check_one_commit_per_session",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_one_commit_per_session",
      "to": "python3"
    },
    {
      "from": "check_open_never_dirties",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_open_never_dirties",
      "to": "self::test_open_never_dirties"
    },
    {
      "from": "check_open_never_dirties",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_open_never_dirties",
      "to": "loto_open_never_dirties"
    },
    {
      "from": "check_open_never_dirties",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_open_never_dirties",
      "to": "git"
    },
    {
      "from": "check_open_never_dirties",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_open_never_dirties",
      "to": "posix_shell"
    },
    {
      "from": "check_open_never_dirties",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_open_never_dirties",
      "to": "python3"
    },
    {
      "from": "check_scar_blocks_work",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_scar_blocks_work",
      "to": "self::test_scar_blocks_work"
    },
    {
      "from": "check_scar_blocks_work",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_scar_blocks_work",
      "to": "loto_scar_blocks_work"
    },
    {
      "from": "check_scar_blocks_work",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_scar_blocks_work",
      "to": "git"
    },
    {
      "from": "check_scar_blocks_work",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_scar_blocks_work",
      "to": "posix_shell"
    },
    {
      "from": "check_scar_blocks_work",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_scar_blocks_work",
      "to": "python3"
    },
    {
      "from": "check_scope_enforced",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_scope_enforced",
      "to": "self::test_scope_enforced"
    },
    {
      "from": "check_scope_enforced",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_scope_enforced",
      "to": "loto_scope_enforced"
    },
    {
      "from": "check_scope_enforced",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_scope_enforced",
      "to": "git"
    },
    {
      "from": "check_scope_enforced",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_scope_enforced",
      "to": "posix_shell"
    },
    {
      "from": "check_scope_enforced",
      "kind": "requires",
      "source_block": "CHECKS",
      "source_id": "check_scope_enforced",
      "to": "python3"
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
      "from": "repo_loto_evidence",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "repo_loto_evidence",
      "to": "Way Seer Erin"
    },
    {
      "from": "repo_mutation_gate",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "repo_mutation_gate",
      "to": "Way Seer Erin"
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
