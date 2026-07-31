# UCNS–EDCM v0.14 full-corpus execution gate

**Status:** implemented, test-backed procedural evidence; report schema
`0.14.1`. No real-system corpus is admitted or executed by this module, no
post-run falsifier is satisfied by the gate alone, and no carrier, EDCM, or
METAPAT activation follows.

**Predecessor:** the v0.13
[`partial initiation boundary`](PARTIAL_INITIATION_BOUNDARY_V013.md).

## Question

EDCM requires every turn of each admitted corpus to run before failure-seeking
comparison or candidate admission. The existing `observe_corpus()` iterator
preserved order and performed no sampling, but it could not prove that a caller
actually exhausted the iterator.

v0.14 asks:

> What is the smallest fail-closed receipt that distinguishes a complete
> admitted-corpus execution from a prefix, iterator failure, malformed turn, or
> declared turn-count mismatch?

## Manifest boundary

`AdmittedCorpusManifest` requires:

1. corpus and source version;
2. source-artifact SHA-256 digest;
3. externally declared expected speaker-turn count;
4. license identity;
5. privacy treatment;
6. redaction policy;
7. source-native adapter identity, version, and code reference; and
8. the external admission decision identity.

This module validates that those fields are present. It does not perform the
legal, privacy, consent, redaction, or admission decision and cannot mint its
own authority.

## Complete-run gate

`execute_admitted_corpus()` consumes the supplied iterable until one of two
things happens:

- `StopIteration` proves exhaustion of the supplied turn stream; or
- iteration or exact profile observation fails and an incomplete report records
  the stopping turn index and stable failure class.

A report can be `complete` only when all of these are true:

```text
iterator exhausted
and processed turn count = admitted expected turn count
and exact source stream digest = reconstructed observation stream digest
and no failure exists
```

The stream digest uses ordered, length-prefixed records containing turn index,
speaker identity, and exact UTF-8 text. It is sensitive to source value,
speaker, order, multiplicity, SPACE manifestation, and turn boundary. The fixed
EDCM profile continues to reject surrogate code points and perform no
normalization.

Only `execute_admitted_corpus()` binds the returned report to the module's
executed-run capability. A publicly constructed report with declared
`complete`, exhaustion, counts, and matching digest strings remains ineligible
for post-run analysis and cannot issue a receipt. Reconstructing or replacing a
report also drops that capability.

## Incomplete-run evidence

An incomplete report distinguishes:

- iterator failure;
- turn observation failure;
- exact reconstruction mismatch; and
- exhausted turn-count mismatch.

It retains the number of successfully processed turns, the exact stopping
index, partial stream digests, word-gonol count, SPACE-boundary count, and
carrier-unassigned count. Failure is evidence; it is not coerced to a zero,
empty, or passing result.

`issue_full_corpus_completion_receipt()` rejects every incomplete report.

## Receipt authority

The receipt identity binds the complete ordered manifest evidence identity:
corpus/version, source digest, expected count, license, privacy treatment,
redaction policy, admission decision, and adapter identity/version/code
reference. It also binds the fixed profile identity, both stream digests, all
reported counts, and inactive selection/activation standing. Distinct custody
or redaction declarations therefore produce distinct receipt identities even
when the supplied turn stream is otherwise identical.

A valid receipt opens only:

```text
failure-seeking post-run analysis
```

It does not:

- admit the source corpus;
- prove that a source artifact matches the supplied adapter stream;
- retain or replace raw corpus custody;
- retain or replace per-turn completion-motion trajectories;
- satisfy any carrier or metric falsifier;
- select a candidate;
- validate an EDCM scalar;
- activate EDCM; or
- activate METAPAT.

These firewalls keep execution completeness separate from empirical,
mathematical, measurement, and authority claims.

## Result

| Surface | Standing |
|---|---|
| explicit corpus/admission manifest | implemented evidence boundary |
| iterator exhaustion check | implemented |
| admitted expected-count agreement | implemented |
| exact source/reconstruction stream digest agreement | implemented |
| execution-generated report capability | implemented; public declarations alone remain closed |
| license/privacy/redaction-bound receipt identity | implemented |
| incomplete-run stopping receipt | implemented |
| gate before post-run analysis | implemented |
| source-native MultiWOZ adapter | unresolved |
| corrected full MultiWOZ 2.1 rerun | not performed here |
| later real-system corpus runs | not performed here |
| post-run falsifier implementations | unresolved |
| candidate or carrier selection | none |
| EDCM activation | inactive |
| METAPAT activation | inactive |

## Reproduction

```bash
python -m pytest tests/test_full_corpus.py -q
python -c "from ucns import AdmittedCorpusManifest, CorpusAdapterIdentity, execute_admitted_corpus, issue_full_corpus_completion_receipt; m=AdmittedCorpusManifest(corpus_id='fixture', corpus_version='1', source_artifact_sha256='a'*64, expected_turn_count=2, license_id='fixture', privacy_treatment='synthetic', redaction_policy='none', admission_decision_id='fixture/1', adapter=CorpusAdapterIdentity('fixture-adapter','1','inline')); r=execute_admitted_corpus(m, [('a','A B'),('b','A\u00A0B')]); print(r.status.value, r.processed_turn_count, issue_full_corpus_completion_receipt(r).receipt_id)"
```

## hmmm

The gate can now tell a full turn stream from a hopeful prefix. It still cannot
tell whether an external adapter faithfully represented every field in the
source artifact, whether custody is authenticated, or what the corpus teaches
about carrier geometry. That is the useful next boundary: first the source-native
MultiWOZ adapter and corrected full run, then failure-seeking analysis over its
complete evidence—not before.
