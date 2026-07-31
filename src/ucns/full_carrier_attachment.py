# === MODULE_BUILD ===
# id: edcm_full_carrier_attachment_evidence
#   module_name: full_carrier_attachment
#   module_kind: experiment
#   summary: records exact analytic certificates for the declared full non-null affine carrier and quotient seam while retaining the bounded source-bound Structural Null attachment
#   owner: Erin Spencer
#   public_surface: AffineContinuityCertificate, QuotientSeamCommutationCertificate, CarrierAttachmentEvidenceResult, FullCarrierAttachmentReport, ContinuityEvidenceStanding, run_v015_full_carrier_attachment_experiment
#   internal_surface: exact coefficient validation and fixed mixed-scope RC01-RC10 evidence construction
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: v0.13 source provenance remains attached and no arbitrary observed-element assignment is introduced
#   admin_only: false
#   tests: tests/test_full_carrier_attachment.py
#   rollout: nonselecting v0.15 analytic certificates for the complete declared real affine intervals and non-null quotient, joined to the unchanged v0.13 partial root attachment
#   rollback: remove this module, exports, tests, and v0.15 document while retaining v0.12 specification and v0.13 executable evidence
#   requires: edcm_exact_coordinate_representation_boundary, edcm_partial_initiation_boundary
#   since: 2026-07-31
#   unresolved: arbitrary observed-element transverse assignment, total Structural Null initiation relationship, intrinsic-versus-marked seam choice, proof-assistant formalization, higher geometry, higher-gonol composition, scoped completion, canonical faithful breadth, and carrier selection
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: full_carrier_affine_certificate_is_universal_and_exact
#   given: the v0.15 affine continuity certificate is constructed
#   then: exact coefficients, endpoints, inverse compositions, and epsilon-delta multipliers encode the written proof over both complete real intervals without numerical sampling
#   class: correctness
#   since: 2026-07-31
#
# id: full_carrier_quotient_certificate_commutes_without_moving_the_marked_seam
#   given: the v0.15 quotient seam certificate is constructed
#   then: two-turn deck equivariance and the one-turn sheet identity hold by exact coefficient algebra while coordinate cuts remain nonauthoritative and Structural Null remains outside the non-null quotient
#   class: correctness
#   since: 2026-07-31
#
# id: full_carrier_attachment_retains_mixed_evidence_scopes
#   given: the v0.15 combined report is constructed
#   then: RC01 and non-null RC03 retain analytic standing, RC02 and RC04-RC10 retain their bounded v0.13 executable standing, and no result is relabeled as one uniform arbitrary-real runtime scope
#   class: evidence
#   since: 2026-07-31
#
# id: full_carrier_attachment_does_not_complete_select_or_activate
#   given: analytic non-null evidence and bounded initiation evidence are joined
#   then: arbitrary-element assignment, a total Structural Null relation, machine-checked proof, carrier selection, EDCM activation, and METAPAT activation remain absent and fail closed on substitution
#   class: doctrine
#   since: 2026-07-31
#
# id: external_multiwoz_v0141_handoff_is_exact_and_nonpromoting
#   given: the corrected downstream EDCM MultiWOZ result is recorded in UCNS
#   then: the corpus, report, receipt, producer, and publication identities remain exact while geometry, proof, canon, EDCM activation, and METAPAT activation do not transfer
#   class: evidence
#   since: 2026-07-31
# === END CONTRACTS ===

"""Bounded full-carrier attachment evidence for UCNS v0.15.

This module turns the v0.12 affine and quotient derivations into exact,
tamper-resistant certificate records and joins them to the unchanged v0.13
source-bound root attachment.  The analytic proof covers the declared real
non-null candidate; Python validates its finite proof data but is not presented
as a proof assistant or arbitrary-real runtime.

The combined report deliberately retains mixed scopes.  It does not supply an
arbitrary observed-element transverse assignment or a total topology from
Structural Null to the non-null carrier.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction

from .initiation_boundary import (
    PARTIAL_INITIATION_SCOPE,
    RC_FALSIFIER_IDS,
    PartialInitiationBoundaryReport,
    run_v013_partial_initiation_boundary_experiment,
)
from .mobius_experiment import FalsifierVerdict


V015_FULL_CARRIER_SCHEMA_ID = "ucns.edcm.full-carrier-attachment-evidence"
V015_FULL_CARRIER_SCHEMA_VERSION = "0.15.0"
V015_SELECTION_EFFECT = "none"

AFFINE_CERTIFICATE_ID = "ucns.carrier.affine-real-continuity"
AFFINE_CERTIFICATE_VERSION = "0.15.0"
AFFINE_REAL_SCOPE = "complete-declared-real-affine-intervals"
AFFINE_FORMULA = "B_R(u)=1+u/2; G_R(b)=2*(b-1)"

QUOTIENT_CERTIFICATE_ID = "ucns.carrier.non-null-quotient-seam-commutation"
QUOTIENT_CERTIFICATE_VERSION = "0.15.0"
NON_NULL_QUOTIENT_SCOPE = "declared-non-null-product-quotient-spaces"
QUOTIENT_DESCENT_THEOREM = (
    "continuous-equivariant-map-descends-through-declared-quotient"
)
COORDINATE_CUT_STATUS = "nonauthoritative-representative-only"
STRUCTURAL_NULL_DOMAIN_STATUS = "excluded-disjoint-typed-prestate"

ANALYTIC_PROOF_STATUS = "analytic-certificate-not-machine-checked"
STRUCTURAL_NULL_ATTACHMENT_STATUS = "source-bound-partial-root-attachment"
V015_COMPLETE_RELATIONSHIP_STATUS = (
    "inconclusive-without-arbitrary-element-assignment"
)

V015_HMMM = (
    "arbitrary observed-element transverse assignment remains unresolved",
    "no runtime arbitrary-real object model or machine-checked theorem is supplied",
    "the total topology and relation from Structural Null to arbitrary non-null states remains unresolved",
    "the marked-versus-intrinsic target seam choice remains unresolved",
    "canonical B, higher geometry, higher-gonol composition, and scoped completion remain unresolved",
)

_TRANSVERSE_INTERVAL = (Fraction(-1), Fraction(1))
_BREADTH_INTERVAL = (Fraction(1, 2), Fraction(3, 2))
_FORWARD_INTERCEPT = Fraction(1)
_FORWARD_SLOPE = Fraction(1, 2)
_INVERSE_INTERCEPT = Fraction(-2)
_INVERSE_SLOPE = Fraction(2)
_FORWARD_DELTA_MULTIPLIER = Fraction(2)
_INVERSE_DELTA_MULTIPLIER = Fraction(1, 2)
_DECK_PERIOD = Fraction(2)
_SHEET_TURN_SHIFT = Fraction(1)
_SHEET_REFLECTION_INTERCEPT = Fraction(2)
_SHEET_REFLECTION_SLOPE = Fraction(-1)


class FullCarrierAttachmentError(ValueError):
    """Raised when v0.15 evidence is widened or substituted."""


class ContinuityEvidenceStanding(str, Enum):
    """Standing vocabulary for the deliberately mixed v0.15 evidence."""

    ANALYTIC_SUPPORTED = "analytic-supported"
    EXACT_IMPLEMENTED_SUPPORTED = "exact-implemented-supported"


def _require_fraction(value: Fraction, field_name: str) -> None:
    if not isinstance(value, Fraction):
        raise FullCarrierAttachmentError(
            f"{field_name} must be an exact Fraction"
        )


def _require_positive_fraction(value: Fraction, field_name: str) -> None:
    _require_fraction(value, field_name)
    if value <= 0:
        raise FullCarrierAttachmentError(f"{field_name} must be positive")


def _affine_image(
    intercept: Fraction,
    slope: Fraction,
    value: Fraction,
) -> Fraction:
    return intercept + slope * value


@dataclass(frozen=True, slots=True)
class AffineContinuityCertificate:
    """Exact finite proof data for the declared real affine bijection."""

    source_interval: tuple[Fraction, Fraction] = _TRANSVERSE_INTERVAL
    target_interval: tuple[Fraction, Fraction] = _BREADTH_INTERVAL
    forward_intercept: Fraction = _FORWARD_INTERCEPT
    forward_slope: Fraction = _FORWARD_SLOPE
    inverse_intercept: Fraction = _INVERSE_INTERCEPT
    inverse_slope: Fraction = _INVERSE_SLOPE
    forward_delta_multiplier: Fraction = _FORWARD_DELTA_MULTIPLIER
    inverse_delta_multiplier: Fraction = _INVERSE_DELTA_MULTIPLIER
    certificate_id: str = AFFINE_CERTIFICATE_ID
    certificate_version: str = AFFINE_CERTIFICATE_VERSION
    formula: str = AFFINE_FORMULA
    scope: str = AFFINE_REAL_SCOPE
    proof_status: str = ANALYTIC_PROOF_STATUS
    selection_effect: str = V015_SELECTION_EFFECT

    def __post_init__(self) -> None:
        if self.source_interval != _TRANSVERSE_INTERVAL:
            raise FullCarrierAttachmentError(
                "affine source interval is fixed"
            )
        if self.target_interval != _BREADTH_INTERVAL:
            raise FullCarrierAttachmentError(
                "affine target interval is fixed"
            )
        for value, field_name in (
            (self.forward_intercept, "forward_intercept"),
            (self.forward_slope, "forward_slope"),
            (self.inverse_intercept, "inverse_intercept"),
            (self.inverse_slope, "inverse_slope"),
        ):
            _require_fraction(value, field_name)
        _require_positive_fraction(
            self.forward_delta_multiplier,
            "forward_delta_multiplier",
        )
        _require_positive_fraction(
            self.inverse_delta_multiplier,
            "inverse_delta_multiplier",
        )
        if (
            self.forward_intercept != _FORWARD_INTERCEPT
            or self.forward_slope != _FORWARD_SLOPE
            or self.inverse_intercept != _INVERSE_INTERCEPT
            or self.inverse_slope != _INVERSE_SLOPE
        ):
            raise FullCarrierAttachmentError(
                "affine and inverse coefficients are fixed"
            )
        if tuple(
            _affine_image(
                self.forward_intercept,
                self.forward_slope,
                endpoint,
            )
            for endpoint in self.source_interval
        ) != self.target_interval:
            raise FullCarrierAttachmentError(
                "affine endpoint images must equal the target interval"
            )
        if tuple(
            _affine_image(
                self.inverse_intercept,
                self.inverse_slope,
                endpoint,
            )
            for endpoint in self.target_interval
        ) != self.source_interval:
            raise FullCarrierAttachmentError(
                "inverse endpoint images must equal the source interval"
            )
        forward_after_inverse = (
            self.forward_intercept
            + self.forward_slope * self.inverse_intercept,
            self.forward_slope * self.inverse_slope,
        )
        inverse_after_forward = (
            self.inverse_intercept
            + self.inverse_slope * self.forward_intercept,
            self.inverse_slope * self.forward_slope,
        )
        if forward_after_inverse != (Fraction(0), Fraction(1)):
            raise FullCarrierAttachmentError(
                "forward after inverse must be the exact identity"
            )
        if inverse_after_forward != (Fraction(0), Fraction(1)):
            raise FullCarrierAttachmentError(
                "inverse after forward must be the exact identity"
            )
        if (
            abs(self.forward_slope) * self.forward_delta_multiplier
            != 1
        ):
            raise FullCarrierAttachmentError(
                "forward epsilon-delta multiplier is invalid"
            )
        if (
            abs(self.inverse_slope) * self.inverse_delta_multiplier
            != 1
        ):
            raise FullCarrierAttachmentError(
                "inverse epsilon-delta multiplier is invalid"
            )
        if (
            self.certificate_id != AFFINE_CERTIFICATE_ID
            or self.certificate_version != AFFINE_CERTIFICATE_VERSION
            or self.formula != AFFINE_FORMULA
            or self.scope != AFFINE_REAL_SCOPE
            or self.proof_status != ANALYTIC_PROOF_STATUS
        ):
            raise FullCarrierAttachmentError(
                "affine certificate identity and standing are fixed"
            )
        if self.selection_effect != V015_SELECTION_EFFECT:
            raise FullCarrierAttachmentError(
                "affine certificate cannot select a carrier"
            )

    @property
    def forward_after_inverse_coefficients(
        self,
    ) -> tuple[Fraction, Fraction]:
        """Return exact intercept and slope for ``B_R(G_R(b))``."""

        return (
            self.forward_intercept
            + self.forward_slope * self.inverse_intercept,
            self.forward_slope * self.inverse_slope,
        )

    @property
    def inverse_after_forward_coefficients(
        self,
    ) -> tuple[Fraction, Fraction]:
        """Return exact intercept and slope for ``G_R(B_R(u))``."""

        return (
            self.inverse_intercept
            + self.inverse_slope * self.forward_intercept,
            self.inverse_slope * self.forward_slope,
        )

    def forward_delta(self, epsilon: Fraction) -> Fraction:
        """Instantiate the universal forward modulus with exact evidence."""

        _require_positive_fraction(epsilon, "epsilon")
        return self.forward_delta_multiplier * epsilon

    def inverse_delta(self, epsilon: Fraction) -> Fraction:
        """Instantiate the universal inverse modulus with exact evidence."""

        _require_positive_fraction(epsilon, "epsilon")
        return self.inverse_delta_multiplier * epsilon


@dataclass(frozen=True, slots=True)
class QuotientSeamCommutationCertificate:
    """Exact deck and sheet identities for the declared non-null quotient."""

    source_deck_period: Fraction = _DECK_PERIOD
    target_deck_period: Fraction = _DECK_PERIOD
    map_turn_slope: Fraction = Fraction(1)
    sheet_turn_shift: Fraction = _SHEET_TURN_SHIFT
    sheet_reflection_intercept: Fraction = _SHEET_REFLECTION_INTERCEPT
    sheet_reflection_slope: Fraction = _SHEET_REFLECTION_SLOPE
    affine_certificate_id: str = AFFINE_CERTIFICATE_ID
    certificate_id: str = QUOTIENT_CERTIFICATE_ID
    certificate_version: str = QUOTIENT_CERTIFICATE_VERSION
    descent_theorem: str = QUOTIENT_DESCENT_THEOREM
    coordinate_cut_status: str = COORDINATE_CUT_STATUS
    structural_null_domain_status: str = STRUCTURAL_NULL_DOMAIN_STATUS
    scope: str = NON_NULL_QUOTIENT_SCOPE
    proof_status: str = ANALYTIC_PROOF_STATUS
    selection_effect: str = V015_SELECTION_EFFECT

    def __post_init__(self) -> None:
        for value, field_name in (
            (self.source_deck_period, "source_deck_period"),
            (self.target_deck_period, "target_deck_period"),
            (self.map_turn_slope, "map_turn_slope"),
            (self.sheet_turn_shift, "sheet_turn_shift"),
            (
                self.sheet_reflection_intercept,
                "sheet_reflection_intercept",
            ),
            (self.sheet_reflection_slope, "sheet_reflection_slope"),
        ):
            _require_fraction(value, field_name)
        if (
            self.source_deck_period != _DECK_PERIOD
            or self.target_deck_period != _DECK_PERIOD
            or self.map_turn_slope != 1
        ):
            raise FullCarrierAttachmentError(
                "quotient deck periods and turn map are fixed"
            )
        if (
            self.map_turn_slope * self.source_deck_period
            != self.target_deck_period
        ):
            raise FullCarrierAttachmentError(
                "product map must be equivariant under the deck period"
            )
        if (
            self.sheet_turn_shift != _SHEET_TURN_SHIFT
            or self.sheet_reflection_intercept
            != _SHEET_REFLECTION_INTERCEPT
            or self.sheet_reflection_slope != _SHEET_REFLECTION_SLOPE
        ):
            raise FullCarrierAttachmentError(
                "sheet involution coefficients are fixed"
            )
        breadth_after_source_sheet = (
            _FORWARD_INTERCEPT,
            -_FORWARD_SLOPE,
        )
        target_sheet_after_breadth = (
            self.sheet_reflection_intercept
            + self.sheet_reflection_slope * _FORWARD_INTERCEPT,
            self.sheet_reflection_slope * _FORWARD_SLOPE,
        )
        if breadth_after_source_sheet != target_sheet_after_breadth:
            raise FullCarrierAttachmentError(
                "B_R(-u) must equal the exact target sheet reflection"
            )
        sheet_twice = (
            self.sheet_reflection_intercept
            + self.sheet_reflection_slope
            * self.sheet_reflection_intercept,
            self.sheet_reflection_slope * self.sheet_reflection_slope,
            self.sheet_turn_shift + self.sheet_turn_shift,
        )
        if sheet_twice != (
            Fraction(0),
            Fraction(1),
            self.target_deck_period,
        ):
            raise FullCarrierAttachmentError(
                "sheet involution must square to one target deck period"
            )
        if (
            self.affine_certificate_id != AFFINE_CERTIFICATE_ID
            or self.certificate_id != QUOTIENT_CERTIFICATE_ID
            or self.certificate_version != QUOTIENT_CERTIFICATE_VERSION
            or self.descent_theorem != QUOTIENT_DESCENT_THEOREM
            or self.coordinate_cut_status != COORDINATE_CUT_STATUS
            or self.structural_null_domain_status
            != STRUCTURAL_NULL_DOMAIN_STATUS
            or self.scope != NON_NULL_QUOTIENT_SCOPE
            or self.proof_status != ANALYTIC_PROOF_STATUS
        ):
            raise FullCarrierAttachmentError(
                "quotient certificate identity, scope, and standing are fixed"
            )
        if self.selection_effect != V015_SELECTION_EFFECT:
            raise FullCarrierAttachmentError(
                "quotient certificate cannot select a carrier"
            )

    @property
    def sheet_commutation_coefficients(
        self,
    ) -> tuple[
        tuple[Fraction, Fraction],
        tuple[Fraction, Fraction],
    ]:
        """Return both exact coefficient forms of ``B_R(-u)=2-B_R(u)``."""

        return (
            (_FORWARD_INTERCEPT, -_FORWARD_SLOPE),
            (
                self.sheet_reflection_intercept
                + self.sheet_reflection_slope * _FORWARD_INTERCEPT,
                self.sheet_reflection_slope * _FORWARD_SLOPE,
            ),
        )


@dataclass(frozen=True, slots=True)
class CarrierAttachmentEvidenceResult:
    """One RC standing with its actual analytic or executable scope."""

    falsifier_id: str
    standing: ContinuityEvidenceStanding
    scope: str
    evidence: tuple[str, ...]
    limitation: str

    def __post_init__(self) -> None:
        if self.falsifier_id not in RC_FALSIFIER_IDS:
            raise FullCarrierAttachmentError("unknown RC falsifier id")
        if not isinstance(self.standing, ContinuityEvidenceStanding):
            raise FullCarrierAttachmentError(
                "RC result must use the v0.15 standing vocabulary"
            )
        if not self.scope.strip():
            raise FullCarrierAttachmentError("RC scope must be nonempty")
        if not self.evidence or any(not item.strip() for item in self.evidence):
            raise FullCarrierAttachmentError(
                "RC result must retain nonempty evidence"
            )
        if not self.limitation.strip():
            raise FullCarrierAttachmentError(
                "RC limitation must be nonempty"
            )


def _analytic_result(
    falsifier_id: str,
    scope: str,
    evidence: tuple[str, ...],
    limitation: str,
) -> CarrierAttachmentEvidenceResult:
    return CarrierAttachmentEvidenceResult(
        falsifier_id=falsifier_id,
        standing=ContinuityEvidenceStanding.ANALYTIC_SUPPORTED,
        scope=scope,
        evidence=evidence,
        limitation=limitation,
    )


def _implemented_result(
    upstream: PartialInitiationBoundaryReport,
    falsifier_id: str,
) -> CarrierAttachmentEvidenceResult:
    result = upstream.result(falsifier_id)
    if result.verdict is not FalsifierVerdict.SUPPORTED:
        raise FullCarrierAttachmentError(
            f"{falsifier_id} lacks required v0.13 executable support"
        )
    return CarrierAttachmentEvidenceResult(
        falsifier_id=falsifier_id,
        standing=ContinuityEvidenceStanding.EXACT_IMPLEMENTED_SUPPORTED,
        scope=PARTIAL_INITIATION_SCOPE,
        evidence=(
            f"upstream-schema:{upstream.schema_id}/{upstream.schema_version}",
            *result.evidence,
        ),
        limitation=result.limitation,
    )


def _build_results(
    affine: AffineContinuityCertificate,
    quotient: QuotientSeamCommutationCertificate,
    upstream: PartialInitiationBoundaryReport,
) -> tuple[CarrierAttachmentEvidenceResult, ...]:
    analytic = {
        "RC01": _analytic_result(
            "RC01",
            AFFINE_REAL_SCOPE,
            (
                f"certificate:{affine.certificate_id}/{affine.certificate_version}",
                "forward-modulus:delta=2*epsilon",
                "inverse-modulus:delta=epsilon/2",
                "inverse-compositions:exact-identity",
            ),
            "the certificate is a written universal analytic derivation, not an arbitrary-real runtime or machine-checked theorem",
        ),
        "RC03": _analytic_result(
            "RC03",
            NON_NULL_QUOTIENT_SCOPE,
            (
                f"certificate:{quotient.certificate_id}/{quotient.certificate_version}",
                "two-turn-deck-equivariance:exact",
                "sheet-identity:B_R(-u)=2-B_R(u)",
                f"coordinate-cut:{COORDINATE_CUT_STATUS}",
            ),
            "support covers the non-null quotient only; the marked initiation seam is provenance-bearing and Structural Null is not a limit point",
        ),
    }
    return tuple(
        analytic[falsifier_id]
        if falsifier_id in analytic
        else _implemented_result(upstream, falsifier_id)
        for falsifier_id in RC_FALSIFIER_IDS
    )


@dataclass(frozen=True, slots=True)
class FullCarrierAttachmentReport:
    """Combined analytic non-null and bounded initiation evidence packet."""

    affine_certificate: AffineContinuityCertificate
    quotient_certificate: QuotientSeamCommutationCertificate
    partial_initiation_report: PartialInitiationBoundaryReport
    results: tuple[CarrierAttachmentEvidenceResult, ...]
    schema_id: str = V015_FULL_CARRIER_SCHEMA_ID
    schema_version: str = V015_FULL_CARRIER_SCHEMA_VERSION
    proof_status: str = ANALYTIC_PROOF_STATUS
    structural_null_attachment_status: str = (
        STRUCTURAL_NULL_ATTACHMENT_STATUS
    )
    complete_relationship_status: str = V015_COMPLETE_RELATIONSHIP_STATUS
    arbitrary_element_assignment_status: str = "unresolved"
    selection_effect: str = V015_SELECTION_EFFECT
    edcm_activation: str = "inactive"
    metapat_activation: str = "inactive"
    hmmm: tuple[str, ...] = V015_HMMM

    def __post_init__(self) -> None:
        if not isinstance(
            self.affine_certificate,
            AffineContinuityCertificate,
        ):
            raise FullCarrierAttachmentError(
                "report requires the v0.15 affine certificate"
            )
        if not isinstance(
            self.quotient_certificate,
            QuotientSeamCommutationCertificate,
        ):
            raise FullCarrierAttachmentError(
                "report requires the v0.15 quotient certificate"
            )
        if not isinstance(
            self.partial_initiation_report,
            PartialInitiationBoundaryReport,
        ):
            raise FullCarrierAttachmentError(
                "report requires the v0.13 initiation report"
            )
        upstream = self.partial_initiation_report
        if (
            upstream.result("RC01").verdict
            is not FalsifierVerdict.INCONCLUSIVE
            or upstream.result("RC03").verdict
            is not FalsifierVerdict.INCONCLUSIVE
        ):
            raise FullCarrierAttachmentError(
                "v0.15 cannot rewrite the v0.13 verdict packet"
            )
        if self.results != _build_results(
            self.affine_certificate,
            self.quotient_certificate,
            upstream,
        ):
            raise FullCarrierAttachmentError(
                "v0.15 RC evidence, standing, and mixed scopes are fixed"
            )
        if tuple(item.falsifier_id for item in self.results) != RC_FALSIFIER_IDS:
            raise FullCarrierAttachmentError(
                "v0.15 must retain RC01 through RC10 in order"
            )
        if (
            self.schema_id != V015_FULL_CARRIER_SCHEMA_ID
            or self.schema_version != V015_FULL_CARRIER_SCHEMA_VERSION
            or self.proof_status != ANALYTIC_PROOF_STATUS
            or self.structural_null_attachment_status
            != STRUCTURAL_NULL_ATTACHMENT_STATUS
            or self.complete_relationship_status
            != V015_COMPLETE_RELATIONSHIP_STATUS
            or self.arbitrary_element_assignment_status != "unresolved"
        ):
            raise FullCarrierAttachmentError(
                "v0.15 schema and relationship standings are fixed"
            )
        if self.selection_effect != V015_SELECTION_EFFECT:
            raise FullCarrierAttachmentError(
                "v0.15 cannot select a carrier"
            )
        if self.edcm_activation != "inactive":
            raise FullCarrierAttachmentError("v0.15 cannot activate EDCM")
        if self.metapat_activation != "inactive":
            raise FullCarrierAttachmentError("v0.15 cannot activate METAPAT")
        if self.hmmm != V015_HMMM:
            raise FullCarrierAttachmentError(
                "v0.15 unresolved boundary is fixed"
            )

    def result(self, falsifier_id: str) -> CarrierAttachmentEvidenceResult:
        """Return one fixed mixed-scope result or fail closed."""

        for item in self.results:
            if item.falsifier_id == falsifier_id:
                return item
        raise FullCarrierAttachmentError(
            f"unknown continuity falsifier: {falsifier_id}"
        )


def run_v015_full_carrier_attachment_experiment(
) -> FullCarrierAttachmentReport:
    """Construct the complete bounded v0.15 evidence graph."""

    affine = AffineContinuityCertificate()
    quotient = QuotientSeamCommutationCertificate()
    upstream = run_v013_partial_initiation_boundary_experiment()
    return FullCarrierAttachmentReport(
        affine_certificate=affine,
        quotient_certificate=quotient,
        partial_initiation_report=upstream,
        results=_build_results(affine, quotient, upstream),
    )


__all__ = [
    "AFFINE_CERTIFICATE_ID",
    "AFFINE_CERTIFICATE_VERSION",
    "AFFINE_FORMULA",
    "AFFINE_REAL_SCOPE",
    "ANALYTIC_PROOF_STATUS",
    "COORDINATE_CUT_STATUS",
    "NON_NULL_QUOTIENT_SCOPE",
    "QUOTIENT_CERTIFICATE_ID",
    "QUOTIENT_CERTIFICATE_VERSION",
    "QUOTIENT_DESCENT_THEOREM",
    "STRUCTURAL_NULL_ATTACHMENT_STATUS",
    "STRUCTURAL_NULL_DOMAIN_STATUS",
    "V015_COMPLETE_RELATIONSHIP_STATUS",
    "V015_FULL_CARRIER_SCHEMA_ID",
    "V015_FULL_CARRIER_SCHEMA_VERSION",
    "V015_HMMM",
    "V015_SELECTION_EFFECT",
    "AffineContinuityCertificate",
    "CarrierAttachmentEvidenceResult",
    "ContinuityEvidenceStanding",
    "FullCarrierAttachmentError",
    "FullCarrierAttachmentReport",
    "QuotientSeamCommutationCertificate",
    "run_v015_full_carrier_attachment_experiment",
]
