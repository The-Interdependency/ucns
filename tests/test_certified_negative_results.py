"""Adversarial tests for A0-facing negative-result certification.

A negative result is certified only from the conjunction of validated supplied-
catalogue coverage, exact report binding, exhaustive untruncated search,
recognized coverage-preserving pruning, a complete declared domain, frozen
geometric-domain membership, and a non-unit target. No individual field or
caller assertion is authority.
"""

import importlib
import inspect
from dataclasses import replace
from fractions import Fraction

from ucns import (
    COVERAGE_CANONICAL_EXACT,
    COVERAGE_CANONICAL_SUPERSET,
    COVERAGE_UNCERTIFIED,
    FactorSearchReport,
    FactorizationResultKind,
    NEGATIVE_CERTIFICATION_POLICY_VERSION,
    PAYLOAD_PRUNING_PRESERVES_COVERAGE,
    PAYLOAD_PRUNING_RULE_NAME,
    PAYLOAD_PRUNING_RULE_VERSION,
    S2,
    UCNSObject,
    UNIT,
    factor_search_report,
    factorization_result,
    generate_payload_catalogue,
    in_domain,
    multiply,
)

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
T2 = UCNSObject(1, 1, [(Fraction(0), E)], [0])


def _depth_two_oracle_prime() -> UCNSObject:
    """Return the minimal two-cell oracle-class prime witness.

    Its payload row is ``[S2, None]``. The product has length two, so the only
    host splits are ``2 x 1`` and ``1 x 2``. In either split, the payload
    equation producing the ``None`` cell can equal ``None`` only when both
    contributing payloads are ``None``. The singleton factor therefore has
    unit payload and belongs to the multiplicative unit group. No nontrivial
    factorization remains.
    """
    return UCNSObject(
        2,
        2,
        [(Fraction(0), S2), (Fraction(1), UNIT)],
        [0, 0],
    )


def _noncanonical_flat_superset_member() -> UCNSObject:
    """Return a bounded flat object outside the canonical oracle catalogue."""
    return UCNSObject(
        4,
        4,
        [(Fraction(0), UNIT), (Fraction(3, 2), UNIT)],
        [0, 0],
    )


def test_no_caller_certification_override_exists():
    params = inspect.signature(factorization_result).parameters
    assert set(params) == {"P", "catalogue"}
    assert "catalogue_complete" not in params
    assert "certified" not in params


def test_unit_sentinel_short_circuits_factor_search(monkeypatch):
    module = importlib.import_module("ucns.factorization_result")

    def fail_if_called(*_args, **_kwargs):
        raise AssertionError("UNIT sentinel reached factor search")

    monkeypatch.setattr(module, "factor_search_report", fail_if_called)
    result = module.factorization_result(UNIT)

    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert result.product_domain_label == "depth-0"
    assert result.factors is None
    assert not result.search_exhausted
    assert not result.negative_result_certified
    assert not result.seq_prime_is_absolute
    assert result.requires_scope
    assert result.claim_scope == "not-prime-unit-domain"
    assert result.uncertified_reasons == (
        "unit-domain-primality-inapplicable",
    )
    assert "no factor search was executed" in result.note


def test_flat_prime_is_certified_from_complete_default_search():
    result = factorization_result(S2)

    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert result.factors is None
    assert result.search_exhausted
    assert not result.truncation_occurred
    assert result.coverage_record_validated
    assert result.coverage_bound_to_search_report
    assert result.catalogue_coverage_status in (
        COVERAGE_CANONICAL_EXACT,
        COVERAGE_CANONICAL_SUPERSET,
    )
    assert result.pruning_preserves_coverage
    assert result.pruning_rule == PAYLOAD_PRUNING_RULE_NAME
    assert result.pruning_rule_version == PAYLOAD_PRUNING_RULE_VERSION
    assert PAYLOAD_PRUNING_PRESERVES_COVERAGE
    assert result.negative_result_certified
    assert result.seq_prime_is_absolute == result.negative_result_certified
    assert not result.requires_scope
    assert result.certification_policy_version == NEGATIVE_CERTIFICATION_POLICY_VERSION
    assert result.uncertified_reasons == ()


def test_out_of_bounds_flat_object_is_not_certified():
    product = UCNSObject(
        10,
        5,
        [
            (Fraction(2 * index, 5), UNIT)
            for index in range(5)
        ],
        [0, 0, 0, 0, 0],
    )
    assert not in_domain(product)

    result = factorization_result(product, catalogue=[UNIT])

    assert result.product_domain_label == "depth-1"
    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert result.search_exhausted
    assert result.coverage_record_validated
    assert result.coverage_bound_to_search_report
    assert not result.negative_result_certified
    assert not result.seq_prime_is_absolute
    assert result.requires_scope
    assert result.claim_scope == "catalogue-relative-uncertified"
    assert "target-outside-frozen-domain" in result.uncertified_reasons


def test_depth_two_oracle_prime_certifies_with_default_catalogue():
    product = _depth_two_oracle_prime()

    result = factorization_result(product)

    assert result.product_domain_label == "depth-2-oracle"
    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert result.factors is None
    assert result.search_exhausted
    assert result.coverage_record_validated
    assert result.coverage_bound_to_search_report
    assert result.catalogue_coverage_status == COVERAGE_CANONICAL_EXACT
    assert result.negative_result_certified
    assert result.seq_prime_is_absolute
    assert not result.requires_scope
    assert result.claim_scope == "oracle-domain-relative"
    assert result.uncertified_reasons == ()


def test_depth_two_oracle_prime_with_missing_required_member_is_uncertified():
    product = _depth_two_oracle_prime()
    incomplete = generate_payload_catalogue()
    removed = incomplete.pop()
    assert removed is not None

    result = factorization_result(product, catalogue=incomplete)

    assert result.product_domain_label == "depth-2-oracle"
    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert result.search_exhausted
    assert result.coverage_record_validated
    assert result.coverage_bound_to_search_report
    assert result.catalogue_coverage_status == COVERAGE_UNCERTIFIED
    assert not result.negative_result_certified
    assert not result.seq_prime_is_absolute
    assert result.requires_scope
    assert result.claim_scope == "catalogue-relative-uncertified"
    assert any(
        reason.startswith("catalogue-coverage-uncertified")
        for reason in result.uncertified_reasons
    )


def test_depth_two_oracle_prime_with_structural_superset_still_certifies():
    product = _depth_two_oracle_prime()
    superset = generate_payload_catalogue() + [
        _noncanonical_flat_superset_member()
    ]

    result = factorization_result(product, catalogue=superset)

    assert result.product_domain_label == "depth-2-oracle"
    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert result.search_exhausted
    assert result.coverage_record_validated
    assert result.coverage_bound_to_search_report
    assert result.catalogue_coverage_status == COVERAGE_CANONICAL_SUPERSET
    assert result.negative_result_certified
    assert result.seq_prime_is_absolute
    assert not result.requires_scope
    assert result.uncertified_reasons == ()


def test_empty_custom_catalogue_remains_uncertified_despite_exhaustion():
    result = factorization_result(S2, catalogue=[])

    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert result.search_exhausted
    assert result.catalogue_coverage_status == COVERAGE_UNCERTIFIED
    assert result.coverage_record_validated
    assert result.coverage_bound_to_search_report
    assert not result.negative_result_certified
    assert not result.seq_prime_is_absolute
    assert result.requires_scope
    assert result.claim_scope == "catalogue-relative-uncertified"
    assert any(
        reason.startswith("catalogue-coverage-uncertified")
        for reason in result.uncertified_reasons
    )


def test_multiplicative_unit_is_never_certified_prime():
    result = factorization_result(E)

    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert not result.negative_result_certified
    assert not result.seq_prime_is_absolute
    assert result.claim_scope == "not-prime-unit-domain"
    assert "unit-domain-primality-inapplicable" in result.uncertified_reasons


def test_recursive_one_cell_composite_stays_factors():
    assert multiply(T2, T2) == T2

    result = factorization_result(T2)

    assert result.result_kind == FactorizationResultKind.FACTORS
    assert result.factors is not None
    assert multiply(result.factors[0], result.factors[1]) == T2
    assert not result.negative_result_certified
    assert not result.seq_prime_is_absolute
    assert result.uncertified_reasons == ("factors-found",)


def test_frontier_negative_is_never_certified():
    depth_two_payload = UCNSObject(
        2,
        2,
        [(Fraction(0), S2), (Fraction(1), UNIT)],
        [0, 0],
    )
    product = UCNSObject(
        2,
        2,
        [(Fraction(0), depth_two_payload), (Fraction(1), UNIT)],
        [0, 0],
    )

    result = factorization_result(product, catalogue=[UNIT])

    assert result.result_kind == FactorizationResultKind.SEQ_PRIME
    assert result.product_domain_label == "depth-3+"
    assert not result.negative_result_certified
    assert any(
        reason.startswith("domain-not-complete")
        for reason in result.uncertified_reasons
    )


def _patched_negative_report(**changes) -> FactorSearchReport:
    genuine = factor_search_report(S2)
    assert genuine.result_kind == "SEQ-PRIME"
    return replace(genuine, **changes)


def test_unrecognized_pruning_rule_blocks_certification(monkeypatch):
    module = importlib.import_module("ucns.factorization_result")
    forged = _patched_negative_report(
        pruning_rule="unrecognized-rule",
        pruning_rule_version="999",
        pruning_preserves_coverage=True,
    )
    monkeypatch.setattr(module, "factor_search_report", lambda *a, **k: forged)

    result = module.factorization_result(S2)

    assert not result.negative_result_certified
    assert not result.pruning_preserves_coverage
    assert any(
        reason.startswith("pruning-not-recognized")
        for reason in result.uncertified_reasons
    )


def test_report_catalogue_binding_mismatch_blocks_certification(monkeypatch):
    module = importlib.import_module("ucns.factorization_result")
    forged = _patched_negative_report(
        supplied_catalogue_fingerprint="0" * 64,
    )
    monkeypatch.setattr(module, "factor_search_report", lambda *a, **k: forged)

    result = module.factorization_result(S2)

    assert result.coverage_record_validated
    assert not result.coverage_bound_to_search_report
    assert not result.negative_result_certified
    assert "coverage-not-bound-to-search-report" in result.uncertified_reasons


def test_truncation_or_non_exhaustion_blocks_certification(monkeypatch):
    module = importlib.import_module("ucns.factorization_result")

    truncated = _patched_negative_report(truncation_occurred=True)
    monkeypatch.setattr(module, "factor_search_report", lambda *a, **k: truncated)
    truncated_result = module.factorization_result(S2)
    assert not truncated_result.negative_result_certified
    assert "search-truncated" in truncated_result.uncertified_reasons

    incomplete = _patched_negative_report(search_exhausted=False)
    monkeypatch.setattr(module, "factor_search_report", lambda *a, **k: incomplete)
    incomplete_result = module.factorization_result(S2)
    assert not incomplete_result.negative_result_certified
    assert "search-not-exhausted" in incomplete_result.uncertified_reasons


def test_public_and_compatibility_exports():
    import ucns
    import ucns_recursive

    names = (
        "NEGATIVE_CERTIFICATION_POLICY_VERSION",
        "PAYLOAD_PRUNING_RULE_NAME",
        "PAYLOAD_PRUNING_RULE_VERSION",
        "PAYLOAD_PRUNING_PRESERVES_COVERAGE",
    )
    for module in (ucns, ucns_recursive):
        for name in names:
            assert hasattr(module, name)
