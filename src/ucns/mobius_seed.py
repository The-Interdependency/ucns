# === MODULE_BUILD ===
# id: ucns_mobius_seed_public_surface
#   module_name: mobius_seed
#   module_kind: schema
#   summary: exposes the exact seven-band Möbius Seed of Life builder, receipt types, and deterministic renderer without transferring theorem authority
#   owner: Erin Spencer
#   public_surface: names listed in __all__
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_mobius_seed_public_surface.py
#   rollout: importable UCNS primitive-seven candidate surface
#   rollback: remove this facade while retaining its source modules for review
#   requires: ucns_mobius_seed_exact_geometry, ucns_mobius_seed_model, ucns_mobius_seed_receipt, ucns_mobius_seed_builder, ucns_mobius_seed_renderer
#   since: 2026-08-10
#   unresolved: no complete UCNS object or METAPAT theorem is exported
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: mobius_seed_public_surface_exports_only_bounded_candidate_components
#   given: a consumer imports ucns.mobius_seed
#   then: exact geometry, typed receipts, the builder, and declared-loss renderer are available without a proof, physical-validation, or canonical-completion claim
#   class: safety
#   since: 2026-08-10
# === END CONTRACTS ===

"""Public surface for the UCNS Möbius Seed of Life candidate."""

from .mobius_seed_build import build_mobius_seed_of_life_candidate
from .mobius_seed_exact import HexCoordinate, MobiusSeedError, SeedPlanarPoint, Surd3
from .mobius_seed_model import (
    BOUNDARY_CROSSING_STANDING,
    MOBIUS_SEED_HMMM,
    ZETA_BRIDGE_STATUS,
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
from .mobius_seed_render import render_mobius_seed_obj

__all__ = [
    "BOUNDARY_CROSSING_STANDING",
    "MOBIUS_SEED_HMMM",
    "ZETA_BRIDGE_STATUS",
    "MobiusSeedError",
    "Surd3",
    "SeedPlanarPoint",
    "HexCoordinate",
    "TwistChirality",
    "SeedBandRole",
    "PairRelationship",
    "CoordinateRole",
    "MobiusSeedBand",
    "CenterlineIntersectionOccurrence",
    "BoundaryCrossingObligation",
    "MobiusSeedPair",
    "SuperpositionCoordinate",
    "MobiusSeedOfLifeCandidate",
    "build_mobius_seed_of_life_candidate",
    "render_mobius_seed_obj",
]
