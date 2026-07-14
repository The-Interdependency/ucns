# UCNS Codex handoff index

The repository's Codex assignments are partitioned into ordered files under [`codex-handoff/`](./codex-handoff/) so each package remains independently reviewable. Read the root index and every file belonging to an active assignment before editing code.

## Historical v1.0 completion package

The first eight files preserve the original UCNS v1.0 completion handoff:

1. [`00-overview-and-branch-discipline.md`](./codex-handoff/00-overview-and-branch-discipline.md)
2. [`01-exhaustive-payload-factor-search.md`](./codex-handoff/01-exhaustive-payload-factor-search.md)
3. [`02-negative-result-certification.md`](./codex-handoff/02-negative-result-certification.md)
4. [`03-oracle-catalogue-equivalence.md`](./codex-handoff/03-oracle-catalogue-equivalence.md)
5. [`04-complete-quotient-consumers.md`](./codex-handoff/04-complete-quotient-consumers.md)
6. [`05-nonempty-immutable-object-model.md`](./codex-handoff/05-nonempty-immutable-object-model.md)
7. [`06-codec-claims-license.md`](./codex-handoff/06-codec-claims-license.md)
8. [`07-compatibility-validation-definition-of-done.md`](./codex-handoff/07-compatibility-validation-definition-of-done.md)

That package's behavioral outcomes, safety boundaries, tests, and completion conditions remain historical evidence. Do not reopen or reinterpret them merely because later structural packages were added.

## Completed follow-on package: internal structure and geometric coordinates

9. [`08-idempotents-local-groups-2i-no-go.md`](./codex-handoff/08-idempotents-local-groups-2i-no-go.md)
10. [`09-radius-breadth-fork-semantics.md`](./codex-handoff/09-radius-breadth-fork-semantics.md)

These files formed one ordered structure-only assignment and were implemented through PR #116. The implementation lives in `ucns/relational_geometry.py`, the corrected audit projection in `ucns/geometry_bridge.py`, the executable witness in `contracts/test_local_groups_and_geometry.py`, and the written proof in `docs/local-groups-and-relational-geometry.md`.

The completed dependency chain is:

```text
stored-angle unit convention
  -> normalized carrier and closed product
  -> idempotent census
  -> four-equation local-group census
  -> every internal subgroup is abelian
  -> every 2I homomorphism is constant at an idempotent
  -> recursive radius rho composes by max
  -> breadth lambda composes by addition
  -> every internal subgroup lies on the zero-breadth spindle
  -> fork profile remains a derived nonlinear observable
  -> Phi policy and integration lint must enforce constitutive-simultaneous forks
  -> integration schema must use external rho-action slots, not embedded-group slots
```

The UCNS portion is complete and specification-defended/test-backed under the evidence recorded on PR #116. The downstream Phi policy, METAPAT fork declaration, integration lint, sphere fixture, quaternionic lift, fiq metering, prime-cylinder projection, EDCM measurement, and comparative embedding experiments remain separate future assignments.

## Published state

- Repository: `The-Interdependency/ucns`
- Handoff 08 merged through PR #113, commit `0dfff853d641b7d00e19b8eff68d1fc4cb3e8d7c`
- Handoff 09 merged through PR #114, commit `64367dbb89694d7f69fc17156822bd2bedebbe81`
- Handoffs 08 and 09 implemented through PR #116, commit `515dd69dd1dda1ff47c11a787b0cb78828674b82`
- Evidence runs for PR #116: manifest #217, CI #330, package matrix #303
- The results are not Lean-checked and make no METAPAT, fiq, EDCM, quaternionic-lift, or embedding-performance claim

## hmmm

The internal structure package is closed. The next uncertainty is downstream and semantic: which METAPAT-to-UCNS encoding earns the right to use payload forks as constitutive simultaneity, and how the integration layer proves it did not hide ordinary graph edges inside recursion.
