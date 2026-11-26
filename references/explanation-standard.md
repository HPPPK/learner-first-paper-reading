# Explanation Standard

Use this reference for a blocking prerequisite, difficult passage, or focused
explanation. Assume a capable beginner: the learner can reason carefully but may
not know the subfield's vocabulary. Explain the actual operation and preserve
the technical conditions. Match the language and pace to the learner's request.

## Choose the smallest useful bridge

Teach only the prerequisites needed for the next selected reading. Identify the
specific paragraph, equation, figure, or table they unlock and the question the
learner should be able to answer afterward. In a focused explanation, the supplied
item is the next reading; answer it directly under the entrypoint's brief route
disclosure. Avoid a field-wide prerequisite course or the paper's complete answer.

Use the learner's stated knowledge and demonstrated reasoning to select the gap.
If the learner is technically correct, acknowledge the useful reasoning and move
to the next reading or question. A different choice of words is not a misconception.
If a gap is demonstrated, name the exact mistaken inference and teach that gap.

## Build the explanation in this order

Keep all applicable layers visible through connected prose or short labels;
seven mechanical headings are unnecessary. For an unavailable paper connection,
state the missing evidence instead of inventing a role.

1. **Problem:** State the confusion or technical need this concept addresses. Explain why the operation is needed before naming it.
2. **Plain-language mechanism:** Describe what enters, what changes step by step, and what comes out. Explain causal or computational relationships instead of replacing technical words with synonyms.
3. **Minimal worked example:** Give a hand-checkable numerical example, small diagram, or toy pipeline. Show intermediate operations and the resulting value or change; mark your construction as illustrative.
4. **Precise definition:** Define symbols, dimensions, units, and the formal operation or equation. State the conditions under which the plain explanation is accurate and reconcile it with the example.
5. **Paper role:** Connect the concept to an inspected focal-paper anchor and the specific design choice or reasoning it helps explain. Mark the role Unknown if the paper is absent or the relevant passage is uninspected.
6. **Boundary:** State assumptions, approximation error, failure cases, and what the example does not establish. Separate a mathematical identity, a modeling choice, and an empirical claim.
7. **Further reading:** When external background materially improves understanding, provide a direct authoritative link that supports the background claim. Give the relevant chapter or section and why it helps, using the source-quality reference.

Translation-only output is incomplete: translating a sentence or renaming symbols
does not show the operation. Childish analogies alone are insufficient: an analogy
may orient the learner, but completion requires the mechanism, a concrete example,
precise meaning, and limits. Keep technical terms when they identify useful
distinctions, and explain them where they first matter.

## A compact worked construction

For the supplied equation `y = Wx + b`, suppose the learner needs to understand
how two input values produce two outputs. Label this explanation **Background**
and the numbers an **Analyst** toy construction, rather than a paper result.

The need is to combine input values into each output with learned weights.
Each row of `W` specifies one weighted sum; its corresponding entry of `b` adds
an offset. Take `x = [2, 4]`, `W = [[1, 0.5], [-1, 2]]`, and `b = [1, 0]`.
Then `y[1] = 1*2 + 0.5*4 + 1 = 5` and
`y[2] = -1*2 + 2*4 + 0 = 6`. The learner can check every multiplication and sum.

Precisely, for column vectors `x` of length `L` and `y` of length `H`, `W` has
shape `H` by `L`, `b` has length `H`, and
`y[i] = sum over j=1..L of W[i,j]*x[j] + b[i]`. With fixed `W` and `b`, this is
an affine map; it is linear when `b = 0`. It explains how the outputs are
calculated. It does not establish how weights were learned, forecasting accuracy,
or the operation's role in an unspecified paper. State that paper role **Unknown**.
This supplied equation can be explained fully here; omit links that add no value.

## Return to the original reading

After the background detour, return to the original passage, equation, figure,
or table. In guided mode, ask one small application question that distinguishes
the corrected mechanism from the original misconception, then continue when the
answer demonstrates the relevant understanding. Preserve unresolved gaps in the
learner's notes. For a direct explanation request, complete the explanation and
give the source connection now; do not impose a quiz or claim learner mastery.

Use [Source quality](source-quality.md) for source inspection and attribution.
Label external knowledge **Background** and your inference **Analyst**; an external
definition never establishes the focal paper's reported experimental outcome.
