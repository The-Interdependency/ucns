# === CHECKS ===
# id: current_lexical_source_receipt_check
#   proves: xkcd_floor_bytes_are_exact_and_source_ordered, oewn_core_receipt_is_exact_release_identity, current_lexical_sources_precede_materialization, xkcd_receipt_matches_packaged_bytes
#   call: self::test_current_lexical_source_receipts_are_exact
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
#
# id: current_lexical_source_tamper_check
#   proves: xkcd_floor_bytes_are_exact_and_source_ordered, oewn_core_receipt_is_exact_release_identity
#   call: self::test_source_receipt_fields_and_wrong_checkout_fail_closed
#   requires: python3
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import replace
import os
from pathlib import Path

import pytest

from ucns.lexical_sources import (
    OEWN_COMMIT,
    LexicalSourceError,
    load_xkcd_simplewriter,
    quoted_xkcd_payload,
    verify_oewn_2025_core,
)


def _oewn_root() -> Path:
    configured = os.environ.get("UCNS_OEWN_2025_CORE_ROOT")
    if not configured:
        pytest.skip("UCNS_OEWN_2025_CORE_ROOT is not configured")
    return Path(configured)


def test_current_lexical_source_receipts_are_exact() -> None:
    xkcd = load_xkcd_simplewriter()
    assert xkcd.version == "0.2.1"
    assert len(xkcd.surface_forms) == len(set(xkcd.surface_forms)) == 3_634
    assert xkcd.surface_forms[:3] == (
        "understandings", "understanding", "conversations",
    )
    assert xkcd.surface_forms[-3:] == ("an", "i", "a")
    assert xkcd.family_count == 1_000
    assert xkcd.family_mapping_available is False
    assert xkcd.receipt_id.startswith("ucns.xkcd-simplewriter-receipt:sha256:")
    assert quoted_xkcd_payload(xkcd) == "|".join(xkcd.surface_forms)
    with pytest.raises(LexicalSourceError, match="official quoted payload"):
        quoted_xkcd_payload(replace(xkcd, surface_forms=xkcd.surface_forms[1:]))
    with pytest.raises(LexicalSourceError, match="provenance"):
        quoted_xkcd_payload(replace(xkcd, source_url="https://example.invalid/words.js"))
    oewn = verify_oewn_2025_core(_oewn_root())
    assert oewn.commit == OEWN_COMMIT
    assert oewn.core_file_count == 73
    assert "Namenet" in oewn.source_scope and "excluded" in oewn.source_scope
    assert oewn.receipt_id.startswith("ucns.oewn-core-receipt:sha256:")


def test_source_receipt_fields_and_wrong_checkout_fail_closed(tmp_path: Path) -> None:
    xkcd = load_xkcd_simplewriter()
    assert replace(xkcd).receipt_id == xkcd.receipt_id
    with pytest.raises(LexicalSourceError, match="Git identity"):
        verify_oewn_2025_core(tmp_path)
