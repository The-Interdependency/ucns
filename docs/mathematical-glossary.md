GPT generated; context, prompt Erin Spencer.

# UCNS Mathematical Glossary

## hmm

This glossary is deliberately conservative. It gives working definitions for the current UCNS v1.0 review surface without asking the reader to accept broader metaphysical or architectural claims. Where a term is still exploratory, the definition says so.

---

## 1. UCNS object

**Definition.** A UCNS object is the recursive data object currently implemented as:

```text
UCNSObject(n_dec, n_min, A_plus, F_plus)
```

where `A_plus` is an ordered sequence of `(angle, payload)` pairs and each payload is either another UCNS object or `None`.

**Notation.** Informally, write an object as `G = (n_dec, n_min, A+, F+)`.

**Example.** The smallest standard two-cell object is:

```text
S2 = UCNSObject(2, 2, [(0, None), (1, None)], [0, 0])
```

**Non-example.** A raw integer such as `7` is not by itself a UCNS object until encoded into the UCNS representation.

**Standard relationship.** A UCNS object is closer to a finite labeled sequence or recursive term than to a scalar number.

---

## 2. Unit payload

**Definition.** `None` is the unit payload. It represents absence of recursive payload content in a cell.

**Notation.** The code exports this as `UNIT = None`.

**Example.** A flat object has only `None` payloads.

**Boundary.** `None` is not the same as an empty UCNS object with one or more cells. It is the payload-level unit.

**Standard relationship.** It functions as an identity object in recursive payload multiplication.

---

## 3. Cell

**Definition.** A cell is one entry of `A_plus`: an ordered pair `(angle, payload)`.

**Example.** In `(Fraction(0), None)`, the angle is `0` and the payload is the unit.

**Boundary.** A face bit is not stored in the cell pair; face bits live in the parallel `F_plus` sequence.

**Standard relationship.** A cell is a labeled sequence position.

---

## 4. Angle / phase position

**Definition.** The angle component records a rational position on the UCNS angular carrier.

**Example.** `Fraction(2, 3)` is an angle used in threefold examples.

**Boundary.** Current code uses rational angular positions; the repository does not require an arbitrary real-valued angle field for v1.0.

**Standard relationship.** This is comparable to an element of a finite cyclic or modular phase lattice.

---

## 5. Face sequence

**Definition.** `F_plus` is a binary sequence parallel to `A_plus`.

**Example.** `[0, 0]` is the all-zero face state for a two-cell object.

**Boundary.** Face values are structural bits; they are not truth values in a logical proposition.

**Standard relationship.** A face sequence is a finite binary decoration on the ordered cell sequence.

---

## 6. Declared carrier (`n_dec`)

**Definition.** `n_dec` is the declared carrier or presentation resolution attached to the object.

**Example.** `UCNSObject(2, 2, ..., ...)` has declared carrier `2`.

**Boundary.** `n_dec` is not the same as sequence length.

**Standard relationship.** It is a representation parameter similar to a modulus or resolution label.

---

## 7. Minimal carrier (`n_min`)

**Definition.** `n_min` is the minimal carrier order associated with the object's anchor lattice.

**Example.** `S2` has `n_min = 2`.

**Boundary.** `n_min` is not necessarily equal to `len(A_plus)`.

**Standard relationship.** Comparable to the smallest cyclic grid supporting the represented phase positions.

---

## 8. Recursive depth

**Definition.** Recursive depth is the nesting depth of payloads:

```text
None -> depth 0
UCNSObject -> 1 + max(depth(payloads))
```

**Example.** A flat object whose payloads are all `None` has depth `1`.

**Boundary.** Depth measures payload nesting, not number of cells.

**Standard relationship.** This is term depth for a recursive finite structure.

---

## 9. Multiplication

**Definition.** `multiply(A, B)` forms a cellwise recursive product. For candidate factors with cell counts `p` and `q`, the product has `p*q` cells. Product payloads are recursively multiplied from the corresponding input payloads.

**Notation.** The specs often write this as `A ⊠ B = P`.

**Example.** If both inputs have two cells, the product host has four cells.

**Boundary.** Factorization may be non-unique; multiplication being defined does not imply a unique inverse.

**Standard relationship.** It resembles a structured product over finite labeled sequences with recursive labels.

---

## 10. Factor search

**Definition.** Factor search asks: given a product object `P`, recover a non-trivial pair `(A, B)` such that `multiply(A, B) == P`.

**Current implementation.** `factor_search_v08(P, catalogue=None)`.

**Boundary.** If the solver returns `SEQ-PRIME`, that result is absolute only inside a declared complete domain.

**Standard relationship.** This is a constrained decomposition/search problem over recursive finite objects.

---

## 11. Catalogue

**Definition.** A catalogue is a finite list of payload candidates supplied to the factorization solver.

**Example.** `generate_payload_catalogue()` returns `None` plus the current depth-1 oracle atoms inside the frozen bounds.

**Boundary.** A catalogue is not a proof by itself. It is an input assumption for catalogue-sufficient factorization.

**Standard relationship.** Comparable to a finite candidate basis for recursive subterms.

---

## 12. Catalogue coverage

**Definition.** A catalogue covers a factorization when it contains every recursive payload appearing in the true factors.

**Example.** For Theorem N, if `P = multiply(A, B)`, then a sufficient catalogue includes the recursive payload closure of `A` and `B`.

**Boundary.** Catalogue coverage is a strong assumption. It does not solve the separate problem of discovering a small useful catalogue from `P` alone.

**Standard relationship.** This is an oracle/candidate-set sufficiency assumption.

---

## 13. Witness matrix

**Definition.** A witness matrix is the global consistency structure used to verify that recovered candidate payload assignments explain every product cell simultaneously.

**Example.** For a `p × q` factor split, the witness matrix has one witness per product cell.

**Boundary.** Passing a local quotient step is not enough; all witnesses must agree globally.

**Standard relationship.** Comparable to a consistency certificate for a system of coupled equations.

---

## 14. Oracle class

**Definition.** The depth-2 oracle class is the class of objects whose payloads are drawn from the declared oracle atoms.

**Example.** A depth-2 object whose cell payloads are all depth-1 frozen-domain objects is in the oracle class.

**Boundary.** Oracle-complete does not mean generally complete outside the oracle assumptions.

**Standard relationship.** Comparable to a restricted model class under a fixed basis/candidate set.

---

## 15. Frozen domain D'

**Definition.** D' is the standing bounded depth-2 domain:

```text
depth <= 2
|A_plus| <= 3
n_min <= 4
```

**Example.** A two-cell depth-1 object with `n_min = 2` lies inside D'.

**Boundary.** Products of D' factors may have more cells than either factor; domain membership constraints apply to the objects under classification, not casually to every product claim.

**Standard relationship.** A finite or bounded test/proof domain.

---

## 16. `SEQ-PRIME`

**Definition.** `SEQ-PRIME` is the sentinel returned by `factor_search_v08` when no non-trivial factorization is found under the current solver and catalogue.

**Example.** A length-1 object returns `SEQ-PRIME` under the current defended domain behavior.

**Boundary.** A length-2 flat object is currently composite via the one-cell face-flip factorization path, so it should not be used as the canonical seq-prime example.

**Standard relationship.** This is a scoped negative search result, not automatically a universal primality theorem.

---

## 17. Theorem N

**Definition.** Theorem N is the catalogue-sufficient factorization claim: if `P = multiply(A, B)` and the catalogue contains every recursive payload appearing in `A` or `B`, then `factor_search_v08(P, C)` returns valid factors.

**Boundary.** Theorem N does not claim efficient catalogue discovery, efficient scaling for large catalogues, carrier widening, or total general primality.

**Standard relationship.** This is an algorithmic completeness theorem under finite candidate-set sufficiency.

---

## 18. Public API

**Definition.** For v1.0, `ucns` is the public import namespace. `ucns_recursive` remains a compatibility/internal implementation surface.

**Example.** Prefer:

```text
from ucns import UCNSObject, multiply, factor_search_v08
```

**Boundary.** Direct imports from `ucns_recursive` still work but are deprecated for direct user imports.

**Standard relationship.** This is an API stability boundary, not a mathematical claim.

## hmmm
