# === CHECKS ===
# id: check_full_corpus_manifest_identity
#   proves: full_corpus_manifest_pins_admission_identity
#   call: self::test_manifest_pins_source_adapter_and_admission_boundary
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_full_corpus_exhaustion_and_count_gate
#   proves: full_corpus_gate_requires_exhaustion_and_turn_count
#   call: self::test_complete_run_exhausts_every_turn_and_matches_expected_count
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_full_corpus_exact_reconstruction
#   proves: full_corpus_gate_requires_exact_stream_reconstruction
#   call: self::test_exact_stream_digest_is_stable_across_equivalent_iterables
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_incomplete_corpus_fail_closed
#   proves: incomplete_corpus_run_fails_closed
#   call: self::test_partial_iteration_and_count_mismatch_cannot_issue_receipts
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_invalid_corpus_turn_fail_closed
#   proves: incomplete_corpus_run_fails_closed
#   call: self::test_invalid_turn_records_exact_stopping_boundary
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_full_corpus_receipt_nonactivation
#   proves: full_corpus_receipt_has_no_selection_or_activation_effect
#   call: self::test_completion_receipt_opens_analysis_only
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace

import pytest

from ucns.full_corpus import (
    POST_RUN_GATE_CLOSED,
    POST_RUN_GATE_OPEN,
    AdmittedCorpusManifest,
    CorpusAdapterIdentity,
    CorpusRunFailureKind,
    CorpusRunStatus,
    FullCorpusError,
    execute_admitted_corpus,
    issue_full_corpus_completion_receipt,
)


def _manifest(*, expected_turn_count: int = 4) -> AdmittedCorpusManifest:
    return AdmittedCorpusManifest(
        corpus_id="fixture-dialogue-corpus",
        corpus_version="2026-07-31",
        source_artifact_sha256="a" * 64,
        expected_turn_count=expected_turn_count,
        license_id="CC-BY-4.0-fixture",
        privacy_treatment="synthetic-no-personal-data",
        redaction_policy="none-synthetic-source",
        admission_decision_id="fixture-admission/1",
        adapter=CorpusAdapterIdentity(
            adapter_id="fixture-turn-adapter",
            adapter_version="1.0.0",
            code_reference="tests.test_full_corpus:_turns",
        ),
    )


def _turns() -> list[tuple[str, str]]:
    return [
        ("empty-speaker", ""),
        ("literal-space", "A B"),
        ("nbsp-space", "A\u00A0B"),
        ("unassigned", "A🙂B"),
    ]


def test_manifest_pins_source_adapter_and_admission_boundary() -> None:
    manifest = _manifest()

    assert manifest.expected_turn_count == 4
    assert manifest.source_artifact_sha256 == "a" * 64
    assert manifest.admission_decision_id == "fixture-admission/1"
    assert manifest.adapter.adapter_id == "fixture-turn-adapter"
    assert manifest.license_id == "CC-BY-4.0-fixture"
    assert manifest.privacy_treatment == "synthetic-no-personal-data"
    assert manifest.redaction_policy == "none-synthetic-source"

    with pytest.raises(FullCorpusError, match="SHA-256"):
        replace(manifest, source_artifact_sha256="not-a-digest")
    with pytest.raises(FullCorpusError, match="nonnegative integer"):
        replace(manifest, expected_turn_count=True)
    with pytest.raises(FullCorpusError, match="admission_decision_id"):
        replace(manifest, admission_decision_id="")


def test_complete_run_exhausts_every_turn_and_matches_expected_count() -> None:
    visited: list[int] = []

    def complete_turn_stream():
        for index, turn in enumerate(_turns()):
            visited.append(index)
            yield turn

    report = execute_admitted_corpus(_manifest(), complete_turn_stream())

    assert visited == [0, 1, 2, 3]
    assert report.status is CorpusRunStatus.COMPLETE
    assert report.iterator_exhausted is True
    assert report.processed_turn_count == 4
    assert report.word_gonol_count == 5
    assert report.space_boundary_count == 2
    assert report.carrier_unassigned_count == 1
    assert report.failure is None
    assert report.eligible_for_post_run_analysis is True
    assert report.post_run_gate == POST_RUN_GATE_OPEN

    with pytest.raises(FullCorpusError, match="requires exhaustion"):
        replace(report, iterator_exhausted=False)


def test_exact_stream_digest_is_stable_across_equivalent_iterables() -> None:
    list_report = execute_admitted_corpus(_manifest(), _turns())
    generator_report = execute_admitted_corpus(
        _manifest(),
        (turn for turn in _turns()),
    )

    assert (
        list_report.exact_source_stream_sha256
        == list_report.exact_observation_stream_sha256
    )
    assert (
        generator_report.exact_source_stream_sha256
        == generator_report.exact_observation_stream_sha256
    )
    assert (
        list_report.exact_source_stream_sha256
        == generator_report.exact_source_stream_sha256
    )

    changed = _turns()
    changed[2] = ("nbsp-space", "A B")
    changed_report = execute_admitted_corpus(_manifest(), changed)
    assert (
        changed_report.exact_source_stream_sha256
        != list_report.exact_source_stream_sha256
    )


def test_partial_iteration_and_count_mismatch_cannot_issue_receipts() -> None:
    def broken_turn_stream():
        yield ("speaker-0", "A")
        yield ("speaker-1", "B")
        raise RuntimeError("fixture iterator stopped")

    partial = execute_admitted_corpus(
        _manifest(expected_turn_count=3),
        broken_turn_stream(),
    )

    assert partial.status is CorpusRunStatus.INCOMPLETE
    assert partial.iterator_exhausted is False
    assert partial.processed_turn_count == 2
    assert partial.failure is not None
    assert partial.failure.kind is CorpusRunFailureKind.ITERATION_ERROR
    assert partial.failure.stopping_turn_index == 2
    assert partial.failure.exception_type == "RuntimeError"
    assert partial.post_run_gate == POST_RUN_GATE_CLOSED
    assert partial.eligible_for_post_run_analysis is False

    with pytest.raises(FullCorpusError, match="incomplete corpus"):
        issue_full_corpus_completion_receipt(partial)

    count_mismatch = execute_admitted_corpus(
        _manifest(expected_turn_count=5),
        _turns(),
    )
    assert count_mismatch.status is CorpusRunStatus.INCOMPLETE
    assert count_mismatch.iterator_exhausted is True
    assert count_mismatch.processed_turn_count == 4
    assert count_mismatch.failure is not None
    assert count_mismatch.failure.kind is CorpusRunFailureKind.TURN_COUNT_MISMATCH
    assert count_mismatch.failure.stopping_turn_index == 4

    with pytest.raises(FullCorpusError, match="incomplete corpus"):
        issue_full_corpus_completion_receipt(count_mismatch)


def test_invalid_turn_records_exact_stopping_boundary() -> None:
    report = execute_admitted_corpus(
        _manifest(expected_turn_count=3),
        [
            ("speaker-0", "A"),
            ("speaker-1", "\ud800"),
            ("speaker-2", "B"),
        ],
    )

    assert report.status is CorpusRunStatus.INCOMPLETE
    assert report.processed_turn_count == 1
    assert report.iterator_exhausted is False
    assert report.failure is not None
    assert report.failure.kind is CorpusRunFailureKind.TURN_OBSERVATION_ERROR
    assert report.failure.stopping_turn_index == 1
    assert report.failure.exception_type == "UnicodeEncodeError"


def test_completion_receipt_opens_analysis_only() -> None:
    report = execute_admitted_corpus(_manifest(), _turns())
    receipt = issue_full_corpus_completion_receipt(report)
    repeated = issue_full_corpus_completion_receipt(report)

    assert receipt.gate_effect == POST_RUN_GATE_OPEN
    assert receipt.selection_effect == "none"
    assert receipt.edcm_activation == "inactive"
    assert receipt.metapat_activation == "inactive"
    assert len(receipt.receipt_id) == 64
    assert receipt.receipt_id == repeated.receipt_id

    with pytest.raises(FullCorpusError, match="cannot select"):
        replace(receipt, selection_effect="select-carrier")
    with pytest.raises(FullCorpusError, match="cannot activate EDCM"):
        replace(receipt, edcm_activation="active")
    with pytest.raises(FullCorpusError, match="cannot activate METAPAT"):
        replace(receipt, metapat_activation="active")
