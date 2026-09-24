# === MODULE_BUILD ===
# id: ucns_geometry_public_surface
#   module_name: __init__
#   module_kind: facade
#   summary: geometry-only UCNS public surface including exact scale/representation candidates
#   owner: Erin Spencer
#   public_surface: carrier geometry, framed Mobius root loop, exact Public Gonol carrier, Mobius vesica and seed geometry, modular orbit geometry, visible-circle gonal wave boundary trace, displacement/lift/motion candidates, exact multiplicative scale-action candidate
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol, tests.test_geometry_public_surface, tests.test_carrier, tests.test_modular_orbit, tests.test_gonal_boundary_trace, tests.test_visible_displacement, tests.test_scale_action
#   rollout: active geometry-only package facade
#   rollback: restore prior facade from Git history
#   requires: directed_carrier_floor, ucns_native_mobius_geometry, ucns_public_gonol_geometry, ucns_mobius_vesica_candidate, ucns_mobius_seed_of_life_candidate, ucns_modular_orbit_geometry, ucns_gonal_boundary_trace, ucns_visible_displacement_candidate, ucns_multiplicative_scale_action_candidate
#   since: 2026-08-20
#   unresolved: canonical completion of the full UCNS geometric construction
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: geometry_public_surface_excludes_nongeometric_domains
#   given: the active ucns package facade is imported
#   then: its declared public surface contains geometry only and removed lexical, semantic, EDCM, PTCNA, evaluator, and bridge modules are absent from the package tree
#   class: safety
#   since: 2026-08-20
#
# id: geometry_public_surface_includes_modular_orbit_geometry
#   given: the active ucns package facade is imported
#   then: the exact modular orbit geometry record, error, circle-position record, and builder are public without downstream domain semantics
#   class: correctness
#   since: 2026-09-05
#
# id: geometry_public_surface_includes_gonal_boundary_trace
#   given: the active ucns package facade is imported
#   then: exact visible-circle wave-mode traces, gonal boundary samples, continuum covering witnesses, and builders are public without downstream physical-selection semantics
#   class: correctness
#   since: 2026-09-05
#
# id: geometry_public_surface_includes_visible_displacement_candidate
#   given: the active ucns package facade is imported
#   then: the exact visible-circle displacement candidate record, error, builder, and replay are public with candidate standing
#   class: correctness
#   since: 2026-09-15
#
# id: geometry_public_surface_includes_radius_recursion_candidate
#   given: the active ucns package facade is imported
#   then: the exact radius-recursion candidate record, error, builder, and replay are public with candidate standing
#   class: correctness
#   since: 2026-09-15
#
# id: geometry_public_surface_includes_placement_frame_candidate
#   given: the active ucns package facade is imported
#   then: the exact placement-frame candidate record, error, builder, and replay are public with candidate standing
#   class: correctness
#   since: 2026-09-15
#
# id: geometry_public_surface_includes_displacement_law_candidates
#   given: the active ucns package facade is imported
#   then: the displacement-law candidate registry, composite record, error, builder, and replay are public with candidate standing
#   class: correctness
#   since: 2026-09-15
#
# id: geometry_public_surface_includes_displacement_falsification
#   given: the active ucns package facade is imported
#   then: the displacement falsification controls, report, error, and runner are public with falsification-selection standing
#   class: correctness
#   since: 2026-09-16
#
# id: geometry_public_surface_includes_lattice_carrier_candidate
#   given: the active ucns package facade is imported
#   then: the abstract lattice/carrier address, derivations, record, error, builder, and replay are public with candidate standing
#   class: correctness
#   since: 2026-09-16
#
# id: geometry_public_surface_includes_motion_candidate
#   given: the active ucns package facade is imported
#   then: the motion record, error, builder, replay, and the motion falsification controls and runner are public with candidate standing
#   class: correctness
#   since: 2026-09-19
#
# id: geometry_public_surface_includes_displacement_selection
#   given: the active ucns package facade is imported
#   then: the displacement selection controls, runner, and replay are public with scoped selection standing
#   class: correctness
#   since: 2026-09-19
#
# id: geometry_public_surface_includes_lifted_displacement_candidate
#   given: the active ucns package facade is imported
#   then: the lifted displacement record, error, builder, and replay are public with candidate standing
#   class: correctness
#   since: 2026-09-19
#
# id: geometry_public_surface_includes_lift_selection_candidates
#   given: the active ucns package facade is imported
#   then: the lift-selection builders, error, and controls runner are public with candidate standing
#   class: correctness
#   since: 2026-09-21
#
# id: geometry_public_surface_includes_scale_action_candidate
#   given: the active ucns package facade is imported
#   then: the exact domain-agnostic multiplicative scale action, application receipt, invariant helper, builders, and replay are public with candidate standing
#   class: correctness
#   since: 2026-09-23
# === END CONTRACTS ===

"""UCNS geometry.

The active package surface is deliberately geometric: carriers, exact motion,
Möbius constructions, geometric certificates, modular orbit geometry,
visible-circle gonal wave boundary traces, and topological/prime geometry.
Lexical semantics, corpora, morphology, definition recursion, evaluator
frameworks, PTCNA state, and cross-stack adapters are not UCNS package content.
"""

from .carrier import (
    LIFTED_PERIOD,
    STRUCTURAL_NULL,
    VISIBLE_PERIOD,
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
from .gonal_boundary_trace import (
    CircleWaveCoveringTrace,
    CircleWaveModeTrace,
    GonalBoundarySample,
    GonalBoundaryTraceError,
    build_circle_wave_mode_trace,
    pullback_circle_wave_trace,
)
from .modular_orbit import (
    CircularResiduePosition,
    ModularOrbitError,
    ModularOrbitGeometry,
    build_modular_orbit_geometry,
)
from .public_gonol import (
    PUBLIC_GONOL_157,
    PUBLIC_GONOL_SHA256,
    PublicGonolPosition,
    public_gonol_function,
    public_gonol_position,
    public_gonol_sha256,
)
from .visible_displacement import (
    SCHEMA as VISIBLE_DISPLACEMENT_SCHEMA,
    VERSION as VISIBLE_DISPLACEMENT_VERSION,
    VisibleDisplacementError,
    VisibleDisplacementRecord,
    build_visible_displacement,
    replay_visible_displacement,
)
from .radius_recursion import (
    SCHEMA as RADIUS_RECURSION_SCHEMA,
    VERSION as RADIUS_RECURSION_VERSION,
    RadiusRecursionError,
    RadiusRecursionRecord,
    build_radius_recursion,
    replay_radius_recursion,
)
from .placement_frame import (
    SCHEMA as PLACEMENT_FRAME_SCHEMA,
    VERSION as PLACEMENT_FRAME_VERSION,
    PlacementFrameError,
    PlacementFrameRecord,
    build_placement_frame,
    replay_placement_frame,
)
from .displacement_law import (
    SCHEMA as DISPLACEMENT_LAW_SCHEMA,
    VERSION as DISPLACEMENT_LAW_VERSION,
    DISPLACEMENT_LAW_CANDIDATES,
    DisplacementLawError,
    DisplacementRecord,
    build_displacement,
    replay_displacement,
)
from .displacement_falsification import (
    SCHEMA as DISPLACEMENT_FALSIFICATION_SCHEMA,
    VERSION as DISPLACEMENT_FALSIFICATION_VERSION,
    FALSIFIER_CONTROLS,
    FalsificationError,
    FalsificationReport,
    run_falsification,
)
from .displacement_selection import (
    SCHEMA as DISPLACEMENT_SELECTION_SCHEMA,
    VERSION as DISPLACEMENT_SELECTION_VERSION,
    SELECTION_CONTROLS,
    DisplacementSelectionError,
    run_modular_orbit_permutation_control,
    run_displacement_selection,
    replay_displacement_selection,
)
from .lattice_carrier import (
    SCHEMA as LATTICE_CARRIER_SCHEMA,
    VERSION as LATTICE_CARRIER_VERSION,
    LatticeCarrierError,
    LatticeAddress,
    LatticeCarrierRecord,
    build_lattice_address,
    derive_lattice_from_deck_translations,
    derive_lattice_from_modular_orbit,
    build_lattice_carrier,
    replay_lattice_carrier,
)
from .lifted_displacement import (
    SCHEMA as LIFTED_DISPLACEMENT_SCHEMA,
    VERSION as LIFTED_DISPLACEMENT_VERSION,
    LiftedDisplacementError,
    LiftedDisplacementRecord,
    build_lifted_displacement,
    replay_lifted_displacement,
)
from .lift_selection import (
    SCHEMA as LIFT_SELECTION_SCHEMA,
    VERSION as LIFT_SELECTION_VERSION,
    LiftSelectionError,
    build_provenance_interval_lift,
    build_canonical_witness_lift,
    run_lift_selection_controls,
    run_lift_selection_gate,
    replay_lift_selection_gate,
)
from .motion import (
    SCHEMA as MOTION_SCHEMA,
    VERSION as MOTION_VERSION,
    MotionError,
    MotionStepRecord,
    MotionRecord,
    build_motion,
    replay_motion,
)
from .motion_falsification import (
    SCHEMA as MOTION_FALSIFICATION_SCHEMA,
    VERSION as MOTION_FALSIFICATION_VERSION,
    MOTION_FALSIFIER_CONTROLS,
    MotionFalsificationError,
    run_motion_falsification,
)
from .scale_action import (
    SCHEMA as SCALE_ACTION_SCHEMA,
    VERSION as SCALE_ACTION_VERSION,
    MultiplicativeScaleAction,
    ScaleActionError,
    ScaleActionRecord,
    build_scale_action,
    build_scale_action_record,
    monomial_value,
    replay_scale_action_record,
)
from .mobius_vesica import __all__ as _mobius_vesica_all
from .mobius_vesica import *  # noqa: F401,F403 - geometric public module
from .mobius_seed import __all__ as _mobius_seed_all
from .mobius_seed import *  # noqa: F401,F403 - geometric public module

__all__ = list(dict.fromkeys([
    "CircleWaveCoveringTrace",
    "CircleWaveModeTrace",
    "CircularResiduePosition",
    "DirectMobiusError",
    "GonalBoundarySample",
    "GonalBoundaryTraceError",
    "LIFTED_PERIOD",
    "LiftedCarrierPoint",
    "ModularOrbitError",
    "ModularOrbitGeometry",
    "NativeMobiusFrame",
    "NativeMobiusState",
    "PUBLIC_GONOL_157",
    "PUBLIC_GONOL_SHA256",
    "PublicGonolPosition",
    "DISPLACEMENT_FALSIFICATION_SCHEMA",
    "DISPLACEMENT_FALSIFICATION_VERSION",
    "DISPLACEMENT_LAW_CANDIDATES",
    "DISPLACEMENT_LAW_SCHEMA",
    "DISPLACEMENT_LAW_VERSION",
    "DISPLACEMENT_SELECTION_SCHEMA",
    "DISPLACEMENT_SELECTION_VERSION",
    "DisplacementLawError",
    "DisplacementSelectionError",
    "DisplacementRecord",
    "FALSIFIER_CONTROLS",
    "FalsificationError",
    "FalsificationReport",
    "LATTICE_CARRIER_SCHEMA",
    "LATTICE_CARRIER_VERSION",
    "LIFTED_DISPLACEMENT_SCHEMA",
    "LIFTED_DISPLACEMENT_VERSION",
    "LIFT_SELECTION_SCHEMA",
    "LIFT_SELECTION_VERSION",
    "LatticeAddress",
    "LatticeCarrierError",
    "LatticeCarrierRecord",
    "LiftedDisplacementError",
    "LiftedDisplacementRecord",
    "LiftSelectionError",
    "PLACEMENT_FRAME_SCHEMA",
    "PLACEMENT_FRAME_VERSION",
    "PlacementFrameError",
    "PlacementFrameRecord",
    "RADIUS_RECURSION_SCHEMA",
    "RADIUS_RECURSION_VERSION",
    "RadiusRecursionError",
    "RadiusRecursionRecord",
    "SCALE_ACTION_SCHEMA",
    "SCALE_ACTION_VERSION",
    "ScaleActionError",
    "ScaleActionRecord",
    "MultiplicativeScaleAction",
    "STRUCTURAL_NULL",
    "STRUCTURAL_NULL_ORIGIN",
    "StructuralNullIdentity",
    "VISIBLE_PERIOD",
    "VISIBLE_DISPLACEMENT_SCHEMA",
    "VISIBLE_DISPLACEMENT_VERSION",
    "VisibleCarrierPoint",
    "VisibleDisplacementError",
    "VisibleDisplacementRecord",
    "build_circle_wave_mode_trace",
    "build_displacement",
    "build_canonical_witness_lift",
    "build_lattice_address",
    "build_lattice_carrier",
    "build_lifted_displacement",
    "build_modular_orbit_geometry",
    "build_motion",
    "build_placement_frame",
    "build_provenance_interval_lift",
    "build_radius_recursion",
    "build_scale_action",
    "build_scale_action_record",
    "build_visible_displacement",
    "carrier_from_breadth",
    "deck_translate",
    "derive_lattice_from_deck_translations",
    "derive_lattice_from_modular_orbit",
    "lifted_preimages",
    "MOTION_FALSIFIER_CONTROLS",
    "MOTION_FALSIFICATION_SCHEMA",
    "MOTION_FALSIFICATION_VERSION",
    "MOTION_SCHEMA",
    "MOTION_VERSION",
    "MotionError",
    "MotionFalsificationError",
    "MotionRecord",
    "MotionStepRecord",
    "monomial_value",
    "native_mobius_state",
    "project",
    "public_gonol_function",
    "public_gonol_position",
    "public_gonol_sha256",
    "pullback_circle_wave_trace",
    "radius_from_breadth",
    "replay_displacement",
    "replay_displacement_selection",
    "replay_lattice_carrier",
    "replay_lifted_displacement",
    "replay_motion",
    "replay_placement_frame",
    "replay_radius_recursion",
    "replay_scale_action_record",
    "replay_visible_displacement",
    "run_displacement_selection",
    "run_falsification",
    "run_lift_selection_controls",
    "run_lift_selection_gate",
    "replay_lift_selection_gate",
    "run_modular_orbit_permutation_control",
    "run_motion_falsification",
    "SELECTION_CONTROLS",
    "same_lifted_position",
    "same_visible_position",
] + list(_mobius_vesica_all) + list(_mobius_seed_all)))
