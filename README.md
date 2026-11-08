# SmartAItomation Evals Skills

Nine focused skills for Codex and Claude: **analyze → measure → improve**.

## Start without installation

Unzip the pack into your working project. Give that folder and your dataset to your coding assistant, then ask:

> Read skills/coding-assistant-evals/SKILL.md. Inspect my current traces and evals. Choose the relevant workflow, explain what evidence you found, and help me complete it. Use my existing stack and approved model/budget. Start with local analysis.

All nine folders are under `skills/`. Keep them together because focused skills link to shared templates in `coding-assistant-evals`. To install them, use your coding assistant's supported skill installer with these local folders. Review before copying and do not overwrite a same-named skill automatically. This download does not install anything or make API calls.

## What to use

| Skill | Use it for |
|---|---|
| coding-assistant-evals | Choose a workflow and compare improvements |
| smartai-eval-audit | Check whether existing scores are trustworthy |
| smartai-error-discovery | Review traces and build an error taxonomy |
| smartai-review-interface | Build a compact, persistent review viewer |
| smartai-synthetic-data | Generate feature × role × scenario coverage |
| smartai-code-eval | Write deterministic checks |
| smartai-judge-prompt | Create one judge per interpretive error |
| smartai-validate-evaluator | Compare judges with independent expert labels |
| smartai-evaluate-rag | Separate retrieval and answer quality |

## Try the offline example

From this pack's root, with Python 3:

```sh
python3 skills/coding-assistant-evals/scripts/eval_metrics.py skills/coding-assistant-evals/templates/judge-results-example.csv --include-fixtures
python3 skills/coding-assistant-evals/scripts/check_citations.py skills/coding-assistant-evals/templates/citation-example.json
python3 -m unittest discover -s skills/coding-assistant-evals/scripts -p 'test_*.py'
```

The supplied CSV is a fictional calculation fixture, not results from a model run or a human study. Positive class is **fail**. Missing and invalid verdicts remain visible. The scripts use the Python standard library and do not access the network.

## Suggested exercise

Inspect real inputs and outputs → manually review a diverse sample → cluster specific notes → define one failure → write a code check or judge → compare with held-out expert labels → change the agent → check fixes and regressions on the same cases.

No prescribed model, quota increase, paid run or production deployment is implied. Existing project instructions and the user's current request govern execution.
