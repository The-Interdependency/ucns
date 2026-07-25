# EDCM real-system corpus candidates

**Research authority:** Erin Spencer  
**Recorded:** 2026-07-25  
**Status:** candidate sources found; none ingested, selected, or assigned to holdout  
**Decision surface:** [`UCNS_OPTION_DECISIONS.md`](UCNS_OPTION_DECISIONS.md)

## Purpose

EDCM requires real-system evidence before its UCNS configuration can close. The
corpus program must seek cases that make current examples look incomplete or
worst: contradiction, repair, retraction, refusal, ambiguity, unresolved
reference, speaker-ownership changes, graph disagreement, delayed resolution,
and information loss under projection.

A large average-case corpus is not enough. Each admitted source needs a pinned
version, license record, provenance receipt, privacy treatment, deterministic
adapter, and development/holdout partition.

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
- Boundary: sensitive content, imperfect redaction, dated provider behavior, and
  no independent EDCM outcome labels

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

## Proposed first corpus stack

No source should carry the whole claim. The smallest useful development stack
is:

1. **WildChat-1M:** uncontrolled human-model failure and correction.
2. **PRISM:** preference, interpretation, and alternative-response evidence.
3. **ICSI:** natural multiparty ownership, repair, and extended state.
4. **Molweni:** explicit discourse relations and unresolved references.
5. **MultiWOZ 2.1:** task state and observable completion or failure.

AMI adds multimodal and decision-process evidence. LMSYS adds model diversity
but should remain outside the first ingestion step until its gated license is
accepted and its non-redistribution boundary is implemented.

## Failure-first partition rule

Development slices should deliberately over-sample:

- corrections that fail or require repeated repair;
- assertions later negated, qualified, quoted, or retracted;
- unresolved, contested, or speaker-dependent references;
- identical node support with different edges or graph state;
- topic changes and delayed causal dependencies;
- refusals, hedges, blame transfer, shutdown, and escalation;
- cases where exact evidence and a projection disagree;
- empty, malformed, multilingual, or code-switched turns;
- incomplete tasks and contradictory annotations.

Only after these slices stabilize the configuration should a corpus be
partitioned into ordinary development traffic and a locked holdout. Selection
criteria, random seeds, source hashes, adapter versions, exclusions, and every
manual label must be recorded before the holdout is read.

## Admission gates

A corpus is not admitted merely because it is downloadable. Admission requires:

- license and redistribution review;
- consent and privacy treatment appropriate to the source;
- immutable source version or content hash;
- ordered-turn and speaker-identity preservation;
- distinction among source text, redaction, transcription, and annotation;
- deterministic conversion into an EDCM-specific profile;
- development/holdout separation;
- explicit outcome-label provenance;
- a removal path for sources with deletion obligations.

No raw restricted corpus belongs in the UCNS repository.

## hmmm

The corpora have been found, not domesticated. The next honest step is a small,
version-pinned ingestion manifest and failure-first slice from one open source;
otherwise seven datasets merely become seven impressive ways to postpone the
first ugly transcript.
