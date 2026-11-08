# Judge metrics: positive = fail

TP = expert fail / judge fail; FP = expert pass / judge fail; FN = expert fail / judge pass; TN = expert pass / judge pass.

Agreement = (TP + TN) / valid paired decisions.
Failure recall (TPR) = TP / (TP + FN).
Failure precision = TP / (TP + FP).
Acceptable-case specificity (TNR) = TN / (TN + FP).

Also report total rows, expert-labelled rows, valid pairs, missing expert labels, missing/invalid judge outputs, and decision coverage = valid pairs / expert-labelled rows. Recall lower bound = TP / all expert-labelled failures, counting unscored failures as not caught. These expose a judge that avoids hard cases. Null means a zero denominator, not zero performance.

`eval_metrics.py` accepts one frozen run: `id,error_type,expert_status,judge_status`; optional `category`, `expert_provenance`, `judge_version`, `dataset_version`, `rubric_version`, `split`. Allowed labels are pass/fail; other values remain visible as incomplete decisions. If provenance is supplied, only human_review and human_verified_suggestion are eligible. If omitted, labels are treated as supplied and the report explicitly says they were not verified.

Reject duplicate case/error pairs, missing IDs/error types, and mixed versions/splits. Run separate files for separate judge versions or dev/test. Group results by error type and optional category. Overall metrics are micro averages over case/error decisions, not unique conversations; one trace can appear in several error checks.

The teaching CSV has 8 decisions: TP=2, FP=1, FN=1, TN=1; 5 valid pairs, 7 expert-labelled, 1 missing expert label and 2 incomplete judge outputs. Agreement=60%, recall=66.7%, precision=66.7%, specificity=50%, coverage=71.4%, recall lower bound=50%. This tiny fixture demonstrates arithmetic only.

For real reports, add uncertainty intervals with a documented method and enough representative held-out examples in each important slice. Do not treat a balanced calibration set or targeted challenge set as production prevalence. A single score cannot establish that a judge is safe for every task.

For the bundled synthetic CSV only, add `--include-fixtures`. This explicitly enables teaching arithmetic; it does not measure human alignment.
