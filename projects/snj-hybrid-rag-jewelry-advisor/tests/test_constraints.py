import sys
from pathlib import Path
import unittest
import pandas as pd
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from retrieval import CatalogRetriever, has_size, has_certificate, format_answer
from domain import parse_query, extract_query_sizes


class CatalogConstraints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df=pd.read_csv(ROOT/'data/sample_catalog.csv');cls.engine=CatalogRetriever(cls.df)
    def ids(self,q):return self.engine.retrieve(q,top_k=20).product_id.tolist()
    def test_loose_ruby_is_not_a_ring(self):
        self.assertEqual(self.ids('ruby rời làm bông tai'),['DEMO-001','DEMO-011'])
    def test_unknown_price_cannot_pass_budget(self):
        self.assertEqual(self.ids('ruby rời dưới 1 triệu'),['DEMO-001'])
    def test_eight_does_not_match_eighteen(self):
        self.assertEqual(self.ids('lắc tay citrine vàng 8ly'),['DEMO-003'])
    def test_decimal_size_is_exact(self):
        self.assertEqual(extract_query_sizes('8ly5'),[8.5])
        self.assertEqual(extract_query_sizes('8.5mm'),[8.5])
        self.assertEqual(self.ids('lắc tay citrine 8ly5'),['DEMO-004'])
    def test_certificate_must_be_present(self):
        self.assertEqual(self.ids('ruby rời kiểm định PNJ'),['DEMO-001'])
        self.assertFalse(has_certificate(pd.Series({'certificate':'không kiểm định'})))
    def test_all_required_attributes(self):
        self.assertEqual(self.ids('vòng cẩm thạch size 52 dưới 2 triệu kiểm định PNJ'),['DEMO-006'])
    def test_zero_match_stays_empty(self):
        self.assertEqual(self.ids('nhẫn sapphire'),[])
        self.assertIn('Chưa có',format_answer(self.engine.retrieve('nhẫn sapphire')))
    def test_gender_filter(self):
        self.assertEqual(self.ids('nhẫn nam garnet'),['DEMO-012'])
    def test_input_index_does_not_misalign(self):
        shuffled=self.df.sample(frac=1,random_state=10);engine=CatalogRetriever(shuffled)
        self.assertEqual(engine.retrieve('lắc tay citrine 8ly').product_id.tolist(),['DEMO-003'])
    def test_duplicate_identifiers_are_rejected(self):
        with self.assertRaises(ValueError):CatalogRetriever(pd.concat([self.df,self.df.iloc[:1]]))
    def test_empty_question(self):
        self.assertTrue(self.engine.retrieve(' ').empty)
    def test_tie_order_and_repeatability(self):
        out=[self.ids('ruby rời') for _ in range(10)]
        self.assertTrue(all(x==out[0] for x in out))


if __name__=='__main__':unittest.main()
