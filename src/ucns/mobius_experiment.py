# === MODULE_BUILD ===
# id: edcm_mobius_carrier_experiment
#   module_name: mobius_experiment
#   module_kind: experiment
#   summary: executes the v0.5 source, motion, mapping, and incompatibility falsifier matrix without selecting a carrier
#   owner: Erin Spencer
#   public_surface: CarrierRelationship, FalsifierVerdict, CarrierExperimentState, CandidateTrace, MapCommutationWitness, CarrierMapEvidence, SeparatingWitness, FalsifierResult, MetricDisplay, CarrierExperimentReport, build_v05_witness_packet, directed_cover_trace, evaluate_candidate_trace, evaluate_chart_map, evaluate_separating_witness, run_v05_carrier_experiment
#   internal_surface: validation helpers, report-matrix builders, state comparison helpers
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact source witnesses remain attached to observations and are never normalized
#   admin_only: false
#   tests: tests/test_mobius_experiment.py
#   rollout: explicit UCNS-only v0.5 experiment; no carrier, metric, completion, EDCM, or METAPAT selection
#   rollback: remove this module and its tests without changing the exact EDCM observation profile or directed carrier floor
#   requires: edcm_word_gonol_profile, edcm_completion_motion_evidence, directed_carrier_floor, explicit_comparison_policy_layer, first_competing_evaluator_candidate_families
#   since: 2026-07-29
#   unresolved: direct Mobius state law, element assignment, chart map or incompatibility proof, higher-gonol composition, circle-epicycle-disk-sphere transitions, scoped completion
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: mobius_experiment_preserves_minimum_source_witnesses
#   given: the v0.5 minimum witness packet is built
#   then: every exact source turn reconstructs without normalization and retains one unit of support
#   class: evidence
#   since: 2026-07-29
#
# id: directed_cover_experiment_reports_360_change_and_720_return
#   given: the implemented directed cover is evaluated as comparison candidate C2
#   then: 360 degrees preserves the visible key while changing the lifted representative, 720 degrees returns completely, and the inverse restores the prior state
#   class: evidence
#   since: 2026-07-29
#
# id: carrier_experiment_preserves_three_relationships_without_selection
#   given: a v0.5 carrier experiment report is produced
#   then: all three relationship claims and all sixteen falsifiers remain explicit with no selected candidate or canonization effect
#   class: doctrine
#   since: 2026-07-29
#
# id: chart_and_incompatibility_evidence_remain_separating
#   given: chart-map or incompatibility evidence is supplied
#   then: reversible preserved maps support C2 and falsify C3 for that domain, while a complete failed-map witness can support C3 without promoting it
#   class: correctness
#   since: 2026-07-29
#
# id: carrier_experiment_displays_all_metric_candidates_without_zero_fill
#   given: a report is produced before metric laws are selected
#   then: every one of the nine M-by-B combinations is displayed for every relationship with unresolved value rather than a hidden numeric default
#   class: safety
#   since: 2026-07-29
#
# id: carrier_experiment_retains_evaluation_errors
#   given: an explicit comparison policy raises while evaluating supplied candidate evidence
#   then: the affected falsifier is recorded as error and the remaining report is still returned
#   class: evidence
#   since: 2026-07-29
# === END CONTRACTS ===

"""Candidate-neutral UCNS–EDCM v0.5 carrier experiment.

This module makes the merged v0.5 specifications executable without inventing
the unresolved Möbius assignment or transition law.  It retains:

* the exact minimum source witness packet from ``SEPARATING_FALSIFIERS.md``;
* every relationship candidate and every F01–F16 verdict slot;
* explicit complete and visible state keys under a named comparison policy;
* optional direct-carrier, chart-map, and incompatibility evidence;
* all nine registered ``M × B`` candidate displays without numeric fill; and
* ``hmmm`` constraints and evaluation errors as positive evidence.

The built-in run evaluates only what the current repository can demonstrate:
the exact EDCM observation floor and the directed 4π comparison carrier.  It
does not select a carrier, define a direct Möbius state, treat lifted return as
completion, or change EDCM or METAPAT.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable

from .carrier import (
    LiftedCarrierPoint,
    VISIBLE_PERIOD,
    project,
)
from .comparison import ComparisonPolicy, exact_comparison_policy
from .edcm import EdcmTurnObservation, EdcmWordGonolProfile


V05_EXPERIMENT_SCHEMA_ID = "ucns.edcm.mobius-carrier-experiment"
V05_EXPERIMENT_SCHEMA_VERSION = "0.5.0"
V05_SELECTION_EFFECT = "none"

FALSIFIER_IDS = tuple(f"F{index:02d}" for index in range(1, 17))
PRODUCT_CANDIDATE_IDS = (
    "cell-support-geometric-mean",
    "cell-support-maximum",
    "cell-support-minimum",
)
BREADTH_CANDIDATE_IDS = (
    "cell-log-support",
    "cell-detail",
    "retained-presence",
)
REQUIRED_MAP_DISTINCTIONS = (
    "exact-source",
    "initiation",
    "order",
    "multiplicity",
    "sidedness",
    "parentage",
    "completion-scope",
)
REQUIRED_COMMUTATION_LABELS = (
    "initiation",
    "advance-360",
    "advance-720",
    "inverse",
)
MINIMUM_WITNESS_TEXTS = (
    ("W-empty", ""),
    ("W-first", "A"),
    ("W-space", "A B"),
    ("W-nbsp", "A\u00a0B"),
    ("W-repeat-space", "A  B"),
    ("W-repeat-word", "AB AB"),
    ("W-order-left", "A B"),
    ("W-order-right", "B A"),
    ("W-unassigned", "A🙂B"),
)


class CarrierExperimentError(ValueError):
    """Raised when experiment evidence violates the v0.5 report boundary."""


class CarrierRelationship(str, Enum):
    """The three relationship claims compared by v0.5."""

    DIRECT_MOBIUS = "C1-direct-mobius"
    COVER_CHART = "C2-cover-chart"
    INCOMPATIBLE = "C3-incompatible"


class FalsifierVerdict(str, Enum):
    """The complete v0.5 verdict vocabulary."""

    SUPPORTED = "supported"
    FALSIFIED = "falsified"
    INCONCLUSIVE = "inconclusive"
    UNRESOLVED = "unresolved"
    ERROR = "error"


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise CarrierExperimentError(f"{field} must be nonempty text")


def _require_text_items(values: tuple[str, ...], field: str) -> None:
    if not values:
        raise CarrierExperimentError(f"{field} must retain at least one item")
    for value in values:
        _require_text(value, field)


def _require_state_key(
    values: tuple[tuple[str, str], ...],
    field: str,
) -> None:
    if not values:
        raise CarrierExperimentError(f"{field} must retain at least one field")
    names: set[str] = set()
    for name, value in values:
        _require_text(name, f"{field} name")
        _require_text(value, f"{field} value")
        if name in names:
            raise CarrierExperimentError(f"{field} field names must be unique")
        names.add(name)


@dataclass(frozen=True, slots=True)
class SourceWitness:
    """One exact speaker-turn witness and its source identifier."""

    witness_id: str
    turn: EdcmTurnObservation

    def __post_init__(self) -> None:
        _require_text(self.witness_id, "witness_id")
        if self.turn.source_id != self.witness_id:
            raise CarrierExperimentError(
                "source witness id must equal the exact turn source_id"
            )
        if self.turn.unit_support != 1.0:
            raise CarrierExperimentError("every witness turn must retain unit support")
        reconstructed = "".join(segment.raw_text for segment in self.turn.segments)
        if reconstructed != self.turn.raw_text:
            raise CarrierExperimentError("source witness must reconstruct exactly")


@dataclass(frozen=True, slots=True)
class CarrierExperimentState:
    """Candidate-owned complete and visible state evidence.

    Keys are explicit immutable evidence supplied by the candidate.  The
    experiment never hashes arbitrary objects or infers equality from a Python
    object's identity.
    """

    candidate: CarrierRelationship
    state_id: str
    complete_key: tuple[tuple[str, str], ...]
    visible_key: tuple[tuple[str, str], ...]
    orientation: str
    sidedness: str
    sheet: str
    source_links: tuple[str, ...]
    parent_observation_ids: tuple[str, ...]
    completion_scope: str
    initiation_event_id: str | None = None
    completion_receipt: str | None = None

    def __post_init__(self) -> None:
        if self.candidate is CarrierRelationship.INCOMPATIBLE:
            raise CarrierExperimentError(
                "C3-incompatible is a relationship verdict, not a carrier state"
            )
        _require_text(self.state_id, "state_id")
        _require_state_key(self.complete_key, "complete_key")
        _require_state_key(self.visible_key, "visible_key")
        _require_text(self.orientation, "orientation")
        _require_text(self.sidedness, "sidedness")
        _require_text(self.sheet, "sheet")
        _require_text_items(self.source_links, "source_links")
        for parent_id in self.parent_observation_ids:
            _require_text(parent_id, "parent_observation_id")
        _require_text(self.completion_scope, "completion_scope")
        if self.initiation_event_id is not None:
            _require_text(self.initiation_event_id, "initiation_event_id")
        if self.completion_receipt is not None:
            _require_text(self.completion_receipt, "completion_receipt")

    @property
    def complete_identity(self) -> tuple[object, ...]:
        """Return every retained distinction used by complete-state comparison."""

        return (
            self.complete_key,
            self.orientation,
            self.sidedness,
            self.sheet,
            self.source_links,
            self.parent_observation_ids,
            self.completion_scope,
            self.initiation_event_id,
        )

    @property
    def visible_identity(self) -> tuple[tuple[str, str], ...]:
        """Return only the declared visible projection key."""

        return self.visible_key


@dataclass(frozen=True, slots=True)
class CandidateTrace:
    """Four-state evidence required by the 360°, 720°, and inverse falsifiers."""

    candidate: CarrierRelationship
    version: str
    code_reference: str
    comparison_policy: ComparisonPolicy
    initial: CarrierExperimentState
    after_360: CarrierExperimentState
    after_720: CarrierExperimentState
    inverse_after_360: CarrierExperimentState
    declared_dependencies: tuple[CarrierRelationship, ...] = ()
    native_independence_evidence: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.candidate is CarrierRelationship.INCOMPATIBLE:
            raise CarrierExperimentError(
                "C3-incompatible cannot be supplied as a candidate trace"
            )
        _require_text(self.version, "candidate version")
        _require_text(self.code_reference, "candidate code_reference")
        for state in (
            self.initial,
            self.after_360,
            self.after_720,
            self.inverse_after_360,
        ):
            if state.candidate is not self.candidate:
                raise CarrierExperimentError(
                    "every trace state must use the trace candidate"
                )
        for item in self.native_independence_evidence:
            _require_text(item, "native_independence_evidence")


@dataclass(frozen=True, slots=True)
class MapCommutationWitness:
    """Expected and observed states for one map/transition commutation square."""

    label: str
    expected: CarrierExperimentState
    observed: CarrierExperimentState

    def __post_init__(self) -> None:
        _require_text(self.label, "commutation label")
        if self.expected.candidate is not self.observed.candidate:
            raise CarrierExperimentError(
                "commutation witness states must belong to the same candidate"
            )


@dataclass(frozen=True, slots=True)
class CarrierMapEvidence:
    """Explicit two-way state-map evidence for the C2 chart claim."""

    map_id: str
    version: str
    code_reference: str
    comparison_policy: ComparisonPolicy
    cover_original: CarrierExperimentState
    cover_round_trip: CarrierExperimentState
    mobius_original: CarrierExperimentState
    mobius_round_trip: CarrierExperimentState
    commutation_witnesses: tuple[MapCommutationWitness, ...]
    preserved_distinctions: tuple[str, ...]
    information_loss: tuple[str, ...]
    witness_domain: tuple[str, ...]

    def __post_init__(self) -> None:
        _require_text(self.map_id, "map_id")
        _require_text(self.version, "map version")
        _require_text(self.code_reference, "map code_reference")
        if (
            self.cover_original.candidate is not CarrierRelationship.COVER_CHART
            or self.cover_round_trip.candidate
            is not CarrierRelationship.COVER_CHART
        ):
            raise CarrierExperimentError("cover round trip must use C2 states")
        if (
            self.mobius_original.candidate
            is not CarrierRelationship.DIRECT_MOBIUS
            or self.mobius_round_trip.candidate
            is not CarrierRelationship.DIRECT_MOBIUS
        ):
            raise CarrierExperimentError("Mobius round trip must use C1 states")
        labels = tuple(item.label for item in self.commutation_witnesses)
        if len(set(labels)) != len(labels):
            raise CarrierExperimentError("commutation labels must be unique")
        _require_text_items(self.preserved_distinctions, "preserved_distinctions")
        for item in self.information_loss:
            _require_text(item, "information_loss")
        _require_text_items(self.witness_domain, "witness_domain")


@dataclass(frozen=True, slots=True)
class SeparatingWitness:
    """Constructive evidence that every declared admissible map loses an invariant."""

    witness_id: str
    comparison_policy: ComparisonPolicy
    left_state: CarrierExperimentState
    right_state: CarrierExperimentState
    admissible_map_ids: tuple[str, ...]
    failed_map_ids: tuple[str, ...]
    violated_invariant: str
    maps_identify_states: bool
    detail: str
    rollback_behavior: str

    def __post_init__(self) -> None:
        _require_text(self.witness_id, "witness_id")
        _require_text_items(self.admissible_map_ids, "admissible_map_ids")
        _require_text_items(self.failed_map_ids, "failed_map_ids")
        _require_text(self.violated_invariant, "violated_invariant")
        _require_text(self.detail, "separating detail")
        _require_text(self.rollback_behavior, "rollback_behavior")
        if len(set(self.admissible_map_ids)) != len(self.admissible_map_ids):
            raise CarrierExperimentError("admissible map ids must be unique")
        if len(set(self.failed_map_ids)) != len(self.failed_map_ids):
            raise CarrierExperimentError("failed map ids must be unique")
        if not set(self.failed_map_ids).issubset(self.admissible_map_ids):
            raise CarrierExperimentError(
                "failed map ids must be drawn from the admissible map set"
            )


@dataclass(frozen=True, slots=True)
class FalsifierResult:
    """One relationship/falsifier verdict with retained evidence."""

    relationship: CarrierRelationship
    falsifier_id: str
    verdict: FalsifierVerdict
    detail: str
    witness_ids: tuple[str, ...]
    evidence: tuple[str, ...]
    information_loss: tuple[str, ...] = ()
    error: str | None = None

    def __post_init__(self) -> None:
        if self.falsifier_id not in FALSIFIER_IDS:
            raise CarrierExperimentError(
                f"unknown v0.5 falsifier: {self.falsifier_id}"
            )
        _require_text(self.detail, "falsifier detail")
        _require_text_items(self.witness_ids, "falsifier witness_ids")
        _require_text_items(self.evidence, "falsifier evidence")
        for item in self.information_loss:
            _require_text(item, "information_loss")
        if self.verdict is FalsifierVerdict.ERROR:
            if self.error is None:
                raise CarrierExperimentError("error verdict requires error evidence")
            _require_text(self.error, "error")
        elif self.error is not None:
            raise CarrierExperimentError(
                "only an error verdict may retain an error string"
            )


@dataclass(frozen=True, slots=True)
class MetricDisplay:
    """One explicit unresolved M-by-B display cell."""

    relationship: CarrierRelationship
    product_candidate_id: str
    breadth_candidate_id: str
    verdict: FalsifierVerdict
    value: float | None
    detail: str

    def __post_init__(self) -> None:
        if self.product_candidate_id not in PRODUCT_CANDIDATE_IDS:
            raise CarrierExperimentError("unknown product-character candidate")
        if self.breadth_candidate_id not in BREADTH_CANDIDATE_IDS:
            raise CarrierExperimentError("unknown breadth candidate")
        _require_text(self.detail, "metric display detail")
        if self.value is not None:
            raise CarrierExperimentError(
                "v0.5 carrier experiment cannot fill an unselected metric value"
            )
        if self.verdict is not FalsifierVerdict.UNRESOLVED:
            raise CarrierExperimentError(
                "uncomputed metric displays must remain unresolved"
            )


@dataclass(frozen=True, slots=True)
class CarrierExperimentReport:
    """Complete option-preserving report for one v0.5 experiment run."""

    report_id: str
    witnesses: tuple[SourceWitness, ...]
    relationships: tuple[CarrierRelationship, ...]
    results: tuple[FalsifierResult, ...]
    metric_displays: tuple[MetricDisplay, ...]
    hmmm: tuple[str, ...]
    schema_id: str = V05_EXPERIMENT_SCHEMA_ID
    schema_version: str = V05_EXPERIMENT_SCHEMA_VERSION
    selection_effect: str = V05_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.report_id, "report_id")
        if self.schema_id != V05_EXPERIMENT_SCHEMA_ID:
            raise CarrierExperimentError("experiment schema identity mismatch")
        if self.schema_version != V05_EXPERIMENT_SCHEMA_VERSION:
            raise CarrierExperimentError("experiment schema version mismatch")
        if self.selection_effect != "none":
            raise CarrierExperimentError("carrier experiment cannot select canon")
        if self.relationships != tuple(CarrierRelationship):
            raise CarrierExperimentError(
                "all three carrier relationships must remain present in order"
            )
        expected_witnesses = tuple(item[0] for item in MINIMUM_WITNESS_TEXTS)
        if tuple(item.witness_id for item in self.witnesses) != expected_witnesses:
            raise CarrierExperimentError(
                "report must retain the complete minimum witness packet in order"
            )

        result_keys = tuple(
            (item.relationship, item.falsifier_id) for item in self.results
        )
        expected_result_keys = tuple(
            (relationship, falsifier_id)
            for relationship in CarrierRelationship
            for falsifier_id in FALSIFIER_IDS
        )
        if result_keys != expected_result_keys:
            raise CarrierExperimentError(
                "report must retain every relationship-by-falsifier verdict slot"
            )

        metric_keys = tuple(
            (
                item.relationship,
                item.product_candidate_id,
                item.breadth_candidate_id,
            )
            for item in self.metric_displays
        )
        expected_metric_keys = tuple(
            (relationship, product_id, breadth_id)
            for relationship in CarrierRelationship
            for product_id in PRODUCT_CANDIDATE_IDS
            for breadth_id in BREADTH_CANDIDATE_IDS
        )
        if metric_keys != expected_metric_keys:
            raise CarrierExperimentError(
                "report must display all nine M-by-B combinations per relationship"
            )
        _require_text_items(self.hmmm, "hmmm")

    def result(
        self,
        relationship: CarrierRelationship,
        falsifier_id: str,
    ) -> FalsifierResult:
        """Return the unique retained verdict for one matrix position."""

        for item in self.results:
            if (
                item.relationship is relationship
                and item.falsifier_id == falsifier_id
            ):
                return item
        raise KeyError((relationship, falsifier_id))


def build_v05_witness_packet() -> tuple[SourceWitness, ...]:
    """Build the exact source packet declared by the v0.5 falsifier spec."""

    profile = EdcmWordGonolProfile()
    return tuple(
        SourceWitness(
            witness_id,
            profile.observe_turn(
                speaker_id="v0.5-witness",
                turn_index=index,
                text=text,
                source_id=witness_id,
            ),
        )
        for index, (witness_id, text) in enumerate(MINIMUM_WITNESS_TEXTS)
    )


def _point_key(point: LiftedCarrierPoint) -> tuple[tuple[str, str], ...]:
    return (
        ("breadth", point.breadth.hex()),
        ("lifted-angle", point.angle.hex()),
    )


def _visible_key(point: LiftedCarrierPoint) -> tuple[tuple[str, str], ...]:
    visible = project(point)
    if not hasattr(visible, "angle") or not hasattr(visible, "breadth"):
        raise CarrierExperimentError("directed cover trace requires a non-null point")
    return (
        ("breadth", visible.breadth.hex()),
        ("visible-angle", visible.angle.hex()),
    )


def _cover_state(
    state_id: str,
    point: LiftedCarrierPoint,
) -> CarrierExperimentState:
    return CarrierExperimentState(
        candidate=CarrierRelationship.COVER_CHART,
        state_id=state_id,
        complete_key=_point_key(point),
        visible_key=_visible_key(point),
        orientation="not-inferred-by-directed-cover",
        sidedness="not-inferred-by-directed-cover",
        sheet=(
            "first-lifted-representative"
            if point.angle < VISIBLE_PERIOD
            else "second-lifted-representative"
        ),
        source_links=("synthetic-directed-cover-state:s",),
        parent_observation_ids=(),
        completion_scope="directed-cover-comparison-only",
    )


def directed_cover_trace() -> CandidateTrace:
    """Adapt the implemented directed cover as C2 comparison evidence."""

    initial_point = LiftedCarrierPoint(1.0, 0.0)
    after_360_point = initial_point.deck_translate()
    after_720_point = after_360_point.deck_translate()
    inverse_point = after_360_point.rotate(-VISIBLE_PERIOD)
    return CandidateTrace(
        candidate=CarrierRelationship.COVER_CHART,
        version="directed-cover-floor/1",
        code_reference="ucns.mobius_experiment:directed_cover_trace",
        comparison_policy=exact_comparison_policy(
            name="directed-cover-state-exact",
            version="1",
        ),
        initial=_cover_state("cover:s", initial_point),
        after_360=_cover_state("cover:s+360", after_360_point),
        after_720=_cover_state("cover:s+720", after_720_point),
        inverse_after_360=_cover_state("cover:inverse(s+360)", inverse_point),
    )


def _result(
    relationship: CarrierRelationship,
    falsifier_id: str,
    verdict: FalsifierVerdict,
    detail: str,
    *,
    witness_ids: tuple[str, ...] = ("synthetic-state:s",),
    evidence: tuple[str, ...] = ("explicit v0.5 experiment evidence",),
    information_loss: tuple[str, ...] = (),
    error: str | None = None,
) -> FalsifierResult:
    return FalsifierResult(
        relationship=relationship,
        falsifier_id=falsifier_id,
        verdict=verdict,
        detail=detail,
        witness_ids=witness_ids,
        evidence=evidence,
        information_loss=information_loss,
        error=error,
    )


def _checked_result(
    relationship: CarrierRelationship,
    falsifier_id: str,
    check: Callable[[], bool],
    *,
    supported_detail: str,
    falsified_detail: str,
    evidence: tuple[str, ...],
) -> FalsifierResult:
    try:
        passed = check()
    except Exception as exc:
        return _result(
            relationship,
            falsifier_id,
            FalsifierVerdict.ERROR,
            "explicit comparison policy raised while evaluating retained evidence",
            evidence=evidence,
            error=f"{type(exc).__name__}: {exc}",
        )
    return _result(
        relationship,
        falsifier_id,
        (
            FalsifierVerdict.SUPPORTED
            if passed
            else FalsifierVerdict.FALSIFIED
        ),
        supported_detail if passed else falsified_detail,
        evidence=evidence,
    )


def evaluate_candidate_trace(
    trace: CandidateTrace,
) -> tuple[FalsifierResult, ...]:
    """Evaluate F06–F09 and, for C1, F14 over supplied trace evidence."""

    policy = trace.comparison_policy

    def same_complete(
        left: CarrierExperimentState,
        right: CarrierExperimentState,
    ) -> bool:
        return policy.matches(left.complete_identity, right.complete_identity)

    def same_visible(
        left: CarrierExperimentState,
        right: CarrierExperimentState,
    ) -> bool:
        return policy.matches(left.visible_identity, right.visible_identity)

    changed_distinction = (
        trace.initial.orientation != trace.after_360.orientation
        or trace.initial.sidedness != trace.after_360.sidedness
        or trace.initial.sheet != trace.after_360.sheet
    )
    results = [
        _checked_result(
            trace.candidate,
            "F06",
            lambda: (
                same_visible(trace.initial, trace.after_360)
                and not same_complete(trace.initial, trace.after_360)
                and changed_distinction
            ),
            supported_detail=(
                "360 degrees preserves the visible key and changes a retained "
                "complete-state distinction"
            ),
            falsified_detail=(
                "360-degree evidence failed visible coincidence, complete-state "
                "change, or named distinction retention"
            ),
            evidence=(
                f"policy:{policy.name}@{policy.version}",
                f"initial:{trace.initial.state_id}",
                f"after-360:{trace.after_360.state_id}",
            ),
        ),
        _checked_result(
            trace.candidate,
            "F07",
            lambda: same_complete(trace.initial, trace.after_720),
            supported_detail="720 degrees restores the complete retained state",
            falsified_detail="720-degree evidence does not restore complete state",
            evidence=(
                f"policy:{policy.name}@{policy.version}",
                f"initial:{trace.initial.state_id}",
                f"after-720:{trace.after_720.state_id}",
            ),
        ),
        _checked_result(
            trace.candidate,
            "F08",
            lambda: same_complete(trace.initial, trace.inverse_after_360),
            supported_detail="the declared inverse restores the complete prior state",
            falsified_detail="the declared inverse loses a retained distinction",
            evidence=(
                f"policy:{policy.name}@{policy.version}",
                f"initial:{trace.initial.state_id}",
                f"inverse:{trace.inverse_after_360.state_id}",
            ),
        ),
    ]

    if trace.after_720.completion_receipt is None:
        results.append(
            _result(
                trace.candidate,
                "F09",
                FalsifierVerdict.UNRESOLVED,
                "lifted return is retained but no scoped completion law is supplied",
                evidence=(
                    f"scope:{trace.after_720.completion_scope}",
                    "completion-receipt:absent-not-zero",
                ),
            )
        )
    else:
        results.append(
            _checked_result(
                trace.candidate,
                "F09",
                lambda: (
                    trace.after_720.completion_scope
                    == trace.initial.completion_scope
                    and bool(trace.after_720.completion_receipt)
                ),
                supported_detail=(
                    "completion receipt remains tied to the declared construction scope"
                ),
                falsified_detail="completion receipt changed or omitted its scope",
                evidence=(
                    f"scope:{trace.after_720.completion_scope}",
                    f"receipt:{trace.after_720.completion_receipt}",
                ),
            )
        )

    if trace.candidate is CarrierRelationship.DIRECT_MOBIUS:
        if CarrierRelationship.COVER_CHART in trace.declared_dependencies:
            results.append(
                _result(
                    trace.candidate,
                    "F14",
                    FalsifierVerdict.FALSIFIED,
                    "the direct carrier declares the cover as a state-law dependency",
                    evidence=(
                        f"code-reference:{trace.code_reference}",
                        "dependency:C2-cover-chart",
                    ),
                )
            )
        elif trace.native_independence_evidence:
            results.append(
                _result(
                    trace.candidate,
                    "F14",
                    FalsifierVerdict.SUPPORTED,
                    "native-state independence evidence is supplied without a cover dependency",
                    evidence=trace.native_independence_evidence,
                )
            )
        else:
            results.append(
                _result(
                    trace.candidate,
                    "F14",
                    FalsifierVerdict.UNRESOLVED,
                    "no native-state independence evidence is supplied",
                    evidence=(f"code-reference:{trace.code_reference}",),
                )
            )

    return tuple(results)


def evaluate_chart_map(evidence: CarrierMapEvidence) -> FalsifierResult:
    """Evaluate F12 without treating matching periods as a map."""

    policy = evidence.comparison_policy
    required_labels = set(REQUIRED_COMMUTATION_LABELS)
    supplied_labels = {item.label for item in evidence.commutation_witnesses}
    missing_distinctions = set(REQUIRED_MAP_DISTINCTIONS).difference(
        evidence.preserved_distinctions
    )
    lost_required = set(REQUIRED_MAP_DISTINCTIONS).intersection(
        evidence.information_loss
    )

    def check() -> bool:
        cover_round_trip = policy.matches(
            evidence.cover_original.complete_identity,
            evidence.cover_round_trip.complete_identity,
        )
        mobius_round_trip = policy.matches(
            evidence.mobius_original.complete_identity,
            evidence.mobius_round_trip.complete_identity,
        )
        commutes = all(
            policy.matches(
                item.expected.complete_identity,
                item.observed.complete_identity,
            )
            for item in evidence.commutation_witnesses
        )
        return (
            cover_round_trip
            and mobius_round_trip
            and required_labels.issubset(supplied_labels)
            and commutes
            and not missing_distinctions
            and not lost_required
        )

    return _checked_result(
        CarrierRelationship.COVER_CHART,
        "F12",
        check,
        supported_detail=(
            "explicit two-way maps round-trip and commute while preserving every "
            "required v0.5 distinction"
        ),
        falsified_detail=(
            "the chart evidence fails a round trip, commutation square, or required "
            "distinction-preservation obligation"
        ),
        evidence=(
            f"map:{evidence.map_id}@{evidence.version}",
            f"policy:{policy.name}@{policy.version}",
            f"domain:{','.join(evidence.witness_domain)}",
            (
                "missing-distinction:none"
                if not missing_distinctions
                else f"missing-distinction:{','.join(sorted(missing_distinctions))}"
            ),
            (
                "lost-required:none"
                if not lost_required
                else f"lost-required:{','.join(sorted(lost_required))}"
            ),
        ),
    )


def evaluate_separating_witness(
    witness: SeparatingWitness,
) -> FalsifierResult:
    """Evaluate the constructive evidence required by F13."""

    try:
        states_differ = not witness.comparison_policy.matches(
            witness.left_state.complete_identity,
            witness.right_state.complete_identity,
        )
    except Exception as exc:
        return _result(
            CarrierRelationship.INCOMPATIBLE,
            "F13",
            FalsifierVerdict.ERROR,
            "comparison policy raised while checking the separating states",
            witness_ids=(witness.witness_id,),
            evidence=(f"policy:{witness.comparison_policy.name}",),
            error=f"{type(exc).__name__}: {exc}",
        )

    all_maps_fail = set(witness.failed_map_ids) == set(witness.admissible_map_ids)
    if states_differ and witness.maps_identify_states and all_maps_fail:
        verdict = FalsifierVerdict.SUPPORTED
        detail = (
            "every declared admissible map identifies complete states separated "
            "by the named invariant"
        )
    else:
        verdict = FalsifierVerdict.INCONCLUSIVE
        detail = (
            "the witness does not yet separate every declared admissible map over "
            "distinct complete states"
        )
    return _result(
        CarrierRelationship.INCOMPATIBLE,
        "F13",
        verdict,
        detail,
        witness_ids=(witness.witness_id,),
        evidence=(
            f"violated-invariant:{witness.violated_invariant}",
            f"admissible-maps:{','.join(witness.admissible_map_ids)}",
            f"failed-maps:{','.join(witness.failed_map_ids)}",
            f"rollback:{witness.rollback_behavior}",
        ),
    )


def _baseline_results(
    witnesses: tuple[SourceWitness, ...],
) -> dict[tuple[CarrierRelationship, str], FalsifierResult]:
    witness_ids = tuple(item.witness_id for item in witnesses)
    matrix: dict[tuple[CarrierRelationship, str], FalsifierResult] = {}
    for relationship in CarrierRelationship:
        for falsifier_id in FALSIFIER_IDS:
            matrix[(relationship, falsifier_id)] = _result(
                relationship,
                falsifier_id,
                FalsifierVerdict.UNRESOLVED,
                "the current experiment has not supplied this relationship evidence",
                witness_ids=witness_ids,
                evidence=("hmmm:unresolved-v0.5-obligation",),
            )

        matrix[(relationship, "F02")] = _result(
            relationship,
            "F02",
            FalsifierVerdict.SUPPORTED,
            "every minimum witness reconstructs its exact source without normalization",
            witness_ids=witness_ids,
            evidence=("segment-concatenation equals exact source for all witnesses",),
        )
        matrix[(relationship, "F03")] = _result(
            relationship,
            "F03",
            FalsifierVerdict.UNRESOLVED,
            "word initiation labels and counts are retained but causal pre/post state is not yet supplied",
            witness_ids=witness_ids,
            evidence=("current EDCM profile records mobius-twist initiation labels",),
        )
        matrix[(relationship, "F04")] = _result(
            relationship,
            "F04",
            FalsifierVerdict.UNRESOLVED,
            "repeated SPACE evidence survives but singular seam causality is not yet formalized",
            witness_ids=("W-repeat-space",),
            evidence=("both U+0020 source occurrences remain ordered",),
        )
        matrix[(relationship, "F05")] = _result(
            relationship,
            "F05",
            FalsifierVerdict.SUPPORTED,
            "every complete speaker turn retains exactly one support unit",
            witness_ids=witness_ids,
            evidence=("unit_support=1.0 for every minimum witness",),
        )
        matrix[(relationship, "F10")] = _result(
            relationship,
            "F10",
            FalsifierVerdict.INCONCLUSIVE,
            "source order and multiplicity survive observation but candidate mapping has not been shown lossless",
            witness_ids=("W-repeat-word", "W-order-left", "W-order-right"),
            evidence=("ordered source occurrences remain distinct before carrier mapping",),
        )
        matrix[(relationship, "F15")] = _result(
            relationship,
            "F15",
            FalsifierVerdict.SUPPORTED,
            "all nine M-by-B candidate displays are present without values or selection",
            witness_ids=witness_ids,
            evidence=("nine explicit unresolved metric display cells",),
        )
        matrix[(relationship, "F16")] = _result(
            relationship,
            "F16",
            FalsifierVerdict.INCONCLUSIVE,
            "no scalar, radial, or visible metric projection is emitted by this report",
            witness_ids=witness_ids,
            evidence=("projection-count:0",),
        )
    return matrix


def _metric_displays() -> tuple[MetricDisplay, ...]:
    return tuple(
        MetricDisplay(
            relationship=relationship,
            product_candidate_id=product_id,
            breadth_candidate_id=breadth_id,
            verdict=FalsifierVerdict.UNRESOLVED,
            value=None,
            detail=(
                "displayed without evaluation: carrier experiment does not select "
                "or silently fill metric candidates"
            ),
        )
        for relationship in CarrierRelationship
        for product_id in PRODUCT_CANDIDATE_IDS
        for breadth_id in BREADTH_CANDIDATE_IDS
    )


def run_v05_carrier_experiment(
    *,
    direct_trace: CandidateTrace | None = None,
    chart_map: CarrierMapEvidence | None = None,
    separating_witness: SeparatingWitness | None = None,
    report_id: str = "ucns-edcm-v0.5:carrier-experiment",
) -> CarrierExperimentReport:
    """Run the complete option-preserving v0.5 report matrix.

    The directed cover trace is always evaluated because it is implemented
    comparison evidence.  Direct-carrier, map, and incompatibility evidence are
    optional explicit inputs and never become defaults.
    """

    if (
        direct_trace is not None
        and direct_trace.candidate is not CarrierRelationship.DIRECT_MOBIUS
    ):
        raise CarrierExperimentError("direct_trace must use C1-direct-mobius")

    witnesses = build_v05_witness_packet()
    matrix = _baseline_results(witnesses)

    for item in evaluate_candidate_trace(directed_cover_trace()):
        matrix[(item.relationship, item.falsifier_id)] = item

    if direct_trace is not None:
        for item in evaluate_candidate_trace(direct_trace):
            matrix[(item.relationship, item.falsifier_id)] = item

    if chart_map is not None:
        chart_result = evaluate_chart_map(chart_map)
        matrix[(chart_result.relationship, chart_result.falsifier_id)] = chart_result
        if chart_result.verdict is FalsifierVerdict.SUPPORTED:
            matrix[(CarrierRelationship.INCOMPATIBLE, "F13")] = _result(
                CarrierRelationship.INCOMPATIBLE,
                "F13",
                FalsifierVerdict.FALSIFIED,
                "a reversible preserving chart map exists for the declared witness domain",
                witness_ids=chart_map.witness_domain,
                evidence=(f"map:{chart_map.map_id}@{chart_map.version}",),
            )

    if separating_witness is not None:
        separating_result = evaluate_separating_witness(separating_witness)
        matrix[
            (separating_result.relationship, separating_result.falsifier_id)
        ] = separating_result

    ordered_results = tuple(
        matrix[(relationship, falsifier_id)]
        for relationship in CarrierRelationship
        for falsifier_id in FALSIFIER_IDS
    )
    return CarrierExperimentReport(
        report_id=report_id,
        witnesses=witnesses,
        relationships=tuple(CarrierRelationship),
        results=ordered_results,
        metric_displays=_metric_displays(),
        hmmm=(
            "direct Mobius carrier state and element-assignment law remain unresolved",
            "no chart map or complete incompatibility proof is supplied by default",
            "higher-gonol composition and circle-epicycle-disk-sphere transitions remain unresolved",
            "lifted 720-degree return is not promoted to scoped completion",
        ),
    )


__all__ = [
    "BREADTH_CANDIDATE_IDS",
    "FALSIFIER_IDS",
    "MINIMUM_WITNESS_TEXTS",
    "PRODUCT_CANDIDATE_IDS",
    "REQUIRED_COMMUTATION_LABELS",
    "REQUIRED_MAP_DISTINCTIONS",
    "V05_EXPERIMENT_SCHEMA_ID",
    "V05_EXPERIMENT_SCHEMA_VERSION",
    "V05_SELECTION_EFFECT",
    "CandidateTrace",
    "CarrierExperimentError",
    "CarrierExperimentReport",
    "CarrierExperimentState",
    "CarrierMapEvidence",
    "CarrierRelationship",
    "FalsifierResult",
    "FalsifierVerdict",
    "MapCommutationWitness",
    "MetricDisplay",
    "SeparatingWitness",
    "SourceWitness",
    "build_v05_witness_packet",
    "directed_cover_trace",
    "evaluate_candidate_trace",
    "evaluate_chart_map",
    "evaluate_separating_witness",
    "run_v05_carrier_experiment",
]
