# UCNS stack repair — completed looks like

The UCNS repair is complete only when every applicable statement below is true and evidenced by code, tests, formal artifacts, current claims documentation, or release outputs.

## Theorem and implementation alignment

- **Completed looks like:** Theorem N is stated as an exhaustive-inclusion completeness target for finding a valid factorization.
- **Completed looks like:** no current theorem explanation depends on general cancellativity, quotient uniqueness, or recovery of the original factor pair.
- **Completed looks like:** the documented proof shape matches the actual split, host, payload, face, witness, non-unit, and recomposition stages in the Python solver.
- **Completed looks like:** Theorem N remains `FRONTIER` wherever the faithful formal proof or external review remains incomplete.
- **Completed looks like:** claims ledger, README, theorem note, changelog, examples, docstrings, formal README, and obligation ledger use consistent status language.

## Faithful formal target

- **Completed looks like:** formal success means that actual factor witnesses exist and exactly recompose to the product.
- **Completed looks like:** `FindsFactorization` is no longer an opaque proposition standing in for the entire solver.
- **Completed looks like:** finite catalogue candidates, split candidates, payload assignments, face assignments, unit rejection, and recomposition acceptance are formally represented.
- **Completed looks like:** remaining `sorry` and opaque boundaries are enumerated in `audit/obligation_ledger.md` with no hidden assumptions.
- **Completed looks like:** small Python/Lean conformance fixtures enumerate the same valid witness space in their declared domain.
- **Completed looks like:** a successful Lean build is never described as proof while any transitive theorem hole remains.

## Constructor boundary

- **Completed looks like:** public constructors reject empty object sequences.
- **Completed looks like:** public constructors reject non-positive declared or supplied intrinsic carriers.
- **Completed looks like:** mismatched anchor/face lengths and non-bit faces fail clearly.
- **Completed looks like:** recursive payload type behavior is explicit and tested.
- **Completed looks like:** adversarial constructor tests exist in both the current public API tests and the compatibility test surface.
- **Completed looks like:** valid historical fixtures and supported compatibility imports continue to work.

## Cross-repository bridge

- **Completed looks like:** UCNS owns one official versioned neutral bridge record and import/export adapter.
- **Completed looks like:** every imported bridge object becomes an actual `ucns.UCNSObject`, not a sibling-repository imitation.
- **Completed looks like:** export/import round trip preserves UCNS equality and stable hash.
- **Completed looks like:** external provenance and canon tags survive round trip without changing UCNS equality unless an explicit ratified rule says otherwise.
- **Completed looks like:** malformed schemas, unsupported versions, invalid carriers, invalid faces, and invalid recursive records fail closed.
- **Completed looks like:** successful construction or round trip carries no implicit theorem status.

## Downstream evidence boundary

- **Completed looks like:** consumers can distinguish construction success, finite search exhaustion, validated catalogue coverage, certified domain-relative negative results, theorem status, and absence of proof status.
- **Completed looks like:** no bare domain label, object hash, import success, or geometry equivalence promotes a result to certified or defended.
- **Completed looks like:** bridge metadata cannot forge catalogue coverage, search provenance, or negative certification.
- **Completed looks like:** raw `factor_search_v08` remains catalogue-relative and the evidence-bearing envelope remains the only negative-certification surface.

## Shared stack contract

- **Completed looks like:** a METAPAT semantic module can be represented through the official UCNS bridge.
- **Completed looks like:** EDCM can consume the resulting actual UCNS object for geometry or measurement construction.
- **Completed looks like:** EDCM output preserves `NA != 0`.
- **Completed looks like:** no UCNS theorem status appears in EDCM measurement output merely because UCNS geometry was used.
- **Completed looks like:** canon or manifest digest changes are visible in provenance identity.
- **Completed looks like:** canonical shared fixture data is owned by UCNS and sibling copies have pinned provenance and drift checks.

## Verification and release

- **Completed looks like:** package build, `twine check`, clean-wheel installation, import smoke test, full public and compatibility tests, contract tests, depth examples, and docs claim guardrails pass.
- **Completed looks like:** `lake build Ucns.CarrierLcm` remains clean.
- **Completed looks like:** the faithful finite-search formal target builds with every unresolved proof hole disclosed.
- **Completed looks like:** repo-local skill-lib drift and msdmd checks report clean.
- **Completed looks like:** no release artifact or public text makes universal primality, uniqueness, general cancellation, tractability, or proof-completion claims unsupported by the evidence.

## Final boundary

- **Completed looks like:** a coding specialist can inspect one UCNS public object and determine separately:

  1. its mathematical identity;
  2. its external provenance;
  3. the finite search boundary used;
  4. whether catalogue coverage was validated;
  5. whether a negative was certified and within which domain;
  6. which theorem-status vocabulary applies;
  7. what remains `FRONTIER` or `hmmm`.

## hmmm

Completion does not require the formal search model to copy Python optimization details. Completion requires a proved or test-backed correspondence to the valid witness space, with no opaque success-name substituting for the actual result.