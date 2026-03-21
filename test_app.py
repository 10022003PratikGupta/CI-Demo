import unittest
from code import sub, add, mul
class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.test_add((4, 5), 9)
        self.test_add((1, -1),0)

    def test_sub(self):
        self.test_sub((4, 5), -1)
        self.test_sub((-1, -1), 0)

    def test_mul(self):
        self.test_mul((4, 5), 20)
        self.test_mul((-1, -1), 1)        
        
if __name__ == 'main':
    unittest.main()
