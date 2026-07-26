# === MODULE_BUILD ===
# id: edcm_completion_motion_evidence
#   module_name: edcm_motion
#   module_kind: schema
#   summary: trajectory-first EDCM evidence for explicit geometric assignment, recursive motion, scoped completion, and recoverable lossy scalar projections
#   owner: Erin Spencer
#   public_surface: HmmmBoundary, GeometricAssignment, MotionStep, EpicyclicParentage, CompletionRegistration, EdcmMotionObservation, EdcmCompletionTrace, ScalarProjection, record_word_motion
#   internal_surface: validation helpers
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact observed word text and source provenance remain attached to every motion observation
#   admin_only: false
#   tests: tests/test_edcm_motion.py
#   rollout: experimental EDCM-only represented and candidate-measured trajectory evidence; no assignment law, completion law, or metric selection
#   rollback: remove this module and its public exports without changing the exact word-gonol observation profile
#   since: 2026-07-26
#   unresolved: element-assignment law, Mobius coordinates, circle-epicycle-disk-sphere transitions, higher-gonol composition, and canonical completion measurement
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: edcm_motion_retains_trajectory_identity
#   given: an exact EDCM word observation is bound to explicit geometric and motion evidence
#   then: source provenance, grain, relation, orientation, sidedness, motion, recursive parentage, completion effect, and unresolved capacity remain ordered and recoverable
#   class: evidence
#   since: 2026-07-26
#
# id: edcm_completion_is_scoped_not_epistemic_exhaustion
#   given: completion is registered for a declared construction boundary
#   then: the receipt cannot claim that the underlying unknowable has been exhausted
#   class: safety
#   since: 2026-07-26
#
# id: edcm_scalar_projection_is_declared_lossy
#   given: a scalar metric projection is attached to a motion observation
#   then: it names its policy, retains a source-observation link, declares information loss, and cannot replace the trajectory
#   class: safety
#   since: 2026-07-26
#
# id: edcm_unknown_motion_laws_remain_explicit
#   given: geometric assignment or motion evidence is recorded before the governing law is ratified
#   then: its standing is unresolved or candidate and no default or canonical law is inferred
#   class: doctrine
#   since: 2026-07-26
# === END CONTRACTS ===

"""Trajectory-first UCNS–EDCM completion-motion evidence.

This module implements the first recoverable slice above the exact word-gonol
observation floor. It records externally supplied assignment and motion evidence
without inventing the still-unresolved law that generates them.

The complete trajectory remains the evidence identity. Scalar metric values are
optional, explicitly lossy candidate projections linked back to their source
observation. Completion is registered only for a declared construction boundary;
it never claims epistemic exhaustion of the underlying unknowable.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from math import isfinite

from .edcm import EdcmTurnObservation


EDCM_MOTION_SCHEMA_ID = "ucns.edcm.completion-motion-evidence"
EDCM_MOTION_SCHEMA_VERSION = "0.1.0"
EDCM_MOTION_SCOPE = "edcm-only"
EDCM_MOTION_SELECTION_EFFECT = "none"
EDCM_ASSIGNMENT_LAW_STATUS = "hmmm-unresolved"
EDCM_HIGHER_MOTION_LAW_STATUS = "hmmm-unresolved"


class EdcmMotionError(ValueError):
    """Raised when completion-motion evidence crosses a declared boundary."""


class EvidenceStatus(str, Enum):
    """Statuses currently reachable by this experimental evidence surface."""

    REPRESENTED = "represented-evidence"
    CANDIDATE_MEASURED = "candidate-measured-evidence"


class LawStanding(str, Enum):
    """Noncanonical standing for externally supplied assignment or motion law."""

    UNRESOLVED = "unresolved"
    CANDIDATE = "experiment-candidate"


class GeometryKind(str, Enum):
    """Geometry named by the recovery root without selecting transition laws."""

    CIRCLE = "circle"
    EPICYCLE = "epicycle"
    DISK = "disk"
    SPHERE = "sphere"


class CompletionState(str, Enum):
    """State of a declared construction relative to its own boundary."""

    OPEN = "open"
    IN_MOTION = "in-motion"
    BLOCKED = "blocked"
    REGISTERED = "registered-complete"


class EdcmMetricFamily(str, Enum):
    """Candidate question-families; values are names, not selected formulas."""

    CONSTRAINT_MISMATCH = "constraint-mismatch"
    DISSONANCE_ACCUMULATION = "dissonance-accumulation"
    DRIFT = "drift"
    DIVERGENCE = "divergence"
    INTENSITY = "intensity"
    TURN_BALANCE = "turn-balance"

    @property
    def code(self) -> str:
        return {
            self.CONSTRAINT_MISMATCH: "CM",
            self.DISSONANCE_ACCUMULATION: "DA",
            self.DRIFT: "DRIFT",
            self.DIVERGENCE: "DVG",
            self.INTENSITY: "INT",
            self.TURN_BALANCE: "TBF",
        }[self]


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise EdcmMotionError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise EdcmMotionError(f"{field} must retain at least one item")
    for value in values:
        _require_text(value, field)


@dataclass(frozen=True, slots=True)
class HmmmBoundary:
    """Declared construction boundary plus honest unresolved constraints."""

    boundary_id: str
    declaration: str
    scope: str
    unresolved_constraints: tuple[str, ...]

    def __post_init__(self) -> None:
        _require_text(self.boundary_id, "boundary_id")
        _require_text(self.declaration, "declaration")
        _require_text(self.scope, "scope")
        _require_text_items(self.unresolved_constraints, "unresolved_constraints")


@dataclass(frozen=True, slots=True)
class SourceProvenance:
    """Explicit source identity for one observed element."""

    source_id: str
    source_reference: str
    speaker_id: str
    turn_index: int
    source_digest: str | None = None

    def __post_init__(self) -> None:
        _require_text(self.source_id, "source_id")
        _require_text(self.source_reference, "source_reference")
        _require_text(self.speaker_id, "speaker_id")
        if self.turn_index < 0:
            raise EdcmMotionError("turn_index must be nonnegative")
        if self.source_digest is not None:
            _require_text(self.source_digest, "source_digest")


@dataclass(frozen=True, slots=True)
class ObservedElement:
    """Exact observed element before any geometric assignment projection."""

    element_id: str
    raw_value: str
    grain: str
    ordinal: int
    source_start: int
    source_end: int
    provenance: SourceProvenance

    def __post_init__(self) -> None:
        _require_text(self.element_id, "element_id")
        if not isinstance(self.raw_value, str) or not self.raw_value:
            raise EdcmMotionError("raw_value must preserve a nonempty observed element")
        _require_text(self.grain, "grain")
        if self.ordinal < 0:
            raise EdcmMotionError("ordinal must be nonnegative")
        if self.source_start < 0 or self.source_end <= self.source_start:
            raise EdcmMotionError("source span is invalid")


@dataclass(frozen=True, slots=True)
class GeometricAssignment:
    """Explicit relation evidence; this object does not derive the assignment."""

    relation_id: str
    geometry: GeometryKind
    assignment_law_id: str
    assignment_law_version: str
    law_standing: LawStanding
    orientation: str
    sidedness: str
    parameters: tuple[tuple[str, str], ...] = ()
    evidence: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _require_text(self.relation_id, "relation_id")
        _require_text(self.assignment_law_id, "assignment_law_id")
        _require_text(self.assignment_law_version, "assignment_law_version")
        _require_text(self.orientation, "orientation")
        _require_text(self.sidedness, "sidedness")
        for key, value in self.parameters:
            _require_text(key, "parameter name")
            _require_text(value, "parameter value")
        _require_text_items(self.evidence, "assignment evidence")


@dataclass(frozen=True, slots=True)
class MotionStep:
    """Motion since the prior represented state, without a hidden formula."""

    step_id: str
    from_relation_id: str | None
    to_relation_id: str
    motion_law_id: str
    motion_law_version: str
    law_standing: LawStanding
    description: str
    path_evidence: tuple[str, ...]

    def __post_init__(self) -> None:
        _require_text(self.step_id, "step_id")
        if self.from_relation_id is not None:
            _require_text(self.from_relation_id, "from_relation_id")
        _require_text(self.to_relation_id, "to_relation_id")
        _require_text(self.motion_law_id, "motion_law_id")
        _require_text(self.motion_law_version, "motion_law_version")
        _require_text(self.description, "description")
        _require_text_items(self.path_evidence, "path_evidence")


@dataclass(frozen=True, slots=True)
class EpicyclicParentage:
    """Ordered recursive parentage; repeated parent occurrences are retained."""

    relation: str
    parent_observation_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        _require_text(self.relation, "parentage relation")
        for parent_id in self.parent_observation_ids:
            _require_text(parent_id, "parent_observation_id")
        if self.relation == "root" and self.parent_observation_ids:
            raise EdcmMotionError("root parentage cannot name a parent observation")
        if self.relation != "root" and not self.parent_observation_ids:
            raise EdcmMotionError("non-root parentage requires a parent observation")


@dataclass(frozen=True, slots=True)
class CompletionRegistration:
    """Completion effect scoped to one construction and declared boundary."""

    construction_id: str
    boundary_id: str
    condition_id: str
    state: CompletionState
    effect: str
    evidence: tuple[str, ...]
    remaining_unresolved_capacity: tuple[str, ...]
    underlying_unknowable_exhausted: bool = False

    def __post_init__(self) -> None:
        _require_text(self.construction_id, "construction_id")
        _require_text(self.boundary_id, "boundary_id")
        _require_text(self.condition_id, "condition_id")
        _require_text(self.effect, "completion effect")
        _require_text_items(self.evidence, "completion evidence")
        for item in self.remaining_unresolved_capacity:
            _require_text(item, "remaining_unresolved_capacity")
        if self.underlying_unknowable_exhausted:
            raise EdcmMotionError(
                "construction completion cannot exhaust the underlying unknowable"
            )


@dataclass(frozen=True, slots=True)
class ScalarProjection:
    """Optional candidate scalar projection with explicit recoverable loss."""

    metric_family: EdcmMetricFamily
    value: float
    unit: str
    policy_id: str
    policy_version: str
    source_observation_id: str
    information_loss: tuple[str, ...]

    def __post_init__(self) -> None:
        if (
            isinstance(self.value, bool)
            or not isinstance(self.value, (int, float))
            or not isfinite(float(self.value))
        ):
            raise EdcmMotionError("scalar projection value must be finite")
        _require_text(self.unit, "projection unit")
        _require_text(self.policy_id, "projection policy_id")
        _require_text(self.policy_version, "projection policy_version")
        _require_text(self.source_observation_id, "source_observation_id")
        _require_text_items(self.information_loss, "information_loss")


@dataclass(frozen=True, slots=True)
class EdcmMotionObservation:
    """One complete trajectory-bearing EDCM observation."""

    observation_id: str
    sequence_index: int
    element: ObservedElement
    boundary: HmmmBoundary
    assignment: GeometricAssignment
    motion: MotionStep
    parentage: EpicyclicParentage
    completion: CompletionRegistration
    measurement_status: EvidenceStatus = EvidenceStatus.REPRESENTED
    scalar_projections: tuple[ScalarProjection, ...] = ()

    def __post_init__(self) -> None:
        _require_text(self.observation_id, "observation_id")
        if self.sequence_index < 0:
            raise EdcmMotionError("sequence_index must be nonnegative")
        if self.assignment.relation_id != self.motion.to_relation_id:
            raise EdcmMotionError("motion must terminate at the assigned relation")
        if self.boundary.boundary_id != self.completion.boundary_id:
            raise EdcmMotionError("completion must use the declared hmmm boundary")
        if self.scalar_projections and (
            self.measurement_status is not EvidenceStatus.CANDIDATE_MEASURED
        ):
            raise EdcmMotionError(
                "scalar projections require candidate-measured evidence status"
            )
        for projection in self.scalar_projections:
            if projection.source_observation_id != self.observation_id:
                raise EdcmMotionError(
                    "scalar projection must link to its complete source observation"
                )


@dataclass(frozen=True, slots=True)
class EdcmCompletionTrace:
    """Ordered, append-only value object for a declared completion construction."""

    trace_id: str
    construction_id: str
    boundary: HmmmBoundary
    observations: tuple[EdcmMotionObservation, ...] = ()
    schema_id: str = EDCM_MOTION_SCHEMA_ID
    schema_version: str = EDCM_MOTION_SCHEMA_VERSION
    scope: str = EDCM_MOTION_SCOPE
    selection_effect: str = EDCM_MOTION_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.trace_id, "trace_id")
        _require_text(self.construction_id, "construction_id")
        if self.schema_id != EDCM_MOTION_SCHEMA_ID:
            raise EdcmMotionError("motion schema identity mismatch")
        if self.schema_version != EDCM_MOTION_SCHEMA_VERSION:
            raise EdcmMotionError("motion schema version mismatch")
        if self.scope != EDCM_MOTION_SCOPE:
            raise EdcmMotionError("motion evidence scope must remain EDCM-only")
        if self.selection_effect != "none":
            raise EdcmMotionError("motion evidence cannot select UCNS or EDCM canon")

        seen: set[str] = set()
        for expected_index, observation in enumerate(self.observations):
            if observation.sequence_index != expected_index:
                raise EdcmMotionError("motion observations must retain contiguous order")
            if observation.observation_id in seen:
                raise EdcmMotionError("motion observation ids must be unique")
            if observation.boundary != self.boundary:
                raise EdcmMotionError("every observation must retain the trace boundary")
            if observation.completion.construction_id != self.construction_id:
                raise EdcmMotionError("completion construction identity mismatch")
            for parent_id in observation.parentage.parent_observation_ids:
                if parent_id not in seen:
                    raise EdcmMotionError(
                        "epicyclic parentage must reference an earlier observation"
                    )
            seen.add(observation.observation_id)

    def append(self, observation: EdcmMotionObservation) -> "EdcmCompletionTrace":
        """Return a trace with one ordered observation appended and revalidated."""

        if observation.sequence_index != len(self.observations):
            raise EdcmMotionError("appended observation has the wrong sequence index")
        return replace(self, observations=self.observations + (observation,))

    @property
    def scalar_projections(self) -> tuple[ScalarProjection, ...]:
        return tuple(
            projection
            for observation in self.observations
            for projection in observation.scalar_projections
        )

    @property
    def registered_complete(self) -> bool:
        return bool(self.observations) and (
            self.observations[-1].completion.state is CompletionState.REGISTERED
        )


def record_word_motion(
    *,
    turn: EdcmTurnObservation,
    word_index: int,
    observation_id: str,
    sequence_index: int,
    source_reference: str,
    boundary: HmmmBoundary,
    assignment: GeometricAssignment,
    motion: MotionStep,
    parentage: EpicyclicParentage,
    completion: CompletionRegistration,
    measurement_status: EvidenceStatus = EvidenceStatus.REPRESENTED,
    scalar_projections: tuple[ScalarProjection, ...] = (),
    source_digest: str | None = None,
) -> EdcmMotionObservation:
    """Bind one exact word-gonol observation to supplied motion evidence."""

    if word_index < 0 or word_index >= len(turn.word_gonols):
        raise EdcmMotionError("word_index is outside the exact turn observation")
    word = turn.word_gonols[word_index]
    source_id = turn.source_id or source_reference
    provenance = SourceProvenance(
        source_id=source_id,
        source_reference=source_reference,
        speaker_id=turn.speaker_id,
        turn_index=turn.turn_index,
        source_digest=source_digest,
    )
    element = ObservedElement(
        element_id=f"{source_id}:turn:{turn.turn_index}:word:{word.word_index}",
        raw_value=word.raw_text,
        grain="word",
        ordinal=word.word_index,
        source_start=word.source_start,
        source_end=word.source_end,
        provenance=provenance,
    )
    return EdcmMotionObservation(
        observation_id=observation_id,
        sequence_index=sequence_index,
        element=element,
        boundary=boundary,
        assignment=assignment,
        motion=motion,
        parentage=parentage,
        completion=completion,
        measurement_status=measurement_status,
        scalar_projections=scalar_projections,
    )


__all__ = [
    "EDCM_ASSIGNMENT_LAW_STATUS",
    "EDCM_HIGHER_MOTION_LAW_STATUS",
    "EDCM_MOTION_SCHEMA_ID",
    "EDCM_MOTION_SCHEMA_VERSION",
    "EDCM_MOTION_SCOPE",
    "EDCM_MOTION_SELECTION_EFFECT",
    "CompletionRegistration",
    "CompletionState",
    "EdcmCompletionTrace",
    "EdcmMetricFamily",
    "EdcmMotionError",
    "EdcmMotionObservation",
    "EpicyclicParentage",
    "EvidenceStatus",
    "GeometricAssignment",
    "GeometryKind",
    "HmmmBoundary",
    "LawStanding",
    "MotionStep",
    "ObservedElement",
    "ScalarProjection",
    "SourceProvenance",
    "record_word_motion",
]
