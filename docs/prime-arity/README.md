# Prime-Arity Experiment

Status: `INCUBATING` / `UNRESOLVED`

Prime-arity is placed here as an **incubating UCNS geometry/projection experiment**.

It is not UCNS canon. It is not part of UCNS core source. It is not a theorem. It is not a selected universal UCNS option.

## Placement decision

```text
repository: The-Interdependency/ucns
path: docs/prime-arity/
standing: incubating research candidate
authority: UCNS repository only for geometry/projection experiment custody
canon status: none
selection status: UNRESOLVED
```

## Why this belongs here

The experiment directly concerns UCNS-shaped objects:

```text
origin
arity carriers
recursive load
projection
geometry/cylinder placement
convergence
prime/composite readout
hmmm boundary
```

It stays in `docs/prime-arity/` because the current claim is a research protocol and object schema, not implementation authority or canon.

## Why this is not core

The following remain unresolved:

```text
exact projection law Π
admissible arity-capture law class
independent replay
matched controls
zeta-family alignment validity
whether any theorem exists
```

No behavior-bearing UCNS module should import this experiment. UCNS core remains geometry-only.

## Contents

```text
PREREGISTRATION.md                  frozen research boundary and falsifiers
THIRTEEN_RECURSION_LAYERS.md        thirteen-layer calibration scaffold
THIRTEEN_RECURSION_LAYERS.json      machine-readable thirteen-layer map
METAPAT_RELATIONS.json              typed relation map
UCNS_OBJECTS.jsonl                  minimal UCNS object records
METRICS.json                        determined convergence metrics and controls
audit_coefficient_breadth.py         exact coefficient-ledger and scalar-breadth audit
```

## Coefficient-breadth audit usage

From the repository root:

```bash
uv sync --locked --extra test --extra build
.venv/bin/python docs/prime-arity/audit_coefficient_breadth.py > /tmp/coefficient-audit.json
.venv/bin/python docs/prime-arity/audit_coefficient_breadth.py > /tmp/coefficient-audit-replay.json
cmp /tmp/coefficient-audit.json /tmp/coefficient-audit-replay.json
.venv/bin/python -m pytest tests/test_coefficient_breadth_audit.py
.venv/bin/python tools/verify_skill_lib_contracts.py .
```

The artifact is compact canonical JSON without a trailing newline. The script
replays that same representation before emitting it. Optimized Python (`-O`,
`-OO`, or `PYTHONOPTIMIZE`) refuses to publish evidence. The existing geometry
CI discovers its test-owned checks, and the no-exec contract audit includes this
experiment directory without moving its code into the core package.

The coefficient identity follows by multiplying `C_k(t)` by `(1+q*t)`;
unique factorization of these normalized linear factors preserves the unordered
prime multiset. Tests independently compare all 126 multisets over
`{2,3,5,7,11}` through degree four against subset-product sums. They also retain
the scalar collision `(3,11)` versus `(5,7)`, the supplied-successor boundary,
the restricted empty/nonempty null-faithfulness result, and negative/replay cases.
Finite test success is implementation evidence, not the mathematical proof.

Supplied factors are **not admitted UCNS roles**: their occurrence order and source
provenance are retained separately, while role admission and UCNS arity remain
unresolved. No relation witness is synthesized from factor count. The scalar
candidate is not a complete retained-structure evaluator, and no successor is
discovered here. These limitations remain part of every audit record.

## Load-bearing claim under test

```text
Prime epochs are projected convergence events from recursive arity-load fields.
```

## hmmm

The exact projection law remains unresolved; this placement preserves the candidate without promoting it.
