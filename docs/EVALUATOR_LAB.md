# UCNS evaluator laboratory

**Status:** candidate-evaluation infrastructure; no canonical evaluator selected.  
**Consumers:** internal UCNS research and validation only.

## Purpose

Canonical structural equivalence, product character `M`, and faithful breadth `B` remain unresolved. The evaluator laboratory allows multiple candidates to coexist, run against declared laws, expose disagreements, and retain their witness evidence without appointing a default winner.

## Required objects

- `EvaluatorKind`: equivalence, product character, faithful breadth, or an explicitly named future kind.
- `EvaluatorCandidate`: name, kind, callable evaluator, declared policy dependencies, and status notes.
- `EvaluatorRegistry`: stores multiple candidates per kind and has no implicit default.
- `Witness`: retained test subjects and the relation or law they are intended to pressure.
- `Law`: a named check applied to one candidate.
- `LawResult`: pass/fail/error plus evidence and explanatory detail.
- `LawSuite`: an ordered collection of laws.
- `EvaluationReport`: all law results for one candidate.
- `CandidateComparison`: candidate outputs for one subject and whether they disagree.
- `compare_candidates()`: evaluates candidates side by side without ranking them.

## Registry boundary

Candidate names are unique within an evaluator kind. Replacing a candidate requires an explicit `replace = true` operation.

The registry does not provide `default()`, `best()`, or automatic promotion. Callers must name the candidate or request all candidates of a kind.

## Law execution

A law receives the candidate and returns a `LawResult`. Exceptions are captured as failed results rather than terminating the suite or being mistaken for evidence.

Law suites may be assembled from reusable constructors, including:

- null evaluates to zero;
- output is finite and nonnegative on declared subjects;
- multiplicativity under the actual carrier pairing law;
- invariance under explicitly declared equivalent pairs;
- sensitivity under explicitly declared distinct pairs;
- same-`W`/different-`M` and same-`M`/different-`W` separation witnesses.

The laboratory does not assume that every law applies to every evaluator kind. Applicability is explicit in the selected suite.

## Comparison boundary

Candidate comparison reports outputs and disagreements. It does not infer that majority agreement is truth, that numerical closeness establishes equivalence, or that a passing candidate is canonical.

Subjects and outputs remain attached to the comparison record so later review can reproduce the disagreement.

## Canonization boundary

A candidate may become canon only through a separate explicit decision that records:

- the selected candidate and version;
- the laws and witnesses it passed;
- alternatives retained or rejected;
- information lost by the choice;
- rollback and migration behavior.

No such selection is made by this laboratory.

hmmm: the first candidate suite should pressure actual retained layers and explicit structural policies before any `M` or `B` implementation is promoted.
