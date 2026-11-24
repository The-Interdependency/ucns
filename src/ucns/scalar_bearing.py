# ratios: loc_comments=14:29 imports_exports=1:2 calls_definitions=6:2
"""Exact Unicode bearings shared by geometry profiles. Use unicode_scalar_turn('ë')."""
# === MODULE_BUILD ===
# id: unicode_scalar_bearing
#   module_name: scalar_bearing
#   module_kind: geometry
#   summary: width-independent Unicode scalar admission and SPACE-relative turn
#   owner: Erin Spencer
#   public_surface: scalar_value, unicode_scalar_turn, SPACE_SCALAR, UNICODE_SCALAR_MODULUS
#   internal_surface: scalar validation and exact turn arithmetic
#   auth_boundary: no authority assertion
#   rollout: shared angular function for both encoding and placement profiles
#   rollback: use the prior pinned geometry package for its original records
#   tests: tests/test_unicode_gonol.py, tests/test_attachment_stack.py
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: input scalar remains local
#   admin_only: false
#   requires: none
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: unicode_scalar_has_one_space_relative_bearing
#   given: one valid Unicode scalar
#   then: its exact turn is ((scalar-SPACE) mod 0x110000)/0x110000 with SPACE at turn zero
# === END CONTRACTS ===
from fractions import Fraction

UNICODE_SCALAR_MODULUS = 0x110000
SPACE_SCALAR = 0x20


def scalar_value(character: str) -> int:
    if not isinstance(character, str) or len(character) != 1:
        raise TypeError("glyph must be exactly one Unicode scalar")
    value = ord(character)
    if 0xD800 <= value <= 0xDFFF:
        raise ValueError("surrogate code points are not Unicode scalars")
    return value


def unicode_scalar_turn(character: str) -> Fraction:
    """Exact SPACE-relative turn for one Unicode scalar.

    The full scalar numeric range is the stable modulus. Assignment status is
    deliberately irrelevant, so future Unicode versions cannot move existing
    bearings. Surrogate values are holes, not compressed-away positions.
    """
    value = scalar_value(character)
    return Fraction((value - SPACE_SCALAR) % UNICODE_SCALAR_MODULUS,
                    UNICODE_SCALAR_MODULUS)
# ratios: loc_comments=14:29 imports_exports=1:2 calls_definitions=6:2
