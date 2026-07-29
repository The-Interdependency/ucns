# UCNS–EDCM v0.8 transverse-strip claim — superseded

**Historical status:** merged experiment, corrected by v0.9.

**Correction:** v0.8 did not map transverse displacement into an actual
directed-cover coordinate. It retained the unchanged v0.7 root chart and stored
the transverse value beside it. The exact round trips therefore established an
augmented product envelope:

```text
v0.7 root-loop cover chart × exact transverse sidecar
```

They did not establish a transverse directed-cover chart.

## What remains valid

The v0.8 implementation correctly demonstrated, for `u ∈ {-1, 0, +1}`:

- exact retention of the framed native state and source-linked initiation;
- reversible local-frame `u` and global-side `εu` descriptions;
- exact convention change;
- exact commutation of the augmented envelope with the declared motions; and
- exact removal to the v0.7 root state at `u = 0`.

Those are envelope and coordinate-bookkeeping results.

## What is retracted

The following v0.8 claims are not retained:

- that the transverse value was represented in the actual directed cover;
- that the v0.7 F12 support extended to nonzero transverse fibers; and
- that v0.7 F13 falsification extended to those fibers.

Two envelope states with the same v0.7 root and different transverse values
still have the same actual `LiftedCarrierPoint`. The inverse recovered the
transverse value from the sidecar, not from the cover.

The old `ucns.transverse_strip_chart` public module and its cover-chart names
have been removed. v0.9 replaces them with
`ucns.transverse_envelope`, pins a named exact comparison policy, validates
complete witness identities rather than counts, records the corrected candidate
identity, and constructs the cover-coordinate collisions explicitly.

See
[`EXACT_RATIONAL_TRANSVERSE_ENVELOPE_V09.md`](EXACT_RATIONAL_TRANSVERSE_ENVELOPE_V09.md).

hmmm: the sidecar algebra was exact; the noun “cover” was doing work the
coordinate never performed.
