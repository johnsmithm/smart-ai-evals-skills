---
name: smartai-code-eval
description: "Implement a deterministic evaluator for an objective AI-output or tool-trace failure. Use for schema, citation ID, argument, permission or exact-value contracts; use a judge when meaning must be interpreted."
---

<!-- Modified file. See NOTICE.md and LICENSE at the package root. -->


# One objective rule, one check

State the failure and the fields that can prove it. Implement the smallest deterministic check in the existing project language/framework. Return status, concise reason and evidence IDs. Keep malformed input and missing evidence separate from a legitimate pass.

## Examples and boundaries

| Failure | Objective evidence | What this does not prove |
|---|---|---|
| Unknown citation | Cited IDs absent from retrieved IDs | Whether cited text supports the claim |
| Invalid tool params | Args violate versioned tool schema | Whether the chosen tool satisfies intent |
| Forbidden action | Action exceeds an app-enforced permission | Whether natural-language consent is clear |
| Incorrect total | Total differs from authoritative line-item sum | Whether the right order was selected |
| Invalid output JSON | Parsing/schema failure | Whether valid JSON is correct |

See [check_citations.py](../coding-assistant-evals/scripts/check_citations.py). It checks citation membership only; a response with no citations passes that particular rule. A separate required-citation rule would be needed.

Test a real pass, fail, empty/malformed evidence, repeated IDs and an edge case. Inspect saved traces to confirm the check's assumptions. A regex for “yes” is not reliable proof of booking confirmation; either use a verified app confirmation event bound to the selected listing/slot or a calibrated interpretive judge.

Keep evaluation non-mutating. Mock stateful tools for tests; do not create real orders or bookings just to evaluate a trace. Compare proxy checks with domain-expert labels before calling them valid.
