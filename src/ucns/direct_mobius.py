# === MODULE_BUILD ===
# id: edcm_native_direct_mobius_candidate
#   module_name: direct_mobius
#   module_kind: experiment
#   summary: supplies a native framed Mobius root-loop candidate with Structural Null initiation and exact rational-turn motion evidence
#   owner: Erin Spencer
#   public_surface: StructuralNullIdentity, StructuralNullManifestation, StructuralNullKind, NativeMobiusFrame, NativeMobiusState, MobiusInitiationEvent, NativeMobiusInitiationPacket, DirectMobiusCandidateReport, build_native_mobius_initiation_packet, native_direct_mobius_trace, run_v06_direct_mobius_experiment
#   internal_surface: validation helpers and bounded C1 falsifier-result adapters
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact source witnesses and every SPACE manifestation remain linked without normalization
#   admin_only: false
#   tests: tests/test_direct_mobius.py
#   rollout: explicit UCNS-only v0.6 experiment candidate; no carrier selection, completion, EDCM activation, or METAPAT activation
#   rollback: remove this module, its exports, tests, and v0.6 candidate document while retaining the v0.5 comparison harness
#   requires: edcm_word_gonol_profile, edcm_mobius_carrier_experiment
#   since: 2026-07-29
#   unresolved: arbitrary element assignment, transverse carrier coordinates, chart map or incompatibility proof, scoped completion, higher-gonol composition, circle-epicycle-disk-sphere transitions
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: direct_mobius_structural_null_is_typed_and_source_preserving
#   given: the v0.6 minimum witness packet is adapted to native Mobius initiation evidence
#   then: every exact SPACE and turn-boundary manifestation remains distinct while sharing one typed Structural Null carrier origin that is not numeric zero, absence, or completion
#   class: evidence
#   since: 2026-07-29
#
# id: direct_mobius_initiation_is_causal_and_cardinality_exact
#   given: the v0.6 initiation packet is built
#   then: every word gonol has exactly one pre-state Structural Null cause and one framed root-loop post-state linked to its exact source start
#   class: correctness
#   since: 2026-07-29
#
# id: direct_mobius_repeated_space_preserves_singular_origin_and_occurrences
#   given: exact source A SPACE SPACE B is adapted
#   then: both SPACE occurrences remain distinct manifestations of the singular origin and the immediately preceding second occurrence causes B initiation
#   class: evidence
#   since: 2026-07-29
#
# id: direct_mobius_native_motion_has_360_change_720_return_and_inverse
#   given: a framed root-loop state advances under the native quotient law
#   then: one turn preserves visible phase and reverses the retained local frame, two turns restore complete state, and negative motion is an exact inverse
#   class: correctness
#   since: 2026-07-29
#
# id: direct_mobius_candidate_is_independent_and_nonselecting
#   given: the v0.6 direct candidate enters the v0.5 carrier experiment
#   then: C1 motion and independence evidence is evaluated without a directed-cover dependency, selected carrier, completion receipt, chart claim, incompatibility claim, or consumer activation
#   class: doctrine
#   since: 2026-07-29
#
# id: direct_mobius_report_retains_unresolved_frontier
#   given: the complete v0.6 report is produced
#   then: arbitrary element assignment, transverse coordinates, scoped completion, higher geometry, higher-gonol composition, and the C1-C2 relationship remain explicit hmmm constraints
#   class: safety
#   since: 2026-07-29
# === END CONTRACTS ===

"""Native direct-Möbius root-loop candidate for UCNS–EDCM v0.6.

The candidate implements the exact quotient law declared in
``docs/DIRECT_MOBIUS_CANDIDATE_V06.md``:

    (t, ε) ~ (t + n, (-1)^n ε)

for rational turns ``t`` and integer windings ``n``.  It retains a local frame
as native Möbius state, so a 360-degree visible return is not complete identity
and a 720-degree motion restores the complete root-loop state.

This module intentionally stops before arbitrary element assignment,
transverse coordinates, scoped completion, a C1↔C2 map, higher geometry,
higher-gonol composition, EDCM activation, or METAPAT activation.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from fractions import Fraction

from .edcm import edcm_carrier_position
from .mobius_experiment import (
    CandidateTrace,
    CarrierExperimentReport,
    CarrierExperimentState,
    CarrierRelationship,
    FalsifierResult,
    FalsifierVerdict,
    SourceWitness,
    build_v05_witness_packet,
    run_v05_carrier_experiment,
)
from .comparison import exact_comparison_policy


V06_DIRECT_MOBIUS_SCHEMA_ID = "ucns.edcm.direct-mobius-candidate"
V06_DIRECT_MOBIUS_SCHEMA_VERSION = "0.6.0"
V06_SELECTION_EFFECT = "none"
STRUCTURAL_NULL_ORIGIN_ID = "ucns.edcm.structural-null:space-origin"
NATIVE_MOBIUS_LAW_ID = "ucns.edcm.native-mobius-root-loop"
NATIVE_MOBIUS_LAW_VERSION = "0.6.0"
NATIVE_MOBIUS_SCOPE = "native-mobius-framed-root-loop-candidate-only"


class DirectMobiusError(ValueError):
    """Raised when evidence violates the bounded v0.6 candidate contract."""


def _require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise DirectMobiusError(f"{field} must be nonempty text")


def _require_text_items(
    values: tuple[str, ...],
    field: str,
    *,
    allow_empty: bool = False,
) -> None:
    if not values and not allow_empty:
        raise DirectMobiusError(f"{field} must retain at least one item")
    for value in values:
        _require_text(value, field)


@dataclass(frozen=True, slots=True)
class StructuralNullIdentity:
    """Typed singular carrier-origin identity; never a scalar zero value."""

    origin_id: str = STRUCTURAL_NULL_ORIGIN_ID
    carrier_position: int = 0
    role: str = "structural-null-hidden-zero"

    def __post_init__(self) -> None:
        if self.origin_id != STRUCTURAL_NULL_ORIGIN_ID:
            raise DirectMobiusError("Structural Null origin identity is fixed")
        if self.carrier_position != 0:
            raise DirectMobiusError("Structural Null must remain at carrier position zero")
        if self.role != "structural-null-hidden-zero":
            raise DirectMobiusError("Structural Null role is fixed")


STRUCTURAL_NULL_ORIGIN = StructuralNullIdentity()


class StructuralNullKind(str, Enum):
    """The two source-preserving manifestations admitted by v0.6."""

    TURN_BOUNDARY = "turn-boundary-hidden-zero"
    SPACE_MANIFESTATION = "exact-space-manifestation"


@dataclass(frozen=True, slots=True)
class StructuralNullManifestation:
    """One exact or virtual boundary manifestation of the singular origin."""

    manifestation_id: str
    witness_id: str
    kind: StructuralNullKind
    source_offset: int | None
    source_value: str | None
    origin: StructuralNullIdentity = STRUCTURAL_NULL_ORIGIN

    def __post_init__(self) -> None:
        _require_text(self.manifestation_id, "manifestation_id")
        _require_text(self.witness_id, "witness_id")
        if self.origin is not STRUCTURAL_NULL_ORIGIN:
            raise DirectMobiusError(
                "every manifestation must reference the singular Structural Null"
            )
        if self.kind is StructuralNullKind.TURN_BOUNDARY:
            if self.source_offset is not None or self.source_value is not None:
                raise DirectMobiusError(
                    "turn-boundary hidden zero has no literal source occurrence"
                )
            return
        if self.source_offset is None or self.source_offset < 0:
            raise DirectMobiusError(
                "exact SPACE manifestation requires a nonnegative source offset"
            )
        if (
            not isinstance(self.source_value, str)
            or len(self.source_value) != 1
            or edcm_carrier_position(self.source_value) != 0
        ):
            raise DirectMobiusError(
                "exact SPACE manifestation must retain a source scalar assigned to origin"
            )

    @property
    def source_reference(self) -> str:
        if self.kind is StructuralNullKind.TURN_BOUNDARY:
            return f"{self.witness_id}:turn-boundary"
        assert self.source_offset is not None
        assert self.source_value is not None
        return (
            f"{self.witness_id}:offset:{self.source_offset}:"
            f"U+{ord(self.source_value):04X}"
        )


class NativeMobiusFrame(str, Enum):
    """Retained local-frame sign on the native Möbius root loop."""

    POSITIVE = "positive-local-frame"
    REVERSED = "reversed-local-frame"

    @property
    def sign(self) -> int:
        return 1 if self is NativeMobiusFrame.POSITIVE else -1

    def flipped(self) -> NativeMobiusFrame:
        if self is NativeMobiusFrame.POSITIVE:
            return NativeMobiusFrame.REVERSED
        return NativeMobiusFrame.POSITIVE


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True, slots=True)
class NativeMobiusState:
    """Canonical framed representative of the native Möbius root-loop quotient."""

    phase_turns: Fraction
    frame: NativeMobiusFrame
    source_links: tuple[str, ...]
    parent_observation_ids: tuple[str, ...]
    initiation_event_id: str
    completion_scope: str = NATIVE_MOBIUS_SCOPE

    def __post_init__(self) -> None:
        if not isinstance(self.phase_turns, Fraction):
            raise DirectMobiusError("phase_turns must be an exact Fraction")
        if not Fraction(0) <= self.phase_turns < Fraction(1):
            raise DirectMobiusError("phase_turns must be canonical in [0, 1)")
        if not isinstance(self.frame, NativeMobiusFrame):
            raise DirectMobiusError("frame must be a NativeMobiusFrame")
        _require_text_items(self.source_links, "source_links")
        _require_text_items(
            self.parent_observation_ids,
            "parent_observation_ids",
            allow_empty=True,
        )
        _require_text(self.initiation_event_id, "initiation_event_id")
        if self.completion_scope != NATIVE_MOBIUS_SCOPE:
            raise DirectMobiusError("native Möbius candidate scope is fixed")

    def advance(self, turns: Fraction | int) -> NativeMobiusState:
        """Advance by exact rational turns under the native Möbius quotient law."""

        if isinstance(turns, bool):
            raise DirectMobiusError("turn motion cannot be boolean")
        if isinstance(turns, int):
            turns = Fraction(turns)
        if not isinstance(turns, Fraction):
            raise DirectMobiusError("turn motion must be int or exact Fraction")

        total = self.phase_turns + turns
        whole_turns = total.numerator // total.denominator
        phase = total - whole_turns
        frame = self.frame
        if whole_turns % 2:
            frame = frame.flipped()
        return replace(self, phase_turns=phase, frame=frame)

    @property
    def visible_key(self) -> tuple[tuple[str, str], ...]:
        return (
            ("law", f"{NATIVE_MOBIUS_LAW_ID}@{NATIVE_MOBIUS_LAW_VERSION}"),
            ("visible-phase-turns", _fraction_key(self.phase_turns)),
        )

    @property
    def complete_key(self) -> tuple[tuple[str, str], ...]:
        return (
            ("law", f"{NATIVE_MOBIUS_LAW_ID}@{NATIVE_MOBIUS_LAW_VERSION}"),
            ("phase-turns", _fraction_key(self.phase_turns)),
            ("local-frame", self.frame.value),
        )

    def as_experiment_state(self, state_id: str) -> CarrierExperimentState:
        """Adapt native C1 state without importing any directed-cover field."""

        _require_text(state_id, "state_id")
        return CarrierExperimentState(
            candidate=CarrierRelationship.DIRECT_MOBIUS,
            state_id=state_id,
            complete_key=self.complete_key,
            visible_key=self.visible_key,
            orientation=(
                "native-frame-coherent"
                if self.frame is NativeMobiusFrame.POSITIVE
                else "native-frame-reversed"
            ),
            sidedness=(
                "native-local-side-positive"
                if self.frame is NativeMobiusFrame.POSITIVE
                else "native-local-side-reversed"
            ),
            sheet="not-applicable-native-mobius",
            source_links=self.source_links,
            parent_observation_ids=self.parent_observation_ids,
            completion_scope=self.completion_scope,
            initiation_event_id=self.initiation_event_id,
            completion_receipt=None,
        )


@dataclass(frozen=True, slots=True)
class MobiusInitiationEvent:
    """Causal transition from one Structural Null manifestation into native state."""

    event_id: str
    witness_id: str
    word_index: int
    source_start: int
    boundary: StructuralNullManifestation
    post_state: NativeMobiusState

    def __post_init__(self) -> None:
        _require_text(self.event_id, "event_id")
        _require_text(self.witness_id, "witness_id")
        if self.word_index < 0:
            raise DirectMobiusError("word_index must be nonnegative")
        if self.source_start < 0:
            raise DirectMobiusError("source_start must be nonnegative")
        if self.boundary.witness_id != self.witness_id:
            raise DirectMobiusError("initiation boundary must belong to the same witness")
        if self.post_state.initiation_event_id != self.event_id:
            raise DirectMobiusError("post-state must retain its initiation event identity")
        if self.post_state.phase_turns != 0:
            raise DirectMobiusError("post-initiation phase must begin at Structural Null")
        if self.post_state.frame is not NativeMobiusFrame.POSITIVE:
            raise DirectMobiusError("post-initiation native frame must begin positive")
        if f"witness:{self.witness_id}" not in self.post_state.source_links:
            raise DirectMobiusError("post-state must link to the exact source witness")


@dataclass(frozen=True, slots=True)
class NativeMobiusInitiationPacket:
    """Complete v0.6 source, null-manifestation, and initiation evidence."""

    witnesses: tuple[SourceWitness, ...]
    manifestations: tuple[StructuralNullManifestation, ...]
    initiations: tuple[MobiusInitiationEvent, ...]

    def __post_init__(self) -> None:
        if not self.witnesses:
            raise DirectMobiusError("initiation packet requires source witnesses")
        witness_ids = tuple(item.witness_id for item in self.witnesses)
        if len(set(witness_ids)) != len(witness_ids):
            raise DirectMobiusError("witness ids must be unique")
        if any(item.witness_id not in witness_ids for item in self.manifestations):
            raise DirectMobiusError("every manifestation must link to a packet witness")
        if any(item.witness_id not in witness_ids for item in self.initiations):
            raise DirectMobiusError("every initiation must link to a packet witness")
        expected_words = sum(len(item.turn.word_gonols) for item in self.witnesses)
        if len(self.initiations) != expected_words:
            raise DirectMobiusError(
                "initiation cardinality must equal the exact word-gonol count"
            )
        event_ids = tuple(item.event_id for item in self.initiations)
        if len(set(event_ids)) != len(event_ids):
            raise DirectMobiusError("initiation event ids must be unique")
        manifestation_ids = tuple(item.manifestation_id for item in self.manifestations)
        if len(set(manifestation_ids)) != len(manifestation_ids):
            raise DirectMobiusError("Structural Null manifestation ids must be unique")
        if any(item.origin is not STRUCTURAL_NULL_ORIGIN for item in self.manifestations):
            raise DirectMobiusError("packet must retain one singular Structural Null")

    def witness_manifestations(
        self,
        witness_id: str,
    ) -> tuple[StructuralNullManifestation, ...]:
        return tuple(
            item for item in self.manifestations if item.witness_id == witness_id
        )

    def witness_initiations(
        self,
        witness_id: str,
    ) -> tuple[MobiusInitiationEvent, ...]:
        return tuple(item for item in self.initiations if item.witness_id == witness_id)


@dataclass(frozen=True, slots=True)
class DirectMobiusCandidateReport:
    """Bounded v0.6 C1 evidence plus the complete option-preserving matrix."""

    report_id: str
    packet: NativeMobiusInitiationPacket
    trace: CandidateTrace
    experiment: CarrierExperimentReport
    hmmm: tuple[str, ...]
    schema_id: str = V06_DIRECT_MOBIUS_SCHEMA_ID
    schema_version: str = V06_DIRECT_MOBIUS_SCHEMA_VERSION
    selection_effect: str = V06_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_text(self.report_id, "report_id")
        if self.schema_id != V06_DIRECT_MOBIUS_SCHEMA_ID:
            raise DirectMobiusError("v0.6 report schema identity mismatch")
        if self.schema_version != V06_DIRECT_MOBIUS_SCHEMA_VERSION:
            raise DirectMobiusError("v0.6 report schema version mismatch")
        if self.selection_effect != V06_SELECTION_EFFECT:
            raise DirectMobiusError("v0.6 candidate cannot select a carrier")
        if self.trace.candidate is not CarrierRelationship.DIRECT_MOBIUS:
            raise DirectMobiusError("v0.6 trace must remain C1-direct-mobius")
        if self.trace.declared_dependencies:
            raise DirectMobiusError("native C1 trace cannot depend on another carrier")
        if self.experiment.selection_effect != V06_SELECTION_EFFECT:
            raise DirectMobiusError("embedded experiment cannot select a carrier")
        for falsifier_id in ("F01", "F03", "F04", "F06", "F07", "F08", "F14"):
            if (
                self.experiment.result(
                    CarrierRelationship.DIRECT_MOBIUS,
                    falsifier_id,
                ).verdict
                is not FalsifierVerdict.SUPPORTED
            ):
                raise DirectMobiusError(
                    f"bounded v0.6 evidence must support C1 {falsifier_id}"
                )
        if (
            self.experiment.result(
                CarrierRelationship.DIRECT_MOBIUS,
                "F09",
            ).verdict
            is not FalsifierVerdict.UNRESOLVED
        ):
            raise DirectMobiusError("v0.6 must not promote carrier return to completion")
        _require_text_items(self.hmmm, "hmmm")


def build_native_mobius_initiation_packet() -> NativeMobiusInitiationPacket:
    """Adapt every v0.5 source witness to the bounded native initiation law."""

    witnesses = build_v05_witness_packet()
    manifestations: list[StructuralNullManifestation] = []
    initiations: list[MobiusInitiationEvent] = []

    for witness in witnesses:
        turn_boundary = StructuralNullManifestation(
            manifestation_id=f"{witness.witness_id}:turn-boundary",
            witness_id=witness.witness_id,
            kind=StructuralNullKind.TURN_BOUNDARY,
            source_offset=None,
            source_value=None,
        )
        manifestations.append(turn_boundary)

        spaces_by_offset: dict[int, StructuralNullManifestation] = {}
        for boundary in witness.turn.nesting_boundaries:
            manifestation = StructuralNullManifestation(
                manifestation_id=(
                    f"{witness.witness_id}:space:"
                    f"{boundary.token.codepoint_offset}:"
                    f"{boundary.token.code_point}"
                ),
                witness_id=witness.witness_id,
                kind=StructuralNullKind.SPACE_MANIFESTATION,
                source_offset=boundary.token.codepoint_offset,
                source_value=boundary.token.value,
            )
            manifestations.append(manifestation)
            spaces_by_offset[boundary.token.codepoint_offset] = manifestation

        for word in witness.turn.word_gonols:
            if word.source_start == 0:
                cause = turn_boundary
            else:
                try:
                    cause = spaces_by_offset[word.source_start - 1]
                except KeyError as exc:
                    raise DirectMobiusError(
                        "word initiation lacks an immediately preceding SPACE cause"
                    ) from exc
            event_id = (
                f"{witness.witness_id}:word:{word.word_index}:"
                f"offset:{word.source_start}:initiation"
            )
            post_state = NativeMobiusState(
                phase_turns=Fraction(0),
                frame=NativeMobiusFrame.POSITIVE,
                source_links=(
                    f"witness:{witness.witness_id}",
                    f"word:{witness.witness_id}:{word.word_index}",
                    f"boundary:{cause.manifestation_id}",
                ),
                parent_observation_ids=(f"turn:{witness.witness_id}",),
                initiation_event_id=event_id,
            )
            initiations.append(
                MobiusInitiationEvent(
                    event_id=event_id,
                    witness_id=witness.witness_id,
                    word_index=word.word_index,
                    source_start=word.source_start,
                    boundary=cause,
                    post_state=post_state,
                )
            )

    return NativeMobiusInitiationPacket(
        witnesses=witnesses,
        manifestations=tuple(manifestations),
        initiations=tuple(initiations),
    )


def native_direct_mobius_trace(
    packet: NativeMobiusInitiationPacket | None = None,
) -> CandidateTrace:
    """Build C1 motion evidence from the W-first native initiation state."""

    if packet is None:
        packet = build_native_mobius_initiation_packet()
    events = packet.witness_initiations("W-first")
    if len(events) != 1:
        raise DirectMobiusError("W-first must supply exactly one initiation")
    initial = events[0].post_state
    after_360 = initial.advance(1)
    after_720 = initial.advance(2)
    inverse_after_360 = after_360.advance(-1)
    return CandidateTrace(
        candidate=CarrierRelationship.DIRECT_MOBIUS,
        version=f"native-mobius-root-loop/{NATIVE_MOBIUS_LAW_VERSION}",
        code_reference="ucns.direct_mobius:native_direct_mobius_trace",
        comparison_policy=exact_comparison_policy(
            name="native-mobius-complete-state-exact",
            version=NATIVE_MOBIUS_LAW_VERSION,
        ),
        initial=initial.as_experiment_state("native-mobius:s"),
        after_360=after_360.as_experiment_state("native-mobius:s+360"),
        after_720=after_720.as_experiment_state("native-mobius:s+720"),
        inverse_after_360=inverse_after_360.as_experiment_state(
            "native-mobius:inverse(s+360)"
        ),
        declared_dependencies=(),
        native_independence_evidence=(
            f"native-law:{NATIVE_MOBIUS_LAW_ID}@{NATIVE_MOBIUS_LAW_VERSION}",
            "quotient:(t,epsilon)~(t+n,(-1)^n epsilon)",
            "directed-cover-dependency:none",
            "cover-sheet-field:not-applicable-native-mobius",
        ),
    )


def _falsifier_result(
    falsifier_id: str,
    verdict: FalsifierVerdict,
    detail: str,
    *,
    witness_ids: tuple[str, ...],
    evidence: tuple[str, ...],
) -> FalsifierResult:
    return FalsifierResult(
        relationship=CarrierRelationship.DIRECT_MOBIUS,
        falsifier_id=falsifier_id,
        verdict=verdict,
        detail=detail,
        witness_ids=witness_ids,
        evidence=evidence,
    )


def _replace_results(
    report: CarrierExperimentReport,
    replacements: tuple[FalsifierResult, ...],
) -> CarrierExperimentReport:
    matrix = {
        (item.relationship, item.falsifier_id): item for item in report.results
    }
    for item in replacements:
        matrix[(item.relationship, item.falsifier_id)] = item
    ordered = tuple(
        matrix[(relationship, falsifier_id)]
        for relationship in report.relationships
        for falsifier_id in tuple(f"F{index:02d}" for index in range(1, 17))
    )
    return replace(
        report,
        results=ordered,
        hmmm=(
            "native C1 framed root-loop state is implemented candidate evidence; arbitrary element assignment and transverse coordinates remain unresolved",
            "no C1-to-C2 chart map or complete incompatibility proof is supplied",
            "higher-gonol composition and circle-epicycle-disk-sphere transitions remain unresolved",
            "720-degree root-state return is not promoted to scoped completion",
        ),
    )


def run_v06_direct_mobius_experiment(
    *,
    report_id: str = "ucns-edcm-v0.6:direct-mobius-candidate",
) -> DirectMobiusCandidateReport:
    """Run the bounded C1 candidate through the complete v0.5 matrix."""

    packet = build_native_mobius_initiation_packet()
    trace = native_direct_mobius_trace(packet)
    base = run_v05_carrier_experiment(
        direct_trace=trace,
        report_id=f"{report_id}:comparison-matrix",
    )

    witness_ids = tuple(item.witness_id for item in packet.witnesses)
    repeat_spaces = tuple(
        item
        for item in packet.witness_manifestations("W-repeat-space")
        if item.kind is StructuralNullKind.SPACE_MANIFESTATION
    )
    repeat_initiations = packet.witness_initiations("W-repeat-space")
    repeated_space_supported = (
        len(repeat_spaces) == 2
        and len(repeat_initiations) == 2
        and repeat_initiations[1].boundary is repeat_spaces[1]
        and repeat_spaces[0].origin is repeat_spaces[1].origin
    )
    all_words = sum(len(item.turn.word_gonols) for item in packet.witnesses)
    initiation_supported = (
        len(packet.initiations) == all_words
        and all(item.post_state.initiation_event_id == item.event_id for item in packet.initiations)
    )
    typed_null_supported = (
        all(item.origin is STRUCTURAL_NULL_ORIGIN for item in packet.manifestations)
        and STRUCTURAL_NULL_ORIGIN != 0
        and STRUCTURAL_NULL_ORIGIN != ""
        and STRUCTURAL_NULL_ORIGIN is not None
    )

    experiment = _replace_results(
        base,
        (
            _falsifier_result(
                "F01",
                (
                    FalsifierVerdict.SUPPORTED
                    if typed_null_supported
                    else FalsifierVerdict.FALSIFIED
                ),
                (
                    "typed Structural Null remains distinct from scalar zero, empty text, absence, and every source manifestation"
                    if typed_null_supported
                    else "Structural Null typing or manifestation separation failed"
                ),
                witness_ids=witness_ids,
                evidence=(
                    f"origin:{STRUCTURAL_NULL_ORIGIN.origin_id}",
                    f"manifestations:{len(packet.manifestations)}",
                    "numeric-zero-equality:false",
                    "empty-text-equality:false",
                    "absence-identity:false",
                ),
            ),
            _falsifier_result(
                "F03",
                (
                    FalsifierVerdict.SUPPORTED
                    if initiation_supported
                    else FalsifierVerdict.FALSIFIED
                ),
                (
                    "every word gonol has one source-linked Structural Null cause and framed native post-state"
                    if initiation_supported
                    else "initiation cardinality or causal post-state linkage failed"
                ),
                witness_ids=witness_ids,
                evidence=(
                    f"word-gonols:{all_words}",
                    f"initiation-events:{len(packet.initiations)}",
                    "cause:turn-boundary-or-immediately-preceding-exact-SPACE",
                ),
            ),
            _falsifier_result(
                "F04",
                (
                    FalsifierVerdict.SUPPORTED
                    if repeated_space_supported
                    else FalsifierVerdict.FALSIFIED
                ),
                (
                    "both repeated SPACE occurrences survive as distinct manifestations of one origin and the immediate second occurrence causes B initiation"
                    if repeated_space_supported
                    else "repeated SPACE singular-origin or immediate-cause evidence failed"
                ),
                witness_ids=("W-repeat-space",),
                evidence=(
                    f"exact-space-manifestations:{len(repeat_spaces)}",
                    f"singular-origin:{STRUCTURAL_NULL_ORIGIN.origin_id}",
                    "source-normalization:none",
                ),
            ),
        ),
    )

    return DirectMobiusCandidateReport(
        report_id=report_id,
        packet=packet,
        trace=trace,
        experiment=experiment,
        hmmm=experiment.hmmm,
    )


__all__ = [
    "NATIVE_MOBIUS_LAW_ID",
    "NATIVE_MOBIUS_LAW_VERSION",
    "NATIVE_MOBIUS_SCOPE",
    "STRUCTURAL_NULL_ORIGIN",
    "STRUCTURAL_NULL_ORIGIN_ID",
    "V06_DIRECT_MOBIUS_SCHEMA_ID",
    "V06_DIRECT_MOBIUS_SCHEMA_VERSION",
    "V06_SELECTION_EFFECT",
    "DirectMobiusCandidateReport",
    "DirectMobiusError",
    "MobiusInitiationEvent",
    "NativeMobiusFrame",
    "NativeMobiusInitiationPacket",
    "NativeMobiusState",
    "StructuralNullIdentity",
    "StructuralNullKind",
    "StructuralNullManifestation",
    "build_native_mobius_initiation_packet",
    "native_direct_mobius_trace",
    "run_v06_direct_mobius_experiment",
]
