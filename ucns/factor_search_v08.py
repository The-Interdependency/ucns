"""
ucns.factor_search_v08
=================================
Exhaustive witness-matrix recursive factorization solver.

``factor_search_v08`` preserves the legacy tuple-or-``SEQ-PRIME`` API.
``factor_search_report`` runs the same search while recording what was
supplied, what was actually searched after pruning and normalization, and
whether the finite search boundary was exhausted. The report is provenance,
not a primality certificate.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_factor_search_v08
#   module_name: factor_search_v08
#   module_kind: engine
#   summary: Exhaustive catalogue-bounded factorization with a compatibility sentinel API and a provenance-bearing search report that makes no certification claim.
#   owner: Erin Spencer
#   public_surface: factor_search_v08, factor_search_report, FactorSearchReport, payload_catalogue_fingerprint
#   internal_surface: _prepare_search_catalogues, _search_exhaustive
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_exhaustive_factor_search.py, tests/test_factor_search_provenance.py, ucns_recursive/tests/test_depth2_oracle.py
#   rollout: factor_search_v08 unchanged; factor_search_report additive
#   rollback: remove report API while retaining factor_search_v08 and _search_exhaustive
#   requires: ucns_canonical, ucns_domains, ucns_host_recovery, ucns_payload_system, ucns_witness_matrix, ucns_serialization, ucns_carrier_support_pruning
#   since: 2026-06-02
#   unresolved: negative-result certification deliberately absent
# === END MODULE_BUILD ===

import hashlib
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

from .catalogue_pruning import (
    PAYLOAD_PRUNING_RULE_NAME,
    PAYLOAD_PRUNING_RULE_VERSION,
    prune_payload_catalogue,
)
from .canonical import UCNSObject, is_multiplicative_unit, multiply
from .domains import generate_payload_catalogue
from .host_recovery import recover_face_structures, recover_host_angles
from .payload_system import (
    iter_payload_system_solutions,
    normalize_payload_catalogue,
)
from .serialization import stable_hash
from .witness_matrix import build_witness_matrix

__all__ = [
    "FactorSearchReport",
    "factor_search_report",
    "factor_search_v08",
    "payload_catalogue_fingerprint",
]

FactorPair = Tuple[UCNSObject, UCNSObject]
FactorResult = Union[FactorPair, str]
PreparedCatalogues = Tuple[
    str,
    List[Optional[UCNSObject]],
    List[Optional[UCNSObject]],
]
SEQ_PRIME = "SEQ-PRIME"


def payload_catalogue_fingerprint(
    catalogue: List[Optional[UCNSObject]],
) -> str:
    """Return an order- and duplicate-sensitive catalogue digest.

    The fingerprint identifies the exact sequence passed to this function.
    ``None`` receives an explicit unit marker; non-unit entries are represented
    by their canonical stable hashes. Length prefixes prevent concatenation
    ambiguity.
    """
    digest = hashlib.sha256()
    digest.update(b"ucns-payload-catalogue-fingerprint-v1\x00")
    digest.update(len(catalogue).to_bytes(8, "big"))
    for entry in catalogue:
        token = (
            b"unit"
            if entry is None
            else b"object:" + stable_hash(entry).encode("ascii")
        )
        digest.update(len(token).to_bytes(4, "big"))
        digest.update(token)
    return digest.hexdigest()


@dataclass(frozen=True)
class FactorSearchReport:
    """Outcome and exact search-boundary provenance.

    ``search_exhausted`` means the solver tried every host split, normalized
    payload assignment, and face assignment in the effective catalogue and
    found no factor pair. It does not establish that the supplied catalogue
    covers any mathematical domain, and it does not certify primality.

    Any exception propagates instead of producing a report. There is no
    truncation or hidden solution limit in this search path.
    """

    result_kind: str
    factors: Optional[FactorPair]
    search_exhausted: bool
    catalogue_source: str
    supplied_catalogue_size: int
    supplied_catalogue_fingerprint: str
    effective_catalogue_size: int
    effective_catalogue_fingerprint: str
    pruning_applied: bool
    pruning_rule: str
    pruning_rule_version: str
    truncation_occurred: bool


def _prepare_search_catalogues(
    P: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]],
    prune: bool,
) -> PreparedCatalogues:
    """Return source, raw supplied sequence, and exact searched sequence."""
    source = "default-canonical" if catalogue is None else "caller"
    supplied = (
        generate_payload_catalogue()
        if catalogue is None
        else list(catalogue)
    )
    pruned = (
        prune_payload_catalogue(P, supplied)
        if prune
        else list(supplied)
    )
    effective = normalize_payload_catalogue(pruned)
    return source, supplied, effective


def factor_search_report(
    P: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
    prune: bool = True,
) -> FactorSearchReport:
    """Run factor search and describe the exact finite boundary searched.

    The supplied fingerprint records the caller/default list before any
    transformation. The effective fingerprint records the exact sequence
    enumerated after optional pruning, implicit unit insertion, and structural
    deduplication. This function provides evidence only; it does not label a
    negative result certified or absolute.
    """
    source, supplied, effective = _prepare_search_catalogues(
        P, catalogue, prune
    )
    factors = _search_exhaustive(P, effective)
    exhausted = factors is None

    return FactorSearchReport(
        result_kind=SEQ_PRIME if exhausted else "FACTORS",
        factors=factors,
        search_exhausted=exhausted,
        catalogue_source=source,
        supplied_catalogue_size=len(supplied),
        supplied_catalogue_fingerprint=payload_catalogue_fingerprint(supplied),
        effective_catalogue_size=len(effective),
        effective_catalogue_fingerprint=payload_catalogue_fingerprint(effective),
        pruning_applied=prune,
        pruning_rule=PAYLOAD_PRUNING_RULE_NAME if prune else "",
        pruning_rule_version=PAYLOAD_PRUNING_RULE_VERSION if prune else "",
        truncation_occurred=False,
    )


def factor_search_v08(
    P: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
    prune: bool = True,
) -> FactorResult:
    """Return one exact non-trivial factorization, else ``SEQ-PRIME``.

    The legacy API uses the same prepared effective catalogue as
    :func:`factor_search_report` but does not compute provenance fingerprints.
    ``SEQ-PRIME`` remains catalogue-relative and carries no certification
    through this raw surface.
    """
    _, _, effective = _prepare_search_catalogues(P, catalogue, prune)
    factors = _search_exhaustive(P, effective)
    return factors if factors is not None else SEQ_PRIME


def _search_exhaustive(
    P: UCNSObject,
    catalogue: List[Optional[UCNSObject]],
) -> Optional[FactorPair]:
    """Return the first exact pair or ``None`` after finite exhaustion."""
    n = len(P.A_plus)

    # Prefer non-left-singleton splits so p=1 does not preempt larger factors.
    # Always include p=1: for n=1 it is the only split and may contain two
    # recursive non-unit factors.
    split_candidates = list(range(2, n + 1))
    split_candidates.append(1)

    for p in split_candidates:
        if n % p != 0:
            continue
        q = n // p

        A_angles, B_angles = recover_host_angles(P, p, q)
        face_options = recover_face_structures(P, p, q)
        if not face_options:
            continue

        P_payloads = [
            [P.A_plus[k * q + j][1] for j in range(q)]
            for k in range(p)
        ]

        for S_A, S_B in iter_payload_system_solutions(
            P_payloads, p, q, catalogue
        ):
            witness_matrix = build_witness_matrix(S_A, S_B, P_payloads)
            if not witness_matrix.globally_consistent():
                continue

            for A_faces, B_faces in face_options:
                A_candidate = UCNSObject(
                    P.n_dec,
                    P.n_min,
                    list(zip(A_angles, S_A)),
                    A_faces,
                )
                B_candidate = UCNSObject(
                    P.n_dec,
                    P.n_min,
                    list(zip(B_angles, S_B)),
                    B_faces,
                )
                if (
                    is_multiplicative_unit(A_candidate)
                    or is_multiplicative_unit(B_candidate)
                ):
                    continue
                if multiply(A_candidate, B_candidate) == P:
                    return A_candidate, B_candidate

    return None
