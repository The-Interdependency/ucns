"""
ucns.evidence
=============
Downstream proof-status metadata envelope.

Sibling-repository consumers (METAPAT adapters, EDCM geometry, A0
integrations) need to report what UCNS evidence they actually hold
without flattening it into a boolean. This module gives them one small
vocabulary object, :class:`UCNSEvidence`, that distinguishes:

* object construction succeeded;
* a declared finite search boundary was exhausted;
* catalogue coverage was validated;
* a negative result was certified within a declared domain;
* which theorem-layer status vocabulary applies
  (``DEFENDED`` / ``IMPLEMENTED`` / ``TEST_BACKED`` / ``ORACLE_COMPLETE``
  / ``FRONTIER`` / ``EXPERIMENTAL``);
* that no proof status is attached at all.

Promotion rules (non-negotiable): a bare domain label, an object hash,
an import success, a bridge round trip, or geometry equivalence never
promotes evidence. Search and certification facts enter only through the
evidence-bearing :class:`ucns.factorization_result.FactorizationResult`
envelope; construction and bridge imports produce construction-only
evidence with no proof status attached.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_evidence
#   module_name: evidence
#   module_kind: adapter
#   summary: Non-boolean downstream evidence envelope distinguishing construction success, search exhaustion, validated coverage, certified domain-relative negatives, theorem-layer status vocabulary, and absence of proof status.
#   owner: Erin Spencer
#   public_surface: UCNSEvidence, no_proof_status, evidence_from_construction, evidence_from_bridge_import, evidence_from_factorization_result
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_stack_contract_suite.py, tests/test_bridge_certification_boundary.py
#   rollout: default_enabled additive public API
#   rollback: remove module and its re-exports; consumers fall back to reading FactorizationResult directly
#   requires: ucns_canonical, ucns_factorization_result, ucns_domain_status, ucns_bridge
#   since: 2026-07-12
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass
from typing import Optional, Tuple

from .bridge import BridgeImport
from .canonical import UCNSObject
from .catalogue_coverage import (
    COVERAGE_CANONICAL_EXACT,
    COVERAGE_CANONICAL_SUPERSET,
)
from .domain_status import status_for_object
from .factorization_result import FactorizationResult

__all__ = [
    "UCNSEvidence",
    "no_proof_status",
    "evidence_from_construction",
    "evidence_from_bridge_import",
    "evidence_from_factorization_result",
]


@dataclass(frozen=True)
class UCNSEvidence:
    """What a consumer actually knows about a UCNS object or result.

    Every field defaults to "no evidence". ``proof_status_attached`` is
    True only when theorem-layer vocabulary genuinely applies (it comes
    from an evidence-bearing factorization envelope, never from
    construction or bridge metadata). Manually constructed instances are
    data, not authority; obtain instances from the module constructors.
    """

    source: str
    construction_succeeded: bool = False
    search_boundary_exhausted: bool = False
    search_boundary_fingerprint: str = ""
    catalogue_coverage_validated: bool = False
    negative_result_certified: bool = False
    certified_domain_label: str = ""
    domain_label: str = ""
    theorem_layer_statuses: Tuple[str, ...] = ()
    proof_status_attached: bool = False
    note: str = ""

    @property
    def has_any_proof_evidence(self) -> bool:
        """True iff anything beyond bare construction is in evidence."""
        return (
            self.search_boundary_exhausted
            or self.catalogue_coverage_validated
            or self.negative_result_certified
            or self.proof_status_attached
        )


def no_proof_status(note: str = "") -> UCNSEvidence:
    """Return the explicit absence-of-proof-status envelope."""
    return UCNSEvidence(source="none", note=note)


def evidence_from_construction(obj: Optional[UCNSObject]) -> UCNSEvidence:
    """Evidence carried by a successfully constructed object: only that.

    The domain label is reported for routing, but no theorem status is
    attached — construction success is not a proof event.
    """
    return UCNSEvidence(
        source="construction",
        construction_succeeded=True,
        domain_label=status_for_object(obj).label,
        note="Construction success only; no proof status attached.",
    )


def evidence_from_bridge_import(imported: BridgeImport) -> UCNSEvidence:
    """Evidence carried by a successful bridge import: construction only.

    Bridge provenance and canon tags are deliberately not consulted:
    they cannot assert search provenance, catalogue coverage, theorem
    status, or negative certification.
    """
    evidence = evidence_from_construction(imported.obj)
    return UCNSEvidence(
        source="bridge-import",
        construction_succeeded=True,
        domain_label=evidence.domain_label,
        note=(
            "Bridge import success only; provenance tags carry no proof "
            "status and were not consulted."
        ),
    )


def evidence_from_factorization_result(
    result: FactorizationResult,
) -> UCNSEvidence:
    """Map the evidence-bearing factorization envelope into the vocabulary.

    This is the only constructor that can attach search-exhaustion,
    coverage, certification, or theorem-layer status facts, and it only
    relays what the envelope itself established. Envelopes where no
    search actually ran (the unit-sentinel short-circuit: no factors, no
    exhausted boundary, no certification) attach NO proof status —
    "not a primality candidate" is an absence, not evidence.
    """
    certified = bool(result.negative_result_certified)
    search_ran = bool(result.search_exhausted or result.factors is not None)
    attach_status = search_ran or certified
    covering_status = result.catalogue_coverage_status in (
        COVERAGE_CANONICAL_EXACT,
        COVERAGE_CANONICAL_SUPERSET,
    )
    return UCNSEvidence(
        source="factorization-result",
        construction_succeeded=True,
        search_boundary_exhausted=bool(result.search_exhausted),
        search_boundary_fingerprint=result.effective_catalogue_fingerprint,
        catalogue_coverage_validated=bool(
            result.coverage_record_validated
            and result.coverage_bound_to_search_report
            and covering_status
        ),
        negative_result_certified=certified,
        certified_domain_label=(
            result.product_domain_label if certified else ""
        ),
        domain_label=result.product_domain_label,
        theorem_layer_statuses=(
            tuple(
                status.value
                for status in result.product_domain_metadata.statuses
            )
            if attach_status
            else ()
        ),
        proof_status_attached=attach_status,
        note=result.note,
    )
