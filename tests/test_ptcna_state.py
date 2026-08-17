# === CHECKS ===
# id: check_ucns_ptcna_exact_shape
#   proves: ucns_ptcna_state_has_exact_requested_shape
#   call: self::test_receipt_has_exact_dense_shape_and_state_digest
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_ucns_ptcna_deterministic_receipt
#   proves: ucns_ptcna_receipt_is_deterministic_and_provenance_bound
#   call: self::test_receipt_is_byte_deterministic_and_provenance_bound
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_ucns_ptcna_tamper_rejection
#   proves: ucns_ptcna_receipt_rejects_tampering
#   call: self::test_every_tested_authority_tamper_is_rejected
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_ucns_ptcna_status_firewall
#   proves: ucns_ptcna_candidate_transfers_no_status
#   call: self::test_receipt_preserves_candidate_and_nonclaim_boundaries
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from copy import deepcopy
from hashlib import sha256

import pytest

from ucns.edcm import PUBLIC_GONOL_SHA256
from ucns.ptcna_state import (
    PTCNA_STATE_BYTES,
    PTCNA_STATE_ELEMENTS,
    PTCNA_STATE_SHAPE,
    PTCNAStateReceiptError,
    build_ptcna_state_receipt,
    canonical_receipt_bytes,
    validate_ptcna_state_receipt,
)


COMMIT = "1" * 40


def test_receipt_has_exact_dense_shape_and_state_digest() -> None:
    receipt = build_ptcna_state_receipt(COMMIT)
    assert PTCNA_STATE_SHAPE == (157, 7, 7, 53)
    assert PTCNA_STATE_ELEMENTS == 407_729
    assert PTCNA_STATE_BYTES == 3_261_832
    assert receipt["state"]["shape"] == [157, 7, 7, 53]
    assert receipt["state"]["axis_names"] == [
        "public_gonol_position", "circle_phase", "seed_phase", "neural_node"
    ]
    assert receipt["state"]["sha256"] == sha256(b"\0" * PTCNA_STATE_BYTES).hexdigest()


def test_receipt_is_byte_deterministic_and_provenance_bound() -> None:
    first = build_ptcna_state_receipt(COMMIT)
    second = build_ptcna_state_receipt(COMMIT)
    assert canonical_receipt_bytes(first) == canonical_receipt_bytes(second)
    assert first["provenance"]["public_gonol_sha256"] == PUBLIC_GONOL_SHA256
    assert first["producer"]["commit"] == COMMIT
    assert validate_ptcna_state_receipt(first) == first


@pytest.mark.parametrize(
    ("section", "field", "value"),
    [
        ("state", "shape", [157, 7, 53]),
        ("state", "sha256", "0" * 64),
        ("producer", "commit", "2" * 40),
        ("provenance", "public_gonol_sha256", "0" * 64),
        ("boundaries", "geometry_selected", True),
    ],
)
def test_every_tested_authority_tamper_is_rejected(section: str, field: str, value: object) -> None:
    receipt = build_ptcna_state_receipt(COMMIT)
    tampered = deepcopy(receipt)
    tampered[section][field] = value
    with pytest.raises(PTCNAStateReceiptError):
        validate_ptcna_state_receipt(tampered)


def test_receipt_preserves_candidate_and_nonclaim_boundaries() -> None:
    receipt = build_ptcna_state_receipt(COMMIT)
    assert receipt["candidate"] == {
        "id": "ucns-ptcna-157x7x7x53-v1",
        "scope": "ptcna-initialization-only",
        "standing": "candidate",
        "selected": False,
    }
    assert receipt["boundaries"]["geometry_selected"] is False
    assert receipt["boundaries"]["usefulness_established"] is False
    assert receipt["boundaries"]["production_privacy_established"] is False
