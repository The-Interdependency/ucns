# === CHECKS ===
# id: relational_carrier_exact_boundary_check
#   proves: relational_carrier_is_intrinsic_and_metadata_free, relational_carrier_preserves_order_multiplicity_and_sidedness, relational_carrier_roundtrip_is_canonical
#   call: self::test_relational_carrier_exact_boundary
#   timeout: 30
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import json

import pytest

from ucns.relational_carrier import (
    RelationalCarrierError,
    build_relational_carrier,
    parse_relational_carrier,
    relational_carrier_bytes,
)


def test_relational_carrier_exact_boundary() -> None:
    carrier = build_relational_carrier(3, ((0, 4, 1), (0, 4, 1), (1, 5, 2)))
    encoded = relational_carrier_bytes(carrier)
    assert parse_relational_carrier(encoded) == carrier
    assert relational_carrier_bytes(parse_relational_carrier(encoded)) == encoded
    assert encoded.endswith(b"\n")
    assert b"English" not in encoded and b"provenance" not in encoded

    variants = (
        build_relational_carrier(3, ((0, 4, 1), (1, 5, 2), (0, 4, 1))),
        build_relational_carrier(3, ((0, 4, 1), (1, 5, 2))),
        build_relational_carrier(3, ((1, 4, 0), (0, 4, 1), (1, 5, 2))),
        build_relational_carrier(3, ((0, 6, 1), (0, 4, 1), (1, 5, 2))),
    )
    assert all(item.stable_identity != carrier.stable_identity for item in variants)

    value = json.loads(encoded)
    value["geometry_attached"] = True
    with pytest.raises(RelationalCarrierError):
        parse_relational_carrier(
            json.dumps(value, sort_keys=True, separators=(",", ":")).encode() + b"\n"
        )
    for field in (
        "geometry_attached",
        "measurement_attached",
        "theorem_status_transfer",
    ):
        for invalid in (0, 1, "false"):
            value = json.loads(encoded)
            value[field] = invalid
            with pytest.raises(RelationalCarrierError, match="exact boolean"):
                parse_relational_carrier(
                    json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
                    + b"\n"
                )
    with pytest.raises(RelationalCarrierError, match="canonical"):
        parse_relational_carrier(json.dumps(json.loads(encoded), indent=2).encode())
    with pytest.raises(RelationalCarrierError, match="dense"):
        parse_relational_carrier(encoded.replace(b'"nodes":[0,1,2]', b'"nodes":[0,2]'))
