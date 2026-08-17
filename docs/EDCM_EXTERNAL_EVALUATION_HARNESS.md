# EDCM external evaluation harness

**Status:** test-backed candidate-evidence transport; no benchmark selection, measurement validity, EDCM activation, or canon effect.

## Boundary

`ucns.external_evaluation` opens only after an execution-generated `FullCorpusCompletionReceipt`. It does not admit a corpus, expose corpus material implicitly, choose an evaluator, define a benchmark, or decide whether an evaluator's semantics are valid.

Every disclosed case explicitly carries:

- a unique ordered case id;
- a subject digest;
- a custody reference;
- a disclosure-authority id; and
- a canonical-JSON payload selected by the caller.

Raw corpus evidence is never fetched from the upstream receipt. The caller decides what payload may cross the process boundary.

## Evaluator identity and execution

The plan pins evaluator id, version, code reference, executable SHA-256, exact argument vector, declared environment-key names, network policy, wall timeout, input limit, and output limit. The executable path must be absolute and its bytes must match the declared digest before execution.

Environment values are process inputs but are deliberately excluded from receipts so secrets are not persisted. Their names must exactly match the declaration. Arguments are retained verbatim and therefore must never contain secrets.

The harness does not itself implement a network namespace. `caller-isolated` means the caller-supplied wrapper or environment enforces isolation; `declared-external` records that external transport may occur. Authentication and network enforcement remain `hmmm` rather than inferred.

## Protocol

The evaluator reads one canonical JSON request from standard input and emits one JSON response on standard output. Standard error is diagnostic evidence.

The response must contain exactly:

```json
{
  "schema_id": "ucns.edcm.external-evaluator-response",
  "schema_version": "1.0.0",
  "plan_id": "declared-plan",
  "evaluator": {
    "evaluator_id": "declared-evaluator",
    "evaluator_version": "declared-version"
  },
  "results": [
    {
      "case_id": "case-1",
      "status": "ok",
      "output": {},
      "evidence": ["evaluator-specific evidence"],
      "error": null
    }
  ]
}
```

Results must cover every requested case exactly once and in order. Allowed statuses are `ok`, `unresolved`, and `error`. Protocol, plan, evaluator, case coverage, JSON, timeout, executable, or resource disagreement produces an incomplete receipt; it is never converted to a score or skip.

## Receipt

The receipt retains request, stdout, and stderr digests; bounded output excerpts; byte counts; elapsed time; return code; timeout standing; parsed results; visible failure evidence; and its own identity. A completed receipt remains `candidate-measured-evidence` with:

```text
selection_effect: none
measurement_validity: not-established
edcm_activation: inactive
canon_status: none
```

## Next boundary

The next work is one preregistered UCNS representation benchmark. It must freeze its corpus cases, disclosed payloads, evaluator candidate, relation question, scoring/comparison rule, resource limits, and accepted outcomes before using this harness.
