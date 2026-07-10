"""
ucns.catalogue_certificate
==========================
Machine-checked catalogue coverage for negative-result certification.

A ``SEQ-PRIME`` from ``factor_search_v08`` is *catalogue-relative*: the
search exhausts the supplied candidate payloads and nothing more.  An
empty or incomplete caller catalogue must therefore never turn into an
"absolute" prime claim (codex-handoff/02).  This module provides the
machine check that binds a certification to the **exact** catalogue
that was searched:

- :func:`catalogue_fingerprint` — deterministic digest over the ordered
  canonical hashes of the supplied catalogue (explicit unit markers),
  preserving the actual search input including order and duplicates;
- :class:`CatalogueCertificate` — domain label, catalogue rule version,
  exact fingerprint, coverage status, and validation reason;
- :func:`check_catalogue_coverage` — structural containment check of
  the canonical required catalogue for a domain label inside the
  supplied catalogue (order-insensitive, duplication-insensitive);
- :func:`validate_certificate` — rejects a certificate reused against a
  different catalogue, domain, or rule version.

Caller-supplied booleans such as ``catalogue_complete=True`` are
deliberately unsupported: coverage is recomputed from the catalogue
itself, never asserted.

Coverage statuses:

``canonical-exact``     structural set equality with the canonical
                        required catalogue for the domain
``canonical-superset``  structural superset of the canonical required
                        catalogue
``uncertified``         anything else, including every domain for which
                        the repository currently permits no
                        completeness claim
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_catalogue_certificate
#   module_name: catalogue_certificate
#   module_kind: engine
#   summary: Machine-checked catalogue coverage certificates binding negative-result certification to the exact searched catalogue, domain label, and catalogue rule version.
#   owner: Erin Spencer
#   public_surface: CatalogueCertificate, catalogue_fingerprint, check_catalogue_coverage, validate_certificate, COVERAGE_CANONICAL_EXACT, COVERAGE_CANONICAL_SUPERSET, COVERAGE_UNCERTIFIED
#   internal_surface: _required_catalogue_for_label, _structural_set
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_v1_ws2_negative_certification
#   rollout: default_enabled; consumed by ucns.factorization_result
#   rollback: remove module; factorization_result falls back to never-certified
#   requires: ucns_canonical, ucns_domains, ucns_serialization
#   since: 2026-07-10
#   unresolved: none
# === END MODULE_BUILD ===

import hashlib
from dataclasses import dataclass
from typing import List, Optional, Tuple

from .canonical import UCNSObject
from .domains import ORACLE_CATALOGUE_RULE_VERSION, generate_payload_catalogue
from .serialization import stable_hash

__all__ = [
    "CatalogueCertificate",
    "catalogue_fingerprint",
    "check_catalogue_coverage",
    "validate_certificate",
    "COVERAGE_CANONICAL_EXACT",
    "COVERAGE_CANONICAL_SUPERSET",
    "COVERAGE_UNCERTIFIED",
]

COVERAGE_CANONICAL_EXACT = "canonical-exact"
COVERAGE_CANONICAL_SUPERSET = "canonical-superset"
COVERAGE_UNCERTIFIED = "uncertified"

_UNIT_MARKER = b"UNIT\x00"


def catalogue_fingerprint(
    catalogue: List[Optional[UCNSObject]],
) -> str:
    """Deterministic digest binding to the exact supplied catalogue.

    The digest covers the ordered sequence of canonical object hashes
    with explicit unit markers, so order and duplication are part of
    the audit fingerprint even though coverage checking itself is
    order-insensitive.
    """
    digest = hashlib.sha256()
    digest.update(b"ucns-catalogue-fingerprint-v1\x00")
    for entry in catalogue:
        if entry is None:
            digest.update(_UNIT_MARKER)
        else:
            digest.update(stable_hash(entry).encode("ascii"))
            digest.update(b"\x00")
    return digest.hexdigest()


@dataclass(frozen=True)
class CatalogueCertificate:
    """Machine-checked coverage result for one (catalogue, domain) pair."""

    domain_label: str
    rule_version: str
    fingerprint: str
    coverage_status: str
    reason: str

    @property
    def certifies_coverage(self) -> bool:
        return self.coverage_status in (
            COVERAGE_CANONICAL_EXACT,
            COVERAGE_CANONICAL_SUPERSET,
        )


def _structural_set(
    catalogue: List[Optional[UCNSObject]],
) -> Tuple[bool, List[UCNSObject]]:
    """(unit present, structurally deduplicated non-unit entries)."""
    has_unit = False
    unique: List[UCNSObject] = []
    for entry in catalogue:
        if entry is None:
            has_unit = True
            continue
        if any(entry == seen for seen in unique):
            continue
        unique.append(entry)
    return has_unit, unique


def _required_catalogue_for_label(
    domain_label: str,
) -> Optional[List[Optional[UCNSObject]]]:
    """Canonical required catalogue for a domain label, or ``None`` when
    the repository permits no completeness claim for that label.

    - ``depth-1``: flat factors carry only unit payloads, so the
      required payload catalogue is exactly ``[None]``.
    - ``depth-2-oracle``: the canonical oracle-atom catalogue.
    - everything else (``depth-0`` unit domain, frontier labels,
      unknown labels): no certifiable catalogue exists.
    """
    if domain_label == "depth-1":
        return [None]
    if domain_label == "depth-2-oracle":
        return generate_payload_catalogue()
    return None


def check_catalogue_coverage(
    catalogue: List[Optional[UCNSObject]],
    domain_label: str,
) -> CatalogueCertificate:
    """Machine-check whether *catalogue* covers *domain_label*.

    Coverage is recomputed structurally from the catalogue contents;
    no caller assertion is consulted.
    """
    fingerprint = catalogue_fingerprint(catalogue)
    required = _required_catalogue_for_label(domain_label)
    if required is None:
        return CatalogueCertificate(
            domain_label=domain_label,
            rule_version=ORACLE_CATALOGUE_RULE_VERSION,
            fingerprint=fingerprint,
            coverage_status=COVERAGE_UNCERTIFIED,
            reason=(
                f"domain {domain_label!r} has no certifiable canonical "
                "catalogue in this release"
            ),
        )

    req_unit, req_objects = _structural_set(required)
    got_unit, got_objects = _structural_set(catalogue)

    if req_unit and not got_unit:
        return CatalogueCertificate(
            domain_label=domain_label,
            rule_version=ORACLE_CATALOGUE_RULE_VERSION,
            fingerprint=fingerprint,
            coverage_status=COVERAGE_UNCERTIFIED,
            reason="catalogue is missing the unit payload",
        )

    missing = [
        obj for obj in req_objects
        if not any(obj == got for got in got_objects)
    ]
    if missing:
        return CatalogueCertificate(
            domain_label=domain_label,
            rule_version=ORACLE_CATALOGUE_RULE_VERSION,
            fingerprint=fingerprint,
            coverage_status=COVERAGE_UNCERTIFIED,
            reason=(
                f"catalogue is missing {len(missing)} canonical "
                f"member(s) required for {domain_label!r}"
            ),
        )

    extra = [
        obj for obj in got_objects
        if not any(obj == req for req in req_objects)
    ]
    exact = not extra and got_unit == req_unit
    return CatalogueCertificate(
        domain_label=domain_label,
        rule_version=ORACLE_CATALOGUE_RULE_VERSION,
        fingerprint=fingerprint,
        coverage_status=(
            COVERAGE_CANONICAL_EXACT if exact else COVERAGE_CANONICAL_SUPERSET
        ),
        reason=(
            "structural set equality with the canonical catalogue"
            if exact
            else "structural superset of the canonical catalogue"
        ),
    )


def validate_certificate(
    certificate: CatalogueCertificate,
    catalogue: List[Optional[UCNSObject]],
    domain_label: str,
) -> bool:
    """True iff *certificate* binds to exactly this catalogue, domain,
    and catalogue rule version.  A certificate produced for catalogue A
    is rejected when presented with catalogue B."""
    if certificate.domain_label != domain_label:
        return False
    if certificate.rule_version != ORACLE_CATALOGUE_RULE_VERSION:
        return False
    return certificate.fingerprint == catalogue_fingerprint(catalogue)
