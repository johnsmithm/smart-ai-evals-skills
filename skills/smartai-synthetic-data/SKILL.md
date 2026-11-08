---
name: smartai-synthetic-data
description: "Generate and verify synthetic AI test inputs from feature, role and scenario coverage plus authoritative facts. Use when starting without traffic, filling dataset gaps or testing a known failure."
---

<!-- Modified file. See NOTICE.md and LICENSE at the package root. -->


# Generate useful cases, not automatic truth

Read the product scope, roles, tool contracts and versioned source facts. Map **feature × role × scenario** into plausible combinations. A role should change the workflow or authority; do not add demographic traits that are irrelevant to the task.

## Build the set

1. Define facts and state first: fictional users, products/listings, orders, dates/timezones, permissions and available slots. Pin a snapshot ID. Mark absent and conflicting facts explicitly.
2. Choose plausible tuples. For example: book_viewing × returning_renter × previous_listing_ambiguous. Include ordinary success, missing data, ambiguous history, no answer, tool failure, stale state and permission boundaries where the product supports them.
3. Generate realistic messages/history from the tuple. Include short and indirect requests, corrections and follow-ups. Avoid placing the desired answer or failure label in the user's input.
4. Write expected behavior and evidence separately from input. Distinguish a correct answer, necessary clarification, abstention and escalation. Validate every claimed fact against the snapshot. Missing evidence remains unverified.
5. Deduplicate near-identical cases. Group variants of a conversation/template into the same train/dev/test split before tuning. Record generator, seed/config if available and synthetic provenance.
6. Run the authorized product pipeline to capture real predictions and tool events. If execution is unavailable, label authored outputs as fixtures, not observed model traces.

## Review and measure coverage

Sample generated inputs for realism, ambiguity and source support. Human approval of a reference needs an actual reviewer record; generation does not provide it. Show counts by feature/role/scenario and unresolved evidence gaps. Preserve representative real examples separately from intentionally difficult synthetic cases.

Use [synthetic-data-prompt.txt](../coding-assistant-evals/templates/synthetic-data-prompt.txt), [case fixture](../coding-assistant-evals/templates/dataset-schema.json) and [data contract](../coding-assistant-evals/references/data-contract.md). Avoid fixed universal sample counts: choose coverage and volume for the decision, review capacity and budget.
