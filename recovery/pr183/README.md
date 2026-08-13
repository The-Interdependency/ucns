# PR #183 interval-boundary source recovery

This recovery surface exists only to make the preserved readable PR #181 implementation available to Codex/VM work without modifying `main` or PR #183.

Recovered source: `src/ucns/prime_interval_boundaries.py`

Provenance:
- recovered from the preserved PR #181 artifact `ucns-p7-interval-boundary-invariants-v1.patch` in the ChatGPT Library;
- the preserved `UCNS_P7_INTERVAL_BOUNDARY_MANIFEST.json` records the same source identity;
- expected decoded size: `35535` bytes;
- expected decoded line count: `905`;
- expected SHA-256: `6a79463856ea0171d7d29881fdb7e66780fab29779ff1c5fd1b71eaae7f9fc3c`.

The source is stored as ordered base64 chunks to avoid text-encoding damage through the recovery transport. Reconstruct on the VM from a checkout of this branch:

```bash
cat recovery/pr183/prime_interval_boundaries.py.b64.part* \
  | base64 -d \
  > /tmp/prime_interval_boundaries.recovered.py

wc -l -c /tmp/prime_interval_boundaries.recovered.py
sha256sum /tmp/prime_interval_boundaries.recovered.py
```

Expected:

```text
905 35535 /tmp/prime_interval_boundaries.recovered.py
6a79463856ea0171d7d29881fdb7e66780fab29779ff1c5fd1b71eaae7f9fc3c  /tmp/prime_interval_boundaries.recovered.py
```

Recovery rule:
1. compare this readable implementation with the API expected by PR #183 wrappers/tests;
2. if compatible, use this provenance-backed source instead of the corrupt compressed payload;
3. if a compatibility layer is required, keep it minimal and explicit rather than reconstructing mathematical behavior by assumption;
4. preserve the recovered SHA and PR #181 provenance in the #183 preservation ledger;
5. this recovery branch confers no theorem status and is not intended for merge into `main` as-is.
