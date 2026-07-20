# msdmd:1.0
skill:
  name: cyl_primes_04_unit_cylinder_surface_generator
  version: "0.1.0"
  author: "wayseer00 / Erin Patrick Spencer (The Interdependency LLC)"
  description: "Generates coordinates for the faint unit cylinder (r=1) surface mesh. Granular module 4/8. Provides the geometric base whose circumference explicitly involves π. msdmd compliant."
  inputs:
    - name: z_min
      type: float
    - name: z_max
      type: float
    - name: resolution_theta
      type: int
      default: 50
    - name: resolution_z
      type: int
      default: 20
  outputs:
    - name: x_surf, y_surf, z_surf
      type: "2D arrays (meshgrid)"
  relations:
    - "Unit cylinder geometry (r=1) — direct π involvement via 2πr"
    - "UCNS circular topology preservation on cylinder"
  epistemic_status: "prototype / IMPLEMENTED"
  msdmd_compliant: true
  granularity_factor: 8
  list_position: 4

"""
Unit Cylinder Surface Generator (msdmd skill 04/8)
"""
import numpy as np

def generate_unit_cylinder_surface(z_min: float, z_max: float, resolution_theta: int = 50, resolution_z: int = 20):
    """Return meshgrid x, y, z for unit cylinder surface."""
    theta = np.linspace(0, 2 * np.pi, resolution_theta)
    z = np.linspace(z_min, z_max, resolution_z)
    theta, z = np.meshgrid(theta, z)
    x = np.cos(theta)
    y = np.sin(theta)
    return x, y, z

if __name__ == "__main__":
    x, y, z = generate_unit_cylinder_surface(0, 100)
    print(f"Generated cylinder surface mesh: shape {x.shape}")