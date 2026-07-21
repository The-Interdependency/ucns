# === MODULE_BUILD ===
# id: foundations_public_surface
#   module_name: ucns public surface
#   module_kind: schema
#   summary: exports only the ratified carrier and structural-support foundations
#   owner: Erin Spencer
#   public_surface: carrier and structure names listed in __all__
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_public_surface.py, tests/test_structure.py
#   rollout: importable foundations prototype only
#   rollback: remove structure exports while preserving carrier floor
#   requires: directed_carrier_floor, structural_cell_support_floor
#   since: 2026-07-21
#   unresolved: receipts, metadata, canonical structural equivalence, M, B, complete UCNS object
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: public_surface_exposes_only_ratified_foundations
#   given: a consumer imports ucns
#   then: only the ratified carrier and structural-support foundations are exported; no M, B, factorization, or theorem surface is implied
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

"""UCNS definition-first carrier and structural-support foundations.

No complete ``UCNSObject``, product character, faithful-breadth evaluator,
theorem-bearing arithmetic, or downstream-consumer promise is exported yet.
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
from .structure import (
    Carrier,
    Cell,
    Structure,
    collapse,
    make_carrier,
    pair,
    prune,
    support_weight,
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
    "Carrier",
    "Cell",
    "Structure",
    "collapse",
    "make_carrier",
    "pair",
    "prune",
    "support_weight",
]
