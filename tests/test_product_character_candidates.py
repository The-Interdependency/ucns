# === CHECKS ===
# id: check_product_of_supports_candidate
#   proves: product_of_supports_is_multiplicative, product_of_supports_separates_from_W, product_of_supports_null_is_zero
#   call: self::test_product_of_supports_candidate
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from ucns import STRUCTURAL_NULL, Carrier, Cell, pair, support_weight
from ucns.product_character_candidates import (
    PRODUCT_OF_SUPPORTS_CANDIDATE,
    product_of_supports,
    same_M_different_W_witness,
    same_W_different_M_witness,
    separation_suite_for_product_of_supports,
)


def test_product_of_supports_candidate() -> None:
    # Null floor
    assert product_of_supports(STRUCTURAL_NULL) == 0.0

    # Unit cells give neutral M = 1
    unit = Carrier((Cell(coordinate="u", mu=1.0),))
    assert product_of_supports(unit) == 1.0

    # Separation direction 1: same W, different M
    w = same_W_different_M_witness()
    left, right = w.subjects
    assert support_weight(left) == support_weight(right) == 2.0
    assert product_of_supports(left) == 1.0
    assert product_of_supports(right) == 2.0

    # Separation direction 2: same M, different W
    m = same_M_different_W_witness()
    d, e = m.subjects
    assert product_of_supports(d) == product_of_supports(e) == 1.0
    assert support_weight(d) != support_weight(e)

    # Multiplicativity under actual pairing
    p = pair(left, right)
    assert product_of_supports(p) == product_of_supports(left) * product_of_supports(right)

    # Full laboratory suite
    suite = separation_suite_for_product_of_supports()
    report = suite.evaluate(PRODUCT_OF_SUPPORTS_CANDIDATE)
    assert report.all_passed, [r for r in report.results if not r.passed]
