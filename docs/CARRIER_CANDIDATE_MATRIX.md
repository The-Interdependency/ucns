# UCNS–EDCM v0.5 carrier candidate matrix

> **Status:** option-preserving comparison specification. No carrier relationship, product character `M`, or faithful-breadth candidate `B` is selected or ranked.
>
> **Experiment boundary:** carrier assignment and complete trajectory come before visible, radial, or scalar projections. Carrier pairing may be investigated after assignment; typed payload dispatch remains outside v0.5.

## 1. Relationship candidates

v0.5 compares exactly three mutually exclusive relationship claims.

| ID | Relationship claim | Required evidence | What would falsify it |
|---|---|---|---|
| `C1-direct-mobius` | The EDCM target is a direct Möbius carrier whose native state supplies the initiation twist, orientation change after 360°, and complete return after 720°. | A source-preserving native state, a unique causal initiation event, orientation/sidedness evidence, exact inverse behavior, and scoped completion receipts. | Failure to preserve a required source or causal distinction; no nontrivial state change after 360°; no complete return after 720°; or dependence on an undeclared cover to define native state. |
| `C2-cover-chart` | The implemented directed 720° cover is a chart or lifted presentation of a distinct Möbius carrier. | An explicit, versioned map between cover states and Möbius states that preserves source assignment, initiation causality, orientation/sidedness, ordered parentage, 360° visible coincidence, and 720° complete return. | Two states identified by the proposed map differ in any required retained distinction; a required Möbius state has no cover representative; or the map imports the twist only as a label rather than preserving its causal action. |
| `C3-incompatible` | The direct Möbius carrier and directed cover cannot represent one another while preserving all decided EDCM distinctions. | A minimal separating witness plus the precise invariant that no admissible map can preserve. Both source structures and the failed map attempt remain available. | Construction of an explicit map satisfying every v0.5 preservation and inverse obligation for the witness domain. |

`C3-incompatible` is a relationship verdict, not a third geometric carrier implementation. It remains a necessary candidate because incompatibility is preferable to silently identifying structures that retain different information.

No candidate is a fallback or default. Failure of one candidate retains the other two; agreement by two candidates is not a vote.

## 2. Required comparison dimensions

Each candidate report must fill every dimension below with `preserved`, `lost`, `unresolved`, `not-applicable`, or `error`, followed by a source-linked witness.

| Dimension | `C1-direct-mobius` question | `C2-cover-chart` question | `C3-incompatible` question |
|---|---|---|---|
| Structural Null / hidden zero | Is the superpositioned SPACE-origin condition native and singular without rewriting source manifestations? | Does the chart map preserve the singular origin and every exact SPACE witness? | Which null or origin distinction prevents a faithful map? |
| initiation causality | Does crossing the origin initiate each new word gonol? | Does the map preserve the event and its pre/post state rather than merely its label? | Which initiation history becomes indistinguishable? |
| seam uniqueness | Is the initiation seam derived uniquely from the declared origin and source boundary? | Is seam identity invariant under the chart map? | Which competing seams or anchors cannot be reconciled? |
| 360° state | Is visible position restored while orientation/sidedness remains changed? | Do cover deck state and Möbius orientation correspond exactly? | Which 360° distinction one representation cannot express? |
| 720° return | Does the complete state return under declared equivalence? | Does the round trip commute through the chart map? | Which retained distinction prevents complete return equivalence? |
| exact inverse | Does every declared transition have an exact inverse over retained state? | Do forward and inverse maps commute with candidate motion? | What minimal transition loses invertibility? |
| exact source | Are value, code point, offset, speaker turn, and source identifier reconstructable? | Does mapping leave the untouched source witness linked and exact? | Which map step would normalize, merge, or drop source evidence? |
| ordered concatenation | Are word order, occurrence order, multiplicity, and left/right sidedness retained? | Does the map preserve the same order and sidedness? | Which ordered pair collapses or commutes incorrectly? |
| recursive parentage | Are prior nodes and reference receipts retained without flattening? | Does the chart preserve parent identity and edge direction? | Which shared or repeated parent becomes indistinguishable? |
| completion scope | Is completion tied to a declared construction and boundary? | Does the chart preserve that scope and its receipt? | Which scope is broadened, narrowed, or lost? |
| projection loss | Does every projection name every discarded distinction? | Can every chart or scalar output recover the complete source trajectory? | Which claimed projection hides a required distinction? |

A missing value is not zero. An exception or inability to represent a dimension is retained as evidence.

## 3. Map obligations for `C2-cover-chart`

Calling the directed cover a “Möbius chart” requires more than matching periods.

For the declared witness domain, the candidate must provide:

1. a map from complete cover states to complete Möbius states;
2. a map back to cover states;
3. declared state-equivalence policies on both sides;
4. round-trip evidence under those policies;
5. commutation evidence for initiation, 360° motion, 720° motion, and exact inverse motion;
6. preservation evidence for source, order, multiplicity, sidedness, and recursive parentage; and
7. an explicit loss record for any non-bijective projection.

A shared visible 360° coordinate or a shared nominal 720° period is necessary comparison evidence but is not sufficient to establish a chart relationship.

## 4. Separation obligations for `C3-incompatible`

An incompatibility report must be constructive. It must identify:

1. the smallest source-preserving witness currently known;
2. the candidate maps attempted;
3. the exact invariant violated by each map;
4. the two complete states that become incorrectly identified or separated;
5. whether the failure concerns assignment, initiation, motion, return, inverse, parentage, or completion; and
6. a rollback statement retaining both representations for later experiments.

“Incompatible” cannot be inferred merely because two implementations use different coordinates or vocabulary.

## 5. Product-character and breadth candidate cross-product

The carrier experiment does not select metrics. Every admitted carrier report must display all three registered cell-only product-character candidates and all three registered breadth candidates as a nine-combination cross-product.

Product-character candidates:

- `M-geometric-mean-positive-support`;
- `M-maximum-positive-support`;
- `M-minimum-positive-support`.

Breadth candidates:

- `B-log-aggregate-cell-support`;
- `B-cell-detail`;
- `B-retained-presence`.

| | `B-log-aggregate-cell-support` | `B-cell-detail` | `B-retained-presence` |
|---|---|---|---|
| `M-geometric-mean-positive-support` | display `M_geo × B_log` | display `M_geo × B_detail` | display `M_geo × B_presence` |
| `M-maximum-positive-support` | display `M_max × B_log` | display `M_max × B_detail` | display `M_max × B_presence` |
| `M-minimum-positive-support` | display `M_min × B_log` | display `M_min × B_detail` | display `M_min × B_presence` |

For each cell in this table, a report must retain:

- both candidate identities and versions;
- the complete input trajectory reference;
- output or explicit failure;
- evaluator scope;
- comparison policy;
- unresolved and unmeasured layers;
- law-suite results; and
- disagreement with every other displayed cell.

The nine displays are pressure instruments. Passing a law suite does not make a candidate canonical, numerical closeness does not establish structural equivalence, and majority agreement does not select a winner. A cell-only evaluator fails outside its declared scope rather than treating retained layers as absent.

## 6. Projection order

The lawful experiment order is:

1. preserve the exact source and boundary evidence;
2. assign under a named carrier candidate;
3. record initiation and complete motion state;
4. apply the separating falsifiers;
5. record candidate disagreement and unresolved status;
6. only then emit visible, radial, or scalar projections; and
7. link every projection back to the complete trajectory with declared loss.

A projection cannot be used as the sole identity of the state it summarizes.

## 7. Usage guidance

Use this matrix as the required comparison surface for issue #145 and any later carrier implementation. Reports should be grouped by witness, then carrier relationship, then the nine `M × B` displays. The report must not contain `selected`, `preferred`, `best`, `canonical`, or an implicit default field unless a separate authority decision has actually been recorded.

## hmmm

v0.5 gets leverage only if the candidates can disagree in public. The decisive evidence is not that two pictures both travel 720°; it is whether the same exact source occurrence, initiation cause, sided state, order, parentage, and completion receipt survive a reversible map between them.