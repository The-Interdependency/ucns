# UCNS evaluator laboratory

**Status:** reproducible candidate-evaluation infrastructure; no canonical evaluator selected.  
**Consumers:** internal UCNS research and validation only.

## Purpose

Canonical structural equivalence, product character `M`, and faithful breadth
`B` remain unresolved. The evaluator laboratory lets multiple versioned
candidates coexist, run against declared laws, expose disagreements, and retain
witness evidence without appointing a default winner.

## Candidate identity

Every `EvaluatorCandidate` records:

- name and evaluator kind;
- version;
- explicit code reference;
- declared scope;
- policy dependencies;
- notes.

Callable identity is not inferred from memory address or bytecode.

## Registry boundary

Candidate names are unique within an evaluator kind. Replacement requires
`replace = true`. The registry provides no `default()`, `best()`, majority vote,
or automatic promotion.

## Explicit comparison

Every `LawSuite` and `compare_candidates()` call requires a named versioned
`ComparisonPolicy`. Exact, absolute, relative, combined, ULP, interval-overlap,
and custom comparison policies may coexist. No hidden numerical tolerance is
permitted.

## Law execution

Law suites retain pass, failure, exception, evidence, comparison-policy name,
and explanatory detail. Reusable laws include:

- null evaluates to zero;
- finite nonnegative output;
- multiplicativity under the actual Cartesian cell pairing law;
- invariance under explicitly declared equivalent witnesses;
- sensitivity under explicitly declared distinct witnesses;
- same-`W`/different-candidate and same-candidate/different-`W` separation.

Not every law applies to every evaluator kind. Applicability is explicit in the
selected suite.

## Reproducible witness evidence

Experiment manifests pin:

- candidate identity;
- witness-corpus digest;
- law-suite digest;
- structural-policy digests;
- comparison policy;
- traversal policy when applicable;
- declared environment.

Subjects are content-addressed only through named versioned `ContentAdapter`
values. UCNS does not hash arbitrary Python objects implicitly.

Witness corpora distinguish development and holdout partitions and record
hand-authored, generated, adversarial, historical, mutation, and metamorphic
origins.

## Candidate comparison

Candidate comparison reports outputs, evaluation errors, and disagreement under
the selected comparison policy. It does not infer that majority agreement is
truth, numerical closeness is structural equivalence, or a passing candidate is
canonical.

## Decision packets

A candidate packet records development and holdout reports, minimized
counterexamples, retained alternatives, information loss, rollback behavior,
and separate candidate, witness, and decision authorship.

A packet is reviewable only with passing holdout evidence and rollback behavior.
Reviewable does not mean canonical; `CandidateDecisionPacket.canonical` remains
false.

## Initial candidates

The repository supplies explicit noncanonical equivalence, cell-only `M`, and
`B` candidate families described in [`CANDIDATE_PACKS.md`](CANDIDATE_PACKS.md).
They exist to produce pressure, disagreements, and counterexamples.

## Canonization boundary

A candidate may become canon only through a separate explicit decision recording:

- selected candidate and version;
- code identity and scope;
- laws, witnesses, comparison, traversal, and holdout evidence;
- alternatives retained or rejected;
- information lost;
- rollback and migration behavior;
- decision authority.

No such selection is made by this laboratory.

hmmm: external holdout custody and independent calibration remain evidence
obligations outside the candidate's own implementation.
