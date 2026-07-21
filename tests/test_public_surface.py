# === CHECKS ===
# id: check_public_surface_is_bounded
#   proves: public_surface_exposes_only_ratified_foundations
#   call: self::test_public_surface_is_bounded
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import ucns


def test_public_surface_is_bounded() -> None:
    exported = set(ucns.__all__)
    assert "LiftedCarrierPoint" in exported
    assert "STRUCTURAL_NULL" in exported
    assert "Cell" in exported
    assert "Carrier" in exported
    assert "support_weight" in exported
    assert "pair" in exported
    assert "prune" in exported
    assert "collapse" in exported

    assert "UCNSObject" not in exported
    assert "product_character" not in exported
    assert "faithful_breadth" not in exported
    assert "multiply" not in exported
    assert "factor" not in exported
    assert "TheoremN" not in exported
