GPT generated; context, prompt Erin Spencer.

# UCNS Reproducibility Guide

## hmm

This guide gives reviewers a short path from repository checkout to the current UCNS v1.0 review surface. It is designed for proof pressure and computational reproduction, not persuasion.

---

## 1. Local setup

Use a clean checkout of the repository, then install the package in editable development mode. UCNS has no runtime dependencies beyond the Python standard library. Development extras are used for packaging checks.

---

## 2. Test surface

Run the full unittest discovery surface under `ucns_recursive/tests/`.

Expected v1.0-prep target: all tests pass.

Important interpretation: `test_depth2_full_domain.py` is a compact closure sweep plus hand-constructed edge cases. It is not a literal exhaustive enumeration over every payload assignment in D'. Its role is `TEST-BACKED`, not proof replacement.

---

## 3. Public API smoke surface

For v1.0, new code should import from `ucns` and `ucns.a0_safe`. The `ucns_recursive` package remains importable as a compatibility/internal implementation surface.

A reviewer should confirm that these public surfaces import successfully:

- `UCNSObject`
- `UNIT`
- `multiply`
- `factor_search_v08`
- `depth_of`
- `factorization_result`
- `ucns.a0_safe.identity`
- `ucns.a0_safe.describe`
- `ucns.a0_safe.canonical`
- `ucns.a0_safe.factor`

---

## 4. Minimal worked examples

The reproducible examples live in:

```text
examples/depth_examples/
```

The example set should include:

- depth-1 minimal seq-prime case
- depth-2 oracle composite case
- depth-3 catalogue-sufficient case
- insufficient-catalogue scoped failure case

Each example should print deterministic status lines and assert either exact recomposition or explicitly scoped failure behavior.

---

## 5. Depth-3 sweep artifact

The depth-3 asymmetric empirical check referenced by Theorem N currently lives under:

```text
code/sweeps/t9_minimal_cat.py
```

If a future branch renames or removes that artifact, update this guide and `docs/claims-ledger.md` in the same pull request.

---

## 6. Interpreting `SEQ-PRIME`

A raw `SEQ-PRIME` from `factor_search_v08` is not automatically a universal primality claim.

External or A0-facing presentations should prefer the `factorization_result` envelope because it carries:

- product identity hash
- domain label
- typed domain-status metadata
- result kind
- `seq_prime_is_absolute`
- claim scope
- explanatory note

`seq_prime_is_absolute` is true only when the product lies in a declared complete domain. Outside that domain, the result must be described as non-absolute and catalogue/domain-scoped.

---

## 7. Release-candidate expectations

Before a v1.0.0 tag, the release candidate should satisfy:

```text
[ ] full unittest discovery passes
[ ] public API smoke surface imports successfully
[ ] example scripts run without assertion failure
[ ] package build succeeds
[ ] package metadata check succeeds
[ ] claims ledger matches README/spec status language
[ ] CHANGELOG includes the release-prep PR
[ ] no known failing test is accepted as v1.0.0-ready
```

## hmmm
