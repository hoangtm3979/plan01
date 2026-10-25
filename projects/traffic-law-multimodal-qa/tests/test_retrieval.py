from pathlib import Path
import sys,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from retrieval_baseline import ranking_metrics,article_key,TextRetriever,sample_data

class RetrievalEvaluation(unittest.TestCase):
    def test_recall_uses_all_relevant_articles(self):
        r=ranking_metrics(['x','a','a','b'],{'a','b','c'})
        self.assertEqual(r['precision_at_1'],0)
        self.assertEqual(r['recall_at_5'],2/3)
        self.assertEqual(r['mrr_at_10'],.5)
    def test_compound_law_identifier(self):
        self.assertNotEqual(article_key('LAW1','1'),article_key('LAW2','1'))
    def test_empty_or_unknown_query_does_not_force_a_hit(self):
        e=TextRetriever(sample_data()[0]);self.assertEqual(e.retrieve('zzzzzz'),[])
        self.assertEqual(ranking_metrics([],{'a'})['mrr_at_10'],0)
    def test_synthetic_known_retrieval(self):
        e=TextRetriever(sample_data()[0])
        self.assertEqual(e.retrieve('màu xanh hình vuông')[0],'DEMO::2')
    def test_missing_relevance_is_rejected(self):
        with self.assertRaises(ValueError):ranking_metrics(['a'],set())

if __name__=='__main__':unittest.main()
