# Workstream 5 — nonempty immutable `UCNSObject`

## Release decision

Make `UCNSObject` a recursively immutable canonical value object. Do not keep mutable public lists while retaining a structural `__hash__`; do not merely patch the demonstrated set-membership example.

## Constructor and value-model requirements

- Reject empty `A_plus`/`F_plus` immediately.
- Accept sequence inputs for compatibility, but store canonical tuples.
- `n_dec` and the constructor’s `n_min` argument must be positive integers and must reject booleans.
- Validate equal cell/face lengths.
- Face values must be exact integer bits `0` or `1`; reject booleans unless a deliberate compatibility decision is documented and tested.
- Convert supported rational angles deliberately to `Fraction`; reject floats, non-rational values, booleans, NaN-like values, and malformed cells.
- Normalize angles into the documented `[0, 4)` policy during construction.
- Validate each payload is `UCNSObject` or `None`.
- Compute canonical intrinsic `n_min` from normalized angles and require `n_dec` to be a multiple of it.
- Make `A_plus`, `F_plus`, `A_minus`, and `F_minus` immutable tuples.
- Prevent reassignment of canonical fields after construction.
- Make `normalize()` idempotent and non-mutating; construction must already produce normalized objects.
- Preserve equality semantics unless a separately justified correction is needed: `n_min`, ordered normalized cells, recursive payloads, and faces are identity; `n_dec` remains excluded if that is still the documented policy.
- Keep `__hash__` only after immutability is enforced, and make it consistent with `__eq__` recursively.
- Implement safe copy/deepcopy behavior for immutable values, ideally returning `self`.

Because objects become immutable, `multiply(A, None)` and `multiply(None, A)` may safely return `A` directly.

Audit all code that assumes list equality or mutates object fields. Update production code and tests to the immutable public contract; do not weaken immutability to preserve incidental list assertions.

Update PR #96’s base-geometry language so the runtime carrier is the nonempty normalized object set. Empty objects are rejected rather than described as a partially defined edge case.

## Required tests

- Empty construction raises `ValueError` or a documented typed subclass.
- Zero, negative, Boolean, and non-integer carrier values are rejected.
- Invalid faces, malformed cells, invalid angles, and invalid payloads are rejected.
- Normalization occurs at construction and `normalize()` returns the same value without mutation.
- Public tuple item assignment fails.
- Canonical attribute reassignment fails.
- Nested payloads are equally immutable.
- Hash equality follows object equality.
- Set/dict membership is stable for the object lifetime.
- `stable_hash(obj)` cannot change because caller mutation is impossible.
- `copy.copy` and `copy.deepcopy` preserve value identity safely.
- Multiplication, serialization, quotient enumeration, codecs, stores, and all existing algebra contracts pass under the immutable representation.
- No production path can manufacture an empty object after construction.

## Workstream 5 acceptance

A valid `UCNSObject` cannot be mutated into an invalid or differently hashed value, and an empty UCNS object cannot be constructed through the public API.

---
