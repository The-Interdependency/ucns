# === MODULE_BUILD ===
# id: ucns_mobius_seed_builder
#   module_name: mobius_seed_build
#   module_kind: experiment
#   summary: constructs all seven bands, twenty-one pair relations, exact Q(sqrt(3)) projected events, coordinate multiplicities, and unresolved four-crossing obligations
#   owner: Erin Spencer
#   public_surface: build_mobius_seed_of_life_candidate
#   internal_surface: phase schedule, exact unit-circle intersections, pair classification, and coordinate grouping
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: no user data; source-fixed and candidate-selected values remain labeled in the receipt
#   admin_only: false
#   tests: tests/test_mobius_seed_build.py
#   rollout: executable nonselecting primitive-seven construction
#   rollback: remove this module and dependent rendering while retaining exact/model/source records
#   requires: ucns_mobius_seed_exact_geometry, ucns_mobius_seed_model, ucns_mobius_seed_receipt
#   since: 2026-08-10
#   unresolved: exact three-dimensional boundary realization and global smooth-embedding compatibility
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: mobius_seed_builder_constructs_complete_seven_band_pair_ledger
#   given: the primitive-seven builder runs
#   then: one monad and six outer bands produce twelve vesicas, six secondary overlaps, three tangencies, thirty-nine occurrence-addressed projected events, and thirteen exact coordinates
#   class: correctness
#   since: 2026-08-10
#
# id: mobius_seed_builder_records_four_crossing_obligations_per_adjacent_pair
#   given: each of the twelve radius-distance pairs is classified as braid-adjacent
#   then: it receives two alternating candidate order events and four unresolved single-boundary crossing obligations without fabricated coordinates
#   class: evidence
#   since: 2026-08-10
# === END CONTRACTS ===

"""Builder for the exact bounded Möbius Seed of Life candidate."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from typing import Iterable

from .direct_mobius import NativeMobiusFrame
from .mobius_seed_exact import (
    HexCoordinate,
    MobiusSeedError,
    ORIGIN_POINT,
    SQRT3_OVER_2,
    SQRT3_OVER_6,
    SeedPlanarPoint,
    Surd3,
)
from .mobius_seed_model import (
    BoundaryCrossingObligation,
    CenterlineIntersectionOccurrence,
    CoordinateRole,
    MobiusSeedBand,
    MobiusSeedPair,
    PairRelationship,
    SeedBandRole,
    SuperpositionCoordinate,
    TwistChirality,
)
from .mobius_seed_receipt import MobiusSeedOfLifeCandidate


def _bands() -> tuple[MobiusSeedBand, ...]:
    centers = (
        HexCoordinate(0, 0), HexCoordinate(1, 0), HexCoordinate(0, 1),
        HexCoordinate(-1, 1), HexCoordinate(-1, 0), HexCoordinate(0, -1),
        HexCoordinate(1, -1),
    )
    phases = (
        Fraction(0), Fraction(1), Fraction(7, 6), Fraction(4, 3),
        Fraction(3, 2), Fraction(5, 3), Fraction(11, 6),
    )
    return tuple(
        MobiusSeedBand(
            band_id=f"M{index}",
            ordinal=index,
            role=(SeedBandRole.MONAD if index == 0 else SeedBandRole.DYAD if index == 1 else SeedBandRole.OUTER),
            center=centers[index],
            lifted_phase_turns=phases[index],
            frame=(NativeMobiusFrame.POSITIVE if phases[index] < 1 else NativeMobiusFrame.REVERSED),
            chirality=(TwistChirality.DEOSIL if index == 0 else TwistChirality.WIDDERSHINS),
        )
        for index in range(7)
    )


def _intersection_points(left: SeedPlanarPoint, right: SeedPlanarPoint):
    delta = right - left
    squared_distance = delta.squared_norm
    midpoint = (left + right) / 2
    if squared_distance == Surd3(4):
        return (("tangent", midpoint),)
    factor = {Surd3(1): SQRT3_OVER_2, Surd3(3): SQRT3_OVER_6}.get(squared_distance)
    if factor is None:
        raise MobiusSeedError("Seed pair distance must be 1, 3, or 4")
    perpendicular = SeedPlanarPoint(-delta.y, delta.x)
    offset = perpendicular.scaled(factor)
    points = (("plus", midpoint + offset), ("minus", midpoint - offset))
    if any((point - left).squared_norm != Surd3(1) or (point - right).squared_norm != Surd3(1) for _, point in points):
        raise MobiusSeedError("derived event is not on both unit circles")
    return points


def _pair(left: MobiusSeedBand, right: MobiusSeedBand) -> MobiusSeedPair:
    pair_id = f"{left.band_id}:{right.band_id}"
    distance = (right.center_point - left.center_point).squared_norm
    relationship = {
        Surd3(1): PairRelationship.VESICA_ADJACENT,
        Surd3(3): PairRelationship.SECONDARY_OVERLAP,
        Surd3(4): PairRelationship.OPPOSITE_TANGENCY,
    }[distance]
    adjacent = relationship is PairRelationship.VESICA_ADJACENT
    occurrences = []
    obligations = []
    for index, (branch, point) in enumerate(_intersection_points(left.center_point, right.center_point)):
        over = left.band_id if adjacent and index == 0 else right.band_id if adjacent else None
        under = right.band_id if adjacent and index == 0 else left.band_id if adjacent else None
        occurrence_id = f"{pair_id}:centerline:{branch}"
        occurrences.append(CenterlineIntersectionOccurrence(
            occurrence_id=occurrence_id,
            pair_id=pair_id,
            branch=branch,
            point=point,
            over_band_id=over,
            under_band_id=under,
        ))
        if adjacent:
            assert over is not None and under is not None
            for slot in (0, 1):
                left_transverse = 1 if slot == 0 else -1
                obligations.append(BoundaryCrossingObligation(
                    obligation_id=f"{occurrence_id}:single-boundary-slot:{slot}",
                    pair_id=pair_id,
                    centerline_occurrence_id=occurrence_id,
                    local_slot=slot,
                    left_local_transverse=left_transverse,
                    right_local_transverse=-left_transverse,
                    over_band_id=(over if slot == 0 else under),
                    under_band_id=(under if slot == 0 else over),
                ))
    return MobiusSeedPair(
        pair_id=pair_id,
        left_band_id=left.band_id,
        right_band_id=right.band_id,
        squared_center_distance=distance,
        relationship=relationship,
        braid_adjacent=adjacent,
        phase_delta_turns=(right.lifted_phase_turns - left.lifted_phase_turns) % 2,
        centerline_occurrences=tuple(occurrences),
        boundary_obligations=tuple(obligations),
        dyad_pair=pair_id == "M0:M1",
    )


def _coordinates(occurrences: Iterable[CenterlineIntersectionOccurrence]):
    grouped: dict[SeedPlanarPoint, list[str]] = {}
    for occurrence in occurrences:
        grouped.setdefault(occurrence.point, []).append(occurrence.occurrence_id)
    output = []
    for index, (point, ids) in enumerate(sorted(grouped.items(), key=lambda item: item[0].to_float())):
        role = (
            CoordinateRole.CENTRAL_SUPERPOSITION if point == ORIGIN_POINT
            else CoordinateRole.THREE_OCCURRENCE if len(ids) == 3
            else CoordinateRole.SINGLE_OCCURRENCE
        )
        prefix = "center" if point == ORIGIN_POINT else "triple" if len(ids) == 3 else "single"
        output.append(SuperpositionCoordinate(
            coordinate_id=f"seed-coordinate:{prefix}" if prefix == "center" else f"seed-coordinate:{prefix}:{index}",
            point=point,
            occurrence_ids=tuple(sorted(ids)),
            role=role,
        ))
    return tuple(output)


def build_mobius_seed_of_life_candidate() -> MobiusSeedOfLifeCandidate:
    bands = _bands()
    pairs = tuple(_pair(bands[i], bands[j]) for i, j in combinations(range(7), 2))
    occurrences = tuple(item for pair in pairs for item in pair.centerline_occurrences)
    return MobiusSeedOfLifeCandidate(bands=bands, pairs=pairs, coordinates=_coordinates(occurrences))
