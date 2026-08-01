# === MODULE_BUILD ===
# id: edcm_full_corpus_execution_gate
#   module_name: full_corpus
#   module_kind: experiment
#   summary: fail-closed EDCM corpus execution reports and completion receipts that require iterator exhaustion, declared turn-count agreement, and exact source reconstruction before post-run analysis
#   owner: Erin Spencer
#   public_surface: CorpusAdapterIdentity, AdmittedCorpusManifest, CorpusRunStatus, CorpusRunFailureKind, CorpusRunFailure, FullCorpusExecutionReport, FullCorpusCompletionReceipt, execute_admitted_corpus, issue_full_corpus_completion_receipt
#   internal_surface: exact profile-implementation validation, length-prefixed turn-stream hashing, executed-run capability binding, incomplete-report construction, and complete manifest-bound receipt identity helpers
#   auth_boundary: admission authority remains external and is retained by admission_decision_id
#   storage_boundary: raw corpus and per-turn observations remain in source or downstream custody; this bounded report retains counts and linked digests only
#   network_boundary: none
#   user_data_boundary: exact source text enters the fixed EDCM profile without normalization; the report retains no raw text and cannot replace source or trajectory custody
#   admin_only: false
#   tests: tests/test_full_corpus.py
#   rollout: explicit UCNS-only v0.14 execution gate; no corpus is admitted by this module, no real-system run is claimed, and no carrier, EDCM, or METAPAT activation follows
#   rollback: remove this module, its exports, tests, and v0.14 document while retaining the full-corpus authority decision and v0.13 carrier evidence
#   requires: edcm_word_gonol_profile
#   since: 2026-07-31
#   unresolved: source-native corpus adapters, authenticated source custody, actual corrected MultiWOZ and later corpus runs, post-run falsifier implementations, completion-motion trajectories, and EDCM-scoped selection
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: full_corpus_manifest_pins_admission_identity
#   given: a corpus is declared for EDCM execution
#   then: source version and digest, expected turn count, license, privacy and redaction treatment, adapter identity, and external admission decision remain explicit
#   class: evidence
#   since: 2026-07-31
#
# id: full_corpus_gate_requires_exhaustion_and_turn_count
#   given: an admitted corpus iterable is executed through the exact EDCM profile
#   then: a complete report requires iterator exhaustion and exact agreement with the manifest's expected turn count
#   class: correctness
#   since: 2026-07-31
#
# id: full_corpus_gate_requires_exact_stream_reconstruction
#   given: every successfully processed speaker turn is observed
#   then: the exact fixed profile implementation with canonical authority fields observes exact built-in turn tuples, speaker ids, and text values and length-prefixed source and reconstructed-observation stream digests agree before the report can complete
#   class: evidence
#   since: 2026-07-31
#
# id: incomplete_corpus_run_fails_closed
#   given: iteration, observation, reconstruction, or expected-count agreement fails
#   then: the exact stopping index and failure class remain visible and no post-run completion receipt can be issued
#   class: safety
#   since: 2026-07-31
#
# id: full_corpus_receipt_has_no_selection_or_activation_effect
#   given: a full-corpus completion receipt is issued
#   then: it requires module-executed evidence, binds every authority-bearing manifest field, opens only failure-seeking post-run analysis, and cannot select a carrier, validate EDCM measurement, activate EDCM, or activate METAPAT
#   class: doctrine
#   since: 2026-07-31
# === END CONTRACTS ===

"""Fail-closed full-corpus execution evidence for the EDCM profile.

This module closes one procedural proof boundary: post-run failure-seeking
analysis cannot receive a completion receipt until the supplied corpus iterator
is exhausted, the externally admitted turn count matches, and the exact source
turn stream agrees with the stream reconstructed by the fixed EDCM profile.

The report is not corpus custody and is not an EDCM measurement. It retains
counts and deterministic links while the raw source, per-turn observations, and
completion-motion trajectories remain in their declared custody systems.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
import string
from typing import Iterable

from .edcm import (
    EDCM_PROFILE_ID,
    EDCM_PROFILE_OPTIONS,
    EDCM_PROFILE_SCOPE,
    EDCM_PROFILE_VERSION,
    EdcmTurnObservation,
    EdcmWordGonolProfile,
)


V014_FULL_CORPUS_SCHEMA_ID = "ucns.edcm.full-corpus-execution"
V014_FULL_CORPUS_SCHEMA_VERSION = "0.14.1"
V014_FULL_CORPUS_SELECTION_EFFECT = "none"
V014_FULL_CORPUS_EDCM_ACTIVATION = "inactive"
V014_FULL_CORPUS_METAPAT_ACTIVATION = "inactive"
POST_RUN_GATE_OPEN = "open-for-failure-seeking-analysis-only"
POST_RUN_GATE_CLOSED = "closed-incomplete-corpus-execution"

_TURN_STREAM_DOMAIN = b"ucns.edcm.exact-turn-stream.v1\x00"
_RECEIPT_DOMAIN = b"ucns.edcm.full-corpus-receipt.v0141\x00"
_EXECUTED_RUN_CAPABILITY = object()
_HEX_DIGITS = frozenset(string.hexdigits)


class FullCorpusError(ValueError):
    """Raised when a full-corpus evidence boundary is violated."""


class CorpusRunStatus(str, Enum):
    """Whether the declared corpus execution reached its complete gate."""

    COMPLETE = "complete"
    INCOMPLETE = "incomplete"


class CorpusRunFailureKind(str, Enum):
    """Stable failure classes for incomplete execution evidence."""

    ITERATION_ERROR = "iteration-error"
    TURN_OBSERVATION_ERROR = "turn-observation-error"
    RECONSTRUCTION_MISMATCH = "reconstruction-mismatch"
    TURN_COUNT_MISMATCH = "turn-count-mismatch"


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise FullCorpusError(f"{field_name} must be nonempty text")


def _require_nonnegative_int(value: int, field_name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise FullCorpusError(f"{field_name} must be a nonnegative integer")


def _require_sha256(value: str, field_name: str) -> None:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in _HEX_DIGITS for character in value)
    ):
        raise FullCorpusError(f"{field_name} must be a 64-character SHA-256 hex digest")


def _length_prefixed(value: bytes) -> bytes:
    return len(value).to_bytes(8, "big", signed=False) + value


def _turn_stream_record(
    *,
    turn_index: int,
    speaker_id: str,
    text: str,
) -> bytes:
    _require_nonnegative_int(turn_index, "turn_index")
    if type(speaker_id) is not str:
        raise FullCorpusError("speaker_id must be exact built-in text")
    if type(text) is not str:
        raise FullCorpusError("turn text must be exact built-in text")
    return b"".join(
        (
            turn_index.to_bytes(8, "big", signed=False),
            _length_prefixed(speaker_id.encode("utf-8", errors="strict")),
            _length_prefixed(text.encode("utf-8", errors="strict")),
        )
    )


@dataclass(frozen=True, slots=True)
class CorpusAdapterIdentity:
    """Explicit identity for the source-native adapter outside this module."""

    adapter_id: str
    adapter_version: str
    code_reference: str

    def __post_init__(self) -> None:
        _require_text(self.adapter_id, "adapter_id")
        _require_text(self.adapter_version, "adapter_version")
        _require_text(self.code_reference, "code_reference")


@dataclass(frozen=True, slots=True)
class AdmittedCorpusManifest:
    """External admission and exact source boundary for one complete run."""

    corpus_id: str
    corpus_version: str
    source_artifact_sha256: str
    expected_turn_count: int
    license_id: str
    privacy_treatment: str
    redaction_policy: str
    admission_decision_id: str
    adapter: CorpusAdapterIdentity

    def __post_init__(self) -> None:
        _require_text(self.corpus_id, "corpus_id")
        _require_text(self.corpus_version, "corpus_version")
        _require_sha256(self.source_artifact_sha256, "source_artifact_sha256")
        _require_nonnegative_int(self.expected_turn_count, "expected_turn_count")
        _require_text(self.license_id, "license_id")
        _require_text(self.privacy_treatment, "privacy_treatment")
        _require_text(self.redaction_policy, "redaction_policy")
        _require_text(self.admission_decision_id, "admission_decision_id")
        if not isinstance(self.adapter, CorpusAdapterIdentity):
            raise FullCorpusError("adapter must be a CorpusAdapterIdentity")

    @property
    def evidence_identity(self) -> tuple[str, ...]:
        """Return every authority-bearing manifest field in declared order."""

        return (
            self.corpus_id,
            self.corpus_version,
            self.source_artifact_sha256,
            str(self.expected_turn_count),
            self.license_id,
            self.privacy_treatment,
            self.redaction_policy,
            self.admission_decision_id,
            self.adapter.adapter_id,
            self.adapter.adapter_version,
            self.adapter.code_reference,
        )


@dataclass(frozen=True, slots=True)
class CorpusRunFailure:
    """Exact stopping boundary for one incomplete corpus execution."""

    kind: CorpusRunFailureKind
    stopping_turn_index: int
    detail: str
    exception_type: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.kind, CorpusRunFailureKind):
            raise FullCorpusError("failure kind must be a CorpusRunFailureKind")
        _require_nonnegative_int(self.stopping_turn_index, "stopping_turn_index")
        _require_text(self.detail, "failure detail")
        if self.exception_type is not None:
            _require_text(self.exception_type, "exception_type")


@dataclass(frozen=True, slots=True)
class FullCorpusExecutionReport:
    """Bounded execution evidence; never a replacement for source custody."""

    manifest: AdmittedCorpusManifest
    status: CorpusRunStatus
    iterator_exhausted: bool
    processed_turn_count: int
    exact_source_stream_sha256: str
    exact_observation_stream_sha256: str
    word_gonol_count: int
    space_boundary_count: int
    carrier_unassigned_count: int
    failure: CorpusRunFailure | None
    schema_id: str = V014_FULL_CORPUS_SCHEMA_ID
    schema_version: str = V014_FULL_CORPUS_SCHEMA_VERSION
    profile_id: str = EDCM_PROFILE_ID
    profile_version: str = EDCM_PROFILE_VERSION
    profile_scope: str = EDCM_PROFILE_SCOPE
    selection_effect: str = V014_FULL_CORPUS_SELECTION_EFFECT
    edcm_activation: str = V014_FULL_CORPUS_EDCM_ACTIVATION
    metapat_activation: str = V014_FULL_CORPUS_METAPAT_ACTIVATION
    _execution_capability: object | None = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
    )

    def __post_init__(self) -> None:
        if not isinstance(self.manifest, AdmittedCorpusManifest):
            raise FullCorpusError("manifest must be an AdmittedCorpusManifest")
        if not isinstance(self.status, CorpusRunStatus):
            raise FullCorpusError("status must be a CorpusRunStatus")
        if not isinstance(self.iterator_exhausted, bool):
            raise FullCorpusError("iterator_exhausted must be bool")
        for field_name in (
            "processed_turn_count",
            "word_gonol_count",
            "space_boundary_count",
            "carrier_unassigned_count",
        ):
            _require_nonnegative_int(getattr(self, field_name), field_name)
        _require_sha256(
            self.exact_source_stream_sha256,
            "exact_source_stream_sha256",
        )
        _require_sha256(
            self.exact_observation_stream_sha256,
            "exact_observation_stream_sha256",
        )
        if self.schema_id != V014_FULL_CORPUS_SCHEMA_ID:
            raise FullCorpusError("full-corpus schema identity mismatch")
        if self.schema_version != V014_FULL_CORPUS_SCHEMA_VERSION:
            raise FullCorpusError("full-corpus schema version mismatch")
        if (
            self.profile_id != EDCM_PROFILE_ID
            or self.profile_version != EDCM_PROFILE_VERSION
            or self.profile_scope != EDCM_PROFILE_SCOPE
        ):
            raise FullCorpusError("full-corpus report requires the fixed EDCM profile")
        if self.selection_effect != "none":
            raise FullCorpusError("full-corpus evidence cannot select a candidate")
        if self.edcm_activation != "inactive":
            raise FullCorpusError("full-corpus evidence cannot activate EDCM")
        if self.metapat_activation != "inactive":
            raise FullCorpusError("full-corpus evidence cannot activate METAPAT")

        complete_invariants = (
            self.iterator_exhausted
            and self.processed_turn_count == self.manifest.expected_turn_count
            and self.exact_source_stream_sha256
            == self.exact_observation_stream_sha256
            and self.failure is None
        )
        if self.status is CorpusRunStatus.COMPLETE and not complete_invariants:
            raise FullCorpusError(
                "complete corpus status requires exhaustion, count agreement, "
                "exact reconstruction, and no failure"
            )
        if self.status is CorpusRunStatus.INCOMPLETE:
            if complete_invariants:
                raise FullCorpusError(
                    "an invariant-complete corpus report cannot be marked incomplete"
                )
            if not isinstance(self.failure, CorpusRunFailure):
                raise FullCorpusError("incomplete corpus report requires a failure")

    @property
    def post_run_gate(self) -> str:
        if self.eligible_for_post_run_analysis:
            return POST_RUN_GATE_OPEN
        return POST_RUN_GATE_CLOSED

    @property
    def eligible_for_post_run_analysis(self) -> bool:
        return (
            self.status is CorpusRunStatus.COMPLETE
            and self._execution_capability is _EXECUTED_RUN_CAPABILITY
        )


@dataclass(frozen=True, slots=True)
class FullCorpusCompletionReceipt:
    """Receipt that opens analysis only; it carries no selection authority."""

    report: FullCorpusExecutionReport
    gate_effect: str = POST_RUN_GATE_OPEN
    selection_effect: str = V014_FULL_CORPUS_SELECTION_EFFECT
    edcm_activation: str = V014_FULL_CORPUS_EDCM_ACTIVATION
    metapat_activation: str = V014_FULL_CORPUS_METAPAT_ACTIVATION

    def __post_init__(self) -> None:
        if not isinstance(self.report, FullCorpusExecutionReport):
            raise FullCorpusError("receipt report must be a FullCorpusExecutionReport")
        if self.report._execution_capability is not _EXECUTED_RUN_CAPABILITY:
            raise FullCorpusError(
                "completion receipt requires execution-generated run evidence"
            )
        if not self.report.eligible_for_post_run_analysis:
            raise FullCorpusError(
                "an incomplete corpus report cannot issue a completion receipt"
            )
        if self.gate_effect != POST_RUN_GATE_OPEN:
            raise FullCorpusError("completion receipt opens only the post-run gate")
        if self.selection_effect != "none":
            raise FullCorpusError("completion receipt cannot select a candidate")
        if self.edcm_activation != "inactive":
            raise FullCorpusError("completion receipt cannot activate EDCM")
        if self.metapat_activation != "inactive":
            raise FullCorpusError("completion receipt cannot activate METAPAT")

    @property
    def receipt_id(self) -> str:
        manifest = self.report.manifest
        values = (
            V014_FULL_CORPUS_SCHEMA_ID,
            V014_FULL_CORPUS_SCHEMA_VERSION,
            *manifest.evidence_identity,
            self.report.profile_id,
            self.report.profile_version,
            self.report.profile_scope,
            self.report.status.value,
            str(self.report.iterator_exhausted).lower(),
            self.report.exact_source_stream_sha256,
            self.report.exact_observation_stream_sha256,
            str(self.report.processed_turn_count),
            str(self.report.word_gonol_count),
            str(self.report.space_boundary_count),
            str(self.report.carrier_unassigned_count),
            self.report.selection_effect,
            self.report.edcm_activation,
            self.report.metapat_activation,
        )
        digest = sha256(_RECEIPT_DOMAIN)
        for value in values:
            digest.update(_length_prefixed(value.encode("utf-8")))
        return digest.hexdigest()


def _empty_stream_digest():
    digest = sha256()
    digest.update(_TURN_STREAM_DOMAIN)
    return digest


def _bind_executed_run(
    report: FullCorpusExecutionReport,
) -> FullCorpusExecutionReport:
    """Bind module-created evidence to the exact execution path."""

    object.__setattr__(
        report,
        "_execution_capability",
        _EXECUTED_RUN_CAPABILITY,
    )
    return report


def _incomplete_report(
    *,
    manifest: AdmittedCorpusManifest,
    iterator_exhausted: bool,
    processed_turn_count: int,
    source_digest,
    observation_digest,
    word_gonol_count: int,
    space_boundary_count: int,
    carrier_unassigned_count: int,
    failure: CorpusRunFailure,
) -> FullCorpusExecutionReport:
    return _bind_executed_run(FullCorpusExecutionReport(
        manifest=manifest,
        status=CorpusRunStatus.INCOMPLETE,
        iterator_exhausted=iterator_exhausted,
        processed_turn_count=processed_turn_count,
        exact_source_stream_sha256=source_digest.hexdigest(),
        exact_observation_stream_sha256=observation_digest.hexdigest(),
        word_gonol_count=word_gonol_count,
        space_boundary_count=space_boundary_count,
        carrier_unassigned_count=carrier_unassigned_count,
        failure=failure,
    ))


def execute_admitted_corpus(
    manifest: AdmittedCorpusManifest,
    turns: Iterable[tuple[str, str]],
    *,
    profile: EdcmWordGonolProfile | None = None,
) -> FullCorpusExecutionReport:
    """Consume every supplied turn and return complete or explicit partial evidence."""

    if not isinstance(manifest, AdmittedCorpusManifest):
        raise FullCorpusError("manifest must be an AdmittedCorpusManifest")
    active_profile = EdcmWordGonolProfile() if profile is None else profile
    if type(active_profile) is not EdcmWordGonolProfile:
        raise FullCorpusError(
            "profile must use the exact EdcmWordGonolProfile implementation"
        )
    if (
        type(active_profile.profile_id) is not str
        or type(active_profile.version) is not str
        or type(active_profile.scope) is not str
        or type(active_profile.options) is not tuple
        or any(
            type(option) is not tuple
            or len(option) != 2
            or any(type(value) is not str for value in option)
            for option in active_profile.options
        )
        or active_profile.profile_id != EDCM_PROFILE_ID
        or active_profile.version != EDCM_PROFILE_VERSION
        or active_profile.scope != EDCM_PROFILE_SCOPE
        or active_profile.options != EDCM_PROFILE_OPTIONS
    ):
        raise FullCorpusError(
            "profile authority fields and options must be exact and canonical"
        )

    source_digest = _empty_stream_digest()
    observation_digest = _empty_stream_digest()
    processed_turn_count = 0
    word_gonol_count = 0
    space_boundary_count = 0
    carrier_unassigned_count = 0

    try:
        iterator = iter(turns)
    except Exception as exc:
        return _incomplete_report(
            manifest=manifest,
            iterator_exhausted=False,
            processed_turn_count=0,
            source_digest=source_digest,
            observation_digest=observation_digest,
            word_gonol_count=0,
            space_boundary_count=0,
            carrier_unassigned_count=0,
            failure=CorpusRunFailure(
                kind=CorpusRunFailureKind.ITERATION_ERROR,
                stopping_turn_index=0,
                detail="the declared turn source could not produce an iterator",
                exception_type=type(exc).__name__,
            ),
        )

    while True:
        try:
            turn = next(iterator)
        except StopIteration:
            break
        except Exception as exc:
            return _incomplete_report(
                manifest=manifest,
                iterator_exhausted=False,
                processed_turn_count=processed_turn_count,
                source_digest=source_digest,
                observation_digest=observation_digest,
                word_gonol_count=word_gonol_count,
                space_boundary_count=space_boundary_count,
                carrier_unassigned_count=carrier_unassigned_count,
                failure=CorpusRunFailure(
                    kind=CorpusRunFailureKind.ITERATION_ERROR,
                    stopping_turn_index=processed_turn_count,
                    detail="the declared turn iterator raised before exhaustion",
                    exception_type=type(exc).__name__,
                ),
            )

        turn_index = processed_turn_count
        try:
            if type(turn) is not tuple or len(turn) != 2:
                raise FullCorpusError(
                    "each admitted corpus turn must be a (speaker_id, text) tuple"
                )
            speaker_id, text = turn
            source_record = _turn_stream_record(
                turn_index=turn_index,
                speaker_id=speaker_id,
                text=text,
            )
            observation = active_profile.observe_turn(
                speaker_id=speaker_id,
                turn_index=turn_index,
                text=text,
                source_id=manifest.corpus_id,
            )
            if not isinstance(observation, EdcmTurnObservation):
                raise FullCorpusError(
                    "EDCM profile returned a non-observation turn result"
                )
            observation_record = _turn_stream_record(
                turn_index=observation.turn_index,
                speaker_id=observation.speaker_id,
                text=observation.raw_text,
            )
        except Exception as exc:
            return _incomplete_report(
                manifest=manifest,
                iterator_exhausted=False,
                processed_turn_count=processed_turn_count,
                source_digest=source_digest,
                observation_digest=observation_digest,
                word_gonol_count=word_gonol_count,
                space_boundary_count=space_boundary_count,
                carrier_unassigned_count=carrier_unassigned_count,
                failure=CorpusRunFailure(
                    kind=CorpusRunFailureKind.TURN_OBSERVATION_ERROR,
                    stopping_turn_index=turn_index,
                    detail="the exact EDCM profile could not observe this turn",
                    exception_type=type(exc).__name__,
                ),
            )

        source_digest.update(source_record)
        observation_digest.update(observation_record)
        processed_turn_count += 1
        word_gonol_count += len(observation.word_gonols)
        space_boundary_count += len(observation.nesting_boundaries)
        carrier_unassigned_count += len(observation.carrier_unassigned)

        if source_record != observation_record:
            return _incomplete_report(
                manifest=manifest,
                iterator_exhausted=False,
                processed_turn_count=processed_turn_count,
                source_digest=source_digest,
                observation_digest=observation_digest,
                word_gonol_count=word_gonol_count,
                space_boundary_count=space_boundary_count,
                carrier_unassigned_count=carrier_unassigned_count,
                failure=CorpusRunFailure(
                    kind=CorpusRunFailureKind.RECONSTRUCTION_MISMATCH,
                    stopping_turn_index=turn_index,
                    detail="the observed turn stream did not reconstruct its source",
                ),
            )

    if processed_turn_count != manifest.expected_turn_count:
        return _incomplete_report(
            manifest=manifest,
            iterator_exhausted=True,
            processed_turn_count=processed_turn_count,
            source_digest=source_digest,
            observation_digest=observation_digest,
            word_gonol_count=word_gonol_count,
            space_boundary_count=space_boundary_count,
            carrier_unassigned_count=carrier_unassigned_count,
            failure=CorpusRunFailure(
                kind=CorpusRunFailureKind.TURN_COUNT_MISMATCH,
                stopping_turn_index=processed_turn_count,
                detail="exhausted turn count does not match the admitted manifest",
            ),
        )

    if source_digest.hexdigest() != observation_digest.hexdigest():
        return _incomplete_report(
            manifest=manifest,
            iterator_exhausted=True,
            processed_turn_count=processed_turn_count,
            source_digest=source_digest,
            observation_digest=observation_digest,
            word_gonol_count=word_gonol_count,
            space_boundary_count=space_boundary_count,
            carrier_unassigned_count=carrier_unassigned_count,
            failure=CorpusRunFailure(
                kind=CorpusRunFailureKind.RECONSTRUCTION_MISMATCH,
                stopping_turn_index=processed_turn_count,
                detail="complete source and observation stream digests disagree",
            ),
        )

    return _bind_executed_run(FullCorpusExecutionReport(
        manifest=manifest,
        status=CorpusRunStatus.COMPLETE,
        iterator_exhausted=True,
        processed_turn_count=processed_turn_count,
        exact_source_stream_sha256=source_digest.hexdigest(),
        exact_observation_stream_sha256=observation_digest.hexdigest(),
        word_gonol_count=word_gonol_count,
        space_boundary_count=space_boundary_count,
        carrier_unassigned_count=carrier_unassigned_count,
        failure=None,
    ))


def issue_full_corpus_completion_receipt(
    report: FullCorpusExecutionReport,
) -> FullCorpusCompletionReceipt:
    """Open only the post-run analysis gate for an invariant-complete report."""

    return FullCorpusCompletionReceipt(report=report)


__all__ = [
    "POST_RUN_GATE_CLOSED",
    "POST_RUN_GATE_OPEN",
    "V014_FULL_CORPUS_EDCM_ACTIVATION",
    "V014_FULL_CORPUS_METAPAT_ACTIVATION",
    "V014_FULL_CORPUS_SCHEMA_ID",
    "V014_FULL_CORPUS_SCHEMA_VERSION",
    "V014_FULL_CORPUS_SELECTION_EFFECT",
    "AdmittedCorpusManifest",
    "CorpusAdapterIdentity",
    "CorpusRunFailure",
    "CorpusRunFailureKind",
    "CorpusRunStatus",
    "FullCorpusCompletionReceipt",
    "FullCorpusError",
    "FullCorpusExecutionReport",
    "execute_admitted_corpus",
    "issue_full_corpus_completion_receipt",
]
