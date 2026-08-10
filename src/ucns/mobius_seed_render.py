# === MODULE_BUILD ===
# id: ucns_mobius_seed_renderer
#   module_name: mobius_seed_render
#   module_kind: presentation
#   summary: renders the seven candidate Möbius bands as deterministic Wavefront OBJ text with reversed transverse seam indexing
#   owner: Erin Spencer
#   public_surface: render_mobius_seed_obj
#   internal_surface: deterministic sampled vertex and face emission
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: no user data; rendering loss and unresolved intersections are embedded in output comments
#   admin_only: false
#   tests: tests/test_mobius_seed_render.py
#   rollout: deterministic inspectable 3D export for the nonselecting candidate
#   rollback: remove the renderer without altering exact construction receipts
#   requires: ucns_mobius_seed_builder, ucns_mobius_seed_receipt
#   since: 2026-08-10
#   unresolved: mesh output does not certify smooth embedding or boundary-crossing transversality
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: mobius_seed_obj_renderer_is_deterministic_and_reverses_the_seam
#   given: fixed longitudinal and transverse sample counts
#   then: OBJ vertex and face counts are deterministic, the final seam reverses transverse indexing, and output standing disclaims embedding proof
#   class: correctness
#   since: 2026-08-10
# === END CONTRACTS ===

"""Deterministic OBJ rendering for the Möbius Seed candidate."""

from __future__ import annotations

from .mobius_seed_build import build_mobius_seed_of_life_candidate
from .mobius_seed_exact import MobiusSeedError
from .mobius_seed_model import (
    MOBIUS_SEED_HALF_WIDTH,
    MOBIUS_SEED_RADIUS,
    MOBIUS_SEED_SCHEMA_ID,
    MOBIUS_SEED_SCHEMA_VERSION,
    RENDERING_STANDING,
)
from .mobius_seed_receipt import MobiusSeedOfLifeCandidate


def render_mobius_seed_obj(
    candidate: MobiusSeedOfLifeCandidate | None = None,
    *,
    longitudinal_steps: int = 84,
    transverse_steps: int = 6,
    radius: float = float(MOBIUS_SEED_RADIUS),
    half_width: float = float(MOBIUS_SEED_HALF_WIDTH),
) -> str:
    if candidate is None:
        candidate = build_mobius_seed_of_life_candidate()
    if isinstance(longitudinal_steps, bool) or not isinstance(longitudinal_steps, int) or longitudinal_steps < 7:
        raise MobiusSeedError("longitudinal_steps must be an integer at least seven")
    if isinstance(transverse_steps, bool) or not isinstance(transverse_steps, int) or transverse_steps < 1:
        raise MobiusSeedError("transverse_steps must be a positive integer")
    lines = [
        f"# {MOBIUS_SEED_SCHEMA_ID}@{MOBIUS_SEED_SCHEMA_VERSION}",
        f"# construction-sha256 {candidate.construction_digest}",
        f"# standing {RENDERING_STANDING}",
        "# boundary-crossing obligations are not realized or certified by this mesh",
    ]
    ring_size = transverse_steps + 1
    offset = 0
    for band in candidate.bands:
        lines.append(f"o {band.band_id}")
        for i in range(longitudinal_steps):
            for j in range(ring_size):
                point = band.point(
                    i / longitudinal_steps,
                    -1.0 + 2.0 * j / transverse_steps,
                    radius=radius,
                    half_width=half_width,
                )
                lines.append(f"v {point[0]:.17g} {point[1]:.17g} {point[2]:.17g}")
        def vertex(ring: int, branch: int) -> int:
            return offset + ring * ring_size + branch + 1
        for i in range(longitudinal_steps):
            next_i = (i + 1) % longitudinal_steps
            for j in range(transverse_steps):
                if i < longitudinal_steps - 1:
                    a, b, c, d = vertex(i, j), vertex(next_i, j), vertex(next_i, j + 1), vertex(i, j + 1)
                else:
                    a, b, c, d = vertex(i, j), vertex(0, transverse_steps - j), vertex(0, transverse_steps - j - 1), vertex(i, j + 1)
                lines.append(f"f {a} {b} {c} {d}")
        offset += longitudinal_steps * ring_size
    return "\n".join(lines) + "\n"
