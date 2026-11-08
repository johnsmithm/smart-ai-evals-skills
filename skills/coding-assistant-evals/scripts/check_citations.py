#!/usr/bin/env python3
"""One objective rule: no cited ID may be absent from retrieved IDs. No model calls."""
import argparse
import json

def check(case):
    for field in ('retrieved_ids', 'cited_ids'):
        values = case.get(field)
        if not isinstance(values,list) or any(not isinstance(v,str) or not v.strip() for v in values):
            return {'eligible':False, 'status':None, 'reason':f'Missing or invalid {field}', 'evidence':[]}
    unknown = sorted(set(case['cited_ids']) - set(case['retrieved_ids']))
    return {'eligible':True, 'status':'fail' if unknown else 'pass',
            'reason':'Cited IDs were not retrieved' if unknown else 'No cited ID lies outside the retrieved set',
            'evidence':unknown,
            'scope':'Membership only. Does not check factual support, source correctness or required citation presence.'}

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('json_path')
    a=p.parse_args()
    with open(a.json_path,encoding='utf-8') as f:
        case=json.load(f)
    if not isinstance(case,dict):
        p.error('Input must be an object')
    print(json.dumps(check(case),indent=2))
