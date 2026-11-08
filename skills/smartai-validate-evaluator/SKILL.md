---
name: smartai-validate-evaluator
description: "Validate a code evaluator or LLM judge against independent domain-expert labels, diagnose false positives and false negatives, and report class-specific agreement on held-out data."
---

<!-- Modified file. See NOTICE.md and LICENSE at the package root. -->


# Validate the evaluator before trusting its score

## Prepare an honest comparison

- Define the error type and a frozen rubric. Expert labels must refer to the same saved output/trace the judge sees.
- Split by conversation and near-duplicate/template group. Train examples may enter the prompt; dev supports revisions; test stays sealed until the judge is frozen. Choose sizes for coverage and uncertainty, not a universal ratio.
- Include both acceptable and failing cases plus difficult boundaries. Keep AI suggestions and unreviewed synthetic references out of expert ground truth.
- Keep the expert's verdict/notes out of the judge's test input. Give the judge the evidence needed to decide, not the answer key.
- Record dataset, rubric, prompt/model and source versions. A fresh test is needed after tuning on revealed test failures.

## Positive = failure

| Expert | Judge | Meaning |
|---|---|---|
| fail | fail | TP: caught failure |
| pass | fail | FP: false alarm |
| fail | pass | FN: missed failure |
| pass | pass | TN: acceptable case accepted |

Report agreement, failure recall TP/(TP+FN), failure precision TP/(TP+FP), acceptable-case specificity TN/(TN+FP), counts and decision coverage. A missing/invalid judge result is not a pass. Show recall lower bound TP/all expert failures when some are unscored.

Use [eval_metrics.py](../coding-assistant-evals/scripts/eval_metrics.py) on [the sample CSV](../coding-assistant-evals/templates/judge-results-example.csv). It compares saved decisions locally without model calls. See [metrics.md](../coding-assistant-evals/references/metrics.md).

## Improve only what the evidence supports

Inspect FP and FN separately. Cluster disagreement causes: ambiguous rubric, missing context, mismatched source time, poor expert label, or judge failure. Fix references through an explicit reviewed revision; never overwrite a label simply to agree with the model.

Adjust one judge element, rerun dev, inspect changes and regressions, then freeze. Treat “90% agreement” as a possible project target, not a universal release rule: a judge that always passes a 90%-pass dataset reaches 90% while catching zero failures. Include class-specific requirements, critical-error review and sample-size uncertainty.

Do not apply a prevalence correction by default. A balanced judge-validation set estimates judge behavior, not production success rate. Production prevalence needs a representative sample; correction methods add assumptions about stable error rates and uncertainty.

For the bundled synthetic CSV only, add `--include-fixtures`. This explicitly enables teaching arithmetic; it does not measure human alignment.
