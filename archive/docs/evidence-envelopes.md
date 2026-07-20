# UCNS serialized evidence envelopes

## Bridge record

Create a versioned canonical identity record for any UCNS object or the unit sentinel:

```python
import ucns

record = ucns.bridge_record(ucns.S2)
serialized = record.to_json()
restored = ucns.UCNSBridgeRecord.from_json(serialized)
assert restored == record
```

`UCNSBridgeRecord` binds:

```text
canonical UCNS JSON
stable SHA-256 object hash
canonical serialization version
typed domain statuses
completeness prerequisite
SEQ-PRIME claim scope
depth, n_min, length, and unit/frontier flags
producer id and evidence digest
```

The constructor verifies that `object_hash` is the SHA-256 digest of the exact canonical JSON bytes.

## Factorization evidence

Create a serialized result only through the authoritative UCNS policy path:

```python
import ucns

evidence = ucns.factorization_evidence(ucns.S2)
assert evidence.negative_result_certified
```

`factorization_evidence()` accepts a product and optional catalogue. It does **not** accept a caller-built `FactorizationResult` or a certification boolean. It runs `ucns.factorization_result()` and serializes:

```text
product stable hash and domain status
result kind and factor stable hashes
claim scope and note
negative-certification policy version
search exhaustion and truncation
catalogue source, sizes, and fingerprints
coverage status, validation, and report binding
pruning rule/version and coverage-preservation status
explicit uncertified reasons
producer id and evidence digest
```

A certified negative record fails construction unless every existing UCNS certification condition remains true.

## Deserialization behavior

Both records:

- reject unknown and missing fields;
- require exact boolean, integer, string, and sequence types;
- reject unsupported schema versions and producer ids;
- recompute and verify their evidence digest;
- emit deterministic canonical JSON.

## Trust boundary

Evidence digests are tamper-evident content identities. They are not signatures and do not authenticate who transmitted a record.

Domain statuses and negative certification are UCNS evidence. They do not automatically validate a consumer's empirical measurements, ontology, or external factual claims.

## hmmm

A future transport may add signed producer attestations. No signature or external trust system is claimed by version 1 of these envelopes.
