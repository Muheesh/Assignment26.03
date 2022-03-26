import operations as op
import unittest
class Checkoperation(unittest.TestCase):
    def setUp(self):
        self.a = 153
        self.b = 14
        self.c = 250
    def tearDown(self) :
        self.a = 0
        self.b = 0
        self.c = 0
    def test_armstrong(self):
        x = op.Armstrong(self.a)
        self.assertTrue(x)
    def test_divisible(self):
        y = op.divisible(self.c)
        self.assertTrue(y)
    def test_largest(self):
        z = op.largest(self.a,self.b,self.c)
        self.assertEqual(self.c, z)
    def test_even(self):
        even = op.even(self.b)
        self.assertTrue(even)
if __name__=="__main__":
    unittest.main()
