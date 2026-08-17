# === CHECKS ===
# id: check_prime_relational_identity_nonleakage
#   proves: prime_relational_fixture_identity_excludes_values
#   call: self::test_public_identity_does_not_leak_value
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_h1_reconstruction
#   proves: prime_relational_h1_requires_complementary_unique_reconstruction
#   call: self::test_h1_all_erased_relations_reconstruct_exactly_in_both_implementations
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_encoder_source_independence
#   proves: prime_relational_encoders_remain_source_independent
#   call: self::test_frozen_encoders_do_not_delegate_to_shared_or_peer_helpers
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_registered_resource_bounds
#   proves: prime_relational_complete_run_obeys_registered_resources
#   call: self::test_complete_cli_run_obeys_registered_resource_bounds
#   requires: python3, posix_resource, sched_affinity
#   timeout: 30
#   mutates: filesystem
#   cleanup: tempdir_teardown
#
# id: check_prime_relational_h2_irreducibility
#   proves: prime_relational_h2_tests_every_whole_view
#   call: self::test_h2_every_whole_view_is_irreducible
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_h3_matched_baseline
#   proves: prime_relational_h3_applies_frozen_software_complexity_criterion
#   call: self::test_h3_registered_criterion_falsifies_only_software_advantage
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_h3_architecture_isomorphism
#   proves: prime_relational_baseline_isomorphism_blocks_architecture_transfer
#   call: self::test_h3_baseline_preserves_prime_cardinality_architecture
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_failure_propagation
#   proves: prime_relational_failure_propagation_is_scope_bounded
#   call: self::test_h3_failure_does_not_deprecate_architecture_dependents
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_prime_relational_independent_replay
#   proves: prime_relational_replay_avoids_product_import, prime_relational_replay_scopes_registered_falsification
#   call: self::test_independent_replay_agrees_with_committed_report
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import ast
import os
from pathlib import Path
import importlib.util
import subprocess
import sys

import pytest

from ucns.prime_relational_reconstruction import (
    PREREGISTRATION_PATH,
    public_relation_identity,
    run_architecture_gates,
)


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def report():
    return run_architecture_gates(ROOT / PREREGISTRATION_PATH)


def test_public_identity_does_not_leak_value():
    fields = dict(group="G2", ordinal=0, source="n0", target="n1")
    assert public_relation_identity(**fields, value=19) == public_relation_identity(
        **fields, value=20
    )


def test_h1_all_erased_relations_reconstruct_exactly_in_both_implementations(report):
    assert report["h1"]["status"] == "SURVIVED"
    assert report["h1"]["exact_recoveries"] == 17
    assert all(len(row["replay_candidates"]) == 1 for row in report["h1"]["erasures"])
    assert all(row["primary_recovery"] == row["replay_candidates"][0] for row in report["h1"]["erasures"])
    assert {row["checksum_view"] for row in report["h1"]["erasures"]} == {"P2", "P3", "P5", "P7"}


def test_frozen_encoders_do_not_delegate_to_shared_or_peer_helpers():
    module_path = ROOT / "src/ucns/prime_relational_reconstruction.py"
    tree = ast.parse(module_path.read_text(encoding="utf-8"))
    encoders = {"encode_p2", "encode_p3", "encode_p5", "encode_p7"}
    functions = {
        node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)
    }
    assert encoders <= functions.keys()
    assert "_encode" not in functions
    for encoder in encoders:
        called_names = {
            call.func.id
            for call in ast.walk(functions[encoder])
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
        }
        assert not called_names.intersection(encoders)


def test_complete_cli_run_obeys_registered_resource_bounds(tmp_path):
    if not hasattr(os, "sched_getaffinity") or not hasattr(os, "sched_setaffinity"):
        pytest.skip("registered one-CPU enforcement requires POSIX CPU affinity")
    import resource

    output = tmp_path / "resource-bounded-report.json"
    memory_bytes = 256 * 1024 * 1024

    def apply_registered_bounds():
        available = os.sched_getaffinity(0)
        os.sched_setaffinity(0, {min(available)})
        resource.setrlimit(resource.RLIMIT_AS, (memory_bytes, memory_bytes))

    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "ucns.prime_relational_reconstruction",
            "--repository-root",
            str(ROOT),
            "--output",
            str(output),
        ],
        cwd=ROOT,
        env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
        capture_output=True,
        check=False,
        preexec_fn=apply_registered_bounds,
        text=True,
        timeout=30,
    )
    assert completed.returncode == 0, completed.stderr
    bounded_report = __import__("json").loads(output.read_text(encoding="utf-8"))
    assert bounded_report["resource_bound_enforcement"]["bounds"] == {
        "cpu_count": 1,
        "memory_mib": 256,
        "per_complete_run_seconds": 30,
    }


def test_h2_every_whole_view_is_irreducible(report):
    assert report["h2"]["status"] == "SURVIVED"
    assert report["h2"]["irreducible_leave_outs"] == 4
    assert [row["view"] for row in report["h2"]["leave_outs"]] == ["P2", "P3", "P5", "P7"]
    assert all(row["independent_replay_degrees_of_freedom"] > 0 for row in report["h2"]["leave_outs"])


def test_h3_registered_criterion_falsifies_only_software_advantage(report):
    h3 = report["h3"]
    assert h3["status"] == "FALSIFIED"
    assert h3["status_scope"] == "registered-semantic-label-and-dispatch-advantage"
    assert h3["baseline_matches_or_exceeds"] is True
    assert h3["baseline_strictly_simpler"] is True
    assert h3["baseline"]["encoded_field_cells"] == h3["prime_family"]["encoded_field_cells"] == 21
    assert h3["baseline"]["h1_exact_recoveries"] == h3["prime_family"]["h1_exact_recoveries"] == 17
    assert h3["baseline"]["h2_irreducible_leave_outs"] == h3["prime_family"]["h2_irreducible_leave_outs"] == 4


def test_h3_baseline_preserves_prime_cardinality_architecture(report):
    audit = report["h3"]["structural_audit"]
    assert audit["baseline_architecture_relation"] == "STRUCTURALLY_ISOMORPHIC"
    assert audit["architecture_distinguishing_control"] is False
    assert all(audit["checks"].values())
    assert audit["unchanged_architecture_variables"] == [
        "2/3/5/7 cardinality signature",
        "F_257 arithmetic",
        "four-block source partition",
        "sum-mod-field checksum operator",
        "21 encoded field cells",
    ]
    assert report["architecture_status"] == "UNRESOLVED"


def test_h3_failure_does_not_deprecate_architecture_dependents(report):
    assert report["load_bearing_failure"] == "H3"
    assert report["registered_program_status"] == "FALSIFIED"
    assert report["registered_falsification_scope"] == "semantic-label-and-dispatch-advantage-only"
    assert report["failure_propagation"] == {
        "deprecation_map": [],
        "status": "BLOCKED",
        "target_scope": "prime-cardinality-dependent-claims",
    }
    assert set(report["dependent_escalations"].values()) == {"UNRESOLVED"}
    assert report["prior_bounded_results"] == {
        "edcm_absolute_recovered_dissonance": "FALSIFIED",
        "edcm_normalized_recovered_dissonance": "SURVIVED",
        "ucns_p5_p7_exact_distinction": "SURVIVED",
    }
    assert report["external_or_sealed_labels_inspected"] is False
    assert report["canon_selection"] is None
    assert report["post_registration_audit"] == {
        "criterion_changed": False,
        "leakage_detected": False,
        "preregistration_changed": False,
        "terminal_interpretation_drift_detected": True,
        "terminal_interpretation_drift": (
            "registered software-complexity falsification was broadened to "
            "prime-cardinality architecture and its dependent claims"
        ),
    }


def test_independent_replay_agrees_with_committed_report(tmp_path, report):
    report_path = tmp_path / "report.json"
    import json
    report_path.write_text(json.dumps(report), encoding="utf-8")
    tool_path = ROOT / "tools/replay_prime_relational_reconstruction.py"
    spec = importlib.util.spec_from_file_location("independent_prime_replay", tool_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    replay = module.replay(ROOT / PREREGISTRATION_PATH, report_path)
    assert replay["status"] == "AGREED"
    assert replay["checks"]["structural_isomorphism"] is True
    assert replay["checks"]["architecture_unresolved"] is True
    assert replay["checks"]["propagation_blocked"] is True
    assert replay["h1_exact_recoveries"] == 17
    assert replay["h2_dimensions"] == {"P2": 1, "P3": 2, "P5": 4, "P7": 6}
