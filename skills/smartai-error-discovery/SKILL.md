---
name: smartai-error-discovery
description: "Discover application-specific AI failure types from human trace reviews, organize notes into a taxonomy and suggest diverse cases to inspect next. Use before choosing or revising quality evaluators."
---

<!-- Modified file. See NOTICE.md and LICENSE at the package root. -->


# Discover errors before scoring them

Read [the review contract](../coding-assistant-evals/references/review-contract.md). Inventory fields and inspect varied records: user intent, history, observable agent actions, tool inputs/results and source state. A final answer alone may conceal a wrong action.

## Breadth → depth → breadth

1. Start with a mix of random cases, different features/conditions, long traces and risky outcomes. Record why each case was selected. These discovery counts do not estimate production prevalence.
2. Ask the domain expert to mark **Good / Bad / Skip** and write a specific note. Preserve disagreement or uncertainty; do not turn guesses into gold labels.
3. Cluster notes into behaviors that a team can change. Use the [taxonomy prompt](../coding-assistant-evals/templates/taxonomy-prompt.txt). Keep source IDs and exact evidence, inclusion/exclusion boundaries, examples and counterexamples. A trace can have several errors.
4. Inspect similar unreviewed traces for that behavior. AI labels remain suggestions with their own provenance until a human checks them. Show confirmed counts separately from suggested counts.
5. Add random cases and uncovered categories again. Re-review earlier examples when the definition changes. Track new failure types per review batch and remaining coverage gaps.

Stop or narrow the discovery round when successive diverse batches add little new information and important slices are covered. State the batch sizes and remaining uncertainty; this is not proof that all errors were found.

## What an actionable note looks like

Weak: “Wrong booking.”

Useful: “At assistant step 6, create_viewing books L-42 at 16:00 although the renter only asked which slots were free. Ask for confirmation of that listing and slot before creating a booking.”

Do not force every note into a prewritten taxonomy. Split “bad tool use” into evidence-backed issues such as wrong listing reference, invalid slot argument, booking without confirmation, or a success claim after a failed tool result.

## Output

Review records; taxonomy version; confirmed/suggested counts; representative errors and correct counterexamples; coverage table; next samples to inspect. Keep annotation work bounded to the active session. Do not start indefinite monitors or background agents unless requested.

Use [review interface](../smartai-review-interface/SKILL.md) if the evidence is hard to inspect. Next, choose [code](../smartai-code-eval/SKILL.md) or [judge](../smartai-judge-prompt/SKILL.md) per error.
