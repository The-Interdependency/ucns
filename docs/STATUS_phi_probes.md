# STATUS — Φ composition probes (reference copy; witness runs in edcmbone)

**Date:** 2026-05-30
**Repo:** `the-interdependency/ucns`
**Branch:** `claude/phi-composition-probes-spec-cowUB`

This repo holds a **reference copy** of the three Φ-composition probes and the
English-UCNS freight spec, filed beside the UCNS proofs and `ucns-spec.md` that
they reason about. The probes import `ucns_v04` + `closed_tokens`, which are the
**worked substrate in the `edcmbone` repo, not here**. Running them from this
repo therefore exits at the import guard:

```
FATAL: run from repo root (needs ucns_v04.py + closed_tokens.py).
  import error: No module named 'ucns_v04'
```

This is expected: `the-interdependency/ucns` carries the UCNS *theory*
(`ucns-spec.md`, completeness/quotient proofs, frontier docs) but not the
English-freight encoder. The executable witness lives in `edcmbone`.

## Reproduction of record (in `edcmbone`, same branch, 2026-05-30)

Run from the `edcmbone` repo root against its worked `ucns_v04.py` +
`closed_tokens.py` (`DISPATCH` = 196):

| probe | §R claim | observed | match |
|---|---|---|---|
| v1 `phi_compose_probe.py` | carrier 100%, coordinate ~43% | 400/400 (100%), 173/400 (43.2%) | ✅ |
| v2 `phi_compose_probe_v2.py` | 600/600 both laws | 600/600, 600/600 | ✅ |
| v3 `phi_compose_probe_v3.py` | payload 600/600, face 5/5 | 600/600, 5/5 | ✅ |

See `edcmbone:docs/STATUS_phi_probes.md` for the full reproduction record,
including the one-line import-hygiene note on v1/v2 (two unused symbols,
`minimal_gonal_order` / `norm_turn`, removed; probe logic unchanged).

## Why a copy lives here too

The spec (`docs/eng_ucns_spec.md`) reasons throughout against `ucns-spec.md`
sections (§5.1 chirality, §8 unit, §11 ordered product, §12 disk-flip) that are
canonical **in this repo**. Co-locating the freight spec and its probes here
keeps the cross-references one repo away from their targets for readers working
in the UCNS theory tree. The single source of executable truth remains
`edcmbone`; this copy is documentation, and its probes are runnable only when
placed alongside the `edcmbone` substrate.

## Pending decisions (unchanged from the handoff; do not block this commit)

1. **Spec home** — repo-local `docs/` (here and in edcmbone) vs. canon promotion
   to `edcmbone:canon_eng/`. Erin's call.
2. **Signed commit** — add `-S` for a canon-grade freeze if a key is
   provisioned.
