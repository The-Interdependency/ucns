# === MODULE_BUILD ===
# id: edcm_carrier_coordinate_admissibility_experiment
#   module_name: carrier_coordinate
#   module_kind: experiment
#   summary: evaluates a declared family of exact-rational transverse-to-cover coordinate laws against actual directed-cover materialization, injectivity, root restriction, convention invariance, and motion commutation
#   owner: Erin Spencer
#   public_surface: CarrierCoordinateCandidate, CarrierCoordinateImage, CarrierCoordinateCandidateResult, CarrierCoordinateAdmissibilityReport, carrier_coordinate_candidates, map_transverse_to_actual_cover, run_v010_carrier_coordinate_experiment
#   internal_surface: exact coordinate adapters, binary64 materialization identities, exhaustive witness-key validation, collision classes, root restrictions, convention witnesses, and motion witnesses
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and native completion scope remain linked through every candidate coordinate image
#   admin_only: false
#   tests: tests/test_carrier_coordinate.py
#   rollout: explicit UCNS-only v0.10 bounded candidate experiment; no carrier selection, faithful-breadth canon, arbitrary-element assignment, global equivalence, completion, EDCM activation, or METAPAT activation
#   rollback: remove this module, its exports, tests, and v0.10 document while retaining the v0.5 through v0.9 evidence
#   requires: edcm_exact_rational_transverse_envelope_experiment, directed_carrier_floor, explicit_comparison_policy_layer
#   since: 2026-07-29
#   unresolved: real-valued continuity, arbitrary-element assignment, canonical faithful breadth, global Mobius-to-cover equivalence, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: carrier_coordinate_family_is_explicit_and_nonselecting
#   given: the v0.10 experiment is constructed
#   then: every candidate has a fixed name, version, formula, coordinate basis, code reference, and scope; all results remain visible and selection_effect remains none
#   class: doctrine
#   since: 2026-07-29
#
# id: carrier_coordinate_uses_actual_cover_fields
#   given: a candidate maps one transverse envelope
#   then: the declared exact breadth and unchanged lifted turn materialize as the breadth and angle of an actual LiftedCarrierPoint; wrapper-only identity does not count as coordinate injectivity
#   class: correctness
#   since: 2026-07-29
#
# id: carrier_coordinate_report_validates_complete_witness_identities
#   given: a v0.10 report is constructed or replaced through the public dataclass API
#   then: every expected candidate, event, fiber, convention, and transition key appears exactly once in declared order and collision witnesses are re-derived from the actual cover identities
#   class: evidence
#   since: 2026-07-29
#
# id: carrier_coordinate_zero_fiber_restricts_to_v07
#   given: any declared v0.10 candidate receives exact transverse zero
#   then: its actual directed-cover point equals the unchanged v0.7 root materialization under the pinned exact comparison policy
#   class: correctness
#   since: 2026-07-29
#
# id: carrier_coordinate_admissibility_retains_failures
#   given: a candidate loses transverse sign, collapses fibers, or fails to commute with root motion
#   then: the exact collision or motion witness remains in its result and the candidate is rejected only on the declared finite domain
#   class: evidence
#   since: 2026-07-29
#
# id: carrier_coordinate_constructive_result_does_not_select
#   given: a candidate is injective and passes every declared criterion on the bounded exact-rational domain
#   then: its status is admissible-on-declared-domain while carrier selection, faithful-breadth canon, arbitrary-element assignment, EDCM activation, and METAPAT activation remain absent
#   class: safety
#   since: 2026-07-29
# === END CONTRACTS ===

"""Bounded carrier-coordinate admissibility experiment for UCNS v0.10.

v0.9 proved that an exact transverse sidecar beside the v0.7 root chart is not
itself a transverse directed-cover embedding.  This module declares four
candidate laws that place the transverse value into an actual
:class:`ucns.carrier.LiftedCarrierPoint` coordinate:

* constant root breadth;
* unsigned local radial displacement;
* signed local-frame radial displacement; and
* signed global-side radial displacement.

Each law preserves the root angle and maps exact transverse zero to the v0.7
root breadth.  The bounded experiment then retains every actual-cover
collision, convention comparison, root restriction, and motion-commutation
witness over the v0.9 45-fiber exact-rational stress grid.

An admissible result is scoped to that declared domain.  It is not a carrier
selection, a canonical faithful-breadth law, a real-continuity theorem, or an
arbitrary-element assignment.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from .carrier import VISIBLE_PERIOD, LiftedCarrierPoint
from .comparison import ComparisonMode, ComparisonPolicy, exact_comparison_policy
from .direct_mobius import NativeMobiusInitiationPacket
from .transverse_envelope import (
    TRANSVERSE_TRANSITION_LABELS,
    FramedMobiusStripState,
    TransverseCoordinateConvention,
    TransverseEnvelopeReport,
    TransverseEnvelopeState,
    convert_transverse_convention,
    exact_rational_stress_fibers,
    mobius_to_transverse_envelope,
    run_v09_transverse_envelope_experiment,
)


V010_CARRIER_COORDINATE_SCHEMA_ID = (
    "ucns.edcm.carrier-coordinate-admissibility"
)
V010_CARRIER_COORDINATE_SCHEMA_VERSION = "0.10.0"
V010_SELECTION_EFFECT = "none"
CARRIER_COORDINATE_SCOPE = (
    "bounded-exact-rational-transverse-to-directed-cover-only"
)
CARRIER_COORDINATE_COMPARISON_POLICY_NAME = (
    "carrier-coordinate-admissibility-exact"
)
CARRIER_COORDINATE_COMPARISON_POLICY_VERSION = "0.10.0"
CARRIER_COORDINATE_COMPARISON_POLICY_CODE_REFERENCE = (
    "ucns.comparison:exact_comparison_policy"
)
CARRIER_COORDINATE_CANDIDATE_VERSION = "0.10.0"
CARRIER_COORDINATE_CODE_REFERENCE = (
    "ucns.carrier_coordinate:map_transverse_to_actual_cover"
)
CARRIER_COORDINATE_RADIAL_SCALE = Fraction(1, 2)
CARRIER_COORDINATE_ROOT_BREADTH = Fraction(1)


class CarrierCoordinateError(ValueError):
    """Raised when carrier-coordinate evidence crosses its declared boundary."""


class CarrierCoordinateBasis(str, Enum):
    """Declared transverse evidence used by a candidate radial law."""

    CONSTANT_ROOT = "constant-root-breadth"
    ABSOLUTE_LOCAL = "absolute-local-transverse"
    SIGNED_LOCAL = "signed-local-transverse"
    SIGNED_GLOBAL = "signed-global-transverse"


class CarrierCoordinateAdmissibility(str, Enum):
    """Bounded experiment status; neither value selects a carrier."""

    ADMISSIBLE = "admissible-on-declared-domain"
    REJECTED = "rejected-on-declared-domain"


def carrier_coordinate_exact_comparison_policy() -> ComparisonPolicy:
    """Return the named exact policy pinned by the v0.10 experiment."""

    return exact_comparison_policy(
        name=CARRIER_COORDINATE_COMPARISON_POLICY_NAME,
        version=CARRIER_COORDINATE_COMPARISON_POLICY_VERSION,
    )


def _validate_policy(policy: ComparisonPolicy) -> None:
    if not isinstance(policy, ComparisonPolicy):
        raise TypeError("comparison_policy must be ComparisonPolicy")
    if policy.name != CARRIER_COORDINATE_COMPARISON_POLICY_NAME:
        raise CarrierCoordinateError("carrier-coordinate policy name is fixed")
    if policy.version != CARRIER_COORDINATE_COMPARISON_POLICY_VERSION:
        raise CarrierCoordinateError("carrier-coordinate policy version is fixed")
    if policy.mode is not ComparisonMode.EXACT:
        raise CarrierCoordinateError("carrier-coordinate policy must be exact")
    if (
        policy.code_reference
        != CARRIER_COORDINATE_COMPARISON_POLICY_CODE_REFERENCE
    ):
        raise CarrierCoordinateError(
            "carrier-coordinate comparison implementation reference is fixed"
        )


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise CarrierCoordinateError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise CarrierCoordinateError(f"{field} must retain at least one item")
    for value in values:
        _require_text(value, field)


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _actual_cover_key(
    point: LiftedCarrierPoint,
) -> tuple[tuple[str, str], ...]:
    """Return the exact stored binary64 identity of an actual cover point."""

    if not isinstance(point, LiftedCarrierPoint):
        raise TypeError("point must be LiftedCarrierPoint")
    return (
        ("breadth-binary64", point.breadth.hex()),
        ("angle-binary64", point.angle.hex()),
    )


def _normalize_lifted_turns(value: Fraction) -> Fraction:
    whole_periods = value // 2
    return value - 2 * whole_periods


def _exact_turns(value: Fraction | int) -> Fraction:
    if isinstance(value, bool):
        raise CarrierCoordinateError("candidate motion cannot be boolean")
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, Fraction):
        raise CarrierCoordinateError(
            "candidate motion must be int or exact Fraction"
        )
    return value


def _materialize(
    breadth: Fraction,
    lifted_turns: Fraction,
) -> LiftedCarrierPoint:
    if not isinstance(breadth, Fraction) or breadth <= 0:
        raise CarrierCoordinateError(
            "candidate actual-cover breadth must be an exact positive Fraction"
        )
    if not isinstance(lifted_turns, Fraction):
        raise CarrierCoordinateError(
            "candidate lifted turns must remain an exact Fraction"
        )
    return LiftedCarrierPoint(
        float(breadth),
        float(_normalize_lifted_turns(lifted_turns)) * VISIBLE_PERIOD,
    )


@dataclass(frozen=True, slots=True)
class CarrierCoordinateCandidate:
    """One explicitly identified, noncanonical candidate radial law."""

    candidate_id: str
    basis: CarrierCoordinateBasis
    formula: str
    version: str = CARRIER_COORDINATE_CANDIDATE_VERSION
    code_reference: str = CARRIER_COORDINATE_CODE_REFERENCE
    scope: str = CARRIER_COORDINATE_SCOPE
    selection_effect: str = V010_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.candidate_id, "candidate_id")
        if not isinstance(self.basis, CarrierCoordinateBasis):
            raise CarrierCoordinateError(
                "basis must be CarrierCoordinateBasis"
            )
        _require_text(self.formula, "formula")
        if self.version != CARRIER_COORDINATE_CANDIDATE_VERSION:
            raise CarrierCoordinateError("candidate version is fixed")
        if self.code_reference != CARRIER_COORDINATE_CODE_REFERENCE:
            raise CarrierCoordinateError("candidate code reference is fixed")
        if self.scope != CARRIER_COORDINATE_SCOPE:
            raise CarrierCoordinateError("candidate scope is fixed")
        if self.selection_effect != V010_SELECTION_EFFECT:
            raise CarrierCoordinateError("candidate cannot select a carrier")

    @property
    def identity_key(self) -> tuple[str, str, str]:
        return self.candidate_id, self.version, self.basis.value


def carrier_coordinate_candidates() -> tuple[CarrierCoordinateCandidate, ...]:
    """Return the complete ordered v0.10 candidate family without a default."""

    return (
        CarrierCoordinateCandidate(
            candidate_id="constant-root-breadth",
            basis=CarrierCoordinateBasis.CONSTANT_ROOT,
            formula="B(u)=1",
        ),
        CarrierCoordinateCandidate(
            candidate_id="unsigned-local-radial",
            basis=CarrierCoordinateBasis.ABSOLUTE_LOCAL,
            formula="B(u)=1+abs(u)/2",
        ),
        CarrierCoordinateCandidate(
            candidate_id="signed-local-affine-radial",
            basis=CarrierCoordinateBasis.SIGNED_LOCAL,
            formula="B(u)=1+u/2",
        ),
        CarrierCoordinateCandidate(
            candidate_id="signed-global-affine-radial",
            basis=CarrierCoordinateBasis.SIGNED_GLOBAL,
            formula="B(u)=1+(frame_sign*u)/2",
        ),
    )


def _candidate_breadth(
    candidate: CarrierCoordinateCandidate,
    state: TransverseEnvelopeState,
) -> Fraction:
    local = state.local_transverse
    if candidate.basis is CarrierCoordinateBasis.CONSTANT_ROOT:
        return CARRIER_COORDINATE_ROOT_BREADTH
    if candidate.basis is CarrierCoordinateBasis.ABSOLUTE_LOCAL:
        return CARRIER_COORDINATE_ROOT_BREADTH + (
            abs(local) * CARRIER_COORDINATE_RADIAL_SCALE
        )
    if candidate.basis is CarrierCoordinateBasis.SIGNED_LOCAL:
        return CARRIER_COORDINATE_ROOT_BREADTH + (
            local * CARRIER_COORDINATE_RADIAL_SCALE
        )
    if candidate.basis is CarrierCoordinateBasis.SIGNED_GLOBAL:
        return CARRIER_COORDINATE_ROOT_BREADTH + (
            state.global_transverse * CARRIER_COORDINATE_RADIAL_SCALE
        )
    raise CarrierCoordinateError("unknown carrier-coordinate candidate basis")


@dataclass(frozen=True, slots=True)
class CarrierCoordinateImage:
    """One source-linked candidate image in actual directed-cover fields."""

    candidate: CarrierCoordinateCandidate
    source_state: TransverseEnvelopeState
    declared_breadth: Fraction
    declared_lifted_turns: Fraction
    actual_point: LiftedCarrierPoint
    comparison_policy: ComparisonPolicy
    mapping_status: str = "candidate-mapped-into-actual-cover"

    def __post_init__(self) -> None:
        if not isinstance(self.candidate, CarrierCoordinateCandidate):
            raise TypeError("candidate must be CarrierCoordinateCandidate")
        if not isinstance(self.source_state, TransverseEnvelopeState):
            raise TypeError("source_state must be TransverseEnvelopeState")
        _validate_policy(self.comparison_policy)
        if self.declared_breadth != _candidate_breadth(
            self.candidate,
            self.source_state,
        ):
            raise CarrierCoordinateError(
                "declared breadth does not match the candidate formula"
            )
        if self.declared_lifted_turns != (
            self.source_state.root_chart.lifted_turns
        ):
            raise CarrierCoordinateError(
                "candidate map must preserve the root lifted coordinate"
            )
        expected_point = _materialize(
            self.declared_breadth,
            self.declared_lifted_turns,
        )
        if not self.comparison_policy.matches(
            _actual_cover_key(self.actual_point),
            _actual_cover_key(expected_point),
        ):
            raise CarrierCoordinateError(
                "candidate image is not materialized in actual cover fields"
            )
        if self.mapping_status != "candidate-mapped-into-actual-cover":
            raise CarrierCoordinateError("candidate mapping status is fixed")

    @property
    def event_id(self) -> str:
        return self.source_state.root_chart.initiation_event_id

    @property
    def local_transverse(self) -> Fraction:
        return self.source_state.local_transverse

    @property
    def convention(self) -> TransverseCoordinateConvention:
        return self.source_state.convention

    @property
    def exact_coordinate_key(self) -> tuple[tuple[str, str], ...]:
        return (
            ("breadth", _fraction_key(self.declared_breadth)),
            ("lifted-turns", _fraction_key(self.declared_lifted_turns)),
        )

    @property
    def actual_cover_key(self) -> tuple[tuple[str, str], ...]:
        return _actual_cover_key(self.actual_point)

    @property
    def source_coordinate_key(self) -> tuple[object, ...]:
        return (
            self.source_state.actual_cover_identity,
            ("local-transverse", _fraction_key(self.local_transverse)),
        )

    @property
    def evidence_key(self) -> tuple[str, str, str, str]:
        return (
            self.candidate.candidate_id,
            self.event_id,
            _fraction_key(self.local_transverse),
            self.convention.value,
        )


def map_transverse_to_actual_cover(
    state: TransverseEnvelopeState,
    candidate: CarrierCoordinateCandidate,
    comparison_policy: ComparisonPolicy | None = None,
) -> CarrierCoordinateImage:
    """Map one exact transverse envelope into actual cover breadth and angle."""

    if not isinstance(state, TransverseEnvelopeState):
        raise TypeError("state must be TransverseEnvelopeState")
    if not isinstance(candidate, CarrierCoordinateCandidate):
        raise TypeError("candidate must be CarrierCoordinateCandidate")
    policy = comparison_policy or carrier_coordinate_exact_comparison_policy()
    _validate_policy(policy)
    breadth = _candidate_breadth(candidate, state)
    lifted_turns = state.root_chart.lifted_turns
    return CarrierCoordinateImage(
        candidate=candidate,
        source_state=state,
        declared_breadth=breadth,
        declared_lifted_turns=lifted_turns,
        actual_point=_materialize(breadth, lifted_turns),
        comparison_policy=policy,
    )


@dataclass(frozen=True, slots=True)
class CarrierCoordinateRootRestrictionWitness:
    candidate: CarrierCoordinateCandidate
    event_id: str
    convention: TransverseCoordinateConvention
    image: CarrierCoordinateImage
    expected_root_point: LiftedCarrierPoint
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _validate_policy(self.comparison_policy)
        _require_text(self.event_id, "event_id")
        if self.image.local_transverse != 0:
            raise CarrierCoordinateError("root restriction requires exact zero")
        if self.image.event_id != self.event_id:
            raise CarrierCoordinateError("root restriction lost event identity")
        if self.image.candidate != self.candidate:
            raise CarrierCoordinateError("root restriction lost candidate identity")
        if self.image.convention is not self.convention:
            raise CarrierCoordinateError("root restriction lost convention")

    @property
    def passes(self) -> bool:
        return self.comparison_policy.matches(
            self.image.actual_cover_key,
            _actual_cover_key(self.expected_root_point),
        )

    @property
    def evidence_key(self) -> tuple[str, str, str]:
        return (
            self.candidate.candidate_id,
            self.event_id,
            self.convention.value,
        )


@dataclass(frozen=True, slots=True)
class CarrierCoordinateConventionWitness:
    candidate: CarrierCoordinateCandidate
    event_id: str
    local_transverse: Fraction
    local_image: CarrierCoordinateImage
    global_image: CarrierCoordinateImage
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _validate_policy(self.comparison_policy)
        _require_text(self.event_id, "event_id")
        if self.local_image.convention is not (
            TransverseCoordinateConvention.LOCAL_FRAME
        ):
            raise CarrierCoordinateError("local image convention is mislabeled")
        if self.global_image.convention is not (
            TransverseCoordinateConvention.GLOBAL_SIDE
        ):
            raise CarrierCoordinateError("global image convention is mislabeled")
        if self.local_image.candidate != self.candidate:
            raise CarrierCoordinateError("local image lost candidate identity")
        if self.global_image.candidate != self.candidate:
            raise CarrierCoordinateError("global image lost candidate identity")
        if (
            self.local_image.event_id != self.event_id
            or self.global_image.event_id != self.event_id
        ):
            raise CarrierCoordinateError("convention witness lost event identity")
        if (
            self.local_image.local_transverse != self.local_transverse
            or self.global_image.local_transverse != self.local_transverse
        ):
            raise CarrierCoordinateError(
                "convention witness changed the local transverse value"
            )

    @property
    def passes(self) -> bool:
        return self.comparison_policy.matches(
            self.local_image.actual_cover_key,
            self.global_image.actual_cover_key,
        )

    @property
    def evidence_key(self) -> tuple[str, str, str]:
        return (
            self.candidate.candidate_id,
            self.event_id,
            _fraction_key(self.local_transverse),
        )


@dataclass(frozen=True, slots=True)
class CarrierCoordinateMotionWitness:
    candidate: CarrierCoordinateCandidate
    event_id: str
    local_transverse: Fraction
    convention: TransverseCoordinateConvention
    label: str
    turns: Fraction
    expected_image: CarrierCoordinateImage
    observed_point: LiftedCarrierPoint
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _validate_policy(self.comparison_policy)
        _require_text(self.event_id, "event_id")
        if self.label not in TRANSVERSE_TRANSITION_LABELS:
            raise CarrierCoordinateError("unknown candidate transition label")
        if not isinstance(self.turns, Fraction):
            raise CarrierCoordinateError("motion witness turns must be exact")
        if self.expected_image.candidate != self.candidate:
            raise CarrierCoordinateError("motion witness lost candidate identity")
        if self.expected_image.event_id != self.event_id:
            raise CarrierCoordinateError("motion witness lost event identity")
        if self.expected_image.convention is not self.convention:
            raise CarrierCoordinateError("motion witness lost convention")
        if self.expected_image.local_transverse != self.local_transverse:
            raise CarrierCoordinateError("motion witness changed transverse value")

    @property
    def passes(self) -> bool:
        return self.comparison_policy.matches(
            self.expected_image.actual_cover_key,
            _actual_cover_key(self.observed_point),
        )

    @property
    def evidence_key(self) -> tuple[str, str, str, str, str]:
        return (
            self.candidate.candidate_id,
            self.event_id,
            _fraction_key(self.local_transverse),
            self.convention.value,
            self.label,
        )


@dataclass(frozen=True, slots=True)
class CarrierCoordinateCollisionWitness:
    candidate: CarrierCoordinateCandidate
    event_id: str
    convention: TransverseCoordinateConvention
    first: CarrierCoordinateImage
    second: CarrierCoordinateImage
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _validate_policy(self.comparison_policy)
        _require_text(self.event_id, "event_id")
        if self.first.candidate != self.candidate:
            raise CarrierCoordinateError("first collision lost candidate identity")
        if self.second.candidate != self.candidate:
            raise CarrierCoordinateError("second collision lost candidate identity")
        if self.first.event_id != self.event_id or self.second.event_id != self.event_id:
            raise CarrierCoordinateError("collision witness lost event identity")
        if (
            self.first.convention is not self.convention
            or self.second.convention is not self.convention
        ):
            raise CarrierCoordinateError("collision convention is mislabeled")
        if self.first.local_transverse == self.second.local_transverse:
            raise CarrierCoordinateError(
                "collision requires distinct transverse values"
            )
        if not self.comparison_policy.matches(
            self.first.actual_cover_key,
            self.second.actual_cover_key,
        ):
            raise CarrierCoordinateError(
                "collision witness must share an actual cover coordinate"
            )

    @property
    def evidence_key(self) -> tuple[str, str, str, str, str]:
        return (
            self.candidate.candidate_id,
            self.event_id,
            self.convention.value,
            _fraction_key(self.first.local_transverse),
            _fraction_key(self.second.local_transverse),
        )


def _motion_inputs(
    initial: FramedMobiusStripState,
    label: str,
) -> tuple[FramedMobiusStripState, Fraction]:
    if label == "initiation":
        return initial, Fraction(0)
    if label == "advance-360":
        return initial, Fraction(1)
    if label == "advance-720":
        return initial, Fraction(2)
    if label == "inverse":
        return initial.advance(1), Fraction(-1)
    raise CarrierCoordinateError("unknown candidate transition label")


def _build_images(
    candidate: CarrierCoordinateCandidate,
    packet: NativeMobiusInitiationPacket,
    fibers: tuple[Fraction, ...],
    policy: ComparisonPolicy,
) -> tuple[CarrierCoordinateImage, ...]:
    images: list[CarrierCoordinateImage] = []
    for event in packet.initiations:
        for local_transverse in fibers:
            native = FramedMobiusStripState(event.post_state, local_transverse)
            for convention in TransverseCoordinateConvention:
                images.append(
                    map_transverse_to_actual_cover(
                        mobius_to_transverse_envelope(native, convention),
                        candidate,
                        policy,
                    )
                )
    return tuple(images)


def _build_root_restrictions(
    candidate: CarrierCoordinateCandidate,
    packet: NativeMobiusInitiationPacket,
    policy: ComparisonPolicy,
) -> tuple[CarrierCoordinateRootRestrictionWitness, ...]:
    witnesses: list[CarrierCoordinateRootRestrictionWitness] = []
    for event in packet.initiations:
        native = FramedMobiusStripState(event.post_state, Fraction(0))
        for convention in TransverseCoordinateConvention:
            envelope = mobius_to_transverse_envelope(native, convention)
            witnesses.append(
                CarrierCoordinateRootRestrictionWitness(
                    candidate=candidate,
                    event_id=event.event_id,
                    convention=convention,
                    image=map_transverse_to_actual_cover(
                        envelope,
                        candidate,
                        policy,
                    ),
                    expected_root_point=envelope.root_chart.materialized_point,
                    comparison_policy=policy,
                )
            )
    return tuple(witnesses)


def _build_convention_witnesses(
    candidate: CarrierCoordinateCandidate,
    packet: NativeMobiusInitiationPacket,
    fibers: tuple[Fraction, ...],
    policy: ComparisonPolicy,
) -> tuple[CarrierCoordinateConventionWitness, ...]:
    witnesses: list[CarrierCoordinateConventionWitness] = []
    for event in packet.initiations:
        for local_transverse in fibers:
            native = FramedMobiusStripState(event.post_state, local_transverse)
            local_state = mobius_to_transverse_envelope(
                native,
                TransverseCoordinateConvention.LOCAL_FRAME,
            )
            global_state = convert_transverse_convention(
                local_state,
                TransverseCoordinateConvention.GLOBAL_SIDE,
            )
            witnesses.append(
                CarrierCoordinateConventionWitness(
                    candidate=candidate,
                    event_id=event.event_id,
                    local_transverse=local_transverse,
                    local_image=map_transverse_to_actual_cover(
                        local_state,
                        candidate,
                        policy,
                    ),
                    global_image=map_transverse_to_actual_cover(
                        global_state,
                        candidate,
                        policy,
                    ),
                    comparison_policy=policy,
                )
            )
    return tuple(witnesses)


def _build_motion_witnesses(
    candidate: CarrierCoordinateCandidate,
    packet: NativeMobiusInitiationPacket,
    fibers: tuple[Fraction, ...],
    policy: ComparisonPolicy,
) -> tuple[CarrierCoordinateMotionWitness, ...]:
    witnesses: list[CarrierCoordinateMotionWitness] = []
    for event in packet.initiations:
        for local_transverse in fibers:
            initial = FramedMobiusStripState(event.post_state, local_transverse)
            for convention in TransverseCoordinateConvention:
                for label in TRANSVERSE_TRANSITION_LABELS:
                    start, turns = _motion_inputs(initial, label)
                    start_image = map_transverse_to_actual_cover(
                        mobius_to_transverse_envelope(start, convention),
                        candidate,
                        policy,
                    )
                    expected_image = map_transverse_to_actual_cover(
                        mobius_to_transverse_envelope(
                            start.advance(turns),
                            convention,
                        ),
                        candidate,
                        policy,
                    )
                    observed = start_image.actual_point.rotate(
                        float(turns) * VISIBLE_PERIOD
                    )
                    witnesses.append(
                        CarrierCoordinateMotionWitness(
                            candidate=candidate,
                            event_id=event.event_id,
                            local_transverse=local_transverse,
                            convention=convention,
                            label=label,
                            turns=turns,
                            expected_image=expected_image,
                            observed_point=observed,
                            comparison_policy=policy,
                        )
                    )
    return tuple(witnesses)


def _collision_witnesses_from_images(
    candidate: CarrierCoordinateCandidate,
    images: tuple[CarrierCoordinateImage, ...],
    policy: ComparisonPolicy,
) -> tuple[CarrierCoordinateCollisionWitness, ...]:
    grouped: dict[
        tuple[str, str],
        dict[tuple[tuple[str, str], ...], list[CarrierCoordinateImage]],
    ] = {}
    for image in images:
        group_key = (image.event_id, image.convention.value)
        grouped.setdefault(group_key, {}).setdefault(
            image.actual_cover_key,
            [],
        ).append(image)

    witnesses: list[CarrierCoordinateCollisionWitness] = []
    for event_id, convention_value in (
        (image.event_id, image.convention.value) for image in images
    ):
        group_key = (event_id, convention_value)
        coordinate_groups = grouped.pop(group_key, None)
        if coordinate_groups is None:
            continue
        convention = TransverseCoordinateConvention(convention_value)
        for coordinate_images in coordinate_groups.values():
            if len(coordinate_images) < 2:
                continue
            first = coordinate_images[0]
            for second in coordinate_images[1:]:
                witnesses.append(
                    CarrierCoordinateCollisionWitness(
                        candidate=candidate,
                        event_id=event_id,
                        convention=convention,
                        first=first,
                        second=second,
                        comparison_policy=policy,
                    )
                )
    return tuple(witnesses)


@dataclass(frozen=True, slots=True)
class CarrierCoordinateCandidateResult:
    """Complete bounded evidence for one candidate, passing or failing."""

    candidate: CarrierCoordinateCandidate
    images: tuple[CarrierCoordinateImage, ...]
    root_restrictions: tuple[CarrierCoordinateRootRestrictionWitness, ...]
    convention_witnesses: tuple[CarrierCoordinateConventionWitness, ...]
    motion_witnesses: tuple[CarrierCoordinateMotionWitness, ...]
    collision_witnesses: tuple[CarrierCoordinateCollisionWitness, ...]
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _validate_policy(self.comparison_policy)
        if not isinstance(self.candidate, CarrierCoordinateCandidate):
            raise TypeError("candidate must be CarrierCoordinateCandidate")
        groups = (
            self.images,
            self.root_restrictions,
            self.convention_witnesses,
            self.motion_witnesses,
            self.collision_witnesses,
        )
        for group in groups:
            if any(item.candidate != self.candidate for item in group):
                raise CarrierCoordinateError(
                    "candidate result contains evidence from another candidate"
                )
            if any(
                item.comparison_policy != self.comparison_policy
                for item in group
            ):
                raise CarrierCoordinateError(
                    "candidate result contains an unpinned comparison policy"
                )

    @property
    def root_restriction_passes(self) -> bool:
        return bool(self.root_restrictions) and all(
            item.passes for item in self.root_restrictions
        )

    @property
    def convention_invariance_passes(self) -> bool:
        return bool(self.convention_witnesses) and all(
            item.passes for item in self.convention_witnesses
        )

    @property
    def motion_commutation_passes(self) -> bool:
        return bool(self.motion_witnesses) and all(
            item.passes for item in self.motion_witnesses
        )

    @property
    def fiber_injectivity_passes(self) -> bool:
        return bool(self.images) and not self.collision_witnesses

    @property
    def admissibility(self) -> CarrierCoordinateAdmissibility:
        if (
            self.root_restriction_passes
            and self.convention_invariance_passes
            and self.motion_commutation_passes
            and self.fiber_injectivity_passes
        ):
            return CarrierCoordinateAdmissibility.ADMISSIBLE
        return CarrierCoordinateAdmissibility.REJECTED

    @property
    def criterion_receipts(self) -> tuple[tuple[str, bool], ...]:
        return (
            ("actual-cover-fiber-injectivity", self.fiber_injectivity_passes),
            ("zero-fiber-root-restriction", self.root_restriction_passes),
            ("coordinate-convention-invariance", self.convention_invariance_passes),
            ("root-motion-commutation", self.motion_commutation_passes),
        )


def _build_candidate_result(
    candidate: CarrierCoordinateCandidate,
    packet: NativeMobiusInitiationPacket,
    fibers: tuple[Fraction, ...],
    policy: ComparisonPolicy,
) -> CarrierCoordinateCandidateResult:
    images = _build_images(candidate, packet, fibers, policy)
    return CarrierCoordinateCandidateResult(
        candidate=candidate,
        images=images,
        root_restrictions=_build_root_restrictions(
            candidate,
            packet,
            policy,
        ),
        convention_witnesses=_build_convention_witnesses(
            candidate,
            packet,
            fibers,
            policy,
        ),
        motion_witnesses=_build_motion_witnesses(
            candidate,
            packet,
            fibers,
            policy,
        ),
        collision_witnesses=_collision_witnesses_from_images(
            candidate,
            images,
            policy,
        ),
        comparison_policy=policy,
    )


def _expected_collision_keys(
    candidate: CarrierCoordinateCandidate,
    images: tuple[CarrierCoordinateImage, ...],
    policy: ComparisonPolicy,
) -> tuple[tuple[str, str, str, str, str], ...]:
    return tuple(
        item.evidence_key
        for item in _collision_witnesses_from_images(
            candidate,
            images,
            policy,
        )
    )


@dataclass(frozen=True, slots=True)
class CarrierCoordinateAdmissibilityReport:
    """Complete v0.10 family evidence with exhaustive identity validation."""

    report_id: str
    transverse_report: TransverseEnvelopeReport
    candidates: tuple[CarrierCoordinateCandidate, ...]
    fibers: tuple[Fraction, ...]
    comparison_policy: ComparisonPolicy
    results: tuple[CarrierCoordinateCandidateResult, ...]
    hmmm: tuple[str, ...]
    schema_id: str = V010_CARRIER_COORDINATE_SCHEMA_ID
    schema_version: str = V010_CARRIER_COORDINATE_SCHEMA_VERSION
    code_reference: str = (
        "ucns.carrier_coordinate:run_v010_carrier_coordinate_experiment"
    )
    selection_effect: str = V010_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.report_id, "report_id")
        _validate_policy(self.comparison_policy)
        if self.schema_id != V010_CARRIER_COORDINATE_SCHEMA_ID:
            raise CarrierCoordinateError("v0.10 schema identity mismatch")
        if self.schema_version != V010_CARRIER_COORDINATE_SCHEMA_VERSION:
            raise CarrierCoordinateError("v0.10 schema version mismatch")
        if self.code_reference != (
            "ucns.carrier_coordinate:run_v010_carrier_coordinate_experiment"
        ):
            raise CarrierCoordinateError("v0.10 code reference mismatch")
        if self.selection_effect != V010_SELECTION_EFFECT:
            raise CarrierCoordinateError("v0.10 cannot select a carrier")
        if self.transverse_report.selection_effect != V010_SELECTION_EFFECT:
            raise CarrierCoordinateError(
                "v0.10 input cannot carry a selection effect"
            )
        if self.fibers != self.transverse_report.fibers:
            raise CarrierCoordinateError(
                "v0.10 fibers must be the exact v0.9 stress domain"
            )
        if self.candidates != carrier_coordinate_candidates():
            raise CarrierCoordinateError(
                "v0.10 must retain the complete declared candidate family"
            )
        if tuple(result.candidate for result in self.results) != self.candidates:
            raise CarrierCoordinateError(
                "v0.10 results must retain candidate order and identity"
            )

        packet = self.transverse_report.root_report.direct_report.packet
        event_ids = tuple(event.event_id for event in packet.initiations)
        fiber_keys = tuple(_fraction_key(value) for value in self.fibers)
        convention_keys = tuple(
            convention.value for convention in TransverseCoordinateConvention
        )

        for result in self.results:
            candidate_id = result.candidate.candidate_id
            expected_image_keys = tuple(
                (candidate_id, event_id, fiber, convention)
                for event_id in event_ids
                for fiber in fiber_keys
                for convention in convention_keys
            )
            if tuple(item.evidence_key for item in result.images) != (
                expected_image_keys
            ):
                raise CarrierCoordinateError(
                    "candidate images must cover every event/fiber/convention"
                )

            expected_restriction_keys = tuple(
                (candidate_id, event_id, convention)
                for event_id in event_ids
                for convention in convention_keys
            )
            if tuple(
                item.evidence_key for item in result.root_restrictions
            ) != expected_restriction_keys:
                raise CarrierCoordinateError(
                    "root restrictions must cover every event/convention"
                )

            expected_convention_keys = tuple(
                (candidate_id, event_id, fiber)
                for event_id in event_ids
                for fiber in fiber_keys
            )
            if tuple(
                item.evidence_key for item in result.convention_witnesses
            ) != expected_convention_keys:
                raise CarrierCoordinateError(
                    "convention witnesses must cover every event/fiber"
                )

            expected_motion_keys = tuple(
                (candidate_id, event_id, fiber, convention, label)
                for event_id in event_ids
                for fiber in fiber_keys
                for convention in convention_keys
                for label in TRANSVERSE_TRANSITION_LABELS
            )
            if tuple(
                item.evidence_key for item in result.motion_witnesses
            ) != expected_motion_keys:
                raise CarrierCoordinateError(
                    "motion witnesses must cover every declared transition"
                )

            if tuple(
                item.evidence_key for item in result.collision_witnesses
            ) != _expected_collision_keys(
                result.candidate,
                result.images,
                self.comparison_policy,
            ):
                raise CarrierCoordinateError(
                    "collision witnesses must be re-derived from actual cover identities"
                )

        expected_statuses = (
            CarrierCoordinateAdmissibility.REJECTED,
            CarrierCoordinateAdmissibility.REJECTED,
            CarrierCoordinateAdmissibility.ADMISSIBLE,
            CarrierCoordinateAdmissibility.REJECTED,
        )
        if tuple(result.admissibility for result in self.results) != (
            expected_statuses
        ):
            raise CarrierCoordinateError(
                "v0.10 candidate outcomes changed without a new experiment identity"
            )
        _require_text_items(self.hmmm, "hmmm")

    @property
    def admissible_candidate_ids(self) -> tuple[str, ...]:
        """Return passing evidence without appointing a selected candidate."""

        return tuple(
            result.candidate.candidate_id
            for result in self.results
            if result.admissibility is CarrierCoordinateAdmissibility.ADMISSIBLE
        )


def run_v010_carrier_coordinate_experiment(
    *,
    report_id: str = "ucns-edcm-v0.10:carrier-coordinate-admissibility",
    max_denominator: int = 8,
) -> CarrierCoordinateAdmissibilityReport:
    """Run the complete bounded v0.10 candidate-family experiment."""

    transverse_report = run_v09_transverse_envelope_experiment(
        report_id=f"{report_id}:transverse-envelope",
        max_denominator=max_denominator,
    )
    packet = transverse_report.root_report.direct_report.packet
    fibers = exact_rational_stress_fibers(max_denominator)
    policy = carrier_coordinate_exact_comparison_policy()
    candidates = carrier_coordinate_candidates()
    return CarrierCoordinateAdmissibilityReport(
        report_id=report_id,
        transverse_report=transverse_report,
        candidates=candidates,
        fibers=fibers,
        comparison_policy=policy,
        results=tuple(
            _build_candidate_result(candidate, packet, fibers, policy)
            for candidate in candidates
        ),
        hmmm=(
            "the signed local affine radial law is injective only on the declared exact-rational stress domain after materialization into actual binary64 cover fields",
            "an admissible bounded candidate is evidence, not a selected carrier, canonical faithful-breadth law, global Mobius-to-cover equivalence, or real-continuity theorem",
            "constant breadth and unsigned radial displacement retain explicit actual-cover collision witnesses",
            "signed global radial displacement retains explicit failures to commute with odd root-loop motion",
            "arbitrary-element assignment, higher geometry, scoped completion, EDCM activation, and METAPAT activation remain unresolved",
        ),
    )


__all__ = [
    "CARRIER_COORDINATE_CANDIDATE_VERSION",
    "CARRIER_COORDINATE_CODE_REFERENCE",
    "CARRIER_COORDINATE_COMPARISON_POLICY_CODE_REFERENCE",
    "CARRIER_COORDINATE_COMPARISON_POLICY_NAME",
    "CARRIER_COORDINATE_COMPARISON_POLICY_VERSION",
    "CARRIER_COORDINATE_RADIAL_SCALE",
    "CARRIER_COORDINATE_ROOT_BREADTH",
    "CARRIER_COORDINATE_SCOPE",
    "V010_CARRIER_COORDINATE_SCHEMA_ID",
    "V010_CARRIER_COORDINATE_SCHEMA_VERSION",
    "V010_SELECTION_EFFECT",
    "CarrierCoordinateAdmissibility",
    "CarrierCoordinateAdmissibilityReport",
    "CarrierCoordinateBasis",
    "CarrierCoordinateCandidate",
    "CarrierCoordinateCandidateResult",
    "CarrierCoordinateCollisionWitness",
    "CarrierCoordinateConventionWitness",
    "CarrierCoordinateError",
    "CarrierCoordinateImage",
    "CarrierCoordinateMotionWitness",
    "CarrierCoordinateRootRestrictionWitness",
    "carrier_coordinate_candidates",
    "carrier_coordinate_exact_comparison_policy",
    "map_transverse_to_actual_cover",
    "run_v010_carrier_coordinate_experiment",
]
