# UCNS-native caching prototype

This is a software-only prototype for UCNS-native cache identity. It does not claim hardware speedups, does not replace existing KV/cache mechanisms, and does not transfer UCNS-A theorem status into caching behavior.

```text
UCNS object
    |
    v
canonical identity ---------------> exact cache key
    |
    v
primitive streams:
  angle / rotation / chirality
    |
    v
Braider
    |
    v
emergent lattice hash ------------> structural cache key
    |
    v
factorization candidates ---------> sub-cache reuse
```

Mainstream flat caches usually key opaque values by an external hash and find exact or prefix matches. This prototype derives identity from UCNS canonical structure, nested payload hashes, factorization envelopes, and three deterministic primitive streams.

The primitive streams are equal-length LCM-aligned bit traces: angle bits come from normalized angle sequence data, rotation bits from carrier step changes, and chirality bits from face/orientation bits. The Braider zips those traces into local events, hashes the full event sequence into an emergent lattice address, and reports repeated triples/subsequences as reusable windows.

Factorization-informed reuse uses scoped UCNS factorization metadata. A non-absolute `SEQ-PRIME` result is never treated as proof that no reusable substructure exists. Cache keys carry a scope note so downstream A0 code does not imply proof status beyond the domain status returned by UCNS.

## Current limitations

- The `a0-betatest` checkout was not present in this workspace, so inference integration behind `A0_UCNS_CACHE=1` remains a downstream hook.
- The Braider is a deterministic software model, not hardware evidence.
- Structural-hit tests need a stable fixture with shared braid identity and distinct canonical identity.
- edcmbone fidelity comparison is not wired because the sibling checkout was unavailable.

## Phase plan

1. Establish deterministic UCNS keys, streams, braider hashes, and an observable in-memory store.
2. Add A0 read-through/write-through integration behind `A0_UCNS_CACHE=1` in the a0-betatest inference path.
3. Add measured benchmarks before making performance claims.
4. Add optional edcmbone guards when that package is installed.

hmmm: the cache can hum in pure Python, but the absent sibling engine means it has not yet learned where A0 keeps the expensive spoons.
