# === MODULE_BUILD ===
# id: ucns_mobius_seed_receipt
#   module_name: mobius_seed_receipt
#   module_kind: experiment
#   summary: validates and serializes the complete bounded seven-band construction while preserving source hypotheses, candidate assumptions, and the UCNS-to-METAPAT authority boundary
#   owner: Erin Spencer
#   public_surface: MobiusSeedOfLifeCandidate
#   internal_surface: invariant validation, deterministic manifest serialization, and construction digest
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: source authority and proof standing remain explicit
#   admin_only: false
#   tests: tests/test_mobius_seed_receipt.py
#   rollout: detailed machine receipt for the nonselecting primitive-seven candidate
#   rollback: remove this module and its generated receipts while retaining the source and construction modules
#   requires: ucns_mobius_seed_model
#   since: 2026-08-10
#   unresolved: smooth embedding, physical derivation, spectral operator, zeta correspondence, critical-line theorem, and proof-assistant formalization
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: mobius_seed_receipt_validates_complete_invariant_counts
#   given: the seven-band construction is wrapped as a candidate receipt
#   then: seven bands, twenty-one pairs, thirty-nine pair occurrences, thirteen projected coordinates, the fifteen-fold center bundle, and forty-eight crossing obligations are enforced
#   class: evidence
#   since: 2026-08-10
#
# id: mobius_seed_receipt_separates_source_assumptions_and_zeta_authority
#   given: the detailed manifest is serialized
#   then: source-fixed claims, candidate-only phase and chirality choices, the unresolved center interpretation, UCNS ownership, and absent zeta proof machinery remain separately declared
#   class: doctrine
#   since: 2026-08-10
# === END CONTRACTS ===

"""Validated receipt for the Möbius Seed of Life candidate."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json

from .mobius_seed_exact import MobiusSeedError
from .mobius_seed_model import (
    CHIRALITY_SCHEDULE_STANDING,
    CoordinateRole,
    MOBIUS_SEED_BAND_COUNT,
    MOBIUS_SEED_BOUNDARY_OBLIGATION_COUNT,
    MOBIUS_SEED_HMMM,
    MOBIUS_SEED_HALF_WIDTH,
    MOBIUS_SEED_OUTER_PHASE_STEP_TURNS,
    MOBIUS_SEED_PAIR_COUNT,
    MOBIUS_SEED_PHASE_PERIOD_TURNS,
    MOBIUS_SEED_RADIUS,
    MOBIUS_SEED_SCHEMA_ID,
    MOBIUS_SEED_SCHEMA_VERSION,
    MOBIUS_SEED_SCOPE,
    MOBIUS_SEED_SELECTION_EFFECT,
    MOBIUS_SEED_UNIQUE_COORDINATE_COUNT,
    PHASE_SCHEDULE_STANDING,
    RENDERING_STANDING,
    SOURCE_CENTER_HYPOTHESIS,
    UCNS_CENTER_STANDING,
    ZETA_BRIDGE_STATUS,
    MobiusSeedBand,
    MobiusSeedPair,
    PairRelationship,
    SuperpositionCoordinate,
)
from .mobius_seed_exact import fraction_key


@dataclass(frozen=True, slots=True)
class MobiusSeedOfLifeCandidate:
    bands: tuple[MobiusSeedBand, ...]
    pairs: tuple[MobiusSeedPair, ...]
    coordinates: tuple[SuperpositionCoordinate, ...]
    hmmm: tuple[str, ...] = MOBIUS_SEED_HMMM
    schema_id: str = MOBIUS_SEED_SCHEMA_ID
    schema_version: str = MOBIUS_SEED_SCHEMA_VERSION
    selection_effect: str = MOBIUS_SEED_SELECTION_EFFECT
    scope: str = MOBIUS_SEED_SCOPE
    rendering_standing: str = RENDERING_STANDING
    zeta_bridge_status: str = ZETA_BRIDGE_STATUS

    def __post_init__(self) -> None:
        if (
            self.schema_id != MOBIUS_SEED_SCHEMA_ID
            or self.schema_version != MOBIUS_SEED_SCHEMA_VERSION
            or self.selection_effect != "none"
            or self.scope != MOBIUS_SEED_SCOPE
            or self.hmmm != MOBIUS_SEED_HMMM
        ):
            raise MobiusSeedError("candidate identity or bounded standing mismatch")
        if len(self.bands) != MOBIUS_SEED_BAND_COUNT:
            raise MobiusSeedError("candidate requires seven bands")
        if tuple(item.band_id for item in self.bands) != tuple(f"M{i}" for i in range(7)):
            raise MobiusSeedError("band order must remain M0 through M6")
        if len(self.pairs) != MOBIUS_SEED_PAIR_COUNT:
            raise MobiusSeedError("candidate requires all twenty-one pairs")
        relationships = tuple(item.relationship for item in self.pairs)
        if (
            relationships.count(PairRelationship.VESICA_ADJACENT) != 12
            or relationships.count(PairRelationship.SECONDARY_OVERLAP) != 6
            or relationships.count(PairRelationship.OPPOSITE_TANGENCY) != 3
        ):
            raise MobiusSeedError("pair relationship counts mismatch")
        if len(self.centerline_occurrences) != 39:
            raise MobiusSeedError("candidate requires thirty-nine pair occurrences")
        if len(self.coordinates) != MOBIUS_SEED_UNIQUE_COORDINATE_COUNT:
            raise MobiusSeedError("candidate requires thirteen projected coordinates")
        if sorted(item.multiplicity for item in self.coordinates) != [1] * 6 + [3] * 6 + [15]:
            raise MobiusSeedError("coordinate multiplicity spectrum mismatch")
        if len(self.boundary_obligations) != MOBIUS_SEED_BOUNDARY_OBLIGATION_COUNT:
            raise MobiusSeedError("candidate requires forty-eight crossing obligations")
        dyad = tuple(item for item in self.pairs if item.dyad_pair)
        if len(dyad) != 1 or dyad[0].pair_id != "M0:M1" or dyad[0].phase_delta_turns != 1:
            raise MobiusSeedError("M0:M1 must remain the exact one-turn dyad")

    @property
    def centerline_occurrences(self):
        return tuple(item for pair in self.pairs for item in pair.centerline_occurrences)

    @property
    def boundary_obligations(self):
        return tuple(item for pair in self.pairs for item in pair.boundary_obligations)

    @property
    def center_bundle(self) -> SuperpositionCoordinate:
        return next(item for item in self.coordinates if item.role is CoordinateRole.CENTRAL_SUPERPOSITION)

    def manifest(self) -> dict[str, object]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "selection_effect": self.selection_effect,
            "scope": self.scope,
            "source_basis": {
                "title": "Intersecting Möbius Strips and Quantum Geometry",
                "repository_path": "docs/source/INTERSECTING_MOBIUS_STRIPS_AND_QUANTUM_GEOMETRY.md",
                "retained_claims": [
                    "one-turn opposite-side relation and two-turn return",
                    "two centerline events and four single-boundary crossing claims for a Möbius vesica",
                    "seven-band Seed of Life with anti-aligned first dyad",
                    "incremental phase shifting and three-dimensional braided-fibration hypothesis",
                    "geometric-null-center hypothesis",
                ],
                "not_fixed_by_source": [
                    "the exact one-sixth-turn outer phase increment",
                    "the central-deosil outer-widdershins chirality convention",
                    "the occurrence-addressed pair ordering used by the candidate braid ledger",
                    "a smooth embedding or boundary-crossing solution",
                    "a spectral operator or zeta correspondence",
                ],
            },
            "candidate_assumptions": {
                "phase_schedule_standing": PHASE_SCHEDULE_STANDING,
                "chirality_schedule_standing": CHIRALITY_SCHEDULE_STANDING,
                "pair_order_standing": "candidate-alternating-order-at-each-projected-vesica-event",
            },
            "center_interpretation_boundary": {
                "source_hypothesis": SOURCE_CENTER_HYPOTHESIS,
                "current_ucns_standing": UCNS_CENTER_STANDING,
                "resolution": "hmmm-unresolved-without-authority-transfer",
            },
            "authority_boundary": {
                "ucns_owns": [
                    "construction",
                    "phase-and-chirality schedule",
                    "pair and occurrence ledger",
                    "exact projected-coordinate invariants",
                    "rendering contract",
                ],
                "metapat_may_consume_later": [
                    "commit-pinned invariant receipt",
                    "separately defined spectral operator",
                    "separately proved zeta correspondence",
                ],
                "authority_transfer": "none",
            },
            "parameters": {
                "radius": fraction_key(MOBIUS_SEED_RADIUS),
                "half_width": fraction_key(MOBIUS_SEED_HALF_WIDTH),
                "phase_period_turns": fraction_key(MOBIUS_SEED_PHASE_PERIOD_TURNS),
                "outer_phase_step_turns": fraction_key(MOBIUS_SEED_OUTER_PHASE_STEP_TURNS),
            },
            "counts": {
                "bands": len(self.bands),
                "pairs": len(self.pairs),
                "braid_adjacent_pairs": sum(item.braid_adjacent for item in self.pairs),
                "centerline_occurrences": len(self.centerline_occurrences),
                "unique_projected_coordinates": len(self.coordinates),
                "boundary_crossing_obligations": len(self.boundary_obligations),
            },
            "bands": [item.manifest() for item in self.bands],
            "pairs": [item.manifest() for item in self.pairs],
            "coordinate_multiplicity_ledger": [item.manifest() for item in self.coordinates],
            "rendering_standing": self.rendering_standing,
            "zeta_bridge_status": self.zeta_bridge_status,
            "hmmm": list(self.hmmm),
        }

    @property
    def construction_digest(self) -> str:
        payload = json.dumps(self.manifest(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        return sha256(payload.encode("utf-8")).hexdigest()

    def manifest_json(self, *, indent: int = 2) -> str:
        payload = dict(self.manifest())
        payload["construction_sha256"] = self.construction_digest
        return json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=indent) + "\n"
