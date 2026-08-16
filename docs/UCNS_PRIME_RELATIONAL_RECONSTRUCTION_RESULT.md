# UCNS prime-cardinality relational reconstruction result

Date: 2026-08-16
Terminal status: **ARCHITECTURE FALSIFIED**

## Result

The prerequisite gate survived: P2 is explicit, P3 is independently
source-native, all seventeen public relation identities are unique, and value
mutation leaves identity unchanged.

H1 **SURVIVED**. All seventeen preregistered single-relation erasures had
exactly one admissible `F_257` reconstruction equal to the hidden source value.
The subtraction implementation and a separate exhaustive 257-candidate replay
agreed for every erasure.

H2 **SURVIVED**. Removing P2, P3, P5, or P7 left respectively `1`, `2`, `4`,
or `6` independent field degrees of freedom. Constructive alternative
assignments and the independent dimension calculation agreed, so every view
uniquely mattered somewhere under whole-view removal.

H3 **FALSIFIED** the load-bearing prime-specific advantage. The anonymous
typed-block baseline achieved the same `17/17` exact H1 recoveries and `4/4`
irreducible H2 leave-outs using the same 21 field cells and seventeen public
relation identities. It required one generic encoder dispatch and zero prime
semantic control fields, versus four dispatches and two prime controls for the
prime-labelled family.

Under the frozen rule, equal reconstruction by a materially simpler,
information-matched representation is decisive. The complete stated
architecture is therefore **FALSIFIED**, not unresolved.

## Evidence ledger

| Gate | Status | Evidence |
|---|---|---|
| P2 explicit construction | SURVIVED | direct `G2` encoder plus complementary `G7` checksum |
| P3 independent construction | SURVIVED | direct source-native `G3` encoder; no P5/P7 input |
| identity non-leakage | SURVIVED | all 17 value mutations preserve public identity |
| H1 reconstruction | SURVIVED | 17/17 exact; exhaustive replay agrees |
| H2 irreducibility | SURVIVED | 4/4 leave-outs ambiguous; degrees `1,2,4,6` |
| H3 simpler baseline | FALSIFIED | equal `17/17`, `4/4`, and 21 cells; lower semantic/dispatch complexity |
| multi-loss reconstruction | DEPRECATED | dependent on surviving prime-specific advantage |
| recursive reconstruction | DEPRECATED | dependent on surviving prime-specific advantage |
| scale transitions | DEPRECATED | cannot rescue the stated advantage after matched baseline equality |
| multimodal reconstruction | DEPRECATED | cannot rescue the stated advantage after matched baseline equality |
| externally authored fixtures | DEPRECATED | not run after terminal dependency failure |
| EDCM external validity for this architecture | DEPRECATED | not run after terminal dependency failure |
| joint UCNS–EDCM architecture | DEPRECATED | load-bearing UCNS architectural advantage failed |

## Exact receipts

```text
skill-lib authority          6ef2e4c123225f9db20e5230e5894c9c86b42ee6
UCNS frozen parent           123495018f50ef63697de7f8e0d15f1dc9e826b2
EDCM frozen candidate        02f71b5610512108066bc91c40f6055b44ba32e4
preregistration commit       89d4c61
producer implementation      c146584
independent replay           8274f03
frozen-protocol compliance   d979751
work graph                   b6684f8098ced71a4a3966d26f2dfe146c5582815909181a2527ef0038338545
aggregate report SHA-256     c9a1d4b45c88a12d666e5e85e62710f8d20401ce08f57d6fff4f03bae0f1aaed
repeat                       byte-identical
external/sealed labels       not inspected
```

The independent replay imports no UCNS product module. It reproduced `17`
exact H1 recoveries, H2 dimensions `P2=1`, `P3=2`, `P5=4`, `P7=6`, and the H3
matched-simpler falsifier.

## Surviving bounded claims

- The prior exact P5/P7 distinction remains `SURVIVED` for its frozen diagrams.
- This controlled prime-cardinality code reconstructs all seventeen declared
  single erasures.
- Every one of its four views is irreducible under the declared whole-view
  leave-out test.
- EDCM absolute recovered dissonance remains `FALSIFIED`.
- EDCM normalized recovered dissonance remains `SURVIVED` at its controlled
  scale-confound gate.

None of these bounded results supplies a prime-specific advantage over the
matched typed-block code.

## Usage guidance

Reproduce the producer and independent replay:

```bash
PYTHONPATH=src python -m ucns.prime_relational_reconstruction \
  --repository-root . --output /tmp/prime-relations.json
python tools/replay_prime_relational_reconstruction.py \
  docs/evidence/UCNS_PRIME_RELATIONAL_RECONSTRUCTION_PREREGISTRATION.json \
  /tmp/prime-relations.json
```

Do not continue the deprecated adversaries as though they could vindicate the
stated architecture. A future program would require a materially different
claim and a new preregistration; it may not be described as repair of this
falsified claim.

## Remaining nonclaims

This result is not a universal impossibility theorem. It does not negate the
existing P5/P7 mathematical distinctions, validate or invalidate EDCM in
general, select UCNS or EDCM canon, or establish claims about physical
necessity, consciousness, prime metaphysics, spectra, or zeta functions.

## hmmm

Whether some future non-prime-specific multimodal error-correcting architecture
is useful remains open. It is outside this frozen claim because the decisive
failure is precisely that the prime-labelled architecture supplied no advantage
over its simpler matched-information realization.
