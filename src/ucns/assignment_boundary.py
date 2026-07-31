# === MODULE_BUILD ===
# id: edcm_assignment_admission_boundary
#   module_name: assignment_boundary
#   module_kind: experiment
#   summary: admits arbitrary-domain observed-element occurrences through explicit content adapters and records one total tagged assignment outcome without deriving geometry from evidence identity
#   owner: Erin Spencer
#   public_surface: ObservedElementAdmission, AssignmentOutcomeReceipt, AssignmentAdmissionTrace, AssignmentAdmissionBoundaryReport, AssignmentDisposition, RejectedAssignmentMechanism, AssignmentFalsifierResult, AssignmentEvidenceStanding, admit_observed_element, record_assignment_outcome, run_v016_assignment_admission_boundary_experiment
#   internal_surface: fixed AA01-AA07 evidence construction and exact validation helpers
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: adapter-produced bytes and an isolated subject snapshot remain exact evidence; their digest never becomes a geometric coordinate
#   admin_only: false
#   tests: tests/test_assignment_boundary.py
#   rollout: nonselecting v0.16 admission and assignment-outcome evidence over explicitly adapted occurrences; no universal assignment law, total Structural Null relationship, EDCM activation, or METAPAT activation
#   rollback: remove this module, exports, tests, and v0.16 document while retaining v0.15 carrier evidence and the reusable ContentAdapter/SubjectRecord infrastructure
#   requires: reproducible_witness_experiment_pipeline, edcm_completion_motion_evidence, edcm_full_carrier_attachment_evidence
#   since: 2026-07-31
#   unresolved: arbitrary observed-element geometric assignment, total Structural Null initiation relationship, circle-epicycle-disk-sphere transitions, higher-gonol composition, scoped completion, canonical faithful breadth, and carrier selection
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: assignment_admission_requires_explicit_domain_adapter
#   given: an arbitrary-domain observed element is admitted for assignment research
#   then: a named versioned ContentAdapter creates an isolated SubjectRecord and its digest is labeled evidence identity only, never a geometric coordinate
#   class: safety
#   since: 2026-07-31
#
# id: assignment_admission_preserves_occurrence_order_and_multiplicity
#   given: equal-content occurrences enter one admission trace
#   then: each occurrence retains its own admission and receipt identity in exact input order even when subject digests are equal
#   class: evidence
#   since: 2026-07-31
#
# id: assignment_outcome_is_total_and_exclusive_over_admitted_evidence
#   given: an explicitly admitted occurrence reaches the v0.16 assignment boundary
#   then: exactly one tagged outcome is recorded as unresolved, explicit supplied candidate, or rejected mechanism and invalid combinations fail closed
#   class: correctness
#   since: 2026-07-31
#
# id: assignment_identity_mechanisms_cannot_derive_geometry
#   given: content digest, runtime hash, repr, object identity, or the historical A0 Blake2 phase lanes are proposed as a universal assignment law
#   then: the mechanism can be retained only as an explicit rejected outcome and supplies no GeometricAssignment
#   class: doctrine
#   since: 2026-07-31
#
# id: supplied_assignment_remains_candidate_evidence
#   given: a caller supplies an explicit GeometricAssignment for one admitted occurrence
#   then: the exact relation, law identity, standing, orientation, sidedness, parameters, and evidence remain linked without derivation, selection, or canonical promotion
#   class: evidence
#   since: 2026-07-31
#
# id: assignment_boundary_does_not_complete_initiation_or_activate
#   given: the v0.16 report joins admission evidence to the v0.15 carrier report
#   then: arbitrary-element geometry, the total Structural Null relationship, carrier selection, EDCM activation, and METAPAT activation remain absent
#   class: safety
#   since: 2026-07-31
# === END CONTRACTS ===

"""Observed-element admission and assignment-outcome evidence for UCNS v0.16.

The pinned A0 recovery specimen contains no admissible universal law that maps
arbitrary content into UCNS geometry.  Its executable content-to-angle path uses
Blake2-derived fixed phase lanes and ordinary-circle projection, all explicitly
rejected as the final assignment law by the recovery record.

This module closes a narrower, earlier obligation: define how an observed
element becomes exact assignment *evidence* before a geometric law exists.
Arbitrary domains enter only through named, versioned ``ContentAdapter``
values.  Each admitted occurrence then receives exactly one tagged outcome:
unresolved, an explicitly supplied candidate relation, or an explicitly
rejected mechanism.  Evidence digests identify evidence; they never generate
coordinates.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .edcm_motion import GeometricAssignment
from .experiments import ContentAdapter, SubjectRecord, text_content_adapter
from .full_carrier_attachment import (
    V015_COMPLETE_RELATIONSHIP_STATUS,
    FullCarrierAttachmentReport,
    run_v015_full_carrier_attachment_experiment,
)


V016_ASSIGNMENT_ADMISSION_SCHEMA_ID = (
    "ucns.edcm.assignment-admission-boundary"
)
V016_ASSIGNMENT_ADMISSION_SCHEMA_VERSION = "0.16.0"
V016_SELECTION_EFFECT = "none"

ASSIGNMENT_ADMISSION_SCOPE = (
    "explicit-content-adapter-admitted-observed-element-occurrences"
)
ADAPTER_EVIDENCE_IDENTITY_ROLE = (
    "evidence-identity-only-not-geometric-coordinate"
)
ASSIGNMENT_OUTCOME_RELATION_STATUS = (
    "total-tagged-over-admitted-occurrences"
)
ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS = "unresolved-no-derived-law"

ASSIGNMENT_FALSIFIER_IDS = tuple(f"AA{index:02d}" for index in range(1, 8))

V016_HMMM = (
    "the exact law assigning an arbitrary observed element to circle, epicycle, disk, or sphere geometry remains unresolved",
    "content-adapter and subject digests are evidence identities only and cannot supply transverse, angular, radial, orientation, or sidedness coordinates",
    "the total topology and initiation relation from Structural Null to arbitrary non-null states remains unresolved",
    "explicit supplied candidate relations still require independent derivation, falsification, and authority before selection",
    "higher-gonol composition, scoped completion, canonical B, proof-assistant formalization, and carrier selection remain unresolved",
)


class AssignmentAdmissionError(ValueError):
    """Raised when v0.16 evidence crosses its declared admission boundary."""


class AssignmentDisposition(str, Enum):
    """The exhaustive assignment outcomes for an admitted occurrence."""

    UNRESOLVED = "unresolved-no-law"
    SUPPLIED_CANDIDATE = "explicit-supplied-candidate"
    REJECTED_MECHANISM = "rejected-mechanism"


class RejectedAssignmentMechanism(str, Enum):
    """Identity-derived mechanisms that may be retained only as rejections."""

    A0_BLAKE2_PHASE_LANES = "a0-blake2-derived-phase-lanes"
    CONTENT_DIGEST_TO_GEOMETRY = "content-digest-to-geometry"
    RUNTIME_HASH_TO_GEOMETRY = "runtime-hash-to-geometry"
    REPR_TO_GEOMETRY = "repr-to-geometry"
    OBJECT_ID_TO_GEOMETRY = "object-id-to-geometry"


class AssignmentEvidenceStanding(str, Enum):
    """Standing vocabulary for the fixed v0.16 falsifier packet."""

    EXACT_IMPLEMENTED_SUPPORTED = "exact-implemented-supported"
    NEGATIVE_SUPPORTED = "negative-supported"
    UNRESOLVED = "unresolved"


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise AssignmentAdmissionError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise AssignmentAdmissionError(f"{field} must retain evidence")
    for value in values:
        _require_text(value, field)


@dataclass(frozen=True, slots=True)
class ObservedElementAdmission:
    """One exact occurrence admitted before any geometric assignment."""

    admission_id: str
    occurrence_index: int
    subject_record: SubjectRecord
    source_id: str
    source_reference: str
    grain: str
    provenance: tuple[str, ...]
    evidence_identity_role: str = ADAPTER_EVIDENCE_IDENTITY_ROLE
    scope: str = ASSIGNMENT_ADMISSION_SCOPE
    selection_effect: str = V016_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.admission_id, "admission_id")
        if self.occurrence_index < 0:
            raise AssignmentAdmissionError(
                "occurrence_index must be nonnegative"
            )
        if not isinstance(self.subject_record, SubjectRecord):
            raise AssignmentAdmissionError(
                "admission requires an explicit SubjectRecord"
            )
        _require_text(self.source_id, "source_id")
        _require_text(self.source_reference, "source_reference")
        _require_text(self.grain, "grain")
        _require_text_items(self.provenance, "provenance")
        if self.evidence_identity_role != ADAPTER_EVIDENCE_IDENTITY_ROLE:
            raise AssignmentAdmissionError(
                "adapter digest must remain evidence identity only"
            )
        if self.scope != ASSIGNMENT_ADMISSION_SCOPE:
            raise AssignmentAdmissionError("assignment admission scope is fixed")
        if self.selection_effect != V016_SELECTION_EFFECT:
            raise AssignmentAdmissionError(
                "observed-element admission cannot select geometry"
            )

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        """Return exact evidence identity with no geometric interpretation."""

        record = self.subject_record
        return (
            self.admission_id,
            self.occurrence_index,
            record.name,
            record.digest,
            record.adapter_name,
            record.adapter_version,
            record.adapter_code_reference,
            self.source_id,
            self.source_reference,
            self.grain,
            self.provenance,
            self.evidence_identity_role,
        )


def admit_observed_element(
    *,
    admission_id: str,
    occurrence_index: int,
    subject_name: str,
    subject: Any,
    adapter: ContentAdapter,
    source_id: str,
    source_reference: str,
    grain: str,
    provenance: tuple[str, ...],
) -> ObservedElementAdmission:
    """Admit one arbitrary-domain occurrence through an explicit adapter."""

    if not isinstance(adapter, ContentAdapter):
        raise TypeError("adapter must be ContentAdapter")
    record = SubjectRecord.create(subject_name, subject, adapter)
    return ObservedElementAdmission(
        admission_id=admission_id,
        occurrence_index=occurrence_index,
        subject_record=record,
        source_id=source_id,
        source_reference=source_reference,
        grain=grain,
        provenance=provenance,
    )


@dataclass(frozen=True, slots=True)
class AssignmentOutcomeReceipt:
    """Exactly one assignment outcome linked to one admitted occurrence."""

    receipt_id: str
    admission: ObservedElementAdmission
    disposition: AssignmentDisposition
    evidence: tuple[str, ...]
    assignment: GeometricAssignment | None = None
    rejected_mechanism: RejectedAssignmentMechanism | None = None
    geometric_relation_derived_from_subject_digest: bool = False
    selection_effect: str = V016_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.receipt_id, "receipt_id")
        if not isinstance(self.admission, ObservedElementAdmission):
            raise AssignmentAdmissionError(
                "assignment outcome requires an admitted occurrence"
            )
        if self.receipt_id != f"{self.admission.admission_id}:assignment-outcome":
            raise AssignmentAdmissionError(
                "receipt identity must derive from the admission identity"
            )
        if not isinstance(self.disposition, AssignmentDisposition):
            raise AssignmentAdmissionError(
                "assignment outcome disposition is invalid"
            )
        _require_text_items(self.evidence, "assignment outcome evidence")
        if self.geometric_relation_derived_from_subject_digest:
            raise AssignmentAdmissionError(
                "subject evidence identity cannot derive geometry"
            )
        if self.selection_effect != V016_SELECTION_EFFECT:
            raise AssignmentAdmissionError(
                "assignment outcome cannot select geometry"
            )

        if self.disposition is AssignmentDisposition.UNRESOLVED:
            if self.assignment is not None or self.rejected_mechanism is not None:
                raise AssignmentAdmissionError(
                    "unresolved outcome cannot contain assignment or rejection"
                )
        elif self.disposition is AssignmentDisposition.SUPPLIED_CANDIDATE:
            if not isinstance(self.assignment, GeometricAssignment):
                raise AssignmentAdmissionError(
                    "supplied-candidate outcome requires GeometricAssignment"
                )
            if self.rejected_mechanism is not None:
                raise AssignmentAdmissionError(
                    "supplied candidate cannot also be a rejected mechanism"
                )
        else:
            if self.assignment is not None:
                raise AssignmentAdmissionError(
                    "rejected mechanism cannot supply GeometricAssignment"
                )
            if not isinstance(
                self.rejected_mechanism,
                RejectedAssignmentMechanism,
            ):
                raise AssignmentAdmissionError(
                    "rejected outcome requires a named rejected mechanism"
                )

    @property
    def subject_digest(self) -> str:
        return self.admission.subject_record.digest


def record_assignment_outcome(
    admission: ObservedElementAdmission,
    *,
    evidence: tuple[str, ...],
    assignment: GeometricAssignment | None = None,
    rejected_mechanism: RejectedAssignmentMechanism | None = None,
) -> AssignmentOutcomeReceipt:
    """Record the sole outcome for an admission without a hidden default law."""

    if not isinstance(admission, ObservedElementAdmission):
        raise TypeError("admission must be ObservedElementAdmission")
    if assignment is not None and rejected_mechanism is not None:
        raise AssignmentAdmissionError(
            "an assignment outcome cannot be both supplied and rejected"
        )
    if assignment is not None:
        disposition = AssignmentDisposition.SUPPLIED_CANDIDATE
    elif rejected_mechanism is not None:
        disposition = AssignmentDisposition.REJECTED_MECHANISM
    else:
        disposition = AssignmentDisposition.UNRESOLVED
    return AssignmentOutcomeReceipt(
        receipt_id=f"{admission.admission_id}:assignment-outcome",
        admission=admission,
        disposition=disposition,
        evidence=evidence,
        assignment=assignment,
        rejected_mechanism=rejected_mechanism,
    )


@dataclass(frozen=True, slots=True)
class AssignmentAdmissionTrace:
    """Ordered outcomes for one explicitly admitted occurrence stream."""

    trace_id: str
    outcomes: tuple[AssignmentOutcomeReceipt, ...]
    scope: str = ASSIGNMENT_ADMISSION_SCOPE
    outcome_relation_status: str = ASSIGNMENT_OUTCOME_RELATION_STATUS
    selection_effect: str = V016_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.trace_id, "trace_id")
        if not self.outcomes:
            raise AssignmentAdmissionError(
                "assignment admission trace must retain at least one outcome"
            )
        if self.scope != ASSIGNMENT_ADMISSION_SCOPE:
            raise AssignmentAdmissionError("assignment trace scope is fixed")
        if self.outcome_relation_status != ASSIGNMENT_OUTCOME_RELATION_STATUS:
            raise AssignmentAdmissionError(
                "assignment outcome relation status is fixed"
            )
        if self.selection_effect != V016_SELECTION_EFFECT:
            raise AssignmentAdmissionError(
                "assignment admission trace cannot select geometry"
            )

        admission_ids: set[str] = set()
        receipt_ids: set[str] = set()
        for expected_index, outcome in enumerate(self.outcomes):
            if not isinstance(outcome, AssignmentOutcomeReceipt):
                raise AssignmentAdmissionError(
                    "trace outcomes must be AssignmentOutcomeReceipt values"
                )
            if outcome.admission.occurrence_index != expected_index:
                raise AssignmentAdmissionError(
                    "admitted occurrences must retain contiguous input order"
                )
            if outcome.admission.admission_id in admission_ids:
                raise AssignmentAdmissionError(
                    "admission identities must be unique per occurrence"
                )
            if outcome.receipt_id in receipt_ids:
                raise AssignmentAdmissionError(
                    "assignment receipt identities must be unique"
                )
            admission_ids.add(outcome.admission.admission_id)
            receipt_ids.add(outcome.receipt_id)

    @property
    def subject_digests(self) -> tuple[str, ...]:
        """Return digests in occurrence order without deduplication."""

        return tuple(outcome.subject_digest for outcome in self.outcomes)

    @property
    def has_total_outcome_evidence(self) -> bool:
        """Every admitted occurrence has exactly one validated tagged outcome."""

        return len(self.outcomes) == len(
            {outcome.admission.admission_id for outcome in self.outcomes}
        )

    @property
    def all_have_supplied_candidate_relations(self) -> bool:
        return all(
            outcome.disposition is AssignmentDisposition.SUPPLIED_CANDIDATE
            for outcome in self.outcomes
        )


@dataclass(frozen=True, slots=True)
class AssignmentFalsifierResult:
    """One fixed v0.16 admission/assignment falsifier standing."""

    falsifier_id: str
    standing: AssignmentEvidenceStanding
    evidence: tuple[str, ...]
    limitation: str

    def __post_init__(self) -> None:
        if self.falsifier_id not in ASSIGNMENT_FALSIFIER_IDS:
            raise AssignmentAdmissionError("unknown assignment falsifier id")
        if not isinstance(self.standing, AssignmentEvidenceStanding):
            raise AssignmentAdmissionError(
                "assignment falsifier standing is invalid"
            )
        _require_text_items(self.evidence, "assignment falsifier evidence")
        _require_text(self.limitation, "assignment falsifier limitation")


def _build_results(
    trace: AssignmentAdmissionTrace,
) -> tuple[AssignmentFalsifierResult, ...]:
    return (
        AssignmentFalsifierResult(
            "AA01",
            AssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                "ContentAdapter:name+version+code-reference",
                "SubjectRecord:isolated-snapshot+encoded-bytes+digest",
                f"identity-role:{ADAPTER_EVIDENCE_IDENTITY_ROLE}",
            ),
            "support begins only after the caller supplies an adapter for the subject domain",
        ),
        AssignmentFalsifierResult(
            "AA02",
            AssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"trace:{trace.trace_id}",
                "ordered-occurrence-indexes:0..n-1",
                "equal-content-digests-remain-repeated",
            ),
            "occurrence preservation does not establish a geometric relation",
        ),
        AssignmentFalsifierResult(
            "AA03",
            AssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"outcome-relation:{ASSIGNMENT_OUTCOME_RELATION_STATUS}",
                "exclusive-tags:unresolved|supplied-candidate|rejected-mechanism",
                "malformed-combinations:fail-closed",
            ),
            "totality is over admitted evidence outcomes, not successful geometric assignments",
        ),
        AssignmentFalsifierResult(
            "AA04",
            AssignmentEvidenceStanding.NEGATIVE_SUPPORTED,
            tuple(
                f"rejected:{mechanism.value}"
                for mechanism in RejectedAssignmentMechanism
                if mechanism
                is not RejectedAssignmentMechanism.A0_BLAKE2_PHASE_LANES
            ),
            "digests, hashes, repr values, and object identities may identify evidence or diagnostics but cannot derive geometry",
        ),
        AssignmentFalsifierResult(
            "AA05",
            AssignmentEvidenceStanding.NEGATIVE_SUPPORTED,
            (
                "a0-commit:7af8debf6ef3905f01baff02b43d8c3bee16ccbc",
                "a0-blob:83a7d0088821d179de0d4264020663664bbec36c",
                f"rejected:{RejectedAssignmentMechanism.A0_BLAKE2_PHASE_LANES.value}",
            ),
            "A0 retains order and orientation clues, but its Blake2 lanes, fixed lane count, ordinary 2pi phase, and sine-sign chirality do not transfer as the assignment law",
        ),
        AssignmentFalsifierResult(
            "AA06",
            AssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                "GeometricAssignment:explicit-caller-supplied-only",
                "LawStanding:unresolved|experiment-candidate",
                f"selection-effect:{V016_SELECTION_EFFECT}",
            ),
            "the container validates evidence shape and linkage, not the truth or authority of the supplied candidate law",
        ),
        AssignmentFalsifierResult(
            "AA07",
            AssignmentEvidenceStanding.UNRESOLVED,
            (
                f"geometric-assignment:{ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS}",
                f"structural-null-relationship:{V015_COMPLETE_RELATIONSHIP_STATUS}",
            ),
            "no arbitrary-element geometry or total Structural Null initiation relationship is supplied",
        ),
    )


@dataclass(frozen=True, slots=True)
class AssignmentAdmissionBoundaryReport:
    """v0.16 admission evidence joined to unchanged v0.15 carrier standing."""

    upstream: FullCarrierAttachmentReport
    demonstration_trace: AssignmentAdmissionTrace
    results: tuple[AssignmentFalsifierResult, ...]
    schema_id: str = V016_ASSIGNMENT_ADMISSION_SCHEMA_ID
    schema_version: str = V016_ASSIGNMENT_ADMISSION_SCHEMA_VERSION
    admission_status: str = "implemented-explicit-adapter-domain"
    outcome_relation_status: str = ASSIGNMENT_OUTCOME_RELATION_STATUS
    arbitrary_element_assignment_status: str = (
        ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS
    )
    complete_relationship_status: str = V015_COMPLETE_RELATIONSHIP_STATUS
    selection_effect: str = V016_SELECTION_EFFECT
    edcm_activation: str = "inactive"
    metapat_activation: str = "inactive"
    hmmm: tuple[str, ...] = V016_HMMM

    def __post_init__(self) -> None:
        if not isinstance(self.upstream, FullCarrierAttachmentReport):
            raise AssignmentAdmissionError(
                "v0.16 report requires the exact v0.15 upstream report"
            )
        if not isinstance(self.demonstration_trace, AssignmentAdmissionTrace):
            raise AssignmentAdmissionError(
                "v0.16 report requires an assignment admission trace"
            )
        if self.results != _build_results(self.demonstration_trace):
            raise AssignmentAdmissionError(
                "v0.16 assignment falsifier packet is fixed"
            )
        if tuple(result.falsifier_id for result in self.results) != (
            ASSIGNMENT_FALSIFIER_IDS
        ):
            raise AssignmentAdmissionError(
                "v0.16 must retain AA01 through AA07 in order"
            )
        if (
            self.schema_id != V016_ASSIGNMENT_ADMISSION_SCHEMA_ID
            or self.schema_version != V016_ASSIGNMENT_ADMISSION_SCHEMA_VERSION
            or self.admission_status != "implemented-explicit-adapter-domain"
            or self.outcome_relation_status != ASSIGNMENT_OUTCOME_RELATION_STATUS
            or self.arbitrary_element_assignment_status
            != ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS
            or self.complete_relationship_status
            != V015_COMPLETE_RELATIONSHIP_STATUS
        ):
            raise AssignmentAdmissionError(
                "v0.16 schema and assignment standings are fixed"
            )
        if self.selection_effect != V016_SELECTION_EFFECT:
            raise AssignmentAdmissionError(
                "v0.16 cannot select geometry"
            )
        if self.edcm_activation != "inactive":
            raise AssignmentAdmissionError("v0.16 cannot activate EDCM")
        if self.metapat_activation != "inactive":
            raise AssignmentAdmissionError("v0.16 cannot activate METAPAT")
        if self.hmmm != V016_HMMM:
            raise AssignmentAdmissionError(
                "v0.16 unresolved boundary is fixed"
            )

    def result(self, falsifier_id: str) -> AssignmentFalsifierResult:
        for result in self.results:
            if result.falsifier_id == falsifier_id:
                return result
        raise AssignmentAdmissionError(
            f"unknown assignment falsifier: {falsifier_id}"
        )


def _demonstration_trace() -> AssignmentAdmissionTrace:
    adapter = text_content_adapter(
        name="ucns-v016-exact-text",
        version=V016_ASSIGNMENT_ADMISSION_SCHEMA_VERSION,
    )
    admissions = tuple(
        admit_observed_element(
            admission_id=f"v016-demo:occurrence:{index}",
            occurrence_index=index,
            subject_name=f"word-occurrence-{index}",
            subject=value,
            adapter=adapter,
            source_id="v016-demonstration",
            source_reference="fixture://assignment-admission",
            grain="word",
            provenance=("hand-authored boundary witness",),
        )
        for index, value in enumerate(("same", "same", "historical-phase"))
    )
    outcomes = (
        record_assignment_outcome(
            admissions[0],
            evidence=("no ratified arbitrary-element assignment law",),
        ),
        record_assignment_outcome(
            admissions[1],
            evidence=("duplicate occurrence retained without deduplication",),
        ),
        record_assignment_outcome(
            admissions[2],
            rejected_mechanism=(
                RejectedAssignmentMechanism.A0_BLAKE2_PHASE_LANES
            ),
            evidence=(
                "pinned A0 prototype mechanism rejected as final assignment law",
            ),
        ),
    )
    return AssignmentAdmissionTrace(
        trace_id="ucns-v016-assignment-admission-demonstration",
        outcomes=outcomes,
    )


def run_v016_assignment_admission_boundary_experiment(
) -> AssignmentAdmissionBoundaryReport:
    """Construct the fixed v0.16 admission and assignment-outcome evidence."""

    upstream = run_v015_full_carrier_attachment_experiment()
    trace = _demonstration_trace()
    return AssignmentAdmissionBoundaryReport(
        upstream=upstream,
        demonstration_trace=trace,
        results=_build_results(trace),
    )


__all__ = [
    "ADAPTER_EVIDENCE_IDENTITY_ROLE",
    "ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS",
    "ASSIGNMENT_ADMISSION_SCOPE",
    "ASSIGNMENT_FALSIFIER_IDS",
    "ASSIGNMENT_OUTCOME_RELATION_STATUS",
    "V016_ASSIGNMENT_ADMISSION_SCHEMA_ID",
    "V016_ASSIGNMENT_ADMISSION_SCHEMA_VERSION",
    "V016_HMMM",
    "V016_SELECTION_EFFECT",
    "AssignmentAdmissionBoundaryReport",
    "AssignmentAdmissionError",
    "AssignmentAdmissionTrace",
    "AssignmentDisposition",
    "AssignmentEvidenceStanding",
    "AssignmentFalsifierResult",
    "AssignmentOutcomeReceipt",
    "ObservedElementAdmission",
    "RejectedAssignmentMechanism",
    "admit_observed_element",
    "record_assignment_outcome",
    "run_v016_assignment_admission_boundary_experiment",
]
