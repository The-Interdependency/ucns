# STATUS — operational-widening probes (reference copy; witness runs in edcmbone)

**Date:** 2026-06-01
**Repo:** `the-interdependency/ucns`
**Branch:** `claude/operational-widening-probes`

This repo holds a **reference copy** of the four operational-widening probes and
the per-sublattice finiteness law, filed beside the UCNS theory
(`ucns-spec.md`, the recursive-factorization engine, frontier docs) they reason
about. The probes import `ucns_v04` + `closed_tokens` (the worked encoder
substrate in the `edcmbone` repo, not here), so from this repo they exit at the
import guard by design:

```
ModuleNotFoundError: No module named 'ucns_v04'
```

This is expected: `the-interdependency/ucns` carries the UCNS *theory* but not
the English-freight encoder. The executable witness lives in `edcmbone`.

## Reproduction of record (in `edcmbone`, same branch, 2026-06-01)

Run from the `edcmbone` repo root against its worked `ucns_v04.py` +
`closed_tokens.py`:

| probe | claim | observed | exit |
|---|---|---|---|
| `operational_widening_probe.py` | {8,16,32} dyadic band closes under ⊠ | constructibility + closure + PCEA OK | 0 |
| `ternary_widening_probe.py` | threefold in-band, associative, order-carrying | 27/27 in-band; associative OK; order-sensitive OK; PCEA OK | 0 |
| `prime5_widening_probe.py` | per-prime finiteness survives coherence prime 5 | pure-5 closed; cross → ⟨2,5⟩; navigable | 0 |
| `prime_carpet_probe.py` | per-sublattice law across 53 prime axes | all 53 pure-power closed; all cross → ⟨p,2⟩ | 0 |

See `edcmbone:docs/ucns_operational_widening.md` §5.1 for the full reproduction
record, including:
- the one-line import-hygiene note on `ternary_widening_probe.py` (pre-import
  `fractions` before the `sys.path` mutation; probe logic unchanged), and
- the honest provenance gap: the 99.3% / {8,16,32} *frequency* measurement is
  attributed to `frequency_probe.py`, which is **not in either repo**; the
  closure claims reproduce without it, but the empirical distribution is
  unwitnessed in-repo.

## Boundary note (per `edcmbone:docs/ucns-boundary.md`)

This is UCNS-A carrier behavior under ⊠ (the recursive-factorization algebra in
this repo's `ucns_recursive`). No proof-scope claim transfers to UCNS-G / EDCM
metrics without an explicit source-backed bridge. The law is a statement about
`n_min` closure under composition, nothing more.
