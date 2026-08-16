# === CHECKS ===
# id: check_external_evaluation_corpus_gate
#   proves: external_evaluation_requires_completed_corpus_gate
#   call: self::test_plan_requires_execution_generated_completion_receipt
#   requires: python3
#   timeout: 10
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_external_evaluator_identity_disclosure_binding
#   proves: external_evaluator_identity_and_disclosure_are_bound
#   call: self::test_request_binds_identity_command_cases_and_disclosure
#   requires: python3
#   timeout: 10
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_external_evaluation_resource_bounds
#   proves: external_evaluation_is_resource_bounded
#   call: self::test_timeout_input_output_and_executable_bounds_fail_closed
#   requires: python3
#   timeout: 20
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_external_response_reconciliation
#   proves: external_response_reconciliation_is_fail_closed
#   call: self::test_response_requires_exact_protocol_and_ordered_case_coverage
#   requires: python3
#   timeout: 15
#   mutates: temporary_path
#   cleanup: pytest temporary_path
#
# id: check_external_evaluation_nonpromotion
#   proves: external_evaluation_receipt_is_nonpromoting
#   call: self::test_complete_external_receipt_is_candidate_evidence_only
#   requires: python3
#   timeout: 10
#   mutates: temporary_path
#   cleanup: pytest temporary_path
# === END CHECKS ===

from __future__ import annotations

from dataclasses import replace
from hashlib import sha256
import json
from pathlib import Path
import sys

import pytest

from ucns.external_evaluation import (
    PROTOCOL_VERSION,
    RESPONSE_SCHEMA_ID,
    ExternalEvaluationCase,
    ExternalEvaluationError,
    ExternalEvaluationPlan,
    ExternalEvaluationStatus,
    ExternalEvaluatorCommand,
    ExternalEvaluatorIdentity,
    execute_external_evaluation,
)
from ucns.full_corpus import (
    AdmittedCorpusManifest,
    CorpusAdapterIdentity,
    execute_admitted_corpus,
    issue_full_corpus_completion_receipt,
)


def _file_digest(path: str) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


def _corpus_receipt():
    manifest = AdmittedCorpusManifest(
        corpus_id="external-fixture", corpus_version="1",
        source_artifact_sha256="a" * 64, expected_turn_count=2,
        license_id="fixture-license", privacy_treatment="synthetic",
        redaction_policy="none", admission_decision_id="fixture-admission/1",
        adapter=CorpusAdapterIdentity("fixture-adapter", "1", "tests:fixture"),
    )
    report = execute_admitted_corpus(manifest, (("a", "ONE TWO"), ("b", "THREE")))
    return issue_full_corpus_completion_receipt(report)


def _case(case_id: str = "case-1") -> ExternalEvaluationCase:
    return ExternalEvaluationCase(
        case_id=case_id, subject_digest=sha256(case_id.encode()).hexdigest(),
        custody_reference=f"fixture:{case_id}",
        disclosure_authority_id="fixture-disclosure/1",
        payload={"text": case_id},
    )


VALID_EVALUATOR = r'''
import json,sys
r=json.load(sys.stdin)
out={"schema_id":"ucns.edcm.external-evaluator-response","schema_version":"1.0.0","plan_id":r["plan_id"],"evaluator":{"evaluator_id":r["evaluator"]["evaluator_id"],"evaluator_version":r["evaluator"]["evaluator_version"]},"results":[{"case_id":c["case_id"],"status":"ok","output":{"length":len(c["payload"]["text"])},"evidence":["fixture-length"],"error":None} for c in r["cases"]]}
json.dump(out,sys.stdout,sort_keys=True,separators=(",",":"))
'''


def _plan(*, code: str = VALID_EVALUATOR, cases=None, timeout: int = 5,
          max_input: int = 100_000, max_output: int = 100_000,
          executable_digest: str | None = None) -> ExternalEvaluationPlan:
    executable = str(Path(sys.executable).resolve())
    evaluator = ExternalEvaluatorIdentity(
        "fixture-evaluator", "1", "tests.test_external_evaluation:fixture",
        executable_digest or _file_digest(executable),
    )
    command = ExternalEvaluatorCommand(
        (executable, "-c", code), timeout, max_input, max_output,
        network_policy="caller-isolated",
    )
    return ExternalEvaluationPlan(
        "fixture-plan", "1", "What candidate relation is reported?",
        _corpus_receipt(), evaluator, command,
        tuple(cases or (_case("case-1"), _case("case-2"))),
    )


def test_plan_requires_execution_generated_completion_receipt() -> None:
    plan = _plan()
    with pytest.raises(ExternalEvaluationError, match="FullCorpusCompletionReceipt"):
        replace(plan, corpus_receipt=plan.corpus_receipt.report)  # type: ignore[arg-type]


def test_request_binds_identity_command_cases_and_disclosure() -> None:
    plan = _plan()
    request = plan.request()
    assert request["upstream"]["completion_receipt_id"] == plan.corpus_receipt.receipt_id
    assert request["evaluator"]["executable_sha256"] == plan.evaluator.executable_sha256
    assert request["execution"]["argv"] == list(plan.command.argv)
    assert [item["case_id"] for item in request["cases"]] == ["case-1", "case-2"]
    assert all(item["disclosure_authority_id"] == "fixture-disclosure/1" for item in request["cases"])
    changed = replace(plan, cases=(replace(plan.cases[0], disclosure_authority_id="other/2"), plan.cases[1]))
    assert execute_external_evaluation(changed).request_sha256 != execute_external_evaluation(plan).request_sha256
    with pytest.raises(ExternalEvaluationError, match="environment keys"):
        execute_external_evaluation(plan, environment={"SECRET": "not-declared"})


def test_timeout_input_output_and_executable_bounds_fail_closed() -> None:
    with pytest.raises(ExternalEvaluationError, match="executable digest mismatch"):
        execute_external_evaluation(_plan(executable_digest="0" * 64))
    with pytest.raises(ExternalEvaluationError, match="max_input_bytes"):
        execute_external_evaluation(_plan(max_input=10))

    timeout = execute_external_evaluation(_plan(code="import time; time.sleep(5)", timeout=1))
    assert timeout.status is ExternalEvaluationStatus.INCOMPLETE
    assert timeout.timed_out is True
    assert timeout.failure == "timeout"

    oversized = execute_external_evaluation(_plan(code="print('x'*100000)", max_output=1024))
    assert oversized.status is ExternalEvaluationStatus.INCOMPLETE
    assert oversized.returncode != 0


def test_response_requires_exact_protocol_and_ordered_case_coverage() -> None:
    wrong = r'''
import json,sys
r=json.load(sys.stdin)
json.dump({"schema_id":"ucns.edcm.external-evaluator-response","schema_version":"1.0.0","plan_id":r["plan_id"],"evaluator":{"evaluator_id":"fixture-evaluator","evaluator_version":"1"},"results":[]},sys.stdout)
'''
    receipt = execute_external_evaluation(_plan(code=wrong))
    assert receipt.status is ExternalEvaluationStatus.INCOMPLETE
    assert "cover every case exactly once" in receipt.failure
    assert receipt.response_results == ()


def test_complete_external_receipt_is_candidate_evidence_only() -> None:
    receipt = execute_external_evaluation(_plan())
    assert receipt.status is ExternalEvaluationStatus.COMPLETE
    assert [item["case_id"] for item in receipt.response_results] == ["case-1", "case-2"]
    assert receipt.selection_effect == "none"
    assert receipt.measurement_validity == "not-established"
    assert receipt.edcm_activation == "inactive"
    assert receipt.canon_status == "none"
    assert receipt.evidence_status == "candidate-measured-evidence"
    assert len(receipt.receipt_id) == 64
    with pytest.raises(ExternalEvaluationError, match="cannot promote"):
        replace(receipt, edcm_activation="active")
