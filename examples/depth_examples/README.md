GPT generated; context, prompt Erin Spencer.

# UCNS Depth Examples

## hmm

These examples are intentionally small. Their job is to make the v1.0 review surface reproducible without requiring a reviewer to read the whole repository first.

Run each file from the repository root:

```text
python examples/depth_examples/depth1_minimal.py
python examples/depth_examples/depth2_oracle_minimal.py
python examples/depth_examples/depth3_catalogue_sufficient.py
python examples/depth_examples/insufficient_catalogue_failure.py
```

Expected behavior:

| Example | Expected result | Purpose |
|---|---|---|
| `depth1_minimal.py` | absolute `SEQ-PRIME` for a length-1 object | minimal defended-domain negative case |
| `depth2_oracle_minimal.py` | recovered factors recompose exactly | minimal oracle/composite recovery case |
| `depth3_catalogue_sufficient.py` | recovered factors recompose exactly with explicit catalogue closure | minimal Theorem N catalogue-sufficient case |
| `insufficient_catalogue_failure.py` | non-absolute scoped `SEQ-PRIME` | demonstrates why catalogue scope must be reported |

These files are examples, not new theorem proofs. The theorem/proof-status surface lives in `ucns-spec.md`, `ucns-theorem-n.md`, and `docs/claims-ledger.md`.

## hmmm
