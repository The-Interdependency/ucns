# msdmd:1.0
skill:
  name: cyl_primes_01_efficient_prime_generator
  version: "0.1.0"
  author: "wayseer00 / Erin Patrick Spencer (The Interdependency LLC)"
  description: "Efficient prime generation via sieve. Granular module 1/8 for Cylindrical Graph of Primes UCNS visualization. Outputs list of primes + basic metadata. msdmd compliant for a0p / skill-lib integration."
  inputs:
    - name: limit
      type: int
      description: "Upper bound for prime generation (inclusive)."
  outputs:
    - name: primes
      type: list[int]
      description: "Sorted list of primes ≤ limit."
    - name: count
      type: int
  relations:
    - "UCNS cylindrical embedding extension"
    - "pi-primes link (previous conversation)"
    - "foundational unit-circle primes visualization seed"
  epistemic_status: "prototype / IMPLEMENTED + TEST-BACKED"
  msdmd_compliant: true
  granularity_factor: 8
  list_position: 1
  stop_after: 5

"""
Efficient Prime Generator (msdmd skill 01/8)
Part of Cylindrical Graph of Primes UCNS extension.
"""
import math

def generate_primes(limit: int) -> list[int]:
    """Return sorted list of primes ≤ limit using simple sieve."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]

if __name__ == "__main__":
    primes = generate_primes(100)
    print(f"Generated {len(primes)} primes ≤ 100")
    print(primes[:10], "...")