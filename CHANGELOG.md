# Changelog

## v0.8.1 — PyPI Release Candidate

### Packaging
- Added enriched PyPI metadata and classifiers.
- Added project URLs and author metadata.
- Added build + twine validation workflow.
- Added wheel build dependency.

### CI
- GitHub Actions workflow now:
  - builds the package
  - validates metadata via twine
  - installs built wheel artifact
  - runs the UCNS test suite

### Status
UCNS remains an experimental/research-stage algebraic system.
The repository currently defends:
- flat kernel algebra
- depth-1 restricted completeness
- depth-2 oracle completeness
- catalogue-sufficient completeness (Theorem N)

### Compatibility
Test target:
- Python 3.8+

### Notes
This release is intended first for TestPyPI validation before public PyPI publication.

GPT generated; context, prompt Erin Spencer.
