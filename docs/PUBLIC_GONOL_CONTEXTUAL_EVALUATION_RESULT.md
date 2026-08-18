# Public Gonol contextual-function structural evaluation result

**Authority:** Erin Spencer

**Recorded:** 2026-08-18

**Status:** `SURVIVED — not proved`

**Selection effect:** none

## Protocol

This result executes the resource-run repair protocol:

- protocol identity:
  `ucns.public-gonol-contextual-protocol:sha256:6129ef20a93eb925e95a52af11341a30f933302be1f60024e42215611abe6e3d`;
- protocol commit:
  `e97617c360a6a1d783f3f89f60a23194846b98aa`;
- exact local OEWN 2025 Core checkout:
  `/home/wayseer_interdependentway_org/.cache/oewn-2025`;
- source checkout commit:
  `dc343f2683279ecbb13fab4e2fd778d7b162d287`;
- two independent complete source builds required and completed;
- no artificial wall-clock stopping rule;
- no artificial memory stopping rule; and
- no tuning, retry, third deciding build, or changed result criterion.

The repaired protocol supersedes the historical 420-second protocol only
because that runtime bound was unauthorized and not load-bearing to the
structural claim. The old blocker remains preserved evidence and is not
rewritten into a result.

## Result

The completed semantic receipt is
`generated/public-gonol-contextual-evaluation-result.json`:

- file SHA-256:
  `06a6cf3158c4934440094fb639330d673f451b0a607fb96b9dd0bc47470ca60e`;
- evaluation identity:
  `ucns.public-gonol-contextual-evaluation:sha256:f9f995b1f73949411d9402364a637cc978c09db6e460f0ab7a7c15e4b1ba4c8b`;
- semantic run receipt SHA-256:
  `d5f5231e8617f38b78430158c33f91f8be782c1c92d07ca9ce46d9c994a14053`;
- completed full source builds: `2`;
- independent replay: byte-identical; and
- status: `SURVIVED — not proved`.

Frozen metric result:

| Metric | Result |
|---|---:|
| Candidate distinct results in `empty` context | 84 |
| Candidate distinct results in `anchor-once` context | 84 |
| Candidate distinct results in `anchor-twice` context | 84 |
| Candidate context changes | 168 |
| Required candidate context changes | 168 |
| Identity-only distinct results in each context | 1 |
| Identity-only context changes | 0 |
| Direct application replay agrees | true |

The candidate therefore satisfied the frozen structural-control rule against
the identity-only baseline for the sealed function table, anchor, contexts, and
target indices.

## Resource observations

The resource receipt is
`generated/public-gonol-contextual-resource-observations.json`:

- file SHA-256:
  `d140e6a11c0259edee3cc0d433cbd45a2fdcddd1b5e7939a0e01a90887ceacff`;
- resource observation identity:
  `ucns.public-gonol-contextual-resource-observations:sha256:46a4ba94fb9ee8c748ce268db0fb1f222398912f15c6bc467b3ce1b733860b2c`;
- preflight: source present, no network/API quota required, no artificial
  wall-clock or memory limit;
- first build elapsed: `298733053267` ns;
- second build elapsed: `306699794272` ns;
- peak process memory observed: `1455644672` bytes; and
- both observations reached `completed-source-build-and-contextual-metric`.

## Nonclaims

`SURVIVED — not proved` is limited to exact structural discrimination relative
to the identity-only control. It does not establish semantic usefulness,
punctuation grammar, parsing, precedence, context-selection authority, EDCM
measurement validity, canonical UCNS semantics, or a general function law.

## Usage guidance

Reproduce the result from a fresh checkout with the exact local OEWN source
checkout available:

```bash
uv run --extra test python -m ucns.public_gonol_contextual_evaluation \
  /home/wayseer_interdependentway_org/.cache/oewn-2025 \
  generated/public-gonol-contextual-evaluation-result.json \
  generated/public-gonol-contextual-resource-observations.json
```

Once the evaluator starts, let both complete source builds reach their natural
terminal condition unless the user explicitly cancels the run or a real resource
emergency occurs.

## Deprecated blocker

The historical blocker remains:

- blocker identity:
  `ucns.public-gonol-contextual-evaluation-blocker:sha256:5a74f083892fe9e95b3c314c5764e675fcd1e06e1c121ab8dcf535952725feaf`;
- historical protocol identity:
  `ucns.public-gonol-contextual-protocol:sha256:ea7f9e55b114c91781358c41b8d71a1b459ca39431f39395112d8d64d110c526`; and
- status: `DEPRECATED` by resource-run repair, not deleted.

## hmmm

Whether definition-derived contextual functions are useful outside this
structural-control test remains unresolved. Testing semantic efficacy,
source-authorized contexts, grammar, parsing, precedence, EDCM measurement
validity, or UCNS canon requires a separate preregistered experiment.
