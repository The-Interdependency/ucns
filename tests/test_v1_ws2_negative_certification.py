"""Workstream 2 — machine-checkable negative-result certification.

No code path may set ``seq_prime_is_absolute`` /
``negative_result_certified`` from a domain label alone: certification
requires exhaustion plus machine-checked catalogue coverage bound to
the exact catalogue (codex-handoff/02).
"""

import inspect
from fractions import Fraction

from ucns import (
    UCNSObject,
    UNIT,
    FactorizationResultKind,
    catalogue_fingerprint,
    check_catalogue_coverage,
    factorization_result,
    generate_payload_catalogue,
    multiply,
    validate_certificate,
)

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
S2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
S3 = UCNSObject(
    3, 3,
    [(Fraction(0), UNIT), (Fraction(2, 3), UNIT), (Fraction(4, 3), UNIT)],
    [0, 0, 0],
)
# depth-2 oracle-class composite and its factors
D2_A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
D2_P = multiply(D2_A, S2)


def test_no_caller_completeness_assertion_exists():
    params = inspect.signature(factorization_result).parameters
    assert "catalogue_complete" not in params
    assert all(
        p.annotation is not bool and p.default is not True
        for p in params.values()
    ), "no caller boolean may assert completeness"


def test_flat_composite_empty_catalogue_not_certified_prime():
    """A flat composite searched with catalogue=[] must never produce a
    certified negative.  The exhaustive path finds the factors (flat
    payloads need only the implicit unit candidate)."""
    P = multiply(S2, S3)
    res = factorization_result(P, catalogue=[])
    assert not res.negative_result_certified
    assert not res.seq_prime_is_absolute
    if res.result_kind == FactorizationResultKind.FACTORS:
        A, B = res.factors
        assert multiply(A, B) == P
    else:
        assert res.uncertified_reasons


def test_incomplete_custom_catalogue_records_missing_coverage():
    """SEQ-PRIME under an incomplete custom catalogue is non-certified
    and names the coverage gap."""
    res = factorization_result(D2_P, catalogue=[UNIT])
    assert res.result_kind == FactorizationResultKind.SEQ_PRIME
    assert res.product_domain_label == "depth-2-oracle"
    assert not res.negative_result_certified
    assert not res.seq_prime_is_absolute
    assert any(
        reason.startswith("catalogue-coverage-uncertified")
        for reason in res.uncertified_reasons
    )
    assert res.catalogue_source == "caller"


def test_default_catalogue_certifies_oracle_domain_prime():
    """The canonical default catalogue certifies a negative only in a
    recognized complete/oracle domain, after exhaustive search."""
    prime_d2 = UCNSObject(2, 2, [(Fraction(0), S2)], [0])
    res = factorization_result(prime_d2)
    assert res.product_domain_label == "depth-2-oracle"
    assert res.result_kind == FactorizationResultKind.SEQ_PRIME
    assert res.search_exhausted
    assert res.catalogue_coverage_status == "canonical-exact"
    assert res.negative_result_certified
    assert res.seq_prime_is_absolute == res.negative_result_certified
    assert res.catalogue_source == "default-canonical"


def test_superset_catalogue_certifies():
    extra = UCNSObject(1, 1, [(Fraction(0), S2)], [0])
    catalogue = generate_payload_catalogue() + [extra]
    prime_d2 = UCNSObject(2, 2, [(Fraction(0), S2)], [0])
    res = factorization_result(prime_d2, catalogue=catalogue)
    assert res.result_kind == FactorizationResultKind.SEQ_PRIME
    assert res.catalogue_coverage_status == "canonical-superset"
    assert res.negative_result_certified


def test_certificate_binds_to_exact_catalogue():
    cat_a = generate_payload_catalogue()
    cat_b = generate_payload_catalogue()[:-1]
    cert_a = check_catalogue_coverage(cat_a, "depth-2-oracle")
    assert cert_a.certifies_coverage
    assert validate_certificate(cert_a, cat_a, "depth-2-oracle")
    assert not validate_certificate(cert_a, cat_b, "depth-2-oracle")
    assert not validate_certificate(cert_a, cat_a, "depth-1")
    assert catalogue_fingerprint(cat_a) != catalogue_fingerprint(cat_b)


def test_reorder_and_duplicate_reflected_consistently():
    cat = generate_payload_catalogue()
    reordered = list(reversed(cat))
    duplicated = cat + cat[1:2]
    for variant in (reordered, duplicated):
        cert = check_catalogue_coverage(variant, "depth-2-oracle")
        assert cert.certifies_coverage, "coverage is order/dup-insensitive"
    # ...while the audit fingerprint records the actual input:
    assert catalogue_fingerprint(cat) != catalogue_fingerprint(reordered)
    assert catalogue_fingerprint(cat) != catalogue_fingerprint(duplicated)


def test_frontier_negative_never_certified():
    d3 = UCNSObject(
        2, 2,
        [(Fraction(0), UCNSObject(2, 2, [(Fraction(0), S2)], [0])),
         (Fraction(1), UNIT)],
        [0, 0],
    )
    res = factorization_result(d3, catalogue=generate_payload_catalogue())
    assert res.product_domain_label in ("depth-3+", "depth-2-non-oracle")
    if res.result_kind == FactorizationResultKind.SEQ_PRIME:
        assert not res.negative_result_certified
        assert any(
            reason.startswith("domain-not-complete")
            for reason in res.uncertified_reasons
        )


def test_unit_domain_never_certified_prime():
    res = factorization_result(E)
    assert res.result_kind == FactorizationResultKind.SEQ_PRIME
    assert not res.negative_result_certified
    assert "unit-domain-primality-inapplicable" in res.uncertified_reasons


def test_found_factorization_stays_factors_with_evidence():
    P = multiply(S2, S3)
    res = factorization_result(P)
    assert res.result_kind == FactorizationResultKind.FACTORS
    assert not res.negative_result_certified
    A, B = res.factors
    assert multiply(A, B) == P
    assert "recompose" in res.note
