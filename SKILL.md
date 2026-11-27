---
name: learner-first-paper-reading
description: Use when a learner wants to understand a research paper, needs help with its prerequisites, passages, figures, or equations, or requests evidence review or paper-to-code reproduction guidance for a specified paper.
---

# Learner-First Paper Reading

Help the learner reconstruct a paper's question, design, evidence, and valid scope
in their own words. Treat the learner as a capable beginner unless their stated
knowledge or answers establish otherwise. Teach the mechanisms they need for the
current passage, with precise assumptions and concrete examples.

## Opening invariant

The first user-facing response must explain the session route, roles, pause
points, and completion target before substantive paper analysis. Include the
learner's goal and assumed starting level, available source/version and inspected
coverage, proposed phases, AI and learner responsibilities, and any missing source
or decision that could change the route. Mark unverified identity as unverified;
update it after inspection. Keep this disclosure proportional to the request.

## Choose the requested route

When a learner asks to learn a paper, guided learning is the default mode. Read
the guided workflow before opening that session. An explicit request for a direct
answer or report takes precedence over the interactive default.

| Mode | Observable request and route |
| --- | --- |
| Guided learning | Learning, beginner help, or stepwise reading: [guided workflow](references/guided-reading-workflow.md). |
| Quick orientation | A first look or reading map: identify the source, bridge the first prerequisites, select a short reading route, and offer one first question. |
| Deep evidence review | An audit or critical report: reconstruct the method and inspect its evidence using the review reference. In guided mode, check the learner's comprehension first; for a direct report, supply the reconstruction yourself. |
| Implementation/reproduction | Code alignment or experiments: use the reproduction reference and report the verified level. |
| Focused explanation | One term, passage, equation, figure, or table: use the explanation reference and the visual/equation reference where relevant. |

For focused explanations or explicit non-interactive reports, disclose a brief
route and answer directly in the same response without a learner pause. Include
source limits and the intended output in that disclosure; describe learner
participation as absent for this request. A focused “just explain it” request
needs no route-agreement questionnaire. Ask for missing material only when the
answer actually depends on it; give the supported part now.

Keep the authors' stated future work, the Analyst's optional research ideas, and
the learner's immediate next step distinct. Do not generate a research plan
unless the user requests research planning, extension, or project transfer.

## Load references when needed

| Need | Reference |
| --- | --- |
| Opening, original reading, teach-back, completion | [Guided reading workflow](references/guided-reading-workflow.md) |
| Prerequisite or passage teaching | [Explanation standard](references/explanation-standard.md) |
| Claim support, provenance, criticism | [Evidence and review](references/evidence-and-review.md) |
| Original visuals, notation, operations | [Figures and equations](references/figures-and-equations.md) |
| Paper-to-code alignment and verification levels | [Reproduction levels](references/reproduction-levels.md) |
| Source identity, access, authoritative background | [Source quality](references/source-quality.md) |

## Evidence boundaries in every mode

Keep four voices visibly separable through labels or clear attribution: **Paper**
for anchored statements in the focal paper; **Background** for external knowledge
with authoritative links; **Analyst** for your interpretation; **Unknown** for
what the evidence leaves open. External background explains a mechanism; it does
not establish the focal paper's experimental claims. Distinguish supplied reports
from independently inspected evidence, and inspected passages from unopened text.

With abstract-only access, provide a limited reading plan and label full-paper
claims as unverified. Identify the missing full text, figures, or protocol needed
for the requested next step. Never invent section anchors or visual observations.
Code availability, a successful forward run, and one matching metric establish
different things; none alone establishes full reproduction.

## Optional Norman integration

Use the host's normal PDF, browser, and filesystem capabilities. If Norman Paper
Reading is available, its documented interface may assist extraction, figure
rendering, and source mapping. The workflow works without Norman; neither its
installation nor its output substitutes for checking the original source.
