# msdmd:1.0
skill:
  name: cyl_primes_02_pi_explicit_angle_mapper
  version: "0.1.0"
  author: "wayseer00 / Erin Patrick Spencer (The Interdependency LLC)"
  description: "Maps primes to cylindrical angle θ = 2 * π * f(p) with explicit π. Granular module 2/8. Supports modulus for residue classes (helices on cylinder). msdmd compliant."
  inputs:
    - name: primes
      type: list[int]
    - name: modulus
      type: int
      default: 360
    - name: z_scale
      type: str
      enum: ["index", "log", "value"]
  outputs:
    - name: thetas
      type: list[float]
      description: "Angles in radians (involves 2π explicitly)."
    - name: xs, ys, zs
      type: list[float]
  relations:
    - "Direct geometric link to π via circular cross-section"
    - "UCNS unit-circle base extended to cylinder"
    - "Residue class helices for prime patterns"
  epistemic_status: "prototype / IMPLEMENTED"
  msdmd_compliant: true
  granularity_factor: 8
  list_position: 2

"""
Pi-Explicit Cylindrical Angle Mapper (msdmd skill 02/8)
Explicitly uses π in θ for UCNS cylindrical primes graph.
"""
import math

def map_to_cylinder(primes: list[int], modulus: int = 360, z_scale: str = "index"):
    """Return xs, ys, zs, thetas for unit cylinder placement."""
    n = len(primes)
    if n == 0:
        return [], [], [], []
    thetas = [2 * math.pi * (p % modulus) / modulus for p in primes]
    xs = [math.cos(t) for t in thetas]
    ys = [math.sin(t) for t in thetas]
    if z_scale == "index":
        zs = list(range(n))
    elif z_scale == "log":
        zs = [math.log(p) for p in primes]
    else:
        zs = [float(p) for p in primes]
    return xs, ys, zs, thetas

if __name__ == "__main__":
    from msdmd_cyl_primes_01_efficient_prime_generator import generate_primes
    primes = generate_primes(50)
    xs, ys, zs, thetas = map_to_cylinder(primes)
    print(f"Mapped {len(primes)} primes. Example θ[0] = {thetas[0]:.4f} rad ({thetas[0]*180/math.pi:.1f}°)")