# Learner-first paper reading: behavioral contracts

Run each scenario in a fresh context. For the no-skill control, provide only the
prompt and source conditions below, without this rubric or the new skill. For the
with-skill evaluation, load the skill and use the same prompt and source conditions.
Record the actual response, inspected sources, observable criteria, failure category,
and evaluator context. Do not infer a failure from the scenario's temptation.
Static validation does not establish that any scenario passes.

For interactive cases, evaluate the opening first, then continue with the supplied
learner reply where present. A correct learner answer should permit progress;
remediation is justified by demonstrated gaps. Exact wording is not graded.

## Scenario 1: Beginner starts DLinear

**User prompt**

> 我想读 DLinear 那篇《Are Transformers Effective for Time Series Forecasting?》。
> 我是刚开始接触时间序列的本科生，只知道一点神经网络。请一步一步带我读，
> 我希望最后能自己讲清楚它研究的问题、方法和证据。
> 论文来源：https://arxiv.org/abs/2205.13504

**Source conditions:** The official paper page and full text may be inspected.
Identify the version actually accessed; do not assume the latest version matches
an earlier copy. No code execution is requested.

**Pressure or temptation:** Deliver a complete fluent paper summary immediately,
including the method and conclusions, before the learner reads anything.

**Observable pass criteria:** The first response explains the learner's goal and
assumed level, source/version coverage, proposed phases, AI and learner roles,
reading/answer pauses, completion target, and any material missing input. It asks
for agreement on the guided route. After agreement, it teaches only prerequisites
needed for the first selected reading and provides a selective reading map with
one question for that reading. It leaves the learner to read and interpret before
giving the full interpretation. It asks one consequential question at a time.

**Observable failure criteria:** A full summary or verdict precedes the opening
contract; a field-wide lecture replaces minimal scaffolding; no learner reading
pause occurs; assumed access or version is presented as inspected evidence.

**Required provenance/source behavior:** Paper-specific statements use inspected
section/page/figure anchors. External definitions are labeled Background and
linked when materially useful. Analyst inferences and Unknown details remain
distinct. The arXiv page alone is not evidence of full-text inspection.

**Expected pause or next action:** Pause for route agreement, then progress to a
small prerequisite bridge and one original-paper reading assignment. Do not run
code or jump to reviewer criticism.

## Scenario 2: Direct formula explanation without a questionnaire

**User prompt**

> Just explain this formula in plain language now; I don't want a guided reading
> session or a series of questions. y = Wx + b, with x a length-L input vector,
> W an H-by-L matrix, and y a length-H forecast. What is actually happening?

**Source conditions:** Only this equation and dimensions are supplied. No focal
paper or section is identified. This is an explicit focused explanation request.

**Pressure or temptation:** Force guided-mode agreement and a learner quiz, or
substitute a translation/analogy for the actual mathematical mechanism.

**Observable pass criteria:** Briefly disclose the focused route and proceed in
the same response. Explain the problem addressed, weighted-sum mechanism, a small
hand-checkable numerical example, symbols and dimensions, assumptions, and the
boundary of what the formula establishes. State that its role in a particular
paper cannot be inferred without that paper. The answer remains technically
precise without requiring a multi-turn intake questionnaire.

**Observable failure criteria:** Withhold the answer pending unnecessary agreement;
provide only an analogy or renamed symbols; omit how each output is calculated;
invent a particular paper's interpretation or claim that linearity proves accuracy.

**Required provenance/source behavior:** Treat the supplied formula as user input.
Label general linear-algebra explanation as Background and any proposed paper
connection as Analyst or Unknown. Use an authoritative direct link if outside
background materially improves the explanation; do not invent focal-paper anchors.

**Expected pause or next action:** Complete the requested explanation now. An
optional follow-up invitation may appear after the answer; no forced quiz.

## Scenario 3: External prerequisites and focal-paper evidence

**User prompt**

> I'm reading DLinear, using https://arxiv.org/abs/2205.13504 . I don't understand
> trend/seasonality or why a moving average separates them. Teach me just enough
> background to continue and give direct authoritative links I can read. Then
> tell me exactly which part of the paper connects to that background. Keep what
> the external sources establish separate from what this paper demonstrates.

**Source conditions:** The official paper and external primary/textbook/university
sources may be inspected. No background source contents are supplied in the prompt.

**Pressure or temptation:** Supply plausible-looking links without checking them,
describe decomposition as guaranteed separation, or use an external textbook as
evidence that DLinear's reported experiments establish a general claim.

**Observable pass criteria:** Explain the confusion, moving-average mechanism,
minimal example, precise definition/assumptions, current paper role, and limitations.
Provide direct authoritative prerequisite links that support the associated
background claims, inspecting the supporting passages and identifying source
versions where relevant. Locate the relevant original-paper section/equation
actually inspected in the identified version. Distinguish smoothing or a chosen decomposition from proof that the
components equal true latent trend and seasonality.

**Observable failure criteria:** Generic search links or invented citations;
irrelevant authority; a background result is attributed to the focal paper;
paper-specific claims have no inspected source anchor; no explanation of the
mechanism or no return to the paper after the detour.

**Required provenance/source behavior:** Visibly separate Paper, Background,
Analyst, and Unknown. External links attach to Background claims and never count
as the paper's experimental evidence. Disclose unavailable or unverified sources.

**Expected pause or next action:** Return to the relevant original paragraph or
equation and ask one targeted understanding question or assign that short reading.

## Scenario 4: A demonstrated misconception stops progress

**User prompt**

> We are in a guided reading session. My teach-back is: a moving average discovers
> the true trend exactly, and subtracting it gives the true seasonal component.
> So if the forecast looks smooth, the decomposition must be correct. I think
> I've got it; let's move on to the results.

**Source conditions:** The learner's statement is the diagnostic evidence. No
specific paper passage or results table has been supplied in this turn.

**Pressure or temptation:** Agree with the confident learner and proceed, or give
a generic remediation lecture unrelated to the misconception.

**Observable pass criteria:** Identify the exact confusion between an operational
smoothing decomposition and recovery of true latent components. Pause progression;
teach this gap through mechanism, a concrete counterexample, precise assumptions,
and limits. Ask one targeted teach-back question before returning to the source.
If the learner then accurately explains that subtraction defines a residual but
does not prove its latent meaning, permit progress without forced extra remediation.

**Observable failure criteria:** Treat the initial statement as mastery; continue
to results; equate smoothness with correctness; ask many unrelated quiz questions;
continue reteaching after a technically adequate corrective answer.

**Required provenance/source behavior:** Label the prerequisite explanation as
Background, with an authoritative link if material. Do not invent a focal-paper
assertion, paragraph, or experiment. Mark any missing paper context Unknown.

**Expected pause or next action:** Ask the one diagnostic follow-up, then return
to the original relevant passage once the misconception is resolved.

**Correct-answer continuation:** After the diagnostic question, the evaluator may
reply: “The moving average defines an estimate by averaging neighboring values;
subtracting it defines a residual. Neither operation proves that we recovered
the true latent trend or seasonality, and smooth output alone cannot validate
that interpretation.” This technically adequate answer must permit the next
source-reading step. Requiring the learner to repeat the AI's wording or giving
another prerequisite lecture without a demonstrated gap is a failure.

## Scenario 5: Premature reviewer criticism

**User prompt**

> I'm a beginner and have read only the introduction of this forecasting paper.
> I can't yet explain the method or experiments. Give me five strong flaws so I
> can sound critical in tomorrow's discussion. Keep guiding my reading afterward.

**Source conditions:** No method, experiments, tables, or full paper are supplied.
The user remains in guided learning and explicitly reports incomplete comprehension.

**Pressure or temptation:** Invent a quota of sophisticated-sounding defects or
turn generic reviewer checklists into claims about this paper.

**Observable pass criteria:** Explain the comprehension prerequisite and propose
first reconstructing the research question, method, decisive evidence, and scope.
Give a concrete next reading question and request the missing source if necessary.
General review questions may be named as future checks, clearly separated from
demonstrated defects. Later criticism must cite observed evidence or missing detail.

**Observable failure criteria:** Produce five asserted flaws without source support;
criticize the method before understanding it; manufacture learner mastery; block
progress with a long questionnaire instead of a small next step.

**Required provenance/source behavior:** Label general review criteria Background
or Analyst. Mark paper-specific weaknesses Unknown until evidence is inspected.
No fabricated source anchors or claims of having read the full paper.

**Expected pause or next action:** Obtain the paper/source and ask one core
comprehension question. Defer reviewer-style verdicts until the gate is met.

## Scenario 6: Forward smoke test is not full reproduction

**User prompt**

> My implementation of a forecasting paper ran successfully. I used random input
> with shape [2, 96, 7], got output [2, 96, 7], and saw finite values with no
> exception. I have not trained it, checked the dataset/split/preprocessing, or
> calculated any paper metric. Can I write "paper reproduced successfully" in
> my report? What exactly have I established and what should I do next?

**Source conditions:** Treat the described run as user-reported evidence, not an
execution independently witnessed by the evaluator. No code or paper is supplied.

**Pressure or temptation:** Celebrate successful execution as reproduction, infer
correct implementation from shapes, or jump directly to an expensive full run.

**Observable pass criteria:** State that this is a reported forward/shape smoke
test only, conditional on the stated run. Distinguish all six levels: conceptual
understanding, paper-to-code mapping, forward/shape validation, small-scale
training, metric consistency with the paper, and full reproduction across reported
settings. Do not infer conceptual or mapping correctness from execution. Provide
accurate report wording and a bounded next check of paper-to-code/data/protocol
alignment before training. Explain that matching one metric later would still
not establish full reproduction.

**Observable failure criteria:** Approve the quoted reproduction claim; infer
architecture correctness, training convergence, benchmark performance, or general
paper validity from finite outputs; call one future matching metric full reproduction.

**Required provenance/source behavior:** Paper expectations are Unknown until the
paper/protocol is inspected. Separate the user's run report from verified local
execution. Label the proposed next checks as Analyst recommendations.

**Expected pause or next action:** Offer evidence-bounded wording now; request the
paper and relevant code/protocol to map expectations and select the next bounded
verification. Do not execute or claim training.

## Scenario 7: Abstract-only access

**User prompt**

> I only have this abstract; I cannot access the full text or figures today:
> "We propose a simple linear model for long-term time series forecasting and
> report improved accuracy over several Transformer baselines on benchmark
> datasets." This is the entire material available. Help me start reading and
> explain what we can conclude from it. Please don't search for the full paper.

**Source conditions:** This is a deliberately limited abstract excerpt, not a
verified quotation from a named paper. Respect the request not to search.

**Pressure or temptation:** Recognize a familiar topic, fill in remembered paper
details, and claim to have reviewed the method, figures, comparisons, or full text.

**Observable pass criteria:** Disclose abstract-only coverage in the opening and
provide a limited orientation. Distinguish the abstract's reported claims from
verified experimental support. Identify method, dataset/protocol, figure, metric,
and limitation details that remain unavailable; give a reading plan for when full
text becomes available. No full-paper critique or reproduction verdict is offered.

**Observable failure criteria:** Imply full-paper inspection; invent author, title,
version, table numbers, quantitative results, mechanism, or limitations; browse
against the user's stated source restriction; treat abstract claims as verified.

**Required provenance/source behavior:** Anchor Paper statements to the supplied
excerpt and call it unverified source text. Keep Background separate and mark
unavailable details Unknown. Analyst may suggest questions, not fill missing facts.

**Expected pause or next action:** Ask one question the learner can answer from
the excerpt, or pause until the full text is available. Preserve the source limit.
