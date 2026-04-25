# ucns — Unit Circle Number System

> **The unit circle is a Möbius disk with recursive epicycles.**

A zero-dependency Python library for creating **compact, efficient embeddings**
using a novel **Unit Circle Number System (UCNS)**.

---

## Why UCNS?

Traditional dense embeddings (word2vec, BERT, OpenAI Ada, …) store each
dimension as a 32-bit float.  UCNS embeddings encode every dimension as an
**angle** θ ∈ \[0, 2π\) on the unit circle:

| Property | float32 embedding | UCNS embedding |
|---|---|---|
| Bytes per dimension | 4 | 2 (uint16) |
| Similarity computation | dot product + two L2 norms | mean cos(Δθ) – no normalisation |
| Geometric space | Euclidean Rⁿ | Unit torus (S¹)ⁿ |
| Hierarchical structure | no | yes (Möbius / Poincaré disk) |
| External dependencies | numpy / torch / … | **none** |

The compression and speed gains come from two structural properties:

1. **All embeddings already live on the unit sphere** – the inner product
   `cos(θᵢ − φᵢ)` never needs a length normalisation step.
2. **Angles fit in 16 bits** – 0.0001 rad resolution with half the storage of
   float32.

---

## Architecture

```
input data
    │
    ▼
real-valued signal  (ordinals / floats / bytes …)
    │
    ▼  FFT  (Cooley–Tukey O(n log n), pure Python)
Epicycle decomposition  ──►  amplitudes  +  phases
                                              │
                                              ▼
                                    UCNS embedding vector
                                    (list of n angles in [0, τ))
```

The **Möbius disk** (Poincaré disk model of the hyperbolic plane) is available
as a companion geometry for encoding *hierarchical* relationships.  Points deep
in the tree live near the boundary of the disk (high hyperbolic radius); root
nodes sit near the centre.

---

## Installation

```bash
pip install ucns          # from PyPI (no dependencies)
# or from source:
pip install .
```

Python ≥ 3.8 required.  No third-party packages needed.

---

## Quick start

```python
from ucns import UCNEmbedding

emb = UCNEmbedding(dim=64)

# Encode any data to a list of 64 angles
v1 = emb.encode("hello world")
v2 = emb.encode("hello world")
v3 = emb.encode("completely different")

print(emb.similarity(v1, v2))   # 1.0  (identical)
print(emb.similarity(v1, v3))   # < 1.0

# Compact storage: 64 × 2 bytes = 128 bytes (vs 256 bytes for float32)
packed = emb.encode_packed("hello world")
print(len(packed))              # 128
restored = UCNEmbedding.unpack(packed)

# Nearest-neighbour search
corpus = [emb.encode(w) for w in ["cat", "dog", "fish", "bird"]]
idx, score = emb.nearest(emb.encode("cat"), corpus)
print(idx, score)               # 0  1.0
```

---

## API reference

### `UCN` — core unit-circle number

```python
from ucns import UCN, TAU

u = UCN(1.23)           # angle in radians, normalised to [0, τ)
v = UCN.from_real(0.5)  # map float → UCN
w = u * v               # rotation (angle addition)
d = u.arc_distance(v)   # geodesic distance on S¹ ∈ [0, π]
s = u.dot(v)            # cos(θ_u − θ_v) ∈ [−1, 1]
b = u.to_bytes()        # 2-byte compact serialisation
```

### `EpicycleDecomposition` — FFT on the unit circle

```python
from ucns import EpicycleDecomposition

d = EpicycleDecomposition([1, 2, 3, 4, 5, 6, 7, 8])
print(d.amplitudes)          # per-frequency radii
print(d.phases)              # per-frequency UCN angles
print(d.reconstruct())       # lossless signal reconstruction
sim = d.phase_similarity(d2) # amplitude-weighted phase cosine
packed = d.pack()            # uint16 serialisation (2 bytes/freq)
```

### `MobiusTransform` — Möbius disk automorphisms

```python
from ucns import MobiusTransform, poincare_distance

T = MobiusTransform(a=0.3 + 0.1j, phi=0.5)   # a ∈ open unit disk
w = T(0.2 + 0j)                                # apply transform
T_inv = T.inverse()                             # T_inv(T(z)) == z
d = poincare_distance(0.1 + 0j, 0.5 + 0j)     # hyperbolic metric
```

### Similarity metrics

```python
from ucns.similarity import phase_cosine, arc_distance, hyperbolic_cosine, top_k_overlap

phase_cosine(a, b)          # mean cos(θᵢ − φᵢ)  ∈ [−1, 1]
arc_distance(a, b)          # mean arc distance,  ∈ [0, 1]
hyperbolic_cosine(a, b)     # Poincaré-disk based ∈ [−1, 1]
top_k_overlap(amps_a, amps_b, k=8)  # dominant-frequency Jaccard ∈ [0, 1]
```

---

## Running the tests

```bash
python -m pytest tests/ -v
# or without pytest:
python -m unittest discover tests/
```

---

## Mathematical background

### Unit Circle Number System

Every UCN is a point on the unit circle S¹ ⊂ ℂ:

    z = e^(iθ),   θ ∈ [0, 2π)

S¹ is a compact abelian group under multiplication.  Representing data as
angles exploits this group structure: similarity becomes circular correlation,
arithmetic becomes rotation, and conjugation becomes reflection.

### Möbius disk

The open unit disk D = {z ∈ ℂ : |z| < 1} with the Poincaré metric is a
model of the hyperbolic plane.  Every conformal automorphism has the form

    T_{a,φ}(z) = e^(iφ) · (z − a) / (1 − ā·z)

These transformations preserve the circular boundary ∂D = S¹ and the
hyperbolic metric  d(z,w) = 2 arctanh(|(z−w)/(1−w̄z)|).

### Epicycles

Any periodic signal can be written as a sum of circular motions:

    x(t) = Σ_k  Aₖ · e^(i(2πkt/N + φₖ))

This is the Fourier series interpreted geometrically.  The FFT computes the
amplitudes *Aₖ* and phases *φₖ* in O(N log N) time.  UCNS stores only the
phases (the angular part), giving a compact multi-scale fingerprint.

---

## License

Apache 2.0 — see [LICENSE](LICENSE).
