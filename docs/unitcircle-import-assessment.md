# UnitCircle import assessment — 2026-06-21

Source inspected: <https://github.com/erinepshovel-code/UnitCircle>

Cloned commit:

```text
d705319ef787985f3bbe426d9d59c2634af55241 2026-05-25 00:06:18 -0700 Merge pull request #9 from erinepshovel-code/claude/ucns-g-prime-cylinder-7NaQN
```

## Summary

`erinepshovel-code/UnitCircle` is an exploratory visualization and experiment
repository, not a packaged Python library. Its README describes a master's
thesis support system for mapping primes onto a unit circle by residue class,
with optional Möbius doubled-surface rendering and EML experiment scripts.

It should **not** be imported wholesale into the `ucns` package runtime at this time. A bounded visualization example has been imported under `examples/visualization/unitcircle_prime_geometry/`.

## Import decision

Status: **bounded example import only; do not import into package runtime yet**.

Reasons:

1. **License/provenance is maintainer-approved for this repo.** The source
   repository root did not contain a `LICENSE` file in the inspected commit,
   but the maintainer clarified that both repositories are theirs and the
   imported artifact will inherit this repo's UCNS/Apache-2.0 licensing.
2. **Scope is mostly visualization/experiment support.** Active scripts build
   prime datasets, train a toy EML tree, construct a gonal-Möbius embedding,
   and provide a self-contained UCNS v0.3 flat kernel. These are useful
   research artifacts, but they are not ready as package runtime APIs.
3. **The repository itself marks the work as exploratory.** Its README says the
   code supports intuition, pattern inspection, hypothesis formation, and
   explanation, and does not claim proofs or new theorems.
4. **Smoke checks revealed caution flags.** The `scripts/ucns_flat_kernel.py
   self-check` command executes, but reports `"flip_law_holds": false`. That
   makes the flat-kernel script unsuitable for direct promotion into the
   theorem-facing `ucns` package without reconciliation and tests.
5. **There is overlap with existing `ucns` modules.** This repo already has
   public `ucns.core`, `ucns.mobius`, `ucns.epicycle`, and
   `ucns.geometry_bridge` surfaces. UnitCircle's gonal/Möbius/epicycle scripts
   should be reconciled against those before any import.

## Candidate material, by destination

### Best candidate: documentation / examples, not package runtime

The safest import path is an example artifact under:

```text
examples/visualization/unitcircle_prime_geometry/
```

That example should include a README declaring:

- the exact UCNS claim or geometry boundary it illustrates;
- that it is not a proof;
- that UCNS-G / EDCM visual geometry does not inherit UCNS-A theorem status;
- how to regenerate any CSV outputs from scripts.

### Possible future code extraction

Potentially useful pure-stdlib pieces after review:

- prime sieve / residue dataset generation from `scripts/build_prime_datasets.py`;
- gonal-Möbius state construction from `scripts/build_gonal_mobius_embedding.py`;
- command examples showing how prime residue visualizations relate to existing
  `ucns.geometry_bridge` terminology.

These should be adapted rather than copied verbatim unless tests and claim
boundaries are settled.

### Not recommended for import now

- EML training code: experiment-specific, not a UCNS runtime primitive.
- Historical `code/` artifacts: read-only theorem-frontier snapshots.
- `scripts/ucns_flat_kernel.py`: overlaps with existing UCNS algebra and has a
  self-check result that needs investigation before reuse.
- Generated data/run outputs: should remain out of the package.

## Checks performed

```bash
git clone --depth 1 https://github.com/erinepshovel-code/UnitCircle /tmp/UnitCircle
find /tmp/UnitCircle -maxdepth 3 -type f
sed -n '1,240p' README.md
sed -n '1,220p' MANIFEST.md
sed -n '1,220p' CLAUDE.md
rg '^import |^from ' -n scripts code *.py
python scripts/ucns_flat_kernel.py self-check
python scripts/build_gonal_mobius_embedding.py --max-value 20 --out /tmp/gonal_test.csv
python scripts/build_prime_datasets.py --x-max 1000 --modulus 360 --log-grid-points 16 --window 7 --out-dir /tmp/unitcircle_data
python scripts/build_prime_datasets.py --x-max 1000 --modulus 360 --surface-mode mobius --log-grid-points 16 --window 7 --out-dir /tmp/unitcircle_data_mobius
git ls-tree --name-only HEAD
git log -1 --format='%H %ci %s'
```

## hmmm

UnitCircle is now licensed for this repo by maintainer instruction, but only one
lantern has been brought inside: the bridge still needs tests before any
load-bearing package API is built from it.
