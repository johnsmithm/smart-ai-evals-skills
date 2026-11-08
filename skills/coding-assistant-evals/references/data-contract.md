# Keep inputs, references and predictions apart

- Case: stable `id`, `conversation_id`, feature/role/scenario tags, split and near-duplicate group.
- Product input: message, prior messages, approved source IDs and state snapshot available at that moment. No expert verdicts or test answers.
- Reference evidence: expected behavior, authoritative source IDs/spans, snapshot/version and verification state. It may require clarification rather than a final answer.
- Prediction: saved output plus actual trace events; model/prompt/tool versions, cost and latency when measured.
- Event: stable event/step ID, role, type, content, tool call ID/name/arguments and matching tool output. Never pair by adjacent row alone when calls run concurrently.
- Review: trace/error scope, Good/Bad/Skip or pass/fail/uncertain, notes, issue step, reviewer, time, rubric version and provenance.

Use `human_review`, `ai_suggestion`, `human_verified_suggestion`, or `synthetic_fixture` as distinct provenance values. A missing reviewer is not manual review. A whole-trace Bad cannot be reused as a fail label for every error type.

The legacy `dataset-schema.json` filename contains an example record, not a JSON Schema validator. Its synthetic label is a fixture and must not be counted as a human label. For real calibration, join independent expert labels to the exact saved prediction by stable ID/error/rubric version.

Judge input excludes expert status and expert notes on the evaluated case. Reviewed training examples may enter the judge prompt; dev/test labels may not. Keep related conversations and template variants in one split.
