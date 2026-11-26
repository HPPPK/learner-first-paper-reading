# Figures, Tables, and Equations

Use the inspected paper version and source anchors from [Source quality](source-quality.md).
Keep literal source content, authors' interpretation, your explanation, and
unknowns distinguishable under the four voices in [Evidence and review](evidence-and-review.md).
In guided mode, preserve the learner's first observation before offering yours.
For a focused explanation, give the requested explanation directly.

## Read the original visual first

Inspect the original figure or table image, including its caption and footnotes,
before describing it whenever source access permits. Render the relevant PDF page
or open the source image; show or link the original visual beside the explanation
when the host permits. Identify the page, figure/table number, version, and panel.
Text extraction can assist reading values but can lose column alignment, labels,
or footnotes; it does not substitute for visual inspection. An Analyst sketch may
teach a concept, but must be labeled illustrative and kept separate from the
original visual and its evidence.

If a visual is unreadable or unavailable, disclose the access limit and what
cannot be checked. Request a clearer source or zoom/render the original when
possible. Explain any inspected caption as caption text only; it cannot establish
unseen axes, curves, values, or layout. Do not invent visual observations. If only
part of a panel is legible, bound observations to that part and mark the rest
Unknown rather than filling it from familiarity with the paper.

Read each figure or table in this order:

1. **Purpose:** Identify the question or comparison the visual is meant to address and its inspected source anchor.
2. **Axes/units/legend:** Read the axes, scales and units, legend and panel labels; for a table, read row/column headers, units, metric direction, emphasis marks, and footnotes. State when an axis, unit, or legend is absent or inapplicable, rather than inferring it.
3. **Literal observations:** Describe legible values or patterns and uncertainty as shown; separate observation from interpretation. Name the compared panels, rows, or conditions. Do not infer exact values from an unreadable plot or causation from ordering.
4. **Author interpretation:** Attribute the authors' explanation to the inspected caption or text. Preserve any difference between what they claim and what is directly visible.
5. **Supported claim:** Connect the observation to an anchored claim, explaining how strongly the comparison or measurement supports it. Separate an Analyst inference from a Paper statement.
6. **Boundary:** State conditions and limits, and what the visual does not establish. Check sample/replicate units, aggregation, uncertainty definitions, axis truncation, omitted conditions, and plausible alternatives when relevant.

For example, two legible table entries can establish a reported ordering under
their stated protocol. Without the unit, uncertainty, and comparison conditions,
that ordering alone cannot establish a reliable population difference. Treat this
as an illustrative reasoning pattern, not a finding about an unspecified paper.

## Unpack an equation as an operation

Use the original equation and its surrounding definitions; preserve its numbering
and assumptions. Explain what it does before treating notation as self-explanatory.

1. **Purpose:** Explain the problem or computational need addressed by the equation before reading its symbols aloud.
2. **Symbols and dimensions:** Define every symbol, index, domain, shape or dimension, and units where applicable. Distinguish learned parameters, observed inputs, intermediate values, random variables, and outputs. Mark undefined notation Unknown.
3. **Operation:** Trace the inputs through the operations or steps to the outputs. Explain summation, transformation, optimization, or probabilistic dependence as applicable; identify any change of shape and check dimensional compatibility.
4. **Hand-checkable example:** Give a small numerical or toy construction with intermediate calculations and the result, labeled Analyst illustration. Reconcile it with the formal equation; the numbers are not the paper's measurements.
5. **Assumptions:** State the conditions or assumptions under which the equation or explanation is valid. Distinguish an identity or definition from an approximation, modeling choice, and empirically tested assertion; name relevant failure cases.
6. **Paper role:** Connect the inspected equation anchor to its role in the method, derivation, objective, or evaluation. State this role Unknown if the necessary passage is uninspected; a generic formula cannot identify its use in an unspecified paper.
7. **Code mapping when relevant:** When implementation or reproduction is requested, map each symbol and operation to a concrete file/function, tensor shape, and configuration at an identified code revision. Record mismatches and missing operations; a plausible mapping is not execution or evidence of metric agreement.

Use the [explanation standard](explanation-standard.md) for the minimal worked
example and prerequisite bridge. If no code is involved, state that implementation
mapping is outside this focused explanation; do not manufacture a code location.
In guided mode, return to the original equation after teaching and ask one small
application question. Correct reasoning permits progress; preserve unresolved
notation or assumptions instead of smoothing them into apparent understanding.
