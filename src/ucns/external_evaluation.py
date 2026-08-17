# === MODULE_BUILD ===
# id: edcm_external_evaluation_harness
#   module_name: external_evaluation
#   module_kind: instrument
#   summary: executes one explicitly identified external evaluator behind the completed EDCM corpus gate and emits bounded reconciled nonpromoting receipts
#   owner: Erin Spencer
#   public_surface: ExternalEvaluatorIdentity, ExternalEvaluatorCommand, ExternalEvaluationCase, ExternalEvaluationPlan, ExternalEvaluationStatus, ExternalEvaluationReceipt, execute_external_evaluation
#   internal_surface: canonical request encoding, executable validation, process-group timeout, output-bound enforcement, response reconciliation
#   auth_boundary: external corpus admission and per-case disclosure authority remain caller supplied and receipt bound
#   storage_boundary: request and response bytes are process-local; receipts retain digests, bounded excerpts, and parsed result evidence
#   network_boundary: evaluator network access is declared but must be enforced by the caller-provided wrapper or execution environment
#   user_data_boundary: only explicitly supplied case payloads cross the process boundary; raw corpus custody is neither inferred nor fetched
#   admin_only: false
#   tests: tests/test_external_evaluation.py
#   rollout: candidate external evaluation transport only; no benchmark, evaluator selection, measurement validity, EDCM activation, or canon effect
#   rollback: remove module, exports, tests, and documentation while retaining the full-corpus gate and skill-lib boundary runner
#   requires: edcm_full_corpus_execution_gate, skill_lib_boundary_runner
#   since: 2026-08-16
#   unresolved: authenticated remote transport, network sandbox enforcement, external secret delivery, and evaluator-specific semantic validity
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: external_evaluation_requires_completed_corpus_gate
#   given: an external EDCM evaluation plan is constructed or executed
#   then: it binds an execution-generated FullCorpusCompletionReceipt and cannot run from a declaration, incomplete report, or corpus prefix
#   class: safety
#   since: 2026-08-16
#
# id: external_evaluator_identity_and_disclosure_are_bound
#   given: cases cross the external process boundary
#   then: evaluator identity, executable digest, exact argv, declared environment keys, network policy, case order, subject digests, custody references, and disclosure authorities enter the request and receipt identity
#   class: evidence
#   since: 2026-08-16
#
# id: external_evaluation_is_resource_bounded
#   given: an external evaluator is executed
#   then: input size, output file size, wall timeout, and process group termination are enforced rather than merely reported
#   class: safety
#   since: 2026-08-16
#
# id: external_response_reconciliation_is_fail_closed
#   given: an evaluator returns candidate results
#   then: protocol, plan, evaluator echo, exact ordered case coverage, result status, and JSON shape must reconcile or the receipt remains incomplete with the failure visible
#   class: evidence
#   since: 2026-08-16
#
# id: external_evaluation_receipt_is_nonpromoting
#   given: an external evaluation completes successfully
#   then: evaluator outputs remain candidate evidence and cannot select a benchmark or evaluator, validate UCNS measurement, activate EDCM, or confer canon status
#   class: doctrine
#   since: 2026-08-16
# === END CONTRACTS ===

"""Fail-closed process boundary for post-corpus EDCM candidate evaluation."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import tempfile
import time
from typing import Any, Mapping

from .full_corpus import FullCorpusCompletionReceipt


REQUEST_SCHEMA_ID = "ucns.edcm.external-evaluator-request"
RESPONSE_SCHEMA_ID = "ucns.edcm.external-evaluator-response"
RECEIPT_SCHEMA_ID = "ucns.edcm.external-evaluation-receipt"
PROTOCOL_VERSION = "1.0.0"
MAX_RECEIPT_EXCERPT_BYTES = 16_384


class ExternalEvaluationError(ValueError):
    pass


def _text(value: str, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ExternalEvaluationError(f"{field} must be nonempty text")
    return value


def _sha(value: str, field: str) -> str:
    if not isinstance(value, str) or len(value) != 64:
        raise ExternalEvaluationError(f"{field} must be a SHA-256 digest")
    try:
        int(value, 16)
    except ValueError as exc:
        raise ExternalEvaluationError(f"{field} must be hexadecimal") from exc
    return value.lower()


def _canonical(value: object) -> bytes:
    try:
        return json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ExternalEvaluationError("external evaluation evidence must be canonical JSON") from exc


def _digest(value: bytes) -> str:
    return sha256(value).hexdigest()


@dataclass(frozen=True, slots=True)
class ExternalEvaluatorIdentity:
    evaluator_id: str
    evaluator_version: str
    code_reference: str
    executable_sha256: str
    protocol_version: str = PROTOCOL_VERSION

    def __post_init__(self) -> None:
        _text(self.evaluator_id, "evaluator_id")
        _text(self.evaluator_version, "evaluator_version")
        _text(self.code_reference, "code_reference")
        object.__setattr__(self, "executable_sha256", _sha(self.executable_sha256, "executable_sha256"))
        if self.protocol_version != PROTOCOL_VERSION:
            raise ExternalEvaluationError("unsupported evaluator protocol version")


@dataclass(frozen=True, slots=True)
class ExternalEvaluatorCommand:
    argv: tuple[str, ...]
    timeout_seconds: int
    max_input_bytes: int
    max_output_bytes: int
    environment_keys: tuple[str, ...] = ()
    network_policy: str = "caller-isolated"

    def __post_init__(self) -> None:
        argv = tuple(self.argv)
        if not argv or any(not isinstance(item, str) or not item for item in argv):
            raise ExternalEvaluationError("argv requires nonempty text entries")
        executable = Path(argv[0])
        if not executable.is_absolute():
            raise ExternalEvaluationError("evaluator executable path must be absolute")
        if any(isinstance(value, bool) or not isinstance(value, int) or value <= 0 for value in (
            self.timeout_seconds, self.max_input_bytes, self.max_output_bytes,
        )):
            raise ExternalEvaluationError("resource bounds must be positive integers")
        keys = tuple(self.environment_keys)
        if len(set(keys)) != len(keys) or any(not key or "=" in key for key in keys):
            raise ExternalEvaluationError("environment keys must be unique valid names")
        if self.network_policy not in {"caller-isolated", "declared-external"}:
            raise ExternalEvaluationError("unknown network policy")
        object.__setattr__(self, "argv", argv)
        object.__setattr__(self, "environment_keys", keys)


@dataclass(frozen=True, slots=True)
class ExternalEvaluationCase:
    case_id: str
    subject_digest: str
    custody_reference: str
    disclosure_authority_id: str
    payload: Any

    def __post_init__(self) -> None:
        _text(self.case_id, "case_id")
        object.__setattr__(self, "subject_digest", _sha(self.subject_digest, "subject_digest"))
        _text(self.custody_reference, "custody_reference")
        _text(self.disclosure_authority_id, "disclosure_authority_id")
        _canonical(self.payload)

    def request_value(self) -> dict[str, object]:
        return {
            "case_id": self.case_id, "subject_digest": self.subject_digest,
            "custody_reference": self.custody_reference,
            "disclosure_authority_id": self.disclosure_authority_id,
            "payload": self.payload,
        }


@dataclass(frozen=True, slots=True)
class ExternalEvaluationPlan:
    plan_id: str
    plan_version: str
    question: str
    corpus_receipt: FullCorpusCompletionReceipt
    evaluator: ExternalEvaluatorIdentity
    command: ExternalEvaluatorCommand
    cases: tuple[ExternalEvaluationCase, ...]

    def __post_init__(self) -> None:
        _text(self.plan_id, "plan_id")
        _text(self.plan_version, "plan_version")
        _text(self.question, "question")
        if not isinstance(self.corpus_receipt, FullCorpusCompletionReceipt):
            raise ExternalEvaluationError("plan requires a FullCorpusCompletionReceipt")
        if not isinstance(self.evaluator, ExternalEvaluatorIdentity):
            raise ExternalEvaluationError("plan requires ExternalEvaluatorIdentity")
        if not isinstance(self.command, ExternalEvaluatorCommand):
            raise ExternalEvaluationError("plan requires ExternalEvaluatorCommand")
        cases = tuple(self.cases)
        if not cases or any(not isinstance(case, ExternalEvaluationCase) for case in cases):
            raise ExternalEvaluationError("plan requires at least one external evaluation case")
        ids = tuple(case.case_id for case in cases)
        if len(set(ids)) != len(ids):
            raise ExternalEvaluationError("external evaluation case ids must be unique")
        object.__setattr__(self, "cases", cases)

    def request(self) -> dict[str, object]:
        manifest = self.corpus_receipt.report.manifest
        return {
            "schema_id": REQUEST_SCHEMA_ID, "schema_version": PROTOCOL_VERSION,
            "plan_id": self.plan_id, "plan_version": self.plan_version,
            "question": self.question,
            "upstream": {
                "completion_receipt_id": self.corpus_receipt.receipt_id,
                "corpus_manifest_evidence_identity": list(manifest.evidence_identity),
            },
            "evaluator": {
                "evaluator_id": self.evaluator.evaluator_id,
                "evaluator_version": self.evaluator.evaluator_version,
                "code_reference": self.evaluator.code_reference,
                "executable_sha256": self.evaluator.executable_sha256,
                "protocol_version": self.evaluator.protocol_version,
            },
            "execution": {
                "argv": list(self.command.argv),
                "environment_keys": list(self.command.environment_keys),
                "network_policy": self.command.network_policy,
                "timeout_seconds": self.command.timeout_seconds,
                "max_input_bytes": self.command.max_input_bytes,
                "max_output_bytes": self.command.max_output_bytes,
            },
            "cases": [case.request_value() for case in self.cases],
        }


class ExternalEvaluationStatus(str, Enum):
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"


@dataclass(frozen=True, slots=True)
class ExternalEvaluationReceipt:
    plan_id: str
    status: ExternalEvaluationStatus
    upstream_completion_receipt_id: str
    evaluator_id: str
    evaluator_version: str
    request_sha256: str
    stdout_sha256: str
    stderr_sha256: str
    stdout_bytes: int
    stderr_bytes: int
    stdout_excerpt: str
    stderr_excerpt: str
    elapsed_seconds: float
    returncode: int | None
    timed_out: bool
    response_results: tuple[dict[str, Any], ...]
    failure: str | None
    selection_effect: str = "none"
    measurement_validity: str = "not-established"
    edcm_activation: str = "inactive"
    canon_status: str = "none"
    evidence_status: str = "candidate-measured-evidence"

    def __post_init__(self) -> None:
        object.__setattr__(self, "status", ExternalEvaluationStatus(self.status))
        _text(self.plan_id, "plan_id")
        _sha(self.upstream_completion_receipt_id, "upstream_completion_receipt_id")
        _text(self.evaluator_id, "evaluator_id")
        _text(self.evaluator_version, "evaluator_version")
        for field, value in (
            ("request_sha256", self.request_sha256),
            ("stdout_sha256", self.stdout_sha256),
            ("stderr_sha256", self.stderr_sha256),
        ):
            _sha(value, field)
        if self.status is ExternalEvaluationStatus.COMPLETE and (
            self.failure is not None or self.timed_out or self.returncode != 0
        ):
            raise ExternalEvaluationError("complete receipt requires successful reconciled execution")
        if self.status is ExternalEvaluationStatus.INCOMPLETE and self.failure is None:
            raise ExternalEvaluationError("incomplete receipt requires visible failure evidence")
        if (
            self.selection_effect != "none"
            or self.measurement_validity != "not-established"
            or self.edcm_activation != "inactive"
            or self.canon_status != "none"
            or self.evidence_status != "candidate-measured-evidence"
        ):
            raise ExternalEvaluationError("external evaluation receipt cannot promote evidence")

    @property
    def receipt_id(self) -> str:
        return _digest(_canonical({
            "schema_id": RECEIPT_SCHEMA_ID, "schema_version": PROTOCOL_VERSION,
            "plan_id": self.plan_id, "status": self.status.value,
            "upstream_completion_receipt_id": self.upstream_completion_receipt_id,
            "evaluator_id": self.evaluator_id, "evaluator_version": self.evaluator_version,
            "request_sha256": self.request_sha256, "stdout_sha256": self.stdout_sha256,
            "stderr_sha256": self.stderr_sha256, "stdout_bytes": self.stdout_bytes,
            "stderr_bytes": self.stderr_bytes, "returncode": self.returncode,
            "timed_out": self.timed_out, "response_results": self.response_results,
            "failure": self.failure, "selection_effect": self.selection_effect,
            "measurement_validity": self.measurement_validity,
            "edcm_activation": self.edcm_activation, "canon_status": self.canon_status,
            "evidence_status": self.evidence_status,
        }))


def _file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _bounded_excerpt(data: bytes) -> str:
    excerpt = data[:MAX_RECEIPT_EXCERPT_BYTES].decode("utf-8", errors="replace")
    if len(data) > MAX_RECEIPT_EXCERPT_BYTES:
        excerpt += f"\n[truncated {len(data) - MAX_RECEIPT_EXCERPT_BYTES} bytes]"
    return excerpt


def _validate_response(plan: ExternalEvaluationPlan, value: object) -> tuple[dict[str, Any], ...]:
    if not isinstance(value, dict):
        raise ExternalEvaluationError("response must be a JSON object")
    expected_keys = {"schema_id", "schema_version", "plan_id", "evaluator", "results"}
    if set(value) != expected_keys:
        raise ExternalEvaluationError("response fields do not match protocol")
    if value["schema_id"] != RESPONSE_SCHEMA_ID or value["schema_version"] != PROTOCOL_VERSION:
        raise ExternalEvaluationError("response protocol mismatch")
    if value["plan_id"] != plan.plan_id:
        raise ExternalEvaluationError("response plan mismatch")
    if value["evaluator"] != {
        "evaluator_id": plan.evaluator.evaluator_id,
        "evaluator_version": plan.evaluator.evaluator_version,
    }:
        raise ExternalEvaluationError("response evaluator mismatch")
    results = value["results"]
    if not isinstance(results, list):
        raise ExternalEvaluationError("response results must be a list")
    expected_ids = [case.case_id for case in plan.cases]
    actual_ids: list[str] = []
    normalized: list[dict[str, Any]] = []
    for result in results:
        if not isinstance(result, dict) or set(result) != {"case_id", "status", "output", "evidence", "error"}:
            raise ExternalEvaluationError("result fields do not match protocol")
        if result["status"] not in {"ok", "unresolved", "error"}:
            raise ExternalEvaluationError("unknown result status")
        if not isinstance(result["evidence"], list) or any(not isinstance(item, str) or not item for item in result["evidence"]):
            raise ExternalEvaluationError("result evidence must be nonempty text entries")
        if result["status"] == "error" and not isinstance(result["error"], str):
            raise ExternalEvaluationError("error result requires error text")
        if result["status"] != "error" and result["error"] is not None:
            raise ExternalEvaluationError("non-error result cannot carry error text")
        _canonical(result["output"])
        actual_ids.append(result["case_id"])
        normalized.append(result)
    if actual_ids != expected_ids:
        raise ExternalEvaluationError("response must cover every case exactly once in order")
    return tuple(normalized)


def execute_external_evaluation(
    plan: ExternalEvaluationPlan, *, environment: Mapping[str, str] = (),
) -> ExternalEvaluationReceipt:
    if not isinstance(plan, ExternalEvaluationPlan):
        raise ExternalEvaluationError("execute requires ExternalEvaluationPlan")
    supplied_environment = dict(environment)
    if set(supplied_environment) != set(plan.command.environment_keys):
        raise ExternalEvaluationError("supplied environment keys do not match declaration")
    if any(not isinstance(value, str) for value in supplied_environment.values()):
        raise ExternalEvaluationError("environment values must be text")
    executable = Path(plan.command.argv[0]).resolve()
    if not executable.is_file() or _file_sha256(executable) != plan.evaluator.executable_sha256:
        raise ExternalEvaluationError("evaluator executable digest mismatch")
    request_bytes = _canonical(plan.request())
    if len(request_bytes) > plan.command.max_input_bytes:
        raise ExternalEvaluationError("canonical request exceeds max_input_bytes")

    started = time.monotonic()
    timed_out = False
    returncode: int | None = None
    failure: str | None = None
    results: tuple[dict[str, Any], ...] = ()
    with tempfile.TemporaryDirectory(prefix="ucns-external-evaluation-") as temporary:
        stdout_path = Path(temporary) / "stdout"
        stderr_path = Path(temporary) / "stderr"

        def limit_output() -> None:
            resource.setrlimit(resource.RLIMIT_FSIZE, (
                plan.command.max_output_bytes, plan.command.max_output_bytes,
            ))

        with stdout_path.open("wb") as stdout, stderr_path.open("wb") as stderr:
            process = subprocess.Popen(
                plan.command.argv, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr,
                env=supplied_environment, start_new_session=True, preexec_fn=limit_output,
            )
            try:
                process.communicate(
                    input=request_bytes, timeout=plan.command.timeout_seconds
                )
                returncode = process.returncode
            except subprocess.TimeoutExpired:
                timed_out = True
                failure = "timeout"
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.communicate()
                returncode = process.returncode
        stdout_bytes_value = stdout_path.read_bytes()
        stderr_bytes_value = stderr_path.read_bytes()

    elapsed = round(time.monotonic() - started, 6)
    if len(stdout_bytes_value) > plan.command.max_output_bytes or len(stderr_bytes_value) > plan.command.max_output_bytes:
        failure = failure or "evaluator output exceeded bound"
    if failure is None and returncode != 0:
        failure = f"evaluator exited with status {returncode}"
    if failure is None:
        try:
            response = json.loads(stdout_bytes_value.decode("utf-8"))
            results = _validate_response(plan, response)
        except (UnicodeDecodeError, json.JSONDecodeError, ExternalEvaluationError) as exc:
            failure = f"response reconciliation failed: {exc}"

    return ExternalEvaluationReceipt(
        plan.plan_id,
        ExternalEvaluationStatus.COMPLETE if failure is None else ExternalEvaluationStatus.INCOMPLETE,
        plan.corpus_receipt.receipt_id, plan.evaluator.evaluator_id,
        plan.evaluator.evaluator_version, _digest(request_bytes),
        _digest(stdout_bytes_value), _digest(stderr_bytes_value),
        len(stdout_bytes_value), len(stderr_bytes_value),
        _bounded_excerpt(stdout_bytes_value), _bounded_excerpt(stderr_bytes_value),
        elapsed, returncode, timed_out, results, failure,
    )


__all__ = [
    "PROTOCOL_VERSION", "RECEIPT_SCHEMA_ID", "REQUEST_SCHEMA_ID",
    "RESPONSE_SCHEMA_ID", "ExternalEvaluationCase", "ExternalEvaluationError",
    "ExternalEvaluationPlan", "ExternalEvaluationReceipt", "ExternalEvaluationStatus",
    "ExternalEvaluatorCommand", "ExternalEvaluatorIdentity", "execute_external_evaluation",
]
