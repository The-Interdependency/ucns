# === MODULE_BUILD ===
# id: edcm_gonol_initiation_structural_null_boundary
#   module_name: gonol_initiation
#   module_kind: experiment
#   summary: separates Structural Null from neighboring zero and absence roles, records one total tagged initiation outcome per admitted occurrence, and retains bounded 360-degree/720-degree root-return evidence
#   owner: Erin Spencer
#   public_surface: OriginRole, OriginTermRecord, GonolInitiationReceipt, GonolInitiationOutcome, GonolInitiationTrace, GonolInitiationScopeCompletionReceipt, RootLoopReturnWitness, GonolInitiationBoundaryReport, GonolInitiationDisposition, RejectedOriginSubstitution, GonolInitiationEvidenceStanding, GonolInitiationFalsifierResult, origin_term_registry, initiate_word_gonol, record_gonol_initiation_outcome, issue_gonol_initiation_scope_completion_receipt, build_root_loop_return_witness, run_v017_gonol_initiation_boundary_experiment
#   internal_surface: fixed GI01-GI08 evidence construction and exact validation helpers
#   auth_boundary: the in-process scope-exhaustion issuer accepts only an exact validated v0.17 authority report whose full v0.16 admission trace and every ordered v0.17 disposition, admission evidence identity, initiation receipt, rejection, evidence tuple, and trace field match the fixed producer-owned demonstration; receipt identity binds that complete evidence while external transport authentication remains outside this module
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: v0.16 adapter evidence and exact source-bound Structural Null manifestations remain linked; neither evidence identity nor carrier position zero becomes geometry
#   admin_only: false
#   tests: tests/test_gonol_initiation.py
#   rollout: nonselecting v0.17 initiation-evidence boundary over admitted occurrences with bounded native-root return semantics; no arbitrary geometry, total Structural Null topology, scoped completion, EDCM activation, or METAPAT activation
#   rollback: remove this module, exports, tests, and v0.17 document while retaining v0.16 admission evidence and v0.13 bounded initiation evidence
#   requires: edcm_assignment_admission_boundary, edcm_partial_initiation_boundary
#   since: 2026-07-31
#   unresolved: arbitrary observed-element geometric assignment, total Structural Null topology, intrinsic seam derivation, higher geometry, higher-gonol composition, scoped completion, canonical faithful breadth, and carrier selection
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: gonol_initiation_origin_roles_are_domain_separated
#   given: the v0.17 origin registry is constructed
#   then: Structural Null, source SPACE manifestation, carrier position zero, directed-cover null, neutral M, algebraic zero, absent cell, and NA retain distinct domain-qualified roles and only Structural Null may be an initiation prestate
#   class: doctrine
#   since: 2026-07-31
#
# id: gonol_initiation_requires_explicit_structural_null_transition
#   given: one v0.16 admitted word occurrence is initiated as a gonol
#   then: exactly one source-bound boundary manifestation links the singular typed Structural Null prestate to an initiated non-null evidence state while geometric assignment remains absent
#   class: correctness
#   since: 2026-07-31
#
# id: gonol_initiation_outcome_is_total_and_exclusive
#   given: v0.16 admitted occurrences enter one v0.17 trace
#   then: every occurrence retains exact order and receives exactly one initiated, unresolved, or rejected-substitution outcome with malformed combinations rejected
#   class: evidence
#   since: 2026-07-31
#
# id: gonol_initiation_root_return_is_bounded_and_noncompleting
#   given: the unchanged v0.13 source-bound root trajectory is retained
#   then: 360 degrees preserve the visible projection while changing complete local state, 720 degrees restore complete local state, both receipts survive, and no construction completion is registered
#   class: evidence
#   since: 2026-07-31
#
# id: gonol_initiation_rejects_zero_and_absence_substitutions
#   given: SPACE text, carrier zero, directed-cover null, neutral M, algebraic zero, absent cell, or NA is proposed as the Structural Null prestate
#   then: the proposal can be retained only as an explicit rejected substitution and cannot create an initiation receipt
#   class: safety
#   since: 2026-07-31
#
# id: gonol_initiation_does_not_assign_complete_select_or_activate
#   given: the v0.17 report joins origin separation, initiation outcomes, and root-return evidence
#   then: arbitrary geometry, total Structural Null topology, scoped completion, carrier selection, EDCM activation, and METAPAT activation remain absent
#   class: safety
#   since: 2026-07-31
#
# id: gonol_initiation_scope_receipt_is_producer_issued
#   given: the exact validated v0.17 authority report matching the fixed full producer-owned demonstration scope is supplied to the scope-exhaustion issuer
#   then: receipt scope, cardinality, full ordered outcome evidence digest, and identity derive from that report while consistent multi-layer prefixes, id-preserving outcome changes, sampling, construction completion, and selection remain absent
#   class: evidence
#   since: 2026-07-31
# === END CONTRACTS ===

"""Gonol-initiation and Structural Null evidence for UCNS v0.17.

The EDCM target already decides that Structural Null is singular
superpositioned space and that a new gonol initiates through the Möbius twist.
This module makes that causal evidence shape explicit without inventing the
missing geometric assignment or total carrier topology.

Every v0.16 admitted occurrence receives one initiation outcome.  A word-gonol
outcome may carry one explicit source-bound twist receipt; other occurrences
remain unresolved or retain a rejected zero/absence substitution.  The module
also preserves the unchanged v0.13 root-loop witness for 360-degree local-frame
change and 720-degree complete local return.  Local return is not registered
construction completion.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from hashlib import sha256
import json

from .assignment_boundary import (
    ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS,
    AssignmentAdmissionBoundaryReport,
    ObservedElementAdmission,
    run_v016_assignment_admission_boundary_experiment,
)
from .direct_mobius import (
    STRUCTURAL_NULL_ORIGIN,
    NativeMobiusFrame,
    StructuralNullIdentity,
    StructuralNullKind,
    StructuralNullManifestation,
)
from .edcm import EDCM_GONOL_INITIATION
from .initiation_boundary import (
    InitiatedCarrierState,
    PartialInitiationBoundaryReport,
)


V017_GONOL_INITIATION_SCHEMA_ID = (
    "ucns.edcm.gonol-initiation-structural-null-boundary"
)
V017_GONOL_INITIATION_SCHEMA_VERSION = "0.17.0"
V017_SELECTION_EFFECT = "none"

GONOL_INITIATION_SCOPE = (
    "explicit-initiation-evidence-over-v016-admitted-occurrences"
)
GONOL_INITIATION_OUTCOME_RELATION_STATUS = (
    "total-tagged-over-assignment-admitted-occurrences"
)
INITIATED_WORD_STATE_STATUS = (
    "initiated-non-null-evidence-geometric-assignment-unresolved"
)
ROOT_LOOP_RETURN_SCOPE = "v013-source-bound-native-root-loop-only"
ROOT_LOOP_COMPLETION_STATUS = "local-return-not-scoped-completion"
TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS = "unresolved-no-total-topology"
GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_ID = (
    "ucns.edcm.gonol-initiation-ordered-scope-completion-receipt"
)
GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_VERSION = "0.19.0"
GONOL_INITIATION_SCOPE_AUTHORITY_SOURCE = (
    "src/ucns/gonol_initiation.py:"
    "issue_gonol_initiation_scope_completion_receipt"
)
V017_DEMONSTRATION_TRACE_ID = "ucns-v017-gonol-initiation-demonstration"
V017_DEMONSTRATION_EXPECTED_ADMISSION_IDS = tuple(
    f"v016-demo:occurrence:{index}" for index in range(3)
)
V017_DEMONSTRATION_EXPECTED_OUTCOME_IDS = tuple(
    f"{admission_id}:gonol-initiation-outcome"
    for admission_id in V017_DEMONSTRATION_EXPECTED_ADMISSION_IDS
)

GONOL_INITIATION_FALSIFIER_IDS = tuple(
    f"GI{index:02d}" for index in range(1, 9)
)

V017_HMMM = (
    "the exact geometric relation entered after an admitted word initiates remains unresolved",
    "the source-bound twist receipt does not provide a total topology from Structural Null to arbitrary non-null states",
    "the 360-degree and 720-degree witness is bounded native-root evidence rather than a universal payload, orientation, completion, or higher-geometry law",
    "intrinsic and invariant-equivalence-class seam alternatives remain unresolved",
    "higher-gonol composition, epicycle-disk-sphere transitions, scoped completion, canonical B, proof-assistant formalization, and carrier selection remain unresolved",
)


class GonolInitiationError(ValueError):
    """Raised when v0.17 evidence crosses its declared initiation boundary."""


class OriginRole(str, Enum):
    """Domain-separated roles that must not collapse into one bare zero."""

    STRUCTURAL_NULL = "structural-null"
    SOURCE_SPACE_MANIFESTATION = "source-space-manifestation"
    CARRIER_POSITION_ZERO = "carrier-position-zero"
    DIRECTED_COVER_NULL = "directed-cover-coordinate-free-null"
    NEUTRAL_PRODUCT_CHARACTER = "neutral-product-character-m-equals-one"
    ALGEBRAIC_ZERO = "payload-algebraic-zero"
    ABSENT_CELL = "field-empty-absent-cell"
    NOT_AVAILABLE = "typed-not-available"


class OriginTermStanding(str, Enum):
    """Standing of one role in the fixed v0.17 separation registry."""

    DECIDED_CONSTRAINT = "decided-constraint"
    IMPLEMENTED_SOURCE_ROLE = "implemented-source-role"
    SUPERSEDED_COMPARISON = "superseded-for-edcm"
    TYPED_DISTINCTION = "typed-distinction"


class GonolInitiationDisposition(str, Enum):
    """Exhaustive v0.17 outcomes for an already admitted occurrence."""

    INITIATED = "explicit-mobius-twist-receipt"
    UNRESOLVED = "unresolved-no-gonol-declaration"
    REJECTED_SUBSTITUTION = "rejected-origin-substitution"


class RejectedOriginSubstitution(str, Enum):
    """Neighboring roles that cannot impersonate Structural Null."""

    SOURCE_SPACE_AS_PRESTATE = "source-space-manifestation-as-prestate"
    CARRIER_ZERO_AS_PRESTATE = "carrier-position-zero-as-prestate"
    DIRECTED_COVER_NULL_AS_PRESTATE = "directed-cover-null-as-edcm-prestate"
    NEUTRAL_M_AS_PRESTATE = "neutral-product-character-as-prestate"
    ALGEBRAIC_ZERO_AS_PRESTATE = "algebraic-zero-as-prestate"
    ABSENT_CELL_AS_PRESTATE = "absent-cell-as-prestate"
    NA_AS_PRESTATE = "not-available-as-prestate"


class GonolInitiationEvidenceStanding(str, Enum):
    """Standing vocabulary for the fixed GI01-GI08 packet."""

    EXACT_IMPLEMENTED_SUPPORTED = "exact-implemented-supported"
    BOUNDED_UPSTREAM_SUPPORTED = "bounded-upstream-supported"
    NEGATIVE_SUPPORTED = "negative-supported"
    UNRESOLVED = "unresolved"


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise GonolInitiationError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise GonolInitiationError(f"{field} must retain evidence")
    for value in values:
        _require_text(value, field)


@dataclass(frozen=True, slots=True)
class OriginTermRecord:
    """One domain-qualified origin, zero, neutrality, or absence role."""

    role: OriginRole
    term_id: str
    claimed_sense: str
    standing: OriginTermStanding
    may_be_initiation_prestate: bool

    def __post_init__(self) -> None:
        if not isinstance(self.role, OriginRole):
            raise GonolInitiationError("origin role is invalid")
        _require_text(self.term_id, "term_id")
        if not self.term_id.startswith("ucns."):
            raise GonolInitiationError("origin term id must be domain-qualified")
        _require_text(self.claimed_sense, "claimed_sense")
        if not isinstance(self.standing, OriginTermStanding):
            raise GonolInitiationError("origin standing is invalid")
        if self.may_be_initiation_prestate != (
            self.role is OriginRole.STRUCTURAL_NULL
        ):
            raise GonolInitiationError(
                "only Structural Null may be the initiation prestate"
            )
        if self.role is OriginRole.STRUCTURAL_NULL and (
            self.standing is not OriginTermStanding.DECIDED_CONSTRAINT
        ):
            raise GonolInitiationError(
                "Structural Null must retain decided-constraint standing"
            )


def origin_term_registry() -> tuple[OriginTermRecord, ...]:
    """Return the fixed domain-separated v0.17 origin-role registry."""

    return (
        OriginTermRecord(
            OriginRole.STRUCTURAL_NULL,
            "ucns.edcm_origin.structural_null",
            "singular superpositioned hidden-zero initiation prestate",
            OriginTermStanding.DECIDED_CONSTRAINT,
            True,
        ),
        OriginTermRecord(
            OriginRole.SOURCE_SPACE_MANIFESTATION,
            "ucns.edcm_origin.space_manifestation",
            "exact source or turn-boundary witness linked to the singular origin",
            OriginTermStanding.IMPLEMENTED_SOURCE_ROLE,
            False,
        ),
        OriginTermRecord(
            OriginRole.CARRIER_POSITION_ZERO,
            "ucns.edcm_carrier.position_zero",
            "U+0020 address in the exact public 157-position carrier",
            OriginTermStanding.IMPLEMENTED_SOURCE_ROLE,
            False,
        ),
        OriginTermRecord(
            OriginRole.DIRECTED_COVER_NULL,
            "ucns.directed_cover.coordinate_free_null",
            "coordinate-free absence in the comparison carrier",
            OriginTermStanding.SUPERSEDED_COMPARISON,
            False,
        ),
        OriginTermRecord(
            OriginRole.NEUTRAL_PRODUCT_CHARACTER,
            "ucns.product_character.neutral",
            "proposed non-null multiplicative value M equals one",
            OriginTermStanding.TYPED_DISTINCTION,
            False,
        ),
        OriginTermRecord(
            OriginRole.ALGEBRAIC_ZERO,
            "ucns.payload.algebraic_zero",
            "zero value inside one declared payload algebra",
            OriginTermStanding.TYPED_DISTINCTION,
            False,
        ),
        OriginTermRecord(
            OriginRole.ABSENT_CELL,
            "ucns.cell.absent",
            "field-empty potential cell with support mu equal to zero",
            OriginTermStanding.TYPED_DISTINCTION,
            False,
        ),
        OriginTermRecord(
            OriginRole.NOT_AVAILABLE,
            "ucns.evidence.not_available",
            "typed absence or inapplicability distinct from every zero",
            OriginTermStanding.TYPED_DISTINCTION,
            False,
        ),
    )


@dataclass(frozen=True, slots=True)
class GonolInitiationReceipt:
    """One causal word-gonol initiation with no inferred geometry."""

    receipt_id: str
    gonol_id: str
    admission: ObservedElementAdmission
    boundary_manifestation: StructuralNullManifestation
    pre_state: StructuralNullIdentity = STRUCTURAL_NULL_ORIGIN
    initiation_event: str = EDCM_GONOL_INITIATION
    twist_receipt_count: int = 1
    post_state_status: str = INITIATED_WORD_STATE_STATUS
    geometric_assignment: None = None
    parent_gonol_ids: tuple[str, ...] = ()
    completion_registered: bool = False
    scope: str = GONOL_INITIATION_SCOPE
    selection_effect: str = V017_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.receipt_id, "receipt_id")
        _require_text(self.gonol_id, "gonol_id")
        if not isinstance(self.admission, ObservedElementAdmission):
            raise GonolInitiationError(
                "gonol initiation requires a v0.16 admitted occurrence"
            )
        if self.admission.grain != "word":
            raise GonolInitiationError(
                "v0.17 initiates only the decided smallest word gonol"
            )
        if not isinstance(
            self.boundary_manifestation,
            StructuralNullManifestation,
        ):
            raise GonolInitiationError(
                "gonol initiation requires an explicit boundary manifestation"
            )
        if self.boundary_manifestation.origin is not STRUCTURAL_NULL_ORIGIN:
            raise GonolInitiationError(
                "boundary manifestation must link the singular Structural Null"
            )
        if self.boundary_manifestation.witness_id != self.admission.source_id:
            raise GonolInitiationError(
                "boundary manifestation must retain the admitted source identity"
            )
        if self.pre_state is not STRUCTURAL_NULL_ORIGIN:
            raise GonolInitiationError(
                "gonol initiation prestate must be singular Structural Null"
            )
        if self.receipt_id != f"{self.admission.admission_id}:gonol-initiation":
            raise GonolInitiationError(
                "initiation receipt identity must derive from admission identity"
            )
        if self.initiation_event != EDCM_GONOL_INITIATION:
            raise GonolInitiationError(
                "a new gonol must initiate through the Mobius twist"
            )
        if self.twist_receipt_count != 1:
            raise GonolInitiationError(
                "an initiated gonol must retain exactly one twist receipt"
            )
        if self.post_state_status != INITIATED_WORD_STATE_STATUS:
            raise GonolInitiationError(
                "initiated post-state standing is fixed"
            )
        if self.geometric_assignment is not None:
            raise GonolInitiationError(
                "initiation receipt cannot manufacture geometric assignment"
            )
        if self.parent_gonol_ids:
            raise GonolInitiationError(
                "higher-gonol composition remains unresolved in v0.17"
            )
        if self.completion_registered:
            raise GonolInitiationError(
                "gonol initiation is not registered construction completion"
            )
        if self.scope != GONOL_INITIATION_SCOPE:
            raise GonolInitiationError("gonol initiation scope is fixed")
        if self.selection_effect != V017_SELECTION_EFFECT:
            raise GonolInitiationError(
                "gonol initiation receipt cannot select geometry"
            )

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        return (
            self.receipt_id,
            self.gonol_id,
            self.admission.evidence_identity,
            self.boundary_manifestation.manifestation_id,
            self.boundary_manifestation.source_reference,
            self.pre_state.origin_id,
            self.initiation_event,
            self.twist_receipt_count,
            self.post_state_status,
        )


def initiate_word_gonol(
    admission: ObservedElementAdmission,
    *,
    gonol_id: str,
    boundary_manifestation: StructuralNullManifestation,
) -> GonolInitiationReceipt:
    """Create one explicit pre-geometric word-gonol initiation receipt."""

    if not isinstance(admission, ObservedElementAdmission):
        raise TypeError("admission must be ObservedElementAdmission")
    return GonolInitiationReceipt(
        receipt_id=f"{admission.admission_id}:gonol-initiation",
        gonol_id=gonol_id,
        admission=admission,
        boundary_manifestation=boundary_manifestation,
    )


@dataclass(frozen=True, slots=True)
class GonolInitiationOutcome:
    """Exactly one initiation outcome for one admitted occurrence."""

    outcome_id: str
    admission: ObservedElementAdmission
    disposition: GonolInitiationDisposition
    evidence: tuple[str, ...]
    initiation: GonolInitiationReceipt | None = None
    rejected_substitution: RejectedOriginSubstitution | None = None
    selection_effect: str = V017_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.outcome_id, "outcome_id")
        if not isinstance(self.admission, ObservedElementAdmission):
            raise GonolInitiationError(
                "initiation outcome requires an admitted occurrence"
            )
        if self.outcome_id != (
            f"{self.admission.admission_id}:gonol-initiation-outcome"
        ):
            raise GonolInitiationError(
                "initiation outcome identity must derive from admission identity"
            )
        if not isinstance(self.disposition, GonolInitiationDisposition):
            raise GonolInitiationError("initiation disposition is invalid")
        _require_text_items(self.evidence, "initiation outcome evidence")
        if self.selection_effect != V017_SELECTION_EFFECT:
            raise GonolInitiationError(
                "initiation outcome cannot select geometry"
            )

        if self.disposition is GonolInitiationDisposition.INITIATED:
            if not isinstance(self.initiation, GonolInitiationReceipt):
                raise GonolInitiationError(
                    "initiated outcome requires one initiation receipt"
                )
            if self.initiation.admission != self.admission:
                raise GonolInitiationError(
                    "initiation receipt must retain the same admitted occurrence"
                )
            if self.rejected_substitution is not None:
                raise GonolInitiationError(
                    "initiated outcome cannot also reject a substitution"
                )
        elif self.disposition is GonolInitiationDisposition.UNRESOLVED:
            if self.initiation is not None or self.rejected_substitution is not None:
                raise GonolInitiationError(
                    "unresolved outcome cannot contain initiation or rejection"
                )
        else:
            if self.initiation is not None:
                raise GonolInitiationError(
                    "rejected substitution cannot create an initiation receipt"
                )
            if not isinstance(
                self.rejected_substitution,
                RejectedOriginSubstitution,
            ):
                raise GonolInitiationError(
                    "rejected outcome requires a named origin substitution"
                )

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        """Retain disposition, admission, receipt, rejection, and evidence."""

        return (
            self.outcome_id,
            self.admission.evidence_identity,
            self.disposition.value,
            self.evidence,
            (
                self.initiation.evidence_identity
                if self.initiation is not None
                else None
            ),
            (
                self.rejected_substitution.value
                if self.rejected_substitution is not None
                else None
            ),
            self.selection_effect,
        )


def record_gonol_initiation_outcome(
    admission: ObservedElementAdmission,
    *,
    evidence: tuple[str, ...],
    initiation: GonolInitiationReceipt | None = None,
    rejected_substitution: RejectedOriginSubstitution | None = None,
) -> GonolInitiationOutcome:
    """Record one exclusive initiation outcome without a hidden default."""

    if not isinstance(admission, ObservedElementAdmission):
        raise TypeError("admission must be ObservedElementAdmission")
    if initiation is not None and rejected_substitution is not None:
        raise GonolInitiationError(
            "an initiation outcome cannot be both initiated and rejected"
        )
    if initiation is not None:
        disposition = GonolInitiationDisposition.INITIATED
    elif rejected_substitution is not None:
        disposition = GonolInitiationDisposition.REJECTED_SUBSTITUTION
    else:
        disposition = GonolInitiationDisposition.UNRESOLVED
    return GonolInitiationOutcome(
        outcome_id=f"{admission.admission_id}:gonol-initiation-outcome",
        admission=admission,
        disposition=disposition,
        evidence=evidence,
        initiation=initiation,
        rejected_substitution=rejected_substitution,
    )


@dataclass(frozen=True, slots=True)
class GonolInitiationTrace:
    """Ordered total tagged initiation evidence over admitted occurrences."""

    trace_id: str
    outcomes: tuple[GonolInitiationOutcome, ...]
    scope: str = GONOL_INITIATION_SCOPE
    outcome_relation_status: str = GONOL_INITIATION_OUTCOME_RELATION_STATUS
    selection_effect: str = V017_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.trace_id, "trace_id")
        if not self.outcomes:
            raise GonolInitiationError(
                "gonol initiation trace must retain at least one outcome"
            )
        if self.scope != GONOL_INITIATION_SCOPE:
            raise GonolInitiationError("gonol initiation trace scope is fixed")
        if (
            self.outcome_relation_status
            != GONOL_INITIATION_OUTCOME_RELATION_STATUS
        ):
            raise GonolInitiationError(
                "gonol initiation outcome relation status is fixed"
            )
        if self.selection_effect != V017_SELECTION_EFFECT:
            raise GonolInitiationError(
                "gonol initiation trace cannot select geometry"
            )

        admission_ids: set[str] = set()
        outcome_ids: set[str] = set()
        gonol_ids: set[str] = set()
        for expected_index, outcome in enumerate(self.outcomes):
            if not isinstance(outcome, GonolInitiationOutcome):
                raise GonolInitiationError(
                    "trace outcomes must be GonolInitiationOutcome values"
                )
            if outcome.admission.occurrence_index != expected_index:
                raise GonolInitiationError(
                    "admitted occurrences must retain contiguous input order"
                )
            if outcome.admission.admission_id in admission_ids:
                raise GonolInitiationError(
                    "admission identities must remain unique per occurrence"
                )
            if outcome.outcome_id in outcome_ids:
                raise GonolInitiationError(
                    "initiation outcome identities must be unique"
                )
            if outcome.initiation is not None:
                if outcome.initiation.gonol_id in gonol_ids:
                    raise GonolInitiationError(
                        "initiated gonol identities must be unique"
                    )
                gonol_ids.add(outcome.initiation.gonol_id)
            admission_ids.add(outcome.admission.admission_id)
            outcome_ids.add(outcome.outcome_id)

    @property
    def has_total_outcome_evidence(self) -> bool:
        return len(self.outcomes) == len(
            {outcome.admission.admission_id for outcome in self.outcomes}
        )

    @property
    def subject_digests(self) -> tuple[str, ...]:
        return tuple(
            outcome.admission.subject_record.digest for outcome in self.outcomes
        )

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        """Return the complete ordered outcome evidence identity."""

        return (
            self.trace_id,
            tuple(outcome.evidence_identity for outcome in self.outcomes),
            self.scope,
            self.outcome_relation_status,
            self.selection_effect,
        )


@dataclass(frozen=True, slots=True)
class RootLoopReturnWitness:
    """Bounded v0.13 360-degree/720-degree root-return evidence."""

    initial: InitiatedCarrierState
    after_360: InitiatedCarrierState
    after_720: InitiatedCarrierState
    visible_return_degrees: int = 360
    complete_local_return_degrees: int = 720
    scope: str = ROOT_LOOP_RETURN_SCOPE
    completion_status: str = ROOT_LOOP_COMPLETION_STATUS
    completion_registered: bool = False

    def __post_init__(self) -> None:
        for state in (self.initial, self.after_360, self.after_720):
            if not isinstance(state, InitiatedCarrierState):
                raise GonolInitiationError(
                    "root return witness requires v0.13 initiated states"
                )
        attachment_ids = {
            state.attachment.attachment_identity
            for state in (self.initial, self.after_360, self.after_720)
        }
        if len(attachment_ids) != 1:
            raise GonolInitiationError(
                "root return states must retain one initiation attachment"
            )
        if self.initial.motion_history:
            raise GonolInitiationError(
                "initial root state cannot contain motion receipts"
            )
        if len(self.after_360.motion_history) != 1:
            raise GonolInitiationError(
                "360-degree state must retain one motion receipt"
            )
        if len(self.after_720.motion_history) != 2:
            raise GonolInitiationError(
                "720-degree state must retain both motion receipts"
            )
        if any(
            receipt.motion_turns != Fraction(1)
            for receipt in self.after_720.motion_history
        ):
            raise GonolInitiationError(
                "root return receipts must each retain one exact visible turn"
            )
        if (
            self.after_360.motion_history
            != self.after_720.motion_history[:1]
        ):
            raise GonolInitiationError(
                "720-degree history must append without replacing 360 evidence"
            )
        if self.initial.visible_identity != self.after_360.visible_identity:
            raise GonolInitiationError(
                "360 degrees must restore the declared visible projection"
            )
        if (
            self.initial.complete_local_identity
            == self.after_360.complete_local_identity
        ):
            raise GonolInitiationError(
                "360 degrees must change complete local root state"
            )
        if (
            self.initial.complete_local_identity
            != self.after_720.complete_local_identity
        ):
            raise GonolInitiationError(
                "720 degrees must restore complete local root state"
            )
        if (
            self.initial.native_state.frame is not NativeMobiusFrame.POSITIVE
            or self.after_360.native_state.frame
            is not NativeMobiusFrame.REVERSED
            or self.after_720.native_state.frame
            is not NativeMobiusFrame.POSITIVE
        ):
            raise GonolInitiationError(
                "root return witness must retain positive-reversed-positive frames"
            )
        if (
            self.visible_return_degrees != 360
            or self.complete_local_return_degrees != 720
            or self.scope != ROOT_LOOP_RETURN_SCOPE
            or self.completion_status != ROOT_LOOP_COMPLETION_STATUS
        ):
            raise GonolInitiationError(
                "root return degrees, scope, and completion standing are fixed"
            )
        if self.completion_registered:
            raise GonolInitiationError(
                "local root return cannot register construction completion"
            )


def build_root_loop_return_witness(
    report: PartialInitiationBoundaryReport,
) -> RootLoopReturnWitness:
    """Retain the exact unchanged v0.13 root trajectory as one witness."""

    if not isinstance(report, PartialInitiationBoundaryReport):
        raise TypeError("report must be PartialInitiationBoundaryReport")
    initial, after_360, after_720 = report.trajectory
    return RootLoopReturnWitness(initial, after_360, after_720)


@dataclass(frozen=True, slots=True)
class GonolInitiationFalsifierResult:
    """One fixed GI01-GI08 initiation-boundary standing."""

    falsifier_id: str
    standing: GonolInitiationEvidenceStanding
    evidence: tuple[str, ...]
    limitation: str

    def __post_init__(self) -> None:
        if self.falsifier_id not in GONOL_INITIATION_FALSIFIER_IDS:
            raise GonolInitiationError("unknown gonol-initiation falsifier id")
        if not isinstance(self.standing, GonolInitiationEvidenceStanding):
            raise GonolInitiationError(
                "gonol-initiation falsifier standing is invalid"
            )
        _require_text_items(self.evidence, "gonol-initiation falsifier evidence")
        _require_text(self.limitation, "gonol-initiation falsifier limitation")


def _build_results(
    trace: GonolInitiationTrace,
    root_return: RootLoopReturnWitness,
) -> tuple[GonolInitiationFalsifierResult, ...]:
    terms = origin_term_registry()
    initiated = tuple(
        outcome.initiation
        for outcome in trace.outcomes
        if outcome.initiation is not None
    )
    return (
        GonolInitiationFalsifierResult(
            "GI01",
            GonolInitiationEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"origin-roles:{len(terms)}",
                "domain-qualified-term-ids:unique",
                "sole-initiation-prestate:ucns.edcm_origin.structural_null",
            ),
            "the registry separates roles; it does not construct the missing total topology",
        ),
        GonolInitiationFalsifierResult(
            "GI02",
            GonolInitiationEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"explicit-initiations:{len(initiated)}",
                f"prestate:{STRUCTURAL_NULL_ORIGIN.origin_id}",
                "boundary-manifestation:source-bound",
                f"post-state:{INITIATED_WORD_STATE_STATUS}",
            ),
            "support applies only when a caller explicitly declares the admitted occurrence to be a word gonol and supplies a boundary manifestation",
        ),
        GonolInitiationFalsifierResult(
            "GI03",
            GonolInitiationEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                "twist-receipts-per-initiated-gonol:1",
                "receipt-links:admission+boundary+singular-prestate",
                "geometric-assignment:absent",
            ),
            "receipt cardinality establishes causal evidence shape, not geometric truth",
        ),
        GonolInitiationFalsifierResult(
            "GI04",
            GonolInitiationEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
            (
                f"outcome-relation:{GONOL_INITIATION_OUTCOME_RELATION_STATUS}",
                "exclusive-tags:initiated|unresolved|rejected-substitution",
                "ordered-occurrence-identity:retained",
            ),
            "totality is over tagged initiation evidence for v0.16 admissions, not over possible subjects or geometric states",
        ),
        GonolInitiationFalsifierResult(
            "GI05",
            GonolInitiationEvidenceStanding.BOUNDED_UPSTREAM_SUPPORTED,
            (
                f"scope:{root_return.scope}",
                "visible-after-360:equal",
                "complete-local-after-360:changed",
                "native-frame:positive-to-reversed",
            ),
            "support is bounded to the unchanged source-bound v0.13 native root-loop candidate",
        ),
        GonolInitiationFalsifierResult(
            "GI06",
            GonolInitiationEvidenceStanding.BOUNDED_UPSTREAM_SUPPORTED,
            (
                "complete-local-after-720:equal",
                "motion-receipts:2",
                f"completion:{ROOT_LOOP_COMPLETION_STATUS}",
            ),
            "local return is not a scoped completion receipt and does not exhaust the unknowable",
        ),
        GonolInitiationFalsifierResult(
            "GI07",
            GonolInitiationEvidenceStanding.NEGATIVE_SUPPORTED,
            tuple(
                f"rejected:{substitution.value}"
                for substitution in RejectedOriginSubstitution
            ),
            "neighboring roles remain available in their own domains but cannot impersonate the singular initiation prestate",
        ),
        GonolInitiationFalsifierResult(
            "GI08",
            GonolInitiationEvidenceStanding.UNRESOLVED,
            (
                f"arbitrary-geometric-assignment:{ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS}",
                f"total-structural-null-topology:{TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS}",
                "carrier-selection:none",
                "EDCM-activation:inactive",
                "METAPAT-activation:inactive",
            ),
            "initiation evidence does not supply arbitrary geometry, a total topology, scoped completion, or consumer activation",
        ),
    )


@dataclass(frozen=True, slots=True)
class GonolInitiationBoundaryReport:
    """v0.17 initiation evidence joined to unchanged v0.16 and v0.13 standing."""

    upstream: AssignmentAdmissionBoundaryReport
    origin_terms: tuple[OriginTermRecord, ...]
    demonstration_trace: GonolInitiationTrace
    root_return: RootLoopReturnWitness
    results: tuple[GonolInitiationFalsifierResult, ...]
    schema_id: str = V017_GONOL_INITIATION_SCHEMA_ID
    schema_version: str = V017_GONOL_INITIATION_SCHEMA_VERSION
    origin_separation_status: str = "implemented-fixed-domain-registry"
    initiation_outcome_relation_status: str = (
        GONOL_INITIATION_OUTCOME_RELATION_STATUS
    )
    arbitrary_element_assignment_status: str = (
        ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS
    )
    total_structural_null_topology_status: str = (
        TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS
    )
    selection_effect: str = V017_SELECTION_EFFECT
    edcm_activation: str = "inactive"
    metapat_activation: str = "inactive"
    hmmm: tuple[str, ...] = V017_HMMM

    def __post_init__(self) -> None:
        if not isinstance(self.upstream, AssignmentAdmissionBoundaryReport):
            raise GonolInitiationError(
                "v0.17 report requires the exact v0.16 upstream report"
            )
        if self.origin_terms != origin_term_registry():
            raise GonolInitiationError(
                "v0.17 origin-role registry is fixed and ordered"
            )
        if len({term.term_id for term in self.origin_terms}) != len(
            self.origin_terms
        ):
            raise GonolInitiationError(
                "domain-qualified origin term ids must be unique"
            )
        if not isinstance(self.demonstration_trace, GonolInitiationTrace):
            raise GonolInitiationError(
                "v0.17 report requires an initiation trace"
            )
        expected_upstream = run_v016_assignment_admission_boundary_experiment()
        if (
            self.upstream.demonstration_trace
            != expected_upstream.demonstration_trace
        ):
            raise GonolInitiationError(
                "v0.17 authority report must retain the exact full producer admission trace"
            )
        expected_demonstration_trace = _demonstration_trace(expected_upstream)
        if self.demonstration_trace != expected_demonstration_trace:
            raise GonolInitiationError(
                "v0.17 authority report must retain every full producer outcome"
            )
        upstream_admissions = tuple(
            outcome.admission
            for outcome in self.upstream.demonstration_trace.outcomes
        )
        if (
            self.demonstration_trace.trace_id != V017_DEMONSTRATION_TRACE_ID
            or tuple(
                admission.admission_id for admission in upstream_admissions
            )
            != V017_DEMONSTRATION_EXPECTED_ADMISSION_IDS
            or tuple(
                outcome.outcome_id
                for outcome in self.demonstration_trace.outcomes
            )
            != V017_DEMONSTRATION_EXPECTED_OUTCOME_IDS
        ):
            raise GonolInitiationError(
                "v0.17 authority report must retain the fixed full producer scope"
            )
        if tuple(
            outcome.admission for outcome in self.demonstration_trace.outcomes
        ) != upstream_admissions:
            raise GonolInitiationError(
                "v0.17 trace must retain the exact v0.16 admitted occurrences"
            )
        expected_root_return = build_root_loop_return_witness(
            self.upstream.upstream.partial_initiation_report
        )
        if self.root_return != expected_root_return:
            raise GonolInitiationError(
                "v0.17 must retain the unchanged v0.13 root-return witness"
            )
        if self.results != _build_results(
            self.demonstration_trace,
            self.root_return,
        ):
            raise GonolInitiationError(
                "v0.17 GI01-GI08 falsifier packet is fixed"
            )
        if tuple(result.falsifier_id for result in self.results) != (
            GONOL_INITIATION_FALSIFIER_IDS
        ):
            raise GonolInitiationError(
                "v0.17 must retain GI01 through GI08 in order"
            )
        if (
            self.schema_id != V017_GONOL_INITIATION_SCHEMA_ID
            or self.schema_version != V017_GONOL_INITIATION_SCHEMA_VERSION
            or self.origin_separation_status
            != "implemented-fixed-domain-registry"
            or self.initiation_outcome_relation_status
            != GONOL_INITIATION_OUTCOME_RELATION_STATUS
            or self.arbitrary_element_assignment_status
            != ARBITRARY_GEOMETRIC_ASSIGNMENT_STATUS
            or self.total_structural_null_topology_status
            != TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS
        ):
            raise GonolInitiationError(
                "v0.17 schema and boundary standings are fixed"
            )
        if self.selection_effect != V017_SELECTION_EFFECT:
            raise GonolInitiationError("v0.17 cannot select geometry")
        if self.edcm_activation != "inactive":
            raise GonolInitiationError("v0.17 cannot activate EDCM")
        if self.metapat_activation != "inactive":
            raise GonolInitiationError("v0.17 cannot activate METAPAT")
        if self.hmmm != V017_HMMM:
            raise GonolInitiationError(
                "v0.17 unresolved boundary is fixed"
            )

    def result(self, falsifier_id: str) -> GonolInitiationFalsifierResult:
        for result in self.results:
            if result.falsifier_id == falsifier_id:
                return result
        raise GonolInitiationError(
            f"unknown gonol-initiation falsifier: {falsifier_id}"
        )


def _trace_evidence_sha256(trace: GonolInitiationTrace) -> str:
    return sha256(
        json.dumps(
            trace.evidence_identity,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _scope_completion_receipt_id(
    report: GonolInitiationBoundaryReport,
) -> str:
    trace = report.demonstration_trace
    payload = {
        "authority_schema_id": report.schema_id,
        "authority_schema_version": report.schema_version,
        "expected_admission_ids": [
            outcome.admission.admission_id
            for outcome in report.upstream.demonstration_trace.outcomes
        ],
        "expected_outcome_ids": [
            outcome.outcome_id for outcome in trace.outcomes
        ],
        "expected_trace_evidence_sha256": _trace_evidence_sha256(trace),
        "receipt_schema_id": (
            GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_ID
        ),
        "receipt_schema_version": (
            GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_VERSION
        ),
        "source_scope_id": trace.trace_id,
    }
    return sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


@dataclass(frozen=True, slots=True)
class GonolInitiationScopeCompletionReceipt:
    """Producer-issued proof that one v0.17 outcome trace is exhaustive."""

    authority_report: GonolInitiationBoundaryReport
    upstream_trace: GonolInitiationTrace
    receipt_id: str
    source_scope_id: str
    expected_cardinality: int
    expected_outcome_ids: tuple[str, ...]
    expected_trace_evidence_sha256: str
    evidence: tuple[str, ...]
    schema_id: str = GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_ID
    schema_version: str = GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_VERSION
    authority_source: str = GONOL_INITIATION_SCOPE_AUTHORITY_SOURCE
    source_exhausted: bool = True
    sampling: bool = False
    prefix: bool = False
    construction_completion_registered: bool = False
    selection_effect: str = V017_SELECTION_EFFECT

    def __post_init__(self) -> None:
        if not isinstance(
            self.authority_report,
            GonolInitiationBoundaryReport,
        ):
            raise GonolInitiationError(
                "scope completion receipt requires the v0.17 authority report"
            )
        exact_trace = self.authority_report.demonstration_trace
        if self.upstream_trace is not exact_trace:
            raise GonolInitiationError(
                "scope completion receipt must retain the authority report's exact trace"
            )
        authority_admissions = tuple(
            outcome.admission
            for outcome in self.authority_report.upstream.demonstration_trace.outcomes
        )
        trace_admissions = tuple(
            outcome.admission for outcome in exact_trace.outcomes
        )
        if trace_admissions != authority_admissions:
            raise GonolInitiationError(
                "authority trace must exhaust the exact upstream admissions"
            )
        expected_outcome_ids = tuple(
            outcome.outcome_id for outcome in exact_trace.outcomes
        )
        expected_trace_evidence_sha256 = _trace_evidence_sha256(exact_trace)
        expected_evidence = (
            f"authority-report:{self.authority_report.schema_id}/"
            f"{self.authority_report.schema_version}",
            f"authority-source:{GONOL_INITIATION_SCOPE_AUTHORITY_SOURCE}",
            "authority-trace-object:exact",
            f"source-scope-id:{exact_trace.trace_id}",
            f"expected-cardinality:{len(authority_admissions)}",
            f"ordered-outcome-ids:{'|'.join(expected_outcome_ids)}",
            f"trace-evidence-sha256:{expected_trace_evidence_sha256}",
            "source-exhausted:true",
            "sampling:false",
            "prefix:false",
            "construction-completion-registered:false",
        )
        if (
            self.receipt_id != _scope_completion_receipt_id(self.authority_report)
            or self.source_scope_id != exact_trace.trace_id
            or self.expected_cardinality != len(authority_admissions)
            or self.expected_outcome_ids != expected_outcome_ids
            or self.expected_trace_evidence_sha256
            != expected_trace_evidence_sha256
            or self.evidence != expected_evidence
        ):
            raise GonolInitiationError(
                "scope completion receipt must derive from the exact authority report"
            )
        if (
            self.schema_id
            != GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_ID
            or self.schema_version
            != GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_VERSION
            or self.authority_source != GONOL_INITIATION_SCOPE_AUTHORITY_SOURCE
            or self.source_exhausted is not True
            or self.sampling is not False
            or self.prefix is not False
            or self.construction_completion_registered is not False
            or self.selection_effect != V017_SELECTION_EFFECT
        ):
            raise GonolInitiationError(
                "scope completion receipt standing is fixed and nonpromoting"
            )

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        return (
            self.receipt_id,
            self.authority_report.schema_id,
            self.authority_report.schema_version,
            self.upstream_trace.trace_id,
            self.source_scope_id,
            self.expected_cardinality,
            self.expected_outcome_ids,
            self.expected_trace_evidence_sha256,
            self.evidence,
            self.schema_id,
            self.schema_version,
            self.authority_source,
            self.source_exhausted,
            self.sampling,
            self.prefix,
            self.construction_completion_registered,
            self.selection_effect,
        )


def issue_gonol_initiation_scope_completion_receipt(
    report: GonolInitiationBoundaryReport,
) -> GonolInitiationScopeCompletionReceipt:
    """Issue trace-exhaustion evidence from the exact v0.17 producer report."""

    if not isinstance(report, GonolInitiationBoundaryReport):
        raise TypeError("report must be GonolInitiationBoundaryReport")
    trace = report.demonstration_trace
    expected_cardinality = len(report.upstream.demonstration_trace.outcomes)
    expected_outcome_ids = tuple(
        outcome.outcome_id for outcome in trace.outcomes
    )
    expected_trace_evidence_sha256 = _trace_evidence_sha256(trace)
    evidence = (
        f"authority-report:{report.schema_id}/{report.schema_version}",
        f"authority-source:{GONOL_INITIATION_SCOPE_AUTHORITY_SOURCE}",
        "authority-trace-object:exact",
        f"source-scope-id:{trace.trace_id}",
        f"expected-cardinality:{expected_cardinality}",
        f"ordered-outcome-ids:{'|'.join(expected_outcome_ids)}",
        f"trace-evidence-sha256:{expected_trace_evidence_sha256}",
        "source-exhausted:true",
        "sampling:false",
        "prefix:false",
        "construction-completion-registered:false",
    )
    return GonolInitiationScopeCompletionReceipt(
        authority_report=report,
        upstream_trace=trace,
        receipt_id=_scope_completion_receipt_id(report),
        source_scope_id=trace.trace_id,
        expected_cardinality=expected_cardinality,
        expected_outcome_ids=expected_outcome_ids,
        expected_trace_evidence_sha256=expected_trace_evidence_sha256,
        evidence=evidence,
    )


def _demonstration_trace(
    upstream: AssignmentAdmissionBoundaryReport,
) -> GonolInitiationTrace:
    admissions = tuple(
        outcome.admission for outcome in upstream.demonstration_trace.outcomes
    )
    boundary = StructuralNullManifestation(
        manifestation_id="v017-demo:turn-boundary",
        witness_id=admissions[0].source_id,
        kind=StructuralNullKind.TURN_BOUNDARY,
        source_offset=None,
        source_value=None,
    )
    initiation = initiate_word_gonol(
        admissions[0],
        gonol_id="v017-demo:word-gonol:0",
        boundary_manifestation=boundary,
    )
    outcomes = (
        record_gonol_initiation_outcome(
            admissions[0],
            initiation=initiation,
            evidence=(
                "explicit word-gonol declaration",
                "source-bound turn-boundary Structural Null manifestation",
            ),
        ),
        record_gonol_initiation_outcome(
            admissions[1],
            evidence=(
                "no explicit gonol declaration supplied for this occurrence",
            ),
        ),
        record_gonol_initiation_outcome(
            admissions[2],
            rejected_substitution=(
                RejectedOriginSubstitution.ALGEBRAIC_ZERO_AS_PRESTATE
            ),
            evidence=(
                "algebraic zero remains a payload-domain value, not Structural Null",
            ),
        ),
    )
    return GonolInitiationTrace(
        trace_id=V017_DEMONSTRATION_TRACE_ID,
        outcomes=outcomes,
    )


def run_v017_gonol_initiation_boundary_experiment(
) -> GonolInitiationBoundaryReport:
    """Construct the fixed v0.17 initiation and root-return evidence graph."""

    upstream = run_v016_assignment_admission_boundary_experiment()
    trace = _demonstration_trace(upstream)
    root_return = build_root_loop_return_witness(
        upstream.upstream.partial_initiation_report
    )
    return GonolInitiationBoundaryReport(
        upstream=upstream,
        origin_terms=origin_term_registry(),
        demonstration_trace=trace,
        root_return=root_return,
        results=_build_results(trace, root_return),
    )


__all__ = [
    "GONOL_INITIATION_FALSIFIER_IDS",
    "GONOL_INITIATION_OUTCOME_RELATION_STATUS",
    "GONOL_INITIATION_SCOPE",
    "GONOL_INITIATION_SCOPE_AUTHORITY_SOURCE",
    "GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_ID",
    "GONOL_INITIATION_SCOPE_COMPLETION_RECEIPT_SCHEMA_VERSION",
    "INITIATED_WORD_STATE_STATUS",
    "ROOT_LOOP_COMPLETION_STATUS",
    "ROOT_LOOP_RETURN_SCOPE",
    "TOTAL_STRUCTURAL_NULL_TOPOLOGY_STATUS",
    "V017_GONOL_INITIATION_SCHEMA_ID",
    "V017_GONOL_INITIATION_SCHEMA_VERSION",
    "V017_HMMM",
    "V017_SELECTION_EFFECT",
    "V017_DEMONSTRATION_TRACE_ID",
    "V017_DEMONSTRATION_EXPECTED_ADMISSION_IDS",
    "V017_DEMONSTRATION_EXPECTED_OUTCOME_IDS",
    "GonolInitiationBoundaryReport",
    "GonolInitiationDisposition",
    "GonolInitiationError",
    "GonolInitiationEvidenceStanding",
    "GonolInitiationFalsifierResult",
    "GonolInitiationOutcome",
    "GonolInitiationReceipt",
    "GonolInitiationScopeCompletionReceipt",
    "GonolInitiationTrace",
    "OriginRole",
    "OriginTermRecord",
    "OriginTermStanding",
    "RejectedOriginSubstitution",
    "RootLoopReturnWitness",
    "build_root_loop_return_witness",
    "initiate_word_gonol",
    "issue_gonol_initiation_scope_completion_receipt",
    "origin_term_registry",
    "record_gonol_initiation_outcome",
    "run_v017_gonol_initiation_boundary_experiment",
]
