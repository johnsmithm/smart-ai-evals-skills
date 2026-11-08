import unittest
from eval_metrics import report
from check_citations import check

def row(i,e,j,**extra):
    return dict(id=str(i),error_type='booking',expert_status=e,judge_status=j,**extra)

class MetricsTests(unittest.TestCase):
    def test_all_four_cells(self):
        out=report([row(1,'fail','fail'),row(2,'pass','fail'),row(3,'fail','pass'),row(4,'pass','pass')])['overall']
        self.assertEqual(out['confusion'],dict(tp=1,fp=1,fn=1,tn=1))
        self.assertEqual(out['agreement'],.5)
        self.assertEqual(out['specificity'],.5)
    def test_incomplete_failures_reduce_coverage(self):
        out=report([row(1,'fail','fail'),row(2,'fail',''),row(3,'pass','insufficient_evidence'),row(4,'','pass')])['overall']
        self.assertEqual(out['failure_recall'],1)
        self.assertEqual(out['failure_recall_lower_bound'],.5)
        self.assertAlmostEqual(out['decision_coverage'],1/3)
        self.assertEqual(out['invalid_count'],3)
    def test_provenance_is_not_automatic_truth(self):
        rows=[row(1,'fail','fail',expert_provenance='ai_suggestion'),row(2,'pass','pass',expert_provenance='human_verified_suggestion')]
        self.assertEqual(report(rows)['overall']['valid'],1)
    def test_fixture_requires_explicit_mode(self):
        rows=[row(1,'fail','fail',expert_provenance='synthetic_fixture')]
        self.assertEqual(report(rows)['overall']['valid'],0)
        self.assertEqual(report(rows,True)['overall']['valid'],1)
    def test_no_denominator(self):
        out=report([])['overall']
        self.assertIsNone(out['agreement'])
        self.assertIsNone(out['failure_recall'])
    def test_all_pass_is_not_failure_detection(self):
        out=report([row(i,'pass' if i<9 else 'fail','pass') for i in range(10)])['overall']
        self.assertEqual(out['agreement'],.9)
        self.assertEqual(out['failure_recall'],0)
        self.assertIsNone(out['failure_precision'])
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):report([row(1,'fail','fail'),row(1,'pass','pass')])
    def test_empty_id_rejected(self):
        with self.assertRaises(ValueError):report([row('','fail','fail')])
    def test_missing_required_column(self):
        with self.assertRaises(ValueError):report([{'id':'1'}])
    def test_mixed_versions_and_splits_rejected(self):
        for field in ('judge_version','dataset_version','rubric_version','split'):
            with self.subTest(field=field), self.assertRaises(ValueError):
                report([row(1,'pass','pass',**{field:'a'}),row(2,'fail','fail',**{field:'b'})])
    def test_groups_preserve_denominators(self):
        rows=[row(1,'fail','fail',category='orders'),row(2,'pass','fail',category='search')]
        out=report(rows)
        self.assertEqual(out['by_category']['orders']['failure_precision'],1)
        self.assertEqual(out['by_category']['search']['failure_precision'],0)

class CitationTests(unittest.TestCase):
    def test_unknown_id(self):
        self.assertEqual(check({'retrieved_ids':['a'],'cited_ids':['a','b','b']})['evidence'],['b'])
    def test_known_id(self):
        self.assertEqual(check({'retrieved_ids':['a'],'cited_ids':['a']})['status'],'pass')
    def test_absent_citations_is_outside_this_rule(self):
        self.assertEqual(check({'retrieved_ids':['a'],'cited_ids':[]})['status'],'pass')
    def test_missing_and_malformed_evidence(self):
        for case in ({},{'retrieved_ids':'a','cited_ids':[]},{'retrieved_ids':[None],'cited_ids':[]}):
            self.assertFalse(check(case)['eligible'])
            self.assertIsNone(check(case)['status'])

if __name__ == '__main__':unittest.main()
