# === CHECKS ===
# id: check_mobius_seed_public_surface
#   proves: mobius_seed_public_surface_exports_only_bounded_candidate_components
#   call: self::test_public_surface_is_bounded_and_constructible
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import ucns.mobius_seed as public


def test_public_surface_is_bounded_and_constructible() -> None:
    assert "build_mobius_seed_of_life_candidate" in public.__all__
    assert "render_mobius_seed_obj" in public.__all__
    assert "zeta_proof" not in public.__all__
    assert len(public.build_mobius_seed_of_life_candidate().bands) == 7
