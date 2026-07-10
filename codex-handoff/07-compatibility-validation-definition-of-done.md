# Cross-workstream compatibility requirements

- Preserve the legacy `factor_search_v08(P, catalogue=None, prune=True)` tuple-or-sentinel API.
- Route A0-facing claims through the structured result envelope, not the raw sentinel.
- Update `ucns.a0_safe.factor` to expose the new certification metadata without allowing caller assertions to bypass validation.
- Update `ucns.__init__` and `ucns_recursive` wrappers for deliberate new public APIs.
- Keep `ucns` standard-library-only at runtime.
- Preserve supported Python classifiers 3.8, 3.10, 3.11, and 3.12.
- Avoid syntax unavailable on Python 3.8.
- Do not make code under `code/` or the historical snapshot files the production source of truth.
- Preserve exact recomposition checks even after exhaustive enumeration makes candidates more trustworthy.
- Do not weaken tests, delete counterexamples, or change expected results solely to obtain green CI.
- Every caught exception must have a reason. Never catch a completeness/limit error and return a negative sentinel.

---

# Required validation loop

For each workstream:

1. Write or enable a regression that fails for the old behavior.
2. Run the narrowest relevant test and confirm the intended failure.
3. Implement the smallest coherent behavior change.
4. Run the focused test set until green.
5. Run all directly affected contract and compatibility tests.
6. Continue to the next workstream only when the current acceptance criteria are met.

Before declaring completion, run all repository-authoritative checks that apply.

## Python and contracts

```bash
python -m pip install -e '.[dev]'
python -m pytest ucns_recursive/tests tests -v
python audit/reconcile.py
```

PR #96’s contract suites must be collected through their CI shim. Also run the quotient and new completion contracts directly when diagnosing failures.

## Manifest integrity

```bash
(
  cd .agents/skills/manifest
  sha256sum -c generate.py.sha256
)
python .agents/skills/manifest/generate.py --root . --check
```

If the generated block legitimately changes:

```bash
python .agents/skills/manifest/generate.py --root . --write
python .agents/skills/manifest/generate.py --root . --check
```

## Distribution and import boundary

```bash
rm -rf build dist
python -m build
python -m twine check dist/*
```

Reproduce the wheel-install and public-import-boundary smoke test from `.github/workflows/python-package.yml`. Confirm that the built wheel imports `ucns`, exposes the deliberate new APIs, and does not import through `ucns_recursive`.

## Formal/status validation

Because current formal-status documentation will change, use the pinned Lean toolchain and run:

```bash
source "$HOME/.elan/env"
(
  cd formal
  lake exe cache get
  lake build
  lake build Ucns.CarrierLcm
)
```

Mirror the executable `admit`/`axiom` rejection and targeted `CarrierLcm.lean` `sorry` rejection from `.github/workflows/carrier-lcm-target.yml`. Report remaining documented frontier `sorry` leaves honestly; do not call them proofs.

## Supported Python matrix

The final PR must pass the repository’s Python 3.8, 3.10, 3.11, and 3.12 GitHub Actions matrix. A local check on only one interpreter is not enough for a compatibility claim. If a matrix lane fails, inspect and repair it before completion.

## Final stale-claim and consumer searches

Run and inspect, not merely execute:

```bash
git grep -nE 'find_left_factor_or_sentinel|find_right_factor_or_sentinel|left_quotient\(|right_quotient\('
git grep -nE 'partially verified in Lean|no false negative|SEQ-PRIME|absolute|oracle atom|dict\[Hashable'
git grep -nE 'MPL-2.0|Apache-2.0'
git status --short
git diff --check
```

Every remaining hit must be correct in context or explicitly historical/scoped.

---

# Definition of done

Do not mark the handoff complete until all statements below are true:

- [ ] The tower false-negative regression returns exact factors.
- [ ] Payload assignment enumeration equals brute force on the bounded oracle tests.
- [ ] Factor search exhausts assignments and face options before `SEQ-PRIME`.
- [ ] Search truncation or exceptions cannot become a negative result.
- [ ] No custom catalogue produces a certified negative without machine-checked coverage.
- [ ] Catalogue certificates bind to the exact catalogue, domain, and rule version.
- [ ] Oracle-atom classification is extensionally identical to canonical-catalogue membership.
- [ ] The bounded-but-noncatalogue witness is non-oracle.
- [ ] Plural quotient APIs are public and all completeness-claiming consumers use them.
- [ ] Recursive noncommutative right quotient is tested.
- [ ] Store retrieval surfaces every valid remainder it claims to surface.
- [ ] Empty `UCNSObject` construction is impossible.
- [ ] A constructed `UCNSObject` is recursively immutable and hash-stable.
- [ ] All algebra, serialization, store, codec, and compatibility tests pass with immutable tuples.
- [ ] New dictionary encodings preserve supported key types and reject duplicate decoded keys.
- [ ] Legacy dictionary decoding is safe against unhashable or colliding keys.
- [ ] README and claims ledger state the exact executable, catalogue, oracle, and formal boundaries.
- [ ] Root package/release metadata consistently says Apache-2.0.
- [ ] Full Python tests, contract reconciliation, manifest checks, package build/twine checks, wheel smoke test, formal/status checks, and the Python version matrix pass.
- [ ] The PR body contains the required file plan, behavior changes, risks, compatibility notes, and exact validation outcomes.

---

# Required final Codex report

Return a completion report in this exact shape:

```markdown
## Base and head
- Starting base:
- Final head:
- PR #96 integration state:

## Delivered work
### 1. Exhaustive payload/factor search
...
### 2. Negative-result certification
...
### 3. Oracle/catalogue equivalence
...
### 4. Complete quotient consumers
...
### 5. Immutable nonempty object model
...
### 6. Codec, claims, and license
...

## Public API changes
...

## Compatibility and migration notes
...

## Regressions added
- path::test_name — defect protected

## Validation actually run
- command — PASS/FAIL — concise result

## GitHub Actions matrix
- workflow/job — PASS/FAIL — run reference

## Remaining hmmm
...
```

Distinguish checks that passed from checks that were not available. Do not report a check as passing based on expectation or on a different command.

---

## hmmm

The only expected live uncertainty at execution start is whether `main` has advanced after this handoff was published. Inspect any new commits rather than guessing about their effect. PR #96 is already integrated. The six behavioral outcomes, safety boundaries, and completion tests above are not `hmmm`; they are the assignment.
