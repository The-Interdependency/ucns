# Public Gonol definition-derived function table

**Authority:** Erin Spencer  
**Recorded:** 2026-08-18  
**Status:** implemented candidate

## Law

The exact Public Gonol position is the canonical function-table index. For
every punctuation or symbol position, the table binds the frozen Unicode 15.0
character name to source-present OEWN lexical entries and their already-closed
definition gonols.

```text
Public Gonol index
    ↓
frozen source character name
    ↓
OEWN lexical entry / definition gonol(s)
    ↓
definition-derived function binding
    ↓
caller-supplied current atomic gonol + ordered context
    ↓
closed contextual application gonol
```

There is no second symbol numbering and no independent punctuation grammar.
The character name locates lexical evidence; it is not an executable grammar.
OEWN definitions supply the function meaning. UCNS supplies coupling, order,
and atomic closure. The caller supplies context rather than the implementation
inferring prefix, infix, postfix, precedence, scope, or syntax from glyph shape.

## Complete declared table

`src/ucns/public_gonol_functions.py` covers all 84 Public Gonol positions whose
frozen Unicode category is punctuation or symbol. Digits remain quantities and
letters in every admitted script remain lexical glyphs; neither is silently
reclassified as punctuation.

Unicode names resolve directly or compositionally to OEWN lexical terms. Three
source-name gaps use explicit source-present semantic aliases:

- `NABLA` → OEWN `gradient`;
- `SUPERSET OF` → OEWN `set`; and
- `BECAUSE` → OEWN `reason` and `cause`.

The Unicode name retains the exact symbol distinction. These aliases do not
assign an operational grammar or claim that the OEWN terms exhaust every
mathematical or linguistic use.

The sealed receipt is
`generated/public-gonol-function-table-receipt.json`. Two complete builds are
byte-identical at SHA-256
`cabaa71bbae531993c2522e3e8cf30e26f37fcec030c1014f3495a5de62d9f69`.

## Frozen structural evaluation

The table's first contextual-control experiment is frozen in
`docs/PREREGISTRATION_PUBLIC_GONOL_CONTEXTUAL_EVALUATION.md` and its
outcome-free receipt is
`generated/public-gonol-contextual-evaluation-preregistration.json`. The
protocol is a separate producer boundary: it fixes all 84 indices, the
identity-only control, one existing anchor, ordered context multiplicities,
thresholds, and failure behavior before an evaluator can produce a result. It
does not add a usefulness, grammar, parser, or precedence result to this table.

The first exact execution is `BLOCKED`, as recorded in
`docs/PUBLIC_GONOL_CONTEXTUAL_EVALUATION_RESULT.md`: its first complete OEWN
source build exceeded the frozen 420-second bound before a contextual metric or
semantic receipt was emitted. This is neither a failing nor a surviving
function-table result, and it cannot be retried under the exhausted protocol.

## Contextual application

An application contains:

- the current atomic gonol identity;
- its application depth;
- the exact Public Gonol index and bound function identity;
- every definition gonol supplying the function;
- caller-supplied ordered context identities; and
- an intrinsic relation carrier joining those participants.

Closure returns a new atomic identity suitable for another application. Changing
the index, definitions, current state, order, multiplicity, or context changes
the result identity.

## Nonclaims

This construction does not establish semantic efficacy, correct punctuation
for every language, mathematical operator completeness, precedence, parsing,
syntax, context selection, geometry, EDCM measurement validity, or canon above
the declared candidate scope.

## hmmm

- empirical tests that the definition-derived bindings produce useful context;
- authority for selecting context rather than receiving it from the caller;
- multilingual function definitions and domain-specific symbol senses;
- geometry of the contextual application closure; and
- whether any function requires a more specific source than OEWN Core.
