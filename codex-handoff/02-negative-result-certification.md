# Workstream 2 — machine-checkable negative-result certification

## Defect to eliminate

`factorization_result` currently sets `seq_prime_is_absolute` from target-domain metadata alone. An empty or incomplete caller catalogue can therefore turn catalogue-relative search failure into an “absolute” prime claim.

## Required semantics

A certified negative result requires **all** of the following:

1. The raw result is `SEQ-PRIME`.
2. The target belongs to a domain for which the repository currently permits a completeness claim.
3. The search actually exhausted every candidate permitted by its declared search boundary.
4. The exact input catalogue has machine-checked coverage for that target domain, or is a machine-checked superset of the canonical required catalogue.
5. Any pruning used is a named, versioned, coverage-preserving built-in rule, and its application is recorded.
6. No operational truncation, exception, or unresolved search branch occurred.
7. The target is not the unit/empty-payload domain where primality is semantically inapplicable.

A caller-supplied Boolean such as `catalogue_complete=True` is forbidden. Do not trust an assertion that is not cryptographically or structurally bound to the exact catalogue and domain.

## Required data model

Introduce structured search and coverage metadata. Names may vary, but the result must expose equivalents of:

```text
search_complete / search_exhausted
negative_result_certified
catalogue_coverage_status
catalogue_fingerprint
catalogue_rule_version
catalogue_source
pruning_applied
pruning_rule
pruning_preserves_coverage
uncertified_reasons
```

A recommended split is:

- `FactorSearchReport`: raw result plus exhaustion and effective-search provenance.
- `CatalogueCertificate`: domain label, rule version, exact catalogue fingerprint, coverage status, and validation reason.
- `factor_search_v08`: compatibility wrapper returning the legacy tuple/sentinel.
- an internal or public report-producing function used by `factorization_result`.

The catalogue fingerprint must bind to the exact catalogue supplied to the search. A deterministic digest over an ordered sequence of canonical object hashes plus explicit unit markers is acceptable. Coverage checking may be order-insensitive, but the audit fingerprint should preserve the actual search input.

Coverage statuses should distinguish at least:

```text
canonical-exact
canonical-superset
uncertified
```

A custom catalogue may become certified automatically only when a machine check proves that it structurally contains the canonical required catalogue for the recognized domain. An explicit certificate parameter, if offered, must be regenerated or validated against the exact catalogue fingerprint, domain label, and rule version; reject mismatches.

Preserve `seq_prime_is_absolute` for compatibility only as an alias or value equal to `negative_result_certified`. Document it as certified **within the declared UCNS domain**, not universal mathematical primality.

Any exception or search-limit event must propagate or produce a distinct incomplete/error result. It must never be translated into `SEQ-PRIME`.

## Required tests

- A flat known composite searched with `catalogue=[]` must not produce a certified negative. Preferably the repaired exhaustive factor path finds the factors; regardless, `negative_result_certified` must be false unless coverage is certified.
- A `SEQ-PRIME` result with an incomplete custom catalogue is non-certified and records the missing coverage reason.
- The canonical default catalogue can certify a negative only in a recognized complete/oracle domain and only after exhaustive search.
- A structurally verified superset of the canonical catalogue can certify under the same conditions.
- A certificate bound to catalogue A is rejected when used with catalogue B.
- Reordering or duplicating candidates is reflected consistently: coverage may remain valid, while the exact search fingerprint records the actual normalized policy.
- A frontier-domain negative remains non-certified even with a large catalogue.
- The depth-0/unit domain never yields a meaningful certified-prime claim.
- A found factorization remains `FACTORS`, never “certified prime,” and carries recomposition evidence.

## Workstream 2 acceptance

No code path can set `seq_prime_is_absolute` or `negative_result_certified` from a domain label alone.

---
