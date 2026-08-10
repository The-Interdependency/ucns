# === CHECKS ===
# id: check_mobius_seed_obj_renderer
#   proves: mobius_seed_obj_renderer_is_deterministic_and_reverses_the_seam
#   call: self::test_obj_counts_and_reversed_seam
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from ucns.mobius_seed_render import render_mobius_seed_obj


def test_obj_counts_and_reversed_seam() -> None:
    obj = render_mobius_seed_obj(longitudinal_steps=7, transverse_steps=2)
    lines = obj.splitlines()
    vertices = [line for line in lines if line.startswith("v ")]
    faces = [line for line in lines if line.startswith("f ")]
    assert len(vertices) == 7 * 7 * 3
    assert len(faces) == 7 * 7 * 2
    assert faces[12:14] == ["f 19 3 2 20", "f 20 2 1 21"]
    assert "not-smooth-embedding-certification" in obj
    assert obj == render_mobius_seed_obj(longitudinal_steps=7, transverse_steps=2)
