# Workstream 3 — oracle predicate/catalogue equivalence

## Release decision

Use the conservative v1.0 boundary: **an oracle atom is `None` or a structural member of the canonical generated oracle catalogue**. Do not broaden the generator to every syntactically bounded depth-one object in this release unless a separate proof-backed finite definition and acceptable performance are demonstrated. Narrow the claim rather than silently widening it.

## Required changes

- Define one canonical source of truth for oracle payloads.
- Make `is_oracle_atom(obj)` extensionally equivalent to membership in that source.
- Make `is_in_oracle_class` use the same predicate.
- Keep geometric/frozen bounds (`depth`, `|A_plus|`, `n_min`) distinct from oracle-catalogue membership. Being geometrically bounded is not itself an oracle certificate.
- Make the public catalogue stable, deterministic, deduplicated, and immutable or copy-on-return.
- Expose a stable catalogue-rule version/fingerprint for Workstream 2.
- Update every docstring and claim that currently says the generator contains “all depth-1 objects within the bounds.”

The prior false-certainty witness must be explicitly covered:

```python
x = UCNSObject(
    4,
    4,
    [(Fraction(0), None), (Fraction(3, 2), None)],
    [0, 0],
)

assert x not in generate_payload_catalogue()
assert not is_oracle_atom(x)
```

Do not “fix” this test by adding `x` alone to the catalogue. The predicate and generator must agree by construction.

## Required tests

- Every canonical catalogue member is an oracle atom.
- Every oracle atom is structurally present in the canonical catalogue.
- Generate an adversarial bounded universe of normalized depth-one objects using all carrier-grid angles for `n_min <= 4`, lengths `1..3`, and all face assignments; assert predicate-membership equivalence for every sample.
- Include objects inside the geometric bounds but outside the canonical catalogue.
- Assert deterministic catalogue order, no duplicates, and stable fingerprint.
- A depth-two object carrying a bounded-but-non-catalogue payload is classified `depth-2-non-oracle` and cannot receive a certified negative result from the default catalogue.

## Workstream 3 acceptance

The expression below is true for every tested object and true by implementation construction, not merely by a few examples:

```python
is_oracle_atom(obj) == structural_member(obj, generate_payload_catalogue())
```

---
