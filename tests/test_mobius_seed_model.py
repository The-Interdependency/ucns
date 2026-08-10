# === CHECKS ===
# id: check_mobius_seed_band_two_turn_law
#   proves: mobius_seed_band_retains_one_turn_reversal_and_two_turn_return
#   call: self::test_band_phase_schedule_and_two_turn_return
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_mobius_seed_model_occurrence_preservation
#   proves: mobius_seed_model_preserves_pair_and_coordinate_occurrences
#   call: self::test_model_retains_nonvertex_occurrences
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from fractions import Fraction
from math import isclose
from ucns.direct_mobius import NativeMobiusFrame
from ucns.mobius_seed_exact import HexCoordinate, ORIGIN_POINT
from ucns.mobius_seed_model import CoordinateRole, MobiusSeedBand, SeedBandRole, SuperpositionCoordinate, TwistChirality


def _close(left, right):
    return all(isclose(a, b, rel_tol=0.0, abs_tol=1e-12) for a, b in zip(left, right))


def test_band_phase_schedule_and_two_turn_return() -> None:
    band = MobiusSeedBand("M0", 0, SeedBandRole.MONAD, HexCoordinate(0, 0), Fraction(0), NativeMobiusFrame.POSITIVE, TwistChirality.DEOSIL)
    for u in (0.0, 0.125, 0.37):
        for v in (-1.0, -0.25, 0.5, 1.0):
            assert _close(band.point(u + 1, v), band.point(u, -v))
            assert _close(band.point(u + 2, v), band.point(u, v))


def test_model_retains_nonvertex_occurrences() -> None:
    coordinate = SuperpositionCoordinate("seed-coordinate:center", ORIGIN_POINT, tuple(f"o{i}" for i in range(15)), CoordinateRole.CENTRAL_SUPERPOSITION)
    assert coordinate.multiplicity == 15
    assert coordinate.is_vertex is False
    assert coordinate.is_structural_null is False
