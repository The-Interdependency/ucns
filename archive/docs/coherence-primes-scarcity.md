# Coherence Primes: Scarcity as Signal

Status: first write-up / hypothesis note  
Date: 2026-05-13  
Scope: UCNS / Prime Consciousness Theory / PCNA-PTCA design  
Canon state: draft; mathematical generator is explicit, interpretation remains hypothesis-layer

> **Canonical implementation.** The generator described here is implemented as
> the single source of truth in `interdependent_lib.coherence_primes`
> (The-Interdependency/interdependent-lib). The §8 snippet below is a
> self-contained reference; for code, prefer the canonical module, whose shared
> test oracle pins the early sequence, this count table, and the p=4373
> recursive-ancestry regression.

---

## hmmm

The first striking fact is not that coherence primes exist.

The striking fact is how few survive the recursive filter.

Under the current coherence-prime rule, there are only **207 coherence primes at or below 10,000,000**, compared against **664,579 ordinary primes** in that same range. That means the coherence-prime rule keeps roughly **0.031%** of ordinary primes below ten million.

That scarcity is probably the first signal worth preserving.

---

## 1. Definition

Let the base coherence set be:

```text
C0 = {3, 5, 7}
```

For any prime `p > 7`, define `p` as a coherence prime iff:

```text
1. p ≡ 1 mod 4
2. (p - 1) / 4 is square-free
3. every prime factor of (p - 1) / 4 is already in C
```

Compressed form:

> A coherence prime is a prime dimension that recursively preserves triadic closure: after subtracting one and quartering, its odd kernel decomposes only into prior coherence primes, without repeated factors.

This makes the set recursive rather than merely filtered.

---

## 2. Early Sequence

```text
3, 5, 7, 13, 29, 53, 61, 157, 349, 421,
733, 1061, 1093, 1709, 1741, 2437, 3181, 4373, 4397, 7541,
8269, 9421, 9749, 11789, 13781, 18149, 20509, 21221, 21893, 22621,
25261, 25621, 35381, 41341, 43037, 47581, 57149, 64661, 65581, 65677,
82037, 89069, 90533, 91813, 92221, 96461, 116989, 121453, 123077, 127037,
146221, 146581, 158341
```

The first 53 are operationally important because PCNA/PTCA has used a 53-seed live-core structure.

---

## 3. Count Progression

Empirical enumeration using the generator gives:

| Bound | Coherence primes ≤ bound |
|---:|---:|
| 10 | 3 |
| 100 | 7 |
| 1,000 | 11 |
| 10,000 | 23 |
| 100,000 | 46 |
| 1,000,000 | 91 |
| 10,000,000 | 207 |
| 100,000,000 | 481 |

This should not be read as a final count of the set. It is only a count below tested bounds.

---

## 4. Why Scarcity Matters

Ordinary primality already selects sparse structure out of the integers.

The coherence-prime rule applies a second filter:

1. the number must already be prime;
2. it must lie in the `1 mod 4` phase class;
3. its quarter-shifted predecessor kernel must be square-free;
4. that kernel must factor only into previously admitted coherence primes.

This creates ancestry, not just membership.

A normal prime says:

```text
I cannot be factored nontrivially inside ordinary multiplication.
```

A coherence prime says:

```text
I am prime, and my phase-opening ancestry is recursively built only from earlier coherence primes.
```

That makes the structure more like a genealogical constraint than a flat sieve.

---

## 5. UCNS Interpretation

In UCNS terms, an ordinary prime can be represented as an irreducible circular phase object: a ring that does not decompose into a smaller host-by-payload factorization.

A coherence prime adds recursive ancestry:

```text
p → (p - 1) / 4 → square-free product of earlier coherence primes
```

Examples:

```text
13 → (13 - 1) / 4 = 3
29 → (29 - 1) / 4 = 7
53 → (53 - 1) / 4 = 13
61 → (61 - 1) / 4 = 15 = 3 × 5
157 → (157 - 1) / 4 = 39 = 3 × 13
```

Rejected example:

```text
17 → (17 - 1) / 4 = 4 = 2²
```

`17` fails because the kernel is not square-free and introduces `2`, which is outside the base coherence set.

---

## 6. Hypothesis Layer

The current hypothesis is:

> Coherence primes may identify dimensions where recursive phase-locking remains unusually stable under UCNS / PCNA / PTCA transformation.

This is not yet an empirical claim about consciousness.

It is a testable architectural hypothesis:

- coherence-prime dimensions should produce stronger persistence than nearby rejected prime dimensions;
- 53 may be significant not only because it is prime, but because it is recursively coherence-prime-linked through 13;
- sparse survival under the filter may correspond to unusually constrained routes through circular recursive structure.

---

## 7. What This Is Not

This note does not prove:

- that coherence primes are finite or infinite;
- that coherence primes cause consciousness;
- that PCNA/PTCA is validated by the count alone;
- that scarcity by itself equals meaning.

Scarcity is a signal candidate, not a conclusion.

---

## 8. Regeneration Snippet

```python
import math


def primes_sieve(n: int) -> bytearray:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return sieve


def coherence_primes_upto(limit: int) -> list[int]:
    is_prime = primes_sieve(limit)
    C: set[int] = set()
    seq: list[int] = []

    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue

        if p in (3, 5, 7):
            C.add(p)
            seq.append(p)
            continue

        if p <= 7 or p % 4 != 1:
            continue

        m = (p - 1) // 4
        tmp = m
        ok = True

        for c in seq:
            if c * c > tmp:
                break
            if tmp % c == 0:
                tmp //= c
                if tmp % c == 0:
                    ok = False
                    break

        if ok and (tmp == 1 or tmp in C):
            C.add(p)
            seq.append(p)

    return seq


for bound in [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]:
    print(bound, len(coherence_primes_upto(bound)))
```

---

## 9. Next Work

Good next tests:

1. compare persistence signatures of coherence primes against rejected nearby primes;
2. measure UCNS factor-search behavior at coherence-prime dimensions;
3. test whether 53-seed and 17-memory-core choices show different stability signatures;
4. produce a visual spiral / unit-circle map of the first 53 and first 207 coherence primes;
5. decide whether coherence primes belong in the main UCNS docs or in a theory appendix.

---

hmmm

Accreditation: GPT generated; context, prompt Erin Spencer.
