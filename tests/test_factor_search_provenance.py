"""Tests for exact factor-search boundary provenance.

The report records what was supplied and what was actually searched. It does
not certify negative results or call them absolute.
"""

import importlib
from fractions import Fraction

import pytest

from ucns import (
    FactorSearchReport,
    UCNSObject,
    UNIT,
    factor_search_report,
    factor_search_v08,
    multiply,
    payload_catalogue_fingerprint,
)
from ucns.payload_system import normalize_payload_catalogue

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
T2 = UCNSObject(1, 1, [(Fraction(0), E)], [0])
S2 = UCNSObject(
    2,
    2,
    [(Fraction(0), UNIT), (Fraction(1), UNIT)],
    [0, 0],
)
S3 = UCNSObject(
    3,
    3,
    [
        (Fraction(0), UNIT),
        (Fraction(2, 3), UNIT),
        (Fraction(4, 3), UNIT),
    ],
    [0, 0, 0],
)


def test_empty_supplied_catalogue_records_implicit_unit_search():
    report = factor_search_report(S2, catalogue=[], prune=False)

    assert isinstance(report, FactorSearchReport)
    assert report.catalogue_source == "caller"
    assert report.supplied_catalogue_size == 0
    assert report.supplied_catalogue_fingerprint == payload_catalogue_fingerprint([])
    assert report.effective_catalogue_size == 1
    assert report.effective_catalogue_fingerprint == payload_catalogue_fingerprint([UNIT])
    assert report.search_exhausted
    assert report.result_kind == "SEQ-PRIME"
    assert not report.truncation_occurred


def test_supplied_fingerprint_preserves_order_and_duplicates():
    base = [UNIT, E]
    reordered = [E, UNIT]
    duplicated = [UNIT, E, E]

    assert payload_catalogue_fingerprint(base) != payload_catalogue_fingerprint(reordered)
    assert payload_catalogue_fingerprint(base) != payload_catalogue_fingerprint(duplicated)


def test_effective_fingerprint_matches_normalized_sequence():
    first = factor_search_report(S2, catalogue=[E, UNIT, E], prune=False)
    second = factor_search_report(S2, catalogue=[UNIT, E], prune=False)

    expected = normalize_payload_catalogue([E, UNIT, E])
    assert expected == [UNIT, E]
    assert first.supplied_catalogue_fingerprint != second.supplied_catalogue_fingerprint
    assert first.effective_catalogue_size == second.effective_catalogue_size == 2
    assert first.effective_catalogue_fingerprint == payload_catalogue_fingerprint(expected)
    assert first.effective_catalogue_fingerprint == second.effective_catalogue_fingerprint


def test_pruning_provenance_names_rule_and_records_post_prune_search():
    report = factor_search_report(S2, catalogue=[UNIT, E, S3], prune=True)

    # Flat S2 has empty payload support. Carrier-1 E legitimately survives;
    # carrier-3 S3 is removed. The searched sequence is therefore [unit, E].
    assert report.pruning_applied
    assert report.pruning_rule == "carrier-lcm-payload-support"
    assert report.pruning_rule_version == "1"
    assert report.supplied_catalogue_size == 3
    assert report.effective_catalogue_size == 2
    assert report.effective_catalogue_fingerprint == payload_catalogue_fingerprint([UNIT, E])


def test_factor_report_and_legacy_wrapper_use_same_search():
    report = factor_search_report(T2, catalogue=[UNIT, E], prune=False)
    legacy = factor_search_v08(T2, catalogue=[UNIT, E], prune=False)

    assert report.result_kind == "FACTORS"
    assert report.factors is not None
    assert not report.search_exhausted
    assert not report.truncation_occurred
    assert isinstance(legacy, tuple)
    assert multiply(report.factors[0], report.factors[1]) == T2
    assert multiply(legacy[0], legacy[1]) == T2
    assert report.factors[0] == legacy[0]
    assert report.factors[1] == legacy[1]


def test_negative_report_means_exhaustion_not_certification():
    report = factor_search_report(S2, catalogue=[UNIT], prune=False)

    assert report.result_kind == "SEQ-PRIME"
    assert report.factors is None
    assert report.search_exhausted
    assert not report.truncation_occurred
    assert not hasattr(report, "negative_result_certified")
    assert not hasattr(report, "seq_prime_is_absolute")
    assert not hasattr(report, "catalogue_coverage_status")


def test_search_exceptions_propagate_without_report(monkeypatch):
    module = importlib.import_module("ucns.factor_search_v08")

    def boom(_product, _catalogue):
        raise RuntimeError("search failed")

    monkeypatch.setattr(module, "_search_exhaustive", boom)
    with pytest.raises(RuntimeError, match="search failed"):
        module.factor_search_report(S2, catalogue=[UNIT], prune=False)


def test_public_and_compatibility_exports():
    import ucns
    import ucns_recursive

    for name in (
        "FactorSearchReport",
        "factor_search_report",
        "payload_catalogue_fingerprint",
    ):
        assert hasattr(ucns, name)
        assert hasattr(ucns_recursive, name)
