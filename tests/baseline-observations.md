# Fresh-context no-skill baseline observations

## Conditions and evidence boundaries

Date of assessment: 2026-11-26. The controller supplied three independent fresh
no-skill evaluator records for scenarios 1, 3, and 6 in `scenarios.md`. This file
assesses those recorded responses; the assessor did not rerun the prompts or
independently reopen the paper, textbook, or code. The exact prompts and source
conditions are in the scenario rubric. The records contain verbatim assistant
responses, tool/source inventories, and access limitations.

Local audit records, retained by the controller outside the published skill:

- `.superpowers/sdd/2026-11-26-learner-first-paper-reading/baseline-s1.md`
- `.superpowers/sdd/2026-11-26-learner-first-paper-reading/baseline-s3.md`
- `.superpowers/sdd/2026-11-26-learner-first-paper-reading/baseline-s6.md`

The controller identifies these as independent fresh controls without the new
skill. Each record says no paper-reading skill, memory file, or repository file
was read and no subagent was spawned; writing its own evidence report was the
only recorded filesystem mutation. Model/version, sampling configuration, and
complete evaluator dispatch transcripts are not present in the supplied records.
These are three observed runs, not a frequency estimate or proof that all hosts
behave the same way. No new-skill behavior has been evaluated yet.

## Scenario 1: Beginner starts DLinear

**Assessment:** Partial pass. No summary-first failure was observed. The observed
gaps concern the opening agreement and explicit learner-owned original reading.

**Observed passes and response features**

- The opening proposes small steps: “先弄懂论文在问什么，再理解 DLinear 怎么做，
  最后检查实验能支持哪些结论.” It says the assistant will explain with an example
  and ask the learner to restate it. This is real process/role disclosure,
  although it is not the complete opening contract.
- It identifies the inspected arXiv copy as v3, revised 17 August 2022. The
  record reports that both abstract-page metadata and the extracted PDF version
  stamp supported that identity. It does not claim to have read the entire paper.
- It teaches a bounded input/output prerequisite using electricity demand and
  the quantities L, T, and C. It avoids a field-wide lecture, complete DLinear
  summary, code execution, and reviewer criticism.
- It cites Section 2 for task formulation and the introduction/Section 4 for
  the research question. The record's inspected PDF excerpt covers those places.
- It ends with one consequential question about 15-minute temperature/humidity
  observations and pauses for an answer. This is a genuine comprehension pause.

**Observed gaps and exact categories**

- **OPENING_ROUTE_AGREEMENT_MISSING:** It moves directly from the route to
  “第一步：先看懂它要预测什么” and substantive teaching. It never asks the learner
  to agree to the route before starting. The earlier source-inspection update
  also proposes a next step without requesting agreement.
- **OPENING_TARGET_AND_READING_ROLE_INCOMPLETE:** The opening describes examples
  and teach-back, but does not explicitly set the learner's original-paper
  reading role or the end-of-session independent reconstruction target. The
  novice level is reflected in its teaching rather than stated as an assumption.
- **ORIGINAL_READING_ASSIGNMENT_NOT_YET_PRESENT:** Section links are offered as
  citations, but no selected section is assigned for the learner to read with a
  reading question or read/skim/defer rationale. The final question checks the
  assistant's toy example. This turn therefore demonstrates a comprehension
  pause, not an original-paper reading pause. Whether a later turn would add
  that reading step is untested.
- **SOURCE_COVERAGE_DISCLOSURE_PARTIAL:** “我已打开…论文 PDF” accurately reports
  opening the PDF. The response does not disclose that only the returned excerpt
  was inspected. This is incomplete coverage disclosure, not an observed false
  assertion of full-paper reading.

**Source/tool coverage:** The record reports `functions.exec`/`web__run` opening
the official arXiv abstract and following its PDF and HTML links. The visible PDF
extraction covered lines 0–339 of 1,272, including Sections 2–4 and the opening
experimental results/table. The HTML result exposed metadata but no body lines.
No figure screenshots, appendices beyond the excerpt, code, secondary sources,
or alternate paper versions were inspected. `apply_patch` wrote the audit record.
All requested endpoints opened; no technical access failure was reported.

**Continuation boundary:** No simulated learner continuation was produced. The
response requested a content answer rather than route agreement, so behavior
after agreement and later reading stages remain untested.

**Implication for the skill contract:** Preserve the control's small examples,
source identity, single-question pacing, and restraint. Add a concise complete
opening, a real route-agreement pause in guided mode, explicit inspected coverage,
and a learner-owned original reading assignment. Do not justify the skill by
claiming this control dumped a full summary; it did not.

## Scenario 3: External prerequisites and focal-paper evidence

**Assessment:** Pass on the substantive explanation, source/provenance boundary,
and return-to-paper criteria exercised by this prompt. No background-to-paper
evidence substitution or invented-link failure was observed.

**Observed passes and response features**

- It opens with the mechanism and its boundary: “It gives an estimated
  separation, whose quality depends on the averaging window.” It defines trend
  and seasonality and attributes those definitions to Hyndman and Athanasopoulos's
  textbook rather than DLinear.
- The response labels its own worked construction “my toy example,” calculates
  `(11+14+11)/3=12`, explains cancellation, and then states the assumptions about
  balanced seasonal weights and slowly changing trend. It notes window error
  and residual noise instead of promising exact latent-component recovery.
- It supplies direct textbook chapter links and named section titles. The
  record reports actually opening the relevant textbook sections and following
  redirects to the canonical consolidated decomposition chapter.
- “Now return to these exact places in the paper” introduces Section 3 on PDF
  page 3, Section 4 on page 4, and Section 5.2/Table 2 on pages 4–5. These are
  bounded original-paper reading pointers and match the recorded inspected text.
- It distinguishes the textbook, the paper's construction, its own illustrative
  example, and the limits of the evidence through attribution and prose. Literal
  headings for every voice are not required by this rubric. It explicitly says
  benchmark comparisons “do not establish that moving averages recover the true
  physical trend and seasonality, or that decomposition always improves
  forecasting.” That marks what the available evidence does not establish.
- Its closing distinction is direct: “The textbook supplies the background and
  its assumptions. DLinear uses that background as a model design and evaluates
  the resulting forecasts.” External background is not counted as experimental
  evidence for the focal paper.

**Observed gaps and exact categories:** No substantive scenario-3 failure category
is supported by this record. The response provides short reading pointers rather
than a follow-up teach-back question, which satisfies the scenario's alternative
of assigning the relevant reading. Whether the learner can apply the explanation
is untested; absence of a follow-up turn is not evidence of learner mastery or of
a teaching failure.

**Source/tool coverage:** The record reports `functions.exec`/`web__run` inspecting
the arXiv abstract and v3 PDF text, especially Sections 3, 4, 5.2 and Table 2;
the textbook graphics chapter Section 2.3; and decomposition Sections 3.2–3.4.
The legacy `components.html` and `classical-decomposition.html` URLs redirected
to `https://otexts.com/fpp3/decomposition.html`; the final response uses that
canonical chapter and `https://otexts.com/fpp3/graphics.html`. A PDF-page
screenshot request produced no visibly rendered image in the tool output; the
response does not rely on visual inspection. No official code or cited
Autoformer/FEDformer papers were opened. `apply_patch` wrote the audit record.
No source access failure was reported.

**Implication for the skill contract:** Preserve and standardize behavior already
demonstrated without the skill: authoritative inspected links, mechanism plus
worked example, assumptions/limits, visible attribution, and return to the
original paper. This baseline supports a regression contract, not a claim that
the host cannot provide sourced prerequisite teaching. Do not add a requirement
for mechanical headings solely because the control used clear prose attribution.

## Scenario 6: Reported forward smoke test

**Assessment:** Pass on rejecting reproduction inflation and choosing bounded
next checks. Partial coverage of the stronger six-level/reporting contract.

**Observed passes and response features**

- It immediately rejects the proposed wording: “No. You have established that
  your implementation passes a forward-pass smoke test, not that you have
  reproduced the paper.” No claim of successful paper reproduction is made.
- It limits the result to the supplied random input and output, and explicitly
  says the run does not establish paper computation, training, or reported
  forecasting performance. It does not infer conceptual or mapping correctness
  from shapes.
- Its proposed report wording names the smoke test and states that training and
  evaluation against the paper's protocol remain pending.
- It recommends checking dataset/version, chronological splits, variables,
  normalization, lengths, preprocessing leakage, and equations/configuration
  before training. Then it separates a small training check from protocol-based
  training/evaluation and reported-metric comparisons. No expensive execution or
  claim of independently running the model occurs.

**Observed gaps and exact categories**

- **REPRODUCTION_LADDER_INCOMPLETE:** The response covers mapping, forward
  validation, small training, and metric comparison, but does not explicitly
  identify conceptual understanding as a separate level or distinguish metric
  consistency from full reproduction across the reported settings. Its final
  permission to claim “reproduced the reported results” is conditional on
  supporting experiments, but does not explain that one matching metric alone
  remains insufficient. This is missing ladder coverage, not an observed claim
  that one metric proves full reproduction.
- **REPORTED_EVIDENCE_QUALIFIER_MISSING:** The source record correctly says no
  run was independently inspected, but the user-facing answer does not explicitly
  say “based on your reported run” or equivalent. “You have established” and the
  proposed report wording treat the prompt's account as the premise. They do not
  claim that the assistant independently verified execution; the improvement is
  clearer attribution, not correction of fabricated tool use.
- **EXPECTED_SHAPE_NOT_VERIFIED:** The response calls the dimensions “expected
  output dimensions,” although no paper or configuration was supplied to verify
  what the expected dimensions should be. The observed evidence establishes the
  reported shape only. Its later warning that matching shapes can hide incorrect
  computations is appropriate but does not supply the missing shape specification.
- **NEXT_SOURCE_REQUEST_NOT_PRESENT:** Concrete alignment checks are suggested,
  but the answer does not request the missing paper/code/protocol needed to
  perform them against actual expectations.

**Source/tool coverage:** The evaluator used the user prompt and ordinary
reasoning only. No paper, implementation, dataset, logs, external sources, memory,
or skill files were inspected; no code was executed. `functions.exec` invoked
`apply_patch` solely to write the audit record. No technical access failure was
reported. These conditions support assessment of response wording and next-step
selection, not verification of the claimed run or any paper-specific protocol.

**Implication for the skill contract:** Preserve the control's clear rejection of
reproduction inflation, evidence-bounded report wording, and pre-training checks.
Add the explicit six-level ladder, the one-metric/full-settings distinction,
reported-versus-witnessed execution attribution, and a request for the missing
source before verifying expectations. Do not characterize this control as having
called the paper reproduced.

## Task 1 conclusion and limits

The required three controls have actual response evidence. The observed gaps are
primarily session-contract/original-reading enforcement (scenario 1) and explicit
ladder/source-attribution coverage (scenario 6). Scenario 3 demonstrates that
good prerequisite sourcing and evidence boundaries already occur without the
new skill. Scenarios 2, 4, 5, and 7 were specified but were not run as no-skill
controls in this task. No with-skill pass, full reading session, learner learning
outcome, or reproduction result is claimed by these baseline observations.
