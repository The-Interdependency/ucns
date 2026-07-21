# === MODULE_BUILD ===
# id: carrier_floor_public_surface
#   module_name: ucns public surface
#   module_kind: schema
#   summary: exports only the ratified carrier-floor primitives
#   owner: Erin Spencer
#   public_surface: carrier-floor names listed in __all__
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_public_surface.py
#   rollout: importable prototype only
#   rollback: remove exports
#   requires: directed_carrier_floor
#   since: 2026-07-21
#   unresolved: full UCNS object public surface
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: public_surface_exposes_only_carrier_floor
#   given: a consumer imports ucns
#   then: only the ratified carrier-floor API is exported and no factorization or theorem surface is implied
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

"""UCNS definition-first carrier floor.

No full ``UCNSObject`` or theorem-bearing arithmetic is exported yet.
"""

from .carrier import (
    LIFTED_PERIOD,
    STRUCTURAL_NULL,
    VISIBLE_PERIOD,
    CarrierPoint,
    LiftedCarrierPoint,
    VisibleCarrierPoint,
    VisiblePoint,
    carrier_from_breadth,
    deck_translate,
    lifted_preimages,
    project,
    radius_from_breadth,
    same_lifted_position,
    same_visible_position,
)

__all__ = [
    "LIFTED_PERIOD",
    "STRUCTURAL_NULL",
    "VISIBLE_PERIOD",
    "CarrierPoint",
    "LiftedCarrierPoint",
    "VisibleCarrierPoint",
    "VisiblePoint",
    "carrier_from_breadth",
    "deck_translate",
    "lifted_preimages",
    "project",
    "radius_from_breadth",
    "same_lifted_position",
    "same_visible_position",
]
