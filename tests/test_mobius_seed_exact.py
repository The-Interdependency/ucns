# === CHECKS ===
# id: check_mobius_seed_exact_geometry
#   proves: mobius_seed_exact_geometry_is_closed_and_reversible
#   call: self::test_exact_surd_and_hex_geometry
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from fractions import Fraction
from ucns.mobius_seed_exact import HexCoordinate, Surd3


def test_exact_surd_and_hex_geometry() -> None:
    assert Surd3(1, 1) * Surd3(1, -1) == Surd3(-2)
    assert HexCoordinate(1, 0).planar_point.x == Surd3(1)
    assert HexCoordinate(0, 1).planar_point.y == Surd3(0, Fraction(1, 2))
    assert HexCoordinate(1, 0).distance(HexCoordinate(0, 1)) == 1
