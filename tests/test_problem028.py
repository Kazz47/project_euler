from problems.Problem028 import DiagonalSum
import unittest

class test_problem028(unittest.TestCase):

    def test_find_5(self):
        self.assertEqual(101, DiagonalSum.find(5))

    def test_find_1001(self):
        self.assertEqual(669171001, DiagonalSum.find(1001))

if __name__ == '__main__':
    unittest.main()
