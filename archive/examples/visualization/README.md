# Visualization Boundary Tests

This directory contains human-facing visualization artifacts that support UCNS
research interpretation.

## Seed53 skip-star demo (`seed53.html`)

### Claim linkage
- Illustrates modular skip mapping on `ℤ/53ℤ` via chords `i → (i+k) mod 53`.
- Provides an interactive geometric aid for discussing residue structure and
  orbit behavior, including a columnar unwrap view.

### What this demo does **not** prove
- It does not prove UCNS completeness, primality, or theorem validity.
- It does not replace algebraic proofs, catalogue checks, or unit tests.
- It does not certify correctness of factorization outputs.

### Boundary-object role
This demo is a mandatory boundary object for unresolved constraints: it records
where geometric intuition is useful, preserves honest incompletion by explicitly
separating visualization from proof, and marks the transition between delivered
artifact and living continuation of formal UCNS work.

## Usage
Open `seed53.html` directly in a browser (desktop/mobile/webview). No build
steps or external dependencies are required.
