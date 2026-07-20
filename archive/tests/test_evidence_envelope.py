from __future__ import annotations

from dataclasses import replace
from fractions import Fraction

import pytest

from ucns import (
    BRIDGE_RECORD_SCHEMA_ID,
    BRIDGE_RECORD_SCHEMA_VERSION,
    FACTORIZATION_EVIDENCE_SCHEMA_ID,
    FACTORIZATION_EVIDENCE_SCHEMA_VERSION,
    NEGATIVE_CERTIFICATION_POLICY_VERSION,
    S2,
    UNIT,
    FactorizationResultKind,
    UCNSBridgeRecord,
    UCNSFactorizationEvidence,
    UCNSObject,
    bridge_record,
    factorization_evidence,
    stable_hash,
)

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
T2 = UCNSObject(1, 1, [(Fraction(0), E)], [0])


def test_bridge_record_binds_canonical_json_stable_hash_and_domain_status() -> None:
    record = bridge_record(S2)

    assert record.schema_id == BRIDGE_RECORD_SCHEMA_ID
    assert record.schema_version == BRIDGE_RECORD_SCHEMA_VERSION
    assert record.object_hash == stable_hash(S2)
    assert record.domain_label == "depth-1"
    assert record.domain_statuses == ("DEFENDED", "TEST_BACKED")
    assert record.completeness_guaranteed is True
    assert record.is_verified_domain is True
    assert record.evidence_digest


def test_bridge_record_roundtrips_through_canonical_json() -> None:
    record = bridge_record(S2)
    assert UCNSBridgeRecord.from_dict(record.to_dict()) == record
    assert UCNSBridgeRecord.from_json(record.to_json()) == record
    assert record.to_json() == UCNSBridgeRecord.from_json(record.to_json()).to_json()


def test_unit_bridge_record_is_typed_and_not_a_prime_claim() -> None:
    record = bridge_record(UNIT)
    assert record.is_unit is True
    assert record.length == 0
    assert record.domain_label == "depth-0"
    assert record.seq_prime_claim_scope == "not-prime-unit-domain"


def test_bridge_record_rejects_hash_tamper_unknown_fields_and_type_coercion() -> None:
    record = bridge_record(S2)
    tampered = record.to_dict()
    tampered["object_hash"] = "0" * 64
    with pytest.raises(ValueError, match="object_hash does not match"):
        UCNSBridgeRecord.from_dict(tampered)

    unknown = record.to_dict()
    unknown["invented"] = True
    with pytest.raises(ValueError, match="unknown bridge record fields"):
        UCNSBridgeRecord.from_dict(unknown)

    coerced = record.to_dict()
    coerced["is_unit"] = "false"
    with pytest.raises(ValueError, match="is_unit must be a boolean"):
        UCNSBridgeRecord.from_dict(coerced)

    coerced = record.to_dict()
    coerced["depth"] = "1"
    with pytest.raises(ValueError, match="depth must be an integer"):
        UCNSBridgeRecord.from_dict(coerced)


def test_flat_prime_serializes_certified_negative_evidence() -> None:
    evidence = factorization_evidence(S2)

    assert evidence.schema_id == FACTORIZATION_EVIDENCE_SCHEMA_ID
    assert evidence.schema_version == FACTORIZATION_EVIDENCE_SCHEMA_VERSION
    assert evidence.product_hash == stable_hash(S2)
    assert evidence.result_kind == FactorizationResultKind.SEQ_PRIME.value
    assert evidence.factor_hashes == ()
    assert evidence.negative_result_certified is True
    assert evidence.seq_prime_is_absolute is True
    assert evidence.certification_policy_version == NEGATIVE_CERTIFICATION_POLICY_VERSION
    assert evidence.search_exhausted is True
    assert evidence.truncation_occurred is False
    assert evidence.coverage_record_validated is True
    assert evidence.coverage_bound_to_search_report is True
    assert evidence.pruning_preserves_coverage is True
    assert evidence.uncertified_reasons == ()


def test_certified_evidence_roundtrips_without_losing_policy_fields() -> None:
    evidence = factorization_evidence(S2)
    assert UCNSFactorizationEvidence.from_dict(evidence.to_dict()) == evidence
    assert UCNSFactorizationEvidence.from_json(evidence.to_json()) == evidence


def test_unit_result_remains_explicitly_uncertified() -> None:
    evidence = factorization_evidence(UNIT)
    assert evidence.result_kind == FactorizationResultKind.SEQ_PRIME.value
    assert evidence.negative_result_certified is False
    assert evidence.seq_prime_is_absolute is False
    assert evidence.claim_scope == "not-prime-unit-domain"
    assert evidence.search_exhausted is False
    assert evidence.uncertified_reasons == ("unit-domain-primality-inapplicable",)


def test_incomplete_catalogue_remains_uncertified_despite_exhaustion() -> None:
    evidence = factorization_evidence(S2, catalogue=[])
    assert evidence.search_exhausted is True
    assert evidence.negative_result_certified is False
    assert evidence.seq_prime_is_absolute is False
    assert any(
        reason.startswith("catalogue-coverage-uncertified")
        for reason in evidence.uncertified_reasons
    )


def test_recovered_factors_are_serialized_by_stable_hash_only() -> None:
    evidence = factorization_evidence(T2)
    assert evidence.result_kind == FactorizationResultKind.FACTORS.value
    assert len(evidence.factor_hashes) == 2
    assert evidence.negative_result_certified is False
    assert evidence.seq_prime_is_absolute is False
    assert evidence.uncertified_reasons == ("factors-found",)


def test_certified_record_with_broken_policy_invariant_fails_closed() -> None:
    evidence = factorization_evidence(S2)
    with pytest.raises(ValueError, match="search_exhausted"):
        replace(evidence, search_exhausted=False, evidence_digest="")

    with pytest.raises(ValueError, match="certification_policy_version"):
        replace(
            evidence,
            certification_policy_version="invented-policy",
            evidence_digest="",
        )


def test_factorization_evidence_rejects_tamper_unknown_fields_and_type_coercion() -> None:
    evidence = factorization_evidence(S2)
    tampered = evidence.to_dict()
    tampered["claim_scope"] = "invented"
    with pytest.raises(ValueError, match="evidence_digest does not match"):
        UCNSFactorizationEvidence.from_dict(tampered)

    unknown = evidence.to_dict()
    unknown["invented"] = True
    with pytest.raises(ValueError, match="unknown factorization evidence fields"):
        UCNSFactorizationEvidence.from_dict(unknown)

    coerced = evidence.to_dict()
    coerced["negative_result_certified"] = "true"
    with pytest.raises(
        ValueError,
        match="negative_result_certified must be a boolean",
    ):
        UCNSFactorizationEvidence.from_dict(coerced)

    coerced = evidence.to_dict()
    coerced["supplied_catalogue_size"] = "1"
    with pytest.raises(ValueError, match="supplied_catalogue_size must be an integer"):
        UCNSFactorizationEvidence.from_dict(coerced)
