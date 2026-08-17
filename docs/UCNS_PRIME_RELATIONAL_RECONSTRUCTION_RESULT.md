# UCNS prime-cardinality relational reconstruction result

Registered execution: 2026-08-16

Interpretation correction: 2026-08-17

Registered H3 status: **FALSIFIED — semantic-label and dispatch advantage only**

Prime-cardinality architecture: **UNRESOLVED**

Deprecation propagation: **BLOCKED; exact map `[]`**

## Corrected result

H1 **SURVIVED — not proved**. All seventeen frozen single-relation erasures
had exactly one admissible `F_257` reconstruction equal to the hidden fixture
value. The subtraction implementation and exhaustive 257-candidate replay
agreed.

H2 **SURVIVED — not proved**. Removing P2, P3, P5, or P7 left respectively
`1`, `2`, `4`, or `6` independent field degrees of freedom. Constructive
alternatives and the independent dimension calculation agreed on all four
leave-outs.

The frozen H3 rule **FALSIFIED** an advantage for the prime-labelled,
source-specialized software realization. The anonymous implementation matched
`17/17` H1 and `4/4` H2 with the same 21 cells while using fewer semantic
control fields and one generic dispatch.

That result does **not** falsify the prime-cardinality architecture. The
anonymous baseline retained the complete 2/3/5/7 cardinality signature, the
same four source blocks, `F_257` arithmetic, sum-mod-field checksums, and the
same 21-cell information budget. It changed names, dispatch specialization,
and checksum placement. Those are implementation variables inside a
structurally isomorphic realization, not a control that removes prime
cardinality.

The correct reading is therefore:

```text
registered semantic/dispatch advantage  FALSIFIED
prime-cardinality architecture          UNRESOLVED
```

No criterion was changed and no replacement baseline was introduced after the
result. A genuinely architecture-distinguishing control requires a new claim
and a new preregistration.

## Frozen-versus-executed audit

| Surface | Frozen requirement | Current execution | Audit |
|---|---|---|---|
| hypothesis | H1 reconstruction; H2 whole-view irreducibility; H3 registered complexity comparison | all three executed | H1/H2 survived; H3 falsified only its registered software-complexity advantage |
| fixture | exact G2/G3/G5/G7 values and value-blind identities | unchanged; 17 unique identities | no fixture drift or value leakage |
| independent encoders | no shared encoder helper | current head has four non-delegating source entry points | first execution commit `c146584` used a shared helper; repaired after outcome in `d979751`, so the first execution was not pristine |
| matched-information baseline | B0/B1/B2/B3 sizes 2/3/5/7, 21 cells, typed cyclic checksums | executable baseline matches 17/17 and 4/4 | baseline is structurally isomorphic to the prime-cardinality family; it is not an architectural control |
| resource bounds | one CPU, 256 MiB, 30 seconds | POSIX test harness applies one-CPU affinity, `RLIMIT_AS=256 MiB`, and a 30-second timeout | current execution passes the enforced bound |
| stopping rule | stop dependent escalation at first load-bearing falsification | H3 stops later execution | stop retained; propagation target corrected to the claim H3 actually varied |
| failure propagation | propagate only to actual dependents of the failed claim | original terminal report deprecated seven prime-architecture dependents | post-registration scope drift; broad propagation retracted |
| external/sealed labels | must not be inspected | not inspected | no external-label leakage detected |

The initial producer commit also recorded baseline outcomes before the baseline
was executed. Commit `d979751` later made the baseline executable and reproduced
the tuple. That reproduction preserves the arithmetic result but does not erase
the post-outcome implementation history.

## Exact minimal propagation map

No prime-cardinality architectural claim is deprecated by this H3 result:

```json
[]
```

The unexecuted dependent work is restored to `UNRESOLVED`, not promoted to
`SURVIVED`:

| Dependent claim | Correct status |
|---|---|
| multi-loss prime reconstruction | UNRESOLVED |
| recursive prime reconstruction | UNRESOLVED |
| cross-scale prime reconstruction | UNRESOLVED |
| multimodal prime reconstruction | UNRESOLVED |
| externally authored prime reconstruction | UNRESOLVED |
| EDCM external validation for the prime architecture | UNRESOLVED |
| joint UCNS–EDCM prime architecture | UNRESOLVED |

## Independently preserved results

- UCNS P5/P7 exact distinction: `SURVIVED` in its frozen scope.
- Controlled prime-cardinality H1: `SURVIVED — not proved`.
- Controlled prime-cardinality H2: `SURVIVED — not proved`.
- EDCM absolute recovered dissonance: `FALSIFIED`.
- EDCM normalized recovered dissonance: `SURVIVED` at its controlled
  scale-confound gate.

None receives proof, canon, measurement-validity, certification, or semantic
authority from this correction.

## Receipts

```text
PR #197 frozen head             89d4c615ff09831604c69861ff51b7139bee24f2
PR #198 audited parent          6ddae018bee20fdfe738ac26e71e69a29c275368
skill-lib doctrine used         b4234ca29529f56526541df8deb58c2c19570792
EDCM frozen candidate           02f71b5610512108066bc91c40f6055b44ba32e4
preregistration JSON SHA-256    a1a94812fde4d397f874fd3dcbd1d57ddcecdebc23a9e18835a0030cd7076823
original report SHA-256         c9a1d4b45c88a12d666e5e85e62710f8d20401ce08f57d6fff4f03bae0f1aaed
corrected report SHA-256        f5f2ce7d81bdafe849d08d1f373aca459059304fc5779c1646c46e3f86891eae
work-graph SHA-256              b6684f8098ced71a4a3966d26f2dfe146c5582815909181a2527ef0038338545
external/sealed labels          not inspected
```

The preregistration Markdown, JSON, and frozen work graph remain unchanged.
Git history retains the original execution and terminal interpretation; this
correction does not rewrite either history or the preregistration.

## Usage guidance

Reproduce the corrected producer report, then run the independent replay:

```bash
PYTHONPATH=src python -m ucns.prime_relational_reconstruction \
  --repository-root . --output /tmp/prime-relations.json
python tools/replay_prime_relational_reconstruction.py \
  docs/evidence/UCNS_PRIME_RELATIONAL_RECONSTRUCTION_PREREGISTRATION.json \
  /tmp/prime-relations.json
```

Consume `h3.status` only as the frozen semantic-label/dispatch criterion.
Consume `architecture_status` for architectural standing. Do not consume the
historical deprecation list; its replacement map is empty. Do not implement a
non-prime control on this preregistration after seeing these outcomes.

## hmmm

- The result of a newly preregistered, genuinely non-prime-cardinality matched
  control is `hmmm`.
- Natural multimodal behavior, external authorship, measurement validity, and
  independent external replication remain `hmmm`.
