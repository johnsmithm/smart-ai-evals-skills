---
name: smartai-eval-audit
description: "Audit an existing LLM evaluation system for misleading metrics, weak labels, leakage, unvalidated judges and missing failure coverage. Use when assessing whether existing eval results support a decision."
---

<!-- Modified file. See NOTICE.md and LICENSE at the package root. -->


# Audit the evidence behind the score

Inspect the actual dataset, traces, rubric, prompts, labels, run metadata and dashboard. Use available local files or authorized connectors. Missing artifacts are evidence gaps, not proof that the team never did the work.

## Six checks

1. **Failure discovery.** Can each important evaluator be traced to observed product failures or an explicit product requirement? Generic helpfulness averages can supplement, but cannot replace actionable checks.
2. **Test coverage.** Count features, user roles, conditions and critical slices. Separate representative samples from targeted stress tests. A set with 90 easy shipping cases and 10 failed technical cases can show 90% accuracy while technical accuracy is 0%.
3. **Labels.** Who reviewed the cases? Are source evidence and rubric versions retained? Do uncertain, unreviewed or AI-suggested labels accidentally count as expert truth?
4. **Checks.** Prefer code for exact contracts and a focused judge for interpretation. Verify pass/fail boundaries, evidence requirements and handling of missing information. If a numeric rubric is intentional, inspect its anchors and threshold calibration rather than banning numeric scores.
5. **Calibration.** Compare judges with independently reviewed held-out cases. Look for few-shot/test leakage, near-duplicate conversations across splits, only one class, and hidden invalid outputs. Report failure precision/recall and acceptable-case specificity alongside agreement.
6. **Experiments.** Are comparisons paired on the same cases and source state? Are versions, cost, latency, fixes and regressions visible? Did failure distribution change after a release?

## Deliver a useful finding

For each finding write: **observed artifact → consequence → smallest useful fix → verification**. Mark it confirmed, suspected or unknown. Prioritize by impact and occurrence, not by checklist order. Link example case IDs and inspect disagreements before blaming the model.

If nothing exists, start from accessible traces or a small, explicitly synthetic set and a review interface. Existing deterministic safety/permission checks can still be useful before a full taxonomy exists.

Next routes: [error discovery](../smartai-error-discovery/SKILL.md), [judge validation](../smartai-validate-evaluator/SKILL.md), [RAG](../smartai-evaluate-rag/SKILL.md).
