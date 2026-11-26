# Reproduction Levels

Keep exactly these six states distinct. Do not collapse them into a binary
reproduced/not-reproduced label. Report evidence for each state separately;
state numbers organize different claims, rather than certify an automatic ladder.
A later state does not automatically establish earlier states. Running a model
can leave both conceptual understanding and paper-to-code correctness unverified.

## Six states and the evidence they require

| State | Name | Evidence needed to support this state | Boundary of the claim |
| --- | --- | --- | --- |
| 1 | Conceptual understanding | Explain the question, method and key design choice, decisive evidence, and valid scope in the learner's own words; record demonstrated gaps. | Understanding does not establish code correctness or execution. |
| 2 | Paper-to-code mapping | Inspect paper anchors against an identified code revision, file/function, operation, configuration, and tensor shape; record matches and mismatches. | A source mapping does not establish that a run succeeds or results agree. |
| 3 | Forward/shape validation | Inspect the input construction and output shapes, finite-value checks, command/configuration, environment, and run log for a bounded forward test. | This does not establish training, metric consistency, or architecture correctness from shapes alone. |
| 4 | Small-scale training | Inspect a bounded data subset and split, loss trace, parameter update evidence, finite gradients where applicable, saved checkpoint, and run identity. | A trainable small case does not establish benchmark performance or the paper's complete protocol. |
| 5 | Metric consistency with the paper | Inspect the named setting's data/split, preprocessing and selection protocol, metric implementation, agreed tolerance, run provenance, and measured result against the paper's value. | One matching setting or metric does not establish full reproduction. |
| 6 | Full reproduction across reported settings | Inspect coverage of all reported settings in the paper's identified version, required datasets/baselines/ablations, seeds and uncertainty, protocol alignment, results, and deviations. | The conclusion remains bounded to this version, scope and tolerances; it does not prove general validity outside them. |

Advance a claimed state only when its required evidence has been inspected;
leave missing checks explicitly unverified. Record the transition as prior claim
-> new claim, added evidence and its location, source version/run identity,
remaining mismatches, and what still cannot be concluded. A failed or partial
check remains a result to report rather than permission to relabel the next state.
Use not assessed, reported, independently checked, partial, or failed as evidence
statuses within a state; these qualifiers are not additional reproduction states.

For 1 -> 2, add an inspected mapping rather than infer code from understanding.
For 2 -> 3, add actual forward-run evidence. For 3 -> 4, add a bounded training
record, including updates rather than loss output alone. For 4 -> 5, add an
evaluation aligned to one identified paper setting and a justified comparison
tolerance. For 5 -> 6, audit the complete set of reported settings and missing
coverage. A deliberately reduced scope is a partial reproduction within that
scope; do not silently redefine the paper's full set to make state 6 pass.

## Preserve who observed execution

Label user-reported execution as reported; reserve independently verified execution
for an actual inspected run and its logs, with the verified scope named. If the
user supplies logs you inspect, say that the supplied logs were inspected rather
than claiming to have run the code yourself. Record who ran it, where and when,
code revision, configuration, input/data identity, and the exact observed output
as available. Unknown fields remain unknown. Neither a prompt's account nor a
checkpoint file alone demonstrates an independently observed training run.

## Map a smoke test to state 3 only

A forward/shape smoke test supports state 3 only, within its checked inputs and
configuration. If the run is only described by the learner, report it as a
user-reported state-3 check, conditional on that account. Random input producing
finite output with a reported shape supports the reported execution observation;
the shape is not verified as the paper's expected shape without an inspected
specification. States 1 and 2 remain unassessed unless separately checked.

Suggested wording for that situation:

> Based on your reported run, the implementation passed a forward/shape smoke
> test for the stated input and output. This is reported state-3 evidence.
> Paper-to-code alignment, training, paper-metric agreement, and full reproduction
> remain unverified; the run has not been independently inspected here.

For a witnessed run, name the actual command, code/configuration, input/output,
and log inspected. Say “forward/shape validation passed for this case,” bounded
to that case. One matching metric does not establish full reproduction, even if
it is independently measured. At state 5, say which metric and setting agreed,
the tolerance, discrepancies, and which settings remain unchecked.

## Check paper, code, data, and protocol before training

Before training, check the identified paper against code, data, and protocol.
Request the missing paper, relevant implementation, and configuration when these
are unavailable. Mark expectations Unknown until inspected. Compare task and
input/output semantics, equations and tensor operations, dimensions, padding,
normalization, loss, architecture, initialization, and parameter sharing.

Check dataset versions, independent sampling units and grouped splits,
train/validation/test separation, preprocessing fit scope and leakage, metric
aggregation, seeds, hyperparameter selection, optimizer, stopping, and compute.
Tie each mismatch to an inspected anchor and code/configuration location. An
official repository is an implementation source, not proof that every default
matches the paper. Choose the smallest useful verification after this mapping;
do not turn a smoke-test question into authorization for expensive experiments.

Keep proposed checks labeled Analyst, reported paper expectations labeled Paper,
external software semantics labeled Background, and unsupported details Unknown.
Use [Evidence and review](evidence-and-review.md) for comparison fairness and
claim boundaries. These instructions classify evidence; they do not themselves
run training or establish that any paper has been reproduced.
