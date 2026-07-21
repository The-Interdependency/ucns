# Agent instructions

Read, in order:

1. `CANON.md`
2. `docs/chapter-1.md`
3. `.agents/skills/README.md`
4. the source module's `MODULE_BUILD` and `CONTRACTS` blocks
5. the corresponding test module's `CHECKS` block

Rules:

- Preserve the directed 720-degree lifted carrier and 360-degree visible
  projection.
- Do not reintroduce Möbius, seam, hidden-zero, automatic orientation reversal,
  or one-circle-completion semantics as formal carrier claims.
- Do not create a complete `UCNSObject` until `mu`, `W`, `M`, `B`, and canonical
  structural equivalence are explicitly constructed and tested.
- Do not restore archived arithmetic or theorem language by name similarity.
- Use `hmmm` for unresolved constraints; do not fill them with guessed certainty.
- Every behavior-bearing source module must own skill-lib `MODULE_BUILD` and
  `CONTRACTS` declarations. Every executable test must own a resolving `CHECKS`
  declaration.
- Run `python tools/verify_skill_lib_contracts.py .` and the complete test suite
  before claiming `test-backed` status.
