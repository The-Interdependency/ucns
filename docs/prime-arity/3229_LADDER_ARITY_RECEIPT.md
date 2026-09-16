# 3229-Ladder Fourth-Power-Coset Audit Receipt

Status: `INCUBATING` / `UNRESOLVED`

This is deterministic carrier-filter evidence. It is not UCNS canon, a
coset-to-prime constructor, or a cryptographic primitive.

## Frozen construction

```text
k_m = int("3" + "2" * m + "9")
n_m = 4*k_m + 1
m = 0..17
label = HIT iff [U(n):U(n)^4] == 4; CONTROL otherwise
```

JSON receipt SHA-256: `6827148677c2505110f131c2ee039649fe4700d1802640070ff2a0c4b4d63600`

## Results

| m | k | n | complete factorization | phi(n) | image order | arity_4 | label |
|---:|---:|---:|:---|---:|---:|---:|:---|
| 0 | 39 | 157 | `157` | 156 | 39 | 4 | **HIT** |
| 1 | 329 | 1317 | `3 * 439` | 876 | 219 | 4 | **HIT** |
| 2 | 3229 | 12917 | `12917` | 12916 | 3229 | 4 | **HIT** |
| 3 | 32229 | 128917 | `137 * 941` | 127840 | 7990 | 16 | **CONTROL** |
| 4 | 322229 | 1288917 | `3^2 * 7 * 41 * 499` | 717120 | 22410 | 32 | **CONTROL** |
| 5 | 3222229 | 12888917 | `12888917` | 12888916 | 3222229 | 4 | **HIT** |
| 6 | 32222229 | 128888917 | `17 * 31 * 199 * 1229` | 116709120 | 1823580 | 64 | **CONTROL** |
| 7 | 322222229 | 1288888917 | `3 * 429629639` | 859259276 | 214814819 | 4 | **HIT** |
| 8 | 3222222229 | 12888888917 | `487 * 26465891` | 12862422540 | 3215605635 | 4 | **HIT** |
| 9 | 32222222229 | 128888888917 | `41 * 79 * 3917 * 10159` | 124109631360 | 1939212990 | 64 | **CONTROL** |
| 10 | 322222222229 | 1288888888917 | `3 * 7 * 491 * 1193 * 104779` | 734384810880 | 11474762670 | 64 | **CONTROL** |
| 11 | 3222222222229 | 12888888888917 | `137 * 94079480941` | 12794809407840 | 799675587990 | 16 | **CONTROL** |
| 12 | 32222222222229 | 128888888888917 | `131 * 71707 * 13720901` | 127903211202000 | 7993950700125 | 16 | **CONTROL** |
| 13 | 322222222222229 | 1288888888888917 | `3^2 * 19 * 43 * 257 * 682052477` | 792010247970816 | 6187580062272 | 128 | **CONTROL** |
| 14 | 3222222222222229 | 12888888888888917 | `41 * 151 * 2081875123387` | 12491250740316000 | 780703171269750 | 16 | **CONTROL** |
| 15 | 32222222222222229 | 128888888888888917 | `1297 * 3733 * 26620580017` | 128755013987146752 | 2011797093549168 | 64 | **CONTROL** |
| 16 | 322222222222222229 | 1288888888888888917 | `3 * 7 * 67 * 916054647397931` | 725515280739160560 | 45344705046197535 | 16 | **CONTROL** |
| 17 | 3222222222222222229 | 12888888888888888917 | `3691 * 29611 * 117928387517` | 12884961755546924400 | 805310109721682775 | 16 | **CONTROL** |

## Summary

- HIT rows: [0, 1, 2, 5, 7, 8]
- CONTROL rows: [3, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17]
- Prime HIT rows: [0, 2, 5]
- Composite HIT rows: [1, 7, 8]
- Therefore HIT is not a primality test.

## Feasibility boundary

All emitted rows are completely factored inside the unsigned 64-bit boundary. The next row, m=18, has n=128888888888888888917 and is deliberately excluded because it exceeds that frozen deterministic domain.

## Standing

```text
3229-ladder generation: REPLAYED
emitted factorizations: COMPLETE
fourth-power coset arities: DERIVED
carrier-filter significance: UNRESOLVED
canon status: NONE
cryptographic significance: UNRESOLVED
```

## hmmm

The ladder supplies a reproducible carrier filter, but no UCNS law currently selects the ladder or turns an arity-four HIT into a prime-speaking rule.
