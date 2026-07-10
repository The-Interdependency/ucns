"""
ucns.factorization_result
===================================
A0-facing factorization result envelopes.

The raw solver ``factor_search_v08`` remains unchanged and returns either a
factor pair or the legacy string sentinel ``"SEQ-PRIME"``.  This module wraps
that result with canonical product identity and typed domain-status metadata
so callers do not mistake frontier-domain results for absolute primality.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_factorization_result
#   module_name: factorization_result
#   module_kind: engine
#   summary: A0-facing factorization-result envelope wrapping the raw solver output with canonical product identity and typed domain-status so SEQ-PRIME is correctly scoped.
#   owner: Erin Spencer
#   public_surface: FactorizationResultKind, FactorizationResult, factorization_result
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive/tests/test_factorization_result.py
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domain_status, ucns_factor_search_v08, ucns_serialization
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Tuple

from .canonical import UCNSObject, is_multiplicative_unit, multiply
from .catalogue_certificate import (
    COVERAGE_UNCERTIFIED,
    CatalogueCertificate,
    check_catalogue_coverage,
)
from .domain_status import DomainStatusMetadata, status_for_object
from .domains import generate_payload_catalogue
from .factor_search_v08 import FactorSearchReport, factor_search_report
from .serialization import stable_hash


class FactorizationResultKind(str, Enum):
    """Result kinds returned by the factorization envelope."""

    FACTORS = "FACTORS"
    SEQ_PRIME = "SEQ-PRIME"


@dataclass(frozen=True)
class FactorizationResult:
    """Self-describing factorization output for A0-facing consumers.

    ``negative_result_certified`` is True only when ALL of the
    certification conditions hold (codex-handoff/02): the raw result is
    ``SEQ-PRIME``; the target's domain permits a completeness claim and
    is not the unit domain; the search demonstrably exhausted its
    declared boundary; the exact input catalogue has machine-checked
    coverage for the domain (canonical-exact or a structurally verified
    superset); and any pruning applied is the named, versioned,
    coverage-preserving built-in rule.  ``uncertified_reasons`` records
    every failed condition.

    ``seq_prime_is_absolute`` is retained for compatibility as an exact
    alias of ``negative_result_certified``.  "Absolute" means *certified
    within the declared UCNS domain* — never universal mathematical
    primality.  No caller-supplied assertion can set it: coverage is
    recomputed from the exact catalogue by
    ``ucns.catalogue_certificate``.
    """

    product_hash: str
    product_domain_label: str
    product_domain_metadata: DomainStatusMetadata
    result_kind: FactorizationResultKind
    factors: Optional[Tuple[UCNSObject, UCNSObject]]
    seq_prime_is_absolute: bool
    claim_scope: str
    note: str
    # Certification metadata (codex-handoff/02).  Defaults keep older
    # positional construction working; ``factorization_result`` always
    # fills them explicitly.
    negative_result_certified: bool = False
    search_exhausted: bool = False
    catalogue_coverage_status: str = COVERAGE_UNCERTIFIED
    catalogue_fingerprint: str = ""
    catalogue_rule_version: str = ""
    catalogue_source: str = ""
    pruning_applied: bool = False
    pruning_rule: str = ""
    pruning_preserves_coverage: bool = True
    uncertified_reasons: Tuple[str, ...] = field(default=())

    @property
    def has_factors(self) -> bool:
        """Return True iff this envelope contains a recovered factor pair."""
        return self.factors is not None

    @property
    def requires_scope(self) -> bool:
        """Return True iff the result must be presented with domain scope."""
        return not self.seq_prime_is_absolute


def _certification(
    P: UCNSObject,
    metadata: DomainStatusMetadata,
    report: FactorSearchReport,
    coverage: CatalogueCertificate,
) -> Tuple[bool, Tuple[str, ...]]:
    """Evaluate every certification condition; returns (certified, reasons)."""
    reasons: List[str] = []
    if not metadata.completeness_guaranteed:
        reasons.append(
            f"domain-not-complete:{metadata.label}"
        )
    if metadata.label == "depth-0" or is_multiplicative_unit(P):
        reasons.append("unit-domain-primality-inapplicable")
    if not report.search_exhausted:
        reasons.append("search-not-exhausted")
    if not coverage.certifies_coverage:
        reasons.append(f"catalogue-coverage-uncertified:{coverage.reason}")
    if report.pruning_applied and not report.pruning_preserves_coverage:
        reasons.append(f"pruning-not-coverage-preserving:{report.pruning_rule}")
    return (not reasons, tuple(reasons))


def factorization_result(
    P: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
) -> FactorizationResult:
    """Run the exhaustive search and return a certified envelope.

    Certification is machine-derived: the coverage certificate is
    recomputed from the exact catalogue (the canonical default when
    ``catalogue is None``), and search exhaustion comes from the
    search report.  There is no parameter by which a caller can assert
    completeness.  Any search exception propagates; it is never
    converted into a negative result.
    """
    metadata = status_for_object(P)
    product_hash = stable_hash(P)
    supplied: List[Optional[UCNSObject]] = (
        generate_payload_catalogue() if catalogue is None else list(catalogue)
    )
    report = factor_search_report(P, catalogue=supplied, prune=True)
    coverage = check_catalogue_coverage(supplied, metadata.label)
    catalogue_source = (
        "default-canonical" if catalogue is None else "caller"
    )

    if report.factors is not None:
        A, B = report.factors
        note = "Recovered factors recompose to product."
        if multiply(A, B) != P:
            # This should never happen if the solver preserves its
            # soundness contract.  Keep the guard for envelope callers.
            note = "Recovered factors failed recomposition guard. Treat as invalid."
        return FactorizationResult(
            product_hash=product_hash,
            product_domain_label=metadata.label,
            product_domain_metadata=metadata,
            result_kind=FactorizationResultKind.FACTORS,
            factors=(A, B),
            seq_prime_is_absolute=False,
            claim_scope="composite-found",
            note=note,
            negative_result_certified=False,
            search_exhausted=report.search_exhausted,
            catalogue_coverage_status=coverage.coverage_status,
            catalogue_fingerprint=report.supplied_catalogue_fingerprint,
            catalogue_rule_version=coverage.rule_version,
            catalogue_source=catalogue_source,
            pruning_applied=report.pruning_applied,
            pruning_rule=report.pruning_rule,
            pruning_preserves_coverage=report.pruning_preserves_coverage,
            uncertified_reasons=("factors-found",),
        )

    certified, reasons = _certification(P, metadata, report, coverage)
    return FactorizationResult(
        product_hash=product_hash,
        product_domain_label=metadata.label,
        product_domain_metadata=metadata,
        result_kind=FactorizationResultKind.SEQ_PRIME,
        factors=None,
        seq_prime_is_absolute=certified,
        claim_scope=metadata.seq_prime_claim_scope,
        note=(
            "SEQ-PRIME certified within the declared domain: exhaustive "
            "search over a machine-checked covering catalogue."
            if certified
            else "SEQ-PRIME is catalogue-relative and NOT certified: "
            + "; ".join(reasons)
        ),
        negative_result_certified=certified,
        search_exhausted=report.search_exhausted,
        catalogue_coverage_status=coverage.coverage_status,
        catalogue_fingerprint=report.supplied_catalogue_fingerprint,
        catalogue_rule_version=coverage.rule_version,
        catalogue_source=catalogue_source,
        pruning_applied=report.pruning_applied,
        pruning_rule=report.pruning_rule,
        pruning_preserves_coverage=report.pruning_preserves_coverage,
        uncertified_reasons=reasons,
    )


__all__ = [
    "FactorizationResultKind",
    "FactorizationResult",
    "factorization_result",
]
