# ratios: loc_comments=167:80 imports_exports=13:10 calls_definitions=48:12
# === CHECKS ===
# id: check_coefficient_audit_exact_ledger
#   proves: coefficient_audit_exact_ledger
#   call: self::test_coefficient_ledger_matches_independent_subset_products
#   requires: python3, pytest
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_coefficient_audit_restricted_breadth
#   proves: coefficient_audit_restricted_breadth
#   call: self::test_collision_and_restricted_null_faithfulness
#   requires: python3, pytest
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_coefficient_audit_supplied_successor
#   proves: coefficient_audit_exact_ledger
#   call: self::test_supplied_successor_does_not_select_an_observed_anchor
#   requires: python3, pytest
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_coefficient_audit_factor_custody
#   proves: coefficient_audit_retains_factors_without_role_admission
#   call: self::test_factor_order_and_provenance_do_not_invent_role_admission
#   requires: python3, pytest
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_coefficient_audit_optimized_refusal
#   proves: coefficient_audit_fails_closed
#   call: self::test_optimized_execution_cannot_emit_evidence
#   requires: python3, pytest
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_coefficient_audit_stdout_replay
#   proves: coefficient_audit_emits_replayed_bytes, coefficient_audit_restricted_breadth
#   call: self::test_exact_stdout_replays_and_preserves_taxonomy
#   requires: python3, pytest
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_coefficient_audit_arithmetic_failure
#   proves: coefficient_audit_fails_closed, coefficient_audit_exact_ledger
#   call: self::test_planted_arithmetic_fault_cannot_emit_evidence
#   requires: python3, pytest
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_coefficient_audit_invalid_input
#   proves: coefficient_audit_rejects_invalid_inputs
#   call: self::test_invalid_factor_coefficients_and_provenance_refuse
#   requires: python3, pytest
#   timeout: 30
#   mutates: none
#   cleanup: none
# id: check_contract_audit_discovers_prime_arity_experiments
#   proves: contract_audit_reports_graph_gaps, contract_audit_is_no_exec
#   call: self::test_docs_experiment_gaps_are_detected_without_execution
#   requires: python3, pytest
#   timeout: 30
#   mutates: filesystem
#   cleanup: pytest temporary_path
# === END CHECKS ===

"""Usage: pytest tests/test_coefficient_breadth_audit.py.

Load the documentation-owned experiment only during an executable check. The
subset-product oracle does not call the update recurrence it is checking.
Subprocess checks capture the exact artifact, reject optimized execution, and
seed a wrong anchor to demonstrate that a failed falsifier emits no evidence.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, combinations_with_replacement
import json
from math import prod
import os
from pathlib import Path
import runpy
import subprocess
import sys

import pytest

from tools.verify_skill_lib_contracts import audit_repository

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "docs/prime-arity/audit_coefficient_breadth.py"


@pytest.fixture
def coefficient_audit():
    """Load a fresh experiment namespace, without importing it as core UCNS."""
    namespace = runpy.run_path(str(AUDIT))
    return namespace["build_audit"].__globals__


def _subset_coefficients(factors):
    return tuple(
        sum(prod(subset) for subset in combinations(factors, degree))
        for degree in range(len(factors) + 1)
    )


def test_coefficient_ledger_matches_independent_subset_products(coefficient_audit):
    primes = (2, 3, 5, 7, 11)
    seen = {}
    cases = 0
    for degree in range(5):
        for factors in combinations_with_replacement(primes, degree):
            expected = _subset_coefficients(factors)
            actual = coefficient_audit["coefficient_layers"](factors)
            assert actual == expected
            assert actual[-1] == prod(factors)
            assert seen.setdefault(actual, factors) == factors
            for q in primes:
                assert coefficient_audit["update_coefficients"](actual, q) == _subset_coefficients(factors + (q,))
            cases += 1
    assert cases == 126
    # Repeated factors remain repeated, not deduplicated or counted as roles.
    assert coefficient_audit["coefficient_layers"]((3, 3)) == (1, 6, 9)


def test_collision_and_restricted_null_faithfulness(coefficient_audit):
    assert coefficient_audit["coefficient_layers"]((3, 11)) == (1, 14, 33)
    assert coefficient_audit["coefficient_layers"]((5, 7)) == (1, 12, 35)
    for factors in ((3, 11), (5, 7)):
        assert coefficient_audit["evaluated_size"](factors) == 48
        assert coefficient_audit["exact_radius"](factors) == Fraction(47, 48)
    for degree in range(5):
        for factors in combinations_with_replacement((2, 3, 5, 7, 11), degree):
            size = coefficient_audit["evaluated_size"](factors)
            radius = coefficient_audit["exact_radius"](factors)
            assert size == prod(1 + factor for factor in factors)
            assert (size == 1) == (factors == ())
            assert (radius == 0) == (factors == ())
            assert 0 <= radius < 1


def test_supplied_successor_does_not_select_an_observed_anchor(coefficient_audit):
    base = coefficient_audit["coefficient_layers"]((43, 67))
    assert coefficient_audit["update_coefficients"](base, 3) == (1, 113, 3211, 8643)
    assert coefficient_audit["update_coefficients"](base, 5) == (1, 115, 3431, 14405)
    report = coefficient_audit["build_audit"]()
    assert report["tests"]["successor_q_discovery"] == "UNRESOLVED"
    assert report["tests"]["observed_role_sets_are_nested"] == [False, False]
    assert report["tests"]["constructs_observed_successors"] is False


def test_factor_order_and_provenance_do_not_invent_role_admission(coefficient_audit):
    make = coefficient_audit["retained_record"]
    left = make((3, 11), "fixture:left")
    right = make((11, 3), "fixture:right")
    assert left["coefficient_vector"] == right["coefficient_vector"]
    assert left["provenance"]["supplied_factors"] == [3, 11]
    assert right["provenance"]["supplied_factors"] == [11, 3]
    assert left["provenance"]["source"] != right["provenance"]["source"]
    # Even an empty factor record retains provenance: this test does not call
    # the complete record Structural Null or promote a full breadth evaluator.
    for record in (left, right, make((), "fixture:empty")):
        assert record["relations"]["role_admission"] == "UNRESOLVED"
        assert record["relations"]["ucns_arity"] is None
        assert record["relations"]["factor_semantics"] == "supplied prime factors, not admitted UCNS roles"


def test_optimized_execution_cannot_emit_evidence():
    environment = dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1")
    for flags, optimize in ((["-O"], "0"), (["-OO"], "0"), ([], "1"), ([], "2")):
        rejected = subprocess.run(
            [sys.executable, *flags, str(AUDIT)],
            env=dict(environment, PYTHONOPTIMIZE=optimize),
            capture_output=True,
            timeout=20,
        )
        assert rejected.returncode != 0
        assert rejected.stdout == b""
        assert b"optimized Python cannot produce coefficient audit evidence" in rejected.stderr


def test_exact_stdout_replays_and_preserves_taxonomy(coefficient_audit):
    environment = dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1")
    outputs = [
        subprocess.run(
            [sys.executable, str(AUDIT)], env=environment, capture_output=True, check=True, timeout=20
        ).stdout
        for _ in range(2)
    ]
    assert outputs[0] == outputs[1]
    report = coefficient_audit["replay_canonical_json"](outputs[0])
    assert coefficient_audit["canonical_json_bytes"](report) == outputs[0]
    assert report["verdict"] == "UNRESOLVED"
    assert report["standing"] == "incubating; non-canonical"
    assert report["tests"]["finite_exhaustive_replay_cases"] == 126
    expected = {
        "coefficient_update_law": "PROVEN",
        "full_coefficient_vector_preserves_unordered_prime_multiset": "PROVEN",
        "successor_q_discovery": "UNRESOLVED",
        "C_at_1_as_injective_structure_encoding": "FALSIFIED",
        "B_c_null_faithful_on_positive_prime_role_multisets": "SURVIVED",
        "B_c_as_complete_UCNS_breadth_evaluator": "UNRESOLVED",
        "full_retained_structure_breadth": "BLOCKED",
    }
    assert {key: report["tests"][key] for key in expected} == expected
    assert report["tests"]["factor_count_is_UCNS_arity"] is False
    for anchor in report["anchors"].values():
        assert "factors" in anchor and "roles" not in anchor
        assert anchor["retained_record"]["relations"]["ucns_arity"] is None
    # The former pretty stdout was not the artifact the strict parser replayed.
    with pytest.raises(ValueError, match="canonical byte"):
        coefficient_audit["replay_canonical_json"]((json.dumps(report, indent=2) + "\n").encode())


def test_planted_arithmetic_fault_cannot_emit_evidence(coefficient_audit, monkeypatch):
    code = (
        "import runpy; "
        f"m=runpy.run_path({str(AUDIT)!r}); "
        "m['FACTOR_SETS']['157']=(151,); m['main']()"
    )
    failed = subprocess.run(
        [sys.executable, "-c", code],
        env=dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1"),
        capture_output=True,
        timeout=20,
    )
    assert failed.returncode != 0 and b"AssertionError" in failed.stderr
    assert failed.stdout == b""
    # Seed a real recurrence defect and require the independent subset oracle
    # to notice it, then restore the fresh module's namespace.
    update = coefficient_audit["update_coefficients"]

    def broken_update(coefficients, successor):
        result = update(coefficients, successor)
        return result[:-1] + (result[-1] + 1,)

    with monkeypatch.context() as patch:
        patch.setitem(coefficient_audit, "update_coefficients", broken_update)
        with pytest.raises(AssertionError):
            assert coefficient_audit["coefficient_layers"]((3, 11)) == _subset_coefficients((3, 11))


def test_invalid_factor_coefficients_and_provenance_refuse(coefficient_audit):
    for value in (True, False, -3, 0, 1, 4, 2.0, "3", None):
        for name in ("coefficient_layers", "evaluated_size", "exact_radius"):
            with pytest.raises(ValueError):
                coefficient_audit[name]((value,))
        with pytest.raises(ValueError):
            coefficient_audit["update_coefficients"]((1,), value)
    for coefficients in ((), (2,), (True,), (1, 0), (1, -3), (1, 3.0)):
        with pytest.raises(ValueError):
            coefficient_audit["update_coefficients"](coefficients, 3)
    for source in (None, "", "   ", 4):
        with pytest.raises(ValueError):
            coefficient_audit["retained_record"]((3,), source)


def test_docs_experiment_gaps_are_detected_without_execution(tmp_path):
    from test_skill_lib_boundary_runner import _repo

    root = _repo(tmp_path, "def test_probe():\n    pass\n", [{"id": "check_probe", "function": "test_probe"}])
    assert audit_repository(root)[0]
    directory = root / "docs/prime-arity"
    directory.mkdir(parents=True)
    # No imported or executed experiment is necessary to detect the missing
    # declarations, including a source-owned orphan obligation.
    probe = directory / "probe.py"
    probe.write_text(
        "# === CONTRACTS ===\n# id: orphan_experiment\n#   given: an experiment\n"
        "#   then: it remains accountable\n# === END CONTRACTS ===\n"
        "raise RuntimeError('must never execute during declaration audit')\n",
        encoding="utf-8",
    )
    ok, problems = audit_repository(root)
    assert not ok
    assert any(str(probe) in problem and "missing MODULE_BUILD" in problem for problem in problems)
    assert any("orphan_experiment has no CHECKS" in problem for problem in problems)
# ratios: loc_comments=167:80 imports_exports=13:10 calls_definitions=48:12
