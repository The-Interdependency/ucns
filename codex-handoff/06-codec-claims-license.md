# Workstream 6 — typed dict keys, claims, and licensing

## Dictionary-key identity

Preserve the existing documented value behavior—non-byte scalar **values** may continue to decode as bytes—but dictionary keys must round-trip with type identity and must never collapse silently.

Implement a versioned, explicit dictionary-key tag layer for newly encoded dictionaries. Support this exact key subset unless a broader subset is fully tested:

```text
bytes
str
int
bool
finite float
tuple of supported key types, recursively
```

Use exact-type dispatch so `bool` is not accidentally encoded as `int`. `bytearray`, lists, dicts, sets, custom objects, non-finite floats, and tuples containing unsupported elements must raise `EncodingError` when used as keys.

A suitable encoding is a dedicated key wrapper containing a version marker, a type tag, and a payload. It may reuse the recursive list encoding internally, but parsing must be strict and unambiguous. New encodings must preserve distinctions such as:

```python
{1: b"int", "1": b"str", b"1": b"bytes"}
```

Note that Python itself treats `True` and `1` as the same dictionary key; do not claim the codec can preserve two entries that cannot coexist in the input dictionary.

Decoder requirements:

- Parse and validate the version marker and tag.
- Reconstruct the original supported key type.
- Reconstruct tuple keys recursively as tuples, never lists.
- Verify the decoded key is hashable.
- Detect duplicate decoded keys and raise `EncodingError`; never overwrite an earlier entry silently.
- Reject malformed wrappers, unknown tags, invalid numeric text, non-finite floats, and odd key/value content.
- Preserve decoding of legacy dictionaries when possible. Legacy keys may retain the old bytes-coercion behavior, but the compatibility path must also reject unhashable keys and duplicate-key collapse rather than crashing or overwriting.

Update the module-level round-trip claim from `dict[Hashable, T]` to the exact supported-key contract.

## Required codec tests

- `1`, `"1"`, and `b"1"` coexist and round-trip distinctly.
- String keys round-trip as strings in newly encoded dictionaries.
- Integer, Boolean, finite float, tuple, nested tuple, empty tuple, and mixed supported tuple keys round-trip with exact types.
- Unsupported and non-finite keys raise `EncodingError` at encode time.
- Malformed tags and unknown versions raise at decode time.
- A malicious or hand-built object containing duplicate decoded keys raises rather than overwrites.
- Legacy byte-key dictionaries still decode.
- Existing list/value coercion tests continue to pass, with assertions updated only where the new key contract deliberately changes behavior.

## Claims reconciliation

After the code behavior is final, audit all live documentation and code docstrings with at least:

```bash
git grep -nE 'partially verified in Lean|SEQ-PRIME|absolute|complete|completeness|no false negative|oracle atom|dict\[Hashable|MPL-2.0|Apache-2.0'
```

Required claim state:

- Exact recomposition gives unconditional factor-return soundness.
- The executable payload search is catalogue-complete only because it now exhausts the finite supplied catalogue; tests are evidence, not Lean proof.
- Theorem N and the executable-solver correspondence remain formal frontier work unless all relevant Lean statements are actually discharged without `sorry`.
- A green Lean build means declarations type-check; it does not transfer proof through `sorry`, opaque solver predicates, or tests.
- `SEQ-PRIME` is certified only within a declared domain, with machine-checked catalogue coverage and demonstrated search exhaustion.
- Custom catalogues are uncertified by default unless an exact machine check proves coverage.
- The oracle class is exact canonical-catalogue membership, not all geometrically bounded depth-one objects.
- Plural quotient APIs expose multiplicity; singular APIs are compatibility selectors.
- The runtime carrier excludes empty objects.
- `UCNSObject` is immutable.
- The codec’s supported dictionary-key types are stated exactly.

Treat `README.md` together with `docs/claims-ledger.md` as current release-status authority. Update `CLAUDE.md`, `REVIEW_PACKET.md`, `CHANGELOG.md`, API docstrings, proof-scope banners, and other current docs that repeat superseded claims. Do not rewrite dated historical artifacts as though their old statements were current; add a clear scope/correction banner when history must remain visible.

## License reconciliation

The root `LICENSE` and `pyproject.toml` identify Apache-2.0. Make all root-package and release metadata agree with Apache-2.0, including `CLAUDE.md` and `.zenodo.json` where applicable.

Do not blindly replace license strings inside genuinely imported, vendored, or separately licensed artifacts. Inspect each occurrence, preserve third-party attribution when it is real, and clarify the boundary. The final audit must distinguish:

- repository/package license: Apache-2.0;
- separately licensed imported material: its own license, with explicit attribution.

Never hand-edit the generated manifest block in `CLAUDE.md`. Regenerate it with the checked-in manifest tool when needed.

## Workstream 6 acceptance

No supported dictionary can lose or overwrite a key because two key encodings decode identically, and no live root-package metadata contradicts the Apache-2.0 license or the final solver/claim boundaries.

---
