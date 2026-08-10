# === CHECKS ===
# id: check_mobius_seed_complete_pair_ledger
#   proves: mobius_seed_builder_constructs_complete_seven_band_pair_ledger
#   call: self::test_complete_pair_and_coordinate_ledger
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_mobius_seed_crossing_obligations
#   proves: mobius_seed_builder_records_four_crossing_obligations_per_adjacent_pair
#   call: self::test_four_unrealized_obligations_per_adjacent_pair
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from ucns.mobius_seed_build import build_mobius_seed_of_life_candidate
from ucns.mobius_seed_model import PairRelationship


def test_complete_pair_and_coordinate_ledger() -> None:
    seed = build_mobius_seed_of_life_candidate()
    relationships = tuple(item.relationship for item in seed.pairs)
    assert len(seed.bands) == 7
    assert len(seed.pairs) == 21
    assert relationships.count(PairRelationship.VESICA_ADJACENT) == 12
    assert relationships.count(PairRelationship.SECONDARY_OVERLAP) == 6
    assert relationships.count(PairRelationship.OPPOSITE_TANGENCY) == 3
    assert len(seed.centerline_occurrences) == 39
    assert len(seed.coordinates) == 13
    assert sorted(item.multiplicity for item in seed.coordinates) == [1] * 6 + [3] * 6 + [15]


def test_four_unrealized_obligations_per_adjacent_pair() -> None:
    seed = build_mobius_seed_of_life_candidate()
    adjacent = tuple(item for item in seed.pairs if item.braid_adjacent)
    assert len(adjacent) == 12
    assert len(seed.boundary_obligations) == 48
    for pair in adjacent:
        assert len(pair.centerline_occurrences) == 2
        assert len(pair.boundary_obligations) == 4
        assert all(item.realized_point is None for item in pair.boundary_obligations)
        first, second = pair.centerline_occurrences
        assert first.over_band_id == second.under_band_id
        assert first.under_band_id == second.over_band_id
