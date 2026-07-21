# UCNS — definition-first restart

UCNS is rebuilding from its carrier definition rather than patching the former
factorization kernel.

The previous implementation, specifications, tests, formal work, and
experiments remain preserved under [`archive/`](archive/) with complete Git
history. They are evidence and potential machinery, not current canon.

## Current formal foundation

The carrier is a **directed twofold branched angular cover**:

- Structural Null is the unique coordinate-free absence of distinction.
- Non-null carrier points have a 720-degree lifted period.
- The visible projection has a 360-degree period.
- One visible lap advances to the second lifted representative on the same
  directed path.
- Two visible laps complete the lifted return.
- A 360-degree displacement does not automatically negate, reflect, reverse
  parity or chirality, invert a frame, or transform a payload.

The earlier Möbius/seam account remains provenance only. It is not the formal
object definition. See [`CANON.md`](CANON.md) and
[`docs/chapter-1.md`](docs/chapter-1.md).

## Active code

The root package currently implements only the carrier floor:

- Structural Null;
- the faithful-breadth-to-radius map supplied with an already-known breadth;
- 720-degree lifted points;
- 360-degree visible projection;
- deck translation and the one/two branch law.

It does **not** yet implement a complete `UCNSObject`, faithful-breadth
evaluation, support weights, product character, pairing, payload dispatch,
factorization, encoding, or Theorem N.

## Verification

```text
python tools/verify_skill_lib_contracts.py .
python -m pytest
python -m build
python -m twine check dist/*
```

The source owns skill-lib `MODULE_BUILD` and `CONTRACTS` declarations; tests own
`CHECKS` declarations. The no-exec audit fails closed on missing contracts,
unknown witnesses, or unresolved `self::` calls.

## Build doctrine

This build is pinned to
`The-Interdependency/skill-lib@fa6e6200bc274657de2334754bbbf98844ef6541`.
See [`.agents/skills/README.md`](.agents/skills/README.md) and
[`STACK_MANIFEST.json`](STACK_MANIFEST.json).

hmmm: the topology is executable; the three measuring instruments still have
to earn their names under traffic.
