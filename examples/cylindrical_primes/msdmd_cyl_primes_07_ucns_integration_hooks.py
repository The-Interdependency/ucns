# msdmd:1.0
skill:
  name: cyl_primes_07_ucns_integration_hooks
  version: "0.1.0"
  author: "wayseer00 / Erin Patrick Spencer (The Interdependency LLC)"
  description: "UCNS / a0p / EDCM integration hooks for the cylindrical primes graph. Granular module 7/8. Provides data export, simple coloring hooks, and serialization compatible with other UCNS components. msdmd compliant."
  inputs:
    - name: xs, ys, zs, thetas, twin_pairs
  outputs:
    - name: ucns_payload
      description: "Dict ready for a0p or EDCM consumption (points, edges, metadata)"
  relations:
    - "Bridge from visualization layer to core UCNS / EDCM / a0p ecosystem"
    - "Preserves relational structure (twin couplings, residue helices) for higher layers"
  epistemic_status: "prototype / IMPLEMENTED"
  msdmd_compliant: true
  granularity_factor: 8
  list_position: 7

"""
UCNS / a0p / EDCM Integration Hooks (msdmd skill 07/8)
"""
import json

def build_ucns_payload(xs, ys, zs, thetas, twin_pairs, primes=None, extra_metadata=None):
    """Return a dict payload suitable for a0p, EDCM, or other UCNS consumers."""
    payload = {
        "type": "cylindrical_primes_graph",
        "version": "0.1.0",
        "points": [
            {"prime": p if primes else i, "x": xs[i], "y": ys[i], "z": zs[i], "theta": thetas[i]}
            for i in range(len(xs))
        ],
        "twin_skeletal_edges": [
            {"p1": tp[0], "p2": tp[1]} for tp in twin_pairs
        ],
        "geometry": {
            "r": 1.0,
            "theta_definition": "2 * pi * (p % modulus) / modulus",
            "pi_involvement": "explicit via 2*pi in angle mapping"
        },
        "metadata": extra_metadata or {}
    }
    return payload

def export_payload_json(payload, filepath="cyl_primes_ucns_payload.json"):
    with open(filepath, "w") as f:
        json.dump(payload, f, indent=2)
    print(f"UCNS payload exported: {filepath}")
    return filepath

if __name__ == "__main__":
    print("Module 07 ready. Use build_ucns_payload(...) then export or pass to a0p/EDCM.")