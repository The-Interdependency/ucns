# msdmd:1.0
skill:
  name: cyl_primes_03_twin_prime_skeletal_connector
  version: "0.1.0"
  author: "wayseer00 / Erin Patrick Spencer (The Interdependency LLC)"
  description: "Detects twin prime pairs and builds skeletal edge list for cylinder visualization. Granular module 3/8. Realizes the 'twin prime families provide skeletal structure' on the cylindrical graph. msdmd compliant."
  inputs:
    - name: primes
      type: list[int]
  outputs:
    - name: twin_pairs
      type: list[tuple[int, int]]
    - name: edge_indices
      type: list[tuple[int, int]]
  relations:
    - "Twin primes as skeletal structure on cylinder (per foundational description)"
    - "UCNS relational preservation (twin couplings)"
  epistemic_status: "prototype / IMPLEMENTED + TEST-BACKED"
  msdmd_compliant: true
  granularity_factor: 8
  list_position: 3

"""
Twin Prime Skeletal Connector (msdmd skill 03/8)
Builds the red 'bones' / edges on the cylindrical graph.
"""
def find_twin_prime_edges(primes: list[int]):
    """Return list of (idx1, idx2) for twin pairs in the primes list."""
    prime_set = set(primes)
    prime_to_idx = {p: i for i, p in enumerate(primes)}
    twin_pairs = []
    edge_indices = []
    for p in primes:
        if p + 2 in prime_set:
            i1 = prime_to_idx[p]
            i2 = prime_to_idx[p + 2]
            twin_pairs.append((p, p + 2))
            edge_indices.append((i1, i2))
    return twin_pairs, edge_indices

if __name__ == "__main__":
    from msdmd_cyl_primes_01_efficient_prime_generator import generate_primes
    primes = generate_primes(200)
    twins, edges = find_twin_prime_edges(primes)
    print(f"Found {len(twins)} twin prime pairs in first 200 primes.")