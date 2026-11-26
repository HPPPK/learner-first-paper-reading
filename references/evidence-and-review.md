# Evidence and Review

Use this reference to connect what the paper says to what its evidence supports.
Establish source identity and inspected coverage with [Source quality](source-quality.md).
An author's report, a reader's inference, and an independently checked result
have different evidential roles, even when their wording sounds similar.

## Keep four voices visible

Use labels or equally clear attribution. Split a sentence when its source changes.

- **Paper:** Attribute explicit statements and reported results to an inspected
  source anchor in the focal paper's identified version. Say whether the authors
  propose, derive, observe, or interpret something; reporting is not independent
  verification.
- **Background:** Attribute external definitions or mechanisms to an authoritative
  source and link the supporting passage when it materially helps. This knowledge
  explains the paper; it cannot supply the paper's missing experimental evidence.
- **Analyst:** Mark an inference, interpretation, toy construction, criticism, or
  recommendation as your own. Name its premises separately from the conclusion.
- **Unknown:** State what the available evidence does not establish, why it is
  unresolved, and what source or measurement could settle it. Missing reporting
  does not prove the authors performed an incorrect procedure.

For example, a paper may report a lower error in one table (**Paper**). A textbook
can explain the error measure (**Background**). The suggestion that a design
choice caused the improvement is **Analyst** unless a controlled comparison
supports it; that causal explanation may remain **Unknown**.

## Build a claim-evidence-boundary card

For each load-bearing claim, record the claim and source anchor; offered evidence
(experiment, derivation, figure, or table); direct observation; support strength;
conditions; alternative explanations; and unknowns. Connect each observation to
the specific claim it supports, rather than collecting disconnected citations.

| Card field | What to record |
| --- | --- |
| Claim | Exact scope and inspected section/page/equation anchor; preserve the difference between an author's wording and your paraphrase. |
| Evidence | The actual comparison, derivation, or measurement offered, its source location, and inspected coverage. |
| Direct observation | Values, ordering, or derivation steps that can be checked; distinguish these from the authors' interpretation. |
| Support strength | Explain whether the evidence directly supports, partially supports, conflicts with, or leaves the claim untested, and why. |
| Boundary | Data, population, assumptions, protocol, uncertainty, and alternative explanations limiting the inference. |
| Unknowns | Missing detail or untested extension, plus the source or experiment needed to resolve it. |

If a table supports better average error under one protocol, retain that scope.
It need not establish a mechanism, robustness on another population, or superiority
on every case. A valid derivation supports its conclusion under its assumptions;
it need not establish that an empirical dataset satisfies them.

## Check the unit and comparison

Identify the unit of analysis, the independent sampling unit, repeated or grouped
observations, and how uncertainty is calculated. Ask whether windows, images,
patients, tasks, or seeds are independent evidence for the stated conclusion.
Repeated observations from one source can share information. Check whether the
split and uncertainty calculation respect that grouping; do not silently count
every measurement as an independent replicate. Distinguish per-example metrics,
dataset aggregates, and averages across runs.

Compare baselines under the same task, split, preprocessing, metric definition,
tuning budget, and compute conditions, or record each difference and its possible
effect. Inspect data versions, train/validation/test separation, leakage risks,
input/output settings, optimization, stopping and selection rules, and resource
budgets. A different budget is a comparison condition to assess, not automatically
a disqualifying flaw. Ask what question the comparison can fairly answer.

## Gate paper-specific reviewer criticism

In guided mode, enter reviewer-style critique only after the learner can accurately
reconstruct the research question, method, decisive evidence, and valid scope.
Use their actual teach-back, one consequential question at a time; one correct
definition cannot establish the whole gate. Accept technically adequate wording.

If comprehension is incomplete, defer paper-specific reviewer criticism and ask
one targeted comprehension question about the missing connection. Obtain the
relevant source if needed, teach the demonstrated gap, and return to that source.
A request for five strong flaws does not waive the check while guided learning
continues. General review questions can be offered as **Analyst** future checks;
they are not established defects of this paper.

For an explicit non-interactive critical report, first supply a source-grounded
reconstruction yourself and then assess it. Do not claim that the learner passed
a gate or impose a simulated learner exchange. Apply source limits in either mode.

## Review only what the evidence warrants

Tie every criticism to inspected source evidence or an explicit missing detail.
For each concern, name the anchor, observation or omission, inference, consequence
for the claim, and evidence that would resolve it. Separate a demonstrated flaw,
a plausible alternative explanation, and a question left open by reporting.
Do not invent flaws to fill a quota. If no strong flaw is established, say so and
retain the unanswered checks without turning them into verdicts.

After comprehension, inspect relevant baselines, splits, metrics, statistical
units, uncertainty and seeds, ablations, compute, leakage, distribution shift,
mechanism claims, generalizability, and reproducibility gaps. Select checks by the
paper's claims and design; the list is not a required count of criticisms.

Preserve the learner's original interpretation and unresolved questions in the
optional [reading note](../assets/reading-note-template.md). Use
[Figures and equations](figures-and-equations.md) for visual and mathematical
evidence, and [Reproduction levels](reproduction-levels.md) for execution claims.
