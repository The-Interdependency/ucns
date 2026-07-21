# === CHECKS ===
# id: check_public_surface_is_bounded
#   proves: public_surface_exposes_only_carrier_floor
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
    assert "UCNSObject" not in exported
    assert "multiply" not in exported
    assert "factor" not in exported
    assert "TheoremN" not in exported
