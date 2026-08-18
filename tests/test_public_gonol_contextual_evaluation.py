# === CHECKS ===
# id: public_gonol_contextual_evaluation_control_check
#   proves: public_gonol_contextual_evaluation_consumes_merged_protocol, public_gonol_contextual_evaluation_preserves_nonclaim_boundary
#   call: self::test_metric_keeps_exact_index_and_context_control_separate
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: public_gonol_contextual_evaluation_direct_replay_check
#   proves: public_gonol_contextual_evaluation_replays_source_and_application_independently
#   call: self::test_direct_replay_matches_public_application_for_all_frozen_indices
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: public_gonol_contextual_evaluation_two_build_check
#   proves: public_gonol_contextual_evaluation_replays_source_and_application_independently
#   call: self::test_executor_runs_two_source_builds_before_decision
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: public_gonol_contextual_evaluation_resource_preflight_check
#   proves: public_gonol_contextual_evaluation_consumes_merged_protocol
#   call: self::test_resource_preflight_records_no_artificial_runtime_bound
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: public_gonol_contextual_evaluation_blocker_receipt_check
#   proves: public_gonol_contextual_evaluation_preserves_nonclaim_boundary
#   call: self::test_blocker_receipt_preserves_the_resource_breach_without_a_result
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: public_gonol_contextual_evaluation_result_receipt_check
#   proves: public_gonol_contextual_evaluation_replays_source_and_application_independently, public_gonol_contextual_evaluation_preserves_nonclaim_boundary
#   call: self::test_result_receipt_records_two_build_survival_without_claim_promotion
#   timeout: 20
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from hashlib import sha256
import json
from pathlib import Path

from ucns import public_gonol_contextual_evaluation as evaluation_module
from ucns.edcm import PUBLIC_GONOL_SHA256
from ucns.public_gonol_contextual_evaluation import (
    _SemanticRun,
    _direct_contextual_application,
    _metric_payload,
    _resource_preflight,
    execute_public_gonol_contextual_protocol,
    semantic_evaluation_bytes,
)
from ucns.public_gonol_contextual_protocol import PUBLIC_GONOL_CONTEXTUAL_PROTOCOL
from ucns.public_gonol_functions import (
    FUNCTIONAL_INDEX_NAMES,
    AtomicFunctionState,
    FunctionDefinitionBinding,
    PublicGonolFunction,
    PublicGonolFunctionTable,
    apply_public_gonol_function,
)


def _table() -> PublicGonolFunctionTable:
    functions = tuple(
        PublicGonolFunction(
            index,
            glyph,
            unicode_name,
            (FunctionDefinitionBinding(
                lexical_term=f"term-{index}",
                lexical_entry_keys=(f"entry-{index}",),
                definition_gonol_ids=(f"definition-{index}",),
            ),),
        )
        for index, glyph, unicode_name in FUNCTIONAL_INDEX_NAMES
    )
    return PublicGonolFunctionTable(
        source_receipt_id="synthetic-source",
        definition_layer_id="synthetic-definition-layer",
        functions=functions,
        public_gonol_sha256=PUBLIC_GONOL_SHA256,
    )


def test_metric_keeps_exact_index_and_context_control_separate() -> None:
    metric = _metric_payload(_table(), PUBLIC_GONOL_CONTEXTUAL_PROTOCOL)
    assert metric["status"] == "SURVIVED — not proved"
    assert metric["metrics"] == {
        "candidate_distinct_results_by_context": {
            "empty": 84, "anchor-once": 84, "anchor-twice": 84,
        },
        "identity_only_distinct_results_by_context": {
            "empty": 1, "anchor-once": 1, "anchor-twice": 1,
        },
        "candidate_context_changes": 168,
        "identity_only_context_changes": 0,
        "required_candidate_context_changes": 168,
        "direct_application_replay_agrees": True,
    }
    receipt = semantic_evaluation_bytes({"metric": metric})
    assert b'"semantic usefulness"' not in receipt
    assert '"status":"SURVIVED — not proved"'.encode("utf-8") in receipt


def test_direct_replay_matches_public_application_for_all_frozen_indices() -> None:
    table = _table()
    state = AtomicFunctionState("definition-2")
    for index in PUBLIC_GONOL_CONTEXTUAL_PROTOCOL.target_indices:
        for _, multiplicity in PUBLIC_GONOL_CONTEXTUAL_PROTOCOL.contexts:
            context = ("definition-2",) * multiplicity
            primary = apply_public_gonol_function(table, index, state, context)
            replay = _direct_contextual_application(table, index, state, context)
            assert replay.result_atomic_gonol_id == primary.result_atomic_gonol_id


def test_executor_runs_two_source_builds_before_decision(monkeypatch, tmp_path) -> None:
    calls: list[int] = []

    def fake_preflight(source_repo):
        return {"can_start": True, "failure_reason": None, "source_repo": str(source_repo)}

    def fake_semantic_run(source_repo, protocol, ordinal):
        del source_repo, protocol
        calls.append(ordinal)
        payload = {"metric": {"status": "FALSIFIED"}, "standing": "synthetic"}
        return (
            _SemanticRun(payload=payload, receipt_bytes=b"same-semantic-run\n", status="FALSIFIED"),
            {
                "full_source_build_ordinal": ordinal,
                "terminal_condition": "completed-source-build-and-contextual-metric",
            },
            None,
        )

    monkeypatch.setattr(evaluation_module, "_resource_preflight", fake_preflight)
    monkeypatch.setattr(evaluation_module, "_semantic_run", fake_semantic_run)
    semantic, resources = execute_public_gonol_contextual_protocol(tmp_path)
    semantic_payload = json.loads(semantic)
    resource_payload = json.loads(resources)
    assert calls == [1, 2]
    assert semantic_payload["status"] == "FALSIFIED"
    assert semantic_payload["completed_full_source_builds"] == 2
    assert semantic_payload["byte_identical_independent_replay"] is True
    assert resource_payload["all_observations_reached_natural_terminal_condition"] is True


def test_resource_preflight_records_no_artificial_runtime_bound(tmp_path) -> None:
    preflight = _resource_preflight(tmp_path)
    assert preflight["can_start"] is True
    assert preflight["source_repo_exists"] is True
    assert preflight["artificial_wall_clock_limit"] is None
    assert preflight["artificial_memory_limit_bytes"] is None
    assert preflight["stopping_rule"] == "natural terminal condition"


def test_blocker_receipt_preserves_the_resource_breach_without_a_result() -> None:
    artifact = Path(__file__).parents[1] / "generated" / "public-gonol-contextual-evaluation-blocker.json"
    payload = json.loads(artifact.read_text(encoding="utf-8"))
    identifier = payload.pop("blocker_id")
    digest = sha256(json.dumps(
        payload, ensure_ascii=False, allow_nan=False, sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n").hexdigest()
    assert identifier == f"ucns.public-gonol-contextual-evaluation-blocker:sha256:{digest}"
    assert payload["status"] == "BLOCKED"
    assert payload["completed_full_source_builds"] == 0
    assert payload["observation"]["emitted_semantic_receipt"] is False
    assert payload["observation"]["observed_process_elapsed_seconds_lower_bound"] > (
        payload["observation"]["frozen_max_wall_seconds_per_build"]
    )


def test_result_receipt_records_two_build_survival_without_claim_promotion() -> None:
    artifact = Path(__file__).parents[1] / "generated" / "public-gonol-contextual-evaluation-result.json"
    payload = json.loads(artifact.read_text(encoding="utf-8"))
    identifier = payload.pop("evaluation_id")
    digest = sha256(json.dumps(
        payload, ensure_ascii=False, allow_nan=False, sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n").hexdigest()
    assert identifier == f"ucns.public-gonol-contextual-evaluation:sha256:{digest}"
    assert payload["status"] == "SURVIVED — not proved"
    assert payload["completed_full_source_builds"] == 2
    assert payload["byte_identical_independent_replay"] is True
    assert payload["semantic_run_receipt_sha256"] == payload["second_semantic_run_receipt_sha256"]
    assert payload["semantic_run"]["metric"]["metrics"] == {
        "candidate_distinct_results_by_context": {
            "empty": 84, "anchor-once": 84, "anchor-twice": 84,
        },
        "identity_only_distinct_results_by_context": {
            "empty": 1, "anchor-once": 1, "anchor-twice": 1,
        },
        "candidate_context_changes": 168,
        "identity_only_context_changes": 0,
        "required_candidate_context_changes": 168,
        "direct_application_replay_agrees": True,
    }
    assert "semantic usefulness" in payload["nonclaims"]
    resource_artifact = (
        Path(__file__).parents[1]
        / "generated"
        / "public-gonol-contextual-resource-observations.json"
    )
    resource_payload = json.loads(resource_artifact.read_text(encoding="utf-8"))
    assert resource_payload["semantic_evaluation_sha256"] == sha256(
        artifact.read_bytes(),
    ).hexdigest()
    assert resource_payload["artificial_resource_limit_applied"] is False
    assert resource_payload["resource_preflight"]["artificial_wall_clock_limit"] is None
    assert resource_payload["resource_preflight"]["artificial_memory_limit_bytes"] is None
    assert resource_payload["all_observations_reached_natural_terminal_condition"] is True
    assert [
        item["terminal_condition"] for item in resource_payload["resource_observations"]
    ] == [
        "completed-source-build-and-contextual-metric",
        "completed-source-build-and-contextual-metric",
    ]
