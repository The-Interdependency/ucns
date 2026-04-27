# UCN Embeddings (archived)

This directory archives the original UCN embedding library that was previously
the main content of this repository.  The library provides:

- `UCN` — a single unit-circle number (angle arithmetic, compact serialisation)
- `EpicycleDecomposition` — FFT-based signal decomposition on the unit circle
- `MobiusTransform` — conformal automorphisms of the Poincaré disk
- `UCNEmbedding` — high-level embedding API
- Similarity metrics: `phase_cosine`, `arc_distance`, `hyperbolic_cosine`, `top_k_overlap`

This code has been archived here because the repository has been refocused on
UCNS (Unit Circle Number System) sequence theory and recursive factorization.
The embedding library belongs in a separate repository.
