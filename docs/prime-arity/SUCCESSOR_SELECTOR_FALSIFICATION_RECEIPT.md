# Prime-Arity Successor-Selector Falsification Receipt

Status: `INCUBATING` / `UNRESOLVED`

This audit is retained in UCNS experiment custody. It is not UCNS canon
and is not part of PCEA runtime.

JSON receipt SHA-256: `6ea75e9dd98863ced178750263094e0c401c5d7f8824ff7405896327772bb6db`

## Gate

The next role or carrier must be derived from retained UCNS structure without supplied q, future-label access, target tables, or fitted constants.

Tested candidates: 6; falsified: 6; survivors: 0.

## Anchor selectors

| selector | exact matches | tested | verdict |
|:---|---:|---:|:---|
| `least_unused_prime_append` | 0 | 2 | **FALSIFIED** |
| `least_unit_order_prime_append` | 0 | 2 | **FALSIFIED** |
| `least_squarefree_next_arity` | 0 | 2 | **FALSIFIED** |

Neither observed role transition is append-only, so supplying any new
coefficient-update role `q` cannot transform either source multiset into
its observed successor multiset.

## 3229-ladder selectors

Known HIT indices: [0, 1, 2, 5, 7, 8]

Known CONTROL indices: [3, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17]

| selector | exact next HITs | CONTROL landings | verdict |
|:---|---:|---:|:---|
| `immediate_decimal_step` | 3 | 3 | **FALSIFIED** |
| `factor_component_step` | 1 | 5 | **FALSIFIED** |
| `quartic_kernel_step` | 1 | 4 | **FALSIFIED** |

`scan_to_next_hit` and `known_hit_lookup` reproduce observations only by
consulting future labels or storing targets. They are rejected controls,
not surviving selectors.

## Standing

```text
coefficient recursion: PROVEN
successor q derivation: UNRESOLVED
tested successor laws: FALSIFIED
selector: MISSING
overall: UNRESOLVED
canon status: NONE
PCEA runtime status: NOT INCLUDED
```

## hmmm

The selector remains missing.
