---
name: smartai-evaluate-rag
description: "Evaluate a RAG system by separating retrieval evidence coverage from generated-answer faithfulness, correctness and completeness. Use for diagnosing chunking, search, filters, reranking or generation failures."
---

<!-- Modified file. See LICENSE at the package root. -->


# Find which part of RAG failed

Read complete cases: message/history, query, retrieved IDs and text, actual context sent to the model, output and versioned reference evidence. A retrieved chunk later dropped by the context budget is not evidence the generator received.

## Define relevance before changing chunks

Pin corpus version and evidence units: document/page/spans or stable fact IDs. Chunk IDs change with chunking. Map new chunks to the same evidence spans and deduplicate overlap rather than comparing incompatible chunk labels. Record all required evidence groups for multi-source answers.

Show correct retrieved, incorrect retrieved and missed evidence separately. No-answer cases have no gold evidence: retrieval recall is undefined for those cases; evaluate abstention and false support separately, not as perfect recall.

## Retrieval measures

- **Recall@k:** relevant evidence units found / required relevant units.
- **Precision:** relevant returned units / returned units. If reporting strict Precision@k, use k and explicitly count missing slots as zero. State which denominator you use.
- **Complete-evidence coverage:** proportion of answerable cases where all required evidence groups reach the model.
- **MRR:** reciprocal rank of the first relevant result, appropriate when one result can answer the question. For graded relevance use a documented NDCG gain convention.

These are evidence-selection metrics. Do not call cosine similarity answer accuracy. Use [retrieval example](../coding-assistant-evals/templates/retrieval-example.json) to see hit/miss/extra accounting.

## Generation measures

Evaluate separately: faithfulness to supplied context; correctness against authoritative sources; completeness for each question; citations; needed clarification/abstention. A fully grounded but outdated answer can be faithful and incorrect. Missing a requested field is a completeness issue, not automatically hallucination.

Use [a calibrated judge](../smartai-judge-prompt/SKILL.md) for interpretive failures and code for exact contracts. Report retrieval/answer/both views and slice counts, not only a single aggregate.

## Paired improvements

Test the diagnosed bottleneck: document parsing (tables/images), structure-aware chunks, size/overlap, embeddings, hybrid search, filters/date permissions, reranking, parent expansion or history-to-query rewriting. Tune on dev, keep source facts constant and compare cost/latency/context budget. Test generator changes with fixed context to isolate them. Strong retrieval does not excuse a bad answer; extra context can also add distractors.

Keep rejected experiments visible. Use [experiment.md](../coding-assistant-evals/templates/experiment.md) and preserve fixes/regressions per category. Agent routing is one option, not a prerequisite for good RAG.
