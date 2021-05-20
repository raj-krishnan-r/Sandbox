import unittest
from main import pre_tokenisation
class TestGen(unittest.TestCase):
    def test_expression_cleaner(self):
        self.assertEqual(['(','5','+','4','+','56','+','20',')'], pre_tokenisation('(5+4+56+20)'))
        self.assertEqual(['(','10','+','4',')','*','56','/','20',')'], pre_tokenisation('(10+4)*56/20)'))
        self.assertEqual(['5','+','5'], pre_tokenisation('5+5'))
        