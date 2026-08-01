# UCNS reproducible witness and experiment manifests

**Status:** bounded research infrastructure; no candidate is canonized here.  
**Consumers:** internal UCNS candidate research only.

## Purpose

Candidate evidence must survive process restarts, code movement, and independent review. An experiment therefore identifies its subjects, witness corpus, candidate implementation, law suite, structural policies, numerical comparison policy, traversal policy, and declared environment.

## Explicit serialization

UCNS does not hash arbitrary Python objects. A `ContentAdapter` is named and versioned and must produce bytes for the subject domain it claims to encode.

A `SubjectRecord` contains the untouched subject and a digest derived from:

- adapter name and version;
- adapter-produced bytes;
- a UCNS subject-domain prefix.

The digest identifies evidence only. v0.16 explicitly prohibits using it,
runtime hash, `repr`, or object identity to derive a geometric assignment.
v0.17 consumes v0.16 admission identity for ordering and provenance only; its
typed initiation receipt does not turn that digest into a Structural Null
prestate, geometric coordinate, orientation, or completion law.
v0.18 accepts independent exact rational coordinate input only after explicit
initiation. The proposal records `derived_from_evidence_identity = false`; the
subject digest remains linked provenance and cannot populate transverse,
lifted-turn, frame, side, or assignment-law fields. Equal-content occurrences
may therefore retain equal digests and receive distinct explicit proposals
without deduplication or hidden derivation.
v0.19 derives a candidate coordinate from structural source address rather
than evidence identity. The only law inputs are the exact occurrence index and
the cardinality of its complete finite ordered v0.17 trace. The derivation
retains the exact trace and outcome objects and records that content and digest
were unused. Equal-content occurrences therefore receive distinct coordinates
when their ordered addresses differ. Prefixes, reordered traces, and copied
upstream graphs cannot substitute for the authority-bearing trace. Binary64
remains a linked rendering, and the law remains nonselected.

JSON, text, and bytes adapters are supplied as conveniences. Domain objects require domain adapters.

## Witness corpora

A `WitnessCorpus` retains content-addressed subjects and named cases. Every case records:

- its subjects;
- expectation;
- origin: hand-authored, generated, adversarial, historical, mutation, or metamorphic;
- partition: development or holdout;
- authorship and provenance.

Development and holdout partitions remain distinct. Hidden holdout material may live outside the public repository while its corpus digest remains pinned by the experiment.

## Experiment manifest

An `ExperimentManifest` pins:

- candidate name, kind, version, code reference, scope, and policy dependencies;
- corpus digest;
- law-suite digest;
- structural-policy digests;
- numerical-comparison policy;
- recursive-traversal policy when applicable;
- declared environment fields.

Callable bytecode is not guessed or implicitly hashed. A candidate's explicit code reference is part of its identity.

## Overfitting safeguards

The infrastructure supports:

- development and holdout partitions;
- generated mutations;
- metamorphic transforms;
- adversarial and historical witness origins;
- greedy counterexample minimization;
- separate candidate, witness, and decision authorship records.

A decision packet is not reviewable unless both development and holdout reports pass and rollback behavior is recorded. Reviewable does not mean canonical.

## Reproduction

Two runs claiming the same manifest are compared through an explicit result adapter. The reproduction record stores matching digests or explains why reproduction could not be established.

## Nonclaims

This infrastructure does not establish mathematical truth, select a candidate, provide hidden-witness storage, or transfer theorem status.

hmmm: corpus quality and external holdout custody remain independent evidence obligations.
