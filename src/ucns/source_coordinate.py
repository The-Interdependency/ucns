# === MODULE_BUILD ===
# id: edcm_source_coordinate_derivation_boundary
#   module_name: source_coordinate
#   module_kind: experiment
#   summary: derives exact signed-local circle-candidate coordinates from complete finite ordered source-occurrence addresses while retaining exact upstream initiation identity and explicit blocked outcomes
#   owner: Erin Spencer
#   public_surface: OrderedSourceCoordinate, SourceCoordinateDerivation, AppliedSourceCoordinateAssignment, SourceCoordinateOutcome, SourceCoordinateTrace, SourceCoordinateBoundaryReport, SourceCoordinateDisposition, SourceCoordinateEvidenceStanding, SourceCoordinateFalsifierResult, derive_ordered_source_coordinate, derive_source_coordinate, apply_source_coordinate_assignment, derive_source_coordinate_trace, run_v019_source_coordinate_derivation_experiment
#   internal_surface: fixed SC01-SC10 evidence construction and exact validation helpers
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact v0.17 trace identity, source occurrence index, and complete finite scope cardinality derive coordinates; content, digests, runtime identity, carrier position, and projections do not
#   admin_only: false
#   tests: tests/test_source_coordinate.py
#   rollout: nonselecting v0.19 ordered-source-address derivation candidate over explicitly initiated words with explicit blocked outcomes and no completion or activation
#   rollback: remove this module, exports, tests, and v0.19 document while retaining v0.18 explicit-input candidate application
#   requires: edcm_explicit_geometric_assignment_boundary, edcm_gonol_initiation_structural_null_boundary, edcm_exact_coordinate_representation_boundary
#   since: 2026-07-31
#   unresolved: canonical law selection, cross-scope and higher-gonol composition, total Structural Null topology, higher geometry, completion, faithful breadth, and consumer activation
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: source_coordinate_law_uses_complete_ordered_source_address
#   given: an occurrence index i in a complete finite ordered scope of cardinality n
#   then: exact p=(2i+1)/(2n), u=2p-1, and t=2p derive only from the retained source address and invalid addresses fail closed
#   class: correctness
#   since: 2026-07-31
#
# id: source_coordinate_law_is_exact_and_scope_injective
#   given: distinct occurrence indices in the same declared finite scope
#   then: their exact source positions, transverse values, lifted turns, and coordinate identities remain distinct without binary64 conversion
#   class: correctness
#   since: 2026-07-31
#
# id: source_coordinate_derivation_retains_exact_initiation_identity
#   given: one initiated v0.17 outcome receives a derived coordinate
#   then: the exact upstream trace and outcome objects, admission, initiation, boundary, source address, law identity, formula, and code reference remain linked
#   class: evidence
#   since: 2026-07-31
#
# id: source_coordinate_assignment_applies_exact_candidate_reversibly
#   given: one valid source-coordinate derivation is applied
#   then: exact candidate and inverse, native frame, local side, GeometricAssignment, and declared-loss rendering remain mutually consistent
#   class: correctness
#   since: 2026-07-31
#
# id: source_coordinate_outcomes_are_total_exclusive_and_ordered
#   given: a complete v0.17 initiation trace enters v0.19
#   then: every exact outcome appears once in order as derived-assigned, blocked-unresolved, or blocked-rejected with no prefix, reordering, deduplication, or fallback
#   class: evidence
#   since: 2026-07-31
#
# id: source_coordinate_law_rejects_identity_shortcuts_and_nonselection
#   given: v0.19 evidence is reported
#   then: digests, runtime identity, A0 lanes, carrier position, projections, and renderings derive no coordinate while selection, higher geometry, completion, and activation remain absent
#   class: safety
#   since: 2026-07-31
# === END CONTRACTS ===

"""Exact ordered-source coordinate derivation evidence for UCNS v0.19.

For occurrence i in a complete finite ordered source scope of cardinality n,
the candidate law assigns exact midpoint p=(2*i+1)/(2*n), then derives signed
local transverse u=2*p-1 and lifted turns t=2*p. The map is exact and
injective within its declared scope. It uses source address and cardinality,
never content, digest, runtime identity, carrier position, projection, or
binary64 rendering.

Only explicitly initiated word outcomes receive geometry. Other initiation
outcomes remain explicit blockers. This implements a named candidate law; it
does not select the law, compose scopes or higher gonols, construct total
Structural Null topology, or register completion.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction

from .direct_mobius import NativeMobiusFrame
from .edcm_motion import GeometricAssignment, GeometryKind, LawStanding
from .exact_coordinate import (
    BINARY64_RENDERING_STATUS,
    EXACT_COORDINATE_CANDIDATE_ID,
    Binary64CarrierRendering,
    ExactCarrierCoordinate,
    recover_signed_local_transverse,
    render_exact_coordinate_binary64,
    signed_local_exact_coordinate,
)
from .explicit_geometric_assignment import (
    ExplicitGeometricAssignmentBoundaryReport,
    run_v018_explicit_geometric_assignment_experiment,
)
from .gonol_initiation import (
    TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS,
    GonolInitiationDisposition,
    GonolInitiationOutcome,
    GonolInitiationReceipt,
    GonolInitiationTrace,
)


V019_SOURCE_COORDINATE_SCHEMA_ID = "ucns.edcm.source-coordinate-derivation-boundary"
V019_SOURCE_COORDINATE_SCHEMA_VERSION = "0.19.0"
V019_SELECTION_EFFECT = "none"
SOURCE_COORDINATE_SCOPE = "complete-finite-ordered-v017-initiation-trace-occurrence-address"
SOURCE_COORDINATE_LAW_ID = "ucns.edcm.ordered-source-cell-midpoint-coordinate"
SOURCE_COORDINATE_LAW_VERSION = "0.19.0"
SOURCE_COORDINATE_LAW_FORMULA = "p=(2*i+1)/(2*n); u=2*p-1; t=2*p"
SOURCE_COORDINATE_CODE_REFERENCE = "src/ucns/source_coordinate.py:derive_ordered_source_coordinate"
SOURCE_COORDINATE_LAW_STATUS = "implemented-exact-finite-ordered-scope-candidate"
SOURCE_COORDINATE_ASSIGNMENT_STATUS = "source-address-derived-circle-candidate-assignment"
SOURCE_COORDINATE_OUTCOME_RELATION_STATUS = "total-tagged-over-complete-v017-initiation-trace"
ARBITRARY_SOURCE_ASSIGNMENT_STATUS = "partial-derived-for-initiated-word-outcomes-with-explicit-blockers"
SOURCE_COORDINATE_HIGHER_GEOMETRY_STATUS = "unresolved-circle-entry-only"
SOURCE_COORDINATE_FALSIFIER_IDS = tuple(f"SC{index:02d}" for index in range(1, 11))
V019_HMMM = (
    "selection or canonization of the ordered-source midpoint law remains unresolved",
    "cross-scope stability and higher-gonol composition are not supplied by a finite trace-local address law",
    "the total topology from singular Structural Null to arbitrary non-null carrier states remains unresolved",
    "circle-to-epicycle, epicycle-to-disk, disk-to-sphere, and recursive scale transitions remain unresolved",
    "scoped completion, canonical B, proof-assistant formalization, carrier selection, and consumer activation remain unresolved",
)


class SourceCoordinateError(ValueError):
    """Raised when v0.19 evidence crosses its derivation boundary."""


class SourceCoordinateDisposition(str, Enum):
    DERIVED_ASSIGNED = "source-coordinate-derived-and-assigned"
    BLOCKED_UNRESOLVED = "blocked-by-unresolved-initiation"
    BLOCKED_REJECTED = "blocked-by-rejected-initiation"


class SourceCoordinateEvidenceStanding(str, Enum):
    EXACT_IMPLEMENTED_SUPPORTED = "exact-implemented-supported"
    BOUNDED_UPSTREAM_SUPPORTED = "bounded-upstream-supported"
    NEGATIVE_SUPPORTED = "negative-supported"
    UNRESOLVED = "unresolved"


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise SourceCoordinateError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise SourceCoordinateError(f"{field} must retain evidence")
    for value in values:
        _require_text(value, field)


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _expected_frame(lifted_turns: Fraction) -> NativeMobiusFrame:
    return NativeMobiusFrame.POSITIVE if lifted_turns < 1 else NativeMobiusFrame.REVERSED


def _local_side(local_transverse: Fraction) -> str:
    if local_transverse < 0:
        return "local-negative"
    if local_transverse > 0:
        return "local-positive"
    return "local-root"


@dataclass(frozen=True, slots=True)
class OrderedSourceCoordinate:
    occurrence_index: int
    scope_cardinality: int
    source_position: Fraction
    local_transverse: Fraction
    lifted_turns: Fraction
    frame: NativeMobiusFrame
    law_id: str = SOURCE_COORDINATE_LAW_ID
    law_version: str = SOURCE_COORDINATE_LAW_VERSION
    formula: str = SOURCE_COORDINATE_LAW_FORMULA
    code_reference: str = SOURCE_COORDINATE_CODE_REFERENCE
    scope: str = SOURCE_COORDINATE_SCOPE
    selection_effect: str = V019_SELECTION_EFFECT

    def __post_init__(self) -> None:
        if (
            not isinstance(self.occurrence_index, int)
            or isinstance(self.occurrence_index, bool)
            or not isinstance(self.scope_cardinality, int)
            or isinstance(self.scope_cardinality, bool)
        ):
            raise SourceCoordinateError("source address fields must be integers")
        if self.scope_cardinality <= 0 or not 0 <= self.occurrence_index < self.scope_cardinality:
            raise SourceCoordinateError("source address lies outside the complete scope")
        if not all(
            isinstance(value, Fraction)
            for value in (self.source_position, self.local_transverse, self.lifted_turns)
        ):
            raise SourceCoordinateError("source coordinates must be exact Fractions")
        expected_position = Fraction(2 * self.occurrence_index + 1, 2 * self.scope_cardinality)
        expected_transverse = 2 * expected_position - 1
        expected_turns = 2 * expected_position
        if self.source_position != expected_position:
            raise SourceCoordinateError("source_position must be the ordered-cell midpoint")
        if self.local_transverse != expected_transverse:
            raise SourceCoordinateError("local_transverse must equal 2*p-1")
        if self.lifted_turns != expected_turns:
            raise SourceCoordinateError("lifted_turns must equal 2*p")
        if not 0 < self.source_position < 1 or not -1 < self.local_transverse < 1 or not 0 < self.lifted_turns < 2:
            raise SourceCoordinateError("derived coordinate lies outside its exact open intervals")
        if self.frame is not _expected_frame(self.lifted_turns):
            raise SourceCoordinateError("frame must follow native two-turn parity")
        if (
            self.law_id,
            self.law_version,
            self.formula,
            self.code_reference,
            self.scope,
            self.selection_effect,
        ) != (
            SOURCE_COORDINATE_LAW_ID,
            SOURCE_COORDINATE_LAW_VERSION,
            SOURCE_COORDINATE_LAW_FORMULA,
            SOURCE_COORDINATE_CODE_REFERENCE,
            SOURCE_COORDINATE_SCOPE,
            V019_SELECTION_EFFECT,
        ):
            raise SourceCoordinateError("ordered-source coordinate law identity is fixed")

    @property
    def local_side(self) -> str:
        return _local_side(self.local_transverse)

    @property
    def exact_identity(self) -> tuple[object, ...]:
        return (
            self.occurrence_index,
            self.scope_cardinality,
            _fraction_key(self.source_position),
            _fraction_key(self.local_transverse),
            _fraction_key(self.lifted_turns),
            self.frame.value,
            self.local_side,
            self.law_id,
            self.law_version,
            self.formula,
            self.code_reference,
            self.scope,
        )


def derive_ordered_source_coordinate(
    occurrence_index: int,
    scope_cardinality: int,
) -> OrderedSourceCoordinate:
    if (
        not isinstance(occurrence_index, int)
        or isinstance(occurrence_index, bool)
        or not isinstance(scope_cardinality, int)
        or isinstance(scope_cardinality, bool)
    ):
        raise TypeError("source address fields must be integers")
    if scope_cardinality <= 0 or not 0 <= occurrence_index < scope_cardinality:
        raise SourceCoordinateError("source address requires 0 <= i < n")
    position = Fraction(2 * occurrence_index + 1, 2 * scope_cardinality)
    transverse = 2 * position - 1
    turns = 2 * position
    return OrderedSourceCoordinate(
        occurrence_index,
        scope_cardinality,
        position,
        transverse,
        turns,
        _expected_frame(turns),
    )


def _derivation_evidence(
    trace: GonolInitiationTrace,
    outcome: GonolInitiationOutcome,
    address: OrderedSourceCoordinate,
) -> tuple[str, ...]:
    return (
        f"upstream-trace:{trace.trace_id}",
        f"upstream-outcome:{outcome.outcome_id}",
        f"source-address:{address.occurrence_index}/{address.scope_cardinality}",
        f"law:{SOURCE_COORDINATE_LAW_ID}/{SOURCE_COORDINATE_LAW_VERSION}",
        f"formula:{SOURCE_COORDINATE_LAW_FORMULA}",
        f"code-reference:{SOURCE_COORDINATE_CODE_REFERENCE}",
        "content-and-digest-not-used",
    )


@dataclass(frozen=True, slots=True)
class SourceCoordinateDerivation:
    derivation_id: str
    upstream_trace: GonolInitiationTrace
    upstream_outcome: GonolInitiationOutcome
    address: OrderedSourceCoordinate
    evidence: tuple[str, ...]
    derived_from_source_occurrence_address: bool = True
    derived_from_content_or_digest: bool = False
    scope: str = SOURCE_COORDINATE_SCOPE
    selection_effect: str = V019_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.derivation_id, "derivation_id")
        if not isinstance(self.upstream_trace, GonolInitiationTrace):
            raise SourceCoordinateError("derivation requires exact upstream trace")
        if not isinstance(self.upstream_outcome, GonolInitiationOutcome):
            raise SourceCoordinateError("derivation requires exact upstream outcome")
        if not isinstance(self.address, OrderedSourceCoordinate):
            raise SourceCoordinateError("derivation requires ordered source coordinate")
        index = self.upstream_outcome.admission.occurrence_index
        if self.address.occurrence_index != index:
            raise SourceCoordinateError("address must retain occurrence index")
        if self.address.scope_cardinality != len(self.upstream_trace.outcomes):
            raise SourceCoordinateError("address must bind complete scope cardinality")
        if self.upstream_trace.outcomes[index] is not self.upstream_outcome:
            raise SourceCoordinateError("derivation must retain exact upstream outcome object")
        if (
            self.upstream_outcome.disposition is not GonolInitiationDisposition.INITIATED
            or self.upstream_outcome.initiation is None
        ):
            raise SourceCoordinateError("only an initiated word can derive geometry")
        if self.derivation_id != f"{self.upstream_outcome.outcome_id}:source-coordinate":
            raise SourceCoordinateError("derivation id must derive from upstream outcome")
        if self.evidence != _derivation_evidence(self.upstream_trace, self.upstream_outcome, self.address):
            raise SourceCoordinateError("derivation evidence is fixed")
        if not self.derived_from_source_occurrence_address or self.derived_from_content_or_digest:
            raise SourceCoordinateError("only source occurrence address may derive coordinates")
        if self.scope != SOURCE_COORDINATE_SCOPE or self.selection_effect != V019_SELECTION_EFFECT:
            raise SourceCoordinateError("derivation scope and nonselection are fixed")

    @property
    def initiation(self) -> GonolInitiationReceipt:
        initiation = self.upstream_outcome.initiation
        if initiation is None:
            raise SourceCoordinateError("derivation lost upstream initiation")
        return initiation

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        return (
            self.derivation_id,
            self.upstream_trace.trace_id,
            self.upstream_outcome.outcome_id,
            self.initiation.evidence_identity,
            self.address.exact_identity,
            self.evidence,
            self.derived_from_source_occurrence_address,
            self.derived_from_content_or_digest,
            self.scope,
        )


def derive_source_coordinate(
    upstream_trace: GonolInitiationTrace,
    upstream_outcome: GonolInitiationOutcome,
) -> SourceCoordinateDerivation:
    if not isinstance(upstream_trace, GonolInitiationTrace):
        raise TypeError("upstream_trace must be GonolInitiationTrace")
    if not isinstance(upstream_outcome, GonolInitiationOutcome):
        raise TypeError("upstream_outcome must be GonolInitiationOutcome")
    address = derive_ordered_source_coordinate(
        upstream_outcome.admission.occurrence_index,
        len(upstream_trace.outcomes),
    )
    return SourceCoordinateDerivation(
        f"{upstream_outcome.outcome_id}:source-coordinate",
        upstream_trace,
        upstream_outcome,
        address,
        _derivation_evidence(upstream_trace, upstream_outcome, address),
    )


def _assignment_parameters(
    derivation: SourceCoordinateDerivation,
    coordinate: ExactCarrierCoordinate,
) -> tuple[tuple[str, str], ...]:
    address = derivation.address
    return (
        ("candidate-id", EXACT_COORDINATE_CANDIDATE_ID),
        ("source-trace-id", derivation.upstream_trace.trace_id),
        ("source-occurrence-index", str(address.occurrence_index)),
        ("source-scope-cardinality", str(address.scope_cardinality)),
        ("source-position", _fraction_key(address.source_position)),
        ("local-transverse", _fraction_key(coordinate.local_transverse)),
        ("breadth", _fraction_key(coordinate.breadth)),
        ("lifted-turns", _fraction_key(coordinate.lifted_turns)),
        ("source-coordinate-law-formula", SOURCE_COORDINATE_LAW_FORMULA),
    )


def _assignment_evidence(
    derivation: SourceCoordinateDerivation,
) -> tuple[str, ...]:
    return (
        f"derivation:{derivation.derivation_id}",
        f"initiation-receipt:{derivation.initiation.receipt_id}",
        f"upstream-outcome:{derivation.upstream_outcome.outcome_id}",
        f"code-reference:{SOURCE_COORDINATE_CODE_REFERENCE}",
        "exact-source-address-coordinate-and-inverse-validated",
    )


@dataclass(frozen=True, slots=True)
class AppliedSourceCoordinateAssignment:
    receipt_id: str
    derivation: SourceCoordinateDerivation
    exact_coordinate: ExactCarrierCoordinate
    rendering: Binary64CarrierRendering
    assignment: GeometricAssignment
    exact_coordinate_role: str = "authoritative-candidate-evidence-identity"
    rendering_role: str = BINARY64_RENDERING_STATUS
    source_coordinate_law_status: str = SOURCE_COORDINATE_LAW_STATUS
    completion_registered: bool = False
    parent_gonol_ids: tuple[str, ...] = ()
    scope: str = SOURCE_COORDINATE_SCOPE
    selection_effect: str = V019_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.receipt_id, "assignment receipt_id")
        if not isinstance(self.derivation, SourceCoordinateDerivation):
            raise SourceCoordinateError("assignment requires a source derivation")
        if self.receipt_id != f"{self.derivation.derivation_id}:assignment":
            raise SourceCoordinateError("assignment id must derive from derivation")
        address = self.derivation.address
        expected_coordinate = signed_local_exact_coordinate(
            address.local_transverse,
            address.lifted_turns,
        )
        if self.exact_coordinate != expected_coordinate:
            raise SourceCoordinateError("assignment must retain exact derived coordinate")
        if recover_signed_local_transverse(self.exact_coordinate) != address.local_transverse:
            raise SourceCoordinateError("assignment must retain exact inverse")
        expected_rendering = render_exact_coordinate_binary64(self.exact_coordinate)
        if (
            self.rendering.exact_coordinate != expected_rendering.exact_coordinate
            or self.rendering.rendering_identity != expected_rendering.rendering_identity
            or self.rendering.rendering_policy_id != expected_rendering.rendering_policy_id
            or self.rendering.rendering_policy_version != expected_rendering.rendering_policy_version
            or self.rendering.code_reference != expected_rendering.code_reference
            or self.rendering.information_loss != expected_rendering.information_loss
            or self.rendering.status != expected_rendering.status
            or self.rendering.selection_effect != expected_rendering.selection_effect
        ):
            raise SourceCoordinateError("rendering must retain exact coordinate source")
        initiation = self.derivation.initiation
        relation_id = f"{initiation.gonol_id}:source-derived-circle-candidate-relation"
        if (
            not isinstance(self.assignment, GeometricAssignment)
            or self.assignment.relation_id != relation_id
            or self.assignment.geometry is not GeometryKind.CIRCLE
            or self.assignment.assignment_law_id != SOURCE_COORDINATE_LAW_ID
            or self.assignment.assignment_law_version != SOURCE_COORDINATE_LAW_VERSION
            or self.assignment.law_standing is not LawStanding.CANDIDATE
            or self.assignment.orientation != address.frame.value
            or self.assignment.sidedness != address.local_side
            or self.assignment.parameters != _assignment_parameters(self.derivation, self.exact_coordinate)
            or self.assignment.evidence != _assignment_evidence(self.derivation)
        ):
            raise SourceCoordinateError("source-derived assignment fields are fixed")
        if (
            self.exact_coordinate_role != "authoritative-candidate-evidence-identity"
            or self.rendering_role != BINARY64_RENDERING_STATUS
            or self.source_coordinate_law_status != SOURCE_COORDINATE_LAW_STATUS
        ):
            raise SourceCoordinateError("exact and rendered evidence roles are fixed")
        if self.completion_registered or self.parent_gonol_ids:
            raise SourceCoordinateError("assignment cannot complete or compose higher gonols")
        if self.scope != SOURCE_COORDINATE_SCOPE or self.selection_effect != V019_SELECTION_EFFECT:
            raise SourceCoordinateError("assignment scope and nonselection are fixed")

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        return (
            self.receipt_id,
            self.derivation.evidence_identity,
            self.exact_coordinate.exact_identity,
            self.assignment.relation_id,
            self.assignment.assignment_law_id,
            self.assignment.assignment_law_version,
            self.assignment.orientation,
            self.assignment.sidedness,
            self.assignment.parameters,
            self.assignment.evidence,
            self.exact_coordinate_role,
            self.rendering_role,
            self.scope,
        )


def apply_source_coordinate_assignment(
    derivation: SourceCoordinateDerivation,
) -> AppliedSourceCoordinateAssignment:
    if not isinstance(derivation, SourceCoordinateDerivation):
        raise TypeError("derivation must be SourceCoordinateDerivation")
    address = derivation.address
    coordinate = signed_local_exact_coordinate(
        address.local_transverse,
        address.lifted_turns,
    )
    assignment = GeometricAssignment(
        relation_id=(
            f"{derivation.initiation.gonol_id}:"
            "source-derived-circle-candidate-relation"
        ),
        geometry=GeometryKind.CIRCLE,
        assignment_law_id=SOURCE_COORDINATE_LAW_ID,
        assignment_law_version=SOURCE_COORDINATE_LAW_VERSION,
        law_standing=LawStanding.CANDIDATE,
        orientation=address.frame.value,
        sidedness=address.local_side,
        parameters=_assignment_parameters(derivation, coordinate),
        evidence=_assignment_evidence(derivation),
    )
    return AppliedSourceCoordinateAssignment(
        f"{derivation.derivation_id}:assignment",
        derivation,
        coordinate,
        render_exact_coordinate_binary64(coordinate),
        assignment,
    )


@dataclass(frozen=True, slots=True)
class SourceCoordinateOutcome:
    outcome_id: str
    upstream: GonolInitiationOutcome
    disposition: SourceCoordinateDisposition
    evidence: tuple[str, ...]
    applied_assignment: AppliedSourceCoordinateAssignment | None = None
    scope: str = SOURCE_COORDINATE_SCOPE
    selection_effect: str = V019_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.outcome_id, "source-coordinate outcome_id")
        if not isinstance(self.upstream, GonolInitiationOutcome):
            raise SourceCoordinateError("outcome requires upstream initiation outcome")
        if self.outcome_id != f"{self.upstream.outcome_id}:source-coordinate-outcome":
            raise SourceCoordinateError("outcome id must derive from upstream")
        if not isinstance(self.disposition, SourceCoordinateDisposition):
            raise SourceCoordinateError("source-coordinate disposition is invalid")
        _require_text_items(self.evidence, "source-coordinate outcome evidence")
        if self.evidence != _outcome_evidence(self.upstream, self.disposition):
            raise SourceCoordinateError("source-coordinate outcome evidence is fixed")
        if self.scope != SOURCE_COORDINATE_SCOPE or self.selection_effect != V019_SELECTION_EFFECT:
            raise SourceCoordinateError("outcome scope and nonselection are fixed")
        if self.disposition is SourceCoordinateDisposition.DERIVED_ASSIGNED:
            if not isinstance(self.applied_assignment, AppliedSourceCoordinateAssignment):
                raise SourceCoordinateError("derived outcome requires assignment")
            if (
                self.upstream.disposition is not GonolInitiationDisposition.INITIATED
                or self.applied_assignment.derivation.upstream_outcome is not self.upstream
            ):
                raise SourceCoordinateError("assignment must retain exact initiated outcome")
        elif self.applied_assignment is not None:
            raise SourceCoordinateError("blocked outcome cannot carry assignment")
        elif (
            self.disposition is SourceCoordinateDisposition.BLOCKED_UNRESOLVED
            and self.upstream.disposition is not GonolInitiationDisposition.UNRESOLVED
        ):
            raise SourceCoordinateError("unresolved blocker must retain upstream standing")
        elif (
            self.disposition is SourceCoordinateDisposition.BLOCKED_REJECTED
            and self.upstream.disposition is not GonolInitiationDisposition.REJECTED_SUBSTITUTION
        ):
            raise SourceCoordinateError("rejected blocker must retain upstream standing")


def _outcome_evidence(
    upstream: GonolInitiationOutcome,
    disposition: SourceCoordinateDisposition,
) -> tuple[str, ...]:
    return (
        f"upstream-outcome:{upstream.outcome_id}",
        f"source-coordinate-disposition:{disposition.value}",
        "no-hidden-coordinate-default",
    )


def _record_source_coordinate_outcome(
    trace: GonolInitiationTrace,
    upstream: GonolInitiationOutcome,
) -> SourceCoordinateOutcome:
    if upstream.disposition is GonolInitiationDisposition.INITIATED:
        applied = apply_source_coordinate_assignment(
            derive_source_coordinate(trace, upstream)
        )
        disposition = SourceCoordinateDisposition.DERIVED_ASSIGNED
    elif upstream.disposition is GonolInitiationDisposition.UNRESOLVED:
        applied = None
        disposition = SourceCoordinateDisposition.BLOCKED_UNRESOLVED
    else:
        applied = None
        disposition = SourceCoordinateDisposition.BLOCKED_REJECTED
    return SourceCoordinateOutcome(
        f"{upstream.outcome_id}:source-coordinate-outcome",
        upstream,
        disposition,
        _outcome_evidence(upstream, disposition),
        applied,
    )


@dataclass(frozen=True, slots=True)
class SourceCoordinateTrace:
    trace_id: str
    upstream_trace: GonolInitiationTrace
    outcomes: tuple[SourceCoordinateOutcome, ...]
    scope: str = SOURCE_COORDINATE_SCOPE
    outcome_relation_status: str = SOURCE_COORDINATE_OUTCOME_RELATION_STATUS
    selection_effect: str = V019_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.trace_id, "source-coordinate trace_id")
        if not isinstance(self.upstream_trace, GonolInitiationTrace):
            raise SourceCoordinateError("trace requires exact upstream trace")
        if not self.outcomes or len(self.outcomes) != len(self.upstream_trace.outcomes):
            raise SourceCoordinateError("trace must retain complete nonempty upstream")
        if (
            self.scope != SOURCE_COORDINATE_SCOPE
            or self.outcome_relation_status != SOURCE_COORDINATE_OUTCOME_RELATION_STATUS
            or self.selection_effect != V019_SELECTION_EFFECT
        ):
            raise SourceCoordinateError("trace scope and standing are fixed")
        outcome_ids: set[str] = set()
        coordinate_ids: set[tuple[tuple[str, str], ...]] = set()
        for index, (upstream, outcome) in enumerate(
            zip(self.upstream_trace.outcomes, self.outcomes, strict=True)
        ):
            if not isinstance(outcome, SourceCoordinateOutcome):
                raise SourceCoordinateError("trace contains invalid outcome")
            if outcome.upstream is not upstream:
                raise SourceCoordinateError("trace must retain exact upstream objects")
            if upstream.admission.occurrence_index != index:
                raise SourceCoordinateError("upstream order must remain contiguous")
            if outcome.outcome_id in outcome_ids:
                raise SourceCoordinateError("outcome identities must be unique")
            outcome_ids.add(outcome.outcome_id)
            applied = outcome.applied_assignment
            if applied is not None:
                if applied.derivation.upstream_trace is not self.upstream_trace:
                    raise SourceCoordinateError("derivation must retain exact full trace")
                coordinate_id = applied.exact_coordinate.exact_identity
                if coordinate_id in coordinate_ids:
                    raise SourceCoordinateError("derived coordinates must be injective")
                coordinate_ids.add(coordinate_id)

    @property
    def assignments(self) -> tuple[AppliedSourceCoordinateAssignment, ...]:
        return tuple(
            outcome.applied_assignment
            for outcome in self.outcomes
            if outcome.applied_assignment is not None
        )

    @property
    def has_total_outcome_evidence(self) -> bool:
        return len(self.outcomes) == len(self.upstream_trace.outcomes)


def derive_source_coordinate_trace(
    upstream_trace: GonolInitiationTrace,
) -> SourceCoordinateTrace:
    if not isinstance(upstream_trace, GonolInitiationTrace):
        raise TypeError("upstream_trace must be GonolInitiationTrace")
    return SourceCoordinateTrace(
        f"{upstream_trace.trace_id}:source-coordinate-trace",
        upstream_trace,
        tuple(
            _record_source_coordinate_outcome(upstream_trace, outcome)
            for outcome in upstream_trace.outcomes
        ),
    )


@dataclass(frozen=True, slots=True)
class SourceCoordinateFalsifierResult:
    falsifier_id: str
    standing: SourceCoordinateEvidenceStanding
    evidence: tuple[str, ...]
    limitation: str

    def __post_init__(self) -> None:
        if self.falsifier_id not in SOURCE_COORDINATE_FALSIFIER_IDS:
            raise SourceCoordinateError("unknown source-coordinate falsifier")
        if not isinstance(self.standing, SourceCoordinateEvidenceStanding):
            raise SourceCoordinateError("invalid source-coordinate standing")
        _require_text_items(self.evidence, "source-coordinate falsifier evidence")
        _require_text(self.limitation, "source-coordinate limitation")


def _build_results(
    trace: SourceCoordinateTrace,
) -> tuple[SourceCoordinateFalsifierResult, ...]:
    assignments = trace.assignments
    derived_ids = tuple(item.exact_coordinate.exact_identity for item in assignments)
    blockers = len(trace.outcomes) - len(assignments)
    return (
        SourceCoordinateFalsifierResult(
            "SC01",
            SourceCoordinateEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"upstream-trace:{trace.upstream_trace.trace_id}",
                f"scope-cardinality:{len(trace.upstream_trace.outcomes)}",
                "address:occurrence-index+complete-scope-cardinality",
            ),
            "the law is trace-local and does not establish cross-scope composition",
        ),
        SourceCoordinateFalsifierResult(
            "SC02",
            SourceCoordinateEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"law:{SOURCE_COORDINATE_LAW_ID}/{SOURCE_COORDINATE_LAW_VERSION}",
                f"formula:{SOURCE_COORDINATE_LAW_FORMULA}",
                "arithmetic:Fraction-only",
            ),
            "exact execution does not canonize the law",
        ),
        SourceCoordinateFalsifierResult(
            "SC03",
            SourceCoordinateEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                "scope-injectivity:distinct-indices-have-distinct-midpoints",
                f"derived-count:{len(derived_ids)}",
                f"unique-derived-count:{len(set(derived_ids))}",
            ),
            "injectivity is within one declared complete finite scope",
        ),
        SourceCoordinateFalsifierResult(
            "SC04",
            SourceCoordinateEvidenceStanding.BOUNDED_UPSTREAM_SUPPORTED,
            (
                f"applied-assignments:{len(assignments)}",
                "exact-law:B(u)=1+u/2",
                "exact-inverse:u=2*(B-1)",
                "frame:native-two-turn-parity",
                "side:sign-of-u",
            ),
            "the v0.11 circle coordinate remains a nonselected candidate",
        ),
        SourceCoordinateFalsifierResult(
            "SC05",
            SourceCoordinateEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"outcome-relation:{SOURCE_COORDINATE_OUTCOME_RELATION_STATUS}",
                f"outcome-count:{len(trace.outcomes)}",
                f"blocked-outcomes:{blockers}",
                "exclusive-tags:derived|blocked-unresolved|blocked-rejected",
            ),
            "totality is over exact upstream outcomes, not all possible subjects",
        ),
        SourceCoordinateFalsifierResult(
            "SC06",
            SourceCoordinateEvidenceStanding.NEGATIVE_SUPPORTED,
            (
                "content-digest:unused",
                "runtime-hash-repr-object-id:unused",
                "a0-blake2-phase-lanes:unused",
                "carrier-position-and-scalar-projection:unused",
            ),
            "negative evidence does not establish semantic adequacy",
        ),
        SourceCoordinateFalsifierResult(
            "SC07",
            SourceCoordinateEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                "upstream-object-identity:retained",
                "prefixes-and-reordering:rejected",
                "equal-content-occurrences:addressed-separately",
            ),
            "source address preserves occurrence identity rather than content meaning",
        ),
        SourceCoordinateFalsifierResult(
            "SC08",
            SourceCoordinateEvidenceStanding.NEGATIVE_SUPPORTED,
            (
                "exact-coordinate:authoritative-candidate-evidence",
                f"binary64:{BINARY64_RENDERING_STATUS}",
                "rendering-cannot-replace-exact-identity",
            ),
            "rendering remains only a linked lossy view",
        ),
        SourceCoordinateFalsifierResult(
            "SC09",
            SourceCoordinateEvidenceStanding.UNRESOLVED,
            (
                f"law-standing:{LawStanding.CANDIDATE.value}",
                f"selection-effect:{V019_SELECTION_EFFECT}",
                "cross-scope-composition:unresolved",
            ),
            "implementation and falsifiability do not select the law",
        ),
        SourceCoordinateFalsifierResult(
            "SC10",
            SourceCoordinateEvidenceStanding.UNRESOLVED,
            (
                f"total-structural-null-topology:{TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS}",
                f"higher-geometry:{SOURCE_COORDINATE_HIGHER_GEOMETRY_STATUS}",
                "completion:unregistered",
                "consumer-activation:inactive",
            ),
            "coordinate derivation is not topology, higher motion, or completion",
        ),
    )


@dataclass(frozen=True, slots=True)
class SourceCoordinateBoundaryReport:
    upstream: ExplicitGeometricAssignmentBoundaryReport
    demonstration_trace: SourceCoordinateTrace
    results: tuple[SourceCoordinateFalsifierResult, ...]
    schema_id: str = V019_SOURCE_COORDINATE_SCHEMA_ID
    schema_version: str = V019_SOURCE_COORDINATE_SCHEMA_VERSION
    law_status: str = SOURCE_COORDINATE_LAW_STATUS
    assignment_status: str = SOURCE_COORDINATE_ASSIGNMENT_STATUS
    arbitrary_source_assignment_status: str = ARBITRARY_SOURCE_ASSIGNMENT_STATUS
    total_structural_null_topology_status: str = TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS
    higher_geometry_status: str = SOURCE_COORDINATE_HIGHER_GEOMETRY_STATUS
    selection_effect: str = V019_SELECTION_EFFECT
    edcm_activation: str = "inactive"
    metapat_activation: str = "inactive"
    hmmm: tuple[str, ...] = V019_HMMM

    def __post_init__(self) -> None:
        if not isinstance(self.upstream, ExplicitGeometricAssignmentBoundaryReport):
            raise SourceCoordinateError("report requires exact v0.18 report")
        if not isinstance(self.demonstration_trace, SourceCoordinateTrace):
            raise SourceCoordinateError("report requires source-coordinate trace")
        exact_trace = self.upstream.upstream.demonstration_trace
        if self.demonstration_trace.upstream_trace is not exact_trace:
            raise SourceCoordinateError("report must retain exact v0.17 trace object")
        if not self.demonstration_trace.assignments:
            raise SourceCoordinateError("demonstration requires a derived assignment")
        if self.results != _build_results(self.demonstration_trace):
            raise SourceCoordinateError("falsifier packet must match exact evidence")
        if tuple(item.falsifier_id for item in self.results) != SOURCE_COORDINATE_FALSIFIER_IDS:
            raise SourceCoordinateError("report must retain SC01-SC10 in order")
        if (
            self.schema_id,
            self.schema_version,
            self.law_status,
            self.assignment_status,
            self.arbitrary_source_assignment_status,
            self.total_structural_null_topology_status,
            self.higher_geometry_status,
            self.selection_effect,
            self.edcm_activation,
            self.metapat_activation,
            self.hmmm,
        ) != (
            V019_SOURCE_COORDINATE_SCHEMA_ID,
            V019_SOURCE_COORDINATE_SCHEMA_VERSION,
            SOURCE_COORDINATE_LAW_STATUS,
            SOURCE_COORDINATE_ASSIGNMENT_STATUS,
            ARBITRARY_SOURCE_ASSIGNMENT_STATUS,
            TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS,
            SOURCE_COORDINATE_HIGHER_GEOMETRY_STATUS,
            V019_SELECTION_EFFECT,
            "inactive",
            "inactive",
            V019_HMMM,
        ):
            raise SourceCoordinateError("v0.19 schema and boundary are fixed")

    def result(self, falsifier_id: str) -> SourceCoordinateFalsifierResult:
        for result in self.results:
            if result.falsifier_id == falsifier_id:
                return result
        raise SourceCoordinateError(f"unknown source-coordinate falsifier: {falsifier_id}")


def run_v019_source_coordinate_derivation_experiment(
) -> SourceCoordinateBoundaryReport:
    upstream = run_v018_explicit_geometric_assignment_experiment()
    trace = derive_source_coordinate_trace(upstream.upstream.demonstration_trace)
    return SourceCoordinateBoundaryReport(
        upstream,
        trace,
        _build_results(trace),
    )


__all__ = [
    "ARBITRARY_SOURCE_ASSIGNMENT_STATUS",
    "SOURCE_COORDINATE_HIGHER_GEOMETRY_STATUS",
    "SOURCE_COORDINATE_ASSIGNMENT_STATUS",
    "SOURCE_COORDINATE_CODE_REFERENCE",
    "SOURCE_COORDINATE_FALSIFIER_IDS",
    "SOURCE_COORDINATE_LAW_FORMULA",
    "SOURCE_COORDINATE_LAW_ID",
    "SOURCE_COORDINATE_LAW_STATUS",
    "SOURCE_COORDINATE_LAW_VERSION",
    "SOURCE_COORDINATE_OUTCOME_RELATION_STATUS",
    "SOURCE_COORDINATE_SCOPE",
    "V019_HMMM",
    "V019_SELECTION_EFFECT",
    "V019_SOURCE_COORDINATE_SCHEMA_ID",
    "V019_SOURCE_COORDINATE_SCHEMA_VERSION",
    "AppliedSourceCoordinateAssignment",
    "OrderedSourceCoordinate",
    "SourceCoordinateBoundaryReport",
    "SourceCoordinateDerivation",
    "SourceCoordinateDisposition",
    "SourceCoordinateError",
    "SourceCoordinateEvidenceStanding",
    "SourceCoordinateFalsifierResult",
    "SourceCoordinateOutcome",
    "SourceCoordinateTrace",
    "apply_source_coordinate_assignment",
    "derive_ordered_source_coordinate",
    "derive_source_coordinate",
    "derive_source_coordinate_trace",
    "run_v019_source_coordinate_derivation_experiment",
]
