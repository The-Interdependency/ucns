# === MODULE_BUILD ===
# id: edcm_partial_initiation_boundary
#   module_name: initiation_boundary
#   module_kind: experiment
#   summary: attaches the typed Structural Null prestate to exact root coordinates through source-provenance marked seams and retained twist receipts
#   owner: Erin Spencer
#   public_surface: StructuralNullTopologyKind, MarkedInitiationSeam, SeamCoordinateView, TwistReceipt, PartialInitiationAttachment, CarrierMotionReceipt, RootVisibleProjection, InitiatedCarrierState, ContinuityFalsifierResult, PartialInitiationBoundaryReport, partial_initiation_exact_comparison_policy, build_partial_initiation_attachments, view_marked_seam_at_cut, project_root_visible_state, initiate_carrier_state, advance_attached_state, exact_sheet_involution, run_v013_partial_initiation_boundary_experiment
#   internal_surface: exact validation helpers and fixed RC01-RC10 result construction
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact source witness, boundary manifestation, word occurrence, offsets, parentage, and initiation provenance remain linked without normalization
#   admin_only: false
#   tests: tests/test_initiation_boundary.py
#   rollout: explicit UCNS-only v0.13 partial-attachment experiment; no carrier selection, canonical faithful breadth, arbitrary-element assignment, full real-continuity theorem, EDCM activation, or METAPAT activation
#   rollback: remove this module, its exports, tests, and v0.13 document while retaining the v0.12 specification and all earlier evidence
#   requires: edcm_native_direct_mobius_candidate, edcm_exact_coordinate_representation_boundary
#   since: 2026-07-30
#   unresolved: arbitrary-real seam-side limits, intrinsic seam derivation, arbitrary-element transverse assignment, higher geometry, higher-gonol composition, scoped completion, and global carrier relationship
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: partial_initiation_structural_null_topology_is_explicit
#   given: a v0.13 initiation attachment is constructed
#   then: typed Structural Null remains a disjoint marked prestate connected to a non-null exact root only by the declared partial initiation relation
#   class: doctrine
#   since: 2026-07-30
#
# id: partial_initiation_seam_is_provenance_bearing
#   given: one source-linked initiation is represented under different numeric coordinate cuts
#   then: the marked seam and attachment identity retain the event, boundary manifestation, native source links, and parent observations while each numeric cut remains a nonauthoritative view
#   class: evidence
#   since: 2026-07-30
#
# id: partial_initiation_twist_receipt_is_source_bound
#   given: each minimum-packet word gonol initiates
#   then: exactly one twist receipt links its typed prestate, marked seam, exact source occurrence, native post-state, and exact root coordinate
#   class: correctness
#   since: 2026-07-30
#
# id: partial_initiation_motion_preserves_360_720_and_history
#   given: an attached root state advances by two successive visible turns
#   then: the versioned source-linked visible projection returns after one exact turn while complete local state changes, a second exact turn restores local state, and both endpoint-validated motion receipts remain appended
#   class: correctness
#   since: 2026-07-30
#
# id: partial_initiation_exact_quotient_compatibility
#   given: an exact rational signed-local coordinate enters the declared sheet involution
#   then: D maps B(u),t to B(-u),t+1 exactly and applying D twice restores the original coordinate
#   class: correctness
#   since: 2026-07-30
#
# id: partial_initiation_report_executes_rc_packet_without_selection
#   given: the v0.13 report is produced
#   then: RC01 through RC10 use canonical built-in payload and container types and the constructor-bound exact ComparisonPolicy over fixed complete result payloads and partial scope, while canonical attachment identities bind the trajectory to one retained report attachment and consumer activation remains absent
#   class: safety
#   since: 2026-07-30
# === END CONTRACTS ===

"""Partial Structural-Null initiation attachment for UCNS v0.13.

The v0.12 specification separates a smooth non-null coordinate component from
the missing topology that attaches Structural Null, a causal initiation seam,
exact source evidence, and motion history.  This module implements the smallest
honest attachment:

* Structural Null is an explicit disjoint typed prestate;
* each existing v0.6 initiation event owns a marked, provenance-bearing seam;
* one retained twist receipt connects that prestate to the exact v0.11 root
  coordinate and native Möbius root-loop state;
* motion appends source-linked receipts while preserving 360-degree change and
  720-degree local return; and
* RC01-RC10 are reported with the limits of the executable domain visible.

The relation is partial: it covers the complete nine-witness, fourteen-word
minimum packet at the root coordinate.  It does not assign arbitrary elements
to transverse coordinates, prove arbitrary-real seam limits, select a carrier
or breadth law, establish completion, or activate EDCM or METAPAT.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction

from .comparison import (
    ComparisonMode,
    ComparisonPolicy,
    exact_comparison_policy,
)
from .direct_mobius import (
    STRUCTURAL_NULL_ORIGIN,
    MobiusInitiationEvent,
    NativeMobiusFrame,
    NativeMobiusInitiationPacket,
    NativeMobiusState,
    StructuralNullIdentity,
    StructuralNullManifestation,
    build_native_mobius_initiation_packet,
)
from .exact_coordinate import (
    Binary64CollisionWitness,
    ExactCarrierCoordinate,
    binary64_collision_witnesses,
    signed_local_exact_coordinate,
)
from .mobius_experiment import FalsifierVerdict


V013_INITIATION_BOUNDARY_SCHEMA_ID = (
    "ucns.edcm.partial-initiation-boundary"
)
V013_INITIATION_BOUNDARY_SCHEMA_VERSION = "0.13.2"
V013_SELECTION_EFFECT = "none"

PARTIAL_INITIATION_SCOPE = (
    "minimum-source-packet-marked-seam-exact-rational-root-attachment"
)
PARTIAL_INITIATION_RELATION_ID = (
    "ucns.edcm.structural-null-to-root.partial-initiation"
)
PARTIAL_INITIATION_RELATION_VERSION = "0.13.0"
MARKED_SEAM_POLICY_ID = "ucns.edcm.marked-source-initiation-seam"
MARKED_SEAM_POLICY_VERSION = "0.13.0"
TWIST_RECEIPT_LAW_ID = "ucns.edcm.source-bound-root-twist-receipt"
TWIST_RECEIPT_LAW_VERSION = "0.13.0"
SEAM_COORDINATE_VIEW_STATUS = "nonauthoritative-coordinate-cut-view"
ROOT_VISIBLE_PROJECTION_ID = "ucns.edcm.root-visible-projection"
ROOT_VISIBLE_PROJECTION_VERSION = "0.13.1"
ROOT_VISIBLE_PROJECTION_INFORMATION_LOSS = (
    "native-local-frame",
    "whole-lifted-turn-count",
    "append-only-motion-history",
)
RC_COMPARISON_POLICY_NAME = "ucns.edcm.v013-rc-exact"
RC_COMPARISON_POLICY_VERSION = "0.13.2"
RC_COMPARISON_POLICY_CODE_REFERENCE = (
    "ucns.comparison:exact_comparison_policy"
)

RC_FALSIFIER_IDS = tuple(f"RC{index:02d}" for index in range(1, 11))
RC_EXPECTED_VERDICTS = (
    ("RC01", FalsifierVerdict.INCONCLUSIVE),
    ("RC02", FalsifierVerdict.SUPPORTED),
    ("RC03", FalsifierVerdict.INCONCLUSIVE),
    ("RC04", FalsifierVerdict.SUPPORTED),
    ("RC05", FalsifierVerdict.SUPPORTED),
    ("RC06", FalsifierVerdict.SUPPORTED),
    ("RC07", FalsifierVerdict.SUPPORTED),
    ("RC08", FalsifierVerdict.SUPPORTED),
    ("RC09", FalsifierVerdict.SUPPORTED),
    ("RC10", FalsifierVerdict.SUPPORTED),
)

V013_COORDINATE_COMPONENT_STATUS = (
    "exact-rational-quotient-compatible-candidate"
)
V013_SEAM_STATUS = "marked-provenance-bearing-on-minimum-packet"
V013_STRUCTURAL_NULL_TOPOLOGY_STATUS = (
    "explicit-disjoint-typed-prestate-with-partial-initiation-relation"
)
V013_COMPLETE_RELATIONSHIP_STATUS = (
    "inconclusive-partial-root-attachment-only"
)
V013_HMMM = (
    "arbitrary-real seam-side limits remain unimplemented",
    "intrinsic and invariant-equivalence-class seam alternatives remain unresolved",
    "arbitrary observed-element and transverse initiation assignment remains unresolved",
    "circle, epicycle, disk, sphere, recursive composition, and scoped completion remain unresolved",
    "the complete global carrier relationship remains inconclusive",
)


class InitiationBoundaryError(ValueError):
    """Raised when v0.13 evidence crosses its declared partial boundary."""


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise InitiationBoundaryError(f"{field} must be nonempty text")


def _require_fraction(value: Fraction, field: str) -> None:
    if not isinstance(value, Fraction):
        raise InitiationBoundaryError(f"{field} must be an exact Fraction")


def _require_exact_string_tuple_tree(value: object, field: str) -> None:
    """Reject equality-overloading values from authority-bearing identities."""

    if type(value) is str:
        return
    if type(value) is tuple:
        for item in value:
            _require_exact_string_tuple_tree(item, field)
        return
    raise InitiationBoundaryError(
        f"{field} must contain only exact built-in tuple and str values"
    )


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _normalize_turns(value: Fraction, period: Fraction) -> Fraction:
    _require_fraction(value, "turns")
    whole_periods = value // period
    return value - period * whole_periods


def partial_initiation_exact_comparison_policy() -> ComparisonPolicy:
    """Return the named exact policy pinned by the v0.13 RC packet."""

    return exact_comparison_policy(
        name=RC_COMPARISON_POLICY_NAME,
        version=RC_COMPARISON_POLICY_VERSION,
    )


def _validate_comparison_policy(policy: ComparisonPolicy) -> None:
    if not isinstance(policy, ComparisonPolicy):
        raise TypeError("comparison_policy must be ComparisonPolicy")
    if policy.name != RC_COMPARISON_POLICY_NAME:
        raise InitiationBoundaryError(
            "v0.13 comparison policy name is fixed"
        )
    if policy.version != RC_COMPARISON_POLICY_VERSION:
        raise InitiationBoundaryError(
            "v0.13 comparison policy version is fixed"
        )
    if policy.mode is not ComparisonMode.EXACT:
        raise InitiationBoundaryError(
            "v0.13 comparison policy must be exact"
        )
    if policy.code_reference != RC_COMPARISON_POLICY_CODE_REFERENCE:
        raise InitiationBoundaryError(
            "v0.13 comparison implementation reference is fixed"
        )


class StructuralNullTopologyKind(str, Enum):
    """Explicit v0.13 topology for the pre-initiation state."""

    DISJOINT_MARKED_PRESTATE = (
        "disjoint-marked-prestate-with-partial-initiation-relation"
    )


@dataclass(frozen=True, slots=True)
class MarkedInitiationSeam:
    """One source-provenance seam; no numeric angle is authoritative."""

    seam_id: str
    event_id: str
    witness_id: str
    word_index: int
    source_start: int
    manifestation: StructuralNullManifestation
    topology: StructuralNullTopologyKind = (
        StructuralNullTopologyKind.DISJOINT_MARKED_PRESTATE
    )
    policy_id: str = MARKED_SEAM_POLICY_ID
    policy_version: str = MARKED_SEAM_POLICY_VERSION
    selection_effect: str = V013_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.seam_id, "seam_id")
        _require_text(self.event_id, "event_id")
        _require_text(self.witness_id, "witness_id")
        if self.word_index < 0:
            raise InitiationBoundaryError("word_index must be nonnegative")
        if self.source_start < 0:
            raise InitiationBoundaryError("source_start must be nonnegative")
        if self.manifestation.witness_id != self.witness_id:
            raise InitiationBoundaryError(
                "marked seam must retain its source witness"
            )
        if self.manifestation.origin is not STRUCTURAL_NULL_ORIGIN:
            raise InitiationBoundaryError(
                "marked seam must reference the singular Structural Null"
            )
        if self.seam_id != f"{self.event_id}:marked-seam":
            raise InitiationBoundaryError(
                "marked seam identity must derive from its initiation event"
            )
        if self.topology is not (
            StructuralNullTopologyKind.DISJOINT_MARKED_PRESTATE
        ):
            raise InitiationBoundaryError(
                "v0.13 Structural Null topology is fixed"
            )
        if (
            self.policy_id != MARKED_SEAM_POLICY_ID
            or self.policy_version != MARKED_SEAM_POLICY_VERSION
        ):
            raise InitiationBoundaryError("marked seam policy is fixed")
        if self.selection_effect != V013_SELECTION_EFFECT:
            raise InitiationBoundaryError(
                "marked seam cannot select a carrier"
            )

    @property
    def evidence_identity(self) -> tuple[str, ...]:
        return (
            self.seam_id,
            self.event_id,
            self.witness_id,
            str(self.word_index),
            str(self.source_start),
            self.manifestation.manifestation_id,
            self.manifestation.source_reference,
            self.topology.value,
            f"{self.policy_id}@{self.policy_version}",
        )


@dataclass(frozen=True, slots=True)
class SeamCoordinateView:
    """A movable numeric cut linked to, but never defining, a marked seam."""

    seam: MarkedInitiationSeam
    coordinate_cut_turns: Fraction
    status: str = SEAM_COORDINATE_VIEW_STATUS

    def __post_init__(self) -> None:
        if not isinstance(self.seam, MarkedInitiationSeam):
            raise InitiationBoundaryError(
                "coordinate view requires a marked seam"
            )
        _require_fraction(self.coordinate_cut_turns, "coordinate_cut_turns")
        if not Fraction(0) <= self.coordinate_cut_turns < Fraction(1):
            raise InitiationBoundaryError(
                "coordinate cut must be normalized to [0, 1)"
            )
        if self.status != SEAM_COORDINATE_VIEW_STATUS:
            raise InitiationBoundaryError(
                "numeric seam view must remain nonauthoritative"
            )

    @property
    def structural_seam_identity(self) -> tuple[str, ...]:
        return self.seam.evidence_identity


def view_marked_seam_at_cut(
    seam: MarkedInitiationSeam,
    coordinate_cut_turns: Fraction,
) -> SeamCoordinateView:
    """Return a movable numeric view without changing retained seam identity."""

    if not isinstance(seam, MarkedInitiationSeam):
        raise TypeError("seam must be MarkedInitiationSeam")
    _require_fraction(coordinate_cut_turns, "coordinate_cut_turns")
    return SeamCoordinateView(
        seam=seam,
        coordinate_cut_turns=_normalize_turns(
            coordinate_cut_turns,
            Fraction(1),
        ),
    )


@dataclass(frozen=True, slots=True)
class TwistReceipt:
    """Source-bound evidence for one transition out of Structural Null."""

    receipt_id: str
    event: MobiusInitiationEvent
    seam: MarkedInitiationSeam
    pre_state: StructuralNullIdentity
    post_native_state: NativeMobiusState
    post_coordinate: ExactCarrierCoordinate
    source_links: tuple[str, ...]
    relation_id: str = PARTIAL_INITIATION_RELATION_ID
    relation_version: str = PARTIAL_INITIATION_RELATION_VERSION
    law_id: str = TWIST_RECEIPT_LAW_ID
    law_version: str = TWIST_RECEIPT_LAW_VERSION
    scope: str = PARTIAL_INITIATION_SCOPE
    selection_effect: str = V013_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.receipt_id, "receipt_id")
        if self.pre_state is not STRUCTURAL_NULL_ORIGIN:
            raise InitiationBoundaryError(
                "twist receipt prestate must be typed Structural Null"
            )
        if self.event.event_id != self.seam.event_id:
            raise InitiationBoundaryError(
                "twist receipt seam and event must agree"
            )
        if self.event.boundary is not self.seam.manifestation:
            raise InitiationBoundaryError(
                "twist receipt must retain the exact causal manifestation"
            )
        if self.post_native_state != self.event.post_state:
            raise InitiationBoundaryError(
                "twist receipt must retain the event native post-state"
            )
        if self.post_native_state.phase_turns != 0 or (
            self.post_native_state.frame is not NativeMobiusFrame.POSITIVE
        ):
            raise InitiationBoundaryError(
                "twist receipt must begin at the positive native root"
            )
        if (
            self.post_coordinate.local_transverse != 0
            or self.post_coordinate.breadth != 1
            or self.post_coordinate.lifted_turns != 0
        ):
            raise InitiationBoundaryError(
                "partial initiation attaches only to the exact root coordinate"
            )
        if not self.source_links:
            raise InitiationBoundaryError(
                "twist receipt must retain source links"
            )
        if self.receipt_id != f"{self.event.event_id}:twist-receipt":
            raise InitiationBoundaryError(
                "twist receipt identity must derive from its initiation event"
            )
        if self.source_links != self.event.post_state.source_links + (
            f"seam:{self.seam.seam_id}",
        ):
            raise InitiationBoundaryError(
                "twist receipt must retain exact event links and its marked seam"
            )
        if (
            self.relation_id != PARTIAL_INITIATION_RELATION_ID
            or self.relation_version != PARTIAL_INITIATION_RELATION_VERSION
            or self.law_id != TWIST_RECEIPT_LAW_ID
            or self.law_version != TWIST_RECEIPT_LAW_VERSION
        ):
            raise InitiationBoundaryError(
                "partial initiation relation and twist law are fixed"
            )
        if self.scope != PARTIAL_INITIATION_SCOPE:
            raise InitiationBoundaryError(
                "partial initiation scope is fixed"
            )
        if self.selection_effect != V013_SELECTION_EFFECT:
            raise InitiationBoundaryError(
                "twist receipt cannot select a carrier"
            )


@dataclass(frozen=True, slots=True)
class PartialInitiationAttachment:
    """One declared edge from typed prestate to exact non-null root state."""

    event: MobiusInitiationEvent
    seam: MarkedInitiationSeam
    twist_receipt: TwistReceipt

    def __post_init__(self) -> None:
        if self.event.event_id != self.seam.event_id:
            raise InitiationBoundaryError(
                "attachment event and seam must agree"
            )
        if (
            self.event.witness_id != self.seam.witness_id
            or self.event.word_index != self.seam.word_index
            or self.event.source_start != self.seam.source_start
            or self.event.boundary is not self.seam.manifestation
        ):
            raise InitiationBoundaryError(
                "attachment seam must retain exact event provenance"
            )
        if self.twist_receipt.event is not self.event:
            raise InitiationBoundaryError(
                "attachment must retain one exact event object"
            )
        if self.twist_receipt.seam is not self.seam:
            raise InitiationBoundaryError(
                "attachment must retain one exact seam object"
            )

    @property
    def attachment_identity(self) -> tuple[object, ...]:
        native_state = self.twist_receipt.post_native_state
        return (
            self.event.event_id,
            self.seam.evidence_identity,
            self.twist_receipt.receipt_id,
            self.twist_receipt.post_coordinate.exact_identity,
            ("native-source-links", native_state.source_links),
            (
                "native-parent-observation-ids",
                native_state.parent_observation_ids,
            ),
            ("native-completion-scope", native_state.completion_scope),
            ("native-initiation-event-id", native_state.initiation_event_id),
        )


def build_partial_initiation_attachments(
    packet: NativeMobiusInitiationPacket | None = None,
) -> tuple[PartialInitiationAttachment, ...]:
    """Attach every v0.6 initiation to the exact v0.11 root coordinate."""

    if packet is None:
        packet = build_native_mobius_initiation_packet()
    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")

    attachments: list[PartialInitiationAttachment] = []
    for event in packet.initiations:
        seam = MarkedInitiationSeam(
            seam_id=f"{event.event_id}:marked-seam",
            event_id=event.event_id,
            witness_id=event.witness_id,
            word_index=event.word_index,
            source_start=event.source_start,
            manifestation=event.boundary,
        )
        coordinate = signed_local_exact_coordinate(
            Fraction(0),
            Fraction(0),
        )
        receipt = TwistReceipt(
            receipt_id=f"{event.event_id}:twist-receipt",
            event=event,
            seam=seam,
            pre_state=STRUCTURAL_NULL_ORIGIN,
            post_native_state=event.post_state,
            post_coordinate=coordinate,
            source_links=event.post_state.source_links
            + (f"seam:{seam.seam_id}",),
        )
        attachments.append(
            PartialInitiationAttachment(
                event=event,
                seam=seam,
                twist_receipt=receipt,
            )
        )
    return tuple(attachments)


@dataclass(frozen=True, slots=True)
class CarrierMotionReceipt:
    """One append-only exact motion step linked to an initiation attachment."""

    step_index: int
    motion_turns: Fraction
    attachment_id: tuple[object, ...]
    before_native_key: tuple[tuple[str, str], ...]
    after_native_key: tuple[tuple[str, str], ...]
    before_coordinate_identity: tuple[tuple[str, str], ...]
    after_coordinate_identity: tuple[tuple[str, str], ...]

    def __post_init__(self) -> None:
        if self.step_index < 0:
            raise InitiationBoundaryError(
                "motion receipt step_index must be nonnegative"
            )
        _require_fraction(self.motion_turns, "motion_turns")
        if self.motion_turns == 0:
            raise InitiationBoundaryError(
                "motion receipt must retain a nonzero displacement"
            )
        if not self.attachment_id:
            raise InitiationBoundaryError(
                "motion receipt must link its initiation attachment"
            )
        for value, field in (
            (self.before_native_key, "before_native_key"),
            (self.after_native_key, "after_native_key"),
            (self.before_coordinate_identity, "before_coordinate_identity"),
            (self.after_coordinate_identity, "after_coordinate_identity"),
        ):
            if not value:
                raise InitiationBoundaryError(
                    f"{field} must retain complete state evidence"
                )


@dataclass(frozen=True, slots=True)
class RootVisibleProjection:
    """Versioned source-linked visible view used only by RC04."""

    attachment_identity: tuple[object, ...]
    source_links: tuple[str, ...]
    parent_observation_ids: tuple[str, ...]
    source_candidate_id: str
    local_transverse: Fraction
    breadth: Fraction
    visible_turns: Fraction
    projection_id: str = ROOT_VISIBLE_PROJECTION_ID
    projection_version: str = ROOT_VISIBLE_PROJECTION_VERSION
    information_loss: tuple[str, ...] = (
        ROOT_VISIBLE_PROJECTION_INFORMATION_LOSS
    )

    def __post_init__(self) -> None:
        if not self.attachment_identity:
            raise InitiationBoundaryError(
                "visible projection must retain its attachment identity"
            )
        if not self.source_links or any(
            not item.strip() for item in self.source_links
        ):
            raise InitiationBoundaryError(
                "visible projection must retain native source links"
            )
        if any(not item.strip() for item in self.parent_observation_ids):
            raise InitiationBoundaryError(
                "visible projection parent observations must be nonempty"
            )
        _require_text(self.source_candidate_id, "source_candidate_id")
        _require_fraction(self.local_transverse, "local_transverse")
        _require_fraction(self.breadth, "breadth")
        _require_fraction(self.visible_turns, "visible_turns")
        if not Fraction(0) <= self.visible_turns < Fraction(1):
            raise InitiationBoundaryError(
                "visible projection turns must be normalized to [0, 1)"
            )
        if (
            self.projection_id != ROOT_VISIBLE_PROJECTION_ID
            or self.projection_version != ROOT_VISIBLE_PROJECTION_VERSION
        ):
            raise InitiationBoundaryError(
                "RC04 visible projection identity is fixed"
            )
        if self.information_loss != ROOT_VISIBLE_PROJECTION_INFORMATION_LOSS:
            raise InitiationBoundaryError(
                "RC04 visible projection loss declaration is fixed"
            )


@dataclass(frozen=True, slots=True)
class InitiatedCarrierState:
    """Exact root state plus append-only trajectory evidence."""

    attachment: PartialInitiationAttachment
    native_state: NativeMobiusState
    coordinate: ExactCarrierCoordinate
    motion_history: tuple[CarrierMotionReceipt, ...] = ()

    def __post_init__(self) -> None:
        if self.native_state.initiation_event_id != self.attachment.event.event_id:
            raise InitiationBoundaryError(
                "carrier state must retain its initiation event"
            )
        if self.coordinate.local_transverse != 0 or self.coordinate.breadth != 1:
            raise InitiationBoundaryError(
                "v0.13 initiated state remains on the exact root fiber"
            )
        if (
            self.coordinate.lifted_turns % 1
            != self.native_state.phase_turns
        ):
            raise InitiationBoundaryError(
                "native and exact-coordinate visible phases must agree"
            )
        expected_frame = (
            NativeMobiusFrame.POSITIVE
            if self.coordinate.lifted_turns < 1
            else NativeMobiusFrame.REVERSED
        )
        if self.native_state.frame is not expected_frame:
            raise InitiationBoundaryError(
                "native frame must agree with the exact lifted representative"
            )
        expected_native = self.attachment.twist_receipt.post_native_state
        expected_coordinate = self.attachment.twist_receipt.post_coordinate
        for expected_index, receipt in enumerate(self.motion_history):
            if receipt.step_index != expected_index:
                raise InitiationBoundaryError(
                    "motion receipts must retain contiguous append order"
                )
            if receipt.attachment_id != self.attachment.attachment_identity:
                raise InitiationBoundaryError(
                    "motion receipt must retain the same initiation attachment"
                )
            if (
                receipt.before_native_key != expected_native.complete_key
                or receipt.before_coordinate_identity
                != expected_coordinate.exact_identity
            ):
                raise InitiationBoundaryError(
                    "motion receipt before endpoint must match its trajectory"
                )
            expected_native = expected_native.advance(
                receipt.motion_turns
            )
            expected_coordinate = signed_local_exact_coordinate(
                expected_coordinate.local_transverse,
                expected_coordinate.lifted_turns + receipt.motion_turns,
            )
            if (
                receipt.after_native_key != expected_native.complete_key
                or receipt.after_coordinate_identity
                != expected_coordinate.exact_identity
            ):
                raise InitiationBoundaryError(
                    "motion receipt after endpoint must match its trajectory"
                )
        if (
            self.native_state != expected_native
            or self.coordinate != expected_coordinate
        ):
            raise InitiationBoundaryError(
                "carrier state must equal its complete motion trajectory endpoint"
            )

    @property
    def visible_identity(self) -> RootVisibleProjection:
        """Return the exact named projection used by RC04."""

        return project_root_visible_state(self)

    @property
    def complete_local_identity(self) -> tuple[object, ...]:
        return (
            self.coordinate.exact_identity,
            self.native_state.complete_key,
        )


def project_root_visible_state(
    state: InitiatedCarrierState,
) -> RootVisibleProjection:
    """Project one root state while retaining its exact source-evidence link."""

    if not isinstance(state, InitiatedCarrierState):
        raise TypeError("state must be InitiatedCarrierState")
    native_origin = state.attachment.twist_receipt.post_native_state
    return RootVisibleProjection(
        attachment_identity=state.attachment.attachment_identity,
        source_links=native_origin.source_links,
        parent_observation_ids=native_origin.parent_observation_ids,
        source_candidate_id=state.coordinate.provenance.source_candidate_id,
        local_transverse=state.coordinate.local_transverse,
        breadth=state.coordinate.breadth,
        visible_turns=state.coordinate.lifted_turns % 1,
    )


def initiate_carrier_state(
    attachment: PartialInitiationAttachment,
) -> InitiatedCarrierState:
    """Materialize the exact non-null post-state of one partial attachment."""

    if not isinstance(attachment, PartialInitiationAttachment):
        raise TypeError("attachment must be PartialInitiationAttachment")
    return InitiatedCarrierState(
        attachment=attachment,
        native_state=attachment.twist_receipt.post_native_state,
        coordinate=attachment.twist_receipt.post_coordinate,
    )


def advance_attached_state(
    state: InitiatedCarrierState,
    turns: Fraction | int,
) -> InitiatedCarrierState:
    """Advance exact root state and append one non-erasing motion receipt."""

    if not isinstance(state, InitiatedCarrierState):
        raise TypeError("state must be InitiatedCarrierState")
    if isinstance(turns, bool):
        raise InitiationBoundaryError("motion turns cannot be boolean")
    if isinstance(turns, int):
        turns = Fraction(turns)
    _require_fraction(turns, "turns")
    if turns == 0:
        raise InitiationBoundaryError("motion turns must be nonzero")

    native_after = state.native_state.advance(turns)
    coordinate_after = signed_local_exact_coordinate(
        state.coordinate.local_transverse,
        state.coordinate.lifted_turns + turns,
    )
    receipt = CarrierMotionReceipt(
        step_index=len(state.motion_history),
        motion_turns=turns,
        attachment_id=state.attachment.attachment_identity,
        before_native_key=state.native_state.complete_key,
        after_native_key=native_after.complete_key,
        before_coordinate_identity=state.coordinate.exact_identity,
        after_coordinate_identity=coordinate_after.exact_identity,
    )
    return InitiatedCarrierState(
        attachment=state.attachment,
        native_state=native_after,
        coordinate=coordinate_after,
        motion_history=state.motion_history + (receipt,),
    )


def exact_sheet_involution(
    coordinate: ExactCarrierCoordinate,
) -> ExactCarrierCoordinate:
    """Apply exact ``D(B(u), t) = (B(-u), t+1)``."""

    if not isinstance(coordinate, ExactCarrierCoordinate):
        raise TypeError("coordinate must be ExactCarrierCoordinate")
    return signed_local_exact_coordinate(
        -coordinate.local_transverse,
        coordinate.lifted_turns + Fraction(1),
    )


@dataclass(frozen=True, slots=True)
class ContinuityFalsifierResult:
    """One RC01-RC10 verdict with declared executable scope and limitation."""

    falsifier_id: str
    verdict: FalsifierVerdict
    scope: str
    evidence: tuple[str, ...]
    limitation: str

    def __post_init__(self) -> None:
        if type(self.falsifier_id) is not str:
            raise InitiationBoundaryError(
                "continuity falsifier id must be exact built-in str"
            )
        if self.falsifier_id not in RC_FALSIFIER_IDS:
            raise InitiationBoundaryError(
                "unknown continuity falsifier id"
            )
        if type(self.verdict) is not FalsifierVerdict:
            raise InitiationBoundaryError(
                "continuity verdict must be an exact FalsifierVerdict"
            )
        if type(self.scope) is not str:
            raise InitiationBoundaryError(
                "continuity scope must be exact built-in str"
            )
        _require_text(self.scope, "scope")
        if type(self.evidence) is not tuple or any(
            type(item) is not str for item in self.evidence
        ):
            raise InitiationBoundaryError(
                "continuity evidence must be an exact tuple of built-in str values"
            )
        if not self.evidence or any(not item.strip() for item in self.evidence):
            raise InitiationBoundaryError(
                "continuity falsifier must retain evidence"
            )
        if type(self.limitation) is not str:
            raise InitiationBoundaryError(
                "continuity limitation must be exact built-in str"
            )
        _require_text(self.limitation, "limitation")


@dataclass(frozen=True, slots=True)
class PartialInitiationBoundaryReport:
    """Complete bounded v0.13 attachment and RC01-RC10 evidence packet."""

    attachments: tuple[PartialInitiationAttachment, ...]
    trajectory: tuple[InitiatedCarrierState, ...]
    sheet_witness: tuple[ExactCarrierCoordinate, ExactCarrierCoordinate]
    seam_views: tuple[SeamCoordinateView, SeamCoordinateView]
    binary64_witnesses: tuple[Binary64CollisionWitness, ...]
    results: tuple[ContinuityFalsifierResult, ...]
    comparison_policy: ComparisonPolicy = field(
        default_factory=partial_initiation_exact_comparison_policy,
        init=False,
        repr=False,
        compare=False,
    )
    schema_id: str = V013_INITIATION_BOUNDARY_SCHEMA_ID
    schema_version: str = V013_INITIATION_BOUNDARY_SCHEMA_VERSION
    coordinate_component_status: str = V013_COORDINATE_COMPONENT_STATUS
    seam_status: str = V013_SEAM_STATUS
    structural_null_topology_status: str = (
        V013_STRUCTURAL_NULL_TOPOLOGY_STATUS
    )
    complete_relationship_status: str = V013_COMPLETE_RELATIONSHIP_STATUS
    selection_effect: str = V013_SELECTION_EFFECT
    edcm_activation: str = "inactive"
    metapat_activation: str = "inactive"
    hmmm: tuple[str, ...] = V013_HMMM

    def __post_init__(self) -> None:
        policy = partial_initiation_exact_comparison_policy()
        object.__setattr__(self, "comparison_policy", policy)
        _validate_comparison_policy(policy)
        if type(self.results) is not tuple or any(
            type(item) is not ContinuityFalsifierResult
            for item in self.results
        ):
            raise InitiationBoundaryError(
                "v0.13 results must be an exact tuple of "
                "ContinuityFalsifierResult values"
            )
        if (
            self.schema_id != V013_INITIATION_BOUNDARY_SCHEMA_ID
            or self.schema_version != V013_INITIATION_BOUNDARY_SCHEMA_VERSION
        ):
            raise InitiationBoundaryError("v0.13 schema identity mismatch")
        if type(self.attachments) is not tuple or any(
            type(item) is not PartialInitiationAttachment
            for item in self.attachments
        ):
            raise InitiationBoundaryError(
                "v0.13 attachments must be an exact tuple of "
                "PartialInitiationAttachment values"
            )
        retained_attachment_identities = tuple(
            item.attachment_identity for item in self.attachments
        )
        for identity in retained_attachment_identities:
            _require_exact_string_tuple_tree(
                identity,
                "v0.13 attachment identities",
            )
        if len(self.attachments) != 14:
            raise InitiationBoundaryError(
                "v0.13 must retain all fourteen minimum-packet initiations"
            )
        if len({item.event.event_id for item in self.attachments}) != 14:
            raise InitiationBoundaryError(
                "v0.13 initiation event identities must be unique"
            )
        expected_attachments = tuple(
            item.attachment_identity
            for item in build_partial_initiation_attachments()
        )
        if tuple(
            item.attachment_identity for item in self.attachments
        ) != expected_attachments:
            raise InitiationBoundaryError(
                "v0.13 must retain the fixed minimum-packet attachments"
            )
        if type(self.trajectory) is not tuple or any(
            type(item) is not InitiatedCarrierState
            for item in self.trajectory
        ):
            raise InitiationBoundaryError(
                "v0.13 trajectory must be an exact tuple of "
                "InitiatedCarrierState values"
            )
        if len(self.trajectory) != 3:
            raise InitiationBoundaryError(
                "v0.13 trajectory must retain initial, 360, and 720 states"
            )
        initial, after_360, after_720 = self.trajectory
        if initial.motion_history:
            raise InitiationBoundaryError(
                "initial trajectory state cannot contain motion receipts"
            )
        if len(after_360.motion_history) != 1:
            raise InitiationBoundaryError(
                "360 state must retain one motion receipt"
            )
        if len(after_720.motion_history) != 2:
            raise InitiationBoundaryError(
                "720 state must retain both motion receipts"
            )
        if (
            after_360.motion_history[0].motion_turns != Fraction(1)
            or after_720.motion_history[0].motion_turns != Fraction(1)
            or after_720.motion_history[1].motion_turns != Fraction(1)
        ):
            raise InitiationBoundaryError(
                "360 and 720 trajectory receipts must each advance one exact turn"
            )
        attachment_identities = tuple(
            item.attachment.attachment_identity for item in self.trajectory
        )
        for identity in attachment_identities:
            _require_exact_string_tuple_tree(
                identity,
                "v0.13 attachment identities",
            )
        if not (
            policy.matches(attachment_identities[0], attachment_identities[1])
            and policy.matches(
                attachment_identities[1],
                attachment_identities[2],
            )
        ):
            raise InitiationBoundaryError(
                "all trajectory states must retain one initiation attachment"
            )
        if not any(
            policy.matches(attachment_identities[0], retained_identity)
            for retained_identity in retained_attachment_identities
        ):
            raise InitiationBoundaryError(
                "trajectory must use one retained report attachment"
            )
        if not policy.matches(
            after_360.motion_history,
            after_720.motion_history[:1],
        ):
            raise InitiationBoundaryError(
                "trajectory histories must extend without replacement"
            )
        if not policy.matches(
            initial.visible_identity,
            after_360.visible_identity,
        ):
            raise InitiationBoundaryError(
                "360 motion must restore visible position"
            )
        if policy.matches(
            initial.complete_local_identity,
            after_360.complete_local_identity,
        ):
            raise InitiationBoundaryError(
                "360 motion must change complete local state"
            )
        if not policy.matches(
            initial.complete_local_identity,
            after_720.complete_local_identity,
        ):
            raise InitiationBoundaryError(
                "720 motion must restore complete local state"
            )
        first_sheet, second_sheet = self.sheet_witness
        if not policy.matches(
            exact_sheet_involution(first_sheet),
            second_sheet,
        ):
            raise InitiationBoundaryError(
                "sheet witness must satisfy exact quotient compatibility"
            )
        if not policy.matches(
            exact_sheet_involution(second_sheet),
            first_sheet,
        ):
            raise InitiationBoundaryError(
                "sheet involution must square to identity"
            )
        first_view, second_view = self.seam_views
        if not policy.matches(
            first_view.structural_seam_identity,
            second_view.structural_seam_identity,
        ):
            raise InitiationBoundaryError(
                "numeric cut movement cannot change marked seam identity"
            )
        if policy.matches(
            first_view.coordinate_cut_turns,
            second_view.coordinate_cut_turns,
        ):
            raise InitiationBoundaryError(
                "seam-cut witness requires distinct numeric views"
            )
        if not policy.matches(
            tuple(
                item.evidence_identity for item in self.binary64_witnesses
            ),
            tuple(
                item.evidence_identity
                for item in binary64_collision_witnesses()
            ),
        ):
            raise InitiationBoundaryError(
                "v0.13 must retain both fixed binary64 collision witnesses"
            )
        if tuple(item.falsifier_id for item in self.results) != RC_FALSIFIER_IDS:
            raise InitiationBoundaryError(
                "v0.13 must report RC01 through RC10 in order"
            )
        if any(
            item.scope != PARTIAL_INITIATION_SCOPE
            for item in self.results
        ):
            raise InitiationBoundaryError(
                "every v0.13 RC result must retain the partial initiation scope"
            )
        if not policy.matches(
            tuple(
                (item.falsifier_id, item.verdict)
                for item in self.results
            ),
            RC_EXPECTED_VERDICTS,
        ):
            raise InitiationBoundaryError(
                "v0.13 RC verdict map is fixed and cannot promote an inconclusive result"
            )
        if not policy.matches(
            self.results,
            _expected_continuity_results(),
        ):
            raise InitiationBoundaryError(
                "v0.13 RC result payload is fixed and cannot be reconstructed"
            )
        if (
            self.coordinate_component_status
            != V013_COORDINATE_COMPONENT_STATUS
            or self.seam_status != V013_SEAM_STATUS
            or self.structural_null_topology_status
            != V013_STRUCTURAL_NULL_TOPOLOGY_STATUS
            or self.complete_relationship_status
            != V013_COMPLETE_RELATIONSHIP_STATUS
        ):
            raise InitiationBoundaryError(
                "v0.13 boundary statuses are fixed"
            )
        if self.selection_effect != V013_SELECTION_EFFECT:
            raise InitiationBoundaryError("v0.13 cannot select a carrier")
        if self.edcm_activation != "inactive":
            raise InitiationBoundaryError("v0.13 cannot activate EDCM")
        if self.metapat_activation != "inactive":
            raise InitiationBoundaryError("v0.13 cannot activate METAPAT")
        if self.hmmm != V013_HMMM:
            raise InitiationBoundaryError(
                "v0.13 unresolved boundary is fixed"
            )

    def result(self, falsifier_id: str) -> ContinuityFalsifierResult:
        """Return one fixed RC result or fail closed."""

        for item in self.results:
            if item.falsifier_id == falsifier_id:
                return item
        raise InitiationBoundaryError(
            f"unknown continuity falsifier: {falsifier_id}"
        )


def _rc_result(
    falsifier_id: str,
    verdict: FalsifierVerdict,
    evidence: tuple[str, ...],
    limitation: str,
) -> ContinuityFalsifierResult:
    return ContinuityFalsifierResult(
        falsifier_id=falsifier_id,
        verdict=verdict,
        scope=PARTIAL_INITIATION_SCOPE,
        evidence=evidence,
        limitation=limitation,
    )


def _expected_continuity_results(
) -> tuple[ContinuityFalsifierResult, ...]:
    """Build the complete fixed RC01-RC10 payload from canonical evidence."""

    packet = build_native_mobius_initiation_packet()
    attachments = build_partial_initiation_attachments(packet)
    initial = initiate_carrier_state(attachments[0])
    after_360 = advance_attached_state(initial, 1)
    after_720 = advance_attached_state(after_360, 1)
    sheet_first = signed_local_exact_coordinate(
        Fraction(1, 3),
        Fraction(2, 5),
    )
    sheet_second = exact_sheet_involution(sheet_first)
    source_reconstruction = all(
        "".join(segment.raw_text for segment in witness.turn.segments)
        == witness.turn.raw_text
        for witness in packet.witnesses
    )
    exact_order = tuple(
        item.event.event_id for item in attachments
    ) == tuple(item.event_id for item in packet.initiations)

    return (
        _rc_result(
            "RC01",
            FalsifierVerdict.INCONCLUSIVE,
            (
                "exact-rational-affine-inverse:u=2*(B-1)",
                "real-analytic-formula-recorded-by-v0.12",
            ),
            "the runtime admits exact rationals, not arbitrary real values or a machine proof of real continuity",
        ),
        _rc_result(
            "RC02",
            FalsifierVerdict.SUPPORTED,
            (
                f"input:{sheet_first.exact_identity}",
                f"sheet-image:{sheet_second.exact_identity}",
                "D-squared:exact-identity",
            ),
            "support is exact on the declared rational coordinate domain and does not establish a selected global chart",
        ),
        _rc_result(
            "RC03",
            FalsifierVerdict.INCONCLUSIVE,
            (
                "marked-seam-coordinate-cut-independent:true",
                "arbitrary-real-side-limits:not-represented",
            ),
            "movable-cut independence is executable, but arbitrary-real seam-side limit commutation is not",
        ),
        _rc_result(
            "RC04",
            FalsifierVerdict.SUPPORTED,
            (
                f"visible-projection:{ROOT_VISIBLE_PROJECTION_ID}@{ROOT_VISIBLE_PROJECTION_VERSION}",
                "visible-after-360:equal",
                "complete-local-after-360:changed",
                "retained-change:native-frame-and-lifted-representative",
                "projection-loss:native-frame,whole-lifted-turn-count,motion-history",
            ),
            "support is bounded to the source-linked exact root attachment",
        ),
        _rc_result(
            "RC05",
            FalsifierVerdict.SUPPORTED,
            (
                "complete-local-after-720:equal",
                f"motion-receipts:{len(after_720.motion_history)}",
                "history-erasure:false",
            ),
            "local return is not promoted to scoped construction completion",
        ),
        _rc_result(
            "RC06",
            FalsifierVerdict.SUPPORTED,
            (
                f"marked-seams:{len(attachments)}",
                "numeric-cut-authority:none",
                "coordinate-cut-shift-preserves-seam:true",
            ),
            "the marked-seam candidate is supported; intrinsic and invariant-class alternatives remain unresolved",
        ),
        _rc_result(
            "RC07",
            FalsifierVerdict.SUPPORTED,
            (
                f"topology:{StructuralNullTopologyKind.DISJOINT_MARKED_PRESTATE.value}",
                f"partial-initiation-edges:{len(attachments)}",
                f"relation:{PARTIAL_INITIATION_RELATION_ID}@{PARTIAL_INITIATION_RELATION_VERSION}",
            ),
            "the attachment is partial and root-only, not a general arbitrary-element relation",
        ),
        _rc_result(
            "RC08",
            (
                FalsifierVerdict.SUPPORTED
                if source_reconstruction and exact_order
                else FalsifierVerdict.FALSIFIED
            ),
            (
                f"source-witnesses:{len(packet.witnesses)}",
                f"source-linked-initiations:{len(attachments)}",
                f"exact-reconstruction:{str(source_reconstruction).lower()}",
                f"exact-initiation-order:{str(exact_order).lower()}",
            ),
            "support covers the complete fixed minimum packet, not a full real-system corpus",
        ),
        _rc_result(
            "RC09",
            FalsifierVerdict.SUPPORTED,
            (
                f"binary64-collision-witnesses:{len(binary64_collision_witnesses())}",
                "binary64-role:lossy-nonauthoritative-rendering",
            ),
            "the exact coordinate remains rational evidence; no arbitrary-real machine representation is supplied",
        ),
        _rc_result(
            "RC10",
            FalsifierVerdict.SUPPORTED,
            (
                "carrier-selection:none",
                "canonical-B-selection:none",
                "EDCM-activation:inactive",
                "METAPAT-activation:inactive",
            ),
            "v0.13 adds experiment evidence only",
        ),
    )


def run_v013_partial_initiation_boundary_experiment(
) -> PartialInitiationBoundaryReport:
    """Build the complete fixed v0.13 attachment and RC evidence packet."""

    packet = build_native_mobius_initiation_packet()
    attachments = build_partial_initiation_attachments(packet)
    initial = initiate_carrier_state(attachments[0])
    after_360 = advance_attached_state(initial, 1)
    after_720 = advance_attached_state(after_360, 1)

    sheet_first = signed_local_exact_coordinate(
        Fraction(1, 3),
        Fraction(2, 5),
    )
    sheet_second = exact_sheet_involution(sheet_first)

    seam_first = view_marked_seam_at_cut(
        attachments[0].seam,
        Fraction(0),
    )
    seam_second = view_marked_seam_at_cut(
        attachments[0].seam,
        Fraction(1, 3),
    )

    results = _expected_continuity_results()

    return PartialInitiationBoundaryReport(
        attachments=attachments,
        trajectory=(initial, after_360, after_720),
        sheet_witness=(sheet_first, sheet_second),
        seam_views=(seam_first, seam_second),
        binary64_witnesses=binary64_collision_witnesses(),
        results=results,
    )


__all__ = [
    "MARKED_SEAM_POLICY_ID",
    "MARKED_SEAM_POLICY_VERSION",
    "PARTIAL_INITIATION_RELATION_ID",
    "PARTIAL_INITIATION_RELATION_VERSION",
    "PARTIAL_INITIATION_SCOPE",
    "RC_COMPARISON_POLICY_CODE_REFERENCE",
    "RC_COMPARISON_POLICY_NAME",
    "RC_COMPARISON_POLICY_VERSION",
    "RC_EXPECTED_VERDICTS",
    "RC_FALSIFIER_IDS",
    "ROOT_VISIBLE_PROJECTION_ID",
    "ROOT_VISIBLE_PROJECTION_INFORMATION_LOSS",
    "ROOT_VISIBLE_PROJECTION_VERSION",
    "SEAM_COORDINATE_VIEW_STATUS",
    "TWIST_RECEIPT_LAW_ID",
    "TWIST_RECEIPT_LAW_VERSION",
    "V013_COMPLETE_RELATIONSHIP_STATUS",
    "V013_COORDINATE_COMPONENT_STATUS",
    "V013_HMMM",
    "V013_INITIATION_BOUNDARY_SCHEMA_ID",
    "V013_INITIATION_BOUNDARY_SCHEMA_VERSION",
    "V013_SEAM_STATUS",
    "V013_SELECTION_EFFECT",
    "V013_STRUCTURAL_NULL_TOPOLOGY_STATUS",
    "CarrierMotionReceipt",
    "ContinuityFalsifierResult",
    "InitiatedCarrierState",
    "InitiationBoundaryError",
    "MarkedInitiationSeam",
    "PartialInitiationAttachment",
    "PartialInitiationBoundaryReport",
    "RootVisibleProjection",
    "SeamCoordinateView",
    "StructuralNullTopologyKind",
    "TwistReceipt",
    "advance_attached_state",
    "build_partial_initiation_attachments",
    "exact_sheet_involution",
    "initiate_carrier_state",
    "partial_initiation_exact_comparison_policy",
    "project_root_visible_state",
    "run_v013_partial_initiation_boundary_experiment",
    "view_marked_seam_at_cut",
]
