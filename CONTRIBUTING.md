# Contributing

Contributions are welcome when they make the learning workflow clearer, more
testable, or more faithful to inspected evidence.

## Before opening a change

1. Describe the learner problem and the smallest proposed change.
2. Identify whether it changes instructions, packaging, examples, or tests.
3. Separate observed behavior from the behavior you expect.
4. Check [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) before adapting an external
   workflow, template, or substantial wording.

## Behavior changes

Every behavior change needs a failure case before an instruction change. Add or
update an observable scenario in `tests/scenarios.md`, record the baseline or
regression, then make the smallest instruction change. Static tests are necessary
but cannot establish agent behavior on their own.

Do not add fabricated paper anchors, quotations, figure observations, execution
records, or learning outcomes. A paper-specific example must identify its source,
version/access conditions, inspected location, and remaining Unknowns. A synthetic
example must say that it is synthetic.

## Local validation

Run both suites from the repository root:

```bash
python3 tests/validate_contract.py
python3 tests/validate_standalone.py
```

For Markdown or SVG changes, also check relative links and inspect the rendered
result. For YAML changes, parse the files locally when a parser is available.

## Attribution and licensing

Keep the four voices—Paper, Background, Analyst, and Unknown—distinct. Preserve
attribution for conceptual influences and include the source project's stated
license status. Do not copy material whose rights are unclear or imply that an
upstream project endorses this one.

## Pull request checklist

- [ ] The change addresses a named learner or maintainer problem.
- [ ] New behavior has an observable scenario or regression test.
- [ ] `validate_contract.py` and `validate_standalone.py` pass.
- [ ] Source claims and examples have evidence boundaries.
- [ ] Attribution and license notes are complete.
- [ ] Documentation says what remains untested.
