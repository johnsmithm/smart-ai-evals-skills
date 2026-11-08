---
name: smartai-review-interface
description: "Build or improve a compact HTML trace and output review interface with filters, evidence panels and persistent Good/Bad notes. Use for human annotation of CSV/JSON AI outputs or agent traces."
---

<!-- Modified file. See LICENSE at the package root. -->


# Make the evidence easy to review

Inspect the schema and several records first. Reuse the app's stack. For a new standalone course exercise, Flask + HTML with SQLite is a useful default; adapt to the user's chosen stack and port.

## Default workflow

- Wide list when no item is selected; optional filters at the side. Search IDs/text and sort by date, review status or relevant metadata. Show counts next to filter options, calculated over the same current filter scope.
- With an item selected: readable conversation/content on the left, **Good / Bad, notes, Save & Next, Skip** on the right. Keep previous notes as a simple number/text list that refreshes with the selected record. Persist drafts before navigation and keep the list's filters and scroll position.
- Show full observable history and all steps. Group each tool call with its result by call ID; show compact parameter/result summaries, expandable JSON, and a step picker for a noted issue within the same review form.
- Expose the listing/order/document/calendar snapshot that existed at the time. Do not silently substitute today's state.
- Match the domain: emails look like emails; CV and job requirements sit beside the generated posting; traces read like a conversation. Display only captured evidence, not invented private reasoning.

Keep advanced metadata out of the default form. Add it only if useful for the assigned workflow. Keep Good/Bad labels separate from per-error decisions; a trace-level Bad does not identify every failure type.

## Durable data

Use stable record IDs, reviewer, timestamp, rubric version, note, optional issue step and provenance. AI suggestions and accepted suggestions have separate states. Preserve original data and annotation history. Server storage is authoritative; browser backup can protect an unsaved draft but is not a shared database.

## Verify the real interaction

Load → filter → open evidence → label → write note → next → back → reload. Check the note and selected record match, persistence works, and list position survives. Also test Skip, unsaved-draft behavior, empty filters, keyboard focus and a phone-width layout. Escape untrusted HTML; do not fetch remote images from trace content automatically. Keep existing authentication and restrict serving to intended files.

Use [viewer-builder.txt](../coding-assistant-evals/templates/viewer-builder.txt) as a concise build prompt. Report what was actually exercised, not just that the HTML exists.
