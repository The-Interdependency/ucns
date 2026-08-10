# === MODULE_BUILD ===
# id: ucns_mobius_seed_model
#   module_name: mobius_seed_model
#   module_kind: experiment
#   summary: defines occurrence-preserving Möbius Seed bands, pair relations, crossing obligations, and projected superposition coordinates
#   owner: Erin Spencer
#   public_surface: schema constants, TwistChirality, SeedBandRole, PairRelationship, CoordinateRole, MobiusSeedBand, CenterlineIntersectionOccurrence, BoundaryCrossingObligation, MobiusSeedPair, SuperpositionCoordinate
#   internal_surface: typed validation of candidate standing and cardinality
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: source hypotheses, candidate assumptions, and unresolved claims remain separately labeled
#   admin_only: false
#   tests: tests/test_mobius_seed_model.py
#   rollout: nonselecting typed evidence model for the primitive-seven construction
#   rollback: remove this module and dependent candidate files while retaining the source record
#   requires: ucns_mobius_seed_exact_geometry, edcm_native_direct_mobius_candidate
#   since: 2026-08-10
#   unresolved: smooth embedding, boundary transversality, physical standing, and spectral interpretation
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: mobius_seed_band_retains_one_turn_reversal_and_two_turn_return
#   given: one phase- and chirality-labeled Seed band is sampled
#   then: one turn reverses its local transverse side and two turns restore the complete sampled point
#   class: correctness
#   since: 2026-08-10
#
# id: mobius_seed_model_preserves_pair_and_coordinate_occurrences
#   given: pair events and shared projected coordinates are recorded
#   then: pair identity, crossing obligations, multiplicity, nonvertex standing, and non-Structural-Null standing remain explicit without occurrence merging
#   class: safety
#   since: 2026-08-10
# === END CONTRACTS ===

"""Typed evidence model for the Möbius Seed of Life candidate."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum
from fractions import Fraction
from math import cos, isfinite, pi, sin

from .direct_mobius import NativeMobiusFrame
from .mobius_seed_exact import (
    HexCoordinate,
    MobiusSeedError,
    ORIGIN_POINT,
    SeedPlanarPoint,
    Surd3,
    fraction_key,
)

MOBIUS_SEED_SCHEMA_ID = "ucns.mobius-seed-of-life-candidate"
MOBIUS_SEED_SCHEMA_VERSION = "0.1.0"
MOBIUS_SEED_SELECTION_EFFECT = "none"
MOBIUS_SEED_SCOPE = "seven-band-mobius-seed-of-life-candidate-only"
MOBIUS_SEED_RADIUS = Fraction(1)
MOBIUS_SEED_HALF_WIDTH = Fraction(1, 6)
MOBIUS_SEED_PHASE_PERIOD_TURNS = Fraction(2)
MOBIUS_SEED_OUTER_PHASE_STEP_TURNS = Fraction(1, 6)
MOBIUS_SEED_BAND_COUNT = 7
MOBIUS_SEED_PAIR_COUNT = 21
MOBIUS_SEED_ADJACENT_PAIR_COUNT = 12
MOBIUS_SEED_CENTERLINE_OCCURRENCE_COUNT = 39
MOBIUS_SEED_UNIQUE_COORDINATE_COUNT = 13
MOBIUS_SEED_BOUNDARY_OBLIGATION_COUNT = 48

CENTERLINE_STANDING = "exact-planar-seed-scaffold"
BOUNDARY_CROSSING_STANDING = (
    "authority-declared-four-crossing-obligation-not-embedding-verified"
)
RENDERING_STANDING = (
    "deterministic-sampled-rendering-not-smooth-embedding-certification"
)
ZETA_BRIDGE_STATUS = (
    "unresolved-no-spectral-operator-zeta-correspondence-or-critical-line-proof"
)
PHASE_SCHEDULE_STANDING = (
    "candidate-sixfold-increment-on-the-reversed-half-of-the-two-turn-cycle"
)
CHIRALITY_SCHEDULE_STANDING = (
    "candidate-rendering-convention-central-deosil-outer-widdershins"
)
SOURCE_CENTER_HYPOTHESIS = (
    "source-proposed-geometric-null-anchor-and-topological-void"
)
UCNS_CENTER_STANDING = (
    "exact-projected-occurrence-bundle-not-promoted-to-vertex-or-structural-null"
)
MOBIUS_SEED_HMMM = (
    "the deterministic surface mesh is a rendering candidate, not a proof that the seven bands form one transverse smooth embedding",
    "the four single-boundary crossing obligations for each adjacent vesica pair do not yet possess solved exact three-dimensional coordinates or transversality certificates",
    "the central fifteen-occurrence projected bundle is not a gonol vertex and is not promoted to the singular Structural Null",
    "no physical electron, Pauli-exclusion, probability-node, or quantum-field interpretation is established by this construction",
    "no self-adjoint operator, spectrum, determinant, trace formula, zeta-zero correspondence, critical-line argument, or proof-assistant theorem has yet been derived",
    "METAPAT may consume commit-pinned UCNS invariants later but does not own or silently rewrite this geometry",
)


class TwistChirality(IntEnum):
    WIDDERSHINS = -1
    DEOSIL = 1


class SeedBandRole(str, Enum):
    MONAD = "central-monad"
    DYAD = "first-outer-dyad"
    OUTER = "subsequent-outer-band"


class PairRelationship(str, Enum):
    VESICA_ADJACENT = "radius-distance-vesica-braid-adjacent"
    SECONDARY_OVERLAP = "sqrt3-radius-distance-secondary-overlap"
    OPPOSITE_TANGENCY = "two-radius-distance-opposite-tangency"


class CoordinateRole(str, Enum):
    CENTRAL_SUPERPOSITION = "central-fifteen-occurrence-superposition"
    THREE_OCCURRENCE = "three-occurrence-projected-coordinate"
    SINGLE_OCCURRENCE = "single-occurrence-projected-coordinate"


@dataclass(frozen=True, slots=True)
class MobiusSeedBand:
    band_id: str
    ordinal: int
    role: SeedBandRole
    center: HexCoordinate
    lifted_phase_turns: Fraction
    frame: NativeMobiusFrame
    chirality: TwistChirality

    def __post_init__(self) -> None:
        if self.band_id != f"M{self.ordinal}" or not 0 <= self.ordinal < 7:
            raise MobiusSeedError("band identity and ordinal disagree")
        if not Fraction(0) <= self.lifted_phase_turns < Fraction(2):
            raise MobiusSeedError("lifted phase must be normalized to [0, 2)")
        expected = (
            NativeMobiusFrame.POSITIVE
            if self.lifted_phase_turns < 1
            else NativeMobiusFrame.REVERSED
        )
        if self.frame is not expected:
            raise MobiusSeedError("band frame must follow lifted phase parity")

    @property
    def visible_phase_turns(self) -> Fraction:
        return self.lifted_phase_turns % 1

    @property
    def center_point(self) -> SeedPlanarPoint:
        return self.center.planar_point

    def point(
        self,
        u_turns: float,
        transverse: float,
        *,
        radius: float = float(MOBIUS_SEED_RADIUS),
        half_width: float = float(MOBIUS_SEED_HALF_WIDTH),
    ) -> tuple[float, float, float]:
        values = (u_turns, transverse, radius, half_width)
        if any(isinstance(value, bool) or not isfinite(float(value)) for value in values):
            raise MobiusSeedError("surface parameters must be finite real numbers")
        if not -1.0 <= float(transverse) <= 1.0:
            raise MobiusSeedError("transverse must be in [-1, 1]")
        if radius <= 0 or half_width <= 0 or half_width >= radius:
            raise MobiusSeedError("radius and half-width are out of range")
        center_x, center_y = self.center_point.to_float()
        angle = 2.0 * pi * float(u_turns)
        twist = pi * (
            self.chirality.value * float(u_turns)
            + float(self.lifted_phase_turns)
        )
        local = float(half_width) * float(transverse)
        radial = float(radius) + local * cos(twist)
        return (
            center_x + radial * cos(angle),
            center_y + radial * sin(angle),
            local * sin(twist),
        )

    def manifest(self) -> dict[str, object]:
        return {
            "band_id": self.band_id,
            "ordinal": self.ordinal,
            "role": self.role.value,
            "center_hex": self.center.manifest(),
            "center_exact": self.center_point.manifest(),
            "lifted_phase_turns": fraction_key(self.lifted_phase_turns),
            "visible_phase_turns": fraction_key(self.visible_phase_turns),
            "frame": self.frame.value,
            "chirality": self.chirality.name.lower(),
        }


@dataclass(frozen=True, slots=True)
class CenterlineIntersectionOccurrence:
    occurrence_id: str
    pair_id: str
    branch: str
    point: SeedPlanarPoint
    over_band_id: str | None
    under_band_id: str | None
    standing: str = CENTERLINE_STANDING

    def __post_init__(self) -> None:
        if not self.occurrence_id or not self.pair_id or not self.branch:
            raise MobiusSeedError("centerline occurrence identity must be nonempty")
        if (self.over_band_id is None) != (self.under_band_id is None):
            raise MobiusSeedError("candidate crossing order must be complete or absent")
        if self.over_band_id == self.under_band_id and self.over_band_id is not None:
            raise MobiusSeedError("one band cannot occupy both crossing-order roles")

    def manifest(self) -> dict[str, object]:
        return {
            "occurrence_id": self.occurrence_id,
            "branch": self.branch,
            "point": self.point.manifest(),
            "over_band_id": self.over_band_id,
            "under_band_id": self.under_band_id,
            "standing": self.standing,
        }


@dataclass(frozen=True, slots=True)
class BoundaryCrossingObligation:
    obligation_id: str
    pair_id: str
    centerline_occurrence_id: str
    local_slot: int
    left_local_transverse: int
    right_local_transverse: int
    over_band_id: str
    under_band_id: str
    realized_point: None = None
    standing: str = BOUNDARY_CROSSING_STANDING

    def __post_init__(self) -> None:
        if self.local_slot not in (0, 1):
            raise MobiusSeedError("boundary local slot must be zero or one")
        if {self.left_local_transverse, self.right_local_transverse} != {-1, 1}:
            raise MobiusSeedError("boundary obligation must pair opposite branches")
        if self.realized_point is not None:
            raise MobiusSeedError("v0.1 cannot claim a realized boundary point")

    def manifest(self) -> dict[str, object]:
        return {
            "obligation_id": self.obligation_id,
            "centerline_occurrence_id": self.centerline_occurrence_id,
            "local_slot": self.local_slot,
            "left_local_transverse": self.left_local_transverse,
            "right_local_transverse": self.right_local_transverse,
            "over_band_id": self.over_band_id,
            "under_band_id": self.under_band_id,
            "realized_point": None,
            "standing": self.standing,
        }


@dataclass(frozen=True, slots=True)
class MobiusSeedPair:
    pair_id: str
    left_band_id: str
    right_band_id: str
    squared_center_distance: Surd3
    relationship: PairRelationship
    braid_adjacent: bool
    phase_delta_turns: Fraction
    centerline_occurrences: tuple[CenterlineIntersectionOccurrence, ...]
    boundary_obligations: tuple[BoundaryCrossingObligation, ...]
    dyad_pair: bool = False

    def __post_init__(self) -> None:
        if self.pair_id != f"{self.left_band_id}:{self.right_band_id}":
            raise MobiusSeedError("pair identity must retain ordered band identities")
        expected = {
            PairRelationship.VESICA_ADJACENT: (Surd3(1), 2, 4, True),
            PairRelationship.SECONDARY_OVERLAP: (Surd3(3), 2, 0, False),
            PairRelationship.OPPOSITE_TANGENCY: (Surd3(4), 1, 0, False),
        }[self.relationship]
        distance, events, obligations, adjacent = expected
        if (
            self.squared_center_distance != distance
            or len(self.centerline_occurrences) != events
            or len(self.boundary_obligations) != obligations
            or self.braid_adjacent is not adjacent
        ):
            raise MobiusSeedError("pair relationship evidence is inconsistent")
        if self.braid_adjacent and len(
            {(item.over_band_id, item.under_band_id) for item in self.centerline_occurrences}
        ) != 2:
            raise MobiusSeedError("adjacent pair order must alternate")

    def manifest(self) -> dict[str, object]:
        return {
            "pair_id": self.pair_id,
            "left_band_id": self.left_band_id,
            "right_band_id": self.right_band_id,
            "squared_center_distance": self.squared_center_distance.manifest(),
            "relationship": self.relationship.value,
            "braid_adjacent": self.braid_adjacent,
            "dyad_pair": self.dyad_pair,
            "phase_delta_turns": fraction_key(self.phase_delta_turns),
            "centerline_occurrences": [item.manifest() for item in self.centerline_occurrences],
            "boundary_obligations": [item.manifest() for item in self.boundary_obligations],
        }


@dataclass(frozen=True, slots=True)
class SuperpositionCoordinate:
    coordinate_id: str
    point: SeedPlanarPoint
    occurrence_ids: tuple[str, ...]
    role: CoordinateRole
    is_vertex: bool = False
    is_structural_null: bool = False

    def __post_init__(self) -> None:
        if len(set(self.occurrence_ids)) != len(self.occurrence_ids):
            raise MobiusSeedError("coordinate occurrences must remain unique")
        expected = {
            CoordinateRole.CENTRAL_SUPERPOSITION: 15,
            CoordinateRole.THREE_OCCURRENCE: 3,
            CoordinateRole.SINGLE_OCCURRENCE: 1,
        }[self.role]
        if len(self.occurrence_ids) != expected:
            raise MobiusSeedError("coordinate role and multiplicity disagree")
        if self.role is CoordinateRole.CENTRAL_SUPERPOSITION and self.point != ORIGIN_POINT:
            raise MobiusSeedError("central superposition must remain at the origin")
        if self.is_vertex or self.is_structural_null:
            raise MobiusSeedError("projected coordinates cannot be silently promoted")

    @property
    def multiplicity(self) -> int:
        return len(self.occurrence_ids)

    def manifest(self) -> dict[str, object]:
        return {
            "coordinate_id": self.coordinate_id,
            "point": self.point.manifest(),
            "occurrence_ids": list(self.occurrence_ids),
            "multiplicity": self.multiplicity,
            "role": self.role.value,
            "is_vertex": False,
            "is_structural_null": False,
        }
