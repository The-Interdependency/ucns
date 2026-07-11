"""Tests for machine-checkable supplied-catalogue coverage evidence.

Coverage is not primality certification.  These tests pin structural coverage,
exact fingerprint binding, forged-record rejection, and separation from the
pruned effective search boundary recorded by ``FactorSearchReport``.
"""

from dataclasses import replace
from fractions import Fraction

from ucns import (
    CATALOGUE_COVERAGE_RULE_VERSION,
    COVERAGE_CANONICAL_EXACT,
    COVERAGE_CANONICAL_SUPERSET,
    COVERAGE_UNCERTIFIED,
    CatalogueCoverage,
    UCNSObject,
    UNIT,
    check_catalogue_coverage,
    coverage_matches_search_report,
    factor_search_report,
    generate_payload_catalogue,
    payload_catalogue_fingerprint,
    validate_catalogue_coverage,
)

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
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
NON_CANONICAL_FLAT = UCNSObject(
    4,
    4,
    [(Fraction(0), UNIT), (Fraction(3, 2), UNIT)],
    [0, 0],
)


def test_depth_one_exact_and_superset_coverage():
    exact = check_catalogue_coverage([UNIT], "depth-1")
    superset = check_catalogue_coverage([UNIT, E], "depth-1")

    assert exact.coverage_status == COVERAGE_CANONICAL_EXACT
    assert exact.covers_required_catalogue
    assert exact.missing_count == 0
    assert exact.extra_count == 0
    assert exact.required_catalogue_size == 1

    assert superset.coverage_status == COVERAGE_CANONICAL_SUPERSET
    assert superset.covers_required_catalogue
    assert superset.missing_count == 0
    assert superset.extra_count == 1


def test_depth_two_canonical_catalogue_is_exact():
    catalogue = generate_payload_catalogue()
    coverage = check_catalogue_coverage(catalogue, "depth-2-oracle")

    assert coverage.coverage_rule_version == CATALOGUE_COVERAGE_RULE_VERSION
    assert coverage.coverage_status == COVERAGE_CANONICAL_EXACT
    assert coverage.covers_required_catalogue
    assert coverage.catalogue_fingerprint == payload_catalogue_fingerprint(catalogue)
    assert coverage.required_catalogue_fingerprint == payload_catalogue_fingerprint(
        generate_payload_catalogue()
    )
    assert coverage.missing_count == 0
    assert coverage.extra_count == 0


def test_depth_two_superset_and_missing_member():
    canonical = generate_payload_catalogue()
    superset = canonical + [NON_CANONICAL_FLAT]
    incomplete = canonical[:-1]

    superset_coverage = check_catalogue_coverage(
        superset, "depth-2-oracle"
    )
    incomplete_coverage = check_catalogue_coverage(
        incomplete, "depth-2-oracle"
    )

    assert superset_coverage.coverage_status == COVERAGE_CANONICAL_SUPERSET
    assert superset_coverage.covers_required_catalogue
    assert superset_coverage.extra_count == 1

    assert incomplete_coverage.coverage_status == COVERAGE_UNCERTIFIED
    assert not incomplete_coverage.covers_required_catalogue
    assert incomplete_coverage.missing_count == 1
    assert "missing 1 canonical member" in incomplete_coverage.reason


def test_order_and_duplicates_change_binding_not_structural_coverage():
    canonical = generate_payload_catalogue()
    reordered = list(reversed(canonical))
    duplicated = canonical + canonical[1:2]

    base = check_catalogue_coverage(canonical, "depth-2-oracle")
    reorder_record = check_catalogue_coverage(
        reordered, "depth-2-oracle"
    )
    duplicate_record = check_catalogue_coverage(
        duplicated, "depth-2-oracle"
    )

    assert base.coverage_status == COVERAGE_CANONICAL_EXACT
    assert reorder_record.coverage_status == COVERAGE_CANONICAL_EXACT
    assert duplicate_record.coverage_status == COVERAGE_CANONICAL_EXACT

    assert base.catalogue_fingerprint != reorder_record.catalogue_fingerprint
    assert base.catalogue_fingerprint != duplicate_record.catalogue_fingerprint
    assert base.catalogue_size != duplicate_record.catalogue_size


def test_unit_frontier_and_unknown_domains_are_uncertified():
    for label in (
        "depth-0",
        "depth-2-non-oracle",
        "depth-3+",
        "unknown-domain",
    ):
        coverage = check_catalogue_coverage(
            generate_payload_catalogue(), label
        )
        assert coverage.coverage_status == COVERAGE_UNCERTIFIED
        assert not coverage.covers_required_catalogue
        assert coverage.required_catalogue_rule_version == ""
        assert coverage.required_catalogue_fingerprint == ""


def test_full_recomputation_rejects_forged_status():
    incomplete = generate_payload_catalogue()[:-1]
    genuine = check_catalogue_coverage(
        incomplete, "depth-2-oracle"
    )
    forged = replace(
        genuine,
        coverage_status=COVERAGE_CANONICAL_EXACT,
        missing_count=0,
        reason="forged",
    )

    assert not genuine.covers_required_catalogue
    assert forged.covers_required_catalogue
    assert validate_catalogue_coverage(
        genuine, incomplete, "depth-2-oracle"
    )
    assert not validate_catalogue_coverage(
        forged, incomplete, "depth-2-oracle"
    )


def test_record_is_bound_to_domain_rule_and_exact_catalogue():
    catalogue = generate_payload_catalogue()
    record = check_catalogue_coverage(catalogue, "depth-2-oracle")

    assert validate_catalogue_coverage(
        record, catalogue, "depth-2-oracle"
    )
    assert not validate_catalogue_coverage(
        record, list(reversed(catalogue)), "depth-2-oracle"
    )
    assert not validate_catalogue_coverage(record, catalogue, "depth-1")

    catalogue.pop()
    assert not validate_catalogue_coverage(
        record, catalogue, "depth-2-oracle"
    )


def test_coverage_binds_to_report_supplied_not_effective_catalogue():
    supplied = [UNIT, E, S3]
    report = factor_search_report(S2, catalogue=supplied, prune=True)
    coverage = check_catalogue_coverage(supplied, "depth-1")

    assert coverage.coverage_status == COVERAGE_CANONICAL_SUPERSET
    assert coverage_matches_search_report(coverage, report)
    assert coverage.catalogue_fingerprint == report.supplied_catalogue_fingerprint
    assert coverage.catalogue_size == report.supplied_catalogue_size

    # Carrier-3 S3 is pruned for the flat target, so the actual searched
    # boundary differs. PR #102 records that boundary separately.
    assert report.effective_catalogue_size < report.supplied_catalogue_size
    assert (
        report.effective_catalogue_fingerprint
        != report.supplied_catalogue_fingerprint
    )

    reordered = check_catalogue_coverage(
        list(reversed(supplied)), "depth-1"
    )
    assert reordered.covers_required_catalogue
    assert not coverage_matches_search_report(reordered, report)


def test_coverage_record_contains_no_negative_certification_claim():
    coverage = check_catalogue_coverage([UNIT], "depth-1")

    assert isinstance(coverage, CatalogueCoverage)
    assert not hasattr(coverage, "negative_result_certified")
    assert not hasattr(coverage, "seq_prime_is_absolute")
    assert not hasattr(coverage, "search_exhausted")


def test_public_and_compatibility_exports():
    import ucns
    import ucns_recursive

    names = (
        "CatalogueCoverage",
        "CATALOGUE_COVERAGE_RULE_VERSION",
        "COVERAGE_CANONICAL_EXACT",
        "COVERAGE_CANONICAL_SUPERSET",
        "COVERAGE_UNCERTIFIED",
        "check_catalogue_coverage",
        "validate_catalogue_coverage",
        "coverage_matches_search_report",
    )
    for module in (ucns, ucns_recursive):
        for name in names:
            assert hasattr(module, name)
