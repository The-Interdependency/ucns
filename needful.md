# What UCNS needs to compare multimodal digital-object relations

UCNS already has much of the comparison laboratory, but it cannot yet compare multimodal digital-object relations successfully in a general or canonical sense.

The repository can preserve arbitrary evidence, identify it through versioned adapters, retain repeated layers, traverse graphs safely, run candidate evaluators, and compare their outputs under explicit policies. What is missing is the semantic bridge from modality-specific digital evidence to typed relations.

## What “successful comparison” must mean

For two multimodal objects, UCNS should return a structured result such as:

- equivalent under a declared relation;
- different under that relation;
- incomparable because required evidence is absent;
- unresolved because a policy, alignment, traversal, or resource boundary failed.

It should also return the evidence and receipts supporting that result. A Boolean similarity score alone would violate the repository’s preservation rules.

The comparison must be explicitly scoped. These are different questions:

- Are two files byte-identical?
- Do they encode the same audiovisual work?
- Does an image depict the entity named by a caption?
- Does an audio segment align with a video interval?
- Are two documents revisions of the same work?
- Does one object derive from, quote, contradict, or temporally precede another?

UCNS needs a named relation predicate for each question. It must not collapse them into generic “similarity.”

## What UCNS already provides

The reusable foundation is substantial:

- `ContentAdapter` provides versioned, reproducible evidence identity without hashing arbitrary Python representations: `src/ucns/experiments.py`.
- `SubjectRecord` snapshots the adapted evidence and binds its digest to adapter identity: `src/ucns/experiments.py`.
- `RetainedStructure` preserves repeated evidence layers without flattening them or silently measuring them: `src/ucns/envelope.py`.
- Recursive graphs can be traversed with explicit identity, cycle semantics, and budgets: `src/ucns/traversal.py`.
- Retained layers can be paired through occurrence-addressed plans with explicit treatment of unmatched evidence: `src/ucns/layer_pairing.py`.
- Candidate evaluators are named, versioned, scoped, and policy-bound: `src/ucns/laboratory.py`.
- Candidate output comparison already requires an explicit comparison policy: `src/ucns/laboratory.py`.
- Experiment manifests, witness partitions, reproduction checks, and decision packets already exist.

These are the correct research controls. They are not yet a multimodal relation model.

## What must be added

### 1. A typed digital-object envelope

Define a `DigitalObjectRecord` that preserves:

- stable occurrence identity;
- source URI or custody reference;
- exact source digest;
- media type and declared modality;
- byte length and encoding/container metadata;
- acquisition time and provenance;
- rights, consent, redaction, and access constraints;
- parent object and derivation history;
- ordered modality-part occurrences;
- the untouched source or an authenticated source reference.

The object must distinguish the work, file, encoding, rendition, segment, and occurrence. Two identical files may be distinct occurrences; two different files may be renditions of one work.

### 2. Versioned modality adapters

Add domain adapters rather than using the generic byte adapter as semantic identity:

- text: exact code points, offsets, spans, language declarations;
- image: dimensions, color space, orientation, frames, regions;
- audio: sample rate, channels, exact sample/time intervals;
- video: streams, time base, frames, shots, audio tracks;
- structured data: schema identity, records and paths;
- compound documents: pages, embedded media, layout regions and reading order.

Each adapter must emit a canonical evidence representation while retaining the original. Decoder/backend version, configuration, failures, and information loss belong in the adapter identity.

This is representation, not yet interpretation. OCR, transcription, object detection, embeddings, and captions must be separate candidate-derived layers.

### 3. A typed relation graph

The existing `Cell.relation` field is only arbitrary payload. UCNS needs first-class relation records containing:

- relation type and version;
- ordered endpoints with roles;
- directionality and arity;
- endpoint occurrence or segment selectors;
- temporal, spatial, textual, or structural anchors;
- asserted, observed, derived, or candidate standing;
- producer identity and code reference;
- supporting and contradicting evidence;
- confidence or interval only when its meaning is declared;
- provenance and information loss;
- unresolved fields and failure receipts.

Initial relation families should remain separate:

- identity: `same-bytes`, `same-encoding`, `same-work`;
- structure: `contains`, `part-of`, `references`;
- derivation: `revision-of`, `transcoded-from`, `excerpt-of`;
- alignment: `corresponds-to`, `temporally-aligns`, `region-describes`;
- semantic: `depicts`, `mentions`, `expresses`;
- logical or evidential: `supports`, `contradicts`;
- sequence: `precedes`, `overlaps`.

No universal relation algebra should be assumed.

### 4. Anchor and alignment types

Cross-modal relations are meaningful only when their endpoints are addressable. UCNS needs exact typed selectors:

- byte ranges;
- Unicode/code-point spans;
- page and layout regions;
- image rectangles or masks;
- audio sample/time intervals;
- video frame/time intervals;
- structured-data paths;
- graph-node references.

Conversions between coordinate systems need explicit versioned transforms and round-trip or bounded-error receipts. An OCR span cannot silently become the source image region, and floating timestamps cannot silently replace rational media time bases.

### 5. A relation-comparison protocol

Comparing two relation graphs requires more than comparing evaluator outputs. Freeze:

1. object and occurrence identity;
2. modality adapters;
3. endpoint identity and admissible correspondence;
4. relation vocabulary and version;
5. graph traversal policy;
6. alignment candidate;
7. structural projection policy;
8. modality-specific value comparator;
9. missing-evidence semantics;
10. aggregation and decision rule;
11. resource bounds and failure behavior.

The result should contain at least:

- matched relations;
- left-only and right-only relations;
- endpoint/alignment disagreements;
- property disagreements;
- retained incomparable evidence;
- truncation or decoder failures;
- declared losses;
- final `match`, `different`, `incomparable`, or `unresolved` verdict.

### 6. Modality-specific comparators

The current policies cover generic equality, tolerances, ULP distance, intervals, and custom functions. Multimodal work requires explicit candidates for:

- exact span and region equality;
- temporal overlap and boundary error;
- spatial overlap, containment, and coordinate-transform consistency;
- text equivalence under a specifically authorized normalization;
- sequence alignment;
- graph matching;
- calibrated semantic-model output comparison;
- uncertainty interval or distribution comparison.

These should extend the registry rather than create a hidden global comparator.

### 7. Typed evaluator dispatch

This is an explicit repository gap. Evaluator selection must depend on declared endpoint and relation types, not arbitrary callable behavior.

A dispatch rule should state:

```text
(relation type, left modality, right modality, adapter versions)
→ eligible evaluator candidates
```

Unsupported combinations must return `incomparable` or `unresolved`; they must not fall back to byte equality, generic embeddings, or string conversion.

### 8. Evidence-bearing extraction layers

Derived representations should be retained as separate, nonauthoritative layers:

- OCR;
- speech transcription;
- captions;
- detected regions or events;
- embeddings;
- entity links;
- temporal segmentation.

Every such layer needs model identity, version, parameters, source anchors, execution environment, uncertainty, and failure receipts. Raw evidence must remain reachable. Embeddings can be candidate instruments, never universal object or relation identity.

### 9. Laws and adversarial witnesses

At minimum, every relation comparator should be tested for:

- identity/reflexivity where applicable;
- symmetry only for symmetric relation types;
- direction preservation for directed relations;
- endpoint-role preservation;
- order and multiplicity preservation;
- invariance under declared lossless re-encoding;
- sensitivity to changed anchors or relation direction;
- no equivalence from shared metadata alone;
- no equivalence from missing evidence;
- stability under chunking and compound-object decomposition;
- explicit behavior for unsupported modality pairs;
- cycle and budget receipt preservation;
- source recovery after every lossy projection.

The corpus should include equal-content distinct occurrences, different encodings of one work, misleading metadata, offset timestamps, OCR/transcription errors, duplicated segments, reordered components, conflicting modalities, adversarial near-duplicates, and incomplete files.

### 10. Independent calibration and decision authority

The repository correctly says fixtures are not evidence of generality. Successful operation needs:

- real, licensed multimodal corpora;
- independently authored relation annotations;
- development and externally controlled holdout evidence;
- inter-annotator disagreement retained rather than averaged away;
- modality and relation-specific error analysis;
- reproduction across supported environments;
- rollback and migration behavior;
- a separate authority decision before any candidate becomes canonical.

## Smallest coherent implementation sequence

The decisive path is:

1. Define `DigitalObjectRecord`, typed anchors, and `RelationAssertion` without adding semantic evaluators.
2. Implement exact adapters for text, image, audio, and video containers.
3. Implement a relation-graph envelope and receipt-preserving comparison report.
4. Preregister one bounded comparison: for example, exact audiovisual segment-alignment relations across two renditions.
5. Add two independent alignment implementations and a frozen decision rule.
6. Execute against hand-authored, metamorphic, adversarial, and held-out witnesses.
7. Accept `distinguish`, `no-distinguish`, `incomparable`, or `unresolved`.
8. Only then consider broader semantic relations such as `depicts` or `expresses`.

## Bottom line

UCNS does not primarily need another scalar similarity metric. It needs a typed, provenance-preserving relation graph over modality-aware, addressable digital-object occurrences.

The present repository already supplies most of the governance and experimental machinery. The decisive missing surfaces are:

- multimodal object schemas;
- modality-native adapters;
- exact cross-modal anchors;
- typed relation semantics;
- typed evaluator dispatch;
- relation-graph comparison reports;
- independently calibrated real-world evidence.

Until canonical structural equivalence, retained-layer measurement, typed dispatch, and external calibration are resolved, UCNS can conduct rigorous candidate comparisons—but should not claim that it successfully or canonically compares multimodal digital-object relations.
