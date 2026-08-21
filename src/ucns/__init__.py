# === MODULE_BUILD ===
# id: ucns_geometry_public_surface
#   module_name: __init__
#   module_kind: facade
#   summary: geometry-only UCNS public surface
#   owner: Erin Spencer
#   public_surface: carrier geometry, framed Mobius root loop, exact Public Gonol carrier, Mobius vesica and seed geometry
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: geometry module tests
#   rollout: active geometry-only package facade
#   rollback: restore prior facade from Git history
#   requires: directed_carrier_floor, ucns_native_mobius_geometry, ucns_public_gonol_geometry, ucns_mobius_vesica_candidate, ucns_mobius_seed_of_life_candidate
#   since: 2026-08-20
#   unresolved: canonical completion of the full UCNS geometric construction
# === END MODULE_BUILD ===

"""UCNS geometry.

The active package surface is deliberately geometric: carriers, exact motion,
Möbius constructions, geometric certificates, and topological/prime geometry.
Lexical semantics, corpora, morphology, definition recursion, evaluator
frameworks, PTCNA state, and cross-stack adapters are not UCNS package content.
"""

from .carrier import (
    STRUCTURAL_NULL as DIRECTED_STRUCTURAL_NULL,
    LiftedCarrierPoint,
    VisibleCarrierPoint,
    carrier_from_breadth,
    deck_translate,
    lifted_preimages,
    project,
    radius_from_breadth,
    same_lifted_position,
    same_visible_position,
)
from .direct_mobius import (
    DirectMobiusError,
    NativeMobiusFrame,
    NativeMobiusState,
    STRUCTURAL_NULL_ORIGIN,
    StructuralNullIdentity,
    native_mobius_state,
)
from .public_gonol import (
    PUBLIC_GONOL_157,
    PUBLIC_GONOL_SHA256,
    PublicGonolPosition,
    public_gonol_function,
    public_gonol_position,
    public_gonol_sha256,
)
from .mobius_vesica import *  # noqa: F401,F403 - geometric public module
from .mobius_seed import *  # noqa: F401,F403 - geometric public module

__all__ = [
    "DIRECTED_STRUCTURAL_NULL",
    "DirectMobiusError",
    "LiftedCarrierPoint",
    "NativeMobiusFrame",
    "NativeMobiusState",
    "PUBLIC_GONOL_157",
    "PUBLIC_GONOL_SHA256",
    "PublicGonolPosition",
    "STRUCTURAL_NULL_ORIGIN",
    "StructuralNullIdentity",
    "VisibleCarrierPoint",
    "carrier_from_breadth",
    "deck_translate",
    "lifted_preimages",
    "native_mobius_state",
    "project",
    "public_gonol_function",
    "public_gonol_position",
    "public_gonol_sha256",
    "radius_from_breadth",
    "same_lifted_position",
    "same_visible_position",
]
