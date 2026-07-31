# === MODULE_BUILD ===
# id: edcm_explicit_geometric_assignment_boundary
#   module_name: explicit_geometric_assignment
#   module_kind: experiment
#   summary: applies the surviving exact signed-local circle-coordinate candidate to explicitly initiated word occurrences while keeping coordinate input separate from evidence identity and the source-to-coordinate law unresolved
#   owner: Erin Spencer
#   public_surface: ExplicitCoordinateProposal, AppliedGeometricAssignment, GeometricAssignmentOutcome, GeometricAssignmentTrace, ExplicitGeometricAssignmentBoundaryReport, GeometricAssignmentDisposition, RejectedGeometricAssignmentMechanism, GeometricAssignmentEvidenceStanding, GeometricAssignmentFalsifierResult, propose_explicit_coordinate, apply_explicit_geometric_assignment, record_geometric_assignment_outcome, run_v018_explicit_geometric_assignment_experiment
#   internal_surface: fixed GA01-GA09 evidence construction and exact validation helpers
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: v0.17 initiation and v0.16 adapter evidence remain exact; independently supplied exact coordinate input never becomes evidence identity and evidence identity never derives geometry
#   admin_only: false
#   tests: tests/test_explicit_geometric_assignment.py
#   rollout: nonselecting v0.18 exact-coordinate candidate application over explicitly initiated word occurrences; no universal source-to-coordinate derivation, total Structural Null topology, higher geometry, completion, EDCM activation, or METAPAT activation
#   rollback: remove this module, exports, tests, and v0.18 document while retaining v0.17 initiation evidence and v0.11 exact-coordinate candidate evidence
#   requires: edcm_gonol_initiation_structural_null_boundary, edcm_exact_coordinate_representation_boundary
#   since: 2026-07-31
#   unresolved: source-to-coordinate derivation law, total Structural Null topology, intrinsic seam derivation, epicycle-disk-sphere transitions, higher-gonol composition, scoped completion, canonical faithful breadth, and carrier selection
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: explicit_geometry_requires_initiated_word_and_independent_exact_input
#   given: one admitted word occurrence is proposed for v0.18 geometric assignment
#   then: the proposal retains the exact v0.17 initiation receipt and independent Fraction-valued coordinate input while evidence identity, digest, and carrier position derive no geometric field
#   class: safety
#   since: 2026-07-31
#
# id: explicit_geometry_applies_exact_signed_local_candidate_reversibly
#   given: a valid explicit coordinate proposal is applied
#   then: the exact v0.11 signed-local candidate maps u to B(u)=1+u/2, recovers u exactly, retains normalized lifted turns, and records one candidate GeometricAssignment with fixed initiation, proposal, implementation, and inverse evidence
#   class: correctness
#   since: 2026-07-31
#
# id: explicit_geometry_preserves_mobius_frame_and_local_side
#   given: an exact lifted-turn and local-transverse proposal enters the candidate relation
#   then: frame parity follows the two-turn native root law, local side follows the sign of u, exact identity survives, and binary64 remains a declared-loss rendering only
#   class: evidence
#   since: 2026-07-31
#
# id: explicit_geometry_outcomes_are_total_exclusive_and_ordered
#   given: v0.17 initiation outcomes enter one v0.18 trace
#   then: every occurrence in one retained exact upstream trace keeps order and receives exactly one assigned, unresolved, or rejected outcome without prefixes, deduplication, or malformed combinations
#   class: evidence
#   since: 2026-07-31
#
# id: explicit_geometry_rejects_identity_projection_and_upstream_substitution
#   given: digest, runtime hash, repr, object identity, A0 Blake2 lanes, binary64 rendering identity, carrier position alone, scalar projection, or an invalid upstream prestate is proposed as geometry
#   then: the mechanism remains named negative evidence and cannot create an AppliedGeometricAssignment
#   class: doctrine
#   since: 2026-07-31
#
# id: explicit_geometry_does_not_claim_total_law_complete_select_or_activate
#   given: the v0.18 report joins explicit candidate application to v0.17 initiation evidence
#   then: the source-to-coordinate derivation law, total Structural Null topology, higher geometry, composition, completion, carrier selection, EDCM activation, and METAPAT activation remain absent
#   class: safety
#   since: 2026-07-31
# === END CONTRACTS ===

"""Explicit exact-coordinate geometric-assignment evidence for UCNS v0.18.

This module advances the v0.17 causal doorway without inventing the missing
universal law.  Any explicitly initiated word occurrence may receive the
surviving v0.11 signed-local circle-coordinate candidate when a caller supplies
an independent exact rational coordinate proposal.  The proposal is evidence
input, not a coordinate derived from source content, its digest, carrier
position, a scalar metric, or the historical A0 Blake2 phase lanes.

The resulting receipt retains the initiation, exact coordinate and inverse,
native two-turn frame parity, local side, one candidate ``GeometricAssignment``,
and a linked lossy binary64 rendering.  It does not establish how arbitrary
source evidence should generate coordinate input, a total Structural Null
topology, higher geometry, higher-gonol composition, or completion.
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
    binary64_collision_witnesses,
    recover_signed_local_transverse,
    render_exact_coordinate_binary64,
    signed_local_exact_coordinate,
)
from .gonol_initiation import (
    TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS,
    GonolInitiationBoundaryReport,
    GonolInitiationDisposition,
    GonolInitiationOutcome,
    GonolInitiationReceipt,
    GonolInitiationTrace,
    run_v017_gonol_initiation_boundary_experiment,
)


V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_ID = (
    "ucns.edcm.explicit-geometric-assignment-boundary"
)
V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_VERSION = "0.18.0"
V018_SELECTION_EFFECT = "none"

EXPLICIT_GEOMETRIC_ASSIGNMENT_SCOPE = (
    "explicit-exact-coordinate-candidate-over-v017-initiated-word-occurrences"
)
EXPLICIT_COORDINATE_INPUT_ROLE = (
    "independent-experiment-input-not-derived-from-evidence-identity"
)
EXPLICIT_ASSIGNMENT_LAW_ID = (
    "ucns.edcm.explicit-signed-local-circle-assignment"
)
EXPLICIT_ASSIGNMENT_LAW_VERSION = "0.18.0"
EXPLICIT_ASSIGNMENT_CODE_REFERENCE = (
    "src/ucns/explicit_geometric_assignment.py:apply_explicit_geometric_assignment"
)
EXPLICIT_ASSIGNMENT_STATUS = (
    "implemented-exact-input-candidate-application"
)
SOURCE_TO_COORDINATE_LAW_STATUS = "unresolved-no-source-to-coordinate-law"
ARBITRARY_ELEMENT_ASSIGNMENT_STATUS = (
    "partial-explicit-input-only-not-total-derived-assignment"
)
HIGHER_GEOMETRY_STATUS = "unresolved-circle-entry-only"
GEOMETRIC_ASSIGNMENT_OUTCOME_RELATION_STATUS = (
    "total-tagged-over-v017-initiation-outcomes"
)

GEOMETRIC_ASSIGNMENT_FALSIFIER_IDS = tuple(
    f"GA{index:02d}" for index in range(1, 10)
)

V018_HMMM = (
    "the law deriving exact transverse and lifted-turn coordinates from arbitrary source evidence remains unresolved",
    "explicit coordinate proposals make candidate application executable but do not prove that their values are the lawful source assignment",
    "the total topology from singular Structural Null to arbitrary non-null carrier states remains unresolved",
    "circle-to-epicycle, epicycle-to-disk, disk-to-sphere, and recursive scale transitions remain unresolved",
    "higher-gonol composition, scoped completion, canonical B, proof-assistant formalization, carrier selection, and consumer activation remain unresolved",
)


class ExplicitGeometricAssignmentError(ValueError):
    """Raised when v0.18 evidence crosses its declared assignment boundary."""


class GeometricAssignmentDisposition(str, Enum):
    """Exhaustive v0.18 outcomes for one v0.17 initiation outcome."""

    ASSIGNED = "explicit-exact-coordinate-candidate-applied"
    UNRESOLVED = "unresolved-no-coordinate-proposal"
    REJECTED = "rejected-geometric-assignment-mechanism"


class RejectedGeometricAssignmentMechanism(str, Enum):
    """Mechanisms that cannot create v0.18 geometric assignment evidence."""

    CONTENT_DIGEST = "content-or-subject-digest-as-geometry"
    RUNTIME_HASH = "runtime-hash-as-geometry"
    REPR = "repr-as-geometry"
    OBJECT_ID = "object-id-as-geometry"
    A0_BLAKE2_PHASE_LANES = "a0-blake2-phase-lanes-as-assignment-law"
    BINARY64_RENDERING_IDENTITY = "binary64-rendering-as-exact-identity"
    CARRIER_POSITION_ONLY = "public-gonol-position-as-complete-geometry"
    SCALAR_PROJECTION = "metric-scalar-projection-as-trajectory"
    UPSTREAM_ORIGIN_SUBSTITUTION = "invalid-origin-role-as-structural-null-prestate"


class GeometricAssignmentEvidenceStanding(str, Enum):
    """Standing vocabulary for the fixed GA01-GA09 packet."""

    EXACT_IMPLEMENTED_SUPPORTED = "exact-implemented-supported"
    BOUNDED_UPSTREAM_SUPPORTED = "bounded-upstream-supported"
    NEGATIVE_SUPPORTED = "negative-supported"
    UNRESOLVED = "unresolved"


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ExplicitGeometricAssignmentError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise ExplicitGeometricAssignmentError(f"{field} must retain evidence")
    for value in values:
        _require_text(value, field)


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _expected_frame(lifted_turns: Fraction) -> NativeMobiusFrame:
    coordinate = signed_local_exact_coordinate(Fraction(0), lifted_turns)
    if coordinate.lifted_turns < Fraction(1):
        return NativeMobiusFrame.POSITIVE
    return NativeMobiusFrame.REVERSED


def _local_side(local_transverse: Fraction) -> str:
    if local_transverse < 0:
        return "local-negative"
    if local_transverse > 0:
        return "local-positive"
    return "local-root"


@dataclass(frozen=True, slots=True)
class ExplicitCoordinateProposal:
    """Independent exact coordinate input linked to one initiated word."""

    proposal_id: str
    initiation: GonolInitiationReceipt
    local_transverse: Fraction
    lifted_turns: Fraction
    frame: NativeMobiusFrame
    evidence: tuple[str, ...]
    input_role: str = EXPLICIT_COORDINATE_INPUT_ROLE
    derived_from_evidence_identity: bool = False
    scope: str = EXPLICIT_GEOMETRIC_ASSIGNMENT_SCOPE
    selection_effect: str = V018_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.proposal_id, "proposal_id")
        if not isinstance(self.initiation, GonolInitiationReceipt):
            raise ExplicitGeometricAssignmentError(
                "coordinate proposal requires an initiated word receipt"
            )
        if self.proposal_id != f"{self.initiation.receipt_id}:coordinate-proposal":
            raise ExplicitGeometricAssignmentError(
                "coordinate proposal identity must derive from initiation identity"
            )
        if not isinstance(self.local_transverse, Fraction):
            raise ExplicitGeometricAssignmentError(
                "local_transverse must be an exact Fraction"
            )
        if not isinstance(self.lifted_turns, Fraction):
            raise ExplicitGeometricAssignmentError(
                "lifted_turns must be an exact Fraction"
            )
        coordinate = signed_local_exact_coordinate(
            self.local_transverse,
            self.lifted_turns,
        )
        if self.lifted_turns != coordinate.lifted_turns:
            raise ExplicitGeometricAssignmentError(
                "coordinate proposal lifted_turns must be normalized to [0, 2)"
            )
        if not isinstance(self.frame, NativeMobiusFrame):
            raise ExplicitGeometricAssignmentError(
                "coordinate proposal requires a native Mobius frame"
            )
        if self.frame is not _expected_frame(coordinate.lifted_turns):
            raise ExplicitGeometricAssignmentError(
                "native frame must follow exact two-turn lifted parity"
            )
        _require_text_items(self.evidence, "coordinate proposal evidence")
        if self.input_role != EXPLICIT_COORDINATE_INPUT_ROLE:
            raise ExplicitGeometricAssignmentError(
                "coordinate input must remain independent experiment evidence"
            )
        if self.derived_from_evidence_identity:
            raise ExplicitGeometricAssignmentError(
                "evidence identity cannot derive geometric coordinate input"
            )
        if self.scope != EXPLICIT_GEOMETRIC_ASSIGNMENT_SCOPE:
            raise ExplicitGeometricAssignmentError(
                "explicit geometric-assignment scope is fixed"
            )
        if self.selection_effect != V018_SELECTION_EFFECT:
            raise ExplicitGeometricAssignmentError(
                "coordinate proposal cannot select geometry"
            )

    @property
    def local_side(self) -> str:
        return _local_side(self.local_transverse)

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        return (
            self.proposal_id,
            self.initiation.evidence_identity,
            _fraction_key(self.local_transverse),
            _fraction_key(self.lifted_turns),
            self.frame.value,
            self.local_side,
            self.evidence,
            self.input_role,
        )


def propose_explicit_coordinate(
    initiation: GonolInitiationReceipt,
    *,
    local_transverse: Fraction,
    lifted_turns: Fraction,
    evidence: tuple[str, ...],
) -> ExplicitCoordinateProposal:
    """Create independent exact candidate input for one initiated word."""

    if not isinstance(initiation, GonolInitiationReceipt):
        raise TypeError("initiation must be GonolInitiationReceipt")
    normalized = signed_local_exact_coordinate(
        local_transverse,
        lifted_turns,
    ).lifted_turns
    return ExplicitCoordinateProposal(
        proposal_id=f"{initiation.receipt_id}:coordinate-proposal",
        initiation=initiation,
        local_transverse=local_transverse,
        lifted_turns=normalized,
        frame=_expected_frame(normalized),
        evidence=evidence,
    )


def _assignment_parameters(
    proposal: ExplicitCoordinateProposal,
    coordinate: ExactCarrierCoordinate,
) -> tuple[tuple[str, str], ...]:
    return (
        ("candidate-id", EXACT_COORDINATE_CANDIDATE_ID),
        ("local-transverse", _fraction_key(coordinate.local_transverse)),
        ("breadth", _fraction_key(coordinate.breadth)),
        ("lifted-turns", _fraction_key(coordinate.lifted_turns)),
        ("coordinate-input-role", proposal.input_role),
    )


def _assignment_evidence(
    proposal: ExplicitCoordinateProposal,
) -> tuple[str, ...]:
    return (
        f"initiation-receipt:{proposal.initiation.receipt_id}",
        f"coordinate-proposal:{proposal.proposal_id}",
        f"code-reference:{EXPLICIT_ASSIGNMENT_CODE_REFERENCE}",
        "exact-coordinate-and-inverse-validated",
    )


@dataclass(frozen=True, slots=True)
class AppliedGeometricAssignment:
    """One exact candidate relation applied to an explicitly initiated word."""

    receipt_id: str
    proposal: ExplicitCoordinateProposal
    exact_coordinate: ExactCarrierCoordinate
    rendering: Binary64CarrierRendering
    assignment: GeometricAssignment
    exact_coordinate_role: str = "authoritative-candidate-evidence-identity"
    rendering_role: str = BINARY64_RENDERING_STATUS
    source_to_coordinate_law_status: str = SOURCE_TO_COORDINATE_LAW_STATUS
    completion_registered: bool = False
    parent_gonol_ids: tuple[str, ...] = ()
    scope: str = EXPLICIT_GEOMETRIC_ASSIGNMENT_SCOPE
    selection_effect: str = V018_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.receipt_id, "assignment receipt_id")
        if not isinstance(self.proposal, ExplicitCoordinateProposal):
            raise ExplicitGeometricAssignmentError(
                "applied assignment requires explicit coordinate proposal"
            )
        if self.receipt_id != f"{self.proposal.proposal_id}:assignment":
            raise ExplicitGeometricAssignmentError(
                "assignment receipt identity must derive from proposal identity"
            )
        expected_coordinate = signed_local_exact_coordinate(
            self.proposal.local_transverse,
            self.proposal.lifted_turns,
        )
        if self.exact_coordinate != expected_coordinate:
            raise ExplicitGeometricAssignmentError(
                "assignment must retain the exact signed-local coordinate"
            )
        if recover_signed_local_transverse(self.exact_coordinate) != (
            self.proposal.local_transverse
        ):
            raise ExplicitGeometricAssignmentError(
                "assignment must recover exact local transverse input"
            )
        expected_rendering = render_exact_coordinate_binary64(
            self.exact_coordinate
        )
        if (
            self.rendering.exact_coordinate != expected_rendering.exact_coordinate
            or self.rendering.rendering_identity
            != expected_rendering.rendering_identity
            or self.rendering.rendering_policy_id
            != expected_rendering.rendering_policy_id
            or self.rendering.rendering_policy_version
            != expected_rendering.rendering_policy_version
            or self.rendering.code_reference != expected_rendering.code_reference
            or self.rendering.information_loss
            != expected_rendering.information_loss
            or self.rendering.status != expected_rendering.status
            or self.rendering.selection_effect
            != expected_rendering.selection_effect
        ):
            raise ExplicitGeometricAssignmentError(
                "binary64 rendering must remain linked to exact coordinate source"
            )
        if self.rendering_role != BINARY64_RENDERING_STATUS:
            raise ExplicitGeometricAssignmentError(
                "binary64 point must remain a declared-loss rendering"
            )
        if not isinstance(self.assignment, GeometricAssignment):
            raise ExplicitGeometricAssignmentError(
                "applied assignment requires GeometricAssignment evidence"
            )
        initiation = self.proposal.initiation
        expected_relation_id = f"{initiation.gonol_id}:circle-candidate-relation"
        if (
            self.assignment.relation_id != expected_relation_id
            or self.assignment.geometry is not GeometryKind.CIRCLE
            or self.assignment.assignment_law_id != EXPLICIT_ASSIGNMENT_LAW_ID
            or self.assignment.assignment_law_version
            != EXPLICIT_ASSIGNMENT_LAW_VERSION
            or self.assignment.law_standing is not LawStanding.CANDIDATE
            or self.assignment.orientation != self.proposal.frame.value
            or self.assignment.sidedness != self.proposal.local_side
            or self.assignment.parameters
            != _assignment_parameters(self.proposal, self.exact_coordinate)
            or self.assignment.evidence != _assignment_evidence(self.proposal)
        ):
            raise ExplicitGeometricAssignmentError(
                "candidate GeometricAssignment identity and fields are fixed"
            )
        if self.exact_coordinate_role != (
            "authoritative-candidate-evidence-identity"
        ):
            raise ExplicitGeometricAssignmentError(
                "exact coordinate must remain the candidate evidence identity"
            )
        if self.source_to_coordinate_law_status != SOURCE_TO_COORDINATE_LAW_STATUS:
            raise ExplicitGeometricAssignmentError(
                "source-to-coordinate law must remain unresolved"
            )
        if self.completion_registered:
            raise ExplicitGeometricAssignmentError(
                "candidate assignment cannot register construction completion"
            )
        if self.parent_gonol_ids:
            raise ExplicitGeometricAssignmentError(
                "higher-gonol composition remains unresolved in v0.18"
            )
        if self.scope != EXPLICIT_GEOMETRIC_ASSIGNMENT_SCOPE:
            raise ExplicitGeometricAssignmentError(
                "applied assignment scope is fixed"
            )
        if self.selection_effect != V018_SELECTION_EFFECT:
            raise ExplicitGeometricAssignmentError(
                "applied assignment cannot select geometry"
            )

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        return (
            self.receipt_id,
            self.proposal.evidence_identity,
            self.exact_coordinate.exact_identity,
            self.assignment.relation_id,
            self.assignment.assignment_law_id,
            self.assignment.assignment_law_version,
            self.assignment.orientation,
            self.assignment.sidedness,
            self.assignment.evidence,
            EXPLICIT_ASSIGNMENT_CODE_REFERENCE,
            self.exact_coordinate_role,
            self.rendering_role,
        )


def apply_explicit_geometric_assignment(
    proposal: ExplicitCoordinateProposal,
) -> AppliedGeometricAssignment:
    """Apply the fixed exact signed-local circle candidate to one proposal."""

    if not isinstance(proposal, ExplicitCoordinateProposal):
        raise TypeError("proposal must be ExplicitCoordinateProposal")
    coordinate = signed_local_exact_coordinate(
        proposal.local_transverse,
        proposal.lifted_turns,
    )
    assignment = GeometricAssignment(
        relation_id=(
            f"{proposal.initiation.gonol_id}:circle-candidate-relation"
        ),
        geometry=GeometryKind.CIRCLE,
        assignment_law_id=EXPLICIT_ASSIGNMENT_LAW_ID,
        assignment_law_version=EXPLICIT_ASSIGNMENT_LAW_VERSION,
        law_standing=LawStanding.CANDIDATE,
        orientation=proposal.frame.value,
        sidedness=proposal.local_side,
        parameters=_assignment_parameters(proposal, coordinate),
        evidence=_assignment_evidence(proposal),
    )
    return AppliedGeometricAssignment(
        receipt_id=f"{proposal.proposal_id}:assignment",
        proposal=proposal,
        exact_coordinate=coordinate,
        rendering=render_exact_coordinate_binary64(coordinate),
        assignment=assignment,
    )


@dataclass(frozen=True, slots=True)
class GeometricAssignmentOutcome:
    """Exactly one v0.18 outcome linked to one v0.17 initiation outcome."""

    outcome_id: str
    upstream: GonolInitiationOutcome
    disposition: GeometricAssignmentDisposition
    evidence: tuple[str, ...]
    applied_assignment: AppliedGeometricAssignment | None = None
    rejected_mechanism: RejectedGeometricAssignmentMechanism | None = None
    selection_effect: str = V018_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.outcome_id, "geometric assignment outcome_id")
        if not isinstance(self.upstream, GonolInitiationOutcome):
            raise ExplicitGeometricAssignmentError(
                "geometric assignment outcome requires v0.17 initiation evidence"
            )
        expected_id = (
            f"{self.upstream.admission.admission_id}:geometric-assignment-outcome"
        )
        if self.outcome_id != expected_id:
            raise ExplicitGeometricAssignmentError(
                "geometric outcome identity must derive from admission identity"
            )
        if not isinstance(self.disposition, GeometricAssignmentDisposition):
            raise ExplicitGeometricAssignmentError(
                "geometric assignment disposition is invalid"
            )
        _require_text_items(self.evidence, "geometric assignment outcome evidence")
        if self.selection_effect != V018_SELECTION_EFFECT:
            raise ExplicitGeometricAssignmentError(
                "geometric assignment outcome cannot select geometry"
            )

        if self.disposition is GeometricAssignmentDisposition.ASSIGNED:
            if not isinstance(self.applied_assignment, AppliedGeometricAssignment):
                raise ExplicitGeometricAssignmentError(
                    "assigned outcome requires AppliedGeometricAssignment"
                )
            if self.upstream.disposition is not GonolInitiationDisposition.INITIATED:
                raise ExplicitGeometricAssignmentError(
                    "geometric assignment requires an initiated upstream word"
                )
            if self.upstream.initiation != (
                self.applied_assignment.proposal.initiation
            ):
                raise ExplicitGeometricAssignmentError(
                    "applied assignment must retain the upstream initiation receipt"
                )
            if self.rejected_mechanism is not None:
                raise ExplicitGeometricAssignmentError(
                    "assigned outcome cannot also reject a mechanism"
                )
        elif self.disposition is GeometricAssignmentDisposition.UNRESOLVED:
            if (
                self.applied_assignment is not None
                or self.rejected_mechanism is not None
            ):
                raise ExplicitGeometricAssignmentError(
                    "unresolved outcome cannot contain assignment or rejection"
                )
        else:
            if self.applied_assignment is not None:
                raise ExplicitGeometricAssignmentError(
                    "rejected mechanism cannot create applied assignment"
                )
            if not isinstance(
                self.rejected_mechanism,
                RejectedGeometricAssignmentMechanism,
            ):
                raise ExplicitGeometricAssignmentError(
                    "rejected outcome requires a named mechanism"
                )


def record_geometric_assignment_outcome(
    upstream: GonolInitiationOutcome,
    *,
    evidence: tuple[str, ...],
    applied_assignment: AppliedGeometricAssignment | None = None,
    rejected_mechanism: RejectedGeometricAssignmentMechanism | None = None,
) -> GeometricAssignmentOutcome:
    """Record one exclusive assignment outcome without a hidden default law."""

    if not isinstance(upstream, GonolInitiationOutcome):
        raise TypeError("upstream must be GonolInitiationOutcome")
    if applied_assignment is not None and rejected_mechanism is not None:
        raise ExplicitGeometricAssignmentError(
            "geometric assignment outcome cannot be assigned and rejected"
        )
    if applied_assignment is not None:
        disposition = GeometricAssignmentDisposition.ASSIGNED
    elif rejected_mechanism is not None:
        disposition = GeometricAssignmentDisposition.REJECTED
    else:
        disposition = GeometricAssignmentDisposition.UNRESOLVED
    return GeometricAssignmentOutcome(
        outcome_id=(
            f"{upstream.admission.admission_id}:geometric-assignment-outcome"
        ),
        upstream=upstream,
        disposition=disposition,
        evidence=evidence,
        applied_assignment=applied_assignment,
        rejected_mechanism=rejected_mechanism,
    )


@dataclass(frozen=True, slots=True)
class GeometricAssignmentTrace:
    """Ordered total tagged assignment evidence over v0.17 outcomes."""

    trace_id: str
    upstream_trace: GonolInitiationTrace
    outcomes: tuple[GeometricAssignmentOutcome, ...]
    scope: str = EXPLICIT_GEOMETRIC_ASSIGNMENT_SCOPE
    outcome_relation_status: str = GEOMETRIC_ASSIGNMENT_OUTCOME_RELATION_STATUS
    selection_effect: str = V018_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.trace_id, "geometric assignment trace_id")
        if not isinstance(self.upstream_trace, GonolInitiationTrace):
            raise ExplicitGeometricAssignmentError(
                "geometric assignment trace requires its exact upstream trace"
            )
        if not self.outcomes:
            raise ExplicitGeometricAssignmentError(
                "geometric assignment trace must retain at least one outcome"
            )
        if self.scope != EXPLICIT_GEOMETRIC_ASSIGNMENT_SCOPE:
            raise ExplicitGeometricAssignmentError(
                "geometric assignment trace scope is fixed"
            )
        if self.outcome_relation_status != (
            GEOMETRIC_ASSIGNMENT_OUTCOME_RELATION_STATUS
        ):
            raise ExplicitGeometricAssignmentError(
                "geometric assignment outcome relation status is fixed"
            )
        if self.selection_effect != V018_SELECTION_EFFECT:
            raise ExplicitGeometricAssignmentError(
                "geometric assignment trace cannot select geometry"
            )
        if len(self.outcomes) != len(self.upstream_trace.outcomes) or any(
            outcome.upstream is not upstream
            for outcome, upstream in zip(
                self.outcomes,
                self.upstream_trace.outcomes,
                strict=True,
            )
        ):
            raise ExplicitGeometricAssignmentError(
                "v0.18 outcomes must retain the complete exact upstream trace"
            )

        upstream_ids: set[str] = set()
        outcome_ids: set[str] = set()
        assignment_ids: set[str] = set()
        for expected_index, outcome in enumerate(self.outcomes):
            if not isinstance(outcome, GeometricAssignmentOutcome):
                raise ExplicitGeometricAssignmentError(
                    "trace outcomes must be GeometricAssignmentOutcome values"
                )
            if outcome.upstream.admission.occurrence_index != expected_index:
                raise ExplicitGeometricAssignmentError(
                    "v0.18 outcomes must retain contiguous upstream order"
                )
            if outcome.upstream.outcome_id in upstream_ids:
                raise ExplicitGeometricAssignmentError(
                    "upstream initiation outcome identities must remain unique"
                )
            if outcome.outcome_id in outcome_ids:
                raise ExplicitGeometricAssignmentError(
                    "geometric assignment outcome identities must be unique"
                )
            if outcome.applied_assignment is not None:
                assignment_id = outcome.applied_assignment.receipt_id
                if assignment_id in assignment_ids:
                    raise ExplicitGeometricAssignmentError(
                        "applied assignment receipt identities must be unique"
                    )
                assignment_ids.add(assignment_id)
            upstream_ids.add(outcome.upstream.outcome_id)
            outcome_ids.add(outcome.outcome_id)

    @property
    def has_total_outcome_evidence(self) -> bool:
        return len(self.outcomes) == len(self.upstream_trace.outcomes)

    @property
    def assigned_receipts(self) -> tuple[AppliedGeometricAssignment, ...]:
        return tuple(
            outcome.applied_assignment
            for outcome in self.outcomes
            if outcome.applied_assignment is not None
        )

    @property
    def subject_digests(self) -> tuple[str, ...]:
        return tuple(
            outcome.upstream.admission.subject_record.digest
            for outcome in self.outcomes
        )


@dataclass(frozen=True, slots=True)
class GeometricAssignmentFalsifierResult:
    """One fixed GA01-GA09 assignment-evidence standing."""

    falsifier_id: str
    standing: GeometricAssignmentEvidenceStanding
    evidence: tuple[str, ...]
    limitation: str

    def __post_init__(self) -> None:
        if self.falsifier_id not in GEOMETRIC_ASSIGNMENT_FALSIFIER_IDS:
            raise ExplicitGeometricAssignmentError(
                "unknown geometric-assignment falsifier id"
            )
        if not isinstance(self.standing, GeometricAssignmentEvidenceStanding):
            raise ExplicitGeometricAssignmentError(
                "geometric-assignment falsifier standing is invalid"
            )
        _require_text_items(self.evidence, "geometric-assignment falsifier evidence")
        _require_text(self.limitation, "geometric-assignment falsifier limitation")


def _build_results(
    trace: GeometricAssignmentTrace,
) -> tuple[GeometricAssignmentFalsifierResult, ...]:
    assigned = trace.assigned_receipts
    collisions = binary64_collision_witnesses()
    return (
        GeometricAssignmentFalsifierResult(
            "GA01",
            GeometricAssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"applied-assignments:{len(assigned)}",
                "required-upstream:v017-explicit-initiated-word",
                "link:initiation-receipt+source-admission+twist",
            ),
            "support applies only to explicitly initiated word occurrences",
        ),
        GeometricAssignmentFalsifierResult(
            "GA02",
            GeometricAssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"coordinate-input-role:{EXPLICIT_COORDINATE_INPUT_ROLE}",
                "coordinate-fields:exact-Fraction-u+lifted-turns",
                "evidence-identity-to-coordinate:false",
            ),
            "the boundary validates the declared separation but cannot audit how an external caller chose the proposal values",
        ),
        GeometricAssignmentFalsifierResult(
            "GA03",
            GeometricAssignmentEvidenceStanding.BOUNDED_UPSTREAM_SUPPORTED,
            (
                f"candidate:{EXACT_COORDINATE_CANDIDATE_ID}",
                "law:B(u)=1+u/2",
                "inverse:u=2*(B-1)",
                "lifted-turn-domain:[0,2)",
            ),
            "the exact coordinate law is a surviving candidate and is not a selected faithful-breadth law",
        ),
        GeometricAssignmentFalsifierResult(
            "GA04",
            GeometricAssignmentEvidenceStanding.BOUNDED_UPSTREAM_SUPPORTED,
            (
                "frame:[0,1)=positive;[1,2)=reversed",
                "side:sign-of-exact-local-transverse",
                "two-visible-turns:local-frame-return",
            ),
            "frame and side behavior is bounded to the native root and signed-local candidate semantics",
        ),
        GeometricAssignmentFalsifierResult(
            "GA05",
            GeometricAssignmentEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"outcome-relation:{GEOMETRIC_ASSIGNMENT_OUTCOME_RELATION_STATUS}",
                "exclusive-tags:assigned|unresolved|rejected",
                "ordered-occurrence-identity:retained",
            ),
            "totality is over v0.17 evidence outcomes, not successful assignments for every possible source element",
        ),
        GeometricAssignmentFalsifierResult(
            "GA06",
            GeometricAssignmentEvidenceStanding.NEGATIVE_SUPPORTED,
            (
                "identity:exact-rational-coordinate",
                f"rendering:{BINARY64_RENDERING_STATUS}",
                f"binary64-collision-witnesses:{len(collisions)}",
            ),
            "binary64 points remain useful renderings but cannot identify arbitrary exact rational assignments",
        ),
        GeometricAssignmentFalsifierResult(
            "GA07",
            GeometricAssignmentEvidenceStanding.NEGATIVE_SUPPORTED,
            tuple(
                f"rejected:{mechanism.value}"
                for mechanism in RejectedGeometricAssignmentMechanism
            ),
            "rejected mechanisms may remain evidence in their own domains but cannot manufacture assignment geometry",
        ),
        GeometricAssignmentFalsifierResult(
            "GA08",
            GeometricAssignmentEvidenceStanding.UNRESOLVED,
            (
                f"source-to-coordinate-law:{SOURCE_TO_COORDINATE_LAW_STATUS}",
                f"arbitrary-element-assignment:{ARBITRARY_ELEMENT_ASSIGNMENT_STATUS}",
            ),
            "no evidence-supported rule yet derives proposal coordinates from arbitrary admitted source elements",
        ),
        GeometricAssignmentFalsifierResult(
            "GA09",
            GeometricAssignmentEvidenceStanding.UNRESOLVED,
            (
                f"total-structural-null-topology:{TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS}",
                f"higher-geometry:{HIGHER_GEOMETRY_STATUS}",
                "completion:not-registered",
                "carrier-selection:none",
                "EDCM-activation:inactive",
                "METAPAT-activation:inactive",
            ),
            "circle entry evidence does not supply total topology, recursive geometry, composition, completion, or activation",
        ),
    )


@dataclass(frozen=True, slots=True)
class ExplicitGeometricAssignmentBoundaryReport:
    """v0.18 candidate application joined to unchanged v0.17 standing."""

    upstream: GonolInitiationBoundaryReport
    demonstration_trace: GeometricAssignmentTrace
    results: tuple[GeometricAssignmentFalsifierResult, ...]
    schema_id: str = V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_ID
    schema_version: str = V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_VERSION
    explicit_candidate_application_status: str = EXPLICIT_ASSIGNMENT_STATUS
    source_to_coordinate_law_status: str = SOURCE_TO_COORDINATE_LAW_STATUS
    arbitrary_element_assignment_status: str = ARBITRARY_ELEMENT_ASSIGNMENT_STATUS
    total_structural_null_topology_status: str = (
        TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS
    )
    higher_geometry_status: str = HIGHER_GEOMETRY_STATUS
    selection_effect: str = V018_SELECTION_EFFECT
    edcm_activation: str = "inactive"
    metapat_activation: str = "inactive"
    hmmm: tuple[str, ...] = V018_HMMM

    def __post_init__(self) -> None:
        if not isinstance(self.upstream, GonolInitiationBoundaryReport):
            raise ExplicitGeometricAssignmentError(
                "v0.18 report requires the exact v0.17 upstream report"
            )
        if not isinstance(self.demonstration_trace, GeometricAssignmentTrace):
            raise ExplicitGeometricAssignmentError(
                "v0.18 report requires a geometric assignment trace"
            )
        if self.demonstration_trace.upstream_trace is not (
            self.upstream.demonstration_trace
        ):
            raise ExplicitGeometricAssignmentError(
                "v0.18 trace must retain the report's exact upstream trace"
            )
        if not self.demonstration_trace.assigned_receipts:
            raise ExplicitGeometricAssignmentError(
                "v0.18 demonstration must retain at least one applied assignment"
            )
        upstream_outcomes = self.upstream.demonstration_trace.outcomes
        if tuple(
            outcome.upstream for outcome in self.demonstration_trace.outcomes
        ) != upstream_outcomes:
            raise ExplicitGeometricAssignmentError(
                "v0.18 trace must retain the exact v0.17 initiation outcomes"
            )
        if self.results != _build_results(self.demonstration_trace):
            raise ExplicitGeometricAssignmentError(
                "v0.18 GA01-GA09 falsifier packet is fixed"
            )
        if tuple(result.falsifier_id for result in self.results) != (
            GEOMETRIC_ASSIGNMENT_FALSIFIER_IDS
        ):
            raise ExplicitGeometricAssignmentError(
                "v0.18 must retain GA01 through GA09 in order"
            )
        if (
            self.schema_id != V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_ID
            or self.schema_version
            != V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_VERSION
            or self.explicit_candidate_application_status
            != EXPLICIT_ASSIGNMENT_STATUS
            or self.source_to_coordinate_law_status
            != SOURCE_TO_COORDINATE_LAW_STATUS
            or self.arbitrary_element_assignment_status
            != ARBITRARY_ELEMENT_ASSIGNMENT_STATUS
            or self.total_structural_null_topology_status
            != TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS
            or self.higher_geometry_status != HIGHER_GEOMETRY_STATUS
        ):
            raise ExplicitGeometricAssignmentError(
                "v0.18 schema and assignment standings are fixed"
            )
        if self.selection_effect != V018_SELECTION_EFFECT:
            raise ExplicitGeometricAssignmentError(
                "v0.18 cannot select geometry"
            )
        if self.edcm_activation != "inactive":
            raise ExplicitGeometricAssignmentError(
                "v0.18 cannot activate EDCM"
            )
        if self.metapat_activation != "inactive":
            raise ExplicitGeometricAssignmentError(
                "v0.18 cannot activate METAPAT"
            )
        if self.hmmm != V018_HMMM:
            raise ExplicitGeometricAssignmentError(
                "v0.18 unresolved boundary is fixed"
            )

    def result(self, falsifier_id: str) -> GeometricAssignmentFalsifierResult:
        for result in self.results:
            if result.falsifier_id == falsifier_id:
                return result
        raise ExplicitGeometricAssignmentError(
            f"unknown geometric-assignment falsifier: {falsifier_id}"
        )


def _demonstration_trace(
    upstream: GonolInitiationBoundaryReport,
) -> GeometricAssignmentTrace:
    initiation_outcomes = upstream.demonstration_trace.outcomes
    initiation = initiation_outcomes[0].initiation
    if initiation is None:
        raise ExplicitGeometricAssignmentError(
            "v0.18 demonstration requires the v0.17 initiated word"
        )
    proposal = propose_explicit_coordinate(
        initiation,
        local_transverse=Fraction(1, 3),
        lifted_turns=Fraction(0),
        evidence=(
            "independent hand-authored exact coordinate proposal",
            "proposal value is not derived from source content or digest",
        ),
    )
    applied = apply_explicit_geometric_assignment(proposal)
    outcomes = (
        record_geometric_assignment_outcome(
            initiation_outcomes[0],
            applied_assignment=applied,
            evidence=(
                "explicit exact signed-local circle candidate applied",
            ),
        ),
        record_geometric_assignment_outcome(
            initiation_outcomes[1],
            evidence=(
                "no initiated gonol and no independent coordinate proposal",
            ),
        ),
        record_geometric_assignment_outcome(
            initiation_outcomes[2],
            rejected_mechanism=(
                RejectedGeometricAssignmentMechanism.UPSTREAM_ORIGIN_SUBSTITUTION
            ),
            evidence=(
                "invalid Structural Null prestate substitution remains blocking evidence",
            ),
        ),
    )
    return GeometricAssignmentTrace(
        trace_id="ucns-v018-explicit-geometric-assignment-demonstration",
        upstream_trace=upstream.demonstration_trace,
        outcomes=outcomes,
    )


def run_v018_explicit_geometric_assignment_experiment(
) -> ExplicitGeometricAssignmentBoundaryReport:
    """Construct the fixed v0.18 exact-input assignment evidence graph."""

    upstream = run_v017_gonol_initiation_boundary_experiment()
    trace = _demonstration_trace(upstream)
    return ExplicitGeometricAssignmentBoundaryReport(
        upstream=upstream,
        demonstration_trace=trace,
        results=_build_results(trace),
    )


__all__ = [
    "ARBITRARY_ELEMENT_ASSIGNMENT_STATUS",
    "EXPLICIT_ASSIGNMENT_CODE_REFERENCE",
    "EXPLICIT_ASSIGNMENT_LAW_ID",
    "EXPLICIT_ASSIGNMENT_LAW_VERSION",
    "EXPLICIT_ASSIGNMENT_STATUS",
    "EXPLICIT_COORDINATE_INPUT_ROLE",
    "EXPLICIT_GEOMETRIC_ASSIGNMENT_SCOPE",
    "GEOMETRIC_ASSIGNMENT_FALSIFIER_IDS",
    "GEOMETRIC_ASSIGNMENT_OUTCOME_RELATION_STATUS",
    "HIGHER_GEOMETRY_STATUS",
    "SOURCE_TO_COORDINATE_LAW_STATUS",
    "V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_ID",
    "V018_EXPLICIT_GEOMETRIC_ASSIGNMENT_SCHEMA_VERSION",
    "V018_HMMM",
    "V018_SELECTION_EFFECT",
    "AppliedGeometricAssignment",
    "ExplicitCoordinateProposal",
    "ExplicitGeometricAssignmentBoundaryReport",
    "ExplicitGeometricAssignmentError",
    "GeometricAssignmentDisposition",
    "GeometricAssignmentEvidenceStanding",
    "GeometricAssignmentFalsifierResult",
    "GeometricAssignmentOutcome",
    "GeometricAssignmentTrace",
    "RejectedGeometricAssignmentMechanism",
    "apply_explicit_geometric_assignment",
    "propose_explicit_coordinate",
    "record_geometric_assignment_outcome",
    "run_v018_explicit_geometric_assignment_experiment",
]
