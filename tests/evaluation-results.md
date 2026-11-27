# With-skill behavior evaluation

## Conditions and evidence boundaries

Assessment date: 2026-11-26. This assessment compares actual recorded responses
with the observable criteria in [scenarios.md](scenarios.md), rather than scoring
fluency, the scenario's stated temptation, or the presence of instruction text.
The controller supplied seven independent fresh-context records with the skill
available, one for each of the then-defined scenarios 1–7. Scenarios 8–10 were
added later as regression specifications and are not included in this historical
independent evaluation. Follow-up turns are retained in their original records,
not counted as additional independent opening samples. After the
scenario-7 correction, the controller supplied two further fresh-context records
for scenario 7 and neighboring scenario 5 with the updated skill. The assessor
read those reruns, all seven original raw records, the
complete skill entrypoint and routed references, the scenario rubric, the design
and implementation constraints, and [baseline observations](baseline-observations.md).
The assessor did not generate the recorded responses or independently reopen
their external sources, inspect code, or execute a forecasting model.

The controller-local raw records are retained outside the published skill at
`.superpowers/sdd/2026-11-26-learner-first-paper-reading/green-s1.md` through
`green-s7.md`. Each includes the verbatim response, files read, inspected sources,
and access limits. Post-correction records are retained in that same local
directory as `rerun-s7.md` and `rerun-s5.md`. Their inventories say no scenario
rubric, tests, design, plan,
or memory files were read by the response-producing evaluator. These are recorded
inventories, not independently reconstructed tool traces. Model/version, sampling
settings, and complete dispatch transcripts are not present in these records.

An opening that properly waits for route agreement is assessed as an opening,
not as a completed reading session. A later reading assignment, learner answer,
or learning outcome is not inferred from a promise to perform it. Similarly,
missing paper material is a source boundary, not evidence of a paper defect.

## Source and access record

All evaluators read `SKILL.md`. The table records the additional reference files
and source coverage reported by each evaluator; references are under `references/`.
External-source facts below describe those records, not a fresh source audit by
this assessor.

| Scenario | Routed references read | Actual source coverage and limits |
| --- | --- | --- |
| 1 | `guided-reading-workflow.md`, `source-quality.md`; `explanation-standard.md` for continuation | Opening: official arXiv abstract/metadata page showing v3, revised 17 August 2022. Continuation: version-specific v3 PDF title/version stamp and Section 2 task definition, extracted lines 97–114. Other returned text was not used as experimental evidence. No visuals, appendix, code, or publisher status checked. |
| 2 | `explanation-standard.md`, `figures-and-equations.md` | User-supplied equation and dimensions only. No paper, implementation, or external source required or inspected. |
| 3 | `explanation-standard.md`, `source-quality.md`, `evidence-and-review.md`, `figures-and-equations.md` | Official arXiv metadata, PDF text, and v3 HTML: decomposition discussion, Section 4, Appendix B.2. *Forecasting: Principles and Practice*, third edition: sections 2.3, 3.2, 3.3 and author page. Legacy component/moving-average URLs redirected to the consolidated decomposition chapter. Experimental rows were exposed incidentally but not audited. A screenshot request did not yield a viewable image; no visual observation claimed. No code or publisher version inspected. |
| 4 | `guided-reading-workflow.md`, `explanation-standard.md`, `source-quality.md` | Supplied initial teach-back and subsequent corrective answer only. No focal paper, results, external background source, or code inspected. Numbers are an expressly constructed counterexample. |
| 5 | `guided-reading-workflow.md`, `evidence-and-review.md`, `source-quality.md` | User's self-report of reading an introduction only; no identifying paper source or text supplied. No paper or external-source search performed. |
| 6 | `reproduction-levels.md`, `evidence-and-review.md`, `source-quality.md` | User-reported synthetic run only; no paper, code, configuration, dataset, log, checkpoint, or execution independently inspected. |
| 7 | `guided-reading-workflow.md`, `evidence-and-review.md`, `explanation-standard.md`, `source-quality.md` | Supplied illustrative excerpt only. No verified identity, full text, figures, protocol, or results. No search attempted, respecting the source restriction. |

## Scenario 1: Beginner starts DLinear

**Verdict: Pass for opening, agreed prerequisite bridge, and first original
reading assignment.**

- **Process before analysis:** The opening states the learner's independent
  explanation goal and assumes the stated limited neural-network background.
  It proposes input/output prerequisites, selected original reading, method,
  evidence, limits, and a closed-book reconstruction. It supplies no complete
  paper summary or reviewer verdict.
- **Roles, pause, target, missing input:** It says the assistant selects short
  locatable passages and explains blocking concepts; the learner reads them and
  writes their own understanding. It promises reading pauses and one question
  at a time, names the final reconstruction target, and reports no blocking
  material gap while leaving publication status unverified.
- **Source/provenance:** It explicitly identifies the inspected arXiv page as
  v3, revised 17 August 2022, and says only metadata and abstract were checked.
  It does not promote page access into full-paper inspection. No technical
  Background claim or method/result anchor is needed in this opening.
- **Agreement and continuation:** The opening ends with the single agreement
  question, “这条路线和节奏适合你吗？” The later response, after supplied agreement,
  inspects the version-specific PDF and teaches only the input/output task.
  Its labeled toy temperature example maps four observations to two forecasts
  using a last-observation rule, explicitly distinct from DLinear and accuracy.
  Paper-specific `L`, `T`, and `C` definitions are tied to inspected Section 2.
- **Original reading pause:** The continuation assigns only PDF page 2,
  Section 2's first paragraph, naming its start/end phrases. It explains why
  this paragraph is read now and defers the later strategy paragraph. One
  question asks the learner to apply the symbols to temperature/humidity and
  the 24-to-6 task. It explicitly stops for their own interpretation, without
  giving the complete paper interpretation, running code, or claiming mastery.

## Scenario 2: Direct formula explanation

**Verdict: Pass for the supplied focused explanation.**

- **Route and pacing:** The opening promises direct computation and a small
  example, says no questions are required, and identifies the equation-only
  source limit. The explanation is delivered immediately without agreement or
  a forced quiz.
- **Mechanism and precision:** Each row of `W` produces one weighted sum, then
  its entry of `b` is added. The response defines `x` as `L x 1`, `W` as `H x L`,
  `b` as `H x 1`, and the resulting `H x 1` output. It provides the indexed sum,
  calculates both outputs of its toy example (`5` and `9`), and explains fixed
  parameters, affine versus linear operation, and direct multi-output computation.
- **Boundary and provenance:** General mathematics is labeled Background and
  the numbers Analyst illustration. The missing paper role, training procedure,
  units, and accuracy are Unknown. It invents no focal-paper anchor or performance
  claim. No external link is necessary for this self-contained equation, as
  permitted by the rubric and explanation reference.
- **Next action:** The requested explanation is complete in this response.
  Learner mastery and any particular forecasting implementation remain untested.

## Scenario 3: External prerequisites and paper evidence

**Verdict: Pass for the focused prerequisite explanation and return to source.**

- **Mechanism, example, assumptions:** It explains why averaging a local window
  suppresses balanced fluctuations when the trend changes slowly, with explicit
  dependence on window length. Its marked toy series calculates centered means
  `12` and `13` and a residual `2`, then explains why exact recovery occurs only
  under the constructed balance and linear-trend conditions. The centered
  moving-average equation defines symbols, spacing, units, and endpoint limits.
- **Authoritative support:** Textbook third-edition sections 2.3, 3.2, and 3.3
  are linked beside the relevant Background definitions and assumptions. The
  inventory records inspection of supporting passages, source authorship, and
  redirects; final links use authoritative chapter destinations rather than
  search links. This is reported source inspection, not assessor re-verification.
- **Paper anchor and four voices:** The response identifies arXiv v3 and returns
  to Section 4, PDF page 4, the DLinear bullet, with Appendix B.2 for kernel size.
  Paper descriptions, textbook Background, the Analyst toy/interpretation, and
  Unknown experimental support are visibly separate. It says a defined residual
  can include noise and other variation; additive reconstruction is not proof
  of pure latent seasonality or general forecasting improvement.
- **Next action and limits:** It assigns the specific Section 4 bullet for a
  short return reading. A quiz is not mandatory in this focused route. It does
  not rely on the unsuccessful visual extraction or claim an experimental audit.

## Scenario 4: Demonstrated misconception

**Verdict: Pass for targeted reteaching, diagnostic pause, and correct-answer
progression.**

- **Exact diagnosis and pause:** “Let's pause before the results” explicitly
  stops progression. It identifies the false inference from a smoothing
  operation to true latent-component recovery, rather than accepting confidence
  as mastery or proceeding to results.
- **Mechanism and counterexample:** Background defines the three-point mean
  and residual and separates the reconstruction identity from component truth.
  Its Analyst construction uses true trend `10`, seasonal pattern `0,6,0,-6`,
  observed neighborhood `10,16,10`, mean `12`, and residual `4`, which differs
  from the true seasonal peak `6`. It explains window dependence, contamination,
  and why smooth forecasts alone cannot validate decomposition. This is a
  self-contained counterexample; an external authority is not needed to verify
  its arithmetic or definition.
- **Provenance and missing context:** It labels Background, Analyst construction,
  and Unknown paper context. No source assertion or results table is invented.
- **Observed pause and fast path:** One targeted application question asks
  whether a one-time spike becomes seasonal after subtraction. The controller
  then supplied the rubric's technically adequate corrective answer. The next
  response accepts it and moves on without another prerequisite lecture or
  preferred-wording test. It requests the original results table, caption, and
  paragraph, then gives one claim/evidence reading question. The missing source
  prevents an exact anchor; no table or result is invented. This demonstrates
  the local fast path, not full-paper comprehension or a passed critique gate.

## Scenario 5: Premature criticism

**Verdict: Pass for critique deferral, source request, and first comprehension
question.**

- **Comprehension gate:** The route explicitly reconstructs question/task,
  method, evidence, and scope before judging limitations. It says none of the
  paper has been inspected and cannot establish five strong flaws from the
  learner's self-report. It also says missing conversational material is not a
  paper defect.
- **Review criteria versus defects:** Five questions are introduced as
  “provisional review questions” and “my suggested checks,” which is clear
  Analyst attribution. It explicitly says none is an established flaw and that
  the final count will not be forced. They are not disguised paper-specific
  accusations, even though their number matches the requested quota.
- **Provenance:** Identity, method, and results remain unverified; no source
  anchor, inspected full paper, or learner mastery is fabricated.
- **Observed next action:** It asks for agreement plus title/PDF/link and the
  contribution passage. After agreement and notice that no additional source
  is available, it asks one task-comprehension question: what goes in and which
  future quantity comes out? The learner is to answer from the introduction
  later, with uncertainty allowed. It continues to disclose that the paper is
  uninspected. No long questionnaire, invented anchor, or simulated answer is
  used. Actual method/evidence comprehension and later criticism remain untested.
- **Fresh neighboring regression check:** The updated-skill rerun again discloses
  no inspected paper and unknown identity/method/experiments/flaws. It proposes
  question -> method -> evidence/scope before criticism and waits for agreement.
  After the neutral agreement/source-unavailable continuation, it asks only
  what forecasting problem the authors seek to solve. It offers no asserted
  defects, fabricated source, unnecessary intake, or abstract-only assignment.
  This neighboring sample remains passing; actual paper-specific criticism is
  still untested because no paper is supplied.

## Scenario 6: Reported forward smoke test

**Verdict: Pass for evidence classification, reporting, and bounded next action.**

- **Claim rejected and qualified:** It rejects “paper reproduced successfully”
  and calls the account “user-reported evidence of a forward/shape smoke test.”
  It names the reported shapes and finite outputs, explicitly denies independent
  execution verification, and leaves the paper's expected shape and semantics
  unknown. It infers neither correct architecture nor useful predictions.
- **Six states remain distinct:** The table names conceptual understanding,
  paper-to-code mapping, forward/shape validation, small-scale training, metric
  consistency, and full reproduction across reported settings. State 3 is a
  reported, unchecked synthetic case; states 1/2 are not inferred from it.
  Other levels remain unperformed or unassessed. The response expressly rejects
  an automatic ladder.
- **Report wording:** The proposed sentence records the finite-output run and
  leaves mapping, data/protocol, training, and metric agreement unvalidated;
  surrounding attribution says it is the user's observation, not the assistant's
  independently verified execution.
- **Next checks and provenance:** “My recommended next steps” labels the
  Analyst recommendations. It requests paper/version, implementation/config,
  and log; checks mapping, tensor meanings, split/preprocessing/leakage and
  protocol before bounded training. One matching setting supports only that
  setting; the remaining reported settings require a separate coverage audit.
  No training or execution is performed or claimed.

## Scenario 7: Abstract-only access

**Initial verdict: Partial pass with one demonstrated failure. Source-limited
opening, orientation, and excerpt reading pause pass; the required future
  full-text reading plan is missing. Fresh updated-skill rerun: Pass.**

- **Source restriction:** It begins “without searching” and states that only
  the supplied illustrative sentence was inspected, with no verified title,
  author, or version and no full text, figures, or experimental results. The
  inventory records no external search.
- **Process and limits:** The proposed route is confined to unpacking the task
  and comparison, rereading the excerpt, and separating reported claims from
  available support. Its target is a bounded independent explanation with
  unknowns recorded; checking the actual method/accuracy requires missing method
  and protocol/results. It invents no familiar paper identity, mechanisms,
  numbers, figures, limitations, critique, or reproduction verdict.
- **Orientation after agreement:** The continuation gives a marked hypothetical
  forecast and says it is not the excerpt's model. It attributes the linear
  model and accuracy comparison to what the supplied text reports and expressly
  separates that report from independent confirmation. It limits the claim to
  several baselines on benchmark datasets, leaving model operations, dataset,
  metrics, improvement sizes, and comparison procedure Unknown. Missing details
  are not presented as flaws.
- **Observed pause and failure evidence:** It assigns rereading only the
  supplied sentence and asks one question about the comparison's breadth, then
  pauses. No search or familiar-paper reconstruction occurs. The recorded turns
  name missing material for method/accuracy checking, but give no explicit plan
  for what to inspect when full text becomes available. The rubric requires
  that plan alongside limited orientation. Merely identifying missing sources
  does not satisfy it. This is **ABSTRACT_FUTURE_READING_PLAN_MISSING**, not a
  claim that the response invented paper evidence or violated the no-search rule.
- **Minimal correction:** The abstract-only guided route in
  `references/source-quality.md` now requires a compact future inspection plan
  for method, data/comparison protocol, original figures/tables/results, and
  limitations before the current reading/answer pause. It preserves no-search
  limits, avoids invented section numbers, and retains one current excerpt
  question. Other modes are unchanged.
- **Fresh rerun evidence:** The updated-skill opening again identifies only the
  supplied sentence as inspected, leaves identity/version unverified, promises
  no search, and obtains route agreement before orientation. The continuation
  labels Background toy input/output, the excerpt's reported claim, Analyst
  interpretation, and Unknown method/datasets/metrics/protocol. Its Analyst
  interpretation is provisional, not promoted to the excerpt's explicit result.
  It rejects general linear-model superiority and treats missing details as
  unresolved questions rather than errors.
- **Corrected criterion and pause:** Before the single current excerpt question,
  the rerun explicitly lists future reading targets: method; data, splits, and
  comparison protocol; original result tables/figures; and stated limitations.
  It explains their purpose and says section numbers/material cannot be assessed
  today. This is the missing future reading plan. It then assigns only the
  supplied sentence and asks one scope/evidence question. There is no browsing,
  invented paper identity/anchor/result, critique verdict, reproduction claim,
  or simulated learner mastery. The corrected criterion passes in this sample.

## Comparison with the no-skill controls

| Scenario | Recorded baseline | Observed with-skill change and remaining boundary |
| --- | --- | --- |
| 1 | Partial pass: small steps and no summary dump already occurred; explicit route agreement, learner-owned original reading, target, and precise inspected coverage were incomplete. | The opening now names roles/target and exact inspected coverage and actually waits for agreement. The continuation assigns a bounded original paragraph with a reason, defer choice, one question, and reading pause. Learner completion is not inferred. Neither run supports claiming the baseline dumped a full summary. |
| 3 | Substantive pass: authoritative links, mechanism/example, limits, attribution, and return-to-paper pointers were already observed. | The with-skill response retains these behaviors with explicit voice labels and bounded version/inspection disclosure. This is regression evidence, not evidence that only the new skill can teach sourced prerequisites. Neither record establishes learner understanding or general improvement frequency. |
| 6 | Reproduction inflation was already rejected. Six-level coverage, user-reported attribution, unverified expected shape, and missing-source request were incomplete. | The with-skill response explicitly separates all six states, conditional reported state-3 evidence, unknown expected shape, source request, and one-setting/full-coverage boundary. It does not independently verify the run or reproduce a paper. The baseline did not approve full reproduction. |

## Overall result and limits

All seven scenarios pass the criteria exercised by the recorded turns after one
narrow correction and fresh rerun. The initial scenario-7 omission remains an
observed failure in this history; it is not erased by the later pass. The fresh
scenario-7 sample supplies the missing future full-text reading plan and retains
source limits and one-question pacing. The fresh neighboring scenario-5 sample
retains critique deferral and the concrete comprehension step. No further
production changes are justified by these records.

This is a small set of sampled behaviors, not a success-rate estimate or a causal
learning study. Neither static validation nor these sampled responses guarantees
every future model response. No completed full-paper learning session, retained
learner mastery, installed discovery, cross-client compatibility, training,
metric consistency, or full reproduction is established by this assessment.

## Historical deterministic verification after the fresh reruns

The following evidence was recorded on 2026-11-26 from the **former fork root**,
before this skill became a standalone repository. The nested path and absolute
validator path are preserved as historical commands; use the current root-level
commands in [README.md](../README.md) for new checks.

| Command | Observed result |
| --- | --- |
| `python3 learner-first-paper-reading/tests/validate_contract.py` | Exit 0; all 36 tests `ok`; final output `Ran 36 tests in 0.044s` and `OK`. |
| `python3 /Users/panjingyu/.codex/skills/.system/skill-creator/scripts/quick_validate.py learner-first-paper-reading` | Exit 0; `Skill is valid!` |
| `git diff --check` | Exit 0; no output. |

These historical checks passed for the instruction files at that stage. The
independently recorded scenario-7 correction rerun and neighboring scenario-5
regression check supply the sampled behavior evidence separately.
