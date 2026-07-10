# UnitCircle prime-geometry visualization example

This example imports the safest UnitCircle visualization artifact into the UCNS
repo as a bounded research-support example.

Source:

- Repository: <https://github.com/erinepshovel-code/UnitCircle>
- Inspected commit: `d705319ef787985f3bbe426d9d59c2634af55241`
- Imported file: `scripts/build_gonal_mobius_embedding.py`
- Local file: `gonal_mobius_embedding.py`

Licensing/provenance note: this import follows the maintainer instruction that
UnitCircle will inherit UCNS licensing because both repositories are owned by
the same maintainer. The local artifact is therefore treated as part of this
repo's Apache-2.0 distribution.

## What it illustrates

The script constructs a small CSV embedding over integer values using four
layers:

1. gonal roots of unity;
2. a doubled Möbius/spinor face lift;
3. epicyclic radial modulation;
4. soft assignment into prime-anchor basins.

This is useful for visualizing prime-indexed unit-circle / doubled-surface
geometry and for comparing terminology with `ucns.geometry_bridge`.

## What it does not prove

This example does **not** prove prime-distribution theorems, UCNS-A factorization
claims, UCNS-G / EDCM bridge claims, or Theorem N. It is an exploratory visual
and dataset-generation artifact only.

## Why only this file was imported

The broader UnitCircle repo contains EML training scripts, historical UCNS
artifacts, and a `scripts/ucns_flat_kernel.py` script. Those were not imported
because they either overlap with existing `ucns` package APIs, are experiment-
specific, or need reconciliation before reuse. In particular, the inspected
flat-kernel self-check executed but reported `"flip_law_holds": false`, so it
must not be promoted into theorem-facing package code without further work.

## Usage

From the repo root:

```bash
python examples/visualization/unitcircle_prime_geometry/gonal_mobius_embedding.py \
  --n 29 \
  --chi 1 \
  --epicycles "1.0:1,0.5:-1" \
  --basin-primes "3,5,7,13,29,53" \
  --tau 0.35 \
  --max-value 500 \
  --out /tmp/gonal_mobius_embedding.csv
```

## hmmm

This example is a lantern, not a load-bearing theorem beam: it shines on the
shape of a possible bridge while leaving the bridge inspection unfinished.
