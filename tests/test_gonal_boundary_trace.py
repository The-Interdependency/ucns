# === CHECKS ===
# id: check_gonal_boundary_trace_samples_circle_wave_mode_exactly
#   proves: gonal_boundary_trace_samples_circle_wave_mode_exactly
#   call: self::test_circle_wave_mode_trace_is_exact
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_gonal_boundary_trace_matches_modular_covering_pullback
#   proves: gonal_boundary_trace_matches_modular_covering_pullback
#   call: self::test_modular_action_is_exact_wave_covering_trace
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_gonal_boundary_trace_fails_closed_on_incompatible_geometry
#   proves: gonal_boundary_trace_fails_closed_on_incompatible_geometry
#   call: self::test_trace_bridge_fails_closed
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_gonal_boundary_trace_does_not_select_downstream_physics
#   proves: gonal_boundary_trace_does_not_select_downstream_physics
#   call: self::test_trace_surface_is_geometry_only
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from fractions import Fraction

import pytest

from ucns.gonal_boundary_trace import (
    GonalBoundaryTraceError,
    build_circle_wave_mode_trace,
    pullback_circle_wave_trace,
)
from ucns.modular_orbit import build_modular_orbit_geometry


def test_circle_wave_mode_trace_is_exact() -> None:
    trace = build_circle_wave_mode_trace(9, 2, range(1, 9))

    assert trace.positions == tuple(range(1, 9))
    assert trace.samples[0].boundary_turn == Fraction(1, 9)
    assert trace.phase_at(1) == Fraction(2, 9)
    assert trace.phase_at(5) == Fraction(1, 9)
    assert trace.phase_at(8) == Fraction(7, 9)


def test_modular_action_is_exact_wave_covering_trace() -> None:
    geometry = build_modular_orbit_geometry(9, 2, range(1, 9))
    source = build_circle_wave_mode_trace(9, 1, range(1, 9))
    covering = pullback_circle_wave_trace(source, geometry)

    assert covering.covering_degree == 2
    assert covering.time_scale == 2
    assert covering.target.harmonic == 2
    assert covering.action == geometry.action
    for source_residue, target_residue in geometry.action:
        assert source.phase_at(target_residue) == covering.target.phase_at(source_residue)


def test_trace_bridge_fails_closed() -> None:
    source = build_circle_wave_mode_trace(9, 1, range(1, 9))
    wrong_modulus = build_modular_orbit_geometry(7, 2, range(1, 7))
    with pytest.raises(GonalBoundaryTraceError, match="moduli must match"):
        pullback_circle_wave_trace(source, wrong_modulus)

    wrong_carrier = build_modular_orbit_geometry(9, 2, (1, 2, 4, 5, 7, 8))
    with pytest.raises(GonalBoundaryTraceError, match="carriers must match"):
        pullback_circle_wave_trace(source, wrong_carrier)

    zero_cover = build_modular_orbit_geometry(9, 0, (0,))
    zero_trace = build_circle_wave_mode_trace(9, 1, (0,))
    with pytest.raises(GonalBoundaryTraceError, match="positive-degree"):
        pullback_circle_wave_trace(zero_trace, zero_cover)


def test_trace_surface_is_geometry_only() -> None:
    geometry = build_modular_orbit_geometry(9, 7, range(1, 9))
    source = build_circle_wave_mode_trace(9, 2, range(1, 9))
    payload = pullback_circle_wave_trace(source, geometry).as_dict()
    text = repr(payload).lower()

    assert payload["covering_degree"] == 7
    assert payload["time_scale"] == 7
    assert payload["target"]["harmonic"] == 14
    for forbidden in ("epac", "pcea", "fibonacci", "prime", "particle", "energy"):
        assert forbidden not in text
