# === MODULE_BUILD ===
# id: edcm_transverse_strip_cover_chart_candidate
#   module_name: transverse_strip_chart
#   module_kind: experiment
#   summary: extends the bounded root-loop chart across three exact transverse witness fibers while preserving local-frame and global-side coordinate conventions
#   owner: Erin Spencer
#   public_surface: FramedMobiusStripState, TransverseCoverChartState, TransverseCoordinateConvention, TransverseStripReport, mobius_to_transverse_cover, transverse_cover_to_mobius, convert_transverse_convention, build_transverse_round_trips, build_transverse_motion_witnesses, run_v08_transverse_strip_experiment
#   internal_surface: exact coordinate adapters, convention-change witnesses, root restriction witnesses, and report-matrix extension
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and native completion scope remain linked through every transverse map
#   admin_only: false
#   tests: tests/test_transverse_strip_chart.py
#   rollout: explicit UCNS-only v0.8 bounded transverse witness experiment; no radial assignment, arbitrary-element assignment, global carrier equivalence, carrier selection, completion, EDCM activation, or METAPAT activation
#   rollback: remove this module, its exports, tests, and v0.8 candidate document while retaining the v0.5 through v0.7 experiments
#   requires: edcm_root_loop_cover_chart_candidate, edcm_native_direct_mobius_candidate
#   since: 2026-07-29
#   unresolved: radial and faithful-breadth assignment, arbitrary element assignment, continuous-strip generality, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: transverse_strip_maps_are_exact_two_way_inverses
#   given: an exact rational framed transverse state inside the declared bound and either admitted coordinate convention
#   then: native-to-cover-to-native and cover-to-native-to-cover restore every retained distinction exactly
#   class: correctness
#   since: 2026-07-29
#
# id: transverse_strip_preserves_every_source_linked_witness
#   given: all fourteen minimum-packet initiations are crossed with the negative, zero, and positive transverse witnesses under both coordinate conventions
#   then: all eighty-four map rows retain exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and native completion scope
#   class: evidence
#   since: 2026-07-29
#
# id: transverse_strip_restricts_exactly_to_v07_root_loop
#   given: the transverse coordinate is exact zero
#   then: removing the transverse coordinate recovers the unchanged v0.7 native and cover root-loop states for every initiation and both conventions
#   class: correctness
#   since: 2026-07-29
#
# id: transverse_strip_commutes_with_bounded_motion
#   given: initiation, positive 360-degree motion, positive 720-degree motion, and inverse 360-degree motion are evaluated for every declared transverse map row
#   then: mapping after native motion exactly equals chart motion after mapping
#   class: correctness
#   since: 2026-07-29
#
# id: transverse_coordinate_conventions_remain_reversible_and_nonselecting
#   given: local-frame displacement and global-side displacement are compared on the same bounded state
#   then: their exact sheet-aware change of coordinates and bounded motion commute in both directions without appointing either convention as canonical
#   class: safety
#   since: 2026-07-29
#
# id: transverse_strip_support_is_bounded_and_nonselecting
#   given: the complete v0.8 report is produced
#   then: F12 is supported and F13 falsified only for the declared finite transverse witness packet while selection remains none and radial assignment, continuous-strip generality, arbitrary elements, completion, higher geometry, EDCM, and METAPAT remain unresolved
#   class: doctrine
#   since: 2026-07-29
# === END CONTRACTS ===

"""Bounded framed-transverse C1↔C2 chart experiment for UCNS–EDCM v0.8.

The v0.7 map relates the framed native root loop to the first and second
representatives of the directed cover.  This module adds one exact local
transverse coordinate ``u`` while retaining the v0.7 state as an explicit
subobject.

Two coordinate conventions remain admissible:

* ``local-frame`` keeps ``u`` fixed when the native frame changes;
* ``global-side`` records ``frame.sign * u`` and therefore changes sign after
  one visible turn.

They are joined by an exact sheet-aware change of coordinates.  The experiment
does not select one convention.  It evaluates the complete minimum initiation
packet at the three exact witnesses ``u = -1, 0, +1``.  The implementation can
represent other exact rational values inside the bound, but the report does not
claim continuous-strip generality from the finite witness packet.

The coordinate is transverse only.  It is not faithful breadth, carrier radius,
arbitrary-element assignment, higher geometry, or scoped completion.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from fractions import Fraction

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
    RootLoopChartReport,
    RootLoopCoverChartState,
    mobius_to_root_loop_cover,
    root_loop_cover_to_mobius,
    run_v07_root_loop_chart_experiment,
)


V08_TRANSVERSE_STRIP_SCHEMA_ID = "ucns.edcm.transverse-strip-cover-chart"
V08_TRANSVERSE_STRIP_SCHEMA_VERSION = "0.8.0"
V08_SELECTION_EFFECT = "none"
TRANSVERSE_STRIP_MAP_ID = "ucns.edcm.mobius-directed-cover-transverse-strip-chart"
TRANSVERSE_STRIP_MAP_VERSION = "0.8.0"
TRANSVERSE_STRIP_SCOPE = "bounded-framed-transverse-witness-domain-only"
TRANSVERSE_BOUND = Fraction(1)
TRANSVERSE_WITNESS_VALUES = (
    Fraction(-1),
    Fraction(0),
    Fraction(1),
)
TRANSVERSE_TRANSITION_LABELS = (
    "initiation",
    "advance-360",
    "advance-720",
    "inverse",
)


class TransverseStripError(ValueError):
    """Raised when evidence crosses or violates the bounded v0.8 contract."""


class TransverseCoordinateConvention(str, Enum):
    """Admitted exact coordinate descriptions of the same framed fiber."""

    LOCAL_FRAME = "local-frame-displacement"
    GLOBAL_SIDE = "global-side-displacement"


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise TransverseStripError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise TransverseStripError(f"{field} must retain at least one item")
    for value in values:
        _require_text(value, field)


def _exact_fraction(value: Fraction | int, field: str) -> Fraction:
    if isinstance(value, bool):
        raise TransverseStripError(f"{field} cannot be boolean")
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, Fraction):
        raise TransverseStripError(f"{field} must be int or exact Fraction")
    return value


def _validate_transverse(value: Fraction) -> None:
    if not isinstance(value, Fraction):
        raise TransverseStripError("transverse coordinate must be an exact Fraction")
    if abs(value) > TRANSVERSE_BOUND:
        raise TransverseStripError("transverse coordinate exceeds the declared bound")


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True, slots=True)
class FramedMobiusStripState:
    """Native framed root-loop state plus one exact local transverse coordinate."""

    root_state: NativeMobiusState
    local_transverse: Fraction
    map_scope: str = TRANSVERSE_STRIP_SCOPE

    def __post_init__(self) -> None:
        if not isinstance(self.root_state, NativeMobiusState):
            raise TypeError("root_state must be NativeMobiusState")
        _validate_transverse(self.local_transverse)
        if self.map_scope != TRANSVERSE_STRIP_SCOPE:
            raise TransverseStripError("transverse strip scope is fixed")

    @property
    def global_transverse(self) -> Fraction:
        return self.root_state.frame.sign * self.local_transverse

    def advance(self, turns: Fraction | int) -> FramedMobiusStripState:
        """Advance native motion while retaining local-frame displacement."""

        displacement = _exact_fraction(turns, "turn motion")
        return replace(self, root_state=self.root_state.advance(displacement))

    @property
    def complete_key(self) -> tuple[tuple[str, str], ...]:
        return (
            *self.root_state.complete_key,
            ("local-transverse", _fraction_key(self.local_transverse)),
            ("global-transverse", _fraction_key(self.global_transverse)),
            ("scope", self.map_scope),
        )


@dataclass(frozen=True, slots=True)
class TransverseCoverChartState:
    """Exact v0.7 cover root plus one explicitly interpreted coordinate."""

    root_chart: RootLoopCoverChartState
    transverse_coordinate: Fraction
    convention: TransverseCoordinateConvention
    map_id: str = TRANSVERSE_STRIP_MAP_ID
    map_version: str = TRANSVERSE_STRIP_MAP_VERSION
    map_scope: str = TRANSVERSE_STRIP_SCOPE

    def __post_init__(self) -> None:
        if not isinstance(self.root_chart, RootLoopCoverChartState):
            raise TypeError("root_chart must be RootLoopCoverChartState")
        _validate_transverse(self.transverse_coordinate)
        if not isinstance(self.convention, TransverseCoordinateConvention):
            raise TransverseStripError(
                "convention must be a TransverseCoordinateConvention"
            )
        if self.map_id != TRANSVERSE_STRIP_MAP_ID:
            raise TransverseStripError("transverse map identity is fixed")
        if self.map_version != TRANSVERSE_STRIP_MAP_VERSION:
            raise TransverseStripError("transverse map version is fixed")
        if self.map_scope != TRANSVERSE_STRIP_SCOPE:
            raise TransverseStripError("transverse map scope is fixed")

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

    def advance(self, turns: Fraction | int) -> TransverseCoverChartState:
        """Advance the root chart and update the declared coordinate exactly."""

        displacement = _exact_fraction(turns, "chart motion")
        new_root = self.root_chart.advance(displacement)
        local_transverse = self.local_transverse
        if self.convention is TransverseCoordinateConvention.LOCAL_FRAME:
            coordinate = local_transverse
        else:
            coordinate = new_root.mapped_frame.sign * local_transverse
        return replace(
            self,
            root_chart=new_root,
            transverse_coordinate=coordinate,
        )

    @property
    def complete_key(self) -> tuple[tuple[str, str], ...]:
        return (
            ("map", f"{self.map_id}@{self.map_version}"),
            ("convention", self.convention.value),
            ("lifted-turns", _fraction_key(self.root_chart.lifted_turns)),
            ("transverse-coordinate", _fraction_key(self.transverse_coordinate)),
            ("local-transverse", _fraction_key(self.local_transverse)),
            ("global-transverse", _fraction_key(self.global_transverse)),
        )


def _cover_from_root_and_local(
    *,
    root_chart: RootLoopCoverChartState,
    local_transverse: Fraction,
    convention: TransverseCoordinateConvention,
) -> TransverseCoverChartState:
    _validate_transverse(local_transverse)
    if not isinstance(convention, TransverseCoordinateConvention):
        raise TransverseStripError(
            "convention must be a TransverseCoordinateConvention"
        )
    if convention is TransverseCoordinateConvention.LOCAL_FRAME:
        coordinate = local_transverse
    else:
        coordinate = root_chart.mapped_frame.sign * local_transverse
    return TransverseCoverChartState(
        root_chart=root_chart,
        transverse_coordinate=coordinate,
        convention=convention,
    )


def mobius_to_transverse_cover(
    state: FramedMobiusStripState,
    convention: TransverseCoordinateConvention,
) -> TransverseCoverChartState:
    """Map one exact framed native strip state into the chosen cover chart."""

    if not isinstance(state, FramedMobiusStripState):
        raise TypeError("state must be FramedMobiusStripState")
    return _cover_from_root_and_local(
        root_chart=mobius_to_root_loop_cover(state.root_state),
        local_transverse=state.local_transverse,
        convention=convention,
    )


def transverse_cover_to_mobius(
    state: TransverseCoverChartState,
) -> FramedMobiusStripState:
    """Recover the exact native framed strip state from either convention."""

    if not isinstance(state, TransverseCoverChartState):
        raise TypeError("state must be TransverseCoverChartState")
    return FramedMobiusStripState(
        root_state=root_loop_cover_to_mobius(state.root_chart),
        local_transverse=state.local_transverse,
    )


def convert_transverse_convention(
    state: TransverseCoverChartState,
    convention: TransverseCoordinateConvention,
) -> TransverseCoverChartState:
    """Change exact coordinate convention without changing represented state."""

    if not isinstance(state, TransverseCoverChartState):
        raise TypeError("state must be TransverseCoverChartState")
    return _cover_from_root_and_local(
        root_chart=state.root_chart,
        local_transverse=state.local_transverse,
        convention=convention,
    )


@dataclass(frozen=True, slots=True)
class TransverseStripRoundTrip:
    """Two-way map evidence for one initiation, fiber, and convention."""

    event: MobiusInitiationEvent
    convention: TransverseCoordinateConvention
    native_original: FramedMobiusStripState
    cover_image: TransverseCoverChartState
    native_round_trip: FramedMobiusStripState
    cover_round_trip: TransverseCoverChartState

    def __post_init__(self) -> None:
        if self.native_original.root_state != self.event.post_state:
            raise TransverseStripError(
                "round trip must retain the event's exact native root state"
            )
        if self.native_round_trip != self.native_original:
            raise TransverseStripError("native round trip lost a distinction")
        if self.cover_round_trip != self.cover_image:
            raise TransverseStripError("cover round trip lost a distinction")
        if self.cover_image.convention is not self.convention:
            raise TransverseStripError("cover image lost coordinate convention")
        if (
            self.cover_image.root_chart.initiation_event_id
            != self.event.event_id
        ):
            raise TransverseStripError("cover image lost initiation identity")
        boundary_link = f"boundary:{self.event.boundary.manifestation_id}"
        if boundary_link not in self.cover_image.root_chart.source_links:
            raise TransverseStripError("cover image lost Structural Null cause")


def build_transverse_round_trips(
    packet: NativeMobiusInitiationPacket,
) -> tuple[TransverseStripRoundTrip, ...]:
    """Cross every initiation with every fiber and both coordinate conventions."""

    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    rows: list[TransverseStripRoundTrip] = []
    for event in packet.initiations:
        for local_transverse in TRANSVERSE_WITNESS_VALUES:
            native_original = FramedMobiusStripState(
                root_state=event.post_state,
                local_transverse=local_transverse,
            )
            for convention in TransverseCoordinateConvention:
                cover_image = mobius_to_transverse_cover(
                    native_original,
                    convention,
                )
                native_round_trip = transverse_cover_to_mobius(cover_image)
                cover_round_trip = mobius_to_transverse_cover(
                    native_round_trip,
                    convention,
                )
                rows.append(
                    TransverseStripRoundTrip(
                        event=event,
                        convention=convention,
                        native_original=native_original,
                        cover_image=cover_image,
                        native_round_trip=native_round_trip,
                        cover_round_trip=cover_round_trip,
                    )
                )
    return tuple(rows)


@dataclass(frozen=True, slots=True)
class RootLoopRestrictionWitness:
    """Evidence that exact transverse zero removes to the unchanged v0.7 map."""

    event_id: str
    convention: TransverseCoordinateConvention
    native_strip: FramedMobiusStripState
    cover_strip: TransverseCoverChartState
    expected_native_root: NativeMobiusState
    expected_cover_root: RootLoopCoverChartState

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        if self.native_strip.local_transverse != 0:
            raise TransverseStripError("root restriction requires transverse zero")
        if self.native_strip.root_state != self.expected_native_root:
            raise TransverseStripError("native zero fiber changed the v0.7 root")
        if self.cover_strip.root_chart != self.expected_cover_root:
            raise TransverseStripError("cover zero fiber changed the v0.7 chart")
        if self.cover_strip.local_transverse != 0:
            raise TransverseStripError("cover zero fiber must remain exact zero")


def build_root_loop_restrictions(
    packet: NativeMobiusInitiationPacket,
) -> tuple[RootLoopRestrictionWitness, ...]:
    """Build exact zero-fiber restrictions for every initiation and convention."""

    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    witnesses: list[RootLoopRestrictionWitness] = []
    for event in packet.initiations:
        native_strip = FramedMobiusStripState(event.post_state, Fraction(0))
        expected_cover_root = mobius_to_root_loop_cover(event.post_state)
        for convention in TransverseCoordinateConvention:
            witnesses.append(
                RootLoopRestrictionWitness(
                    event_id=event.event_id,
                    convention=convention,
                    native_strip=native_strip,
                    cover_strip=mobius_to_transverse_cover(
                        native_strip,
                        convention,
                    ),
                    expected_native_root=event.post_state,
                    expected_cover_root=expected_cover_root,
                )
            )
    return tuple(witnesses)


@dataclass(frozen=True, slots=True)
class TransverseMotionWitness:
    """Exact commutation evidence for one map row and one transition."""

    event_id: str
    label: str
    convention: TransverseCoordinateConvention
    local_transverse: Fraction
    turns: Fraction
    start_native: FramedMobiusStripState
    expected: TransverseCoverChartState
    observed: TransverseCoverChartState

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        if self.label not in TRANSVERSE_TRANSITION_LABELS:
            raise TransverseStripError("unknown transverse transition label")
        _validate_transverse(self.local_transverse)
        if not isinstance(self.turns, Fraction):
            raise TransverseStripError("transition turns must be an exact Fraction")
        if self.start_native.local_transverse != self.local_transverse:
            raise TransverseStripError("motion witness changed the native fiber")
        if self.expected != self.observed:
            raise TransverseStripError("transverse chart does not commute exactly")


def _motion_witness(
    *,
    event_id: str,
    label: str,
    convention: TransverseCoordinateConvention,
    initial: FramedMobiusStripState,
) -> TransverseMotionWitness:
    if label == "initiation":
        start_native = initial
        turns = Fraction(0)
    elif label == "advance-360":
        start_native = initial
        turns = Fraction(1)
    elif label == "advance-720":
        start_native = initial
        turns = Fraction(2)
    elif label == "inverse":
        start_native = initial.advance(1)
        turns = Fraction(-1)
    else:
        raise TransverseStripError("unknown transverse transition label")
    expected = mobius_to_transverse_cover(
        start_native.advance(turns),
        convention,
    )
    observed = mobius_to_transverse_cover(
        start_native,
        convention,
    ).advance(turns)
    return TransverseMotionWitness(
        event_id=event_id,
        label=label,
        convention=convention,
        local_transverse=initial.local_transverse,
        turns=turns,
        start_native=start_native,
        expected=expected,
        observed=observed,
    )


def build_transverse_motion_witnesses(
    packet: NativeMobiusInitiationPacket,
) -> tuple[TransverseMotionWitness, ...]:
    """Commute all four transitions over all eighty-four map rows."""

    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    witnesses: list[TransverseMotionWitness] = []
    for event in packet.initiations:
        for local_transverse in TRANSVERSE_WITNESS_VALUES:
            initial = FramedMobiusStripState(
                event.post_state,
                local_transverse,
            )
            for convention in TransverseCoordinateConvention:
                for label in TRANSVERSE_TRANSITION_LABELS:
                    witnesses.append(
                        _motion_witness(
                            event_id=event.event_id,
                            label=label,
                            convention=convention,
                            initial=initial,
                        )
                    )
    return tuple(witnesses)


@dataclass(frozen=True, slots=True)
class ConventionRoundTripWitness:
    """Exact two-way change of coordinates for one represented strip state."""

    event_id: str
    native_state: FramedMobiusStripState
    local_state: TransverseCoverChartState
    global_state: TransverseCoverChartState
    local_round_trip: TransverseCoverChartState
    global_round_trip: TransverseCoverChartState

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        if (
            self.local_state.convention
            is not TransverseCoordinateConvention.LOCAL_FRAME
        ):
            raise TransverseStripError("local convention witness is mislabeled")
        if (
            self.global_state.convention
            is not TransverseCoordinateConvention.GLOBAL_SIDE
        ):
            raise TransverseStripError("global convention witness is mislabeled")
        if self.local_round_trip != self.local_state:
            raise TransverseStripError("local convention round trip failed")
        if self.global_round_trip != self.global_state:
            raise TransverseStripError("global convention round trip failed")
        if self.local_state.local_transverse != self.global_state.local_transverse:
            raise TransverseStripError("coordinate change altered represented state")


def build_convention_round_trips(
    packet: NativeMobiusInitiationPacket,
) -> tuple[ConventionRoundTripWitness, ...]:
    """Change conventions in both directions for all forty-two native states."""

    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    witnesses: list[ConventionRoundTripWitness] = []
    for event in packet.initiations:
        for local_transverse in TRANSVERSE_WITNESS_VALUES:
            native_state = FramedMobiusStripState(
                event.post_state,
                local_transverse,
            )
            local_state = mobius_to_transverse_cover(
                native_state,
                TransverseCoordinateConvention.LOCAL_FRAME,
            )
            global_state = mobius_to_transverse_cover(
                native_state,
                TransverseCoordinateConvention.GLOBAL_SIDE,
            )
            witnesses.append(
                ConventionRoundTripWitness(
                    event_id=event.event_id,
                    native_state=native_state,
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
                )
            )
    return tuple(witnesses)


@dataclass(frozen=True, slots=True)
class ConventionMotionWitness:
    """Evidence that coordinate change and bounded motion commute exactly."""

    event_id: str
    label: str
    local_transverse: Fraction
    turns: Fraction
    expected_global: TransverseCoverChartState
    observed_global: TransverseCoverChartState

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        if self.label not in TRANSVERSE_TRANSITION_LABELS:
            raise TransverseStripError("unknown convention transition label")
        _validate_transverse(self.local_transverse)
        if not isinstance(self.turns, Fraction):
            raise TransverseStripError("transition turns must be an exact Fraction")
        if self.expected_global != self.observed_global:
            raise TransverseStripError(
                "coordinate change does not commute with bounded motion"
            )


def build_convention_motion_witnesses(
    packet: NativeMobiusInitiationPacket,
) -> tuple[ConventionMotionWitness, ...]:
    """Commute local-to-global conversion with all declared transitions."""

    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    witnesses: list[ConventionMotionWitness] = []
    for event in packet.initiations:
        for local_transverse in TRANSVERSE_WITNESS_VALUES:
            initial = FramedMobiusStripState(
                event.post_state,
                local_transverse,
            )
            for label in TRANSVERSE_TRANSITION_LABELS:
                if label == "initiation":
                    start_native = initial
                    turns = Fraction(0)
                elif label == "advance-360":
                    start_native = initial
                    turns = Fraction(1)
                elif label == "advance-720":
                    start_native = initial
                    turns = Fraction(2)
                else:
                    start_native = initial.advance(1)
                    turns = Fraction(-1)
                local_start = mobius_to_transverse_cover(
                    start_native,
                    TransverseCoordinateConvention.LOCAL_FRAME,
                )
                expected_global = convert_transverse_convention(
                    local_start.advance(turns),
                    TransverseCoordinateConvention.GLOBAL_SIDE,
                )
                observed_global = convert_transverse_convention(
                    local_start,
                    TransverseCoordinateConvention.GLOBAL_SIDE,
                ).advance(turns)
                witnesses.append(
                    ConventionMotionWitness(
                        event_id=event.event_id,
                        label=label,
                        local_transverse=local_transverse,
                        turns=turns,
                        expected_global=expected_global,
                        observed_global=observed_global,
                    )
                )
    return tuple(witnesses)


def _extend_transverse_matrix(
    root_report: RootLoopChartReport,
    *,
    round_trip_count: int,
    root_restriction_count: int,
    motion_count: int,
    convention_round_trip_count: int,
    convention_motion_count: int,
) -> CarrierExperimentReport:
    """Extend only the bounded F12/F13 evidence; retain all other v0.7 cells."""

    experiment = root_report.experiment
    f12 = experiment.result(CarrierRelationship.COVER_CHART, "F12")
    f13 = experiment.result(CarrierRelationship.INCOMPATIBLE, "F13")
    transverse_evidence = (
        "transverse-witness-values:-1/1,0/1,1/1",
        "transverse-conventions:local-frame-displacement,global-side-displacement",
        f"transverse-round-trips:{round_trip_count}",
        f"root-loop-restrictions:{root_restriction_count}",
        f"transverse-motion-commutations:{motion_count}",
        f"coordinate-change-round-trips:{convention_round_trip_count}",
        f"coordinate-change-commutations:{convention_motion_count}",
    )
    replacements = {
        (CarrierRelationship.COVER_CHART, "F12"): replace(
            f12,
            evidence=(*f12.evidence, *transverse_evidence),
        ),
        (CarrierRelationship.INCOMPATIBLE, "F13"): replace(
            f13,
            evidence=(*f13.evidence, *transverse_evidence),
        ),
    }
    return replace(
        experiment,
        results=tuple(
            replacements.get((item.relationship, item.falsifier_id), item)
            for item in experiment.results
        ),
        hmmm=(
            "F12 support and F13 falsification extend only to the exact minimum packet crossed with transverse witnesses -1, 0, and +1",
            "the local-frame and global-side coordinates are reversible chart conventions on this domain; neither is selected as canonical",
            "the finite witness packet does not establish continuous-strip generality",
            "transverse displacement is not canonical B, carrier radius, or arbitrary-element assignment",
            "radial assignment, higher-gonol composition, and circle-epicycle-disk-sphere transitions remain unresolved",
            "720-degree state return is not promoted to scoped completion",
        ),
    )


@dataclass(frozen=True, slots=True)
class TransverseStripReport:
    """Complete v0.8 bounded transverse evidence with no option selection."""

    report_id: str
    root_report: RootLoopChartReport
    round_trips: tuple[TransverseStripRoundTrip, ...]
    root_restrictions: tuple[RootLoopRestrictionWitness, ...]
    motion_witnesses: tuple[TransverseMotionWitness, ...]
    convention_round_trips: tuple[ConventionRoundTripWitness, ...]
    convention_motion_witnesses: tuple[ConventionMotionWitness, ...]
    experiment: CarrierExperimentReport
    hmmm: tuple[str, ...]
    schema_id: str = V08_TRANSVERSE_STRIP_SCHEMA_ID
    schema_version: str = V08_TRANSVERSE_STRIP_SCHEMA_VERSION
    selection_effect: str = V08_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.report_id, "report_id")
        if self.schema_id != V08_TRANSVERSE_STRIP_SCHEMA_ID:
            raise TransverseStripError("v0.8 report schema identity mismatch")
        if self.schema_version != V08_TRANSVERSE_STRIP_SCHEMA_VERSION:
            raise TransverseStripError("v0.8 report schema version mismatch")
        if self.selection_effect != V08_SELECTION_EFFECT:
            raise TransverseStripError("v0.8 cannot select a carrier or convention")
        if self.experiment.selection_effect != V08_SELECTION_EFFECT:
            raise TransverseStripError("embedded experiment cannot select a carrier")

        initiation_count = len(self.root_report.direct_report.packet.initiations)
        convention_count = len(TransverseCoordinateConvention)
        fiber_count = len(TRANSVERSE_WITNESS_VALUES)
        expected_round_trips = initiation_count * fiber_count * convention_count
        if len(self.round_trips) != expected_round_trips:
            raise TransverseStripError("v0.8 must retain every transverse map row")
        if len(self.root_restrictions) != initiation_count * convention_count:
            raise TransverseStripError("v0.8 must restrict every zero-fiber row")
        if (
            len(self.motion_witnesses)
            != expected_round_trips * len(TRANSVERSE_TRANSITION_LABELS)
        ):
            raise TransverseStripError("v0.8 must commute every map transition")
        if len(self.convention_round_trips) != initiation_count * fiber_count:
            raise TransverseStripError(
                "v0.8 must change coordinates for every native strip state"
            )
        if (
            len(self.convention_motion_witnesses)
            != initiation_count
            * fiber_count
            * len(TRANSVERSE_TRANSITION_LABELS)
        ):
            raise TransverseStripError(
                "v0.8 must commute coordinate change with every transition"
            )
        if (
            self.experiment.result(
                CarrierRelationship.COVER_CHART,
                "F12",
            ).verdict
            is not FalsifierVerdict.SUPPORTED
        ):
            raise TransverseStripError("bounded v0.8 evidence must support F12")
        if (
            self.experiment.result(
                CarrierRelationship.INCOMPATIBLE,
                "F13",
            ).verdict
            is not FalsifierVerdict.FALSIFIED
        ):
            raise TransverseStripError(
                "a reversible bounded strip map must falsify F13 on that domain"
            )
        _require_text_items(self.hmmm, "hmmm")


def run_v08_transverse_strip_experiment(
    *,
    report_id: str = "ucns-edcm-v0.8:bounded-transverse-strip-chart",
) -> TransverseStripReport:
    """Run the finite exact transverse witness experiment without selection."""

    root_report = run_v07_root_loop_chart_experiment(
        report_id=f"{report_id}:root-loop"
    )
    packet = root_report.direct_report.packet
    round_trips = build_transverse_round_trips(packet)
    root_restrictions = build_root_loop_restrictions(packet)
    motion_witnesses = build_transverse_motion_witnesses(packet)
    convention_round_trips = build_convention_round_trips(packet)
    convention_motion_witnesses = build_convention_motion_witnesses(packet)
    experiment = _extend_transverse_matrix(
        root_report,
        round_trip_count=len(round_trips),
        root_restriction_count=len(root_restrictions),
        motion_count=len(motion_witnesses),
        convention_round_trip_count=len(convention_round_trips),
        convention_motion_count=len(convention_motion_witnesses),
    )
    return TransverseStripReport(
        report_id=report_id,
        root_report=root_report,
        round_trips=round_trips,
        root_restrictions=root_restrictions,
        motion_witnesses=motion_witnesses,
        convention_round_trips=convention_round_trips,
        convention_motion_witnesses=convention_motion_witnesses,
        experiment=experiment,
        hmmm=experiment.hmmm,
    )


__all__ = [
    "TRANSVERSE_BOUND",
    "TRANSVERSE_STRIP_MAP_ID",
    "TRANSVERSE_STRIP_MAP_VERSION",
    "TRANSVERSE_STRIP_SCOPE",
    "TRANSVERSE_TRANSITION_LABELS",
    "TRANSVERSE_WITNESS_VALUES",
    "V08_SELECTION_EFFECT",
    "V08_TRANSVERSE_STRIP_SCHEMA_ID",
    "V08_TRANSVERSE_STRIP_SCHEMA_VERSION",
    "ConventionMotionWitness",
    "ConventionRoundTripWitness",
    "FramedMobiusStripState",
    "RootLoopRestrictionWitness",
    "TransverseCoordinateConvention",
    "TransverseCoverChartState",
    "TransverseMotionWitness",
    "TransverseStripError",
    "TransverseStripReport",
    "TransverseStripRoundTrip",
    "build_convention_motion_witnesses",
    "build_convention_round_trips",
    "build_root_loop_restrictions",
    "build_transverse_motion_witnesses",
    "build_transverse_round_trips",
    "convert_transverse_convention",
    "mobius_to_transverse_cover",
    "run_v08_transverse_strip_experiment",
    "transverse_cover_to_mobius",
]
