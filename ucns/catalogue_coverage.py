"""
ucns.catalogue_coverage
=======================
Machine-checkable payload-catalogue coverage records.

PR #102 records two distinct catalogue boundaries for factor search:

* the raw catalogue supplied by the caller or default builder; and
* the effective catalogue actually searched after optional pruning,
  implicit-unit insertion, and structural deduplication.

Coverage is a property of the *supplied* catalogue.  The effective search
boundary remains separately identified by ``FactorSearchReport``.  A later
negative-result policy may combine supplied coverage, effective-search
exhaustion, and a recognized coverage-preserving pruning rule.  This module
performs only the coverage check; it does not certify ``SEQ-PRIME`` or call a
negative result absolute.

Coverage statuses are structural-set statements.  Catalogue order and
repeated entries do not change coverage, but they do change the exact
``catalogue_fingerprint`` carried by the record.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_catalogue_coverage
#   module_name: catalogue_coverage
#   module_kind: engine
#   summary: Recomputable catalogue-coverage records bound to an exact supplied catalogue fingerprint, domain label, and required catalogue rule version; makes no primality-certification claim.
#   owner: Erin Spencer
#   public_surface: CatalogueCoverage, CATALOGUE_COVERAGE_RULE_VERSION, COVERAGE_CANONICAL_EXACT, COVERAGE_CANONICAL_SUPERSET, COVERAGE_UNCERTIFIED, check_catalogue_coverage, validate_catalogue_coverage, coverage_matches_search_report
#   internal_surface: _required_catalogue_for_domain, _structural_tokens
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_catalogue_coverage.py
#   rollout: additive evidence surface; no FactorizationResult integration
#   rollback: remove module and public re-exports
#   requires: ucns_domains, ucns_factor_search_v08, ucns_serialization
#   since: 2026-07-11
#   unresolved: negative-result certification deliberately remains separate
# === END MODULE_BUILD ===

from dataclasses import dataclass
from typing import List, Optional, Set, Tuple

from .canonical import UCNSObject
from .domains import ORACLE_CATALOGUE_RULE_VERSION, generate_payload_catalogue
from .factor_search_v08 import FactorSearchReport, payload_catalogue_fingerprint
from .serialization import stable_hash

__all__ = [
    "CatalogueCoverage",
    "CATALOGUE_COVERAGE_RULE_VERSION",
    "COVERAGE_CANONICAL_EXACT",
    "COVERAGE_CANONICAL_SUPERSET",
    "COVERAGE_UNCERTIFIED",
    "check_catalogue_coverage",
    "validate_catalogue_coverage",
    "coverage_matches_search_report",
]

CATALOGUE_COVERAGE_RULE_VERSION = "catalogue-coverage-v1"
DEPTH1_PAYLOAD_RULE_VERSION = "flat-unit-payload-v1"

COVERAGE_CANONICAL_EXACT = "canonical-exact"
COVERAGE_CANONICAL_SUPERSET = "canonical-superset"
COVERAGE_UNCERTIFIED = "uncertified"

_UNIT_TOKEN = "unit"


@dataclass(frozen=True)
class CatalogueCoverage:
    """Recomputable coverage evidence for one supplied catalogue and domain.

    ``covers_required_catalogue`` means only that the supplied structural set
    contains the release's canonical required payload set for ``domain_label``.
    It says nothing about search exhaustion, pruning validity, target
    non-triviality, or primality.

    Do not trust a caller-constructed instance.  Use
    :func:`validate_catalogue_coverage`, which recomputes the complete expected
    record and requires exact dataclass equality.
    """

    domain_label: str
    coverage_rule_version: str
    required_catalogue_rule_version: str
    catalogue_size: int
    catalogue_fingerprint: str
    required_catalogue_size: int
    required_catalogue_fingerprint: str
    supplied_unique_size: int
    coverage_status: str
    missing_count: int
    extra_count: int
    reason: str

    @property
    def covers_required_catalogue(self) -> bool:
        return self.coverage_status in (
            COVERAGE_CANONICAL_EXACT,
            COVERAGE_CANONICAL_SUPERSET,
        )


def _structural_tokens(
    catalogue: List[Optional[UCNSObject]],
) -> Set[str]:
    """Return equality-aligned structural tokens for coverage comparison."""
    tokens: Set[str] = set()
    for entry in catalogue:
        if entry is None:
            tokens.add(_UNIT_TOKEN)
        else:
            tokens.add("object:" + stable_hash(entry))
    return tokens


def _required_catalogue_for_domain(
    domain_label: str,
) -> Optional[Tuple[List[Optional[UCNSObject]], str]]:
    """Return (required catalogue, rule version), or ``None`` if unsupported.

    * ``depth-1`` factors carry unit payloads only, so ``[None]`` is the
      canonical required payload set.
    * ``depth-2-oracle`` uses the exact canonical oracle catalogue established
      by PR #103.
    * the unit domain and frontier/unknown domains intentionally have no
      certifiable required catalogue in this release.
    """
    if domain_label == "depth-1":
        return [None], DEPTH1_PAYLOAD_RULE_VERSION
    if domain_label == "depth-2-oracle":
        return generate_payload_catalogue(), ORACLE_CATALOGUE_RULE_VERSION
    return None


def check_catalogue_coverage(
    catalogue: List[Optional[UCNSObject]],
    domain_label: str,
) -> CatalogueCoverage:
    """Recompute structural coverage for the exact supplied catalogue.

    The fingerprint is order- and duplicate-sensitive and therefore binds to
    the exact supplied sequence.  Coverage itself is structural-set based:
    order and duplicate entries neither add nor remove mathematical coverage.
    """
    supplied = list(catalogue)
    supplied_fingerprint = payload_catalogue_fingerprint(supplied)
    supplied_tokens = _structural_tokens(supplied)
    required_spec = _required_catalogue_for_domain(domain_label)

    if required_spec is None:
        return CatalogueCoverage(
            domain_label=domain_label,
            coverage_rule_version=CATALOGUE_COVERAGE_RULE_VERSION,
            required_catalogue_rule_version="",
            catalogue_size=len(supplied),
            catalogue_fingerprint=supplied_fingerprint,
            required_catalogue_size=0,
            required_catalogue_fingerprint="",
            supplied_unique_size=len(supplied_tokens),
            coverage_status=COVERAGE_UNCERTIFIED,
            missing_count=0,
            extra_count=len(supplied_tokens),
            reason=(
                "domain %r has no canonical required payload catalogue in "
                "this release" % domain_label
            ),
        )

    required, required_rule_version = required_spec
    required_tokens = _structural_tokens(required)
    missing = required_tokens - supplied_tokens
    extra = supplied_tokens - required_tokens

    if missing:
        status = COVERAGE_UNCERTIFIED
        reason = (
            "supplied catalogue is missing %d canonical member(s) required "
            "for %r" % (len(missing), domain_label)
        )
    elif extra:
        status = COVERAGE_CANONICAL_SUPERSET
        reason = "structural superset of the canonical required catalogue"
    else:
        status = COVERAGE_CANONICAL_EXACT
        reason = "structural set equality with the canonical required catalogue"

    return CatalogueCoverage(
        domain_label=domain_label,
        coverage_rule_version=CATALOGUE_COVERAGE_RULE_VERSION,
        required_catalogue_rule_version=required_rule_version,
        catalogue_size=len(supplied),
        catalogue_fingerprint=supplied_fingerprint,
        required_catalogue_size=len(required),
        required_catalogue_fingerprint=payload_catalogue_fingerprint(required),
        supplied_unique_size=len(supplied_tokens),
        coverage_status=status,
        missing_count=len(missing),
        extra_count=len(extra),
        reason=reason,
    )


def validate_catalogue_coverage(
    coverage: CatalogueCoverage,
    catalogue: List[Optional[UCNSObject]],
    domain_label: str,
) -> bool:
    """Return True only when full recomputation exactly matches ``coverage``.

    Checking only a fingerprint, rule version, or caller-provided status is not
    sufficient.  Exact record equality prevents a forged
    ``canonical-exact``/``canonical-superset`` status from passing validation.
    """
    return coverage == check_catalogue_coverage(catalogue, domain_label)


def coverage_matches_search_report(
    coverage: CatalogueCoverage,
    report: FactorSearchReport,
) -> bool:
    """Return True iff coverage is bound to the report's supplied catalogue.

    This deliberately compares the supplied catalogue boundary, not the
    pruned effective boundary.  PR #102 records the effective search
    fingerprint and pruning metadata separately; a later policy must evaluate
    those facts in addition to this binding.
    """
    return (
        coverage.catalogue_size == report.supplied_catalogue_size
        and coverage.catalogue_fingerprint
        == report.supplied_catalogue_fingerprint
    )
