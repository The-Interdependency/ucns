# === MODULE_BUILD ===
# id: reproducible_witness_experiment_pipeline
#   module_name: experiments
#   module_kind: instrument
#   summary: snapshots and content-addresses subjects, corpora, implementations, laws, manifests, holdouts, mutations, reproduction checks, and decision packets
#   owner: Erin Spencer
#   public_surface: ContentAdapter, AdapterRegistry, json_content_adapter, text_content_adapter, bytes_content_adapter, SubjectRecord, WitnessOrigin, CorpusPartition, AuthorshipRecord, WitnessCase, WitnessCorpus, CandidateIdentity, PolicyDigest, LawSuiteDigest, ExperimentManifest, ExperimentResult, MetamorphicCase, MutationCase, Counterexample, NamedTransform, generate_metamorphic_cases, generate_mutation_cases, greedy_minimize_counterexample, HoldoutReport, CandidateDecisionPacket, ReproductionCheck, check_reproduction, build_candidate_decision_packet, comparison_policy_digest, traversal_policy_digest
#   internal_surface: _digest_bytes, _canonical_json, _validate_report_owner
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_experiments.py
#   rollout: reproducible candidate-research evidence infrastructure only
#   rollback: remove experiment exports; candidate laboratory remains process-local
#   requires: evaluator_candidate_laboratory, explicit_comparison_policy_layer, cycle_safe_traversal_policy
#   since: 2026-07-21
#   unresolved: external sealed holdout storage and canonical decision authority
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: subject_identity_requires_explicit_adapter
#   given: an arbitrary candidate-research subject is content-addressed
#   then: a named versioned ContentAdapter supplies bytes and the stored record retains an isolated snapshot of those bytes and subject state
#   class: safety
#   since: 2026-07-21
#
# id: experiment_manifests_pin_all_research_inputs
#   given: a candidate experiment is declared
#   then: candidate code identity, law implementation and fixtures, corpus, policies, comparison, traversal, and environment are content-addressed in one manifest
#   class: evidence
#   since: 2026-07-21
#
# id: development_and_holdout_evidence_are_separate
#   given: witness cases are assembled into a corpus and decision packet
#   then: development and holdout partitions remain explicit and a packet cannot be reviewable without passing holdout evidence for the same candidate
#   class: safety
#   since: 2026-07-21
#
# id: candidate_witness_and_decision_authorship_are_recorded
#   given: a witness case or candidate decision packet is content-addressed
#   then: authorship role, author, provenance, and separate candidate, witness, and decision records remain identity-bearing evidence
#   class: evidence
#   since: 2026-07-21
#
# id: reproduction_checks_report_match_or_reason
#   given: two complete ExperimentResult values claim the same manifest
#   then: an explicit result adapter compares every result field or records why reproduction could not be established
#   class: evidence
#   since: 2026-07-21
# === END CONTRACTS ===

from __future__ import annotations

import json
from collections.abc import Callable, Iterable, Mapping, Sequence
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from typing import Any

from .comparison import ComparisonPolicy
from .laboratory import EvaluationReport, EvaluatorCandidate, LawSuite
from .traversal import TraversalPolicy


Encoder = Callable[[Any], bytes]


def _digest_bytes(payload: bytes) -> str:
    return sha256(payload).hexdigest()


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


@dataclass(frozen=True, slots=True)
class ContentAdapter:
    name: str
    version: str
    encoder: Encoder
    code_reference: str
    description: str = ""

    def __post_init__(self) -> None:
        if (
            not self.name.strip()
            or not self.version.strip()
            or not self.code_reference.strip()
        ):
            raise ValueError(
                "content adapter name, version, and code reference must be nonempty"
            )
        if not callable(self.encoder):
            raise TypeError("content adapter encoder must be callable")

    def encode(self, value: Any) -> bytes:
        encoded = self.encoder(value)
        if not isinstance(encoded, bytes):
            raise TypeError("content adapter must return bytes")
        return bytes(encoded)

    @property
    def identity(self) -> str:
        return _digest_bytes(
            _canonical_json(
                {
                    "name": self.name,
                    "version": self.version,
                    "code_reference": self.code_reference,
                }
            )
        )


@dataclass(slots=True)
class AdapterRegistry:
    _adapters: dict[str, ContentAdapter] = field(default_factory=dict, repr=False)

    def register(self, adapter: ContentAdapter, *, replace: bool = False) -> None:
        if adapter.name in self._adapters and not replace:
            raise ValueError(f"content adapter already registered: {adapter.name}")
        self._adapters[adapter.name] = adapter

    def resolve(self, name: str) -> ContentAdapter:
        try:
            return self._adapters[name]
        except KeyError as exc:
            raise KeyError(f"unknown content adapter: {name}") from exc


def json_content_adapter(
    *, name: str = "canonical-json", version: str = "1"
) -> ContentAdapter:
    return ContentAdapter(
        name,
        version,
        _canonical_json,
        "ucns.experiments:json_content_adapter",
        "sorted-key canonical JSON for JSON-compatible values",
    )


def text_content_adapter(
    *, name: str = "utf8-text", version: str = "1"
) -> ContentAdapter:
    def encode(value: Any) -> bytes:
        if not isinstance(value, str):
            raise TypeError("text adapter requires str")
        return value.encode("utf-8")

    return ContentAdapter(
        name,
        version,
        encode,
        "ucns.experiments:text_content_adapter",
    )


def bytes_content_adapter(
    *, name: str = "raw-bytes", version: str = "1"
) -> ContentAdapter:
    def encode(value: Any) -> bytes:
        if not isinstance(value, bytes):
            raise TypeError("bytes adapter requires bytes")
        return value

    return ContentAdapter(
        name,
        version,
        encode,
        "ucns.experiments:bytes_content_adapter",
    )


@dataclass(frozen=True, slots=True)
class SubjectRecord:
    name: str
    adapter_name: str
    adapter_version: str
    adapter_code_reference: str
    encoded_snapshot: bytes
    digest: str
    _subject_snapshot: Any = field(repr=False)

    @classmethod
    def create(
        cls, name: str, subject: Any, adapter: ContentAdapter
    ) -> "SubjectRecord":
        if not name.strip():
            raise ValueError("subject name must be nonempty")
        encoded = adapter.encode(subject)
        try:
            snapshot = deepcopy(subject)
        except Exception as exc:
            raise TypeError("subject must support isolated snapshotting") from exc
        if adapter.encode(snapshot) != encoded:
            raise ValueError("subject snapshot does not reproduce adapter bytes")
        envelope = (
            b"ucns-subject\0"
            + adapter.identity.encode()
            + b"\0"
            + encoded
        )
        return cls(
            name,
            adapter.name,
            adapter.version,
            adapter.code_reference,
            encoded,
            _digest_bytes(envelope),
            snapshot,
        )

    @property
    def subject(self) -> Any:
        return deepcopy(self._subject_snapshot)


class WitnessOrigin(str, Enum):
    HAND_AUTHORED = "hand-authored"
    GENERATED = "generated"
    ADVERSARIAL = "adversarial"
    HISTORICAL = "historical"
    MUTATION = "mutation"
    METAMORPHIC = "metamorphic"


class CorpusPartition(str, Enum):
    DEVELOPMENT = "development"
    HOLDOUT = "holdout"


@dataclass(frozen=True, slots=True)
class AuthorshipRecord:
    role: str
    author: str
    provenance: str

    def __post_init__(self) -> None:
        if (
            not self.role.strip()
            or not self.author.strip()
            or not self.provenance.strip()
        ):
            raise ValueError(
                "authorship role, author, and provenance must be nonempty"
            )


@dataclass(frozen=True, slots=True)
class WitnessCase:
    name: str
    subject_digests: tuple[str, ...]
    expectation: str
    origin: WitnessOrigin
    partition: CorpusPartition
    authorship: AuthorshipRecord
    notes: str = ""

    def __post_init__(self) -> None:
        if (
            not self.name.strip()
            or not self.expectation.strip()
            or not self.subject_digests
        ):
            raise ValueError(
                "witness case requires name, expectation, and subjects"
            )
        object.__setattr__(self, "subject_digests", tuple(self.subject_digests))
        object.__setattr__(self, "origin", WitnessOrigin(self.origin))
        object.__setattr__(self, "partition", CorpusPartition(self.partition))

    @property
    def digest(self) -> str:
        return _digest_bytes(
            _canonical_json(
                {
                    "name": self.name,
                    "subjects": self.subject_digests,
                    "expectation": self.expectation,
                    "origin": self.origin.value,
                    "partition": self.partition.value,
                    "authorship_role": self.authorship.role,
                    "author": self.authorship.author,
                    "provenance": self.authorship.provenance,
                    "notes": self.notes,
                }
            )
        )


@dataclass(frozen=True, slots=True)
class WitnessCorpus:
    name: str
    version: str
    subjects: tuple[SubjectRecord, ...]
    cases: tuple[WitnessCase, ...]

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.version.strip():
            raise ValueError("corpus name and version must be nonempty")
        subjects = tuple(self.subjects)
        cases = tuple(self.cases)
        digests = [subject.digest for subject in subjects]
        if len(digests) != len(set(digests)):
            raise ValueError(
                "content-identical subjects are stored once; occurrence multiplicity belongs in witness case references"
            )
        known = set(digests)
        for case in cases:
            missing = set(case.subject_digests) - known
            if missing:
                raise ValueError(
                    "witness case references unknown subject digests: "
                    f"{sorted(missing)}"
                )
        object.__setattr__(self, "subjects", subjects)
        object.__setattr__(self, "cases", cases)

    def cases_for(self, partition: CorpusPartition) -> tuple[WitnessCase, ...]:
        selected = CorpusPartition(partition)
        return tuple(case for case in self.cases if case.partition is selected)

    @property
    def digest(self) -> str:
        return _digest_bytes(
            _canonical_json(
                {
                    "name": self.name,
                    "version": self.version,
                    "subjects": tuple(subject.digest for subject in self.subjects),
                    "cases": tuple(case.digest for case in self.cases),
                }
            )
        )


@dataclass(frozen=True, slots=True)
class CandidateIdentity:
    name: str
    kind: str
    version: str
    code_reference: str
    scope: str
    policy_dependencies: tuple[str, ...]
    digest: str

    @classmethod
    def from_candidate(cls, candidate: EvaluatorCandidate) -> "CandidateIdentity":
        payload = {
            "name": candidate.name,
            "kind": candidate.kind.value,
            "version": candidate.version,
            "code_reference": candidate.code_reference,
            "scope": candidate.scope,
            "policy_dependencies": candidate.policy_dependencies,
        }
        return cls(
            candidate.name,
            candidate.kind.value,
            candidate.version,
            candidate.code_reference,
            candidate.scope,
            candidate.policy_dependencies,
            _digest_bytes(_canonical_json(payload)),
        )


@dataclass(frozen=True, slots=True)
class PolicyDigest:
    name: str
    version: str
    code_reference: str
    digest: str

    @classmethod
    def create(
        cls,
        name: str,
        version: str,
        parameters: Mapping[str, str] | None = None,
        *,
        code_reference: str = "data-only-policy",
    ) -> "PolicyDigest":
        if (
            not name.strip()
            or not version.strip()
            or not code_reference.strip()
        ):
            raise ValueError(
                "policy identity requires name, version, and code reference"
            )
        payload = {
            "name": name,
            "version": version,
            "code_reference": code_reference,
            "parameters": dict(parameters or {}),
        }
        return cls(
            name,
            version,
            code_reference,
            _digest_bytes(_canonical_json(payload)),
        )


@dataclass(frozen=True, slots=True)
class LawSuiteDigest:
    name: str
    digest: str

    @classmethod
    def from_suite(cls, suite: LawSuite) -> "LawSuiteDigest":
        identities = []
        for law in suite.laws:
            if law.code_reference == "unrecorded" or law.fixture_digest == "unrecorded":
                raise ValueError(
                    f"law {law.name!r} requires recorded code and fixture identity"
                )
            identities.append(
                {
                    "name": law.name,
                    "version": law.version,
                    "code_reference": law.code_reference,
                    "fixture_digest": law.fixture_digest,
                }
            )
        payload = {
            "name": suite.name,
            "laws": tuple(identities),
            "comparison": {
                "name": suite.comparison.name,
                "version": suite.comparison.version,
                "code_reference": suite.comparison.code_reference,
                "parameters": suite.comparison.parameters,
            },
        }
        return cls(suite.name, _digest_bytes(_canonical_json(payload)))


@dataclass(frozen=True, slots=True)
class ExperimentManifest:
    name: str
    version: str
    candidate: CandidateIdentity
    corpus_digest: str
    law_suite: LawSuiteDigest
    policy_digests: tuple[PolicyDigest, ...]
    comparison_digest: PolicyDigest
    traversal_digest: PolicyDigest | None = None
    environment: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if (
            not self.name.strip()
            or not self.version.strip()
            or not self.corpus_digest.strip()
        ):
            raise ValueError("experiment manifest fields must be nonempty")
        object.__setattr__(self, "policy_digests", tuple(self.policy_digests))
        object.__setattr__(self, "environment", tuple(self.environment))

    @property
    def digest(self) -> str:
        return _digest_bytes(
            _canonical_json(
                {
                    "name": self.name,
                    "version": self.version,
                    "candidate": self.candidate.digest,
                    "corpus": self.corpus_digest,
                    "law_suite": self.law_suite.digest,
                    "policies": tuple(p.digest for p in self.policy_digests),
                    "comparison": self.comparison_digest.digest,
                    "traversal": self.traversal_digest.digest if self.traversal_digest else None,
                    "environment": self.environment,
                }
            )
        )


def comparison_policy_digest(policy: ComparisonPolicy) -> PolicyDigest:
    return PolicyDigest.create(
        policy.name,
        policy.version,
        dict(policy.parameters),
        code_reference=policy.code_reference,
    )


def traversal_policy_digest(policy: TraversalPolicy) -> PolicyDigest:
    parameters = {
        "cycle_mode": policy.cycle_mode.value,
        "max_depth": str(policy.budget.max_depth),
        "max_nodes": str(policy.budget.max_nodes),
    }
    if policy.resolver_reference is not None:
        parameters["resolver_reference"] = policy.resolver_reference
    return PolicyDigest.create(
        policy.name,
        policy.version,
        parameters,
        code_reference="ucns.traversal:traverse",
    )


@dataclass(frozen=True, slots=True)
class ExperimentResult:
    manifest_digest: str
    report: EvaluationReport
    corpus_partition: CorpusPartition
    reproducible: bool
    reproduction_note: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(self, "corpus_partition", CorpusPartition(self.corpus_partition))


@dataclass(frozen=True, slots=True)
class MetamorphicCase:
    name: str
    source_digest: str
    transformed_digest: str
    expected_relation: str


@dataclass(frozen=True, slots=True)
class MutationCase:
    name: str
    source_digest: str
    mutated_digest: str
    changed_dimension: str


@dataclass(frozen=True, slots=True)
class Counterexample:
    law_name: str
    subject_digests: tuple[str, ...]
    detail: str
    minimized: bool = False


def greedy_minimize_counterexample(
    subjects: Sequence[Any],
    still_fails: Callable[[tuple[Any, ...]], bool],
) -> tuple[Any, ...]:
    retained = list(subjects)
    changed = True
    while changed and len(retained) > 1:
        changed = False
        for index in range(len(retained)):
            candidate = tuple(retained[:index] + retained[index + 1 :])
            if candidate and still_fails(candidate):
                retained = list(candidate)
                changed = True
                break
    return tuple(retained)


@dataclass(frozen=True, slots=True)
class HoldoutReport:
    corpus_digest: str
    report: EvaluationReport

    @property
    def passed(self) -> bool:
        return self.report.all_passed


@dataclass(frozen=True, slots=True)
class CandidateDecisionPacket:
    candidate: CandidateIdentity
    scope: str
    development_report: EvaluationReport
    holdout_report: HoldoutReport | None
    counterexamples: tuple[Counterexample, ...]
    alternatives_retained: tuple[str, ...]
    information_loss: tuple[str, ...]
    rollback_behavior: str
    candidate_authorship: AuthorshipRecord
    witness_authorship: AuthorshipRecord
    decision_authorship: AuthorshipRecord

    @property
    def reviewable(self) -> bool:
        return (
            self.development_report.all_passed
            and self.holdout_report is not None
            and self.holdout_report.passed
            and bool(self.rollback_behavior.strip())
            and self.candidate_authorship.role != self.witness_authorship.role
            and self.decision_authorship.role
            not in {self.candidate_authorship.role, self.witness_authorship.role}
        )

    @property
    def canonical(self) -> bool:
        return False


@dataclass(frozen=True, slots=True)
class NamedTransform:
    name: str
    transform: Callable[[Any], Any]
    expected_relation: str
    version: str = "1"
    code_reference: str = "unrecorded"

    def __post_init__(self) -> None:
        if (
            not self.name.strip()
            or not self.expected_relation.strip()
            or not self.version.strip()
            or not self.code_reference.strip()
            or not callable(self.transform)
        ):
            raise ValueError(
                "named transform requires name, callable, relation, version, and code reference"
            )


def generate_metamorphic_cases(
    subjects: Iterable[SubjectRecord],
    transforms: Iterable[NamedTransform],
    adapter: ContentAdapter,
) -> tuple[tuple[SubjectRecord, ...], tuple[MetamorphicCase, ...]]:
    generated: list[SubjectRecord] = []
    cases: list[MetamorphicCase] = []
    selected_transforms = tuple(transforms)
    for subject in tuple(subjects):
        for transform in selected_transforms:
            transformed = SubjectRecord.create(
                f"{subject.name}:{transform.name}",
                transform.transform(subject.subject),
                adapter,
            )
            generated.append(transformed)
            cases.append(
                MetamorphicCase(
                    transform.name,
                    subject.digest,
                    transformed.digest,
                    transform.expected_relation,
                )
            )
    return tuple(generated), tuple(cases)


def generate_mutation_cases(
    subjects: Iterable[SubjectRecord],
    transforms: Iterable[NamedTransform],
    adapter: ContentAdapter,
) -> tuple[tuple[SubjectRecord, ...], tuple[MutationCase, ...]]:
    generated: list[SubjectRecord] = []
    cases: list[MutationCase] = []
    selected_transforms = tuple(transforms)
    for subject in tuple(subjects):
        for transform in selected_transforms:
            mutated = SubjectRecord.create(
                f"{subject.name}:{transform.name}",
                transform.transform(subject.subject),
                adapter,
            )
            generated.append(mutated)
            cases.append(
                MutationCase(
                    transform.name,
                    subject.digest,
                    mutated.digest,
                    transform.expected_relation,
                )
            )
    return tuple(generated), tuple(cases)


@dataclass(frozen=True, slots=True)
class ReproductionCheck:
    manifest_digest: str
    reproduced: bool
    first_digest: str | None
    second_digest: str | None
    note: str


def check_reproduction(
    first: ExperimentResult,
    second: ExperimentResult,
    *,
    adapter: ContentAdapter,
) -> ReproductionCheck:
    if first.manifest_digest != second.manifest_digest:
        return ReproductionCheck(
            first.manifest_digest, False, None, None, "manifest digests differ"
        )
    try:
        first_digest = _digest_bytes(adapter.encode(first))
        second_digest = _digest_bytes(adapter.encode(second))
    except Exception as exc:
        return ReproductionCheck(
            first.manifest_digest,
            False,
            None,
            None,
            f"result adapter failed: {type(exc).__name__}: {exc}",
        )
    reproduced = first_digest == second_digest
    return ReproductionCheck(
        first.manifest_digest,
        reproduced,
        first_digest,
        second_digest,
        "result digests match" if reproduced else "result digests differ",
    )


def _validate_report_owner(
    candidate: EvaluatorCandidate, report: EvaluationReport, label: str
) -> None:
    if report.candidate_name != candidate.name or report.kind is not candidate.kind:
        raise ValueError(
            f"{label} report belongs to {report.kind.value}:{report.candidate_name}, "
            f"not {candidate.kind.value}:{candidate.name}"
        )


def build_candidate_decision_packet(
    candidate: EvaluatorCandidate,
    *,
    development_report: EvaluationReport,
    holdout_report: HoldoutReport | None,
    counterexamples: Iterable[Counterexample] = (),
    alternatives_retained: Iterable[str] = (),
    information_loss: Iterable[str] = (),
    rollback_behavior: str,
    candidate_authorship: AuthorshipRecord,
    witness_authorship: AuthorshipRecord,
    decision_authorship: AuthorshipRecord,
) -> CandidateDecisionPacket:
    _validate_report_owner(candidate, development_report, "development")
    if holdout_report is not None:
        _validate_report_owner(candidate, holdout_report.report, "holdout")
    return CandidateDecisionPacket(
        CandidateIdentity.from_candidate(candidate),
        candidate.scope,
        development_report,
        holdout_report,
        tuple(counterexamples),
        tuple(alternatives_retained),
        tuple(information_loss),
        rollback_behavior,
        candidate_authorship,
        witness_authorship,
        decision_authorship,
    )
