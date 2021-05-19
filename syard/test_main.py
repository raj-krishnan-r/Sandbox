import unittest
from main import pre_tokenisation
class TestGen(unittest.TestCase):
    def test_expression_cleaner(self):
        self.assertEqual(pre_tokenisation('(5+4+56+20)'),['(','5','+','4','+','56','+','20',')'])
        