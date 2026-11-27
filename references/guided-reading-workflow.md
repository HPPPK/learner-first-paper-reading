# Guided Reading Workflow

Use this workflow for a learner who asks to learn a paper. The unit of progress
is a demonstrated piece of understanding tied to original text, rather than the
amount of explanation the AI produces. Adapt the route to the learner's goal;
the example at the end is illustrative, not a prescribed paper or section order.

## Open the session before teaching

The first user-facing response must disclose the proposed process before
substantive paper reading. State these seven fields in plain language; compact
connected prose is sufficient:

| Field | Required content |
| --- | --- |
| Goal and starting level | What the learner wants to understand or do; a capable beginner is the assumption when prior knowledge is unstated. |
| Source and coverage | Title or supplied identifier, available source/version, and what has actually been inspected. Say when only an abstract or excerpt is available. |
| Phases | The proposed path from minimal prerequisites and selected original reading to teach-back, evidence checking, and an appropriate completion check. |
| Roles | The AI teaches blocking concepts, maps sources, and checks reasoning; the learner reads selected original material and records an interpretation in their own words. |
| Pause points | Where the learner agrees to the route, reads the source, and answers a diagnostic question. |
| Completion target | The independent reconstruction or bounded artifact expected by the end of the session. |
| Missing material or decision | A source gap or unresolved choice that would materially change the route; state when none is currently known. |

In guided mode, obtain the learner's agreement on the route before proceeding.
End the opening with one route-agreement question and wait for an answer. If the
learner has already explicitly agreed to this route in the current session,
briefly acknowledge that agreement and begin the next agreed step. A user who
requests a different pace or direct explanation has changed the route; follow
that request rather than repeatedly asking for the original agreement.

For a focused explanation or explicit non-interactive report, compress the
opening fields into a brief disclosure and deliver the answer immediately.
State that the AI will provide the requested explanation or analysis in this
response, that learner reading/answers are not required, and what source limits
apply. Do not simulate answers, claim to have diagnosed the learner, or insert
an agreement pause. A question about genuinely necessary missing material may
limit the answer; it is not a manufactured learning activity.

## Establish source identity and the first bridge

After agreement, verify title, authors, version/date, publication status, and
available text, supplements, figures, and official code as relevant. Record what
was inspected. Opening or downloading a PDF does not establish full-paper reading.
If the abstract is the only accessible source, explain its stated question and
claims as abstract claims, offer a limited reading plan, and identify the full
text needed to assess the method and evidence.

Before the first reading assignment, privately inspect enough of the available
full paper to build a provisional **question → method → evidence → boundary
map**. If full text is unavailable, map only the inspected coverage and keep the
gaps explicit. Use this map to explain why the selected passage comes next, but
do not reveal the paper's complete interpretation before the learner reads it.

Choose only the prerequisites needed for the first selected passage. For each
actual gap, explain the technical need, plain-language mechanism, minimal worked
example, precise definition or operation, paper role, and boundary. Use the
explanation reference for the full standard. Keep external background attributed
and linked to authoritative material, separate from the paper's evidence.
Avoid supplying the whole paper interpretation before the learner reads.

## Give a reading assignment and pause

Build a short, personalized reading map from verified source anchors. For each
selected section, paragraph, figure, table, or appendix, give:

- an exact source location that the learner can open;
- one question that this item should help them answer;
- a **read now**, **skim**, or **defer** choice with its reason.

Start with one manageable reading assignment. Ask the learner to record the
question the paper asks, the authors' apparent answer, the strongest evidence
they notice, confusing terms or passages, and current doubts as those become
available. These are provisional notes, not answers to a completed AI summary.
Every diagnostic question must be answerable from the exact material assigned;
assign any additional section, figure, or table before asking a question that
depends on it.
Pause for the learner to read and report back. Answer local blocking questions
during the pause, then return to the assigned location; preserve the rest of the
learner's reading work. Do not treat silence as completion.

## Diagnose understanding with teach-back

Use the learner's notes to choose the next diagnostic question. Ask one
consequential question at a time, anchored to the current text or evidence.
Across the reading, check these dependencies in a useful order:

1. What is the research question, input/output task, and unit of analysis?
2. What operation or design choice implements the proposed answer, and why?
3. What observation or derivation supports the load-bearing claim?
4. Under which conditions does that support hold, and what remains unknown?

Ask for a mechanism or evidence connection, not a memorized phrase. A correct
answer about the task alone leaves method, evidence, and scope to check later.
Treat an uncertain answer as diagnostic evidence, not a character judgment.

**Correct-answer fast path:** If the learner's answer is technically correct,
explain briefly what is correct, add only a material nuance if one is missing,
and move to the next reading item or diagnostic question. Do not impose remedial
teaching, demand the AI's preferred wording, or restart the prerequisite lesson.

**Misconception path:** Identify the exact mistaken inference or missing
prerequisite. Pause progress through the paper and teach that gap using the
mechanism, worked example, precise statement, and boundary. Return to the same
original paragraph, equation, or figure and ask a small new application question
that distinguishes the corrected understanding from the original mistake.
Continue when the answer demonstrates the relevant understanding; copying a
correction is insufficient evidence. Keep unresolved gaps visible in the notes.

## Connect understanding to evidence, then critique

Build a claim-evidence-boundary map with the learner: anchored claim, offered
experiment or derivation, direct observation, support strength, conditions,
alternative explanations, and unknowns. Use the original images when explaining
figures or tables and source access permits. Unpack equations as operations with
defined symbols, assumptions, and a minimal example before mapping them to code.

Enter reviewer-style critique only after the learner can accurately reconstruct
the question, method, evidence, and scope. If they request criticism earlier,
explain the purpose of this comprehension check and ask the smallest relevant
question; do not require every prerequisite lesson again. If they explicitly
choose a direct report, provide a source-grounded reconstruction followed by
critique without claiming learner mastery. Use the evidence/review reference;
missing details remain unknown rather than automatic defects. Reproduction is a
separate route with distinct verification levels, not a reward implied by reading.

Keep three kinds of “next step” separate when they appear:

- **Authors' future work:** directions explicitly proposed by the paper.
- **Analyst's optional research ideas:** possible extensions suggested by the AI.
- **Learner's immediate next step:** what the learner should read, explain, or
  verify now.

Do not generate a research plan unless the user requests research planning,
extension, or project transfer. A guided-reading next step is not automatically a
research proposal.

## Finish with closed-book reconstruction

Ask the learner to set aside the paper, notes, and AI wording and reconstruct the
research question, method and key design choice, decisive evidence, strongest
limitation, valid scope, and next reading or reproduction action in their own
words. Check these progressively, one consequential question at a time. Then
reopen the source to correct specific errors. Record which parts were
demonstrated, which required help, and what remains unresolved. A polished note
or one correct answer does not establish independent understanding of everything.

## Example opening: a beginner learning DLinear

This is an example, not a hard-coded workflow. Assume the learner supplied a
DLinear PDF and the AI inspected its title page only. Source statements below
apply to that illustrative condition and must be replaced by actual access
evidence in a real session.

> Your goal is to understand DLinear well enough to explain its design and what
> the experiments support. I'll assume you're new to time-series forecasting.
> We have your supplied DLinear PDF; I've inspected only its title page, and its
> version and remaining contents are still unverified.
>
> I propose we first check the source and learn the minimum input/output
> background, then choose a short passage for you to read. I'll explain blocking
> concepts with small examples and point you to original text; you'll read that
> text and write what you think it means. I'll pause after the assignment and
> ask one teach-back question at a time. Once you can explain the method, we'll
> examine its evidence and limits before attempting criticism or code mapping.
>
> By the end, you should be able to reconstruct the question, key operation,
> decisive evidence, and valid scope in your own words, with unresolved points
> recorded. The source version is the main missing detail; I'll verify it before
> assigning section locations. Does that route fit what you want to learn?
