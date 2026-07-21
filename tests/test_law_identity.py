# === CHECKS ===
# id: check_law_identity_covers_fixtures
#   proves: law_identity_covers_implementation_and_fixtures
#   call: self::test_law_identity_covers_fixtures
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from ucns import null_zero_law


def test_law_identity_covers_fixtures() -> None:
    first = null_zero_law(fixture_digest="null-fixture-a")
    second = null_zero_law(fixture_digest="null-fixture-b")
    assert first.version == second.version == "1"
    assert first.code_reference == second.code_reference
    assert first.fixture_digest != second.fixture_digest
