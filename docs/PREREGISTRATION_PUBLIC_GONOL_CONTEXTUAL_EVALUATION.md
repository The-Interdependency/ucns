# Public Gonol contextual-function structural evaluation

**Authority:** Erin Spencer

**Recorded:** 2026-08-18

**Status:** resource-run repair preregistered before replacement evaluation

**Selection effect:** none

## Decision

This is a bounded structural-control test. It asks whether the sealed Public
Gonol definition-derived function table retains the exact canonical-index and
ordered-context distinctions already represented by source-bound atomic
closure, rather than collapsing to an identity-only control.

It does **not** test whether the definitions are useful, grammatically correct,
semantically true, contextually appropriate, or canonical. A surviving result
would be `SURVIVED — not proved`, limited to the constructed table and this
control. It cannot promote a punctuation grammar, parser, precedence rule,
measurement claim, or UCNS canon.

## Frozen inputs

| Input | Exact identity |
|---|---|
| Parent UCNS state | `564765e34651c83c26b7047d8085fd874e0b7f6d` |
| Function-table receipt | SHA-256 `cabaa71bbae531993c2522e3e8cf30e26f37fcec030c1014f3495a5de62d9f69` |
| Function-table identity | `ucns.public-gonol-function-table:sha256:05e8b6d3c14a34c409343cfee6fec7db9e507cbb179a6b97a606a1d093d1fc10` |
| OEWN definition-layer receipt | SHA-256 `bcfbf0c724a8507e00d1d3205f32de2cce489731ce019a2f883e90abd56f7c5c` |
| OEWN definition-layer identity | `ucns.oewn-definition-layer:sha256:e9bc04c98c3663287f9fda1bf17431fb6cffc102ec347294ad02db4007f4aa57` |
| OEWN Core source receipt | `ucns.oewn-core-receipt:sha256:3ea1f9f0d60bb0c440d7bcb6375050673c0cd03b774f87fed9e4be223bc3c973` |
| Frozen Public Gonol | SHA-256 `55d10c84529a4d7bc7714786357e977b68d9df2ac3f73d20e229580b552c2ef5` |

The source cache must be available locally. The evaluator will make no network
request and will reject a source, definition-layer, function-table, or Public
Gonol identity mismatch before producing an outcome.

This protocol supersedes the historical preregistration identity
`ucns.public-gonol-contextual-protocol:sha256:ea7f9e55b114c91781358c41b8d71a1b459ca39431f39395112d8d64d110c526`
and blocker identity
`ucns.public-gonol-contextual-evaluation-blocker:sha256:5a74f083892fe9e95b3c314c5764e675fcd1e06e1c121ab8dcf535952725feaf`
only for this reason: that historical protocol contained an unauthorized
arbitrary runtime bound. The old blocked receipt remains preserved evidence of
that stopped attempt; it is not reinterpreted as a contextual-function result.

## Frozen probe and control

The target set is all 84 declared punctuation/symbol positions in the sealed
function table. The test anchor is fixed mechanically, before evaluation, to
function index `2`, binding ordinal `0`, definition ordinal `0`. Its definition
gonol initializes the current atomic state. The anchor is a deterministic
existing table member; it was not chosen from an observed result.

Every probe function, including the anchor, is the already-gonolized OEWN
definition or definitions bound in the sealed table. Those definitions are the
only source-authored examples admitted here. The evaluator does not inspect or
tune against their English text, convert them into a new punctuation grammar,
or introduce an independently authored example fixture.

For every target index, the later evaluator will call the existing
`apply_public_gonol_function` with precisely these caller-supplied contexts:

| Context label | Ordered anchor multiplicity |
|---|---:|
| `empty` | 0 |
| `anchor-once` | 1 |
| `anchor-twice` | 2 |

The control is fixed as
`return-current-state-regardless-of-index-or-context`. It ignores all function
indices and all context. Neither the probe nor the control selects a syntax,
operator position, parsing rule, or semantic interpretation.

## Frozen decision rule

The candidate must meet every condition:

1. Within each of the three contexts, the 84 target applications have exactly
   84 distinct result identities.
2. For every target index, both ordered context transitions change the result:
   `empty → anchor-once` and `anchor-once → anchor-twice` — 168 changes total.
3. The identity-only control has exactly one result identity in each context
   and zero changing transitions.
4. The candidate therefore strictly exceeds the control on both frozen
   dimensions: `84 > 1` and `168 > 0`.
5. Two independent complete source builds emit byte-identical execution
   receipts.

If all five conditions hold, record `SURVIVED — not proved`. Any index
collision, missing target, unchanged required transition, incorrect control
count, non-identical replay, or negative per-run metric is `FALSIFIED`; do not
adjust definitions, aliases, anchor, contexts, baseline, metric, or threshold.
A missing pinned source, failed identity check, failed resource preflight, or
real resource emergency is `BLOCKED`. Every non-surviving status stops this
test rather than repairing it in place.

## Resource and serialization rules

- exactly two complete source builds; no retry or third deciding run;
- resource preflight before compute, following
  `The-Interdependency/skill-lib@e284d02e7d4bedbbcf8481426a389b1d5e39551b:RESOURCE_RUN_INVARIANT.md`;
- no artificial wall-clock stopping rule;
- no artificial memory stopping rule; memory is observed, not used as a
  scientific cutoff;
- once started, each healthy source build runs to its natural terminal
  condition;
- deterministic canonical UTF-8 JSON with sorted keys and a terminating
  newline;
- preserve target/result identities, aggregate counts, elapsed time, peak
  memory, source identities, and the exact frozen protocol identity;
- freeze each complete result before byte comparison; and
- use an evaluator implementation distinct from the function-table producer.

The protocol-only receipt is
`generated/public-gonol-contextual-evaluation-preregistration.json`. It is
outcome-free and exists before the replacement execution result receipt.
Its SHA-256 is
`92fe7963af52c60d79b55a157eba747b8624eab54ffd8a336bcbcc06ded2b910` and
its protocol identity is
`ucns.public-gonol-contextual-protocol:sha256:6129ef20a93eb925e95a52af11341a30f933302be1f60024e42215611abe6e3d`.

## Usage guidance

Regenerate only the outcome-free protocol receipt:

```bash
uv run --extra test python -m ucns.public_gonol_contextual_protocol \
  generated/public-gonol-contextual-evaluation-preregistration.json
```

After confirming the local OEWN checkout and resource preflight are sufficient,
execute the complete two-build evaluation:

```bash
uv run --extra test python -m ucns.public_gonol_contextual_evaluation \
  /home/wayseer_interdependentway_org/.cache/oewn-2025 \
  generated/public-gonol-contextual-evaluation-result.json \
  generated/public-gonol-contextual-resource-observations.json
```

Once the evaluation starts, let it reach its natural terminal condition unless
the user explicitly cancels it or a real resource emergency occurs.

## Domain claim

| Field | Declaration |
|---|---|
| Surface | definition-derived contextual function |
| Term identity | `ucns.public_gonol.contextual_function_structural_discrimination` |
| Claiming domain | UCNS |
| Claim type | specialized candidate structural test |
| Scope | the frozen table, anchor, three ordered contexts, and identity-only control above |
| Authority | Erin Spencer's Public Gonol function-table direction and source-bound OEWN construction |
| Included | exact index binding, definition-gonol membership, atomic closure, context order and multiplicity |
| Excluded | semantic efficacy, grammar, parsing, precedence, context authority, EDCM validity, canon |
| Standing | resource-run repair preregistered; no outcome recorded |

Unicode names only locate existing OEWN evidence. Where the table carries an
explicit source-present alias, the alias remains frozen evidence, not an
alternate function claim. This protocol selects no competing semantic authority.

## hmmm

Whether these closures produce useful contextual behavior requires a separately
authorized task, source-authored examples, and outcome authority. This control
cannot determine natural-language punctuation, domain-specific symbol senses,
or a general function grammar.
