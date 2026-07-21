# UCNS explicit comparison policies

**Status:** candidate-research infrastructure; no numerical equality policy is canonical.

## Purpose

Numerical equality is itself a choice. A fixed hidden tolerance can erase meaningful small differences, reject equivalent large values, or confuse floating-point saturation with mathematical identity.

Every candidate comparison and law suite therefore names a `ComparisonPolicy`.

## Initial modes

- exact equality;
- absolute tolerance;
- relative tolerance;
- combined relative and absolute tolerance;
- units-in-last-place distance;
- interval overlap;
- custom domain comparator.

Each policy is named, versioned, and records its parameters. A `ComparisonRegistry` preserves multiple policies without appointing a default. Replacement requires an explicit operation.

## Boundary

Comparison policies decide only whether two reported outputs match under a declared rule. They do not establish structural equivalence, candidate correctness, or canonical numerical representation.

## Required evidence

Experiment manifests pin the selected comparison policy and its parameters. Law reports record the policy name used.

hmmm: rational, symbolic, interval, arbitrary-precision, and domain-unit comparisons remain available future policies rather than being collapsed into binary-float tolerance.