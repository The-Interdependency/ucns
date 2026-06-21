GPT generated; context, prompt Erin Spencer.

# UCNS Mathematical Glossary

## hmm

This glossary is deliberately conservative. It gives working definitions for the current UCNS v1.0 review surface without asking the reader to accept broader claims.

---

## 1. UCNS object

A UCNS object is the recursive data object currently implemented as `UCNSObject(n_dec, n_min, A_plus, F_plus)`. `A_plus` is an ordered sequence of `(angle, payload)` pairs, and each payload is either another UCNS object or `None`.

Example: `S2 = UCNSObject(2, 2, [(0, None), (1, None)], [0, 0])`.

A raw integer such as `7` is not by itself a UCNS object until encoded into the UCNS representation.

---

## 2. Unit payload

`None` is the unit payload. It represents absence of recursive payload content in a cell and is exported as `UNIT`.

A flat object has only `None` payloads.

---

## 3. Cell

A cell is one entry of `A_plus`: an ordered pair `(angle, payload)`. A face bit is not stored in the cell pair; face bits live in the parallel `F_plus` sequence.

---

## 4. Angle / phase position

The angle component records a rational position on the UCNS angular carrier. Current code uses rational angular positions; v1.0 does not require arbitrary real-valued angles.

---

## 5. Face sequence

`F_plus` is a binary sequence parallel to `A_plus`. Face values are structural bits, not truth values in a logical proposition.

---

## 6. Declared carrier (`n_dec`)

`n_dec` is the declared carrier or presentation resolution attached to the object. It is not the same as sequence length.

---

## 7. Minimal carrier (`n_min`)

`n_min` is the minimal carrier order associated with the object's anchor lattice. It is not necessarily equal to `len(A_plus)`.

---

## 8. Recursive depth

Recursive depth is the nesting depth of payloads:

```text
None -> depth 0
UCNSObject -> 1 + max(depth(payloads))
```

Depth measures payload nesting, not number of cells.

---

## 9. Multiplication

`multiply(A, B)` forms a cellwise recursive product. For candidate factors with cell counts `p` and `q`, the product has `p*q` cells. Product payloads are recursively multiplied from corresponding input payloads.

Factorization may be non-unique; multiplication being defined does not imply a unique inverse.

---

## 10. Factor search

Factor search asks: given a product object `P`, recover a non-trivial pair `(A, B)` such that `multiply(A, B) == P`.

Current implementation: `factor_search_v08(P, catalogue=None)`.

If the solver returns `SEQ-PRIME`, that result is absolute only inside a declared complete domain.

---

## 11. Catalogue

A catalogue is a finite list of payload candidates supplied to the factorization solver. `generate_payload_catalogue()` returns `None` plus the current depth-1 oracle atoms inside the frozen bounds.

---

## 12. Catalogue coverage

A catalogue covers a factorization when it contains every recursive payload appearing in the true factors. Catalogue coverage is a strong assumption; it does not solve the separate problem of discovering a small useful catalogue from `P` alone.

---

## 13. Witness matrix

A witness matrix is the global consistency structure used to verify that recovered candidate payload assignments explain every product cell simultaneously. Passing a local quotient step is not enough; all witnesses must agree globally.

---

## 14. Oracle class

The depth-2 oracle class is the class of objects whose payloads are drawn from the declared oracle atoms. Oracle-complete does not mean generally complete outside the oracle assumptions.

---

## 15. Frozen domain D'

D' is the standing bounded depth-2 domain:

```text
depth <= 2
|A_plus| <= 3
n_min <= 4
```

Products of D' factors may have more cells than either factor; domain membership constraints apply to the object being classified.

---

## 16. Multiplicative unit group

The multiplicative unit group is broader than the identity element. In current code, `is_unit` identifies the identity, while `is_multiplicative_unit` identifies the broader class of length-1 UNIT-payload objects that must be filtered as trivial factors.

This is analogous to excluding unit factors when defining primality.

---

## 17. `SEQ-PRIME`

`SEQ-PRIME` is the sentinel returned by `factor_search_v08` when no non-trivial factorization is found under the current solver and catalogue.

Example: a flat length-2 object returns `SEQ-PRIME` in the defended depth-1 domain after multiplicative-unit factors are filtered.

This is a scoped negative search result, not automatically a universal primality theorem.

---

## 18. Theorem N

Theorem N is the catalogue-sufficient factorization claim: if `P = multiply(A, B)` and the catalogue contains every recursive payload appearing in `A` or `B`, then `factor_search_v08(P, C)` returns valid factors.

It does not claim efficient catalogue discovery, efficient scaling for large catalogues, carrier widening, or total general primality.

---

## 19. Public API

For v1.0, `ucns` is the public import namespace. `ucns_recursive` remains a compatibility shim.

Preferred import:

```text
from ucns import UCNSObject, multiply, factor_search_v08
```

## hmmm
