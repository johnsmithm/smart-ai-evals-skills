#!/usr/bin/env python3
"""Compare saved decisions; positive = fail. Standard library only; no API calls."""
import argparse
import csv
import json
from collections import defaultdict

LABELS = {'pass', 'fail'}
HUMAN = {'human_review', 'human_verified_suggestion'}

def norm(value):
    return (value or '').strip().lower()

def ratio(n, d):
    return n / d if d else None

def summarize(rows, include_fixtures=False):
    counts = dict(tp=0, fp=0, fn=0, tn=0)
    invalid = []
    expert_count = failures = missing_expert = invalid_judge = 0
    for row in rows:
        expert, judge = norm(row.get('expert_status')), norm(row.get('judge_status'))
        provenance = norm(row.get('expert_provenance'))
        allowed = HUMAN | ({'synthetic_fixture'} if include_fixtures else set())
        has_provenance = 'expert_provenance' in row
        expert_ok = expert in LABELS and (not has_provenance or provenance in allowed)
        issues = []
        if not expert_ok:
            missing_expert += 1
            issues.append('missing_or_ineligible_expert_label')
        else:
            expert_count += 1
            failures += expert == 'fail'
        if judge not in LABELS:
            invalid_judge += 1
            issues.append('missing_or_invalid_judge_label')
        if issues:
            invalid.append({'id':row['id'], 'error_type':row['error_type'], 'issues':issues,
                            'expert_status':expert, 'judge_status':judge, 'expert_provenance':provenance})
            continue
        key = 'tp' if expert == judge == 'fail' else 'fn' if expert == 'fail' else 'fp' if judge == 'fail' else 'tn'
        counts[key] += 1
    tp, fp, fn, tn = (counts[k] for k in ('tp','fp','fn','tn'))
    valid = sum(counts.values())
    return {'total':len(rows), 'valid':valid, 'expert_labelled':expert_count,
            'invalid_count':len(invalid), 'missing_or_ineligible_expert':missing_expert,
            'missing_or_invalid_judge':invalid_judge, 'invalid':invalid,
            'confusion':counts, 'agreement':ratio(tp+tn, valid),
            'failure_precision':ratio(tp,tp+fp), 'failure_recall':ratio(tp,tp+fn),
            'specificity':ratio(tn,tn+fp), 'decision_coverage':ratio(valid,expert_count),
            'failure_recall_lower_bound':ratio(tp,failures), 'positive_class':'fail'}

def report(rows, include_fixtures=False):
    groups, categories = defaultdict(list), defaultdict(list)
    keys = set()
    required = {'id','error_type','expert_status','judge_status'}
    for row in rows:
        if not required.issubset(row):
            raise ValueError('Each row requires id,error_type,expert_status,judge_status')
        if not row['id'].strip() or not row['error_type'].strip():
            raise ValueError('Empty id or error_type')
        key = (row['id'].strip(), row['error_type'].strip())
        if key in keys:
            raise ValueError(f'Duplicate case/error pair: {key}')
        keys.add(key)
        groups[key[1]].append(row)
        if 'category' in row:
            categories[row['category'].strip() or 'unclassified'].append(row)
    metadata = {}
    for field in ('judge_version','dataset_version','rubric_version','split'):
        if any(field in r for r in rows):
            values = {r.get(field,'').strip() for r in rows}
            if len(values) != 1 or not next(iter(values), ''):
                raise ValueError(f'Missing or mixed {field}; compare one frozen run/split at a time')
            metadata[field] = next(iter(values))
    return {'overall':summarize(rows, include_fixtures),
            'by_error_type':{k:summarize(v, include_fixtures) for k,v in sorted(groups.items())},
            'by_category':{k:summarize(v, include_fixtures) for k,v in sorted(categories.items())},
            'metadata':metadata, 'fixture_mode':include_fixtures,
            'provenance_unverified_rows':sum('expert_provenance' not in r for r in rows),
            'note':'Micro-averaged case/error decisions, not unique traces. Null = undefined denominator. '+
                   ('Includes teaching fixtures: not measured human alignment.' if include_fixtures else
                    'Supplied human provenance is not independently verified by this script.')}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_path')
    parser.add_argument('--output')
    parser.add_argument('--include-fixtures', action='store_true', help='Allow synthetic_fixture labels for teaching arithmetic; never human alignment.')
    args = parser.parse_args()
    try:
        with open(args.csv_path, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            if not {'id','error_type','expert_status','judge_status'}.issubset(reader.fieldnames or []):
                raise ValueError('CSV requires id,error_type,expert_status,judge_status')
            rows = list(reader)
        result = json.dumps(report(rows,args.include_fixtures), indent=2, allow_nan=False)
    except (ValueError, KeyError) as error:
        parser.error(str(error))
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:
            f.write(result+'\n')
    else:
        print(result)

if __name__ == '__main__':
    main()
