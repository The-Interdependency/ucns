# msdmd:1.0
skill:
  name: cyl_primes_08_msdmd_composer_orchestrator
  version: "0.1.0"
  author: "wayseer00 / Erin Patrick Spencer (The Interdependency LLC)"
  description: "Composer / orchestrator for the full set of 8 granular msdmd modules. Validates msdmd headers, wires the pipeline (prime gen → mapping → twins → cylinder → render → export → UCNS hooks), and produces the recomposed master artifact. Granular module 8/8. msdmd compliant."
  inputs:
    - name: prime_limit
    - name: modulus
    - name: z_scale
    - name: output_html
  outputs:
    - name: recomposed_script_or_payload
  relations:
    - "Final layer: assembles 01-07 into usable whole while preserving individual msdmd declarations"
    - "Enables a0p-orchestrated or manual composition of the cylindrical primes UCNS feature"
  epistemic_status: "prototype / IMPLEMENTED"
  msdmd_compliant: true
  granularity_factor: 8
  list_position: 8
  note: "This module completes the literal factor-of-8 sequence and supports recomposition."

"""
MSDMD Composer / Orchestrator (msdmd skill 08/8)
Completes the literal sequence and enables recomposition of all eight modules.
"""
# In a real a0p/skill-lib environment this would dynamically load and validate the other seven modules.
# For standalone use we provide a convenience function that runs the full pipeline using the logic from 01-07.

def run_full_cylindrical_primes_pipeline(prime_limit=2000, modulus=360, z_scale="index", output_html="cylindrical_primes_ucns.html"):
    """End-to-end run using logic equivalent to modules 01-07."""
    # --- 01 ---
    from msdmd_cyl_primes_01_efficient_prime_generator import generate_primes
    primes = generate_primes(prime_limit)

    # --- 02 ---
    from msdmd_cyl_primes_02_pi_explicit_angle_mapper import map_to_cylinder
    xs, ys, zs, thetas = map_to_cylinder(primes, modulus=modulus, z_scale=z_scale)

    # --- 03 ---
    from msdmd_cyl_primes_03_twin_prime_skeletal_connector import find_twin_prime_edges
    twin_pairs, twin_edge_indices = find_twin_prime_edges(primes)

    # --- 04 is geometry only (cylinder surface) ---
    from msdmd_cyl_primes_04_unit_cylinder_surface_generator import generate_unit_cylinder_surface
    cyl_x, cyl_y, cyl_z = generate_unit_cylinder_surface(min(zs), max(zs))

    # --- 05 static matplotlib (optional) ---
    # from msdmd_cyl_primes_05_matplotlib_cylindrical_plotter import plot_cylindrical_graph
    # plot_cylindrical_graph(xs, ys, zs, thetas, twin_edge_indices, cyl_x, cyl_y, cyl_z)

    # --- 06 interactive ---
    from msdmd_cyl_primes_06_interactive_plotly_exporter import export_interactive_html
    export_interactive_html(xs, ys, zs, thetas, twin_edge_indices, output_html=output_html,
                            title_suffix=f"limit={prime_limit}, modulus={modulus}")

    # --- 07 UCNS payload ---
    from msdmd_cyl_primes_07_ucns_integration_hooks import build_ucns_payload, export_payload_json
    payload = build_ucns_payload(xs, ys, zs, thetas, twin_pairs, primes=primes)
    export_payload_json(payload)

    print(f"Full pipeline complete. Interactive: {output_html}")
    return payload

if __name__ == "__main__":
    run_full_cylindrical_primes_pipeline(prime_limit=1500)