# ratios: loc_comments=0:14 imports_exports=0:0 calls_definitions=0:0
"""Base-geometry contract tests (test-build / msdmd convention).

Each module in this package implements the evidence for one obligation
of the base-geometry completion handoff.  The *promises* live as
``# === CONTRACTS ===`` blocks in the source modules that own them
(``ucns/canonical.py``, ``ucns/division_theory.py``); this package only
implements the checks.

Every module exposes one no-argument aggregate callable named
``contract_<obligation_id>`` (the test-build runner entry point) plus
granular pytest-discoverable ``test_*`` functions.  Determinism: all
randomness is seeded; identical command strings reproduce identical
runs (latest-run-wins applies to logs, not outcomes).
"""
# ratios: loc_comments=0:14 imports_exports=0:0 calls_definitions=0:0
