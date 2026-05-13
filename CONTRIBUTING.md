# Contributing to UCNS

Thank you for your interest in the Unit Circle Number System project.

UCNS is currently a research-stage mathematical and computational system. Contributions are welcome in four broad categories:

- mathematical formalization
- implementation correctness
- packaging / tooling
- empirical verification

## Priority areas

Current high-value contribution areas:

1. Formal mathematical definitions
2. Counterexamples and adversarial constructions
3. Proof review and theorem separation
4. Packaging / CI hardening
5. Catalogue minimization strategies
6. Complexity analysis
7. Cross-language implementations

## Contribution guidelines

Please clearly distinguish between:

- theorem
- proof sketch
- empirical observation
- implementation behavior
- conjecture
- speculation

The repository intentionally preserves exploratory artifacts alongside defended implementation layers. Maintaining this distinction is critical.

## Development setup

```bash
git clone https://github.com/The-Interdependency/ucns.git
cd ucns
python -m pip install -e .[dev]
python -m unittest discover ucns_recursive/tests/ -v
```

## Packaging checks

```bash
python -m build
python -m twine check dist/*
```

## Style

- Prefer explicitness over compression.
- Keep theorem claims bounded and testable.
- Preserve historical artifacts when superseded; mark them clearly.
- Avoid silently changing theorem-status language.

## Licensing

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

GPT generated; context, prompt Erin Spencer.
