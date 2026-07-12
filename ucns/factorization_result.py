"""
ucns.factorization_result
===================================
A0-facing factorization result envelopes.

The raw solver remains catalogue-relative. This module is the only surface
that may certify a negative result, and it does so only by combining:

* a recomputed domain classification;
* membership in the frozen geometric domain;
* a complete, non-unit target domain;
* exhaustive search provenance from ``factor_search_report``;
* a fully recomputed positive catalogue-coverage record bound to that report;
* no truncation; and
* either no pruning or the exact built-in pruning rule/version whose
  coverage-preservation property is recorded by the search report.

The ``None`` unit sentinel is handled before search. No caller boolean,
caller-built coverage record, or bare domain label can certify ``SEQ-PRIME``.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_factorization_result
#   module_name: factorization_result
#   module_kind: engine
#   summary: A0-facing factorization envelope that certifies negative results only from frozen-domain membership, validated catalogue coverage, exact search-report binding, exhaustive untruncated search, recognized sound pruning, a complete declared domain, and a non-unit target.
#   owner: Erin Spencer
#   public_surface: FactorizationResultKind, FactorizationResult, NEGATIVE_CERTIFICATION_POLICY_VERSION, factorization_result
#   internal_surface: _pruning_is_recognized, _negative_certification_reasons, _claim_scope
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_certified_negative_results.py, tests/test_one_shot_catalogue.py, ucns_recursive/tests/test_factorization_result.py
#   rollout: default_enabled for A0-facing envelopes; raw factor_search_v08 remains catalogue-relative
#   rollback: retain provenance and coverage evidence but set negative_result_certified and seq_prime_is_absolute false
#   requires: ucns_canonical, ucns_domain_status, ucns_domains, ucns_factor_search_v08, ucns_catalogue_coverage, ucns_carrier_support_pruning, ucns_serialization
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, List, Optional, Tuple

from .canonical import UCNSObject, is_multiplicative_unit, multiply
from .catalogue_coverage import (
    COVERAGE_UNCERTIFIED,
    CatalogueCoverage,
    check_catalogue_coverage,
    coverage_matches_search_report as coverage_binds_to_report,
    validate_catalogue_coverage,
)
from .catalogue_pruning import (
    PAYLOAD_PRUNING_PRESERVES_COVERAGE,
    PAYLOAD_PRUNING_RULE_NAME,
    PAYLOAD_PRUNING_RULE_VERSION,
)
from .domain_status import DomainStatusMetadata, status_for_object
from .domains import generate_payload_catalogue, in_domain
from .factor_search_v08 import FactorSearchReport, factor_search_report
from .serialization import stable_hash

NEGATIVE_CERTIFICATION_POLICY_VERSION = "negative-certification-v1"


class FactorizationResultKind(str, Enum):
    """Result kinds returned by the factorization envelope."""

    FACTORS = "FACTORS"
    SEQ_PRIME = "SEQ-PRIME"


@dataclass(frozen=True)
class FactorizationResult:
    """Self-describing factorization output for A0-facing consumers.

    ``negative_result_certified`` is true only for a ``SEQ-PRIME`` result that
    satisfies every policy condition documented at module level.
    ``seq_prime_is_absolute`` is retained as a legacy alias and is set to the
    exact same value by :func:`factorization_result`. Here "absolute" means
    certified within the declared UCNS domain, not universal mathematical
    primality.

    The appended fields have defaults so older positional construction of the
    original envelope remains possible. Manually constructed records are data,
    not certification authority; callers should obtain this type from
    :func:`factorization_result`.
    """

    product_hash: str
    product_domain_label: str
    product_domain_metadata: DomainStatusMetadata
    result_kind: FactorizationResultKind
    factors: Optional[Tuple[UCNSObject, UCNSObject]]
    seq_prime_is_absolute: bool
    claim_scope: str
    note: str

    negative_result_certified: bool = False
    certification_policy_version: str = ""
    search_exhausted: bool = False
    truncation_occurred: bool = False
    catalogue_source: str = ""
    supplied_catalogue_size: int = 0
    supplied_catalogue_fingerprint: str = ""
    effective_catalogue_size: int = 0
    effective_catalogue_fingerprint: str = ""
    catalogue_coverage_status: str = COVERAGE_UNCERTIFIED
    catalogue_coverage_reason: str = ""
    catalogue_coverage_rule_version: str = ""
    required_catalogue_rule_version: str = ""
    required_catalogue_fingerprint: str = ""
    coverage_record_validated: bool = False
    coverage_bound_to_search_report: bool = False
    pruning_applied: bool = False
    pruning_rule: str = ""
    pruning_rule_version: str = ""
    pruning_preserves_coverage: bool = False
    uncertified_reasons: Tuple[str, ...] = ()

    @property
    def has_factors(self) -> bool:
        """Return True iff this envelope contains a recovered factor pair."""
        return self.factors is not None

    @property
    def requires_scope(self) -> bool:
        """Return True iff the result must be presented with explicit scope."""
        return not self.seq_prime_is_absolute


def _pruning_is_recognized(report: FactorSearchReport) -> bool:
    """Return true only for no pruning or the exact sound built-in rule."""
    if not report.pruning_applied:
        return (
            report.pruning_rule == ""
            and report.pruning_rule_version == ""
            and report.pruning_preserves_coverage
        )
    return (
        PAYLOAD_PRUNING_PRESERVES_COVERAGE
        and report.pruning_preserves_coverage
        and report.pruning_rule == PAYLOAD_PRUNING_RULE_NAME
        and report.pruning_rule_version == PAYLOAD_PRUNING_RULE_VERSION
    )


def _negative_certification_reasons(
    product: UCNSObject,
    metadata: DomainStatusMetadata,
    report: FactorSearchReport,
    coverage: CatalogueCoverage,
    coverage_validated: bool,
    coverage_bound: bool,
) -> Tuple[str, ...]:
    """Return every failed certification condition for a negative result."""
    reasons: List[str] = []

    if report.result_kind != FactorizationResultKind.SEQ_PRIME.value:
        reasons.append("search-result-not-seq-prime")
    if report.factors is not None:
        reasons.append("factors-found")
    if not metadata.completeness_guaranteed:
        reasons.append("domain-not-complete:%s" % metadata.label)
    if not in_domain(product):
        reasons.append("target-outside-frozen-domain")
    if metadata.label == "depth-0" or is_multiplicative_unit(product):
        reasons.append("unit-domain-primality-inapplicable")
    if not report.search_exhausted:
        reasons.append("search-not-exhausted")
    if report.truncation_occurred:
        reasons.append("search-truncated")
    if not coverage_validated:
        reasons.append("coverage-record-not-validated")
    if not coverage_bound:
        reasons.append("coverage-not-bound-to-search-report")
    if not coverage.covers_required_catalogue:
        reasons.append(
            "catalogue-coverage-uncertified:%s" % coverage.reason
        )
    if not _pruning_is_recognized(report):
        reasons.append(
            "pruning-not-recognized-as-coverage-preserving:%s@%s"
            % (report.pruning_rule, report.pruning_rule_version)
        )

    return tuple(reasons)


def _claim_scope(
    product: UCNSObject,
    metadata: DomainStatusMetadata,
    certified: bool,
) -> str:
    if metadata.label == "depth-0" or is_multiplicative_unit(product):
        return "not-prime-unit-domain"
    if certified or not metadata.completeness_guaranteed:
        return metadata.seq_prime_claim_scope
    return "catalogue-relative-uncertified"


def _evidence_fields(
    report: FactorSearchReport,
    coverage: CatalogueCoverage,
    coverage_validated: bool,
    coverage_bound: bool,
) -> dict:
    """Return the shared provenance fields for envelope construction."""
    return {
        "certification_policy_version": NEGATIVE_CERTIFICATION_POLICY_VERSION,
        "search_exhausted": report.search_exhausted,
        "truncation_occurred": report.truncation_occurred,
        "catalogue_source": report.catalogue_source,
        "supplied_catalogue_size": report.supplied_catalogue_size,
        "supplied_catalogue_fingerprint": report.supplied_catalogue_fingerprint,
        "effective_catalogue_size": report.effective_catalogue_size,
        "effective_catalogue_fingerprint": report.effective_catalogue_fingerprint,
        "catalogue_coverage_status": coverage.coverage_status,
        "catalogue_coverage_reason": coverage.reason,
        "catalogue_coverage_rule_version": coverage.coverage_rule_version,
        "required_catalogue_rule_version": coverage.required_catalogue_rule_version,
        "required_catalogue_fingerprint": coverage.required_catalogue_fingerprint,
        "coverage_record_validated": coverage_validated,
        "coverage_bound_to_search_report": coverage_bound,
        "pruning_applied": report.pruning_applied,
        "pruning_rule": report.pruning_rule,
        "pruning_rule_version": report.pruning_rule_version,
        "pruning_preserves_coverage": _pruning_is_recognized(report),
    }


def factorization_result(
    P: Optional[UCNSObject],
    catalogue: Optional[Iterable[Optional[UCNSObject]]] = None,
) -> FactorizationResult:
    """Run exhaustive factor search and return a machine-scoped envelope.

    The ``None`` unit sentinel is returned as an explicitly uncertified,
    non-prime unit-domain envelope without invoking factor search. For concrete
    objects there is intentionally no completeness/certification boolean
    parameter. Caller catalogues are materialized exactly once, then that same
    sequence is used for both search and coverage, so one-shot iterables cannot
    create different evidence boundaries. Search exceptions propagate; they
    never become negative results.
    """
    metadata = status_for_object(P)
    product_hash = stable_hash(P)

    if P is None:
        return FactorizationResult(
            product_hash=product_hash,
            product_domain_label=metadata.label,
            product_domain_metadata=metadata,
            result_kind=FactorizationResultKind.SEQ_PRIME,
            factors=None,
            seq_prime_is_absolute=False,
            claim_scope="not-prime-unit-domain",
            note=(
                "The UNIT sentinel is the multiplicative identity, not a "
                "primality candidate; no factor search was executed."
            ),
            negative_result_certified=False,
            certification_policy_version=NEGATIVE_CERTIFICATION_POLICY_VERSION,
            uncertified_reasons=("unit-domain-primality-inapplicable",),
        )

    supplied = (
        generate_payload_catalogue()
        if catalogue is None
        else list(catalogue)
    )
    search_catalogue = None if catalogue is None else supplied
    report = factor_search_report(P, catalogue=search_catalogue, prune=True)
    coverage = check_catalogue_coverage(supplied, metadata.label)
    coverage_validated = validate_catalogue_coverage(
        coverage, supplied, metadata.label
    )
    coverage_bound = coverage_binds_to_report(coverage, report)
    evidence = _evidence_fields(
        report, coverage, coverage_validated, coverage_bound
    )

    if report.factors is not None:
        A, B = report.factors
        if multiply(A, B) != P:
            raise RuntimeError(
                "factor-search soundness violation: recovered factors do not "
                "recompose to the requested product"
            )
        return FactorizationResult(
            product_hash=product_hash,
            product_domain_label=metadata.label,
            product_domain_metadata=metadata,
            result_kind=FactorizationResultKind.FACTORS,
            factors=(A, B),
            seq_prime_is_absolute=False,
            claim_scope="composite-found",
            note="Recovered factors recompose to product.",
            negative_result_certified=False,
            uncertified_reasons=("factors-found",),
            **evidence,
        )

    if report.result_kind != FactorizationResultKind.SEQ_PRIME.value:
        raise ValueError(
            "Unknown factor-search report result: %r" % report.result_kind
        )

    reasons = _negative_certification_reasons(
        P,
        metadata,
        report,
        coverage,
        coverage_validated,
        coverage_bound,
    )
    certified = not reasons
    return FactorizationResult(
        product_hash=product_hash,
        product_domain_label=metadata.label,
        product_domain_metadata=metadata,
        result_kind=FactorizationResultKind.SEQ_PRIME,
        factors=None,
        seq_prime_is_absolute=certified,
        claim_scope=_claim_scope(P, metadata, certified),
        note=(
            "SEQ-PRIME certified within the declared UCNS domain from "
            "validated coverage and exhaustive search."
            if certified
            else "SEQ-PRIME remains catalogue-relative and uncertified: "
            + "; ".join(reasons)
        ),
        negative_result_certified=certified,
        uncertified_reasons=reasons,
        **evidence,
    )


__all__ = [
    "FactorizationResultKind",
    "FactorizationResult",
    "NEGATIVE_CERTIFICATION_POLICY_VERSION",
    "factorization_result",
]
