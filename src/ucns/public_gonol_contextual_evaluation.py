# === MODULE_BUILD ===
# id: ucns_public_gonol_contextual_evaluation
#   module_name: public_gonol_contextual_evaluation
#   module_kind: experiment
#   summary: executes the merged frozen Public Gonol contextual structural protocol with two source rebuilds and an independent direct application replay
#   owner: Erin Spencer
#   public_surface: execute_public_gonol_contextual_protocol, semantic_evaluation_bytes, resource_observation_bytes, main
#   internal_surface: _validated_source_build, _evaluate_table, _direct_contextual_application, _resource_observation
#   auth_boundary: frozen Public Gonol contextual protocol only; evaluator cannot revise it
#   storage_boundary: caller-selected deterministic semantic receipt plus separate runtime observation receipt
#   network_boundary: none; exact local OEWN source checkout required
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol_contextual_evaluation
#   rollout: child execution of merged protocol a62de5bf2451d9ff0b7ff738566810c3dc796aae
#   rollback: remove execution output while preserving protocol, source receipts, and recorded result evidence
#   requires: ucns_public_gonol_contextual_protocol, ucns_public_gonol_function_table
#   since: 2026-08-18
#   unresolved: semantic usefulness, source-authorized context selection, grammar, parsing, precedence, and canonical semantics
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: public_gonol_contextual_evaluation_consumes_merged_protocol
#   given: the contextual structural evaluator is executed
#   then: it accepts only the exact merged protocol sources, anchor, target set, contexts, control, thresholds, and resource bounds
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

"""Execute the merged Public Gonol contextual structural evaluation.

The deterministic semantic receipt intentionally excludes elapsed time and peak
memory so the two independent source builds can be compared byte-for-byte.
Those runtime observations are emitted in a separate receipt and are still
enforced against the frozen limits.  This module evaluates the frozen table;
it does not interpret punctuation or introduce a grammar.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import argparse
from contextlib import contextmanager
import json
from pathlib import Path
from time import perf_counter_ns
import resource
import signal
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
MERGED_PROTOCOL_COMMIT = "a62de5bf2451d9ff0b7ff738566810c3dc796aae"
EVALUATION_STANDING = "frozen-contextual-structural-control-result"


class PublicGonolContextualEvaluationError(ValueError):
    """Raised for a non-resource evaluator inconsistency."""


class PublicGonolContextualEvaluationBlocked(RuntimeError):
    """Raised when exact source evidence or frozen resource bounds are absent."""


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


def _resource_observation(
    ordinal: int,
    started_ns: int,
    protocol: PublicGonolContextualProtocol,
) -> Mapping[str, object]:
    elapsed_ns = perf_counter_ns() - started_ns
    peak_memory_bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    within_limits = (
        elapsed_ns <= protocol.max_wall_seconds_per_build * 1_000_000_000
        and peak_memory_bytes <= protocol.max_memory_bytes_per_build
    )
    return {
        "full_source_build_ordinal": ordinal,
        "elapsed_nanoseconds": elapsed_ns,
        "peak_process_memory_bytes": peak_memory_bytes,
        "within_frozen_limits": within_limits,
    }


@contextmanager
def _wall_clock_limit(seconds: int):
    """Fail closed at the registered per-build wall-clock limit on POSIX."""

    if seconds <= 0:
        raise PublicGonolContextualEvaluationError("wall-clock limit must be positive")
    if not hasattr(signal, "setitimer"):
        raise PublicGonolContextualEvaluationBlocked(
            "POSIX wall-clock enforcement is unavailable for the frozen protocol",
        )

    def _expired(signum: int, frame: object) -> None:
        del signum, frame
        raise PublicGonolContextualEvaluationBlocked("frozen wall-clock bound exceeded")

    previous_handler = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, _expired)
    previous_timer = signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)
        if previous_timer != (0.0, 0.0):
            signal.setitimer(signal.ITIMER_REAL, *previous_timer)


def _semantic_run(
    source_repo: str | Path,
    protocol: PublicGonolContextualProtocol,
    ordinal: int,
) -> tuple[_SemanticRun | None, Mapping[str, object], str | None]:
    started_ns = perf_counter_ns()
    try:
        with _wall_clock_limit(protocol.max_wall_seconds_per_build):
            source_build = _validated_source_build(source_repo, protocol)
            metric = _metric_payload(source_build.table, protocol)
    except PublicGonolContextualEvaluationBlocked as error:
        resource_observation = _resource_observation(ordinal, started_ns, protocol)
        return None, resource_observation, str(error)
    except PublicGonolFunctionError as error:
        resource_observation = _resource_observation(ordinal, started_ns, protocol)
        return None, resource_observation, f"function-table construction failed: {error}"
    resource_observation = _resource_observation(ordinal, started_ns, protocol)
    if not resource_observation["within_frozen_limits"]:
        return None, resource_observation, "frozen resource bound exceeded"
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
    first, first_resources, first_blocker = _semantic_run(source_repo, protocol, 1)
    resources: list[Mapping[str, object]] = [first_resources]
    if first is None:
        semantic_payload = {
            "schema_id": EVALUATION_SCHEMA_ID,
            "schema_version": EVALUATION_SCHEMA_VERSION,
            "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
            "protocol_id": protocol.protocol_id,
            "status": BLOCKED_STATUS,
            "blocked_reason": first_blocker,
            "completed_full_source_builds": 1,
            "standing": EVALUATION_STANDING,
            "nonclaims": list(protocol.as_payload()["nonclaims"]),
        }
    elif first.status == NEGATIVE_STATUS:
        semantic_payload = {
            "schema_id": EVALUATION_SCHEMA_ID,
            "schema_version": EVALUATION_SCHEMA_VERSION,
            "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
            "protocol_id": protocol.protocol_id,
            "status": NEGATIVE_STATUS,
            "completed_full_source_builds": 1,
            "semantic_run_receipt_sha256": sha256(first.receipt_bytes).hexdigest(),
            "semantic_run": first.payload,
            "standing": EVALUATION_STANDING,
            "nonclaims": list(protocol.as_payload()["nonclaims"]),
        }
    else:
        second, second_resources, second_blocker = _semantic_run(source_repo, protocol, 2)
        resources.append(second_resources)
        if second is None:
            semantic_payload = {
                "schema_id": EVALUATION_SCHEMA_ID,
                "schema_version": EVALUATION_SCHEMA_VERSION,
                "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
                "protocol_id": protocol.protocol_id,
                "status": BLOCKED_STATUS,
                "blocked_reason": second_blocker,
                "completed_full_source_builds": 2,
                "first_semantic_run_receipt_sha256": sha256(first.receipt_bytes).hexdigest(),
                "standing": EVALUATION_STANDING,
                "nonclaims": list(protocol.as_payload()["nonclaims"]),
            }
        elif first.receipt_bytes != second.receipt_bytes:
            semantic_payload = {
                "schema_id": EVALUATION_SCHEMA_ID,
                "schema_version": EVALUATION_SCHEMA_VERSION,
                "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
                "protocol_id": protocol.protocol_id,
                "status": NEGATIVE_STATUS,
                "completed_full_source_builds": 2,
                "first_semantic_run_receipt_sha256": sha256(first.receipt_bytes).hexdigest(),
                "second_semantic_run_receipt_sha256": sha256(second.receipt_bytes).hexdigest(),
                "byte_identical_independent_replay": False,
                "standing": EVALUATION_STANDING,
                "nonclaims": list(protocol.as_payload()["nonclaims"]),
            }
        else:
            semantic_payload = {
                "schema_id": EVALUATION_SCHEMA_ID,
                "schema_version": EVALUATION_SCHEMA_VERSION,
                "merged_protocol_commit": MERGED_PROTOCOL_COMMIT,
                "protocol_id": protocol.protocol_id,
                "status": POSITIVE_STATUS,
                "completed_full_source_builds": 2,
                "semantic_run_receipt_sha256": sha256(first.receipt_bytes).hexdigest(),
                "semantic_run": first.payload,
                "byte_identical_independent_replay": True,
                "standing": EVALUATION_STANDING,
                "nonclaims": list(protocol.as_payload()["nonclaims"]),
            }
    semantic_bytes = semantic_evaluation_bytes(semantic_payload)
    resource_payload = {
        "schema_id": RESOURCE_SCHEMA_ID,
        "schema_version": EVALUATION_SCHEMA_VERSION,
        "semantic_evaluation_sha256": sha256(semantic_bytes).hexdigest(),
        "resource_observations": resources,
        "all_observations_within_frozen_limits": all(
            item["within_frozen_limits"] for item in resources
        ),
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
