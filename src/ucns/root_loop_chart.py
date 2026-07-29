# === MODULE_BUILD ===
# id: edcm_root_loop_cover_chart_candidate
#   module_name: root_loop_chart
#   module_kind: experiment
#   summary: tests an exact reversible chart between the native framed Mobius root loop and the directed twofold cover over the bounded v0.7 witness domain
#   owner: Erin Spencer
#   public_surface: RootLoopCoverChartState, RootLoopChartRoundTrip, RootLoopChartReport, mobius_to_root_loop_cover, root_loop_cover_to_mobius, build_root_loop_chart_round_trips, build_root_loop_chart_evidence, run_v07_root_loop_chart_experiment
#   internal_surface: exact-turn normalization and report-matrix adapters
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and completion scope remain linked through both maps
#   admin_only: false
#   tests: tests/test_root_loop_chart.py
#   rollout: explicit UCNS-only v0.7 bounded chart experiment; no global carrier equivalence, carrier selection, completion, EDCM activation, or METAPAT activation
#   rollback: remove this module, its exports, tests, and v0.7 candidate document while retaining the v0.5 and v0.6 experiments
#   requires: directed_carrier_floor, edcm_mobius_carrier_experiment, edcm_native_direct_mobius_candidate
#   since: 2026-07-29
#   unresolved: extension beyond the framed root loop, transverse and radial assignment, arbitrary element assignment, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: root_loop_chart_maps_are_exact_two_way_inverses
#   given: any exact rational state in the bounded framed Mobius root-loop domain or its exact directed-cover chart image
#   then: both Mobius-to-cover-to-Mobius and cover-to-Mobius-to-cover round trips restore every retained state distinction
#   class: correctness
#   since: 2026-07-29
#
# id: root_loop_chart_preserves_every_source_linked_initiation
#   given: the complete v0.6 minimum witness packet enters the v0.7 chart adapter
#   then: all fourteen word initiations retain exact source, Structural Null cause, initiation identity, order, multiplicity, sidedness, parentage, and completion scope
#   class: evidence
#   since: 2026-07-29
#
# id: root_loop_chart_commutes_with_bounded_motion
#   given: initiation, positive 360-degree motion, positive 720-degree motion, and inverse 360-degree motion are evaluated
#   then: mapping after native motion exactly equals chart motion after mapping for every declared transition
#   class: correctness
#   since: 2026-07-29
#
# id: root_loop_chart_uses_cover_sheet_as_hypothesis_not_native_orientation
#   given: a native frame is mapped to a directed-cover representative
#   then: first-versus-second lifted representative carries the candidate chart correspondence while the directed carrier API remains unchanged and no topology-owned orientation field is invented
#   class: safety
#   since: 2026-07-29
#
# id: root_loop_chart_support_is_bounded_and_nonselecting
#   given: the complete v0.7 report is produced
#   then: F12 is supported and F13 falsified only for the declared root-loop witness domain while selection remains none and global equivalence, completion, higher geometry, EDCM, and METAPAT remain unresolved
#   class: doctrine
#   since: 2026-07-29
# === END CONTRACTS ===

"""Bounded C1↔C2 root-loop chart experiment for UCNS–EDCM v0.7.

The native v0.6 Möbius state is ``(p, frame)`` with exact rational phase
``0 <= p < 1``.  The v0.7 chart hypothesis maps that state to an exact rational
lifted turn in the directed twofold cover:

* positive local frame -> ``alpha = p``;
* reversed local frame -> ``alpha = p + 1``.

The inverse uses the first or second lifted representative to recover the local
frame.  This correspondence is tested as an explicit chart hypothesis.  It does
not change the directed carrier floor or claim that topology intrinsically owns
a frame inversion.

The exact rational chart state is authoritative experiment evidence.  Its
``LiftedCarrierPoint`` materialization is a nonauthoritative geometric display
at fixed breadth one.  That fixed breadth is not canonical faithful breadth and
does not assign arbitrary elements to transverse or radial coordinates.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction

from .carrier import LiftedCarrierPoint, VISIBLE_PERIOD
from .comparison import exact_comparison_policy
from .direct_mobius import (
    NATIVE_MOBIUS_SCOPE,
    DirectMobiusCandidateReport,
    MobiusInitiationEvent,
    NativeMobiusFrame,
    NativeMobiusInitiationPacket,
    NativeMobiusState,
    run_v06_direct_mobius_experiment,
)
from .mobius_experiment import (
    REQUIRED_COMMUTATION_LABELS,
    REQUIRED_MAP_DISTINCTIONS,
    CarrierExperimentReport,
    CarrierExperimentState,
    CarrierMapEvidence,
    CarrierRelationship,
    FalsifierVerdict,
    MapCommutationWitness,
    run_v05_carrier_experiment,
)


V07_ROOT_LOOP_CHART_SCHEMA_ID = "ucns.edcm.root-loop-cover-chart"
V07_ROOT_LOOP_CHART_SCHEMA_VERSION = "0.7.0"
V07_SELECTION_EFFECT = "none"
ROOT_LOOP_CHART_MAP_ID = "ucns.edcm.mobius-directed-cover-root-loop-chart"
ROOT_LOOP_CHART_MAP_VERSION = "0.7.0"
ROOT_LOOP_CHART_SCOPE = "bounded-framed-root-loop-witness-domain-only"
ROOT_LOOP_CHART_BREADTH = Fraction(1)


class RootLoopChartError(ValueError):
    """Raised when evidence exceeds or violates the bounded chart contract."""


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise RootLoopChartError(f"{field} must be nonempty text")


def _require_text_items(
    values: tuple[str, ...],
    field: str,
    *,
    allow_empty: bool = False,
) -> None:
    if not values and not allow_empty:
        raise RootLoopChartError(f"{field} must retain at least one item")
    for value in values:
        _require_text(value, field)


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _exact_turns(value: Fraction | int) -> Fraction:
    if isinstance(value, bool):
        raise RootLoopChartError("chart motion cannot be boolean")
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, Fraction):
        raise RootLoopChartError("chart motion must be int or exact Fraction")
    return value


def _normalize_lifted_turns(value: Fraction) -> Fraction:
    """Return the exact representative in the directed cover interval [0, 2)."""

    whole_periods = value // 2
    return value - 2 * whole_periods


@dataclass(frozen=True, slots=True)
class RootLoopCoverChartState:
    """Exact source-linked chart state on the bounded directed root loop."""

    lifted_turns: Fraction
    source_links: tuple[str, ...]
    parent_observation_ids: tuple[str, ...]
    initiation_event_id: str
    completion_scope: str = NATIVE_MOBIUS_SCOPE
    breadth: Fraction = ROOT_LOOP_CHART_BREADTH
    map_id: str = ROOT_LOOP_CHART_MAP_ID
    map_version: str = ROOT_LOOP_CHART_MAP_VERSION
    chart_scope: str = ROOT_LOOP_CHART_SCOPE

    def __post_init__(self) -> None:
        if not isinstance(self.lifted_turns, Fraction):
            raise RootLoopChartError("lifted_turns must be an exact Fraction")
        if not Fraction(0) <= self.lifted_turns < Fraction(2):
            raise RootLoopChartError("lifted_turns must be canonical in [0, 2)")
        if self.breadth != ROOT_LOOP_CHART_BREADTH:
            raise RootLoopChartError(
                "bounded root-loop chart breadth is the fixed display coordinate one"
            )
        _require_text_items(self.source_links, "source_links")
        _require_text_items(
            self.parent_observation_ids,
            "parent_observation_ids",
            allow_empty=True,
        )
        _require_text(self.initiation_event_id, "initiation_event_id")
        if self.completion_scope != NATIVE_MOBIUS_SCOPE:
            raise RootLoopChartError("completion scope must remain the native root loop")
        if self.map_id != ROOT_LOOP_CHART_MAP_ID:
            raise RootLoopChartError("root-loop chart map identity is fixed")
        if self.map_version != ROOT_LOOP_CHART_MAP_VERSION:
            raise RootLoopChartError("root-loop chart map version is fixed")
        if self.chart_scope != ROOT_LOOP_CHART_SCOPE:
            raise RootLoopChartError("root-loop chart scope is fixed")

    @property
    def visible_phase_turns(self) -> Fraction:
        if self.lifted_turns < 1:
            return self.lifted_turns
        return self.lifted_turns - 1

    @property
    def sheet(self) -> str:
        if self.lifted_turns < 1:
            return "first-lifted-representative"
        return "second-lifted-representative"

    @property
    def mapped_frame(self) -> NativeMobiusFrame:
        if self.lifted_turns < 1:
            return NativeMobiusFrame.POSITIVE
        return NativeMobiusFrame.REVERSED

    @property
    def materialized_point(self) -> LiftedCarrierPoint:
        """Return a nonauthoritative float rendering on the existing cover."""

        return LiftedCarrierPoint(
            float(self.breadth),
            float(self.lifted_turns) * VISIBLE_PERIOD,
        )

    def advance(self, turns: Fraction | int) -> RootLoopCoverChartState:
        """Advance exact chart turns modulo the two-turn directed cover."""

        displacement = _exact_turns(turns)
        return replace(
            self,
            lifted_turns=_normalize_lifted_turns(
                self.lifted_turns + displacement
            ),
        )

    @property
    def complete_key(self) -> tuple[tuple[str, str], ...]:
        return (
            ("map", f"{self.map_id}@{self.map_version}"),
            ("lifted-turns", _fraction_key(self.lifted_turns)),
            ("declared-chart-breadth", _fraction_key(self.breadth)),
        )

    @property
    def visible_key(self) -> tuple[tuple[str, str], ...]:
        return (
            ("map", f"{self.map_id}@{self.map_version}"),
            ("visible-phase-turns", _fraction_key(self.visible_phase_turns)),
            ("declared-chart-breadth", _fraction_key(self.breadth)),
        )

    def as_experiment_state(self, state_id: str) -> CarrierExperimentState:
        """Adapt exact chart evidence without changing the carrier floor."""

        _require_text(state_id, "state_id")
        return CarrierExperimentState(
            candidate=CarrierRelationship.COVER_CHART,
            state_id=state_id,
            complete_key=self.complete_key,
            visible_key=self.visible_key,
            orientation=f"chart-mapped-{self.mapped_frame.value}",
            sidedness=f"chart-mapped-{self.mapped_frame.value}",
            sheet=self.sheet,
            source_links=self.source_links,
            parent_observation_ids=self.parent_observation_ids,
            completion_scope=self.completion_scope,
            initiation_event_id=self.initiation_event_id,
            completion_receipt=None,
        )


def mobius_to_root_loop_cover(
    state: NativeMobiusState,
) -> RootLoopCoverChartState:
    """Apply the exact v0.7 C1-to-C2 root-loop chart hypothesis."""

    if not isinstance(state, NativeMobiusState):
        raise TypeError("state must be NativeMobiusState")
    sheet_offset = (
        Fraction(0)
        if state.frame is NativeMobiusFrame.POSITIVE
        else Fraction(1)
    )
    return RootLoopCoverChartState(
        lifted_turns=state.phase_turns + sheet_offset,
        source_links=state.source_links,
        parent_observation_ids=state.parent_observation_ids,
        initiation_event_id=state.initiation_event_id,
        completion_scope=state.completion_scope,
    )


def root_loop_cover_to_mobius(
    state: RootLoopCoverChartState,
) -> NativeMobiusState:
    """Apply the exact inverse C2-to-C1 root-loop chart hypothesis."""

    if not isinstance(state, RootLoopCoverChartState):
        raise TypeError("state must be RootLoopCoverChartState")
    return NativeMobiusState(
        phase_turns=state.visible_phase_turns,
        frame=state.mapped_frame,
        source_links=state.source_links,
        parent_observation_ids=state.parent_observation_ids,
        initiation_event_id=state.initiation_event_id,
        completion_scope=state.completion_scope,
    )


@dataclass(frozen=True, slots=True)
class RootLoopChartRoundTrip:
    """Two-way map evidence for one exact causal word initiation."""

    event: MobiusInitiationEvent
    mobius_original: NativeMobiusState
    cover_image: RootLoopCoverChartState
    mobius_round_trip: NativeMobiusState
    cover_round_trip: RootLoopCoverChartState

    def __post_init__(self) -> None:
        if self.mobius_original != self.event.post_state:
            raise RootLoopChartError(
                "round trip must begin at the event's exact native post-state"
            )
        if self.mobius_round_trip != self.mobius_original:
            raise RootLoopChartError("Mobius round trip lost a retained distinction")
        if self.cover_round_trip != self.cover_image:
            raise RootLoopChartError("cover round trip lost a retained distinction")
        if self.cover_image.initiation_event_id != self.event.event_id:
            raise RootLoopChartError("chart image lost initiation identity")
        required_boundary_link = f"boundary:{self.event.boundary.manifestation_id}"
        if required_boundary_link not in self.cover_image.source_links:
            raise RootLoopChartError("chart image lost the Structural Null cause")


def build_root_loop_chart_round_trips(
    packet: NativeMobiusInitiationPacket,
) -> tuple[RootLoopChartRoundTrip, ...]:
    """Map and invert every source-linked v0.6 initiation in packet order."""

    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    round_trips: list[RootLoopChartRoundTrip] = []
    for event in packet.initiations:
        mobius_original = event.post_state
        cover_image = mobius_to_root_loop_cover(mobius_original)
        mobius_round_trip = root_loop_cover_to_mobius(cover_image)
        cover_round_trip = mobius_to_root_loop_cover(mobius_round_trip)
        round_trips.append(
            RootLoopChartRoundTrip(
                event=event,
                mobius_original=mobius_original,
                cover_image=cover_image,
                mobius_round_trip=mobius_round_trip,
                cover_round_trip=cover_round_trip,
            )
        )
    return tuple(round_trips)


def _commutation_witness(
    label: str,
    initial: NativeMobiusState,
    turns: Fraction | int,
) -> MapCommutationWitness:
    expected = mobius_to_root_loop_cover(initial.advance(turns))
    observed = mobius_to_root_loop_cover(initial).advance(turns)
    return MapCommutationWitness(
        label=label,
        expected=expected.as_experiment_state(f"chart:{label}:map-after-motion"),
        observed=observed.as_experiment_state(f"chart:{label}:motion-after-map"),
    )


def build_root_loop_chart_evidence(
    packet: NativeMobiusInitiationPacket,
) -> CarrierMapEvidence:
    """Build exhaustive-domain round-trip and transition evidence for F12."""

    if not isinstance(packet, NativeMobiusInitiationPacket):
        raise TypeError("packet must be NativeMobiusInitiationPacket")
    round_trips = build_root_loop_chart_round_trips(packet)
    if len(round_trips) != len(packet.initiations):
        raise RootLoopChartError(
            "chart evidence must round-trip every source-linked initiation"
        )
    first_events = packet.witness_initiations("W-first")
    if len(first_events) != 1:
        raise RootLoopChartError("W-first must supply exactly one initiation")
    mobius_original = first_events[0].post_state
    cover_original = mobius_to_root_loop_cover(mobius_original)
    mobius_round_trip = root_loop_cover_to_mobius(cover_original)
    cover_round_trip = mobius_to_root_loop_cover(mobius_round_trip)

    initiation_expected = mobius_to_root_loop_cover(first_events[0].post_state)
    initiation_observed = cover_original
    commutation_witnesses = (
        MapCommutationWitness(
            label="initiation",
            expected=initiation_expected.as_experiment_state(
                "chart:initiation:map-native-post-state"
            ),
            observed=initiation_observed.as_experiment_state(
                "chart:initiation:source-linked-cover-post-state"
            ),
        ),
        _commutation_witness("advance-360", mobius_original, 1),
        _commutation_witness("advance-720", mobius_original, 2),
        _commutation_witness("inverse", mobius_original.advance(1), -1),
    )
    return CarrierMapEvidence(
        map_id=ROOT_LOOP_CHART_MAP_ID,
        version=ROOT_LOOP_CHART_MAP_VERSION,
        code_reference=(
            "ucns.root_loop_chart:build_root_loop_chart_evidence"
        ),
        comparison_policy=exact_comparison_policy(
            name="root-loop-cover-chart-exact",
            version=ROOT_LOOP_CHART_MAP_VERSION,
        ),
        cover_original=cover_original.as_experiment_state(
            "chart:cover-original"
        ),
        cover_round_trip=cover_round_trip.as_experiment_state(
            "chart:cover-round-trip"
        ),
        mobius_original=mobius_original.as_experiment_state(
            "chart:mobius-original"
        ),
        mobius_round_trip=mobius_round_trip.as_experiment_state(
            "chart:mobius-round-trip"
        ),
        commutation_witnesses=commutation_witnesses,
        preserved_distinctions=REQUIRED_MAP_DISTINCTIONS,
        information_loss=(),
        witness_domain=tuple(item.witness_id for item in packet.witnesses),
    )


def _merge_chart_matrix(
    direct_report: DirectMobiusCandidateReport,
    chart_report: CarrierExperimentReport,
) -> CarrierExperimentReport:
    """Retain v0.6 C1 evidence while replacing only F12 and bounded F13."""

    replacements = {
        (
            CarrierRelationship.COVER_CHART,
            "F12",
        ): replace(
            chart_report.result(CarrierRelationship.COVER_CHART, "F12"),
            witness_ids=tuple(
                item.witness_id for item in direct_report.packet.witnesses
            ),
            evidence=(
                *chart_report.result(
                    CarrierRelationship.COVER_CHART,
                    "F12",
                ).evidence,
                f"initiation-round-trips:{len(direct_report.packet.initiations)}",
                f"commutation-witnesses:{len(REQUIRED_COMMUTATION_LABELS)}",
            ),
        ),
        (
            CarrierRelationship.INCOMPATIBLE,
            "F13",
        ): chart_report.result(CarrierRelationship.INCOMPATIBLE, "F13"),
    }
    results = tuple(
        replacements.get((item.relationship, item.falsifier_id), item)
        for item in direct_report.experiment.results
    )
    return replace(
        direct_report.experiment,
        results=results,
        hmmm=(
            "F12 support and F13 falsification apply only to the exact framed root-loop witness domain",
            "fixed chart breadth one is not canonical B, radial assignment, or transverse geometry",
            "arbitrary element assignment and extension beyond the root loop remain unresolved",
            "higher-gonol composition and circle-epicycle-disk-sphere transitions remain unresolved",
            "720-degree root-state return is not promoted to scoped completion",
        ),
    )


@dataclass(frozen=True, slots=True)
class RootLoopChartReport:
    """Complete v0.7 bounded chart evidence with option-preserving verdicts."""

    report_id: str
    direct_report: DirectMobiusCandidateReport
    round_trips: tuple[RootLoopChartRoundTrip, ...]
    chart_evidence: CarrierMapEvidence
    experiment: CarrierExperimentReport
    hmmm: tuple[str, ...]
    schema_id: str = V07_ROOT_LOOP_CHART_SCHEMA_ID
    schema_version: str = V07_ROOT_LOOP_CHART_SCHEMA_VERSION
    selection_effect: str = V07_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.report_id, "report_id")
        if self.schema_id != V07_ROOT_LOOP_CHART_SCHEMA_ID:
            raise RootLoopChartError("v0.7 report schema identity mismatch")
        if self.schema_version != V07_ROOT_LOOP_CHART_SCHEMA_VERSION:
            raise RootLoopChartError("v0.7 report schema version mismatch")
        if self.selection_effect != V07_SELECTION_EFFECT:
            raise RootLoopChartError("v0.7 chart cannot select a carrier")
        if self.experiment.selection_effect != V07_SELECTION_EFFECT:
            raise RootLoopChartError("embedded experiment cannot select a carrier")

        event_ids = tuple(
            item.event.event_id for item in self.round_trips
        )
        expected_event_ids = tuple(
            item.event_id for item in self.direct_report.packet.initiations
        )
        if event_ids != expected_event_ids:
            raise RootLoopChartError(
                "round trips must cover every initiation exactly once in order"
            )
        if self.chart_evidence.witness_domain != tuple(
            item.witness_id for item in self.direct_report.packet.witnesses
        ):
            raise RootLoopChartError("chart evidence must name the complete witness domain")
        if (
            tuple(item.label for item in self.chart_evidence.commutation_witnesses)
            != REQUIRED_COMMUTATION_LABELS
        ):
            raise RootLoopChartError(
                "chart evidence must retain every required transition in order"
            )
        if self.chart_evidence.preserved_distinctions != REQUIRED_MAP_DISTINCTIONS:
            raise RootLoopChartError(
                "chart evidence must preserve every required distinction"
            )
        if self.chart_evidence.information_loss:
            raise RootLoopChartError(
                "exact bounded chart state cannot declare a lost distinction"
            )
        if (
            self.experiment.result(
                CarrierRelationship.COVER_CHART,
                "F12",
            ).verdict
            is not FalsifierVerdict.SUPPORTED
        ):
            raise RootLoopChartError("bounded v0.7 evidence must support F12")
        if (
            self.experiment.result(
                CarrierRelationship.INCOMPATIBLE,
                "F13",
            ).verdict
            is not FalsifierVerdict.FALSIFIED
        ):
            raise RootLoopChartError(
                "a reversible bounded chart must falsify F13 for the same domain"
            )
        _require_text_items(self.hmmm, "hmmm")


def run_v07_root_loop_chart_experiment(
    *,
    report_id: str = "ucns-edcm-v0.7:root-loop-cover-chart",
) -> RootLoopChartReport:
    """Run the exact bounded C1↔C2 chart experiment without selecting a carrier."""

    direct_report = run_v06_direct_mobius_experiment(
        report_id=f"{report_id}:direct-candidate"
    )
    round_trips = build_root_loop_chart_round_trips(direct_report.packet)
    chart_evidence = build_root_loop_chart_evidence(direct_report.packet)
    chart_matrix = run_v05_carrier_experiment(
        direct_trace=direct_report.trace,
        chart_map=chart_evidence,
        report_id=f"{report_id}:chart-matrix",
    )
    experiment = _merge_chart_matrix(direct_report, chart_matrix)
    return RootLoopChartReport(
        report_id=report_id,
        direct_report=direct_report,
        round_trips=round_trips,
        chart_evidence=chart_evidence,
        experiment=experiment,
        hmmm=experiment.hmmm,
    )


__all__ = [
    "ROOT_LOOP_CHART_BREADTH",
    "ROOT_LOOP_CHART_MAP_ID",
    "ROOT_LOOP_CHART_MAP_VERSION",
    "ROOT_LOOP_CHART_SCOPE",
    "V07_ROOT_LOOP_CHART_SCHEMA_ID",
    "V07_ROOT_LOOP_CHART_SCHEMA_VERSION",
    "V07_SELECTION_EFFECT",
    "RootLoopChartError",
    "RootLoopChartReport",
    "RootLoopChartRoundTrip",
    "RootLoopCoverChartState",
    "build_root_loop_chart_evidence",
    "build_root_loop_chart_round_trips",
    "mobius_to_root_loop_cover",
    "root_loop_cover_to_mobius",
    "run_v07_root_loop_chart_experiment",
]
