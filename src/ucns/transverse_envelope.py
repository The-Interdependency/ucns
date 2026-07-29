# === MODULE_BUILD ===
# id: edcm_exact_rational_transverse_envelope_experiment
#   module_name: transverse_envelope
#   module_kind: experiment
#   summary: repairs the v0.8 sidecar overclaim and evaluates a source-preserving exact-rational transverse envelope without claiming a directed-cover embedding
#   owner: Erin Spencer
#   public_surface: FramedMobiusStripState, TransverseCoordinateConvention, TransverseEnvelopeState, TransverseEnvelopeReport, TransverseCarrierCollisionWitness, exact_rational_stress_fibers, mobius_to_transverse_envelope, transverse_envelope_to_mobius, convert_transverse_convention, run_v09_transverse_envelope_experiment
#   internal_surface: exact identity adapters, exhaustive witness-key validation, root restriction witnesses, motion witnesses, and cover-collision evidence
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and native completion scope remain linked through every envelope map
#   admin_only: false
#   tests: tests/test_transverse_envelope.py
#   rollout: explicit UCNS-only v0.9 repair and bounded exact-rational stress experiment; no transverse cover embedding, radial assignment, arbitrary-element assignment, global carrier equivalence, carrier selection, completion, EDCM activation, or METAPAT activation
#   rollback: remove this module, its exports, tests, and v0.9 document while retaining the v0.5 through v0.7 experiments and the v0.8 historical erratum
#   requires: edcm_root_loop_cover_chart_candidate, edcm_native_direct_mobius_candidate, explicit_comparison_policy_layer
#   since: 2026-07-29
#   unresolved: an injective transverse or radial directed-cover coordinate, faithful-breadth assignment, arbitrary element assignment, real-valued continuity, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: transverse_envelope_maps_preserve_exact_rational_state
#   given: a framed native state with any admitted exact rational transverse coordinate and either coordinate convention
#   then: native-to-envelope-to-native and envelope-to-native-to-envelope restore every declared identity field under the pinned exact comparison policy
#   class: correctness
#   since: 2026-07-29
#
# id: transverse_envelope_comparison_policy_is_explicit
#   given: a v0.9 round trip, restriction, motion, convention, collision, or report verdict is constructed
#   then: the named versioned exact comparison policy and implementation reference are retained and no hidden equality tolerance is used
#   class: doctrine
#   since: 2026-07-29
#
# id: transverse_envelope_report_validates_complete_witness_identities
#   given: a v0.9 report is constructed or replaced through the public dataclass API
#   then: every expected event, fiber, convention, and transition key appears exactly once in declared order and remains cross-checked against the v0.7 root report
#   class: evidence
#   since: 2026-07-29
#
# id: transverse_envelope_restricts_exactly_to_v07_root_loop
#   given: the transverse coordinate is exact zero
#   then: removing the envelope field recovers the unchanged v0.7 native and cover root-loop states for every initiation and both conventions
#   class: correctness
#   since: 2026-07-29
#
# id: transverse_envelope_exposes_cover_nonembedding
#   given: two distinct transverse values share the same v0.7 root state
#   then: their envelope identities remain distinct while their actual directed-cover coordinates coincide, proving that the envelope is not an injective transverse cover map
#   class: safety
#   since: 2026-07-29
#
# id: transverse_envelope_does_not_extend_cover_verdicts
#   given: the complete v0.9 report is produced
#   then: F12 support and F13 falsification retain only the v0.7 root-loop map identity while transverse cover extension remains inconclusive and selection remains none
#   class: doctrine
#   since: 2026-07-29
# === END CONTRACTS ===

"""Exact-rational transverse envelope repair experiment for UCNS v0.9.

The merged v0.8 experiment placed an exact transverse value beside the v0.7
root-loop chart, but did not map that value into an actual directed-cover
coordinate.  Calling the product a transverse cover chart therefore overstated
the evidence.

This module keeps the useful exact algebra and names the object honestly:

``v0.7 root-loop cover chart × exact transverse sidecar``.

The sidecar admits exact :class:`fractions.Fraction` values in ``[-1, +1]`` and
preserves both local-frame and global-side descriptions.  Every experiment
comparison uses a pinned named exact policy and every report validates complete
event/fiber/convention/transition identities rather than tuple lengths.

The report also constructs explicit collisions: distinct transverse envelope
states materialize to the same actual directed-cover coordinate.  Consequently
v0.9 does not extend the v0.7 F12/F13 verdicts beyond the root loop.  An
injective transverse or radial cover coordinate remains unresolved.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from fractions import Fraction

from .comparison import ComparisonMode, ComparisonPolicy, exact_comparison_policy
from .direct_mobius import (
    MobiusInitiationEvent,
    NativeMobiusFrame,
    NativeMobiusInitiationPacket,
    NativeMobiusState,
)
from .mobius_experiment import (
    CarrierExperimentReport,
    CarrierRelationship,
    FalsifierVerdict,
)
from .root_loop_chart import (
    ROOT_LOOP_CHART_MAP_ID,
    ROOT_LOOP_CHART_MAP_VERSION,
    RootLoopChartReport,
    RootLoopCoverChartState,
    mobius_to_root_loop_cover,
    root_loop_cover_to_mobius,
    run_v07_root_loop_chart_experiment,
)


V09_TRANSVERSE_ENVELOPE_SCHEMA_ID = "ucns.edcm.exact-rational-transverse-envelope"
V09_TRANSVERSE_ENVELOPE_SCHEMA_VERSION = "0.9.0"
V09_SELECTION_EFFECT = "none"
TRANSVERSE_ENVELOPE_ADAPTER_ID = (
    "ucns.edcm.mobius-root-chart-exact-rational-transverse-envelope"
)
TRANSVERSE_ENVELOPE_ADAPTER_VERSION = "0.9.0"
TRANSVERSE_ENVELOPE_SCOPE = "bounded-exact-rational-transverse-envelope-only"
TRANSVERSE_CARRIER_MAPPING_STATUS = "unmapped-sidecar"
TRANSVERSE_BOUND = Fraction(1)
TRANSVERSE_STRESS_MAX_DENOMINATOR = 8
TRANSVERSE_TRANSITION_LABELS = (
    "initiation",
    "advance-360",
    "advance-720",
    "inverse",
)
TRANSVERSE_COMPARISON_POLICY_NAME = "transverse-envelope-exact"
TRANSVERSE_COMPARISON_POLICY_VERSION = "0.9.0"
TRANSVERSE_COMPARISON_POLICY_CODE_REFERENCE = (
    "ucns.comparison:exact_comparison_policy"
)


class TransverseEnvelopeError(ValueError):
    """Raised when evidence violates the exact-rational envelope boundary."""


class TransverseCoordinateConvention(str, Enum):
    """Two reversible descriptions of one framed transverse sidecar."""

    LOCAL_FRAME = "local-frame-displacement"
    GLOBAL_SIDE = "global-side-displacement"


def transverse_exact_comparison_policy() -> ComparisonPolicy:
    """Return the named exact policy pinned by the v0.9 experiment."""

    return exact_comparison_policy(
        name=TRANSVERSE_COMPARISON_POLICY_NAME,
        version=TRANSVERSE_COMPARISON_POLICY_VERSION,
    )


def _validate_policy(policy: ComparisonPolicy) -> None:
    if not isinstance(policy, ComparisonPolicy):
        raise TypeError("comparison_policy must be ComparisonPolicy")
    if policy.name != TRANSVERSE_COMPARISON_POLICY_NAME:
        raise TransverseEnvelopeError("transverse comparison policy name is fixed")
    if policy.version != TRANSVERSE_COMPARISON_POLICY_VERSION:
        raise TransverseEnvelopeError("transverse comparison policy version is fixed")
    if policy.mode is not ComparisonMode.EXACT:
        raise TransverseEnvelopeError("transverse comparison policy must be exact")
    if policy.code_reference != TRANSVERSE_COMPARISON_POLICY_CODE_REFERENCE:
        raise TransverseEnvelopeError(
            "transverse comparison implementation reference is fixed"
        )


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise TransverseEnvelopeError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise TransverseEnvelopeError(f"{field} must retain at least one item")
    for value in values:
        _require_text(value, field)


def _exact_fraction(value: Fraction | int, field: str) -> Fraction:
    if isinstance(value, bool):
        raise TransverseEnvelopeError(f"{field} cannot be boolean")
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, Fraction):
        raise TransverseEnvelopeError(f"{field} must be int or exact Fraction")
    return value


def _validate_transverse(value: Fraction) -> None:
    if not isinstance(value, Fraction):
        raise TransverseEnvelopeError(
            "transverse coordinate must be an exact Fraction"
        )
    if abs(value) > TRANSVERSE_BOUND:
        raise TransverseEnvelopeError(
            "transverse coordinate exceeds the declared exact-rational bound"
        )


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def exact_rational_stress_fibers(
    max_denominator: int = TRANSVERSE_STRESS_MAX_DENOMINATOR,
) -> tuple[Fraction, ...]:
    """Return a deterministic reduced rational stress grid in ``[-1, +1]``.

    The grid is finite experiment evidence.  It is not presented as a proof
    over every rational value or as evidence of real-valued continuity.
    """

    if (
        isinstance(max_denominator, bool)
        or not isinstance(max_denominator, int)
        or max_denominator < 1
    ):
        raise TransverseEnvelopeError(
            "max_denominator must be a positive integer"
        )
    return tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for denominator in range(1, max_denominator + 1)
                for numerator in range(-denominator, denominator + 1)
            }
        )
    )


def _validate_fibers(fibers: tuple[Fraction, ...]) -> None:
    if not fibers:
        raise TransverseEnvelopeError("transverse stress domain cannot be empty")
    for value in fibers:
        _validate_transverse(value)
    if tuple(sorted(set(fibers))) != fibers:
        raise TransverseEnvelopeError(
            "transverse fibers must be unique and sorted exactly"
        )
    for required in (Fraction(-1), Fraction(0), Fraction(1)):
        if required not in fibers:
            raise TransverseEnvelopeError(
                "transverse fibers must retain -1, 0, and +1"
            )


def _native_root_identity(state: NativeMobiusState) -> tuple[object, ...]:
    return (
        state.complete_key,
        state.source_links,
        state.parent_observation_ids,
        state.initiation_event_id,
        state.completion_scope,
    )


def _native_identity(state: FramedMobiusStripState) -> tuple[object, ...]:
    return (
        _native_root_identity(state.root_state),
        _fraction_key(state.local_transverse),
        _fraction_key(state.global_transverse),
        state.scope,
    )


def _root_identity(state: RootLoopCoverChartState) -> tuple[object, ...]:
    return (
        state.complete_key,
        state.source_links,
        state.parent_observation_ids,
        state.initiation_event_id,
        state.completion_scope,
    )


@dataclass(frozen=True, slots=True)
class FramedMobiusStripState:
    """Native framed root-loop state plus one exact local transverse value."""

    root_state: NativeMobiusState
    local_transverse: Fraction
    scope: str = TRANSVERSE_ENVELOPE_SCOPE

    def __post_init__(self) -> None:
        if not isinstance(self.root_state, NativeMobiusState):
            raise TypeError("root_state must be NativeMobiusState")
        _validate_transverse(self.local_transverse)
        if self.scope != TRANSVERSE_ENVELOPE_SCOPE:
            raise TransverseEnvelopeError("native transverse scope is fixed")

    @property
    def global_transverse(self) -> Fraction:
        return self.root_state.frame.sign * self.local_transverse

    def advance(self, turns: Fraction | int) -> FramedMobiusStripState:
        displacement = _exact_fraction(turns, "native motion")
        return replace(self, root_state=self.root_state.advance(displacement))

    @property
    def complete_identity(self) -> tuple[object, ...]:
        return _native_identity(self)


@dataclass(frozen=True, slots=True)
class TransverseEnvelopeState:
    """A v0.7 root chart plus an explicit exact-rational sidecar."""

    root_chart: RootLoopCoverChartState
    transverse_coordinate: Fraction
    convention: TransverseCoordinateConvention
    adapter_id: str = TRANSVERSE_ENVELOPE_ADAPTER_ID
    adapter_version: str = TRANSVERSE_ENVELOPE_ADAPTER_VERSION
    adapter_scope: str = TRANSVERSE_ENVELOPE_SCOPE
    carrier_mapping_status: str = TRANSVERSE_CARRIER_MAPPING_STATUS

    def __post_init__(self) -> None:
        if not isinstance(self.root_chart, RootLoopCoverChartState):
            raise TypeError("root_chart must be RootLoopCoverChartState")
        _validate_transverse(self.transverse_coordinate)
        if not isinstance(self.convention, TransverseCoordinateConvention):
            raise TransverseEnvelopeError(
                "convention must be a TransverseCoordinateConvention"
            )
        if self.adapter_id != TRANSVERSE_ENVELOPE_ADAPTER_ID:
            raise TransverseEnvelopeError("transverse adapter identity is fixed")
        if self.adapter_version != TRANSVERSE_ENVELOPE_ADAPTER_VERSION:
            raise TransverseEnvelopeError("transverse adapter version is fixed")
        if self.adapter_scope != TRANSVERSE_ENVELOPE_SCOPE:
            raise TransverseEnvelopeError("transverse adapter scope is fixed")
        if self.carrier_mapping_status != TRANSVERSE_CARRIER_MAPPING_STATUS:
            raise TransverseEnvelopeError(
                "transverse value must remain explicitly unmapped in the cover"
            )

    @property
    def mapped_frame(self) -> NativeMobiusFrame:
        return self.root_chart.mapped_frame

    @property
    def local_transverse(self) -> Fraction:
        if self.convention is TransverseCoordinateConvention.LOCAL_FRAME:
            return self.transverse_coordinate
        return self.mapped_frame.sign * self.transverse_coordinate

    @property
    def global_transverse(self) -> Fraction:
        if self.convention is TransverseCoordinateConvention.GLOBAL_SIDE:
            return self.transverse_coordinate
        return self.mapped_frame.sign * self.transverse_coordinate

    @property
    def actual_cover_identity(self) -> tuple[object, ...]:
        """Return the unchanged v0.7 directed-cover chart coordinate identity."""

        return _root_identity(self.root_chart)

    @property
    def complete_identity(self) -> tuple[object, ...]:
        return (
            ("adapter", f"{self.adapter_id}@{self.adapter_version}"),
            ("scope", self.adapter_scope),
            ("carrier-mapping", self.carrier_mapping_status),
            ("convention", self.convention.value),
            ("root", self.actual_cover_identity),
            ("coordinate", _fraction_key(self.transverse_coordinate)),
            ("local", _fraction_key(self.local_transverse)),
            ("global", _fraction_key(self.global_transverse)),
        )

    def advance(self, turns: Fraction | int) -> TransverseEnvelopeState:
        displacement = _exact_fraction(turns, "envelope motion")
        new_root = self.root_chart.advance(displacement)
        local_transverse = self.local_transverse
        coordinate = (
            local_transverse
            if self.convention is TransverseCoordinateConvention.LOCAL_FRAME
            else new_root.mapped_frame.sign * local_transverse
        )
        return replace(
            self,
            root_chart=new_root,
            transverse_coordinate=coordinate,
        )


def _envelope_from_root_and_local(
    *,
    root_chart: RootLoopCoverChartState,
    local_transverse: Fraction,
    convention: TransverseCoordinateConvention,
) -> TransverseEnvelopeState:
    _validate_transverse(local_transverse)
    if not isinstance(convention, TransverseCoordinateConvention):
        raise TransverseEnvelopeError(
            "convention must be a TransverseCoordinateConvention"
        )
    coordinate = (
        local_transverse
        if convention is TransverseCoordinateConvention.LOCAL_FRAME
        else root_chart.mapped_frame.sign * local_transverse
    )
    return TransverseEnvelopeState(
        root_chart=root_chart,
        transverse_coordinate=coordinate,
        convention=convention,
    )


def mobius_to_transverse_envelope(
    state: FramedMobiusStripState,
    convention: TransverseCoordinateConvention,
) -> TransverseEnvelopeState:
    """Attach an exact transverse sidecar to the v0.7 root chart."""

    if not isinstance(state, FramedMobiusStripState):
        raise TypeError("state must be FramedMobiusStripState")
    return _envelope_from_root_and_local(
        root_chart=mobius_to_root_loop_cover(state.root_state),
        local_transverse=state.local_transverse,
        convention=convention,
    )


def transverse_envelope_to_mobius(
    state: TransverseEnvelopeState,
) -> FramedMobiusStripState:
    """Recover the framed native state from the explicit envelope."""

    if not isinstance(state, TransverseEnvelopeState):
        raise TypeError("state must be TransverseEnvelopeState")
    return FramedMobiusStripState(
        root_state=root_loop_cover_to_mobius(state.root_chart),
        local_transverse=state.local_transverse,
    )


def convert_transverse_convention(
    state: TransverseEnvelopeState,
    convention: TransverseCoordinateConvention,
) -> TransverseEnvelopeState:
    """Change exact sidecar convention without changing represented state."""

    if not isinstance(state, TransverseEnvelopeState):
        raise TypeError("state must be TransverseEnvelopeState")
    return _envelope_from_root_and_local(
        root_chart=state.root_chart,
        local_transverse=state.local_transverse,
        convention=convention,
    )


@dataclass(frozen=True, slots=True)
class TransverseEnvelopeRoundTrip:
    """Policy-bound two-way envelope evidence for one declared row."""

    event: MobiusInitiationEvent
    convention: TransverseCoordinateConvention
    native_original: FramedMobiusStripState
    envelope_image: TransverseEnvelopeState
    native_round_trip: FramedMobiusStripState
    envelope_round_trip: TransverseEnvelopeState
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _validate_policy(self.comparison_policy)
        if not self.comparison_policy.matches(
            _native_identity(self.native_original),
            _native_identity(
                FramedMobiusStripState(
                    self.event.post_state,
                    self.native_original.local_transverse,
                )
            ),
        ):
            raise TransverseEnvelopeError(
                "round trip must retain the event's exact native root state"
            )
        if not self.comparison_policy.matches(
            _native_identity(self.native_round_trip),
            _native_identity(self.native_original),
        ):
            raise TransverseEnvelopeError("native envelope round trip lost evidence")
        if not self.comparison_policy.matches(
            self.envelope_round_trip.complete_identity,
            self.envelope_image.complete_identity,
        ):
            raise TransverseEnvelopeError("envelope round trip lost evidence")
        if self.envelope_image.convention is not self.convention:
            raise TransverseEnvelopeError("envelope image lost its convention")
        if self.envelope_image.root_chart.initiation_event_id != self.event.event_id:
            raise TransverseEnvelopeError("envelope image lost initiation identity")
        boundary_link = f"boundary:{self.event.boundary.manifestation_id}"
        if boundary_link not in self.envelope_image.root_chart.source_links:
            raise TransverseEnvelopeError(
                "envelope image lost the Structural Null cause"
            )

    @property
    def evidence_key(self) -> tuple[str, str, str]:
        return (
            self.event.event_id,
            _fraction_key(self.native_original.local_transverse),
            self.convention.value,
        )


@dataclass(frozen=True, slots=True)
class RootLoopRestrictionWitness:
    """Policy-bound evidence that exact zero removes to the v0.7 root map."""

    event_id: str
    convention: TransverseCoordinateConvention
    native_envelope: FramedMobiusStripState
    cover_envelope: TransverseEnvelopeState
    expected_native_root: NativeMobiusState
    expected_cover_root: RootLoopCoverChartState
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        _validate_policy(self.comparison_policy)
        if self.native_envelope.local_transverse != 0:
            raise TransverseEnvelopeError("root restriction requires exact zero")
        if not self.comparison_policy.matches(
            _native_root_identity(self.native_envelope.root_state),
            _native_root_identity(self.expected_native_root),
        ):
            raise TransverseEnvelopeError("native zero fiber changed the v0.7 root")
        if not self.comparison_policy.matches(
            _root_identity(self.cover_envelope.root_chart),
            _root_identity(self.expected_cover_root),
        ):
            raise TransverseEnvelopeError("zero sidecar changed the v0.7 chart")
        if self.cover_envelope.local_transverse != 0:
            raise TransverseEnvelopeError("cover envelope zero must remain exact")

    @property
    def evidence_key(self) -> tuple[str, str]:
        return self.event_id, self.convention.value


@dataclass(frozen=True, slots=True)
class TransverseMotionWitness:
    """Policy-bound commutation evidence for one envelope transition."""

    event_id: str
    label: str
    convention: TransverseCoordinateConvention
    local_transverse: Fraction
    turns: Fraction
    expected: TransverseEnvelopeState
    observed: TransverseEnvelopeState
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        _validate_policy(self.comparison_policy)
        if self.label not in TRANSVERSE_TRANSITION_LABELS:
            raise TransverseEnvelopeError("unknown transverse transition label")
        _validate_transverse(self.local_transverse)
        if not isinstance(self.turns, Fraction):
            raise TransverseEnvelopeError("transition turns must be exact")
        if not self.comparison_policy.matches(
            self.expected.complete_identity,
            self.observed.complete_identity,
        ):
            raise TransverseEnvelopeError(
                "transverse envelope does not commute exactly"
            )

    @property
    def evidence_key(self) -> tuple[str, str, str, str]:
        return (
            self.event_id,
            _fraction_key(self.local_transverse),
            self.convention.value,
            self.label,
        )


@dataclass(frozen=True, slots=True)
class ConventionRoundTripWitness:
    """Policy-bound two-way coordinate-description evidence."""

    event_id: str
    native_state: FramedMobiusStripState
    local_state: TransverseEnvelopeState
    global_state: TransverseEnvelopeState
    local_round_trip: TransverseEnvelopeState
    global_round_trip: TransverseEnvelopeState
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        _validate_policy(self.comparison_policy)
        if self.local_state.convention is not TransverseCoordinateConvention.LOCAL_FRAME:
            raise TransverseEnvelopeError("local convention witness is mislabeled")
        if self.global_state.convention is not TransverseCoordinateConvention.GLOBAL_SIDE:
            raise TransverseEnvelopeError("global convention witness is mislabeled")
        if not self.comparison_policy.matches(
            self.local_round_trip.complete_identity,
            self.local_state.complete_identity,
        ):
            raise TransverseEnvelopeError("local convention round trip failed")
        if not self.comparison_policy.matches(
            self.global_round_trip.complete_identity,
            self.global_state.complete_identity,
        ):
            raise TransverseEnvelopeError("global convention round trip failed")
        if not self.comparison_policy.matches(
            _native_identity(transverse_envelope_to_mobius(self.local_state)),
            _native_identity(transverse_envelope_to_mobius(self.global_state)),
        ):
            raise TransverseEnvelopeError("coordinate change altered represented state")

    @property
    def evidence_key(self) -> tuple[str, str]:
        return self.event_id, _fraction_key(self.native_state.local_transverse)


@dataclass(frozen=True, slots=True)
class ConventionMotionWitness:
    """Policy-bound coordinate-change and motion commutation evidence."""

    event_id: str
    label: str
    local_transverse: Fraction
    turns: Fraction
    expected_global: TransverseEnvelopeState
    observed_global: TransverseEnvelopeState
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        _validate_policy(self.comparison_policy)
        if self.label not in TRANSVERSE_TRANSITION_LABELS:
            raise TransverseEnvelopeError("unknown convention transition label")
        _validate_transverse(self.local_transverse)
        if not isinstance(self.turns, Fraction):
            raise TransverseEnvelopeError("transition turns must be exact")
        if not self.comparison_policy.matches(
            self.expected_global.complete_identity,
            self.observed_global.complete_identity,
        ):
            raise TransverseEnvelopeError(
                "coordinate change does not commute with motion"
            )

    @property
    def evidence_key(self) -> tuple[str, str, str]:
        return (
            self.event_id,
            _fraction_key(self.local_transverse),
            self.label,
        )


@dataclass(frozen=True, slots=True)
class TransverseCarrierCollisionWitness:
    """Evidence that the sidecar is not mapped into the actual cover."""

    event_id: str
    convention: TransverseCoordinateConvention
    first: TransverseEnvelopeState
    second: TransverseEnvelopeState
    comparison_policy: ComparisonPolicy

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        _validate_policy(self.comparison_policy)
        if self.first.convention is not self.convention:
            raise TransverseEnvelopeError("first collision convention is mislabeled")
        if self.second.convention is not self.convention:
            raise TransverseEnvelopeError("second collision convention is mislabeled")
        if self.first.local_transverse == self.second.local_transverse:
            raise TransverseEnvelopeError(
                "collision witness requires distinct transverse values"
            )
        if self.comparison_policy.matches(
            self.first.complete_identity,
            self.second.complete_identity,
        ):
            raise TransverseEnvelopeError(
                "distinct transverse envelopes must retain distinct identities"
            )
        if not self.comparison_policy.matches(
            self.first.actual_cover_identity,
            self.second.actual_cover_identity,
        ):
            raise TransverseEnvelopeError(
                "collision witness must share one actual cover coordinate"
            )

    @property
    def evidence_key(self) -> tuple[str, str]:
        return self.event_id, self.convention.value


def build_transverse_round_trips(
    packet: NativeMobiusInitiationPacket,
    fibers: tuple[Fraction, ...],
    comparison_policy: ComparisonPolicy,
) -> tuple[TransverseEnvelopeRoundTrip, ...]:
    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    _validate_fibers(fibers)
    _validate_policy(comparison_policy)
    rows: list[TransverseEnvelopeRoundTrip] = []
    for event in packet.initiations:
        for local_transverse in fibers:
            native = FramedMobiusStripState(event.post_state, local_transverse)
            for convention in TransverseCoordinateConvention:
                envelope = mobius_to_transverse_envelope(native, convention)
                native_round_trip = transverse_envelope_to_mobius(envelope)
                rows.append(
                    TransverseEnvelopeRoundTrip(
                        event=event,
                        convention=convention,
                        native_original=native,
                        envelope_image=envelope,
                        native_round_trip=native_round_trip,
                        envelope_round_trip=mobius_to_transverse_envelope(
                            native_round_trip,
                            convention,
                        ),
                        comparison_policy=comparison_policy,
                    )
                )
    return tuple(rows)


def build_root_loop_restrictions(
    packet: NativeMobiusInitiationPacket,
    comparison_policy: ComparisonPolicy,
) -> tuple[RootLoopRestrictionWitness, ...]:
    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    _validate_policy(comparison_policy)
    witnesses: list[RootLoopRestrictionWitness] = []
    for event in packet.initiations:
        native = FramedMobiusStripState(event.post_state, Fraction(0))
        expected_cover = mobius_to_root_loop_cover(event.post_state)
        for convention in TransverseCoordinateConvention:
            witnesses.append(
                RootLoopRestrictionWitness(
                    event_id=event.event_id,
                    convention=convention,
                    native_envelope=native,
                    cover_envelope=mobius_to_transverse_envelope(
                        native,
                        convention,
                    ),
                    expected_native_root=event.post_state,
                    expected_cover_root=expected_cover,
                    comparison_policy=comparison_policy,
                )
            )
    return tuple(witnesses)


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
    raise TransverseEnvelopeError("unknown transverse transition label")


def build_transverse_motion_witnesses(
    packet: NativeMobiusInitiationPacket,
    fibers: tuple[Fraction, ...],
    comparison_policy: ComparisonPolicy,
) -> tuple[TransverseMotionWitness, ...]:
    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    _validate_fibers(fibers)
    _validate_policy(comparison_policy)
    witnesses: list[TransverseMotionWitness] = []
    for event in packet.initiations:
        for local_transverse in fibers:
            initial = FramedMobiusStripState(event.post_state, local_transverse)
            for convention in TransverseCoordinateConvention:
                for label in TRANSVERSE_TRANSITION_LABELS:
                    start, turns = _motion_inputs(initial, label)
                    witnesses.append(
                        TransverseMotionWitness(
                            event_id=event.event_id,
                            label=label,
                            convention=convention,
                            local_transverse=local_transverse,
                            turns=turns,
                            expected=mobius_to_transverse_envelope(
                                start.advance(turns),
                                convention,
                            ),
                            observed=mobius_to_transverse_envelope(
                                start,
                                convention,
                            ).advance(turns),
                            comparison_policy=comparison_policy,
                        )
                    )
    return tuple(witnesses)


def build_convention_round_trips(
    packet: NativeMobiusInitiationPacket,
    fibers: tuple[Fraction, ...],
    comparison_policy: ComparisonPolicy,
) -> tuple[ConventionRoundTripWitness, ...]:
    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    _validate_fibers(fibers)
    _validate_policy(comparison_policy)
    witnesses: list[ConventionRoundTripWitness] = []
    for event in packet.initiations:
        for local_transverse in fibers:
            native = FramedMobiusStripState(event.post_state, local_transverse)
            local_state = mobius_to_transverse_envelope(
                native,
                TransverseCoordinateConvention.LOCAL_FRAME,
            )
            global_state = mobius_to_transverse_envelope(
                native,
                TransverseCoordinateConvention.GLOBAL_SIDE,
            )
            witnesses.append(
                ConventionRoundTripWitness(
                    event_id=event.event_id,
                    native_state=native,
                    local_state=local_state,
                    global_state=global_state,
                    local_round_trip=convert_transverse_convention(
                        convert_transverse_convention(
                            local_state,
                            TransverseCoordinateConvention.GLOBAL_SIDE,
                        ),
                        TransverseCoordinateConvention.LOCAL_FRAME,
                    ),
                    global_round_trip=convert_transverse_convention(
                        convert_transverse_convention(
                            global_state,
                            TransverseCoordinateConvention.LOCAL_FRAME,
                        ),
                        TransverseCoordinateConvention.GLOBAL_SIDE,
                    ),
                    comparison_policy=comparison_policy,
                )
            )
    return tuple(witnesses)


def build_convention_motion_witnesses(
    packet: NativeMobiusInitiationPacket,
    fibers: tuple[Fraction, ...],
    comparison_policy: ComparisonPolicy,
) -> tuple[ConventionMotionWitness, ...]:
    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    _validate_fibers(fibers)
    _validate_policy(comparison_policy)
    witnesses: list[ConventionMotionWitness] = []
    for event in packet.initiations:
        for local_transverse in fibers:
            initial = FramedMobiusStripState(event.post_state, local_transverse)
            for label in TRANSVERSE_TRANSITION_LABELS:
                start, turns = _motion_inputs(initial, label)
                local_start = mobius_to_transverse_envelope(
                    start,
                    TransverseCoordinateConvention.LOCAL_FRAME,
                )
                witnesses.append(
                    ConventionMotionWitness(
                        event_id=event.event_id,
                        label=label,
                        local_transverse=local_transverse,
                        turns=turns,
                        expected_global=convert_transverse_convention(
                            local_start.advance(turns),
                            TransverseCoordinateConvention.GLOBAL_SIDE,
                        ),
                        observed_global=convert_transverse_convention(
                            local_start,
                            TransverseCoordinateConvention.GLOBAL_SIDE,
                        ).advance(turns),
                        comparison_policy=comparison_policy,
                    )
                )
    return tuple(witnesses)


def build_transverse_carrier_collisions(
    packet: NativeMobiusInitiationPacket,
    comparison_policy: ComparisonPolicy,
) -> tuple[TransverseCarrierCollisionWitness, ...]:
    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    _validate_policy(comparison_policy)
    collisions: list[TransverseCarrierCollisionWitness] = []
    for event in packet.initiations:
        negative = FramedMobiusStripState(event.post_state, Fraction(-1))
        positive = FramedMobiusStripState(event.post_state, Fraction(1))
        for convention in TransverseCoordinateConvention:
            collisions.append(
                TransverseCarrierCollisionWitness(
                    event_id=event.event_id,
                    convention=convention,
                    first=mobius_to_transverse_envelope(negative, convention),
                    second=mobius_to_transverse_envelope(positive, convention),
                    comparison_policy=comparison_policy,
                )
            )
    return tuple(collisions)


@dataclass(frozen=True, slots=True)
class TransverseEnvelopeReport:
    """Complete v0.9 repair evidence with exhaustive identity validation."""

    report_id: str
    root_report: RootLoopChartReport
    fibers: tuple[Fraction, ...]
    comparison_policy: ComparisonPolicy
    round_trips: tuple[TransverseEnvelopeRoundTrip, ...]
    root_restrictions: tuple[RootLoopRestrictionWitness, ...]
    motion_witnesses: tuple[TransverseMotionWitness, ...]
    convention_round_trips: tuple[ConventionRoundTripWitness, ...]
    convention_motion_witnesses: tuple[ConventionMotionWitness, ...]
    carrier_collisions: tuple[TransverseCarrierCollisionWitness, ...]
    experiment: CarrierExperimentReport
    transverse_cover_verdict: FalsifierVerdict
    hmmm: tuple[str, ...]
    candidate_id: str = TRANSVERSE_ENVELOPE_ADAPTER_ID
    candidate_version: str = TRANSVERSE_ENVELOPE_ADAPTER_VERSION
    code_reference: str = (
        "ucns.transverse_envelope:run_v09_transverse_envelope_experiment"
    )
    schema_id: str = V09_TRANSVERSE_ENVELOPE_SCHEMA_ID
    schema_version: str = V09_TRANSVERSE_ENVELOPE_SCHEMA_VERSION
    selection_effect: str = V09_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.report_id, "report_id")
        _validate_policy(self.comparison_policy)
        _validate_fibers(self.fibers)
        if self.candidate_id != TRANSVERSE_ENVELOPE_ADAPTER_ID:
            raise TransverseEnvelopeError("v0.9 candidate identity mismatch")
        if self.candidate_version != TRANSVERSE_ENVELOPE_ADAPTER_VERSION:
            raise TransverseEnvelopeError("v0.9 candidate version mismatch")
        if self.code_reference != (
            "ucns.transverse_envelope:run_v09_transverse_envelope_experiment"
        ):
            raise TransverseEnvelopeError("v0.9 code reference mismatch")
        if self.schema_id != V09_TRANSVERSE_ENVELOPE_SCHEMA_ID:
            raise TransverseEnvelopeError("v0.9 schema identity mismatch")
        if self.schema_version != V09_TRANSVERSE_ENVELOPE_SCHEMA_VERSION:
            raise TransverseEnvelopeError("v0.9 schema version mismatch")
        if self.selection_effect != V09_SELECTION_EFFECT:
            raise TransverseEnvelopeError("v0.9 cannot select a carrier")
        if self.experiment.selection_effect != V09_SELECTION_EFFECT:
            raise TransverseEnvelopeError("embedded experiment cannot select a carrier")
        if not self.comparison_policy.matches(
            self.experiment,
            self.root_report.experiment,
        ):
            raise TransverseEnvelopeError(
                "transverse evidence cannot alter the v0.7 carrier verdict matrix"
            )
        if self.transverse_cover_verdict is not FalsifierVerdict.INCONCLUSIVE:
            raise TransverseEnvelopeError(
                "transverse cover extension must remain inconclusive"
            )

        packet = self.root_report.direct_report.packet
        event_ids = tuple(item.event_id for item in packet.initiations)
        fiber_keys = tuple(_fraction_key(value) for value in self.fibers)
        convention_keys = tuple(item.value for item in TransverseCoordinateConvention)

        expected_round_trip_keys = tuple(
            (event_id, fiber, convention)
            for event_id in event_ids
            for fiber in fiber_keys
            for convention in convention_keys
        )
        if tuple(item.evidence_key for item in self.round_trips) != (
            expected_round_trip_keys
        ):
            raise TransverseEnvelopeError(
                "round trips must cover every event/fiber/convention exactly in order"
            )
        expected_round_trip_events = tuple(
            event
            for event in packet.initiations
            for _fiber in self.fibers
            for _convention in TransverseCoordinateConvention
        )
        if not self.comparison_policy.matches(
            tuple(item.event for item in self.round_trips),
            expected_round_trip_events,
        ):
            raise TransverseEnvelopeError(
                "round-trip events must cross-check against the v0.7 root packet"
            )

        expected_restriction_keys = tuple(
            (event_id, convention)
            for event_id in event_ids
            for convention in convention_keys
        )
        if tuple(item.evidence_key for item in self.root_restrictions) != (
            expected_restriction_keys
        ):
            raise TransverseEnvelopeError(
                "root restrictions must cover every event/convention exactly"
            )

        expected_motion_keys = tuple(
            (event_id, fiber, convention, label)
            for event_id in event_ids
            for fiber in fiber_keys
            for convention in convention_keys
            for label in TRANSVERSE_TRANSITION_LABELS
        )
        if tuple(item.evidence_key for item in self.motion_witnesses) != (
            expected_motion_keys
        ):
            raise TransverseEnvelopeError(
                "motion witnesses must cover every declared transition exactly"
            )

        expected_convention_keys = tuple(
            (event_id, fiber)
            for event_id in event_ids
            for fiber in fiber_keys
        )
        if tuple(item.evidence_key for item in self.convention_round_trips) != (
            expected_convention_keys
        ):
            raise TransverseEnvelopeError(
                "coordinate round trips must cover every native state exactly"
            )

        expected_convention_motion_keys = tuple(
            (event_id, fiber, label)
            for event_id in event_ids
            for fiber in fiber_keys
            for label in TRANSVERSE_TRANSITION_LABELS
        )
        if tuple(
            item.evidence_key for item in self.convention_motion_witnesses
        ) != expected_convention_motion_keys:
            raise TransverseEnvelopeError(
                "coordinate motion witnesses must cover every transition exactly"
            )

        if tuple(item.evidence_key for item in self.carrier_collisions) != (
            expected_restriction_keys
        ):
            raise TransverseEnvelopeError(
                "cover collisions must cover every event/convention exactly"
            )

        f12 = self.experiment.result(CarrierRelationship.COVER_CHART, "F12")
        f13 = self.experiment.result(CarrierRelationship.INCOMPATIBLE, "F13")
        root_map_key = f"map:{ROOT_LOOP_CHART_MAP_ID}@{ROOT_LOOP_CHART_MAP_VERSION}"
        if root_map_key not in f12.evidence or root_map_key not in f13.evidence:
            raise TransverseEnvelopeError(
                "F12/F13 must retain the v0.7 root map identity"
            )
        if any(self.candidate_id in item for item in (*f12.evidence, *f13.evidence)):
            raise TransverseEnvelopeError(
                "transverse envelope identity cannot be attributed to F12/F13"
            )
        _require_text_items(self.hmmm, "hmmm")


def run_v09_transverse_envelope_experiment(
    *,
    report_id: str = "ucns-edcm-v0.9:exact-rational-transverse-envelope",
    max_denominator: int = TRANSVERSE_STRESS_MAX_DENOMINATOR,
) -> TransverseEnvelopeReport:
    """Run the repair and finite exact-rational stress experiment."""

    root_report = run_v07_root_loop_chart_experiment(
        report_id=f"{report_id}:root-loop"
    )
    packet = root_report.direct_report.packet
    fibers = exact_rational_stress_fibers(max_denominator)
    policy = transverse_exact_comparison_policy()
    return TransverseEnvelopeReport(
        report_id=report_id,
        root_report=root_report,
        fibers=fibers,
        comparison_policy=policy,
        round_trips=build_transverse_round_trips(packet, fibers, policy),
        root_restrictions=build_root_loop_restrictions(packet, policy),
        motion_witnesses=build_transverse_motion_witnesses(
            packet,
            fibers,
            policy,
        ),
        convention_round_trips=build_convention_round_trips(
            packet,
            fibers,
            policy,
        ),
        convention_motion_witnesses=build_convention_motion_witnesses(
            packet,
            fibers,
            policy,
        ),
        carrier_collisions=build_transverse_carrier_collisions(packet, policy),
        experiment=root_report.experiment,
        transverse_cover_verdict=FalsifierVerdict.INCONCLUSIVE,
        hmmm=(
            "v0.8 is reclassified as a transverse envelope over the v0.7 root chart, not a transverse directed-cover embedding",
            "the exact-rational adapter is parametric, while the report supplies only a finite denominator-bounded stress domain rather than a theorem over all rationals",
            "distinct transverse envelopes collide at the same actual directed-cover coordinate until an injective transverse or radial assignment is supplied",
            "F12 support and F13 falsification remain bounded to the v0.7 root-loop map",
            "no coordinate convention, carrier, faithful breadth, radial law, completion law, EDCM activation, or METAPAT activation is selected",
        ),
    )


__all__ = [
    "TRANSVERSE_BOUND",
    "TRANSVERSE_CARRIER_MAPPING_STATUS",
    "TRANSVERSE_COMPARISON_POLICY_CODE_REFERENCE",
    "TRANSVERSE_COMPARISON_POLICY_NAME",
    "TRANSVERSE_COMPARISON_POLICY_VERSION",
    "TRANSVERSE_ENVELOPE_ADAPTER_ID",
    "TRANSVERSE_ENVELOPE_ADAPTER_VERSION",
    "TRANSVERSE_ENVELOPE_SCOPE",
    "TRANSVERSE_STRESS_MAX_DENOMINATOR",
    "TRANSVERSE_TRANSITION_LABELS",
    "V09_SELECTION_EFFECT",
    "V09_TRANSVERSE_ENVELOPE_SCHEMA_ID",
    "V09_TRANSVERSE_ENVELOPE_SCHEMA_VERSION",
    "ConventionMotionWitness",
    "ConventionRoundTripWitness",
    "FramedMobiusStripState",
    "RootLoopRestrictionWitness",
    "TransverseCarrierCollisionWitness",
    "TransverseCoordinateConvention",
    "TransverseEnvelopeError",
    "TransverseEnvelopeReport",
    "TransverseEnvelopeRoundTrip",
    "TransverseEnvelopeState",
    "TransverseMotionWitness",
    "build_convention_motion_witnesses",
    "build_convention_round_trips",
    "build_root_loop_restrictions",
    "build_transverse_carrier_collisions",
    "build_transverse_motion_witnesses",
    "build_transverse_round_trips",
    "convert_transverse_convention",
    "exact_rational_stress_fibers",
    "mobius_to_transverse_envelope",
    "run_v09_transverse_envelope_experiment",
    "transverse_envelope_to_mobius",
    "transverse_exact_comparison_policy",
]
