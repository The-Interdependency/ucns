# === CHECKS ===
# id: public_gonol_contextual_protocol_freeze_check
#   proves: public_gonol_contextual_protocol_freezes_all_evaluation_choices, public_gonol_contextual_protocol_does_not_smuggle_efficacy
#   call: self::test_protocol_freezes_sources_controls_thresholds_and_nonclaims
#   timeout: 20
#   mutates: none
#   cleanup: none
#
# id: public_gonol_contextual_protocol_replay_check
#   proves: public_gonol_contextual_protocol_receipt_replays_exactly
#   call: self::test_protocol_receipt_is_exact_and_outcome_free
#   timeout: 20
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.public_gonol_contextual_protocol import (
    ANCHOR_FUNCTION_INDEX,
    CONTEXTS,
    IDENTITY_ONLY_CONTROL,
    PUBLIC_GONOL_CONTEXTUAL_PROTOCOL,
    TARGET_INDICES,
    PublicGonolContextualProtocolError,
    contextual_protocol_bytes,
    main,
)


def test_protocol_freezes_sources_controls_thresholds_and_nonclaims() -> None:
    protocol = PUBLIC_GONOL_CONTEXTUAL_PROTOCOL
    assert protocol.target_indices == TARGET_INDICES
    assert protocol.anchor_function_index == ANCHOR_FUNCTION_INDEX
    assert protocol.contexts == CONTEXTS
    assert protocol.baseline == IDENTITY_ONLY_CONTROL
    assert protocol.required_target_distinct_results == 84
    assert protocol.required_baseline_distinct_results == 1
    assert protocol.required_context_changes_per_index == 2
    assert protocol.independent_replays == 2
    assert protocol.required_full_source_builds == 2
    assert protocol.wall_clock_stopping_rule == "none-natural-terminal-condition"
    assert protocol.memory_stopping_rule == "none-observe-only"
    assert protocol.artificial_resource_limit_applied is False
    assert protocol.selection_effect == "none"
    assert protocol.outcome_recorded is False
    with pytest.raises(PublicGonolContextualProtocolError, match="source evidence"):
        replace(protocol, table_receipt_sha256="0" * 64)
    with pytest.raises(PublicGonolContextualProtocolError, match="target indices"):
        replace(protocol, target_indices=TARGET_INDICES[:-1])
    with pytest.raises(PublicGonolContextualProtocolError, match="contexts"):
        replace(protocol, contexts=CONTEXTS[:-1])
    with pytest.raises(PublicGonolContextualProtocolError, match="thresholds"):
        replace(protocol, required_context_changes_per_index=1)
    with pytest.raises(PublicGonolContextualProtocolError, match="resource-run doctrine"):
        replace(protocol, wall_clock_stopping_rule="420-second-timeout")
    with pytest.raises(PublicGonolContextualProtocolError, match="outcome"):
        replace(protocol, outcome_recorded=True)


def test_protocol_receipt_is_exact_and_outcome_free(tmp_path) -> None:
    first = contextual_protocol_bytes()
    second = contextual_protocol_bytes()
    assert first == second
    assert b'"outcome_recorded":false' in first
    assert b'"semantic usefulness"' in first
    assert b'"result"' not in first
    output = tmp_path / "protocol.json"
    assert main([str(output)]) == 0
    assert output.read_bytes() == first
