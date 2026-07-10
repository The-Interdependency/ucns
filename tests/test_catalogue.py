from ucns.catalogue import build_catalogue_d1, build_catalogue_d2_oracle
from ucns.domains import S2, depth_of, generate_payload_catalogue, is_in_oracle_class


def structural_key(obj):
    return (
        obj.n_min,
        tuple(obj.F_plus),
        tuple((angle, structural_key(payload) if payload is not None else None) for angle, payload in obj.A_plus),
    )


def test_build_catalogue_d1_matches_payload_catalogue_without_unit():
    expected = [obj for obj in generate_payload_catalogue() if obj is not None]
    result = build_catalogue_d1()
    assert result == expected
    assert all(depth_of(obj) == 1 for obj in result)


def test_build_catalogue_d2_oracle_with_narrow_basis_is_depth2_oracle_only():
    result = build_catalogue_d2_oracle(payload_basis=[None, S2])
    assert result
    assert all(depth_of(obj) == 2 for obj in result)
    assert all(is_in_oracle_class(obj) for obj in result)
    assert all(any(payload is not None for _angle, payload in obj.A_plus) for obj in result)


def test_build_catalogue_d2_oracle_deduplicates_structural_values():
    result = build_catalogue_d2_oracle(payload_basis=[None, S2, S2])
    keys = [structural_key(obj) for obj in result]
    assert len(keys) == len(set(keys))
