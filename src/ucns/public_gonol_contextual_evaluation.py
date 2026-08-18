# === MODULE_BUILD ===
# id: ucns_public_gonol_contextual_evaluation
#   module_name: public_gonol_contextual_evaluation
#   module_kind: experiment
#   summary: executes the resource-run-compliant Public Gonol contextual structural protocol with two source rebuilds and an independent direct application replay
#   owner: Erin Spencer
#   public_surface: execute_public_gonol_contextual_protocol, semantic_evaluation_bytes, resource_observation_bytes, main
#   internal_surface: _resource_preflight, _validated_source_build, _evaluate_table, _direct_contextual_application, _resource_observation
#   auth_boundary: frozen Public Gonol contextual protocol only; evaluator cannot revise it
#   storage_boundary: caller-selected deterministic semantic receipt plus separate runtime observation receipt
#   network_boundary: none; exact local OEWN source checkout required
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol_contextual_evaluation
#   rollout: child execution of resource-run repair protocol superseding the historical 420-second blocked execution
#   rollback: remove execution output while preserving protocol, source receipts, and recorded result evidence
#   requires: ucns_public_gonol_contextual_protocol, ucns_public_gonol_function_table
#   since: 2026-08-18
#   unresolved: semantic usefulness, source-authorized context selection, grammar, parsing, precedence, and canonical semantics
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: public_gonol_contextual_evaluation_consumes_merged_protocol
#   given: the contextual structural evaluator is executed
#   then: it accepts only the exact resource-run-compliant protocol sources, anchor, target set, contexts, control, thresholds, and natural terminal stopping rule
#   class: safety
#   since: 2026-08-18
#
# id: public_gonol_contextual_evaluation_replays_source_and_application_independently
#   given: a complete OEWN source build is evaluated
#   then: two full source builds and a direct construction replay agree with the public function application for every frozen target and ordered context
#   class: evidence
#   since: 2026-08-18
#
# id: public_gonol_contextual_evaluation_preserves_nonclaim_boundary
#   given: the structural control survives or fails
#   then: the result is limited to exact identity discrimination relative to the identity-only control and cannot establish usefulness, grammar, parsing, precedence, measurement validity, or canon
#   class: doctrine
#   since: 2026-08-18
# === END CONTRACTS ===

"""Execute the Public Gonol contextual structural evaluation.

The deterministic semantic receipt intentionally excludes elapsed time and peak
memory so the two independent source builds can be compared byte-for-byte.
Those runtime observations are emitted in a separate receipt.  The resource-run
repair protocol deliberately applies no artificial wall-clock or memory cutoff:
resource scarcity is preflighted before launch, and a started healthy run is
allowed to reach its natural terminal condition.  This module evaluates the
frozen table; it does not interpret punctuation or introduce a grammar.

Usage:
    python -m ucns.public_gonol_contextual_evaluation SOURCE_REPO SEMANTIC_JSON RESOURCES_JSON

Run only after resource preflight supports completing both full source builds.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import argparse
import json
import os
from pathlib import Path
from time import perf_counter_ns
import resource
import shutil
from typing import Mapping, Sequence

from .edcm import public_gonol_sha256
from .lexical_sources import LexicalSourceError, verify_oewn_2025_core
from .oewn_core import load_oewn_core
from .oewn_definition_recursion import build_oewn_definition_layer, definition_layer_bytes
from .public_gonol_contextual_protocol import (
    BLOCKED_STATUS,
    NEGATIVE_STATUS,
    POSITIVE_STATUS,
    PUBLIC_GONOL_CONTEXTUAL_PROTOCOL,
    PublicGonolContextualProtocol,
)
from .public_gonol_functions import (
    APPLICATION_STANDING,
    CONTEXT_RELATION_CODE,
    FUNCTION_RELATION_CODE,
    AtomicFunctionState,
    ContextualFunctionApplication,
    PublicGonolFunctionError,
    PublicGonolFunctionTable,
    apply_public_gonol_function,
    build_public_gonol_function_table,
    function_table_bytes,
)
from .relational_carrier import build_relational_carrier

EVALUATION_SCHEMA_ID = "ucns.public-gonol-contextual-evaluation"
RESOURCE_SCHEMA_ID = "ucns.public-gonol-contextual-resource-observations"
EVALUATION_SCHEMA_VERSION = "1.0.0"
MERGED_PROTOCOL_COMMIT = "e97617c360a6a1d783f3f89f60a23194846b98aa"
EVALUATION_STANDING = "frozen-contextual-structural-control-result"


class PublicGonolContextualEvaluationError(ValueError):
    """Raised for a non-resource evaluator inconsistency."""


class PublicGonolContextualEvaluationBlocked(RuntimeError):
    """Raised when exact source evidence or preflight requirements are absent."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"


def _identity(prefix: str, value: object) -> str:
    return prefix + sha256(_canonical_bytes(value)).hexdigest()


@dataclass(frozen=True, slots=True)
class _SourceBuild:
    table: PublicGonolFunctionTable
    source_receipt_id: str
    definition_layer_id: str
    table_id: str


@dataclass(frozen=True, slots=True)
class _SemanticRun:
    payload: Mapping[str, object]
    receipt_bytes: bytes
    status: str


def _direct_contextual_application(
    table: PublicGonolFunctionTable,
    public_gonol_index: int,
    current_state: AtomicFunctionState,
    ordered_context_gonol_ids: tuple[str, ...],
) -> ContextualFunctionApplication:
    """Reconstruct one closure directly, without calling the public applicator."""

    function = table.by_index.get(public_gonol_index)
    if function is None:
        raise PublicGonolContextualEvaluationError("frozen functional index is absent")
    definition_ids = tuple(
        identifier
        for binding in function.bindings
        for identifier in binding.definition_gonol_ids
    )
    node_count = 1 + len(definition_ids) + len(ordered_context_gonol_ids)
    edges = [(0, FUNCTION_RELATION_CODE, offset + 1) for offset in range(len(definition_ids))]
    context_offset = 1 + len(definition_ids)
    edges.extend(
        (0, CONTEXT_RELATION_CODE, context_offset + offset)
        for offset in range(len(ordered_context_gonol_ids))
    )
    return ContextualFunctionApplication(
        prior_atomic_gonol_id=current_state.atomic_gonol_id,
        prior_application_depth=current_state.application_depth,
        public_gonol_index=public_gonol_index,
        function_id=function.function_id,
        definition_gonol_ids=definition_ids,
        ordered_context_gonol_ids=ordered_context_gonol_ids,
        carrier=build_relational_carrier(node_count, edges),
        atomic_at_next_application=True,
        standing=APPLICATION_STANDING,
    )


def _anchor_definition_id(
    table: PublicGonolFunctionTable,
    protocol: PublicGonolContextualProtocol,
) -> str:
    try:
        function = table.by_index[protocol.anchor_function_index]
        binding = function.bindings[protocol.anchor_binding_ordinal]
        return binding.definition_gonol_ids[protocol.anchor_definition_ordinal]
    except (IndexError, KeyError) as error:  # frozen table unexpectedly incomplete
        raise PublicGonolContextualEvaluationError("frozen anchor is absent from function table") from error


def _context_ids(anchor_id: str, multiplicity: int) -> tuple[str, ...]:
    return (anchor_id,) * multiplicity


def _metric_payload(
    table: PublicGonolFunctionTable,
    protocol: PublicGonolContextualProtocol,
) -> Mapping[str, object]:
    """Evaluate all frozen contexts and verify direct replay per application."""

    anchor_id = _anchor_definition_id(table, protocol)
    initial_state = AtomicFunctionState(anchor_id)
    candidate_by_context: dict[str, tuple[tuple[int, str], ...]] = {}
    baseline_by_context: dict[str, tuple[tuple[int, str], ...]] = {}
    direct_replay_agrees = True
    for label, multiplicity in protocol.contexts:
        context = _context_ids(anchor_id, multiplicity)
        candidate_rows: list[tuple[int, str]] = []
        baseline_rows: list[tuple[int, str]] = []
        for index in protocol.target_indices:
            primary = apply_public_gonol_function(table, index, initial_state, context)
            replay = _direct_contextual_application(table, index, initial_state, context)
            if primary.result_atomic_gonol_id != replay.result_atomic_gonol_id:
                direct_replay_agrees = False
            candidate_rows.append((index, primary.result_atomic_gonol_id))
            baseline_rows.append((index, initial_state.atomic_gonol_id))
        candidate_by_context[label] = tuple(candidate_rows)
        baseline_by_context[label] = tuple(baseline_rows)

    candidate_counts = {
        label: len({result for _, result in rows})
        for label, rows in candidate_by_context.items()
    }
    baseline_counts = {
        label: len({result for _, result in rows})
        for label, rows in baseline_by_context.items()
    }
    candidate_changes = 0
    baseline_changes = 0
    labels = tuple(label for label, _ in protocol.contexts)
    for index in protocol.target_indices:
        for previous, following in zip(labels, labels[1:]):
            candidate_before = dict(candidate_by_context[previous])[index]
            candidate_after = dict(candidate_by_context[following])[index]
            baseline_before = dict(baseline_by_context[previous])[index]
            baseline_after = dict(baseline_by_context[following])[index]
            candidate_changes += candidate_before != candidate_after
            baseline_changes += baseline_before != baseline_after

    required_changes = (
        len(protocol.target_indices) * protocol.required_context_changes_per_index
    )
    candidate_passes = (
        direct_replay_agrees
        and all(count == protocol.required_target_distinct_results for count in candidate_counts.values())
        and candidate_changes == required_changes
    )
    baseline_passes = (
        all(count == protocol.required_baseline_distinct_results for count in baseline_counts.values())
        and baseline_changes == 0
    )
    strict_control_advantage = (
        candidate_passes
        and baseline_passes
        and protocol.required_target_distinct_results > protocol.required_baseline_distinct_results
        and candidate_changes > baseline_changes
    )
    status = POSITIVE_STATUS if strict_control_advantage else NEGATIVE_STATUS
    return {
        "anchor_definition_gonol_id": anchor_id,
        "initial_atomic_state": {
            "atomic_gonol_id": initial_state.atomic_gonol_id,
            "application_depth": initial_state.application_depth,
        },
        "candidate_result_ids": {
            label: [{"public_gonol_index": index, "result_atomic_gonol_id": result}
                    for index, result in rows]
            for label, rows in candidate_by_context.items()
        },
        "identity_only_control_result_ids": {
            label: [{"public_gonol_index": index, "result_atomic_gonol_id": result}
                    for index, result in rows]
            for label, rows in baseline_by_context.items()
        },
        "metrics": {
            "candidate_distinct_results_by_context": candidate_counts,
            "identity_only_distinct_results_by_context": baseline_counts,
            "candidate_context_changes": candidate_changes,
            "identity_only_context_changes": baseline_changes,
            "required_candidate_context_changes": required_changes,
            "direct_application_replay_agrees": direct_replay_agrees,
        },
        "status": status,
    }


def _validated_source_build(
    source_repo: str | Path,
    protocol: PublicGonolContextualProtocol,
) -> _SourceBuild:
    """Rebuild and validate every producer identity required by the protocol."""

    try:
        source_receipt = verify_oewn_2025_core(source_repo)
    except LexicalSourceError as error:
        raise PublicGonolContextualEvaluationBlocked(str(error)) from error
    if source_receipt.receipt_id != protocol.oewn_source_receipt_id:
        raise PublicGonolContextualEvaluationBlocked("OEWN source receipt differs from frozen protocol")
    snapshot = load_oewn_core(source_repo, source_receipt)
    definition_layer = build_oewn_definition_layer(snapshot)
    if definition_layer.layer_id != protocol.definition_layer_id:
        raise PublicGonolContextualEvaluationBlocked("OEWN definition layer differs from frozen protocol")
    if sha256(definition_layer_bytes(definition_layer)).hexdigest() != protocol.definition_layer_receipt_sha256:
        raise PublicGonolContextualEvaluationBlocked("OEWN definition-layer receipt differs from frozen protocol")
    table = build_public_gonol_function_table(snapshot, definition_layer)
    if table.table_id != protocol.table_id:
        raise PublicGonolContextualEvaluationBlocked("function table differs from frozen protocol")
    if sha256(function_table_bytes(table)).hexdigest() != protocol.table_receipt_sha256:
        raise PublicGonolContextualEvaluationBlocked("function-table receipt differs from frozen protocol")
    if public_gonol_sha256() != protocol.public_gonol_sha256:
        raise PublicGonolContextualEvaluationBlocked("Public Gonol differs from frozen protocol")
    return _SourceBuild(
        table=table,
        source_receipt_id=source_receipt.receipt_id,
        definition_layer_id=definition_layer.layer_id,
        table_id=table.table_id,
    )


def _meminfo_available_bytes() -> int | None:
    meminfo = Path("/proc/meminfo")
    if not meminfo.is_file():
        return None
    for line in meminfo.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("MemAvailable:"):
            parts = line.split()
            if len(parts) >= 2:
                return int(parts[1]) * 1024
    return None


def _resource_preflight(source_repo: str | Path) -> Mapping[str, object]:
    """Inspect scarce resources before launching the complete compute run."""

    source_path = Path(source_repo)
    source_exists = source_path.is_dir()
    worktree_usage = shutil.disk_usage(Path.cwd())
    source_usage = shutil.disk_usage(source_path if source_exists else Path.cwd())
    return {
        "source_repo": str(source_path),
        "source_repo_exists": source_exists,
        "cpu_count": os.cpu_count(),
        "mem_available_bytes": _meminfo_available_bytes(),
        "worktree_free_bytes": worktree_usage.free,
        "source_filesystem_free_bytes": source_usage.free,
        "network_required": False,
        "api_quota_required": False,
        "artificial_wall_clock_limit": None,
        "artificial_memory_limit_bytes": None,
        "stopping_rule": "natural terminal condition",
        "can_start": source_exists,
        "failure_reason": None if source_exists else "exact local OEWN source checkout is absent",
    }


def _resource_observation(
    ordinal: int,
    started_ns: int,
    protocol: PublicGonolContextualProtocol,
    terminal_condition: str,
) -> Mapping[str, object]:
    elapsed_ns = perf_counter_ns() - started_ns
    peak_memory_bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    return {
        "full_source_build_ordinal": ordinal,
        "elapsed_nanoseconds": elapsed_ns,
        "peak_process_memory_bytes": peak_memory_bytes,
        "terminal_condition": terminal_condition,
        "resource_run_doctrine_id": protocol.resource_run_doctrine_id,
        "wall_clock_stopping_rule": protocol.wall_clock_stopping_rule,
        "memory_stopping_rule": protocol.memory_stopping_rule,
        "artificial_resource_limit_applied": protocol.artificial_resource_limit_applied,
    }


def _semantic_run(
    source_repo: str | Path,
    protocol: PublicGonolContextualProtocol,
    ordinal: int,
) -> tuple[_SemanticRun | None, Mapping[str, object], str | None]:
    started_ns = perf_counter_ns()
    try:
        source_build = _validated_source_build(source_repo, protocol)
        metric = _metric_payload(source_build.table, protocol)
    except PublicGonolContextualEvaluationBlocked as error:
        resource_observation = _resource_observation(
            ordinal, started_ns, protocol, "blocked-before-complete-source-build",
        )
        return None, resource_observation, str(error)
    except PublicGonolFunctionError as error:
        resource_observation = _resource_observation(
            ordinal, started_ns, protocol, "function-table-construction-error",
        )
        return None, resource_observation, f"function-table construction failed: {error}"
    resource_observation = _resource_observation(
        ordinal, started_ns, protocol, "completed-source-build-and-contextual-metric",
    )
    payload = {
        "schema_id": EVALUATION_SCHEMA_ID,
        "schema_version": EVALUATION_SCHEMA_VERSION,
        "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
        "protocol_id": protocol.protocol_id,
        "source_receipt_id": source_build.source_receipt_id,
        "definition_layer_id": source_build.definition_layer_id,
        "table_id": source_build.table_id,
        "public_gonol_sha256": protocol.public_gonol_sha256,
        "metric": metric,
        "standing": EVALUATION_STANDING,
        "nonclaims": list(protocol.as_payload()["nonclaims"]),
    }
    receipt_bytes = _canonical_bytes({
        "semantic_run_id": _identity("ucns.public-gonol-contextual-semantic-run:sha256:", payload),
        **payload,
    })
    return _SemanticRun(payload=payload, receipt_bytes=receipt_bytes, status=metric["status"]), resource_observation, None


def semantic_evaluation_bytes(
    payload: Mapping[str, object],
) -> bytes:
    """Serialize only deterministic source/result evidence for byte comparison."""

    return _canonical_bytes({
        "evaluation_id": _identity("ucns.public-gonol-contextual-evaluation:sha256:", payload),
        **payload,
    })


def resource_observation_bytes(payload: Mapping[str, object]) -> bytes:
    """Serialize observed runtime facts separately from deterministic evidence."""

    return _canonical_bytes({
        "resource_observation_id": _identity(
            "ucns.public-gonol-contextual-resource-observations:sha256:", payload,
        ),
        **payload,
    })


def execute_public_gonol_contextual_protocol(
    source_repo: str | Path,
    protocol: PublicGonolContextualProtocol = PUBLIC_GONOL_CONTEXTUAL_PROTOCOL,
) -> tuple[bytes, bytes]:
    """Execute the immutable protocol and return semantic plus resource receipts."""

    if protocol != PUBLIC_GONOL_CONTEXTUAL_PROTOCOL:
        raise PublicGonolContextualEvaluationError("only the merged frozen protocol is admissible")
    preflight = _resource_preflight(source_repo)
    resources: list[Mapping[str, object]] = []
    if preflight["can_start"] is not True:
        semantic_payload = {
            "schema_id": EVALUATION_SCHEMA_ID,
            "schema_version": EVALUATION_SCHEMA_VERSION,
            "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
            "protocol_id": protocol.protocol_id,
            "status": BLOCKED_STATUS,
            "blocked_reason": preflight["failure_reason"],
            "completed_full_source_builds": 0,
            "standing": EVALUATION_STANDING,
            "nonclaims": list(protocol.as_payload()["nonclaims"]),
        }
    else:
        runs: list[_SemanticRun | None] = []
        blockers: list[str | None] = []
        for ordinal in range(1, protocol.required_full_source_builds + 1):
            run, run_resources, blocker = _semantic_run(source_repo, protocol, ordinal)
            runs.append(run)
            resources.append(run_resources)
            blockers.append(blocker)
        complete_runs = [run for run in runs if run is not None]
        if len(complete_runs) != protocol.required_full_source_builds:
            semantic_payload = {
                "schema_id": EVALUATION_SCHEMA_ID,
                "schema_version": EVALUATION_SCHEMA_VERSION,
                "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
                "protocol_id": protocol.protocol_id,
                "status": BLOCKED_STATUS,
                "blocked_reasons": [reason for reason in blockers if reason is not None],
                "completed_full_source_builds": len(complete_runs),
                "standing": EVALUATION_STANDING,
                "nonclaims": list(protocol.as_payload()["nonclaims"]),
            }
        else:
            first, second = complete_runs
            byte_identical = first.receipt_bytes == second.receipt_bytes
            run_statuses = [first.status, second.status]
            semantic_run_hashes = [
                sha256(first.receipt_bytes).hexdigest(),
                sha256(second.receipt_bytes).hexdigest(),
            ]
            if all(status == POSITIVE_STATUS for status in run_statuses) and byte_identical:
                status = POSITIVE_STATUS
                semantic_run = first.payload
            else:
                status = NEGATIVE_STATUS
                semantic_run = first.payload if byte_identical else None
            semantic_payload = {
                "schema_id": EVALUATION_SCHEMA_ID,
                "schema_version": EVALUATION_SCHEMA_VERSION,
                "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
                "protocol_id": protocol.protocol_id,
                "status": status,
                "completed_full_source_builds": len(complete_runs),
                "semantic_run_receipt_sha256": semantic_run_hashes[0],
                "first_semantic_run_receipt_sha256": semantic_run_hashes[0],
                "second_semantic_run_receipt_sha256": semantic_run_hashes[1],
                "run_statuses": run_statuses,
                "byte_identical_independent_replay": byte_identical,
                "semantic_run": semantic_run,
                "standing": EVALUATION_STANDING,
                "nonclaims": list(protocol.as_payload()["nonclaims"]),
            }
    semantic_bytes = semantic_evaluation_bytes(semantic_payload)
    resource_payload = {
        "schema_id": RESOURCE_SCHEMA_ID,
        "schema_version": EVALUATION_SCHEMA_VERSION,
        "semantic_evaluation_sha256": sha256(semantic_bytes).hexdigest(),
        "resource_preflight": preflight,
        "resource_observations": resources,
        "all_observations_reached_natural_terminal_condition": all(
            item["terminal_condition"] == "completed-source-build-and-contextual-metric"
            for item in resources
        ),
        "artificial_resource_limit_applied": protocol.artificial_resource_limit_applied,
    }
    return semantic_bytes, resource_observation_bytes(resource_payload)


def main(argv: Sequence[str] | None = None) -> int:
    """Write a deterministic semantic receipt and separate runtime observations."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_repo", help="exact local OEWN 2025 Core checkout")
    parser.add_argument("semantic_output", help="deterministic evaluation receipt")
    parser.add_argument("resource_output", help="runtime observation receipt")
    args = parser.parse_args(argv)
    semantic, resources = execute_public_gonol_contextual_protocol(args.source_repo)
    semantic_path = Path(args.semantic_output)
    resource_path = Path(args.resource_output)
    semantic_path.parent.mkdir(parents=True, exist_ok=True)
    resource_path.parent.mkdir(parents=True, exist_ok=True)
    semantic_path.write_bytes(semantic)
    resource_path.write_bytes(resources)
    return 0


__all__ = [
    "EVALUATION_STANDING", "PublicGonolContextualEvaluationBlocked",
    "PublicGonolContextualEvaluationError", "execute_public_gonol_contextual_protocol",
    "main", "resource_observation_bytes", "semantic_evaluation_bytes",
]


if __name__ == "__main__":  # pragma: no cover - exercised through CLI integration
    raise SystemExit(main())
