GPT generated; context and canon by Erin Spencer.

# UCNS Reproducibility Guide

## hmm

This guide gives reviewers a short path from repository checkout to the current
UCNS review surface. It is designed for canon verification, proof pressure, and
computational reproduction—not persuasion.

UCNS has two deliberately separated surfaces:

```text
canonical public gonol:
    fixed SPACE/ZERO Möbius twist origin
    exact 157-position arrangement
    orientation reversal after 360 degrees
    complete return after 720 degrees

normalized factorization subsystem:
    UCNSObject / multiply / factor_search_v08
    internally projected n_min
    Theorem N FRONTIER
```

No bridge between them is assumed.

---

## 1. Local setup

Use a clean checkout, then install the package in editable development mode:

```bash
python -m pip install -e .[dev]
```

UCNS has no runtime dependencies beyond the Python standard library.

---

## 2. Full test surface

Run the same complete pytest surface used by CI:

```bash
python -m pytest ucns_recursive/tests tests -v
```

Expected release-candidate target: all tests pass on every advertised Python
version.

Important interpretation: `test_depth2_full_domain.py` is a compact closure
sweep plus hand-constructed edge cases. It is not a literal exhaustive
enumeration over every payload assignment in D'. Its role is `TEST-BACKED`, not
proof replacement.

---

## 3. Public-gonol canon checks

A reviewer should verify:

```bash
python -m pytest \
  tests/test_public_gonol.py \
  tests/test_public_gonol_claim_guard.py \
  tests/test_public_gonol_status_recovery.py \
  tests/test_public_identity_recovery.py \
  tests/test_mobius_compatibility_scope.py \
  -v
```

The checked facts include:

- exact A0 source commit and public arrangement digest;
- position `0` is SPACE/ZERO and remains fixed;
- digit `"0"` is an ordinary nonzero glyph;
- exact faces, chirality, adjacency, mirror, and lifted traversal;
- repeated-character full 157-step revolution;
- one 360-degree circuit changes orientation and 720 degrees restores it;
- `PrivateGonal` exposes no application-level `2π` inscription method;
- classical disk/embedding utilities cannot claim public-frame authority;
- Theorem N and Carrier-LCM remain scoped to the normalized subsystem;
- public/internal bridge obligations remain visible and open.

The Lean public-frame surface is checked separately:

```bash
cd formal
lake build Ucns.PublicGonol
```

A green build establishes that the declarations type-check. It does not promote
unrelated `sorry`-backed completeness statements.

---

## 4. Public API smoke surface

New code should import from `ucns` and `ucns.a0_safe`. The `ucns_recursive`
package remains a compatibility shim.

A reviewer should confirm these public surfaces import successfully:

```text
PUBLIC_GONOL_157
ORIGIN
face / chirality / mirror_of
encode_text_path / decode_text_path
PrivateGonal
UCNSObject
UNIT
multiply
factor_search_v08
depth_of
factorization_result
ucns.a0_safe.identity / describe / canonical / factor
```

The smoke test must not imply that `PrivateGonal` is a `UCNSObject`, or that the
public gonol is normalized through `UCNSObject.normalize()`.

---

## 5. Minimal factorization examples

The normalized-subsystem examples live in:

```text
examples/depth_examples/
```

They include:

- depth-1 minimal seq-prime case;
- depth-2 oracle composite case;
- depth-3 catalogue-sufficient search case;
- catalogue-boundary scoped result case.

Each example should assert exact recomposition or explicitly scoped behavior.
They are not examples of the public-gonol bridge, because no such bridge exists.

---

## 6. Depth-3 sweep source

The historical asymmetric sweep source lives at:

```text
code/sweeps/t9_minimal_cat.py
```

The script records a configured experiment. Source text alone does not prove
that a stated number of cases executed successfully. Numerical execution claims
require an immutable CI run, committed report, or release artifact tied to an
exact revision.

---

## 7. Interpreting `SEQ-PRIME`

A raw `SEQ-PRIME` from `factor_search_v08` is not automatically a universal
primality claim.

External or A0-facing presentations should prefer the `factorization_result`
envelope because it carries product identity, domain label, typed domain status,
result kind, `seq_prime_is_absolute`, claim scope, and explanation.

`seq_prime_is_absolute` is true only inside a declared complete normalized
factorization domain. It is not a statement about the public gonol.

---

## 8. Distribution validation

```bash
rm -rf build dist
python -m build
python -m twine check dist/*
```

Then install the built wheel in a clean environment and repeat the public import
boundary plus complete pytest surface.

---

## 9. Release-candidate expectations

```text
[ ] full pytest surface passes on Python 3.8, 3.10, 3.11, and 3.12
[ ] public-gonol source pin and arrangement digest pass
[ ] origin, lifted-path, private-transform, and 720-degree formal checks pass
[ ] no 2π inscription method exists on the canonical public frame
[ ] public API and compatibility import smoke tests pass
[ ] factorization examples run with scoped claims
[ ] package build and Twine checks pass
[ ] README, RELEASE, spec, claims ledger, Zenodo, and package metadata agree
[ ] CHANGELOG contains the public-gonol recovery
[ ] bridge obligations PG-4 and PG-5 remain visibly OPEN
[ ] no known failing test is accepted as v1.0.0-ready
```

## hmmm

Reproducibility can establish source identity, software behavior, and formal
type-checking. It cannot manufacture the missing public/internal bridge or
promote a frontier theorem.
