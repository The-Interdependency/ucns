# TestPyPI release-candidate validation

## Purpose

The `TestPyPI release-candidate validation` workflow establishes the publication boundary required before any public PyPI or final `v1.0.0` decision.

It is deliberately narrower than a release workflow:

- it can publish only the existing `ucns==1.0.0rc1` candidate to TestPyPI;
- it can validate an already-published TestPyPI candidate without uploading again;
- it runs only by explicit manual dispatch from `main`;
- publication uses the protected `testpypi` GitHub environment and trusted publishing;
- it does not create a Git tag, GitHub Release, final `v1.0.0`, or public PyPI upload;
- it does not promote Theorem N beyond `FRONTIER`.

## Prerequisite repository configuration

Configure a TestPyPI trusted publisher for:

```text
project: ucns
github owner: The-Interdependency
repository: ucns
workflow: testpypi-release-candidate.yml
environment: testpypi
```

Protect the `testpypi` environment with required reviewers if available. The workflow receives `id-token: write` only in its publish job.

No long-lived TestPyPI API token is required or expected.

## Publish and validate

In GitHub Actions, select **TestPyPI release-candidate validation**, choose the `main` branch, and run with:

```text
operation: publish-and-validate
confirmation: publish-ucns-1.0.0rc1-to-testpypi
```

The workflow will:

1. prove it is running in `The-Interdependency/ucns` from `refs/heads/main`, and check out the exact commit the dispatch resolved to (a later push to `main` cannot change what this run tests or uploads);
2. verify the package name and exact version `1.0.0rc1` from `pyproject.toml`;
3. install supported release tooling;
4. run the complete Python test suite;
5. build the sdist and wheel;
6. run `twine check`;
7. install the built wheel into a clean environment and re-run the public import-boundary smoke test from outside the checkout, so the repository source tree cannot shadow the installed wheel;
8. upload the immutable distribution artifact as Actions evidence;
9. publish only to TestPyPI through trusted publishing;
10. install `ucns==1.0.0rc1` from TestPyPI in a fresh environment with bounded retries;
11. download the TestPyPI wheel and require its packaged contents to be identical to this run's built wheel (generator `WHEEL`/`RECORD` metadata excluded), so a stale candidate published from a different commit fails rather than validating;
12. verify package metadata, public imports, and the deprecated-import firewall.

TestPyPI does not permit overwriting an existing filename/version. After the candidate is present, use the validation-only operation rather than attempting another upload.

## Validate an existing candidate

Use:

```text
operation: validate-existing
confirmation: validate-ucns-1.0.0rc1-on-testpypi
```

This repeats source tests, local build checks, clean-wheel checks, the fresh TestPyPI install, and the wheel-content binding check without invoking the publisher job. Because the binding check compares the immutable TestPyPI wheel against the wheel built from the dispatched commit, validation passes only when the published candidate still matches the current `main` source.

## Failure meanings

- **Repository/ref preflight fails:** dispatch was not from `main` or not from the canonical repository.
- **Version preflight fails:** the source tree is not the declared `1.0.0rc1` candidate; rotate the workflow deliberately for a later candidate.
- **Build or tests fail:** the candidate is not publication-ready.
- **Publish authorization fails:** the `testpypi` environment or trusted-publisher binding is absent or mismatched.
- **Upload says the file already exists:** switch to `validate-existing`; TestPyPI artifacts are immutable.
- **Fresh install fails after retries:** the publication is unavailable or malformed and the TestPyPI gate remains open.
- **Wheel-content binding fails:** the immutable TestPyPI `1.0.0rc1` was built from a different source state than the dispatched commit; it is not evidence for the current candidate, and a later candidate version must be rotated in deliberately.

## Evidence boundary

A successful workflow establishes that one exact source commit produced installable TestPyPI artifacts matching the declared package/version and public import boundary.

It does not establish:

- a final public release decision;
- a `v1.0.0` tag;
- public PyPI availability;
- total general recursive primality;
- completion of Theorem N's `sorry`-closed Lean obligations;
- external formal review;
- downstream proof or measurement validity.

## hmmm

The first successful TestPyPI run is still an operational event, not a theorem. A package may cross a publication boundary while its explicitly recorded mathematical frontier remains exactly where the evidence says it is.
