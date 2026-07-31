# EDCM real-system corpus candidates

**Research authority:** Erin Spencer  
**Recorded:** 2026-07-25  
**Status:** candidate sources found; the first complete downstream MultiWOZ 2.1
run exposed and repaired a SPACE-origin assignment defect; v0.14 now supplies a
fail-closed generic execution receipt, while the source-native adapter and
corrected complete MultiWOZ rerun remain downstream work
**Decision surface:** [`UCNS_OPTION_DECISIONS.md`](UCNS_OPTION_DECISIONS.md)

## Purpose

EDCM requires real-system evidence before its UCNS configuration can close. The
corpus program must seek cases that make current examples look incomplete or
worst: contradiction, repair, retraction, refusal, ambiguity, unresolved
reference, speaker-ownership changes, graph disagreement, delayed resolution,
and information loss under projection.

A large average-case total is not enough. Each admitted source needs a license
record, provenance receipt, privacy treatment, deterministic adapter, and a
completion receipt proving that every source turn was processed. The execution
unit is the full admitted corpus, not a sample or holdout partition.

## First full-run profile repair

The first complete downstream MultiWOZ 2.1 run processed all 10,438 dialogues
and 143,048 turns. Its `ucns.profile.edcm-word-gonol/0.1.0` report classified
4,094 source occurrences as out of alphabet:

| Source code point | Occurrences | Correct profile role |
|---|---:|---|
| U+0009 CHARACTER TABULATION | 1,976 | SPACE-origin manifestation |
| U+000A LINE FEED | 2,115 | SPACE-origin manifestation |
| U+00A0 NO-BREAK SPACE | 3 | SPACE-origin manifestation |

That report remains immutable evidence of the `0.1.0` profile behavior; it is
not rewritten into a corrected result. Profile `0.2.0` instead pins the Unicode
White_Space set, assigns each such source code point to the U+0020 position-zero
carrier token, and preserves the exact raw value, code point, offset, and turn
reconstruction. These 4,094 occurrences are therefore SPACE boundaries, not
alphabet failures, under the repaired profile. A new complete run must carry a
new profile identity and supersession receipt. Non-SPACE unmapped code points
remain retained and reported as positive coverage-failure evidence.

The v0.14 full-corpus execution gate now prevents a prefix, iterator failure,
or turn-count mismatch from receiving a post-run analysis receipt. It does not
retroactively receipt the historical run and does not establish that a
source-native MultiWOZ adapter matches the archived source artifact. See
[`FULL_CORPUS_EXECUTION_GATE_V014.md`](FULL_CORPUS_EXECUTION_GATE_V014.md).

## Candidate sources

### WildChat-1M — primary uncontrolled human-model development candidate

WildChat contains approximately one million opt-in real-world conversations and
more than 2.5 million interaction turns with ChatGPT. It is multilingual and
contains ambiguous, toxic, topic-switching, and otherwise irregular traffic
that polished benchmarks tend to remove.

- Source: [AllenAI WildChat-1M dataset card](https://huggingface.co/datasets/allenai/WildChat-1M)
- Paper: [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://arxiv.org/abs/2405.01470)
- Access: public, ODC-BY; approximately 3.36 GB
- EDCM value: correction chains, refusal, escalation, topic change, ambiguity,
  empty inputs, and long-tail behavior
- Boundary: sensitive content, imperfect redaction, and dated provider behavior;
  source text and redaction effects must remain distinguishable

### PRISM — preference and interpretation candidate

PRISM records 8,011 live conversations with 21 language models, linked to
fine-grained participant feedback and stated preferences. Its conversation
trees and alternative responses are useful for testing whether EDCM preserves
ownership, disagreement, subjective interpretation, and correction.

- Source: [PRISM project repository](https://github.com/HannahKirk/prism-alignment)
- Dataset: [PRISM on Hugging Face](https://huggingface.co/datasets/HannahRoseKirk/prism-alignment)
- Paper: [The PRISM Alignment Dataset](https://arxiv.org/abs/2404.16019)
- Access: human text CC BY 4.0; model text CC BY-NC 4.0 plus provider terms
- EDCM value: alternative responses, explicit ratings, open feedback,
  controversial prompts, and participant-linked interpretation
- Boundary: elicited research interaction rather than uncontrolled deployment;
  licensing differs across fields

### LMSYS-Chat-1M — cross-model field-traffic candidate

LMSYS-Chat-1M contains one million real-world conversations with 25 language
models collected through the Vicuna demo and Chatbot Arena. It offers broad
model and language variation, including unsafe conversations retained for
research.

- Source: [LMSYS-Chat-1M dataset card and license](https://huggingface.co/datasets/lmsys/lmsys-chat-1m)
- Paper: [LMSYS-Chat-1M](https://arxiv.org/abs/2309.11998)
- Access: gated acceptance; no redistribution; deletion requests must be honored
- EDCM value: cross-model comparison, multilingual traffic, moderation
  boundaries, and long-tail prompts
- Boundary: average dialogue is short, redaction can alter evidence, benchmark
  contamination is possible, and access terms prevent repository inclusion

### ICSI Meeting Corpus — natural multiparty system candidate

The ICSI corpus contains roughly 70 hours of naturally occurring multiparty
meetings with orthographic transcripts and dialogue-act annotations. It is
human-human rather than human-model evidence, which makes it valuable as an
independent interaction class instead of another copy of chatbot behavior.

- Source: [ICSI Meeting Corpus](https://groups.inf.ed.ac.uk/ami/icsi/)
- Access: transcripts, signals, and some annotations under CC BY 4.0
- EDCM value: interruption, repair, speaker ownership, unresolved references,
  disagreement, and extended group state
- Boundary: transcript and annotation evidence must remain distinct; spoken
  interaction cannot silently inherit chatbot adapters

### AMI Meeting Corpus — constrained collaborative process candidate

AMI contains about 100 hours of multimodal meetings. Roughly two-thirds are
scenario-elicited design-team meetings and the remainder are naturally
occurring meetings, providing both controlled tasks and messier collaboration.

- Source: [AMI Meeting Corpus](https://groups.inf.ed.ac.uk/ami/corpus/)
- Download and license: [AMI corpus downloads](https://groups.inf.ed.ac.uk/ami/download/)
- Access: signals, transcripts, and some annotations under CC BY 4.0
- EDCM value: decision points, assigned roles, disfluency, attention,
  disagreement, repair, and multimodal constraint
- Boundary: elicited and naturally occurring partitions must never be merged
  without preserving their provenance

### MultiWOZ 2.1 — task-state and failed-completion candidate

MultiWOZ 2.1 contains 10,438 human-human Wizard-of-Oz task dialogues with goals,
turns, belief state, booking state, and documented incomplete or erroneous
cases. It is not uncontrolled field traffic, but supplies observable task
constraints and outcomes.

- Source: [University of Cambridge MultiWOZ 2.1 deposit](https://www.repository.cam.ac.uk/items/74e8d468-9442-424a-bb3b-1bb88dcb8673/full)
- Access: CC BY 4.0; archived dataset approximately 13 MB
- EDCM value: state transitions, failed bookings, repair, constraint reduction,
  and measurable completion
- Boundary: crowdworker setting, annotation errors, and incomplete tasks are
  evidence—not noise to remove

### Molweni — discourse-graph and unresolved-reference candidate

Molweni derives 10,000 multiparty dialogues from Ubuntu chat and adds 78,245
discourse relations plus answerable and unanswerable questions. It directly
pressures the currently unresolved graph-contribution dimension.

- Source: [Molweni repository](https://github.com/HIT-SCIR/Molweni)
- Paper: [Molweni at COLING 2020](https://aclanthology.org/2020.coling-main.238/)
- Access: repository declares Apache 2.0
- EDCM value: directed relation labels, clarification, speaker identity,
  discourse graphs, and positive unresolved-reference evidence
- Boundary: it is a filtered and annotated derivative of Ubuntu chat; source,
  filter, and annotation effects must remain explicit

## Full-corpus run queue

Each admitted source is run in full. The queue orders engineering work; it does
not define a sample, ranking, or claim that earlier corpora are more
authoritative.

1. **MultiWOZ 2.1:** smallest open source in the set, useful for proving the
   end-to-end adapter, turn accounting, exact-text receipts, and complete-run
   reporting.
2. **Molweni:** full discourse-graph and unresolved-reference pressure.
3. **PRISM:** full preference, interpretation, and alternative-response
   pressure.
4. **ICSI:** full natural multiparty ownership, interruption, and repair.
5. **AMI:** full multimodal and decision-process evidence, with native
   partitions retained as provenance rather than execution fragments.
6. **WildChat-1M:** full uncontrolled human-model traffic after privacy and
   storage handling are ready.
7. **LMSYS-Chat-1M:** full gated source after license acceptance and
   non-redistribution controls are implemented.

The first engineering milestone is therefore a complete MultiWOZ run, not a
MultiWOZ slice. A source that cannot be processed completely is reported as an
incomplete run with the exact stopping point and reason.

## Failure-seeking post-run rule

Failure-seeking happens after each full run. Reports must surface and count:

- corrections that fail or require repeated repair;
- assertions later negated, qualified, quoted, or retracted;
- unresolved, contested, or speaker-dependent references;
- identical node support with different edges or graph state;
- topic changes and delayed causal dependencies;
- refusals, hedges, blame transfer, shutdown, and escalation;
- cases where exact evidence and a projection disagree;
- every non-SPACE out-of-alphabet code point and affected word gonol;
- repeated, leading, and trailing source-preserved SPACE manifestations;
- empty, malformed, multilingual, or code-switched turns;
- incomplete tasks and contradictory annotations.

Candidate configurations run over the same complete turn stream. Configuration
comparison may sort or filter the resulting evidence for inspection, but it may
not pretend that an inspected subset was the corpus execution.

## Admission gates

A corpus is not admitted merely because it is downloadable. Admission requires:

- license and redistribution review;
- consent and privacy treatment appropriate to the source;
- immutable source version or content hash;
- ordered-turn and speaker-identity preservation;
- distinction among source text, redaction, transcription, and annotation;
- deterministic conversion into the EDCM-specific word-gonol profile;
- exact speaker-turn count before and after conversion;
- a full-run completion or explicit incomplete-run receipt;
- iterator exhaustion, expected-turn-count agreement, and exact
  source/reconstruction stream-digest agreement before post-run analysis;
- exact non-SPACE out-of-alphabet and SPACE-origin boundary coverage totals;
- no source-text normalization or sampled execution;
- outcome-label provenance only when a separate predictive study uses labels;
- a removal path for sources with deletion obligations.

No raw restricted corpus belongs in the UCNS repository.

## hmmm

The first complete MultiWOZ 2.1 run did what the corpus program was meant to do:
it exposed a boundary error that fixtures missed. The repaired profile now needs
an immutable source-native full-corpus rerun and v0.14 completion receipt. After
that, Molweni
tests whether the same source-preserving profile retains graph and
unresolved-reference evidence without flattening it.
