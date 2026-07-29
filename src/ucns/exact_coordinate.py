# === MODULE_BUILD ===
# id: edcm_exact_coordinate_representation_boundary
#   module_name: exact_coordinate
#   module_kind: experiment
#   summary: preserves the signed-local carrier-coordinate candidate as exact rational evidence and exhibits explicit binary64 rendering collisions
#   owner: Erin Spencer
#   public_surface: ExactCoordinateProvenance, ExactCarrierCoordinate, Binary64CarrierRendering, Binary64CollisionKind, Binary64CollisionWitness, ExactCoordinateBoundaryReport, signed_local_exact_coordinate, recover_signed_local_transverse, render_exact_coordinate_binary64, binary64_collision_witnesses, run_v011_exact_coordinate_boundary_experiment
#   internal_surface: exact Fraction validation, exact coordinate identities, binary64 rendering identities, and fixed witness construction
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact local transverse value, lifted turn, upstream candidate identity, law identity, and rendering loss remain linked
#   admin_only: false
#   tests: tests/test_exact_coordinate.py
#   rollout: explicit UCNS-only v0.11 representation-boundary experiment; no carrier selection, canonical faithful breadth, arbitrary-element assignment, real-continuity theorem, EDCM activation, or METAPAT activation
#   rollback: remove this module, its exports, tests, and v0.11 document while retaining the complete v0.10 candidate-family evidence
#   requires: edcm_carrier_coordinate_admissibility_experiment, directed_carrier_floor
#   since: 2026-07-29
#   unresolved: real-continuous full-carrier map, arbitrary-element assignment, canonical faithful breadth, global Mobius-to-cover equivalence, higher geometry, and scoped completion
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: exact_coordinate_signed_local_law_round_trips
#   given: any exact rational local transverse value in the declared interval is mapped by the signed-local affine law
#   then: breadth remains an exact positive Fraction and the exact inverse recovers the original transverse value without enumeration or binary64 conversion
#   class: correctness
#   since: 2026-07-29
#
# id: exact_coordinate_provenance_is_fixed_and_retained
#   given: an exact coordinate record is constructed
#   then: the v0.10 source candidate, v0.11 law identity, code reference, scope, and nonselection effect remain attached and fail closed on substitution
#   class: evidence
#   since: 2026-07-29
#
# id: exact_coordinate_binary64_is_declared_rendering
#   given: an exact coordinate is materialized as a LiftedCarrierPoint
#   then: the actual binary64 fields, exact source record, rendering policy, and known information losses remain linked while the float point is classified only as a rendering
#   class: safety
#   since: 2026-07-29
#
# id: exact_coordinate_binary64_breadth_collision_is_retained
#   given: exact transverse values zero and two to the minus fifty-third are rendered at the same lifted turn
#   then: their exact breadths remain distinct while their actual binary64 LiftedCarrierPoint identities collide
#   class: evidence
#   since: 2026-07-29
#
# id: exact_coordinate_binary64_turn_collision_is_retained
#   given: exact lifted turns one and one plus two to the minus fifty-four are rendered at the same transverse value
#   then: their exact lifted turns remain distinct while their actual binary64 LiftedCarrierPoint identities collide
#   class: evidence
#   since: 2026-07-29
#
# id: exact_coordinate_boundary_does_not_select_or_activate
#   given: the v0.11 boundary report is constructed
#   then: exact rational injectivity and binary64 noninjectivity are reported together while carrier selection, faithful-breadth canon, arbitrary-element assignment, real-continuity theorem, EDCM activation, and METAPAT activation remain absent
#   class: doctrine
#   since: 2026-07-29
# === END CONTRACTS ===

"""Exact-coordinate and binary64-rendering boundary for UCNS v0.11.

v0.10 found the signed-local affine radial candidate admissible on a finite
45-fiber materialization domain.  This module separates two claims that finite
binary64 evidence could not settle:

* over exact rationals ``B(u) = 1 + u/2`` has exact inverse
  ``u = 2(B - 1)``; and
* a ``LiftedCarrierPoint`` cannot preserve that injectivity over every exact
  rational because its stored fields are binary64 renderings.

The exact record is the evidence identity.  A float point is retained only as a
linked, explicitly lossy rendering.  This experiment does not select the
candidate or establish the unresolved full-carrier real-continuity claim.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction

from .carrier import VISIBLE_PERIOD, LiftedCarrierPoint
from .carrier_coordinate import (
    CARRIER_COORDINATE_CANDIDATE_VERSION,
    V010_CARRIER_COORDINATE_SCHEMA_ID,
    V010_CARRIER_COORDINATE_SCHEMA_VERSION,
)


V011_EXACT_COORDINATE_SCHEMA_ID = "ucns.edcm.exact-coordinate-boundary"
V011_EXACT_COORDINATE_SCHEMA_VERSION = "0.11.0"
V011_SELECTION_EFFECT = "none"

EXACT_COORDINATE_SCOPE = (
    "signed-local-exact-rational-and-binary64-rendering-boundary"
)
EXACT_COORDINATE_CANDIDATE_ID = "signed-local-affine-radial"
EXACT_COORDINATE_LAW_ID = "signed-local-affine-radial-exact"
EXACT_COORDINATE_LAW_VERSION = "0.11.0"
EXACT_COORDINATE_FORMULA = "B(u)=1+u/2; u=2*(B-1)"
EXACT_COORDINATE_CODE_REFERENCE = (
    "ucns.exact_coordinate:signed_local_exact_coordinate"
)
EXACT_COORDINATE_RENDERING_POLICY_ID = (
    "ucns.rendering.exact-coordinate-to-binary64"
)
EXACT_COORDINATE_RENDERING_POLICY_VERSION = "0.11.0"
EXACT_COORDINATE_RENDERING_CODE_REFERENCE = (
    "ucns.exact_coordinate:render_exact_coordinate_binary64"
)
EXACT_COORDINATE_STATUS = "exact-rational-candidate-coordinate"
BINARY64_RENDERING_STATUS = "lossy-nonauthoritative-rendering"
EXACT_COORDINATE_LAW_STATUS = (
    "exact-rational-bijection-on-declared-transverse-interval"
)
BINARY64_COORDINATE_STATUS = (
    "not-injective-on-arbitrary-exact-rational-domain"
)

_ROOT_BREADTH = Fraction(1)
_RADIAL_SCALE = Fraction(1, 2)
_TRANSVERSE_MIN = Fraction(-1)
_TRANSVERSE_MAX = Fraction(1)
_LIFTED_TURN_PERIOD = Fraction(2)

_BINARY64_INFORMATION_LOSS = (
    "exact rational breadth is rounded to one binary64 value",
    "exact rational lifted turns are rounded before multiplication by binary64 2*pi",
)


class ExactCoordinateError(ValueError):
    """Raised when exact-coordinate evidence crosses its declared boundary."""


class Binary64CollisionKind(str, Enum):
    """Exact distinction lost by one retained binary64 collision witness."""

    BREADTH = "breadth-rounding"
    LIFTED_TURN = "lifted-turn-rounding"


def _require_fraction(value: Fraction, field_name: str) -> None:
    if not isinstance(value, Fraction):
        raise ExactCoordinateError(f"{field_name} must be an exact Fraction")


def _fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _normalize_lifted_turns(value: Fraction) -> Fraction:
    _require_fraction(value, "lifted_turns")
    whole_periods = value // _LIFTED_TURN_PERIOD
    return value - _LIFTED_TURN_PERIOD * whole_periods


def _rendering_key(
    point: LiftedCarrierPoint,
) -> tuple[tuple[str, str], ...]:
    if not isinstance(point, LiftedCarrierPoint):
        raise TypeError("point must be LiftedCarrierPoint")
    return (
        ("breadth-binary64", point.breadth.hex()),
        ("angle-binary64", point.angle.hex()),
    )


@dataclass(frozen=True, slots=True)
class ExactCoordinateProvenance:
    """Fixed upstream candidate and exact-law identity for one coordinate."""

    source_schema_id: str = V010_CARRIER_COORDINATE_SCHEMA_ID
    source_schema_version: str = V010_CARRIER_COORDINATE_SCHEMA_VERSION
    source_candidate_id: str = EXACT_COORDINATE_CANDIDATE_ID
    source_candidate_version: str = CARRIER_COORDINATE_CANDIDATE_VERSION
    law_id: str = EXACT_COORDINATE_LAW_ID
    law_version: str = EXACT_COORDINATE_LAW_VERSION
    formula: str = EXACT_COORDINATE_FORMULA
    code_reference: str = EXACT_COORDINATE_CODE_REFERENCE
    scope: str = EXACT_COORDINATE_SCOPE
    selection_effect: str = V011_SELECTION_EFFECT

    def __post_init__(self) -> None:
        expected = (
            V010_CARRIER_COORDINATE_SCHEMA_ID,
            V010_CARRIER_COORDINATE_SCHEMA_VERSION,
            EXACT_COORDINATE_CANDIDATE_ID,
            CARRIER_COORDINATE_CANDIDATE_VERSION,
            EXACT_COORDINATE_LAW_ID,
            EXACT_COORDINATE_LAW_VERSION,
            EXACT_COORDINATE_FORMULA,
            EXACT_COORDINATE_CODE_REFERENCE,
            EXACT_COORDINATE_SCOPE,
            V011_SELECTION_EFFECT,
        )
        actual = (
            self.source_schema_id,
            self.source_schema_version,
            self.source_candidate_id,
            self.source_candidate_version,
            self.law_id,
            self.law_version,
            self.formula,
            self.code_reference,
            self.scope,
            self.selection_effect,
        )
        if actual != expected:
            raise ExactCoordinateError(
                "exact-coordinate provenance identity is fixed"
            )


@dataclass(frozen=True, slots=True)
class ExactCarrierCoordinate:
    """Exact rational evidence for one nonselected signed-local coordinate."""

    local_transverse: Fraction
    breadth: Fraction
    lifted_turns: Fraction
    provenance: ExactCoordinateProvenance = field(
        default_factory=ExactCoordinateProvenance
    )
    status: str = EXACT_COORDINATE_STATUS
    selection_effect: str = V011_SELECTION_EFFECT

    def __post_init__(self) -> None:
        _require_fraction(self.local_transverse, "local_transverse")
        _require_fraction(self.breadth, "breadth")
        _require_fraction(self.lifted_turns, "lifted_turns")
        if not _TRANSVERSE_MIN <= self.local_transverse <= _TRANSVERSE_MAX:
            raise ExactCoordinateError(
                "local_transverse must remain in the declared interval [-1, 1]"
            )
        expected_breadth = (
            _ROOT_BREADTH + _RADIAL_SCALE * self.local_transverse
        )
        if self.breadth != expected_breadth:
            raise ExactCoordinateError(
                "breadth must equal the exact signed-local affine law"
            )
        if self.breadth <= 0:
            raise ExactCoordinateError("exact coordinate breadth must be positive")
        if not Fraction(0) <= self.lifted_turns < _LIFTED_TURN_PERIOD:
            raise ExactCoordinateError(
                "lifted_turns must be normalized to the exact interval [0, 2)"
            )
        if not isinstance(self.provenance, ExactCoordinateProvenance):
            raise ExactCoordinateError(
                "exact coordinate requires fixed provenance"
            )
        if self.status != EXACT_COORDINATE_STATUS:
            raise ExactCoordinateError("exact coordinate status is fixed")
        if self.selection_effect != V011_SELECTION_EFFECT:
            raise ExactCoordinateError("exact coordinate cannot select a carrier")

    @property
    def exact_identity(self) -> tuple[tuple[str, str], ...]:
        return (
            ("candidate", self.provenance.source_candidate_id),
            ("local-transverse", _fraction_key(self.local_transverse)),
            ("breadth", _fraction_key(self.breadth)),
            ("lifted-turns", _fraction_key(self.lifted_turns)),
        )


def signed_local_exact_coordinate(
    local_transverse: Fraction,
    lifted_turns: Fraction,
) -> ExactCarrierCoordinate:
    """Map exact ``u`` to exact ``(B, t)`` under the v0.11 candidate law."""

    _require_fraction(local_transverse, "local_transverse")
    _require_fraction(lifted_turns, "lifted_turns")
    return ExactCarrierCoordinate(
        local_transverse=local_transverse,
        breadth=_ROOT_BREADTH + _RADIAL_SCALE * local_transverse,
        lifted_turns=_normalize_lifted_turns(lifted_turns),
    )


def recover_signed_local_transverse(
    coordinate: ExactCarrierCoordinate,
) -> Fraction:
    """Recover exact ``u = 2(B - 1)`` from one validated coordinate."""

    if not isinstance(coordinate, ExactCarrierCoordinate):
        raise TypeError("coordinate must be ExactCarrierCoordinate")
    recovered = 2 * (coordinate.breadth - _ROOT_BREADTH)
    if recovered != coordinate.local_transverse:
        raise ExactCoordinateError("exact coordinate inverse identity mismatch")
    return recovered


@dataclass(frozen=True, slots=True)
class Binary64CarrierRendering:
    """One lossy actual ``LiftedCarrierPoint`` linked to exact source evidence."""

    exact_coordinate: ExactCarrierCoordinate
    actual_point: LiftedCarrierPoint
    rendering_policy_id: str = EXACT_COORDINATE_RENDERING_POLICY_ID
    rendering_policy_version: str = (
        EXACT_COORDINATE_RENDERING_POLICY_VERSION
    )
    code_reference: str = EXACT_COORDINATE_RENDERING_CODE_REFERENCE
    information_loss: tuple[str, ...] = _BINARY64_INFORMATION_LOSS
    status: str = BINARY64_RENDERING_STATUS
    selection_effect: str = V011_SELECTION_EFFECT

    def __post_init__(self) -> None:
        if not isinstance(self.exact_coordinate, ExactCarrierCoordinate):
            raise ExactCoordinateError(
                "binary64 rendering requires exact coordinate source evidence"
            )
        if not isinstance(self.actual_point, LiftedCarrierPoint):
            raise ExactCoordinateError(
                "binary64 rendering requires an actual LiftedCarrierPoint"
            )
        expected = LiftedCarrierPoint(
            float(self.exact_coordinate.breadth),
            float(self.exact_coordinate.lifted_turns) * VISIBLE_PERIOD,
        )
        if _rendering_key(self.actual_point) != _rendering_key(expected):
            raise ExactCoordinateError(
                "binary64 rendering does not match the exact source coordinate"
            )
        if (
            self.rendering_policy_id
            != EXACT_COORDINATE_RENDERING_POLICY_ID
            or self.rendering_policy_version
            != EXACT_COORDINATE_RENDERING_POLICY_VERSION
            or self.code_reference
            != EXACT_COORDINATE_RENDERING_CODE_REFERENCE
        ):
            raise ExactCoordinateError("binary64 rendering identity is fixed")
        if self.information_loss != _BINARY64_INFORMATION_LOSS:
            raise ExactCoordinateError(
                "binary64 rendering must retain its declared information loss"
            )
        if self.status != BINARY64_RENDERING_STATUS:
            raise ExactCoordinateError(
                "binary64 point must remain classified as a rendering"
            )
        if self.selection_effect != V011_SELECTION_EFFECT:
            raise ExactCoordinateError(
                "binary64 rendering cannot select a carrier"
            )

    @property
    def rendering_identity(self) -> tuple[tuple[str, str], ...]:
        return _rendering_key(self.actual_point)


def render_exact_coordinate_binary64(
    coordinate: ExactCarrierCoordinate,
) -> Binary64CarrierRendering:
    """Render exact candidate evidence into the current binary64 point type."""

    if not isinstance(coordinate, ExactCarrierCoordinate):
        raise TypeError("coordinate must be ExactCarrierCoordinate")
    return Binary64CarrierRendering(
        exact_coordinate=coordinate,
        actual_point=LiftedCarrierPoint(
            float(coordinate.breadth),
            float(coordinate.lifted_turns) * VISIBLE_PERIOD,
        ),
    )


@dataclass(frozen=True, slots=True)
class Binary64CollisionWitness:
    """Two distinct exact coordinates sharing one actual binary64 identity."""

    witness_id: str
    kind: Binary64CollisionKind
    first: Binary64CarrierRendering
    second: Binary64CarrierRendering
    exact_difference: str
    conclusion: str = (
        "binary64-rendering-not-injective-on-arbitrary-exact-rational-domain"
    )

    def __post_init__(self) -> None:
        if not isinstance(self.witness_id, str) or not self.witness_id.strip():
            raise ExactCoordinateError("collision witness_id must be nonempty")
        if not isinstance(self.kind, Binary64CollisionKind):
            raise ExactCoordinateError(
                "collision witness kind must be Binary64CollisionKind"
            )
        if self.first.exact_coordinate.exact_identity == (
            self.second.exact_coordinate.exact_identity
        ):
            raise ExactCoordinateError(
                "collision witness requires distinct exact coordinates"
            )
        if self.first.rendering_identity != self.second.rendering_identity:
            raise ExactCoordinateError(
                "collision witness requires one shared binary64 identity"
            )
        if not isinstance(self.exact_difference, str) or not (
            self.exact_difference.strip()
        ):
            raise ExactCoordinateError(
                "collision witness must describe the exact lost distinction"
            )
        if self.conclusion != (
            "binary64-rendering-not-injective-on-arbitrary-exact-rational-domain"
        ):
            raise ExactCoordinateError(
                "collision witness conclusion is fixed"
            )
        if self.kind is Binary64CollisionKind.BREADTH:
            if (
                self.first.exact_coordinate.breadth
                == self.second.exact_coordinate.breadth
            ):
                raise ExactCoordinateError(
                    "breadth collision must retain distinct exact breadths"
                )
            if (
                self.first.exact_coordinate.lifted_turns
                != self.second.exact_coordinate.lifted_turns
            ):
                raise ExactCoordinateError(
                    "breadth collision must hold lifted turns fixed"
                )
        if self.kind is Binary64CollisionKind.LIFTED_TURN:
            if (
                self.first.exact_coordinate.lifted_turns
                == self.second.exact_coordinate.lifted_turns
            ):
                raise ExactCoordinateError(
                    "turn collision must retain distinct exact lifted turns"
                )
            if (
                self.first.exact_coordinate.breadth
                != self.second.exact_coordinate.breadth
            ):
                raise ExactCoordinateError(
                    "turn collision must hold exact breadth fixed"
                )

    @property
    def evidence_identity(self) -> tuple[object, ...]:
        return (
            self.witness_id,
            self.kind,
            self.first.exact_coordinate.exact_identity,
            self.second.exact_coordinate.exact_identity,
            self.first.rendering_identity,
            self.second.rendering_identity,
            self.exact_difference,
            self.conclusion,
        )


def binary64_collision_witnesses() -> tuple[Binary64CollisionWitness, ...]:
    """Return fixed breadth and lifted-turn collision witnesses."""

    breadth_first = render_exact_coordinate_binary64(
        signed_local_exact_coordinate(Fraction(0), Fraction(0))
    )
    breadth_second = render_exact_coordinate_binary64(
        signed_local_exact_coordinate(
            Fraction(1, 2**53),
            Fraction(0),
        )
    )
    turn_first = render_exact_coordinate_binary64(
        signed_local_exact_coordinate(Fraction(0), Fraction(1))
    )
    turn_second = render_exact_coordinate_binary64(
        signed_local_exact_coordinate(
            Fraction(0),
            Fraction(1) + Fraction(1, 2**54),
        )
    )
    return (
        Binary64CollisionWitness(
            witness_id="binary64-breadth-rounding-at-root",
            kind=Binary64CollisionKind.BREADTH,
            first=breadth_first,
            second=breadth_second,
            exact_difference=(
                "u differs by 1/2^53 and exact breadth differs by 1/2^54"
            ),
        ),
        Binary64CollisionWitness(
            witness_id="binary64-lifted-turn-rounding-at-one",
            kind=Binary64CollisionKind.LIFTED_TURN,
            first=turn_first,
            second=turn_second,
            exact_difference="exact lifted turns differ by 1/2^54",
        ),
    )


@dataclass(frozen=True, slots=True)
class ExactCoordinateBoundaryReport:
    """Complete v0.11 exact-versus-binary64 representation boundary."""

    collision_witnesses: tuple[Binary64CollisionWitness, ...]
    provenance: ExactCoordinateProvenance = field(
        default_factory=ExactCoordinateProvenance
    )
    schema_id: str = V011_EXACT_COORDINATE_SCHEMA_ID
    schema_version: str = V011_EXACT_COORDINATE_SCHEMA_VERSION
    exact_law_status: str = EXACT_COORDINATE_LAW_STATUS
    binary64_status: str = BINARY64_COORDINATE_STATUS
    rendering_role: str = BINARY64_RENDERING_STATUS
    selection_effect: str = V011_SELECTION_EFFECT
    edcm_activation: str = "inactive"
    metapat_activation: str = "inactive"
    hmmm: tuple[str, ...] = (
        "real continuity of the complete Mobius-to-cover relationship remains unresolved",
        "arbitrary observed-element assignment remains unresolved",
        "canonical faithful breadth remains unresolved",
        "circle, epicycle, disk, sphere, recursive composition, and completion remain unresolved",
    )

    def __post_init__(self) -> None:
        if (
            self.schema_id != V011_EXACT_COORDINATE_SCHEMA_ID
            or self.schema_version != V011_EXACT_COORDINATE_SCHEMA_VERSION
        ):
            raise ExactCoordinateError("v0.11 schema identity mismatch")
        if not isinstance(self.provenance, ExactCoordinateProvenance):
            raise ExactCoordinateError(
                "v0.11 report requires fixed exact-coordinate provenance"
            )
        if tuple(item.kind for item in self.collision_witnesses) != (
            Binary64CollisionKind.BREADTH,
            Binary64CollisionKind.LIFTED_TURN,
        ):
            raise ExactCoordinateError(
                "v0.11 report must retain both fixed collision witnesses in order"
            )
        expected_witnesses = tuple(
            item.evidence_identity for item in binary64_collision_witnesses()
        )
        if tuple(
            item.evidence_identity for item in self.collision_witnesses
        ) != expected_witnesses:
            raise ExactCoordinateError(
                "v0.11 report collision witness identities are fixed"
            )
        if self.selection_effect != V011_SELECTION_EFFECT:
            raise ExactCoordinateError("v0.11 cannot select a carrier")
        if self.exact_law_status != EXACT_COORDINATE_LAW_STATUS:
            raise ExactCoordinateError("v0.11 exact-law status is fixed")
        if self.binary64_status != BINARY64_COORDINATE_STATUS:
            raise ExactCoordinateError("v0.11 binary64 status is fixed")
        if self.rendering_role != BINARY64_RENDERING_STATUS:
            raise ExactCoordinateError(
                "v0.11 binary64 points must remain renderings"
            )
        if self.edcm_activation != "inactive":
            raise ExactCoordinateError("v0.11 cannot activate EDCM")
        if self.metapat_activation != "inactive":
            raise ExactCoordinateError("v0.11 cannot activate METAPAT")
        if not self.hmmm or any(not item.strip() for item in self.hmmm):
            raise ExactCoordinateError(
                "v0.11 unresolved boundary must remain explicit"
            )


def run_v011_exact_coordinate_boundary_experiment(
) -> ExactCoordinateBoundaryReport:
    """Run the complete fixed v0.11 representation-boundary experiment."""

    return ExactCoordinateBoundaryReport(
        collision_witnesses=binary64_collision_witnesses()
    )


__all__ = [
    "BINARY64_RENDERING_STATUS",
    "BINARY64_COORDINATE_STATUS",
    "EXACT_COORDINATE_CANDIDATE_ID",
    "EXACT_COORDINATE_CODE_REFERENCE",
    "EXACT_COORDINATE_FORMULA",
    "EXACT_COORDINATE_LAW_ID",
    "EXACT_COORDINATE_LAW_STATUS",
    "EXACT_COORDINATE_LAW_VERSION",
    "EXACT_COORDINATE_RENDERING_CODE_REFERENCE",
    "EXACT_COORDINATE_RENDERING_POLICY_ID",
    "EXACT_COORDINATE_RENDERING_POLICY_VERSION",
    "EXACT_COORDINATE_SCOPE",
    "EXACT_COORDINATE_STATUS",
    "V011_EXACT_COORDINATE_SCHEMA_ID",
    "V011_EXACT_COORDINATE_SCHEMA_VERSION",
    "V011_SELECTION_EFFECT",
    "Binary64CarrierRendering",
    "Binary64CollisionKind",
    "Binary64CollisionWitness",
    "ExactCarrierCoordinate",
    "ExactCoordinateBoundaryReport",
    "ExactCoordinateError",
    "ExactCoordinateProvenance",
    "binary64_collision_witnesses",
    "recover_signed_local_transverse",
    "render_exact_coordinate_binary64",
    "run_v011_exact_coordinate_boundary_experiment",
    "signed_local_exact_coordinate",
]
