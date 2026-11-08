# Review contract

Keep the default annotation form small: Good/Bad, notes, Save/Next and Skip. Put extra metadata behind a secondary control only if the assigned workflow benefits from it.

A useful note identifies the specific behavior, evidence and expected alternative. "Bad answer" is not actionable. "The response adds a date absent from the supplied sources; ask for the missing date" can become a test.

Keep expert labels, model suggestions and accepted suggestions separate. Store reviewer/source, timestamp and rubric version. A suggestion is not a manual review merely because it is displayed in the interface.

Keep the full conversation and relevant tool evidence available. Preserve the original input/output; revisions belong in new versions. Avoid leaking reference answers into the product's inputs. A reviewer may mark a case uncertain or skip it rather than inventing ground truth.

Choose a positive class before calculating metrics. Here, fail is positive. Report denominator counts, invalid judge results and missing expert labels. Never silently drop invalid rows or count them as successful passes.
