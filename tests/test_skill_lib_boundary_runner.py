# ratios: loc_comments=98:209 imports_exports=6:16 calls_definitions=74:18
# === CHECKS ===
# id: check_boundary_runner_audit_gate
#   proves: boundary_runner_audits_before_execution
#   call: self::test_audit_gap_prevents_execution
#   requires: python3
#   timeout: 10
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_boundary_runner_capability_timeout_consumption
#   proves: boundary_runner_consumes_capabilities_and_timeouts
#   call: self::test_missing_capability_and_timeout_are_enforced
#   requires: python3
#   timeout: 15
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_boundary_runner_registered_capability_detection
#   proves: boundary_runner_consumes_capabilities_and_timeouts
#   call: self::test_registered_posix_capabilities_are_detected
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_boundary_runner_status_continuation
#   proves: boundary_runner_classifies_and_continues, boundary_pytest_observes_actual_outcomes
#   call: self::test_runner_classifies_all_outcomes_and_continues
#   requires: python3
#   timeout: 20
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_boundary_runner_receipt_binding
#   proves: boundary_runner_receipt_is_bounded_and_bound
#   call: self::test_receipt_binds_declarations_outputs_and_identity
#   requires: python3
#   timeout: 10
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_boundary_runner_nonactivation
#   proves: boundary_runner_has_no_activation_effect
#   call: self::test_passing_receipt_has_no_activation_or_selection_effect
#   requires: python3
#   timeout: 10
#   mutates: temporary_path
#   cleanup: pytest temporary_path
# === END CHECKS ===

# === CHECKS ===
# id: check_boundary_runner_skips_are_not_passes
#   proves: boundary_runner_classifies_and_continues
#   call: self::test_skips_xfails_and_mixed_parameters_are_not_passes
#   requires: python3, pytest
#   timeout: 30
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_boundary_runner_invalid_declaration_continuation
#   proves: boundary_runner_classifies_and_continues
#   call: self::test_invalid_execution_metadata_does_not_abort_later_checks
#   requires: python3, pytest
#   timeout: 15
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_boundary_runner_source_identity
#   proves: boundary_runner_receipt_is_bounded_and_bound
#   call: self::test_source_mutation_prevents_acceptance
#   requires: python3, pytest
#   timeout: 15
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_boundary_runner_report_and_discovery_boundaries
#   proves: boundary_runner_classifies_and_continues, boundary_runner_receipt_is_bounded_and_bound
#   call: self::test_report_errors_suffix_discovery_and_launch_continuation
#   requires: python3, pytest
#   timeout: 20
#   mutates: temporary_path
#   cleanup: pytest temporary_path
# === END CHECKS ===

from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


RUNNER_PATH = Path(__file__).parents[1] / "tools" / "run_skill_lib_boundaries.py"
SPEC = importlib.util.spec_from_file_location("run_skill_lib_boundaries", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
runner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runner
SPEC.loader.exec_module(runner)


def _repo(tmp_path: Path, functions: str, checks: list[dict[str, str]]) -> Path:
    root = tmp_path / "repo"
    (root / "src" / "pkg").mkdir(parents=True)
    (root / "tools").mkdir()
    (root / "tests").mkdir()
    contracts: list[str] = []
    check_lines: list[str] = []
    for index, check in enumerate(checks):
        contract_id = f"contract_{index}"
        contracts.extend([
            f"# id: {contract_id}", "#   given: fixture input",
            "#   then: fixture outcome", "#   class: evidence", "#",
        ])
        check_lines.extend([
            f"# id: {check['id']}", f"#   proves: {contract_id}",
            f"#   call: self::{check['function']}",
            f"#   requires: {check.get('requires', 'python3')}",
            f"#   timeout: {check.get('timeout', '5')}",
            "#   mutates: none", "#   cleanup: none", "#",
        ])
    (root / "src" / "pkg" / "feature.py").write_text(
        "\n".join([
            "# === MODULE_BUILD ===", "# id: fixture_module",
            "#   module_name: feature", "#   module_kind: instrument",
            "#   summary: fixture", "#   owner: fixture", "#   public_surface: none",
            "#   internal_surface: none", "#   auth_boundary: none",
            "#   storage_boundary: none", "#   network_boundary: none",
            "#   user_data_boundary: none", "#   admin_only: false",
            "#   tests: tests/test_feature.py", "#   rollout: fixture",
            "#   rollback: remove", "# === END MODULE_BUILD ===",
            "# === CONTRACTS ===", *contracts, "# === END CONTRACTS ===", "",
        ]), encoding="utf-8"
    )
    (root / "tests" / "test_feature.py").write_text(
        "\n".join(["# === CHECKS ===", *check_lines, "# === END CHECKS ===", "", functions]),
        encoding="utf-8",
    )
    return root


def test_audit_gap_prevents_execution(tmp_path: Path) -> None:
    root = _repo(tmp_path, "def test_never():\n    raise AssertionError('ran')\n", [{"id": "check_never", "function": "test_never"}])
    source = root / "src" / "pkg" / "feature.py"
    source.write_text(source.read_text().replace(
        "# === END CONTRACTS ===",
        "# id: orphan\n#   given: x\n#   then: y\n# === END CONTRACTS ===",
    ))
    receipt = runner.run_boundaries(root)
    assert receipt["status"] == "audit-gap"
    assert receipt["outcomes"] == []
    assert len(receipt["receipt_sha256"]) == 64


def test_missing_capability_and_timeout_are_enforced(tmp_path: Path) -> None:
    root = _repo(tmp_path, "def test_missing():\n    pass\n", [{
        "id": "check_missing", "function": "test_missing",
        "requires": "capability-that-cannot-exist",
    }])
    receipt = runner.run_boundaries(root)
    assert receipt["outcomes"][0]["status"] == "ERROR"
    assert receipt["outcomes"][0]["missing_capabilities"] == (
        "capability-that-cannot-exist",
    )

    root = _repo(tmp_path / "timeout", "import time\ndef test_slow():\n    time.sleep(5)\n", [{
        "id": "check_slow", "function": "test_slow", "timeout": "1",
    }])
    receipt = runner.run_boundaries(root)
    assert receipt["outcomes"][0]["status"] == "TIMEOUT"
    assert receipt["outcomes"][0]["duration_seconds"] < 4


def test_registered_posix_capabilities_are_detected() -> None:
    assert runner._capability_available("posix_resource") == (
        runner.os.name == "posix"
        and importlib.util.find_spec("resource") is not None
    )
    assert runner._capability_available("sched_affinity") == (
        hasattr(runner.os, "sched_getaffinity")
        and hasattr(runner.os, "sched_setaffinity")
    )


def test_runner_classifies_all_outcomes_and_continues(tmp_path: Path) -> None:
    functions = """
def test_pass():
    pass
def test_fail():
    assert False
def test_error():
    raise RuntimeError("AssertionError mentioned by a broken harness")
class ContractViolation(AssertionError):
    pass
def test_subclass():
    raise ContractViolation("broken")
"""
    checks = [
        {"id": "check_pass", "function": "test_pass"},
        {"id": "check_fail", "function": "test_fail"},
        {"id": "check_error", "function": "test_error"},
        {"id": "check_subclass", "function": "test_subclass"},
    ]
    receipt = runner.run_boundaries(_repo(tmp_path, functions, checks))
    assert [item["status"] for item in receipt["outcomes"]] == [
        "PASS", "FAIL", "ERROR", "FAIL",
    ]
    assert receipt["outcome_counts"] == {
        "PASS": 1, "FAIL": 2, "ERROR": 1, "TIMEOUT": 0, "SKIP": 0,
    }


def test_report_errors_suffix_discovery_and_launch_continuation(tmp_path: Path, monkeypatch) -> None:
    report = tmp_path / "report.xml"
    assert runner._pytest_outcome(report, 0)[0] == "ERROR"
    for text in ("not json", "[]", '{"status": "PASS"}', '{"status": "PASS", "calls": [], "other": [], "origins": {}}'):
        report.write_text(text)
        assert runner._pytest_outcome(report, 0)[0] == "ERROR"
    root = _repo(tmp_path, "def test_first():\n    pass\ndef test_later():\n    pass\n", [
        {"id": "check_first", "function": "test_first"},
        {"id": "check_later", "function": "test_later"},
    ])
    (root / "tests/test_feature.py").rename(root / "tests/feature_test.py")
    original = runner._run_check

    def launch(repository, check):
        if check.id == "check_first":
            raise OSError("fixture process launch failed")
        return original(repository, check)

    monkeypatch.setattr(runner, "_run_check", launch)
    receipt = runner.run_boundaries(root)
    assert [outcome["status"] for outcome in receipt["outcomes"]] == ["ERROR", "PASS"]
    assert receipt["outcomes"][0]["diagnostic"].startswith("OSError:")
    assert receipt["status"] == "not-passed"


def test_receipt_binds_declarations_outputs_and_identity(tmp_path: Path) -> None:
    root = _repo(tmp_path, "def test_output():\n    print('evidence')\n", [{
        "id": "check_output", "function": "test_output",
    }])
    receipt = runner.run_boundaries(root)
    outcome = receipt["outcomes"][0]
    assert outcome["contract_ids"] == ("contract_0",)
    assert outcome["mutates"] == outcome["cleanup"] == "none"
    assert outcome["stdout_bytes"] > 0
    assert len(outcome["stdout_sha256"]) == 64
    identity = receipt.pop("receipt_sha256")
    encoded = json.dumps(
        receipt, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    assert identity == sha256(encoded).hexdigest()


def test_passing_receipt_has_no_activation_or_selection_effect(tmp_path: Path) -> None:
    receipt = runner.run_boundaries(_repo(
        tmp_path, "def test_pass():\n    pass\n",
        [{"id": "check_pass", "function": "test_pass"}],
    ))
    assert receipt["status"] == "passed"
    assert receipt["selection_effect"] == "none"
    assert receipt["edcm_activation"] == "inactive"
    assert receipt["canon_status"] == "none"


def test_skips_xfails_and_mixed_parameters_are_not_passes(tmp_path: Path) -> None:
    bodies = (
        "import pytest\ndef test_probe():\n    pytest.skip('not observed')\n",
        "import pytest\n@pytest.mark.xfail(reason='broken')\ndef test_probe():\n    assert False\n",
        "import pytest\n@pytest.mark.parametrize('x', [1, 2])\ndef test_probe(x):\n    if x == 2: pytest.skip('partial')\n",
    )
    for index, body in enumerate(bodies):
        root = _repo(tmp_path / str(index), body, [{"id": "check_probe", "function": "test_probe"}])
        receipt = runner.run_boundaries(root)
        assert receipt["status"] == "not-passed"
        assert receipt["outcomes"][0]["status"] == "SKIP"
    for index, decorator in enumerate(("@pytest.mark.xfail(strict=False)", "@pytest.mark.xfail(strict=True)")):
        body = "import pytest\n" + decorator + "\ndef test_probe():\n    pass\n"
        root = _repo(tmp_path / f"xpass{index}", body, [{"id": "check_probe", "function": "test_probe"}])
        receipt = runner.run_boundaries(root)
        assert receipt["status"] == "not-passed"
        assert receipt["outcomes"][0]["status"] == "FAIL"
    assert runner.run_boundaries(tmp_path / "absent")["status"] == "audit-gap"


def test_invalid_execution_metadata_does_not_abort_later_checks(tmp_path: Path) -> None:
    root = _repo(tmp_path, "def test_bad():\n    pass\ndef test_good():\n    pass\n", [
        {"id": "check_bad", "function": "test_bad", "timeout": "not-an-integer"},
        {"id": "check_good", "function": "test_good"},
    ])
    receipt = runner.run_boundaries(root)
    assert [outcome["status"] for outcome in receipt["outcomes"]] == ["ERROR", "PASS"]
    assert receipt["status"] == "not-passed"


def test_source_mutation_prevents_acceptance(tmp_path: Path) -> None:
    root = _repo(tmp_path, "from pathlib import Path\ndef test_probe():\n    p=Path('src/pkg/feature.py')\n    p.write_text(p.read_text()+'\\n# mutation\\n')\n", [
        {"id": "check_probe", "function": "test_probe"},
    ])
    receipt = runner.run_boundaries(root)
    assert receipt["outcomes"][0]["status"] == "PASS"
    assert receipt["status"] == "not-passed"
    assert receipt["source_before_sha256"] != receipt["source_after_sha256"]
    assert receipt["source_unchanged"] is False
    root = _repo(tmp_path / "restored", "from pathlib import Path\ndef test_probe():\n    p=Path('src/pkg/feature.py')\n    original=p.read_bytes()\n    p.write_bytes(original+b'\\n# transient\\n')\n    p.write_bytes(original)\n", [
        {"id": "check_probe", "function": "test_probe"},
    ])
    receipt = runner.run_boundaries(root)
    assert receipt["source_before_sha256"] == receipt["source_after_sha256"]
    assert receipt["source_unchanged"] is False
    assert receipt["status"] == "not-passed"
    assert "src/pkg/feature.py" in receipt["outcomes"][0]["source_events"]
# === CHECKS ===
# id: check_boundary_runner_import_origin
#   proves: boundary_runner_receipt_is_bounded_and_bound, boundary_pytest_observes_actual_outcomes
#   call: self::test_check_imports_bound_source_despite_ambient_pythonpath
#   requires: python3, pytest
#   timeout: 15
#   mutates: temporary_path
#   cleanup: pytest temporary_path
# === END CHECKS ===


def test_check_imports_bound_source_despite_ambient_pythonpath(tmp_path: Path, monkeypatch) -> None:
    body = "import pkg.feature\ndef test_probe():\n    assert pkg.feature.VALUE == 'bound'\n"
    root = _repo(tmp_path, body, [{"id": "check_probe", "function": "test_probe"}])
    source = root / "src/pkg/feature.py"
    source.write_text(source.read_text() + "VALUE = 'bound'\n")
    # A regular package avoids unrelated namespace packages in the host.
    (root / "src/pkg/__init__.py").write_text(source.read_text().replace("fixture_module", "fixture_init").replace("contract_0", "init_contract"))
    (root / "tests/test_feature.py").write_text((root / "tests/test_feature.py").read_text().replace("#   proves: contract_0", "#   proves: contract_0, init_contract"))
    alternate = tmp_path / "alternate"
    (alternate / "pkg").mkdir(parents=True)
    (alternate / "pkg/__init__.py").write_text("")
    (alternate / "pkg/feature.py").write_text("VALUE = 'wrong'\n")
    monkeypatch.setenv("PYTHONPATH", str(alternate))
    receipt = runner.run_boundaries(root)
    assert receipt["status"] == "passed", receipt
    assert receipt["outcomes"][0]["imported_sources"]["pkg.feature"] == [str(source)]
# ratios: loc_comments=98:209 imports_exports=6:16 calls_definitions=74:18
