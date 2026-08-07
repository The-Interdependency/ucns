# UCNS work-graph reports

Machine consumers should start with [`repository-plan-report.json`](repository-plan-report.json) when asking what part UCNS plays in the wider Interdependency plan.

The report is **repo-owned**: UCNS remains authoritative for its own system definition, mathematical/geometric candidates, provenance, and scoped proof/status evidence. `skill-lib` may aggregate this report into an organization-level plan, but aggregation does not transfer UCNS authority or promote candidate evidence to canon.

The report pins the exact UCNS source commit it describes and the frozen `skill-lib` repository-plan-report contract (`the-interdependency.repository-plan-report` v1.0.0, schema Git blob `9b347b2dff7692054b571602f30ee6d00c2e7265`). A later agent should treat a newer `main` commit as a possible staleness boundary and refresh or review the report rather than silently assuming it still describes the repository.

`STACK_MANIFEST.json` remains a separate work-specific cross-repository identity record. It is not replaced by this repo-level portfolio report.

## hmmm

The report contract is frozen, but organization-wide automatic repository discovery remains intentionally unresolved. Portfolio completeness therefore depends on the explicit report set supplied to the `interdependent-work-graph` aggregator.
