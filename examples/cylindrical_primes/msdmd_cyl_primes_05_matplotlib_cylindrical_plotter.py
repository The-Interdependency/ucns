# msdmd:1.0
skill:
  name: cyl_primes_05_matplotlib_cylindrical_plotter
  version: "0.1.0"
  author: "wayseer00 / Erin Patrick Spencer (The Interdependency LLC)"
  description: "Renders static 3D cylindrical graph using matplotlib (scatter + twin edges + cylinder wireframe). Granular module 5/8. Includes title and labels explicitly referencing π and UCNS. Stop after five per instruction. msdmd compliant."
  inputs:
    - name: xs, ys, zs, thetas
    - name: twin_edge_indices
    - name: cylinder_mesh (optional)
  outputs:
    - name: fig
      type: matplotlib figure
  relations:
    - "Visualization layer for UCNS cylindrical primes"
    - "Explicit π in geometry and labeling"
    - "Twin skeletal structure rendered"
  epistemic_status: "prototype / IMPLEMENTED"
  msdmd_compliant: true
  granularity_factor: 8
  list_position: 5
  note: "Stopped after five granular items as instructed. Items 6-8 (Plotly exporter, full UCNS hooks, compliance validator) deferred."

"""
Matplotlib Cylindrical Plotter (msdmd skill 05/8)
Static renderer for the UCNS cylindrical primes graph.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_cylindrical_graph(xs, ys, zs, thetas, twin_edge_indices, cylinder_x=None, cylinder_y=None, cylinder_z=None, title_suffix=""):
    """Create and show static 3D plot."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Primes
    ax.scatter(xs, ys, zs, c=zs, cmap='viridis', s=20, alpha=0.8, label='Primes')

    # Twin skeletal edges
    for i1, i2 in twin_edge_indices:
        ax.plot([xs[i1], xs[i2]], [ys[i1], ys[i2]], [zs[i1], zs[i2]], color='red', linewidth=1.5, alpha=0.7)

    # Optional cylinder surface
    if cylinder_x is not None:
        ax.plot_wireframe(cylinder_x, cylinder_y, cylinder_z, color='gray', alpha=0.15, linewidth=0.5)

    ax.set_xlabel('X = cos(θ)')
    ax.set_ylabel('Y = sin(θ)')
    ax.set_zlabel('Z (scaled)')
    ax.set_title(f'Cylindrical Graph of Primes — UCNS Extension\n{title_suffix}\nθ = 2π × (p mod m)/m | Twin primes = skeletal structure')
    ax.legend()
    plt.tight_layout()
    plt.show()
    return fig

if __name__ == "__main__":
    print("Module 5/8 loaded. Combine with 01-04 for full static render.")