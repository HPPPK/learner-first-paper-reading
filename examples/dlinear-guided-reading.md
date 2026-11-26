# Guided DLinear reading

## Evidence status

This is a curated **demonstration**, adapted from the validated DLinear scenario;
it is not a verbatim live transcript and does not establish a learning outcome.
The focal source is the official arXiv record for
[Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/abs/2205.13504).
In an actual session, the agent must identify and inspect the version it uses
before asserting a paper-specific section, figure, or result.

## Learner request

> I am new to time-series forecasting and know only basic neural networks. Help
> me read DLinear step by step so I can explain its question, method, evidence,
> and valid scope myself.

## Turn 1 — disclose the route before teaching

> Your target is an independent explanation of the paper's research question,
> key operation, evidence, and scope. I will treat you as a capable beginner.
> The supplied source is the official arXiv record; before assigning exact text,
> I will confirm the version and record what I actually inspect.
>
> I propose five phases: verify the source; bridge only the input-window and
> forecast-horizon concepts needed for the first passage; give you one short
> original-paper reading; check your teach-back; then connect claims to evidence
> before any reviewer-style critique. I will explain blocking concepts, locate
> sources, and check reasoning. You will read each selected item and explain it
> in your own words. I will pause now for route agreement, again while you read,
> and after one consequential question at a time.
>
> We finish when you can reconstruct the question, method, decisive evidence,
> limits, and unresolved points without copying my wording. The paper version is
> the only material detail not yet confirmed. **Does this route fit your goal?**

That final question is the **route agreement** gate. The assistant does not give
away the full paper interpretation in the opening.

## Turn 2 — after agreement, bridge one prerequisite

Assume the source check identified arXiv version 3 and the learner agreed.

> **Background — mechanism.** A forecasting example takes a fixed block of past
> observations as its input window and asks the model to output a fixed block of
> future observations. If the look-back length is (L=4) and the horizon is
> (H=2), one training pair might be past values `[10, 12, 11, 13]` and future
> targets `[14, 13]`. The model sees four positions and produces two predictions.
> This notation defines the task shape; it does not say which model will predict
> well or whether the data split is valid.
>
> **Paper — read now.** Open the identified v3 full text and read the task-
> definition passage in Section 2 where the input look-back window and future
> forecasting horizon are defined. Do not read the results tables yet.
>
> **Reading assignment.** In your own words, what information is available to
> the model at prediction time, and what exact block must it produce? Give a tiny
> example with your own (L) and (H), then pause.

The assistant has returned the learner to an original-paper reading assignment
and left the interpretation unfinished for the learner.

## Voice ledger

| Voice | What it means in this demonstration |
| --- | --- |
| **Paper** | Source identity and the selected task-definition anchor, conditional on inspecting the stated version. No experimental result is asserted here. |
| **Background** | The generic input-window/horizon explanation and toy numbers. They are teaching material, not paper evidence. |
| **Analyst** | The proposed order—task definition before method and results—and the single diagnostic question. |
| **Unknown** | Whether the learner understands the passage, what the decisive experiment is, and what the results support. Those remain open until later reading. |

## What this example does not prove

It does not show a completed paper reading, mastery, automatic route compliance,
or DLinear's empirical validity. Those require later learner responses and
inspection of the relevant method, figures, tables, protocol, and limitations.
